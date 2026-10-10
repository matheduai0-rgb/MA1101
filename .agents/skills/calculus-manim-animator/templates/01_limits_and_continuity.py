"""
Template: Socratic Limit & Epsilon-Delta Challenge (MA1101)
Topic: Definition of a Limit (lim x->c f(x) = L)
Style: Grant Sanderson (3Blue1Brown)
"""

from manim import *

class EpsilonDeltaLimitScene(Scene):
    def construct(self):
        # -------------------------------------------------------------
        # ACT 1: The Pique / Puzzle
        # -------------------------------------------------------------
        title = Text("How do we rigorously trap a limit?", font_size=32)
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

        f = lambda x: 0.2 * x**2 + 1.2
        curve = axes.plot(f, color=YELLOW, stroke_width=3)
        
        c_val = 3.0
        L_val = f(c_val) # 3.0
        pt_target = axes.c2p(c_val, L_val)
        dot_target = Dot(pt_target, color=YELLOW, radius=0.07)
        label_L = MathTex(r"L", color=YELLOW, font_size=28).next_to(axes.c2p(0, L_val), LEFT)
        label_c = MathTex(r"c", color=YELLOW, font_size=28).next_to(axes.c2p(c_val, 0), DOWN)

        self.play(Create(axes), Create(curve), FadeIn(dot_target), Write(label_L), Write(label_c), run_time=2)
        self.wait(1.5)

        # -------------------------------------------------------------
        # ACT 2: Visual Discovery (The Epsilon-Delta Game)
        # -------------------------------------------------------------
        epsilon_val = 0.8
        delta_val = 0.6

        # Horizontal epsilon target band
        eps_band = axes.get_horizontal_line(axes.c2p(6, L_val + epsilon_val), color=BLUE_B, stroke_width=1.5).set_stroke(opacity=0.6)
        eps_band_low = axes.get_horizontal_line(axes.c2p(6, L_val - epsilon_val), color=BLUE_B, stroke_width=1.5).set_stroke(opacity=0.6)
        eps_area = Polygon(
            axes.c2p(0, L_val - epsilon_val),
            axes.c2p(6, L_val - epsilon_val),
            axes.c2p(6, L_val + epsilon_val),
            axes.c2p(0, L_val + epsilon_val),
            color=BLUE_E,
            fill_opacity=0.25,
            stroke_width=0
        )
        eps_text = MathTex(r"L \pm \varepsilon", color=BLUE_C, font_size=26).next_to(axes.c2p(0, L_val + epsilon_val), LEFT)

        self.play(FadeIn(eps_area), Create(eps_band), Create(eps_band_low), Write(eps_text))
        self.wait(1.5)

        # Vertical delta response band
        delta_area = Polygon(
            axes.c2p(c_val - delta_val, 0),
            axes.c2p(c_val + delta_val, 0),
            axes.c2p(c_val + delta_val, 7),
            axes.c2p(c_val - delta_val, 7),
            color=GREEN_E,
            fill_opacity=0.25,
            stroke_width=0
        )
        delta_text = MathTex(r"c \pm \delta", color=GREEN_C, font_size=26).next_to(axes.c2p(c_val, 0), DOWN, buff=0.8)

        self.play(FadeIn(delta_area), Write(delta_text))
        self.wait(1.5)

        # -------------------------------------------------------------
        # ACT 3: Socratic Inversion
        # -------------------------------------------------------------
        socratic_question = Text(
            "Can we always find a δ window narrow enough to stay inside ε?",
            font_size=26,
            color=TEAL_A
        ).to_edge(UP, buff=0.4)

        self.play(Transform(title, socratic_question))
        self.wait(2)

        # Shrink epsilon to demonstrate the challenge
        new_eps = 0.35
        new_delta = 0.25
        new_eps_area = Polygon(
            axes.c2p(0, L_val - new_eps),
            axes.c2p(6, L_val - new_eps),
            axes.c2p(6, L_val + new_eps),
            axes.c2p(0, L_val + new_eps),
            color=BLUE_E,
            fill_opacity=0.35,
            stroke_width=0
        )
        new_delta_area = Polygon(
            axes.c2p(c_val - new_delta, 0),
            axes.c2p(c_val + new_delta, 0),
            axes.c2p(c_val + new_delta, 7),
            axes.c2p(c_val - new_delta, 7),
            color=GREEN_E,
            fill_opacity=0.35,
            stroke_width=0
        )

        self.play(
            Transform(eps_area, new_eps_area),
            Transform(delta_area, new_delta_area),
            run_time=3,
            rate_func=smooth
        )
        self.wait(2)

        # -------------------------------------------------------------
        # ACT 4: Formal Crystallization
        # -------------------------------------------------------------
        formal_def = MathTex(
            r"\forall \varepsilon > 0,\; \exists \delta > 0 \;\text{such that}",
            r"0 < |x - c| < \delta \implies |f(x) - L| < \varepsilon",
            font_size=28
        ).to_corner(UR, buff=0.5)
        formal_def[0].set_color(BLUE_C)
        formal_def[1].set_color(GREEN_C)

        box = SurroundingRectangle(formal_def, color=WHITE, buff=0.15, stroke_width=1.5)

        self.play(Write(formal_def), Create(box))
        self.wait(2.5)
