# Changelog

## v0.1.0 — 2026-09-29

First version.

- 7 plugins: exec-core, exec-observer, exec-trajectory, exec-influence, exec-communication, exec-leadership, exec-product-leadership.
- 20 skills, 16 commands.
- 29 researched source dossiers in `sources/`, synced into `exec-core:doctrine-library`.
- Career Brain scaffold (schema version 1) with evidence log, people files, trajectory models, meetings, reviews, and a Product Brain registry compatible with pm-brain scaffolds.
- `scripts/build.py` and `scripts/validate.py`.

Hardening after an independent review, same day:
- Fixed misattributions (Pfeffer on superiors, "scope is taken", Grove/Hughes Johnson on context, Maister's "intimacy") and a canonical example that treated a motive as an inference.
- Resolved contradictions: follow-up notes (ownership vs coordination), sponsorship as a relationship type, autonomy rules for ledgers and `self/`, `visibility+` logged before it happened.
- `/position-for-promotion` now requires ruling unreadiness and fit in or out on evidence.
- Provenance tags aligned with pm-brain, with a translation table; person hypotheses namespaced `H-P-<slug>-<n>`; rate forecasts only at medium confidence.
- Scaffold templates renamed `.tmpl` so the plugin copy is never mistaken for a live Brain.
- Every domain skill gained Standards, Evidence to gather, and Diagnostic questions sections; standards and observer skills gained a Doctrine basis that labels system synthesis.
- Build generates the doctrine map from actual citations and regenerates plugin README lists; the validator checks sections, vocabularies, YAML, and long Windows paths.
- Editing pass removing roughly two thirds of the contrastive "X, not Y" constructions and other tics from the repo's own text.
