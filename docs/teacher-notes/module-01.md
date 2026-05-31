# Module 1 — Teacher Notes

**Module:** Setup & Mental Model
**Time:** 60 minutes
**Difficulty for instructor:** Low content, high logistics. The teaching is easy; getting twenty laptops installed is the work. Plan for the install to eat more time than you expect.

---

## Timing breakdown

- **0:00 – 0:05** — Why setup matters. "Every later exercise inherits a broken setup." Set the expectation that today is plumbing.
- **0:05 – 0:20** — Walk the install + auth + persistent defaults live, projector on. Have students follow along, not watch.
- **0:20 – 0:25** — The four-phase loop. Keep it short — they'll *do* it in five minutes, so don't over-explain.
- **0:25 – 0:55** — Exercise. This is where you walk the room.
- **0:55 – 1:00** — Debrief: one sentence each — "what does your test check, and which loop phase did you trust least?"

If the install runs long, **cut the loop lecture, not the exercise.** They learn the loop by running it, not by hearing about it.

## Before the session

- **Confirm `pddl-pyvalidator` installs on a clean machine** the day before. If PyPI or the repo moved, you want to know first, not during the room walk.
- Have the proxy incantation ready for the BGU network (`export HTTPS_PROXY=...`). If auth calls hang for one student, they'll hang for several.
- Decide your stance on installers: recommend the **native installer** as the default. It removes the entire class of `nvm`/PATH problems, which is where most of your room-walk time will otherwise go.
- Pre-write the model/effort `settings.json` on the projector machine so you can show a real one, not describe it.

## What to emphasize live

1. **`claude --version` is the gate.** Nobody touches the exercise until that command prints a version in a *fresh* shell. Say it twice.
2. **Don't max effort by reflex.** Plant this here even though Module 5 develops it. Students will otherwise pin effort to `max` and wonder why everything is slow.
3. **Identity vs. authentication are different problems.** The wrong-author commit is the concrete failure. Show `git config user.name` resolving differently in two directories — it lands better than any slide.

## Live demo cues

- Show `/status` immediately after auth. It's the single best "is my setup sane?" command and students forget it exists.
- Run `/context` once on an empty session so they see what "nearly empty" looks like — it gives them a baseline for Module 2 and 3 when it fills up.
- When you set the model, show **both** mechanisms (`settings.json` and `ANTHROPIC_MODEL`) and then say which one you actually use and why. The env-var-wins-over-settings gotcha is worth 30 seconds — it's a real source of "why is it using the wrong model" confusion.

## The multi-account section is a known soft spot

The spec asked for a worked example built on the author's "existing" multi-account setup. On inspection, the author's machine has a single git identity — so the page documents the `includeIf` mechanism generically and flags it for review (see the `OMER REVIEW` comment in the page and `PENDING.md`).

Practical consequence for you:

- **If even one student has a real lab/personal split, make them the demo.** Have them run `git config user.name` in a lab repo and a personal repo. If the answers are the same and they didn't expect that, you've just found a latent wrong-author-commit bug, live. That's the whole lesson.
- If nobody in the room has two identities, keep this short. Don't manufacture urgency — frame it as "here's the mechanism for when you join a lab repo," and move on.
- Resist teaching SSH-key-per-account in depth. Identity (`includeIf`) is the 90% case; authentication is a rabbit hole.

## Anticipated student questions

**"Native installer or npm — which?"**
Native installer unless you have a specific reason to want the npm package (you already manage Node tightly, or you're scripting installs). The native installer avoids PATH/`nvm` problems, which is most of what breaks.

**"Do I need an API key, or does my Claude subscription work?"**
Subscription works and is the default. Use an API key only when you need per-grant cost tracking.

**"Where does the model setting actually live?"**
`~/.claude/settings.json` for the persistent default; `ANTHROPIC_MODEL` in the shell overrides it for that shell. If both are set, the environment variable wins. Pick one.

**"What's the difference between this and the ChatGPT/Claude website?"**
Defer to Module 0 if you haven't run it yet, or give the one-liner: this has your filesystem and shell and runs a loop; the website has neither. Don't get pulled into the full comparison here.

**"Can I use it offline / on an air-gapped cluster node?"**
No. The model calls go out to the API (or your configured Bedrock/Vertex endpoint). Mention this now because someone always tries it on a compute node with no egress and blames the install.

## What to do if a student finishes early

- Have them try the **wrong** path on purpose: ask Claude a vague version of the task ("make the validator better") and watch the plan get mushy. This previews Module 0's "where it struggles" and Module 5's failure modes.
- Or have them set up the `includeIf` config and verify it with `git config user.name` in two directories, even if they only have one identity today.

## Failure modes for the instructor

- **The install swallows the hour.** If 30% of the room is still installing at the 25-minute mark, stop trying to fix each laptop individually. Pair the stuck students with working ones and let the exercise proceed for everyone who's ready. A broken install is fixable after class; lost momentum is not.
- **One weird PATH problem you can't solve fast.** Don't debug it in front of the room. Hand that student the native installer one-liner, have them run it in a fresh terminal, and move on. It resolves 80% of PATH issues without diagnosis.
- **A student wants to configure MCP servers now.** Redirect. One paragraph in the page is deliberate. MCP is a later-session topic and will derail this one.
- **The exercise "succeeds" but the test is hollow.** A student reports green but the test asserts nothing real. Good — that's a Module 5 preview. Note it, don't fix it, and tell them to remember it.

## Bridge to Module 2

End with: "Your tools work and you know the loop. But Claude is still guessing about *your* repo — your conventions, your dead files, where new code goes. Module 2 is the single highest-leverage thing you can do about that: one file, `CLAUDE.md`, that tells Claude what it can't infer."
