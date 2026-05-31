# Module 0 — Why This Course Exists

**Time:** 15–20 minutes.
**Prerequisites:** None. This is the framing module — read it before you install anything.

---

## The one claim this course makes

Claude Code is a research tool with a definite shape. It is not magic, and it is not a chat window that can see your code. Used inside its shape, it saves you a week. Used outside it, it quietly wastes an afternoon and hands you plausible-looking work you then have to debug. This course is about the shape: where the tool fits, where it doesn't, and how to tell the difference before you've burned the afternoon.

If you came in skeptical, good. The fastest way to distrust a tool permanently is to be oversold on it once.

## What Claude Code is

A terminal-native agent. You run `claude` in a repo and it gets tool access to your filesystem and shell — it can read and edit files, run commands, grep, run your tests, and (optionally) reach external tools over MCP. It works by running a loop: **read** the relevant files, **plan** a sequence of changes, **act** by editing and running things, **verify** by testing and re-reading. Module 1 has you run that loop end-to-end; for now, just hold the shape.

The consequences of "terminal-native agent" are the whole point:

- It works across **many files at once**, not one buffer.
- It can run **long tasks** — a refactor that touches thirty files, a test suite that takes two minutes — because it has a real shell, not a text box.
- It can **observe results** (a stack trace, a failing assertion, `git diff`) and react to them, instead of guessing at output it can't see.

## What it is not

Three tools get confused with Claude Code. They are not interchangeable:

- **Not Cursor.** Cursor is editor-coupled: it lives in your IDE, optimized for a tight edit-and-review loop on code you're actively looking at. Claude Code lives in the terminal and is optimized for longer, multi-file, run-it-yourself tasks. If you've used Cursor heavily, this is the difference that will trip you up most — name it out loud.
- **Not Copilot.** Copilot is autocomplete. It predicts the next few lines as you type. It is not agentic: it doesn't plan, run commands, or verify. Different job entirely.
- **Not chat Claude.** The Claude website has no persistent workspace, no shell, no ability to run your tests. You paste code in and copy answers out. Claude Code *is* in your repo. The gap between "describe my code to an assistant" and "an assistant that has my code" is most of what this course is about.

## Where it shines

Concrete tasks where Claude Code reliably earns its keep:

- **Long-running work across many files.** A rename that ripples through a package. Threading a new argument through a call chain.
- **Repetitive refactors.** The kind that are mechanical but too numerous to do by hand without errors.
- **Reading an unfamiliar codebase.** "Where's the entry point, where do the tests live, what should I read first?" is a genuinely good first prompt in a repo you've never seen.
- **Writing tests.** Especially edge cases you'd skip when bored.
- **Running and interpreting experiments.** Driving a script, reading the logs, summarizing what happened — anything that benefits from having a real shell.

## Where it struggles

This is the half of the picture most tutorials skip. Claude Code is weak, sometimes dangerously confident, on:

- **Fuzzy specs.** "Make it better." "Optimize this." "Clean it up." With no success criterion, Claude guesses at what you meant and commits to the guess. The output looks like work and may be the wrong work.
- **Tasks that need runtime state it can't observe.** A bug that only appears with a specific tensor shape on the GPU, or a race that shows up only under SLURM. Claude can't see what it can't run.
- **Novel algorithm *design*.** Reimplementing a published algorithm from a clear description: good. Inventing a new heuristic or a new training scheme: that's research, and it's yours. Claude is a strong typing partner and a poor co-author of novel ideas.
- **Anything where the success criterion is taste.** API design, what to name the public interface, whether an abstraction earns its keep. Claude will produce *a* answer, confidently. Whether it's a *good* one is your call.

The pattern: Claude Code is strongest when the success criterion is explicit and checkable, and weakest when it isn't. Most of this course is techniques for making the criterion explicit — a `CLAUDE.md` (Module 2), a failing test (Module 3), a slash command with a fixed output shape (Module 4).

## "Claude wrote it, you own it"

The principle to carry through the whole course, introduced here and given teeth in Module 5:

**If your name is on the paper, the code is yours — regardless of who typed it.**

A reviewer will not accept "Claude wrote that part" as a defense of a wrong result. You cannot delegate accountability to a tool. This is not a reason to avoid Claude Code; it's a reason to read what it produces. The researchers who get burned are the ones who treated "it ran and the tests passed" as "it's correct." Those are different claims, and Module 5 is about the gap between them.

!!! note "For RL, DRL, MARL, and heuristic-search students"
    The exercises in this course lean PDDL-flavored, because that's where the
    instructor can answer your questions live. **You are not in the wrong room.**
    The techniques — making a repo Claude-friendly, driving TDD loops, building a
    slash command, auditing AI output — are domain-independent. Where a PDDL
    example appears, mentally substitute your own: a reward function instead of a
    PDDL action, a replay buffer instead of a state parser. Module 6 includes a
    bring-your-own-repo option built specifically so you apply the whole pipeline
    to your actual research code. Bring a repo.

## Exercise: name the difference

You'll watch two short screen recordings of Claude Code on the same project:

- **Recording A** — a structured task with a checkable goal. It goes well.
- **Recording B** — a vague task with no clear success criterion. It flails.

Before the instructor says anything, write down: **what's different about the two tasks** — not the two outputs, the two *tasks*. The point isn't that one worked; it's *why* one was set up to work and the other wasn't. That distinction is the entire course in miniature.

<!-- BLOCKED: The two screen recordings (A: structured task succeeding in PyValidator; B: vague task flailing) must be produced by Omer. See PENDING.md item 3. Until they exist, run this as a live demo or describe both runs verbally. Format: asciinema preferred, mp4 acceptable. -->

!!! warning "Recordings pending"
    The two demo recordings are not yet produced. Run this section as a live
    demo, or describe both runs from memory, until the clips are recorded.

**Success criterion:** you can state, in one sentence, the difference between a task Claude Code is set up to succeed at and one it isn't. If your sentence is about the *task's success criterion* and not about Claude being "smart" or "dumb," you've got it.

## Recap

- Claude Code is a terminal-native agent that runs a read → plan → act → verify loop with real shell access. It is not Cursor, not Copilot, not the chat website.
- It shines when the success criterion is explicit and checkable; it struggles when it's fuzzy, unobservable, novel, or a matter of taste.
- Whatever it writes, you own. Read it.

Next: Module 1 — install it, configure it, and run the loop once yourself.
