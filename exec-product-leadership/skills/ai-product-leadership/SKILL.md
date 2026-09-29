---
name: ai-product-leadership
description: "Coach the user to operate as the organization's credible AI product executive: mapping capability task by task (the jagged frontier), evaluation as the governance mechanism for probabilistic systems, AI unit economics and margin, risk tiers and launch gates, portfolio lanes instead of feature dates, build/buy/partner, moats, and organizational adoption. Use when the user presents or reviews an AI strategy, initiative, launch, budget, vendor choice, or quality problem to executives or a board; when executives ask for 'our AI strategy'; or when positioning AI expertise as a route to larger scope."
---

# AI Product Leadership

## Purpose

For an AI PM, the fastest legitimate route to executive scope is becoming the person the executive team trusts on AI: the one who can tell capability from hype, make the economics legible to a CFO, turn quality in a probabilistic system into something governable, and allocate bets whose feasibility is uncertain. Few people in most companies can do all of that, and distinctive value is what sponsors look for.

The same expertise can become a trap: executives will happily consult the AI expert forever without giving them an organization. This skill develops the executive version of AI expertise: judgment, governance, economics, and portfolio, delivered in the posture of an owner rather than an advisor.

Claims in this field date quickly. The underlying sources carry dates; check them before relying on any number.

## Use when

- Presenting or reviewing an AI strategy, initiative, launch, budget, vendor, or quality problem for executives.
- An executive asks for "our AI strategy," or proposes "use AI for X" after a demo.
- Finance challenges inference cost or AI margins.
- The user wants to expand scope through AI (platform, evaluation, governance, adoption).
- The board or leadership asks about AI risk.

## Don't use when

- Hands-on AI craft (prompting, model tuning, pipeline design), which belongs to product or engineering.
- General product leadership questions without an AI dimension (use `product-leadership`).

## Standards

Everything this skill produces follows the three exec-core standards. If exec-core isn't loaded, apply them as stated here:
- **Evidence:** separate what happened from inference; label any claim about another person's view or motive as a hypothesis with confidence and a falsifier; never state it as fact.
- **Posture:** when the user's behavior is part of the problem, fix the behavior before the wording.
- **Prose:** answer first, recommendation over options, owners and dates, no filler.

## Core doctrine

