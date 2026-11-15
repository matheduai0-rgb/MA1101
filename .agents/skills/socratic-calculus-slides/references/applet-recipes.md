# Applet Recipes: Predict, Explore, Reveal

An applet in a Socratic deck exists to settle a question the room has already committed to. Build
it from the question backwards.

## The pattern

1. **One thing to drag.** A glider on a curve, a point on an axis, or a slider. If nothing moves,
   it is a picture; use a static figure and save the board.
2. **A live readout of the asked-about quantity.** If the prediction is about a slope, show the
   slope as a number that changes while dragging.
3. **The punchline starts hidden.** The tangent line, the exact area, the limit value: put it
   behind a JSXGraph checkbox so the lecturer shows it only after a student has said it.
4. **Start in a state that does not give the answer away.** Place the glider far from the limit
   position; start `n` small.
5. **A question beside it, not instructions.** The left column carries a `predict` block and, on a
   click, a notice question. "Geser slider" is for the presenter notes.

Two-column layout with the board at `height="330px"` on the right fits comfortably. Full-width
under a block: `height="280px"`.

## Skeleton

```html
<JSXGraphBoard
  height="330px"
  :boundingbox="[-0.4, 24, 3.2, -3]"
  :init="(board, JXG) => {
    const f = (x) => 5 * x * x;
    const curve = board.create('functiongraph', [f, 0, 3.2], { strokeColor: '#50a5fa', strokeWidth: 3 });
    const P = board.create('point', [1, 5], { name: 'P', fixed: true, color: '#f5be3c', size: 3 });
    const Q = board.create('glider', [2, 20, curve], { name: 'Q', color: '#fb7185', size: 4 });
    board.create('line', [P, Q], { strokeColor: '#fb7185', strokeWidth: 2 });
    board.create('text', [0.1, 22, () => 'kemiringan PQ = ' + ((Q.Y() - 5) / (Q.X() - 1 || 1e-9)).toFixed(3)], { fontSize: 15 });
    const show = board.create('checkbox', [0.1, 19.5, 'tampilkan garis singgung di P'], { fontSize: 13 });
    board.create('line', [[1, 5], [2, 15]], { strokeColor: '#34d399', strokeWidth: 2, dash: 2, visible: () => show.Value() });
  }"
/>
```

Things that bite inside an inline `:init`:

- The attribute is delimited by double quotes, so use single quotes for every JS string.
- Avoid `<` and `>` comparisons (the Vue template parser can read them as tags). Use
  `Math.min`/`Math.max`, `Math.sign`, or a ternary on a subtraction (`a - b > 0` still contains
  `>`; write `Math.max(a - b, 0)` or move the logic into a component).
- Guard divisions that hit zero while dragging (`|| 1e-9`).
- Colours: curve `#50a5fa`, fixed/primary point `#f5be3c`, moving object `#fb7185`, revealed
  object `#34d399`, secondary `#2dd4bf`. Text inherits a light colour from the board CSS.
- A slider: `board.create('slider', [[x1, y], [x2, y], [min, start, max]], { name: 'n', snapWidth: 1 })`,
  read with `s.Value()`.
- If the logic outgrows about twelve lines or needs comparisons and loops, write a component in
  `components/` modelled on `JSXGraphBoard.vue` (dynamic `useId()` container id, `freeBoard` in
  `onUnmounted`).

## Still figures for "cut, approximate, add up"

For ideas built on one thin slice (work, volume, mass, pumping), put a still labeled figure next
to the question before or beside the applet. Draw one slice and label its thickness (Δx or Δy),
the quantity on it (F(x), r, y) and the product it gives (ΔW ≈ F(x)·Δx). When two pictures
describe the same idea (a spring and its force graph), draw the same slice in both with dashed
guides between them. `components/WorkFigure.vue` is a working example (inline SVG, five `kind`s).
Do not label what students are being asked to find: in a fill-in or independent problem, leave out
the weight, radius or distance the question asks for (the `reveal` prop does this for the cable).

## Recipes by topic

Each line gives: predict question → what is dragged → live readout → hidden punchline.

- **Limit at a hole** ($\frac{x^2-1}{x-1}$ at 1): "Di $x=1$ fungsi tak terdefinisi. Nilai $f(x)$
  di dekatnya: A tak menentu, B mendekati 2, C membesar?" → glider on the curve → $x$ and $f(x)$ →
  dashed horizontal line $y = 2$.
- **One-sided limits** (piecewise jump): "Dari kiri dan dari kanan, sama?" → glider → $f(x)$ →
  the two limit levels.
- **Derivative as slope**: skeleton above.
- **Derivative as a function**: "Di mana grafik $f'$ memotong sumbu-$x$?" → glider with tangent →
  slope value → trace of the point $(x, f'(x))$ behind a checkbox.
- **Linear approximation**: "Sejauh mana garis singgung masih 'cukup dekat'?" → glider for
  $x$ away from $a$ → error $|f(x) - L(x)|$ → shaded error band.
- **Extrema / first derivative test**: "Di titik mana $f'$ berganti tanda?" → glider with tangent
  → sign and value of $f'$ → markers at critical points.
- **Optimization** (box, fence): "Potongan sudut berapa yang memberi volume terbesar?" → slider
  for the cut → volume → point on the $V(x)$ graph and its maximum.
- **Mean Value Theorem**: "Selalu adakah titik dengan garis singgung sejajar tali busur?" → glider
  $c$ → tangent slope vs. secant slope → the parallel tangent(s).
- **Riemann sums**: "Dengan $n$ makin besar, jumlah kiri naik atau turun?" → slider $n$ → sum →
  exact value. `CalcRiemannSum` already does most of this.
- **FTC 1** (area function): "Di mana $A(x) = \int_0^x f$ paling cepat bertambah?" → glider $x$ →
  shaded area and $A(x)$ → graph of $A$ and its slope.
- **Area between curves**: "Irisan tegak atau datar yang lebih mudah?" → glider moving a
  representative strip → strip height → the other slicing direction.
- **Volumes**: reuse `DiskWasherBoard`, `CrossSectionBoard`, and the 3D boards in `components/`;
  ask "Berapa jari-jari cakram di posisi ini?" before the slider moves.
