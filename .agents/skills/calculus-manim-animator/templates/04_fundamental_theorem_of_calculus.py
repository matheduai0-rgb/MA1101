"""
Template: Socratic Fundamental Theorem of Calculus (MA1101)
Topic: FTC Part 1 - Why the derivative of accumulation is the rate curve
Style: Grant Sanderson (3Blue1Brown)
"""

from manim import *

class SocraticFTCScene(Scene):
    def construct(self):
        # -------------------------------------------------------------
        # ACT 1: The Pique / Puzzle
        # -------------------------------------------------------------
        title = Text("Why are slopes and areas inverse operations?", font_size=30)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))
        self.wait(1.5)

        axes = Axes(
            x_range=[0, 7, 1],
            y_range=[0, 6, 1],
            x_length=8.5,
            y_length=5,
            axis_config={"color": GRAY_C}
        ).add_coordinates()
        axes.shift(DOWN * 0.4)

        f = lambda t: 0.1 * t**2 + 1.2
        graph = axes.plot(f, color=YELLOW, stroke_width=3)
        graph_label = MathTex(r"f(t)", color=YELLOW, font_size=28).next_to(axes.c2p(5.5, f(5.5)), UP)

        self.play(Create(axes), Create(graph), FadeIn(graph_label), run_time=2)
        self.wait(1)

        # -------------------------------------------------------------
        # ACT 2: Visual Discovery (Accumulating Area A(x))
        # -------------------------------------------------------------
        x_val = ValueTracker(3.2)
        dx_constant = 0.4

        # Main accumulation area from 1 to x
        acc_area = always_redraw(lambda:
            axes.get_area(graph, x_range=[1.0, x_val.get_value()], color=BLUE_E, opacity=0.5)
        )
        
        # Marginal added strip between x and x + dx
        marginal_strip = always_redraw(lambda:
            axes.get_area(
                graph,
                x_range=[x_val.get_value(), x_val.get_value() + dx_constant],
                color=RED_C,
                opacity=0.75
            )
        )

        area_label = MathTex(r"A(x) = \int_a^x f(t)\,dt", color=BLUE_C, font_size=26)
        area_label.to_corner(UL, buff=0.6)

        self.play(FadeIn(acc_area), FadeIn(marginal_strip), Write(area_label))
        self.wait(1.5)

        # -------------------------------------------------------------
        # ACT 3: Socratic Inversion (The Marginal Strip's Area)
        # -------------------------------------------------------------
        socratic_question = Text(
            "What is the area of this thin added strip dA?",
            font_size=26,
            color=TEAL_A
        ).to_edge(UP, buff=0.4)

        self.play(Transform(title, socratic_question))
        self.wait(1.5)

        strip_label = MathTex(
            r"dA \approx f(x) \cdot dx",
            font_size=28,
            color=RED_C
        ).to_corner(UR, buff=0.6)

        self.play(Write(strip_label))
        self.wait(1.5)

        rearranged = MathTex(
            r"\frac{dA}{dx} \approx f(x)",
            font_size=30,
            color=RED_C
        ).next_to(strip_label, DOWN, buff=0.3)

        self.play(Write(rearranged))
        self.wait(1.5)

        # Animate x shifting smoothly forward
        self.play(x_val.animate.set_value(5.0), run_time=3.5, rate_func=smooth)
        self.wait(1.5)

        # -------------------------------------------------------------
        # ACT 4: Formal Crystallization (FTC Part 1)
        # -------------------------------------------------------------
        ftc_formula = MathTex(
            r"\frac{d}{dx} \left[ \int_a^x f(t)\,dt \right]",
            r"=",
            r"f(x)",
            font_size=32
        ).to_corner(UR, buff=0.6)
        ftc_formula[0].set_color(BLUE_C)
        ftc_formula[2].set_color(YELLOW)

        box = SurroundingRectangle(ftc_formula, color=BLUE_B, buff=0.15)
        theorem_title = Text("Fundamental Theorem of Calculus (Part 1)", font_size=20, color=GRAY_B)
        theorem_title.next_to(box, DOWN, buff=0.2)

        self.play(
            FadeOut(strip_label),
            FadeOut(rearranged),
            Write(ftc_formula),
            Create(box),
            FadeIn(theorem_title)
        )
        self.wait(2.5)
