---
name: executive-trust
description: "Model and grow the specific trust each senior leader extends to the user, from trust with information up through trust with judgment, decisions, people, ambiguity, and representing the company. Decomposes trust into credibility, reliability, intimacy (safety), and self-orientation; audits commitments, candor, loyalty, and discretion with evidence; identifies the next tier and the behavior that earns it. Use when an executive seems not to trust the user, before asking for scope, after a trust-damaging event, or when the user asks how to earn a senior leader's confidence."
---

# Executive Trust

## Purpose

Scope follows trust. Before a senior leader hands someone ambiguity, people, money, or risk, they have to believe that person will use it the way they would, or better. This skill makes that belief diagnosable: which kind of trust does a given executive already extend, which kind comes next, and what behavior would earn it.

## Use when

- "My VP doesn't trust me" / "I'm being micromanaged."
- Before asking an executive for scope, a role, or a big decision.
- After a trust-damaging event: a missed date, a surprise, a conflict.
- Preparing to work with a new senior leader.

## Don't use when

- The issue is the relationship with the direct manager as a system (use `managing-up`, which uses this skill's model).

## The trust tiers

Trust is extended in escalating tiers. Each is revealed by what the executive does, not says.

| Tier | The executive trusts you with | Revealed by |
|---|---|---|
| 1. Information | Hearing the real status, including bad news, early | They rely on your updates without checking elsewhere |
| 2. Judgment | Your opinion on things that matter | They ask what you think, including outside your scope |
| 3. Decisions | Making calls without them | They stop asking to review; they back your calls publicly |
| 4. People | Leading others | They give you a team, or route people to you |
| 5. Ambiguity and risk | Undefined, high-stakes problems | "Figure out what we should do about X" |
| 6. Representation | Speaking for them or the company | They send you to customers, peers' staff, the board |

The tiers are this system's synthesis; the behaviors that earn each one come from the doctrine below. The central question of the whole system is a question about tiers: what would move each important executive one tier up?

## Standards

Everything this skill produces follows the three exec-core standards. If exec-core isn't loaded, apply them as stated here:
- **Evidence:** separate what happened from inference; label any claim about another person's view or motive as a hypothesis with confidence and a falsifier; never state it as fact.
- **Posture:** when the user's behavior is part of the problem, fix the behavior before the wording.
- **Prose:** answer first, recommendation over options, owners and dates, no filler.

## Core doctrine

1. **Trust is built from specific, checkable behaviors** [Campbell]. They include keeping your word, loyalty (what you say about them when they're absent), integrity (no gap between reported and known status), discretion, candor delivered with care, and visibly putting the team first.
2. **Trust decomposes into credibility, reliability, intimacy, and self-orientation** [Maister]. Credibility is about your words; reliability, your actions over time; intimacy (in Maister's sense, safety), whether they can bring you hard things; self-orientation, whether you seem to be working your own angle. Self-orientation divides everything else, which makes it the specific risk for an ambitious PM.
3. **Dependability and honesty determine how much can be delegated** [Gabarro & Kotter]. Slipped commitments and softened status reports directly block scope. Re-baseline the moment a date is at risk.
4. **Latitude is information** [McCord]. Less discretion than peers (more check-ins, more approvals) is evidence about how the user's judgment is perceived. Ask which past decision created the doubt.
5. **Coachability is the first test** [Campbell]. Executives watch whether feedback visibly changes behavior within weeks, and whether the person reports back.
6. **No surprises; show your reasoning** [Cagan's pledge to executives; Bezos, Earn Trust]. Preview anything risky before it lands, bring evidence when you disagree, and own the outcome.
7. **Voice, then commit** [Campbell; Grove; Bezos]. Argue fully before a decision, commit publicly after, never relitigate outside the room. Few behaviors earn trust from above faster.
8. **Vulnerability-based trust, calibrated** [Lencioni vs Pfeffer]. Admitting mistakes first builds peer trust on stable teams; in evaluative or first-impression settings, disclosed weakness can cost influence. Calibrate by audience.
9. **Candor measured at the listener's ear** [Scott]. The user saying "I was direct but kind" is not evidence. What did the executive do next?
10. **Bad news early and unspun** [McCord; Slootman; Campbell]. The first time an executive discovers shaded bad news, trust resets.

## Evidence to gather

- `people/<slug>.md`: trust signals, friction, open loops.
- Evidence entries naming them (grep `evidence/LOG.md` by slug), especially types `allocation` and `feedback`, and meeting debriefs with them.
- Their rows in `models/reputation.md` and `models/sponsorship.md`.
- The user's recent commitments to this person and whether each was kept.
- Their Product Brain `stakeholders/<slug>.md` for what they want from the product.

## Reasoning procedure

1. **Pick the executive.** Load their `people/` file, reputation hypotheses, and the last 90 days of evidence naming them.
2. **Place the current tier** from revealed behavior. Cite evidence per tier. If evidence is thin, say the tier is unknown.
3. **Run the trust audit** (`references/trust-audit.md`): word, loyalty, integrity, discretion, candor, team-first, plus the four trust-equation components.
4. **Find the weakest component** with evidence. That's usually what blocks the next tier.
5. **Check the alternative explanation** (`evidence-discipline`): is the "distrust" actually the executive's style, workload, their own boss's pressure, or a structural reason (a reorg pending, a peer's territory)?
6. **Name the next tier and the behavior that earns it.** Usually small and repeated: a run of kept commitments, one well-handled piece of bad news, a recommendation that costs the user's own area, one decision the executive watches the user make well.
7. **If trust was damaged,** plan the repair: own it fully and specifically, say what changes, then demonstrate over several interactions. Don't ask for scope during repair.

## Diagnostic questions

- What has this executive given you in the last 90 days: information, requests for your opinion, decisions left to you, people, undefined problems, rooms? What have they stopped giving you?
- When did you last bring them bad news before they heard it elsewhere?
- Which commitment to them did you last renegotiate or miss?
- What have you said about them when they weren't there?
- When did you last recommend something that cost your own area?

## Failure modes

- Asking for scope from an executive who hasn't yet extended trust with judgment.
- Treating warmth as trust. Friendly executives who never delegate have not extended trust.
- Softening status to protect the relationship (it destroys the relationship).
- Relitigating decisions in hallways or in front of one's own team.
- Visible self-orientation: recommendations that conveniently expand the user's scope; talking about career in business settings.
- Over-apologizing after a mistake instead of owning it and fixing it (reads as low confidence).

## Output

```
<Executive>: currently extends trust with <tier(s)>, (<confidence>). Evidence: <revealed behavior>.
Weakest component: <component>. Evidence: <...>.
Alternative explanation: <and how to tell>.
Next tier: <tier>. What earns it: <specific behaviors, repeated over <timeframe>>.
This week: <one concrete move>.
Don't: <the tempting move that would cost trust>.
```

## Tensions in the doctrine

- **Trust-first vs power-first.** Campbell, Maister, and Lencioni say trust is earned through integrity, loyalty, and putting the team first. Pfeffer's research says being liked and being good are overrated for advancement; visibility and power matter more. Both describe real mechanisms: Pfeffer's tactics can win promotion while lowering the specific trust that gets someone handed ambiguity. This skill optimizes for trust, and `organizational-politics` handles power, with a legitimacy filter.
- **Full support vs disagree and commit.** Grove asks for full support after a decision; Bezos's disagree-and-commit explicitly lets dissent remain on record. Both forbid relitigating.
- **Candor upward.** Scott advocates it, carefully sequenced; Pfeffer finds that making superiors feel good about themselves works, so criticism that embarrasses them is costly. Test with a small, private, specific item first and watch the reaction.

## Interactions

- `managing-up` applies this model to the manager relationship specifically.
- `sponsorship` requires trust at tier 2 or higher; nobody sponsors someone they don't trust with judgment.
- `trajectory-model` records trust signals; `evidence-discipline` governs how perception of trust is inferred.

## References

- `references/trust-audit.md`: the per-executive audit, the trust-equation diagnosis, repair protocol, and coachability check.
