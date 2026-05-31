# Pending Decisions

Items that block production of remaining modules. Each must be resolved by Omer
before the corresponding module can ship.

## High priority (block specific modules)

### 1. Module 5 — Real bug example
**Blocks:** Module 5 exercise.
**Required:** A real diff from your git history (any of your repos) where Claude
introduced a subtle bug you caught. Ideal properties:
- Bug is non-obvious from reading the diff in isolation.
- Becomes obvious when running tests or reading carefully.
- The diff is small enough to fit on one screen.
- You can articulate what made it look right.

Strip any sensitive content. Add the diff under `exercises/m05-bug-hunt/` along
with a short context file describing what task Claude was asked to do.

### 2. Module 6 — Repo privacy decisions
**Blocks:** Module 6 case studies B and C.
**Required:** Decide for each of `pddl-copilot` and `pddl-copilot-experiments`:
- (a) Make fully public.
- (b) Create stripped public fork (recommended — also serves as recruiting material).
- (c) Keep private — case study becomes "read the slides, discuss in class."

If creating stripped forks, the fork should preserve the architecture lessons
(skill structure, folder conventions) without exposing in-flight research or
unpublished results.

### 3. Module 0 — Screen recordings
**Blocks:** Module 0 exercise.
**Required:** Two short screen recordings (3–5 minutes each):
- Recording A: Claude Code doing a structured task in PyValidator and succeeding.
- Recording B: Claude Code attempting a vague task and producing mediocre output.

Format: asciinema preferred (renders inline in MkDocs Material with the
asciinema-player extension), mp4 acceptable. Host on the repo or unlisted YouTube.

## Medium priority (affect content choices)

### 4. Module 3 — Function to delete
**Blocks:** Module 3 exercise specifics.
**Required:** Pick which small self-contained function in PyValidator students
will delete and have Claude restore. Criteria:
- Small (15–40 lines).
- Has a clear test that can be made to fail when the function is missing.
- Has unambiguous correct behavior — not a "design choice" function.

Predicate arity checking is one candidate. Plan-action-name parsing is another.

### 5. Live vs. async cadence
**Blocks:** Schedule communication to participants.
**Required:** Confirm or revise the "two ~2-hour sessions per week for 3 weeks"
cadence. Coordinate with the lab calendar.

### 6. AI honesty policy
**Affects:** Module 5 content.
**Required:** What does the lab require participants to disclose about
AI-assisted code in publications? Module 5 should reflect actual policy.
If no formal policy exists, that's a finding worth surfacing — and possibly
proposing one as a course outcome.

## Low priority (nice-to-haves)

### 7. Asciinema-player MkDocs integration
If using asciinema recordings, add the plugin to `mkdocs.yml`. Not required
for the course to function — mp4 in `<video>` tags works too.

### 8. License for the workshop repo
Set when publishing. CC BY-SA 4.0 is conventional for educational content;
MIT for any code.

### 9. Domain-specific Module 0 framing for RL students
**Status: addressed.** Module 0 now has a "For RL, DRL, MARL, and heuristic-search
students" callout box inviting adaptation, plus a verbal reinforcement note in the
Module 0 teacher notes. Review the wording if you want it stronger/softer.

### 10. Marp slide generation
If a live kickoff lecture is desired, set up Marp to generate slides from
the same markdown. Don't dual-source the content.

## Inline markers placed during production

Every `<!-- BLOCKED: -->` and `<!-- OMER REVIEW: -->` comment in the source is
mirrored here so none get lost between batches.

### Batch 1 (Modules 0–1)

- **`docs/module-00-framing.md`** — `BLOCKED`: the two demo screen recordings
  (A: structured task succeeds; B: vague task flails) are unproduced. Maps to
  item 3 above. Page currently instructs running it as a live demo until clips exist.
- **`docs/module-01-setup.md`** — `OMER REVIEW`: the multi-account git section.
  Your real `~/.gitconfig` has a *single* identity (omereliy, personal gmail, gh
  credential helper) — no `includeIf`, no per-directory configs, no zsh hook. The
  page documents the recommended `includeIf` mechanism generically (not as a
  transcription of your setup) and uses placeholders (`~/lab/`, `lab@example.com`).
  Confirm your actual multi-account mechanism (if any) and supply the real lab
  email + directory path. Note: the coherent multi-account *authentication* answer
  is a per-directory SSH key via `sshCommand` (already stubbed in
  `gitconfig-lab.example`); the `gh` credential helper is machine-wide and does
  *not* switch by directory, so it can't carry a true two-account HTTPS setup on
  its own. New item, not previously in this file.
- **`exercises/m01-pyvalidator-setup/README.md`** — `OMER REVIEW`: PyPI metadata
  for `pddl-pyvalidator` declares no source/home URL, so the public clone URL
  (`<PYVALIDATOR_REPO_URL>`) and repo directory name are placeholders. Fill in the
  real public repo. A pip-install fallback is documented so the exercise still
  works meanwhile. New item, not previously in this file.

### Batch 2 (Modules 3–4)

- **`docs/module-03-workflows.md`** — two `OMER REVIEW`s: (a) SLURM section can't
  verify BGU cluster specifics (partition/account/QOS); (b) Ollama section left
  deliberately short with no asserted VRAM/hostname. Fill in real cluster + Ollama
  details, or point at the cluster's own docs.
- **`exercises/m03-tdd-loop/README.md`** — `OMER REVIEW`: which PyValidator
  function students delete is pending your pick (maps to item 4 above). The
  predicate-arity check is the working candidate; confirm it has a clean red test
  and fill in the exact path, or name a replacement.
- **`exercises/m03-tdd-loop/example.sbatch`** — `OMER REVIEW`: `<PARTITION>` /
  `<ACCOUNT>` / module-load lines are placeholders. Replace with real BGU values.
- **`docs/module-04-slash-commands.md`** — `OMER REVIEW`: maps to item 2. The spec
  named pddl-copilot as an `induce/instantiate/orchestrate` triad + six-compartment
  vocabulary; the repo today is a 4-plugin marketplace with no such skills. Page
  teaches decomposition from the real `pddl-authoring`/`pddl-fixing` split. Confirm
  whether the triad is history to mention or to drop, and whether to link the repo.

### Batch 3 (Modules 5–6)

- **`docs/module-05-failure-modes.md`** — `BLOCKED` (item 1): the primary bug-hunt
  exercise needs your real bug diff. Page + exercise ship a fallback (review a
  public PR with the checklist) until it lands. Also `OMER REVIEW` (item 6): the
  AI-disclosure policy admonition is a placeholder — state the real lab/BGU policy
  or confirm none exists. Do not invent one.
- **`exercises/m05-bug-hunt/README.md`** — `BLOCKED` (item 1): add `bug-diff.patch`
  + `context.md` (sensitive content stripped). `review-checklist.md` is complete
  and unblocked.
- **`docs/module-06-case-studies.md`** — two `OMER REVIEW`s, both mapping to item 2
  (repo privacy). Case B (pddl-copilot) and Case C (pddl-copilot-experiments) have
  conditional public/fork/private blocks. NOTE: I read both repos to ground the
  lessons but deliberately did NOT transcribe unpublished internals (sweep names,
  checkpoint dates, results) into this public page — Case C carries in-flight
  research. Decide public / stripped-fork / private per repo, then fill in
  concretely. Same induce/instantiate/orchestrate-vs-marketplace note as Batch 2.

## How to resolve

Strike items as you complete them. When all "high priority" items are resolved,
the agent producing the remaining modules can fill in the corresponding
exercises and decisions. When all items are resolved, the course is production-
ready.
