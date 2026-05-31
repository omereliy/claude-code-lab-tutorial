# Shell & Claude Code config templates

Copy what you need; don't paste blindly. Every value here is an example.

## Files

| File | Goes to | What it does |
|------|---------|--------------|
| `claude-settings.example.json` | `~/.claude/settings.json` | Persistent model + effort defaults. **Recommended.** |
| `zshrc-snippet.sh` | append to `~/.zshrc` | PATH fix + optional env-var model default. |
| `gitconfig.example` | `~/.gitconfig` | Default identity + `includeIf` for a second identity. |
| `gitconfig-lab.example` | `~/.gitconfig-lab` | Lab identity, loaded only for repos under `~/lab/`. |
| `gitconfig-personal.example` | `~/.gitconfig-personal` | Personal identity (optional; the default in `~/.gitconfig` may be enough). |

## Model & effort

Prefer `claude-settings.example.json` (the settings file) for a persistent
default. Use the `ANTHROPIC_MODEL` line in `zshrc-snippet.sh` only if you want a
shell-specific override — and remember the env var **wins** over the settings
file, which is a common source of "why is it using the wrong model?"

Effort defaults to a sensible level per model. Set `effortLevel` only if you
have a reason. Don't reflexively crank it up — Module 5 explains why effort is a
cost/quality decision, not a "more is better" dial. (The persistent `effortLevel`
accepts `low`/`medium`/`high`/`xhigh`; `max` exists but is session-only, set via
`/effort`, not this file.)

## Git identity (only if you commit under more than one account)

`includeIf` is a git feature, not a shell feature — no zsh hook needed. The
config in `~/.gitconfig` loads `~/.gitconfig-lab` automatically for any repo
under `~/lab/`. Adjust the path and identities to your own accounts.

Verify before trusting it:

```bash
cd ~/lab/any-repo && git config user.name        # should be your lab name
cd ~/personal/any-repo && git config user.name    # should be your personal name
```

Identity is separate from authentication. `includeIf` fixes *who the commit is
attributed to*. Pushing still uses `gh auth` (HTTPS) or an SSH key — check
`gh auth status`.
