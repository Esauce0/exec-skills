---
name: executive-communication
description: "Design and review communication to executives and boards for both substance and altitude: weekly updates, recommendations, decision requests, escalations, bad news, narrative memos, promotion cases, and board material. Chooses the right form for the reader's state (pyramid, narrative, shared diagnosis), separates what's decided from what's open, and decides what genuinely needs escalation. Use when writing or reviewing anything for senior leaders, deciding whether and how to escalate, preparing board or leadership-team material, or when feedback says the user's communication 'isn't executive.'"
---

# Executive Communication

## Purpose

Senior people judge judgment largely through communication: what someone chooses to tell them, what they decide on their own, what they escalate, how they frame bad news. This skill handles the substance and structure of executive communication. The sentence-level standard lives in `executive-prose` and the underlying behavior in `executive-posture`, and the three are designed to be used together.

## Use when

- Writing or reviewing an update, recommendation, escalation, memo, promotion case, or board material.
- Deciding whether something should be escalated at all.
- Feedback that the user's communication isn't executive, is too long, too detailed, or lacks a point.

## Don't use when

- Live meetings: use `meeting-presence` (it uses this skill's structures verbally).

## Standards

Everything this skill produces follows the three exec-core standards. If exec-core isn't loaded, apply them as stated here:
- **Evidence:** separate what happened from inference; label any claim about another person's view or motive as a hypothesis with confidence and a falsifier; never state it as fact.
- **Posture:** when the user's behavior is part of the problem, fix the behavior before the wording.
- **Prose:** answer first, recommendation over options, owners and dates, no filler.

## Core doctrine

1. **The reader's question determines the structure** [Minto]. Write the reader's question down; the governing thought answers it. If you can't write the governing thought in one sentence, the analysis isn't done.
2. **Situation, complication, question, answer** [Minto]. The introduction contains only what the reader will accept without argument, then what changed, then the answer.
3. **Vertical and horizontal logic** [Minto]. Each level summarizes the level below. Groupings contain one kind of idea, in a stated order, with no overlaps and no gaps. Headings state assertions; a topic heading such as "Findings" is intellectually blank.
4. **For decisions that matter, write a narrative** [Bezos/Amazon]. Connected prose exposes the weak reasoning that bullets hide. Weak memos usually come from underestimating the work, and strong writers underestimate it too.
5. **Choose the form by the reader's state** [Minto; Amazon; synthesis]. Use a strict pyramid for an aligned, busy reader; a narrative memo with an answer-first summary for a skeptic with time; shared diagnosis first for a reader hostile to the conclusion; and a problem statement plus open questions for one who is still exploring.
6. **Report what's broken; no happy talk** [Slootman; McCord]. Lead with the problem, the diagnosis, the fix, and the ask.
7. **Fluff is a warning sign** [Rumelt]. Translate each strategic sentence into plain words and ask what anyone would do differently tomorrow. If nothing, cut it.
8. **Present to executives to learn their view** [Larson]. Lead with the answer; expect interruption; extract the concern behind their pushback.
9. **Connect to impact** [Doshi]. Updates written only at the execution level to readers operating at the impact level produce conflict that looks like disagreement but is a level mismatch.
10. **State confidence as probabilities** [Duke]. "About 70%, and the risk is the vendor API" beats "we should be fine."
11. **Escalate by co-writing the disagreement** [Hughes Johnson]. Joint escalations with a shared statement of facts and each side's case signal organizational leadership.
12. **Boards govern a few things; bring them altitude** [Charan]. Those things are the company's central idea, strategy, risk, talent and succession, and performance. Never surprise a board.

## The escalation test

Before anything goes up, sort every item:

| Category | Test | Action |
|---|---|---|
| Mine to decide | Within my decision rights (`self/current-role.md`); my manager would be surprised I asked | Decide; report in one line with the reason if non-obvious |
| Mine to recommend, theirs to decide | Exceeds my authority, or crosses a peer's area with no agreement, or exceeds risk tolerance | Escalate with recommendation, deadline, and cost of delay |
| Theirs, I need to inform | Affects their commitments or their stakeholders | Inform, briefly, early |
| Noise | Doesn't change their understanding or decisions | Cut |

Most drafts escalate at least one item from the first row. Catching it is often the single highest-value edit.

## Modes

Templates live in `executive-prose/references/formats.md` (exec-core). What differs by mode:

| Mode | The reader's question | Common failure |
|---|---|---|
| Weekly update | "Do I need to know or do anything?" | Activity reporting; burying the one thing that matters |
| Recommendation | "What should we do, and why should I believe you?" | Options without a recommendation; no cost stated |
| Decision request / escalation | "What do you need from me, by when?" | In-scope decisions sent up; no deadline; complaint instead of decision |
| Bad news | "How bad, what are you doing, what do you need?" | Late, minimized, spun, buried |
| Narrative memo | "Is this reasoning sound?" | Bullets in paragraph clothing; missing alternatives and objections |
| Promotion case | "Is this person already doing the job?" | Current-level wins; self-congratulation; no development area |
| Board material | "What does this mean for the company, and what do you need from us?" | Operating detail; surprises; no clear ask (see `references/board-altitude.md`) |

## Evidence to gather

- The recipient's `people/` file: priorities, pressures, intake style.
- `self/current-role.md § Decision rights`, for the escalation test.
- Product Brain strategy, recent decisions, metrics, and `rules/writing.md`.
- Earlier communications to this reader (evidence type `communication`) and how they landed.

## Reasoning procedure

1. **Reader:** who exactly, what they know, what they believe, their current pressures (from their `people/` file), how they take in information.
2. **Question:** write the reader's question.
3. **Escalation test** on every item.
4. **Governing thought:** one sentence that answers the question. If it won't come, go back to the analysis.
5. **Form:** choose by reader state.
6. **Build:** SCQA opening, then supporting points in a stated order, each an assertion.
7. **Substance checks:** implications not activity; decided vs open vs asks separated; numbers with comparisons; owners and dates; confidence stated once; bad news first.
8. **Posture check** with `executive-posture`, then a prose check with `executive-prose`.
9. **Privacy check:** nothing from the Career Brain in the artifact.

## Output

For a new draft: the draft itself, then at most two lines on the choices made (the form chosen, what was decided rather than escalated). For a review of an existing draft:

```
Verdict: <what the draft signals to this reader, one sentence>.
Substance: <what's wrong with the thinking: missing decision, wrong altitude, buried bad news, no recommendation>.
Escalation: <items that should be decided, not asked>.
Structure: <does the first two lines answer the reader's question?>.
Posture: <per executive-posture>.
Rewrite: <the revised draft>.
The behavior to change next time: <one line>.
```

## Diagnostic questions

- What is the reader's question, written as a question?
- What must the first two lines say?
- Which items in this draft are yours to decide?
- What changed since the reader last heard about this?
- What's the bad news, and is it first?
- Which detail proves you looked underneath the dashboard?
- What would a skeptical reader call unsupported?

## Failure modes

- Activity reporting in place of state and implications.
- Escalation leaks: decisions within the writer's authority sent up as questions.
- Options without a recommendation, or a recommendation without its cost.
- Bad news buried, minimized, or late.
- The wrong form for the reader's state: a wall of text to a listener, bullets for a contested decision.
- Over-compression that strips the context the reader needs to decide.
- Fluff or executive theater: strategic vocabulary with no choice behind it.
- Career Brain content leaking into a shareable artifact.

## Tensions in the doctrine

- **Pyramid vs narrative.** Minto for busy, aligned readers who need the answer; Amazon narratives when the reasoning itself is on trial. Many real memos need both: an answer-first summary over a narrative body.
- **Brevity vs context.** Short is usually better; over-compression that strips decision-relevant context is a real failure mode (see executive-prose before-after example 6).
- **Win vs learn.** Pfeffer's research favors projecting confidence and power when presenting; Larson favors presenting to learn the executive's view. The two fit together if the user projects confidence in the recommendation while staying curious about the objection.

## Interactions

- `executive-prose` (sentence standard) and `executive-posture` (behavior) are applied to every output.
- `enterprise-thinking` supplies the business framing; `decision-making` supplies decision rights and reversibility.
- `meeting-presence` uses the same structures verbally.

## References

- `references/board-altitude.md`: what boards govern, what they need from management presenters, translating operating detail to board altitude, and the board briefing structure.
- `references/review-rubric.md`: the full review rubric for `/review-exec-update`, with scoring guidance.
