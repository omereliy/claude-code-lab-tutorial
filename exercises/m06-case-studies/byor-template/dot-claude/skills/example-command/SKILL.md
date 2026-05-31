---
description: [When should Claude/you invoke this? Write it as a trigger, not a title. e.g. "Summarize the latest experiment run's log into a one-screen report"]
argument-hint: [<what to pass>, e.g. <path-to-log> or <run-id>]
---

<!--
BYOR slash-command template (Module 4). This is a single SKILL.md — ONE file.
Do NOT add a scripts/ folder or extra files; that turns a slash command into a
skill, which is not the BYOR task. Copy this directory into your repo at
.claude/skills/<your-command-name>/SKILL.md and rename it.

The value of a slash command is the OUTPUT SHAPE it specifies, not that it runs
a tool. Be specific about what Claude should produce.
-->

[Your prompt body. Use $ARGUMENTS for what the user passes. Example structure:]

Take `$ARGUMENTS` and [do the thing].

Then produce a summary, not a dump:
- [grouping: by what?]
- [drop duplicates / noise]
- [order by: what matters most first]
- [end with a one-line verdict / headline]

If [the nothing-to-report case], say so in one line — do not invent findings.
