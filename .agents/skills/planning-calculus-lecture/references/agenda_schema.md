# agenda.toml schema

One file per meeting, saved in the deck folder: `2026/slides/NN_slug/agenda.toml`. If no deck folder
exists yet, create the folder first (next free number, slug from the first subchapter). The format
is TOML because `tomllib` is in Python's standard library; PyYAML is not installed here.

A complete, validated example is `assets/example_agenda.toml` (meeting 27, 6.3 + 6.4). Copy it and
edit; do not write one from memory.

## Top level

| key | type | required | notes |
|---|---|---|---|
| `meeting` | int | yes | pertemuan number from the syllabus (1–30) |
| `date` | string | no | ISO date, e.g. `"2026-11-23"` |
| `slot_minutes` | number | yes | 100 for MA1101 (4 SKS, two meetings a week) |
| `buffer_minutes` | number | no | default 5; the validator keeps Σ segments ≤ slot − buffer |
| `template` | string | yes | `two-subchapter`, `one-subchapter`, or `review` |
| `deck` | string | no | deck folder(s); add once slides exist |
| `previous_exit` | string | no | last meeting's exit-ticket prompt, so the opening can use its answers |

## `[[subchapter]]` (one per syllabus subtopic)

| key | notes |
|---|---|
| `code`, `title` | from `scripts/meeting_info.py` (e.g. `"6.4"`, `"Fungsi Eksponen dan Logaritma Umum"`) |
| `purcell` | textbook section the lecturer uses. The lecturer confirms it; do not guess other books' numbers |
| `goal` | one sentence with an observable verb (menghitung, menentukan, menjelaskan, ...). Avoid "memahami" |
| `big_question` | ends with "?"; answerable at the end, not at the start |
| `prior` | list of what the hook stands on |
| `misconceptions` | 1–2 short phrases; each must appear in some segment's `targets` |

## `[[segment]]` (in teaching order)

| key | notes |
|---|---|
| `name` | plain Indonesian, what happens |
| `stage` | Socratic arc stage 1–10 (see socratic-calculus-slides step 2); 0 = buffer/admin |
| `minutes` | planned minutes; keep each ≤ 15 |
| `mode` | the main response mode, same wording as the `mode` chips ("Pikir 30 dtk", "Diskusi berpasangan · 1 mnt", ...) |
| `student_minutes` | optional; minutes students are working. Default: estimated from `mode` |
| `subchapter` | which subchapter code it serves |
| `targets` | misconception phrases this segment confronts (copy them exactly) |
| `cut` | `true` if it can be dropped when late. At least two; never stage 1, 7 or 10 |
| `slides` | optional, filled after the deck exists: `"9-10"`. Lets `estimate_timing.py --agenda` compare |

## `[exit_ticket]`

| key | notes |
|---|---|
| `goal` | subchapter code the ticket checks |
| `prompt` | one task, answerable in ≤ 3 min on a small paper |
| `bridge` | the open question that opens the next meeting |
| `materials` | list: paper, markers, poll method |

## Templates (100 minutes)

- **two-subchapter** (18 of 30 MA1101 meetings): full arc A ≈ 55 min (stages 1–7), a 3-min cut-able
  check at about minute 47–50, compressed arc B ≈ 40 min (problem + predict merged, one discovery,
  name, guided example, independent problem in pairs that doubles as practice), exit ticket 5 min.
- **one-subchapter**: one full arc with two predict/discover pairs and both partial and independent
  examples (≈ 65 min), then 25–30 min of pair practice or a short KBF-style quiz, then the exit ticket.
- **review**: three stations (e.g. one per Bab), each opened by a diagnostic vote; misconceptions come
  from earlier retro.md files.
