---
name: attribution-analysis
description: "Diagnose the cause behind a career outcome or a stalled trajectory: capability gap, behavior/posture gap, visibility gap, attribution gap, perception lag, sponsorship gap, opportunity gap, context, fit, or genuine unreadiness. Generates competing explanations, names the evidence that discriminates between them, and matches the intervention to the cause. Use when analyzing a promotion miss, surprising feedback, a lost opportunity, a win that didn't change anything, or when the user asks 'why isn't this working?' or 'why did that happen?'"
---

# Attribution Analysis

## Purpose

The most expensive mistake in career development is applying the right fix to the wrong cause. Visibility tactics aimed at a capability gap produce executive theater, more hard work on a visibility gap leads to burnout and resentment, and waiting out a sponsorship gap can cost years.

This skill decides which cause is actually binding, with honest confidence, before anyone prescribes anything.

## Use when

- A promotion or opportunity went to someone else, or didn't happen.
- Feedback surprised the user.
- A clear win didn't change how the user is treated.
- The user feels stuck and has a theory about why.
- A monthly review shows a ledger that isn't moving.

## Don't use when

- The situation is a single low-stakes interaction; record it and wait for a pattern.

## The cause classes

| Cause | What it means | Typical discriminating evidence |
|---|---|---|
| **Capability gap** | The user can't yet do what the next level requires | Attempted it and fell short; consistent feedback from independent sources; no instance of doing it well |
| **Behavior / posture gap** | The user can do it but defaults to current-level behavior, especially under pressure | Instances of doing it, but only in low-stakes settings; posture leaks in communications |
| **Visibility gap** | The user does it; the deciders haven't seen it | Strong grade B evidence; visibility map shows deciders lack direct exposure |
| **Attribution gap** | Deciders saw the work but credit it to the manager, the team, or a peer | Work described by others without the user's name; the manager presents the user's work upward |
| **Perception lag** | Reputation was formed on older evidence and hasn't updated | Feedback cites events from long ago; recent evidence contradicts it; the person hasn't seen the recent work |
| **Sponsorship gap** | Nobody with power is spending capital on the user | No dated acts of advocacy above the manager; the user isn't discussed when roles open |
| **Opportunity gap** | The current role offers no chance to demonstrate the next-level dimension | No B-grade opportunities in the scope ledger; the dimension is structurally out of reach (no reports, no budget) |
| **Context / structural** | Company circumstances: freeze, reorg, the manager's own standing, a level cap in this org | Peers also stalled; allocation frozen broadly; the manager hasn't been promoted in years |
| **Fit / values** | The organization rewards something different from what the user optimizes for | Promoted people show a different profile (revealed ladder); the user's strengths are low-status here |
| **Genuine unreadiness** | Ambition is ahead of readiness, and the organization's judgment is broadly correct | Multiple independent sources agree; the gaps are real in the readiness ledger |

Causes usually combine, so the job is to find the *binding* one: the cause whose removal would change the outcome.

## Standards

Everything this skill produces follows the three exec-core standards. If exec-core isn't loaded, apply them as stated here:
- **Evidence:** separate what happened from inference; label any claim about another person's view or motive as a hypothesis with confidence and a falsifier; never state it as fact.
- **Posture:** when the user's behavior is part of the problem, fix the behavior before the wording.
- **Prose:** answer first, recommendation over options, owners and dates, no filler.

## Doctrine basis

The ten cause classes and the intervention table are this system's synthesis. The sources behind them:

- Sort a stall into capability, visibility to the deciders, relationship with them, or context before prescribing more output [Pfeffer].
- Separate capability, visibility, perception or bias, and context; some attribution problems are structural [Ibarra].
- Sponsorship skews toward people like the sponsor [Hewlett].
- The higher you go, the more problems are behavioral, and perception lags behavior change [Goldsmith].
- Surprise at review time usually means withheld feedback [Scott].
- Don't judge an approach by one outcome [Duke].

## Evidence to gather

- `models/readiness.md`, `models/visibility.md`, `models/sponsorship.md`, `models/reputation.md`.
- Feedback entries across sources and time (grep `evidence/LOG.md` for type `feedback`).
- `self/level-model.md § Revealed ladder`, and the scope ledger.
- Observable scope changes of two or three peers over the same period (for the context check).
- The documentation of the outcome itself: announcement, decision, calibration result.

## Reasoning procedure

