# Module 4 — Slash Commands and Skills

**Time:** 75 minutes (20 min content, 45 min exercise, 10 min recap).
**Prerequisites:** Modules 1–3. Comfortable running Claude in a repo.

---

## What this module is about

You retype the same prompts. *"Validate this domain and tell me what's actually wrong."* *"Summarize this run's log."* *"Check this plan against the problem."* This module is about capturing those into **slash commands** — and, just as importantly, knowing when to stop there and not over-build into a skill you'll regret.

The discipline this module teaches is restraint. The mechanics take ten minutes; the judgment takes the rest.

## The decision tree (and the mistake everyone makes)

```
one-off task                          -> just type it
task you repeat                       -> slash command (a prompt template, /name)
repeated + bundled scripts +
  structured outputs / auto-invoke    -> skill
a standard across projects/people     -> plugin
```

The mistake — and almost everyone makes it in week one — is jumping two or three rungs down on day one. People build a skill (or a plugin) when a slash command would do, or build a slash command when typing the prompt twice would have been faster. **Default to the lowest rung that works.** The cost of premature abstraction is real, and we'll come back to it.

## Slash command anatomy

A custom slash command is created today as a **skill**: a `SKILL.md` file in a named directory.

- Project-level (committed, shared with the repo): `.claude/skills/<name>/SKILL.md`
- Personal (all your projects): `~/.claude/skills/<name>/SKILL.md`

You invoke it with `/<name>`. Custom commands *moved to* skills; the older single-file form `.claude/commands/<name>.md` still works for backward compatibility, but skills are the recommended way. Same invocation either way.

The minimal shape is frontmatter plus a prompt body:

```markdown
---
description: Validate a PDDL domain and summarize the errors by type
argument-hint: <path-to-domain.pddl>
---

Run the project's PDDL validator on $ARGUMENTS. Then summarize the result:
group errors by type, drop duplicates, order by severity, and suggest a fix
where it's obvious. Do not dump the raw output.
```

What's in there:

- **`description`** — what the command does. This is also how Claude decides whether to *auto-invoke* it, so write it like a trigger, not a title.
- **`argument-hint`** — shown during autocomplete; documents what to pass.
- **`$ARGUMENTS`** — everything you type after the command. Positional `$1`, `$2` also work.
- The body is a **prompt template**. That's the whole thing. The value is in what output shape you specify.

Two more mechanisms you'll see, both a step up in complexity — useful to recognize, not needed today:

- **`@path/to/file`** pulls a file's contents into the prompt.
- **`` !`command` ``** runs a shell command *before* Claude sees the prompt and injects its output. This requires the command to be pre-approved via an `allowed-tools` frontmatter entry, which is why it's not "minimal."

## Slash command vs skill — the real line

The line is **not** the file format — both are `SKILL.md` now. The line is structure and invocation:

- A **slash command** is a skill that's just a prompt template. One file. You invoke it explicitly by name.
- A **skill**, in the heavier sense, is a prompt *plus* bundled scripts, reference files, and structured logic — often invoked *autonomously* by Claude based on its description.

If your `SKILL.md` is one file with a prompt in it, you've built a slash command. The moment you add a `scripts/` folder, multiple reference files, and lean on auto-invocation, you've built a skill. Today we build the former, full stop.

## Worked example: `/validate-domain`

Why this one is worth extracting: every PDDL researcher validates a domain a dozen times a day, and the validator's raw output is a wall of undifferentiated text — syntax complaints tangled with type errors tangled with arity mismatches, in file order, often duplicated. You read the whole wall to find the one line that matters.

The command's job is to wrap the validator and return a **grouped, prioritized summary** instead:

- **Input:** a domain file path, via `$ARGUMENTS`.
- **Action:** run the validator on that path.
- **Output shape (the actual value):** errors grouped by type (syntax, undeclared predicate, predicate arity, type-hierarchy), de-duplicated, ordered by severity, with a suggested fix where the fix is obvious.

Notice there's no code here. The command is pure prompt engineering — the leverage is entirely in specifying the output shape. That's the signature of a task that should be a slash command and not a skill: the work is in *how Claude reports*, not in *bundled logic*. The full reference command is in the teacher notes; you'll write your own version in the exercise.

## The skill architecture, briefly (inspiration, not homework)

To recognize when something *should* be a skill, look at a real one. `pddl-copilot` is a plugin marketplace built from several skills. Two of them illustrate why you'd split work into multiple skills rather than one:

- **`pddl-authoring`** — invoked when you want to *draft* PDDL from a natural-language description. Its definition of "done": the draft parses and validates.
- **`pddl-fixing`** — invoked when a draft *doesn't behave as described*. Its definition of "done" is heavier: parse → validate the problem → solve → validate the plan → check the trajectory, against explicit intent scenarios, escalating to a human after five iterations without convergence.

