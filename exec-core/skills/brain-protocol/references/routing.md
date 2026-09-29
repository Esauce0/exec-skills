# Routing: what to load for each job

Paths are relative to the Career Brain root unless prefixed `product:`. "Relevant" means: only for the people or products actually involved.

## By command

| Command | Career Brain | Product Brains |
|---|---|---|
| /coach-me | self/current-role, models/trajectory, relevant people/, last weekly review, evidence LOG (last 30 days, scan) | strategy + decisions + stakeholders for products involved |
| /capture | people/INDEX, relevant people/, evidence/_SCHEMA, models/scope (for scope-change entries) | stakeholder files for people named (read only, to cross-check facts) |
| /review-my-week | evidence LOG (7 days), those entries, commitments, meetings/ (7 days), models/trajectory, last weekly review | decisions and ingestion/meetings from the last 7 days, all active products |
| /review-my-month | evidence LOG (30-35 days), weekly reviews of the month, all models/, commitments, opportunities, self/level-model | decisions from the month; strategy for products whose priority shifted |
| /career-retrospective | self/career-history, all models/ with their review history, monthly reviews and retros in the period, self/level-model, self/ambitions | strategy snapshots if available |
| /position-for-promotion | self/level-model, self/ambitions, models/readiness, models/reputation, models/sponsorship, models/visibility, evidence entries tagged `readiness:*` | decisions the user drove, metrics for products they own |
| /expand-my-scope | self/current-role, models/scope, opportunities, models/readiness, people/ for boss and skip | strategy, roadmap, org/team, recent decisions for adjacent products |
| /analyze-stakeholder | people/<slug>, evidence entries naming them (grep LOG), meetings/ with them, models/reputation (their hypotheses) | stakeholders/<slug> in every Product Brain, ingestion/meetings where they appear, decisions they made |
| /prepare-exec-meeting | people/ for each attendee, meetings/ prior with them, models/reputation + sponsorship rows for them, self/current-role, commitments | strategy, relevant decisions and metrics, stakeholders/ for attendees, rules/writing |
| /debrief-exec-meeting | the prep file in meetings/, people/ for attendees, models/ rows for them | none required |
| /review-exec-update | self/current-role (decision rights), people/ for the recipient | strategy, decisions, metrics for the product the update covers, rules/writing |
| /prepare-board-update | self/current-role, people/ for the CEO/exec sponsor of the slot | strategy, metrics, decisions (quarter), market knowledge |
| /audit-my-time | self/current-role, self/level-model, models/readiness, commitments | knowledge/org/rituals for recurring meetings |
| /frame-decision | self/current-role (decision rights), people/ for the decider and affected peers | decisions/ (precedents), strategy, metrics, hypotheses |
| /review-product-altitude | self/level-model, models/readiness | strategy, roadmap, features/, metrics |

## By situation type (for /coach-me and skill-triggered coaching)

| Situation | Load |
|---|---|
| A tense interaction with an executive | that person's people/ file, their reputation hypotheses, the last 3 evidence entries naming them, the relevant product's stakeholder file |
| "Am I ready?" / promotion timing | self/level-model, models/readiness, models/sponsorship, models/visibility |
| A new opportunity or reorg | self/current-role, models/scope, opportunities, people/ for boss and skip, strategy of affected products |
| Conflict with a peer | both people/ files, relevant decisions in the Product Brain, models/reputation rows for the boss |
| Feedback received | the giver's people/ file, prior feedback entries (grep LOG for `feedback`), models/reputation |
| A draft to a senior reader | self/current-role, recipient's people/ file, product rules/writing |

## Scanning the LOG

`evidence/LOG.md` has one line per entry: date, type, people, one-line summary, signal tags, path. Grep it by person slug, type, or signal tag (`scope+`, `trust-`, `sponsorship?`) before opening entries. Open at most the 5-8 most relevant entries for any single question.
