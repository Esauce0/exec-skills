# Evidence entry schema

Path: `evidence/YYYY/MM/YYYY-MM-DD-<slug>.md`. One event per file. Append-only: corrections go in a dated note at the bottom, and the original text stays.

Every entry also gets one line in `evidence/LOG.md`.

```markdown
---
date: YYYY-MM-DD
type: meeting | feedback | recognition | win | setback | decision | scope-change | escalation | communication | observation | allocation | reorg
people: [<slug>, <slug>]
products: [<product-brain-slug>]
source: direct | reported | documentary | self-assessment
provenance: <path to verbatim notes or transcript, a Product Brain file, or "(chat, no artifact)">
signals: [<controlled tags>]
---

## What happened
<!-- Observations only. Who said or did what, when, in what setting. Verbatim quotes only if from notes, a transcript, or a message; otherwise mark as paraphrase. -->

## Why it might matter
<!-- Inference, labeled. Which hypotheses in models/ this bears on, and in which direction. -->

## My part
<!-- What the owner did, said, decided, or didn't. Posture shown, if relevant. -->

## Follow-ups
<!-- Open loops created, with owner and date. -->

## Corrections
<!-- Dated notes if anything above turns out to be wrong. -->
```

## Signal vocabulary

Tag only what the entry supports. Use `?` for plausible-but-unclear (e.g., `sponsorship?`).

| Tag | Meaning |
|---|---|
| `scope+` / `scope-` | Ownership, people, budget, decision rights, ambiguity, or strategic importance gained or lost |
| `trust+` / `trust-` | A tier of trust extended or withdrawn (information, judgment, decisions, people, ambiguity, representation) |
| `visibility+` / `visibility-` | Work seen by, and attributed to the owner by, someone above the manager, or the opposite |
| `sponsorship+` / `sponsorship-` | An act of advocacy (or withdrawal) by someone with power |
| `relationship:<slug>+` / `-` | Change in a specific working relationship |
| `posture:<level>` | Posture the owner showed: `coordinator`, `project-manager`, `expert`, `product-manager`, `product-leader`, `org-leader`, `executive` (exec-core executive-posture) |
| `readiness:<dimension>+` / `-` | Evidence for or against a next-level dimension. Dimensions: `scope-ambiguity`, `strategic-contribution`, `leverage-through-others`, `judgment`, `enterprise-acumen`, `talent`, `peer-leadership`, `executive-communication`, `operating-rhythm`, `ownership` (as in models/readiness.md) |
| `feedback:solicited` / `feedback:unsolicited` | Feedback and whether the owner asked for it |
| `activity-only` | Real work with no trajectory signal. Recorded so reviews can see the ratio. |

## Type guide

- **allocation**: someone gave or withheld scope, a room, a problem, headcount, budget, a nomination. The strongest evidence type.
- **feedback**: a specific evaluative statement about the owner or their work.
- **recognition**: public or written credit. Weaker than allocation.
- **communication**: a notable message the owner sent (exec update, escalation, memo), for later posture review.
- **observation**: anything the owner noticed that bears on a model (a reorg rumor stays out unless sourced; note the source quality).
