# Person file schema (career view)

Filename: `<firstname-lastname>.md`. One file per person who matters to the owner's trajectory: manager, skip-level, executives, peers, key cross-functional partners, direct reports. Sponsorship is recorded on the evidence-gated ladder (Sponsorship level), never as a relationship type.

This is the career view: how the person relates to the owner's trajectory. The product view (what they want from a product) lives in Product Brains under `stakeholders/`. Link, don't duplicate.

Every claim about the person's priorities, preferences, or views carries a date and a provenance tag. Anything not observed is a hypothesis and lives in `models/reputation.md` or in the Hypotheses section below, in hypothesis format.

```markdown
# <Name> — <Title>

## Snapshot
- Relationship to me: manager | skip-level | executive | peer | cross-functional | report | external
- Org / reports to:
- Formal power over my trajectory: <e.g., writes my review; sits in calibration; controls budget for area X>
- Informal influence: <evidence-based: whose opinion they shape, forums they run>
- Sponsorship level: contact | ally | mentor | connector | opportunity-giver | sponsor  (see models/sponsorship.md; evidence required)
- Last touched: YYYY-MM-DD   <!-- auto-maintained -->
- Product Brain profiles: <links to stakeholders/<slug>.md in each Product Brain>

## What they are accountable for
<!-- Documentary: their OKRs, their updates, what their boss holds them to. -->

## Stated priorities
<!-- In their words, dated, with source. -->
- YYYY-MM-DD — <priority>  `<provenance>`

## Observed priorities
<!-- What they spend attention on, ask about, fund, or push back on. Behavior, dated. -->
- YYYY-MM-DD — <observation>  `<provenance>`

## Pressures and incentives
<!-- Structural: what they're measured on, what's at risk for them, what changed around them. This is where behavior gets explained before any character inference. -->

## How they like to receive information
<!-- Evidence-based: reader vs listener, detail level, pre-reads, pre-wiring, channel, timing. Mark each as observed or reported. -->

## Trust signals toward me
<!-- Dated. Allocation first (scope, rooms, problems delegated, names put forward), then direct statements, then observed behavior. -->
- YYYY-MM-DD — <signal>  `<provenance>`

## Friction and concerns
<!-- Dated. Theirs about me or my work, and mine about working with them. Facts, not feelings. -->

## What I can do for them
<!-- Their problems I'm positioned to help with. The strongest relationships are built here. -->

## Hypotheses
<!-- Short ones about this person (priorities, incentives). IDs are namespaced by person: H-P-<slug>-1, H-P-<slug>-2. Perception-of-me hypotheses go in models/reputation.md and are linked here. Use the hypothesis format. -->

## Interaction log
- YYYY-MM-DD — <one line>  → [evidence](../evidence/YYYY/MM/<file>.md) or [meeting](../meetings/<file>.md)

## Open loops
<!-- Things I owe them; things they owe me. With dates. -->

## Unknowns that matter
<!-- What I don't know about them that would change how I work with them. These become questions to answer, not gaps to fill with guesses. -->
```

## Rules

- No personality typing, no armchair psychology, no labels ("political," "insecure," "difficult"). Describe behavior and incentives.
- Stated and observed priorities are kept separate on purpose. The gap between them is often the most useful thing in the file.
- A sponsorship level of connector or above requires a dated act in the Trust signals section; "sponsor" requires a dated act of advocacy in a decision.
