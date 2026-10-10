"""
Template: Socratic Local Linearity & Derivative (MA1101)
Topic: Differentiability as Local Linearity via Camera Zoom
Style: Grant Sanderson (3Blue1Brown)
"""

from manim import *

class LocalLinearityZoomScene(MovingCameraScene):
    def construct(self):
        # -------------------------------------------------------------
        # ACT 1: The Pique / Puzzle
        # -------------------------------------------------------------
        title = Text("What does a curve look like under a microscope?", font_size=32)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        self.wait(1.5)

        axes = Axes(
            x_range=[-1, 5, 1],
            y_range=[-1, 7, 1],
            x_length=8.5,
            y_length=5.5,
            axis_config={"color": GRAY_C}
        ).add_coordinates()
        axes.shift(DOWN * 0.3)

        # Non-linear cubic curve
        f = lambda x: 0.25 * (x - 2)**3 - 0.7 * (x - 2) + 2.5
        curve = axes.plot(f, color=YELLOW, stroke_width=3)
        
        x0 = 2.0
        y0 = f(x0) # 2.5
        pt_target = axes.c2p(x0, y0)
        dot = Dot(pt_target, color=RED_C, radius=0.08)
        
        self.play(Create(axes), Create(curve), run_time=2)
        self.play(FadeIn(dot, scale=1.5))
        self.wait(1.5)

        # -------------------------------------------------------------
        # ACT 2: Visual Discovery (Zooming Deeply into the Point)
        # -------------------------------------------------------------
        # Add tangent line spanning full range
        f_prime_x0 = -0.7
        tangent_fn = lambda x: y0 + f_prime_x0 * (x - x0)
        tangent_line = axes.plot(tangent_fn, x_range=[0.5, 3.5], color=TEAL_C, stroke_width=2.5)

        self.play(FadeOut(title))

        # Camera zooms 15x into the target point
        self.play(
            self.camera.frame.animate.scale(0.12).move_to(pt_target),
            run_time=4.5,
            rate_func=smooth
        )
        self.wait(1.5)

        # -------------------------------------------------------------
        # ACT 3: Socratic Inversion
        # -------------------------------------------------------------
        # Reveal tangent right on top of the zoomed curve
        self.play(Create(tangent_line), run_time=2)
        self.wait(2)

        # Restore camera frame out
        self.play(
            self.camera.frame.animate.scale(1 / 0.12).move_to(ORIGIN),
            run_time=3.5,
            rate_func=smooth
        )
        self.wait(1.5)

        # -------------------------------------------------------------
        # ACT 4: Formal Crystallization (Linear Approximation)
        # -------------------------------------------------------------
        approx_formula = MathTex(
            r"L(x)",
            r"=",
            r"f(c)",
            r"+",
            r"f'(c)(x - c)",
            font_size=32
        ).to_corner(UR, buff=0.6)
        approx_formula[0].set_color(TEAL_C)
        approx_formula[4].set_color(YELLOW)

        box = SurroundingRectangle(approx_formula, color=BLUE_B, buff=0.15)
        note = Text("Best linear approximation at x = c", font_size=22, color=GRAY_B)
        note.next_to(box, DOWN, buff=0.2)

        self.play(Write(approx_formula), Create(box), FadeIn(note))
        self.wait(2.5)
