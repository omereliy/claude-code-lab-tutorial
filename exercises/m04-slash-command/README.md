# Exercise m04 — Build `/validate-domain`

**Module:** 4 — Slash Commands and Skills
**Time:** ~45 minutes.
**Goal:** build a working `/validate-domain <path>` slash command — **one file,
no scripts** — that turns the messy raw output of a PDDL validator into a
grouped, prioritized summary.

This exercise is self-contained. The only dependency is Python 3 (for the stub
validator); you do not need PyValidator installed.

---

## What's here

```
m04-slash-command/
├── README.md            # this file
├── validate_stub.py     # a FAKE validator that prints realistic, messy output
└── examples/
    └── blocks.pddl      # a domain with three planted errors
```

The stub is a fixture. **Don't edit it** — the exercise is the command, not the
validator. Run it once to see the mess you're taming:

```bash
cd exercises/m04-slash-command
python3 validate_stub.py examples/blocks.pddl
```

You'll get unsorted findings across several categories, mixed severities, and a
duplicate — exactly the wall of text a real validator hands you.

## Step 1 — Create the command (one file)

From the exercise directory, create exactly one file:

```
.claude/skills/validate-domain/SKILL.md
```

That single `SKILL.md` is the whole command. **Do not** add a `scripts/`
folder, a second markdown file, or anything else — the moment you do, you've
started building a skill, which is not this exercise.

Minimum shape:

```markdown
---
description: Validate a PDDL domain and summarize the errors grouped by type
argument-hint: <path-to-domain.pddl>
---

<your prompt here — see Step 2 for what it must specify>
```

## Step 2 — Make the prompt specify the output *shape*

The value of this command is not that it runs the validator — it's *how it
reports*. Your prompt body must instruct Claude to:

1. Run the validator on the path in `$ARGUMENTS`
   (here: `python3 validate_stub.py $ARGUMENTS`).
2. Produce a **summary, not a dump**:
   - group findings by category (syntax / type / undeclared predicate / arity),
   - drop exact duplicates,
   - order by severity (parse-blocking first),
   - suggest a fix where it's obvious,
   - end with a one-line verdict.
3. If the domain is actually valid, say so in one line — **do not invent
   problems.**

Use `$ARGUMENTS` for the path. Do **not** hardcode `examples/blocks.pddl` — a
command that only works on one file isn't a command.

## Step 3 — Run it

Start Claude from the exercise directory so the relative paths resolve:

```bash
cd exercises/m04-slash-command
claude
```

Then:

```
/validate-domain examples/blocks.pddl
```

If `/validate-domain` doesn't appear, the skill directory was created *after*
this session started — run `/reload-skills`, or restart `claude`.

Compare your command's output to the raw `python3 validate_stub.py
examples/blocks.pddl`. The raw version is the problem; your summary is the
solution.

## Success criterion

Running `/validate-domain examples/blocks.pddl` produces a **grouped,
prioritized summary** — categories of problem visible at a glance, duplicates
gone, most-severe first, with a one-line verdict — **not** a raw log dump and
**not** a vague "there are some errors."

Concretely, your output should make these three planted problems legible as
distinct categories: an **undeclared type** (`crate`), an **undeclared
predicate** (`stackable`), and a **predicate-arity** mismatch (`on` used with 3
args, declared with 2).

## If you finish early

- Run your command on a **clean** domain (delete the three bad lines from a copy
  of `blocks.pddl`). Does it correctly say "valid," or does it manufacture
  findings? If it invents problems, that's the bug to fix — and a preview of
  Module 5's "confident hallucination."
- Add a second positional argument (`$2`), e.g. a minimum severity to report,
  and see how `$1`/`$2` differ from `$ARGUMENTS`. Still one file; still a slash
  command.

**Do not** turn this into a skill (scripts, multiple files, auto-invocation).
If you're tempted, that's Module 4's whole lesson talking — resist it.
