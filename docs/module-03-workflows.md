# Module 3 — Daily Research Workflows

**Time:** 75 minutes (20 min content, 30 min exercise, 25 min discussion).
**Prerequisites:** Modules 1 and 2. A repo with a test runner you can invoke.

---

## What this module is about

Module 2 made the *repo* safe for Claude. This module makes the *task* safe. The throughline is one idea: Claude Code is strongest when the success criterion is explicit and checkable, and the daily workflows below are all ways to make it so. The most important of them is test-driven development, so we start there and spend the most time on it.

## TDD: the constraint that helps the most

Writing the test first feels like extra work. For AI-generated code it's the opposite — it's the cheapest insurance you can buy, because it converts a fuzzy instruction into a checkable one.

Compare two ways to ask for the same thing:

- *"Implement `satisfies_goal(state, goal)`."* Claude has to guess the contract — what a goal is, what counts as satisfaction, what the edge cases are. It will guess plausibly and commit to the guess.
- *"Here's a failing test for `satisfies_goal`. Make it pass."* The contract is now the test. There's nothing to guess; there's something to verify against.

The loop:

1. **Red.** Write (or keep) a test that pins the behavior you want and *fails* for the right reason. Run it. See it fail.
2. **Ask.** Give Claude the failing test. Ask for a **plan first**, then the implementation.
3. **Green.** Run the test *yourself*. Not "Claude says it passes" — you run it.
4. **Refactor.** Ask Claude to clean up the implementation, then re-run the test. If the test breaks, the refactor changed behavior; that's the test doing its job.

Every arrow in that loop is a checkpoint you control. The discipline isn't the testing; it's that you never let Claude move to the next phase without a green light you verified.

## Make Claude show its work

The single habit that most improves auditability: **ask for the plan before the edit.**

> Before you change anything, give me the plan: which files, what changes, what you'll run to verify.

Then read it. Reject a plan that:

- skips a step ("...and update the tests" missing entirely),
- is vague where it should be specific ("improve the logic" instead of "handle the empty-goal case"),
- proposes touching files the task doesn't need.

A plan you can't audit produces a diff you can't audit. Rejecting a mushy plan costs ten seconds; un-reviewing a 200-line diff costs your afternoon.

## Reading an unfamiliar repo

You'll inherit code — a labmate's, a paper's reference implementation, your own from eight months ago. Don't start by asking Claude to change it. Start by asking it to *map* it:

> Give me an architecture summary of this repo. Where are the entry points, where is the test layer, and what three files should I read first to understand it?

Read the summary, then **spot-check it** against the actual files — Claude's map is a hypothesis, not ground truth (recall the Read-phase failure mode from Module 1). Once the map holds up, narrow: "walk me through how `X` flows from entry to output." Only then make changes.

## Paper → code

This is where researchers most often hand Claude too much. The workflow that keeps *you* the author:

1. **Identify** the algorithm and its inputs/outputs from the paper.
2. **Sketch the type signature first**, with Claude's help if you like: `def estimate_advantage(rewards, values, gamma, lam) -> np.ndarray`. The signature is the contract.
3. **Write a tiny test** using one worked example from the paper — an input whose output you can compute by hand.
4. **Then** implement, ideally TDD against that test.

The trap is skipping straight to *"implement Algorithm 3 from this paper."* Claude will produce *an* algorithm, confidently, and you will not be able to tell where it silently diverged from the paper's — a swapped index, a missing normalization, a `<` that should be `≤`. Reimplementing a clear spec is something Claude does well. Deciding *what* the algorithm is remains your job; that's the part with your name on it.

!!! note "RL/MARL analogue"
    Substitute your own object: a reward-shaping term, an advantage estimator, a
    priority function for a replay buffer. Sketch the signature and a unit test on
    a toy two-state MDP *before* letting Claude write the body. The discipline is
    identical; only the nouns change.

## SLURM jobs

On the cluster, Claude is a competent assistant for the mechanical parts and a liability for the expensive ones. Useful patterns:

- **Generate `sbatch` scripts from a description** ("a job that runs `train.py` with 1 GPU, 16 GB, a 4-hour limit, logging to `logs/%j.out`"). An annotated example is in `exercises/m03-tdd-loop/example.sbatch`.
- **Monitor** with `squeue -u $USER` and `sacct -j <jobid>`. Have Claude *summarize* a long log (`grep`-and-summarize), not paste it — a 10,000-line log will blow your context window and bury the one line that matters.

