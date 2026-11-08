"""
Template: Volume Benda Putar — Metode Cakram & Metode Cincin (MA1101 Subtopik 5.2.a)
Subtopik: 5.2.a Volume Benda Putar: Metode Cakram dan Cincin (Disks & Washers)
Bahasa: Indonesia
Gaya: Grant Sanderson (3Blue1Brown) & Metode Sokratik
Deskripsi:
  Visualisasi komparatif 4 babak untuk Metode Cakram (Disk) vs Metode Cincin (Washer)
  ketika daerah datar diputar 360 derajat mengelilingi sumbu-x:
    - Panel Kiri (Metode Cakram / Disk Method):
        Daerah di bawah y = sqrt(x) pada [0, 4] menempel penuh pada sumbu-x.
        Pias tegak (Δx tegak lurus sumbu putar) menyapu keping cakram pejal berjari-jari R(x) = sqrt(x):
          A(x) = pi * [R(x)]^2 = pi * x  =>  V = pi * int_0^4 x dx = 8*pi.
    - Panel Kanan (Metode Cincin / Washer Method):
        Daerah di antara y = sqrt(x) dan garis y = 0.5*x pada [0, 4] memiliki celah terhadap sumbu-x.
        Pias tegak menyapu cincin berlubang (washer) dengan jari-jari luar R(x) = sqrt(x) dan
        jari-jari dalam r(x) = 0.5*x:
          A(x) = pi * ([R(x)]^2 - [r(x)]^2) = pi * (x - 0.25*x^2)  =>  V = 8*pi/3.

  Babak 1 (Dilema)      : Apa perbedaan bentuk keping 3D saat daerah menempel penuh pada sumbu putar
                          dibandingkan saat ada celah (rongga) di antara daerah dan sumbu putar?
  Babak 2 (Eksplorasi)  : Sapuan cakram pejal (kiri) vs cincin berlubang (kanan) sepanjang x in [0, 4].
  Babak 3 (Inversi)     : Mengapa luas cincin adalah pi*(R^2 - r^2) dan BUKAN pi*(R - r)^2?
                          Bagaimana jika diputar mengelilingi garis y = k?
  Babak 4 (Kristalisasi): Rumus umum Metode Cakram & Cincin (termasuk sumbu putar y = k).

Render:
  ../scripts/preview_scene.sh 32_volumes_disk_and_washer_method.py DiskAndWasherVolumeScene -s
"""

from manim import *
import numpy as np


CARD_BG = "#141B28"


def r_outer(x):
    return np.sqrt(max(0.0, x))


def r_inner(x):
    return 0.5 * x


