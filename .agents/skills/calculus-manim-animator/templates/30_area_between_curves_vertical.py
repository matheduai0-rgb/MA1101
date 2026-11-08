"""
Template: Luas Daerah di Antara Dua Kurva — Pias Tegak Δx (MA1101 Subtopik 5.1)
Subtopik: 5.1 Luas Daerah pada Bidang
Bahasa: Indonesia
Gaya: Grant Sanderson (3Blue1Brown) & Metode Sokratik
Deskripsi:
  Visualisasi 4 babak untuk prinsip "Iris, Hampiri, Integralkan" (Slice, Approximate, Integrate)
  pada daerah di antara dua kurva y = f(x) dan y = g(x) menggunakan pias tegak (Δx):
    - Fungsi atas : f(x) = 3 - 0.5*(x - 1)^2   (parabola kuning, terbuka ke bawah, puncak (1, 3))
    - Fungsi bawah: g(x) = 0.5*(x - 1)^2 - 1   (parabola sian, terbuka ke atas, puncak (1, -1))
    - Titik potong: f(x) = g(x) <=> 4 - (x - 1)^2 = 0 <=> x = -1 (y = 1) dan x = 3 (y = 1).
    - Perhatikan bahwa untuk x di sekitar 1, kurva bawah g(x) berada DI BAWAH sumbu-x (g(x) < 0),
      tetapi tinggi pias tegak tetap h(x) = y_atas - y_bawah = f(x) - g(x) > 0!
    - Luas eksak: int_{-1}^3 [f(x) - g(x)] dx = int_{-1}^3 [4 - (x-1)^2] dx = 32/3.

  Babak 1 (Dilema)      : Bagaimana menghitung luas daerah melengkung di antara dua kurva f(x) dan g(x),
                          terutama ketika sebagian kurva bawah menyelam ke bawah sumbu-x (g(x) < 0)?
  Babak 2 (Eksplorasi)  : Metode "Iris, Hampiri, Integralkan": pias tegak selebar Δx menyapu dari x = -1
                          ke x = 3. Saat g(x) < 0, jarak vertikal tetap f(x) + (-g(x)) = f(x) - g(x).
                          Penghalusan partisi n = 4 -> 10 -> 24 -> daerah kontinu.
  Babak 3 (Inversi)     : Bagaimana jika kedua kurva saling berpotongan di tengah selang (bertukar posisi
                          atas dan bawah)? Apakah int_a^b [f(x) - g(x)] dx masih sama dengan luas?
  Babak 4 (Kristalisasi): Rumus umum pias tegak A = int_a^b (y_atas - y_bawah) dx dan pemecahan selang
                          A = int_a^b |f(x) - g(x)| dx untuk kurva yang berpotongan.

Render:
  ../scripts/preview_scene.sh 30_area_between_curves_vertical.py AreaBetweenCurvesVerticalScene -s
"""

from manim import *
import numpy as np


A_LEFT = -1.0
B_RIGHT = 3.0
CARD_BG = "#141B28"


def f_top(x):
    return 3.0 - 0.5 * (x - 1.0) ** 2


def g_bot(x):
    return 0.5 * (x - 1.0) ** 2 - 1.0


