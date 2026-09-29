---
source: Hamel Husain, Shreya Shankar, Eugene Yan, and the co-authors of "What We Learned from a Year of Building with LLMs" (Yan, Bischof, Frye, Husain, Liu, Shankar)
slug: ai-evals-practitioners
role-in-system: Evaluation as the operating core of AI product quality and as the executive governance mechanism for probabilistic systems. How a leader makes AI quality legible, sets launch gates, and stops vibes-based shipping.
feeds-skills: [ai-product-leadership, evidence-discipline, decision-making, executive-communication, product-leadership, organizational-design, managerial-leverage]
last-researched: 2026-09-29
---

# AI evals practitioners: Husain, Shankar, Yan and co-authors

## Why this source matters here
These are practitioners and researchers who built or advised many LLM products in 2023-2025. Husain is an independent ML consultant. Shankar is a data-systems and HCI researcher (EvalGen, and an MLOps interview study). Yan writes on applied LLM patterns. With Bischof, Frye and Liu they co-wrote the most-cited field report on building with LLMs (2024). Their shared finding is that AI products fail or succeed on the quality of the measurement loop, not on the choice of model. Their vantage point is the team and the individual contributor. For this system, the executive translation is the point. The user will not write most evals as a Director or VP. The user must require them, staff them, read their outputs, and use them to decide launches and to make probabilistic behavior understandable to executives used to deterministic software. The field is two to three years old and shifting toward agent evaluation, so treat specific techniques as perishable. The principles (look at the data, measure specific failure modes, assign an owner) have been stable across 2023-2026.

