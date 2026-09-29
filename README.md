# exec-skills

An executive-development operating system for product and AI leaders, built as a Claude Code plugin marketplace. 20 skills and 16 workflows across 7 plugins.

It exists to answer one question, continuously and specifically:

> What should I be doing differently today so that increasingly senior leaders trust me with greater scope, ambiguity, people, money, strategic importance, and organizational risk?

It reasons across three things at once: researched executive doctrine, a private Career Brain that remembers your trajectory and stakeholders, and the Product Brains that hold your actual product context. Generic advice counts as failure.

## How it works

```
EXECUTIVE DOCTRINE        sources/<thinker>/doctrine.md — 29 researched dossiers
        ↓                 distilled into
EXECUTIVE SKILLS          20 skills, organized by job to be done (never by thinker)
        ↓                 chained by
EXECUTIVE WORKFLOWS       16 commands: /coach-me, /review-my-week, /prepare-exec-meeting, ...
        ↓                 reasoning over
CAREER + PRODUCT BRAINS   your private trajectory record + your product context
        ↓                 applied to
THE CURRENT EVENT         a meeting, a draft, a decision, a piece of feedback
        ↓
COACHING OUTPUT           diagnosis, evidence, the move, what would change the call
```

Each workflow makes the model reason across both layers: the doctrine in the skills and the facts of your situation in the Brains.

## Start here

| You want to... | Run |
|---|---|
| Set up your Career Brain (once) | `/setup-career-brain` |
| Get guidance on a real situation | `/coach-me <situation>` |
| Record what happened | `/capture <notes or description>` |
| Prepare for / debrief an executive meeting | `/prepare-exec-meeting`, `/debrief-exec-meeting` |
| Fix an update before it goes to your VP | `/review-exec-update` |
| See whether this week moved anything | `/review-my-week` |
| Find out whether you're actually ready | `/position-for-promotion` |

A fuller guide: [docs/usage.md](docs/usage.md).

## Plugins

| Plugin | Job | Skills | Commands |
|---|---|---|---|
| [exec-core](exec-core/README.md) | The standards and memory interface everything inherits | evidence-discipline, executive-prose, executive-posture, brain-protocol, doctrine-library | /coach-me, /capture, /setup-career-brain |
| [exec-observer](exec-observer/README.md) | An honest longitudinal model of your organizational position | trajectory-model, attribution-analysis | /review-my-week, /review-my-month, /career-retrospective |
| [exec-trajectory](exec-trajectory/README.md) | Close the gap to the next level; grow scope legitimately | next-level-readiness, scope-expansion, enterprise-thinking | /position-for-promotion, /expand-my-scope |
| [exec-influence](exec-influence/README.md) | Trust, sponsorship, and influence | executive-trust, managing-up, sponsorship, organizational-politics | /analyze-stakeholder |
| [exec-communication](exec-communication/README.md) | Communicate at the right altitude | executive-communication, meeting-presence | /prepare-exec-meeting, /debrief-exec-meeting, /review-exec-update, /prepare-board-update |
| [exec-leadership](exec-leadership/README.md) | Output through others and systems | managerial-leverage, decision-making | /audit-my-time, /frame-decision |
| [exec-product-leadership](exec-product-leadership/README.md) | Lead product capability; be the credible AI product executive | product-leadership, ai-product-leadership | /review-product-altitude |

## The standards every skill inherits

- **Evidence discipline.** Observation, evidence, inference, hypothesis, and recommendation are kept separate. No motive or perception is stated as fact. Revealed allocation (scope, rooms, problems delegated) outranks praise. Confidence is capped by longitudinal evidence. The coach does not flatter, does not assume your promotion is deserved, and says so when you're operating below the level you want.
- **Executive prose.** Answer first, hierarchy over chronology, implications over activity, recommendations over option lists, ownership over coordination. Corporate filler and AI writing tells are banned by list. The system's own output follows the standard.
- **Executive posture.** Diagnoses whether a message or behavior signals coordinator, project manager, expert, product manager, product leader, organizational leader, or executive, and fixes the behavior producing the signal before the wording, since rewording alone is executive theater.

## Install

From a local clone:

```bash
claude plugin marketplace add /path/to/exec-skills
claude plugin install exec-core@exec-skills
claude plugin install exec-observer@exec-skills
claude plugin install exec-trajectory@exec-skills
claude plugin install exec-influence@exec-skills
claude plugin install exec-communication@exec-skills
claude plugin install exec-leadership@exec-skills
claude plugin install exec-product-leadership@exec-skills
```

Then run `/setup-career-brain`.

## Privacy

The Career Brain holds hypotheses about named people and about your standing. It lives outside this repo, wherever you choose, and should never sit in a shared drive or a repo with a shared remote. Skills never copy its contents into Product Brains, tickets, shared docs, or messages.

## Repository

```
.claude-plugin/marketplace.json
exec-*/                      7 plugins: .claude-plugin/plugin.json, README, skills/, commands/
sources/<thinker>/           authoring layer: researched doctrine dossiers
docs/                        architecture, doctrine map, usage, roadmap
scripts/build.py             syncs sources into exec-core's doctrine library; regenerates the doctrine map
scripts/validate.py          structural and consistency checks
```

Design rationale, including where and why this departs from Paweł Huryn's [pm-skills](https://github.com/phuryn/pm-skills): [docs/architecture.md](docs/architecture.md). Which sources feed which skills: [docs/doctrine-map.md](docs/doctrine-map.md).

```bash
python scripts/build.py
python scripts/validate.py
```
