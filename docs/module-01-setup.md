# Module 1 — Setup & Mental Model

**Time:** 60 minutes (15 min setup walkthrough, 30 min exercise, 15 min troubleshooting).
**Prerequisites:** A laptop with a terminal (macOS or Linux). A Claude subscription or an Anthropic API key.

---

## What this module gives you

Two things. First, a working Claude Code install with persistent defaults, so you never re-pick a model or fight your shell again. Second, a mental model of the single loop Claude Code runs — read, plan, act, verify — so that when it misbehaves later, you know *which phase* broke.

Everything after this module assumes `claude` runs and you've configured it once. A shaky setup is inherited by every later exercise. Spend the 15 minutes now.

## Install

Two supported paths. Pick one.

**Native installer (recommended).** Installs a self-contained binary; no Node required.

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

**npm.** If you already manage Node and prefer it:

```bash
npm install -g @anthropic-ai/claude-code
```

The npm package needs **Node.js 18 or later**. Check with `node --version`. If you manage Node with `nvm`, read the PATH gotcha in "What goes wrong" before you start.

Confirm the install in a new shell:

```bash
claude --version
```

If you get `claude: command not found`, the install location isn't on your `PATH` — again, see "What goes wrong." Don't proceed until `claude --version` prints a version.

## First run and authentication

Run `claude` from any directory. On first launch it opens a browser to authenticate. Two account types:

- **Claude subscription** (Pro / Max / Team). Usage is covered by the plan. This is the right default for most lab members.
- **Anthropic API key** (Console, pre-paid credits). Use this when you're billing to a specific grant or project and want per-token cost tracking. The Console creates a "Claude Code" workspace so the spend is visible.

If the browser doesn't open, the TUI prints a URL to paste. To switch accounts later, run `/login` inside a session.

You're authenticated once `claude` drops you at a prompt without nagging. Type `/status` to confirm: it shows the version, the active model, and the logged-in account.

## Persistent defaults: model and effort

You do **not** want to choose a model every session. Set it once.

### Model

The persistent mechanism is the `model` field in your user settings, `~/.claude/settings.json`:

```json
{
  "model": "opus"
}
```

Useful aliases: `opus`, `sonnet`, `haiku`, `opusplan` (Opus while planning, Sonnet to execute), and `opus[1m]` / `sonnet[1m]` for the 1M-token context variants. The in-session `/model` command shows the active model and, on recent versions, saves your pick back to user settings when you confirm it.

There's also an environment variable, `ANTHROPIC_MODEL`, which takes precedence over the settings file for whatever session it's exported in. A shell profile is a legitimate place to set it — for example, the line currently in this course author's `~/.zshrc`:

```bash
export ANTHROPIC_MODEL=opus[1m]
```

Either approach is fine. Pick one, so you don't end up with `settings.json` saying one thing and your shell saying another (the environment variable wins, which surprises people). For a single machine, the settings file is the cleaner choice; the env var is handy when you want different defaults in different shells.

### Effort

Effort level controls how much reasoning the model spends before answering. It is **not** a slider you should pin to maximum. A file rename doesn't need deep reasoning; an algorithm reimplementation does. Module 5 treats this as a deliberate cost/quality decision — here, just set a sane default.

Persistent default in `~/.claude/settings.json`:

```json
{
  "model": "opus",
  "effortLevel": "high"
}
```

Adjust per session with `/effort`, or per shell with the `CLAUDE_CODE_EFFORT_LEVEL` environment variable. The levels available depend on the model — run `/effort` and let the picker show you what your model supports rather than guessing. Note that for current models the old `MAX_THINKING_TOKENS` knob no longer governs this; effort is the setting that matters.

A ready-to-edit `settings.json` and shell snippet are in `exercises/m01-pyvalidator-setup/shell-config/`.

## Multiple GitHub identities

Many of you commit under a lab identity in lab repos and a personal identity elsewhere. The failure you want to avoid is pushing a commit authored by the wrong person — annoying to fix and embarrassing in a shared history.

There are two separable problems here, and conflating them is the usual source of pain:

1. **Commit identity** — the `name`/`email` stamped into each commit. This is pure git config.
2. **Authentication** — the credential that lets you push to GitHub. This is `gh auth`, an SSH key, or a credential helper, and it's independent of identity.

For commit identity, the robust mechanism is git's `includeIf`, which loads a different config file depending on which directory the repo lives in. It is a git feature, not a shell feature, so it works in any shell and needs no hook.

In `~/.gitconfig`:

```gitconfig
[user]
    name = omereliy
    email = personal@example.com

# Repos under ~/lab/ commit with the lab identity instead.
[includeIf "gitdir:~/lab/"]
    path = ~/.gitconfig-lab
```

In `~/.gitconfig-lab`:

```gitconfig
[user]
    name = omere-auditale
    email = lab@example.com
```

Verify it works without writing a single commit:

```bash
cd ~/lab/some-repo && git config user.name        # -> omere-auditale
cd ~/personal/some-repo && git config user.name    # -> omereliy
```

The trailing slash in `gitdir:~/lab/` matters — it matches any repo *under* that directory.

Authentication is the other half, and — unlike identity — it does not switch by directory on its own. The GitHub CLI credential helper (`gh auth git-credential`) authenticates as whichever account `gh` is currently logged into, machine-wide; `gh auth status` shows which. For authentication that genuinely follows the directory, give each account its own SSH key and select it with a per-directory `sshCommand` in the same `includeIf` file (stubbed in `gitconfig-lab.example`). Get identity right first regardless: pushing to the wrong remote fails loudly, but committing as the wrong person fails silently — and the silent failure is the one this section exists to prevent.

