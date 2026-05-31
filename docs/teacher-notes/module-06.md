# Module 6 — Teacher Notes

**Module:** Case Studies
**Time:** 60–90 minutes in-session + take-home extension
**Difficulty for instructor:** Medium. The content is yours to tell; the risk is over-telling the case studies and under-serving BYOR, which is where the value actually is for half the room.

---

## Timing breakdown

- **0:00 – 0:35** — The three instructor case studies (A, B, C). ~10 min each. Resist going longer.
- **0:35 – 0:45** — BYOR setup. Get RL/MARL students pointed at their own repo *now*.
- **0:45 – 0:90** — In-session start on an extension; the rest is take-home.

If you're tight, **compress A/B/C, protect BYOR.** The case studies can be read on the site; the BYOR kickoff needs you in the room to unblock people.

## Two things are blocked — read before you teach this

1. **Repo privacy (PENDING.md item 2).** Case studies B and C depend on whether
   `pddl-copilot` and `pddl-copilot-experiments` are public, stripped forks, or
   private. The page has conditional blocks for each outcome. **Decide before
   class** and tell students which path is live, or B/C become confusing.
   - `pddl-copilot-experiments` carries unpublished research (live sweeps,
     contamination-control data). The page deliberately contains only generic,
     transferable conventions — no observed internals. Keep it that way until you
     decide on a stripped fork.
2. **The induce/instantiate/orchestrate mismatch.** The COURSE_SPEC describes
   pddl-copilot as an `induce/instantiate/orchestrate` triad with a
   six-compartment vocabulary. The repo today is a 4-plugin marketplace with no
   such skills. The page teaches decomposition from the *current* structure
   (authoring vs fixing). If the triad is earlier history you want to tell,
   tell it live as history — don't present it as the current architecture.

## Push RL/MARL/DRL students to BYOR — explicitly

Spec-mandated and the single highest-value move in the module. Say it directly:
"If you work in RL, MARL, DRL, or heuristic search, do BYOR. The PDDL extensions
will feel like tourism." Then *help them scope it* in the room — one `CLAUDE.md`,
one TDD loop, one slash command. The ones who leave with a plan for their own
repo are the ones for whom the course paid off.

If you have several such students, consider pairing them so the BYOR work has a
review partner.

## Tell the path, not the destination

The case studies are worth nothing as "here's my nice repo." They're worth a lot
as "here's what I tried first, why it failed, and what I changed." Specifically:

- **PyValidator:** the early `CLAUDE.md` that was wrong, and what made it right.
  The API decision Claude couldn't make.
- **pddl-copilot:** the decomposition that *wasn't* chosen first. Why one skill
  became several.
- **Experiments:** the reproduction that failed two months later, and the folder
  convention that fixed it.

If you only have time for one war story per repo, make it the abandoned attempt.
This audience learns from failures; the spec says so for a reason.

## On Case C — keep it about conventions, not results

The reproducibility lesson is the *folder discipline* (stamped result dirs,
versioned configs, a changelog, anonymized inputs). Those are portable to any
experiment repo, including RL students' own. Do **not** turn this into a tour of
your actual results or unpublished findings — partly because it's blocked on the
privacy decision, partly because the conventions are the transferable part and
the results aren't.

## Anticipated student questions

**"Can I see pddl-copilot / the experiments repo?"**
Depends on the privacy decision (item 2). Give the live answer. If private, the
case study is read-along; the conventions still transfer to their work.

**"My repo is a mess — is it even worth writing a CLAUDE.md?"**
Especially then. A messy, mutating research repo is exactly where the Module 2
lever has the most leverage. Scope it small: conventions, dead files, where new
code goes. Don't wait for the repo to be clean.

**"I don't have a self-contained function to TDD on."**
Find the smallest pure function in the repo — a metric, a transform, a check.
If there's genuinely none, that's a finding about the repo's testability worth
discussing.

**"Which extension should I pick?"**
RL/MARL/DRL → BYOR, no contest. PDDL-adjacent and want a guided path →
PyValidator (it's public and self-contained). Only pick the copilot/experiments
extensions if those repos are accessible.

## What to do if a student finishes early (in session)

- Have them start the BYOR writeup *now*, while the experience is fresh — the
  writeup is the deliverable and the part most likely to be skipped.
- Or have them do a second slash command for their own repo. The second one is
  always faster and proves the skill transferred.

## The BYOR writeups are a lab asset

Spec note worth acting on: collect the BYOR writeups. Across a cohort they become
a library of "what worked in my domain" — RL, MARL, search, planning. Future
cohorts read them to see the techniques in their own field. Tell students their
writeup may be shared (and let them opt out).

## Failure modes for the instructor

- **Case studies eat the clock; BYOR gets five minutes.** The most common and
  most costly failure here. Time-box A/B/C hard. BYOR is the payoff.
- **You present the repos as polished.** Then the lesson inverts — students think
  AI-assisted research is clean, and Module 5's whole point evaporates. Show the
  scars.
- **A privacy decision wasn't made.** If you walk in without deciding, B and C
  collapse into vague gestures. Decide first.
- **RL students quietly disengage.** If they're doing a PDDL extension and
  looking bored, redirect to BYOR mid-session. It's never too late to switch them.

## Closing the course

This is the last module. Close on the through-line, not a feature list: "Make the
repo Claude-friendly first. Drive it with constrained loops — tests, slash
commands. Never accept output you haven't read. Everything else is reps." Then
point them at BYOR as the first rep.
