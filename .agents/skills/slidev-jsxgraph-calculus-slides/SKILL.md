---
name: slidev-jsxgraph-calculus-slides
description: >-
  Technical layer for MA1101 Slidev decks: the dark "Obsidian" theme, KaTeX rules, BeamerBlock,
  two-column layouts, the vertical space budget, JSXGraph Vue components in components/ (catalogue
  included), Slidev's MCP tools, and Playwright overflow checks. Use when building or fixing the
  mechanics of a Slidev calculus deck: text clipped or overflowing, KaTeX not rendering or raw
  LaTeX showing, a JSXGraph board blank or misbehaving, writing or reusing a .vue applet, layout or
  theme problems, exporting slide PNGs, or asking which components already exist. Pairs with
  socratic-calculus-slides, which decides what goes on the slides; for legacy Reveal.js decks use
  reveal-cindyjs-calculus-slides instead.
---

# Slidev + JSXGraph Interactive Calculus Slides (MA1101)

This skill holds the technical conventions for MA1101 lecture decks built with **Slidev (Vite + Vue 3 + Markdown)**, **KaTeX** and **JSXGraph**. It covers how a deck is laid out, styled, wired to applets and checked. What the slides say and in what order (questions, Pólya scaffolding, timing) belongs to `socratic-calculus-slides`; read both when writing a deck.

---

## 1. Core Architecture & AI-Native Stack

Every MA1101 Slidev lecture deck consists of:
1. **Slidev Deck (`slides.md`)**:
   - Built on Vue 3, Vite, and UnoCSS / Tailwind.
   - Configured with `canvasWidth: 980`, 16:9 ratio, and 3Blue1Brown Dark Obsidian styling (`#0c1018` dark canvas, `#141b28` cards, gold `#f5be3c`, cyan `#2dd4bf`, blue `#50a5fa`).
2. **KaTeX Math Typesetting**:
   - Typesets LaTeX calculus formulas cleanly with standard `$f(x)$` and `$$\int_a^b f(x) dx$$` delimiters.
   - Zero tolerance for `.katex-error` or unparsed environments.
3. **JSXGraph Vue 3 Components**:
   - Interactive calculus applets in `components/` (about 25, e.g. `<CalcRiemannSum />`, `<JSXGraphBoard />`, `<LnAreaBoard />`). See `references/component_catalog.md` before writing a new one.
   - Transform-aware and scale-safe: automatically handles Slidev CSS `transform: scale(...)` without cursor offset bugs.
4. **Slidev Built-in MCP Server**:
   - Exposes structured presentation manipulation tools over `http://localhost:3030/__mcp` or `slidev mcp slides.md`:
     - `slidev-list-slides`, `slidev-get-slide`, `slidev-update-slide`, `slidev-goto-slide`.
5. **Mandatory Automated Text-Overflow Auditor**:
   - Automated verification via `verify_slidev_slides.py` using headless Playwright to guarantee that **zero text or equation is cut off at the bottom or sides**.

---

## 2. Compact Typography & Layout Budget ("Smaller Text" Standard)

> [!IMPORTANT]
> Slidev presentations enforce a fixed 16:9 viewport. Calculus proofs, side-by-side theorem cards, and interactive boards are dense. **Always adhere to the compact typography and layout budget** so all text appears fully without clipping or overflow.

### A. Density Scale Rules
- **Slide Title**: Keep headings concise with `<h2 class="slide-title">` or Markdown `# Title` with compact bottom margin.
- **Beamer-style Callout Blocks & Math Parsing Rule**:
  - Always use the `<BeamerBlock>` component with **blank lines** before and after content so KaTeX and markdown-it parse inner math formulas:
    ```markdown
    <BeamerBlock type="block" title="Teorema Dasar Kalkulus I">

    Jika $f$ kontinu pada $[a, b]$, maka $F(x) = \int_a^x f(t)\,dt$ kontinu pada $[a, b]$ dan:

    $$F'(x) = f(x)$$

    </BeamerBlock>
    ```
  - **Never wrap Markdown math in raw HTML `<div class="...">` tags**, as markdown-it switches to raw HTML mode and skips KaTeX typesetting entirely.
  - For two-column layouts, always use Slidev's native `layout: two-cols-header` (or `layout: two-cols`) with `::left::` and `::right::` slots rather than nested HTML grids.
