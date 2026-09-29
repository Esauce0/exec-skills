# Product Brain adapter

Product Brains are read-only. This file says where to find things in them.

## pm-brain scaffold (type `pm-brain`)

Recognize it by an `INDEX.md` titled "PM Brain" and folders `knowledge/`, `stakeholders/`, `decisions/`, `hypotheses/`, `ingestion/`, `source/`.

| Need | Path in the Product Brain | Notes |
|---|---|---|
| Routing | `INDEX.md` | Always start here |
| Strategy, north star, priorities, tensions | `knowledge/strategy.md` | `§ Tensions` is gold for organizational-politics |
| Roadmap | `knowledge/product/roadmap.md` | Now / Next |
| Metrics (current values) | `knowledge/product/metrics.md` | Definitions live in strategy.md |
| Feature status | `knowledge/product/features/<slug>.md` | |
| Decisions | `decisions/INDEX.md`, `decisions/YYYY-MM-DD-<slug>.md` | Evidence rows carry provenance tags; `What would reverse this` shows judgment |
| Hypotheses | `hypotheses/<feature-slug>.md` | |
| Stakeholders (product view) | `stakeholders/<slug>.md` | What they care about, concerns, comm style, touchpoint log |
| Meetings | `ingestion/meetings/` | Synthesized records; verbatim in `source/` |
| Verbatim sources | `source/` | Read when exact wording matters (quotes, commitments) |
| Team, rituals, tools | `knowledge/org/team.md`, `rituals.md`, `tools.md` | Rituals feed /audit-my-time |
| Market | `knowledge/market/` | |
| Writing rules for this product's audience | `rules/writing.md` | Respect when drafting |
| Maintenance history | `maintenance/log/` | Rarely needed |

### Joining the product view and the career view of a person

The same executive may have a `stakeholders/<slug>.md` in one or more Product Brains and a `people/<slug>.md` in the Career Brain.

- Product view: what they want from the product, their concerns, their communication style as observed in product work.
- Career view: how they relate to the user's trajectory, trust signals, sponsorship, reputation hypotheses.

Read both. Record the link in the Career Brain person file under `Product Brain profiles`. When the two views conflict (for example, communication style), treat the more recent and more specific evidence as current and surface the conflict.

Use the same slug in both when possible. If slugs differ, record the mapping in `brains.md`.

When carrying an evidence row from a Product Brain into the Career Brain, translate its provenance tag with the table in exec-core `evidence-discipline/references/hypothesis-format.md`.

## Any other Product Brain (type `other`)

On first use:

1. Read its README, CLAUDE.md, or index file.
2. Map each row of the table above to the nearest equivalent. Leave a row empty if there is none.
3. Record the mapping in the Career Brain's `brains.md` under that brain's entry, so discovery happens once.
4. If a folder of loose documents has no structure, treat it as `source/`: read selectively by filename and date.

## Folders of multiple Product Brains

If the user keeps several Product Brains under one parent folder, register each separately in `brains.md`. Don't treat the parent as a brain.

## What never to do

- Write to a Product Brain, including "just updating the stakeholder's last-touched date." Suggest the user run that brain's own ingestion instead.
- Copy career hypotheses into Product Brain notes.
- Trust a Product Brain's stakeholder characterization over direct evidence in the Career Brain without saying so.
