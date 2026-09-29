---
name: organizational-politics
description: "Navigate how decisions actually get made when interests diverge and authority is distributed: map power, interests, and the real decision process; build coalitions and pre-wire; read what the system rewards; model stakeholders from evidence; handle opponents and conflicts; and hold a firm ethical line (politically competent, not political). Use when facing cross-functional conflicts, initiatives needing buy-in from people the user doesn't control, reorgs and power shifts, a 'political' peer or executive, stakeholder analysis, or when the user says 'it's all politics.'"
---

# Organizational Politics

## Purpose

Politics, neutrally defined, is how decisions get made when people want different things and no one has complete authority, which describes every organization. A leader who refuses to understand it gets outmaneuvered or stays invisible; a leader who plays it by manipulation eventually loses the trust that bigger scope requires.

The stance this skill develops: **politically competent, not political.** Understand power, interests, and process precisely; pursue outcomes that serve the company through legitimate means; never deceive, take undeserved credit, or advance by damaging colleagues.

## Use when

- An initiative needs support from people the user doesn't control.
- A cross-functional conflict, or a peer or executive who seems to be "playing politics."
- A reorg, leadership change, or power shift.
- Building a stakeholder model (inside `/analyze-stakeholder`).
- The user says "it's all politics" (often a sign they've stopped analyzing).

## Don't use when

- The situation is a straightforward decision within the user's authority (`decision-making`).

## Standards

Everything this skill produces follows the three exec-core standards. If exec-core isn't loaded, apply them as stated here:
- **Evidence:** separate what happened from inference; label any claim about another person's view or motive as a hypothesis with confidence and a falsifier; never state it as fact.
- **Posture:** when the user's behavior is part of the problem, fix the behavior before the wording.
- **Prose:** answer first, recommendation over options, owners and dates, no filler.

## Core doctrine

1. **Politics is advancing by means other than merit, and systems create it** [Horowitz]. When the user describes a political peer, first ask what the system rewards. If leaders grant exceptions to whoever pushes hardest, expect pushing; read it as incentive, not character.
2. **Performance is only the entry ticket** [Pfeffer]. Deciders' perceptions, relationships, and structural position matter more than most people believe. Don't assume the best argument wins on its own.
3. **Map the decision before arguing it** [Watkins; Grove]. Establish who formally decides, who is consulted, who can veto, and who implements; who influences each of them; what the winning and blocking coalitions are; and what the action-forcing event is.
4. **Pre-wire** [Watkins; Hughes Johnson]. Consequential decisions are rarely made in the meeting. Socialize the proposal one-on-one with opinion leaders first, then persuadables, and meet opponents' interests where possible. "I'll present it and they'll see the logic" is a red flag.
5. **Find the kernel under the position** [Larson]. Executives are often directionally right and specifically wrong. Behind a specific suggestion is a real concern; address the concern rather than debating the suggestion.
6. **Make the idea theirs** [Doshi]. Lead stakeholders to the conclusion with questions, and manage their expectations along with the tasks.
7. **Name conflict openly, with the person first** [Campbell; Scott]. The politically competent move with a peer conflict is to raise it directly with the peer, framed as a shared problem. Flattering to someone's face and criticizing behind their back is the observable signature of a political actor (Scott's manipulative insincerity).
8. **Escalate by co-writing the disagreement** [Hughes Johnson]. A joint escalation, with both sides' case stated fairly, signals organizational leadership, and unilateral lobbying signals its absence.
9. **Break conventions, never integrity rules** [Pfeffer]. "Stay in your lane," "wait your turn," and "don't email the VP" are conventions; sometimes breaking them is right. Honesty with data, security, privacy, AI governance, and fairness to colleagues are integrity rules, and breaking them is never right.
10. **Network position matters** [Pfeffer; Ibarra]. Brokers between groups (research and go-to-market, legal and product, platform and business units) gain influence. Build strategic networks before you need them.
11. **The first team and the skillful politician** [Lencioni]. Peers who are hungry and people-smart but short on humility read as skillful politicians. Arguing for the company over one's own function is the antidote.
12. **Motives are unobservable; incentives aren't** [evidence-discipline]. Build stakeholder models only from what people are measured on, what pressures them, and what they have done.

## The legitimacy filter

Apply to every tactic before recommending it. A tactic that fails any test is out.

