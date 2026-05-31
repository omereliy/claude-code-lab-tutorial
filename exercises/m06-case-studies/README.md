# Exercise m06 — Case study extensions + BYOR

**Module:** 6 — Case Studies
**Time:** ~1 hour, take-home.
**Goal:** apply the whole course to one real repo by completing **one** extension
to its stated done condition.

Pick one path. The BYOR path is strongly recommended if you work in RL, DRL,
MARL, or heuristic search.

---

## The four paths

| Path | For whom | Needs |
|------|----------|-------|
| **PyValidator** | want a guided, self-contained task | public repo (`pddl-pyvalidator`) |
| **pddl-copilot** | want to extend a skill | repo accessible — see Module 6 Case B |
| **Experiments** | want a reproducibility task | repo accessible — see Module 6 Case C |
| **BYOR** | RL/MARL/DRL/search, or anyone with their own repo | your own repo |

`pddl-copilot` and `pddl-copilot-experiments` accessibility depends on the
instructor's repo-privacy decision (PENDING.md item 2). If they're private,
pick PyValidator or BYOR.

## Done conditions (the success criterion for each)

- **PyValidator:** add a check that warns on predicates declared but never used
  in any action. **Done when** it fires on a domain with an unused predicate,
  stays silent on one without, and you added a test for both.
- **pddl-copilot:** add one concrete, testable step to a skill (structured
  progress logging is a good first attempt). **Done when** the step runs as part
  of the skill on a real invocation and produces its output.
- **Experiments:** reproduce one algorithm-comparison run, Claude helping
  interpret it. **Done when** you reproduced one result and can state what it
  shows plus one thing you'd check before trusting it.
- **BYOR:** apply Module 2 + 3 + 4 to your own repo. **Done when** your repo has
  a `CLAUDE.md`, one test-driven change, and one working slash command, and the
  writeup is filled in.

**All paths:** you completed one extension to its done condition, and your
writeup names one place Claude helped and one place it didn't. The writeup is the
deliverable.

## BYOR template

In `byor-template/`:

```
byor-template/
├── CLAUDE.md                              # skeleton — copy to your repo root, fill in
├── WRITEUP.md                             # the deliverable — fill in as you go
└── .claude/skills/example-command/SKILL.md  # slash-command template — one file, rename it
```

1. Copy `CLAUDE.md` to your repo root and fill it in (Module 2). Delete the
   bracketed prompts as you go; keep it short and true-now.
2. Run one TDD loop (Module 3) on a small, real function.
3. Copy `.claude/skills/example-command/` into your repo, rename it, and make it
   one slash command you'll actually use (Module 4). **One file — no scripts.**
4. Review with `../m05-bug-hunt/review-checklist.md` (Module 5).
5. Fill in `WRITEUP.md`. That's what you bring back.

## Don't

- **Don't do a PDDL extension if you're an RL/MARL/DRL student.** It'll feel like
  tourism. Do BYOR.
- **Don't scope-creep BYOR into a full refactor.** One `CLAUDE.md`, one TDD loop,
  one slash command. The pipeline is the point, not a rewrite.
