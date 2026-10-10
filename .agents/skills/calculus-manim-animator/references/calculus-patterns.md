# Single-Variable Calculus Manim Patterns

This reference provides idiomatic, bug-free Manim Community Edition patterns tailored for single-variable calculus (MA1101).

---

## 1. Local Linearity & Zooming In (`MovingCameraScene`)

A fundamental 3Blue1Brown insight: *"A differentiable curve is just something that looks straight when you zoom in."*

```python
from manim import *

class LocalLinearityScene(MovingCameraScene):
    def construct(self):
        axes = Axes(
            x_range=[-1, 5, 1],
            y_range=[-1, 8, 2],
            x_length=9,
            y_length=6,
            axis_config={"color": GRAY_C, "stroke_width": 2}
        ).add_coordinates()

        func = lambda x: 0.5 * (x - 2)**3 - (x - 2) + 3
        curve = axes.plot(func, color=YELLOW, stroke_width=3)
        
        x_target = 2.0
        pt_coords = axes.c2p(x_target, func(x_target))
        dot = Dot(pt_coords, color=RED_C, radius=0.08)

        self.play(Create(axes), Create(curve), run_time=2)
        self.play(FadeIn(dot, scale=1.5))
        self.wait(1)

        # Zoom into the point by shrinking the camera frame
        self.play(
            self.camera.frame.animate.scale(0.12).move_to(pt_coords),
            run_time=4,
            rate_func=smooth
        )
        self.wait(2)
```

---

## 2. Dynamic Secant Line Transitioning to Tangent Line (`ValueTracker`)

Demonstrating the limit definition $\frac{df}{dx} = \lim_{\Delta x \to 0} \frac{f(x+\Delta x) - f(x)}{\Delta x}$.

```python
from manim import *

class SecantToTangentScene(Scene):
    def construct(self):
        axes = Axes(
            x_range=[0, 6, 1],
            y_range=[0, 10, 2],
            x_length=8,
            y_length=5
        ).add_coordinates()

        func = lambda x: 0.3 * x**2 + 1
        graph = axes.plot(func, color=YELLOW)
        
        x0 = 2.0
        dx_tracker = ValueTracker(2.5)

        # Dynamic secant line that updates with dx
        secant_line = always_redraw(lambda: 
            axes.get_secant_slope_group(
                x=x0,
                dx=dx_tracker.get_value(),
                dx_line_color=GREEN_C,
                df_line_color=RED_C,
                secant_line_color=TEAL_C,
                secant_line_length=6,
                func=func
            )
        )

        pt0 = Dot(axes.c2p(x0, func(x0)), color=YELLOW)
        pt_dynamic = always_redraw(lambda:
            Dot(axes.c2p(x0 + dx_tracker.get_value(), func(x0 + dx_tracker.get_value())), color=TEAL_C)
        )

        self.play(Create(axes), Create(graph))
        self.play(Create(secant_line), FadeIn(pt0), FadeIn(pt_dynamic))
        self.wait(1)

        # Socratic animation: Send dx -> 0.001
        self.play(
            dx_tracker.animate.set_value(0.01),
            run_time=5,
            rate_func=smooth
        )
        self.wait(2)
```

---

## 3. Riemann Rectangles to Definite Integral ($\int_a^b f(x)dx$)

Visualizing the accumulation of infintesimal slices.

```python
from manim import *

class RiemannIntegralScene(Scene):
    def construct(self):
        axes = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 8, 2],
            x_length=9,
            y_length=5.5
        ).add_coordinates()

        func = lambda x: 0.2 * x**3 - x**2 + 2 * x + 1
        graph = axes.plot(func, x_range=[0.5, 4.5], color=YELLOW)
        
        a, b = 1.0, 4.0

        # Initial coarse Riemann sum (dx = 0.6)
        rects = axes.get_riemann_rectangles(
            graph,
            x_range=[a, b],
            dx=0.6,
            stroke_width=1.0,
            stroke_color=WHITE,
            fill_opacity=0.45,
            color=(BLUE_C, TEAL_C)
        )

        self.play(Create(axes), Create(graph))
        self.play(Create(rects), run_time=2)
        self.wait(1.5)

        # Refine step by step
        for next_dx in [0.25, 0.1, 0.03]:
            new_rects = axes.get_riemann_rectangles(
                graph,
                x_range=[a, b],
                dx=next_dx,
                stroke_width=0.2 if next_dx < 0.1 else 0.8,
                stroke_color=WHITE if next_dx >= 0.1 else None,
                fill_opacity=0.5,
                color=(BLUE_C, TEAL_C)
            )
            self.play(Transform(rects, new_rects), run_time=1.5)
            self.wait(0.8)

        # Culmination: True continuous area
        area = axes.get_area(graph, x_range=[a, b], color=BLUE_D, opacity=0.6)
        self.play(FadeTransform(rects, area), run_time=2)
        self.wait(2)
```

---

## 4. Fundamental Theorem of Calculus (Area Accumulation & Derivative)

Illustrating why $\frac{d}{dx}\int_a^x f(t)dt = f(x)$: the added strip has area $\approx f(x) \cdot dx$.

```python
from manim import *

class FTCScene(Scene):
    def construct(self):
        axes = Axes(
            x_range=[0, 6, 1],
            y_range=[0, 6, 1],
            x_length=8.5,
            y_length=5
        ).add_coordinates()

        f = lambda t: 0.15 * t**2 + 0.8
        graph = axes.plot(f, color=YELLOW)

        x_tracker = ValueTracker(3.0)
        dx = 0.35

        # Accumulated area up to x
        acc_area = always_redraw(lambda:
            axes.get_area(graph, x_range=[1.0, x_tracker.get_value()], color=BLUE_E, opacity=0.5)
        )

        # Marginal addition strip dA = f(x) * dx
        marginal_strip = always_redraw(lambda:
            axes.get_area(
                graph,
                x_range=[x_tracker.get_value(), x_tracker.get_value() + dx],
                color=RED_C,
                opacity=0.7
            )
        )

        self.play(Create(axes), Create(graph))
        self.play(FadeIn(acc_area), FadeIn(marginal_strip))
        
        # Move x to see the continuous accumulation
        self.play(x_tracker.animate.set_value(4.8), run_time=4, rate_func=smooth)
        self.wait(2)
```
