# Claude Code for Research: Workshop Course Specification

**Author:** Omer Eliyahu (SPL Lab, BGU)
**Status:** Spec v1. Module 2 fully built as exemplar; modules 0, 1, 3–6 specified for handoff.
**Audience:** MSc, PhD, and research assistants at SPL Lab. Adjacent fields: classical planning, heuristic search, MARL/MAPF, DRL.

---

## 1. Philosophy

Most Claude Code tutorials are written for product teams shipping production code. This course is written for researchers who:

- Live in exploratory codebases that mutate weekly
- Reimplement algorithms from papers
- Run experiments on HPC and care about reproducibility months later
- Often work alone, so the quality of AI feedback matters disproportionately
- Will be held accountable by reviewers for code they didn't write line-by-line

The course teaches Claude Code as a **research tool with shape**, not as magic. Every module includes failure modes alongside successes. The course explicitly avoids hype.

## 2. Outcomes

By the end of the course, a participant should be able to:

1. Set up Claude Code on macOS or Linux with persistent model/effort defaults and handle multiple GitHub identities.
2. Make any research repo Claude-friendly by writing a `CLAUDE.md` that demonstrably improves Claude's behavior on real tasks.
3. Drive Claude via TDD red-green loops for algorithm reimplementation.
4. Build a working slash command (and explain when *not* to build a skill).
5. Recognize and audit plausible-but-wrong AI output before it enters a paper or experiment.
6. Apply all of the above to their own research code by the final case study.

The single most important takeaway, if everything else is forgotten: **make the repo Claude-friendly first, then drive it with constrained loops (tests, slash commands), and never accept output you haven't read.**

## 3. Format & timing

- **Hands-on workshop**, not a lecture series. Every module has an exercise.
- **7 modules** (numbered 0–6). Total content time ≈ 6–8 hours.
- **Recommended cadence:** two ~2-hour live sessions per week for 3 weeks, plus take-home Module 6.
- Live sessions assume everyone has Claude Code installed and a laptop open.
- All content is also available as a static site for self-paced review.

## 4. Artifact stack

- **Site:** MkDocs Material on GitHub Pages.
- **Repo:** Single repo `claude-code-research-workshop` containing site source, exercises, and stub repos.
- **No slides** as primary artifact. (Optional: Marp can generate slides from the same markdown if needed for a live kickoff.)

```
claude-code-research-workshop/
├── docs/                          # MkDocs site source
│   ├── index.md
│   ├── module-00-framing.md
│   ├── module-01-setup.md
│   ├── module-02-claude-md.md     # FULLY BUILT
│   ├── module-03-workflows.md
│   ├── module-04-slash-commands.md
│   ├── module-05-failure-modes.md
│   ├── module-06-case-studies.md
│   └── teacher-notes/             # Excluded from main nav, linkable
│       └── module-02.md           # FULLY BUILT
├── exercises/
│   ├── m01-pyvalidator-setup/     # Points at public PyValidator repo
│   ├── m02-claude-md-stub/        # FULLY BUILT — intentionally messy
│   ├── m03-tdd-loop/              # Points at PyValidator
│   ├── m04-slash-command/         # Spec only; produces code
│   ├── m05-bug-hunt/              # NEEDS OMER INPUT (real bug from git log)
│   └── m06-case-studies/          # Points at three repos + BYOR template
├── mkdocs.yml
├── .github/workflows/deploy.yml
└── README.md
```

## 5. Module specifications

Each module follows a consistent template:

- **Time budget**
- **Learning objectives**
- **Content outline** (the body of the docs page)
- **Optional practice exercise** (with explicit success criteria)
- **Teacher notes** (what to emphasize live; common pitfalls)
- **Artifacts required**
- **Production status**

---

### Module 0 — Why this course exists

**Time:** 15–20 minutes.

**Objectives:**

- Understand the *shape* of Claude Code as a tool: agentic loop, terminal-native, multi-file, long-running.
- Distinguish it from Cursor, Copilot, and chat Claude — they are not interchangeable.
- Set realistic expectations: where Claude Code will save a week, and where it will quietly waste an afternoon.

**Content outline:**

