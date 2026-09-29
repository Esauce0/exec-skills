---
description: "Audit whether the evidence for operating at the next level actually exists, what's missing, who has seen it, and what to do about the gaps, before building any promotion argument"
argument-hint: "<target role, e.g., 'Director of Product, AI' and optional cycle timing>"
---

# /position-for-promotion

Input: $ARGUMENTS

Before any promotion case gets written, this command establishes whether the case exists. Most users arrive wanting help arguing; the useful answer is often that the argument isn't ready and here is exactly what would make it ready.

## Invocation

```
/position-for-promotion Director of Product, next cycle in March
/position-for-promotion
```

## Workflow

### Step 1: Load

Apply **exec-core:brain-protocol**: `self/level-model.md`, `self/ambitions.md`, `self/current-role.md`, `models/readiness.md`, `models/reputation.md`, `models/sponsorship.md`, `models/visibility.md`, evidence entries tagged `readiness:*` or of type `allocation` or `feedback`, and the last two monthly reviews. From Product Brains: decisions the user drove and metrics for products they own.

If `self/level-model.md` lacks the promotion mechanics (who decides, when, what the packet looks like, whether a role must exist), ask for them, since they shape every later step.

### Step 2: Readiness audit

Apply **exec-trajectory:next-level-readiness** in full: operating level by the work, the three shifts (skills, time, values), dimension ratings from evidence, duration test, transition failure-mode screen.

Apply the evidence standard (next-level, sustained, material, attributable, seen, corroborated) to every item the user wants to cite. Items that fail are listed as such, with the reason.

### Step 3: Perception and cause

Apply **exec-observer:attribution-analysis** to the gap between where the user thinks they are and what the evidence shows. For each weak dimension, consider all ten cause classes: capability, behavior, visibility, attribution, perception lag, sponsorship, opportunity, context, fit, and genuine unreadiness. State explicitly whether genuine unreadiness and fit were ruled out, and on what evidence. If they weren't, say so.

### Step 4: Who decides, and what have they seen

Apply **exec-influence:sponsorship**:
- List the people in the decision (manager, calibration committee, skip-level, VP, CPO).
- For each: what have they directly seen of the user's next-level work in the last two quarters? Would they advocate unprompted? Classify the evidence as sponsorship, mentorship, or goodwill.
- Is there a role? Headcount and org design gating is common and often invisible to the candidate.

### Step 5: The skeptic's case

Run the promotion-committee questions from next-level-readiness `references/promotion-evidence.md` as the strongest fair skeptic. For each, decide whether the objection is right.

### Step 6: Verdict

One of:
- **The case exists.** Evidence meets the standard and deciders have seen it. Move to Step 7.
- **The case exists but is invisible or unattributed.** Plan visibility and sponsorship moves before the cycle.
- **The case is partial.** Specific dimensions lack evidence. Plan leap assignments with dates; agree explicit criteria with the manager.
- **The case doesn't exist yet.** Say so plainly, with the realistic timeline and what would change it.

### Step 7: If the case exists, structure it

Apply **exec-communication:executive-communication**. Build the case from the structure in next-level-readiness `references/promotion-evidence.md`: claim, 3-5 evidence items with outcomes and who saw them, the honest development area, corroboration, and the forward view. Company outcomes first; named credit to others.

### Step 8: Plan the conversation

Draft how the user raises it with their manager: stating the goal explicitly, asking what evidence the manager would need to see, agreeing criteria in writing, and asking who else in the decision the user should be working with. Apply **exec-influence:managing-up**.

### Step 9: Write

Update `models/readiness.md` (propose rating changes), add leap assignments to `commitments.md` (propose), and record the manager conversation plan in `meetings/` if scheduled.

## Output

Treat this template as a checklist of content: keep the order, drop empty items, and write it as prose where prose reads better (exec-core executive-prose).

```
Verdict: <one of the four>, (<confidence>). <Two sentences why.>

Evidence that holds up:
- <item>; dimension; who saw it

Evidence that doesn't (yet):
- <item>; fails on <test>

Gaps by cause: <dimension; cause class; move>

Deciders: <person; what they've seen; ladder level (contact to sponsor), with evidence>
Unreadiness and fit: <ruled out, and on what evidence / not ruled out>
Role available: <yes / no / unknown>

The skeptic's strongest objection: <objection>. It is <right / partly right / wrong> because <evidence>.

Next 90 days:
1. <move with date>
2. ...

<If the case exists:> Case draft: <structured>
<Always:> Manager conversation: <opening lines and the ask>
```

## Notes

- Do not help the user argue for a promotion the evidence doesn't support; redirect the effort into building that evidence.
- If the user's goal is to leave rather than rise here, say which evidence transfers to an external case and which doesn't (internal reputation doesn't; shipped outcomes and scope do).
