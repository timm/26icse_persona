# ICSE 2027 Research Track Submission

Working on a paper for the ICSE 2027 Research Track. CFP source: `docs/cfp.txt`. Structural recipe and writing conventions: `docs/paper-style.md`. Theoretical frame / background synthesis: `docs/background.md`. Validation plan for the composite persona claim: `docs/validation-plan.md`. Reference PDFs in `refs/`. Submission draft in `paper/`.

## Hard formatting rules

- LaTeX class: `\documentclass[10pt,conference]{IEEEtran}` — **do not** include `compsoc` or `compsocconf` options.
- Title 24pt, body 10pt.
- Main text: max **10 pages** inclusive of figures, tables, appendices.
- References: up to **2 additional pages** (references only).
- Accepted papers: +1 extra main-text page for camera-ready.
- Major-revision papers: +1 extra page for the revised version to accommodate required changes.
- Desk-reject risk if spacing/font deviates from IEEE template — do not tweak.
- PDF only.

## Double-anonymous rules

- No author names or affiliations in the PDF.
- Refer to your own prior work in the **third person**.
- If posting a preprint on arXiv, **do not** mention ICSE 2027 submission; prefer to delay posting until after notification.
- Do not contact PC members directly — all communication via program chairs.

## Key dates (AoE, UTC-12)

| Milestone | Date |
|---|---|
| Abstract (mandatory) | 2026-06-23 |
| Submission | 2026-06-30 |
| Author response (3 days) | 2026-09-23 to 2026-09-25 |
| Notification | 2026-10-20 |
| Revision due | 2026-11-17 |
| Camera-ready (direct accept) | 2026-11-24 |
| Final decision (major rev) | 2026-12-18 |
| Camera-ready (major rev accept) | 2027-01-25 |

Submission site: https://icse2027.hotcrp.com/

## Review criteria (address explicitly)

1. **Novelty** — originality vs. state-of-the-art.
2. **Rigor** — soundness, depth, evaluation completeness.
3. **Relevance** — significance/impact for SE.
4. **Verifiability & Transparency** — enough detail for replication; artifact checked by one reviewer.
5. **Presentation** — clarity of exposition.

Outcomes: Accept / Major Revision / Reject.

## Open science

- Default: share artifacts (anonymized link at submission; public upon acceptance).
- Non-sharing must be justified in the paper.
- Qualitative studies: follow reporting guidelines rather than reproducibility mandate.

## GenAI disclosure

- Using GenAI for **content generation** (text, tables, code, citations, data) → disclose in Acknowledgements, cite the AI system.
- Using GenAI purely for **editing/grammar** (Grammarly-style) → no disclosure required.
- GenAI cannot be listed as an author.

## Research areas (pick one, optionally a second)

AI for SE · Analytics · Architecture and Design · Dependability and Security · Evolution · Human and Social Aspects · Requirements and Modeling · SE for AI · Testing and Analysis

## Writing conventions for this repo

- Keep research notes, outline, related-work summaries in separate markdown files under `docs/` — not in this file.
- This file is rules-only; update it if the CFP is revised.
- Structural recipe for the paper (intro, discussion, TTV, etc.) lives in `docs/paper-style.md` — follow it when drafting.
