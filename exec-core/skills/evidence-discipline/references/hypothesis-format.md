# Hypothesis format and provenance tags

Used in every Career Brain `models/` file and in `people/<slug>.md` hypothesis sections. Adapted from the pm-brain hypothesis schema: the evidence rows, provenance tags, and count-the-tags rule work the same way; the status values differ because career hypotheses are about perceptions and trajectories. The translation table below maps pm-brain tags when evidence is carried over from a Product Brain.

## Schema

```markdown
### H-<AREA><n>: <one-sentence claim, stated so it can be wrong>
- **Subject:** <person slug, or "self", or "org">
- **Confidence:** low | medium | high
- **Evidence for:**
  - <claim>  `<provenance-tag>`
- **Evidence against:**
  - <claim>  `<provenance-tag>`
- **Strongest alternative explanation:** <the best competing account of the same evidence>
- **Would weaken if:** <specific observable, ideally within 4-8 weeks>
- **Would strengthen if:** <specific observable>
- **Cheapest test:** <an action that produces discriminating evidence without much cost>
- **Status:** active | supported | weakened | retired
- **Opened:** YYYY-MM-DD
- **Last reviewed:** YYYY-MM-DD
- **Notes:** <gaps, caveats; rows here need no tag>
```

Area codes: `R` reputation, `S` sponsorship, `V` visibility, `C` scope, `D` readiness (development), `T` trajectory. Hypotheses about one person's priorities or incentives live in that person's file as `H-P-<slug>-<n>`, so IDs never collide across people.

## Rules

1. Count the rows under Evidence for and Evidence against, then count the provenance tags; the two numbers must match. Commentary goes under Notes.
2. Confidence follows the rules in the evidence-discipline skill. A hypothesis with only one Evidence-for row is low, whatever it feels like.
3. A hypothesis about a person's perception must have a Strongest alternative explanation. "None" is not accepted.
4. "Would weaken if" must name something observable, such as "If she routes the Q1 planning question to my manager instead of me." "If things change" fails that test.
5. Retire hypotheses rather than deleting them. The history of wrong hypotheses is useful evidence about the user's blind spots.
6. Status changes happen in reviews (`/review-my-month`, `/career-retrospective`) or when a single piece of evidence is strong enough to move confidence by the rules. Record the reason in Notes.

## Provenance tags

Every evidence row ends with exactly one tag.

| Tag | Use for |
|---|---|
| `[evidence/YYYY/MM/<file>.md](../evidence/YYYY/MM/<file>.md)` | A captured evidence entry in the Career Brain. Preferred. |
| `[<brain-slug>:<path>](<absolute path>)` | A file in a Product Brain (decision, meeting ingestion, stakeholder file). The link target is the absolute path, built from the brain's path in `brains.md`, so it resolves from anywhere. |
| `(stakeholder-verbal, <name>, YYYY-MM-DD)` | Something the person said directly to the user, not yet captured as an entry. Same tag as pm-brain. |
| `(reported-by, <reporter>, YYYY-MM-DD)` | A third party's account of what the person said or did. |
| `(document, <title>, YYYY-MM-DD)` | Review, calibration packet, org announcement, OKR doc. |
| `(self-report, YYYY-MM-DD)` | The user's own assessment. Weak evidence about others. |
| `(industry-knowledge)` | General knowledge about how organizations or markets work. Never evidence about a specific person. Same tag as pm-brain. |
| `(chat, no artifact)` | Stated in conversation with no record. Should be captured as an entry soon. Same tag as pm-brain. |

## Translating pm-brain tags

When `/capture`, `/analyze-stakeholder`, or a review carries an evidence row over from a Product Brain file:

| pm-brain tag | Career Brain tag |
|---|---|
| `[ingestion/<path>](../ingestion/<path>)` | `[<brain-slug>:ingestion/<path>](<absolute path>)` |
| `[source/<path>](../source/<path>)` | `[<brain-slug>:source/<path>](<absolute path>)` |
| `(stakeholder-verbal, <name>, <date>)` | unchanged |
| `(intuition, PM, <date>)` | `(self-report, <date>)` |
| `(industry-knowledge)` | unchanged |
| `(chat, no artifact)` | unchanged |

Status values: pm-brain uses `promoted | demoted | killed` for product hypotheses; career hypotheses use `supported | weakened | retired`. Don't copy a status across; re-rate under the Career Brain's confidence rules.

## Example

```markdown
### H-R2: Priya sees me as the owner of AI quality, not just the PM on the eval project.
- **Subject:** priya-raman
- **Confidence:** low
- **Evidence for:**
  - Asked me, not Dan, to present eval results at staff  [evidence/2026/09/2026-09-12-priya-staff-ask.md](../evidence/2026/09/2026-09-12-priya-staff-ask.md)
- **Evidence against:**
  - Q3 planning doc lists Dan as DRI for "model quality"  (document, Q3 planning v4, 2026-07-30)
- **Strongest alternative explanation:** She wanted the person closest to the data in the room, and the ask says nothing about ownership.
- **Would weaken if:** The next quality question at staff is routed to Dan, or she asks Dan to "take it from here."
- **Would strengthen if:** She asks me for a recommendation (not data) on a quality tradeoff, or names me in the Q4 plan.
- **Cheapest test:** Close the staff presentation with a recommendation and a proposed quality bar for Q4, then watch who she asks to own it.
- **Status:** active
- **Opened:** 2026-09-12
- **Last reviewed:** 2026-09-12
- **Notes:** Dan's reaction matters. If he reads this as a land grab it costs more than it gains; see managing-up.
```
