# Module 0 — Teacher Notes

**Module:** Why This Course Exists
**Time:** 15–20 minutes
**Difficulty for instructor:** Low, with one trap — the urge to defend the tool. This module's credibility depends on you *not* doing that.

---

## Timing breakdown

- **0:00 – 0:05** — The one claim: a tool with a definite shape. Acknowledge skepticism in the room directly.
- **0:05 – 0:12** — What it is / is not / where it shines / where it struggles. Move briskly; this is orientation, not depth.
- **0:12 – 0:18** — The two recordings (or live demo). Students write the difference before you reveal it.
- **0:18 – 0:20** — "Claude wrote it, you own it." Plant it; don't develop it (that's Module 5).

This is the shortest module. Don't pad it to fill a slot. If you finish in 15 minutes, start Module 1 early — setup always runs long.

## The one rule: do not defend the tool

When Recording B (the vague task) goes badly, **do not rescue it.** Don't explain that "with a better prompt it would have worked." That's true and it's the lesson — but the students have to arrive at it themselves by comparing the two *tasks*. If you editorialize, you've answered the exercise for them and taught them that the instructor is a salesperson.

Show the warts unedited. A researcher who watches you narrate a failure honestly will trust everything else you say. A researcher who watches you spin a failure will discount the whole course.

## The Cursor problem

If anyone in the room has used Cursor heavily, they are the most likely to be confused, because the tools overlap superficially and differ in workflow. Name the difference out loud:

- Cursor: editor-coupled, tight loop, you're looking at the code as it changes.
- Claude Code: terminal, longer multi-file tasks, you review diffs and test output rather than watch a buffer.

Ask early: "Who here uses Cursor or Copilot regularly?" Their mental model needs the explicit correction; everyone else just needs the map.

## Do NOT demo the flashy features here

This is spec-mandated and worth repeating: **no impressive demos in Module 0.** No slick refactor, no "watch it fix this bug." That's Module 1 and Module 2's job, and doing it here undercuts the honest framing. Module 0 sells nothing. It draws a map.

## On the recordings (currently blocked)

The two recordings are Omer's to produce (PENDING.md item 3). Until they exist:

- **Run it live.** A live demo is actually better than a recording for this module — the failure feels more real. If you do, prepare both tasks in advance:
  - *Structured (A):* a task with a checkable goal in PyValidator, e.g. "add a test that an empty plan is rejected." It should go well.
  - *Vague (B):* "make the validator better" or "clean up this file." Let it wander. Do not help it.
- **Don't fake it.** If the live demo of B happens to go *well*, don't pretend it failed. Say "huh, that went better than usual — why do you think?" and let the room reason about it. The honesty is the point.

## Anticipated student questions

**"So is it better than Cursor / Copilot?"**
Wrong axis. Different tools for different jobs. Copilot for inline autocomplete while you type; Cursor for tight in-editor edits; Claude Code for longer multi-file, run-it-yourself work. Most people use more than one. If a student points out that Copilot now has an agent mode too, concede it immediately — the distinction is the *default* interaction model and origin, not a claim that an agentic Copilot doesn't exist. Don't die on that hill; it costs credibility with the people most worth convincing.

**"Can it design my algorithm for me?"**
No — and you don't want it to. It reimplements clear specs well and invents novel methods poorly. The novel part is your research; that's the part with your name on it.

**"If I have to read everything it writes, what did I save?"**
The typing, the boilerplate, the edge cases you'd skip, the unfamiliar-repo reading. Reading correct code is much faster than writing it. The saving is real; it's just not "I stop thinking."

**"Is it safe to use on unpublished research code?"**
A real question with a lab-policy answer, not a technical one. Defer the substance to Module 5 (and PENDING.md item 6 — the lab's AI-disclosure policy). For now: it's a tool that sends code to an API; treat that like any cloud service your data touches.

## RL/MARL students

Spec-mandated: explicitly invite the adaptation here so they don't spend six modules feeling like tourists. Say it plainly — "the PDDL flavor is so I can answer your questions live; the techniques are yours regardless; bring an RL repo to Module 6." The callout box in the page says this; reinforce it verbally. If you have several RL students, consider pairing them for Module 6 BYOR up front.

## Failure modes for the instructor

- **You oversell and lose the room.** The fastest way to lose a skeptical researcher is one hype sentence. Cut every "transforms your workflow." The page has none; keep it that way live.
- **The map turns into a lecture.** This module is 15 minutes. If you're 25 minutes in and still on "what it is," you've over-explained. Stop and move to Module 1.
- **A student wants the deep comparison now.** Cursor-vs-Claude-Code-vs-Copilot can eat the whole slot. Give the one-paragraph map and promise the rest emerges through use.

## Bridge to Module 1

End with: "That's the map. Now we make it real — install it, configure it so you never fight it again, and run the loop once with your own hands."