1. **What Claude Code is.** A terminal-native agent that runs a read → plan → act → verify loop, with tool access to your filesystem, shell, and (optionally) MCP servers. It is *not* a chat window over your code.
2. **What it is not.** Not Cursor (which is editor-coupled and tighter-loop). Not Copilot (which is autocomplete, not agentic). Not chat Claude (which has no persistent workspace).
3. **Where it shines.** Long-running tasks across many files. Repetitive refactors. Reading unfamiliar codebases. Writing tests. Running and interpreting experiments. Anything that benefits from a real shell.
4. **Where it struggles.** Fuzzy specs ("make it better"). Tasks requiring runtime state Claude can't observe. Novel algorithm design (vs. reimplementation). Anything where the success criterion is taste.
5. **The "Claude wrote it, you own it" principle.** Introduced early, returned to in Module 5. If your name is on the paper, the code is yours regardless of who typed it.

**Optional practice:** Show two short screen recordings (3–5 min each) — Claude Code succeeding on a structured task in PyValidator, and flailing on a vague task. Students name the difference before instructor reveals it. *Recordings to be produced by Omer.*

**Teacher notes:**

- Resist defending Claude when it fails on the "bad" recording. Show the warts unedited.
- If anyone in the audience has used Cursor heavily, name the differences out loud — they will be the most confused.
- Do **not** demo Claude Code's flashiest features in this module. That's Module 1 and Module 2's job.

**Artifacts:** docs page, two screen recordings (Omer).

**Status:** Spec only.

---

### Module 1 — Setup & mental model

**Time:** 60 minutes (15 min content, 30 min exercise, 15 min troubleshooting).

**Objectives:**

- Install Claude Code, authenticate, confirm a working session.
- Configure persistent model and effort level defaults via shell profile.
- Handle multi-account workflows (lab GitHub identity vs. personal).
- Internalize the read → plan → act → verify loop by running it once end-to-end.

**Content outline:**

1. **Install.** `npm install -g @anthropic-ai/claude-code`. Node version requirements per official docs. Auth via `claude` first run.
2. **Persistent defaults via shell profile.** Setting `ANTHROPIC_MODEL` and effort-level environment variables in `~/.zshrc` so you don't pick a model every time. (Omer's actual config is a good reference.)
3. **Multi-account GitHub.** The lab account vs. personal account problem. A zsh hook that swaps git identity based on directory. *Use Omer's existing `omere-auditale` / `omereliy` setup as the worked example.*
4. **First session.** What `claude` does, what `/help` shows, what `/context` reveals. The TUI panes.
5. **The loop.** Read (Claude examines files) → Plan (Claude proposes a sequence) → Act (Claude edits/runs) → Verify (Claude tests, you check). Each phase has failure modes; name them.
6. **MCP basics.** One-paragraph mention. Defer depth to a possible Module 7.

**Optional practice:** Clone PyValidator (public, on PyPI as `pddl-pyvalidator`). Ask Claude "What does this repo do? What's the entry point?" Then ask it to add a single test for an edge case — e.g., empty plan, plan with malformed action name, predicate with wrong arity. **Success criterion:** test exists, runs, passes (or fails meaningfully) under `pytest`. ~30 min.

**Teacher notes:**

- **Verify everyone's setup works before the exercise.** Walk the room. Broken setups kill momentum and embarrass students.
- Common gotchas: outdated Node, expired auth, `npx claude` vs. global install, missing PATH entries on macOS with `nvm`.
- Don't let anyone start the exercise until they've successfully run a no-op like asking Claude what files exist in the repo.
- Show, don't tell, the multi-account zsh hook. If even one student has the auditale/personal split, this is the moment they remember.

**Artifacts:** docs page, recommended shell config snippet (committed to repo), pointer to PyValidator.

**Status:** Spec only.

---

### Module 2 — Making a repo Claude-friendly

**Time:** 75 minutes.

**Status:** **FULLY BUILT.** See `docs/module-02-claude-md.md`, `docs/teacher-notes/module-02.md`, and `exercises/m02-claude-md-stub/`.

The fully-built version is the style and depth template for all other modules. The agent (or human) producing the remaining modules should match this level of concreteness, exercise structure, and teacher-note specificity.

---

### Module 3 — Daily research workflows

**Time:** 75 minutes (20 min content, 30 min exercise, 25 min discussion).

**Objectives:**

