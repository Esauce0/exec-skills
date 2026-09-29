#!/usr/bin/env python3
"""
Validator for exec-skills. Structure follows the approach of phuryn/pm-skills'
validate_plugins.py, extended for this repo's cross-plugin standards and source layer.

Checks
- marketplace.json lists every exec-* plugin directory and nothing else
- plugin.json: required fields, name matches directory, version synced with marketplace
- skills: frontmatter name matches directory, description has trigger phrasing,
  required body sections present, referenced references/ files exist
- commands: frontmatter description + argument-hint; every **plugin:skill** reference resolves
- sources: required frontmatter; feeds-skills slugs are built or planned skills
- relative markdown links inside plugins and docs resolve (code blocks and templates skipped)
- doctrine-library copies are in sync with sources/ (scripts/build.py --check)
- marketplace description counts match the number of skills and commands on disk
- frontmatter parses as YAML (when PyYAML is installed)
- section contract per skill class (domain, standards, infrastructure)
- vocabulary: posture tags, readiness dimensions, sponsorship ladder, no wikilinks
- style warning: em-dash density in skills and commands

Run from the repo root:  python scripts/validate.py
"""

import json
import os
import re
import subprocess
import sys
from pathlib import Path

def _root():
    root = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
    # Windows: long scratch paths can exceed MAX_PATH once plugin subpaths are appended.
    if os.name == "nt" and len(root) > 150 and not root.startswith("\\\\?\\"):
        root = "\\\\?\\" + root
    return Path(root)


ROOT = _root()
PLANNED_SKILLS = {"organizational-design", "talent", "role-transition", "portfolio-strategy"}
INFRA_SKILLS = {"brain-protocol", "doctrine-library"}
STANDARD_SKILLS = {"evidence-discipline", "executive-prose", "executive-posture"}
BASE_SECTIONS = ["## Purpose", "## Use when", "## Don't use when", "## Interactions", "## References"]
STANDARD_SECTIONS = BASE_SECTIONS + ["## Doctrine basis", "## Reasoning procedure", "## Failure modes", "## Output", "## Tensions in the doctrine"]
DOMAIN_SECTIONS = BASE_SECTIONS + ["## Standards", "## Evidence to gather", "## Reasoning procedure", "## Diagnostic questions",
                                   "## Failure modes", "## Output", "## Tensions in the doctrine"]
POSTURE_TAGS = {"coordinator", "project-manager", "expert", "product-manager", "product-leader", "org-leader", "executive"}
READINESS_TAGS = {"scope-ambiguity", "strategic-contribution", "leverage-through-others", "judgment", "enterprise-acumen",
                  "talent", "peer-leadership", "executive-communication", "operating-rhythm", "ownership"}
LADDER = {"contact", "ally", "mentor", "connector", "opportunity-giver", "sponsor"}
EM_DASH_WARN_PER_1000_WORDS = 4.0

errors, warnings = [], []


def err(msg):
    errors.append(msg)


def warn(msg):
    warnings.append(msg)


def frontmatter(text):
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    out = {}
    for line in text[3:end].strip().splitlines():
        m = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line.strip())
        if m:
            val = m.group(2).strip()
            if val.startswith("[") and val.endswith("]"):
                out[m.group(1)] = [v.strip().strip("'\"") for v in val[1:-1].split(",") if v.strip()]
            else:
                out[m.group(1)] = val.strip("'\"")
    return out


def yaml_check(path, text):
    """Parse frontmatter with a real YAML parser when available; plain scalars with ': ' break loaders."""
    try:
        import yaml
    except ImportError:
        return
    end = text.find("\n---", 3)
    if not text.startswith("---") or end == -1:
        return
    try:
        data = yaml.safe_load(text[3:end])
        if not isinstance(data, dict):
            err(f"{rel(path)}: frontmatter is not a YAML mapping")
    except yaml.YAMLError as e:
        err(f"{rel(path)}: frontmatter is not valid YAML ({str(e).splitlines()[0]})")


def resolve(base, target):
    """Join and normalize '..' segments; extended-length (\\\\?\\) paths skip normalization in the OS."""
    prefix = "\\\\?\\"
    raw = str(base / target)
    if raw.startswith(prefix):
        return Path(prefix + os.path.normpath(raw[len(prefix):]))
    return Path(os.path.normpath(raw))


def strip_code(text):
    return re.sub(r"```.*?```", "", text, flags=re.S)


