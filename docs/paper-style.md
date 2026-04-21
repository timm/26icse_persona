# Paper Structural Recipe

Structural conventions for this ICSE 2027 submission. Worked example throughout: `refs/2105.12195v3.pdf` (Chakraborty, Majumder, Menzies, "Bias in ML Software: Why? How? What to Do?", ESEC/FSE 2021 — best paper award).

A "good" paper at this venue = (structural scaffolding below) + (substance: novelty, scope, rigor, named artifact, refuted truism).

## 1. Four-paragraph intro (+ optional throw, + digressions)

| Para | Job | 2105 example |
|---|---|---|
| ¶1 | Everyone does X (universal concern) | "It is the ethical duty of software researchers…" |
| ¶2 | X has a problem (concrete examples) | Amazon / face-recognition / Google Translate bullets |
| (¶2.5 optional throw) | Prior work is inadequate | "Prior works… are 'dumb' because they do not use domain knowledge" |
| ¶3 | New insight suggesting we can solve X | "The insight we offer here is that the root causes of bias might be the prior decisions that generated the training data" |
| ¶4 | What we did + contributions list | "This Fair-SMOTE tactic…" + bulleted contributions |
| (digressions at end) | CYA: caveats, limitations, scope | "training data is mutated but test data remains…"; mutation dangers |

## 2. Page-1 devices

- **Elevator speech.** One sentence stating the take-away, visible on p1 in both abstract and intro. 2105: *"(A) remove biased labels; and (B) rebalance internal distributions such that they are equal based on class and sensitive attributes."* Reviewers who read only p1 should still be able to repeat your claim.
- **Research questions as summary of results.** Either list RQs on p1 with one-line answers, or defer answers to the boxed RQ sections in Results. Either way, RQ labels appear as skimmable anchors.

## 3. Page-2 device: the "groovy graphic"

A single figure on p2 that visually positions your work in the landscape. 2105 Figure 1: three bubbles ("How to find? / Why? / What to do?") with Fair-SMOTE shown addressing all three. A reviewer who sees only this graphic should understand your pitch.

## 4. Related work: survey, then throw

End `§Related Work` with an explicit throw paragraph:

> In summary, prior work suffered from: (1)… (2)… For the rest of this paper, we explore a solution that [new thing].

2105 does exactly this. Without the throw, the related-work section reads as a literature dump; with it, you've earned the right to your contribution.

## 5. RQ-driven results

Each research question gets its own subsection, with:
- The RQ stated in a highlighted box.
- A bolded one-sentence answer at the end ("Thus, the answer for RQ3 is…").
- Supporting table(s) with best-rank cells shaded for skim-readability.

2105 §5 has RQ1–RQ5 in this format. Reviewers skim; this lets them find your answers.

## 6. Discussion is not optional

Results stop at "what happened." Discussion takes the reviewer by the hand and shows implications. Required moves:

1. **Interpret** — why the result holds, not just that it does.
2. **Bound** — when would it fail? what conditions assumed?
3. **Connect** — tie back to the intro truism / prior work.
4. **Extract principle** — a portable lesson bigger than one algorithm.
5. **Contrast** — what does this mean for readers using baseline X?

2105 §6 "Why Fair-SMOTE?" names five sub-claims: *Combination / Uncompromising / Group & Individual / Generality / Versatility*. Each is a one-paragraph mini-argument for uniqueness. Use named sub-headings — reviewers skim for them.

## 7. Threats to Validity: structured checklist

Use the Wohlin taxonomy. One short paragraph per category. Missing a category invites "did not consider X validity" complaints.

| Category | Question | Typical concerns |
|---|---|---|
| **Construct** | Do measurements capture the concept? | Metric choice, operationalization, mono-method bias |
| **Internal** | Are causal inferences sound? | Confounders, selection effects, is observed effect from your treatment? |
| **External** | Does it generalize? | Dataset choice, subject systems, learners, industrial vs. toy |
| **Conclusion** | Are statistical conclusions correct? | Sample size, test choice, multiple comparisons, replicate runs |
| **Reliability** | Can others reproduce? | Replication package, documented procedure |

2105 §7 uses a lighter 4-part version (Sampling / Evaluation / Internal / External) that roughly folds construct into "Evaluation Bias" and defers conclusion-validity to the methodology section (Scott-Knott + 10-run medians in §4.4). Folding is OK *if* you defend the folded concern elsewhere.

## 8. Awards-bait substance (beyond scaffolding)

Structure alone doesn't win awards. 2105's structural recipe is reusable, but its acceptance came from:

- **Large empirical footprint.** 10 datasets × 3 learners × (5 performance + 4 fairness) metrics. Big enough to be unignorable.
- **Named truism, then refuted.** Quotes Berk et al.'s *"It is impossible to achieve fairness and high performance simultaneously"* and the Conclusion explicitly says *"We can reject the pessimism of Berk et al."* Rhetorical crowbar.
- **Statistical testing.** Scott-Knott bi-clustering, ten-run medians, win/tie/loss tables with shaded cells.
- **Named, released artifact.** "Fair-SMOTE" is memorable; GitHub link in footnote on p2 (not buried at end).
- **Pseudocode.** Algorithm 1 is explicit — no hand-waving.

## 9. Standard components checklist (Menzies, slide 25)

- List of attributes (table).
- Attribute distributions (figure).
- Analysis graphic (framework block diagram).
- Literature review (budget 1–5 days).

## 10. Conclusion as portable principle

Don't just summarize. Leave the reviewer with something they can carry to their next paper. 2105's three-point conclusion:

1. We can recommend [thing].
2. We can reject the pessimism of [prior authors].
3. More generally, [portable principle] — e.g., *"rather than blindly applying optimization methods, reflect on the domain; use insights from that reflection to guide improvements."*

## Quick self-check before submitting

- [ ] p1 has an elevator speech a reviewer could quote back.
- [ ] p2 has a groovy graphic that positions the work.
- [ ] Intro follows 4-para skeleton (+ optional prior-work throw, + caveat digressions).
- [ ] Related-work section ends with an explicit throw.
- [ ] Every RQ has a bolded one-line answer.
- [ ] Discussion has named sub-claims for uniqueness, not just a results recap.
- [ ] TTV covers Construct / Internal / External / Conclusion / Reliability (or defends folds).
- [ ] A specific prior truism is quoted and refuted.
- [ ] Artifact is named and linked on an early page.
- [ ] Conclusion ends with a portable principle, not just a summary.