Same domain, but two **different invocation contexts** (write-from-scratch vs. fix-what's-broken) and two **different verification surfaces** (does it parse? vs. does it behave correctly?). That divergence — distinct trigger, distinct definition of done — is the signal that work should be two skills rather than one overloaded one. Each skill also declares its `allowed-tools` (the specific validator and planner tools it may call), which is what makes its verification surface concrete.

You are not building this today. The point is pattern recognition: a slash command is one prompt; a skill is a bounded job with its own trigger and its own verification surface; a plugin is a bundle of those you ship to other people.

<!-- OMER REVIEW: The spec (Module 4 §4) names the pddl-copilot architecture as an
     "induce / instantiate / orchestrate" triad with a "six-compartment predicate
     vocabulary" and a "candidate-and-filter induction loop." The repo today is a
     4-plugin marketplace (pddl-solver, pddl-validator, pddl-parser, pddl-author)
     with NO skills by those names (grep found none). I taught the decomposition
     lesson from the CURRENT structure (pddl-authoring vs pddl-fixing), which is a
     cleaner example anyway. Please confirm: (1) was induce/instantiate/orchestrate
     an earlier design worth mentioning as history, or should it be dropped? (2) Do
     you want pddl-copilot linked from the page, and is the repo public? This ties
     to PENDING.md item 2 (repo-privacy). -->

## When *not* to build a skill

The honest pitfalls, all of which happen to enthusiastic week-one users:

- **Premature abstraction.** You build a skill for a workflow you've done twice. By the time you've done it ten times, the workflow has changed and the skill encodes the old one.
- **Drift.** Skills rot exactly like `CLAUDE.md` does (Module 2). A skill encoding last month's process silently misleads you this month.
- **Duplicating `CLAUDE.md`.** If your skill mostly restates conventions ("we use snake_case, tests go here"), that's `CLAUDE.md`'s job, not a skill's.
- **Skills nobody invokes.** The most common product of week-one skill enthusiasm is a `.claude/skills/` folder full of things you forgot you wrote.

The rule: build the slash command after you've felt the same pain three times. Build the heavier skill only when the slash command is *demonstrably* not enough. Build the plugin when other people ask you for your slash command.

## Exercise: build `/validate-domain`

**Goal:** build a working `/validate-domain <path>` slash command — one file, one moving part — that turns raw validator output into a useful grouped summary.

Full instructions and a self-contained validator stub are in `exercises/m04-slash-command/`. In brief:

1. Create `.claude/skills/validate-domain/SKILL.md` (a single file — no `scripts/`, no extra files; that would be skill-building).
2. Use `$ARGUMENTS` for the domain path. In the body, instruct Claude to run the provided validator on that path and produce a summary: errors grouped by type, de-duplicated, ordered by severity, with an obvious-fix suggestion where possible.
3. Run `/validate-domain examples/blocks.pddl`. The stub emits deliberately messy raw output; your command's job is to make it readable.

**Success criterion:** running `/validate-domain examples/blocks.pddl` produces a **grouped, prioritized summary** — not a raw log dump and not a vague "there are some errors." A reader should be able to see, at a glance, the *categories* of problem and which to fix first.

Time-box: ~45 minutes. If you find yourself writing a Python script or a second file, stop — you've left the exercise.

## What goes wrong

- **The command dumps raw output anyway.** The prompt didn't actually specify the output shape, so Claude just relays the validator. Fix: the body must say *group, dedup, prioritize* — be specific about the shape.
- **The command is hardcoded to one file.** It works on `blocks.pddl` and nothing else because the path was baked in. Fix: `$ARGUMENTS`.
- **The student builds a skill.** Scripts appear, then a second file, then auto-invocation. Redirect to one `SKILL.md` with a prompt. The exercise is a slash command, full stop.
- **The description is a title, not a trigger.** `description: PDDL tool` won't help Claude know when to use it. Write the description as *when to invoke*.

## Recap

- Default to the lowest rung: type it, then slash command, then skill, then plugin. Most people skip too far too fast.
- A custom slash command is a single-file `SKILL.md` whose value is the output shape it specifies. `$ARGUMENTS` is the only mechanism you need.
- A slash command becomes a skill when you add bundled scripts and auto-invocation — recognizable by a distinct trigger and a distinct verification surface.
- Don't build a skill in week one. Felt the pain three times? Slash command. Slash command not enough? Then consider a skill.

Next: Module 5 — the failure modes that survive all of this, and how to catch plausible-but-wrong output before it lands in a paper.