def rel(p):
    return str(p.relative_to(ROOT)).replace("\\", "/")


def main():
    mk_path = ROOT / ".claude-plugin" / "marketplace.json"
    mk = json.loads(mk_path.read_text(encoding="utf-8"))
    version = mk.get("version")
    listed = {p["name"] for p in mk.get("plugins", [])}
    on_disk = {d.name for d in ROOT.glob("exec-*") if d.is_dir()}
    for missing in sorted(on_disk - listed):
        err(f"marketplace.json does not list plugin directory {missing}")
    for extra in sorted(listed - on_disk):
        err(f"marketplace.json lists {extra} but the directory does not exist")

    all_skills = {}
    command_count = 0

    for plugin in sorted(on_disk):
        pdir = ROOT / plugin
        pj_path = pdir / ".claude-plugin" / "plugin.json"
        if not pj_path.is_file():
            err(f"{plugin}: missing .claude-plugin/plugin.json")
            continue
        pj = json.loads(pj_path.read_text(encoding="utf-8"))
        for field in ["name", "version", "description", "author", "keywords"]:
            if not pj.get(field):
                err(f"{plugin}: plugin.json missing {field}")
        if pj.get("name") != plugin:
            err(f"{plugin}: plugin.json name '{pj.get('name')}' does not match directory")
        if pj.get("version") != version:
            err(f"{plugin}: version {pj.get('version')} != marketplace {version}")
        if not (pdir / "README.md").is_file():
            err(f"{plugin}: missing README.md")

        for sdir in sorted((pdir / "skills").glob("*")):
            if not sdir.is_dir():
                continue
            smd = sdir / "SKILL.md"
            if not smd.is_file():
                err(f"{rel(sdir)}: missing SKILL.md")
                continue
            text = smd.read_text(encoding="utf-8")
            yaml_check(smd, text)
            fm = frontmatter(text)
            if fm is None:
                err(f"{rel(smd)}: missing frontmatter")
                continue
            if fm.get("name") != sdir.name:
                err(f"{rel(smd)}: name '{fm.get('name')}' does not match directory")
            desc = fm.get("description", "")
            if len(desc) < 80:
                warn(f"{rel(smd)}: description is short ({len(desc)} chars)")
            if "use when" not in desc.lower():
                err(f"{rel(smd)}: description lacks 'Use when' trigger phrasing")
            if sdir.name in INFRA_SKILLS:
                required = BASE_SECTIONS
            elif sdir.name in STANDARD_SKILLS:
                required = STANDARD_SECTIONS
            else:
                required = DOMAIN_SECTIONS
            for sec in required:
                if not re.search(r"^" + re.escape(sec), text, re.M):
                    err(f"{rel(smd)}: missing section '{sec}'")
            if sdir.name not in INFRA_SKILLS and not re.search(r"^## (Core doctrine|Doctrine basis)", text, re.M):
                err(f"{rel(smd)}: missing '## Core doctrine' or '## Doctrine basis'")
            for ref in set(re.findall(r"`(references/[A-Za-z0-9_./-]+\.md)`", text)):
                if not (sdir / ref).is_file():
                    err(f"{rel(smd)}: referenced file {ref} does not exist")
            all_skills[sdir.name] = plugin

        for cmd in sorted((pdir / "commands").glob("*.md")):
            command_count += 1
            ctext = cmd.read_text(encoding="utf-8")
            yaml_check(cmd, ctext)
            fm = frontmatter(ctext)
            if fm is None:
                err(f"{rel(cmd)}: missing frontmatter")
                continue
            for field in ["description", "argument-hint"]:
                if not fm.get(field):
                    err(f"{rel(cmd)}: missing {field}")

    # command -> skill references of the form **plugin:skill**
    for cmd in sorted(ROOT.glob("exec-*/commands/*.md")):
        for plugin, skill in re.findall(r"\*\*(exec-[a-z-]+):([a-z0-9-]+)\*\*", cmd.read_text(encoding="utf-8")):
            if all_skills.get(skill) != plugin:
                err(f"{rel(cmd)}: references {plugin}:{skill}, which does not exist")

    # sources
    for d in sorted((ROOT / "sources").glob("*")):
        f = d / "doctrine.md"
        if not f.is_file():
            continue
        stext = f.read_text(encoding="utf-8")
        yaml_check(f, stext)
        fm = frontmatter(stext) or {}
        for field in ["source", "slug", "role-in-system", "feeds-skills"]:
            if not fm.get(field):
                err(f"{rel(f)}: missing frontmatter {field}")
        if fm.get("slug") and fm["slug"] != d.name:
            err(f"{rel(f)}: slug '{fm['slug']}' does not match directory")
        for sk in fm.get("feeds-skills", []) if isinstance(fm.get("feeds-skills"), list) else []:
            if sk not in all_skills and sk not in PLANNED_SKILLS:
                warn(f"{rel(f)}: feeds unknown skill '{sk}'")

    # relative links
    md_files = list(ROOT.glob("exec-*/**/*.md")) + list((ROOT / "docs").glob("*.md")) + [ROOT / "README.md"]
    for f in md_files:
        if not f.is_file() or "doctrine-library" in f.parts and f.parent.name == "references" and f.name != "_index.md":
            continue
        body = strip_code(f.read_text(encoding="utf-8"))
        for target in re.findall(r"\]\(([^)\s]+)\)", body):
            if target.startswith(("http://", "https://", "mailto:", "#")) or "{{" in target or "<" in target:
                continue
            path = target.split("#")[0]
            if not path:
                continue
            if not resolve(f.parent, path).exists():
                err(f"{rel(f)}: broken link -> {target}")

    # build sync
    r = subprocess.run([sys.executable, str(ROOT / "scripts" / "build.py"), "--check"], capture_output=True, text=True)
    if r.returncode != 0:
        err("doctrine-library or doctrine map out of date:\n" + r.stdout.strip())

    # counts in marketplace description
    desc = mk.get("description", "")
    m_sk = re.search(r"(\d+) skills", desc)
    m_cmd = re.search(r"(\d+) workflows", desc)
    if m_sk and int(m_sk.group(1)) != len(all_skills):
        err(f"marketplace.json says {m_sk.group(1)} skills; found {len(all_skills)}")
    if m_cmd and int(m_cmd.group(1)) != command_count:
        err(f"marketplace.json says {m_cmd.group(1)} workflows; found {command_count}")

    # vocabulary consistency across plugins and the scaffold
    vocab_files = [f for f in ROOT.glob("exec-*/**/*") if f.is_file() and f.suffix in (".md", ".tmpl")
                   and not ("doctrine-library" in f.parts and f.parent.name == "references")]
    for f in vocab_files:
        text = f.read_text(encoding="utf-8")
        for tag in re.findall(r"`posture:([a-z-]+)`", text):
            if tag not in POSTURE_TAGS:
                err(f"{rel(f)}: unknown posture tag 'posture:{tag}'")
        for tag in re.findall(r"`readiness:([a-z-]+)[+-]?`", text):
            if tag not in READINESS_TAGS and tag != "":
                err(f"{rel(f)}: unknown readiness dimension 'readiness:{tag}'")
        if "[[" in strip_code(text):
            err(f"{rel(f)}: wikilink syntax found; use markdown links")
        for line in text.splitlines():
            m = re.search(r"Sponsorship level:\s*(.+)", line)
            if m and "|" in m.group(1):
                levels = {x.strip().strip("`").split()[0] for x in m.group(1).split("|") if x.strip()}
                if not levels <= LADDER:
                    err(f"{rel(f)}: sponsorship levels {sorted(levels - LADDER)} are not on the ladder")

    # style: em dashes inside output templates (models copy them)
    for f in list(ROOT.glob("exec-*/skills/*/SKILL.md")) + list(ROOT.glob("exec-*/commands/*.md")):
        for block in re.findall(r"```.*?```", f.read_text(encoding="utf-8"), flags=re.S):
            if "—" in block:
                warn(f"{rel(f)}: em dash inside a code block or output template")

    # style: em-dash density
    for f in list(ROOT.glob("exec-*/skills/*/SKILL.md")) + list(ROOT.glob("exec-*/commands/*.md")):
        text = strip_code(f.read_text(encoding="utf-8"))
        words = max(len(text.split()), 1)
        dashes = text.count("—")
        if dashes / words * 1000 > EM_DASH_WARN_PER_1000_WORDS:
            warn(f"{rel(f)}: {dashes} em dashes in {words} words (house style: use sparingly)")

    print(f"Plugins: {len(on_disk)}  Skills: {len(all_skills)}  Commands: {command_count}")
    for w in warnings:
        print("WARN  " + w)
    for e in errors:
        print("ERROR " + e)
    print("OK" if not errors else f"{len(errors)} error(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
