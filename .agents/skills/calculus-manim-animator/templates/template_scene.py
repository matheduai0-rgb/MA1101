"""
Template: Socratic Calculus Scene (MA1101)
Style: Grant Sanderson (3Blue1Brown)
"""

from manim import *

class SocraticCalculusTemplate(Scene):
    def construct(self):
        # -------------------------------------------------------------
        # ACT 1: The Pique / Puzzle (Hook curiosity with an inquiry)
        # -------------------------------------------------------------
        title = Text("What happens when change becomes instantaneous?", font_size=32)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))
        self.wait(1.5)

        # -------------------------------------------------------------
        # ACT 2: Visual Discovery (Introduce the geometric world)
        # -------------------------------------------------------------
        axes = Axes(
            x_range=[0, 6, 1],
            y_range=[0, 8, 2],
            x_length=8.5,
            y_length=5,
            axis_config={"color": GRAY_C}
        ).add_coordinates()
        axes.shift(DOWN * 0.4)

        curve_fn = lambda x: 0.25 * x**2 + 0.5
        curve = axes.plot(curve_fn, color=YELLOW, stroke_width=3)
        curve_label = MathTex(r"f(x) = \frac{1}{4}x^2 + \frac{1}{2}", color=YELLOW, font_size=30)
        curve_label.next_to(axes.c2p(4.5, curve_fn(4.5)), UP)

        self.play(Create(axes), Create(curve), FadeIn(curve_label), run_time=2)
        self.wait(1)

        # Setup dynamic inspection point
        x0 = 2.0
        dx_val = ValueTracker(2.0)

        # Secant group (hypotenuse and slope triangle)
        secant_group = always_redraw(lambda:
            axes.get_secant_slope_group(
                x=x0,
                dx=dx_val.get_value(),
                dx_line_color=GREEN_C,
                df_line_color=RED_C,
                secant_line_color=TEAL_C,
                secant_line_length=5.5,
                func=curve_fn
            )
        )

        pt_fixed = Dot(axes.c2p(x0, curve_fn(x0)), color=YELLOW)
        pt_moving = always_redraw(lambda:
            Dot(axes.c2p(x0 + dx_val.get_value(), curve_fn(x0 + dx_val.get_value())), color=TEAL_C)
        )

        self.play(Create(secant_group), FadeIn(pt_fixed), FadeIn(pt_moving))
        self.wait(1.5)

        # -------------------------------------------------------------
        # ACT 3: Socratic Pause (Pose the guiding question)
        # -------------------------------------------------------------
        socratic_question = Text(
            "As Δx shrinks towards 0, what does this line become?",
            font_size=28,
            color=TEAL_A
        ).to_edge(UP, buff=0.4)

        self.play(Transform(title, socratic_question))
        self.wait(1.5)

        # Animate dx approaching 0 (smooth, reflective pace)
        self.play(
            dx_val.animate.set_value(0.01),
            run_time=4.5,
            rate_func=smooth
        )
        self.wait(2)

        # -------------------------------------------------------------
        # ACT 4: Formal Crystallization (Connect intuition to notation)
        # -------------------------------------------------------------
        formal_formula = MathTex(
            r"\frac{df}{dx}",
            r"=",
            r"\lim_{\Delta x \to 0}",
            r"\frac{f(x+\Delta x) - f(x)}{\Delta x}",
            font_size=32
        )
        formal_formula.to_corner(UR, buff=0.6)
        formal_formula.set_color_by_tex(r"\frac{df}{dx}", TEAL_C)

        box = SurroundingRectangle(formal_formula, color=BLUE_B, buff=0.15)

        self.play(Write(formal_formula), Create(box))
        self.wait(2.5)
