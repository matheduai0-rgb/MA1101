"""
Template: Kulit Tabung di Antara Dua Kurva & Sumbu Putar Bergeser x = k (MA1101 Subtopik 5.3)
Subtopik: 5.3 Volume Benda Putar: Metode Kulit Tabung
Bahasa: Indonesia
Gaya: Grant Sanderson (3Blue1Brown) & Metode Sokratik
Deskripsi:
  Visualisasi komparatif 4 babak untuk daerah R di antara dua kurva y = 2x - x^2 (atas)
  dan y = x^2 (bawah) pada [0, 1] ketika diputar dengan Metode Kulit Tabung (Δx sejajar sumbu):
    - Panel Kiri (Putar Mengelilingi Sumbu-y / x = 0):
        Jari-jari kulit tabung r(x) = x, tinggi h(x) = (2x - x^2) - x^2 = 2x - 2x^2:
          V_y = 2*pi * int_0^1 x*(2x - 2x^2) dx = pi/3.
    - Panel Kanan (Putar Mengelilingi Garis Tegak x = 2 di Kanan Daerah):
        Tinggi pias tetap h(x) = 2x - 2x^2, tetapi jari-jari (jarak dari x ke garis x = 2)
        berubah menjadi r(x) = 2 - x!
          V_{x=2} = 2*pi * int_0^1 (2 - x)*(2x - 2x^2) dx = pi.

  Babak 1 (Dilema)      : Bagaimana menyusun integral kulit tabung untuk daerah di antara dua kurva,
                          dan apa yang berubah jika sumbu putar digeser ke garis tegak x = 2?
  Babak 2 (Eksplorasi)  : Sapuan pias tegak pada kedua panel: membandingkan jari-jari r(x) = x
                          (terhadap sumbu-y) vs r(x) = 2 - x (terhadap garis x = 2).
  Babak 3 (Inversi)     : Bagaimana jika daerah yang sama diputar mengelilingi garis x = -1 di sebelah kiri?
  Babak 4 (Kristalisasi): Rumus umum kulit tabung terhadap garis x = k dan aturan emas memilih
                          Cakram/Cincin (pias tegak lurus) vs Kulit Tabung (pias sejajar).

Render:
  ../scripts/preview_scene.sh 35_shells_vs_washers_and_shifted_axis.py ShellsVsWashersShiftedAxisScene -s
"""

from manim import *
import numpy as np


CARD_BG = "#141B28"


def f_up(x):
    return 2.0 * x - x ** 2


def g_low(x):
    return x ** 2


