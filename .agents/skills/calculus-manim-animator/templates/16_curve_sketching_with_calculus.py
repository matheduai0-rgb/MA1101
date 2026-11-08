"""
Animasi Sokratik: Grafik Fungsi dengan Menggunakan Kalkulus (MA1101)
Subtopik: 3.5 Grafik Fungsi dengan Menggunakan Kalkulus (Asimtot, Kemonotonan & Kecekungan)
Bahasa: Indonesia
Gaya: Grant Sanderson (3Blue1Brown) & Pedagogi Sokratik
"""

from manim import *
import numpy as np

class CurveSketchingScene(Scene):
    def construct(self):
        # -------------------------------------------------------------
        # AKSI 1: Tantangan Sokratik (The Pique / Conundrum)
        # -------------------------------------------------------------
        judul = Text(
            "Bagaimana melukiskan kurva tanpa menebak ribuan titik?",
            font_size=23,
            color=WHITE
        ).to_edge(UP, buff=0.35)

        self.play(Write(judul), run_time=1.3)
        self.wait(0.8)

        # Sumbu koordinat di sisi kiri
        axes = Axes(
            x_range=[-4.2, 4.2, 1],
            y_range=[-3, 6, 1],
            x_length=6.3,
            y_length=5.1,
            axis_config={"color": GRAY_C, "stroke_width": 2},
            tips=True
        ).add_coordinates()
        axes.shift(LEFT * 3.3 + DOWN * 0.25)

        # Fungsi kanonikal f(x) = 2x^2 / (x^2 - 1)
        f = lambda x: (2.0 * x**2) / (x**2 - 1.0)
        f_prime = lambda x: (-4.0 * x) / ((x**2 - 1.0)**2)

        curve_eq = MathTex(
            r"f(x) = \frac{2x^2}{x^2 - 1}",
            color=YELLOW,
            font_size=24
        ).move_to(LEFT * 3.3 + UP * 2.5)

        self.play(Create(axes), Write(curve_eq), run_time=1.4)

        # Titik-titik sampel acak (Ilusi Plotting Titik)
        sample_xs = [-3.0, -2.0, 0.0, 2.0, 3.0]
        sample_dots = VGroup(*[
            Dot(axes.c2p(xs, f(xs)), color=GOLD_B, radius=0.08)
            for xs in sample_xs
        ])
        sample_labels = Text(
            "Hanya menghubungkan titik sampel?\nBahaya diskontinuitas!",
            font_size=15,
            color=ORANGE,
            line_spacing=1.2
        ).move_to(LEFT * 3.3 + DOWN * 1.8)

        self.play(FadeIn(sample_dots, lag_ratio=0.15), run_time=1.0)
        self.play(FadeIn(sample_labels), run_time=0.9)
        self.wait(1.5)

        self.play(FadeOut(sample_dots), FadeOut(sample_labels), run_time=0.8)

        # -------------------------------------------------------------
        # AKSI 2: Membangun Kerangka Tulang Punggung (Scaffolding & Asimtot)
        # -------------------------------------------------------------
        sub_judul = Text(
            "Kalkulus menyingkap kerangka sejati: Asimtot & Titik Kunci",
            font_size=19,
            color=TEAL_C
        ).to_edge(UP, buff=0.35)
        self.play(Transform(judul, sub_judul), run_time=1.0)

        # Asimtot Tegak: x = -1 dan x = 1 (Garis putus-putus merah)
        va_left = DashedLine(
            axes.c2p(-1, -2.8), axes.c2p(-1, 5.8),
            color=RED_C, stroke_width=2.5, dash_length=0.1
        )
        va_right = DashedLine(
            axes.c2p(1, -2.8), axes.c2p(1, 5.8),
            color=RED_C, stroke_width=2.5, dash_length=0.1
        )
        va_lbl_left = MathTex(r"x = -1", color=RED_C, font_size=17).next_to(va_left, UP, buff=0.1)
        va_lbl_right = MathTex(r"x = 1", color=RED_C, font_size=17).next_to(va_right, UP, buff=0.1)

        # Asimtot Datar: y = 2 (Garis putus-putus cyan/teal)
        ha = DashedLine(
            axes.c2p(-4.1, 2), axes.c2p(4.1, 2),
            color=TEAL_C, stroke_width=2.5, dash_length=0.12
        )
        ha_lbl = MathTex(r"y = 2", color=TEAL_C, font_size=18).next_to(axes.c2p(-3.8, 2), UP, buff=0.08)

        # Titik potong & stasioner (0,0)
        origin_dot = Dot(axes.c2p(0, 0), color=GOLD_B, radius=0.09)
        origin_lbl = MathTex(r"(0,0)", color=GOLD_B, font_size=16).next_to(origin_dot, DOWN + RIGHT, buff=0.1)

        self.play(
            Create(va_left), Create(va_right),
            Write(va_lbl_left), Write(va_lbl_right),
            run_time=1.3
        )
        self.play(
            Create(ha), Write(ha_lbl),
            Create(origin_dot), Write(origin_lbl),
            run_time=1.2
        )
        self.wait(1.0)

        # -------------------------------------------------------------
        # AKSI 3: Panel Telemetri Kalkulus & Socratic Inversion
        # -------------------------------------------------------------
        # Kartu panel di sisi kanan
        card_box = Rectangle(
            width=5.8,
            height=5.1,
            color=GRAY_D,
            stroke_width=1.5,
            fill_color="#0e1420",
            fill_opacity=0.92
        ).move_to(RIGHT * 3.4 + DOWN * 0.25)

        card_title = Text("Telemetri Turunan", font_size=21, color=GOLD_B).move_to(RIGHT * 3.4 + UP * 1.95)

        f_prime_tex = MathTex(
            r"f'(x) = \frac{-4x}{(x^2 - 1)^2}",
            color=BLUE_B,
            font_size=20
        ).move_to(RIGHT * 3.4 + UP * 1.35)

        f_double_prime_tex = MathTex(
            r"f''(x) = \frac{12x^2 + 4}{(x^2 - 1)^3}",
            color=PURPLE_B,
            font_size=20
        ).move_to(RIGHT * 3.4 + UP * 0.75)

        divider = Line(LEFT * 2.5, RIGHT * 2.5, color=GRAY_D, stroke_width=1).move_to(RIGHT * 3.4 + UP * 0.35)

        # Matriks Analisis Interval
        row1 = Text("• x < -1 : Naik & Cekung Atas (∪)", font_size=15, color=GREEN_C).move_to(RIGHT * 3.4 + DOWN * 0.1)
        row2 = Text("• -1 < x < 0 : Naik & Cekung Bawah (∩)", font_size=15, color=YELLOW).move_to(RIGHT * 3.4 + DOWN * 0.55)
        row3 = Text("• 0 < x < 1 : Turun & Cekung Bawah (∩)", font_size=15, color=ORANGE).move_to(RIGHT * 3.4 + DOWN * 1.0)
        row4 = Text("• x > 1 : Turun & Cekung Atas (∪)", font_size=15, color=PINK).move_to(RIGHT * 3.4 + DOWN * 1.45)
        socratic_prompt = Text("Puncak lokal di (0,0) | Tanpa titik belok!", font_size=15, color=GOLD_B).move_to(RIGHT * 3.4 + DOWN * 1.95)

        self.play(
            FadeIn(card_box),
            Write(card_title),
            Write(f_prime_tex),
            Write(f_double_prime_tex),
            Create(divider),
            run_time=1.5
        )
        self.play(
            FadeIn(row1), FadeIn(row2), FadeIn(row3), FadeIn(row4),
            FadeIn(socratic_prompt),
            run_time=2.0
        )
        self.wait(2.0)

        # -------------------------------------------------------------
        # AKSI 4: Kristalisasi Formal & Penarikan Tiga Cabang Kurva
        # -------------------------------------------------------------
        final_judul = Text(
            "Sintesis: Kurva Mulus Terkunci oleh Analisis Turunan",
            font_size=20,
            color=GREEN_B
        ).to_edge(UP, buff=0.35)
        self.play(Transform(judul, final_judul), run_time=0.9)

        # Tiga cabang kurva:
        # Cabang Kiri: (-4.1, -1.15)
        branch_left = axes.plot(
            f, x_range=[-4.1, -1.15, 0.02],
            color=YELLOW, stroke_width=3.5
        )
        # Cabang Tengah: (-0.86, 0.86)
        branch_mid = axes.plot(
            f, x_range=[-0.86, 0.86, 0.02],
            color=YELLOW, stroke_width=3.5
        )
        # Cabang Kanan: (1.15, 4.1)
        branch_right = axes.plot(
            f, x_range=[1.15, 4.1, 0.02],
            color=YELLOW, stroke_width=3.5
        )

        self.play(
            Create(branch_left),
            Create(branch_mid),
            Create(branch_right),
            run_time=3.2,
            rate_func=smooth
        )
        self.wait(1.0)

        # Tracer dinamis: garis singgung bergerak di cabang tengah
        x_track = ValueTracker(-0.7)

        def get_tracer_tangent():
            xv = x_track.get_value()
            yv = f(xv)
            m = f_prime(xv)
            dx = 0.4
            p1 = axes.c2p(xv - dx, yv - dx * m)
            p2 = axes.c2p(xv + dx, yv + dx * m)
            return Line(p1, p2, color=TEAL_A, stroke_width=3.0)

        tangent_line = always_redraw(get_tracer_tangent)
        tangent_dot = always_redraw(lambda:
            Dot(axes.c2p(x_track.get_value(), f(x_track.get_value())), color=RED_C, radius=0.08)
        )

        self.play(Create(tangent_line), Create(tangent_dot), run_time=0.8)
        self.play(
            x_track.animate.set_value(0.7),
            run_time=3.5,
            rate_func=linear
        )
        self.wait(1.0)

        # Puncak lokal di (0,0) disorot saat garis singgung horizontal di x=0
        self.play(x_track.animate.set_value(0.0), run_time=1.0)
        horiz_highlight = MathTex(r"f'(0) = 0 \implies \text{Maks Lokal}", color=GOLD_B, font_size=18).move_to(axes.c2p(0, 1.2))
        self.play(Write(horiz_highlight), Flash(origin_dot, color=GOLD_B), run_time=1.2)
        self.wait(2.5)
