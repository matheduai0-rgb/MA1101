---
name: reveal-cindyjs-calculus-slides
description: >-
  Generates and verifies 3Blue1Brown-styled interactive HTML5 lecture slide decks
  for MA1101 (Matematika I / Calculus I) using Reveal.js, KaTeX, CindyJS (real-time
  60 FPS interactive geometry), and embedded Manim CE videos, with mandatory automated
  DOM/viewport text-overflow verification so zero text is ever clipped or hidden.
---

# Reveal.js + CindyJS + Manim Interactive Lecture Slides (MA1101)

This skill equips the Antigravity agent to create, style, and verify interactive HTML5 lecture presentations for **MA1101 (Matematika I / Calculus I)** at FMIPA ITB. It replaces static LaTeX Beamer PDFs with **Reveal.js + KaTeX + CindyJS + Manim CE**, combining Socratic pre-rendered Manim videos with real-time 60 FPS interactive CindyJS applets and automated viewport overflow verification.

---

## 1. Core Architecture & Pedagogical Stack

Every MA1101 lecture deck in `2026/slides/<number>_<topic>/` consists of:
1. **Reveal.js 5 HTML5 Slide Deck (`interactive_cindyjs_reveal.html`)**:
   - Configured at `width: 1120, height: 700, margin: 0.04, center: false` in the **3Blue1Brown Dark Obsidian** palette (`#0c1018` canvas, `#141b28` cards, luminous gold `#f5be3c`, electric blue `#50a5fa`, teal cyan `#2dd4bf`, emerald green `#34d399`, coral rose `#fb7185`).
2. **KaTeX Auto-Render (`v0.16+`)**:
   - Instant vector math typesetting using standard LaTeX delimiters `$...$` and `$$...$$`.
   - Zero `.katex-error` tolerance.
3. **CindyJS (`v0.8.8+`) Live Interactive Applets**:
   - Real-time 60 FPS interactive mathematical canvases (`<div id="CSCanvas..." class="cindy-canvas"></div>`) paired with HTML5 range sliders (`<input type="range">`) and live numerical readouts.
   - Enables lecturers and students to scrub parameters ($x_0, \Delta x, N, \text{unroll } t \in [0, 1], \text{axis } x = k$) live in class.
4. **Manim CE Native `<video>` Embeds**:
   - Pre-rendered Socratic 4-Act `.mp4` / `.ogv` animations (generated via `calculus-manim-animator`) embedded via native HTML5 `<video controls preload="metadata" poster="...">` tags—no external `pympress`/`pdfpc` required.

---

## 2. Compact Typography & Anti-Overflow Layout Rules ("Smaller Text" Standard)

> [!IMPORTANT]
> Reveal.js clips any content that exceeds the configured `1120x700` slide frame (`overflow: hidden` on `.slides > section`). Because calculus derivations, multi-column proofs, and side-by-side examples are text- and formula-dense, **always use compact typography** so all text appears clearly without being cut off at the bottom or right edge.

### A. Standard Compact Font Scale
Use these CSS rules in every slide deck (see [templates/template_reveal_cindy.html](./templates/template_reveal_cindy.html)):
- **Slide Title (`h2.slide-title`)**: `font-size: 1.15em`, `padding: 7px 14px`, `margin-bottom: 10px`.
- **Beamer-style Callout Blocks (`.b-block`, `.b-example`, `.b-alert`)**:
  - Default font size: `0.54em` (`line-height: 1.38`).
  - Block title padding: `4px 12px`; block body padding: `7px 12px`; bottom margin: `8px`.
- **Display Math (`.katex-display`)**:
  - Override default KaTeX `1em` vertical margins to `margin: 0.28em 0 !important;` and `font-size: 0.95em;` so multi-line `aligned` blocks do not push bottom cards off-screen.
- **Density Utility Classes**:
  - Apply `.slide-compact` on `<section class="slide-compact">` to scale all blocks on that slide down to `0.50em` and tighten grid gaps (`10px`).
  - Apply `.slide-ultra-compact` on `<section class="slide-ultra-compact">` for extra-dense exam synthesis or 4-box slides (`0.46em`).
  - Use `.text-xs` (`0.88em`) or `.text-2xs` (`0.80em`) for footnotes, citations, and answer keys.

### B. Layout Safe-Zone Guidelines
1. **Maximum Vertical Stack**:
   - At most **1 top full-width block + 1 two-column grid (`grid-2`)**, OR **2 full-width blocks** per slide.
   - Never stack 3 full-width blocks vertically on a single slide; split into two slides or use `.grid-2` (2x2 layout) with `.slide-compact`.
2. **Interactive Applet Slides (`.grid-applet`)**:
   - Keep `.cindy-canvas` height between `320px` and `350px` so the canvas + slide title + bottom caption stays strictly under `640px` total height.

---

## 3. Mandatory Automated Slide Verification Workflow

After creating or modifying **any** Reveal.js HTML slide deck, you **MUST** run the automated Playwright/Chromium verifier before declaring the task complete:

```bash
.agents/skills/reveal-cindyjs-calculus-slides/scripts/verify_reveal_slides.py \
  <path/to/deck.html> \
  --export-png <path/to/slide_dir>
```

### What `verify_reveal_slides.py` Checks on Every Slide (`1..N`):
1. **Slide Vertical & Horizontal Overflow**:
   - Checks that `section.scrollHeight <= slideHeight` and `section.scrollWidth <= slideWidth`.
2. **Internal Block & Text Clipping**:
   - Inspects every `.b-block`, `.b-example`, `.b-alert`, `.formula-box`, `.control-panel`, `table`, `p`, `li`, and `.katex-display` to ensure:
     - Its bottom bounding box does not exceed the bottom edge of the Reveal.js slide frame.
     - Its right bounding box does not exceed the right edge of the Reveal.js slide frame.
     - No internal container clips its own children (`el.scrollHeight <= el.clientHeight + 2`).
3. **KaTeX Formula Integrity**:
   - Verifies zero `.katex-error` elements exist and no raw unrendered `$$` delimiters remain visible.
4. **CindyJS & Video Readiness**:
   - Verifies all `.cindy-canvas` elements initialize with valid non-zero `<canvas>` dimensions.

### Fixing Failures Reported by the Verifier
If `verify_reveal_slides.py` exits with non-zero status and reports an overflow on Slide $k$:
1. Add `class="slide-compact"` (or `class="slide-ultra-compact"`) to `<section>` for Slide $k$.
2. Convert stacked blocks into a 2-column `.grid-2` layout, or combine multi-line display equations onto a single line (`$$A = B = C$$`).
3. Re-run `verify_reveal_slides.py` until **100% of slides report `PASS (0 overflow, 0 clipped)`**.
