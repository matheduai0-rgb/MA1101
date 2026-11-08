# Alternatives to LaTeX Beamer & Manim for MA1101 (Matematika I)

This reference guide catalogs modern alternatives to **LaTeX Beamer** (focusing on HTML5 slide engines with native LaTeX/Typst support and Typst-native slide frameworks) and **Manim** (focusing on functional/declarative animation frameworks like `reanimate` and `Motion Canvas`, and live interactive math engines like `CindyJS` and `MathBox`).

---

## 1. Why Explore Alternatives for MA1101?

In the standard MA1101 workflow (`2026/slides/*`), lecture decks are authored in **LaTeX Beamer** (`.tex` $\to$ `.pdf`) and paired with **Manim CE** scenes (`.py` $\to$ `.mp4` / `.ogv`). While high-quality, this stack has three main bottlenecks:
1. **PDF Multimedia Limitations**: Standard PDF viewers (`evince`, `okular`) struggle with embedded video playback, requiring wrapper scripts (`present.sh`, `play_video.sh`) with `pympress`, `pdfpc`, or external `mpv` windows.
2. **Zero Live Interactivity**: A pre-rendered MP4 video cannot let the lecturer or student drag a secant point $(x + \Delta x, f(x + \Delta x))$, change the number of Riemann strips $n \in [1, 200]$ on the fly, or toggle rotation axes ($x = 0$ vs. $x = 2$) interactively during class discussions.
3. **Render Turnaround Time**: Modifying a mathematical curve or label in Manim requires re-compiling Python + LaTeX + Cairo/OpenGL + FFmpeg.

---

## 2. Alternatives to LaTeX Beamer (Slide Presentation Engines)

### A. Summary Comparison Matrix

| Engine / Tool | Authoring Syntax | Math Engine (LaTeX / Typst) | Output Format | Native Video & Interactive Applets | Best Use Case |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1. Reveal.js (HTML / Markdown)** | HTML5 or Markdown | **KaTeX** or **MathJax 3** (LaTeX syntax), or `typst.ts` | Self-contained HTML5 | **Full support** (`<video>`, CindyJS, `<canvas>`, WebGL) | Self-contained interactive lecture decks that work in any browser & double as student web notes |
| **2. Quarto (`format: revealjs`)** | Quarto Markdown (`.qmd`) | **MathJax / KaTeX** (LaTeX) or Typst | HTML5 (Reveal.js), PDF, Beamer | **Full support** + executable Python/Julia & Observable JS | Academic courseware where a single `.qmd` file generates both HTML slides and PDF handouts |
| **3. Slidev** | Markdown + Vue 3 (`.md`) | **KaTeX** (LaTeX syntax) | HTML5 SPA / Static Site / PDF | **First-class** Vue components, live stylus drawing, Magic Move | Modern dark-themed slides with equation morphing, live annotations, and reactive widgets |
| **4. Touying / Polylux (Typst)** | Native **Typst** (`.typ`) | **Native Typst Math** (+ `@preview/mitex` for LaTeX) | PDF, SVG, or HTML wrapper | Static PDF/SVG by default; HTML bridge supports video/JS | Direct drop-in replacement for Beamer with **millisecond** live compilation (`typst watch`) |
| **5. Marp (Marpit)** | Pure Markdown (`.md`) | **KaTeX / MathJax** (LaTeX syntax) | HTML5, PDF, PPTX | HTML5 `<video>` & custom `<script>` / `<canvas>` | Lightweight, single-file Markdown slides with CSS theming |
| **6. Manim Slides** | Python (Manim CE / GL) | LaTeX (`MathTex`) | HTML5 (Reveal.js) or Qt GUI | Pre-rendered video segments controlled via keyboard | Turning pure Manim scripts directly into step-by-step slide decks |

---

### B. Detailed Breakdown & Code Snippets

#### 1. Reveal.js + KaTeX (HTML5 Native)
* **Strengths**: Zero build step required if using CDN/local JS bundles; supports Beamer-style dark themes, columns, callout blocks, incremental reveals (`class="fragment"`), speaker notes (`S` key), chalkboard drawing plugins, and direct `<video>` + `<canvas>` embedding.
* **Math Support**: Writes standard LaTeX (`$...$` and `$$...$$`) using the official `RevealMath.KaTeX` or `RevealMath.MathJax3` plugin.
* **See it in action**: Check out our working MA1101 Proof-of-Concept in [`2026/slides/25_volume_metode_kulit_tabung/interactive_cindyjs_reveal.html`](../2026/slides/25_volume_metode_kulit_tabung/interactive_cindyjs_reveal.html).

