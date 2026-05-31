# Module 6 — Case Studies

**Time:** 60–90 minutes in-session, plus a take-home extension.
**Prerequisites:** Modules 1–5. This module applies all of them.

---

## What this module is about

Everything so far has been technique in isolation: a `CLAUDE.md`, a TDD loop, a slash command, a review reflex. This module shows the techniques load-bearing in real research contexts, then hands you one to apply yourself. Three of the case studies are the instructor's own repos; the fourth is yours.

Read for the *decisions*, not the code. Where Claude helped, where it was useless, and — most usefully — what was tried first and abandoned. Final designs teach less than the path to them.

## Case Study A — PyValidator: porting a binary spec to Python

**Repo:** public, on PyPI as `pddl-pyvalidator` (pure-Python PDDL plan validator, Python ≥ 3.10).

The task: replace a compiled validator (the VAL binary) with a pure-Python equivalent you can read, test, and depend on without a build step. A near-ideal Claude Code task — the spec already exists (the binary's behavior), so the success criterion is checkable: does the Python output match the reference?

What to draw from it:

- **`CLAUDE.md` evolved.** It started near-empty and grew toward v1.0 as conventions became real. The Module 2 lesson, lived: you write what's true now and update it when reality changes, not a wishlist up front.
- **Where Claude helped:** boilerplate (parsing scaffolding, the test harness) and *edge-case discovery* — "what inputs break this?" is something Claude is genuinely good at enumerating, and validators live or die on edge cases.
- **Where Claude was useless:** deciding the **public API**. What the package exports, what the function signatures should be, what's stable vs. internal — that's a taste-and-judgment call (Module 0's "success criterion is taste" category). Claude will produce *an* API, confidently; whether it's a *good* one was a human decision.

The shape of the lesson: Claude did the bounded, checkable parts well and the unbounded, judgment parts poorly — exactly as Module 0 predicted.

## Case Study B — pddl-copilot: a skill architecture

**Repo:** a Claude Code plugin marketplace. **Public status: to be decided** (see the conditional note below and PENDING.md item 2).

The lesson here is *decomposition*: why a body of work split into several skills rather than one. The current structure is a marketplace of plugins (PDDL solving, validation, parsing, authoring), and within authoring, the work splits along the line Module 4 drew:

- **Authoring** a PDDL draft from a description — definition of done: it parses and validates.
- **Fixing** a draft that doesn't behave as described — definition of done is heavier: parse → validate → solve → validate the plan → check the trajectory against explicit intent scenarios, escalating to a human after a bounded number of iterations.

Same domain, two **different invocation contexts** and two **different verification surfaces**. That divergence — distinct trigger, distinct definition of done — is the signal to split rather than overload one skill. Each skill also declares the specific tools it may call, which is what makes its verification surface concrete rather than aspirational.

What was tried first and rejected matters more than the final shape — ask the instructor live; that history is the real content of this case study.

!!! note "Conditional content — depends on the repo-privacy decision"
    <!-- OMER REVIEW: PENDING.md item 2. Choose per pddl-copilot:
         (a) public  -> turn the extension below into a real "clone & extend".
         (b) stripped public fork -> point the link at the fork.
         (c) private -> this case study is "read along / discuss in class", no clone.
         ALSO (PENDING + Module 4 marker): the COURSE_SPEC described this repo as an
         `induce / instantiate / orchestrate` triad with a "six-compartment predicate
         vocabulary" and a "candidate-and-filter induction loop". The repo today is a
         4-plugin marketplace with NO skills by those names. I taught the decomposition
         lesson from the CURRENT structure (authoring vs fixing). Confirm whether the
         induce/instantiate/orchestrate design is earlier history worth mentioning, or
         should be dropped entirely. I did NOT transcribe repo internals into this
         public page; fill in concretely once privacy is decided. -->
    **If public / stripped fork:** clone it and read the skill definitions; the
    extension exercise below becomes hands-on.
    **If private:** treat this as a read-along discussed live; skip to the
    PyValidator or BYOR extension for your take-home.

## Case Study C — pddl-copilot-experiments: keeping research code reproducible

**Repo:** a research harness (experimental code that mutates weekly). **Public status: to be decided** (PENDING.md item 2) — and this one carries unpublished, in-flight research, so it is the most likely to stay private or ship as a stripped fork.

This case study is about a problem every experimentalist has: code that changes every week, and a result you need to reproduce two months later for a reviewer. The transferable conventions (these are generic good practice, not specific to any one repo):

- **Date- or run-stamped result directories.** Results land in directories tagged by run and date, never overwritten in place. Two months later, "which run produced Figure 3?" has an answer.
- **Versioned configurations.** Planner/model configs are captured per run, so a result is tied to the exact config that produced it — not to "whatever the defaults were that week."
- **A changelog for the harness.** Research code benefits from the same `development/CHANGELOG.md` discipline as a library: what changed, when, why. It's how you reconstruct what "the code" meant at the time of a past result.
- **An anonymized variant of the inputs.** Keeping an anonymized copy of the domain/problem set alongside the real one supports sharing and contamination-control without exposing in-flight material.

Where Claude Code fits: writing the `sbatch` plumbing, summarizing long run logs (Module 3), and — carefully — interpreting outputs. Where it doesn't: deciding *what* to measure and whether a result is real. Those are research judgments you own (Module 5).

!!! warning "Conditional content — likely private"
    <!-- OMER REVIEW: repo-privacy decision needed (Case C). The page keeps only
         generic, transferable conventions — no repo internals. Full rationale and
         the decision options are in PENDING.md (not part of the deployed site). -->
    **If a stripped fork exists:** it should preserve the folder conventions and
    harness structure while removing results, checkpoints, and unpublished data.
    **If private:** this is a discuss-in-class case study; the conventions above
    are the portable takeaway. Apply them to your own experiment repo regardless.

## Case Study D — Bring Your Own Repo (BYOR)

**This is the one that makes the course pay off for you**, especially if you work in RL, DRL, MARL, or heuristic search rather than planning. The PDDL case studies are adjacent to your work but not *your* work; BYOR is.

Take your own research repo and run the full pipeline on it:

1. **Module 2:** write a `CLAUDE.md` — the real conventions, the dead files, where new code goes, the don't-touch zones.
2. **Module 3:** run one TDD loop on something small and real — restore or add a function with a test you wrote first.
3. **Module 4:** build one slash command for a thing you actually retype — validate a config, summarize a run, check an invariant.
4. **Module 5:** review what Claude produced with the checklist, and write down one failure mode you hit.

A starter template is in `exercises/m06-case-studies/byor-template/`: a `CLAUDE.md` skeleton, a slash-command template, and a writeup template. The writeup is the deliverable.

## Exercise: pick one extension (take-home, ~1 hour)

Pick **one**. Each has an explicit done condition.

- **PyValidator extension.** Add a new validator check: warn on predicates
  declared but never used in any action. **Done when:** the check runs, fires on
  a domain with an unused predicate, stays silent on one without, and you added a
  test for both cases.
- **pddl-copilot extension** *(if public / fork — see Case B)*. Add one concrete,
  testable step to a skill — structured progress logging is a good first attempt.
  **Done when:** the new step runs as part of the skill and produces the logged
  output on a real invocation.
- **Experiments extension** *(if accessible — see Case C)*. Reproduce a single
  algorithm-comparison run and have Claude help interpret the output. **Done
  when:** you reproduced one result and can state, in a sentence, what it shows
  and one thing you'd check before trusting it.
- **BYOR extension** *(recommended for RL/MARL/DRL)*. Apply the full Module 2 + 3
  + 4 pipeline to your own repo. **Done when:** your repo has a `CLAUDE.md`, one
  test-driven change, and one working slash command — and you've filled in the
  writeup template with what worked and what didn't.

**Success criterion (all paths):** you completed one extension to its stated done
condition, and your writeup names one place Claude helped and one place it didn't.
The writeup, not the code, is what you bring back.

## What goes wrong

- **PDDL tourism.** RL/MARL students do a PDDL extension, find it mildly
  interesting, and take nothing back to their own work. If that's you, do BYOR
  instead — the others will feel like sightseeing.
- **BYOR scope creep.** "Apply the techniques to my repo" becomes "refactor my
  whole codebase with Claude." Keep it to *one* of each: one `CLAUDE.md`, one TDD
  loop, one slash command. The point is the pipeline, not a rewrite.
- **The case study read as a success story.** These repos worked *because* of the
  failures along the way — the abandoned designs, the wrong first `CLAUDE.md`, the
  bug that shipped. If you only hear the wins, you've misread the module.
- **Reproducibility deferred.** "I'll organize the results later" is how the
  two-months-later reproduction fails. The conventions in Case C cost little up
  front and save the afternoon you'd otherwise lose. Adopt them before you need
  them.

## Recap

- PyValidator: Claude excelled at bounded, checkable work (boilerplate, edge
  cases) and failed at judgment (the public API). Module 0, confirmed.
- pddl-copilot: split work into skills along *invocation context* and
  *verification surface* — distinct trigger, distinct definition of done.
- Experiments: reproducibility is folder discipline — stamped results, versioned
  configs, a changelog, anonymized inputs. Cheap up front, decisive later.
- BYOR: the techniques are domain-independent. The proof is your own repo with a
  `CLAUDE.md`, a TDD loop, and a slash command — and a writeup of what held and
  what didn't.

This is the end of the core course. You can set a repo up for Claude, drive it
through constrained loops, extract the repeated work, and catch what slips
through. The rest is reps on your own code.
