#!/usr/bin/env python3
"""
Build step for exec-skills.

1. Reads the source citations inside every skill (bracketed tags such as [Grove] or
   [Cagan; Doshi], and "(after Charan)" in references) and adds any cited skill that is
   missing from the cited dossier's `feeds-skills` frontmatter, so the source layer and
   the skills stay traceable in both directions.
2. Syncs every sources/<slug>/doctrine.md into
   exec-core/skills/doctrine-library/references/<slug>.md (the runtime copy).
3. Generates exec-core/skills/doctrine-library/references/_index.md.
4. Generates docs/doctrine-map.md: for each skill, the sources it cites, plus sources
   whose dossiers map to it without being cited there.
5. Regenerates the Skills and Commands lists in each plugin README from frontmatter.

Run from the repo root:  python scripts/build.py
Check mode (no writes, exit 1 if anything is out of date):  python scripts/build.py --check
"""

import json
import os
import re
import sys
from pathlib import Path


def _root() -> Path:
    root = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
    # Windows: long scratch paths can exceed MAX_PATH once plugin subpaths are appended.
    if os.name == "nt" and len(root) > 150 and not root.startswith("\\\\?\\"):
        root = "\\\\?\\" + root
    return Path(root)


ROOT = _root()
SOURCES = ROOT / "sources"
LIB_REFS = ROOT / "exec-core" / "skills" / "doctrine-library" / "references"
DOCTRINE_MAP = ROOT / "docs" / "doctrine-map.md"
GENERATED_NOTE = "<!-- Generated from sources/{slug}/doctrine.md by scripts/build.py. Edit the source, not this copy. -->\n"
PLANNED = ["organizational-design", "talent", "role-transition", "portfolio-strategy"]

# Name fragments that appear in skill citations, mapped to source slugs.
CITATION_NAMES = [
    (r"\bCampbell\b", "bill-campbell"),
    (r"\bCagan\b", "marty-cagan"),
    (r"\bDoshi\b", "shreyas-doshi"),
    (r"\bGrove\b", "andy-grove"),
    (r"\bHughes Johnson\b", "claire-hughes-johnson"),
    (r"\bCharan\b", "ram-charan"),
    (r"\bMcCord\b", "patty-mccord"),
    (r"\bHorowitz\b", "ben-horowitz"),
    (r"\bScott\b", "kim-scott"),
    (r"\bSlootman\b", "frank-slootman"),
    (r"\bPfeffer\b", "jeffrey-pfeffer"),
    (r"\bHewlett\b", "sylvia-ann-hewlett"),
    (r"\bWatkins\b", "michael-watkins"),
    (r"\bIbarra\b", "herminia-ibarra"),
    (r"\bMinto\b", "barbara-minto"),
    (r"\bGabarro\b|\bKotter\b", "gabarro-kotter"),
    (r"\bGoldsmith\b", "marshall-goldsmith"),
    (r"\bBezos\b|\bAmazon\b", "amazon-bezos"),
    (r"\bDuke\b", "annie-duke"),
    (r"\bRumelt\b", "richard-rumelt"),
    (r"\bLencioni\b", "patrick-lencioni"),
    (r"\bLarson\b", "will-larson"),
    (r"\bRabois\b", "keith-rabois"),
    (r"\bHill\b", "linda-hill"),
    (r"\bMaister\b", "david-maister"),
    (r"\bNg\b", "andrew-ng"),
    (r"\ba16z\b|\bCasado\b|\bBornstein\b", "ai-economics-a16z"),
    (r"\bHusain\b|\bShankar\b|\bYan\b|evals practitioners", "ai-evals-practitioners"),
    (r"\bMollick\b|\bDell'Acqua\b|\bNANDA\b|\bMETR\b|ai-product-operators", "ai-product-operators"),
]
BRACKET = re.compile(r"\[([^\[\]\n]{2,160})\](?!\()")
AFTER = re.compile(r"\(after ([^)\n]{2,120})\)")


