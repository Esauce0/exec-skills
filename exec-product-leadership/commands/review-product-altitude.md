---
description: "Review a strategy, roadmap, planning doc, or AI proposal for product-leadership altitude: does it do what a product leader's artifact should, or does it read as a PM's?"
argument-hint: "<file path, pasted document, or product brain area>"
---

# /review-product-altitude

Input: $ARGUMENTS

Evaluates a product artifact against the standard for a product *leader*: strategic context others can act on, real strategy (focus, insight, action, management), the link to company economics, and, for AI work, capability evidence, quality governance, economics, and risk.

## Invocation

```
/review-product-altitude ~/Documents/pm-brain/Navagate/knowledge/strategy.md
/review-product-altitude <pasted Q1 roadmap>
/review-product-altitude our AI assistant expansion proposal
```

## Workflow

### Step 1: Load

Apply **exec-core:brain-protocol**. Read the artifact. From its Product Brain: strategy, metrics, recent decisions, and the stakeholder files for its intended audience. From the Career Brain: `self/level-model.md` and `models/readiness.md` (so feedback maps to the user's target level).

Identify the artifact's audience and purpose. A roadmap for engineering and a strategy for the CPO have different bars.

### Step 2: Leadership altitude

Apply **exec-product-leadership:product-leadership**:
- Which strategic context elements does it provide, and could a PM make a disputed call from it?
- Strategy check: focus (how many top priorities), insight (what makes each pivotal), action (owners and objectives), management (how stalls surface).
- Rumelt stress test: diagnosis, guiding policy, coherent actions. Flag goals dressed as strategy and fluff.
- Does it say what the area will *not* do?

### Step 3: Enterprise link

Apply **exec-trajectory:enterprise-thinking**: does the artifact connect to the company's priorities and economics (revenue, margin, cost, risk, customers)? Would the CFO and the CEO each find what they need?

### Step 4: AI checks (if the artifact involves AI)

Apply **exec-product-leadership:ai-product-leadership**: capability evidence vs demo inference; eval maturity and launch gates; cost per task and margin; risk tier; portfolio lanes instead of feature dates; moat claims.

### Step 5: Posture of the artifact

Apply **exec-core:executive-posture**: what posture does the document signal (feature list = PM; context and bets = product leader; allocation and tradeoffs across the business = organizational leader)? Name the markers.

### Step 6: Output

Follow **exec-core:executive-prose**.

```
Verdict: <altitude the artifact operates at, and the one change that would lift it most>.

What works: <briefly, specific>.

Gaps (ranked):
1. <gap>. Why it matters to this audience. The fix.
2. ...

<If AI:> AI governance and economics: <what's missing>.

Rewrite of the opening: <the first paragraph or section rewritten at leader altitude>.

What this artifact could prove for your Director case: <the readiness dimension it could evidence, if fixed>.
```

### Step 7: Write back

If the artifact is significant (shared with leadership), create an evidence entry of type `communication` with the posture tag. Offer to track the revision.

## Notes

- Don't rewrite the whole document unless asked. The value is the diagnosis and the lead rewrite.
- Never copy Career Brain content (readiness notes, stakeholder hypotheses) into the artifact.
