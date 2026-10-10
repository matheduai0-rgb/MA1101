# 3Blue1Brown Aesthetic & Visual Standards Reference

Grant Sanderson's animations are instantly recognizable due to their disciplined color palette, subtle contrast, and calm pacing.

---

## 1. Official 3b1b Palette Constants (Manim CE)

In Manim CE, use these idiomatic color constants:

| Role | Color Constant | Hex Value | Usage |
| :--- | :--- | :--- | :--- |
| **Primary Curve** | `YELLOW` / `YELLOW_C` | `#F4D03F` | The main mathematical function $f(x)$ under study. |
| **Secondary Curve / Dynamic Target** | `BLUE_C` / `TEAL_C` | `#58C4DD` | The transformed function, anti-derivative $F(x)$, or target line. |
| **Secant / Tangent / Rate of Change** | `RED_C` / `MAROON_B` | `#FC6255` | Derivative indicators, secant lines, velocity vectors, $dx$, $\Delta y$. |
| **Area Fill / Integration** | `GREEN_D` / `BLUE_D` | `#29ABCA` | Riemann slices, under-curve area (`fill_opacity=0.35`). |
| **Focal Highlight / Attention** | `PINK` / `ORANGE` | `#D147BD` | Critical points, roots, inflection points, local maxima. |
| **Coordinate Scaffolding** | `GRAY_C` / `GRAY_D` | `#888888` | Axes, grid lines, tick labels, projection dashed lines (`stroke_opacity=0.5`). |
| **Background** | `BLACK` / Default dark | `#000000` | High-contrast dark canvas. |

---

## 2. Layout Geometry & Safe Zones (16:9 Frame)

Manim's camera frame defaults to dimensions **14.22 units wide by 8.0 units high** (`config.frame_width = 14.22`, `config.frame_height = 8.0`).

### Golden Layout Zones:
1. **Title / Socratic Prompt Banner**:
   - Placed at `.to_edge(UP, buff=0.4)`
   - Font size: `32` to `38` pt.
   - Kept short (1–2 lines max).
2. **Main Coordinate Canvas**:
   - Usually takes up the center-left or full center.
   - Standard dimensions: `x_length=9`, `y_length=5.5`.
   - Centered with `.shift(LEFT * 0.5 + DOWN * 0.2)` if formulas sit on the right edge.
3. **Formal Notation / Computation Side-Panel**:
   - Anchored at `.to_edge(RIGHT, buff=0.8)` or `.to_corner(UR, buff=0.6)`.
   - Math equations aligned left or along equals signs via `TransformMatchingTex`.

---

## 3. LaTeX String Splitting Rules

When animating mathematical derivations, break `MathTex` into logical visual tokens so Manim's `TransformMatchingTex` can track elements smoothly:

```python
# Bad: Monolithic string
eq1 = MathTex(r"\lim_{\Delta x \to 0} \frac{f(x+\Delta x) - f(x)}{\Delta x}")

# Good: Tokenized for smooth morphing
eq1 = MathTex(
    r"\frac{\Delta f}{\Delta x}",
    r"=",
    r"\frac{f(x + \Delta x) - f(x)}{\Delta x}"
)
eq2 = MathTex(
    r"\frac{df}{dx}",
    r"=",
    r"\lim_{\Delta x \to 0}",
    r"\frac{f(x + \Delta x) - f(x)}{\Delta x}"
)
self.play(TransformMatchingTex(eq1, eq2))
```

---

## 4. Animation Pacing Rules (The "Breathe" Principle)

- **Entry**: Never spawn elements instantly (`self.add`). Use gentle creates: `self.play(Create(axes), run_time=1.5)`, `self.play(Write(title))`.
- **Transformation**: Complex rate changes must feel physical. Use `rate_func=smooth` (default) or `rate_func=rush_into` / `rush_from`.
- **The Cognitive Pause**: After any visual transition or question reveal, **always wait at least 1.5–2.5 seconds**:
  ```python
  self.wait(2.0) # Gives the viewer time to parse the geometry before formula pops up
  ```
