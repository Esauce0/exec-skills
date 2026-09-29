---
name: product-leadership
description: "Coach the shift from managing a product to leading product capability: strategic context as the leader's main output, diagnosing team type before prescribing, strategy as focus/insight/action/management, coaching and staffing, topology before process, editing instead of doing, and building product-leadership evidence before having reports. Use when the user asks how to act like a product leader, reviews their area's strategy or roadmap, takes on PMs or a larger area, complains that teams aren't empowered, or needs Director-level product evidence."
---

# Product Leadership

## Purpose

A product leader makes it likely that *other people* make good product decisions, repeatedly, without the leader in the room. That shift, from deciding to creating the conditions for good decisions, is the core of the Director transition in product, and most PMs underestimate how different the work is.

This skill diagnoses where the user's product leadership actually stands, and what evidence of it they can build now, including before they have reports.

## Use when

- The user is moving from owning a product to owning an area, or wants to.
- Reviewing the user's area strategy, roadmap, or planning approach.
- "My team isn't empowered," "leadership just wants dates," "my PMs are weak."
- The user takes on PMs (direct, dotted-line, or as a mentor).
- Building product-leadership evidence for a Director case.

## Don't use when

- The question is craft-level product work on one feature (use pm-skills or product-level skills).
- The question is purely about AI strategy (use `ai-product-leadership`, which applies this skill's model to AI).

## Standards

Everything this skill produces follows the three exec-core standards. If exec-core isn't loaded, apply them as stated here:
- **Evidence:** separate what happened from inference; label any claim about another person's view or motive as a hypothesis with confidence and a falsifier; never state it as fact.
- **Posture:** when the user's behavior is part of the problem, fix the behavior before the wording.
- **Prose:** answer first, recommendation over options, owners and dates, no filler.

## Core doctrine

1. **The leader's primary output is strategic context, not a roadmap** [Cagan]. Mission, scorecard, company objectives, product vision and principles, product strategy, team topology, and team objectives. Test: could a PM on your teams make a disputed prioritization call using only what is written down? A Director candidate whose artifacts are all roadmaps and status decks reads as operating at PM level.
2. **Diagnose the team type before prescribing** [Cagan]. Delivery teams, feature teams, and empowered product teams need different advice. Arguing for outcomes and refusing dates inside a feature-team company backfires; the move there is to earn one problem-shaped assignment and deliver it.
3. **Ownership is proportional to credibility** [Cagan]. "Leadership won't empower us" is usually a credibility gap wearing a complaint. Convert every complaint into the credibility action that would earn the ownership.
4. **Strategy is focus, insight, action, and active management** [Cagan; stress-tested with Rumelt's kernel]. More than three or four top priorities is a focus failure. Each priority needs an insight (data, customer learning, technology shift) that makes it pivotal and an owning team with an objective, and the leader needs a weekly mechanism that surfaces stalls.
5. **Most execution problems are strategy, interpersonal, or culture problems** [Doshi]. The tell is a process fix that keeps failing. Chronic busyness at senior levels usually traces back to missing or unagreed strategy.
6. **Coaching and staffing are the management job** [Cagan; Horowitz]. A new leader still acting as the best PM on the team is a transition risk. Promotion evidence for product leadership includes people developed as well as products shipped.
7. **Editing replaces doing** [Doshi; Rabois]. The leader's quality shows in the questions they ask in their teams' reviews. The failure pattern is "prove I still have it": rewriting PRDs, dominating reviews, jumping into execution.
8. **Topology before process** [Cagan; Horowitz]. Chronic cross-team dependency pain is usually teams drawn around org-chart history instead of problems they can own end to end. Every org design is a tradeoff between communication paths, so design for the decisions teams need to make.
9. **Take written positions** [Horowitz; Amazon]. Disagreement voiced only verbally or after the fact leaves no evidence of judgment. Written positions on contested decisions are both leadership and evidence.
10. **Keep high-integrity commitments** [Cagan]. Refusing dates on principle loses trust. Commit rarely, after enough discovery to commit responsibly, then deliver.

## Evidence to gather

- Product Brain strategy, roadmap, features, and decisions, including who authored each.
- Product Brain org and team files; `self/current-role.md` for PMs led or influenced.
- `models/readiness.md` (leverage and strategic contribution).
- The calendar, for leader time allocation.

## Reasoning procedure

1. **Establish the user's footprint.** From the Career Brain (`self/current-role.md`, scope ledger) and the Product Brains: which teams, PMs, and products does the user own, influence, or advise? Which strategic context artifacts exist, and who wrote them?
2. **Classify the teams** the user leads or influences (team-type diagnostic in `references/leadership-audits.md`). Base the advice on the column the team actually falls in, whatever the company says about itself.
3. **Audit strategic context.** For each element: exists in writing, owner, last updated, can PMs cite it. Sort gaps into those inside the user's authority to fill (Director-level leverage, do them) and those above it (managing-up agenda items).
4. **Check the strategy** with focus, insight, action, management. Stress the diagnosis with Rumelt's kernel: is the challenge named, is there a guiding policy, are the actions coherent?
5. **Audit the user's leader time** if they lead people: coaching and staffing vs delivery meetings.
6. **Find the bridge evidence** if the user has no reports. Product leadership can be demonstrated without a team (see below).
7. **Prescribe** the smallest set of moves that produces grade B or C evidence (per `trajectory-model`) of product leadership.

## Demonstrating product leadership without reports

Grove counted influential individual contributors as managers because their output is the output of the people they influence. For a PM, the evidence that transfers to a Director case:

- **Authoring strategic context others use:** an area strategy, product principles, or an AI quality bar that other teams cite in their own docs.
- **Raising the quality of others' decisions:** running or anchoring product reviews; being the person other PMs seek out before a hard call.
- **Coaching:** a structured coaching relationship with one or two PMs, with visible growth.
- **Owning a cross-team objective:** one outcome that requires several teams, with the user accountable.
- **Topology proposals:** a well-argued proposal to redraw team boundaries around problems, pre-wired with the affected leaders.

Each should be recorded as evidence entries with `readiness:leverage-through-others` or `readiness:strategic-contribution` tags.

## Diagnostic questions

- Could a PM on your teams make a disputed call using only what's written down?
- How many top priorities does your area have, and what's the insight behind each?
- What obstacle did you remove from a team's path last month?
- Which PMs outside your reporting line come to you before a hard call?
- Which of your artifacts do other teams cite?

## Failure modes

- **Roadmap manager:** the area's direction exists only as a list of features with dates.
- **Best PM on the team:** the leader makes the product calls their PMs should make.
- **Empowerment theater:** complaining about lack of empowerment without doing the work to earn it.
- **Priority sprawl:** eight top priorities, each justified by a stakeholder request.
- **Imported rhetoric:** applying empowered-team language in a feature-team company without the credibility to back it.
- **Bigger-PM confusion:** treating "product leadership" as managing a larger product rather than building others' capability.

## Output

```
Product leadership read: <where the user's leadership footprint stands, one or two sentences, with confidence>.
Team context: <team types, with evidence>.
Strategic context gaps: <inside your authority> / <above it>.
Strategy check: <focus, insight, action, management: what fails>.
Leadership evidence you have: <grade B/C items>.
Moves: <2-3, each producing product-leadership evidence>.
```

## Tensions in the doctrine

- **Empowerment vs command.** Cagan: leaders give context and problems, teams choose solutions, and discovery evidence settles disputes. Horowitz: in wartime the leader intervenes in details and doesn't seek dissent. Ask which mode the user's company and area are in before advising; empowerment rhetoric in a real crisis reads as abdication.
- **PM as peer vs PM as "CEO of the product."** Cagan's PM is nobody's boss; Horowitz's Netscape-era PM takes charge. Horowitz's version fits small, founder-driven teams; Cagan's fits larger organizations with strong design and engineering leads.
- **Coaching vs talent density.** Cagan puts coaching at the center of the manager's job. McCord puts more weight on hiring great people and being honest when they no longer fit. McCord fits high-talent-density firms that pay top of market; Cagan fits companies building capability from the people they have.
- **Anti-roadmap vs operating cadence.** Hughes Johnson and Larson give more weight to planning rituals and goal systems than Cagan's rhetoric suggests. In a company with a heavy operating cadence, put Cagan's content inside the cadence.

## Interactions

- `ai-product-leadership` applies this model to AI capability specifically.
- `managerial-leverage` covers delegation, time allocation, and operating cadence in depth.
- `next-level-readiness` scores the evidence this skill helps produce.
- `executive-trust` covers the credibility side (Cagan's pledge to executives maps to its trust ledger).
- `/review-product-altitude` runs this skill against a specific artifact.

## References

- `references/leadership-audits.md`: team-type diagnostic, strategic context audit, strategy check, leader time audit, PM coaching grid, and the complaint-to-credibility conversion table.
- Source dossiers (via `exec-core:doctrine-library`): marty-cagan, shreyas-doshi, ben-horowitz, claire-hughes-johnson, richard-rumelt.