def parse_frontmatter(text: str) -> dict:
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    fm = {}
    for line in text[3:end].strip().splitlines():
        m = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line.strip())
        if not m:
            continue
        key, val = m.group(1), m.group(2).strip()
        if val.startswith("[") and val.endswith("]"):
            fm[key] = [v.strip().strip("'\"") for v in val[1:-1].split(",") if v.strip()]
        else:
            fm[key] = val.strip("'\"")
    return fm


def split_frontmatter(text: str):
    if not text.startswith("---"):
        return "", text
    end = text.find("\n---", 3)
    if end == -1:
        return "", text
    close = end + len("\n---")
    if text[close:close + 1] == "\n":
        close += 1
    return text[:close], text[close:]


def plugin_order() -> list:
    mk = ROOT / ".claude-plugin" / "marketplace.json"
    try:
        listed = [p["name"] for p in json.loads(mk.read_text(encoding="utf-8"))["plugins"]]
    except (OSError, ValueError, KeyError):
        listed = []
    rest = sorted(p.name for p in ROOT.glob("exec-*") if p.is_dir() and p.name not in listed)
    return [ROOT / n for n in listed + rest if (ROOT / n).is_dir()]


def skills() -> list:
    """(plugin_dir, skill_dir) in marketplace order."""
    out = []
    for plugin in plugin_order():
        sd = plugin / "skills"
        if sd.is_dir():
            out += [(plugin, d) for d in sorted(sd.iterdir()) if (d / "SKILL.md").is_file()]
    return out


def cited_sources(skill_dir: Path) -> set:
    files = [skill_dir / "SKILL.md"]
    refs = skill_dir / "references"
    if refs.is_dir() and skill_dir.name != "doctrine-library":
        files += sorted(refs.glob("*.md"))
    found = set()
    for f in files:
        text = re.sub(r"```.*?```", "", f.read_text(encoding="utf-8"), flags=re.S)
        spans = BRACKET.findall(text) + AFTER.findall(text)
        for span in spans:
            for pattern, slug in CITATION_NAMES:
                if re.search(pattern, span):
                    found.add(slug)
    return found


def load_sources() -> list:
    out = []
    for d in sorted(SOURCES.iterdir()):
        f = d / "doctrine.md"
        if f.is_file():
            text = f.read_text(encoding="utf-8")
            out.append({"slug": d.name, "path": f, "text": text, "fm": parse_frontmatter(text)})
    return out


def with_feeds(text: str, feeds: list) -> str:
    return re.sub(r"^feeds-skills:\s*\[.*?\]", "feeds-skills: [" + ", ".join(feeds) + "]", text, count=1, flags=re.M)


def description_lead(desc: str) -> str:
    lead = re.split(r"\.?\s+Use when", desc, maxsplit=1)[0].strip()
    return lead if lead.endswith((".", "?")) else lead + "."


def readme_lists(plugin: Path) -> str:
    lines = []
    sk = [d for p, d in skills() if p == plugin]
    lines += [f"## Skills ({len(sk)})", ""]
    for d in sk:
        fm = parse_frontmatter((d / "SKILL.md").read_text(encoding="utf-8"))
        lines.append(f"- **{d.name}**: {description_lead(fm.get('description', ''))}")
    cmds = sorted((plugin / "commands").glob("*.md"))
    lines += ["", f"## Commands ({len(cmds)})", ""]
    for c in cmds:
        fm = parse_frontmatter(c.read_text(encoding="utf-8"))
        lines.append(f"- `/{c.stem}`: {fm.get('description', '')}")
    return "\n".join(lines) + "\n\n"


