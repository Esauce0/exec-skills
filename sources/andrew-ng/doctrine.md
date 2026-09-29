---
source: Andrew Ng
slug: andrew-ng
role-in-system: The enterprise adoption sequence for AI (early wins, a central capability, literacy by audience, strategy after experience, communications by stakeholder), plus LLM-era guidance on speed, cost and evals from someone who built AI units inside Google and Baidu.
feeds-skills: [ai-product-leadership, portfolio-strategy, organizational-design, talent, enterprise-thinking, executive-communication, decision-making, evidence-discipline, scope-expansion]
last-researched: 2026-09-29
---

# Andrew Ng

## Why this source matters here
Ng founded and led Google Brain, ran Baidu's AI Group, and then founded Landing AI (enterprise AI transformation), AI Fund (a venture studio) and DeepLearning.AI (education). His AI Transformation Playbook (December 2018) is addressed to CEOs of companies worth roughly $500M to $500B. It describes the job of the person who builds an organization's AI capability, which is the executive role this user is aiming at. His letters in The Batch (2024-2025) cover the LLM era: prices falling, prototypes built in days, product decisions as the new bottleneck, evals as the predictor of progress. For transfer: Ng writes as an AI leader with CEO sponsorship and a central team. The user is a PM, so the Playbook describes the destination role and how its credibility gets built. It is not a plan the user can execute alone. The 2018 material predates LLMs and needs heavy re-dating.

## Primary sources
- AI Transformation Playbook: How to lead your company into the AI era (Landing AI, Dec 2018; PDF revision 11-19). The five-step sequence, the pilot criteria, training hours by audience, moats, communications. [consulted] https://landing.ai/wp-content/uploads/2020/05/LandingAI_Transformation_Playbook_11-19.pdf
- "What Artificial Intelligence Can and Can't Do Right Now" (HBR, Nov 9, 2016). The "one second of thought" capability heuristic, useful here as an example of how capability rules of thumb expire. [by reference; title and date confirmed] https://hbr.org/2016/11/what-artificial-intelligence-can-and-cant-do-right-now
- "Opportunities in AI" (Stanford talk, 2023). The AI stack: the application layer is where the large, less-concentrated opportunity sits. [by reference, via summaries]
- "Concrete Ideas Make Strong AI Startups" (The Batch, Jul 24, 2024). Concrete ideas beat vague ones. [consulted] https://www.deeplearning.ai/the-batch/concrete-ideas-make-strong-ai-startups
- "Falling LLM Token Prices and What They Mean for AI Companies" (The Batch, Aug 28, 2024). Cost trajectory and when to optimize. [consulted] https://www.deeplearning.ai/the-batch/falling-llm-token-prices-and-what-they-mean-for-ai-companies
- "AI Product Managers Will Be In-Demand" (The Batch, Jan 15, 2025). The AI PM skill set and engineer-to-PM ratios. [consulted] https://www.deeplearning.ai/the-batch/ai-product-managers-will-be-in-demand/
- VB Transform fireside chat, reported by VentureBeat as "'Sandbox first'" (Jun 24, 2025). Sandbox first, guardrails after proof. [consulted; secondary report of a talk] https://venturebeat.com/orchestration/sandbox-first-andrew-ngs-blueprint-for-accelerating-enterprise-ai-innovation
- "How to Get Through the Product Management Bottleneck" (The Batch, Jul 16, 2025). [consulted] https://www.deeplearning.ai/the-batch/how-to-get-through-the-product-management-bottleneck
- "Improve Agentic Performance with Evals and Error Analysis," Parts 1 and 2 (The Batch, Oct 15 and Oct 22, 2025). [consulted] https://www.deeplearning.ai/the-batch/improve-agentic-performance-with-evals-and-error-analysis-part-1
- AI for Everyone (Coursera, 2019). A non-technical course for business leaders. [by reference]

## Operational doctrine
### D1. The first AI projects must succeed; they do not need to be the most valuable
- **Claim:** Early projects exist to build momentum and belief, not to capture the biggest prize. They should be meaningful enough that nobody calls them trivial and feasible with current technology, with feasibility checked by trusted AI engineers before kickoff. They should have a clear, measurable business objective and be buildable by an AI team partnered with domain experts, showing traction within 6-12 months (2018). Ng's own sequence at Google Brain went Speech first (important but not core), then Maps, and only after two wins a conversation with Ads.
- **Source:** Playbook, step 1 (2018).
- **Changes coaching how:** When the user proposes making "transform our core product with AI" the first bet, the coach asks what credibility-building project comes before it and who the willing internal customer is. It helps the user plan a ladder of internal customers, where each win is the reference for the next conversation.
- **Boundary conditions:** The 6-12 month window reflects 2018, when models were custom-trained. LLM prototypes now take days (Ng, 2025), so the first win should come in weeks. If the organization already has many pilots and nothing in production, another pilot is the problem, not the solution (see ai-product-operators on pilot purgatory).

