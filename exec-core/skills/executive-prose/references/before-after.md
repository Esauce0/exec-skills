# Before and after

Each example shows the draft, the diagnosis (behavior first, words second), the rewrite, and why. The names and products are illustrative.

---

## 1. Weekly update that escalates decisions the writer owns

**Draft**

> Hi Maria, I wanted to provide a quick update on the Copilot workstream. This week we had several productive syncs with Eng, Design, and Legal to ensure alignment on the beta. A few items where I'd love your input:
> 1. Should we launch the beta to 5% or 10% of accounts?
> 2. Should we include the summarization feature, given latency is still at 4.2s?
> 3. Legal wants a new disclosure in the UI. Should we push back?
> Let me know your thoughts! Key takeaways: beta on track, some open questions.

**Diagnosis.** Coordinator posture. Two of the three questions are squarely within a PM's scope (rollout percentage and whether a slow feature ships). Asking Maria to decide them signals the writer doesn't own the product's calls. The third might need her, but only if the disclosure changes the commercial story. The update reports meetings and never says where things stand.

**Rewrite**

> Copilot beta goes to 10% of accounts on Oct 14. Two calls I've made and one where I need you.
>
> I'm holding summarization out of the beta. Latency is 4.2s against our 2s bar, and a slow first impression costs more than a missing feature. It rejoins when we're under 2.5s; Eng estimates three weeks.
>
> Legal wants an AI disclosure banner on every response. I think a single disclosure at first use is enough, and it's what our two closest competitors do. **I need you to back that position with Legal by Friday**, or accept the banner, which our research suggests will cut usage (about 15% lower engagement in the prototype test).

**Why.** The decisions within scope are made and explained in one sentence each, which demonstrates judgment. Only the decision that needs Maria's authority (overruling Legal's default) goes up, with a recommendation, a deadline, and the cost of the alternative.

---

## 2. Slack message about a slip

**Draft**

> Hey! Just wanted to flag that there might be some potential delays on the eval harness due to some dependencies on the data platform team. We're working through it and will keep you posted!

**Diagnosis.** Vague, minimized ("just," "might," "some potential"), dependency posture ("due to dependencies"), no date, no plan, no ask. An executive reading this learns only that something is wrong and that the writer isn't in control of it.

**Rewrite**

> Eval harness slips from Oct 3 to Oct 17. Data platform can't deliver the labeled set until the 10th. I've started with the 2k examples we already have, so the first quality read still lands on the 3rd. No action needed from you.

**Why.** Four sentences give the date, the cause, the mitigation, and whether the reader needs to act.

---

## 3. Options with no recommendation

**Draft**

> For the model provider decision, here are the options:
> - Option A: Stay with Vendor X. Pros: already integrated. Cons: cost.
> - Option B: Move to Vendor Y. Pros: cheaper, better on our evals. Cons: migration effort.
> - Option C: Self-host an open-weights model. Pros: control, cost at scale. Cons: need ML infra.
> Happy to discuss!

**Diagnosis.** Expert posture: analysis with no synthesis (Watkins calls the fix the analyst-to-integrator shift). The work of choosing was handed to the reader. The pros and cons are generic and unquantified, which hides whether the writer did the analysis.

**Rewrite**

> I recommend moving the summarization workload to Vendor Y in Q4 and staying on Vendor X for everything else.
>
> Y beats X on our eval set (91% vs 86% acceptable summaries) at about 40% of the cost. Summarization is 70% of our inference spend, so the switch takes roughly $310k off the annual run rate and moves AI gross margin from 52% to 61%. Migration is about three engineer-weeks because summarization sits behind one interface.
>
> I'm not recommending self-hosting. It only wins above roughly 5x our current volume, and we'd need an ML infra hire we don't have.
>
> If you agree, I'll start the migration Oct 20 and report quality weekly for the first month.

**Why.** The recommendation comes first. The numbers that matter to an executive (quality, cost, margin, effort) replace generic pros and cons. The rejected option is dismissed with its break-even condition, which shows the writer understands when the answer would change.

---

## 4. Cross-team escalation

