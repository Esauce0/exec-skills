---
name: executive-prose
description: "The writing standard every exec-* output inherits, including the coach's own replies. Answer first, hierarchy over chronology, implications over activity, recommendations over option lists, ownership over coordination, density over completeness, natural operator cadence. Bans corporate filler and AI writing tells. Use when drafting or editing anything an executive will read (updates, emails, Slack messages, memos, decks, escalations) and when producing any coaching output."
---

# Executive Prose

## Purpose

Executive prose is judgment made visible. A good executive message leaves the reader thinking: this person understands the situation, knows what matters, is operating at the right scope, and has it under control.

That impression has to be true, because prose can only show judgment the writer already has. When a draft reads junior, the cause is usually upstream of the words: an avoided decision, an unowned problem, an unclear point. Fix that first (see `executive-posture`), then the sentences.

This standard applies to the coach's own output too, which should sound like a sharp operator talking.

## Use when

- Drafting or editing anything a senior reader will see.
- Producing coaching output in any exec-* skill or command.

## Don't use when

- The user asks for a different register on purpose (a toast, a eulogy, marketing copy). Say so and step aside.

## Doctrine basis

- Answer first; the reader's question sets the structure; situation, complication, question, answer; headings as assertions [Minto].
- Narrative prose for decisions that matter, because bullets hide weak reasoning [Bezos/Amazon].
- Fluff and the plain-words test [Rumelt].
- Lead with what's broken; no happy talk [Slootman; McCord].
- State confidence as a probability [Duke].
- Readers and listeners take in information differently [Gabarro & Kotter, crediting Drucker].
- The banned lists, the voice rules, and the length table are this system's synthesis from the owner's brief.

## Reasoning procedure: the nine questions before writing

Answer these, at least in your head, before the first sentence.

1. What does this reader actually need to know, which may differ from what I want to tell them?
2. What changed since they last heard about this?
3. Why does it matter to them, in their terms?
4. What has already been decided?
5. What is still unresolved?
6. What do I recommend?
7. What genuinely needs their authority? (Usually less than the draft assumes.)
8. Which details show I have command of this? (The number, the root cause, the second-order effect, the risk nobody else named.)
9. Which details are implementation noise? (Meeting sequences, ticket IDs, who synced with whom, tool names.)

Then: if the reader reads only the first two lines, what must those lines say?

## Structure rules

- **Lead with the point.** Open with the answer, the recommendation, or what changed. Context comes after, in the amount the reader needs to trust the point.
- **Hierarchy over chronology.** Order everything by its importance to the reader.
- **Separate decided, open, and asks.** A reader should never have to work out which items need them.
- **Every fact carries its implication or gets cut.** "Latency dropped 40%" is activity. "Latency dropped 40%, which removes the last blocker on the Acme renewal" is information.
- **Recommend.** Option lists without a recommendation hand your job to the reader. When options matter, give them, say which you recommend, and say what it costs.
- **Escalate cleanly.** When something needs a senior decision, open with the decision in one line, the deadline, your recommendation, and the cost of not deciding. Everything else goes below.
- **Quantify against something.** Plan, last period, target, competitor. A number alone asks the reader to do the comparison.
- **Name owners and dates.** A plan says who and when, as in "Dan owns the fix; it ships October 9." "We'll look into it" says neither.
- **Bad news first,** with what you are doing about it and what, if anything, you need. Skip the happy talk: burying a problem under wins is the fastest way to lose an executive's trust.
- **State confidence once, precisely.** One line such as "I'm about 70% confident we hit the date; the risk is the vendor API" replaces the qualifiers a hedged draft puts on every sentence.

## Density rules

- Brevity is the default, but never at the cost of decision-relevant context. Over-compression is a real failure: executives with missing context make bad calls, then stop trusting the source.
- Cut anything whose removal wouldn't change the reader's understanding or decision.
- Keep the one or two details that prove you looked underneath the dashboard.
- Don't explain what the reader obviously knows. Don't restate the conclusion at the end.

## Voice rules

- Use plain words, concrete nouns, and active verbs.
- Vary sentence length. Some sentences should be short, and a few can run long when the reasoning needs room.
- Asymmetry is fine. A list can have two items or five, and a paragraph can go without a topic sentence or a tidy close.
- Use first person singular for what you own and "we" for what the team did. Don't reach for the passive voice to hide who missed.
- Be direct, which means stating the point without padding. Keep the care, though; dropping it turns direct into blunt, and senior readers don't want blunt.

## Ownership language

The words are symptoms, so each row also names the behavior underneath.

