---
name: decision-making
description: "Improve decision rights and decision quality: who decides, what's within the user's authority, matching process to reversibility and impact, deciding at roughly 70% information when you can correct course, voice-then-commit, pre-commitment and kill criteria, probabilistic confidence, independent input, and judging decisions by process rather than outcome. Use when the user faces a consequential decision, is unsure whether to decide or escalate, is stuck in consensus, disagrees with a decision, is reviewing a past call, or needs to frame a decision for executives."
---

# Decision Making

## Purpose

Two things about decisions shape how senior leaders see someone. First, decision rights: does this person make the calls within their scope, recommend beyond it, and escalate only what needs more authority? Second, decision quality: are their calls calibrated, fast when cheap to reverse, careful when not, and honest about uncertainty?

This skill develops both. It is also the reference for whether an escalation is a posture leak or the right move.

## Use when

- A consequential decision is in front of the user.
- "Should I decide this or escalate it?"
- A group is stuck, circling toward consensus that won't come.
- The user disagrees with a decision someone else made.
- Reviewing a past decision (especially after a bad outcome).
- Framing a decision for executives (with `/frame-decision`).

## Don't use when

- The issue is how to present an already-made decision (use `executive-communication`).

## Standards

Everything this skill produces follows the three exec-core standards. If exec-core isn't loaded, apply them as stated here:
- **Evidence:** separate what happened from inference; label any claim about another person's view or motive as a hypothesis with confidence and a falsifier; never state it as fact.
- **Posture:** when the user's behavior is part of the problem, fix the behavior before the wording.
- **Prose:** answer first, recommendation over options, owners and dates, no filler.

## Core doctrine

1. **Settle the frame before debating the substance** [Grove]. What exactly is being decided, by when, who decides (one name), who is consulted, who can ratify or veto, who is informed afterward. Many "disagreements" are really unclear frames.
2. **Decide who decides, and keep problem-solving local** [Hughes Johnson]. Say whether a meeting is for discussing or deciding. Escalating decisions that the team's own principles already answer quietly slows the whole company. Where ownership is murky, driving a decision openly (bringing the other plausible owners along) is a visible next-level behavior.
3. **Match process to reversibility and impact** [Bezos]. One-way doors (hard to reverse) deserve rigor and more voices. Two-way doors should be made quickly, by individuals or small groups.
4. **At your level, many two-way doors are one-way** [Doshi]. Sales commitments, customer expectations, a narrative told to executives, and team morale make "reversible" product decisions sticky. Price the real reversal cost.
5. **Decide with about 70% of the information you wish you had, when you can correct course** [Bezos]. Waiting for 90% is usually slow. The condition matters: this holds only where course correction is possible.
6. **Free discussion, clear decision, full support** [Grove]; **have backbone, then disagree and commit** [Bezos]; **get to the best idea, then someone makes the call** [Campbell]. Argue fully before the decision, commit publicly after it, and don't relitigate in side channels. When the user decides: hear every position, speak last, name the principle that broke the tie.
7. **Stop resulting** [Duke]. Judge a decision by its process and what was knowable at the time, not by its outcome. Record reasoning and probabilities before the outcome; bosses will judge on results otherwise.
8. **State confidence as probabilities and ranges** [Duke]. "About 70%" is information; "should be fine" isn't.
9. **Spend decision time in proportion to impact** [Duke]. Low-impact, frequent, reversible decisions deserve seconds.
10. **Set kill criteria before starting; tackle the hardest part first** [Duke]. "If by <date> we haven't reached <state>, we stop." Agreed with the boss in advance.
11. **Collect independent input before discussion** [Duke]. Anchoring on the first or loudest view is the default failure of group decisions.
12. **Premortem the big ones** [Doshi; Duke]. Imagine it failed; name the tigers (real threats), paper tigers (overblown ones), and elephants (the thing nobody is saying). Turn the tigers into tripwires.
13. **Take written positions** [Horowitz; Amazon]. Disagreement only voiced verbally or after the fact leaves no evidence of judgment.
14. **Know the mode** [Horowitz]. Peacetime favors broad input and empowered teams; wartime (existential threat) favors fast, centralized calls. Misreading the mode is a judgment failure in itself.