#### 2. Quarto Reveal.js (`.qmd`)
* **Strengths**: Designed specifically for scientific & academic publishing. Supports Beamer-like callout boxes (`::: {.callout-note}`, `::: {.callout-warning}`, `::: {.callout-tip}`) and side-by-side columns (`:::: {.columns}`).
* **Example (`kulit_tabung.qmd`)**:
  ```markdown
  ---
  title: "MA1101 Matematika I — Bab 5"
  subtitle: "Subtopik 5.3: Metode Kulit Tabung"
  format:
    revealjs:
      theme: dark
      html-math-method: katex
      slide-number: true
  ---

  ## Rumus Metode Kulit Tabung (Putar Sumbu-$y$)

  ::: {.callout-note title="Teorema Metode Kulit Tabung"}
  Jika daerah di bawah $y = f(x)$ pada $[a, b]$ diputar mengelilingi **sumbu-$y$**:
  $$\Delta V \approx 2\pi x\,f(x)\,\Delta x \implies V = 2\pi\int_{a}^{b} x\,f(x)\,dx$$
  :::
  ```

#### 3. Slidev (Markdown + Vue + KaTeX)
* **Strengths**: Built on Vite + Vue 3. Supports **Shiki Magic Move**, built-in **stylus/pen drawing** directly on slides during lectures (via `drauu`), presenter view with timer, and reactive Vue components.
* **Run Command**: `npx slidev slides.md`

#### 4. Typst: Touying (`@preview/touying`) & Polylux (`@preview/polylux`)
* **Strengths**: Typst compiles in **milliseconds** instead of seconds. Its math syntax is concise (`integral_a^b 2 pi x f(x) dif x`), and it includes `@preview/mitex` if you want to paste existing LaTeX equations directly.
* **Example (`kulit_tabung.typ` with Touying)**:
  ```typst
  #import "@preview/touying:0.5.3": *
  #import themes.metropolis: *

  #show: metropolis-theme.with(
    aspect-ratio: "16-9",
    config-info(
      title: [MA1101 Matematika I — Bab 5],
      subtitle: [Subtopik 5.3: Metode Kulit Tabung],
      author: [Tim Pengajar MA1101],
      institution: [FMIPA ITB],
    ),
  )

  #title-slide()

  == Geometri Satu Kulit Tabung
  Jika kulit tabung dibelah vertikal dan dibentangkan rata menjadi balok:
  $ Delta V approx ("keliling") dot ("tinggi") dot ("tebal") = 2 pi r dot h dot Delta r $
  #pause
  Maka untuk putaran mengelilingi sumbu-$y$:
  $ V = 2 pi integral_a^b underbrace(x, "jari-jari") dot underbrace(f(x), "tinggi") dif x $
  ```