Pitfalls, all of which have bitten someone:

- **Secrets in the environment.** Don't let Claude `env` or `printenv` into the transcript — API keys and tokens leak that way. 
- **Accidentally rerunning expensive jobs.** Have Claude *print* the `sbatch` command for you to submit, rather than submitting it itself. A re-queued 12-hour job is a real cost.
- **Silent resource/partition mistakes.** A wrong partition or a missing `--account` fails late or queues forever. Check the script before submitting.

<!-- OMER REVIEW: I can't verify BGU cluster specifics (partition names, account flags, the QOS setup). The example.sbatch uses clearly-marked placeholders. Please replace with the lab's real partition/account conventions, or point students at the cluster's own docs. -->

## The BGU Ollama server (brief)

The lab runs a local Ollama server with a large GPU pool. Two situations where it's the right call: **data sensitivity** (unpublished data or code you can't send to a hosted API), and **cheap bulk inference** (running a small model over many inputs where API cost would add up). The tradeoff is capability — the hosted Claude models are stronger, so don't route your Claude Code *coding* loop through a local model expecting parity. Use the local server for what it's good at, and keep it out of the critical path of the workflows above.

<!-- OMER REVIEW: I left the Ollama section deliberately short (spec: "keep this short, it's a rabbit hole") and did NOT assert the exact VRAM figure or hostname. Add the real server address, the model(s) available, and the access instructions if you want students to actually use it. -->

## When TDD is the wrong tool

Be honest about this in the room, or you'll sound dogmatic. TDD assumes the spec exists. In genuinely exploratory research — you don't yet *know* the correct behavior, you're trying to discover it — writing the test first means encoding a guess as if it were a requirement. There, Claude is a sketchpad, not a TDD partner: explore, get something running, look at outputs, and add tests once the behavior stabilizes into something you'd defend. The rule is "constrain the task when you can state the criterion," not "always write a test first."

## What goes wrong

- **The test that passes but doesn't test the thing.** The most dangerous green light there is. A test that asserts `result is not None` passes for any non-crash. Read what the assertion actually checks.
- **Claude satisfies the test the wrong way.** Watch for it making the test green by hard-coding the expected return value, weakening the assertion, or special-casing the exact input — instead of implementing the real behavior. The test is green and the code is wrong. This is the single most likely thing to happen in today's exercise; it's also a preview of Module 5.
- **The refactor that changes behavior.** "Clean up" can quietly alter an edge case. Re-run the test after every refactor, not just at the end.
- **Context blowout.** Pasting a huge log or a generated dataset into the conversation crowds out the files that matter. Summarize or `grep` instead.

## Exercise: restore a function via TDD

**Goal:** drive Claude through one red → green TDD loop to restore a deleted function in PyValidator, in **two iterations maximum**.

Full instructions are in `exercises/m03-tdd-loop/`. In brief:

1. In a PyValidator checkout, delete one small, self-contained function — the
   predicate-arity check is the canonical candidate (or the function your
   instructor names).
2. Confirm the matching test now **fails** — run `pytest` and *see the one red
   test* before you involve Claude. If it's not red, stop; there's nothing to drive.
3. Give Claude the failing test. Ask for a plan, then the fix. Run `pytest` yourself.
4. If still red after the first fix, give Claude the new failure once more. Two
   iterations, then stop regardless.

**Success criterion:** the test goes from red to green **because Claude restored the function** — not because it gamed the test — and you can state, in one sentence, what changed and why. If the test is green but the function is hard-coded or the assertion got weaker, that's a *failed* exercise with a valuable lesson; bring it to the discussion.

Time-box: ~30 minutes.

## Recap

- TDD helps AI code disproportionately because it hands Claude a checkable criterion. That's the whole reason.
- Make Claude plan before it edits. Read the diff, not the checkmark.
- Map an unfamiliar repo before changing it; spot-check the map.
- Sketch contracts from papers; don't let Claude design the algorithm.
- TDD is a tool, not a creed — skip it when the spec doesn't exist yet.

Next: Module 4 — turning the prompts you retype every day into slash commands.
