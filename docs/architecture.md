# Architecture

This document records the design decisions behind the marketplace: what was borrowed from Paweł Huryn's `pm-skills`, what was changed and why, the plugin and skill taxonomy, the source-to-skill mapping, the workflow layer, the Brain interface, and the two standards every skill inherits (evidence and executive prose).

The central question the whole system serves:

> What should I be doing differently today so that increasingly senior leaders trust me with greater scope, ambiguity, people, money, strategic importance, and organizational risk?

## 1. What pm-skills actually is

Inspected at `phuryn/pm-skills` v2.1.0 (9 plugins, 69 skills, 42 commands).

- A root `.claude-plugin/marketplace.json` lists independently installable plugins. Each plugin has `.claude-plugin/plugin.json`, `skills/<skill>/SKILL.md`, `commands/<command>.md`, and a README.
- **Skills are nouns.** Frameworks and analytical knowledge that load automatically when the conversation matches the frontmatter `description`. The description is the only always-loaded text, so it carries the trigger phrases.
- **Commands are verbs.** User-invoked workflows that chain skills step by step, with checkpoints where the user can redirect, and a closing "offer next steps".
- **Progressive disclosure.** Frontmatter is lean; the body loads on trigger; heavy material sits in `references/` and is read only when the relevant branch is taken (see `pm-ai-shipping/skills/code-review`, whose sub-cases each live in their own reference file).
- **No cross-plugin references.** Plugins install independently, so a command in one plugin never hard-references a command in another. Intra-plugin references are fine.
- **Validation is part of the product.** `validate_plugins.py` plus tests enforce manifest fields, name/directory matching, command frontmatter, version sync, and README counts.
- **Knowledge is attributed but not personified.** Skills name the frameworks' originators (Torres, Cagan, Savoia) and link to further reading, but nobody is role-played.

The philosophy underneath: turn tacit expert practice into procedures a model can run, keep each unit small and composable, let workflows do the chaining, and make the whole thing verifiable.

## 2. Where this system deliberately departs from pm-skills

pm-skills is a menu of stateless tools a PM picks from. This system works more like an operating system, whose value comes from reasoning across doctrine, persistent personal history, product context, and recent events, over months. That difference forces five changes.

| pm-skills | This system | Why |
|---|---|---|
| Stateless; context comes from the conversation | Stateful; every workflow reads and writes the Career Brain and reads Product Brains | Generic advice counts as failure, and patterns only show up longitudinally. |
| Every skill self-contained | A foundation plugin (`exec-core`) holds standards every skill inherits: evidence discipline, executive prose, executive posture, the Brain protocol | The standards are the core of the product, and duplicating them 15 times guarantees drift. |
| No cross-plugin references | Commands reference skills across plugins as `**plugin:skill**` (checked by the validator), and `exec-core` is a required install | This marketplace is installed as a whole. Every domain skill also carries a short Standards section restating the three core rules, so it still behaves if `exec-core` fails to load. |
| Skills encode one framework each | Skills synthesize several sources per job, and record where the sources disagree | The user asked for synthesized doctrine. Real executive situations sit exactly where the sources disagree. |
| Sources are cited in prose | A separate source layer (`sources/<thinker>/doctrine.md`) is the authoring input; skills are built from it; it is synced into `exec-core/skills/doctrine-library` for runtime lookup | Knowledge flows upward from sources into skills. Thinkers never become user-facing units. |

Things kept exactly: nouns vs verbs, lean frontmatter with trigger phrases, one folder per skill with `references/`, commands with `$ARGUMENTS` and checkpoints (gap questions, and approval before model changes), name matches directory, one version across all manifests, a validator.

## 3. Critique of the proposed architecture

The proposal was a good starting hypothesis. Its problems were overlap, a missing foundation, and an observer plugin that mixed state with reasoning.

**Duplicated concepts across plugins.** `executive-readiness` and `next-level-gap` appeared in both `exec-trajectory` and `exec-observer`. `sponsorship` and `sponsorship-map`, `scope-expansion` and `scope-tracker`, `stakeholder-power-map` and `organizational-politics`, `relationship-capital` and `executive-trust` were each one concept split in two. The fix is a rule: **a reasoning capability lives in exactly one skill; a ledger of state lives in exactly one Brain file.** The observer owns the ledgers; the domain skills own the reasoning about each dimension.

