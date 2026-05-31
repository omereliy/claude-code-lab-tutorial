# Module 4 — Teacher Notes

**Module:** Slash Commands and Skills
**Time:** 75 minutes
**Difficulty for instructor:** Low mechanically, high on restraint. The hard part is stopping students from building a skill. Expect to redirect at least a third of the room.

---

## Timing breakdown

- **0:00 – 0:20** — Content. The decision tree and the slash-command/skill line are the load-bearing parts. The worked example is the bridge to the exercise.
- **0:20 – 1:05** — Exercise: build `/validate-domain`. Walk the room.
- **1:05 – 1:15** — Recap. Re-state the decision tree; it's the one thing to retain.

## Say "don't build a skill in week one" twice

This is the single most-ignored and most-expensive piece of advice in the course. Say it in the content section, and say it again before the exercise. The students most eager to build a skill are the ones who will waste the most time on one that drifts out of date before they use it ten times. Frame it as a cost, not a rule: *"a skill you build today encodes today's workflow, and your workflow will change before the skill pays for itself."*

## When showing pddl-copilot, do NOT deep-dive

Spec-mandated. The point of the `pddl-authoring` vs `pddl-fixing` example is to show that *real multi-skill systems exist and decompose for a reason* — different trigger, different verification surface. That's it. If you start walking through the fixing loop's five iterations and intent scenarios, you've turned a 90-second illustration into a 15-minute tangent and taught skill-building, which is exactly what this module avoids. Show the two descriptions, name the two differences, move on.

(Note: the spec described this architecture as an `induce/instantiate/orchestrate` triad; the repo today is a 4-plugin marketplace with no such skills. The page teaches the current structure. See the `OMER REVIEW` marker and `PENDING.md` item 2 — confirm what to say about the history and whether to link the repo.)

## The reference `/validate-domain` command

Show this *after* students have built their own, as one reasonable version — not the answer. Emphasize the value is the output-shape instructions, not any cleverness.

```markdown
---
description: Validate a PDDL domain file and report the errors grouped by type with suggested fixes
argument-hint: <path-to-domain.pddl>
---

Validate the PDDL domain at `$ARGUMENTS`.

1. Run the validator on that path. In this exercise it's the stub:
   `python validate_stub.py $ARGUMENTS`. Substitute the real validator if it's
   installed — `pddl-pyvalidator` ships a `pyval` CLI (`pyval $ARGUMENTS`).
2. Read the raw output, then produce a SUMMARY, not a dump:
   - Group findings by category: syntax, undeclared predicate, predicate arity,
     type-hierarchy.
   - Drop exact duplicates.
   - Order categories by severity (parse-blocking errors first).
   - Per group: one example line, plus a suggested fix where it's obvious
     (e.g. "`on` is used with 3 args but declared with 2 — fix the call or the
     declaration").
   - End with a one-line verdict: usable, or must-fix-first?
3. If the domain is actually valid, say so in one line. Do not invent problems.
```

Walk through *why* each instruction is there:

- The numbered output spec is the whole point — without "group / dedup / order / suggest," Claude relays the wall of text.
- "Do not invent problems" matters: on a clean file, an over-eager command will manufacture findings. This is a Module 5 failure mode (confident hallucination) showing up early.
- `$ARGUMENTS`, not a hardcoded path, is what makes it reusable across every domain they'll ever validate.

## Live demo cues

- Before the exercise, run the stub raw once on the projector: `python validate_stub.py examples/blocks.pddl`. Let the room see the ugly wall of output. *That* is the problem the command solves — they need to feel it.
- Then show one bad command (description as a title, no output shape) producing a dump, and one good one producing a summary. The contrast is the lesson.

## Anticipated student questions

**"Why not just always use a skill — it's more powerful?"**
Because power you don't need is maintenance you do. A one-file command has nothing to drift. A skill with scripts has to be kept in sync with a workflow that changes. Use the heavier tool when the lighter one demonstrably fails, not before.

**"`.claude/commands/` or `.claude/skills/`?"**
Both work and invoke the same way. Custom commands moved to skills (`.claude/skills/<name>/SKILL.md`) and that's the recommended form; the single-file `.claude/commands/<name>.md` is legacy-but-supported. For this exercise, one `SKILL.md` file.

**"Can the command run the validator itself, or do I have to?"**
The body instructs Claude to run it (`python validate_stub.py $ARGUMENTS`) — Claude executes it as a normal tool call when the command runs. You *can* pre-run it with `` !`...` `` injection, but that needs `allowed-tools` and is more than this exercise needs. Keep it to one moving part.

**"My command works on `blocks.pddl` but not other files."**
They hardcoded the path. `$ARGUMENTS`. This is the single most common bug in the exercise.

## Pitfalls to catch during the exercise

- **Skill creep.** The instant you see a `scripts/` directory or a second file appear, redirect: "one `SKILL.md`, one prompt." This is the redirect you'll do most.
- **Output is still a dump.** Their description says *what the tool is*, not *what shape to return*. Have them add the explicit "group / dedup / order / suggest" instructions and re-run.
- **They edited the stub instead of the command.** The exercise is the command. The stub is a fixture; leave it alone.
- **Over-validation.** A command that reports problems on a clean file. Add "do not invent problems" and test on a valid domain.

## What to do if a student finishes early

- Have them run the command on a *clean* domain (no planted errors) and confirm it doesn't manufacture findings. If it does, that's the fix-worthy bug — a Module 5 preview.
- Or: have them add a second positional argument (`$2`) — e.g. a severity threshold — and see how `$1`/`$2` differ from `$ARGUMENTS`. Still one file; still a slash command.
- Do **not** let "finished early" become "now build it as a skill." That's the trap.

## Failure modes for the instructor

- **You let the pddl-copilot example run long.** Cap it at 90 seconds. It's an illustration, not a unit.
- **Half the room builds skills anyway.** Expected. Don't lecture; redirect individually and fast. The ones who build a skill and watch it not-help are also learning the lesson the hard way — that's acceptable.
- **The stub confuses someone.** It's a fixture that prints messy validation output for a `.pddl` path; that's all they need to know. If they're debugging the stub, they've lost the plot — point them back at the command.

## Bridge to Module 5

End with: "You've now made the repo, the task, and your repeated workflows safer for Claude. None of it removes the last responsibility: reading what Claude wrote. Module 5 is about the failure modes that survive everything we've built — plausible-but-wrong code — and the review reflexes that catch them before they reach a paper."
