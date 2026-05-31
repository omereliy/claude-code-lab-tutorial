# Agent Handoff Instructions

You are picking up work on a Claude Code workshop course for academic researchers at SPL Lab, BGU. The original designer (Omer Eliyahu) has approved the course structure. Your job is to produce the remaining modules to match the quality of the exemplar.

## What's already done

- `COURSE_SPEC.md` — the master spec. Read this first, in full, before writing anything.
- `docs/module-02-claude-md.md` — Module 2 page, fully built. **This is your style template.**
- `docs/teacher-notes/module-02.md` — Module 2 teacher notes. **Match this depth.**
- `exercises/m02-claude-md-stub/` — the stub repo for Module 2's exercise. **Match this design philosophy** if asked to build similar stubs.
- `mkdocs.yml` — site config template.
- `.github/workflows/deploy.yml` — GitHub Pages deploy workflow.

## What you're producing

For each module *except* Module 2:

1. `docs/module-0N-<slug>.md` — the page content
2. `docs/teacher-notes/module-0N.md` — teacher notes
3. Any exercise scaffolding listed in the spec for that module

You are **not** producing:

- Module 5's real bug example (Omer must mine his own git history).
- Module 0's screen recordings (Omer must record).
- Decisions about whether `pddl-copilot` and `pddl-copilot-experiments` go public (Omer's call).

When you encounter blocked work, leave a clearly marked `<!-- BLOCKED: ... -->` comment in the relevant page and continue.

## Style requirements (non-negotiable)

Match Module 2's page in these dimensions:

1. **Concreteness.** Every claim is grounded in a specific file path, command, behavior, or observed failure. No statements of the form "Claude is good at X" without a demonstration.

2. **Failure modes alongside successes.** Every module page includes at least one "what goes wrong" subsection. Researchers distrust pure success narratives.

3. **Exercises with explicit success criteria.** Each exercise must answer: "How do I know I'm done?" in one unambiguous sentence.

4. **Operational teacher notes.** Write notes that an instructor can scan during the workshop. "Walk around and verify the test is actually red before students start" beats "ensure students understand TDD."

5. **No motivational language.** Cut: "Claude Code transforms your research workflow." Keep: "Here is the loop. Here is when it breaks."

6. **Length earned, not assumed.** Don't pad. Module 0 should be shorter than Module 2. Module 6 may be longer because it has four sub-cases.

7. **No emojis.** Researchers don't want them. The exemplar has none.

8. **British or American spelling — pick one and be consistent.** (Module 2 uses American; match it unless Omer specifies otherwise.)

## Voice

The voice is direct, slightly opinionated, and assumes a competent reader. It is not the voice of a marketing page. Sample sentences from Module 2 that capture the tone:

> "CLAUDE.md is not documentation for humans. It is the context Claude can't infer from reading your code."

> "The biggest mistake is treating CLAUDE.md as a wishlist. If a convention exists only in your head, writing it down doesn't make it real — Claude will follow it and produce code your codebase can't actually accommodate."

> "If you find yourself writing five paragraphs about the architecture, stop. That's a README problem, not a CLAUDE.md problem."

Match this. Avoid AI-blog-post voice ("Let's dive in!", "In this article, we'll explore...").

## Per-module production order (recommended)

Build in this order to maintain coherence:

1. **Module 1 (Setup)** — straightforward; mostly install + config + first-loop.
2. **Module 0 (Framing)** — easier to write *after* Module 1, because you'll know what Module 1 covers and can avoid duplication.
3. **Module 3 (Workflows)** — TDD loop. Important. Don't rush.
4. **Module 4 (Slash commands)** — be careful not to teach skill-building. The exercise is a slash command, full stop.
5. **Module 5 (Failure modes)** — blocked on Omer's bug example. Produce the page assuming a placeholder, mark the exercise section as blocked.
6. **Module 6 (Case studies)** — blocked on repo privacy decisions. Produce the page with conditional content for each repo's public/private status.

## Exercise design principles

When producing exercise scaffolding:

- **Time-boxed.** State an explicit estimate (e.g., "~30 min"). Do not exceed 60 min for in-session exercises.
- **Self-contained.** Students should not need to clone five repos and install six tools to start.
- **Failable.** Easy success isn't a learning moment. Design exercises where students *can* take the wrong path, observe the consequence, and recover.
- **Realistic.** Use the actual idioms of research code (messy, partial, naming inconsistencies), not synthetic textbook code.

For the Module 2 stub repo `exercises/m02-claude-md-stub/`, study how it embeds traps:

- Two naming conventions in different files (snake_case in most, camelCase in `scratch.py`).
- A `utils.py` containing a function students should reuse but might miss.
- A half-finished `scratch.py` that will distract Claude without CLAUDE.md.
- Tests that establish a clear pattern Claude should follow but doesn't always.

Replicate this *philosophy* (not these exact traps) when designing stubs for other modules.

## File naming

- Module pages: `module-0N-<short-slug>.md` (e.g., `module-03-workflows.md`).
- Teacher notes: `module-0N.md` inside `docs/teacher-notes/`.
- Exercise directories: `m0N-<short-slug>/` inside `exercises/`.

## What to do when uncertain

If you encounter an ambiguity not resolved by the spec:

1. Check `COURSE_SPEC.md` § 7 "Open decisions" — your question may be there.
2. If not, leave an `<!-- OMER REVIEW: ... -->` comment in the relevant file and continue. Do not invent.
3. If the ambiguity blocks an entire module, stop and produce a summary of blocking questions rather than guessing.

## Verification before handing back

Before declaring done:

- [ ] All seven modules have a page.
- [ ] All seven modules have teacher notes.
- [ ] Every exercise has explicit success criteria.
- [ ] Every page has at least one failure-modes subsection.
- [ ] No emojis, no motivational language, no AI-blog tone.
- [ ] `mkdocs serve` runs locally without errors.
- [ ] All `<!-- BLOCKED: -->` and `<!-- OMER REVIEW: -->` comments are listed in a top-level `PENDING.md` so Omer can resolve them.
- [ ] No content invents details about Omer's personal repos that aren't in the spec.

## Final note

The course is for researchers who will be skeptical of AI tooling. Earn their trust by being honest about failure modes, specific about successes, and disciplined about scope. The exemplar Module 2 was written with that audience in mind. Match it.