class AreaBetweenCurvesVerticalScene(Scene):
    def construct(self):
        # =============================================================
        # TATA LETAK: Sumbu Koordinat di Kiri, Kartu Sokratik di Kanan
        # =============================================================
        ax = Axes(
            x_range=[-1.6, 3.6, 1],
            y_range=[-1.6, 3.6, 1],
            x_length=5.9,
            y_length=4.6,
            axis_config={"color": GRAY_C, "stroke_width": 1.6, "include_tip": False},
        ).add_coordinates(font_size=14)
        ax.move_to(LEFT * 3.35 + DOWN * 0.35)

        lbl_x = MathTex("x", font_size=20, color=GRAY_B).next_to(ax.x_axis.get_end(), RIGHT, buff=0.08)
        lbl_y = MathTex("y", font_size=20, color=GRAY_B).next_to(ax.y_axis.get_end(), UP, buff=0.08)

        curve_f = ax.plot(f_top, x_range=[-1.3, 3.3], color=YELLOW, stroke_width=3.8)
        curve_g = ax.plot(g_bot, x_range=[-1.3, 3.3], color=TEAL_C, stroke_width=3.8)

        lbl_f = MathTex(r"y = f(x) = 3 - \tfrac{1}{2}(x-1)^2", font_size=18, color=YELLOW).move_to(
            ax.c2p(1.0, 3.32)
        )
        lbl_g = MathTex(r"y = g(x) = \tfrac{1}{2}(x-1)^2 - 1", font_size=18, color=TEAL_C).move_to(
            ax.c2p(1.0, -1.35)
        )

        dot_left = Dot(ax.c2p(A_LEFT, f_top(A_LEFT)), color=WHITE, radius=0.065)
        dot_right = Dot(ax.c2p(B_RIGHT, f_top(B_RIGHT)), color=WHITE, radius=0.065)
        dash_left = DashedLine(ax.c2p(A_LEFT, 0), ax.c2p(A_LEFT, 1.0), color=GRAY_B, stroke_width=1.5)
        dash_right = DashedLine(ax.c2p(B_RIGHT, 0), ax.c2p(B_RIGHT, 1.0), color=GRAY_B, stroke_width=1.5)
        tag_a = MathTex(r"(-1, 1)", font_size=16, color=WHITE).next_to(dot_left, LEFT, buff=0.14)
        tag_b = MathTex(r"(3, 1)", font_size=16, color=WHITE).next_to(dot_right, RIGHT, buff=0.14)

        # =============================================================
        # BABAK 1: Dilema - Daerah di antara dua kurva (sebagian di bawah sumbu-x)
        # =============================================================
        judul = Text(
            "Bagaimana menghitung luas daerah di antara dua kurva saat g(x) menyelam di bawah sumbu-x?",
            font_size=19, color=WHITE,
        ).to_edge(UP, buff=0.2)

        self.play(Write(judul), run_time=1.3)
        self.play(Create(ax), FadeIn(lbl_x), FadeIn(lbl_y), run_time=0.9)
        self.play(
            Create(curve_f), Write(lbl_f),
            Create(curve_g), Write(lbl_g),
            FadeIn(dot_left), FadeIn(dot_right),
            Create(dash_left), Create(dash_right),
            FadeIn(tag_a), FadeIn(tag_b),
            run_time=1.4,
        )

        card_b1 = VGroup(
            Tex(r"\textbf{Prinsip ``Iris, Hampiri, Integralkan'':}", font_size=20, color=GOLD_B),
            Tex(r"1. \textbf{Iris} daerah dengan pias tegak selebar $\Delta x$.", font_size=17, color=WHITE),
            Tex(r"2. \textbf{Hampiri} luas pias: $\Delta A \approx (y_{\text{atas}} - y_{\text{bawah}})\,\Delta x$.", font_size=17, color=TEAL_A),
            Tex(r"3. \textbf{Integralkan} dari $x = a$ sampai $x = b$:", font_size=17, color=WHITE),
            MathTex(
                r"A = \int_{a}^{b} \big[f(x) - g(x)\big]\,dx",
                font_size=21, color=GOLD_B,
            ),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.11).move_to(RIGHT * 3.45 + UP * 1.65)
        box_b1 = SurroundingRectangle(
            card_b1, color=TEAL_C, fill_color=CARD_BG, fill_opacity=0.94, buff=0.15, corner_radius=0.08
        )
        self.play(FadeIn(box_b1), Write(card_b1), run_time=1.3)
        self.wait(1.0)

        # =============================================================
        # BABAK 2: Eksplorasi - Pias Tegak Menyapu & Invariansi saat g(x) < 0
        # =============================================================
        judul2 = Text(
            "Tinggi pias tegak selalu y_atas - y_bawah = f(x) - g(x), bahkan ketika g(x) < 0!",
            font_size=19, color=TEAL_A,
        ).to_edge(UP, buff=0.2)
        self.play(Transform(judul, judul2), run_time=0.9)

        x_tr = ValueTracker(-0.6)
        dx_strip = 0.26

        # Pias tegak reaktif yang bergerak mengikuti x_tr
        moving_strip = always_redraw(lambda: Polygon(
            ax.c2p(x_tr.get_value() - dx_strip / 2, g_bot(x_tr.get_value())),
            ax.c2p(x_tr.get_value() + dx_strip / 2, g_bot(x_tr.get_value())),
            ax.c2p(x_tr.get_value() + dx_strip / 2, f_top(x_tr.get_value())),
            ax.c2p(x_tr.get_value() - dx_strip / 2, f_top(x_tr.get_value())),
            fill_color=GOLD_B, fill_opacity=0.55,
            stroke_color=WHITE, stroke_width=1.8,
        ))
        top_dot = always_redraw(lambda: Dot(ax.c2p(x_tr.get_value(), f_top(x_tr.get_value())), color=YELLOW, radius=0.055))
        bot_dot = always_redraw(lambda: Dot(ax.c2p(x_tr.get_value(), g_bot(x_tr.get_value())), color=TEAL_A, radius=0.055))

        strip_info = always_redraw(lambda: VGroup(
            MathTex(
                rf"x = {x_tr.get_value():.2f}: \quad f(x) = {f_top(x_tr.get_value()):.2f}, \;\; g(x) = {g_bot(x_tr.get_value()):.2f}",
                font_size=18, color=WHITE,
            ),
            MathTex(
                rf"\text{{Tinggi pias }} h(x) = f(x) - g(x) = {f_top(x_tr.get_value()) - g_bot(x_tr.get_value()):.2f} > 0",
                font_size=19, color=GOLD_B,
            ),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.08).move_to(RIGHT * 3.45 + DOWN * 0.05))

        self.add(moving_strip, top_dot, bot_dot, strip_info)
        self.play(x_tr.animate.set_value(1.0), run_time=2.2, rate_func=smooth)
        self.wait(0.8)
        self.play(x_tr.animate.set_value(2.5), run_time=1.8, rate_func=smooth)
        self.wait(0.5)

        # Penghalusan partisi Riemann di antara dua kurva: n = 6 -> 16 -> daerah kontinu
        def make_between_rects(n_sub):
            rects = VGroup()
            dx = (B_RIGHT - A_LEFT) / n_sub
            for i in range(n_sub):
                xm = A_LEFT + (i + 0.5) * dx
                x_l = A_LEFT + i * dx
                x_r = x_l + dx
                rects.add(Polygon(
                    ax.c2p(x_l, g_bot(xm)),
                    ax.c2p(x_r, g_bot(xm)),
                    ax.c2p(x_r, f_top(xm)),
                    ax.c2p(x_l, f_top(xm)),
                    fill_color=BLUE_D, fill_opacity=0.45,
                    stroke_color=TEAL_B, stroke_width=1.2,
                ))
            return rects

        rects_6 = make_between_rects(6)
        rects_18 = make_between_rects(18)
        exact_area = ax.get_area(curve_f, x_range=[A_LEFT, B_RIGHT], bounded_graph=curve_g, color=BLUE_D, opacity=0.45)

        self.remove(moving_strip, top_dot, bot_dot, strip_info)
        eq_eval = VGroup(
            MathTex(
                r"A = \int_{-1}^{3} \Big[\big(3 - \tfrac{1}{2}(x-1)^2\big) - \big(\tfrac{1}{2}(x-1)^2 - 1\big)\Big]\,dx",
                font_size=17, color=WHITE,
            ),
            MathTex(
                r"= \int_{-1}^{3} \big[4 - (x-1)^2\big]\,dx = \left[4x - \frac{(x-1)^3}{3}\right]_{-1}^{3} = \frac{32}{3}",
                font_size=19, color=TEAL_B,
            ),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1).move_to(RIGHT * 3.45 + DOWN * 0.1)

        # Pias representatif statis di x = 1.4 untuk keyframe akhir
        rep_x = 1.4
        rep_strip = Polygon(
            ax.c2p(rep_x - 0.12, g_bot(rep_x)),
            ax.c2p(rep_x + 0.12, g_bot(rep_x)),
            ax.c2p(rep_x + 0.12, f_top(rep_x)),
            ax.c2p(rep_x - 0.12, f_top(rep_x)),
            fill_color=GOLD_B, fill_opacity=0.65,
            stroke_color=WHITE, stroke_width=1.6,
        )
        rep_lbl = MathTex(r"\Delta x", font_size=16, color=WHITE).next_to(rep_strip, DOWN, buff=0.06)

        self.play(FadeIn(rects_6), Write(eq_eval[0]), run_time=1.1)
        self.play(ReplacementTransform(rects_6, rects_18), run_time=1.1)
        self.play(ReplacementTransform(rects_18, exact_area), FadeIn(rep_strip), FadeIn(rep_lbl), Write(eq_eval[1]), run_time=1.2)
        self.wait(1.2)

        # =============================================================
        # BABAK 3: Inversi Sokratik - Bagaimana jika dua kurva berpotongan?
        # =============================================================
        tanya = Text(
            "Pertanyaan Sokratik: Bagaimana jika f(x) dan g(x) berpotongan di x = c (bertukar atas-bawah)?",
            font_size=19, color=TEAL_A, weight=BOLD,
        ).to_edge(UP, buff=0.2)
        self.play(Transform(judul, tanya), run_time=1.0)
        self.wait(2.5)  # Jeda refleksi Sokratik

        # =============================================================
        # BABAK 4: Kristalisasi - Rumus Nilai Mutlak |f(x) - g(x)| & Pemecahan Selang
        # =============================================================
        judul4 = Text(
            "Kristalisasi Subbab 5.1: Luas Daerah dengan Pias Tegak (Δx)",
            font_size=20, color=GOLD_B, weight=BOLD,
        ).to_edge(UP, buff=0.2)

        final_card = VGroup(
            Tex(r"\textbf{Rumus Umum Pias Tegak ($\Delta x$):}", font_size=19, color=GOLD_B),
            MathTex(
                r"dA = (y_{\text{atas}} - y_{\text{bawah}})\,dx \implies A = \int_{a}^{b} |f(x) - g(x)|\,dx",
                font_size=18, color=WHITE,
            ),
            Tex(r"Jika berpotongan di $x = c \in (a, b)$ ($f \ge g$ di $[a,c]$, $g \ge f$ di $[c,b]$):", font_size=16, color=GRAY_A),
            MathTex(
                r"A = \int_{a}^{c} \big[f(x) - g(x)\big]\,dx + \int_{c}^{b} \big[g(x) - f(x)\big]\,dx",
                font_size=19, color=TEAL_B,
            ),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1).move_to(RIGHT * 3.45 + DOWN * 2.05)
        final_box = SurroundingRectangle(
            final_card, color=GOLD_B, fill_color=CARD_BG, fill_opacity=0.96, buff=0.14, corner_radius=0.08
        )

        overflow = final_box.get_right()[0] - (config.frame_width / 2 - 0.15)
        if overflow > 0:
            VGroup(final_box, final_card).shift(LEFT * overflow)

        self.play(
            Transform(judul, judul4),
            FadeIn(final_box), Write(final_card),
            run_time=1.5,
        )
        self.play(Circumscribe(final_card[1], color=GOLD_A, time_width=0.6), run_time=1.3)
        self.wait(3.0)