### D2. AI strategy follows experience; it cannot be written first
- **Claim:** Ng argues that most companies cannot write a thoughtful AI strategy until they have basic hands-on experience from pilots, a team and training. Strategy is step 4 of 5. Once teams see early successes they can identify where AI creates the most value and concentrate resources there.
- **Source:** Playbook, step 4 (2018).
- **Changes coaching how:** When an executive asks the user for "our AI strategy" in the abstract, the coach recommends pairing any strategy document with evidence from shipped or piloted work. Where no such evidence exists, the coach frames the strategy as explicit hypotheses with dates to revisit them. The user's authority on strategy comes from having run the experiments.
- **Boundary conditions:** When a board or a competitor forces a stance now, waiting is not an option. Write a provisional strategy and label it as such. Rumelt would say diagnosis comes first. Ng's reply is that without experience the diagnosis is guesswork. Both hold, at different stages of maturity.

### D3. Build central capability and lend it to the business units
- **Claim:** A central AI unit (under the CTO, CIO or CDO, or a Chief AI Officer) should build company-wide capability. It runs an initial sequence of cross-functional projects and then a repeatable process for delivering more, sets consistent recruiting and retention standards, and builds platforms no single division would build, such as unified data warehousing. Talent is matrixed into divisions. Ng's analogy is the internet era, where companies running scattered independent experiments failed to transform.
- **Source:** Playbook, step 2 (2018).
- **Changes coaching how:** For scope expansion, the coach points the user toward owning something cross-cutting: evaluation infrastructure, a model gateway, data access standards, AI hiring bars. Owning one more AI feature is not scope expansion. The coach asks: "What would every AI team here need that no single team will build?"
- **Boundary conditions:** Evidence from 2025 cuts against heavy centralization. MIT NANDA found that successful organizations empowered line managers rather than central labs, and that they bought more than they built. Ng himself (2025) warns that approval layers stall large companies. A workable split: centralize platforms, standards and talent, and decentralize ownership of use cases.

### D4. Build AI literacy by audience, with different goals for each
- **Claim:** Ng's notional plan: executives get about 4 hours so they can understand what AI can and cannot do, start on strategy and allocate resources. Division leaders running AI projects get about 12 hours so they can set direction, track progress and course-correct. AI engineer trainees get about 100 hours. The Chief Learning Officer's job is to curate content, not create it.
- **Source:** Playbook, step 3 (2018).
- **Changes coaching how:** The coach treats peer and executive literacy as the user's lever: executives who cannot tell capability from hype make bad portfolio calls. It asks whether the user has a short, repeatable briefing for executives, built on the company's own examples, and a longer one for division leaders who own AI outcomes.
- **Boundary conditions:** The hour counts and curriculum (classes of algorithms) date from 2018. Today, hands-on use of current tools probably teaches executives more than technical explanation (see Mollick in ai-product-operators). Literacy content goes stale within months.

### D5. Build several hard, aligned assets and win in your own sector, not in "AI" generally
- **Claim:** Defensibility comes from several difficult assets aligned with a coherent strategy (Ng cites Porter) and from being the leading AI company in your sector rather than competing broadly with big tech. It also comes from the virtuous cycle (better product, more users, more data) and a deliberate data strategy: strategic acquisition, unified warehouses, and knowing which data is actually valuable. Ng warns against CEOs over-investing in low-value data or buying companies for data that turns out to be useless. His fix is to bring the AI team in early on data acquisition.
- **Source:** Playbook, step 4 (2018); "Opportunities in AI" (2023) on the application layer.
- **Changes coaching how:** When the user's strategy says "our data is our moat," the coach asks which data, whether model quality keeps improving with more of it, whether it is accessible, and whether a competitor could substitute a foundation model plus public data.
- **Boundary conditions:** Casado and Lauten (a16z, 2019) argue data moats are mostly weak scale effects with diminishing returns. Foundation models (2023 onward) have reduced the value of proprietary training data for many language tasks. Treat the virtuous cycle as a hypothesis to test, not a given.

