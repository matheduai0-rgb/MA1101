"""
Template: Strategi Pias Mendatar (Δy) vs Pias Tegak (Δx) (MA1101 Subtopik 5.1)
Subtopik: 5.1 Luas Daerah pada Bidang
Bahasa: Indonesia
Gaya: Grant Sanderson (3Blue1Brown) & Metode Sokratik
Deskripsi:
  Visualisasi komparatif 4 babak untuk daerah R yang dibatasi oleh parabola tidur x = y^2
  dan garis miring x = y + 2 (berpotongan di (1, -1) dan (4, 2)):
    - Panel Kiri (Pias Tegak Δx):
        Pada x in [0, 1], batas atas y = +sqrt(x) dan batas bawah y = -sqrt(x) (cabang parabola yang sama!).
        Pada x in [1, 4], batas atas y = +sqrt(x) tetapi batas bawah berganti menjadi garis y = x - 2!
        Akibatnya pias tegak memaksa kita memecah menjadi 2 integral berbentuk akar:
          A = int_0^1 2*sqrt(x) dx + int_1^4 (sqrt(x) - x + 2) dx = 4/3 + 19/6 = 9/2.
    - Panel Kanan (Pias Mendatar Δy):
        Sepanjang y in [-1, 2], batas kanan SELALU garis x_kanan = y + 2 dan batas kiri SELALU
        parabola x_kiri = y^2! Cukup 1 integral polinom sederhana tanpa akar:
          A = int_{-1}^2 [(y + 2) - y^2] dy = [y^2/2 + 2y - y^3/3]_{-1}^2 = 9/2.

  Babak 1 (Dilema)      : Daerah R dibatasi oleh x = y^2 dan x = y + 2. Mengapa pias tegak (Δx)
                          terbentur pergantian rumus batas bawah di x = 1?
  Babak 2 (Eksplorasi)  : Dua panel berdampingan. Kiri: pias tegak terbelah menjadi 2 daerah di x = 1.
                          Kanan: pias mendatar setebal Δy menyapu mulus dari y = -1 hingga y = 2.
  Babak 3 (Inversi)     : Kapan kita sebaiknya memilih pias mendatar (Δy) dibandingkan pias tegak (Δx)?
  Babak 4 (Kristalisasi): Rumus pias mendatar dA = (x_kanan - x_kiri) dy dan hasil eksak A = 9/2.

Render:
  ../scripts/preview_scene.sh 31_area_horizontal_vs_vertical_slicing.py AreaHorizontalVsVerticalScene -s
"""

from manim import *
import numpy as np


CARD_BG = "#141B28"