**Communication was over-split.** `executive-update`, `executive-communication`, `recommendation-framing`, `escalation`, and `decision-memo` are modes of one discipline with one standard. They collapse into `executive-communication` with mode-specific references. Board communication is the same discipline at a different altitude, so it became a mode with its own reference file, served by `/prepare-board-update`. `meeting-presence` stays separate because live behavior in a room fails differently from writing.

**Leadership was over-split.** `delegation`, `leadership-through-others`, `operating-cadence`, and `managerial-leverage` are one Grove-shaped idea: your output is the output of the organization you influence. They collapse into `managerial-leverage`. `accountability` folds into `decision-making` (decision rights) and `executive-posture` (ownership language). `organizational-design` and `talent` are real, separate skills with less leverage for someone who is not yet running an org, so they are on the roadmap.

**The posture ladder and the evidence standard had no home.** Both are cross-cutting. The user's own example of a strong intervention ("you are escalating three decisions that fall within your scope") is a posture diagnosis, not a writing tip. Posture became a core skill that communication, readiness, and every review consumes.

**`exec-observer` mixed two things.** Maps and trackers (`scope-tracker`, `visibility-map`, `sponsorship-map`) are state. Attribution and drift detection are reasoning. The observer now has two skills: `trajectory-model`, which defines the ledgers and how evidence updates them, and `attribution-analysis`, which answers the question the user cares most about: is this a capability problem, a visibility problem, a perception lag, a sponsorship gap, or context?

