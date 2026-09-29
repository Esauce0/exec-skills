---
description: "Weekly trajectory review: separate what moved your trajectory from competent execution, spot missed openings, and pick the one or two highest-leverage moves for next week"
argument-hint: "<optional: anything notable from the week not yet captured>"
---

# /review-my-week

Input: $ARGUMENTS

A weekly review of meetings, decisions, work, stakeholder interactions, communication, wins, problems, and responsibilities, read through the question that matters: did anything this week change what senior people will trust me with?

## Invocation

```
/review-my-week
/review-my-week Also: Maria asked me to cover her staff meeting next Tuesday
```

## Workflow

### Step 1: Load the week

Apply **exec-core:brain-protocol**:
- `evidence/LOG.md` entries from the last 7 days, and those entries.
- `meetings/` files from the last 7 days (prep and debrief halves).
- `commitments.md` (active), `models/trajectory.md`, last week's review.
- Product Brains: decisions and meeting ingestion from the last 7 days, for active products.
- Optional, with permission: calendar for the week (to catch meetings never captured).

### Step 2: Fill the gaps

The Brain rarely holds the whole week. Ask once, in a single message, only about what's missing. Typical prompts: executive interactions not yet captured; feedback received; decisions made or escalated; messages sent to senior people; anything that surprised you; anything you avoided. Apply the `/capture` procedure to the answers so they become evidence entries.

### Step 3: Grade the work

Apply **exec-observer:trajectory-model** (weekly pass). For each notable piece of work or interaction:
- **A:** current-level excellence.
- **B:** next-level capability demonstrated (per the readiness dimensions).
- **C:** B, seen and attributed by someone with power over the next step.

Count `activity-only` entries against entries with trajectory signals.

### Step 4: Read posture

Apply **exec-core:executive-posture** to the week's notable communications and meeting behavior. Look for recurring leaks (escalation, option-list, activity, dependency, expert, lane) and for moments of next-level posture worth repeating.

### Step 5: Relationships, sponsorship, scope, visibility

- Relationships requiring investment: boss, skip-level, sponsors, and anyone with a friction signal this week; flag key people with no touchpoint in 60 days.
- Emerging sponsorship: any act of advocacy, or a warmer signal worth testing. Classify with `evidence-discipline`; a friendly comment is not sponsorship.
- Scope changes: anything granted, assumed, taken back, or formalized.
- Visibility changes: new exposure to deciders, and whether it was attributed.

### Step 6: Missed openings

Where the week offered a chance to show next-level capability and the user didn't take it: a meeting where they stayed in their lane, a decision they escalated, a cross-team problem they saw and didn't raise. Name specific moments. This is the section users most want to skip; don't let them.

### Step 7: Commitments

Check each active commitment against its "done looks like." Update status.

### Step 8: Moves for next week

Pick at most two, each specific (who, what, when) and tied to a diagnosis. Prefer moves that generate B or C evidence or that address the binding cause from `attribution-analysis`.

### Step 9: Write

Save `reviews/weekly/YYYY-Www.md` with the output below. Update people touchpoints, scope change log, and commitments per brain-protocol. Propose (don't apply) any hypothesis change; monthly review is where those normally happen.

## Output

Treat this template as a checklist of content: keep the order, drop empty items, and write it as prose where prose reads better (exec-core executive-prose).

Follow **exec-core:executive-prose**, omit any section with nothing real in it, and lead with the one-line verdict.

```
Week YYYY-Www: <one line: did the trajectory move, and why or why not>

Moved the trajectory:
- <C and strong B items, with why>

Competent execution (good, not trajectory):
- <A items, briefly>

Next-level behavior shown:
- <specific moments>

Current-level behavior shown:
- <specific moments, with the posture leak named>

Missed openings:
- <specific moments and what the next-level move would have been>

Relationships: <who needs investment, and the specific reason>
Sponsorship: <any act, or signal worth testing>
Scope: <changes>
Visibility: <changes, with attribution>

Commitments: <status line each>

Next week:
1. <move> (addresses <diagnosis>)
2. <move> (addresses <diagnosis>)
```

Then the write-back summary.

## Notes

- If the week was simply competent execution, as most weeks are, say so. The point is to see the ratio over time.
- Don't grade effort. A brutal week of firefighting is usually A-grade.
- Offer `/review-my-month` if this is the last weekly review of the month.
