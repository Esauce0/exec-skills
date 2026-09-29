# Models

Models are derived from evidence. They change through reviews (`/review-my-month`, `/career-retrospective`) or when a single piece of evidence is strong enough under the confidence rules. Every hypothesis uses the format in exec-core `evidence-discipline/references/hypothesis-format.md`:

```markdown
### H-<AREA><n>: <claim stated so it can be wrong>
- **Subject:**
- **Confidence:** low | medium | high
- **Evidence for:**
  - <claim>  `<provenance>`
- **Evidence against:**
  - <claim>  `<provenance>`
- **Strongest alternative explanation:**
- **Would weaken if:**
- **Would strengthen if:**
- **Cheapest test:**
- **Status:** active | supported | weakened | retired
- **Opened:** YYYY-MM-DD
- **Last reviewed:** YYYY-MM-DD
- **Notes:**
```

Area codes: R reputation, S sponsorship, V visibility, C scope, D readiness, T trajectory. Person-level hypotheses live in people files as H-P-<slug>-<n>.

Each model file has a `Last reviewed` date at the top. Files older than 45 days get flagged.

| File | Holds |
|---|---|
| scope.md | Ledger of what the owner owns, across the dimensions senior leaders allocate |
| sponsorship.md | Who advocates for the owner, at what level, on what evidence |
| visibility.md | Who sees the owner's work, what they see, whether it's attributed |
| reputation.md | How key people likely describe the owner, as hypotheses |
| readiness.md | Next-level gap by dimension |
| trajectory.md | The synthesis: direction, leading indicators, drift, the top moves |