* **HTML Export for Typst**: Using [`typst.ts`](https://github.com/Myriad-Dreamin/typst.ts) or Typst 0.13+'s experimental `--features html` (`typst compile --format html`), Typst slides can be rendered directly in the browser alongside HTML5 videos.

---

## 3. Alternatives to Manim (Math Animation & Interactive Engines)

Alternatives to Manim split into two categories:
1. **Interactive Web/Canvas Engines** (real-time 60 FPS manipulation inside HTML slides — *CindyJS, Mafs, JSXGraph, MathBox*).
2. **Programmatic / Functional Video Animation Engines** (timeline/code-driven animations — *Motion Canvas, Reanimate, Javis.jl, CeTZ*).

### A. Summary Comparison Matrix

| Engine / Tool | Language | Paradigm | Output | LaTeX / Typst Support | Key Advantage over Manim CE |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1. CindyJS** | JS + CindyScript | **Interactive** Projective Geometry & GPU Shaders (`CindyGL`) | Live HTML5 `<canvas>` / WebGL | KaTeX / MathJax labels | **60 FPS interactive** sliders, draggable points, & GPU pixel shaders directly inside HTML slides |
| **2. Motion Canvas** | TypeScript | Coroutine / Generator Timeline + **Real-time GUI** | Web Player (`<motion-canvas-player>`) or MP4 | Native `<Latex/>` with SVG morphing | **Real-time visual editor** with timeline scrubbing; exports interactive HTML web player |
| **3. Reanimate** | Haskell | **Purely Functional** SVG combinators (`Double -> SVG`) | MP4, WebM, GIF, SVG | Native LaTeX / Typst $\to$ SVG path extraction | Purely functional time composition (`parA`, `seqA`); deterministic parallel rendering |
| **4. Mafs.dev** | TypeScript / React | Declarative 2D Interactive Math Components | Live HTML `<svg>` DOM | KaTeX | 3Blue1Brown dark aesthetic out of the box (`<Mafs>`, `<Plot.OfX>`, `<MovablePoint>`) |
| **5. JSXGraph** | Vanilla JS | Interactive University Math & Calculus | Live HTML `<svg>` / `<canvas>` | MathJax / KaTeX | Zero build step; built-in Riemann sum, tangent, secant, and integral primitives |
| **6. MathBox (Three.js)** | JS / WebGL | 3D Shader-driven Mathematical Visualization | Live 3D WebGL `<canvas>` | KaTeX / HTML overlay | **Interactive 3D camera rotation** for Solids of Revolution, surfaces, and vector fields |
| **7. Javis.jl** | Julia | Frame-based imperative/reactive animation | MP4, GIF, Live Viewer | `LaTeXStrings.jl` | Direct access to Julia's differential equations (`DifferentialEquations.jl`) & numerics |
| **8. Typst + CeTZ / Lilaq** | Typst | Declarative Vector Graphics (TikZ successor) | PDF, SVG, PNG keyframes | Native Typst Math | Compiles static or multi-frame calculus diagrams in milliseconds |

---

### B. Deep-Dive & Code Examples

#### 1. CindyJS (`cindyjs.org`) — Real-Time Interactive Calculus & WebGL
* **Overview**: Created by the Technical University of Munich (TUM), CindyJS brings the classic *Cinderella* dynamic geometry system to HTML5 with a concise mathematical scripting language (**CindyScript**) and a WebGL shader compiler (**CindyGL**).
* **Why it is ideal for MA1101**:
  * Single `<script src="https://cindyjs.org/dist/latest/Cindy.js"></script>` tag in any HTML slide.
  * You can define draggable points on a canvas and write natural math syntax (`repeat(n, i, ...)`, `plot(f(x))`, `fillpoly(...)`) that executes at 60 FPS whenever the user drags a point or slider.
* **Minimal CindyJS Riemann / Cylindrical Shell Snippet**:
  ```html
  <div id="CSCanvas" style="width: 600px; height: 400px;"></div>
  <script id="csdraw" type="text/x-cindyscript">
    f(x) := 2*x^2 - x^3;
    // Draw shaded shells from x = 0 to 2
    repeat(n, i,
      x1 = (i - 1) * 2 / n;
      x2 = i * 2 / n;
      xm = (x1 + x2) / 2;
      fillpoly([[x1, 0], [x2, 0], [x2, f(xm)], [x1, f(xm)]], color->[0.18, 0.83, 0.75], alpha->0.4);
    );
    plot(f(x), start->0, stop->2, color->[0.96, 0.75, 0.24], size->3);
  </script>
  ```

#### 2. Reanimate (Haskell) — Functional Declarative Animation
* **Overview**: [`reanimate`](https://reanimate.github.io/) models an animation as a pure function from normalized time $t \in [0, 1]$ to an SVG tree (`Animation`). Instead of mutating objects Imperatively like Manim (`self.play(obj.animate.shift(UP))`), you compose animations algebraically using combinators:
  * `seqA :: Animation -> Animation -> Animation` (sequential composition)
  * `parA :: Animation -> Animation -> Animation` (parallel composition)
  * `playThenReverseA :: Animation -> Animation`
  * `latex :: Text -> SVG` (converts LaTeX math into vector SVG strokes for drawing/morphing)
* **Minimal Reanimate Calculus Snippet (`Main.hs`)**:
  ```haskell
  {-# LANGUAGE OverloadedStrings #-}
  module Main (main) where

  import Reanimate
  import Reanimate.Builtin.Documentation

  main :: IO ()
  main = reanimate $ docEnv $ scene $ do
    -- Act 1: Draw LaTeX Integral Formula with stroke animation
    eq <- newSpriteSVG $ center $ scale 2.0 $ withFillColor "white" $
            latex "$V = 2\\pi \\int_{a}^{b} x f(x)\\,dx$"
    play $ drawAnimation (svgAsAnimation eq)
    wait 1.5
  ```

#### 3. Motion Canvas (TypeScript) — Coroutine Animation with Real-Time Studio
* **Overview**: [`motioncanvas.io`](https://motioncanvas.io/) uses TypeScript generators (`function*`) and reactive signals (`createSignal(0)`). Unlike Manim, running `npm start` opens a **real-time browser studio** where you can scrub the timeline, inspect node coordinates, and tweak easing curves live.
* **Minimal Motion Canvas Snippet (`shellScene.tsx`)**:
  ```tsx
  import {makeScene2D, Latex, Line} from '@motion-canvas/2d';
  import {createSignal, all} from '@motion-canvas/core';

  export default makeScene2D(function* (view) {
    const unroll = createSignal(0); // 0 = cylinder, 1 = flat slab
    const formula = <Latex tex="{\color{white} \Delta V = 2\pi r \cdot h \cdot \Delta x}" y={-300} opacity={0} />;
    view.add(formula);

    // Animate unrolling signal and fade in formula simultaneously
    yield* all(
      unroll(1, 2.5),
      formula.opacity(1, 1.5),
    );
  });
  ```

---

## 4. Recommended Hybrid Workflow for MA1101

You do **not** have to abandon your existing 35 Manim scenes! The highest-leverage upgrade for MA1101 is:
1. **Slide Layer**: Author lecture decks in **Reveal.js HTML + KaTeX** (or **Quarto Reveal.js** / **Typst Touying**).
2. **Pre-rendered Socratic Videos**: Embed your existing Manim `.mp4` videos directly via standard HTML5 `<video controls>` tags (eliminating `pympress`/`pdfpc` compatibility issues).
3. **Live Interactive Exploration**: Add **CindyJS** interactive applets right next to the Manim videos so you can scrub parameters ($x_0, \Delta x, n, \text{unroll } t \in [0,1], \text{axis } x = k$) live in class in response to student questions!
