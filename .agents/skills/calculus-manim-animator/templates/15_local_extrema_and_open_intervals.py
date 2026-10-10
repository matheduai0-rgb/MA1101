"""
Animasi Sokratik: Ekstrem Lokal dan Ekstrem pada Selang Buka (MA1101)
Subtopik: 3.3 Ekstrem Lokal & Ekstrem pada Selang Buka (Teorema Titik Kritis Tunggal)
Bahasa: Indonesia
Gaya: Grant Sanderson (3Blue1Brown) & Pedagogi Sokratik
"""

from manim import *
import numpy as np

class LocalExtremaOpenIntervalScene(Scene):
    def construct(self):
        # -------------------------------------------------------------
        # AKSI 1: Tantangan Sokratik (The Pique / Conundrum)
        # -------------------------------------------------------------
        judul = Text(
            "Bagaimana mencari nilai minimum pada selang buka tanpa dinding batas?",
            font_size=23,
            color=WHITE
        ).to_edge(UP, buff=0.35)

        self.play(Write(judul), run_time=1.4)
        self.wait(1.0)

        # Sumbu koordinat di sisi kiri
        # Domain: (0, 5), Range: [0, 9]
        axes = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 10, 2],
            x_length=5.8,
            y_length=5.1,
            axis_config={"color": GRAY_C, "stroke_width": 2},
            tips=True
        ).add_coordinates()
        axes.shift(LEFT * 3.3 + DOWN * 0.3)

        # Fungsi kanonikal f(x) = x + 4/x pada (0, \infty)
        f = lambda x: x + 4.0 / x
        f_prime = lambda x: 1.0 - 4.0 / (x**2)
        f_double_prime = lambda x: 8.0 / (x**3)

        # Plot kurva pada selang (0.55, 4.8)
        curve = axes.plot(f, x_range=[0.55, 4.75], color=YELLOW, stroke_width=3.5)
        curve_label = MathTex(
            r"f(x) = x + \frac{4}{x}, \quad x \in (0, \infty)",
            color=YELLOW,
            font_size=19
        ).move_to(axes.c2p(3.1, 1.8))

        # Asimtot visual / indikator selang buka di x=0
        open_boundary_line = DashedLine(
            axes.c2p(0.05, 0),
            axes.c2p(0.05, 9.5),
            color=RED_C,
            stroke_width=2.0
        )
        open_boundary_label = Text("Tanpa Batas Kiri (x → 0⁺)", font_size=14, color=RED_C)
        open_boundary_label.next_to(open_boundary_line, UR, buff=0.1)

        self.play(Create(axes), run_time=1.0)
        self.play(
            Create(curve),
            Write(curve_label),
            Create(open_boundary_line),
            FadeIn(open_boundary_label),
            run_time=1.8
        )
        self.wait(1.2)

        # -------------------------------------------------------------
        # AKSI 2: Eksplorasi Visual (Lingkungan Buka & Uji Turunan)
        # -------------------------------------------------------------
        # Panel Interaktif di sisi kanan
        card_box = Rectangle(
            width=5.8,
            height=5.0,
            color=GRAY_D,
            stroke_width=1.5,
            fill_color="#0e1420",
            fill_opacity=0.9
        ).move_to(RIGHT * 3.4 + DOWN * 0.3)

        card_title = Text("1. Ekstrem Lokal & Uji Turunan", font_size=20, color=GOLD_B)
        card_title.move_to(RIGHT * 3.4 + UP * 1.9)

        # Lingkungan buka visual (open neighborhood) di sekitar x=2
        delta_val = 0.6
        rect_neighborhood = Rectangle(
            width=axes.x_axis.unit_size * (2 * delta_val),
            height=axes.y_axis.unit_size * 4.5,
            color=TEAL_E,
            fill_color=TEAL_E,
            fill_opacity=0.22,
            stroke_width=1.0
        ).move_to(axes.c2p(2.0, 4.5))

        neighborhood_lbl = Text("Lingkungan Buka (2-δ, 2+δ)", font_size=13, color=TEAL_B)
        neighborhood_lbl.next_to(rect_neighborhood, UP, buff=0.1)

        # Titik stasioner di (2, 4)
        c_pt = axes.c2p(2.0, 4.0)
        LuminousGold = "#F5BE3C"
        dot_c = Dot(c_pt, color=LuminousGold, radius=0.09)
        dot_c_label = MathTex(r"(2, 4)", color=GOLD_A, font_size=18).next_to(dot_c, DOWN, buff=0.15)

        self.play(
            FadeIn(card_box),
            Write(card_title),
            FadeIn(rect_neighborhood),
            FadeIn(neighborhood_lbl),
            FadeIn(dot_c),
            Write(dot_c_label),
            run_time=1.5
        )
        self.wait(1.0)

        # Nilai turunan & pelacakan tanda f'
        x_tracker = ValueTracker(1.1)

        # Garis singgung dinamis
        def get_tangent():
            xv = x_tracker.get_value()
            yv = f(xv)
            m = f_prime(xv)
            dx = 0.55
            p1 = axes.c2p(xv - dx, yv - dx * m)
            p2 = axes.c2p(xv + dx, yv + dx * m)
            col = RED_C if m < -0.15 else (GREEN_C if m > 0.15 else TEAL_A)
            return Line(p1, p2, color=col, stroke_width=3.5)

        tangent_line = always_redraw(get_tangent)
        probe_dot = always_redraw(lambda:
            Dot(axes.c2p(x_tracker.get_value(), f(x_tracker.get_value())), color=WHITE, radius=0.07)
        )

        # Telemetri di dalam kotak kanan
        txt_fprime = MathTex(r"f'(x) = 1 - \frac{4}{x^2}", font_size=20, color=WHITE).move_to(RIGHT * 3.4 + UP * 1.3)
        txt_crit = MathTex(r"f'(x) = 0 \implies x = 2 \quad (x > 0)", font_size=19, color=TEAL_A).move_to(RIGHT * 3.4 + UP * 0.8)

        status_test1 = always_redraw(lambda:
            VGroup(
                Text(
                    "x < 2:  f'(x) < 0 (Turun)",
                    font_size=16,
                    color=RED_C
                ) if x_tracker.get_value() < 1.85 else (
                    Text(
                        "x > 2:  f'(x) > 0 (Naik)",
                        font_size=16,
                        color=GREEN_C
                    ) if x_tracker.get_value() > 2.15 else
                    Text(
                        "x = 2:  f'(2) = 0 (Garis Mendatar)",
                        font_size=16,
                        color=GOLD_A
                    )
                )
            ).move_to(RIGHT * 3.4 + UP * 0.2)
        )

        test1_verdict = Text(
            "Perubahan Tanda: (-) ke (+) ⇒ Min Lokal!",
            font_size=16,
            color=GREEN_B
        ).move_to(RIGHT * 3.4 + DOWN * 0.3)

        # Uji turunan kedua
        txt_fdouble = MathTex(r"f''(x) = \frac{8}{x^3} \implies f''(2) = 1 > 0", font_size=19, color=TEAL_A).move_to(RIGHT * 3.4 + DOWN * 0.85)
        test2_verdict = Text(
            "Cekung ke Atas (∪) ⇒ Minimum Lokal",
            font_size=15,
            color=TEAL_B
        ).move_to(RIGHT * 3.4 + DOWN * 1.35)

        self.play(Write(txt_fprime), Write(txt_crit), run_time=1.2)
        self.play(Create(tangent_line), FadeIn(probe_dot), FadeIn(status_test1), run_time=1.0)
        self.wait(0.5)

        # Gerakkan x dari 1.1 ke 2.0 lalu ke 3.5
        self.play(x_tracker.animate.set_value(2.0), run_time=2.0, rate_func=smooth)
        self.wait(0.8)
        self.play(x_tracker.animate.set_value(3.5), run_time=2.0, rate_func=smooth)
        self.wait(0.8)

        self.play(FadeIn(test1_verdict), run_time=0.8)
        self.play(Write(txt_fdouble), FadeIn(test2_verdict), run_time=1.2)
        self.wait(1.5)

        # -------------------------------------------------------------
        # AKSI 3: Socratic Inversion (Tantangan Selang Buka)
        # -------------------------------------------------------------
        # Ganti pertanyaan di judul
        socratic_question = Text(
            "Mungkinkah kurva turun lebih rendah di tempat lain pada (0, ∞)?",
            font_size=22,
            color=GOLD_A
        ).to_edge(UP, buff=0.35)

        self.play(
            Transform(judul, socratic_question),
            FadeOut(card_title),
            FadeOut(rect_neighborhood),
            FadeOut(neighborhood_lbl),
            FadeOut(tangent_line),
            FadeOut(probe_dot),
            FadeOut(status_test1),
            FadeOut(test1_verdict),
            FadeOut(txt_fprime),
            FadeOut(txt_crit),
            FadeOut(txt_fdouble),
            FadeOut(test2_verdict),
            run_time=1.2
        )
        self.wait(2.0)  # Socratic pause

        # Kartu kanan untuk Teorema Titik Kritis Tunggal
        card_title2 = Text("Teorema Titik Kritis Tunggal", font_size=19, color=GOLD_B).move_to(RIGHT * 3.4 + UP * 1.9)
        self.play(Write(card_title2), run_time=0.8)

        arg1 = Text(
            "Untuk turun lebih rendah dari f(2) = 4,\nkurva yang sedang naik HARUS berbalik arah.",
            font_size=14,
            color=WHITE,
            line_spacing=1.2
        ).move_to(RIGHT * 3.4 + UP * 1.1)

        arg2 = Text(
            "Namun, berbalik arah mewajibkan\nadanya titik kritis BARU (f' = 0).",
            font_size=14,
            color=RED_B,
            line_spacing=1.2
        ).move_to(RIGHT * 3.4 + UP * 0.25)

        arg3 = Text(
            "Karena x = 2 adalah SATU-SATUNYA\ntitik kritis di (0, ∞), kurva TIDAK BISA\npernah berbalik turun lagi!",
            font_size=14,
            color=GREEN_A,
            line_spacing=1.2
        ).move_to(RIGHT * 3.4 + DOWN * 0.7)

        self.play(Write(arg1), run_time=1.4)
        self.wait(0.8)
        self.play(Write(arg2), run_time=1.4)
        self.wait(0.8)
        self.play(Write(arg3), run_time=1.6)
        self.wait(1.5)

        # -------------------------------------------------------------
        # AKSI 4: Formal Crystallization (Limit Ujung & Minimum Mutlak)
        # -------------------------------------------------------------
        final_header = Text(
            "Teorema Titik Kritis Tunggal: Menjamin Ekstrem Mutlak pada Selang Buka",
            font_size=21,
            color=GOLD_A
        ).to_edge(UP, buff=0.35)

        # Panah limit di kurva
        arrow_left_limit = CurvedArrow(
            axes.c2p(1.1, 5.5),
            axes.c2p(0.65, 8.0),
            color=RED_C,
            angle=-TAU/8
        )
        lbl_lim_0 = MathTex(r"\lim_{x \to 0^+} f(x) = +\infty", font_size=17, color=RED_C)
        lbl_lim_0.next_to(arrow_left_limit, UR, buff=0.08)

        arrow_right_limit = CurvedArrow(
            axes.c2p(3.2, 5.0),
            axes.c2p(4.4, 6.0),
            color=BLUE_C,
            angle=-TAU/12
        )
        lbl_lim_inf = MathTex(r"\lim_{x \to \infty} f(x) = +\infty", font_size=17, color=BLUE_C)
        lbl_lim_inf.next_to(arrow_right_limit, UR, buff=0.08)

        self.play(
            Transform(judul, final_header),
            Create(arrow_left_limit),
            Write(lbl_lim_0),
            Create(arrow_right_limit),
            Write(lbl_lim_inf),
            run_time=1.8
        )
        self.wait(1.0)

        # Transisi ke Kesimpulan Mutlak di seluruh panel kanan
        conclusion_box = RoundedRectangle(
            corner_radius=0.16,
            width=5.5,
            height=3.8,
            color=GOLD_A,
            stroke_width=2.0,
            fill_color="#121824",
            fill_opacity=0.96
        ).move_to(RIGHT * 3.4 + DOWN * 0.3)

        conclusion_badge = Text(
            "★ SINTESIS & KESIMPULAN MUTLAK ★",
            font_size=14,
            weight=BOLD,
            color=GOLD_A
        ).move_to(RIGHT * 3.4 + UP * 1.25)

        c_div = Line(LEFT * 2.4, RIGHT * 2.4, color=GRAY_D, stroke_width=1).move_to(RIGHT * 3.4 + UP * 0.95)

        c_p1 = Text("1. Kontinu pada domain buka (0, ∞)", font_size=13, color=WHITE).move_to(RIGHT * 3.4 + UP * 0.65)
        c_p2 = MathTex(r"2. \text{Titik Kritis Tunggal: } x = 2 \ (f'(2) = 0)", font_size=15, color=TEAL_A).move_to(RIGHT * 3.4 + UP * 0.25)
        c_p3 = Text("3. Uji Turunan: (-) ke (+) ⇒ Min Lokal", font_size=13, color=GREEN_B).move_to(RIGHT * 3.4 + DOWN * 0.15)
        SoftGray = "#C8D2E1"
        c_p4 = MathTex(r"4. \lim_{x \to 0^+} f(x) = \infty \quad \text{dan} \quad \lim_{x \to \infty} f(x) = \infty", font_size=14, color=SoftGray).move_to(RIGHT * 3.4 + DOWN * 0.55)

        result_pill = RoundedRectangle(
            corner_radius=0.12,
            width=5.1,
            height=0.8,
            color=GOLD_B,
            fill_color="#1e293b",
            fill_opacity=0.9,
            stroke_width=1.5
        ).move_to(RIGHT * 3.4 + DOWN * 1.25)

        result_txt = MathTex(
            r"f(2) = 4 \implies \mathbf{MINIMUM\ MUTLAK\ di\ (0, \infty)}",
            font_size=16,
            color=GOLD_A
        ).move_to(RIGHT * 3.4 + DOWN * 1.25)

        self.play(
            FadeOut(card_title2),
            FadeOut(arg1),
            FadeOut(arg2),
            FadeOut(arg3),
            FadeIn(conclusion_box),
            Write(conclusion_badge),
            Create(c_div),
            Write(c_p1),
            Write(c_p2),
            Write(c_p3),
            Write(c_p4),
            FadeIn(result_pill),
            Write(result_txt),
            Flash(dot_c, color=GOLD_A, flash_radius=0.45, num_lines=12),
            run_time=2.2
        )
        self.wait(3.0)
