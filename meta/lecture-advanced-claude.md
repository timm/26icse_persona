# Advanced Use of Claude for SE Research

90-minute lecture for SE graduate students. Reflects on a single multi-hour Claude Code session that took an ICSE 2027 research project from an empty directory to a five-document research plan plus working simulation code. The case study is specific (stakeholder-aware SE tool evaluation); the techniques generalize.

Target reader: second-year PhD student writing an SE paper or dissertation chapter. Assumes you can read Python and LaTeX but have used LLMs only casually.

---

## 1. Install (5 min)

Claude Code is the CLI version of Claude. It runs in your terminal, reads and writes files in a directory, and can execute shell commands.

```
# macOS
brew install --cask claude-code

# Linux / WSL
curl -fsSL https://claude.ai/install.sh | sh

# Windows
curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd
```

First run:
```
cd ~/your-project
claude
```

You will be asked to sign in (Anthropic or Claude Pro account). After that, Claude Code has file-system access scoped to the directory where it started.

The rest of the lecture assumes you are running Claude Code in the root of a fresh git repository.

---

## 2. The project we will use as a case study (10 min)

We set out to write an ICSE 2027 Research Track paper arguing that current AI-for-SE tool evaluations inherit Sutton's "instant-oracle" assumption from games and vision, and that this assumption fails for SE because SE artifacts emerge over time under multiple stakeholder value frames.

Concretely we wanted to:
1. Build simulation software (a Monte Carlo model of software-project outcomes under different stakeholder preferences).
2. Use that simulator to show that the same tool recommendation flips from "good" to "bad" when you change the stakeholder mix.
3. Write this up for an ICSE deadline.

This is a typical SE-research task:

> We are writing software. Simulation software that embodies some business logic. To do that, we had to first model the *context* in which the software runs — who uses it, what they care about, how that shapes what "working" means. And that led to a whole bunch of documents, decisions, and citations that are not code but without which the code is meaningless.

That observation is the point of the lecture. Most Claude tutorials teach you to type a prompt and get code. Research is not like that. Research is: *model the context before you write the code.* Claude can help with both, but only if you treat context-modelling as first-class work.

---

## 3. The progression — ten rounds in one session (15 min)

A quick narrative of how the project evolved. Each round added one thing. No single round was heroic; the accumulation is.

**Round 1: scaffolding.** Empty directory. Asked Claude to create `CLAUDE.md` with ICSE 2027 hard constraints (LaTeX class, page limits, deadlines, double-anonymous rules). `CLAUDE.md` is auto-loaded by Claude Code on every session start — the terse rule book.

