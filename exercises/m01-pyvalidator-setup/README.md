# Exercise m01 — Install, configure, and run the loop once

**Module:** 1 — Setup & Mental Model
**Time:** ~30 minutes (after install; budget more if Claude Code isn't installed yet).
**Goal:** prove your setup works by driving Claude Code through one complete
read → plan → act → verify loop on a real, public repo.

This is a *setup confirmation*, not a coding challenge. If it's hard, the
problem is your environment, not your skill — flag the instructor.

---

## Part A — Configure (one time)

Templates live in `shell-config/`. Read its `README.md`, then:

1. Set your persistent model and effort in `~/.claude/settings.json`
   (copy from `shell-config/claude-settings.example.json` and edit).
2. Make sure the Claude Code binary is on your `PATH`
   (`claude --version` works in a **fresh** shell).
3. *Optional, only if you commit under more than one identity:* set up the
   `includeIf` git config from `shell-config/gitconfig*.example` and verify
   with `git config user.name` in two directories.

You're done with Part A when `claude --version` works in a fresh shell and,
once you've started a session with `claude`, the in-session `/status` command
shows the right model and account.

## Part B — Run the loop

1. **Get PyValidator.** It's a pure-Python PDDL plan validator, published as
   `pddl-pyvalidator` (requires Python ≥ 3.10).

   ```bash
   git clone <PYVALIDATOR_REPO_URL>   # see note below
   cd pyvalidator                     # adjust if the repo dir differs
   pip install -e .                   # add pytest if it isn't pulled in
   pytest                             # confirm a green baseline
   ```

   <!-- OMER REVIEW: PyPI metadata for `pddl-pyvalidator` declares no source URL,
        so I can't confirm the public clone URL without inventing it. Please fill in
        <PYVALIDATOR_REPO_URL> with the real public repo and correct the directory
        name if it isn't `pyvalidator`. Tracked in PENDING.md. -->

   **Fallback if you can't clone yet:** `pip install pddl-pyvalidator`, then do
   steps 2–3 against the installed package. You'll write your test in a fresh
   `test_edge.py` that imports from the installed module instead of editing the
   repo's own test suite. The learning is identical.

2. **Read phase, made visible.** From the repo root, run `claude` and ask,
   verbatim:

   > What does this repo do? Where's the entry point, and where do the tests live?

   Read the answer. This is Claude doing the **Read** phase out loud. Note one
   thing it got right and one thing it glossed over.

3. **Plan before act.** Ask Claude to add **one** test for an edge case. Pick one:
   - an **empty plan** (zero actions),
   - a **malformed action name** (e.g. unbalanced parentheses, or an action not
     in the domain),
   - a **predicate with the wrong arity** (too many or too few arguments).

   Tell Claude: *"Propose a plan first. Don't edit anything yet."* Read the plan.
   If it skips a step or is vague about what the test asserts, reject it and ask
   for a sharper one. Only then let it write the test.

4. **Verify.** Run `pytest`. Read the result yourself — don't take Claude's
   "all tests pass" on faith.

## Success criterion

**One sentence, unambiguous:** the new test exists, runs under `pytest`, and
either passes or **fails meaningfully** — the failure points at the validator's
real behavior, not at a broken import or a typo'd fixture.

You should be able to state, in one sentence each:

- what your test checks, and
- which of the four loop phases (read / plan / act / verify) you trusted least,
  and why.

If both sentences come easily, you're done. If your test passes but you can't
say what it actually checks, that's a hollow test — keep it; you'll meet that
failure mode again in Module 5.

## If you finish early

Ask Claude a deliberately vague version of the task — *"make the validator
better"* — and watch the plan turn to mush. That's a preview of Module 0's
"where it struggles" and Module 5's failure modes. You don't have to run it;
just read the plan and notice the difference.
