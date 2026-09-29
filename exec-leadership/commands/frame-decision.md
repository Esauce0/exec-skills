---
description: "Frame a consequential decision: who decides, whether it's yours, reversibility and real reversal cost, options with probabilities, premortem, kill criteria, and produce the recommendation or escalation"
argument-hint: "<the decision in a sentence, plus any context or docs>"
---

# /frame-decision

Input: $ARGUMENTS

Use this for decisions that matter. It establishes whether the call is the user's, sizes the process to the decision, and produces either the decision (with reasoning recorded before the outcome) or a clean recommendation to whoever decides.

## Invocation

```
/frame-decision Move summarization to Vendor Y in Q4?
/frame-decision Whether to hold the beta until latency is under 2s
```

## Workflow

### Step 1: Load

Apply **exec-core:brain-protocol**: `self/current-role.md` (decision rights), people files for the decider and affected peers, and from Product Brains: prior decisions on the topic (precedent), strategy, metrics, hypotheses.

### Step 2: Frame

Apply **exec-leadership:decision-making**: the six frame questions. If no one can say who decides, the first output is a proposal for who should.

### Step 3: Whose call

Run the decision-rights sort. If it's the user's call and they were planning to escalate, say so plainly (this is the posture leak **exec-core:executive-posture** is built to catch). If it's beyond their authority, the output is a recommendation.

### Step 4: Classify and size

Impact and reversibility, with the real reversal cost priced (decision-making `references/decision-toolkit.md`). Size the process: quick for low/two-way; premortem, independent input, and a written memo for high/one-way.

### Step 5: Options and estimates

List the options, including do-nothing and decide-later, with probability-weighted outcomes as ranges. Name the key uncertainty and whether it can be reduced cheaply before deciding. For AI decisions, apply **exec-product-leadership:ai-product-leadership** (capability evidence, eval maturity, economics, risk tier). For decisions with business effects, apply **exec-trajectory:enterprise-thinking**.

### Step 6: Premortem (high-impact only)

Name the tigers, paper tigers, and elephants, and turn each tiger into a tripwire.

### Step 7: Recommend or decide

- The recommendation with confidence.
- Kill criteria.
- If escalating: apply **exec-communication:executive-communication** (decision-request mode): decision needed, by when, recommendation, cost of delay. Escalate jointly with the peer if there's disagreement.
- If contested and the user isn't the decider: the voice-then-commit plan.

### Step 8: Record

Suggest recording the decision in the relevant Product Brain through that brain's own decision workflow (for pm-brain, `/decide`), with reasoning and probabilities captured before the outcome. If the decision matters to the user's trajectory (a visible call, a scope-relevant choice), create a Career Brain evidence entry of type `decision`.

## Output

Treat this template as a checklist of content: keep the order, drop empty items, and write it as prose where prose reads better (exec-core executive-prose).

```
Decision: <sentence>. Decider: <name>. By: <date>.
Whose call: <yours / recommend to X / drive openly>. <If yours and you were going to escalate: say so.>
Type: <impact / reversibility>. Real reversal cost: <...>.

Options:
- <option>: <outcome range, probability>
Recommendation: <option>, ~<confidence>%. Key uncertainty: <...>.
Premortem: tigers <...> → tripwires <...>.
Kill criteria: <...>.

<If escalating:> Draft request: <...>
<If deciding:> Decision note: <...>
```

## Notes

- Never let a decision go up without a recommendation.
- If the analysis shows the decision barely matters, say so and recommend deciding in five minutes.
