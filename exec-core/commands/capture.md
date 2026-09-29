---
description: "Turn raw notes, a transcript, feedback, or a quick description into disciplined evidence entries in your Career Brain"
argument-hint: "<notes, a file path, 'inbox', or a description of what happened>"
---

# /capture

Input: $ARGUMENTS

The observer is only as good as its evidence. This command turns raw material into evidence entries: observations separated from interpretation, people and products tagged, signals marked conservatively.

## Invocation

```
/capture Priya asked me to present eval results at Thursday's staff instead of Dan
/capture ~/notes/2026-09-24-skip-level.md
/capture inbox                   # process everything in the Career Brain's inbox/
```

## Workflow

### Step 1: Load

Apply **exec-core:brain-protocol**: `people/INDEX.md`, `evidence/_SCHEMA.md`, `evidence/LOG.md` (last 30 days, to spot duplicates and patterns), and person files for anyone named. For meeting transcripts tied to a product, check that Product Brain's `ingestion/meetings/` for an existing synthesis (read only).

### Step 2: Split into events

One event per entry. A page of 1:1 notes may hold three events (a piece of feedback, a scope change, a decision). A transcript may hold one.

### Step 3: For each event

Apply **exec-core:evidence-discipline**.

- **Type** from the schema. Prefer `allocation` when someone gave or withheld scope, a room, a problem, people, budget, or a nomination.
- **What happened:** observations only. Who said or did what, when. Verbatim quotes only if the source is verbatim; otherwise paraphrase and mark it.
- **Why it might matter:** inference, labeled, naming the hypotheses in `models/` it bears on.
- **My part:** what the user did or said. Note posture if it's informative.
- **Signals:** tag only what the observation supports. Use `?` when plausible but unclear. Use `activity-only` for real work with no trajectory signal; reviews need that ratio.
- **Source and provenance:** direct, reported, documentary, or self-assessment; link the raw notes if they exist.

If the user's description mixes interpretation into fact ("she was clearly annoyed that I..."), split it: record what she did and said as observation, and the user's read as inference. Mention the split briefly.

### Step 4: Write

- Entry files and LOG lines (act and tell by default).
- New people: skeleton person file with facts only, plus a row in `people/INDEX.md`.
- Existing people: interaction log line, last-touched date, and new stated or observed priorities if the event contains them.
- `scope-change` events: a row in `models/scope.md § Change log`.
- Follow-ups: add to the person's Open loops.

Do not change hypotheses here. If an event is strong enough to move one under the confidence rules, propose the change.

### Step 5: Report

Write-back summary, then at most two lines on anything notable: a pattern forming ("second allocation from Priya this month"), a contradiction with a current hypothesis, or a missing fact worth recording. No coaching unless asked; offer `/coach-me` if something clearly needs it.

## Notes

- Capture the unflattering events too. A Brain that only records wins produces a flattering, useless model.
- Don't infer more signals than the event supports. Over-tagging poisons monthly pattern detection.
- When processing `inbox/`, move processed files into an `inbox/processed/` folder rather than deleting them.
