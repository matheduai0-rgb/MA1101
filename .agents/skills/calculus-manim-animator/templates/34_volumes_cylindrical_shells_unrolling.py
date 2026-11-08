"""
Template: Volume Benda Putar — Metode Kulit Tabung & Pembentangan (MA1101 Subtopik 5.3)
Subtopik: 5.3 Volume Benda Putar: Metode Kulit Tabung (Cylindrical Shells)
Bahasa: Indonesia
Gaya: Grant Sanderson (3Blue1Brown) & Metode Sokratik
Deskripsi:
  Visualisasi 4 babak untuk Metode Kulit Tabung (Cylindrical Shells) ketika daerah di bawah
  kurva kubik y = 2x^2 - x^3 pada [0, 2] diputar mengelilingi sumbu-y:
    - Mengapa Metode Cincin (Δy tegak lurus sumbu-y) gagal? Karena pias mendatar memotong
      kurva yang sama di dua titik dan persamaan x^3 - 2x^2 + y = 0 sulit diinvers!
    - Dengan mengambil pias tegak (Δx SEJAJAR sumbu-y) pada posisi x, perputaran 360 derajat
      mengelilingi sumbu-y menyapu sebuah kulit tabung berjari-jari r = x, tinggi h = f(x),
      dan tebal Δx.
    - Jika kulit tabung dibelah dan dibentangkan menjadi balok persegi panjang:
        Panjang = keliling = 2*pi*x,  Tinggi = f(x),  Tebal = Δx
        => ΔV ≈ 2*pi * x * f(x) * Δx  =>  V = 2*pi * int_0^2 x*(2x^2 - x^3) dx = 16*pi/5.

  Babak 1 (Dilema)      : Memutar y = 2x^2 - x^3 mengelilingi sumbu-y: mengapa pias mendatar (Δy)
                          terjebak pada kurva yang sama?
  Babak 2 (Eksplorasi)  : Pias tegak (Δx sejajar sumbu-y) menyapu kulit tabung 3D di panel kiri,
                          berpasangan secara reaktif dengan lempeng balok hasil pembentangan
                          (panjang 2*pi*x, tinggi f(x)) di panel kanan.
  Babak 3 (Inversi)     : Mengapa pengali depan kulit tabung adalah 2*pi (bukan pi), dan mengapa
                          jari-jari x berpangkat satu (bukan x^2)?
  Babak 4 (Kristalisasi): Rumus umum Metode Kulit Tabung dV = 2*pi * r * h * dr dan evaluasi eksak.

Render:
  ../scripts/preview_scene.sh 34_volumes_cylindrical_shells_unrolling.py CylindricalShellsUnrollingScene -s
"""

from manim import *
import numpy as np


CARD_BG = "#141B28"


def f_cubic(x):
    return 2.0 * (x ** 2) - (x ** 3)


