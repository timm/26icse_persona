# Background & Theoretical Frame

Assembled from:
- `refs/Understanding_the_Value_of_Software_Engineering_Technologies.pdf` — Green, Menzies et al., ASE 2009 ("values" paper).
- `refs/On_the_Usefulness_of_Automatically_Generated_Microservice_Architectures.pdf` — Carvalho et al., TSE 2024 ("usefulness" paper).
- `refs/bitter.md` — Menzies, 2026 talk ("You're Being Promoted, Not Replaced").
- `refs/SE4AI-2.pdf` — Estes, EsfandyariDoulabi, Khanmohammadi, 2026 (GenderMag-extended personas for XAI).
- `refs/cocomo.tex` — stakeholder-aware CEO playbook sketch (4D stakeholder space + COCOMO drivers).

This file is the theoretical frame for the paper. Structural mechanics live in `paper-style.md`.

## One-sentence thesis

AI-for-SE inherits, from games and vision, the assumption that a generated artifact can be assessed the moment it is produced; SE artifacts do not behave that way — their worth emerges slowly, under multiple value frames shaped by stakeholders' cognitive style **and** organizational position. A method for evaluating AI-for-SE tools must therefore support a slower, reflective human–artifact cycle with persona coverage that spans both cognition and power, generated rather than hand-picked.

## The decades-old complaint

| Year | Source | Complaint |
|---|---|---|
| 1976 | Brooks (V-diagram) | The code is not the artifact; what you learned building it is. Domain knowledge carries to project *i+1*. |
| 1983 | Swartout, XPLAIN | Jump straight to code and you lose the *Why*. The system cannot justify itself without the domain principles that drove its refinement. |
| 2004 | Boehm (ASE keynote) | SE tools should be assessed by their *value* to a stakeholder, not just by functionality. |
| 2009 | Green, Menzies et al. (ASE) | Two different `value()` functions (BFC vs. XPOS) applied to the same COCOMO model produce *opposite* tool recommendations: *"if one value function approves of X then the other usually approves of not X."* |
| 2019 | Sutton, *The Bitter Lesson* | Sixty years of evidence: brute-force compute beats human-engineered knowledge. |
| 2024 | Carvalho et al. (TSE) | Search-based microservice identification generates "optimal" architectures, but maintainer profiles (fine-grained vs. coarse-grained) reach opposite adoption decisions on the *same* output. Calls for "interactive and/or customizable approaches." |
| 2026 | Menzies, *bitter.md* | Sutton's examples all share a quiet assumption — *you can assess the "What" the moment it's created.* SE is not chess. |

Forty to fifty years. Same complaint. Still open.

## Sutton's hidden assumption, sharpened

Sutton's winning domains (chess, Go, vision, phonemes) share one property: an **instant oracle**. A move is good/bad in milliseconds; a label matches ground truth immediately; a phoneme aligns or does not.

SE has no such oracle. Properties of interest:

- **Reliability** — measured 18 months into production.
- **Maintainability** — measured by whoever inherits the code.
- **Understandability** — measured under pressure, by non-authors.
- **Value-fit** — measured against a stakeholder's goals, which may themselves shift.

All are slow, contextual, stakeholder-dependent, sometimes revisable. None admit the instant-oracle loop that made scaling work in Sutton's cases.

## The stakeholder-conditioning twin result

- **2009 (values):** there is no universal metric — the same tool flips from "recommended" to "harmful" when the value function changes.
- **2024 (usefulness):** there is no universal maintainer — the same generated architecture flips from "adoptable" to "not adoptable" when the maintainer profile changes.

One finding at the level of *project values*, one at the level of *maintainer preferences*. Both reject universal-claim evaluation. Both propose human-in-the-loop interaction.

## Partial fixes: GenderMag and its extensions

**GenderMag (Burnett et al. 2016)** — cognitive-walkthrough method built from **5 cognitive facets** (motivations; information-processing style; computer self-efficacy; attitude toward risk; learning style) operationalized as **3 canonical personas** (Abi, Pat, Tim). Facet values are fixed; only surface attributes (job title, age, location) are customizable.

**SE4AI (Estes et al. 2026)** — extends to **3 roles × 3 cognitive profiles = 9 personas**. Roles = Project Manager, Product Manager, Software Engineer, treated as a "gradient of technical depth" (1/5, 3/5, 5/5). Demonstrates LLM-simulated personas can stand in for human ones; shows acceptance jumps 16% → 51% when explanations are persona-tailored. Self-reports a failure mode (§5.3, Failure Mode 2): *"Role constraint suppresses cognitive style signals"* — SE4AI's own analysis points to needing richer role/power axes.

**Limits of this line:**

