---
name: next-level-readiness
description: "Assess readiness for the next level (Director, VP, and beyond) against the company's real ladder and a researched generic model: places the user's operating level by the work they do, analyzes the three passage shifts (skills, time, work values), rates evidence dimension by dimension, screens for transition failure modes, builds the skeptic's case, and designs leap assignments. Use when the user raises promotion questions, 'am I ready?', 'what's my gap?', development planning, level calibration, or when feedback says 'not yet'."
---

# Next-Level Readiness

## Purpose

Readiness is sustained evidence of doing the next level's work, with the next level's time allocation and, above all, the next level's values: finding satisfaction in the work the bigger job requires rather than the work that earned the last promotion. Excellent performance at the current level is a different measure.

This skill answers "am I ready?" honestly, and when the answer is "not yet," names precisely what evidence is missing and how to generate it.

## Use when

- "Am I ready for Director?" / "Why didn't I get promoted?" / "What's my gap?"
- Feedback says "not yet," "more strategic," "more leadership," "more executive presence."
- Planning development for the next 6-18 months.
- Inside `/position-for-promotion`, `/review-my-month`, `/career-retrospective`.

## Don't use when

- The question is how to present an existing case persuasively; that's `executive-communication` after this skill has established what the case actually is.

## Standards

Everything this skill produces follows the three exec-core standards. If exec-core isn't loaded, apply them as stated here:
- **Evidence:** separate what happened from inference; label any claim about another person's view or motive as a hypothesis with confidence and a falsifier; never state it as fact.
- **Posture:** when the user's behavior is part of the problem, fix the behavior before the wording.
- **Prose:** answer first, recommendation over options, owners and dates, no filler.

## Core doctrine

1. **Every promotion is a passage with three shifts: skills, time application, and work values** [Charan]. Values is where people most often fail: the characteristic failure at every passage is continuing to do, and enjoy, the work that earned the last promotion.
2. **Readiness is not performance** [Charan; Hughes Johnson]. A case needs evidence of target-level work already done, over time. Stripe's promotion template asks how long the person has been showing next-level behavior. Duration matters, and a pattern takes more than one heroic quarter.
3. **Map level by the work, not the title** [Charan]. A startup "VP" may be at the first management passage; a big-tech Director may run 60 people. AI orgs often have senior titles with no reports. Place the user by what their reports do (if any), whether they own economics, and whether their peers are in other functions.
4. **The competency trap** [Ibarra]. Doing more of what you're good at crowds out leadership work. For an AI PM the comfort zone is usually deep model work, eval tinkering, detailed specs, being the technical tiebreaker. The fix is substituting outward-facing work, not "blocking time for strategy."
5. **Act your way into the next level** [Ibarra]. People change by doing next-level things first and reflecting afterward. Prescribe actions, then review what happened.
6. **The seven shifts** [Watkins]. Specialist to generalist, analyst to integrator, tactician to strategist, bricklayer to architect, problem solver to agenda setter, warrior to diplomat, supporting cast to lead role. Each is an observable behavior change and can be practiced below the title.
7. **The higher you go, the more your problems are behavioral** [Goldsmith]. Success hides this: people confuse what they succeeded because of with what they succeeded in spite of. Adding too much value, winning too much, and not listening cost more with every level.
8. **The transition is an identity change learned by doing** [Hill]. New leaders discover that authority is really interdependence and that their power rests on credibility. Showing off expertise can undermine credibility as a leader.
9. **Barrels** [Rabois]. Organizations are limited by the number of people who can take an idea from inception to done and bring others with them. Barrel evidence is among the strongest promotion evidence there is.
10. **White-box evaluation** [Horowitz]. Executives are judged on whether they know what to do and can get the organization to do it. Results against targets count for less, since they may be sandbagged or lucky.

## Evidence to gather

- `self/level-model.md` (written and revealed ladder) and `models/readiness.md`.
- Evidence entries tagged `readiness:<dimension>+` or `readiness:<dimension>-`, and feedback entries.
- The last four weeks of calendar, for the time shift.
- The user's latest plan or strategy document, read for what it optimizes.
- Product Brain decisions the user drove.

## Reasoning procedure