**Round 2: structural recipe.** Read an award-winning paper (Fair-SMOTE, ESEC/FSE '21) together with a slide deck teaching how to write papers. Extracted a reusable "paper skeleton" into `docs/paper-style.md`: four-paragraph intro, page-1 elevator speech, page-2 groovy graphic, related-work throw, RQ-driven results, discussion, Wohlin threats-to-validity.

**Round 3: theoretical frame.** Read two more papers (a 2009 values paper and a 2024 TSE paper on microservices). Noticed they were saying the same thing 15 years apart. Added a 2006 XOMO paper, a 2026 blog post, and traced the complaint back through Boehm 2004 → Swartout 1983 → Brooks 1976. Wrote `docs/background.md` — the decades-old unresolved problem.

**Round 4: stakeholder model.** Read an SE4AI paper using GenderMag personas. Observed GenderMag handles cognition but not organizational power. Added a sketch document (`cocomo.tex`, from prior work) that models power in a 4D space. Mapped overlap between the two frameworks: two shared axes (motivation, risk), three cognitive-only (info-style, self-efficacy, learning), two positional-only (Control, Now). Result: a composite 7-dimension persona model.

**Round 5: simulation code.** Ported and cleaned up two existing Python files (`cocomo.py`, `xomo.py`) into a single `cocomo_defects.py` that runs a Monte Carlo with effort, risk, and defect outputs. Used the "pivot sampling" idea: coefficients are themselves drawn from literature uncertainty ranges, once per run. No calibration needed.

**Round 6: validation plan.** Four tests to defend the claim that the composite model is "better" than GenderMag alone: distinguishability, non-redundancy, predictive power, actionability. Wrote `docs/validation-plan.md`.

**Round 7: methodology reuse.** Mapped SE4AI's methodology component-by-component to our four tests. Found SE4AI hands us Test 1 entirely and most of Test 3; Tests 2 and 4 are ours to invent. Wrote `docs/methodology-reuse.md`.

**Round 8: open issues.** Throughout, whenever a detail could not be resolved immediately (e.g., which of three COCOMO slope ranges to use, exactly how to map 4D organizational space to 24D driver space), we added it to `todo.md` and kept moving. Code got `TODO:ranges` comments linking back.

**Round 9: scope reduction.** Realized the full validation plan was more than one paper. Sketched a three-paper arc (ICSE 2027, TSE journal extension via SCRE, applied case study). User corrected the timeline: "not 14 months, 1 week + May + June." Cut P1 to minimum viable: Test 1 + one flip case on MOOT. Wrote `docs/research-plan.md`.

**Round 10: this reflection.** The lecture you are reading.

---

## 4. What was built (5 min)

```
26icse_persona/
├── CLAUDE.md            rules auto-loaded every session
├── README.md            human-facing layout map
├── Makefile             build paper/*.tex with tectonic → ~/tmp/<repo>/
├── todo.md              deferred decisions (range choices, stakeholder metric)
├── docs/
│   ├── cfp.txt            source ICSE 2027 call for papers
│   ├── paper-style.md     structural recipe + checklist
│   ├── background.md      theoretical frame, decades-old problem
│   ├── validation-plan.md four tests, machinery from SE4AI
│   ├── methodology-reuse.md SE4AI component-by-component
│   └── research-plan.md   3-paper arc, P1 schedule
├── refs/
│   ├── *.pdf              6 reference papers (read, some cited)
│   ├── cocomo.py          original MC engine
│   ├── cocomo_defects.py  clean port: effort + risk + defects, TODO-marked
│   ├── xomo.py            legacy code (source of defect model, messy)
│   ├── cocomo.tex         stakeholder-aware CEO playbook
│   └── bitter.md          2026 Menzies talk
├── paper/               empty; will hold LaTeX draft
└── meta/
    ├── README.md          explains this folder
    ├── install.md         setup notes
    ├── report.html        Claude Code insights dashboard
    └── lecture-advanced-claude.md  this file
```

Eight thousand words of documents, ~350 lines of working Python, a Makefile, a README, and a research plan with an 8-week schedule. From an empty directory.

---

## 5. Eight meta-techniques (30 min)

### 5.1 Context is first-class work

A typical student-Claude interaction: "write me code that does X." Produces code. Student adapts it.

A research-Claude interaction: "here is a CFP, here is an inspirational paper, here is a related paper, here is a prior-work sketch, here is a critique I wrote two weeks ago — help me synthesize." The output is never just code; it is *documents that encode context*. Those documents become the scaffolding for the code, the paper, and the next session.

Implication: spend the first 30–60 minutes of any new project building context. Don't jump to content. The context you build in the first hour is leverage for the next 40.

### 5.2 Separate rules from synthesis

`CLAUDE.md` is auto-loaded on every session. It has to be terse or it crowds everything else out.

`docs/*.md` are loaded only when relevant. They can be rich, long, and evolving.

Rule of thumb: if a file has instructions ("always use LaTeX class X"), put it in `CLAUDE.md`. If it has a synthesis ("here is the argument of the related-work section"), put it in `docs/`. `CLAUDE.md` points to `docs/` so Claude knows where to look.

### 5.3 Reference material is a tool, not a corpus

We had six PDFs in `refs/`. We did not treat them as "the literature." We used them specifically:

- Fair-SMOTE (2105): *structural exemplar*. We copied its skeleton.
- SE4AI: *methodology donor*. We lifted its LLM-as-Judge protocol.
- 2009 values paper: *mathematical appendix*. We cited its slope ranges.
- XOMO 2006: *cross-check*. We confirmed the effort equation.

Each paper had a role. When a new paper arrived we asked "what role does this one play?" — not "is this relevant?"

### 5.4 Named artifacts force production

Every paper in the three-paper plan has a named, releasable thing: a persona generator, a pain-calculus runtime, a case study. A paper with a named artifact is a paper that had to ship something concrete. A paper with only an idea is a paper you can keep revising forever.

Same rule inside a single paper. Tim's paper template calls this "the elevator speech": one sentence on page 1 a reviewer could quote back. If you can't write it, you don't have a paper yet.

### 5.5 TODO-driven deferral

Several decisions needed to be made that we were not ready to make (which slope range? which distance metric? human spot-check or not?). Rather than either (a) deciding randomly or (b) stopping work to resolve, we wrote a `todo.md` entry and moved on. Code got `# TODO:ranges` comments. Docs got "provisional choice: ..." notes.

This is the discipline of *knowing what you deferred*. A TODO entry is a promise to yourself to revisit. Without it, deferred decisions silently calcify into the thing you shipped.

### 5.6 Code and text in parallel

The simulation code (`cocomo_defects.py`) and the research plan were built *at the same time*. The code didn't wait for perfect theory; the theory didn't wait for running code. Each informed the other:

- When writing the validation plan, we realized we needed a defect output → added it to the code.
- When running the code, we noticed three ranges disagreed → added it to `todo.md`, did not stop.
- When sketching the pain calculus, we realized it needed per-group distance metrics → deferred the details to `todo.md`.

The parallel track keeps momentum. Pure-theory projects stall waiting for "the right framework." Pure-code projects stall waiting for "a clear idea of what to implement."

### 5.7 Triangulate across sources

One paper said COCOMO effort-multiplier slopes were $0.073 \le m \le 0.21$. Another paper said $0.055 \le m \le 0.15$. Old code said $-0.187 \le m \le -0.078$. New code said $-0.166 \le m \le -0.075$. These disagreed.

We did not pick one at random. We tabled them, flagged the discrepancy in `todo.md`, and adopted the user's rule "use the widest, always." Every time three sources disagree on a number, that is a paper-defensibility risk. Documenting the disagreement is more important than resolving it immediately.

### 5.8 Scope to the calendar

At one point the research plan implied 14 months of work. The real deadline was 8 weeks.

Forced scope cut: Test 1 (full) + Test 3 (mini, one flip case). Everything else deferred to P2 and P3.

This was *not* done by asking "how much can we get done?" but by asking "what is the minimum that still constitutes a paper?" Then we built a week-by-week schedule with a gate in week 5. If the gate isn't met, pivot the task; if it still isn't met, pivot the paper.

Scope discipline is the single most common failure mode of student papers.

---

## 6. Lessons and anti-patterns (15 min)

### Do

- **Treat `CLAUDE.md` as the rule book.** Terse, auto-loaded, always true.
- **Let `docs/` evolve.** These are your synthesis documents. They grow as you learn.
- **Ship a named artifact.** Even if small. Naming forces production.
- **Quote a specific prior truism, then refute it.** This is the paper-style playbook's rhetorical crowbar. Works for every discipline.
- **Write tests that run.** `cocomo_defects.py`'s `checks()` function is executable proof the port works. Do this.
- **Cite what you actually read.** We cited XOMO 2006 and the 2009 sawtooth paper because we had read both. We did not cite the 2005 paper the 2006 paper pointed at — we hadn't read it.
- **Keep a `todo.md`.** Decisions you couldn't make. Range choices. Deferred experiments. Revisit before submission.
- **Use Claude to argue with, not just to type.** Push back. Ask "does this make sense?" If it doesn't, say so.

### Don't

- **Don't jump to code or prose before building context.** The first hour of documents pays for the next forty.
- **Don't let `CLAUDE.md` bloat.** It is auto-loaded every session. Long = slow + expensive + crowded.
- **Don't fabricate citations.** If you don't have the paper, say so. Ask for it. This session had one moment where Claude asked "which paper is the 'sawtooth paper'?" rather than guessing. That is correct behavior.
- **Don't commit to one number when three sources disagree.** Document the disagreement. Choose explicitly with justification.
- **Don't scope a paper by ambition.** Scope by calendar. Write the schedule first; fit the claim to the schedule.
- **Don't defer writing to the final week.** Paper draft by mid-period; polish at the end.
- **Don't use Claude as an oracle.** It is a collaborator. It will miss things, make mistakes, and sometimes confidently produce wrong answers. Verify. Cross-check. Argue.

### The generalization

> We are writing software. Simulation software that handles business logic. To do so we needed to model context. That led to a whole bunch of stuff.

Replace "simulation software" with "classifier", "experiment harness", "static analyzer", "dissertation chapter", "grant proposal". The structure is the same:

1. There is an artifact you want to produce.
2. The artifact has meaning only inside some context.
3. That context is rarely written down anywhere.
4. You must model the context before or while you build the artifact.
5. Claude accelerates both tasks, but you have to treat context-modelling as work of equal dignity to coding.

That is what changes when you move from "LLM as autocomplete" to "LLM as research collaborator."

---

## 7. Taking this to your own work (5 min)

Your first hour on a new research project:

1. `claude` in an empty repo.
2. Ask it to draft a `CLAUDE.md` with the hard constraints you already know.
3. Paste in one inspirational paper and one related paper. Ask for a structural recipe (`paper-style.md`) and a theoretical frame (`background.md`).
4. Write a one-sentence claim. If you cannot, you do not yet have a paper.
5. Draft a validation plan: how would you know if the claim is true?
6. Reality-check scope against your actual calendar.
7. Begin.

Your last hour on any day:

1. Update `todo.md` with the decisions you did not make today.
2. Update whichever `docs/*.md` is closest to what you worked on.
3. Commit.

Between those: work as a collaboration. Argue. Cross-check. Defer when stuck. Ship a named thing.

---

## 8. Appendix: commands to know

| Command | What |
|---|---|
| `claude` | Start a session in the current directory |
| `/init` | Generate an initial `CLAUDE.md` based on the repo |
| `/help` | List built-in slash commands |
| `! <cmd>` | Run a shell command from inside the session (without typing it in) |
| `@path/to/file` | Inline-reference a file by path (Claude reads it) |
| `Esc` then `Esc` | Edit previous message |

Specific to this lecture:

| File | Its role |
|---|---|
| `CLAUDE.md` | Terse, auto-loaded rules |
| `docs/paper-style.md` | Structural recipe |
| `docs/background.md` | Theoretical frame |
| `docs/validation-plan.md` | How to defend the claim |
| `docs/methodology-reuse.md` | What to lift from prior work |
| `docs/research-plan.md` | Three-paper arc, 8-week P1 schedule |
| `todo.md` | Deferred decisions |
| `refs/*` | Reference material, one role each |
| `paper/` | The actual submission draft |
| `meta/` | Claude-specific artifacts, not part of the submission |

---

## 9. Close

The project is not done. P1 is eight weeks away. The simulation code has `TODO:ranges` comments in six places. No persona responses have been generated yet. No SE task has been finally locked.

That is fine. The point of the session was not to finish the paper. The point was to build a *scaffold inside which the paper could be finished* under a hard deadline, with decisions made explicitly and debt accounted for.

That is the advanced use of Claude. Not "Claude wrote my code." Not "Claude wrote my paper." Instead:

> Claude helped me build a workspace, a theoretical frame, a validation plan, a methodology map, a schedule, and a set of explicit open questions — *so that* I can do the deep work in the remaining weeks without drowning in context every time I open the laptop.
