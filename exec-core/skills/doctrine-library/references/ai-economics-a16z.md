---
source: Martin Casado and Matt Bornstein (Andreessen Horowitz), with later a16z, Sequoia and Bessemer analyses of AI unit economics
slug: ai-economics-a16z
role-in-system: The CFO and board lens on AI products. Explains why AI gross margins, scaling behavior and defensibility differ from SaaS, and what an AI product leader must be able to explain about inference cost, services creep, pricing and build/buy.
feeds-skills: [ai-product-leadership, enterprise-thinking, executive-communication, portfolio-strategy, decision-making, evidence-discipline, product-leadership]
last-researched: 2026-09-29
---
<!-- Generated from sources/ai-economics-a16z/doctrine.md by scripts/build.py. Edit the source, not this copy. -->

# Martin Casado & Matt Bornstein (a16z) and successors on AI economics

## Why this source matters here
Casado and Bornstein wrote "The New Business of AI" (February 2020) from a venture portfolio view across dozens of AI companies. They argued that AI businesses behave like a hybrid of software and services, with lower margins, harder scaling and weaker moats than SaaS. That vocabulary became the one finance teams use when they challenge AI plans. The LLM era changed the cost structure. Training moved largely to model providers, inference became the main cost of goods sold, and per-token prices at constant capability began falling around 10x a year. Later a16z pieces (2023-2026) and cross-checks from Sequoia and Bessemer update the picture. The user is not a founder, but the same economics apply to an AI feature inside a company: it adds COGS, it can dilute blended SaaS margin, it creates services work, and its pricing unit matters. An aspiring AI product executive has to be able to defend these numbers to a CFO. Transfer caveat: venture investors optimize for outlier outcomes and have portfolio positions, so read their prescriptions as a lens, not neutral fact.

## Primary sources
- Casado & Bornstein, "The New Business of AI (and How It's Different From Traditional Software)" (a16z, Feb 16, 2020). Margins, long tail, services, defensibility, founder advice. [consulted] https://a16z.com/the-new-business-of-ai-and-how-its-different-from-traditional-software/
- Casado & Bornstein, "Taming the Tail: Adventures in Improving AI Economics" (a16z, Aug 12, 2020). Diagnosing and managing long-tail problems. [consulted] https://a16z.com/taming-the-tail-adventures-in-improving-ai-economics/
- Casado & Lauten, "The Empty Promise of Data Moats" (a16z, May 9, 2019). [consulted] https://a16z.com/the-empty-promise-of-data-moats/
- Bornstein, Appenzeller & Casado, "Who Owns the Generative AI Platform?" (a16z, Jan 19, 2023). App-layer margins and value capture. [consulted] https://a16z.com/who-owns-the-generative-ai-platform/
- Appenzeller, Bornstein & Casado, "Navigating the High Cost of AI Compute" (a16z, Apr 27, 2023). [consulted] https://a16z.com/navigating-the-high-cost-of-ai-compute/
- Wang, Erten & Immerman, "Pricing and Packaging Your B2B or Prosumer Generative AI Feature" (a16z, Mar 22, 2024). [consulted] https://a16z.com/pricing-packaging-ai-b2b-prosumer/
- Appenzeller, "Welcome to LLMflation: LLM inference cost is going down fast" (a16z, Nov 12, 2024). [consulted] https://a16z.com/llmflation-llm-inference-cost/
- Wang, Xu, Kahl & Erten, "How 100 Enterprise CIOs Are Building and Buying Gen AI in 2025" (a16z, Jun 10, 2025). [consulted] https://a16z.com/ai-enterprise-2025/
- Erten, "Surviving AI Price Wars Without Destroying Your Business" (a16z, Apr 13, 2026). [consulted] https://a16z.com/surviving-ai-price-wars-without-destroying-your-business/
- Cross-checks outside a16z: Cahn, "AI's $600B Question" (Sequoia, Jun 20, 2024) [consulted] https://www.sequoiacap.com/article/ais-600b-question/ ; Bessemer, "The State of AI 2025" (Aug 13, 2025) [consulted] https://www.bvp.com/atlas/the-state-of-ai-2025
- a16z enterprise newsletter, "AI Is Driving A Shift Towards Outcome-Based Pricing" (Dec 2024). [by reference; seen in listing only]