- **Transparency:** would the user be comfortable if the other person knew exactly what they were doing and why?
- **Truth:** does it involve any false statement, spun data, or misattributed credit?
- **Harm:** does the user gain by damaging a colleague's standing through deception or exclusion?
- **Reciprocity:** does the other party also get something of value?
- **Rule class:** is the rule being bent a convention or an integrity rule?
- **Reversibility:** if exposed, would the user lose trust they can't rebuild?

Legitimate: pre-wiring, framing a proposal in others' interests, building coalitions, choosing timing, asking directly, trading support, making your work visible, crediting others generously.

Not legitimate: withholding information to disadvantage others, spinning metrics, taking credit, insincere flattery, going around people covertly, undermining a rival, gossip.

## Evidence to gather

- People files for every stakeholder in the decision; their Product Brain `stakeholders/` files.
- Product Brain `knowledge/strategy.md § Tensions`, recent `decisions/`, and blocked decisions.
- Evidence entries of type `reorg` and `decision`.
- How recent conflicts were resolved and who was recently promoted (what the system rewards).

## Reasoning procedure

1. **Define the outcome** the user wants and why it serves the company. If it serves mainly the user, say so.
2. **Map the decision** (`references/power-mapping.md`): decision, decider, consulted, veto, implementers, influencers.
3. **Model each key stakeholder** from evidence (`references/stakeholder-model.md`): accountabilities, pressures, stated vs observed priorities, what they gain or lose, current position (support, oppose, persuadable), who influences them. Load Product Brain stakeholder files and Career Brain people files.
4. **Read what the system rewards:** recent promotions, how past conflicts were resolved, whether exceptions go to whoever pushes.
5. **Design the coalition and sequence:** opinion leaders first, then persuadables; meet opponents' interests; identify the action-forcing event.
6. **Choose techniques per person:** consult, reframe, reshape the choice, bring in an opinion leader, ask for an incremental step.
7. **Run the legitimacy filter** on the plan.
8. **Plan the fallback:** the clean joint escalation if the coalition can't be built.

## Diagnostic questions

- Who decides, who can veto, and who implements (and could quietly fail to)?
- What does each key stakeholder gain or lose if this happens?
- Who influences the decider?
- What has this company rewarded in its last three promotions and last two conflicts?
- What is the action-forcing event?
- Would you be comfortable if every stakeholder knew exactly what you're doing and why?

## Failure modes

- Refusing to engage ("I don't do politics"), which leaves outcomes to people who do.
- Presenting to the group without pre-wiring.
- Explaining an opponent's behavior by character instead of incentives.
- Winning the argument on specifics while leaving the real concern unaddressed.
- Coalitions built on one faction; losing when the faction does.
- Cynicism: "it's all politics" as a reason to stop analyzing or acting.
- Crossing the legitimacy line because a tactic "works."

## Output

```
Outcome sought: <and why it serves the company>.
Decision map: <decider / consulted / veto / implementers>.
Stakeholders: <name; position; interest; what they gain or lose; who influences them; evidence>.
Winning coalition: <...>. Blocking risk: <...>.
Sequence: <1. ... 2. ...>, before <action-forcing event>.
Per-person approach: <technique, and the opening line>.
Legitimacy check: <pass, or what was removed>.
Fallback: <joint escalation plan>.
```

## Tensions in the doctrine

- **Politics as disease vs power as fact.** Horowitz and Campbell treat politics as organizational dysfunction to minimize; Pfeffer treats power as a permanent feature to master. Each is right at its level: Horowitz governs how the user should build their own organization; Pfeffer describes the terrain inside someone else's. In a process-heavy, well-run company, lobbying outside the process backfires; in a politicized one, refusing all non-process moves can leave the user invisible.
- **Candor vs flattery.** Scott calls insincere praise manipulative; Pfeffer's research finds flattery works. Specific, sincere praise gets most of the upside without the corrosion.
- **Vulnerability vs status.** Lencioni asks leaders to show weakness to build trust; Pfeffer cites findings that high-status people who disclose weakness in evaluative settings lose influence. Calibrate by audience: peer team vs evaluators.
- **Coalitions vs team-first.** Watkins' coalition building can look like the politics Campbell disliked. The legitimacy filter is the dividing line.

## Interactions

- `executive-trust` and `managing-up` for the individual relationships.
- `scope-expansion` uses the decision map to see who can grant scope.
- `decision-making` for decision rights and escalation.
- `evidence-discipline` governs every claim about another person's motives.

## References

- `references/power-mapping.md`: decision map, influence map, sources of power, reading what the system rewards, and reorg analysis.
- `references/stakeholder-model.md`: the evidence-based stakeholder model used by `/analyze-stakeholder`.
