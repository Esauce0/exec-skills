---
name: doctrine-library
description: "Runtime access to the researched source doctrine behind the exec-* skills: Campbell, Cagan, Doshi, Grove, Hughes Johnson, Charan, McCord, Horowitz, Scott, Slootman, Pfeffer, Hewlett, Watkins, Ibarra, Minto, Lencioni, Larson, Bezos/Amazon, Duke, Rumelt, and others. Use when the user asks what a specific thinker's documented view is, when a skill needs deeper doctrine than its own references, or when sources disagree and the disagreement needs adjudicating for a real situation. Never role-plays or imitates the thinkers."
---

# Doctrine Library

## Purpose

The exec-* skills are organized by job, and the thinkers behind them serve as sources. This library holds the researched dossier for each source so a skill (or the user) can go one level deeper: the exact framework, its boundary conditions, where the source is weak, and where it disagrees with others.

## Use when

- The user asks "what does Grove say about..." or "is this Pfeffer or Campbell territory?"
- A skill's own references don't settle a question and the source material might.
- Two sources point in opposite directions for the user's actual situation.
- Checking whether a piece of advice really has doctrinal support or is folk wisdom.

## Don't use when

- The user wants advice. Route to the job skill; it already synthesizes the sources.
- Anyone asks for an imitation ("answer as Bill Campbell would"). Decline the persona and offer the doctrine: "Here is what his documented approach implies for your situation."

## How to use

1. Open `references/_index.md` to find the relevant dossiers (each lists the skills it feeds and its role in the system).
2. Read only the sections you need. Each dossier has: why the source matters, primary sources, operational doctrine entries (claim, source, how it changes coaching, boundary conditions), frameworks, diagnostic questions, observable signals, anti-patterns, tensions with other sources, limits and biases, and skill mapping.
3. When citing, attribute the idea to the source and the work, in paraphrase. Quote only the short verified quotations in a dossier's "Verified quotations" section. Never invent or reconstruct a quotation.

## Adjudicating disagreements

Sources disagree on things that matter: politics, candor upward, loyalty, speed vs process, empowerment vs command. When they do:

1. State both positions accurately, with their sources.
2. Identify the conditions each position was formed in (founder-CEO in hypergrowth, Fortune 500 transformation, a coach of CEOs, academic research across many firms).
3. Match those conditions to the user's actual situation from the Brain: company stage and culture, the user's level, the specific people involved.
4. Recommend which position governs *here*, and say what evidence would flip it.

Do not average the sources into mush. A real situation usually has a right answer for this user, even when the doctrine as a whole is split.

## Source hygiene

- Dossiers mark which primary sources were consulted directly and which are known by reference. Weight claims accordingly.
- Several sources come from specific contexts (Slootman: turnaround CEO; McCord: Netflix; Campbell: coach to founder-CEOs). Transfer to a PM in a mid-size company is not automatic; each dossier's "Limits and biases" section says where it breaks.
- The AI-specific sources date quickly. Check their dates before relying on them.

## Interactions

Every job skill names its primary sources. This library is where those names resolve.

## References

- `references/_index.md`: generated index of all dossiers.
- `references/<source-slug>.md`: one dossier per source, synced from the repository's `sources/` layer by `scripts/build.py`. Do not edit these copies directly.
