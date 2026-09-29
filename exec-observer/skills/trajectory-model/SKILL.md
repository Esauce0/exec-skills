---
name: trajectory-model
description: "Maintain a longitudinal model of the user's organizational position: scope, sponsorship, visibility, reputation, and readiness ledgers, plus a trajectory hypothesis with leading indicators and drift signals. Distinguishes doing excellent work from accumulating evidence that one can operate at the next level. Use when running weekly and monthly reviews or retrospectives, after significant events, when the user asks 'am I on track?', 'is my career moving?', or 'what's changed?', and when scanning for emerging opportunities."
---

# Trajectory Model

## Purpose

Excellent work is necessary and not sufficient. Trajectory is what increasingly senior people *allocate* to you because of your work: scope, ambiguity, people, money, strategic importance, organizational risk, and rooms. This skill keeps an honest, evidence-based model of that allocation over time, so the user can see whether they're moving, how fast, and why.

It answers three questions no single conversation can:

1. Is my position actually changing, or does it just feel busy?
2. Which of my work is current-level excellence, and which is evidence of next-level capability that the people who decide have seen and attributed to me?
3. What pattern is forming that I would miss week to week?

## Use when

- `/review-my-week`, `/review-my-month`, `/career-retrospective`.
- After a significant event (reorg, promotion cycle, new manager, big win or failure).
- "Am I on track?" and "Why does it feel like nothing is changing?"

## Don't use when

- A single interaction needs interpreting; use `attribution-analysis` and `evidence-discipline`, then record the event.

## Core distinctions

**Performance vs trajectory.** Performance is how well the current job is done, and trajectory is the rate at which senior people extend more scope and trust. The two often diverge: the "reliable pair of hands" keeps getting more *work* while their *scope* stays flat.

**Three grades of work evidence.** Classify each notable piece of work:

| Grade | Meaning | Trajectory effect |
|---|---|---|
| A. Current-level excellence | Did the current job very well | Keeps trust; rarely moves trajectory |
| B. Next-level capability demonstrated | Did something the next level requires (per `next-level-readiness`) | Builds readiness; invisible unless seen |
| C. Next-level capability, seen and attributed by deciders | B, plus someone with power over the next step saw it and knows it was the user's | Moves trajectory |

Most people have plenty of A, some B, and far less C than they think. A shortfall between A and B points to capability or opportunity, while the step from B to C depends on visibility and attribution and needs a different fix (see `attribution-analysis`).

**Allocation is ground truth.** Praise, recognition, and warm 1:1s are weak evidence next to what people with power *give* (and withhold), and the model weights them accordingly (`evidence-discipline`).

**Formal vs informal scope.** Informal scope is real, but it evaporates in a reorg or a manager change. Scope that appears in an org announcement, a planning doc, or an OKR is durable.

## The ledgers

Files live in the Career Brain `models/` (semantics here; locations in `brain-protocol`).

| Ledger | Tracks | Strongest evidence |
|---|---|---|
| **Scope** | Ownership across nine dimensions: areas, people, money, decision rights, ambiguity, strategic importance, organizational risk carried, cross-functional reach, external exposure | Formal grants; undefined problems handed over |
| **Sponsorship** | Each person with power: contact, ally, mentor, connector, opportunity-giver, sponsor | Dated acts of capital-spending: names put forward, defense in calibration, rooms opened |
| **Visibility** | Per audience: exposure, attribution, and which attribute they associate with the user | Deciders directly seeing next-level work with the user's name on it |
| **Reputation** | The calibration sentence each key person would most likely say, as hypotheses | Consistent behavior toward the user across months; direct specific feedback |
| **Readiness** | Next-level gap by dimension (defined in `next-level-readiness`) | Grade B and C evidence entries |
| **Trajectory** | Synthesis: direction, rate, leading indicators, drift, top moves | All of the above |

## Leading indicators

Titles and compensation lag by quarters; the indicators below move first. Details and how to read them: `references/indicators.md`.

- Ambiguous problems handed to the user undefined.
- Asked for a view on matters outside their scope.
- New rooms (or being dropped from rooms).
- The user's framing reused in others' documents and decisions.
- Named as owner by people other than the manager.
- Advocacy by people above the manager.
- Informal scope becoming formal.

## Drift signals

These patterns tend to precede a stall. Each needs evidence, and each has an innocent explanation to rule out.

- Praise without allocation for two or more quarters.
- Visibility concentrated on one person (usually the manager).
- Scope growing in load (more of the same) but not in ambiguity or strategic importance.
- The same "not yet" feedback, with the same content, across cycles.
- The user's area drifting away from the company's top priorities.
- A sponsor losing standing, leaving, or getting a new boss.
- Being consulted less, or later, on things that used to include the user.
- Grade A evidence dominating the log month after month.

## Standards

Everything this skill produces follows the three exec-core standards. If exec-core isn't loaded, apply them as stated here:
- **Evidence:** separate what happened from inference; label any claim about another person's view or motive as a hypothesis with confidence and a falsifier; never state it as fact.
- **Posture:** when the user's behavior is part of the problem, fix the behavior before the wording.
- **Prose:** answer first, recommendation over options, owners and dates, no filler.

