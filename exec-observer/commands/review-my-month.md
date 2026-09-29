---
description: "Monthly pattern review: look across weeks for patterns, update hypotheses about reputation, scope, sponsorship, visibility, readiness, and trajectory, and choose next month's moves"
argument-hint: "<optional: YYYY-MM, defaults to the month just ended>"
---

# /review-my-month

Input: $ARGUMENTS

This review leaves individual events to the weekly reviews and looks only for patterns. It is also the routine place where hypotheses in the Career Brain get updated.

## Invocation

```
/review-my-month
/review-my-month 2026-09
```

## Workflow

### Step 1: Load

Apply **exec-core:brain-protocol**:
- The month's weekly reviews and all evidence entries in the month (scan LOG, open the ones with trajectory signals).
- All of `models/`, `commitments.md`, `opportunities.md`, `self/level-model.md`.
- Product Brains: decisions from the month, and any change in `knowledge/strategy.md` for active products.
- Last month's review.

Note any model file whose `Last reviewed` is stale.

### Step 2: Patterns, not events

Apply **exec-observer:trajectory-model** (monthly synthesis). Look for:
- **Recurring posture** across the month's communications and meetings (from weekly reviews). A single leak is worth a note; it takes about three to call it a pattern.
- **Grade mix trend:** A/B/C counts month over month.
- **Person patterns:** how each key person's behavior toward the user moved, starting with allocation.
- **Signal clusters:** grep LOG for `scope+`, `scope-`, `trust-`, `sponsorship?`, `visibility+`. What cluster is forming?
- **What the user keeps not doing:** missed openings that repeat.

Run the two most relevant checks from **exec-core:evidence-discipline** `references/bias-checks.md` against the month's narrative.

### Step 3: Update hypotheses

For every active hypothesis in `models/`:
- New evidence for or against this month (with provenance).
- Apply the confidence rules. Strengthen, weaken, hold, or retire, with the reason in Notes.
- Update `Last reviewed`.

Open new hypotheses only where a pattern across several events supports one, and start them at low confidence.

Propose all changes together as one reviewable list before writing (unless the Brain's autonomy says act-and-tell for models).

### Step 4: Ledgers

- **Scope:** snapshot changes and trend.
- **Sponsorship:** level changes, concentration risk.
- **Visibility:** deciders with new direct exposure; attribution.
- **Reputation:** any calibration sentence that should change.
- **Readiness:** apply **exec-trajectory:next-level-readiness** to update ratings from the month's B and C evidence.

### Step 5: Diagnose the binding constraint

Apply **exec-observer:attribution-analysis** to the question: what is most limiting the trajectory right now? Name one binding cause, with confidence and a runner-up.

### Step 6: Trajectory and drift

Rewrite H-T1 in `models/trajectory.md` if the evidence moved it. Run the drift checklist. Add any spotted opportunities to `opportunities.md` (evaluation belongs to `/expand-my-scope`).

### Step 7: Commitments and moves

Close or renew commitments with evidence. Choose at most three moves for next month, each tied to the binding constraint or a named hypothesis test.

### Step 8: Write

Save `reviews/monthly/YYYY-MM.md`. Apply approved model changes. Add a row to `models/trajectory.md § Review history`.

## Output

Treat this template as a checklist of content: keep the order, drop empty items, and write it as prose where prose reads better (exec-core executive-prose).

```
<Month>: <one-line verdict on trajectory: direction, rate, confidence>

Patterns this month:
- <pattern, with the evidence count and span>

Binding constraint: <cause class> (hypothesis, <confidence>). <Why, in two sentences.>

Hypothesis changes (proposed):
- H-R2: low → medium. <reason>
- H-S1: retired. <reason>
- New H-V3 (low): <claim>

Ledgers: <scope / sponsorship / visibility / readiness: only real changes>
Drift: <signals, or none>
Grade mix: A <n> / B <n> / C <n> (last month: A / B / C)

Commitments: <kept / dropped / renewed>

Next month:
1. <move> (addresses <diagnosis>)
2. <move> (addresses <diagnosis>)
3. <move> (addresses <diagnosis>)
```

## Notes

- Be willing to say the month changed nothing; a flat month is still a finding worth stating.
- Be willing to say a favorite hypothesis was wrong.
- If the Brain has fewer than about eight evidence entries for the month, say the model is under-fed and that confidence can't rise; the first move is better capture.
