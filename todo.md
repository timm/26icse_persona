# TODO

Open items to resolve before the paper is submission-ready.

## COCOMO range / formula discrepancies

Three sources disagree on slope ranges and the scale-factor parameterization. Current port (`refs/cocomo_defects.py`) uses provisional choices marked with `# TODO:ranges` comments. Resolve before final experiments.

### 1. Effort-multiplier slope ranges (EM⁺, EM⁻)

Three candidate ranges in play:

| Range | EM⁺ (pos slope) | EM⁻ (neg slope) | Source |
|---|---|---|---|
| A | 0.073 … 0.21 | −0.187 … −0.078 | `refs/cocomo.py` (`emsf`) |
| B | 0.055 … 0.15 | −0.166 … −0.075 | `refs/xomo.py` (`Emp`/`Emn`) |
| C | 0.073 … 0.21 | −0.178 … −0.078 | `refs/Understanding_the_Value_of_Software_Engineering_Technologies.pdf` (sawtooth paper, Eq 15) |

User directive: **use the widest range, always.** Provisional choice in the port: widest union, i.e. EM⁺ ∈ [0.055, 0.21] and EM⁻ ∈ [−0.187, −0.075]. Confirm or override.

### 2. Scale-factor parameterization (SF β)

Two *different forms* in play, not just different numbers:

| Form | Expression | Range of `m` | Source |
|---|---|---|---|
| multiplicative | `(6 − z) · m` with `m ∈ U(1.0, 1.5)` | 1.0 … 1.5 | `refs/cocomo.py` (`emsf`, star branch) |
| additive linear | `m · (z − 6)` with `m ∈ U(−0.972, −0.648)` | −0.972 … −0.648 | `refs/xomo.py` (`Sf`) |
| additive linear | `m · (z − 6)` with `m ∈ U(−1.56, −1.014)` | −1.56 … −1.014 | sawtooth paper (Eq 16) |

Provisional choice in the port: **sawtooth form** `m·(z−6)` with `m ∈ U(−1.56, −1.014)` — widest and matches the published math. Confirm.

### 3. COQUALMO defect slope ranges

Phase-by-phase, values paper vs. xomo.py. For each, xomo.py is generally wider.

| Slope | Sawtooth | xomo.py | Port uses |
|---|---|---|---|
| Intro reqs⁺ | 0 … 0.112 | 0.0166 … 0.38 | xomo.py (wider upper bound) |
| Intro reqs⁻ | −0.183 … −0.035 | −0.215 … −0.035 | xomo.py (wider lower) |
| Intro design⁺ | 0 … 0.14 | 0.0066 … 0.145 | xomo.py (essentially same) |
| Intro design⁻ | −0.208 … −0.048 | −0.325 … −0.05 | xomo.py (wider lower) |
| Intro code⁺ | 0 … 0.14 | 0.0066 … 0.145 | xomo.py |
| Intro code⁻ | −0.19 … −0.053 | −0.29 … −0.05 | xomo.py (wider lower) |
| Remove reqs | 0.08 … 0.14 | 0.0 … 0.14 | xomo.py (wider lower) |
| Remove design | 0.1 … 0.156 | 0.0 … 0.156 | xomo.py (wider lower) |
| Remove code | 0.11 … 0.176 | 0.1 … 0.176 | xomo.py |

Confirm the "widest always" policy applies.

### 4. Risk formulation — additive (code) vs. multiplicative (paper)

XOMO 2006 (Fig 4) describes risk contribution as **multiplicative** with EMs:
> *"For sced=vl and rely=vh, coefficients are 1.43 and 1.26, threat factor 2. 1.43·1.26·2 = 3.6036."*

But `cocomo.py` and `xomo.py` use **additive raw table values** (integer penalties 0/1/2/4/8 summed and normalized). The code is a simplification.

Provisional choice in the port: keep the code's additive form (simpler, already implemented). TODO: document the simplification in the paper's methodology section, or switch to multiplicative if reviewers will want fidelity to the 2006 description.

### 5. Defect-intro sign tables: minor gaps

In `xomo.py`:
- `flex` is marked "ignore" at all three phases.
- `pcap` is marked "ignore" at reqs only, but "negative" at design and code.

Sawtooth paper (text near Eq 17) doesn't specify `flex` / `pcap` placement explicitly. Check that the ignore/include pattern is intentional before citing.

### 6. `DefectIntroReqsPos` vs paper

`xomo.py` includes `Data, cplx, pvol, ruse, stor, time` in the positive-slope defect list.
Sawtooth paper lists positive defect features as "flex, data, ruse, stor, time, pvol." Note `flex` appears here in the paper but is "ignore" in xomo.py; `cplx` appears in xomo.py but not in the paper's list.

Resolve before citing.

## Stakeholder-mapping details (deferred)

Approach agreed: each stakeholder group carries a **4D identity vector** (Now, Build, Change, Control — `refs/cocomo__roshomon (1).pdf` Fig 1) and a **sparse 24D wince list** (pain points in COCOMO driver space, with `?` on irrelevant dims). Actions score well on objectives and get penalized by distance to any triggered pain point. Details to lock:

- **Distance metric** — weighted Euclidean in 24D. Weight 0 for `?` dims, 1 otherwise (or graded). Confirm.
- **Pain threshold τ_g** — provisional: relative, "within 15% of driver-space diameter." Needs calibration.
- **Multiple pain points per group** — take min distance (nearest-wince wakes the group).
- **Update rule** — soft penalty `−w·(1 − dist/τ_g)` added to score when triggered; iterate until stable. (Not hard constraints — MC runs are probabilistic.)
- **Pain-point origin** — provisional: mechanically derive from roshomon Table 3 (each action's driver settings → pain vector for the action's "most hates" groups). LLM-generated pain points as a later ablation (follow SE4AI LLM-as-Judge protocol for validation).
- **Two-layer integration** — 4D locates *which groups are loud* in a given org mix; 24D locates *which recommendations make them scream*. Both layers live in the same code path.

## Non-COCOMO TODOs (carried from earlier conversation)

- Pick the concrete SE task for Tests 3 and 4 in `docs/validation-plan.md` (MOOT, microservices, defect ranking, or COCOMO-direct). MOOT is lowest friction.
- Decide LLM-only vs. LLM + human spot-check for the new axes (Control, Now).
- Name the paper's contribution (candidates in `docs/background.md` §Named-contribution candidates).
- PC conflict-of-interest check: Tim is on the ICSE 2027 PC (`docs/cfp.txt` line ~2130). Confirm author-side rules.
- Pre-registration decision: commit hypotheses publicly before running experiments?