class CylindricalShellsUnrollingScene(Scene):
    def construct(self):
        # =============================================================
        # TATA LETAK: Kiri = Kulit Tabung Mengelilingi Sumbu-y, Kanan = Balok Bentangan
        # =============================================================
        ax = Axes(
            x_range=[-2.2, 2.2, 1],
            y_range=[-0.25, 1.65, 0.5],
            x_length=5.5,
            y_length=3.35,
            axis_config={"color": GRAY_C, "stroke_width": 1.6, "include_tip": False},
        ).add_coordinates(font_size=12)
        ax.move_to(LEFT * 3.45 + UP * 0.2)

        hdr_left = Tex(
            r"\textbf{1. Kulit Tabung pada Sumbu-$y$ ($\Delta x \parallel$ Sumbu Putar)}",
            font_size=18, color=YELLOW,
        ).next_to(ax, UP, buff=0.1)

        hdr_right = Tex(
            r"\textbf{2. ``Iris \& Bentangkan'' Menjadi Balok Rata}",
            font_size=18, color=TEAL_C,
        ).move_to(RIGHT * 3.45 + UP * 2.1)

        curve_r = ax.plot(f_cubic, x_range=[0.0, 2.0], color=YELLOW, stroke_width=3.6)
        curve_l = DashedVMobject(
            ax.plot(lambda x: f_cubic(-x), x_range=[-2.0, 0.0], color=YELLOW_E, stroke_width=2.2),
            num_dashes=26,
        )
        area_r = ax.get_area(curve_r, x_range=[0.0, 2.0], color=BLUE_D, opacity=0.35)
        lbl_f = MathTex(r"y = 2x^2 - x^3", font_size=17, color=YELLOW).move_to(ax.c2p(1.42, 1.42))

        # =============================================================
        # BABAK 1: Dilema - Mengapa pias mendatar (Δy) gagal pada y = 2x^2 - x^3?
        # =============================================================
        judul = Text(
            "Memutar y = 2x² - x³ mengelilingi sumbu-y: Mengapa Metode Cincin (Δy) macet?",
            font_size=19, color=WHITE,
        ).to_edge(UP, buff=0.18)

        self.play(Write(judul), run_time=1.3)
        self.play(Create(ax), Write(hdr_left), Write(hdr_right), run_time=1.0)
        self.play(Create(curve_r), FadeIn(area_r), Write(lbl_f), Create(curve_l), run_time=1.3)

        # Tunjukkan sejenak pias mendatar Δy yang terjebak pada kurva yang sama
        bad_dy = Line(ax.c2p(0.82, 0.8), ax.c2p(1.76, 0.8), color=RED_B, stroke_width=5.0)
        bad_lbl = Tex(
            r"Pias $\Delta y$ memotong kurva yang sama! ($x = g(y)$ sulit dicari)",
            font_size=15, color=RED_B,
        ).next_to(ax, DOWN, buff=0.14)
        self.play(Create(bad_dy), FadeIn(bad_lbl), run_time=1.1)
        self.wait(0.9)
        self.play(FadeOut(bad_dy), FadeOut(bad_lbl), run_time=0.6)

        # =============================================================
        # BABAK 2: Eksplorasi - Pias Tegak Menyapu Kulit Tabung & Dibentangkan
        # =============================================================
        judul2 = Text(
            "Solusi: Gunakan pias tegak (Δx ∥ sumbu-y) yang menyapu Kulit Tabung berjari-jari r = x!",
            font_size=18, color=TEAL_A,
        ).to_edge(UP, buff=0.18)
        self.play(Transform(judul, judul2), run_time=0.9)

        x_tr = ValueTracker(0.65)

        def make_shell_3d(x_val):
            h_val = f_cubic(x_val)
            w_rad = abs(ax.c2p(x_val, 0)[0] - ax.c2p(0, 0)[0])
            y_bot = ax.c2p(0, 0)[1]
            y_top = ax.c2p(0, h_val)[1]
            x_c = ax.c2p(0, 0)[0]

            # Dinding silinder kiri dan kanan + elips tutup atas & bawah
            body = Rectangle(
                width=max(0.06, 2 * w_rad),
                height=max(0.04, y_top - y_bot),
                fill_color=GOLD_B, fill_opacity=0.28,
                stroke_color=GOLD_B, stroke_width=1.6,
            ).move_to([x_c, (y_top + y_bot) / 2, 0])

            bot_el = Ellipse(
                width=max(0.06, 2 * w_rad), height=0.22,
                fill_opacity=0.0, stroke_color=GOLD_E, stroke_width=1.5,
            ).move_to([x_c, y_bot, 0])

            top_el = Ellipse(
                width=max(0.06, 2 * w_rad), height=0.24,
                fill_color=GOLD_B, fill_opacity=0.55,
                stroke_color=WHITE, stroke_width=1.8,
            ).move_to([x_c, y_top, 0])

            top_hole = Ellipse(
                width=max(0.04, 2 * w_rad - 0.16), height=0.15,
                fill_color=CARD_BG, fill_opacity=0.92,
                stroke_color=TEAL_B, stroke_width=1.3,
            ).move_to([x_c, y_top, 0])

            strip_r = Rectangle(
                width=0.09, height=max(0.04, y_top - y_bot),
                fill_color=YELLOW, fill_opacity=0.85,
                stroke_color=WHITE, stroke_width=1.2,
            ).move_to([ax.c2p(x_val, 0)[0], (y_top + y_bot) / 2, 0])

            r_arrow = DoubleArrow(
                ax.c2p(0, -0.12), ax.c2p(x_val, -0.12),
                color=TEAL_A, buff=0, stroke_width=2.2, max_tip_length_to_length_ratio=0.18,
            )
            r_tag = MathTex(r"r = x", font_size=15, color=TEAL_A).next_to(r_arrow, DOWN, buff=0.04)

            return VGroup(body, bot_el, top_el, top_hole, strip_r, r_arrow, r_tag)

        def make_unrolled_slab(x_val):
            h_val = f_cubic(x_val)
            # Skala visual balok hasil pembentangan di panel kanan
            slab_w = max(0.4, 2.2 * x_val)
            slab_h = max(0.15, 1.55 * h_val)
            center = np.array([3.45, 0.25, 0.0])

            rect = Rectangle(
                width=slab_w, height=slab_h,
                fill_color=TEAL_C, fill_opacity=0.48,
                stroke_color=WHITE, stroke_width=2.0,
            ).move_to(center)

            # Efek 3D ketebalan Δx
            depth = np.array([0.16, 0.12, 0.0])
            top_face = Polygon(
                rect.get_corner(UL), rect.get_corner(UR),
                rect.get_corner(UR) + depth, rect.get_corner(UL) + depth,
                fill_color=TEAL_B, fill_opacity=0.65, stroke_color=WHITE, stroke_width=1.4,
            )
            side_face = Polygon(
                rect.get_corner(UR), rect.get_corner(DR),
                rect.get_corner(DR) + depth, rect.get_corner(UR) + depth,
                fill_color=TEAL_D, fill_opacity=0.75, stroke_color=WHITE, stroke_width=1.4,
            )

            lbl_len = MathTex(
                rf"\text{{Keliling}} = 2\pi r = 2\pi x",
                font_size=17, color=GOLD_B,
            ).next_to(rect, DOWN, buff=0.12)

            lbl_h = MathTex(
                r"h = f(x)", font_size=16, color=YELLOW
            ).next_to(rect, LEFT, buff=0.1)

            lbl_dx = MathTex(
                r"\Delta x", font_size=15, color=WHITE
            ).next_to(side_face, RIGHT, buff=0.06)

            return VGroup(rect, top_face, side_face, lbl_len, lbl_h, lbl_dx)

        shell_dyn = always_redraw(lambda: make_shell_3d(x_tr.get_value()))
        slab_dyn = always_redraw(lambda: make_unrolled_slab(x_tr.get_value()))

        self.add(shell_dyn, slab_dyn)
        self.play(x_tr.animate.set_value(1.75), run_time=2.6, rate_func=smooth)
        self.play(x_tr.animate.set_value(1.33), run_time=1.3, rate_func=smooth)

        eq_slab = MathTex(
            r"\Delta V \approx \underbrace{(2\pi x)}_{\text{keliling}}\cdot\underbrace{f(x)}_{\text{tinggi}}\cdot\underbrace{\Delta x}_{\text{tebal}}",
            font_size=18, color=TEAL_B,
        ).move_to(RIGHT * 3.45 + DOWN * 1.15)
        self.play(Write(eq_slab), run_time=1.1)
        self.wait(0.8)

        # =============================================================
        # BABAK 3: Inversi Sokratik - Mengapa 2*pi*x*f(x) (bukan pi*x^2)?
        # =============================================================
        tanya = Text(
            "Pertanyaan Sokratik: Mengapa rumus kulit tabung memakai 2πx·f(x) (bukan π[f(x)]²)?",
            font_size=18, color=TEAL_A, weight=BOLD,
        ).to_edge(UP, buff=0.18)
        self.play(Transform(judul, tanya), run_time=1.0)
        self.wait(2.5)  # Jeda refleksi Sokratik

        # =============================================================
        # BABAK 4: Kristalisasi - Rumus Metode Kulit Tabung & Evaluasi Eksak
        # =============================================================
        judul4 = Text(
            "Kristalisasi Subbab 5.3: Metode Kulit Tabung V = 2π ∫ x f(x) dx",
            font_size=19, color=GOLD_B, weight=BOLD,
        ).to_edge(UP, buff=0.18)

        summary_card = VGroup(
            MathTex(
                r"\textbf{Metode Kulit Tabung (Pias $\parallel$ Sumbu Putar):} \quad "
                r"V = 2\pi\int_{a}^{b} \underbrace{x}_{\text{jari-jari}}\cdot\underbrace{f(x)}_{\text{tinggi}}\,dx",
                font_size=18, color=GOLD_B,
            ),
            MathTex(
                r"V = 2\pi\int_{0}^{2} x\big(2x^2 - x^3\big)\,dx = 2\pi\left[\frac{2}{4}x^4 - \frac{1}{5}x^5\right]_{0}^{2} "
                r"= 2\pi\left(8 - \frac{32}{5}\right) = \frac{16\pi}{5}",
                font_size=17, color=WHITE,
            ),
        ).arrange(DOWN, buff=0.08).to_edge(DOWN, buff=0.14)

        summary_box = SurroundingRectangle(
            summary_card, color=GOLD_B, fill_color=CARD_BG, fill_opacity=0.96, buff=0.13, corner_radius=0.08
        )

        self.play(
            Transform(judul, judul4),
            FadeIn(summary_box), Write(summary_card),
            run_time=1.5,
        )
        self.play(Circumscribe(summary_card[0], color=TEAL_A, time_width=0.6), run_time=1.3)
        self.wait(3.0)
