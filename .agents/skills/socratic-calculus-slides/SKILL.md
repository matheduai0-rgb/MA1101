---
name: socratic-calculus-slides
description: >-
  Designs and builds engaging, question-driven calculus lecture decks in Slidev + JSXGraph for
  MA1101: every idea is reached through Socratic questions (hook, predict, explore an applet,
  guided discovery, then the definition), and problem solving is scaffolded with Pólya's four
  phases and support that fades from worked example to half-finished example to independent
  problem with a hint ladder. Use this skill whenever the user asks for lecture slides, a slide
  deck, "slide kuliah", "bahan ajar", a worked-example sequence, practice-problem slides, or an
  interactive applet slide for any calculus topic, and whenever they mention Socratic questioning,
  scaffolding, guided discovery, active learning, "pertanyaan pemantik", Pólya, hints, or making
  slides more engaging or less lecture-heavy, even if they only name a topic ("buatkan slide
  aturan rantai") and do not say "Socratic". Also use it to convert an existing expository deck
  into a questioning one.
---

# Socratic Calculus Slides (Slidev + JSXGraph)

This skill decides **what goes on the slides and in what order** so that a live calculus lecture
runs on questions instead of exposition. The companion skill
`.agents/skills/slidev-jsxgraph-calculus-slides/SKILL.md` owns the technical layer (theme, KaTeX
rules, `BeamerBlock`, JSXGraph component conventions, layout budget). Read it too; its rules still
apply. Where the two disagree on verification, use this skill's checker (see step 6).

The decks are for a lecturer presenting to a room of first-year students (Bahasa Indonesia,
"kalian/kita" register). The lecturer asks, the room thinks or talks, then a click reveals. So
every question needs three things the slide alone cannot provide: a way for the room to respond,
time to do it, and a plan for what the lecturer says when the answer is wrong or nobody speaks.
Those live in the presenter notes, and they are as much a deliverable as the slides.

## Why this structure

Three ideas drive everything below. Keep them in mind and the specific rules follow.

1. **A question only works if the student can make progress on it.** "Apa itu turunan?" is a
   quiz on vocabulary they do not have yet. "Kecepatan apa saja yang bisa kalian hitung dengan
   alat yang sudah kalian punya?" lets them start. Ask from what is on the screen or already
   known, toward the thing you want them to say.
2. **Telling comes after needing.** A definition shown first is a fact to memorise. The same
   definition shown after students have computed three secant slopes and watched them settle is
   the name for something they already own. So formal statements appear late, and the slide that
   carries one says so ("Nama untuk yang baru kalian temukan").
3. **Support is a loan, not a gift.** A worked example helps a novice and holds back someone who
   is nearly there. So the deck withdraws support on purpose: the lecturer models all four Pólya
   phases, then students fill gaps in a half-finished solution, then they solve alone with hints
   available only if they stall. Showing three fully worked examples in a row feels thorough and
   teaches less.

## Workflow

### 1. Pin down the lesson before writing slides

From the request (and the syllabus PDF/XLSX in `2026/` if the subtopic number matters), settle:

- **One learning goal**, phrased as something students will be able to do or explain.
- **Prior knowledge** the hook can stand on.
- **The big question**: one sentence, answerable by the end and not at the start. It goes on the
  title slide and returns near the end.
- **One or two misconceptions** worth surfacing (see `references/question-craft.md` for a bank
  by topic).
- **Scope**: a full lecture deck, or a segment (one worked example, one applet, a problem set).
  A segment keeps the per-slide habits but not the whole arc.

If the topic is clear, do not stop to interview the user; choose sensibly and state the choices
in your summary.

### 2. Plan the arc

A full deck follows this arc. The stage names in the second column are what appears on slide titles; they are plain Indonesian on purpose (see step 3b). Slide counts are typical, not required; 10 to 14 slides suits a
50-minute session because each question costs one to four minutes of room time.

| # | Stage | What happens | Blocks |
|---|-------|--------------|--------|
| 1 | **Judul + Pertanyaan Besar** | The question the lecture will answer. Not answered yet. | `question` |
| 2 | **Mulai dari Soal** | A concrete problem students can attempt with old tools and cannot finish. | `question` → `answer` → follow-up `question` |
| 3 | **Tebak → Coba Geser** | Students commit to a guess, then the applet shows what happens. | `predict`, applet, `question` |
| 4 | **Temukan Bersama** | A chain of 3 to 4 small questions, each one step, ending with students stating the result. | alternating `question` / `answer` |
| 5 | **Sekarang Kita Beri Nama** | Definition or theorem, mapped back onto what they just did. | `BeamerBlock`, `question`, `reflect` |
| 6 | **Apakah Ini Benar?** | A plausible wrong idea, attributed to a fictional student, for the room to diagnose. | `pitfall` → `answer` |
| 7 | **Contoh terpandu** | Full support. All four Pólya phases, each opened by a question. Usually two slides. | `PolyaStepper support="full"` |
| 8 | **Contoh setengah jadi** | Partial support. Same plan, blanks for students to fill. | `PolyaStepper support="partial"` |
| 9 | **Latihan mandiri** | No scaffold. Hint ladder of three, final answer only. | `PolyaStepper support="independent"`, `hint` ×3 |
| 10 | **Tulis Sebelum Pulang** | Students summarise in their own words; one open question points to next time. | `reflect`, `question` |

Topics differ. A theorem-heavy topic may need two discovery slides; a technique topic (e.g.
substitution) may shrink stages 3 to 5 and spend more on 7 to 9. Bend the arc, but keep the three
ideas: question first, formal statement late, support fades.

`assets/example_deck.md` is a complete, verified 11-slide deck on this arc (secant to tangent).
Read it before writing your first deck: it shows the markup, the density that fits, and what
useful presenter notes look like. Borrow its structure, not its content.

### 3. Write the questions

Read `references/question-craft.md` when drafting. The short version:

- One question per moment. Each new question arrives on a click, after the previous answer.
- Give the room a response mode in the `mode` chip: "Pikir 30 dtk", "Diskusi berpasangan · 1 mnt",
  "Angkat jari: A / B / C", "Kerjakan di kertas · 2 mnt". Without one, the fastest student answers
  and the rest watch.
- Prefer questions with more than one defensible answer, or that ask for a reason ("mengapa",
  "bagaimana kalian tahu", "apa yang berubah bila"). Avoid yes/no and fill-in-the-word questions.
- Predict questions offer discrete options (A/B/C) so everyone can commit, and at least one
  option is a real misconception.
- Answers and hints are never visible at click 0. The checker enforces this.

### 3b. Use plain Indonesian

Read `references/indonesian-diction.md` before writing any slide text. A lecturer reviewing an
earlier deck liked the structure but found the wording unfamiliar: coined stage names and formal,
noun-heavy sentences made students work to read the slide before they could think about the
mathematics. So: short everyday sentences, "kalian/kita", titles that say what students do, and
calculus terms taken from the course's own syllabus and earlier decks instead of paraphrased. The
only hard words on a slide should be the ones the lecture is teaching. The guide has a table of
plain replacements for every structural label this skill uses, and a final skim to run on titles,
block labels, questions and presenter notes.

### 4. Build the applet around a question

An applet is there to settle a prediction, so design it backwards from the question it answers.
Something must be draggable; the quantity students are asked about must be shown live; and the
"punchline" object (tangent line, exact value, limit) should start hidden behind a JSXGraph
checkbox so the lecturer reveals it only after the room has said it. See
`references/applet-recipes.md` for the reveal pattern and recipes by topic. Prefer the generic
`<JSXGraphBoard :init="...">` for 2D ideas; reuse an existing component in `components/` when one
already fits; write a new `.vue` component only when the applet needs its own controls or 3D.

### 5. Write the slides

**Deck folder.** New decks live in `2026/slides/NN_slug/` (next free number), containing
`slides.md` plus two symlinks so Slidev finds the shared code and theme:

```bash
ln -s ../../../components components
ln -s ../../../styles styles      # without this the dark theme does not load
```

Several older decks lack the `styles` link and render unstyled on white; do not copy that.

**Components.** This skill ships two components. Copy them into the repo's `components/` once if
they are not there yet:

```bash
cp -n .agents/skills/socratic-calculus-slides/assets/components/*.vue components/
```

- `<SocraticBlock type="question|predict|hint|answer|pitfall|reflect" title="…" mode="…" level="1">`
  Each type has its own colour and icon so students learn to read the slide's intent at a glance.
  Use `BeamerBlock` for content that is stated (problem statements, definitions, worked steps) and
  `SocraticBlock` for anything asked or revealed.
- `<PolyaStepper step="1-2" support="full|partial|independent" />` goes directly under the title
  of every problem-solving slide. It shows which phase the slide is in and how much support is
  left, which makes the fading visible to students.

**Markup rules that matter here** (beyond the companion skill's):

- Put `v-click` on the `SocraticBlock` itself, or on a wrapping `<div v-click class="flex flex-col">`
  when several blocks appear together.
- Hidden `v-click` content still occupies its space. Budget each slide for its **fully revealed**
  state, not its first state.
- Quote the frontmatter `title:` in single quotes and avoid colons in it; an unquoted colon is a YAML error and Slidev will not start (the checker then reports "did not start").
- Write display math with `$$` on its own line above and below. `$$\begin{aligned}` on one line
  renders as raw LaTeX.
- Blank line before and after the content inside any component, or Markdown and KaTeX are skipped.
- Blanks in half-finished examples: `\boxed{\phantom{00}}`.
- In `two-cols-header` slides, the title and `PolyaStepper` go before `::left::`.

**Presenter notes.** End every slide that asks something with an HTML comment (Slidev shows the
last comment as the presenter note). Write them in Indonesian, for the lecturer, in this shape:

```markdown
<!--
Tanya: cara mengajukan dan berapa lama menunggu.
Jawaban diharapkan: …
Jika ada yang menjawab "…" (salah yang umum): pertanyaan balik, bukan koreksi.
Jika hening: pertanyaan yang lebih kecil untuk membuka jalan.
-->
```

The follow-up to a wrong answer should be another question that lets the student find the
problem ("Coba periksa dengan $h = 1$"), because correcting them directly ends the thinking.

**Problem-solving slides.** Phase names are fixed: **1 · Pahami Soal**, **2 · Buat Rencana**,
**3 · Kerjakan**, **4 · Periksa Lagi** (these match `PolyaStepper`). Keep all four by default. If the
lecturer asks to drop Periksa Lagi, give every `PolyaStepper` in that deck `:phases="3"`, use steps
up to 3, and remove the look-back blocks; the checker then expects phases 1–3.

- *Worked example* (`full`): each phase opens with a `question` and resolves on a click. Phase 4
  is a real check (substitute back, sign, units, limiting case, sketch), never "jadi jawabannya…".
- *Half-finished* (`partial`): a structurally similar problem. Phases 1 to 2 are a single question
  ("Rencananya sama; apa dua hal yang harus kalian peroleh?"); phase 3 shows the skeleton with
  blanks; the revealed block lists the fills and one look-back check.
- *Independent* (`independent`): problem statement only, then three `hint` blocks in a
  `grid grid-cols-3`, each on its own click: level 1 reorients (what is asked, which definition),
  level 2 names the strategy, level 3 gives the first move. No hint gives the answer. The last
  click shows the **final answer and a look-back question**, not the full solution; the full
  solution is board work if needed.

Choose problems from the course texts (Stewart; Adams & Essex; Purcell) and cite the section in
the title's right-hand tag. Vary the surface across the three problems (a polynomial, then a
rational function, then a root, say) so students practise the plan, not the pattern.

### 6. Verify, then look

```bash
python3 .agents/skills/socratic-calculus-slides/scripts/verify_socratic_deck.py \
  2026/slides/NN_slug/slides.md --png 2026/slides/NN_slug/previews
```

Add `--scope segment` when the deliverable is a few slides and not a full lecture.

The script runs two passes. The **structure** pass reads the Markdown and checks the pedagogy:
hook present, a question attached to every applet, notes on every question slide, all four Pólya
phases, support fading in order, a hint ladder, an exit reflection. The **render** pass opens every
slide in headless Chromium in its fully revealed state and checks that nothing leaves the frame,
no LaTeX is left raw, boards are mounted, and no answer is visible before a click. It picks its
own free port, so it is safe to run while another Slidev server is up.

Use this checker for these decks. The older `verify_slidev_slides.py` only inspects the first
click state, and in testing it passed slides with unrendered `aligned` blocks.

Fix every error; treat warnings as prompts to reconsider. Then **open the screenshots**
(`slide-NN.png` and `slide-NN-revealed.png`) and read them as a student in the back row would. A
pass means nothing is broken; it does not mean the slide is clear. Typical fixes: cut words from a
question, move an answer to the next slide, add `class: slide-compact` to that slide's
frontmatter, reduce a board to `height="280px"`.

### 7. Report

Tell the user, briefly: the big question and learning goal you chose, the arc slide by slide (one
line each), which misconception the deck targets, the checker result, and where the previews are.
Mention anything you were unsure of (problem difficulty, timing) so they can adjust.

## Converting an existing deck

When asked to make an expository deck Socratic, do not sprinkle questions on top of the existing
order. Reorder: find the definition or theorem slides and move them after a new hook, prediction
and discovery sequence that leads to them; turn "Panduan eksplorasi" text that describes what the
applet shows into a `predict` block plus an observation question; convert the second worked
example to half-finished and the last to independent. Keep the original file and write the new
deck beside it unless told to replace it.

## Reference files

- `references/indonesian-diction.md`: plain-Indonesian rules, replacements for structural labels, and a final wording check. Read before writing slide text.
- `references/question-craft.md`: question types with good and weak examples, the hint ladder,
  response modes, and a misconception bank by MA1101 topic. Read when drafting questions.
- `references/applet-recipes.md`: the predict-then-reveal applet pattern in JSXGraph and recipes
  for limits, derivatives, extrema, Riemann sums, FTC and volumes. Read when building an applet.
- `assets/example_deck.md`: complete verified deck. Read before your first deck.
- `assets/components/`: `SocraticBlock.vue`, `PolyaStepper.vue`.
- `scripts/verify_socratic_deck.py`: structure and render checker.
