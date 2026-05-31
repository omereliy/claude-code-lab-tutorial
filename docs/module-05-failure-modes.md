# Module 5 — Avoiding Failure Modes

**Time:** 60 minutes (15 min content, 30 min exercise, 15 min discussion).
**Prerequisites:** Modules 1–4. You've seen Claude write code; now you learn to distrust it productively.

---

## What this module is about

Everything so far has been about setting Claude up to succeed: a good `CLAUDE.md`, a constraining test, a focused slash command. This module is about the failures that survive all of that — because some always do. The skill is not "make Claude perfect." It's "catch the wrong output before it reaches a paper or an experiment."

The frame is the one from Module 0, now with teeth: **Claude wrote it, you own it.** A reviewer who finds a bug in your method does not care who typed the line. This module is the review reflex that keeps that from happening.

## Cost vs. quality: effort is a decision

Effort level (Module 1) is a dial, and the instinct to pin it to the top is wrong. Higher effort costs more and is slower, and most tasks don't need it. The persistent levels are `low`, `medium`, `high`, `xhigh` (set via `effortLevel` / `/effort`); `max` exists as a session-only setting for the rare case that warrants it. Match the dial to the task:

| Task | Effort | Why |
|------|--------|-----|
| Rename a variable across files | `low` | Mechanical. Deep reasoning buys nothing. |
| Write a test for a known behavior | `low`–`medium` | The behavior is specified; execution is the work. |
| Refactor with behavior preserved | `medium`–`high` | Some judgment, bounded by existing tests. |
| Reimplement an algorithm from a paper | `xhigh`/`max` | Subtle, easy to get plausibly wrong. This is where reasoning pays. |

The trap is treating effort as "quality" rather than "reasoning depth for this task." A top-effort model still produces plausible-but-wrong code; effort reduces the rate, it doesn't eliminate the category. Spend it where the failure would be expensive.

## The signature failure modes

Learn to recognize these four by sight. Each looks fine on a glance, which is exactly the problem.

1. **Plausible-but-wrong.** The code reads correctly, uses the right names, has the right shape — and computes the wrong thing. A `<` that should be `≤`. A normalization applied once too few. The most common and most dangerous mode, because nothing flags it.
2. **Confident hallucination.** Claude calls an API, flag, or function that does not exist, with complete confidence. `np.geometric_mean()`, a `--resume` flag the tool never had. Catches you because the *shape* of the call is idiomatic.
3. **Silent assumption.** You left a gap in the spec; Claude filled it with a guess and didn't tell you. "What happens on an empty input?" — it picked something. The danger isn't the guess; it's the silence. You don't know a decision was made.
4. **Test-that-passes-but-doesn't-test-the-thing.** (You met this in Module 3.) The test is green and asserts nothing meaningful — `assert result is not None`, or it re-derives the expected value with the same buggy logic. Green light, no signal.

What these share: they all pass a casual read. The defense is never a casual read.

## Review patterns

Three reflexes, in increasing cost. Use the cheapest that fits the risk.

- **Spot-check.** Pick the two or three lines where the logic actually lives — the comparison, the index, the recurrence — and read *those* deeply. Skip the boilerplate. You're not reading everything; you're reading the load-bearing lines.
- **Test-run.** Run the thing. Claude can fake a confident explanation; it cannot fake a stack trace or a failing assertion in your own shell. For confident hallucinations, running the code is the fastest possible refutation — the nonexistent API throws `AttributeError` immediately.
- **Walk-through.** Have Claude explain its own diff, line by line, and watch for the vague spots. "This handles the edge case" — *which* edge case, *how*? Vagueness in the explanation marks where Claude itself doesn't have a crisp justification, which is where the silent assumption usually hides.

Match the pattern to the mode: spot-check finds plausible-but-wrong; test-run kills confident hallucination; walk-through surfaces silent assumptions; reading what the assertion *actually checks* catches the hollow test.

## When it goes wrong: roll back, don't patch

When Claude has made a mess — rewrote a file you needed, tangled three changes together, "fixed" something into a worse state — the instinct is to ask Claude to fix it. Resist. The first move is **`git status`**, not another prompt.

- **`git status` first.** See what actually changed before you do anything. Don't argue with Claude about what it did; look.
- **Roll back, don't patch.** `git checkout .` or `git restore` to the last good state, then redo the task with a tighter prompt. Patching a tangled change with more Claude usually deepens the tangle.
- **`git reflog` is your safety net.** Even commits you think you lost are usually recoverable. If Claude rewrote history or you reset too hard, `git reflog` shows where you were.
- **Commit before you let Claude loose.** The cheapest insurance: a clean commit before a substantial Claude task means rollback is always one command away. Make this a habit, not an afterthought.