### D6. Communications is its own workstream, with five audiences
- **Claim:** Ng lists five audiences. Investors need a clear value-creation thesis. Regulators need a credible account of the benefits and ongoing dialogue. Customers need roadmap and marketing messages. Recruits need to see early successes. Employees need explanations that address hype and fear, including fear of automation.
- **Source:** Playbook, step 5 (2018).
- **Changes coaching how:** The coach asks the user to map each AI initiative to the audiences it affects and to draft the message for each, especially the internal one on job impact. Because investor and regulator messages belong to executives, the user's move is to supply the sponsor with a crisp value thesis and risk narrative.
- **Boundary conditions:** Ng noted in 2018 that fear of automation varies by culture. In 2025-2026 the internal message is harder because layoffs attributed to AI are real in some firms. Vague reassurance destroys trust. Say only what leadership will actually commit to.

### D7. Force concreteness: a vague idea is rarely wrong and rarely useful
- **Claim:** Ng argues that vague ideas ("use AI to optimize healthcare assets") win applause and are almost never wrong. Concrete ones, specific enough that an engineer could start a prototype, can be tested and can fail fast. That makes them faster to validate on technical and business feasibility.
- **Source:** "Concrete Ideas Make Strong AI Startups" (Jul 2024).
- **Changes coaching how:** When the user brings an AI strategy full of themes ("AI-powered insights," "agentic transformation"), the coach makes them rewrite each theme as a concrete product statement: a specific user, a specific task, and the evidence that would kill the idea. That is the test of whether the portfolio is real.
- **Boundary conditions:** Board-level narrative needs some abstraction. Keep concreteness at the level of bets and let the themes group them.

