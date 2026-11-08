---
name: calculus-manim-animator
description: >-
  Generates 3Blue1Brown-style Socratic Manim CE animations for single-variable calculus
  (MA1101: limits, continuity, derivatives, optimization, Riemann sums, FTC, and Taylor series).
  Use whenever the user requests visual explanations, mathematical video scenes,
  or runnable Manim Python code for calculus concepts.
---

# Calculus Manim Animator (Socratic & 3Blue1Brown Pedagogy)

This skill equips the Antigravity agent to create elegant, pedagogically profound mathematical animations using the **Manim Community Edition (CE)** library. Rooted in Grant Sanderson's visual philosophy and the Socratic method, animations produced by this skill never introduce formal rigor until intuitive geometric clarity has been unlocked.

---

## 1. The 4-Act Socratic Pedagogical Arc

Every animation script must be structured around a four-stage cognitive journey:

```
┌─────────────────────────────────┐
│  Act 1: The Pique / Conundrum   │  Pique curiosity with a geometric puzzle or physical dilemma.
│     (Curiosity First)           │  Rule: Do NOT state the definition, theorem, or formula yet!
└───────────────┬─────────────────┘
                │
                ▼
┌─────────────────────────────────┐
│   Act 2: Visual Exploration     │  Animate continuous transformation (e.g. zooming into curvature,
│    (Geometric Mechanism)        │  accumulating dynamic strips, sliding secant points).
└───────────────┬─────────────────┘
                │
                ▼
┌─────────────────────────────────┐
│    Act 3: Socratic Inversion    │  Pose a direct question on screen (e.g., "What happens as Δx -> 0?").
│       (Predict Before Reveal)   │  Rule: Pause for 1.5–2.5s to let the viewer reflect.
└───────────────┬─────────────────┘
                │
                ▼
┌─────────────────────────────────┐
│ Act 4: Formal Crystallization   │  Map the now-obvious intuition into precise LaTeX notation
│      (Rigorous Synthesis)       │  (e.g., definition of derivative, FTC, Riemann integral).
└─────────────────────────────────┘
```

---

## 2. Visual Palette & Aesthetic Standards

Animations must follow Grant Sanderson's clean, high-contrast dark aesthetic:

- **Mathematical Curves**: `YELLOW` (primary $f(x)$) and `TEAL_C` (transformed $g(x)$ or target).
- **Rates & Changes**: `RED_C` or `MAROON_B` for tangents, $\Delta y$, velocity vectors, and differentials ($dx$).
- **Accumulations**: `BLUE_D` or `GREEN_D` with `fill_opacity=0.35` for integrals and Riemann sums.
- **Scaffolding**: Thin `GRAY_C` axes and ticks (`stroke_width=1.5`, `stroke_opacity=0.6`).
- **Pacing**: Use `rate_func=smooth` for organic transitions. Always insert `self.wait(1.5)` to `self.wait(2.5)` after key visual shifts to respect cognitive processing time.

For full color codes and LaTeX tokenization strategies, consult [references/color-palette.md](./references/color-palette.md).

---

## 3. Idiomatic Manim CE Implementation Guidelines

### A. Dynamic Reactive Updates (`ValueTracker` + `always_redraw`)
Never manually loop redraws if an updater can do it reactively.
```python
dx_tracker = ValueTracker(2.0)
secant = always_redraw(lambda:
    axes.get_secant_slope_group(
        x=2.0,
        dx=dx_tracker.get_value(),
        func=func,
        secant_line_color=TEAL_C
    )
)
self.play(dx_tracker.animate.set_value(0.001), run_time=4, rate_func=smooth)
```

### B. Local Linearity & Zooming (`MovingCameraScene`)
To show local linearity, animate the camera frame down to microscopic scales:
```python
self.play(
    self.camera.frame.animate.scale(0.12).move_to(axes.c2p(x0, func(x0))),
    run_time=3.5,
    rate_func=smooth
)
```