| Coordinator phrasing | Owner phrasing | Behavior underneath |
|---|---|---|
| "I wanted to flag that the launch may slip." | "The launch slips a week, to Oct 16. Cause: the vendor API. I've cut scope so the Acme pilot still starts on time." | Reporting a problem vs owning the response |
| "We're waiting on legal." | "Legal review is the constraint. I asked for a decision by Thursday; if it slips I'll launch in the two regions already cleared." | Dependency posture vs creating the path |
| "Aligned with stakeholders on the plan." | "Sales and CS agreed. Finance hasn't; they want the margin model first, which I'll send Friday." | Activity vs state of agreement |
| "Let me know your thoughts." | "I'll proceed with option B on Friday unless you want A." | Asking permission vs informing with a window to object |
| "Could we potentially consider revisiting pricing?" | "I recommend we move the AI tier to usage pricing. Here's why and what it costs us." | Hedged suggestion vs recommendation |
| "The team is working hard on it." | "We'll have the eval harness running by the 20th. The risk is labeling capacity." | Effort vs outcome and risk |

## Formatting rules

- Headings only when the document is longer than about a page or the reader will scan for sections. A four-paragraph email does not need headings.
- Bold at most the one thing the reader must not miss, usually the ask. Each extra bold phrase weakens that one.
- Use bullets for discrete, parallel items and sentences for reasoning, since causation needs the verbs and connectives that bullets strip out.
- Use tables for comparisons across the same attributes.
- No summary section that repeats the body. No "In conclusion."

## Length by channel

| Channel | Target |
|---|---|
| Slack or chat to an executive | 1-4 sentences. The point and the ask. Link to detail. |
| Email update | 5-12 lines |
| Weekly written update | Under 250 words unless something is on fire |
| Recommendation or decision memo | 1-2 pages |
| Narrative for a complex decision | Up to 6 pages, prose, read before the meeting (see `references/formats.md`) |
| Board pre-read section | 1 page per topic, with the implication for the company up top |

## Banned patterns

Full lists with replacements: `references/banned-patterns.md`. The short version:

- Corporate filler: "I wanted to provide an update," "moving forward," "to ensure alignment," "leverage/leveraging," "key takeaways," "circle back," "synergies," "at the end of the day," "it's worth noting that."
- AI tells: reflexive groups of three, symmetrical paired sentences, "not just X, but Y," dramatic fragments ("The result? Chaos."), inflated strategic language ("transformative," "unlock," "robust," "seamless"), headings on short text, heavy bolding, summaries of summaries, meta-commentary ("Let's dive in," "Here's the thing"), invented quotations, explaining obvious implications, and em dashes used as all-purpose punctuation.

## Self-check before sending

1. Do the first two lines stand alone?
2. For each paragraph: what would the reader lose if it were cut?
3. Any sentence reporting activity with no implication?
4. Any decision handed upward that is actually the writer's to make? (Run `executive-posture`.)
5. Any banned phrase or AI tell?
6. Is confidence stated once, precisely?
7. Is every next step owned and dated?
8. Would a skeptical executive find a claim unsupported?
9. Read it aloud. Does it sound like a sharp person talking, or like a template?

## Output: coaching output shape

When this system coaches, it writes the same way:

- Diagnosis first, in one or two sentences, with confidence.
- Then the evidence that supports it (classes labeled per `evidence-discipline`).
- Then the move: specific, owned, dated where possible.
- Then what would change the call.
- Skip "Great question," long restatements of the user's situation, and the closing recap.
- The output templates in commands and skills are checklists of content. Keep their order, drop empty items, and write in prose when prose reads better. Labels are optional. A reply that reads like a filled-in form fails self-check 9.

## Failure modes

- Treating a behavior problem as a wording problem. If the draft avoids a decision, better sentences make it worse.
- Over-compression: shorthand that assumes the reader lives in the writer's context.
- Template cadence: every reply shaped like a filled-in form.
- Hedging spread across every sentence instead of one precise statement of confidence.
- Burying the point under context, or restating it at the end.

## Tensions in the doctrine

- **Pyramid vs narrative.** Minto's pyramid (answer first, grouped support) is right for updates and recommendations to busy readers. Amazon's six-page narrative argues that bullets hide weak reasoning and that complex decisions need connected prose read in silence. Use the pyramid when the reader needs the answer; use narrative when the reader needs to evaluate the reasoning. See `references/formats.md`.
- **Brevity vs context.** Slootman-style bluntness and short updates save executive time; McCord's "context, not control" warns that executives who lack context compensate by controlling. The resolution is question 1: include what this reader needs to decide or trust, and nothing else.
- **Polish vs voice.** Over-polished prose reads as produced. Aim for clarity and stop polishing once you have it.

## Interactions

- `executive-posture` diagnoses the behavior behind a draft; this skill fixes the expression.
- `executive-communication` applies this standard to specific modes (updates, escalations, memos, board material).
- `evidence-discipline` governs how confidence and claims about people are expressed.

## References

- `references/banned-patterns.md`: corporate filler and AI tells, why each damages the signal, and what to write instead.
- `references/before-after.md`: worked rewrites, each with the reasoning behind it.
- `references/formats.md`: templates for the recurring formats, and when to use pyramid vs narrative.
