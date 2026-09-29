# Evidence-based stakeholder model

Used by `/analyze-stakeholder`. The model describes what a person is accountable for, what pressures them, what they've said and done, and how they relate to the user's work. It does not describe their personality.

## Rules

1. **Every claim has a date and a source.** Undated, unsourced claims go under Unknowns.
2. **Stated and observed priorities are separate.** The gap between them is often the most useful finding.
3. **Incentives before character.** Explain behavior first by what they're measured on, what their boss is pressing them on, what they stand to lose, and what just changed around them.
4. **No psychological characterization without strong, repeated evidence.** "Detail-oriented in reviews" can be evidenced from behavior. "Insecure" or "political" cannot, and shouldn't be written.
5. **Hypotheses in hypothesis format,** with the strongest alternative explanation and a falsifier.
6. **Say what you don't know.** Unknowns that would change how the user works with the person are listed as questions to answer.

## Sections

| Section | Content | Best evidence |
|---|---|---|
| Accountabilities | What they're measured on; what their boss holds them to | OKRs, org announcements, their own updates |
| Stated priorities | Their words, dated | Meeting notes, all-hands, docs they wrote |
| Observed priorities | What they spend attention on, fund, ask about, push back on | Repeated behavior across meetings |
| Pressures and incentives | What's at risk for them; what changed around them | Their boss's priorities; reorgs; misses in their area |
| Communication preferences | Reader or listener; detail level; pre-reads; pre-wiring; channel; timing | Observed reactions to different formats |
| Relationship history with the user | Interactions, dated, with what happened | Evidence entries, meeting debriefs |
| Trust signals | Allocation first, then direct statements, then behavior | Evidence entries tagged trust+/- |
| Friction | Dated incidents and concerns, both directions | Evidence entries |
| Influence | Formal power, informal reach, who influences them | Decision outcomes, forum membership |
| Opportunities to create value for them | Their problems the user is positioned to help with | Accountabilities + pressures + user's capabilities |
| Unknowns | What would change the approach if known | |

## The value question

The most useful output of a stakeholder model is usually the answer to: **what problem does this person have that the user is unusually positioned to help solve?** That is where relationships with senior people get built.

## Worked mini-example (illustrative)

> **Observed priority:** In the last three staff meetings (2026-08-14, 08-28, 09-11) Priya asked about inference cost before quality each time AI features came up. [evidence/2026/08/..., evidence/2026/09/...]
> **Stated priority:** Her Q3 all-hands named "AI quality and trust" as the top product priority. (document, Q3 all-hands deck, 2026-07-02)
> **Pressure (inference):** The CFO flagged AI gross margin in the Q2 board deck (reported-by, Dan, 2026-07-20). A cost focus fits that pressure better than a change in her quality priority.
> **Hypothesis (low):** Priya will fund quality work that also reduces cost more readily than quality work alone. Would weaken if she approves the pure-quality eval proposal in October without asking about cost.
> **Value opportunity:** An eval harness that lets the team switch summarization to a cheaper model safely addresses both her stated and her observed priority.
