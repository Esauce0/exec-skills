---
description: "Prepare for a consequential executive interaction: what each person likely cares about (from evidence), what to accomplish, own, recommend, ask, and avoid, and where to show next-level capability"
argument-hint: "<meeting: who, when, topic; or a calendar event>"
---

# /prepare-exec-meeting

Input: $ARGUMENTS

Reads the stakeholder, product, and trajectory context for an upcoming meeting and produces a preparation brief grounded in evidence about the people in the room. Opens the meeting loop that `/debrief-exec-meeting` closes.

## Invocation

```
/prepare-exec-meeting Q4 planning review with Priya and Dan on Thursday
/prepare-exec-meeting skip-level with the CPO next week
/prepare-exec-meeting board AI update slot, Nov 12
```

## Workflow

### Step 1: Load

Apply **exec-core:brain-protocol**:
- Career Brain: `people/` for every attendee; prior `meetings/` with them; their rows in `models/reputation.md` and `models/sponsorship.md`; `self/current-role.md` (decision rights); `commitments.md` (anything this meeting could advance); recent evidence naming them.
- Product Brains: strategy, relevant decisions, metrics, `stakeholders/` files for attendees, recent meeting ingestion on the topic, `rules/writing.md`.
- Optional, with permission: the calendar event and any pre-read.

State what's missing, especially if an attendee has no people file.

### Step 2: Read the room from evidence

For each attendee, apply **exec-influence:organizational-politics** (stakeholder model, briefly) and **exec-influence:executive-trust**:
- What they're accountable for and pressured by right now.
- What they've said and done about this topic (dated).
- How they take in information and react to challenge.
- The trust tier they currently extend to the user.
- What they'd count as a good outcome.

Tag every claim about a person with its evidence class. Where evidence is thin, say "unknown" rather than guessing.

### Step 3: Purpose, decider, and objective

Apply **exec-communication:meeting-presence**: what stage the meeting is at (listen, clarify, debate, decide, persuade), who decides, and the user's objective stated so it can be observed at the end.

### Step 4: Substance

Apply **exec-communication:executive-communication** and **exec-core:executive-posture**:
- The opening: answer or recommendation in two sentences.
- What the user will own in the room and decide themselves; what they'll ask for. Run the escalation test.
- Recommendations, with confidence stated once.
- Supporting points the room will need, in the order the decider cares about.
- If a pre-read is needed, draft it (or run `/review-exec-update` on the existing one).

### Step 5: Questions and challenges

- The one question the user will ask that shows next-level thinking. Apply **exec-trajectory:enterprise-thinking** to find the company-level implication nobody has named.
- Likely challenges per attendee, with short answers.

### Step 6: Avoid

Specific to this user and this room: patterns from past debriefs (over-explaining, defending, going technical, adding too much value), topics to keep out, anything that would surprise the manager.

### Step 7: The next-level opportunity

Where in this meeting the user can show capability at the next level: making a call in scope, naming a cross-functional tradeoff with a proposed resolution, owning a problem beyond their charter, representing the company view over the function's. Only if genuine; don't invent one.

### Step 8: Pre-wiring

Who needs to hear the recommendation before the meeting (the manager almost always), in what order, by when.

### Step 9: Write

Create `meetings/YYYY-MM-DD-<slug>.md` with the Prep half filled in (schema in the Career Brain's `meetings/_SCHEMA.md`). Remind the user to run `/debrief-exec-meeting` afterward.

## Output

Treat this template as a checklist of content: keep the order, drop empty items, and write it as prose where prose reads better (exec-core executive-prose).

```
<Meeting>, <date>. Decider: <name>. Stage: <decide / debate / ...>.
Objective: <observable>.

The room:
- <Name>: cares about <...> (evidence). Pressure: <...>. Trust tier: <...>. Watch for: <...>.

Open with: "<two sentences>"
You own: <...>. You'll ask for: <...> (only what needs their authority).
Recommendation(s): <...> (confidence).

Your question: "<...>"
Likely challenges: <challenge → answer>

Avoid: <...>
Next-level opportunity: <...>
Pre-wire: <who, by when, what to say>

Success by the end of the meeting: <observable>
```

## Notes

- For a manager 1:1, keep it short: agenda, the one thing to land, the ask.
- For a board slot, also apply the board briefing structure in executive-communication `references/board-altitude.md`, and pre-wire with the CEO or sponsoring executive.
- Never put Career Brain content into anything shared (pre-reads, slides, agendas).
