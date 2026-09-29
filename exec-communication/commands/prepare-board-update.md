---
description: "Decide what belongs at board altitude versus operating detail, and reconstruct a board update or board slot around strategy, risk, talent, performance, and a clear ask"
argument-hint: "<topic, source material (deck, doc, or product brain), and the sponsoring executive>"
---

# /prepare-board-update

Input: $ARGUMENTS

Takes operating material and rebuilds it for a board: the few things a board governs, at company altitude, with a clear ask and nothing that would surprise the CEO or the directors.

## Invocation

```
/prepare-board-update AI assistant strategy, from ~/decks/ai-q3-review.pptx, slot sponsored by the CPO
/prepare-board-update quarterly product update for the board pre-read
```

## Workflow

### Step 1: Load

Apply **exec-core:brain-protocol**: source material; the Product Brain's strategy, metrics, decisions for the quarter, and market knowledge; the Career Brain `people/` file for the CEO and the sponsoring executive (what the board has already heard, what the sponsor wants from the slot, if known).

Ask, if unknown: is this a decision, a request for input, or information? What has the board already been told about this topic? What does the sponsor want the board to take away?

### Step 2: Sort altitude

Apply **exec-communication:executive-communication** with `references/board-altitude.md`. Sort every item in the source into:
- **Board altitude:** strategy and the company's central idea, material risk, talent and succession, performance trends, capital allocation.
- **Operating detail:** everything else. Keep a short appendix only if directors are likely to ask.

Translate each board-altitude item from activity to company meaning (translation table in the reference).

### Step 3: Enterprise framing

Apply **exec-trajectory:enterprise-thinking**: economics (margin, cash, growth quality), binding constraint, the kernel (diagnosis, guiding policy, coherent actions, what we won't do).

For AI topics, apply **exec-product-leadership:ai-product-leadership**: capability evidence vs hype, economics, risk governance, industry debate vs this company's unit economics.

### Step 4: Build the briefing

Use the board briefing structure: purpose line; what changed; diagnosis; choices and recommendation; risk; talent; the few numbers as trends; the specific ask. One page per topic for the pre-read.

### Step 5: No-surprises check

- Is anything in here news to the CEO or the sponsoring executive? Pre-wire it first.
- Is there bad news? It should reach directors between meetings via the CEO, so the room is never where they first hear it.
- Does anything contradict what the board was previously told? Address it explicitly.

### Step 6: Q&A preparation

The likely director questions (including the question behind the question), short answers, and which ones get "I'll follow up by <date>."

### Step 7: Posture and prose

Apply **exec-core:executive-posture** (company altitude, owner posture, no theater) and **exec-core:executive-prose**.

### Step 8: Write

Save the prep to `meetings/YYYY-MM-DD-board-<topic>.md` (Prep half). If this is new exposure, record the slot itself as an evidence entry of type `allocation` (someone gave the user a board slot). Tag `visibility+` only after the debrief, once directors have actually seen the work and attributed it.

## Output

Treat this template as a checklist of content: keep the order, drop empty items, and write it as prose where prose reads better (exec-core executive-prose).

```
Purpose: <decision / input / information> on <board area>.
Moved to appendix or cut: <operating detail, briefly>.

Pre-read (one page):
<the draft>

Pre-wire: <CEO/sponsor, what to align on, by when>
Likely questions: <question → answer>
Watch: <anything that could surprise or contradict prior board messages>
```

## Notes

- The board slot belongs to the CEO or sponsoring executive. Align with them; never contradict their framing in the room.
- Directors form a succession read on presenters. Composure and directness matter more than slide polish.