1. Cast is small (3 → 9) and categorical.
2. Facets are *cognitive*, not *positional* — they describe *how* someone reasons, not where they sit in the org chart or what they can veto.
3. Role is present but compressed to one axis (technical depth). Accountability, authority, time-horizon, build-vs-use are not represented.

## The missing dimension: organizational power (`cocomo.tex`)

`refs/cocomo.tex` sketches the complement to GenderMag. A **4D stakeholder space**:

| Dim | 0 | 4 |
|---|---|---|
| Now | Now (ship) | Later (sustain) |
| Build | Use (consume) | Build (own) |
| Change | Stable | Change |
| Control | Autonomy | Control |

Eight canonical groups placed in this space (Users, Customers, Developers, QA, Managers, Executives, Regulators, Ops). An organization is modeled as a **weighted mix of at most three groups**; the preference vector is the weighted centroid. Personas are *generated* rather than drawn from a fixed cast.

Nine executive actions (improve personnel, improve tools, relax schedule, reduce functionality, etc.) each map to (a) COCOMO driver changes and (b) a predicted "likes / hates" split in the 4D space. Decision rule combines objective metrics with stakeholder pain constraints:

$$\textit{score}(a) = w_1 \cdot \textit{change}(a) + w_2 \cdot \textit{effort}(a) + w_3 \cdot \textit{risk}(a) - w_4 \cdot \textit{value}(a)$$

subject to $\textit{pain}(g, a) \le \tau_g$ for every stakeholder group $g$. This operationalizes the 2009 paper's `value()` idea as per-group tolerance thresholds.

## GenderMag ↔ cocomo.tex overlap

Two frameworks, partial overlap:

| GenderMag facet | cocomo dimension | Overlap |
|---|---|---|
| Motivations (task vs. tech) | Build (Use vs. Build), partly Now | Partial — both about drive, different angles |
| Attitude toward risk | Change (Stable vs. Change) | Strong |
| Information-processing style | — | GM only (cognition) |
| Computer self-efficacy | — | GM only (cognition) |
| Learning style | — | GM only (cognition) |
| — | Control | cocomo only (org authority) |
| — | Now | cocomo only (time horizon, partly in GM motivations) |

Two dimensions are **independently identified by both frameworks** (motivation, risk). That's convergent evidence: these are robust axes of stakeholder variation, not artifacts of either method. Three are **GM-only** (cognitive); two are **cocomo-only** (positional/temporal).

## Composite persona model

A unified model, seven dimensions:

```
stakeholder = {
  motivation,      ← shared (GM ↔ cocomo Build/Now)
  risk,            ← shared (GM ↔ cocomo Change)
  info-style,      ← GM only  (cognition)
  self-efficacy,   ← GM only  (cognition)
  learning-style,  ← GM only  (cognition)
  control,         ← cocomo only (org power)
  horizon          ← cocomo only (temporal)
}
```

Rhetorical leverage: *two independent frameworks arrived at motivation and risk; we unify them and add the axes each was missing.*

Personas in this model are **generated**, not curated — as weighted mixes of canonical groups (cocomo.tex) crossed with cognitive facet combinations (GenderMag). This replaces the fixed cast of 3 or 9 with a continuous persona space.

## Stacked rhetorical crowbar for the intro

Candidate truisms to quote and refute:

| Truism | Source refuting | Leverage |
|---|---|---|
| "Compute beats knowledge." | Sutton 2019, refuted by Menzies 2026 `bitter.md` | Valid for instant-oracle tasks only. SE has no instant oracle. |
| "Generated code is the artifact." | Swartout 1983 | Without the Why, code cannot justify itself. 40+ years unresolved. |
| "Better metric score means better tool." | Menzies et al. 2009 | Flips with the value function. |
| "Benchmark success means maintainer success." | Carvalho et al. 2024 | Maintainer profiles diverge; same tool output gets opposite adoption verdicts. |
| "A small fixed cast of personas covers the stakeholder space." | SE4AI's own Failure Mode 2 (2026) | Role constraint suppresses cognitive signals; cast needs to be richer and generated. |
| "Gender/race identify the relevant stakeholder axes." | cocomo.tex | Organizational power (Control, Now, Build, Change) is orthogonal to demographics. |

Pick the one(s) closest to the paper's specific contribution; quote, cite, refute.

## Named-contribution candidates

The paper needs a memorable, releasable thing (per `paper-style.md` §8). Current candidates:

- **Slow loop / reflection loop** — the complementary human–artifact cycle to Copilot-style continuous engagement.
- **Composite persona generator** — motivation × risk × cognitive facets × org position, auto-generated from weighted group mixes.
- **Stakeholder pain calculus** — `pain(g, a) ≤ τ_g` as the evaluation substrate, with LLM-simulated personas filling in the per-group judgments.

Whatever the final artifact, it should have a named GitHub link on page 1 or 2.
