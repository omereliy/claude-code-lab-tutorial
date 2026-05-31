# Exercise m05 — Find the planted bug

**Module:** 5 — Avoiding Failure Modes
**Time:** ~30 minutes + 15 min debrief.
**Goal:** find a bug Claude introduced — first by reading only, then by running
tests — and name *what made it look right*.

---

## Status

<!-- BLOCKED: The primary exercise is anchored on a REAL diff from Omer's git
     history where Claude introduced a subtle bug he caught. That diff + its
     context file are not yet in this directory. See PENDING.md item 1.

     When ready, add here:
       - bug-diff.patch        (the diff, sensitive content stripped)
       - context.md            (what task Claude was asked to do; what repo;
                                what made the bug look right — instructor copy)
     and replace the "pending" note below with the real instructions. -->

> **Primary exercise pending.** It uses a real bug diff from the instructor's
> own history — the authenticity is the point; a fabricated bug smells
> synthetic to this audience. Until that diff lands in this directory, run the
> **fallback** below. It trains the same reflex.

## Primary exercise (once the diff is here)

1. Read `bug-diff.patch` and `context.md`. **Reading only — do not run
   anything.** Try to find the bug by eye. Note how long it takes.
2. Now run the tests. Watch the bug surface (or watch it slip through your
   read).
3. Debrief: what made it look right? The disguise mechanism is the lesson.

## Fallback exercise (use until the real diff lands)

1. Pick a real, **merged** pull request from a public repo. Ideal: one where AI
   involvement was claimed. Acceptable: any non-trivial PR you didn't write.
2. Review it as if it were your own submission about to go into a paper's
   artifact, using `review-checklist.md` in this directory.
3. Find **one** thing you would push back on — a load-bearing line you'd want to
   trace, an assumption you'd question, a test that doesn't test the thing.

Work through the checklist top to bottom. It's organized by the four failure
modes, so it doubles as recognition training.

## Success criterion

You can state, in **one sentence**, *what made the bug (or the questionable
code) look right* — the specific reason a careful-but-rushed reviewer would have
approved it.

Finding the bug is secondary. Recognizing the **pattern that disguised it** is
the skill that transfers to your own work. "I found it" is not the deliverable;
"here's why it looked correct" is.

## Files

- `review-checklist.md` — the durable takeaway. Use it here; keep it after.
- `bug-diff.patch`, `context.md` — *pending* (instructor to add).
