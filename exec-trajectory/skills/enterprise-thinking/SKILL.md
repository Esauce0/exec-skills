---
name: enterprise-thinking
description: "Reason at company level rather than product level: the business's economics (cash, margin, velocity, return, growth, customers), the company's binding constraint, strategy as diagnosis/guiding policy/coherent action, cross-functional tradeoffs, and the peer leadership team as the first team. Translates product questions and proposals into terms a CEO and CFO act on. Use when framing a proposal or bet for executives, when feedback says 'think more strategically' or 'broader', when evaluating tradeoffs across teams or functions, or when the user can't explain how their work moves the company."
---

# Enterprise Thinking

## Purpose

Most PMs think about their product very well and about the company only occasionally, while executives start with the company and consider any one product in relation to it. The gap between those two habits is what feedback like "needs to be more strategic" or "needs a broader view" is usually pointing at.

This skill builds the habit: every product question gets restated as a company question, and every proposal carries its effect on the business in the language executives use to make decisions.

## Use when

- Framing a proposal, bet, investment, or tradeoff for executives.
- Feedback mentions strategy, breadth, business acumen, or "thinking like an owner."
- A tradeoff crosses teams or functions.
- The user can't say how their work moves the company's top priorities.

## Don't use when

- The decision is genuinely local to one product with no company-level effect. Not everything needs a P&L paragraph; forcing one reads as theater.

## Standards

Everything this skill produces follows the three exec-core standards. If exec-core isn't loaded, apply them as stated here:
- **Evidence:** separate what happened from inference; label any claim about another person's view or motive as a hypothesis with confidence and a falsifier; never state it as fact.
- **Posture:** when the user's behavior is part of the problem, fix the behavior before the wording.
- **Prose:** answer first, recommendation over options, owners and dates, no filler.

## Core doctrine

1. **Business acumen is a small universal core** [Charan]: cash, margin, velocity, return, growth, customers, and how they interact. Every recommendation to executives gets translated into its effect on these. For AI work: inference and serving cost is margin; iteration and eval cycle time is velocity; growth quality means retained, profitable usage.
2. **Every employee should understand how the business makes money** [McCord]. Test: can the user draw the P&L from memory and mark where their product appears? Name the three levers the CEO talks about most and which one their roadmap moves? Say what they should do this week to move the number leadership watches?
3. **Strategy is a response to a specific challenge** [Rumelt]. The kernel: a diagnosis of what's hard, a guiding policy that rules options out, coherent actions that reinforce each other. Goals are not strategy. Fluff (inflated language imitating strategic thought) is the warning sign.
4. **Find the crux** [Rumelt]. The crux is the most important challenge that can actually be addressed; enterprise thinkers pick one and act on it.
5. **The first team is the peer leadership team** [Lencioni; Larson]. At Director and above, loyalty goes first to the group of peers running the business together, then to one's own function. Arguing for the company over the function, even at a cost to one's own area, is the signature behavior.
6. **Specialist to generalist; analyst to integrator** [Watkins]. Understand every function's mental models well enough to make and explain tradeoffs across them.
7. **Value work you don't do** [Charan, functional passage]. Headcount and investment get argued on business grounds.
8. **Context, not control** [McCord]. Executives control when they doubt someone has the context to make the call they'd make. Demonstrated enterprise understanding earns latitude.
9. **Strategic inflection points show up first in the middle** [Grove]. People close to customers and technology see shifts before executives. An AI PM is often exactly such a "Cassandra"; the enterprise move is to translate the signal into company terms.
10. **Fix execution before touching strategy** [Slootman]. Many "strategy problems" are standards, focus, and pace problems. Enterprise thinking includes knowing which is which.

## Evidence to gather

- `self/profile.md § How the company works`.
- Product Brain strategy, metrics, and market files.
- Company materials the user can see: all-hands, planning documents, board or earnings material.
- Cost and pricing data for the user's products (for AI features, cost per task).
- A finance partner's view, when the numbers matter.

## Reasoning procedure

For any product question, proposal, or tradeoff:

1. **Load the company context:** `self/profile.md § How the company works` (priorities, binding constraint, business model) and the Product Brain's strategy. If the company's priorities or constraint are unknown, that is the first gap to close.
2. **Restate the question at company level.** "Should we build the summarization feature?" becomes "Does this move retention in the enterprise segment enough to justify the margin cost, given that renewals are the company's binding constraint this year?"
3. **Translate** with the business-acumen checklist (`references/enterprise-toolkit.md`): cash, margin, velocity, return, growth, customers, and effects on other units.
4. **Name the binding constraint** the company faces right now (growth, margin, cash, a product gap, talent, trust) and check whether the proposal addresses it or competes with it for resources.
5. **Cross-functional pass:** what would the CFO, the head of sales, the CTO, legal, and customer success each say? Which of them loses something?
6. **Kernel test** any strategy: diagnosis, guiding policy, coherent actions, and what we won't do.
7. **First-team check:** does the recommendation serve the company even if it costs the user's area? If it only serves the user's area, say so.
8. **Write the one paragraph a CFO would accept without rewriting.**

## Diagnostic questions for the user

- What are the company's top three priorities, in leadership's words? Where did you hear them?
- What is the company's binding constraint this year?
- How does your product make money, and what does it cost to serve?
- Which of your peers' priorities does your roadmap make harder?
- When did you last recommend something that cost your own area?
- What would the CFO ask about your last proposal, and did you answer it before they asked?

## Failure modes

- P&L theater: bolting financial language onto a product decision without real numbers or a real tradeoff.
- Function-first advocacy: arguing for headcount because the function needs it, with no business case behind the ask.
- Strategy as a goal list.
- Ignoring the company's actual constraint and optimizing a metric that doesn't matter this year.
- Raising the alarm about an inflection point without a proposal.

## Output

```
Company-level restatement: <the question as the CEO would pose it>.
Business effect: <cash / margin / velocity / return / growth / customers, only what applies, with numbers or ranges>.
Binding constraint: <what it is, and whether this helps or competes>.
Who wins, who pays: <functions and peers>.
Recommendation at company altitude: <one paragraph>.
Gaps in your enterprise picture: <what the user needs to learn, and from whom>.
```

## Tensions in the doctrine

- **Business lens vs product judgment.** Charan pushes everything toward the P&L. Cagan warns product leaders still have to own product judgment, and many valuable product bets can't be justified in next-quarter economics. Use the business lens to frame and prioritize, not to veto everything uncertain.
- **Execution first vs strategy first.** Slootman fixes standards, focus, and pace before strategy. Rumelt insists on a real diagnosis. Follow Slootman in a company that executes poorly on a clear strategy, and Rumelt in one that executes well on the wrong thing.
- **Function vs first team.** Lencioni's first-team loyalty can conflict with a leader's duty to advocate for their people. Advocate in the room with evidence; accept the team's decision; then own it with your own team (no "they made me do it").

## Interactions

- Supplies the enterprise case for `scope-expansion`, `executive-communication` (especially board-altitude mode), `decision-making`, and `ai-product-leadership` (AI economics).
- `next-level-readiness` rates enterprise acumen as a dimension.

## References

- `references/enterprise-toolkit.md`: business-acumen translation checklist, the P&L drill, the kernel test and crux worksheet, cross-functional perspective prompts, and the execution linkage check.