## Doctrine basis

The ledgers, the A/B/C grades, the leading indicators, and the drift list are this system's synthesis. The sources behind them:

- Performance is the entry ticket, and after that the perceptions of those above you are the operative variable [Pfeffer].
- What separates a sponsor from a mentor is that a sponsor spends capital on you rather than only advising [Hewlett].
- A leadership reputation is built socially: others see the leadership work, confirm it, and it sticks [Ibarra].
- Readiness shows up across several quarters of work [Hughes Johnson], and it is different from performance at the current level [Charan].
- Stepping up is nonlinear, so judge it over quarters [Ibarra].

## Evidence to gather

- `evidence/LOG.md`: types and signals, the ratio of `allocation` to `recognition`, the share of `activity-only`.
- Every file in `models/` with its `Last reviewed` date; weekly and monthly reviews.
- `self/level-model.md § Revealed ladder` for base rates.
- Product Brain strategy: is the user's area moving toward the company's priorities or away from them?

## Reasoning procedures

### A. Incremental update (after `/capture` or a debrief)
1. For each new evidence entry, identify which ledgers it touches.
2. Update factual rows (scope change log, sponsorship "most recent act," visibility rows) per the Brain's autonomy setting.
3. If an entry bears on a hypothesis, note it; propose a confidence change only if the confidence rules are met.

### B. Weekly pass (inside `/review-my-week`)
1. Grade the week's notable work A, B, or C.
2. Count `activity-only` entries against entries with trajectory signals.
3. Note leading-indicator movement and any drift signal appearing for the first time.
4. Check active commitments.

### C. Monthly synthesis (inside `/review-my-month`)
1. For each ledger, state the trend over the month and the quarter.
2. Apply `evidence-discipline` confidence rules to every active hypothesis. Weaken, strengthen, or retire with reasons.
3. Run the drift checklist.
4. Rewrite H-T1 (the trajectory hypothesis) if the evidence moved it. State direction plainly. State a rate ("at the current rate, the next level is roughly N months away, because...") only when H-T1 is at medium confidence or higher. Otherwise write "rate: unknown" and name the evidence gap that prevents an estimate.
5. Pick at most three moves for next month. Each must address a named diagnosis.

### D. Opportunity scan (monthly, and on reorgs)
Scan evidence and Product Brains for signals of legitimate opportunity: a problem executives raised repeatedly that nobody owns, a departure, a new company priority, a cross-team seam that keeps failing, a bet the company is starting. Add candidates to `opportunities.md` as `spotted`. Evaluation belongs to `scope-expansion`.

### E. Retrospective (inside `/career-retrospective`)
Compare hypotheses at the start of the period with what happened. Which were right, which wrong, and what does the pattern of errors say about the user's blind spots?

## Diagnostic questions

- What has been allocated to you in the last two quarters, and what was withheld?
- Which undefined problems came to you?
- Which rooms did you enter, and which did you leave?
- Who above your manager has seen your work and knows it was yours?
- What share of this month's work was grade A?
- What would a stall look like here, and is any of it already showing?

## Failure modes

- Treating activity volume as trajectory.
- Updating the model from mood rather than evidence.
- A model built only on the user's account of wins (check the LOG's ratio of unflattering entries).
- Ignoring base rates: if Directors at this company typically take three years from Senior PM, eighteen months is fast. Use `self/level-model.md` revealed-ladder data when available.
- Mistaking one sponsor's enthusiasm for organizational consensus.
- Overreacting to a single bad meeting.

## Output

In reviews, the trajectory section is short:

```
Trajectory: <direction and rate, one sentence, with confidence>.
Moved this period: <ledger changes, only the real ones>.
Grade mix: A <n>, B <n>, C <n>. <One line on what that means.>
Leading indicators: <what moved>.
Drift: <new or persisting signals, or "none">.
Moves: <max 3, each tied to a diagnosis>.
```

## Tensions in the doctrine

- **Performance-first vs perception-first.** Campbell, Slootman, and McCord say results earn trust and trajectory follows. Pfeffer's research says performance is weakly related to advancement and perceptions of superiors matter more. The model resolves this empirically for this user: grade A/B/C separates the two, and the allocation evidence shows which is binding.
- **Act first vs reflect first.** Ibarra argues leaders change by doing new things and reflecting after (outsight); Hughes Johnson emphasizes knowing yourself first. The model supports both: it records experiments as evidence and reflects monthly.

## Interactions

- `attribution-analysis` explains *why* a ledger isn't moving.
- `next-level-readiness` defines the readiness dimensions and level expectations.
- `sponsorship` and `executive-trust` define the levels used in the sponsorship ledger and trust signals.
- `scope-expansion` evaluates opportunities this skill spots.

## References

- `references/indicators.md`: leading indicators, lagging indicators, drift signals, and how to tell each from its innocent explanation.
