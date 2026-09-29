---
description: "Long-horizon review of how your scope, responsibility, reputation, sponsorship, leverage, compensation, visibility, and demonstrated executive capability have changed, and what that implies for the next 12 months"
argument-hint: "<period, e.g., 'last 12 months', '2024-2026', 'whole career'>"
---

# /career-retrospective

Input: $ARGUMENTS

Where monthly reviews find patterns inside a role, this looks across a longer period, often across roles, for the shape of the trajectory: where it accelerated, where it stalled, what the user was consistently right and wrong about, and what that means for the next year.

Run every six months, and after any promotion, reorg, manager change, or job change.

## Invocation

```
/career-retrospective last 12 months
/career-retrospective whole career
```

## Workflow

### Step 1: Load

Apply **exec-core:brain-protocol**: `self/career-history.md`, `self/ambitions.md`, `self/level-model.md`, all `models/` with review histories, monthly reviews and prior retros in the period, `commitments.md` (including closed ones), `opportunities.md` (including dropped). For a whole-career retrospective with a thin Brain, interview the user role by role using the `career-history.md` structure first.

### Step 2: Reconstruct the arc

For the period, lay out a timeline of changes on each dimension:

| Dimension | Start | End | Key inflection points (dated, with evidence) |
|---|---|---|---|
| Scope (the nine dimensions in the scope ledger) | | | |
| Responsibility for people | | | |
| Money (budget, revenue tied to the user's area) | | | |
| Reputation (calibration sentences) | | | |
| Sponsorship | | | |
| Leverage (output through others) | | | |
| Visibility (altitude of regular exposure) | | | |
| Compensation and level | | | |
| Demonstrated executive capability (readiness ratings) | | | |

### Step 3: Find the drivers

Apply **exec-observer:attribution-analysis** to each major inflection, up and down. What actually caused scope to grow when it grew? Typical findings: a turnaround assignment, a sponsor's arrival, a reorg, a crisis the user handled, a written strategy that traveled. Be specific and evidence-based.

### Step 4: Audit the model itself

Apply **exec-observer:trajectory-model** (retrospective procedure):
- Which hypotheses held? Which were wrong, and in which direction?
- Did the user systematically overrate or underrate how senior people saw them?
- Which commitments produced evidence, and which were abandoned? What does the abandonment pattern say?
- Which opportunities were dropped, and were those the right calls?

### Step 5: Rate and base rate

Compare the rate of change to the base rate in `self/level-model.md` (revealed ladder) and to the user's target horizon in `self/ambitions.md`. State plainly whether the current trajectory reaches the target on time, and if not, by how much it misses.

### Step 6: Readiness at the next level and the one after

Apply **exec-trajectory:next-level-readiness**. Where does the evidence say the user is strongest and weakest relative to the next level? Which gaps are structural to the current role (opportunity gaps) versus personal?

### Step 7: Options for the next 12 months

Lay out the real options with their tradeoffs, for example: deepen in the current role, expand scope here, move internally, move companies, change the target. For each: what evidence it would generate, what it risks, what it requires. Recommend one.

### Step 8: Write

Save `reviews/retros/YYYY-MM-DD-<period>.md`. Propose updates to `self/career-history.md § Patterns across roles`, and to `self/capabilities.md` and `self/ambitions.md` if the evidence warrants (everything in `self/` is propose-and-wait).

## Output

Treat this template as a checklist of content: keep the order, drop empty items, and write it as prose where prose reads better (exec-core executive-prose).

```
<Period>: <one-paragraph verdict: how the trajectory actually moved, the main driver, the main limiter>

Arc: <the table from Step 2, only rows with real change>

What drove growth: <causes, evidenced>
What limited it: <causes, evidenced>

Where the model was wrong: <hypotheses and the direction of error>
Blind spot suggested by those errors: <one or two sentences>

Rate: <vs base rate and vs target>

Options for the next 12 months:
- <option>: evidence it generates / risk / requirements
Recommendation: <option and why>

Three commitments for the next six months: <each tied to the recommendation>
```

## Notes

- This is where the coach is most likely to be tempted to flatter, so resist it: a long period of flat scope is a finding that deserves a straight statement.
- Compensation is a lagging indicator, but a strong one when it diverges from scope. Note it either way.