**Draft**

> The data platform team keeps deprioritizing our requests, which is blocking our roadmap. Can you talk to Sam about this? It's really impacting our ability to deliver.

**Diagnosis.** Complaint framed as escalation. No specific decision is requested, no tradeoff is named, and it asks the boss to fight a peer's battle without evidence that the writer tried to resolve it. The writer comes across as a warrior when the moment calls for a diplomat.

**Rewrite**

> Sam and I need a priority call from you and Priya on the data platform's Q4 queue.
>
> The conflict: the labeled-data pipeline we need for AI quality competes with the billing migration. Sam can staff one this quarter. We agree on the facts; we disagree on the ranking.
>
> My case for the pipeline: without it we can't measure quality on the enterprise tier, which is the main renewal risk for Acme and Globex ($2.1M ARR, renewals in January). Sam's case for billing: the migration retires a system with a known compliance gap.
>
> Sam and I are sending this jointly. We'd like a decision by Oct 10 so Q4 planning isn't blocked.

**Why.** The escalation is a clean decision request, made jointly with the peer, stating both sides fairly. That signals the writer handles conflict at an organizational level, which is exactly what an escalation otherwise puts at risk.

---

## 5. Bad news buried under wins

**Draft**

> Great month for the assistant! Weekly actives up 22%, NPS up 6 points, and we shipped three new skills. We also saw some increase in hallucination reports, which we're monitoring closely. Next month we're focused on continued growth.

**Diagnosis.** Happy talk. The most important fact, a quality regression in a probabilistic system that enterprise customers depend on, is minimized and placed last. When the executive learns the size of it from someone else, trust in every future update drops.

**Rewrite**

> Hallucination reports doubled this month (41 to 87 per 10k sessions), almost all in the three new skills. I've pulled two of them back to internal-only until they pass our eval bar; the third is fixed.
>
> Usage is otherwise strong: weekly actives up 22%, NPS up 6. But I'd rather slow skill launches than grow on a quality problem our enterprise customers will find. New skills now need to clear the eval suite before release, which adds about a week to each launch.

**Why.** Bad news first, sized, with action already taken and a process change that prevents recurrence. The good numbers still appear, in their proper place.

---

## 6. The opposite failure: over-compression

**Draft**

> Acme: RAG v2 blocked on ACLs. Pinged SecEng. ETA TBD.

**Diagnosis.** Brevity that removes the context a VP needs. Which customer impact? Why does it matter? What's the plan if SecEng doesn't answer? The shorthand assumes the reader lives in the writer's context.

**Rewrite**

> The Acme rollout is blocked: our retrieval can surface documents a user shouldn't see, because we don't yet enforce their SharePoint permissions. We can't ship to Acme until that's fixed. Security engineering owns the permission service and hasn't committed a date. I'm meeting their lead Thursday; if there's no date by then I'll ask you to raise it with Priya, since Acme's pilot decision is Nov 1.

**Why.** Five sentences restore what the reader needs to judge the risk: the customer, the actual problem in plain words, the owner, the deadline, and the escalation trigger.

---

## 7. Executive theater

**Draft**

> As we think holistically about our AI strategy, it's clear we're at an inflection point. To unlock transformative value, we must move beyond point solutions toward a platform approach that leverages our proprietary data as a durable moat.

**Diagnosis.** Senior vocabulary with no claim a reader could disagree with: it names no choice, cost, number, or owner. Rumelt would call it fluff: the language of strategy without the diagnosis or the choice.

**Rewrite**

> I think we should stop building one-off AI features per product team and fund one shared retrieval and evaluation layer instead. Three teams are building the same pipeline today, which costs us roughly four engineers and produces inconsistent quality. The real advantage is our support-ticket history: 8 years of resolved cases no competitor has. The shared layer is how we use it everywhere. It means pausing two feature launches in Q1. I'd like 30 minutes at the next staff meeting to make the case.

**Why.** The strategic claim becomes a specific choice with a diagnosis, a cost, the asset that makes it defensible, and an ask. Now it can be argued with, which is what makes it strategy.
