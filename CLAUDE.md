# CLAUDE.md

Guidance for agents working on this repository (the exec-skills marketplace itself, not a Career Brain).

## What this is

A Claude Code plugin marketplace: 7 plugins, 20 skills, 16 commands, and a source layer of 29 researched doctrine dossiers. Architecture and rationale: [docs/architecture.md](docs/architecture.md).

## Design rules

- **Skills are nouns** (reasoning capabilities, loaded by description). **Commands are verbs** (workflows that chain skills). This matches pm-skills.
- **Organize by job, never by thinker.** Thinkers live in `sources/`. No skill or command is named after a person, and no skill imitates a person.
- **One capability, one skill; one piece of state, one Brain file.** Before adding a skill, check whether it's a mode of an existing one.
- **Every skill has:** frontmatter `name` (matches the directory) and `description` (with "Use when" trigger phrasing); sections Purpose, Use when, Don't use when, Core doctrine (with source tags), Reasoning procedure, Failure modes, Output, Tensions in the doctrine, Interactions, References. Keep SKILL.md operational and move depth into `references/`.
- **Every command has:** frontmatter `description` and `argument-hint`; a Load step via `exec-core:brain-protocol`; diagnosis before prescription; output in executive prose; a write-back step; one next-step offer.
- **Cross-plugin skill references** use the form `**plugin:skill**` in commands (validated). This deviates from pm-skills on purpose: the marketplace is installed as a whole and exec-core is required.
- **Doctrine must change behavior.** A doctrine entry earns its place only if it changes the coach's diagnosis, questions, or recommendation.
- **Preserve disagreement.** Every skill has a Tensions section. Don't average sources into consensus.
- **Evidence standards apply to the repo too.** Don't invent quotations. Use only verified quotes, under 15 words, in the dossiers' "Verified quotations" sections, and attribute paraphrases to the source and work.
- **The repo models its own prose standard.** Write plainly and directly, answer first, with sparing bold and em dashes and no corporate filler or AI tells. The validator warns on em-dash density.

## Sources

- Canonical dossiers live in `sources/<slug>/doctrine.md`, with frontmatter `source`, `slug`, `role-in-system`, `feeds-skills`, `last-researched`.
- Never edit `exec-core/skills/doctrine-library/references/*`; they're generated.
- After changing sources, run `python scripts/build.py`.

## After any change

```bash
python scripts/build.py
python scripts/validate.py
```

If skills or commands were added or removed, update the counts in `.claude-plugin/marketplace.json` (the validator checks them), the root README, and `docs/architecture.md`. Add a CHANGELOG entry. Keep all manifest versions in sync.

## The Career Brain scaffold

`exec-core/skills/brain-protocol/scaffold/career-brain/` is copied by `/setup-career-brain`. Schema changes there are breaking for existing Brains: bump the schema version in `CAREER-BRAIN.md` and describe the migration in the CHANGELOG.
