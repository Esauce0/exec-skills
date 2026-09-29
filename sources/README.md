# Sources

This is the authoring layer: one folder per source, each with a `doctrine.md` dossier researched against primary or authoritative material where it was accessible. Dossiers mark which works were consulted directly and which are known by reference.

Sources are never user-facing units. Their doctrine flows upward into the job-based skills, and the mapping is many-to-many, with each source feeding several skills and each skill drawing on several sources. See [../docs/doctrine-map.md](../docs/doctrine-map.md).

## Dossier contract

Frontmatter: `source`, `slug` (matches folder), `role-in-system`, `feeds-skills`, `last-researched`.

Sections: why this source matters here; primary sources; operational doctrine (each entry: claim, source, how it changes coaching, boundary conditions); frameworks in operational form; diagnostic questions; observable signals; anti-patterns and misuse; tensions with other sources; limits and biases; skill mapping; verified quotations.

The test for every doctrine entry: does it change the coach's diagnosis, questions, or recommendation? If not, it doesn't belong.

## Rules

- Paraphrase; don't reproduce passages.
- Quotations only if verified in a source read during research, under 15 words, with citation. No invented or reconstructed quotations.
- Flag uncertain attributions as uncertain.
- Record disagreements with other sources rather than smoothing them over.
- After editing, run `python scripts/build.py` to sync the runtime copies in `exec-core/skills/doctrine-library/references/`.

## Roster

Core: Bill Campbell, Marty Cagan, Shreyas Doshi, Andy Grove, Claire Hughes Johnson, Ram Charan, Patty McCord, Ben Horowitz, Kim Scott, Frank Slootman.

Added for direct relevance: Jeffrey Pfeffer (power, the realist counterweight), Sylvia Ann Hewlett (sponsorship, executive presence), Michael Watkins (transitions, the seven shifts), Herminia Ibarra (outsight, networks, sponsorship), Barbara Minto (pyramid principle).

Supplementary: Gabarro & Kotter, Marshall Goldsmith, Amazon/Bezos, Annie Duke, Richard Rumelt, Patrick Lencioni, Will Larson, Keith Rabois, Linda Hill, David Maister.

AI leadership: Andrew Ng, AI economics (a16z and cross-checks), AI evals practitioners (Husain, Shankar, Yan and co-authors), AI product operators (Mollick and others). These date quickly; check `last-researched` and the dates inside.
