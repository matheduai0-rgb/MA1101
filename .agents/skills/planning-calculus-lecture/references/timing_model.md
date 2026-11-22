# Timing model

How `scripts/estimate_timing.py` prices a deck, and how to plan a 100-minute MA1101 meeting.

## Where the numbers come from

- Response-mode costs come from `socratic-calculus-slides/references/question-craft.md`: a poll about
  1 minute, a pair discussion 2–3, paper work 3–5.
- Peer-instruction practice (CWSEI clicker guide): 30 s–1 min individual thinking, 1–4 min
  discussion, close the vote when about three quarters have answered; 4–6 such questions per 50 min.
- Calibration: on the existing decks the model gives deck 35 (6.2) ≈ 64 min and deck 33 (Kerja)
  ≈ 83 min. The research report estimated 55–65 and 75–90 from the same slides. Neither was timed in
  class. Replace the constants with retro.md actuals as they come in.

## Per-slide constants (minutes)

| item | min | why |
|---|---|---|
| any slide | 1.0 | talk, read, transition |
| title slide | 1.5 | big question posed and left open |
| question with no `mode` chip | 0.75 | someone answers quickly |
| `Angkat jari: …`, `Tunjuk di papan` | 1.0 | a vote |
| `Pikir N dtk/mnt` | N + 0.5 | think time + short debrief |
| `Diskusi berpasangan · N mnt`, `Kerjakan di kertas · N mnt`, `Tulis … · N` | N + 1 | work + debrief |
| each `answer` block | 0.5 | reveal and discuss |
| each `hint` block | 0.5 | reveal, wait |
| applet on the slide | 2.0 | dragging, pausing at key states |
| `BeamerBlock` Definisi/Teorema/Rumus/Aturan/Sifat | 1.5 | read and connect to what they found |
| each `PartitionStep` line | 1.0 | worked live |
| `PolyaStepper` full / partial / independent | 2 / 2 / 4 | modelling or solving time beyond the blocks; once per run of slides at that level |

## The 100-minute skeleton (two subchapters)

| min | segment | stage |
|---|---|---|
| 0–5 | big question + 1–2 anonymised answers from last exit ticket | 1 |
| 5–12 | hook problem A: attempt with old tools, get stuck | 2 |
| 12–20 | predict (A/B/C) → applet | 3 |
| 20–30 | discover together; students state the result | 4 |
| 30–38 | name it + fictional student's error | 5–6 |
| 38–47 | guided example A (Pólya, full) | 7 |
| 47–50 | micro-check vote / **cut-able buffer** | 0 |
| 50–62 | hook B + predict/applet | 2–3 |
| 62–74 | discover, name, pitfall B | 4–6 |
| 74–82 | guided example B | 7 |
| 82–92 | partial or independent example in pairs, hint ladder (**cut-able**) | 8–9 |
| 92–100 | exit ticket + bridge question | 10 |

About 55–65% of this is student work, near the level at which active learning narrows achievement
gaps (Theobald et al. 2020: at least two thirds of class time). The "10-minute attention span" is
not well supported; the reason to switch every 10–12 minutes is to get responses and feedback, not
a clock.

## Cut-points

Mark at least two segments `cut = true`. Good candidates: the micro-check buffer, the half-finished
example (move it to homework/PKH), the second applet exploration, hint rung 3 (do it on the board).
Never cut the hook, the worked example, or the exit ticket: the exit ticket is what tells the
lecturer whether the goal was met, and it seeds the next opening.

## When a deck is over budget

Run `estimate_timing.py <slides.md> --slot 100`. Look at the largest rows first. Typical fixes, in
order: shorten a `Kerjakan di kertas` from 2 to 1 min; turn a pair discussion into a vote; move the
half-finished example to homework; merge two discovery slides; drop the second latihan. Report the
change in minutes.
