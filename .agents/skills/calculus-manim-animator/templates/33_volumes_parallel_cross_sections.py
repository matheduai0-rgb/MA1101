"""
Template: Volume Benda Pejal — Metode Irisan Sejajar / Lempeng (MA1101 Subtopik 5.2.b)
Subtopik: 5.2.b Volume Benda Pejal: Metode Irisan Sejajar (Parallel Cross-Sections / Slabs)
Bahasa: Indonesia
Gaya: Grant Sanderson (3Blue1Brown) & Metode Sokratik
Deskripsi:
  Visualisasi 4 babak untuk menghitung volume benda pejal dengan alas daerah datar R di bidang-xy
  (dibatasi oleh y = sqrt(x), sumbu-x, dan x = 4) di mana setiap irisan penampang tegak lurus
  sumbu-x memiliki panjang alas s(x) = sqrt(x) dan luas penampang A(x) = c * [s(x)]^2:
    1. Penampang Persegi (Square):
         A(x) = [s(x)]^2 = x                    =>  V = int_0^4 x dx = 8.
    2. Penampang Setengah Lingkaran (Semicircle, diameter = s(x) => r = s(x)/2):
         A(x) = (1/2) * pi * (s(x)/2)^2 = (pi/8) * [s(x)]^2 = (pi/8)*x  =>  V = pi.
    3. Penampang Segitiga Sama Sisi (Equilateral Triangle):
         A(x) = (sqrt(3)/4) * [s(x)]^2 = (sqrt(3)/4)*x  =>  V = 2*sqrt(3).

  Babak 1 (Dilema)      : Bagaimana menghitung volume benda pejal yang BUKAN benda putar, jika kita
                          mengetahui rumus luas setiap irisan penampang sejajar A(x)?
  Babak 2 (Eksplorasi)  : Tali busur alas s(x) = sqrt(x) menyapu daerah alas di kiri, sementara 3 bentuk
                          penampang (Persegi, Setengah Lingkaran, Segitiga Sama Sisi) tumbuh secara
                          sinkron di kanan sesuai proporsi [s(x)]^2.
  Babak 3 (Inversi)     : Mengapa setengah lingkaran berdiameter s(x) memiliki faktor luas pi/8
                          (bukan pi/2)?
  Babak 4 (Kristalisasi): Rumus umum lempeng V = int_a^b A(x) dx dan kamus faktor bentuk c * [s(x)]^2.

Render:
  ../scripts/preview_scene.sh 33_volumes_parallel_cross_sections.py ParallelCrossSectionsVolumeScene -s
"""

from manim import *
import numpy as np


CARD_BG = "#141B28"


def s_chord(x):
    return np.sqrt(max(0.0, x))