## Decision rights: the sort

| The decision is... | The user should... |
|---|---|
| Within their decision rights (`self/current-role.md`) | Decide. Inform with the reason if non-obvious. |
| Within scope but affects a peer's area | Decide with the peer, or agree who decides. |
| Beyond their authority, or crosses peers with no agreement, or exceeds risk tolerance | Recommend, with a deadline and the cost of delay. Escalate jointly with the peer when there's disagreement. |
| Murky ownership, important, stalling | Offer to drive it openly; name the decider; bring the other plausible owners along. |

## Evidence to gather

- `self/current-role.md § Decision rights`.
- Product Brain `decisions/` (precedent, and what would reverse earlier calls), `hypotheses/`, metrics.
- People files for the decider and the affected peers.
- Outcomes of the user's earlier comparable decisions, reviewed outcome-blind.

## Reasoning procedure

1. **Frame it** with the six questions. If "who decides" has no answer, stop there.
2. **Classify**: impact (low / high) and reversibility (two-way / one-way), with the real reversal cost.
3. **Sort decision rights**: is this the user's call?
4. **Size the process** to the classification: minutes for low/two-way; a premortem, independent input, and a written memo for high/one-way.
5. **Generate options** including "do nothing" and "decide later (by when?)".
6. **Estimate** outcomes as probabilities and ranges; name the key uncertainty and whether it can be reduced cheaply before deciding.
7. **Premortem** (for high-impact): tigers, paper tigers, elephants; convert tigers into tripwires.
8. **Decide or recommend**, with confidence and kill criteria.
9. **Record** the reasoning, probabilities, and kill criteria before the outcome is known (decision record in the Product Brain via its own workflow; a career-relevant decision can also get a Career Brain evidence entry).
10. **After the outcome,** run an outcome-blind review of the process.

## Diagnostic questions

- Who decides? One name.
- Is it yours to decide?
- What would reversing it actually cost?
- What would you have to believe for each option to be right?
- What's your probability, and what would change it?
- What are the kill criteria?
- Whose view hasn't been collected independently?

## Failure modes

- Escalating in-scope decisions (the most common posture leak).
- Consensus-seeking on a decision the user owns.
- Moving slowly on two-way doors and quickly on one-way doors.
- Relitigating after commitment, especially in front of one's own team.
- Resulting: learning the wrong lesson from one outcome.
- Certainty language with no probability behind it.
- Deciding without kill criteria, then continuing out of sunk cost.

## Output

```
Decision: <one sentence>. Decider: <name>. By: <date>.
Type: <impact> / <reversibility>, real reversal cost: <...>.
Whose call: <user decides / user recommends / drive openly>.
Options: <with probability-weighted outcomes, briefly>.
Recommendation: <option>, (~<confidence>%). Key uncertainty: <...>.
Kill criteria / tripwires: <if by <date> ..., we <stop/change>>.
Process: <what's needed before deciding, sized to the type>.
```

## Tensions in the doctrine

- **Full support vs disagree-and-commit.** Grove asks for full support once decided; Bezos lets dissent stay on the record while committing. Both forbid relitigating.
- **Empowered teams vs wartime command.** Cagan: teams decide solutions, evidence settles disputes. Horowitz: in a real crisis the leader decides and doesn't wait. Diagnose the mode first.
- **Two-way doors vs sticky decisions.** Bezos says move fast on reversible decisions; Doshi warns that at senior levels, reversibility is often an illusion. Price the reversal honestly.
- **Speed vs rigor in AI.** See `ai-product-leadership`: risk tiers decide which process applies.

## Interactions

- `executive-posture` uses the decision-rights sort to diagnose escalation leaks.
- `executive-communication` presents decisions and escalations.
- `organizational-politics` maps deciders and vetoes for contested decisions.
- `managerial-leverage` covers delegating decisions to others.

## References

- `references/decision-toolkit.md`: decision frame, reversibility pricing, premortem protocol, kill-criteria template, outcome-blind review, and the voice-then-commit protocol.
