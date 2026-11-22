---
name: planning-calculus-lecture
description: >-
  Plans one 100-minute MA1101 calculus meeting before any slides are written, and reviews it after
  class. Before class it reads the meeting from the syllabus spreadsheet, writes agenda.toml (goals,
  big questions, misconceptions, timed segments on the Socratic arc, cut-points, exit ticket, bridge
  question) and a one-page lecturer run-sheet, and checks the minutes against the slot. It also
  estimates how long an existing deck takes. After class it writes retro.md (planned vs actual minutes,
  questions that fell flat, exit-ticket counts) and proposes changes. Use when the user asks for a
  lesson plan, "rencana kuliah", "agenda pertemuan", "SAP/RPS pertemuan", a run-sheet, timing or a
  minute budget, whether a deck fits the slot, says "kuliah saya molor", or wants to reflect on how a
  class went ("evaluasi kuliah hari ini"). Not for writing slides: hand the agenda to
  socratic-calculus-slides.
---

# Planning a Calculus Lecture (MA1101)

This skill decides **what one meeting is for and how its 100 minutes are spent**. It writes files
that the next skill reads: `socratic-calculus-slides` builds the deck from `agenda.toml`, and the
run-sheet is what the lecturer holds in class. After class, `retro.md` closes the loop.

MA1101 facts this skill relies on:

- 30 meetings, Monday and Thursday, 100 minutes each (4 SKS); the lecturer confirmed the length.
- 18 of 30 meetings carry **two subchapters**. There are no tutorial slots, so in-class practice is
  the only scheduled practice.
- Main text Purcell–Varberg–Rigdon (9th ed.); subchapter codes follow its sections.
- Syllabus: `2026/Silabus_MA1101_Matematika_I_2026_2027.xlsx`, sheet "Jadwal Perkuliahan".

## Why plan before slides

Decks written straight from a topic run long: the existing Socratic decks estimate at 64–83 minutes
for **one** subchapter, so two full arcs cannot fit. Deciding the goal, the misconception and the
minutes first lets the deck be cut to fit before it is built, gives the lecturer cut-points for days
that run late, and makes the exit ticket check the goal that was actually taught.

## Pre-class mode

1. **Read the meeting.**
   `python3 ${CLAUDE_SKILL_DIR}/scripts/meeting_info.py <N>` (or `--all` for the list). It prints
   date, subchapters and `n_subtopics`. Also look at the previous deck's last slide: its bridge
   question is this meeting's opening, and its exit ticket answers (from retro.md, if any) open the
   class.

2. **Choose the template** (`references/agenda_schema.md`, "Templates"):
   - two subchapters → full arc A (~55 min) + compressed arc B (~40 min);
   - one subchapter → full arc + 25–30 min of pair practice;
   - review meeting → three stations.

3. **Write `agenda.toml`** in the deck folder by copying `assets/example_agenda.toml` and editing it.
   Per subchapter: one goal with an observable verb, the big question, prior knowledge, one or two
   misconceptions (from `socratic-calculus-slides/references/question-craft.md`'s bank when it has
   one), and the Purcell section (ask the lecturer if unsure; never invent section numbers). Then
   the segments, in order, with stage, minutes, response mode, `targets` and at least two `cut`.
   If the topic is clear, do not interview the user; choose and state the choices.

4. **Validate and fix until it passes.**
   `python3 ${CLAUDE_SKILL_DIR}/scripts/validate_agenda.py <deck>/agenda.toml`
   It checks: minutes ≤ slot − buffer, every misconception targeted, ≥ 2 cut-points not on the hook,
   worked example or exit, last segment is the exit ticket, exit ticket tied to a goal, enough
   student work (aim 55–65%), and no student data.

5. **Write `runsheet.md`** from `assets/runsheet_template.md`: clock times from the start time,
   slide ranges once known, what the lecturer does, what students do, the cut-points in bold, the
   board plan, and three clock checks (minutes 30, 50, 82).

6. **Hand off.** Say that `socratic-calculus-slides` builds the deck from this agenda. After the
   deck exists, fill each segment's `slides = "a-b"` and run
   `python3 ${CLAUDE_SKILL_DIR}/scripts/estimate_timing.py <deck>/slides.md --slot 100 --agenda <deck>/agenda.toml`.
   If it is over, apply the fixes in `references/timing_model.md` ("When a deck is over budget").

## Timing an existing deck

When the user asks whether a deck fits, or says a lecture ran over, run `estimate_timing.py` on it
and answer with the total, the three most expensive slides, and concrete cuts with the minutes they
save. The constants and their sources are in `references/timing_model.md`. They are estimates;
say so, and prefer the lecturer's measured minutes when a retro exists.

## Post-class mode

When the lecturer reports how a class went, write `retro.md` from `references/retro_template.md`:
planned vs actual minutes per segment, which questions worked or fell flat (and a proposed
replacement), exit-ticket results **as counts and patterns only**, two anonymous answers to open
the next meeting with, and proposed changes to the agenda, the deck, and the misconception bank.
Propose; do not edit `question-craft.md` or the deck unless asked.

**Privacy.** Work only from what the lecturer says. Never open roster, attendance, grade, group,
exam or answer-key files (`2026/K10|K35|K40/`, `2026/Ujian/`, `2025/`, "Daftar Peserta",
"Pembagian Kelompok", "nilai", "kunci") to find numbers, and never write names or NIM. The scripts
refuse such paths and flag 8-digit student numbers.

## Report

Tell the user briefly: the meeting and template, the goals and big questions, the minute plan
(segments with minutes, total vs 100), the cut-points, the exit ticket, the validator result, and
what is left (deck to build, Purcell sections to confirm).

## Files

- `scripts/meeting_info.py`: syllabus xlsx → meeting (stdlib only; openpyxl is not installed).
- `scripts/validate_agenda.py`: agenda checks with verbose fixes.
- `scripts/estimate_timing.py`: slides.md → minutes per slide, total vs slot and agenda. Shares
  slide splitting with `socratic-calculus-slides/scripts/verify_socratic_deck.py`.
- `references/agenda_schema.md`: every agenda field and the three templates. Read before step 3.
- `references/timing_model.md`: constants, sources, the 100-minute skeleton, cut-point rules.
- `references/retro_template.md`: post-class file and privacy rule.
- `assets/example_agenda.toml`: validated agenda for meeting 27 (6.3 + 6.4). Copy, do not retype.
- `assets/runsheet_template.md`: run-sheet layout.