## Primary sources
- Husain, "Your AI Product Needs Evals" (hamel.dev, Mar 29, 2024). Three levels of evaluation and the Rechat case. [consulted] https://hamel.dev/blog/posts/evals/
- Husain, "Creating a LLM-as-a-Judge That Drives Business Results" (hamel.dev, Oct 29, 2024). Principal domain expert, binary judgments, critique shadowing. [consulted] https://hamel.dev/blog/posts/llm-judge/
- Husain, "A Field Guide to Rapidly Improving AI Products" (hamel.dev, Mar 24, 2025). Error analysis, data viewers, experiment-based roadmaps, communicating uncertainty. [consulted] https://hamel.dev/blog/posts/field-guide/
- Husain & Shankar, "LLM Evals: Everything You Need to Know" (FAQ; first published 2025, revised since; the page showed a 2026 revision). [consulted] https://hamel.dev/blog/posts/evals-faq/
- Shankar, Zamfirescu-Pereira, Hartmann, Parameswaran & Arawjo, "Who Validates the Validators? Aligning LLM-Assisted Evaluation of LLM Outputs with Human Preferences" (arXiv Apr 2024; UIST 2024). Criteria drift. [consulted: abstract] https://arxiv.org/abs/2404.12272
- Shankar, Garcia, Hellerstein & Parameswaran, "Operationalizing Machine Learning: An Interview Study" (arXiv Sep 2022). Velocity, validation, versioning. [consulted: abstract] https://arxiv.org/abs/2209.09125
- Yan, "Patterns for Building LLM-based Systems & Products" (eugeneyan.com, Jul-Aug 2023). Seven patterns, with evals first. [consulted] https://eugeneyan.com/writing/llm-patterns/
- Yan, "An LLM-as-Judge Won't Save The Product—Fixing Your Process Will" (eugeneyan.com, Apr 2025). [consulted] https://eugeneyan.com/writing/eval-process/
- Yan, Bischof, Frye, Husain, Liu & Shankar, "What We Learned from a Year of Building with LLMs," Parts I-III (O'Reilly Radar, May 28-Jun 6, 2024). Part II (operational) and Part III (strategy) [consulted]; Part I (tactical) [by reference]. https://www.oreilly.com/radar/what-we-learned-from-a-year-of-building-with-llms-part-iii-strategy/
- Cross-references: Ng, "Improve Agentic Performance with Evals and Error Analysis" (The Batch, Oct 2025) [consulted]; METR, early-2025 developer productivity RCT (Jul 10, 2025) [consulted] https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/

## Operational doctrine
### D1. Stalled AI products usually lack an evaluation system, not a better model
- **Claim:** Husain (2024) argues unsuccessful AI products almost always share one root cause: no robust evaluation system. Teams keep changing prompts, models and code without a way to measure effects or debug. They hit whack-a-mole, where each fix breaks something else. Success tracks iteration speed, and iteration speed depends on a loop of evaluate, inspect, change. He describes three levels of evaluation, rising in cost. Level 1 is cheap, scoped assertions run on every change. Level 2 is human and model review of logged traces. Level 3 is A/B tests, for mature products only.
- **Source:** "Your AI Product Needs Evals" (Mar 2024).
- **Changes coaching how:** When the user reports an AI initiative that "plateaued after the demo," the coach asks about the eval loop before anything about vendors or models. The executive version of the question: "Which failure modes matter, what is our pass rate on each, and how long does it take to measure a change?"
- **Boundary conditions:** In the first days of exploration, informally reading a handful of outputs is enough (Husain; Ng, Oct 2025). The error is staying there after users arrive.

### D2. Look at the data: error analysis comes before metrics
- **Claim:** Read real traces, write notes on what went wrong, and let failure categories emerge from the data instead of from templates. In one client case, three issues accounted for about 60% of problems (Field Guide, 2025). Husain and Shankar advise reviewing at least 100 diverse traces at the start, until new ones stop revealing new failure modes, and then sampling regularly. The 2024 co-authors recommend looking at samples of inputs and outputs every day and watching for drift between development and production data. Custom, low-friction data viewers are the highest-return investment.
- **Source:** Field Guide (Mar 2025); Evals FAQ (2025); "What We Learned... Part II" (May 2024).
- **Changes coaching how:** The coach expects the user, even as an executive, to read a sample of real outputs on a regular cadence and to require a failure-mode taxonomy with frequencies in every AI product review. A dashboard of generic scores is not an acceptable substitute.
- **Boundary conditions:** Reading user data needs privacy controls (consent, redaction, access logging). In regulated settings that constrains who may look and how.

### D3. Generic scores mislead; use binary judgments tied to named failure modes
- **Claim:** 1-5 ratings and off-the-shelf metrics (generic "helpfulness" or "hallucination" scores) produce numbers nobody can act on and give false confidence. Better: pass/fail judgments on specific failure modes, each with a written critique. An LLM judge should be validated against a domain expert's labels, with true-positive and true-negative rates measured separately because failures are rare. LLM judges are worth building only for persistent failure modes that code assertions cannot catch.
- **Source:** "Creating a LLM-as-a-Judge" (Oct 2024); Field Guide (2025); Evals FAQ (2025).
- **Changes coaching how:** When a team reports "quality is 4.2 out of 5" or "hallucination rate 3%," the coach helps the user ask three questions. What exactly counts as a fail? Who decided? How well does the automated judge agree with that person? Most executive dashboards fail these questions.
- **Boundary conditions:** Ranking, creative and preference tasks may need comparative or graded judgments. Mature, high-traffic products can use online A/B metrics for the outcomes that matter most.

### D4. Criteria drift: good cannot be fully specified before you see outputs
- **Claim:** Shankar et al. (2024) found that people need criteria to grade outputs, but grading outputs is what helps them define the criteria. Some criteria depend on the specific outputs observed. Evaluation standards emerge through the act of evaluating; they cannot be set once, independent of the data.
- **Source:** "Who Validates the Validators?" (arXiv Apr 2024; UIST 2024).
- **Changes coaching how:** When executives or a PRD demand fixed acceptance criteria up front, the coach helps the user propose an initial criteria set plus a scheduled revision after the first error-analysis cycle. It helps the user explain why changing the criteria is learning, not scope creep. This is central to communicating probabilistic systems to executives used to specs.
- **Boundary conditions:** Non-negotiables (safety, legal, privacy, regulated accuracy) must be fixed in advance and do not drift. Drift applies to quality criteria, not to hard limits.

### D5. Name one accountable owner of "good"
- **Claim:** Pick a principal domain expert, whose judgment defines success, and give them a benevolent-dictator role over quality decisions. This avoids annotation conflicts and decision paralysis. Domain experts should be able to change prompts directly rather than route everything through engineers. Add annotators only when the product serves genuinely different domains.
- **Source:** "Creating a LLM-as-a-Judge" (2024); Field Guide (2025); Evals FAQ (2025).
- **Changes coaching how:** The coach treats "who owns what good looks like for this AI product?" as an org-design question for the user. If the answer is a committee or nobody, that is the finding. The executive's job is to appoint that person, give them time, and back their calls.
- **Boundary conditions:** One person's taste can encode bias or miss user segments. Pair the owner with periodic checks against user outcomes and a second reviewer on high-stakes criteria.

### D6. The model is the least durable part; invest in the system around it
- **Claim:** The 2024 co-authors argue the model is likely to be the least durable component of the system. Durable investment goes into evals, guardrails, caching, data flywheels and UX. Their other advice: no GPUs before product-market fit. Start with inference APIs, and fine-tune only after proving it is necessary. Their example is BloombergGPT, overtaken by general models within about a year. Their planning implication: what is an infeasible demo today becomes a premium feature within a few years and a commodity soon after, so build systems and organizations with that in mind. Migrating prompts across models is painful. Pin model versions, and use evals to measure the effect of a switch.
- **Source:** "What We Learned... Part III: Strategy" (Jun 6, 2024) and Part II (May 31, 2024).
- **Changes coaching how:** When an investment proposal centers on training or picking "the best model," the coach redirects the user toward the durable assets. The eval suite, specifically, is the asset that makes switching models cheap and safe. That is an argument finance and procurement understand.
- **Boundary conditions:** Self-hosting or fine-tuning is justified by privacy regulation, cost at scale, latency, or a real differentiation need. The co-authors acknowledge these cases.

### D7. The demo-to-product gap is the main planning error; roadmap experiments, not features
- **Claim:** The co-authors write that a demo that works in a controlled setting is worlds apart from a product that works reliably at scale. Husain (2025) proposes roadmaps that commit to an experimentation cadence and to decision timeboxes rather than feature dates. His "capability funnel" shows progress through levels (works at all, works on common cases, works reliably) even before the final result exists. When talking to leadership, he frames it as: in N weeks we will know whether this is feasible, and then we decide.
- **Source:** "What We Learned... Part III" (2024); Field Guide (2025).
- **Changes coaching how:** When the user must give an executive a date for an AI capability, the coach helps convert it into a capability funnel with decision points and eval thresholds. The user commits to dates for decisions and for scoped capability levels, not for unproven quality.
- **Boundary conditions:** Contracts, launches and partner commitments sometimes require dates. In that case commit to a date for a narrower capability that evals already support.

### D8. Calibrate risk by use case and build the UX for fallibility
- **Claim:** Set risk tolerance per use case. Medical or financial outputs need a high bar; internal tools can tolerate more. Separate non-negotiables (reliability, harmlessness) from aspirations and ship a minimum lovable product. Design human-in-the-loop flows and defensive UX: set expectations about limitations, make AI output easy to dismiss or correct, show sources, and collect explicit and implicit feedback as future eval data.
- **Source:** "What We Learned... Part II" (2024); Yan, "Patterns for Building LLM-based Systems & Products" (2023).
- **Changes coaching how:** The coach asks the user to place each AI feature in a risk tier, each with its own eval bar, launch gate and monitoring. The coach treats the choice of risk appetite as an executive decision to escalate explicitly, not one the team should make implicitly.
- **Boundary conditions:** Risk tiers are only as good as the error detection behind them. A low-tier feature with silent, undetectable failures is not low risk.

### D9. Tools do not replace process
- **Claim:** Yan (2025) argues an LLM-as-judge will not save a product. What does is organizational discipline: observe data, annotate, form a hypothesis about the failure, run an experiment. He calls this the scientific method. Teams that buy eval platforms before they have a process automate confusion. The 2024 co-authors make the same point: process comes before tools. Husain and Shankar report spending most of development effort (60-80%) on error analysis and evaluation in their own work, and advise starting with notebooks or simple custom tools.
- **Source:** Yan, "An LLM-as-Judge Won't Save The Product" (Apr 2025); "What We Learned... Part II" (2024); Evals FAQ (2025).
- **Changes coaching how:** When the user proposes buying an evaluation vendor as the fix for quality problems, the coach asks which existing process the tool will speed up. If there is none, the recommendation is to fund the process (people's time, a domain owner, a trace viewer) first.
- **Boundary conditions:** At scale, with an established process, platforms reduce toil and are worth buying.

### D10. Make AI quality legible to executives through findings, not dashboards
- **Claim:** Husain and Shankar advise reporting what error analysis found: the top failure modes and their rates, what was fixed, and the problems caught before users saw them. A wall of metrics is not a report. Shankar's MLOps interview study (2022) named velocity, validation and versioning as what makes production ML work. That is a useful three-part vocabulary for executive reporting on AI systems.
- **Source:** Evals FAQ (2025); "Operationalizing Machine Learning" (2022).
- **Changes coaching how:** The coach helps the user design a recurring AI quality review for their VP or leadership forum. It covers failure modes with trend lines, launch gates passed or failed, open risks, and the decisions needed. It is written answer-first, so a probabilistic system reads as a managed one.
- **Boundary conditions:** Executives differ in how much detail they want. The headline must stand alone, with detail available on request.

### D11. Perceived gains are not measured gains
- **Claim:** In METR's randomized trial (Jul 2025), 16 experienced open-source developers took 19% longer on real issues when allowed AI tools. They had forecast a 24% speedup and still believed afterward that they had been sped up about 20%. METR cautions that this does not show AI fails to speed up most developers; it is one specific setting.
- **Source:** METR (Jul 10, 2025), cross-referenced here as evidence for the evals stance.
- **Changes coaching how:** The coach treats self-reported AI productivity or quality claims, including the user's own and their team's, as hypotheses to measure. It pushes the user to require a measured baseline and a measured comparison before an AI productivity claim goes to executives.
- **Boundary conditions:** Small sample, a specific population, and early-2025 tools. It warns against trusting perception. It does not show that AI tools are useless.

## Frameworks in operational form
**Eval maturity ladder (what a leader should expect and what each level can support):**
| Level | What exists | Decisions it can support |
|---|---|---|
| 0 Vibes | demos, anecdotes | whether to keep exploring |
| 1 Assertions | scoped automated checks on every change | regression safety for known failures |
| 2 Error analysis plus validated judges | failure taxonomy, binary judges checked against an expert | internal launch, prioritizing fixes, model switching |
| 3 Online measurement | A/B or outcome metrics in production | broad launch, pricing on outcomes, portfolio investment |
The coach refuses a broad external launch at Level 0 or 1 for any risk tier above low.

**Launch gate for a probabilistic feature:** (1) Risk tier assigned and signed off by the accountable executive. (2) Top failure modes listed from error analysis of at least 100 real or realistic traces. (3) Pass-rate thresholds per failure mode, with non-negotiables at zero tolerance. (4) Automated judges validated against the domain owner. (5) Defensive UX in place (expectations, correction, sources). (6) Monitoring and a sampling cadence after launch. (7) A named quality owner. (8) Rollback plan and pinned model version.

**Monthly AI quality review (one page, answer first):** status in one sentence; failure modes table (mode, rate now, rate last month, fix in flight); gates passed or failed; incidents caught before users; open risks; decisions needed from leadership; criteria changes and why (criteria drift, logged).

**Error-analysis loop to require of teams (Yan's four steps):** observe traces, annotate failures, form a hypothesis about the cause, run an experiment with a measurable outcome. Repeat on a fixed cadence.

**Date-to-funnel translation (from D7):** replace "feature X by Q3" with stages (feasible, works on common cases, meets gate), a timebox per stage, the eval threshold that ends each stage, and the go/stop decision at each stage.

## Diagnostic questions
- Can the user name the top three failure modes of their AI product and their current rates?
- Who is the accountable owner of "good," and do they have the time and authority to act?
- When did the user last read raw outputs from their own product?
- Are quality numbers binary and tied to named failures, or generic scores?
- Has anyone checked the automated judges against a human expert? How well do they agree?
- If the model provider shipped a new version tomorrow, how long would it take to know whether to switch?
- Is the roadmap committing to dates for unproven quality?
- Are AI productivity claims in executive materials measured or self-reported?

## Observable signals
Positive:
- The user's AI updates lead with failure modes and trend lines rather than feature lists.
- The user has appointed or championed a named quality owner and protected their time.
- The user converts date demands into capability funnels with decision points, and executives accept them.
- The user can say how the team would evaluate a model switch, and roughly how long it would take.
- The user samples real outputs personally on a cadence and cites specific examples in reviews.
- The user escalates the choice of risk appetite explicitly instead of letting the team absorb it.

Negative:
- The user reports "accuracy" or 1-5 scores with no definition of a fail.
- The user launches on the strength of a demo or internal enthusiasm.
- The user proposes an eval platform purchase as the fix while no one reads traces.
- The user's AI roadmap has fixed dates for capabilities no eval has yet demonstrated.
- The user treats every criteria change as scope creep, or never changes criteria.
- The user repeats team or vendor productivity claims without asking how they were measured.

## Anti-patterns and misuse
- Eval theater: large dashboards of unvalidated metrics that look rigorous and change no decisions.
- Pushing all eval work onto engineers while domain experts and PMs never look at outputs.
- Using "evals first" to block exploration. Informal trace reading is the right start.
- Freezing criteria to satisfy a spec culture, and so missing failure modes users actually hit.
- Treating an LLM judge's score as ground truth without checking it against an expert.
- The executive who asks for evals but never reads the findings, which teaches the team that evals are compliance.

## Tensions with other sources
- **Ng (sandbox first, guardrails later) vs. this cluster's rigor:** less conflict than it appears. Both say to start informally and fast. The disagreement is over when to formalize. Ng tolerates later formalization for internal prototypes; these authors formalize as soon as real users or real risk arrive. The risk-tier framework decides.
- **Lab leaders' "ship early and refine in public" (Weil, 2025, in ai-product-operators) vs. risk calibration here:** frontier labs can afford public iteration with their brand and user base. Most enterprises cannot for high-risk uses. For low-risk tiers, iterative public release is right.
- **Bezos/Amazon on high-velocity decisions and two-way doors:** evals are what turn launches into two-way doors (measure, roll back). Without evals, a probabilistic launch is closer to a one-way door for trust.
- **Duke on resulting:** evals separate decision quality from outcome luck. A good-looking launch week is not evidence of quality.
- **Minto on answer-first communication:** failure-mode tables must be wrapped in an answer-first summary for executives. Evidence alone does not communicate.
- **Cagan on feasibility risk in discovery:** evals are how feasibility risk is retired for AI products. They belong in discovery, not only at the end of delivery.
- **Slootman and Horowitz on urgency vs. eval discipline:** urgency cultures read evals as friction. The reply is Ng's and Husain's shared finding that eval discipline is what makes teams faster.
- **Larson on platform work:** eval infrastructure is platform work and faces the usual platform-funding politics.

## Limits and biases
- Commercial interest: Husain and Shankar teach a paid evals course, and several authors consult on this topic. That is not disqualifying, but they have reason to present evals as the central lever.
- Evidence: mostly practitioner case studies, client anecdotes and small-sample research. Few controlled comparisons exist between teams with strong evals and teams without them.
- Level: written for builders and team leads. The executive layer here is this dossier's translation and should be tested against the user's reality.
- Era and drift: 2023-2024 techniques (specific judge setups, RAG patterns) age quickly. Agentic, multi-step systems increase the number of possible failures and change how evals are built (Ng, Oct 2025). Re-check specifics before prescribing them.
- The METR result is one small study, cross-referenced for its caution about perception, not as a general finding about AI productivity.

## Skill mapping
| Doctrine | Skill(s) | How the skill should use it |
|---|---|---|
| D1 | ai-product-leadership, evidence-discipline | Diagnose stalled AI work through the eval loop first |
| D2 | evidence-discipline, ai-product-leadership | Require failure-mode taxonomies; have the user read outputs |
| D3 | evidence-discipline, executive-communication | Interrogate generic scores and unvalidated judges |
| D4 | executive-communication, decision-making | Explain criteria drift; set criteria with scheduled revisions |
| D5 | organizational-design, managerial-leverage | Appoint and protect a single owner of quality |
| D6 | portfolio-strategy, enterprise-thinking | Invest in durable system assets; evals as switching insurance |
| D7 | executive-communication, product-leadership | Turn date demands into capability funnels with decision points |
| D8 | decision-making, ai-product-leadership | Assign risk tiers with distinct gates; escalate risk appetite |
| D9 | decision-making, ai-product-leadership | Fund process before buying tools |
| D10 | executive-communication, board-communication | Run an answer-first monthly AI quality review |
| D11 | evidence-discipline | Treat self-reported AI gains as hypotheses to measure |

## Verified quotations
- "a failure to create robust evaluation systems" (Husain, "Your AI Product Needs Evals," Mar 29, 2024), his named root cause of unsuccessful AI products.
- "users need criteria to grade outputs, but grading outputs helps users define criteria" (Shankar et al., "Who Validates the Validators?", arXiv abstract, Apr 2024).
- "models are likely to be the least durable component in the system" (Yan, Bischof, Frye, Husain, Liu & Shankar, "What We Learned from a Year of Building with LLMs, Part III," O'Reilly, Jun 6, 2024).
