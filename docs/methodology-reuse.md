# SE4AI Methodology Reuse Map

How much of SE4AI's methodology transfers to our "is this a better GenderMag?" study. Purpose: decide what to adopt verbatim, adapt, or invent, before drafting §4 of the paper.

Source: `refs/SE4AI-2.pdf` — Estes, EsfandyariDoulabi, Khanmohammadi, "SE4AI: Requirements Level Explanations for Different Stakeholders", 2026.

Our four tests (from `validation-plan.md`): **Test 1** distinguishability, **Test 2** non-redundancy, **Test 3** predictive power (three-scheme ablation), **Test 4** actionability.

## What lifts directly

| SE4AI component | Location | Maps to |
|---|---|---|
| Structured JSON response schema (`accepts_recommendation`, `clarity_score`, `sufficiency_score`, `preferred_rank`, free-text reasoning) | §4.3.2 | Test 3 per-persona response format |
| LLM-as-Judge validation protocol (rubric scoring + blind classification, two independent judges) | §4.3.4 | **Test 1 in full** — extend rubric to 7 facets, classification to more classes |
| Reliability thresholds — Krippendorff α ≥ 0.80, Cohen κ ≥ 0.61, Spearman ρ | §4.3.4 | Test 1 pass/fail bars |
| Two-round counterbalanced design (Round A raw / Round B explained, with within-subject assignment) | §4.3.1 | Test 3 — adapt as raw vs. persona-mix-recommended |
| Pairwise Wilcoxon rank-sum with Bonferroni; sensitivity under three variance assumptions | §4.1 | Test 3 and Test 4 statistical tests |
| Failure-mode section (FM1 explanation surplus, FM2 role suppression, FM3 weakest facet) | §5.3 | Paper's TTV / limitations template |

## What adapts

| SE4AI component | How to adapt |
|---|---|
| Persona design as role × profile grid (3 × 3 = 9 cells) | Our grid is 7D sparse with weighted mixes. Same conceptual structure; different cardinality. Probably 20–30 representative personas rather than 9. |
| Hypotheses H1–H6 | H1 (Risk → TreeSelection), H2 (InfoProc → Engagement), H3 (SelfEfficacy → Confidence) carry over — these are cognitive-facet hypotheses. H4 (Role → Priority), H5 (TechLevel → Detail) also carry. **Need new hypotheses for Control and Now** — e.g., "Control=4 personas accept high-Sced actions more readily; Control=0 personas reject them." |
| Empirical run-count calibration (N=400 EZR runs, §4.1) | Relevant only if we use MOOT. If so, we inherit N=400 directly; if not, calibrate separately. |

## What's ours to invent

SE4AI validates *one* persona scheme. We compare *three*. The comparative design is not in their paper.

| Test | Why SE4AI doesn't cover it | What we design |
|---|---|---|
| Test 2: Non-redundancy | They don't attempt to show their persona axes aren't recoverable from simpler axes | `cocomo_facets ~ GM_facets` regression; R² or balanced accuracy; pass if R² < 0.3 |
| Test 3: Three-arm ablation | They have one scheme, not three | Scheme A (GM only) vs. B (cocomo only) vs. C (composite) on identical stimuli; measure divergence rate, rank correlation, Scott-Knott clusters |
| Test 4: Actionability | Their H4 (Role → Priority) stops at ranking differences; doesn't reach "different chosen action" | Run pain-calculus from `refs/cocomo__roshomon (1).pdf` §4 on SE recommendations; show chosen action differs across org-mix personas |
| Test 3 — rhetorical jackpot | They have no reason to find divergence cases | Case where Scheme A predicts persona agreement but Scheme C reveals disagreement driven by Control or Now — one clean figure for the paper |

## Design choice we inherit or challenge

**SE4AI accepts LLM-simulated personas as stand-ins for humans** (citing Schuller et al. 2024, CHI, which claims LLM-generated personas are empirically indistinguishable from human-written ones in perceived quality and acceptance).

Two paths:
1. **Inherit.** Cite SE4AI's defense, no human data needed. Faster, cheaper; inherits a single-paper load-bearing assumption.
2. **Challenge (partial).** Use LLM for Tests 1–3 as SE4AI does, but do a small (n = 5–10) human spot-check specifically on the **new axes** (Control, Now). If LLM and human responses correlate on the new dims, independent evidence. If not, a publishable finding regardless.

Path 2 is more defensible for ICSE reviewers who haven't yet accepted the Schuller argument.

## Paragraph for §4 of the paper (draft seed)

> To assess whether the composite 7-facet persona model adds insight beyond GenderMag's five cognitive facets, we adopt and extend the validation protocol of Estes et al. [SE4AI]. Specifically, we reuse their LLM-as-Judge framework (two independent judges, rubric scoring and blind classification) with Krippendorff α ≥ 0.80 and Cohen κ ≥ 0.61 as reliability thresholds, their structured JSON response schema, and their two-round counterbalanced evaluation design. We extend their framework in four ways: (1) the persona grid is 7-dimensional rather than 3 × 3; (2) we add hypotheses H7 and H8 covering the two organizational axes (Control, Now); (3) we compare three persona schemes side-by-side rather than validating one; and (4) we extend beyond ranking divergence to action divergence via the stakeholder pain calculus of [roshomon/cocomo.tex].

## One-liner summary

**Test 1: SE4AI hands it to us. Test 3: SE4AI hands us the measurement, we add the comparative design. Tests 2 and 4: ours to invent.**

That's the cleanest possible position — maximally leveraged, clearly novel where it matters.