**Missing workflows.** The proposal had no way to get evidence *into* the system. Without capture, the observer starves. Added `/capture` (raw notes to evidence entries), `/setup-career-brain` (bootstrap), `/debrief-exec-meeting` (closes the loop opened by `/prepare-exec-meeting`), `/audit-my-time` (leverage audit against the next level's time allocation), `/frame-decision`, and `/review-product-altitude`.

**Missing skill with the highest personal leverage.** For an AI PM, the most credible route to executive scope is becoming the person the executive team trusts on AI: economics, risk, evaluation, and strategy. `ai-product-leadership` was added to the product plugin.

## 4. Plugin taxonomy

There are seven plugins, each named for the job it does.

| Plugin | Job | Skills | Commands |
|---|---|---|---|
| `exec-core` | Hold the standards and the memory interface every other plugin depends on | evidence-discipline, executive-prose, executive-posture, brain-protocol, doctrine-library | /coach-me, /capture, /setup-career-brain |
| `exec-observer` | Maintain an accurate, longitudinal model of my organizational position | trajectory-model, attribution-analysis | /review-my-week, /review-my-month, /career-retrospective |
| `exec-trajectory` | Close the gap to the next level and grow scope legitimately | next-level-readiness, scope-expansion, enterprise-thinking | /position-for-promotion, /expand-my-scope |
| `exec-influence` | Build the trust, sponsorship, and influence that larger scope requires | executive-trust, managing-up, sponsorship, organizational-politics | /analyze-stakeholder |
| `exec-communication` | Communicate at the right altitude with ownership and judgment | executive-communication, meeting-presence | /prepare-exec-meeting, /debrief-exec-meeting, /review-exec-update, /prepare-board-update |
| `exec-leadership` | Multiply output through others and systems | managerial-leverage, decision-making | /audit-my-time, /frame-decision |
| `exec-product-leadership` | Lead product capability, and AI product strategy, at organizational level | product-leadership, ai-product-leadership | /review-product-altitude |

## 5. Skill taxonomy and consolidation

There are twenty skills: fifteen domain skills and five infrastructure skills. Each row shows what was merged into it.

| Skill | Absorbs from the proposal | One-line job |
|---|---|---|
| evidence-discipline | (new) | Separate observation, evidence, inference, hypothesis, recommendation; calibrate confidence; refuse flattery |
| executive-prose | (new) | The writing standard every output inherits |
| executive-posture | escalation (as a behavior), accountability language | Diagnose which posture a behavior signals (coordinator to executive) and the behavior producing it |
| brain-protocol | (new) | Locate, read, and write the Career Brain; read Product Brains safely |
| doctrine-library | sources layer at runtime | Look up and adjudicate what the source doctrine says |
| trajectory-model | reputation-model, scope-tracker, sponsorship-map, visibility-map, trajectory-drift, organizational-opportunity-detection | Maintain the ledgers and the trajectory hypothesis |
| attribution-analysis | attribution-analysis | Diagnose the cause class behind an outcome or a stalled trajectory |
| next-level-readiness | executive-readiness, next-level-gap, promotion-case, succession-positioning, career-capital | Level model, gap analysis, promotion evidence |
| scope-expansion | scope-expansion | Find and legitimately claim enterprise-valuable scope |
| enterprise-thinking | enterprise-thinking | Reason at company level: economics, constraints, cross-functional tradeoffs |
| executive-trust | executive-trust, relationship-capital | Model and grow the tier of trust each executive extends |
| managing-up | managing-up | Run the relationship with the boss (and skip-levels) as a two-way system |
| sponsorship | sponsorship, sponsorship-map (reasoning half) | Distinguish sponsors from mentors and allies; earn and use sponsorship |
| organizational-politics | organizational-politics, stakeholder-power-map, influence-without-authority | Power, interests, coalitions, decision process; the ethical line |
| executive-communication | executive-update, executive-communication, recommendation-framing, escalation (as writing), decision-memo, board-communication | Updates, recommendations, escalations, memos, board altitude |
| meeting-presence | meeting-presence | Behavior in consequential live interactions |
| managerial-leverage | managerial-leverage, delegation, leadership-through-others, operating-cadence | Output through others: leverage, delegation, cadence, time allocation |
| decision-making | decision-making, accountability (decision rights) | Decision rights, reversibility, speed, decision quality |
| product-leadership | product-leadership, empowered-teams, strategic-context, product-org, product-executive-role, product-judgment | From owning a product to owning product capability |
| ai-product-leadership | (new) | Operate as the organization's credible AI product executive |

Roadmap (deliberately not built in v1): `organizational-design`, `talent`, `role-transition` (first 90 days in a bigger job), `portfolio-strategy`, `negotiation` (role, scope, comp). Each needs the user to be closer to running an org before its advice is concrete. See [roadmap.md](roadmap.md).

## 6. Source-to-skill mapping

Twenty-nine sources were researched into `sources/<slug>/doctrine.md`. The generated matrix is in [doctrine-map.md](doctrine-map.md). The strongest sources per skill:

| Skill | Primary doctrine | Counterweight kept on purpose |
|---|---|---|
| executive-posture | Charan (passages), Watkins (seven shifts), Doshi (levels of work) | Pfeffer (perception is part of the job) |
| next-level-readiness | Charan, Watkins, Ibarra, Goldsmith, Hill | Ibarra vs Hughes Johnson on act-first vs know-yourself-first |
| scope-expansion | Watkins, Ibarra (job as platform), Rabois (barrels), Pfeffer (powerful units) | Campbell/Lencioni (team first; empire-building destroys trust) |
| enterprise-thinking | Charan (business acumen), McCord (context), Rumelt (kernel), Lencioni (first team) | Cagan (product leaders still own product judgment alongside the P&L conversation) |
| executive-trust | Campbell, Maister (trust equation), Scott, Lencioni, Bezos (Earn Trust) | Pfeffer (being liked is overrated; power is not granted for virtue) |
| managing-up | Gabarro & Kotter, Watkins (five conversations), Hughes Johnson, Grove, Larson | Scott (candor upward) vs Pfeffer (flatter up) |
| sponsorship | Hewlett, Ibarra, Pfeffer | Campbell (loyalty-based) vs McCord (keeper test: loyalty is not the currency) |
| organizational-politics | Pfeffer, Horowitz, Watkins (coalitions), Lencioni | Horowitz and Campbell (politics as organizational disease) vs Pfeffer (power as a fact to master) |
| executive-communication | Minto, Amazon narratives, Rumelt (fluff), Slootman, Larson, Charan (boards) | Minto's pyramid vs Amazon's narrative memo |
| meeting-presence | Hewlett (EP), Goldsmith, Grove (meetings), Larson, Campbell | Authenticity critiques (Ibarra) vs presence conformity (Hewlett) |
| managerial-leverage | Grove, Hughes Johnson, Doshi (LNO), Rabois, Charan (time applications), McCord | Slootman (leader-driven intensity) vs Hughes Johnson (systems others run) |
| decision-making | Grove, Bezos, Duke, Campbell, Horowitz | Grove's full support vs Bezos's disagree-and-commit; Cagan's empowered teams vs Horowitz's wartime command |
| product-leadership | Cagan, Doshi, Horowitz (Good PM/Bad PM), Hughes Johnson | Cagan's empowerment ideal vs the constraints of most real companies |
| ai-product-leadership | Ng, a16z (AI economics), eval practitioners, Mollick, Cagan | Speed to ship vs evaluation rigor; hype discipline vs strategic urgency |
| trajectory-model, attribution-analysis | Pfeffer, Hewlett, Ibarra, Duke, Scott | Performance-first sources (Campbell, Slootman) vs perception-first (Pfeffer) |

## 7. Workflow layer

Commands chain skills around recurring executive-development jobs. Every command follows the same skeleton:

1. **Load reality** via `brain-protocol`: the Career Brain files the job needs, plus Product Brain files for any product in scope. State what is missing.
2. **Load doctrine**: the skills named in the command.
3. **Reason** through the skill procedures, applying `evidence-discipline` to every claim about people.
4. **Diagnose before prescribing.** Posture and cause come before advice.
5. **Output** in `executive-prose`: diagnosis, evidence, recommendation, the specific move, what would change the call.
6. **Write back** to the Career Brain (evidence entries, ledger updates, open loops), per the Brain's autonomy setting.
7. **Offer the next workflow** in one line.

| Command | Chains | Writes |
|---|---|---|
| /coach-me | routes to 2-4 skills by situation type | evidence entry, commitments |
| /capture | evidence-discipline, trajectory-model | evidence entries, people files, LOG |
| /setup-career-brain | brain-protocol | the Career Brain scaffold |
| /review-my-week | trajectory-model, attribution-analysis, executive-posture, relevant domain skills | reviews/weekly, ledgers, commitments |
| /review-my-month | trajectory-model, attribution-analysis, next-level-readiness, sponsorship | reviews/monthly, model hypotheses |
| /career-retrospective | trajectory-model, attribution-analysis, next-level-readiness | reviews/retros |
| /position-for-promotion | next-level-readiness, attribution-analysis, sponsorship, executive-communication | models/readiness |
| /expand-my-scope | scope-expansion, enterprise-thinking, organizational-politics | opportunities |
| /analyze-stakeholder | organizational-politics, executive-trust, managing-up | people/<slug> |
| /prepare-exec-meeting | meeting-presence, executive-communication, executive-trust, organizational-politics | meetings/<date>-<slug> (prep) |
| /debrief-exec-meeting | meeting-presence, trajectory-model, executive-posture | meetings (debrief), evidence, people |
| /review-exec-update | executive-communication, executive-posture, executive-prose | optional evidence entry |
| /prepare-board-update | executive-communication (board altitude), enterprise-thinking | meetings |
| /audit-my-time | managerial-leverage, next-level-readiness | evidence entry, commitments |
| /frame-decision | decision-making, executive-communication, executive-posture | decision draft |
| /review-product-altitude | product-leadership, ai-product-leadership, enterprise-thinking | optional evidence entry |

Two loops matter most. In the meeting loop, prepare states intended outcomes, debrief compares them with what happened, and the gap becomes evidence. In the review loop, weekly reviews produce evidence and one or two moves; monthly reviews look only for patterns and update hypotheses; retrospectives test whether the hypotheses held.

## 8. Brain interface

Full specification: `exec-core/skills/brain-protocol/SKILL.md` and its references. The decisions:

**Two kinds of Brain, different permissions.** The Career Brain is private, personal, and read-write. Product Brains (the user's existing `pm-brain` scaffolds) are read-only from this system's point of view. Career hypotheses about executives never get written into a Product Brain, because Product Brains may be shared with a team.

**Evidence and models are separate.** `evidence/` is append-only and dated: what happened, who was there, where it came from. `models/` holds hypotheses derived from evidence, each with confidence, supporting and contradicting evidence, and what would falsify it. Reviews are the only routine path from evidence to model changes. This is the evidence discipline built into the file system.

**Conventions borrowed from pm-brain** so the two systems read the same way: `INDEX.md` routing, `_SCHEMA.md` per area, the provenance-tag enum (shared tags kept identical; `reported-by`, `document`, and `self-report` added; a translation table for pm-brain tags), TODO discipline (TODO means the user must supply it; blank means no data yet), canonical ownership (each concept has one home), and an autonomy setting in the Brain's `CAREER-BRAIN.md`.

**Product Brain adapter.** For pm-brain scaffolds the protocol knows where things live (`knowledge/strategy.md`, `stakeholders/`, `decisions/`, `ingestion/meetings/`, `knowledge/product/metrics.md`). For anything else it discovers the equivalents once and records the mapping in the Career Brain's `brains.md`.

## 9. Evidence and inference standard

Full specification: `exec-core/skills/evidence-discipline`. The rules that shape every output:

- Five classes, kept separate: observation (what happened), evidence (an observation offered in support of a claim, with its source), inference (a conclusion reasoned from evidence), hypothesis (a claim about something unobservable, such as how an executive perceives the user, with confidence and a falsifier), and recommendation (an action tied to a diagnosis).
- Revealed preference outranks stated preference. Scope granted, rooms opened, ambiguous problems delegated, and names put forward are stronger evidence than praise.
- One interaction is an anecdote. Confidence is capped by the number and independence of observations and the time they span.
- Every perception hypothesis states the strongest alternative explanation and what would falsify it.
- Motives are unobservable. Explain behavior through incentives and pressures before character.
- The user's account is the main data source and is biased toward the user. The coach asks what the other person would say happened.
- Insufficient context is stated plainly, with what is missing and how it would change the answer.
- Allegiance is to accurate diagnosis. The coach does not flatter, does not assume the promotion is deserved, and names activity-versus-impact confusion, overreach, invisible excellence, and recognition-seeking for current-level work.

## 10. Executive communication standard

Full specification: `exec-core/skills/executive-prose`. Every skill that produces text inherits it, and the coach writes in it too. It is a reasoning discipline before it is a style:

1. What does the reader need to know?
2. What changed?
3. Why does it matter?
4. What has already been decided?
5. What is unresolved?
6. What do I recommend?
7. What genuinely needs escalation?
8. Which details demonstrate command of the situation?
9. Which details are implementation noise?

Then: answer first, hierarchy over chronology, implications over activity, recommendations over option lists, ownership over coordination, concrete over abstract, density over completeness, natural cadence over polish. Corporate filler and AI writing tells are banned by list, with the reason each one damages the signal.

The standard is paired with `executive-posture` on purpose. Rewriting words without changing the behavior underneath is executive theater. When a draft signals the wrong posture, the fix starts with the decision the writer is avoiding.

## Runtime layout

```
exec-skills/
├── .claude-plugin/marketplace.json
├── exec-core/  exec-observer/  exec-trajectory/  exec-influence/
├── exec-communication/  exec-leadership/  exec-product-leadership/
│   └── .claude-plugin/plugin.json, README.md, skills/<skill>/SKILL.md (+ references/), commands/<cmd>.md
├── sources/<thinker>/doctrine.md        authoring layer; synced into exec-core/skills/doctrine-library/references/
├── docs/                                architecture, doctrine map, roadmap, usage guide
├── scripts/build.py                     syncs sources, regenerates the doctrine map
└── scripts/validate.py                  structural and consistency checks
```

The Career Brain is not in this repo. `/setup-career-brain` creates it wherever the user chooses, from the scaffold inside `exec-core/skills/brain-protocol/scaffold/`.

## Decisions recorded after the first review

An independent audit of v0.1 (2026-09-29) found six misattributions, several internal contradictions, and heavy contrastive phrasing in the repo's own text. All were fixed, and the validator now checks the section contract per skill class, tag vocabularies, YAML frontmatter, and citation traceability. Two findings were resolved by decision instead of change:

- **Doctrine digests stay in SKILL.md.** Most SKILL.md files are longer than their references. That's deliberate: the reasoning procedure cites the doctrine on every run, so the digest belongs where it always loads. References hold what only some branches need (audits, templates, worked examples). Doctrine items that no procedure step uses get cut.
- **Bold in reference documents.** The executive-prose rule ("bold at most the one thing the reader must not miss") governs messages to executives. Skill and reference files may bold the lead phrase of list items so they scan; bold inside running sentences is removed.

Doctrine traceability is now generated. `scripts/build.py` reads the citations in each skill, adds any missing skill to the cited dossier's `feeds-skills`, and writes [doctrine-map.md](doctrine-map.md) with two columns per skill: sources it cites, and sources whose dossiers map to it without being cited yet. Frameworks that no single source supplies (the posture ladder, the trust tiers, the cause classes, the A/B/C grades, the ledgers) are labeled as this system's synthesis in their skills.
