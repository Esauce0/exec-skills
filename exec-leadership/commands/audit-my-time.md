---
description: "Audit where your time actually goes against leverage and against the next level's time allocation: find negative leverage, comfort work, and what to stop, delegate, or systematize"
argument-hint: "<optional: period, e.g., 'last 2 weeks'; defaults to the last 2 weeks of calendar>"
---

# /audit-my-time

Input: $ARGUMENTS

Time allocation is one of the most honest readiness signals there is. Each level up shifts time from doing to enabling, to developing leaders, to cross-functional and strategic work. This command compares where the user's time goes with where the next level's goes.

## Invocation

```
/audit-my-time
/audit-my-time last 4 weeks
```

## Workflow

### Step 1: Load

- With permission, read the calendar for the period. Otherwise ask the user for a rough week (recurring meetings plus a typical day) or a calendar export.
- Apply **exec-core:brain-protocol**: `self/current-role.md`, `self/level-model.md`, `models/readiness.md`, `commitments.md`. From Product Brains: `knowledge/org/rituals.md` for recurring meetings.

### Step 2: Classify

For each block, apply **exec-leadership:managerial-leverage**:
- Bucket: own IC production; enabling others; talent; cross-functional business work; strategy and thinking; external.
- Leverage: high, medium, low, or negative, with the reason (reach, durability, unique knowledge at decision time).
- LNO type for the work inside it.
- Meeting type: process or mission; owner; would anyone miss it?

Ask the user to tag the blocks they found most satisfying. This is the values probe from **exec-trajectory:next-level-readiness**: people protect the work they enjoy, and the enjoyable work is usually the previous level's.

### Step 3: Compare

- Current mix vs the target level's mix (company model first; the heuristic table in managerial-leverage `references/leverage-toolkit.md` otherwise).
- Negative leverage instances.
- Comfort work (Ibarra's competency trap): hours spent on craft the user is already excellent at.
- Unowned or decision-less meetings.

### Step 4: Root causes

For the biggest gaps: missing strategy (Doshi: chronic busyness), unclear decision rights, low-maturity delegation, meeting sprawl, or preference for comfort work. Say which, with evidence.

### Step 5: Redesign

- **Stop:** specific blocks, with how to exit gracefully.
- **Delegate:** to whom, at what supervision style (task-relevant maturity).
- **Systematize:** templates, decision frames, cadences that replace recurring personal effort.
- **Add:** the next-level activities missing from the week (e.g., a monthly peer-leader 1:1 series, protected strategy time, a coaching relationship).

### Step 6: Write

Evidence entry (type `observation`, `source: self-assessment`, signal `activity-only`). A self-audit of one's own calendar only records activity; the readiness signal comes later, when the changed allocation produces observable results. Propose one commitment with a check-in date.

## Output

Treat this template as a checklist of content: keep the order, drop empty items, and write it as prose where prose reads better (exec-core executive-prose).

```
Verdict: <your week looks like a <level> week>, (confidence).

Mix: <bucket: current % vs target %>, only the rows that matter.
Negative leverage: <instances>.
Comfort work: <hours and what>.
Root cause: <...>.

Stop: <...>
Delegate: <... → whom, style>
Systematize: <...>
Add: <...>

One change this month: <...>, check-in <date>.
```

## Notes

- Don't moralize about hours; what matters is the mix.
- If the role structurally prevents next-level time (no reports, no cross-functional forum), that's an opportunity gap: offer `/expand-my-scope`.