1. **Set the target and the model.** Read `self/level-model.md`. Use the company's written ladder and, more importantly, its revealed ladder (what recently promoted people actually did). Where the company model is empty, use the generic model in `references/level-model.md`, and say so.
2. **Place the operating level by the work** using the passage map in `references/level-model.md`. Note mismatches between title and operating level in either direction.
3. **Run the three-shift analysis:**
   - *Skills:* which next-level skills have evidence?
   - *Time:* audit the last four weeks of calendar against the target level's mix (see `managerial-leverage`, `/audit-my-time`).
   - *Values:* ask "Name the three things you're proudest of this quarter. Whose work were they? What did only you contribute?" and read the user's latest plan for what it optimizes (the function, the user's visibility, or the business). Work the values gap first.
4. **Rate each readiness dimension** in `models/readiness.md` from evidence entries:
   - `demonstrated-repeatedly`: two or more grade B/C instances across at least two quarters.
   - `demonstrated-once`: one clear instance.
   - `partial`: some elements present, but incomplete.
   - `absent`: no evidence.
   - `unknown`: not enough data.
   For each: seen by deciders? Gap type (capability, behavior, visibility, opportunity)?
5. **Apply the duration test.** For how many quarters has the user been operating at the next level on each strong dimension, and who has seen it?
6. **Screen transition failure modes** (`references/transition-failures.md`): Charan values failure, Ibarra competency trap, Goldsmith habits, Hill misconceptions, Doshi's "prove I still have it."
7. **Build the skeptic's case.** Run the promotion-committee questions in `references/promotion-evidence.md` as the strongest fair skeptic would. Decide which objections are right.
8. **Design leap assignments** for the top gaps: work that forces next-level behavior and produces grade B/C evidence. Values gaps first, then opportunity gaps (route to `scope-expansion`), then visibility gaps (route to `sponsorship`, `executive-communication`).
9. **Give the verdict** with confidence: ready now; ready in roughly N months if specific things happen; or not on the current path, and why.

## Diagnostic questions

- What did the last three people promoted to your target level do in their final year before promotion?
- For how many quarters have you operated at the next level on each dimension, and who saw it?
- Name the three things you're proudest of this quarter. Whose work were they?
- What work do you find most satisfying, and will the next level still need you to do it?
- What would the strongest fair skeptic say, and would they be right?

## Failure modes

- Rating readiness from the user's self-assessment.
- Counting current-level excellence as next-level evidence (grade A as B).
- Ignoring values: the user can do the next-level work but doesn't want to spend their time on it.
- Using the generic model when the company's revealed ladder says something different.
- "Demonstrate before promotion" as open-ended unpaid stretch that never converts (pair it with sponsorship and explicit criteria).
- A verdict softened to protect the user's feelings.

## Output

```
Verdict: <ready now / ready in ~N months if X / not on current path>, (<confidence>).
Operating level (by the work): <passage>, vs title <title>, vs target <target>.
Three shifts:
- Skills: <evidence and gaps>
- Time: <current mix vs target mix>
- Values: <what the user finds satisfying vs what the next level must value>
Dimensions: <table of ratings, only rows that matter>
The skeptic's strongest objection: <objection>. It is <right / partly right / wrong> because <evidence>.
Leap assignments: <1-3, each tied to a gap and the evidence it produces>
```

## Tensions in the doctrine

- **Act first vs know yourself first.** Ibarra prescribes action before reflection. Hughes Johnson starts from self-awareness and working-with-me documents. Use action to generate evidence and self-knowledge together; use self-awareness work when the user's blind spots are interpersonal.
- **Structured passages vs messy product orgs.** Charan's passages assume management layers; product and AI orgs often have senior specialist roles with no reports. For those targets, assess scope, ambiguity, and business impact rather than people leadership, and say which pipeline the user is on.
- **Climb vs choose your level.** Doshi notes the optics load grows sharply with scope and some people rightly decide it doesn't suit them; Scott's rock-star/superstar distinction says steep growth isn't right for everyone at every moment. Charan and Ibarra assume the climb. The coach asks the user which they want, especially after evidence that the user dislikes the next level's work.
- **Demonstrate first vs get the title first.** Stripe-style readiness-by-duration versus the risk of doing the job unpaid indefinitely. Resolve with explicit criteria agreed with the manager and at least one sponsor.

## Interactions

- `trajectory-model` stores the readiness ledger; `attribution-analysis` explains gaps; `scope-expansion` supplies opportunity for missing dimensions; `sponsorship` and `executive-communication` handle visibility; `managerial-leverage` covers time allocation.

## References

- `references/level-model.md`: passage map for product orgs; generic dimension-by-level expectations (Senior PM to CPO).
- `references/promotion-evidence.md`: evidence standard, the skeptic's questions, how to structure a case.
- `references/transition-failures.md`: failure modes by passage, the seven shifts as behaviors, the habits that get worse with seniority.
