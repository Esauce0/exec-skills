---
description: "Build an evidence-based model of a stakeholder: priorities, pressures, incentives, communication preferences, relationship history, trust signals, friction, influence, and where you can create value for them, without inventing psychology"
argument-hint: "<person's name or slug, and optionally what's coming up with them>"
---

# /analyze-stakeholder

Input: $ARGUMENTS

Builds or refreshes a model of one person from evidence across the Career Brain and every Product Brain, and turns it into a plan for working with them.

## Invocation

```
/analyze-stakeholder Priya Raman
/analyze-stakeholder dan-okafor before our Q4 planning fight
```

## Workflow

### Step 1: Gather

Apply **exec-core:brain-protocol**:
- Career Brain: `people/<slug>.md`, every evidence entry naming them (grep LOG by slug), meetings with them, their rows in `models/reputation.md` and `models/sponsorship.md`.
- Every Product Brain: `stakeholders/<slug>.md` (or the mapped slug in `brains.md`), meeting ingestion where they appear, decisions they made or blocked.
- Optional, with permission: recent email threads or calendar history with them.

If there's little evidence, say so. A thin model is better than an invented one.

### Step 2: Build the model

Apply **exec-influence:organizational-politics** (`references/stakeholder-model.md`) and **exec-core:evidence-discipline**. Fill each section from evidence with dates and provenance. Keep stated and observed priorities separate. Explain behavior by incentives and pressures first. Put anything unevidenced under Unknowns.

### Step 3: Trust and relationship

Apply **exec-influence:executive-trust**: which trust tier they currently extend to the user, from revealed behavior; the weakest trust component; the next tier and what earns it. If they're the user's manager, also apply **exec-influence:managing-up** (six-dimension diagnosis). Place them on the sponsorship ladder per **exec-influence:sponsorship**.

### Step 4: Hypotheses

State at most three hypotheses about them (their priorities, how they see the user, how they'll react to something upcoming). Each in hypothesis format with the strongest alternative and a falsifier. Start new ones at low confidence.

### Step 5: Value and approach

- What problem does this person have that the user is unusually positioned to help with?
- How to communicate with them (format, timing, pre-wiring), from evidence.
- If something specific is coming up, the approach for it.

### Step 6: Write

Update `people/<slug>.md` (facts: act and tell; hypotheses and sponsorship level: propose). Add or update their rows in `models/reputation.md` (propose). Never write any of this into the Product Brain's stakeholder file.

## Output

Treat this template as a checklist of content: keep the order, drop empty items, and write it as prose where prose reads better (exec-core executive-prose).

```
<Name>, <title>. Accountable for <...>; currently pressured by <...> (evidence).

Accountable for: <...>
Stated priorities: <dated> | Observed priorities: <dated>. Gap: <if any>.
Pressures: <...>
How to communicate with them: <evidence-based>
Trust extended to you: <tier>, (<confidence>). Next tier: <...> via <behavior>.
Sponsorship level: <level>, based on <evidence>.
Friction: <dated, both directions>

Hypotheses:
- (low) <claim>. Alternative: <...>. Would weaken if: <...>.

Where you can create value for them: <specific>.
<If something is coming up:> Approach: <plan and opening line>.

Unknowns worth resolving: <questions, and how to answer them>.
```

## Notes

- Don't type anyone's personality or use labels like "political," "insecure," or "difficult."
- Separate the product view (what they want from a product) from the career view (how they relate to the user's trajectory).