### D8. Do not prematurely optimize token cost; do plan to switch models
- **Claim:** GPT-4-class token prices fell about 79% per year from March 2023 to August 2024. Ng advises most teams to focus on building something useful rather than optimizing LLM cost. He says an application that is marginally too expensive today may be worth deploying in anticipation of cheaper prices. Teams should periodically reassess models and providers, but switching is hard without good evals.
- **Source:** "Falling LLM Token Prices" (Aug 2024).
- **Changes coaching how:** When finance challenges inference cost, the coach helps the user present three things: the cost trend, a plan for switching models, and the eval harness that makes switching safe. It does not help the user promise margins they cannot yet show.
- **Boundary conditions:** This is a view from the application-builder and venture side. At scale, or when a product needs frontier models whose prices fall more slowly, margins bite (see ai-economics-a16z). Agentic workloads make many calls per task, which can raise cost per task even as per-token prices fall (inferred from Ng's own note that agents benefit from falling prices; not a claim he quantifies).

### D9. Sandbox first; add guardrails once a pilot proves out
- **Claim:** Large companies grind to a halt when any experiment needs sign-off from several VPs. Ng proposes sandboxes: teams prototype quickly with limited private data, and the company invests in observability and guardrails after a project proves valuable. He also says a company cannot let a stray innovation team ship something that damages the brand. He offers moving fast while being responsible as a replacement for the old "move fast and break things" ethos.
- **Source:** VB Transform fireside, as reported by VentureBeat (Jun 2025); his move-fast-responsibly framing in 2024-2025 letters and talks (by reference).
- **Changes coaching how:** The coach helps the user propose two-tier governance: light approval for sandboxes (synthetic or limited data, no external users) and a real gate for production (evals, risk review, monitoring). Designing this is exactly the executive-level contribution: it lets speed and safety coexist, so the organization doesn't have to pick one.
- **Boundary conditions:** Regulated data (health, finance, children's data) may not be usable even in a sandbox. Legal and security must co-design the tiers. "Guardrails later" never means "evals never."

### D10. The best predictor of AI team progress is disciplined evals and error analysis
- **Claim:** From his experience across teams, Ng says the biggest predictor of how fast a team makes progress on an AI agent is whether it runs a disciplined evals and error-analysis process. He says this matters more than using the newest tools. Teams can start by informally reading a handful of traces, then build evals iteratively and find which workflow step falls short of human-level performance.
- **Source:** "Improve Agentic Performance with Evals and Error Analysis," Parts 1-2 (Oct 2025).
- **Changes coaching how:** When the user reviews another team's AI project, or is asked whether a project is on track, the coach steers toward the eval process ("How do you know it got better last week?") and away from model choice or architecture. See ai-evals-practitioners for the full doctrine.
- **Boundary conditions:** This is an observation from Ng's portfolio, not a controlled study.

### D11. When building gets cheap, deciding what to build is the bottleneck
- **Claim:** Agentic coding has moved the constraint from building to deciding what to build: "builder's block." Ng increasingly values PMs with deep user empathy who decide quickly. They use data to refine their mental model of the user and then decide fast from that model, rather than mechanically following the latest survey. Separately (Jan 2025) he lists the AI PM skill set as technical AI proficiency, comfort with iterative development, data proficiency, managing ambiguity and continuous learning. He expects the engineer-to-PM ratio (commonly around 6:1) to shift toward more PM work.
- **Source:** "How to Get Through the Product Management Bottleneck" (Jul 2025); "AI Product Managers Will Be In-Demand" (Jan 2025).
- **Changes coaching how:** The coach treats how fast and how well the user's organization makes decisions as the user's executive value. It asks what mechanisms (decision owners, user-insight cadence, prototype reviews) keep product decisions in step with engineering speed, and whether the user is the bottleneck.
- **Boundary conditions:** Ng limits this to small numbers of critical decisions. High-volume decisions (ad targeting, recommendations) still belong to automated experimentation.

## Frameworks in operational form
**Pilot selection scorecard (from D1; 0-2 each, fund a first project only at 8 or above):**
| Criterion | Question |
|---|---|
| Feasibility | Has a trusted AI engineer who is not the proposer checked it against current models? |
| Time to traction | Visible result in weeks (LLM era) or 6-12 months (custom ML)? |
| Measurable objective | Is there one business metric, with a baseline? |
| Meaningful, not trivial | Would a skeptical executive count success as real evidence? |
| Willing internal customer | Does a domain team with its own stake co-own it? |
| Reference value | Does success make the next, more important conversation easier? |

**Internal-customer ladder:** (1) List candidate internal customers by importance and willingness. (2) Pick a mid-importance, high-willingness partner for win one. (3) Use win one as the reference for win two in a different function. (4) After two wins, open the conversation with the crown-jewel business. (5) At each rung, record the evidence and the sponsor you gained.

**Five-step transformation audit (run on the user's company):** For each step (pilots, central team, literacy, strategy, communications) write down the current evidence, the gap, and who owns the gap. The gap nobody owns but the user could credibly own is a scope-expansion candidate.

**Two-tier AI governance (from D9):** Sandbox tier: synthetic or limited data, internal users only, time-boxed, a single approver. Production tier: an eval suite with pass thresholds, risk classification, privacy and legal review, monitoring, and a named quality owner. A written promotion rule says what evidence moves work from sandbox to production.

**Communications map (from D6):** rows are initiatives; columns are investors (via sponsor), regulators (if applicable), customers, recruits, employees. Each cell holds the message, the owner and the date.

## Diagnostic questions
- Which of the five steps is the organization weakest on, and is the user positioned to fix it?
- Is the user's first or next AI bet chosen to succeed and build belief, or chosen for size?
- Could an engineer start a prototype from the user's current AI roadmap items? Which items are still themes?
- Who at the executive level can explain what current AI can and cannot do in the company's own domain? Did the user teach them?
- Is there a sandbox path, or does every experiment face production-grade approval?
- When the user claims a data advantage, what evidence shows more data improves the product?
- How does the team know its AI system improved last week?
- Is the user's organization deciding what to build as fast as it can now build?

## Observable signals
Positive:
- The user sequences AI bets deliberately and can name the internal customer ladder and the evidence gained at each step.
- The user owns or proposes a cross-cutting AI platform, standard or governance tier that serves several teams.
- The user runs AI literacy sessions for executives or peers, built on the company's own use cases.
- The user's strategy documents cite results from their own pilots and label untested claims as hypotheses.
- The user presents inference cost as a trend with a model-switching plan and an eval harness behind it.
- The user asks about eval process first when assessing any AI project.

Negative:
- The user proposes a flagship, company-defining AI project as the first bet with no feasibility review.
- The user writes AI strategy as themes with no concrete, killable product statements.
- The user treats "we have lots of data" as a moat without evidence.
- The user either ignores cost entirely in executive forums or blocks a useful launch over marginal token cost.
- The user leaves internal fear about automation to HR or to silence.

## Anti-patterns and misuse
- Treating the 2018 Playbook as current: 6-12 month pilot timelines, 100-hour trainee curricula and "data acquisition first" thinking all need re-dating for LLMs.
- Pilot collecting: running many "momentum" pilots that never reach production and calling it transformation.
- Using "strategy follows experience" as a reason never to commit to a strategy.
- Reading "guardrails later" as permission to skip evals, privacy review or legal review for anything user-facing.
- Building a central AI team that becomes an approval bottleneck instead of a capability provider.
- Quoting Ng's cost optimism to finance without the margin analysis finance needs.

## Tensions with other sources
- **Rumelt vs. Ng on strategy timing:** Rumelt puts diagnosis first; Ng says a company cannot diagnose well without experience. Rumelt is more right when the competitive challenge is already clear (a rival's AI product is taking share). Ng is more right when the organization cannot yet tell feasible from infeasible.
- **Cagan (empowered product teams) vs. Ng (central AI unit matrixed out):** Cagan wants durable cross-functional teams that own problems. Ng's matrix lends AI talent project by project. Ng fits early, when talent is scarce. Cagan fits once AI is part of every product team's normal toolkit.
- **Grove, Horowitz and Slootman (urgency) vs. Ng's staged sequence:** if AI is a strategic inflection point for the business, a slow, safe ladder of pilots can be fatal. Ng's sequence fits building internal belief. Urgency fits a visible competitive threat.
- **Bezos/Amazon on two-way doors aligns with the sandbox tier:** make reversible experiments cheap and keep the rigor for one-way doors (production launches, customer commitments).
- **Duke on resulting:** Ng's "first projects must succeed" can push teams to pick safe bets and then read success as validation of AI generally. Duke would ask what was learned about the decision process, not just whether the pilot worked.
- **Within this cluster:** NANDA (2025) favors buying and decentralizing, while Ng favors in-house capability over time. Casado and Lauten (a16z) doubt data moats that Ng's virtuous cycle assumes.

## Limits and biases
- Commercial interest: Landing AI sells transformation help, AI Fund builds startups, and DeepLearning.AI sells training. The Playbook's emphasis on training and partners matches those businesses.
- Context: the Playbook is written for CEOs of large enterprises, and Ng's experience comes from resource-rich tech companies (Google, Baidu) with CEO backing. A PM in a mid-size company cannot run this sequence alone.
- Era: much of the Playbook predates LLMs (Dec 2018). His 2016 capability heuristic (tasks a person does in under a second of thought) is now obsolete. Treat any capability rule of thumb as having a short shelf life.
- Survivorship: the Speech-Maps-Ads story is one success. Failed ladders are not documented.
- Optimism: Ng is consistently bullish on AI value and cost declines. Pair him with the economics and adoption evidence in sibling dossiers.
- The Playbook's "$13 trillion of GDP" figure is an external estimate he cites. Do not reuse it as his finding.

## Skill mapping
| Doctrine | Skill(s) | How the skill should use it |
|---|---|---|
| D1 | ai-product-leadership, portfolio-strategy | Score first and next AI bets for success probability and reference value, not size |
| D2 | ai-product-leadership, evidence-discipline | Require pilot evidence behind strategy claims; label the rest as hypotheses |
| D3 | organizational-design, scope-expansion | Point the user toward cross-cutting AI platforms and standards as scope |
| D4 | ai-product-leadership, executive-communication | Have the user build audience-specific AI literacy briefings for executives |
| D5 | enterprise-thinking, ai-product-leadership | Stress-test moat claims, especially data moats |
| D6 | board-communication, executive-communication | Build per-audience AI communications, with the internal job-impact message first |
| D7 | portfolio-strategy, decision-making | Convert themes into concrete, killable product statements |
| D8 | enterprise-thinking, ai-product-leadership | Frame inference cost as a trend plus a switching plan plus an eval harness |
| D9 | decision-making, organizational-design | Design two-tier (sandbox/production) governance |
| D10 | ai-product-leadership, evidence-discipline | Ask about the eval process first when judging AI project health |
| D11 | product-leadership, managerial-leverage | Treat decision throughput as the user's executive value |

## Verified quotations
- "get the flywheel spinning so that your AI team can gain momentum" (AI Transformation Playbook, step 1, 2018).
- "Expecting an AI team to magically create value from a large dataset" (AI Transformation Playbook, step 4, 2018), which Ng calls a formula with a high chance of failure.
- "a disciplined process for evals and error analysis" (The Batch, "Improve Agentic Performance with Evals and Error Analysis, Part 1," Oct 15, 2025).
