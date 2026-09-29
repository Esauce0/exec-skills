# Write rules

## Canonical homes (Career Brain)

Each concept has one home. Everything else links to it.

| Concept | Canonical home |
|---|---|
| Who I am, stated ambitions, constraints | `self/profile.md`, `self/ambitions.md` |
| Current role, mandate, decision rights, reporting line | `self/current-role.md` |
| What each level expects at this company, and what actually gets people promoted | `self/level-model.md` |
| Strengths and development areas (as evidence-backed claims) | `self/capabilities.md` |
| Prior roles and what changed | `self/career-history.md` |
| A person's relationship to my trajectory | `people/<slug>.md` |
| Something that happened | `evidence/YYYY/MM/<date>-<slug>.md` + one line in `evidence/LOG.md` |
| What I own and how it changed | `models/scope.md` |
| Who advocates for me, with evidence | `models/sponsorship.md` |
| Who sees my work, and what they see | `models/visibility.md` |
| How key people likely perceive me | `models/reputation.md` |
| Next-level gap by dimension | `models/readiness.md` |
| The overall trajectory hypothesis and drift | `models/trajectory.md` |
| Scope and visibility opportunities | `opportunities.md` |
| Development commitments and experiments | `commitments.md` |
| A specific meeting (prep and debrief) | `meetings/YYYY-MM-DD-<slug>.md` |
| Periodic reviews | `reviews/weekly/YYYY-Www.md`, `reviews/monthly/YYYY-MM.md`, `reviews/retros/YYYY-MM-DD-<period>.md` |
| Unprocessed raw material | `inbox/` |

## File naming

- Lowercase, hyphenated slugs. People: `firstname-lastname`. Meetings: `YYYY-MM-DD-<person-or-forum>-<topic>`.
- ISO week for weekly reviews (`2026-W40`).

## Autonomy defaults

Overridden by `CAREER-BRAIN.md § Autonomy`.

| Write | Default |
|---|---|
| New evidence entry and LOG line | Act and tell |
| People touchpoint line, last-touched date | Act and tell |
| New person file (skeleton, facts only) | Act and tell |
| Meeting prep or debrief file | Act and tell |
| Review files | Act and tell |
| Factual ledger rows in `models/` (scope change log, sponsorship "most recent act", visibility audience rows) | Act and tell |
| Ledger snapshots and ratings (scope snapshot, sponsorship level, readiness rating) | Propose and wait |
| New hypothesis in `models/` | Propose and wait |
| Confidence or status change on an existing hypothesis | Propose and wait (except inside a review the user started, where the review proposes all changes together) |
| Anything in `self/` | Propose and wait |
| New commitment | Propose and wait. If three are already active, propose which one to close or replace. |
| Deleting anything | Never without explicit instruction; prefer `Status: retired` |

## Write-back summary

End every command that wrote to the Brain with:

```
Saved: <files created or changed, as relative paths>
Proposed (needs your OK): <model or self changes>
Open: <gaps worth filling, as TODOs>
```

Keep it to two to four lines, with no narration.

## Evidence entry quality bar

- The "What happened" section contains only observations. Interpretation goes under "Why it might matter."
- Quotes only if verbatim from notes, a transcript, or a message. Otherwise paraphrase and mark it as paraphrase.
- Name everyone involved by slug.
- Tag signals from the controlled vocabulary in `evidence/_SCHEMA.md`. Don't tag what the entry doesn't support.
- One event per entry. A week's worth of notes becomes several entries.
