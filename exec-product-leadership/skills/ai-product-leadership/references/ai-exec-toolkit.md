# AI executive toolkit

Checks and templates for leading AI product work at executive altitude. Distilled from the andrew-ng, ai-economics-a16z, ai-evals-practitioners, and ai-product-operators dossiers. Numbers from those sources are dated there; re-check before quoting.

## 1. Capability map (the jagged frontier, made explicit)

| Task (specific user, specific job) | Evidence on our own cases | Status | Failure modes that matter | Next re-test |
|---|---|---|---|---|
| | eval results, N, date | proven / gated / speculative | | next major model release |

A demo is not evidence for the neighboring task.

## 2. Eval maturity ladder

| Level | What exists | Decisions it can support |
|---|---|---|
| 0. Vibes | Demos, anecdotes | Whether to keep exploring |
| 1. Assertions | Scoped automated checks on every change | Regression safety for known failures |
| 2. Error analysis + validated judges | Failure taxonomy from real traces; binary judges checked against a domain owner | Internal launch, prioritizing fixes, switching models |
| 3. Online measurement | A/B or outcome metrics in production | Broad launch, outcome pricing, portfolio investment |

No broad external launch at Level 0 or 1 for any risk tier above low.

## 3. Launch gate for a probabilistic feature

1. Risk tier assigned and signed off by the accountable executive.
2. Top failure modes listed from error analysis of at least ~100 real or realistic traces.
3. Pass-rate thresholds per failure mode; non-negotiable failures at zero tolerance.
4. Automated judges validated against the domain owner's judgments.
5. UX designed for fallibility: expectations set, correction possible, sources shown where relevant.
6. Monitoring and a sampling cadence after launch.
7. A named owner of quality.
8. Rollback plan and a pinned model version.

## 4. Risk tiers

| Tier | Example | Eval bar | Gate |
|---|---|---|---|
| Low | Internal drafting aid | Level 1 | Team lead |
| Medium | Customer-facing suggestions a human reviews | Level 2 | Product leader |
| High | Automated customer-facing actions; regulated data; financial or safety impact | Level 2 minimum, Level 3 before broad launch | Executive sign-off, with legal/security |

Tier boundaries are a leadership decision; write them down.

## 5. Monthly AI quality review (one page, answer first)

```
Status: <one sentence>.
Failure modes: <mode | rate now | last month | fix in flight>.
Gates: <passed / failed this month>.
Caught before users: <incidents>.
Open risks: <top 2-3>.
Decisions needed: <from leadership, with recommendation>.
Criteria changes: <what changed in the definition of "good," and why>.
```

## 6. Date-to-funnel translation

Replace "Feature X by Q3" with stages:

| Stage | Exit criterion (eval threshold) | Time box | Decision at exit |
|---|---|---|---|
| Feasible | Works on N representative cases | 2 weeks | Go / stop |
| Common cases | Pass rate ≥ X on the top failure modes | 4-6 weeks | Go / narrow scope / stop |
| Meets gate | Launch gate satisfied for the tier | as needed | Launch / hold |

Commit to decision dates. Commit to a launch date only once the capability is proven.

## 7. Cost model (three trends)

| Driver | Now | Trend | Range for next 4 quarters | What would break the plan |
|---|---|---|---|---|
| Price per unit of capability | | falling | | |
| Tokens (or calls) per task | | rising with agents, retrieval, reasoning | | |
| Tasks per user per month | | | | |
| Human review / services cost per task | | should fall on a dated plan | | |

Derived: cost per task, cost per active user, gross margin on the AI line, dilution of blended margin. Present each as a range.

## 8. Pricing unit check

What is the pricing unit (seat, usage, outcome)? Does it track customer value? Does it track cost to serve? For outcome pricing, what measurement would settle a billing dispute? Are cohorts retaining, or are these AI tourists?

## 9. Moat questions

For any claimed advantage (data, model, workflow, distribution):
1. Does quality keep rising with more of it?
2. Who else could get an equivalent?
3. How fast does it go stale?
4. What happens when the next foundation model does this out of the box?
5. What non-AI advantage (distribution, workflow position, trust, switching cost) does it compound with?

## 10. Build / buy / partner

| Option | Total cost (incl. evals, monitoring, maintenance, people) | Time to value | Differentiation | Switching cost | Revisit when |
|---|---|---|---|---|---|
| Build | | | | | |
| Buy | | | | | |
| Partner | | | | | |

Is this capability core to how the company wins? If not, the burden of proof is on building.

## 11. Portfolio lanes

| Lane | What goes here | What executives get |
|---|---|---|
| Committed | Outcomes on proven capability | Dates |
| Capability-gated | Bets that need an eval threshold first | Triggers and decision dates |
| Frontier probes | Cheap, time-boxed tests just beyond today's capability | Re-test schedule; kill criteria |

## 12. Adoption program checks

- Leadership: has leadership said clearly what AI means for jobs and incentives?
- Lab: is there a small group turning individual experiments into shared practice?
- Crowd: is shadow AI use being surfaced safely and harvested for use cases?
- Measurement: outcomes against a baseline, not usage or satisfaction surveys.
- Expertise: are humans still exercising judgment on work outside the frontier, and are junior people still building expertise?
