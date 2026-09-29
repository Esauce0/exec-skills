---
description: "Review an executive update, email, escalation, or memo for both substance and communication quality: the thinking, the escalations, the posture it signals, and the prose, then rewrite it"
argument-hint: "<the draft, a file path, and who it's for>"
---

# /review-exec-update

Input: $ARGUMENTS

Evaluates a draft for a senior reader. Substance comes first (is the thinking right?), then posture (what does it signal?), then prose, and the review ends with a rewrite.

## Invocation

```
/review-exec-update <pasted weekly update>, for Maria, VP Product
/review-exec-update ~/drafts/q4-escalation.md for Priya
```

## Workflow

### Step 1: Load

Apply **exec-core:brain-protocol**: the recipient's `people/` file (priorities, pressures, how they take in information), `self/current-role.md` (decision rights, needed for the escalation test), and from the relevant Product Brain the strategy, recent decisions, metrics, and `rules/writing.md`. If the recipient is unknown, ask who it's for; the review depends on it.

### Step 2: Substance

Apply **exec-communication:executive-communication** with its `references/review-rubric.md`:
- The reader's question, and whether the draft answers it in the first two lines.
- Implications vs activity.
- Decided vs open vs asks.
- **The escalation test:** list every item that asks the reader for a decision; mark which are within the user's decision rights. These are the highest-value edits.
- Bad news placement and sizing.
- Owners, dates, numbers with comparisons, confidence.
- Enterprise link to the reader's priorities (**exec-trajectory:enterprise-thinking** if the update frames a bet or tradeoff).

Check facts against the Product Brain where possible (metrics, decisions). Flag contradictions.

### Step 3: Posture

Apply **exec-core:executive-posture**: the posture the draft signals, the markers, the behavior producing it, and the behavior change. Check for overreach too.

### Step 4: Prose

Apply **exec-core:executive-prose**: first-two-lines test, density, banned patterns, AI tells, formatting, length for the channel.

### Step 5: Rewrite

Produce the revised draft. Keep the user's voice where it's already good; don't polish into sameness. Make the calls the draft should have made only if they're clearly within scope and the evidence supports a direction; otherwise mark them `[your call: A or B]` with a recommendation.

### Step 6: Write back (optional)

If the draft is significant (to an executive, about a consequential topic), offer to log it as an evidence entry of type `communication` with the posture tag, so monthly reviews can see patterns in how the user writes upward.

## Output

Treat this template as a checklist of content: keep the order, drop empty items, and write it as prose where prose reads better (exec-core executive-prose).

```
Verdict: <what this draft signals to <reader>, one sentence>.

Substance:
- <the one or two issues that matter most>
Escalation: <items to decide, not ask> (or "clean")
Posture: <shown> → <target>. Behavior underneath: <...>.
Prose: <only the notable issues>

Rewrite:
<the revised draft>

Next time: <one behavior to change>
```

Keep the critique shorter than the rewrite.

## Notes

- Never add Career Brain content to the draft.
- If the draft is fine, say so and suggest at most two edits. Don't manufacture critique.