def expected_outputs() -> dict:
    outputs = {}
    sources = load_sources()
    by_slug = {s["slug"]: s for s in sources}
    skill_list = skills()
    skill_names = [d.name for _, d in skill_list]
    citations = {d.name: cited_sources(d) for _, d in skill_list}

    # 1. sync feeds-skills with actual citations
    for s in sources:
        feeds = s["fm"].get("feeds-skills", [])
        feeds = list(feeds) if isinstance(feeds, list) else []
        added = [sk for sk in skill_names if s["slug"] in citations[sk] and sk not in feeds]
        if added:
            feeds = feeds + added
            s["text"] = with_feeds(s["text"], feeds)
            s["fm"]["feeds-skills"] = feeds
            outputs[s["path"]] = s["text"]

    # 2. runtime copies
    for s in sources:
        fm_block, body = split_frontmatter(s["text"])
        outputs[LIB_REFS / f"{s['slug']}.md"] = fm_block + GENERATED_NOTE.format(slug=s["slug"]) + body

    # 3. library index
    lines = ["# Doctrine library index", "", "<!-- Generated by scripts/build.py. -->", "",
             "| Source | File | What it is uniquely good for | Feeds skills |", "|---|---|---|---|"]
    for s in sources:
        fm = s["fm"]
        feeds = ", ".join(fm.get("feeds-skills", [])) if isinstance(fm.get("feeds-skills"), list) else ""
        lines.append(f"| {fm.get('source', s['slug'])} | [{s['slug']}.md]({s['slug']}.md) | {fm.get('role-in-system', '')} | {feeds} |")
    outputs[LIB_REFS / "_index.md"] = "\n".join(lines) + "\n"

    # 4. doctrine map
    m = ["# Doctrine map", "",
         "<!-- Generated by scripts/build.py from the citations inside each skill and the feeds-skills frontmatter of each dossier. -->", "",
         "**Cited** means the skill's SKILL.md or references cite the source by name. **Mapped only** means the source's dossier lists the skill but the skill doesn't cite it yet: candidates for the next revision, or over-broad mapping in the dossier. Planned skills are marked with an asterisk.", "",
         "## By skill", "", "| Skill | Cited | Mapped only |", "|---|---|---|"]
    feeds_by_source = {s["slug"]: set(s["fm"].get("feeds-skills", []) or []) for s in sources}
    for sk in skill_names + [p for p in PLANNED if p not in skill_names]:
        cited = sorted(citations.get(sk, set()))
        mapped = sorted(slug for slug, f in feeds_by_source.items() if sk in f and slug not in cited)
        label = sk + ("" if sk in skill_names else "*")
        m.append(f"| {label} | {', '.join(cited) or '—'} | {', '.join(mapped) or '—'} |")
    m += ["", "## By source", "", "| Source | Cited by | Mapped only |", "|---|---|---|"]
    for s in sources:
        cited_by = [sk for sk in skill_names if s["slug"] in citations[sk]]
        mapped_only = [sk for sk in (s["fm"].get("feeds-skills") or []) if sk not in cited_by]
        m.append(f"| {s['fm'].get('source', s['slug'])} | {', '.join(cited_by) or '—'} | {', '.join(mapped_only) or '—'} |")
    unresolved = sorted(set().union(*citations.values()) - set(by_slug))
    if unresolved:
        m += ["", "Citations with no dossier: " + ", ".join(unresolved)]
    outputs[DOCTRINE_MAP] = "\n".join(m) + "\n"

    # 5. plugin README lists
    for plugin in plugin_order():
        readme = plugin / "README.md"
        if not readme.is_file():
            continue
        text = readme.read_text(encoding="utf-8")
        start = text.find("## Skills (")
        end = text.find("## Install")
        if start == -1 or end == -1:
            continue
        outputs[readme] = text[:start] + readme_lists(plugin) + text[end:]
    return outputs


def rel(p: Path) -> str:
    return str(p.relative_to(ROOT)).replace("\\", "/")


def main() -> int:
    check = "--check" in sys.argv
    outputs = expected_outputs()
    stale = []
    for path, content in outputs.items():
        current = path.read_text(encoding="utf-8") if path.is_file() else None
        if current != content:
            stale.append(path)
            if not check:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(content, encoding="utf-8", newline="\n")
    valid = {p.name for p in outputs if p.parent == LIB_REFS}
    if LIB_REFS.is_dir():
        for f in LIB_REFS.glob("*.md"):
            if f.name not in valid:
                stale.append(f)
                if not check:
                    f.unlink()
    names = [rel(p) for p in stale]
    if check:
        if names:
            print("Out of date (run python scripts/build.py):")
            for n in names:
                print("  " + n)
            return 1
        print("Build outputs up to date.")
        return 0
    print(f"Updated {len(names)} file(s).")
    for n in names:
        print("  " + n)
    return 0


if __name__ == "__main__":
    sys.exit(main())
