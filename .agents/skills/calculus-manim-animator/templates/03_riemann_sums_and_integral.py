"""
Template: Socratic Riemann Sums to Definite Integral (MA1101)
Topic: Riemann Rectangles, Mesh Refinement, and the Definite Integral
Style: Grant Sanderson (3Blue1Brown)
"""

from manim import *

class SocraticRiemannScene(Scene):
    def construct(self):
        # -------------------------------------------------------------
        # ACT 1: The Pique / Puzzle
        # -------------------------------------------------------------
        title = Text("How do you measure area bounded by a curved shape?", font_size=30)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))
        self.wait(1.5)

        axes = Axes(
            x_range=[0, 6, 1],
            y_range=[0, 7, 1],
            x_length=8.5,
            y_length=5,
            axis_config={"color": GRAY_C}
        ).add_coordinates()
        axes.shift(DOWN * 0.4)

        f = lambda x: 0.15 * x**3 - 0.7 * x**2 + 1.5 * x + 2.0
        graph = axes.plot(f, x_range=[0.5, 5.5], color=YELLOW, stroke_width=3)
        
        a, b = 1.0, 5.0
        line_a = axes.get_vertical_line(axes.c2p(a, f(a)), color=GRAY_A, stroke_width=1.5)
        line_b = axes.get_vertical_line(axes.c2p(b, f(b)), color=GRAY_A, stroke_width=1.5)
        label_a = MathTex(r"a", font_size=26).next_to(axes.c2p(a, 0), DOWN)
        label_b = MathTex(r"b", font_size=26).next_to(axes.c2p(b, 0), DOWN)

        self.play(Create(axes), Create(graph), Create(line_a), Create(line_b), Write(label_a), Write(label_b), run_time=2)
        self.wait(1)

        # -------------------------------------------------------------
        # ACT 2: Visual Discovery (Coarse Riemann Rectangles)
        # -------------------------------------------------------------
        rects = axes.get_riemann_rectangles(
            graph,
            x_range=[a, b],
            dx=0.8,
            stroke_width=1.2,
            stroke_color=WHITE,
            fill_opacity=0.4,
            color=(BLUE_C, TEAL_C)
        )

        sum_label = MathTex(r"\sum_{i=1}^n f(x_i^*) \Delta x \approx \text{Area}", font_size=28)
        sum_label.to_corner(UR, buff=0.6)

        self.play(Create(rects), Write(sum_label), run_time=2)
        self.wait(1.5)

        # -------------------------------------------------------------
        # ACT 3: Socratic Inversion (Refinement as Δx -> 0)
        # -------------------------------------------------------------
        question = Text("What happens as rectangle slices become infinitely thin?", font_size=26, color=TEAL_A)
        question.to_edge(UP, buff=0.4)
        self.play(Transform(title, question))
        self.wait(1.5)

        for next_dx, run_t in [(0.4, 1.2), (0.15, 1.2), (0.04, 1.5)]:
            new_rects = axes.get_riemann_rectangles(
                graph,
                x_range=[a, b],
                dx=next_dx,
                stroke_width=0.2 if next_dx < 0.1 else 0.8,
                stroke_color=WHITE if next_dx >= 0.1 else None,
                fill_opacity=0.55,
                color=(BLUE_C, TEAL_C)
            )
            self.play(Transform(rects, new_rects), run_time=run_t)
            self.wait(0.5)

        # Morph rectangles into the smooth continuous area
        continuous_area = axes.get_area(graph, x_range=[a, b], color=BLUE_D, opacity=0.55)
        self.play(FadeTransform(rects, continuous_area), run_time=2)
        self.wait(1.5)

        # -------------------------------------------------------------
        # ACT 4: Formal Crystallization
        # -------------------------------------------------------------
        integral_formula = MathTex(
            r"\int_a^b f(x)\,dx",
            r"=",
            r"\lim_{n \to \infty} \sum_{i=1}^n f(x_i^*)\,\Delta x",
            font_size=32
        ).to_corner(UR, buff=0.6)
        integral_formula[0].set_color(YELLOW)
        integral_formula[2].set_color(TEAL_C)

        box = SurroundingRectangle(integral_formula, color=BLUE_B, buff=0.15)

        self.play(TransformMatchingTex(sum_label, integral_formula), Create(box))
        self.wait(2.5)