1. **The frontier is jagged; map it task by task** [Mollick; Dell'Acqua et al. 2023]. AI performance varies sharply across tasks that look similar. A demo on one task says little about the next. The executive contribution is a task-level capability map built on the company's own cases.
2. **Evaluation is the governance mechanism** [Husain, Shankar, Yan; Ng]. Stalled AI products usually lack an evaluation system, and a better model won't supply one. Leaders should expect error analysis on real traces, failure-mode taxonomies with frequencies, binary judgments tied to named failure modes, automated judges validated against a domain owner, and one accountable owner of "good." Generic scores ("quality 4.2/5") are not governance.
3. **Criteria drift is learning, not scope creep** [Shankar 2024]. Good can't be fully specified before seeing outputs. Propose an initial criteria set plus a scheduled revision after the first error-analysis cycle, and explain why to executives up front.
4. **Plan in lanes with triggers, not feature dates** [ai-product-operators; evals practitioners]. Committed outcomes on proven capability get dates. Capability-gated bets get eval thresholds that trigger investment. Frontier probes get small time boxes and re-tests on each major model release. Commit to dates only for decisions and scoped capability levels.
5. **AI margins are lower and more variable than SaaS; show them** [Casado & Bornstein, a16z 2020, with later cross-checks]. Every AI feature needs cost per task, cost per active user, and margin impact. For AI bundled into an existing product, the number finance cares about is dilution of blended margin. Build cost models from three trends: price per unit of capability (falling fast), tokens per task (rising with agents, retrieval, and reasoning), and tasks per user.
6. **Services creep and the long tail are real costs** [a16z]. Human review and customer-specific tuning belong in the P&L and in pricing, with a dated plan for what gets automated.
7. **AI is not the moat** [a16z; Ng]. For every "our data is our moat" claim: does quality keep rising with more of this data, who else could get it, how fast does it go stale, and what happens when the next foundation model does the task out of the box?
8. **Risk appetite is an executive decision** [evals practitioners; Ng]. Assign each AI use case a risk tier with its own eval bar, launch gate, and monitoring. Two-tier governance (light for sandboxes, real gates for production) lets speed and safety coexist. Escalate the tier choice to an executive explicitly so no team ends up making it by default.
9. **The first AI projects must succeed, not be the biggest** [Ng]. Build credibility with a ladder of internal customers; each win is the reference for the next. Strategy follows experience: an AI strategy without shipped evidence should be written as explicit hypotheses with dates to revisit.
10. **Own the capability, not one more feature** [Ng]. Cross-cutting assets (evaluation infrastructure, model gateway, data standards, AI hiring bars, adoption programs) are legitimate scope expansion.
11. **Measure outcomes against a baseline** [MIT NANDA 2025, self-reported sample; METR 2025]. Pilot counts are a warning sign. People misjudge AI's effect on their own work, so productivity claims need a measured baseline before they reach executives.
12. **Build/buy/partner is a moving economic decision** [a16z; NANDA; Ng]. Compare total cost (including evals, monitoring, maintenance, people), time to value, differentiation, and switching cost. The eval suite is what makes switching models cheap and safe. Revisit when prices or model quality move.

## Evidence to gather

- Product Brain eval results and quality data, metrics, cost data, and decisions on models and vendors.
- Risk reviews and incidents.
- What each executive involved has said about AI, dated (people files).
- The company's stated AI strategy and where budget is actually going.

## Reasoning procedure

1. **Classify the ask:** capability claim, investment decision, launch decision, strategy request, cost challenge, vendor choice, adoption program, or risk question.
2. **Load reality:** from the Product Brain, the current evals (if any), metrics, cost data, decisions, and the stakeholders' stated concerns; from the Career Brain, what each executive involved has said about AI (hype, fear, skepticism), with dates.
3. **Run the relevant checks** from `references/ai-exec-toolkit.md`: capability map, eval maturity level, launch gate, cost model, moat questions, build/buy/partner table, risk tier, portfolio lanes.
4. **Decide the recommendation.** Make the call the user's scope allows; escalate risk-appetite and investment decisions with a recommendation.
5. **Translate for executives** (below). Answer first; probability expressed as a managed quantity; the decision needed.
6. **Find the leadership move:** is there a cross-cutting capability, governance design, or literacy gap the user could own? Route it to `scope-expansion`.

## Communicating probabilistic systems to executives

Executives are used to software that either works or doesn't. Make AI read as *managed*.

- Lead with the decision and the risk tier.
- Replace "accuracy is 94%" with "on our own cases, it fails in three ways; here is how often each happens now, what we're doing about the worst one, and what we won't ship until it's under X."
- Name what is committed, what is gated on a capability threshold, and what is exploratory, and make a different promise for each.
- Put cost per task and margin impact on the same page as quality.
- Say what would make you stop.
- Separate the industry hype debate (not the user's call) from this bet's unit economics (the user's call). Neither hype nor bubble talk is an argument.

## Diagnostic questions

- Setting the demo aside, what does the capability look like on your own cases?
- What's the eval maturity level, and who owns the definition of "good"?
- What does one task cost, and what does that do to margin?
- What's the risk tier, and who signed it?
- Which commitments depend on capability you haven't proven?
- What would make you stop?

## Failure modes

- **Expert trap:** answering AI questions brilliantly and never owning an AI outcome, budget, or organization.
- **Hype amplification:** promising dates or ROI on capabilities the evals don't support.
- **Reflexive caution:** blocking without offering a governed path to yes, which reads as low enterprise judgment.
- **Vanity metrics:** pilot counts, usage without outcomes, generic quality scores.
- **Margin blindness:** presenting AI revenue or adoption without cost to serve.
- **Model obsession:** debating vendors when the eval system is the actual gap.
- **Feature collecting:** accumulating AI features without owning the capability underneath them.

## Output

For a reviewed AI initiative or strategy:

```
Verdict: <the executive-level read in one or two sentences>.
Capability: <what's proven on our cases, what's gated, what's speculative>.
Quality governance: <eval maturity level, gate status, owner of "good">.
Economics: <cost per task, margin impact, the trend that could break it>.
Risk: <tier, the decision leadership must own>.
Recommendation: <the call, and what would reverse it>.
Leadership move for you: <the capability or governance the user could own>.
```

## Tensions in the doctrine

- **Speed vs rigor.** Frontier labs ship early and iterate in public; enterprise evaluation practice argues for gates. Resolve it by risk tier: sandbox fast, gate production.
- **Central unit vs line ownership.** Ng recommends a central AI team lending capability to business units. The NANDA findings (small, self-reported sample) suggest buying and giving ownership to line managers reaches deployment more often. Match to the company's AI maturity and talent.
- **When to care about cost.** Ng warns against optimizing token cost prematurely; a16z argues margin discipline from the start. Follow Ng early in discovery and a16z once a feature has users and a price.
- **Broad experimentation vs narrow domains.** Mollick favors widespread experimentation to find the frontier; a16z favors narrow problem domains for economics. The two fit different stages of the same portfolio.

## Interactions

- `product-leadership` provides the general leadership model this applies to AI.
- `enterprise-thinking` for the company-level economics and strategy frame.
- `executive-communication` (board-altitude mode) for AI risk and strategy at board level.
- `scope-expansion` for turning a capability gap into owned scope.
- `decision-making` for reversibility and risk-appetite decisions.

## References

- `references/ai-exec-toolkit.md`: eval maturity ladder, launch gate, monthly AI quality review, date-to-funnel translation, cost model, moat questions, build/buy/partner table, risk tiers, capability map template.
- Source dossiers (via `exec-core:doctrine-library`): andrew-ng, ai-economics-a16z, ai-evals-practitioners, ai-product-operators, marty-cagan.
