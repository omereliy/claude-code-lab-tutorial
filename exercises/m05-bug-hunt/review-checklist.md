# AI-output review checklist

A review reflex tuned for AI-generated code. Organized by the four failure
modes from Module 5 — the checklist *is* the recognition training. Use it on a
real diff, not as bedtime reading.

The rule under all of it: **a casual read is not a review.** If you didn't read
the load-bearing lines deeply or run the thing, you didn't review it.

---

## Before you start

- [ ] Do I know what the code is *supposed* to do, independently of Claude's
      description of what it did? (Review against the spec, not the narration.)
- [ ] Is there a clean commit to roll back to if this is worse than it looks?

## 1. Plausible-but-wrong (it reads right, computes wrong)

- [ ] I identified the 2–3 **load-bearing lines** (the comparison, the index,
      the recurrence, the off-by-one candidates) and read *those* deeply.
- [ ] Boundary conditions: `<` vs `<=`, `0` vs `1`, inclusive vs exclusive,
      first/last element.
- [ ] Every transformation that should happen, happens exactly once
      (no missing or doubled normalization / scaling / sign flip).
- [ ] Units and shapes line up (array dims, radians vs degrees, prob vs logit).
- [ ] I traced one concrete input through by hand and got the expected output.

## 2. Confident hallucination (it cites things that don't exist)

- [ ] Every non-obvious API / method / flag actually exists — I checked the
      docs or `--help`, I didn't trust the idiomatic-looking name.
- [ ] **I ran the code.** A nonexistent API throws immediately; a real run is
      the fastest refutation.
- [ ] No invented config keys, env vars, or file paths.
- [ ] Cited papers / equations / constants are real and say what's claimed.

## 3. Silent assumption (it filled a spec gap and didn't say)

- [ ] I found where the spec was ambiguous and checked what Claude *chose*
      (empty input, null, ties, overflow, concurrent access).
- [ ] Default values and fallback branches reflect *my* intent, not a guess.
- [ ] I asked Claude to walk through the diff and flagged every vague phrase
      ("handles the edge case" — which one? how?). Vagueness marks a guess.
- [ ] Nothing was silently dropped, reordered, or "cleaned up" beyond the task.

## 4. Test-that-passes-but-doesn't-test-the-thing

- [ ] Each new test's assertion would **fail** on a subtly-broken version of
      the code (it isn't `assert result is not None` or equivalent).
- [ ] The expected value is computed independently, not re-derived with the
      same logic under test.
- [ ] The test exercises the behavior the task is about, not just that the code
      runs without crashing.
- [ ] I ran the suite **myself** and read the result — I didn't trust
      "all tests pass."

## When it has already gone wrong

- [ ] `git status` **first** — look at what changed before prompting again.
- [ ] Roll back to the last good state; redo with a tighter prompt rather than
      patching the tangle with more Claude.
- [ ] `git reflog` if I think I lost something — it's usually recoverable.

## Before I put my name on it

- [ ] I can explain **every line** to a reviewer who asks "did Claude write
      this?" — if I can't explain a line, I'm not done reviewing.
- [ ] It will still run and make sense in two months, to someone who wasn't here.
- [ ] Effort level was matched to the task — and I reviewed it regardless of
      how high I set the dial.
