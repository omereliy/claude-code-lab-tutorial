# Module 3 — Teacher Notes

**Module:** Daily Research Workflows
**Time:** 75 minutes
**Difficulty for instructor:** Medium. The exercise has one hard prerequisite (a genuinely red test) and one common failure (Claude gaming the test) that you must catch live.

---

## Timing breakdown

- **0:00 – 0:20** — Content. Spend the bulk on TDD; move quickly through SLURM and Ollama.
- **0:20 – 0:50** — Exercise: restore a deleted function via TDD.
- **0:50 – 1:15** — Discussion. This is 25 minutes on purpose — the debrief is where the lesson lands.

If you're short on time, **cut the SLURM and Ollama content, not the discussion.** Those two sections are reference material students can read; the TDD debrief is the part that only happens live.

## The exercise lives or dies on one thing

**The test must be truly red before a student involves Claude.** Walk the room and confirm it. The failure you'll see: a student deletes the function, the import now fails, and `pytest` errors out at *collection* with an `ImportError` — that's not the same as a clean red test, and Claude will "fix" it by patching the import in ways that miss the point. Make sure the red is a real assertion failure (function missing/returning wrong value), not a collection error.

Concretely, before anyone prompts Claude, they should be able to point at output that says one test *failed* (not *errored*), for the right reason.

## The failure you are hunting for in the debrief

Most cohorts produce at least one student whose test went green **without** the function being correctly restored:

- Claude hard-coded the expected return value.
- Claude weakened the assertion to something that always passes.
- Claude special-cased the exact test input.

**This is the most valuable artifact in the room.** Don't treat it as a student failure — treat it as the lesson. Put that diff on the projector (with permission) and ask: "the test is green. Is the code right? How would you have caught this?" That conversation is Module 3's whole point and the bridge to Module 5.

## What to emphasize live

1. **You run the test, not Claude.** Say it explicitly. "Claude says it passes" is a claim; `pytest` in your own shell is evidence.
2. **Plan before edit.** Demonstrate rejecting a vague plan once, live, so they see what "reject and ask for sharper" looks like.
3. **TDD is not a religion.** Pre-empt the dogmatism objection yourself (see below) before a skeptic raises it — you'll have more credibility raising it first.

## When TDD is wrong — say this before someone objects

A researcher will (correctly) point out that TDD assumes you know the answer, and exploratory research often doesn't. Get ahead of it: TDD is for when you can *state the criterion*. For genuinely novel work, Claude is a sketchpad; you add tests once the behavior stabilizes. If you present TDD as universal law, the room's most experienced researchers will tune out. Presenting its limits *first* buys you their trust on everything else.

## SLURM — keep it grounded, keep it short

- If some students have no cluster access, **pair them** with someone who does. Don't let the no-access students disengage.
- The two pitfalls worth stating out loud: (1) never let Claude dump `env`/`printenv` into the transcript — secrets leak; (2) have Claude *print* the `sbatch` line, you submit — so it can't re-queue an expensive job.
- The `example.sbatch` in the exercise dir uses placeholder partition/account values. **Substitute the real BGU values before class** (see the `OMER REVIEW` markers in the page and `PENDING.md`), or tell students explicitly that those fields are placeholders.

## Ollama — resist the rabbit hole

One slide's worth, maximum. The decision rule is the whole content: local server for data you can't send out or cheap bulk inference; hosted Claude for the actual coding loop. If someone wants to benchmark the local model against Claude, that's an after-class conversation, not a workshop segment.

## Anticipated student questions

**"Isn't writing the test first just slower?"**
For throwaway exploration, yes — don't. For anything you'll keep or that Claude writes, the test is what lets you trust a diff you didn't write line-by-line. The time you "lose" writing it you save not auditing 200 lines by hand.

**"Claude wrote the test too. Is that okay?"**
Risky. If Claude writes both the test and the code, it can make both agree on the wrong behavior. Have Claude *propose* a test, but you read it and decide what it should assert. The test is your specification; own it.

**"What if there's no existing test to make red?"**
Then write the smallest one that pins the behavior you want, and confirm it fails before implementing. That *is* the exercise for the paper→code workflow.

## If a student finishes early

- Have them do the **paper→code** workflow on a tiny algorithm: sketch a signature, write one test from a worked example, implement via TDD. This is the harder, more realistic skill.
- Or have them deliberately try to make Claude game the test, then write the assertion that would have caught it. Inoculation by construction.

## Failure modes for the instructor

- **No red, no exercise.** If a student's deletion produces a green suite (they deleted something unused, or there's no covering test), they have nothing to drive. Have a known-good function/test pair ready as a fallback (this is the `OMER REVIEW` item: confirm which PyValidator function has a clean covering test).
- **The room rabbit-holes on SLURM.** Cluster war stories eat time. Acknowledge, park, move on.
- **A green test lulls the room.** If everyone's test passes and nobody looks at the diff, you've lost the lesson. Force the question: "green — but did it restore the function, or fool the test?"

## Bridge to Module 4

End with: "You've seen how a test constrains Claude into auditable work. Some of these constraints you'll want every day — validate this domain, summarize this run. Module 4 is about capturing those repeated prompts as slash commands, and knowing when *not* to over-build them."
