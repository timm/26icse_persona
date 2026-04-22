# Research Plan

Three-paper arc. **P1 must submit by 2026-06-30.** P2 and P3 follow.

## P1 — ICSE 2027 Research Track (deadline 2026-06-30)

**Claim (single sentence).** When GenderMag personas are extended with two organizational-power axes (Control, Now), LLM-simulated stakeholder responses become behaviorally distinguishable in ways the cognitive-only facets cannot capture, and on at least one SE task the extension flips tool-evaluation verdicts.

**In scope:**
- Test 1 (distinguishability) — full, SE4AI-style LLM-as-Judge.
- Mini Test 3 — *one* SE task, *one* clear flip case demonstrating divergence. Not a three-arm ablation.
- Task: **MOOT** (SE4AI infrastructure, calibrated at N=400, re-used).
- Personas: ~9 (small grid crossing cognitive × org-position). Details in `docs/validation-plan.md`.
- Named artifact on GitHub: composite persona generator + judge harness.
- Full structural playbook per `docs/paper-style.md` (4-para intro, groovy graphic, RQ-driven results, discussion with named sub-claims, Wohlin TTV).

**Out of scope (deferred):**
- Test 2 non-redundancy — P2
- Full Test 3 three-arm ablation across tasks — P2
- Test 4 pain-calculus actionability — P3
- Human spot-check on new axes — P2
- Defect-model experiments (`refs/cocomo_defects.py` stays referenced but not exercised) — P3

## 8-week schedule

| Week | Dates | Work |
|---|---|---|
| 1 | now (late April) | Lock scope. Confirm MOOT as task. Lock persona grid. Draft persona prompts. Build LLM-as-Judge scaffold. Set API budget. |
| 2–3 | early May | Build persona harness + judge harness. Pilot on 2 personas. Fix bugs. |
| 4–5 | mid–late May | Run full Test 1. Pilot Test 3 flip case; iterate to find a compelling one. **Week 5 is the gate — if no flip case by then, pivot task.** |
| 6 | early June | Data analysis, statistical tests, tables, figures. |
| 7 | mid June | Draft paper. Intro + results first. |
| 8 | to 2026-06-30 | TTV, conclusion, polish. **Abstract due 2026-06-23, paper due 2026-06-30.** |

## Risks & mitigations

- **LLM API cost/time.** Budget in week 1, not week 5.
- **No flip case found.** Week 5 gate — if Test 3 pilot shows no divergence on MOOT, pivot to another task (microservice identification, defect ranking) while time remains.
- **Writing procrastinated.** Have intro + 3-figure outline drafted by end of week 4; don't leave all writing to week 7.
- **PC conflict.** Tim is on the ICSE 2027 PC (`docs/cfp.txt` ~line 2130). Confirm author-side rules before submission (`todo.md` open item).

## P2 — TSE journal extension via SCRE (Fall 2026 / early 2027)

ICSE 2027 CFP (~line 186) approves journal extensions through the Sustainable Community Review Effort (SCRE). P2 rides P1's reviewers.

**Adds:**
- Test 2 (non-redundancy) — `cocomo_facets ~ GM_facets` regression.
- Full Test 3 three-arm ablation (GM-only / cocomo-only / composite) across 2–3 SE tasks.
- Human spot-check on new axes (Control, Now), n ≈ 5–10 participants.

## P3 — FSE 2027 or EMSE (2027)

**Claim:** applied case study. Stakeholder pain calculus on concrete SE recommendations flips chosen actions.

**Adds:**
- Test 4 (actionability) — pain calculus from `refs/cocomo__roshomon (1).pdf` §4.
- `cocomo_defects.py` exercised (effort + risk + defects objectives).
- Ideally an industry partner for external validity.
- Builds on P1 + P2.

## This week's actions

1. Confirm MOOT as the task (or pick alternative).
2. Lock ~9 persona definitions — draft grid e.g. {Abi, Pat, Tim} × {Autonomy, Neutral, Control}.
3. Stand up the LLM/API harness skeleton and price a week of full-grid runs.
4. Write the "flip case" success criterion: what does a hit look like, what counts as evidence?
5. Resolve one blocking `todo.md` item: widest-ranges choice for EM slopes (needed if any cocomo.py output feeds P1).