class DiskAndWasherVolumeScene(Scene):
    def construct(self):
        # =============================================================
        # TATA LETAK DUA PANEL: Kiri = Metode Cakram, Kanan = Metode Cincin
        # =============================================================
        ax_d = Axes(
            x_range=[-0.3, 4.5, 1],
            y_range=[-2.3, 2.3, 1],
            x_length=5.4,
            y_length=3.35,
            axis_config={"color": GRAY_C, "stroke_width": 1.5, "include_tip": False},
        ).add_coordinates(font_size=12)
        ax_d.move_to(LEFT * 3.45 + UP * 0.2)

        ax_w = Axes(
            x_range=[-0.3, 4.5, 1],
            y_range=[-2.3, 2.3, 1],
            x_length=5.4,
            y_length=3.35,
            axis_config={"color": GRAY_C, "stroke_width": 1.5, "include_tip": False},
        ).add_coordinates(font_size=12)
        ax_w.move_to(RIGHT * 3.45 + UP * 0.2)

        hdr_d = Tex(
            r"\textbf{1. Metode Cakram (\textit{Disk})} — Tanpa Rongga",
            font_size=19, color=TEAL_C,
        ).next_to(ax_d, UP, buff=0.08)

        hdr_w = Tex(
            r"\textbf{2. Metode Cincin (\textit{Washer})} — Berongga!",
            font_size=19, color=GOLD_B,
        ).next_to(ax_w, UP, buff=0.08)

        # Kurva utama dan bayangan cermin rotasi terhadap sumbu-x
        c_d_top = ax_d.plot(r_outer, x_range=[0.0, 4.0], color=YELLOW, stroke_width=3.4)
        c_d_bot = DashedVMobject(
            ax_d.plot(lambda x: -r_outer(x), x_range=[0.0, 4.0], color=YELLOW_E, stroke_width=2.2),
            num_dashes=28,
        )
        area_d = ax_d.get_area(c_d_top, x_range=[0.0, 4.0], color=TEAL_D, opacity=0.35)
        lbl_d_curve = MathTex(r"R(x) = \sqrt{x}", font_size=16, color=YELLOW).move_to(ax_d.c2p(1.5, 1.75))

        c_w_top = ax_w.plot(r_outer, x_range=[0.0, 4.0], color=YELLOW, stroke_width=3.4)
        c_w_in = ax_w.plot(r_inner, x_range=[0.0, 4.0], color=TEAL_C, stroke_width=3.2)
        c_w_top_refl = DashedVMobject(
            ax_w.plot(lambda x: -r_outer(x), x_range=[0.0, 4.0], color=YELLOW_E, stroke_width=2.0),
            num_dashes=28,
        )
        c_w_in_refl = DashedVMobject(
            ax_w.plot(lambda x: -r_inner(x), x_range=[0.0, 4.0], color=TEAL_E, stroke_width=2.0),
            num_dashes=24,
        )
        area_w = ax_w.get_area(c_w_top, x_range=[0.0, 4.0], bounded_graph=c_w_in, color=BLUE_D, opacity=0.38)
        lbl_w_out = MathTex(r"R(x) = \sqrt{x}", font_size=16, color=YELLOW).move_to(ax_w.c2p(1.5, 1.75))
        lbl_w_in = MathTex(r"r(x) = \tfrac{1}{2}x", font_size=15, color=TEAL_C).move_to(ax_w.c2p(3.05, 0.72))

        # =============================================================
        # BABAK 1: Dilema - Daerah Menempel Sumbu Putar vs Daerah Berongga
        # =============================================================
        judul = Text(
            "Memutar pias tegak (Δx) mengelilingi sumbu-x: Kapan menjadi Cakram vs Cincin?",
            font_size=19, color=WHITE,
        ).to_edge(UP, buff=0.18)

        self.play(Write(judul), run_time=1.3)
        self.play(Create(ax_d), Create(ax_w), Write(hdr_d), Write(hdr_w), run_time=1.0)
        self.play(
            Create(c_d_top), FadeIn(area_d), Write(lbl_d_curve),
            Create(c_w_top), Create(c_w_in), FadeIn(area_w), Write(lbl_w_out), Write(lbl_w_in),
            run_time=1.3,
        )
        self.play(Create(c_d_bot), Create(c_w_top_refl), Create(c_w_in_refl), run_time=1.0)

        # =============================================================
        # BABAK 2: Eksplorasi - Sapuan Keping Cakram 3D vs Keping Cincin 3D
        # =============================================================
        judul2 = Text(
            "Pias tegak lurus sumbu putar menyapu Cakram Pejal (πR²) vs Cincin Berlubang (π(R² - r²))!",
            font_size=18, color=TEAL_A,
        ).to_edge(UP, buff=0.18)
        self.play(Transform(judul, judul2), run_time=0.9)

        x_tr = ValueTracker(0.45)

        def make_disk_3d(x_val):
            rad_y = abs(ax_d.c2p(x_val, r_outer(x_val))[1] - ax_d.c2p(x_val, 0)[1])
            center = ax_d.c2p(x_val, 0)
            disk_el = Ellipse(
                width=0.42, height=max(0.06, 2 * rad_y),
                fill_color=TEAL_B, fill_opacity=0.62,
                stroke_color=WHITE, stroke_width=1.8,
            ).move_to(center)
            r_line = Line(center, ax_d.c2p(x_val, r_outer(x_val)), color=YELLOW, stroke_width=3.2)
            r_dot = Dot(ax_d.c2p(x_val, r_outer(x_val)), color=YELLOW, radius=0.05)
            return VGroup(disk_el, r_line, r_dot)

        def make_washer_3d(x_val):
            rad_out = abs(ax_w.c2p(x_val, r_outer(x_val))[1] - ax_w.c2p(x_val, 0)[1])
            rad_in = abs(ax_w.c2p(x_val, r_inner(x_val))[1] - ax_w.c2p(x_val, 0)[1])
            center = ax_w.c2p(x_val, 0)
            outer_el = Ellipse(
                width=0.44, height=max(0.06, 2 * rad_out),
                fill_color=GOLD_B, fill_opacity=0.65,
                stroke_color=WHITE, stroke_width=1.8,
            ).move_to(center)
            inner_hole = Ellipse(
                width=0.22, height=max(0.03, 2 * rad_in),
                fill_color=CARD_BG, fill_opacity=0.96,
                stroke_color=TEAL_B, stroke_width=1.6,
            ).move_to(center)
            line_R = Line(center, ax_w.c2p(x_val, r_outer(x_val)), color=YELLOW, stroke_width=2.8)
            line_r = Line(center, ax_w.c2p(x_val, -r_inner(x_val)), color=TEAL_A, stroke_width=2.8)
            return VGroup(outer_el, inner_hole, line_R, line_r)

        disk_3d = always_redraw(lambda: make_disk_3d(x_tr.get_value()))
        washer_3d = always_redraw(lambda: make_washer_3d(x_tr.get_value()))

        self.add(disk_3d, washer_3d)
        self.play(x_tr.animate.set_value(3.75), run_time=2.8, rate_func=smooth)
        self.play(x_tr.animate.set_value(2.25), run_time=1.2, rate_func=smooth)

        eq_d = MathTex(
            r"V_{\text{cakram}} = \pi\int_{0}^{4} \big(\sqrt{x}\big)^2\,dx = 8\pi",
            font_size=18, color=TEAL_B,
        ).next_to(ax_d, DOWN, buff=0.14)

        eq_w = MathTex(
            r"V_{\text{cincin}} = \pi\int_{0}^{4} \Big[\big(\sqrt{x}\big)^2 - \big(\tfrac{1}{2}x\big)^2\Big]\,dx = \frac{8\pi}{3}",
            font_size=17, color=GOLD_B,
        ).next_to(ax_w, DOWN, buff=0.14)

        self.play(Write(eq_d), Write(eq_w), run_time=1.2)
        self.wait(1.0)

        # =============================================================
        # BABAK 3: Inversi Sokratik - Jebakan (R^2 - r^2) vs (R - r)^2
        # =============================================================
        tanya = Text(
            "Pertanyaan Sokratik: Mengapa luas cincin adalah π(R² - r²) dan BUKAN π(R - r)²?",
            font_size=19, color=TEAL_A, weight=BOLD,
        ).to_edge(UP, buff=0.18)
        self.play(Transform(judul, tanya), run_time=1.0)
        self.wait(2.5)  # Jeda refleksi Sokratik

        # =============================================================
        # BABAK 4: Kristalisasi - Rumus Cakram, Cincin & Rotasi Garis y = k
        # =============================================================
        judul4 = Text(
            "Kristalisasi Subbab 5.2.a: Metode Cakram & Cincin (Pias Tegak Lurus Sumbu Putar!)",
            font_size=19, color=GOLD_B, weight=BOLD,
        ).to_edge(UP, buff=0.18)

        summary_card = VGroup(
            MathTex(
                r"\textbf{Cakram:} \;\; dV = \pi\big[R(x)\big]^2\,dx, \qquad "
                r"\textbf{Cincin:} \;\; dV = \pi\Big(\big[R_{\text{luar}}(x)\big]^2 - \big[r_{\text{dalam}}(x)\big]^2\Big)\,dx",
                font_size=18, color=WHITE,
            ),
            Tex(
                r"$\star$ \textbf{Awas Jebakan:} $R^2 - r^2 \neq (R - r)^2$! "
                r"Jika diputar terhadap garis $y = k$: $R(x) = |y_{\text{luar}} - k|$ dan $r(x) = |y_{\text{dalam}} - k|$.",
                font_size=16, color=GOLD_B,
            ),
        ).arrange(DOWN, buff=0.09).to_edge(DOWN, buff=0.15)

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