class ShellsVsWashersShiftedAxisScene(Scene):
    def construct(self):
        # =============================================================
        # TATA LETAK DUA PANEL: Kiri = Putar Sumbu-y, Kanan = Putar Garis x = 2
        # =============================================================
        ax_l = Axes(
            x_range=[-1.2, 1.4, 1],
            y_range=[-0.2, 1.3, 0.5],
            x_length=5.3,
            y_length=3.3,
            axis_config={"color": GRAY_C, "stroke_width": 1.5, "include_tip": False},
        ).add_coordinates(font_size=12)
        ax_l.move_to(LEFT * 3.45 + UP * 0.22)

        ax_r = Axes(
            x_range=[-0.2, 4.2, 1],
            y_range=[-0.2, 1.3, 0.5],
            x_length=5.5,
            y_length=3.3,
            axis_config={"color": GRAY_C, "stroke_width": 1.5, "include_tip": False},
        ).add_coordinates(font_size=12)
        ax_r.move_to(RIGHT * 3.45 + UP * 0.22)

        hdr_l = Tex(
            r"\textbf{1. Putar Sumbu-$y$ ($x = 0$):} $r(x) = x$",
            font_size=19, color=TEAL_C,
        ).next_to(ax_l, UP, buff=0.08)

        hdr_r = Tex(
            r"\textbf{2. Putar Garis $x = 2$:} $r(x) = 2 - x$",
            font_size=19, color=GOLD_B,
        ).next_to(ax_r, UP, buff=0.08)

        # Panel Kiri: daerah pada [0, 1] dan bayangan cermin di [-1, 0]
        c_l_top = ax_l.plot(f_up, x_range=[0.0, 1.0], color=YELLOW, stroke_width=3.4)
        c_l_bot = ax_l.plot(g_low, x_range=[0.0, 1.0], color=TEAL_C, stroke_width=3.4)
        area_l = ax_l.get_area(c_l_top, x_range=[0.0, 1.0], bounded_graph=c_l_bot, color=TEAL_D, opacity=0.42)
        c_l_top_m = DashedVMobject(ax_l.plot(lambda x: f_up(-x), x_range=[-1.0, 0.0], color=YELLOW_E, stroke_width=2.0), num_dashes=18)
        c_l_bot_m = DashedVMobject(ax_l.plot(lambda x: g_low(-x), x_range=[-1.0, 0.0], color=TEAL_E, stroke_width=2.0), num_dashes=18)

        # Panel Kanan: daerah pada [0, 1], garis sumbu putar x = 2, dan bayangan cermin di [3, 4]
        c_r_top = ax_r.plot(f_up, x_range=[0.0, 1.0], color=YELLOW, stroke_width=3.4)
        c_r_bot = ax_r.plot(g_low, x_range=[0.0, 1.0], color=TEAL_C, stroke_width=3.4)
        area_r = ax_r.get_area(c_r_top, x_range=[0.0, 1.0], bounded_graph=c_r_bot, color=BLUE_D, opacity=0.42)
        axis_x2 = DashedLine(ax_r.c2p(2.0, -0.15), ax_r.c2p(2.0, 1.25), color=RED_B, stroke_width=2.4, dash_length=0.08)
        lbl_x2 = MathTex(r"x = 2", font_size=16, color=RED_B).next_to(ax_r.c2p(2.0, 1.22), UP, buff=0.04)
        c_r_top_m = DashedVMobject(ax_r.plot(lambda x: f_up(4.0 - x), x_range=[3.0, 4.0], color=YELLOW_E, stroke_width=2.0), num_dashes=18)
        c_r_bot_m = DashedVMobject(ax_r.plot(lambda x: g_low(4.0 - x), x_range=[3.0, 4.0], color=TEAL_E, stroke_width=2.0), num_dashes=18)

        # =============================================================
        # BABAK 1: Dilema - Daerah Antara Dua Kurva & Pergeseran Sumbu Putar
        # =============================================================
        judul = Text(
            "Daerah antara y = 2x - x² dan y = x²: Apa yang berubah saat diputar terhadap garis x = 2?",
            font_size=18, color=WHITE,
        ).to_edge(UP, buff=0.18)

        self.play(Write(judul), run_time=1.3)
        self.play(Create(ax_l), Create(ax_r), Write(hdr_l), Write(hdr_r), run_time=1.0)
        self.play(
            Create(c_l_top), Create(c_l_bot), FadeIn(area_l), Create(c_l_top_m), Create(c_l_bot_m),
            Create(c_r_top), Create(c_r_bot), FadeIn(area_r), Create(axis_x2), FadeIn(lbl_x2),
            Create(c_r_top_m), Create(c_r_bot_m),
            run_time=1.4,
        )

        # =============================================================
        # BABAK 2: Eksplorasi - Jari-Jari r(x) = x vs r(x) = 2 - x
        # =============================================================
        judul2 = Text(
            "Tinggi pias tetap h(x) = 2x - 2x², tetapi jari-jari selalu diukur dari sumbu putar!",
            font_size=18, color=TEAL_A,
        ).to_edge(UP, buff=0.18)
        self.play(Transform(judul, judul2), run_time=0.9)

        x_tr = ValueTracker(0.25)

        def make_left_strip(x_val):
            p_bot = ax_l.c2p(x_val, g_low(x_val))
            p_top = ax_l.c2p(x_val, f_up(x_val))
            strip = Line(p_bot, p_top, color=GOLD_B, stroke_width=6.0)
            y_mid = 0.5 * (f_up(x_val) + g_low(x_val))
            r_arr = DoubleArrow(
                ax_l.c2p(0, y_mid), ax_l.c2p(x_val, y_mid),
                color=WHITE, buff=0, stroke_width=2.2, max_tip_length_to_length_ratio=0.22,
            )
            r_lbl = MathTex(r"r = x", font_size=15, color=WHITE).next_to(r_arr, UP, buff=0.04)
            return VGroup(strip, r_arr, r_lbl)

        def make_right_strip(x_val):
            p_bot = ax_r.c2p(x_val, g_low(x_val))
            p_top = ax_r.c2p(x_val, f_up(x_val))
            strip = Line(p_bot, p_top, color=GOLD_B, stroke_width=6.0)
            y_mid = 0.5 * (f_up(x_val) + g_low(x_val))
            r_arr = DoubleArrow(
                ax_r.c2p(x_val, y_mid), ax_r.c2p(2.0, y_mid),
                color=GOLD_B, buff=0, stroke_width=2.4, max_tip_length_to_length_ratio=0.16,
            )
            r_lbl = MathTex(r"r = 2 - x", font_size=15, color=GOLD_B).next_to(r_arr, UP, buff=0.04)
            return VGroup(strip, r_arr, r_lbl)

        left_dyn = always_redraw(lambda: make_left_strip(x_tr.get_value()))
        right_dyn = always_redraw(lambda: make_right_strip(x_tr.get_value()))

        self.add(left_dyn, right_dyn)
        self.play(x_tr.animate.set_value(0.85), run_time=2.4, rate_func=smooth)
        self.play(x_tr.animate.set_value(0.55), run_time=1.2, rate_func=smooth)

        eq_l = MathTex(
            r"V_{y} = 2\pi\int_{0}^{1} x\big(2x - 2x^2\big)\,dx = \frac{\pi}{3}",
            font_size=18, color=TEAL_B,
        ).next_to(ax_l, DOWN, buff=0.14)

        eq_r = MathTex(
            r"V_{x=2} = 2\pi\int_{0}^{1} (2 - x)\big(2x - 2x^2\big)\,dx = \pi",
            font_size=18, color=GOLD_B,
        ).next_to(ax_r, DOWN, buff=0.14)

        self.play(Write(eq_l), Write(eq_r), run_time=1.2)
        self.wait(0.8)

        # =============================================================
        # BABAK 3: Inversi Sokratik - Bagaimana jika diputar terhadap x = -1?
        # =============================================================
        tanya = Text(
            "Pertanyaan Sokratik: Jika diputar terhadap garis x = -1 di kiri daerah, berapakah jari-jari r(x)?",
            font_size=18, color=TEAL_A, weight=BOLD,
        ).to_edge(UP, buff=0.18)
        self.play(Transform(judul, tanya), run_time=1.0)
        self.wait(2.5)  # Jeda refleksi Sokratik

        # =============================================================
        # BABAK 4: Kristalisasi - Rumus Umum Garis x = k & Panduan Cincin vs Kulit Tabung
        # =============================================================
        judul4 = Text(
            "Kristalisasi Subbab 5.3: Kulit Tabung Terhadap Garis x = k & Orientasi Pias",
            font_size=19, color=GOLD_B, weight=BOLD,
        ).to_edge(UP, buff=0.18)

        summary_card = VGroup(
            MathTex(
                r"\textbf{Putar Garis Tegak $x = k$ ($\Delta x \parallel$ sumbu):} \quad "
                r"V = 2\pi\int_{a}^{b} \underbrace{|x - k|}_{\text{jari-jari } r(x)}\cdot\underbrace{\big[f(x) - g(x)\big]}_{\text{tinggi } h(x)}\,dx",
                font_size=17, color=WHITE,
            ),
            Tex(
                r"$\star$ \textbf{Aturan Emas Bab 5:} Pias $\perp$ Sumbu Putar $\implies$ \textbf{Cakram/Cincin} ($\pi R^2$); "
                r"Pias $\parallel$ Sumbu Putar $\implies$ \textbf{Kulit Tabung} ($2\pi r h$).",
                font_size=16, color=GOLD_B,
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
