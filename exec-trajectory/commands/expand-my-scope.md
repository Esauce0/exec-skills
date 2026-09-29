---
description: "Find organizational problems adjacent to your responsibilities where taking ownership creates real enterprise value and demonstrates increased capacity, and design the legitimate path to owning one"
argument-hint: "<optional: a specific opportunity you're considering>"
---

# /expand-my-scope

Input: $ARGUMENTS

Looks for legitimate scope: problems the company needs solved that sit next to the user's current responsibilities, where owning them would create enterprise value and generate next-level evidence. Empire-building candidates get rejected.

## Invocation

```
/expand-my-scope
/expand-my-scope Nobody owns eval infrastructure across the three AI teams
```

## Workflow

### Step 1: Load

Apply **exec-core:brain-protocol**: `self/current-role.md`, `models/scope.md`, `models/readiness.md`, `opportunities.md`, people files for the manager and skip-level, and evidence entries tagged `scope+`, `scope-`, or type `reorg`. From Product Brains: strategy (especially `§ Tensions`), roadmap, org/team, and recent decisions for the user's products and adjacent ones.

### Step 2: Generate candidates

If the user named one, include it and still generate alternatives. Sources:
- Recurring executive frustrations in evidence entries and meeting debriefs.
- Strategy tensions and blocked decisions in Product Brains.
- Seams between teams that keep failing.
- The manager's own overloaded areas (from their person file: accountabilities and observed priorities).
- New company priorities without a clear owner.
- Departures and reorgs.
- For an AI PM: cross-cutting AI capability (evaluation, governance, model platform, cost, adoption) per **exec-product-leadership:ai-product-leadership**.

Aim for 4-8 candidates.

### Step 3: Evaluate

Apply **exec-trajectory:scope-expansion**: the evaluation matrix, the anti-empire test, situation type. Apply **exec-trajectory:enterprise-thinking** to state each candidate's enterprise value in company terms. Use `models/readiness.md` to score evidence value: prefer candidates that demonstrate dimensions rated `absent` or `partial`.

### Step 4: Map legitimacy and power

For the top one or two, apply **exec-influence:organizational-politics**: who can grant it, who currently owns anything adjacent, who might block, what the action-forcing event is. Check the manager relationship with **exec-influence:managing-up**: how does the manager gain if the user takes this?

### Step 5: Design the move

- The one-page ask (template in scope-expansion `references/opportunity-evaluation.md`).
- The pre-wiring sequence: manager first, then adjacent owners, then the decider.
- What the user hands off to make room, and to whom.
- The first visible result and its date.
- The formalization target (plan, OKR, or announcement) and date.

### Step 6: Write

Add or update rows in `opportunities.md` (status `validating` or `proposed`). Propose a commitment for the first step.

## Output

Treat this template as a checklist of content: keep the order, drop empty items, and write it as prose where prose reads better (exec-core executive-prose).

```
Recommendation: pursue <opportunity>. <Why it's legitimate and valuable, two sentences.>

It would demonstrate: <readiness dimensions>.
Risk: <main risk and mitigation>. Cost: <what gets handed off>.

Path:
1. <pre-wire manager, with the opening line>
2. <...>
3. Formalize by <date> via <mechanism>.

Draft ask: <one page>

Other candidates:
- <candidate>: <why not now / why not at all>
```

## Notes

- If the best candidates all fail the anti-empire test, say so. Sometimes the right move is excelling where the user is and waiting for the next reorg.
- If the user's current scope is shaky, the recommendation is to fix it first.
- Never recommend taking something from a peer without that peer's agreement.
