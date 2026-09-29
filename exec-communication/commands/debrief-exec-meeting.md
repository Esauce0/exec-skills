---
description: "Debrief an executive meeting against its prep: what happened, whether the objective was met, signals from each person (with evidence class), the posture you showed, and what to do differently"
argument-hint: "<meeting, plus your notes or a transcript path>"
---

# /debrief-exec-meeting

Input: $ARGUMENTS

Closes the loop opened by `/prepare-exec-meeting`. The gap between what the user intended and what happened is some of the most useful evidence the system collects.

## Invocation

```
/debrief-exec-meeting Q4 planning review, notes in ~/notes/2026-10-02-q4.md
/debrief-exec-meeting skip-level with the CPO. It went sideways when I brought up eval headcount.
```

## Workflow

### Step 1: Load

Apply **exec-core:brain-protocol**: the prep file in `meetings/` (if none exists, debrief anyway and note that no prep was done), `people/` files for attendees, their `models/` rows. Read the user's notes or transcript. Ask two or three quick questions only if the notes miss what matters (decisions made, who said what on the contested point, how it ended).

### Step 2: Observations first

What happened, who said what, what was decided, by whom, with owners. Keep the user's interpretations out of this section. If a transcript exists, quote only verbatim.

### Step 3: Objective

Met, partly met, or not, against the observable success criterion from the prep, with evidence.

### Step 4: Signals by person

For each attendee, apply **exec-core:evidence-discipline**: what did they do or say that bears on trust, priorities, or their view of the user? Classify each signal (allocation, direct statement, observed behavior, tone). Tone alone gets recorded but never drives a hypothesis. Note the strongest alternative explanation for anything surprising.

### Step 5: The user's performance

Apply **exec-communication:meeting-presence** (debrief procedure) and **exec-core:executive-posture**:
- Posture shown, with the specific moments.
- Did they open with the answer? Handle challenge with composure? Make or avoid calls? Ask their question? Stop talking?
- Habits observed (from the presence audit list and this user's known patterns).
- Where they showed next-level behavior, and where they missed the opportunity identified in the prep.

Be direct. If the meeting went badly because of something the user did, say so and say what.

### Step 6: Follow-up

If the user drove the meeting or owns the outcome, draft the 24-hour follow-up note (decisions, owners and dates, open items) per exec-core executive-prose `references/formats.md`. If someone else owns it, follow up only on the user's own commitments.

### Step 7: Write

- Complete the Debrief half of the meeting file.
- Create evidence entries for significant signals (allocation, feedback, decisions), with signal tags.
- Update people files (interaction log, observed priorities, open loops).
- Propose hypothesis changes only if the confidence rules are met; otherwise note the signal for the monthly review.

## Output

Treat this template as a checklist of content: keep the order, drop empty items, and write it as prose where prose reads better (exec-core executive-prose).

```
<Meeting>: <one-line verdict: objective met? what changed?>

What happened: <observations>
Decisions: <decision; owner; date>

Signals:
- <Name>: <signal> (<evidence class>). Alternative reading: <...>.

You: posture <...>. Strong moments: <...>. Costly moments: <...>.
Next time: <one or two behaviors>.

Follow-up: <draft, or "sent">
Saved: <files> | Proposed: <model changes>
```

## Notes

- Debrief within 24 hours when possible; detail fades fast and gets rewritten by memory.
- A meeting that "felt great" with no decision, allocation, or specific statement produced little evidence. Say so.