- Drive Claude through a TDD red-green-refactor loop on a real function.
- Read an unfamiliar repo efficiently by asking Claude for an architecture summary first.
- Implement an algorithm fragment from a paper using Claude as a typing partner, not a designer.
- Manage long-running SLURM jobs at the BGU cluster level.

**Content outline:**

1. **The TDD discipline with Claude.** Why writing the test first is a constraint that disproportionately helps AI-generated code: it bounds the success criterion and gives Claude something to verify against. Show the loop: red → ask → green → ask for refactor.
2. **"Make Claude show its work."** Pattern: ask for the plan before the edit. Reject plans that skip steps. This prevents Claude from producing "looks right" code that you can't audit.
3. **Reading an unfamiliar repo.** First prompt: "Give me an architecture summary of this repo. Where are the entry points, where is the test layer, what files should I look at first?" Then narrow.
4. **Paper → code workflow.** Identify the algorithm. Sketch the type signature *first* with Claude's help. Then write a tiny test. Then implement. The trap: letting Claude design the algorithm rather than implement a sketched one.
5. **SLURM jobs.** Driving Claude to write `sbatch` scripts, monitor logs, summarize runs. Pitfalls: long log files, secrets in env vars, accidentally rerunning expensive jobs.
6. **BGU Ollama server.** *Lab-specific section.* When to use the local Ollama server (200GB VRAM) vs. Claude Code's hosted models. Cost vs. data sensitivity tradeoffs.

**Optional practice:** Delete a small self-contained function in PyValidator (predicate-arity check is a good candidate). Keep its test or write a new failing one. Drive Claude through TDD to restore it. Two iterations max. **Success criterion:** test goes red → green via Claude's edit, and the student can name what changed and why. ~30 min.

**Teacher notes:**

- The exercise lives or dies by the test being **truly red** before students invoke Claude. Walk around and verify.
- Discuss explicitly when TDD is *wrong*: novel exploratory research where the spec doesn't exist yet. Don't be dogmatic.
- For SLURM: if any students don't have cluster access, pair them with someone who does.
- For Ollama: keep this short. It can become a rabbit hole.

**Artifacts:** docs page, link to PyValidator function to delete, example sbatch script.

**Status:** Spec only.

---

### Module 4 — Slash commands and skills

**Time:** 75 minutes (20 min content, 45 min exercise, 10 min recap).

**Objectives:**

- Recognize when a repeated task is worth extracting into a slash command.
- Build one working slash command end-to-end.
- Understand the skill structure at an architectural level *without* attempting to build one.

**Content outline:**

1. **The decision tree.** One-off task → just type it. Repeated task → slash command. Repeated task with structured outputs and reusable scripts → skill. Cross-project standard → consider plugin. Most people skip too far down this list too fast.
2. **Slash command anatomy.** Markdown file in `.claude/skills/<name>/SKILL.md` (recommended) or legacy `.claude/commands/<name>.md`. YAML frontmatter with name and description. The body is a prompt template. `$ARGUMENTS` for parameters. File references with `@filename`. Bash execution with `!`.
3. **Worked example: `/validate-domain`.** Walk through the design. The command wraps PyValidator and produces a human-readable error summary instead of raw output. Why this is worth extracting: every PDDL researcher does this five times a day.
4. **The skill architecture, briefly.** Skills can bundle scripts alongside the SKILL.md. They can be invoked autonomously (Claude decides) or explicitly (`/name`). Show Omer's `induce`/`instantiate`/`orchestrate` triad in `pddl-copilot` as *inspiration*, not as a homework assignment. Explain *why* the work split into three skills rather than one — each has a different invocation context and a different verification surface.
5. **When *not* to build a skill.** Honest pitfalls: premature abstraction, skills that drift from your actual workflow, skills that duplicate `CLAUDE.md` content, skills nobody ever invokes.