1. **State the outcome precisely.** Not "I'm not being taken seriously" but "the Director role on the AI platform went to an external hire on 2026-08-15."
2. **List every plausible cause class,** including the uncomfortable ones (genuine unreadiness, fit) and the ones outside the user's control (context).
3. **For each, name the discriminating evidence:** what would be true if this were the cause and false otherwise. Use `references/cause-classes.md`.
4. **Check the Career Brain** for that evidence: readiness ledger ratings, visibility map, sponsorship map, feedback history, the revealed ladder in `self/level-model.md`.
5. **Weigh.** Apply `evidence-discipline`: independent sources, allocation over praise, longitudinal over single events. Run the counter-questions in exec-core `evidence-discipline/references/bias-checks.md`. Test the error in both directions: some users blame visibility and politics to avoid a capability verdict; others (often strong AI PMs) believe the work will speak for itself and under-weight visibility and sponsorship.
6. **Name the binding cause** with confidence, and the runner-up.
7. **Match the intervention** to the cause (table below). Say explicitly which popular interventions would be wrong here.
8. **Design the cheapest discriminating test** when confidence is low: an action whose result would tell you which cause it is.

## Intervention matching

| Binding cause | Right intervention | Wrong intervention (common) |
|---|---|---|
| Capability | Deliberate stretch with feedback; a smaller-stakes place to practice; learning from someone who does it well | Visibility campaigns (exposes the gap to more people) |
| Behavior / posture | Name the specific leak; practice in the next three high-stakes moments; debrief each | More training on what the user already knows |
| Visibility | Change channels: present your own work, write the doc that travels, ask the manager to bring you into their forums | Working harder on the same work |
| Attribution | Name your work in writing; present rather than hand off; agree with the manager on how credit travels | Complaining about credit; claiming team work as individual |
| Perception lag | Create a new, unmistakable data point in front of the same person; then an explicit "reset" conversation about how they see you now | Assuming the new evidence will be noticed on its own |
| Sponsorship | Solve a problem for a person with power; make your ambitions explicit to them; widen beyond one chain | Asking for sponsorship before having delivered anything for the person |
| Opportunity | Find or create scope that contains the missing dimension (`scope-expansion`); or change roles | Waiting for the role to evolve |
| Context | Decide whether to wait, move internally, or leave; protect optionality | Personalizing it; overworking to beat a freeze |
| Fit | Decide whether to adapt to what this organization rewards or find one that rewards your strengths | Pretending the mismatch will resolve |
| Genuine unreadiness | Accept it, build the gap deliberately, and set a realistic timeline | Politicking for a promotion the user would fail in |

## Diagnostic questions

- What exactly happened, and when?
- Who decided, and what had they seen of your work?
- What would be true if this were a capability gap, and false otherwise? Same question for visibility and sponsorship.
- Did peers stall too?
- What did the last people promoted have that you don't?
- What would your harshest fair critic say caused it?

## Failure modes

- Choosing the least painful cause instead of the best-supported one.
- Treating a single decider's view as the organization's.
- Ignoring context: sometimes nothing the user did caused it.
- Over-owning: attributing structural outcomes to personal failings, which also reads as poor judgment.
- Stopping at diagnosis without a test or a move.

## Output

```
Outcome: <precise>.
Binding cause: <class>, (hypothesis, <confidence>). Why: <discriminating evidence>.
Runner-up: <class>. What would make it the binding one: <evidence>.
Ruled out or unlikely: <classes, one line each>.
What to do: <intervention matched to the cause>.
What not to do: <the tempting wrong intervention>.
Test: <cheapest action that would discriminate, if confidence is low>.
```

## Tensions in the doctrine

- **Pfeffer vs the meritocratic sources** on how much performance explains outcomes. This skill leaves the general question open and asks which cause the evidence supports in this case.
- **Scott vs Pfeffer on candor upward** matters for the perception-lag intervention: an explicit reset conversation is Scott-consistent; Pfeffer's emphasis on how superiors feel about themselves argues for framing the conversation around their goals and leaving their earlier judgment of the user out of it. Match to the person's documented behavior in the Brain.
- **Duke's "resulting"** applies to the user's own analysis: a lost promotion doesn't prove the user's approach was wrong, and a won one doesn't prove it was right.

## Interactions

- Consumes `trajectory-model` ledgers and `next-level-readiness` ratings.
- Hands off to `scope-expansion` (opportunity gaps), `sponsorship` (sponsorship gaps), `executive-communication` and `meeting-presence` (visibility and attribution gaps), `executive-posture` (behavior gaps).

## References

- `references/cause-classes.md`: discriminating questions and tests for each cause class, with worked examples.