## Operational doctrine
### D1. Model AI gross margin as lower and more variable than SaaS, and show it
- **Claim:** In 2020 the authors observed AI companies at roughly 50-60% gross margin, against 60-80%+ for SaaS. The drivers were cloud compute (training, retraining, inference, data) and humans in the loop. In the LLM app layer (Jan 2023), margins ranged up to 90% in a few cases but were more often 50-60%, with app companies spending about 20-40% of revenue on inference and per-customer fine-tuning. Bessemer (Aug 2025) reported fast-scaling AI "Supernovas" near 25% gross margin, often negative, versus about 60% for steadier "Shooting Stars."
- **Source:** "The New Business of AI" (2020); "Who Owns the Generative AI Platform?" (2023); Bessemer State of AI 2025.
- **Changes coaching how:** The coach expects the user to present the margin impact of every AI feature: cost per task, cost per active user, and how both move with usage. Revenue alone is not enough. For an AI feature bundled into an existing SaaS product, the number finance cares about is dilution of blended margin.
- **Boundary conditions:** Internal-productivity AI with no revenue line needs cost per task compared with the labor or time it replaces. All figures are portfolio observations, not audited benchmarks. They date quickly (2020 and 2023 figures predate cheap small models).

### D2. Services creep: plan for it and price it; do not hide it in R&D
- **Claim:** AI products often need human work: labeling, review, onboarding, customization, exception handling. Founders should embrace services deliberately, track the costs honestly rather than burying them in R&D, and commit to a strategy. In 2026 a16z still lists forward-deployed engineers and dedicated customer success among the things that make AI apps defensible.
- **Source:** "The New Business of AI" (2020); "Surviving AI Price Wars" (Apr 2026).
- **Changes coaching how:** When the user's AI product relies on human review or forward-deployed engineers, the coach pushes the user to put that cost in the P&L, reflect it in pricing, and set a dated plan for which parts of the service get automated and how the eval data will show it. If the service share is not shrinking, the user is running a consulting business and should say so.
- **Boundary conditions:** In regulated or high-stakes uses, the human is the product's safety mechanism and should not be automated away to hit a margin target.

### D3. Diagnose the long tail before promising scale
- **Claim:** In 2020 the authors reported that as much as 40-50% of intended functionality may sit in the long tail of user intent. New customers bring new edge cases, so AI businesses can show diseconomies of scale: each gain in quality costs more data and effort. "Taming the Tail" asks whether the problem is consistent across customers (a global tail, one model) or varies by customer (a local tail, costly customization). Remedies: narrow the problem (constrain inputs), convert it (single-turn designs, human failover), componentize it into bounded sub-problems, or use shared global or "trunk" models instead of per-customer models.
- **Source:** "The New Business of AI"; "Taming the Tail" (2020).
- **Changes coaching how:** When a board or executive asks "why doesn't quality improve as we add customers?", the coach has the user classify the tail and name which remedy is in use. When sales promises per-customer customization, the coach flags the margin and maintenance cost.
- **Boundary conditions:** Foundation models absorbed much of the input-coverage tail for general language tasks. Our inference: the tail now shows up mostly as a reliability tail, rare but costly failures, which is an evals problem more than a data problem.

### D4. AI is not the moat; build defensibility the old-fashioned way
- **Claim:** Model architectures are published, pre-trained models are widely available, and customers often control the data. Casado and Lauten (2019) argue that most "data network effects" are really scale effects with diminishing returns, rising costs to find new signal, and data that goes stale. In 2023 the authors found many generative apps undifferentiated and most dollars flowing to infrastructure vendors. What defends an AI product is superior product, workflow integration, distribution, account control and brand. Bessemer (2025) suggests context and memory may be new sources of switching cost and warns about "thin wrapper" exposure.
- **Source:** "The Empty Promise of Data Moats" (2019); "The New Business of AI" (2020); "Who Owns the Generative AI Platform?" (2023); Bessemer 2025.
- **Changes coaching how:** When the user's strategy or board slide claims proprietary data or "our model" as the moat, the coach asks four things. Does quality keep rising with more of this data? Who else could get equivalent data? How fast does it go stale? What happens when the next foundation model does this task out of the box?
- **Boundary conditions:** Some data advantages are durable: exclusive or regulated access, feedback captured inside a workflow others cannot see, and proprietary outcome labels.

