"""
Template: Socratic Taylor Polynomial Approximations (MA1101)
Topic: Osculating Polynomials Hugging cos(x)
Style: Grant Sanderson (3Blue1Brown)
"""

from manim import *
import numpy as np

class SocraticTaylorScene(Scene):
    def construct(self):
        # -------------------------------------------------------------
        # ACT 1: The Pique / Puzzle
        # -------------------------------------------------------------
        title = Text("How do computers evaluate transcendental functions?", font_size=30)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))
        self.wait(1.5)

        axes = Axes(
            x_range=[-4.5, 4.5, 1],
            y_range=[-2.2, 2.5, 1],
            x_length=9,
            y_length=5,
            axis_config={"color": GRAY_C}
        ).add_coordinates()
        axes.shift(DOWN * 0.4)

        cos_fn = lambda x: np.cos(x)
        cos_graph = axes.plot(cos_fn, color=YELLOW, stroke_width=3)
        cos_label = MathTex(r"f(x) = \cos(x)", color=YELLOW, font_size=28).next_to(axes.c2p(3.2, 1.2), UP)

        self.play(Create(axes), Create(cos_graph), FadeIn(cos_label), run_time=2)
        self.wait(1)

        # -------------------------------------------------------------
        # ACT 2: Visual Discovery (Matching Derivatives at x = 0)
        # -------------------------------------------------------------
        # Degree 0: Constant approximation
        p0_fn = lambda x: 1.0
        p0_graph = axes.plot(p0_fn, color=RED_C, stroke_width=2.5)
        p0_label = MathTex(r"P_0(x) = 1", color=RED_C, font_size=28).to_corner(UR, buff=0.6)

        self.play(Create(p0_graph), Write(p0_label))
        self.wait(1.5)

        # Degree 2: Matching curvature
        p2_fn = lambda x: 1.0 - 0.5 * x**2
        p2_graph = axes.plot(p2_fn, x_range=[-2.4, 2.4], color=TEAL_C, stroke_width=2.5)
        p2_label = MathTex(r"P_2(x) = 1 - \frac{x^2}{2!}", color=TEAL_C, font_size=28).to_corner(UR, buff=0.6)

        self.play(Transform(p0_graph, p2_graph), TransformMatchingTex(p0_label, p2_label), run_time=2)
        self.wait(1.5)

        # -------------------------------------------------------------
        # ACT 3: Socratic Inversion
        # -------------------------------------------------------------
        socratic_question = Text(
            "What happens to the region of agreement as order increases?",
            font_size=26,
            color=TEAL_A
        ).to_edge(UP, buff=0.4)

        self.play(Transform(title, socratic_question))
        self.wait(1.5)

        # Degree 4
        p4_fn = lambda x: 1.0 - 0.5 * x**2 + (x**4) / 24.0
        p4_graph = axes.plot(p4_fn, x_range=[-3.2, 3.2], color=GREEN_C, stroke_width=2.5)
        p4_label = MathTex(r"P_4(x) = 1 - \frac{x^2}{2!} + \frac{x^4}{4!}", color=GREEN_C, font_size=28).to_corner(UR, buff=0.6)

        self.play(Transform(p0_graph, p4_graph), TransformMatchingTex(p0_label, p4_label), run_time=2)
        self.wait(1.5)

        # Degree 6
        p6_fn = lambda x: 1.0 - 0.5 * x**2 + (x**4) / 24.0 - (x**6) / 720.0
        p6_graph = axes.plot(p6_fn, x_range=[-4.2, 4.2], color=PURPLE_B, stroke_width=2.5)
        p6_label = MathTex(r"P_6(x) = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \frac{x^6}{6!}", color=PURPLE_B, font_size=28).to_corner(UR, buff=0.6)

        self.play(Transform(p0_graph, p6_graph), TransformMatchingTex(p0_label, p6_label), run_time=2.5)
        self.wait(2)

        # -------------------------------------------------------------
        # ACT 4: Formal Crystallization
        # -------------------------------------------------------------
        taylor_general = MathTex(
            r"T_n(x)",
            r"=",
            r"\sum_{k=0}^n \frac{f^{(k)}(c)}{k!} (x - c)^k",
            font_size=32
        ).to_corner(UL, buff=0.6)
        taylor_general[0].set_color(TEAL_C)
        taylor_general[2].set_color(YELLOW)

        box = SurroundingRectangle(taylor_general, color=BLUE_B, buff=0.15)

        self.play(Write(taylor_general), Create(box))
        self.wait(2.5)