<!-- OMER REVIEW: This multi-account section documents the recommended includeIf approach generically; it is NOT a transcription of your machine's actual git setup, which differs. Needs your confirmation plus the real lab email and directory path (placeholders: ~/lab/, lab@example.com). Full rationale and the specifics live in PENDING.md, which is not part of the deployed site. -->

## Your first session

Start Claude in a repo:

```bash
cd ~/personal/some-repo
claude
```

Three commands worth knowing on day one:

- `/help` — lists the commands available to you. Type `/` to filter as you go.
- `/context` — shows a colored grid of what's currently filling the context window (your files, tool results, memory). You'll lean on this in later modules when sessions get long.
- `/status` — version, model, account, connectivity. The first thing to check when something feels off.

The TUI is a prompt at the bottom, Claude's output above it, and one-line summaries of each tool call as Claude works. The spinner shows the active model and effort level. That's the whole interface; there are no hidden panes to learn.

## The loop: read, plan, act, verify

Claude Code is not a chat window that happens to see your files. It runs an agentic loop, and naming the four phases is the most useful mental model you'll get from this module — because each phase fails in its own recognizable way.

1. **Read.** Claude examines files, runs `grep`/`find`, opens what it thinks is relevant.
   *Failure mode:* it reads the wrong files, or too few, and proceeds confidently on a partial picture. You see this when its plan references something that isn't actually in your code.
2. **Plan.** Claude proposes a sequence of edits/commands before doing them.
   *Failure mode:* the plan silently skips a step ("update the tests" omitted) or is vague where it should be specific. A vague plan produces code you can't audit. Reject it and ask for a sharper one.
3. **Act.** Claude edits files and runs commands.
   *Failure mode:* it edits more than you asked (reformatting unrelated code), or runs something expensive or destructive. This is where reading each tool call as it happens pays off.
4. **Verify.** Claude runs tests, re-reads its diff, checks its own work.
   *Failure mode:* it declares success without actually running anything, or it writes a test that passes but doesn't test the thing. "All tests pass" is a claim, not proof — Module 5 is largely about not taking it on faith.

You drive this loop by inserting yourself at the seams: approve or reject the plan, watch the actions, and check the verification rather than trusting the summary. The exercise below is one full turn through the loop, so the phases stop being abstract.

## MCP, in one paragraph

Claude Code can connect to **MCP servers** — external tools that expose extra capabilities (a database, a planner, a docs index) through a standard protocol. They're useful when you want Claude to reach something beyond your filesystem and shell. It's out of scope here; we mention it only so you recognize the term. Treat it as an advanced topic for a later session, not something to configure today.

## Exercise: install, configure, and run the loop once

**Goal:** confirm your setup works by running Claude Code through one complete read → plan → act → verify loop on a real, public repo.

Full instructions and the shell-config templates are in `exercises/m01-pyvalidator-setup/`. In brief:

1. Install Claude Code, authenticate, and set your persistent model/effort defaults (templates provided).
2. Get **PyValidator** — a pure-Python PDDL plan validator (clone the repo, or `pip install pddl-pyvalidator`; the exercise README covers both).
3. From the repo root, run `claude` and ask: *"What does this repo do? Where's the entry point?"* Read the answer — this is the **Read** phase made visible.
4. Ask Claude to add **one** test for an edge case: an empty plan, a malformed action name, or a predicate with the wrong arity. Make it propose a plan first; only then let it write the test.
5. Run `pytest`.

**Success criterion:** the test exists, runs under `pytest`, and either passes or fails *meaningfully* (the failure points at real behavior, not at a broken import). You should be able to say, in one sentence, what the test checks and which loop phase you trusted least.

Time-box: ~30 minutes. If you spend more than 10 minutes fighting the install, flag the instructor — that's a troubleshooting problem, not an exercise.

## What goes wrong

Setup failures are boring and universal. The common ones:

- **`claude: command not found`.** The install dir isn't on `PATH`. The native installer puts the binary under `~/.local/bin` (add `export PATH="$HOME/.local/bin:$PATH"` to your shell profile). With `nvm`, global npm binaries live under the *active* Node version's prefix — switch Node versions and `claude` disappears from `PATH`. The native installer sidesteps this entirely.
- **Two installs fighting.** You `brew install`ed it once and `npm install -g`'d it another time, and `which -a claude` shows two. Pick one, remove the other, open a fresh shell.
- **Stale auth.** Sessions that worked yesterday throw auth errors today. Run `/login` to re-authenticate. Check `/status` first to see what it thinks is wrong.
- **Old Node.** `npm install -g @anthropic-ai/claude-code` on Node < 18 fails or installs something that won't run. Run `node --version` before you blame Claude.
- **Corporate / campus proxy.** If auth or model calls hang, you're likely behind a proxy that needs `HTTPS_PROXY` set. This one bites people on the BGU network specifically.
- **Python too old for the exercise.** PyValidator needs **Python ≥ 3.10**. If `python --version` shows 3.9 (a common pyenv default), `pip install pddl-pyvalidator` will refuse. Switch interpreters before you start, not during.

None of these are Claude Code bugs. All of them cost you ten minutes if you hit them mid-exercise instead of now.

## Recap

- Install via the native installer (or npm with Node ≥ 18). Confirm with `claude --version`.
- Set model and effort **once** in `~/.claude/settings.json` (or `ANTHROPIC_MODEL` in your shell). Don't max effort by reflex.
- Separate commit *identity* (`includeIf` in git config) from *authentication* (`gh` / SSH). A wrong-author commit is the failure to prevent.
- Claude Code runs one loop — read, plan, act, verify — and each phase fails in a nameable way. Insert yourself at the seams.

Next: Module 2 — making the repo Claude-friendly, the single biggest lever on output quality.