### D5. Plan for variable costs and falling prices at the same time
- **Claim:** At constant capability, LLM inference cost fell about 10x per year (Appenzeller, Nov 2024, measured with MMLU thresholds). Ng measured about 79% per year for GPT-4-class prices (Aug 2024). The "Year of Building with LLMs" authors estimated a halving time of about six months (Jun 2024). But compute remained a major capital sink in 2023, when many AI companies spent most of the capital they raised on compute, and a16z's 2024 pricing guidance says to price at sustainable levels now and expect margins to expand later.
- **Source:** "Welcome to LLMflation" (2024); "Navigating the High Cost of AI Compute" (2023); "Pricing and Packaging" (2024).
- **Changes coaching how:** The coach has the user build the cost model from three trends: price per token, tokens per task (rising with agents, retrieval and reasoning), and tasks per user. Present a range to the CFO, not a single point. Name which trend could break the plan.
- **Boundary conditions:** The 10x-per-year figure applies to a fixed capability level. Products that need the frontier model pay frontier prices, which fall more slowly. Benchmark contamination and methodology caveats apply (Appenzeller notes them).

### D6. Reduce model complexity; choose problem domains narrowly
- **Claim:** The 2020 advice is to run one shared model across customers where possible and to prefer high-volume, lower-complexity tasks over open-ended ones. Before assuming ML is needed, test whether a simpler approach works. Make model economics visible early by checking whether accuracy gains justify their training and maintenance cost.
- **Source:** "The New Business of AI"; "Taming the Tail" (2020).
- **Changes coaching how:** The coach asks the user whether each AI component earns its complexity, and whether a rules-based or smaller-model version would meet the bar. This is a hype-discipline move that executives respect.
- **Boundary conditions:** Enterprise buyers increasingly demand process-specific customization (MIT NANDA, 2025). There is a real tension between what customers want customized and what keeps margins healthy. Resolve it per segment.

### D7. The pricing unit is a strategic choice, not an afterthought
- **Claim:** Packaging: put AI into the core offering when everyone values it and it drives adoption, into an upgrade tier when it is a strong nice-to-have, or into an add-on for power users who get outsized value. Seat pricing lets heavy users erode margin. Hybrid seat-plus-credit models manage that. Outcome-based pricing aligns incentives but needs an agreed outcome definition and reliable AI performance (Mar 2024). Watch for "AI tourists," novelty or mandate-driven buyers who churn. CIOs surveyed in 2025 preferred usage-based to outcome-based pricing because of measurement, attribution and cost-predictability concerns. Erten (Apr 2026) argues the unit is the most underused lever: discount the proof of concept, not the product. She reports premium positions sustaining 10-20% price premiums without material churn in her observation.
- **Source:** "Pricing and Packaging" (2024); "How 100 Enterprise CIOs..." (2025); "Surviving AI Price Wars" (2026).
- **Changes coaching how:** The coach asks the user to state the pricing unit and show how it tracks both customer value and cost to serve. It asks for cohort retention to separate real adopters from AI tourists. For outcome pricing, it asks what eval or measurement system would settle billing disputes.
- **Boundary conditions:** Pricing is usually owned by finance, sales or a pricing team. The user's lever is supplying the value and cost evidence, not deciding alone.

### D8. Enterprise AI buying has matured into procurement
- **Claim:** By mid-2025, per a16z's survey of about 100 CIOs, AI spend had moved from innovation budgets (25% down to 7% of LLM spend) into permanent lines. Multi-model deployment was common (37% running five or more models). Buyers shifted toward third-party applications. Procurement used disciplined evaluation, with security and cost gaining weight because most models perform adequately. Switching costs were rising as agentic workflows accumulated prompt tuning and QA.
- **Source:** "How 100 Enterprise CIOs Are Building and Buying Gen AI in 2025" (Jun 2025).
- **Changes coaching how:** If the user sells AI to enterprises, the coach prepares them for buyer-run evals, security review and cost scrutiny, and for proving value beyond a demo. If the user buys, the coach pushes for an internal eval harness so the company can keep multiple models and switch.
- **Boundary conditions:** This is a survey of a sample reached by an investor with portfolio interests, and it reflects one year's snapshot.