This is why Module 1 separated identity from authentication and why every exercise has you run tests yourself: so that when it goes wrong — and it will — you have a known-good state to return to.

## Reproducibility and honesty

The reviewer's question, asked plainly: *"Did Claude write this, and do you understand it?"* You need an answer you'd defend.

- **You own it.** Authorship of the paper means authorship of the method, regardless of who typed the code. "Claude wrote that part" is not a defense of a wrong result; it's an admission you didn't review it.
- **Understand it well enough to explain it.** The walk-through pattern is not just for catching bugs — it's the bar for whether you can put your name on the code. If you can't explain why a line is there, you haven't finished reviewing.
- **Reproducibility outlives the session.** The code has to run and make sense two months from now, to a reviewer who wasn't in the room. AI assistance doesn't change that bar; it raises the stakes, because it's easy to ship code you never fully read.

!!! warning "Lab AI-disclosure policy — to be confirmed"
    What SPL Lab requires you to disclose about AI-assisted code in publications
    is a policy question, not a technical one, and it is not yet settled.
    <!-- OMER REVIEW: PENDING.md item 6. If a formal lab/BGU policy exists, state
         it here concretely (what must be disclosed, where, in what form). If none
         exists, that absence is itself worth surfacing to students — and possibly
         proposing a policy as a course outcome. Do not invent a policy. -->
    Until then: disclose conservatively, keep your reasoning trail, and treat
    "I can explain every line" as the personal standard regardless of what the
    formal policy turns out to require.

## What goes wrong (with the review process itself)

The failure modes don't stop at the code — your review has its own:

- **Review theater.** Skimming the diff, nodding, approving. A fast read of plausible-but-wrong code feels like review and catches nothing. If you didn't read the load-bearing lines deeply or run the thing, you didn't review it.
- **Trusting the summary over the diff.** Claude's "I added input validation and updated the tests" is a claim. The diff is the evidence. Read the diff.
- **Maxing effort as a substitute for review.** "I used the highest effort, so it's probably right." Effort lowers the error rate; it never removes the need to check.
- **Anchoring on Claude's explanation.** If you ask Claude "is this correct?" it will tend to defend its own code. Better: ask it to *find the bug* in its own diff, or review it yourself against the spec, not against Claude's narration.

## Exercise: find the planted bug

**Goal:** find a real bug Claude introduced — first by reading only, then by running tests — and articulate *what made it look right*.

<!-- BLOCKED: This exercise is anchored on a REAL diff from Omer's git history
     where Claude introduced a subtle bug he caught. That diff is not yet
     produced. See PENDING.md item 1. Until it exists, run the FALLBACK below. -->

!!! warning "Primary exercise pending"
    The primary exercise uses a real bug diff from the instructor's own history
    (the authenticity is the point — a fabricated bug smells synthetic). That
    diff is not yet in the repo. Until it is, run the fallback below; it teaches
    the same reflex.

The flow, once the diff exists (`exercises/m05-bug-hunt/`):

1. Read the diff and the short context file (what task Claude was asked to do). **Reading only — no running.** Try to find the bug by eye. Note how long it takes and whether you find it.
2. Now run the tests. Watch the bug surface (or not).
3. Debrief — the important part — on **what made it look right.** The recognition pattern matters more than the catch.

**Fallback exercise (use until the real diff lands):** pick a real, merged pull
request from a public repo where AI involvement was claimed (or any non-trivial
PR), and code-review it as if it were your own submission. Use the review
checklist in `exercises/m05-bug-hunt/review-checklist.md`. Find one thing you'd
push back on. The skill is identical; only the source of the diff differs.

**Success criterion:** you can name, in one sentence, *what made the bug (or the questionable code) look right* — the specific reason a casual reader would have approved it. Finding the bug is secondary; recognizing the *pattern that disguised it* is the skill that transfers.

## Recap

- Effort is a per-task decision, not a quality slider. It lowers the error rate; it never removes review.
- Four failure modes to recognize by sight: plausible-but-wrong, confident hallucination, silent assumption, hollow test.
- Three review reflexes: spot-check the load-bearing lines, run the thing, walk through the diff. Match the reflex to the mode.
- When it breaks: `git status` first, roll back don't patch, `git reflog` is your net, commit before you let Claude loose.
- You own it. The bar is "I can explain every line," whatever the disclosure policy turns out to require.

Next: Module 6 — the techniques applied to real research repos, plus bring-your-own.
