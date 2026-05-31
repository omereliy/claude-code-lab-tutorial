# Module 2 — Making a Research Repo Claude-Friendly

**Time:** 75 minutes.
**Prerequisites:** Module 1 completed. Claude Code installed and working.

---

## Why this module exists

The single biggest predictor of whether Claude Code feels great or terrible in a repo is one file: `CLAUDE.md`. Not your code quality. Not your test coverage. Not your model choice. The presence and quality of `CLAUDE.md`.

This module is short on theory and long on demonstration. You will run the same small task twice in the same repo — once with no `CLAUDE.md`, once with a minimal one — and watch the difference.

## What Claude can infer, and what it can't

Claude Code reads your files. Given a fresh repo, it can quickly figure out:

- The language and framework.
- The directory layout.
- What dependencies are declared.
- What tests look like (if they exist).
- What the public API of each module is (if it's small).

Claude cannot infer:

- **Naming conventions you haven't named.** If your codebase mixes `snake_case` and `camelCase` for historical reasons, and one is "right" and one is "deprecated," Claude has no way to know.
- **Which files are dead.** Half-finished scratch files look the same as the canonical implementation.
- **Where new things should go.** A new utility function — does it belong in `utils.py`, in a new file, in `state.py`, or in a `helpers/` subpackage you're planning to create?
- **What you're currently working on.** A function called `experimental_v3` could be the latest stable version or the one you're about to delete.
- **The "don't touch" zones.** Some files are load-bearing in non-obvious ways. Claude doesn't know.

`CLAUDE.md` is where you tell Claude all of this — and only this. It is not documentation for humans. It is the context Claude can't infer from reading your code.

## Anatomy of a useful CLAUDE.md

A good `CLAUDE.md` is short. 50–150 lines, typically. It contains:

1. **One-sentence project purpose.** "Pure-Python PDDL plan validator, replaces the compiled VAL binary."
2. **How to run and test.** The exact commands. `pytest tests/`, `ruff check src/`, etc.
3. **Code conventions.** Naming style, type hints, docstring style, line length if non-default.
4. **Where things live.** "Public API in `src/<pkg>/__init__.py`. New parser logic in `parser.py`. Don't add to `state.py` without discussion."
5. **Touch-this-carefully zones.** "`legacy_parser.py` is in use by experiments that don't import the new code. Don't refactor it."
6. **Recent context.** What you're currently working on. Updated when you start a new direction.
7. **Things to *not* do.** "Don't add new dependencies without asking. Don't reformat unrelated code."

What does *not* belong:

- Anything in the README (the README is for humans).
- Architectural diagrams (Claude can't read images, and a diagram in markdown will mislead you about Claude's actual context).
- API documentation (Claude reads the code; it doesn't need your prose summary).
- Wishlist items ("we want to use functional patterns") — Claude will follow them and produce code your codebase can't accommodate.
- Marketing language ("a high-performance, modular framework"). Useless to Claude.

The biggest mistake is treating `CLAUDE.md` as a wishlist. If a convention exists only in your head, writing it down doesn't make it real — Claude will follow it and produce code your codebase can't actually accommodate. Write what is true *now*. Update it when reality changes.

## The exercise: a tale of two runs

You'll run the same task twice in a stub repo. The stub is intentionally messy in realistic research-code ways: mixed conventions across files, a half-finished scratch module, useful utilities that aren't where you'd expect.

### Setup

```bash
git clone https://github.com/<workshop-org>/cc-workshop-stub-pddl-inspector.git
cd cc-workshop-stub-pddl-inspector
pip install -e .
pytest  # confirm baseline
```

Open the repo in Claude Code: `claude` from the repo root.

### Run 1 — no CLAUDE.md

Ask Claude, verbatim:

> Add a function `satisfies_goal(state, goal_conjunction)` that returns True if the state satisfies the goal. A goal is a conjunction of positive predicates (no negation, no disjunction). Add a test.

Do not give any other context. Let Claude take the task end-to-end.

**Observe and record:**

- Which file did Claude put the function in? Was it the right one?
- Did Claude follow the naming convention (`snake_case`) or get pulled into the camelCase from `scratch.py`?
- Did Claude reuse `utils.parse_predicate()`, or re-implement predicate handling?
- What does the test look like? Does it follow the pattern in `tests/test_state.py`?
- Does the test pass? Does it test what it claims to test?

Take notes. You'll compare in 10 minutes.

### Now write a CLAUDE.md

Roll back Claude's changes (`git checkout .`). Now write a `CLAUDE.md` at the repo root. Take 10 minutes. Cover at minimum:

- Project purpose (one sentence).
- How to run tests.
- Where the public API lives, and which file new state-checking utilities go in.
- The naming convention (`snake_case`) and the fact that `scratch.py` is deprecated — don't read it, don't mimic it.
- The fact that `utils.parse_predicate()` exists and should be reused for any predicate parsing.

Resist the urge to be thorough. Cover only what Claude needed but didn't have. The reference version is in the teacher notes if you want to compare after.

### Run 2 — with CLAUDE.md

Same prompt, verbatim. Same task.

**Observe:**

- Did the file placement improve?
- Did the convention hold?
- Did Claude reuse the utility?
- Did the test follow the existing pattern?

Discuss with a neighbor: what changed and why?

## Success criterion

You can complete this exercise even if Claude does the wrong thing both times. The success criterion is observational, not technical: **you can name three concrete differences between Run 1 and Run 2, and explain why each one happened.**

If your Run 2 looks identical to Run 1, your CLAUDE.md didn't say the right things. That's a useful finding too — talk to the instructor.

## What goes wrong

Even with a CLAUDE.md, you'll see failure modes. Some you'll see today:

- **The CLAUDE.md drifts.** You write it once. Six weeks later, the codebase has changed and CLAUDE.md hasn't. Now it's actively lying to Claude. Treat CLAUDE.md as code: it has a maintenance cost, and you pay it.
- **Over-stuffing.** A 500-line CLAUDE.md is worse than a 50-line one. Claude reads it every session; you're spending context-window budget on instructions Claude doesn't need this time.
- **Premature patterns.** "We use the repository pattern for data access." Do you? Or is that aspirational? Don't claim conventions you don't actually have.
- **Forgetting `CLAUDE.local.md`.** Personal overrides — paths, secrets, machine-specific settings — go in `CLAUDE.local.md`, which should be gitignored. Use this when working across multiple machines.

## The 30-minute CLAUDE.md

If you take one practical thing from this module, take this: when you start working in a repo with Claude Code, spend 30 minutes writing a `CLAUDE.md` *before* you ask Claude to do anything substantive. Even a bad first attempt beats nothing. Then iterate: every time Claude does something wrong that the right line in `CLAUDE.md` could have prevented, add that line.

A `CLAUDE.md` is alive. It is the file in your repo that most directly determines the quality of your AI-assisted work, and the one most often neglected.

## Recap

- `CLAUDE.md` is the context Claude can't infer.
- It is not the README, not the architecture doc, not the wishlist.
- The repo determines whether Claude Code feels magical or frustrating, and `CLAUDE.md` is the lever.
- Write a minimal one early. Update it when reality changes.

Next: Module 3 — driving Claude through TDD loops, reading unfamiliar repos, and managing SLURM jobs.