class AreaHorizontalVsVerticalScene(Scene):
    def construct(self):
        # =============================================================
        # TATA LETAK DUA PANEL: Kiri = Pias Tegak (Δx), Kanan = Pias Mendatar (Δy)
        # =============================================================
        ax_v = Axes(
            x_range=[-0.4, 4.5, 1],
            y_range=[-1.6, 2.5, 1],
            x_length=5.5,
            y_length=3.4,
            axis_config={"color": GRAY_C, "stroke_width": 1.5, "include_tip": False},
        ).add_coordinates(font_size=13)
        ax_v.move_to(LEFT * 3.45 + UP * 0.15)

        ax_h = Axes(
            x_range=[-0.4, 4.5, 1],
            y_range=[-1.6, 2.5, 1],
            x_length=5.5,
            y_length=3.4,
            axis_config={"color": GRAY_C, "stroke_width": 1.5, "include_tip": False},
        ).add_coordinates(font_size=13)
        ax_h.move_to(RIGHT * 3.45 + UP * 0.15)

        hdr_v = Tex(
            r"\textbf{Cara 1: Pias Tegak ($\Delta x$)} — Terbelah 2 Daerah!",
            font_size=20, color=MAROON_B,
        ).next_to(ax_v, UP, buff=0.1)

        hdr_h = Tex(
            r"\textbf{Cara 2: Pias Mendatar ($\Delta y$)} — Cukup 1 Integral!",
            font_size=20, color=TEAL_C,
        ).next_to(ax_h, UP, buff=0.1)

        def build_region_curves(ax):
            # Parabola x = y^2 digambar parametrik t -> (t^2, t) untuk t in [-1.35, 2.15]
            parab = ax.plot_parametric_curve(
                lambda t: np.array([t ** 2, t, 0.0]),
                t_range=[-1.35, 2.15],
                color=YELLOW, stroke_width=3.5,
            )
            line = ax.plot(lambda x: x - 2.0, x_range=[0.5, 4.3], color=TEAL_C, stroke_width=3.5)
            d1 = Dot(ax.c2p(1.0, -1.0), color=WHITE, radius=0.055)
            d2 = Dot(ax.c2p(4.0, 2.0), color=WHITE, radius=0.055)
            t1 = MathTex(r"(1,-1)", font_size=15, color=WHITE).next_to(d1, DOWN, buff=0.14)
            t2 = MathTex(r"(4,2)", font_size=15, color=WHITE).next_to(d2, UP + LEFT, buff=0.05)
            lbl_p = MathTex(r"x = y^2", font_size=17, color=YELLOW).move_to(ax.c2p(1.5, 1.68))
            lbl_l = MathTex(r"x = y + 2", font_size=17, color=TEAL_C).move_to(ax.c2p(3.45, 0.7))
            return VGroup(parab, line, d1, d2, t1, t2, lbl_p, lbl_l)

        curves_v = build_region_curves(ax_v)
        curves_h = build_region_curves(ax_h)

        # =============================================================
        # BABAK 1: Dilema - Daerah yang dibatasi oleh x = y^2 dan x = y + 2
        # =============================================================
        judul = Text(
            "Daerah R dibatasi oleh x = y² dan x = y + 2: Mengapa pias tegak (Δx) menjadi rumit?",
            font_size=19, color=WHITE,
        ).to_edge(UP, buff=0.18)

        self.play(Write(judul), run_time=1.3)
        self.play(
            Create(ax_v), Create(ax_h),
            Write(hdr_v), Write(hdr_h),
            run_time=1.0,
        )
        self.play(FadeIn(curves_v), FadeIn(curves_h), run_time=1.2)
        self.wait(0.8)

        # =============================================================
        # BABAK 2: Eksplorasi - Pias Tegak Terbelah di x = 1 vs Pias Mendatar Mulus
        # =============================================================
        # Di Panel Kiri: garis pembagi x = 1 memisahkan Daerah I [0, 1] dan Daerah II [1, 4]
        split_line_v = DashedLine(
            ax_v.c2p(1.0, -1.05), ax_v.c2p(1.0, 1.25), color=RED_B, stroke_width=2.2, dash_length=0.08
        )
        lbl_split = MathTex(r"x = 1", font_size=16, color=RED_B).next_to(ax_v.c2p(1.0, 1.25), UP, buff=0.06)

        # Poligon Daerah I [0, 1] dan Daerah II [1, 4] pada ax_v
        xs_1 = np.linspace(0.0, 1.0, 30)
        pts_reg1 = [ax_v.c2p(x, np.sqrt(x)) for x in xs_1] + [ax_v.c2p(x, -np.sqrt(x)) for x in reversed(xs_1)]
        poly_reg1 = Polygon(*pts_reg1, fill_color=MAROON_B, fill_opacity=0.45, stroke_width=0)

        xs_2 = np.linspace(1.0, 4.0, 40)
        pts_reg2 = [ax_v.c2p(x, np.sqrt(x)) for x in xs_2] + [ax_v.c2p(x, x - 2.0) for x in reversed(xs_2)]
        poly_reg2 = Polygon(*pts_reg2, fill_color=BLUE_D, fill_opacity=0.45, stroke_width=0)

        eq_dx = MathTex(
            r"A = \int_{0}^{1} 2\sqrt{x}\,dx + \int_{1}^{4} \big(\sqrt{x} - x + 2\big)\,dx",
            font_size=18, color=MAROON_A,
        ).next_to(ax_v, DOWN, buff=0.16)

        self.play(
            FadeIn(poly_reg1), FadeIn(poly_reg2),
            Create(split_line_v), FadeIn(lbl_split),
            Write(eq_dx),
            run_time=1.5,
        )
        self.wait(0.8)

        # Di Panel Kanan: Pias mendatar (Δy) menyapu dari y = -1 ke y = 2
        judul2 = Text(
            "Dengan pias mendatar (Δy), batas kanan selalu garis x = y+2 dan batas kiri selalu x = y²!",
            font_size=19, color=TEAL_A,
        ).to_edge(UP, buff=0.18)
        self.play(Transform(judul, judul2), run_time=0.9)

        y_tr = ValueTracker(-0.9)
        dy_strip = 0.22

        h_strip = always_redraw(lambda: Polygon(
            ax_h.c2p(y_tr.get_value() ** 2, y_tr.get_value() - dy_strip / 2),
            ax_h.c2p(y_tr.get_value() + 2.0, y_tr.get_value() - dy_strip / 2),
            ax_h.c2p(y_tr.get_value() + 2.0, y_tr.get_value() + dy_strip / 2),
            ax_h.c2p(y_tr.get_value() ** 2, y_tr.get_value() + dy_strip / 2),
            fill_color=GOLD_B, fill_opacity=0.65,
            stroke_color=WHITE, stroke_width=1.8,
        ))

        # Daerah terarsir bertahap dari y = -1 hingga y_tr pada ax_h
        def get_horiz_area(y_top):
            ys = np.linspace(-1.0, max(-0.98, y_top), 40)
            pts = [ax_h.c2p(y ** 2, y) for y in ys] + [ax_h.c2p(y + 2.0, y) for y in reversed(ys)]
            return Polygon(*pts, fill_color=TEAL_D, fill_opacity=0.45, stroke_width=0)

        swept_area_h = always_redraw(lambda: get_horiz_area(y_tr.get_value()))

        eq_dy = MathTex(
            r"A = \int_{-1}^{2} \big[(y + 2) - y^2\big]\,dy = \frac{9}{2}",
            font_size=19, color=TEAL_B,
        ).next_to(ax_h, DOWN, buff=0.16)

        self.add(swept_area_h, h_strip)
        self.play(y_tr.animate.set_value(1.98), run_time=2.6, rate_func=smooth)
        # Bekukan daerah terarsir penuh dan letakkan pias mendatar representatif di y = 0.75
        full_area_h = get_horiz_area(2.0)
        self.add(full_area_h)
        self.remove(swept_area_h)
        self.play(y_tr.animate.set_value(0.75), Write(eq_dy), run_time=1.1, rate_func=smooth)
        self.wait(1.0)

        # =============================================================
        # BABAK 3: Inversi Sokratik - Kapan memilih Δy vs Δx?
        # =============================================================
        tanya = Text(
            "Pertanyaan Sokratik: Mengapa pada pias mendatar (Δy) kita mengurangkan x_kanan - x_kiri?",
            font_size=19, color=TEAL_A, weight=BOLD,
        ).to_edge(UP, buff=0.18)
        self.play(Transform(judul, tanya), run_time=1.0)
        self.wait(2.5)  # Jeda refleksi Sokratik

        # =============================================================
        # BABAK 4: Kristalisasi - Rumus Umum Pias Mendatar (Δy)
        # =============================================================
        judul4 = Text(
            "Kristalisasi: Rumus Pias Mendatar dA = (x_kanan - x_kiri) dy (Tanpa Pecah Integral & Tanpa Akar!)",
            font_size=18, color=GOLD_B, weight=BOLD,
        ).to_edge(UP, buff=0.18)

        summary_card = VGroup(
            MathTex(
                r"\textbf{Pias Mendatar ($\Delta y$):} \quad dA = \big(x_{\text{kanan}} - x_{\text{kiri}}\big)\,dy = \big[p(y) - q(y)\big]\,dy",
                font_size=19, color=GOLD_B,
            ),
            MathTex(
                r"A = \int_{c}^{d} \big[p(y) - q(y)\big]\,dy = \int_{-1}^{2} (y + 2 - y^2)\,dy = \left[\frac{y^2}{2} + 2y - \frac{y^3}{3}\right]_{-1}^{2} = \frac{9}{2} = 4{,}5",
                font_size=18, color=WHITE,
            ),
        ).arrange(DOWN, buff=0.09).to_edge(DOWN, buff=0.16)

        summary_box = SurroundingRectangle(
            summary_card, color=GOLD_B, fill_color=CARD_BG, fill_opacity=0.96, buff=0.13, corner_radius=0.08
        )

        self.play(
            Transform(judul, judul4),
            FadeIn(summary_box), Write(summary_card),
            run_time=1.5,
        )
        self.play(Circumscribe(summary_card[1], color=TEAL_A, time_width=0.6), run_time=1.3)
        self.wait(3.0)
