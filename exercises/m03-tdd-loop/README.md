# Exercise m03 — Restore a function via TDD

**Module:** 3 — Daily Research Workflows
**Time:** ~30 minutes.
**Goal:** drive Claude through one red → green TDD loop, in **two iterations
max**, to restore a function you deleted — and verify it *restored* the
function rather than *gamed* the test.

This exercise uses PyValidator (`pddl-pyvalidator`, the pure-Python PDDL plan
validator; requires Python ≥ 3.10). Get a checkout the same way as in
exercise m01.

<!-- OMER REVIEW: Which PyValidator function students delete is pending your pick
     (PENDING.md item 4). The criteria: small (15–40 lines), has a clear test
     that goes RED (a real assertion failure, not an import/collection error)
     when the function is missing, and unambiguous correct behavior. The
     predicate-arity check is the working candidate below — confirm it exists and
     has such a test, or name a replacement, and fill in the exact file path. -->

---

## Setup

```bash
# in your PyValidator checkout
pip install -e .
pytest            # confirm a fully GREEN baseline first
```

If the baseline isn't green, fix that before doing anything else — you can't
tell a meaningful red from a broken setup.

## Step 1 — Make it red (the part that matters)

Delete one small, self-contained function. **Candidate:** the predicate-arity
check (the function that rejects a predicate used with the wrong number of
arguments).

```bash
# locate it, then delete just the function body + def line
grep -rni "arity" <pyvalidator-src>/    # find the function
```

Now run the test that covers it:

```bash
pytest -k arity        # adjust to the real test name
```

**You must see one test FAIL — not ERROR.** A failure means an assertion didn't
hold (the behavior is gone). An error at collection (e.g. `ImportError` because
something still imports the deleted name) is *not* the right red — fix the import
so the failure is a clean assertion failure, or you'll spend the exercise on
plumbing instead of the loop.

Do not involve Claude until you can point at one red test that failed for the
right reason.

## Step 2 — Drive the loop

1. Start `claude` in the repo. Show it the failing test output.
2. Ask for a **plan first**: *"This test fails. Propose a plan to fix it — which
   file, what function, what you'll run to verify. Don't edit yet."*
3. Read the plan. If it proposes weakening the test or hard-coding a value,
   reject it and ask again.
4. Let it implement. Then **run `pytest` yourself.**
5. Still red? Give it the new failure once more. After the second iteration,
   stop regardless of outcome.

## Step 3 — Verify it actually restored the function

Green is necessary, not sufficient. Read the diff and confirm:

- The function computes the result; it doesn't hard-code the test's expected value.
- The assertion is the same one you started with (Claude didn't weaken it).
- It isn't special-cased to the exact test input — try a second input by hand.

## Success criterion

The test goes from red to green **because Claude restored the function**, and you
can state in one sentence what changed and why.

If the test is green but the function was gamed (hard-coded, weakened assertion,
special-cased), that is a **failed exercise with the most valuable lesson in the
module** — bring that diff to the discussion. Catching a hollow green is the
whole point.
