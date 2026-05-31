# Module 2 — Teacher Notes

**Module:** Making a Research Repo Claude-Friendly
**Time:** 75 minutes
**Difficulty for instructor:** Medium. Live-demo failure is the pedagogical point, so resist the urge to "fix" it.

---

## Timing breakdown

- **0:00 – 0:10** — Framing. The "one file matters more than anything else" pitch.
- **0:10 – 0:25** — What Claude can/can't infer. Anatomy of CLAUDE.md.
- **0:25 – 0:35** — Live demo Run 1 (no CLAUDE.md). **You drive, projector on.**
- **0:35 – 0:45** — Students write their own CLAUDE.md.
- **0:45 – 0:55** — Students run Run 2 with their CLAUDE.md.
- **0:55 – 1:10** — Debrief: pairs share what changed. Surface patterns.
- **1:10 – 1:15** — Recap and bridge to Module 3.

If you're running tight on time, **cut the recap, not the debrief.** The debrief is where learning consolidates.

## What to emphasize live

1. **CLAUDE.md is not the README.** Say this three times across the module. Students will keep collapsing the two in their heads.
2. **Write what's true now, not what should be true.** This is the single insight that prevents the most common failure (wishlist CLAUDE.md that produces wrong code).
3. **The 30-minute first draft.** Frame this as the entry-level habit. Anyone can do 30 minutes.

## Live demo cues

You're doing Run 1 in front of the room with no CLAUDE.md. Things will likely go wrong. Wanted outcomes — at least one of these usually happens:

- Claude adds the function to a *new* file (`goals.py`?) rather than `state.py`.
- Claude follows the camelCase style from `scratch.py` for the function or its helpers.
- Claude re-implements predicate parsing inline instead of using `utils.parse_predicate()`.
- Claude writes a test that doesn't use the existing `tests/conftest.py` fixtures.
- Claude writes a test that passes but tests the wrong thing.

**Do not "rescue" the demo.** If Claude does something dumb, narrate it and move on. The demo is most pedagogically valuable when it fails partway.

If Claude *succeeds* despite no CLAUDE.md — which happens occasionally — discuss with the room *why* this particular task was inferable. Then sharpen the task: "okay, now ask Claude to update `__init__.py` to export this function." Inconsistency in the exports list will usually break the second prompt.

## Anticipated student questions

**"Should CLAUDE.md be in git?"**
Yes. It's project context, not personal context. Personal overrides go in `CLAUDE.local.md` and are gitignored.

**"Does CLAUDE.md duplicate the README?"**
No. The README is for humans evaluating whether to use your library. CLAUDE.md is for Claude doing work *inside* your library. They overlap maybe 10%.

**"What if I have multiple Claude-related files? `CLAUDE.md`, `AGENTS.md`, etc.?"**
For Claude Code, `CLAUDE.md` is the file Claude looks for by default. Some projects also keep an `AGENTS.md` for cross-tool compatibility (Cursor, OpenAI agents, etc.). One source of truth, multiple symlinks, or just pick one — your call. Don't fragment.

**"My CLAUDE.md is getting huge. Is that a problem?"**
Yes. Claude reads it every session. Over ~500 lines you're spending context budget on instructions Claude doesn't need *this* time. Split into module-specific CLAUDE.md files if your repo has clear sub-packages — Claude Code will pick up the nearest one.

**"What about prompt injection? Can a malicious CLAUDE.md harm me?"**
Treat CLAUDE.md the same as any code file in your repo — review changes in PRs. The risk surface is similar to a malicious `Makefile` or `conftest.py`.

**"Can I have Claude *write* my CLAUDE.md for me?"**
Yes, and it's a fine bootstrap. But you must review and edit. Claude will produce a plausible-looking CLAUDE.md that is partially wrong because it can't observe your team's actual conventions (only what's in code).

## The reference CLAUDE.md

After students have run Run 2 and debriefed, show this as one reasonable version. Emphasize it is *one* reasonable version, not *the* answer.

```markdown
# pddl_inspector

A small Python tool for inspecting PDDL-like states and checking simple goal
conditions. Used as a teaching example; not a production tool.

## Run and test

- Install: `pip install -e .`
- Tests: `pytest tests/`
- Lint: `ruff check src/`

## Code conventions

- All code is `snake_case`. Public API uses underscored names.
- Type hints required on all public functions.
- Docstrings: short imperative form, no formal type sections (types are in
  signatures).
- Line length: 100.

## Where things live

- Public API: re-exported from `src/pddl_inspector/__init__.py`.
- State data structures and state-level operations: `src/pddl_inspector/state.py`.
  New state-checking utilities go here.
- Parsing predicates and atoms: `src/pddl_inspector/parser.py`. Reuse
  `parse_predicate()` for any predicate string handling — do not re-implement.
- Small helpers: `src/pddl_inspector/utils.py`. Read it before adding a new helper.

## Do not touch

- `src/pddl_inspector/scratch.py` — abandoned experimental code in camelCase.
  Do not read, mimic, or import from this file. It will be deleted next refactor.

## Tests

- Pytest. Shared fixtures in `tests/conftest.py` — use them.
- One test file per source module: `tests/test_<modname>.py`.
- New tests for state operations go in `tests/test_state.py`.

## What I'm working on

Currently adding goal-checking utilities to `state.py`. Public API will gain
a `satisfies_goal(state, goal)` function.
```

Walk students through *why* each line is there. The "Do not touch" section is the line they're most likely to forget — point at the messes Claude made in Run 1 that this line would have prevented.

## Pitfalls to surface in debrief

These come up almost every cohort:

- **"My Run 2 looked the same as Run 1."** Their CLAUDE.md probably said the right things in the wrong way. Common: stating principles ("use clean code") instead of instructions ("put new state utilities in `state.py`"). Show them a concrete reframing.
- **"Claude ignored my CLAUDE.md."** Almost never true. Check what they actually wrote. Usually they wrote a fact Claude couldn't act on (e.g., "follow PEP 8" — but PEP 8 doesn't disambiguate `state.py` vs. a new file).
- **"This feels like over-engineering for a small repo."** Push back. A small repo with a one-paragraph CLAUDE.md is fine. The point is the *habit*, not the volume.
- **"What about for code I'll throw away?"** No CLAUDE.md needed. The cost-benefit only makes sense for repos you'll work in repeatedly.

## What to do if a student finishes early

- Have them try a *harder* prompt: "Now refactor the goal check to support negation." Watch Claude make a bigger mess without an updated CLAUDE.md.
- Or: have them remove their CLAUDE.md and try the original prompt with a different model/effort level. The result is informative.

## Bridge to Module 3

End with: "We've made the repo safer for Claude. Now we need to make the *task* safer. Module 3 is about driving Claude through structured loops — TDD, especially — so even when CLAUDE.md isn't enough, you have a second line of defense."

## Failure modes for the instructor

- **Demo goes too well.** Claude nails the no-CLAUDE.md run. Have a backup harder prompt ready (the `__init__.py` exports one above).
- **Demo goes too badly.** Claude crashes or wanders. Cut the demo short, narrate what you saw, move to the exercise. Don't burn 10 minutes trying to recover a demo.
- **A student writes a CLAUDE.md that's mostly README content.** Catch this during the writing window. Ask them: "If Claude could already see your README, what's left for CLAUDE.md to add?"
- **The room splits between confident and lost students.** Pair them. The confident student explaining CLAUDE.md to the lost student consolidates the lesson for both.