### D9. Build, buy or partner is an economic decision that keeps moving
- **Claim:** In 2023 a16z advised most startups to start on hosted model APIs rather than owning infrastructure. In 2026 Erten argues that as inference gets cheaper, building internally becomes cost-competitive with vendors. Vendors then defend through deep workflow integration, continuous model improvement, domain data and forward-deployed engineers. A counterweight outside a16z: MIT NANDA (Jul 2025) found external partnerships reached deployment about 67% of the time against about 33% for internal builds. The report flags this as self-reported and possibly confounded.
- **Source:** "Navigating the High Cost of AI Compute" (2023); "Surviving AI Price Wars" (2026); NANDA "The GenAI Divide" (2025).
- **Changes coaching how:** The coach runs build/buy/partner as a table with total cost (including evals, monitoring, maintenance and people), time to value, differentiation, and switching cost. It asks whether the capability is core to how the company wins. A decision made in 2024 should be revisited when prices or model quality shift.
- **Boundary conditions:** Buying does not remove the need for internal evals; the company still has to verify vendor quality on its own tasks.

### D10. Separate the macro AI bubble debate from your product's unit economics
- **Claim:** Cahn (Sequoia, Jun 2024) estimated a roughly $600B annual revenue gap implied by GPU infrastructure spend. He predicted value would go to infrastructure builders and to companies delivering real value to end users, while speculative capital could be destroyed. He also warned that GPU compute would get commoditized and depreciate quickly.
- **Source:** "AI's $600B Question" (2024).
- **Changes coaching how:** In board or executive conversations, the coach helps the user keep two questions apart. First, is the industry over-invested? That is not the user's call. Second, does this bet have positive unit economics and a path to durable value? That is the user's call. Hype should not justify spending, and bubble talk should not kill a bet with sound unit economics.
- **Boundary conditions:** The macro numbers are stale within months. Use them only to frame the conversation.

## Frameworks in operational form
**AI unit economics sheet for the CFO (from D1, D2, D5):**
| Line | What to estimate | Now | 12 mo (low/high) |
|---|---|---|---|
| Revenue unit | seat, credit, task, outcome | | |
| Inference | price per token x tokens per task x tasks per unit | | |
| Retrieval, infra, storage | per unit | | |
| Human in the loop | review minutes per task x loaded cost | | |
| Customization | per-customer engineering and FDE time | | |
| Evals and monitoring | people plus tooling | | |
| Gross margin | blended, and dilution of the existing product's margin | | |
Close with the single assumption that would most change the answer and how it will be monitored.

**Long-tail diagnosis (from D3):** (1) Sample about 100 real requests or failures. (2) Are failures concentrated in a fat head of cases, or spread thin? (3) Do failure patterns repeat across customers (global) or differ by customer (local)? (4) Pick a remedy: narrow, convert (human failover), componentize, or shared model. (5) State the cost per remaining edge case.

**Moat audit (from D4):** For each claimed advantage, record: evidence that more of it improves the product; who else could get it; its decay rate; whether it survives the next foundation model release; and how much switching cost it creates for the customer.

**Build/buy/partner table (from D9):** columns are build, buy, partner. Rows are total 24-month cost, time to first value, differentiation, required internal skills, switching cost, eval ownership, and data exposure. Decide, then set a trigger for revisiting (price change, quality change, vendor viability).

## Diagnostic questions
- What is the gross margin of the user's AI product or feature today, and can the user derive it on a whiteboard?
- Which cost line grows fastest with usage, and which one with customer count?
- How much human work does each unit of AI output need, and is that share falling?
- Is the tail global or local, and what remedy is in use?
- What would a competitor need to replicate the product if the underlying model became free?
- Does the pricing unit move with both value delivered and cost to serve?
- When was the build/buy decision last revisited, and what has changed since?

## Observable signals
Positive:
- The user brings cost-per-task and margin scenarios to executive reviews without being asked.
- The user names the services component and presents a dated automation plan.
- The user's moat claims come with evidence about data curves, workflow lock-in or distribution.
- The user proposes a pricing unit with retention cohorts that separate real adopters from AI tourists.
- The user revisits build/buy when model prices or quality shift, and documents the trigger.