- **LaTeX Inequalities**:
  - **Always use `\lt` and `\gt`** (e.g. `$a \lt b$`) rather than literal `<` or `>` so the Vue template parser never mistakes math expressions for HTML tags.
- **Slide Compact Utility**:
  - Use class `slide-compact` on dense slides to scale card text down to `0.85rem` and gap spacing to `0.5rem`.

### B. Vertical Budget Rules
- **Slide with Interactive Board**:
  - 1 top title or short theorem card ($< 160\text{px}$).
  - 1 JSXGraph board with `height="300px"` or `height="280px"`.
  - 1 bottom conclusion or numerical readout ($< 60\text{px}$).
  - **Never** stack 2 full-width cards *and* an interactive canvas on the same slide; split into two slides!
- **Slide with Derivations / Multiple Cards**:
  - Use 2-column grids: `<div class="grid grid-cols-2 gap-4">`.

---

## 3. JSXGraph Vue Component Integration

Reuse the components in `components/` (listed with their props and an example deck in `references/component_catalog.md`) before writing a new one:

```html
<!-- Example 1: Pre-built Riemann Sum Board -->
<CalcRiemannSum :initial-n="8" height="300px" :a="0.5" :b="4.5" />

<!-- Example 2: Custom Geometry using JSXGraphBoard -->
<JSXGraphBoard 
  height="300px" 
  :boundingbox="[-3, 6, 6, -3]"
  :init="(board, JXG) => {
    const f = (x) => 0.5 * x * x;
    board.create('functiongraph', [f, -2, 5], { strokeColor: '#50a5fa', strokeWidth: 3 });
    const p = board.create('glider', [2, 2, board.select('functiongraph')], { name: 'P', color: '#f5be3c' });
    board.create('tangent', [p], { strokeColor: '#fb7185', strokeWidth: 2, dash: 2 });
  }" 
/>
```

### Writing a new component
Follow the pattern of the recent applets (`ExpBoard.vue`, `InverseBoard.vue`, `CableSpringBoard.vue`): dynamic `import('jsxgraph')`, a `ResizeObserver`, `freeBoard` on unmount, the board handle stored on the element (`el.__jxgBoard`) so Playwright tests can drive it, decimal commas in readouts, and a checkbox that hides the "punchline" object until the room has answered. Label colours: a global `.jxgbox .JXGtext` rule forces white text, so give coloured labels `cssClass: 'JXGtext jx-<colour>'` with a scoped `!important` rule. After adding a component, run `python3 .agents/skills/slidev-jsxgraph-calculus-slides/scripts/list_components.py` to refresh the catalogue.

### Component Lifecycle Safeguards:
- Always clean up boards in `onUnmounted()` via `JXG.JSXGraph.freeBoard(board)` to prevent memory leaks across slide navigation.
- Never use a hardcoded HTML element ID like `<div id="box">`; always generate a dynamic unique ID per component instance.

---

## 4. Mandatory Automated Verification Workflow

For Socratic decks (anything with `SocraticBlock`/`PolyaStepper`), use `socratic-calculus-slides/scripts/verify_socratic_deck.py` instead: it checks every slide in its fully revealed state, which this older script does not. For other Slidev decks, run:

```bash
python3 .agents/skills/slidev-jsxgraph-calculus-slides/scripts/verify_slidev_slides.py <path/to/slides.md> [--export-png <output_dir>]
```

### What the script verifies:
1. **Vertical / Horizontal Overflow**: Fails if `scrollHeight > clientHeight + 4px` on any slide.
2. **Text Containment**: Scans all cards, headers, paragraphs, and formulas to ensure bounding box bottom and right edges stay strictly within the slide safe area.
3. **KaTeX Integrity**: Checks that zero `.katex-error` elements exist and no raw `$$` or `\begin{aligned}` markers remain unparsed.
4. **Active JSXGraph Canvas**: Verifies that all `<div class="jxgbox">` elements contain an active SVG with non-zero dimensions.
5. **Slide Previews**: Saves high-resolution `.png` snapshots for fast human inspection.

If any slide fails, adjust the typography (`.slide-compact`), reduce canvas height, or split the content across two slides.