class ParallelCrossSectionsVolumeScene(Scene):
    def construct(self):
        # =============================================================
        # TATA LETAK: Kiri = Daerah Alas R di Bidang-xy, Kanan = 3 Penampang A(x)
        # =============================================================
        ax_base = Axes(
            x_range=[-0.3, 4.5, 1],
            y_range=[-0.3, 2.4, 1],
            x_length=5.1,
            y_length=3.35,
            axis_config={"color": GRAY_C, "stroke_width": 1.6, "include_tip": False},
        ).add_coordinates(font_size=13)
        ax_base.move_to(LEFT * 3.55 + UP * 0.22)

        hdr_base = Tex(
            r"\textbf{Daerah Alas $R$ di Bidang-$xy$}",
            font_size=19, color=YELLOW,
        ).next_to(ax_base, UP, buff=0.1)

        curve_top = ax_base.plot(s_chord, x_range=[0.0, 4.0], color=YELLOW, stroke_width=3.6)
        line_right = DashedLine(ax_base.c2p(4.0, 0), ax_base.c2p(4.0, 2.0), color=GRAY_B, stroke_width=1.6)
        base_area = ax_base.get_area(curve_top, x_range=[0.0, 4.0], color=BLUE_D, opacity=0.35)
        lbl_curve = MathTex(r"y = \sqrt{x}", font_size=18, color=YELLOW).move_to(ax_base.c2p(1.6, 1.65))

        # =============================================================
        # BABAK 1: Dilema - Benda Pejal Non-Putar dengan Penampang Sejajar A(x)
        # =============================================================
        judul = Text(
            "Metode Irisan Sejajar (5.2.b): Bagaimana jika penampang tegak lurus sumbu-x bukan lingkaran penuh?",
            font_size=18, color=WHITE,
        ).to_edge(UP, buff=0.18)

        self.play(Write(judul), run_time=1.3)
        self.play(Create(ax_base), Write(hdr_base), run_time=0.9)
        self.play(Create(curve_top), Create(line_right), FadeIn(base_area), Write(lbl_curve), run_time=1.2)

        hdr_shapes = Tex(
            r"\textbf{3 Pilihan Bentuk Penampang Tegak Lurus Sumbu-$x$ (Alas $s(x) = \sqrt{x}$):}",
            font_size=17, color=TEAL_A,
        ).move_to(RIGHT * 3.15 + UP * 2.15)
        self.play(Write(hdr_shapes), run_time=1.0)

        # =============================================================
        # BABAK 2: Eksplorasi - Sapuan s(x) dan Pertumbuhan 3 Penampang A(x)
        # =============================================================
        judul2 = Text(
            "Panjang pias di bidang-xy menjadi alas s(x) bagi lempeng penampang A(x)!",
            font_size=19, color=TEAL_A,
        ).to_edge(UP, buff=0.18)
        self.play(Transform(judul, judul2), run_time=0.9)

        x_tr = ValueTracker(0.5)

        # Tali busur s(x) pada daerah alas di kiri
        chord_group = always_redraw(lambda: VGroup(
            Line(
                ax_base.c2p(x_tr.get_value(), 0),
                ax_base.c2p(x_tr.get_value(), s_chord(x_tr.get_value())),
                color=GOLD_B, stroke_width=5.0,
            ),
            Dot(ax_base.c2p(x_tr.get_value(), 0), color=WHITE, radius=0.055),
            Dot(ax_base.c2p(x_tr.get_value(), s_chord(x_tr.get_value())), color=YELLOW, radius=0.055),
            MathTex(
                rf"s(x) = {s_chord(x_tr.get_value()):.2f}",
                font_size=16, color=GOLD_B,
            ).next_to(ax_base.c2p(x_tr.get_value(), s_chord(x_tr.get_value()) / 2), RIGHT, buff=0.08),
        ))

        # Tiga panggung penampang di panel kanan: Persegi, Setengah Lingkaran, Segitiga Sama Sisi
        centers_x = [1.05, 3.25, 5.45]
        base_y = 0.05
        scale_unit = 0.72  # 1 satuan s(x) = 0.72 satuan layar

        def make_three_sections(x_val):
            s = s_chord(x_val)
            w = max(0.12, s * scale_unit)

            # 1. Persegi (Square)
            c1 = np.array([centers_x[0], base_y, 0.0])
            sq = Polygon(
                c1 + LEFT * w / 2,
                c1 + RIGHT * w / 2,
                c1 + RIGHT * w / 2 + UP * w,
                c1 + LEFT * w / 2 + UP * w,
                fill_color=TEAL_C, fill_opacity=0.5,
                stroke_color=WHITE, stroke_width=2.0,
            )
            base1 = Line(c1 + LEFT * w / 2, c1 + RIGHT * w / 2, color=GOLD_B, stroke_width=4.0)

            # 2. Setengah Lingkaran (Semicircle, diameter = w => radius = w/2)
            c2 = np.array([centers_x[1], base_y, 0.0])
            angles = np.linspace(0, PI, 32)
            semi_pts = [c2 + np.array([(w / 2) * np.cos(a), (w / 2) * np.sin(a), 0.0]) for a in angles]
            semi = Polygon(
                *semi_pts,
                fill_color=BLUE_C, fill_opacity=0.5,
                stroke_color=WHITE, stroke_width=2.0,
            )
            base2 = Line(c2 + LEFT * w / 2, c2 + RIGHT * w / 2, color=GOLD_B, stroke_width=4.0)

            # 3. Segitiga Sama Sisi (Equilateral Triangle, tinggi = (sqrt(3)/2)*w)
            c3 = np.array([centers_x[2], base_y, 0.0])
            tri_h = (np.sqrt(3) / 2.0) * w
            tri = Polygon(
                c3 + LEFT * w / 2,
                c3 + RIGHT * w / 2,
                c3 + UP * tri_h,
                fill_color=MAROON_B, fill_opacity=0.5,
                stroke_color=WHITE, stroke_width=2.0,
            )
            base3 = Line(c3 + LEFT * w / 2, c3 + RIGHT * w / 2, color=GOLD_B, stroke_width=4.0)

            return VGroup(sq, base1, semi, base2, tri, base3)

        sections_dyn = always_redraw(lambda: make_three_sections(x_tr.get_value()))

        # Label tetap di bawah masing-masing bentuk penampang
        lbl_sq = VGroup(
            Tex(r"\textbf{1. Persegi}", font_size=16, color=TEAL_B),
            MathTex(r"A(x) = s^2", font_size=17, color=WHITE),
            MathTex(r"V = \int_0^4 x\,dx = 8", font_size=15, color=TEAL_A),
        ).arrange(DOWN, buff=0.06).move_to([centers_x[0], -0.65, 0])

        lbl_semi = VGroup(
            Tex(r"\textbf{2. $\frac{1}{2}$ Lingkaran}", font_size=16, color=BLUE_B),
            MathTex(r"A(x) = \frac{\pi}{8}s^2", font_size=17, color=WHITE),
            MathTex(r"V = \frac{\pi}{8}\int_0^4 x\,dx = \pi", font_size=15, color=BLUE_A),
        ).arrange(DOWN, buff=0.06).move_to([centers_x[1], -0.65, 0])

        lbl_tri = VGroup(
            Tex(r"\textbf{3. $\triangle$ Sama Sisi}", font_size=16, color=MAROON_A),
            MathTex(r"A(x) = \frac{\sqrt{3}}{4}s^2", font_size=17, color=WHITE),
            MathTex(r"V = \frac{\sqrt{3}}{4}\int_0^4 x\,dx = 2\sqrt{3}", font_size=15, color=MAROON_A),
        ).arrange(DOWN, buff=0.06).move_to([centers_x[2], -0.65, 0])

        eq_base_s = MathTex(
            r"\text{Tali busur alas: } s(x) = y_{\text{atas}} - y_{\text{bawah}} = \sqrt{x} \implies [s(x)]^2 = x",
            font_size=16, color=GOLD_B,
        ).next_to(ax_base, DOWN, buff=0.14)

        self.add(chord_group, sections_dyn)
        self.play(
            FadeIn(lbl_sq), FadeIn(lbl_semi), FadeIn(lbl_tri),
            Write(eq_base_s),
            run_time=1.1,
        )
        self.play(x_tr.animate.set_value(3.85), run_time=2.8, rate_func=smooth)
        self.play(x_tr.animate.set_value(2.5), run_time=1.2, rate_func=smooth)
        self.wait(0.8)

        # =============================================================
        # BABAK 3: Inversi Sokratik - Mengapa setengah lingkaran berpengali pi/8?
        # =============================================================
        tanya = Text(
            "Pertanyaan Sokratik: Mengapa luas setengah lingkaran berdiameter s adalah (π/8)s², bukan (π/2)s²?",
            font_size=18, color=TEAL_A, weight=BOLD,
        ).to_edge(UP, buff=0.18)
        self.play(Transform(judul, tanya), run_time=1.0)
        self.wait(2.5)  # Jeda refleksi Sokratik

        # =============================================================
        # BABAK 4: Kristalisasi - Rumus Umum Lempeng & Kamus Faktor Bentuk
        # =============================================================
        judul4 = Text(
            "Kristalisasi Subbab 5.2.b: Volume Metode Irisan Sejajar V = ∫ A(x) dx",
            font_size=19, color=GOLD_B, weight=BOLD,
        ).to_edge(UP, buff=0.18)

        summary_card = VGroup(
            MathTex(
                r"\textbf{Rumus Umum Lempeng (\textit{Slabs}):} \quad \Delta V \approx A(x)\,\Delta x \implies V = \int_{a}^{b} A(x)\,dx",
                font_size=18, color=GOLD_B,
            ),
            Tex(
                r"$\star$ Untuk setengah lingkaran berdiameter $s$: jari-jarinya adalah $r = \frac{1}{2}s$, sehingga "
                r"$A = \frac{1}{2}\pi r^2 = \frac{1}{2}\pi\left(\frac{s}{2}\right)^2 = \mathbf{\frac{\pi}{8}s^2}$!",
                font_size=16, color=WHITE,
            ),
        ).arrange(DOWN, buff=0.08).to_edge(DOWN, buff=0.15)

        summary_box = SurroundingRectangle(
            summary_card, color=GOLD_B, fill_color=CARD_BG, fill_opacity=0.96, buff=0.13, corner_radius=0.08
        )

        self.play(
            Transform(judul, judul4),
            FadeIn(summary_box), Write(summary_card),
            run_time=1.5,
        )
        self.play(Circumscribe(lbl_semi[1], color=GOLD_A, time_width=0.6), run_time=1.3)
        self.wait(3.0)