Negative:
- The user reports AI revenue or adoption with no cost side.
- The user describes "our proprietary data" or "our model" as the moat without evidence.
- The user promises per-customer customization in deals without costing it.
- The user cites industry hype or bubble headlines instead of the product's own economics.
- The user treats a vendor purchase as removing the need for internal quality measurement.

## Anti-patterns and misuse
- Applying 2020 margin numbers to LLM-era products without re-dating them.
- Treating "AI economics are worse than SaaS" as a reason never to ship. The point is to plan for the costs, not avoid the work.
- Assuming falling token prices will fix margins, while tokens per task rise faster.
- Copying venture-scale "grow now, margins later" logic into a mature company whose CFO is judged on margin.
- Overbuilding outcome-based pricing before the product has evals reliable enough to settle billing.

## Tensions with other sources
- **Ng vs. a16z on cost timing:** Ng (2024) says not to optimize token cost prematurely and to deploy marginally uneconomic apps in anticipation of price drops. Casado, Bornstein and Bessemer emphasize margins and variable costs. Ng is more right in the exploration phase and on internal tools. a16z is more right at scale, and when a CFO must commit to a margin plan.
- **Slootman (margin and efficiency discipline) vs. Supernova-style growth:** Slootman would not accept 25% margins as a strategy. Venture-backed hypergrowth sometimes rationally does. Inside an established company, Slootman's discipline usually applies.
- **Bezos/Amazon on accepting thin margins for scale vs. Casado on durable margins:** the Amazon logic holds only with a credible path to scale economics or lock-in. Without that, low AI margins are just low margins.
- **Rumelt on sources of advantage:** Rumelt agrees that advantage needs a specific, hard-to-copy asset. That reinforces the moat audit and rejects "we use AI" as a strategy.
- **Charan on how the business makes money:** consistent with this source. The user must connect AI to cash, margin, velocity and growth, not just to capability.
- **Duke on forecasting:** cost curves are forecasts. Present them as probability ranges with named assumptions.
- **Within this cluster:** NANDA favors buying and partnering; Erten (2026) warns that cheaper inference makes building competitive; Ng favors in-house capability over time. The table in D9 is where the user resolves this for a specific case.

## Limits and biases
- Venture lens: these authors optimize for venture outcomes and hold positions in both infrastructure and application companies. Their framing can favor narratives that support portfolio companies.
- Evidence quality: margins and cost shares come from portfolio observation and surveys, not audited disclosures. Samples are small and US-centric.
- Era: the 2019-2020 pieces predate LLMs. The 2023 compute-shortage framing was superseded as capacity expanded and prices fell. The 2024-2026 pricing guidance reflects a market still moving fast. Re-date any number before using it with finance.
- Company type: the doctrine is written for startups. Inside an established company, the relevant quantities are margin dilution, cost per task and budget ownership, not startup gross margin.
- The Sequoia and Bessemer cross-checks share the venture lens. No independent academic source on AI app margins was consulted.

## Skill mapping
| Doctrine | Skill(s) | How the skill should use it |
|---|---|---|
| D1 | enterprise-thinking, board-communication | Require margin and cost-per-task alongside AI revenue or adoption |
| D2 | enterprise-thinking, ai-product-leadership | Surface services creep and a dated automation plan |
| D3 | ai-product-leadership, product-leadership | Classify the long tail and name the remedy before promising scale |
| D4 | ai-product-leadership, board-communication | Run the moat audit on any "data/model is our moat" claim |
| D5 | enterprise-thinking, evidence-discipline | Build three-trend cost models and present ranges |
| D6 | decision-making, ai-product-leadership | Challenge unnecessary model complexity as hype discipline |
| D7 | enterprise-thinking, product-leadership | Test the pricing unit against value, cost and retention |
| D8 | ai-product-leadership, executive-communication | Prepare for buyer-run evals; keep an internal harness for model switching |
| D9 | decision-making, portfolio-strategy | Run build/buy/partner as a costed table with revisit triggers |
| D10 | board-communication, executive-communication | Separate macro bubble talk from the product's own unit economics |

## Verified quotations
- "you can replace the services firm, but you can't (completely) replace the services" (Casado & Bornstein, "The New Business of AI," a16z, Feb 16, 2020).
- "How you charge is as much a competitive lever as what you charge." (Erten, "Surviving AI Price Wars Without Destroying Your Business," a16z, Apr 13, 2026).