### C. Smooth Formula Morphing (`TransformMatchingTex`)
Isolate substrings in raw strings (`r"..."`) so Manim can intelligently interpolate math symbols:
```python
eq_secant = MathTex(r"\frac{\Delta y}{\Delta x}", r"=", r"\frac{f(x+\Delta x) - f(x)}{\Delta x}")
eq_deriv  = MathTex(r"\frac{df}{dx}", r"=", r"\lim_{\Delta x \to 0}", r"\frac{f(x+\Delta x) - f(x)}{\Delta x}")
self.play(TransformMatchingTex(eq_secant, eq_deriv))
```

For verified recipes on Riemann sums, FTC, and Taylor polynomials, consult [references/calculus-patterns.md](./references/calculus-patterns.md).

---

## 4. Agent Execution Workflow

When generating Manim animations for calculus topics:

1. **Storyboard Formulation**:
   - Write out the 4 acts explicitly in comments or markdown.
   - Clarify the Socratic question and the central geometric metaphor.
2. **Code Generation**:
   - Write standalone, runnable Python code targeting `manim` (Community Edition).
   - Use Indonesian for on-screen dialogue, question prompts, and annotations to match ITB course conventions (MA1101).
   - Use or extend the starter templates in [templates/](./templates/README.md):
     - [templates/06_related_rates_sliding_ladder.py](./templates/06_related_rates_sliding_ladder.py) (Subtopik 2.8 Laju yang Berkaitan)
     - [templates/07_mean_value_theorem.py](./templates/07_mean_value_theorem.py) (Subtopik 3.6 Teorema Nilai Rata-rata)
     - [templates/08_concavity_and_inflection.py](./templates/08_concavity_and_inflection.py) (Subtopik 3.2 & 3.3 Kecekungan & Titik Belok)
     - [templates/09_applied_optimization_box.py](./templates/09_applied_optimization_box.py) (Subtopik 3.1 & 3.4 Pengoptimuman Kotak Karton)
     - [templates/01_limits_and_continuity.py](./templates/01_limits_and_continuity.py) (Subtopik 1.2 Tantangan Limit $\varepsilon$-$\delta$)
     - [templates/02_derivative_local_linearity.py](./templates/02_derivative_local_linearity.py) (Subtopik 2.2 Kelinieran Lokal Turunan)
     - [templates/03_riemann_sums_and_integral.py](./templates/03_riemann_sums_and_integral.py) (Subtopik 4.2 Jumlah Riemann & Integral Tentu)
     - [templates/04_fundamental_theorem_of_calculus.py](./templates/04_fundamental_theorem_of_calculus.py) (Subtopik 4.3 Teorema Dasar Kalkulus I)
     - [templates/05_taylor_polynomials.py](./templates/05_taylor_polynomials.py) (Subtopik 6.4 Pendekatan Polinomial Taylor)
     - [templates/16_curve_sketching_with_calculus.py](./templates/16_curve_sketching_with_calculus.py) (Subtopik 3.5 Grafik Fungsi dengan Menggunakan Kalkulus)
     - [templates/17_mathematical_modeling_pipeline.py](./templates/17_mathematical_modeling_pipeline.py) (Subtopik 3.4 Pemodelan Matematika & Optimasi Terapan)
     - [templates/18_antiderivatives_family_of_curves.py](./templates/18_antiderivatives_family_of_curves.py) (Subtopik 3.8 Antiturunan & Keluarga Kurva $F(x)+C$)
     - [templates/19_differential_equations_separable.py](./templates/19_differential_equations_separable.py) (Subtopik 3.9 Pengantar Persamaan Diferensial & Pemisahan Peubah)
     - [templates/20_area_polygon_exhaustion.py](./templates/20_area_polygon_exhaustion.py) (Subtopik 4.1 Luas Daerah: Poligon Dalam, Poligon Luar & Notasi Sigma)
     - [templates/21_definite_integral_signed_area.py](./templates/21_definite_integral_signed_area.py) (Subtopik 4.2 Integral Tentu: Jumlah Riemann & Luas Bertanda)
     - [templates/22_first_fundamental_theorem_of_calculus.py](./templates/22_first_fundamental_theorem_of_calculus.py) (Subtopik 4.3 Teorema Dasar Kalkulus Pertama: Fungsi Akumulasi $A'(x)=f(x)$)
     - [templates/23_riemann_difference_telescoping.py](./templates/23_riemann_difference_telescoping.py) (Subtopik 4.1 & 4.2 Selisih Poligon Luar & Dalam: Menara Teleskopik)
     - [templates/24_liquid_flow_net_change_riemann.py](./templates/24_liquid_flow_net_change_riemann.py) (Subtopik 4.2 & 4.4 Laju Alir Fluida & Teorema Perubahan Total)
     - [templates/25_second_fundamental_theorem_of_calculus.py](./templates/25_second_fundamental_theorem_of_calculus.py) (Subtopik 4.4 Teorema Dasar Kalkulus Kedua: $A(x)=F(x)+C$ & Evaluasi $F(b)-F(a)$)
     - [templates/26_mean_value_theorem_for_integrals.py](./templates/26_mean_value_theorem_for_integrals.py) (Subtopik 4.5 Teorema Nilai Rata-rata untuk Integral: $\bar{f}=f(c)$)
     - [templates/27_symmetry_in_definite_integrals.py](./templates/27_symmetry_in_definite_integrals.py) (Subtopik 4.5 Penggunaan Simetri pada Integral Tentu: Fungsi Genap & Ganjil)
     - [templates/28_trapezoidal_and_midpoint_rules.py](./templates/28_trapezoidal_and_midpoint_rules.py) (Subtopik 4.6 Integrasi Numerik: Aturan Trapesium & Titik Tengah)
     - [templates/29_simpsons_parabolic_rule.py](./templates/29_simpsons_parabolic_rule.py) (Subtopik 4.6 Integrasi Numerik: Aturan Parabolik Simpson & Batas Galat)
     - [templates/30_area_between_curves_vertical.py](./templates/30_area_between_curves_vertical.py) (Subtopik 5.1 Luas Daerah pada Bidang: Pias Tegak $\Delta x$ & Kurva Berpotongan)
     - [templates/31_area_horizontal_vs_vertical_slicing.py](./templates/31_area_horizontal_vs_vertical_slicing.py) (Subtopik 5.1 Luas Daerah pada Bidang: Pias Mendatar $\Delta y$ vs Pias Tegak $\Delta x$)
     - [templates/32_volumes_disk_and_washer_method.py](./templates/32_volumes_disk_and_washer_method.py) (Subtopik 5.2.a Volume Benda Putar: Metode Cakram & Metode Cincin)
     - [templates/33_volumes_parallel_cross_sections.py](./templates/33_volumes_parallel_cross_sections.py) (Subtopik 5.2.b Volume Benda Pejal: Metode Irisan Sejajar / Lempeng)
     - [templates/34_volumes_cylindrical_shells_unrolling.py](./templates/34_volumes_cylindrical_shells_unrolling.py) (Subtopik 5.3 Volume Benda Putar: Metode Kulit Tabung & Pembentangan)
     - [templates/35_shells_vs_washers_and_shifted_axis.py](./templates/35_shells_vs_washers_and_shifted_axis.py) (Subtopik 5.3 Metode Kulit Tabung di Antara Dua Kurva & Sumbu Putar Bergeser $x=k$)
3. **Headless Test Render & Batch Export**:
   - Validate geometry and syntax using the preview script:
     ```bash
     .agents/skills/calculus-manim-animator/scripts/preview_scene.sh <path_to_script.py> [SceneName] -s
     ```
   - For batch compilation of lecture slides (PNG) or 1080p presentation videos (MP4):
     ```bash
     .agents/skills/calculus-manim-animator/scripts/build_lecture_pack.py -q high --filter "06"
     ```
   - Verify that text labels and mathematical equations do not overlap curves or fall off the 16:9 safe frame.
4. **Slide Deck Integration (`reveal-cindyjs-calculus-slides`)**:
   - Pair rendered Manim `.mp4` animations with **Reveal.js + KaTeX + CindyJS** interactive HTML5 lecture slides (see [../reveal-cindyjs-calculus-slides/SKILL.md](../reveal-cindyjs-calculus-slides/SKILL.md)).
   - Always run `.agents/skills/reveal-cindyjs-calculus-slides/scripts/verify_reveal_slides.py` on generated HTML slide decks to guarantee zero text overflow or clipping.


