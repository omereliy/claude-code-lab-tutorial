# Module 5 — Teacher Notes

**Module:** Avoiding Failure Modes
**Time:** 60 minutes
**Difficulty for instructor:** Medium-high, and personal. The module's credibility rests on you telling a real failure story of your own. If you can't, the room won't either.

---

## Timing breakdown

- **0:00 – 0:15** — Content. The four failure modes and the three review reflexes are the core. The cost/quality table is quick.
- **0:15 – 0:45** — Exercise: find the bug (real diff if available, fallback PR review otherwise).
- **0:45 – 1:00** — Debrief. This is the module. The catch is secondary; the *pattern recognition* is the lesson.

If you run short, **cut content, not debrief.** Students can read the four modes; they cannot read their way into the reflex of distrusting plausible code.

## The exercise is blocked on a real diff — read this

The primary exercise needs a **real bug from your own git history** where Claude introduced something subtle you caught. This is spec-critical and not optional-feeling:

- **A fabricated bug smells synthetic.** This audience reverse-engineers things for a living. A planted, too-clean bug undermines the whole module — they'll sense it was built to be found.
- The diff should: be non-obvious on a read, become obvious on a run or careful read, fit on one screen, and come with a one-line "what made it look right."
- Strip anything sensitive; drop it in `exercises/m05-bug-hunt/` with a short context file (what task Claude was asked to do).

**Until that diff exists, run the fallback:** have students code-review a real merged PR from a public repo (AI-involvement-claimed if you can find one, any non-trivial PR otherwise) using the review checklist. Same reflex, weaker authenticity. The checklist is already in the exercise dir; the diff is the missing piece.

(Tracked in PENDING.md item 1.)

## Tell your own near-miss

The single most effective thing you can do in this module: **tell a real story of when Claude burned you and you caught it — or didn't.** Researchers trust failure stories far more than success stories. The bug you shipped, the experiment you re-ran, the reviewer comment that stung. If you sanitize this into "sometimes mistakes happen," you've taught nothing. Be specific and a little uncomfortable.

This is also why the spec flags Omer mining his own history: the real diff isn't just an exercise input, it's *the* artifact that makes the module land.

## What to emphasize live

1. **A casual read is not a review.** The four failure modes all pass a glance. Say it plainly: if you skimmed and approved, you didn't review.
2. **Run the thing.** Claude can fake an explanation; it can't fake a stack trace. For hallucinated APIs, running the code is the instant refutation.
3. **`git status` before you argue with Claude.** When it goes wrong, the first move is to *look at what changed*, not to prompt again. Demonstrate this live — make a mess, then `git status`, then `git checkout .`.
4. **Effort is not absolution.** "I used max effort" is not a substitute for reading the diff.

## The cost/quality table — make it concrete

Don't just show the table. Ask the room: "You're renaming a variable across 12 files. Max effort or min?" Then "you're reimplementing the advantage estimator from a paper?" The contrast teaches the principle faster than the table does. The goal is to break the reflex of maxing everything.

## Anticipated student questions

**"If I have to review everything, what did Claude save me?"**
The writing, not the thinking. Reading correct code is far faster than writing it. The saving is real; it just isn't "stop reviewing." (Same answer as Module 0 — they'll re-ask it here with more weight.)

**"How do I know the test actually tests the thing?"**
Read what the assertion checks, and ask whether it would still pass if the function were subtly wrong. A test that passes on a known-broken version is testing nothing. This is the Module 3 hollow-green, returning.

**"What do I tell a reviewer who asks if Claude wrote it?"**
The honest, defensible answer: "Yes, with my review; I can explain every line and here's how it's tested." The indefensible one: "Claude wrote that part" as an excuse. Whether *disclosure* is required is a policy question — see below.

**"Is there a lab/BGU policy on disclosing AI-assisted code?"**
As of now this is unsettled (PENDING.md item 6). Don't invent one. Say what's true: the policy isn't fixed yet; disclose conservatively; keep your reasoning trail; hold yourself to "I can explain every line." If a real policy lands, the page gets updated to state it.

## The review checklist

`exercises/m05-bug-hunt/review-checklist.md` is the durable takeaway — the thing students should pin above their desk. Walk through it once. It's organized by the four failure modes so the checklist *is* the recognition training. Tell them to actually use it on the exercise, not just read it.

## Pitfalls to surface in debrief

- **"I found the bug fast."** Good — now: *what made it look right?* If they can't answer, they pattern-matched luck, not skill. Push for the disguise mechanism.
- **"I read it and it looked fine, then the test caught it."** Perfect illustration of why reading isn't enough. Hold this up.
- **"I'd have approved this in a real PR."** The most honest and most valuable admission. Thank them for it; that's the fear that makes the reflex stick.
- **Review theater.** If someone skimmed and declared it clean, and the bug was real, that's the live demonstration of the module's central risk. Handle it without humiliation — it's the universal default, not a personal failing.

## What to do if a student finishes early

- Have them write the *minimal test that would have caught* the bug. Constructing the catch is harder than finding the bug and cements the lesson.
- Or: have them deliberately ask Claude "is this code correct?" and watch it defend its own bug, then ask "find the bug in this code" and watch the difference. The framing effect is worth seeing firsthand.

## Failure modes for the instructor

- **No real diff, weak fallback.** If you're stuck on the fallback PR, pick the PR *before* class and confirm it has something genuinely reviewable. A trivial PR makes for a flat exercise.
- **You defend Claude.** Same trap as Module 0. If a student finds a bug, don't explain it away. Own it.
- **The debrief becomes a bug-hunt scoreboard.** Who-found-it-fastest is not the point. Redirect every "I found it" to "what disguised it." The pattern is the product.
- **Doom spiral.** A room full of researchers can talk themselves into "then AI is useless." Pull back to the through-line: constrained loops + review make it net-positive. The point is calibrated trust, not no trust.

## Bridge to Module 6

End with: "You can now set Claude up to succeed and catch it when it fails anyway. Module 6 is where it all gets applied to real research repos — including, if you bring one, yours."