**Optional practice:** Build `/validate-domain <path>` end-to-end. The command should: accept a PDDL domain file path, invoke PyValidator (or a stub if PyValidator isn't installed), parse the output, and produce a structured summary (errors grouped by type, suggested fixes if obvious). **Success criterion:** running `/validate-domain examples/blocks.pddl` in any project produces a useful summary, not a raw log dump. ~45 min.

**Teacher notes:**

- **Say "don't build a skill in week one" twice.** It is the single piece of advice most likely to be ignored, and ignoring it is the most expensive mistake students will make.
- When showing `pddl-copilot`, resist the temptation to deep-dive the architecture. The point is to show that "real skill systems exist" — not to teach them how to build one.
- If anyone insists on building a skill during the exercise, redirect them to "build a slash command that does one slice of what your eventual skill will do." Almost always good enough.

**Artifacts:** docs page, walkthrough of `/validate-domain` design, link to `pddl-copilot` skill structure (read-only for inspiration).

**Status:** Spec only.

---

### Module 5 — Avoiding failure modes

**Time:** 60 minutes (15 min content, 30 min exercise, 15 min discussion).

**Objectives:**

- Recognize plausible-but-wrong code visually before running it.
- Develop a code review reflex specifically tuned for AI output.
- Pick model and effort level for the task at hand.
- Articulate, in a sentence, what you'd say if a reviewer asked "did Claude write this?"

**Content outline:**

1. **Cost vs. quality.** Effort level isn't a slider you should max for everything. Quick file rename: minimum. Algorithm reimplementation: maximum. Refactor: middle. Cost and latency follow.
2. **The signature failure modes.** Plausible-but-wrong (looks right, isn't). Confident hallucination (cites an API that doesn't exist). Silent assumption (fills in a spec gap with a guess and doesn't tell you). Test-that-passes-but-doesn't-test-the-thing.
3. **Review patterns.** Spot-check (sample a few lines deeply). Test-run (run the thing — even Claude can't fake a stack trace). Walk-through (have Claude explain its own diff line-by-line and look for vague spots).
4. **Reproducibility & honesty.** What to do when a reviewer asks how the code works. The "Claude wrote it, you own it" principle, this time with teeth. BGU's likely future policies on AI-assisted research (uncertain — flag for students to track).
5. **What to do when it goes wrong.** Roll back, don't patch. `git reflog` is your friend. If Claude rewrote a file you needed, the *first* move is `git status` — not arguing with Claude.

**Optional practice:** Hand students a real diff from Omer's commit history where Claude introduced a subtle bug that Omer caught. Students find the bug, first by reading only, then by running tests. Debrief on *what made it look right*. ~30 min.

**Teacher notes:**

- **CRITICAL: Omer must mine his own git history for a real bug.** A fabricated example will smell synthetic and undermine the module. If no good example exists, replace this exercise with: "code-review this real merged PR from a public repo where AI involvement was claimed."
- The debrief is more important than finding the bug. The point is the *pattern recognition*, not the win.
- Be honest about your own near-misses. Researchers respect failure stories more than success stories.

**Artifacts:** docs page, **a real bug diff with context (Omer to produce)**, review checklist.

**Status:** Spec only. Blocked on Omer's git-history mining.

---

### Module 6 — Case studies

**Time:** 60–90 minutes in-session, plus take-home extension.

**Objectives:**

- See techniques applied in three real research contexts.
- Pick one extension exercise and complete it.
- For RL/MARL/DRL students: apply techniques to their own research repo via the BYOR option.

**Content outline:**

1. **Case study A — PyValidator: porting a binary spec to Python.** The story of replacing a compiled validator with a pure-Python equivalent. What CLAUDE.md looked like at the start vs. at v1.0 release. Where Claude was helpful (boilerplate, edge case discovery). Where it was useless (deciding the public API). Published to PyPI as `pddl-pyvalidator`.
2. **Case study B — pddl-copilot: skill architecture story.** Why the work decomposed into three skills (`induce`, `instantiate`, `orchestrate`). The six-compartment predicate vocabulary. The candidate-and-filter induction loop. Critically: what was tried first and rejected, not just the final design.
3. **Case study C — pddl-copilot-experiments: keeping research code reproducible.** Managing experimental code that mutates weekly. Versioning planner configurations. Reproducing a result two months later. The folder conventions that worked.
4. **Case study D — Bring Your Own Repo (BYOR).** For RL/MARL/heuristic-search students: apply the techniques to your own research code. Write a CLAUDE.md, build one slash command, run a TDD loop on something small. *This is often the most valuable case study for students from adjacent fields.*

**Optional practice:** Pick one case study. Complete its small extension exercise. ~1 hour, take-home.

- **PyValidator extension:** Add a new validator check — e.g., "warn on predicates declared but never used in any action."
- **pddl-copilot extension:** Add one new step to `orchestrate` that does something concrete and testable (structured progress logging is a good first attempt).
- **Experiments extension:** Reproduce a single algorithm comparison run, with Claude Code's help interpreting the output.
- **BYOR extension:** Apply the full Module 2 + Module 3 + Module 4 pipeline to your own repo. Submit a short writeup of what worked and what didn't.

**Teacher notes:**

- **Encourage RL/MARL/DRL students to pick BYOR.** The PDDL-flavored options will feel like tourism for them. BYOR makes the course immediately useful.
- For private repos (pddl-copilot, pddl-copilot-experiments): *Omer to decide whether to make stripped public forks.* If they remain private, case studies B and C become "read the slides and discuss" rather than "clone and extend."
- The BYOR writeups can become a lab resource — short reports from each cohort of what worked in their domain.

**Artifacts:** docs page, links to PyValidator (public) + decisions on pddl-copilot/experiments, BYOR template (CLAUDE.md skeleton + slash command template + writeup template).

**Status:** Spec only. Blocked on Omer's decisions about repo privacy.

---

## 6. Domain adjacency notes (RL, DRL, MARL, heuristic search)

The lessons in this course are domain-independent. The exercises lean PDDL-flavored because:

- Omer has the deepest knowledge there and can answer questions live.
- His three repos provide rich, real case studies.
- PDDL is structurally adjacent to MAPF, heuristic search, and (more loosely) MARL.

For students from RL/DRL backgrounds, the PDDL-flavored exercises are *adequate* but not *ideal*. Mitigations:

- Module 6's BYOR option lets them apply techniques to their own RL code.
- Where possible, framing in earlier modules names RL/MARL analogues alongside planning examples (e.g., "imagine this is your reward function instead of a PDDL action").
- Encourage RL students to bring an RL repo to Module 2 and write its CLAUDE.md during the exercise instead of using the stub.

The instructor should explicitly invite this adaptation in Module 0 so RL students don't feel like they're in the wrong room.

## 7. Open decisions (Omer to resolve before production)

1. **Repo privacy.** Are `pddl-copilot` and `pddl-copilot-experiments` going public, getting stripped public forks, or staying private? Affects Module 6 directly.
2. **Module 5 bug example.** Which real diff from your git history will anchor the exercise? Without one, Module 5 falls back to a weaker alternative.
3. **Module 0 recordings.** Who records the two demo clips? Length, resolution, host (asciinema vs. mp4)?
4. **Live vs. async cadence.** Confirm the "two ~2-hour sessions per week for 3 weeks" structure or propose an alternative that fits the lab schedule.
5. **Audience baseline check.** Survey participants ahead of Module 1: "Have you used Cursor / Copilot / chat AI for code? Are you comfortable on the terminal?" Three audience profiles emerge and Module 1 timing changes accordingly.
6. **AI honesty policy.** What does the lab require participants to disclose about AI-assisted code in publications? Module 5 should reflect the actual policy, not best guesses.

## 8. Production checklist

To move from spec to deployed course:

- [ ] Module 0: docs page + two screen recordings
- [ ] Module 1: docs page + shell config snippet + setup troubleshooting appendix
- [x] Module 2: **fully built** (page, teacher notes, stub repo)
- [ ] Module 3: docs page + PyValidator function selection (Omer picks which function gets deleted) + example sbatch script
- [ ] Module 4: docs page + `/validate-domain` walkthrough + `pddl-copilot` link decision
- [ ] Module 5: docs page + **real bug diff (Omer)** + review checklist
- [ ] Module 6: docs page + BYOR template + repo privacy decisions
- [ ] Site: `mkdocs.yml` finalized, theme polished, deploy workflow tested
- [ ] Repo: README, contributing guide if external participants, license

## 9. Style guide for follow-on production

Anyone producing the remaining modules should match Module 2's properties:

- **Concrete over abstract.** Every claim is grounded in a specific file, command, or observed Claude behavior.
- **Failure modes shown alongside successes.** Each module includes at least one "this is what goes wrong" subsection.
- **Exercises with explicit success criteria.** A student must be able to tell, unambiguously, whether they finished.
- **Teacher notes are operational.** "Walk around and verify X" is more useful than "ensure understanding of X."
- **No motivational fluff.** Researchers tune out "AI will transform your workflow!" content immediately.
- **Length is earned, not assumed.** Module 2's page is long because it has a worked example. Module 0's is short because it doesn't need length.
