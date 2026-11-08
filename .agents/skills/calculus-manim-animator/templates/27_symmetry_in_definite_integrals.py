"""
Template: Penggunaan Simetri pada Integral Tentu (MA1101 Subtopik 4.5)
Subtopik: 4.5 Teorema Nilai Rata-rata untuk Integral dan Penggunaan Simetri
Bahasa: Indonesia
Gaya: Grant Sanderson (3Blue1Brown) & Metode Sokratik
Deskripsi:
  Visualisasi 4 babak untuk Teorema Simetri Integral Tentu pada selang simetris [-a, a]:
    - Fungsi Genap (f(-x) = f(x))  : int_{-a}^a f(x) dx = 2 int_0^a f(x) dx
      Contoh visual: f(x) = x^4 - 2x^2 + 2 pada [-2, 2]  =>  2 * 76/15 = 152/15 ≈ 10.13.
    - Fungsi Ganjil (f(-x) = -f(x)): int_{-a}^a g(x) dx = 0
      Contoh visual: g(x) = x^3 - 3x pada [-2, 2]        =>  (+2) + (-2) = 0.

  Babak 1 (Dilema)      : Menghadapi integral campuran pada [-2, 2]:
                          int_{-2}^2 (x^3 cos x + x^3 - 3x + x^4 - 2x^2 + 2) dx.
                          Apakah semua suku harus dicari antiturunannya?
  Babak 2 (Eksplorasi)  : Dua panel berdampingan (Genap di kiri, Ganjil di kanan).
                          Titik uji serempak -x dan +x menunjukkan f(-x) = f(x) vs g(-x) = -g(x).
                          Pelipatan cermin daerah [-2, 0] ke [0, 2] menggandakan luas fungsi genap
                          dan saling menghapuskan luas bertanda fungsi ganjil.
  Babak 3 (Inversi)     : Mengapa selang HARUS simetris [-a, a]? Bagaimana jika batasnya [-1, 2]?
  Babak 4 (Kristalisasi): Bukti aljabar u = -x, pemecahan cepat integral dilema Babak 1,
                          dan ringkasan Teorema Simetri.

Render:
  ../scripts/preview_scene.sh 27_symmetry_in_definite_integrals.py SymmetryDefiniteIntegralScene -s
"""

from manim import *
import numpy as np


A_LIM = 2.0
CARD_BG = "#141B28"


def f_even(x):
    # Fungsi genap selalu positif pada [-2, 2]: minimum di x = +-1 bernilai 1, di +-2 bernilai 10
    # Diskalakan dengan faktor 1/2 agar pas di sumbu: f(x) = 0.5*(x^4 - 2x^2 + 2)
    return 0.5 * (x ** 4 - 2.0 * x ** 2 + 2.0)


def g_odd(x):
    # Fungsi ganjil pada [-2, 2]: g(x) = 0.5*(x^3 - 3x)
    # int_0^2 0.5*(x^3 - 3x) dx = 0.5 * [x^4/4 - 3x^2/2]_0^2 = 0.5 * (4 - 6) = -1.0
    # int_{-2}^0 0.5*(x^3 - 3x) dx = +1.0
    return 0.5 * (x ** 3 - 3.0 * x)


class SymmetryDefiniteIntegralScene(Scene):
    def construct(self):
        # =============================================================
        # BABAK 1: Dilema - Integral tampak rumit pada selang [-2, 2]
        # =============================================================
        judul = Text(
            "Haruskah kita mencari antiturunan tiap suku pada selang simetris [-2, 2]?",
            font_size=21, color=WHITE,
        ).to_edge(UP, buff=0.2)

        dilema_eq = MathTex(
            r"\int_{-2}^{2} \Big(",
            r"\underbrace{x^3\cos x + \tfrac{1}{2}(x^3 - 3x)}_{\text{Fungsi Ganjil}}",
            r"+",
            r"\underbrace{\tfrac{1}{2}(x^4 - 2x^2 + 2)}_{\text{Fungsi Genap}}",
            r"\Big)\,dx = \;?",
            font_size=24,
        ).next_to(judul, DOWN, buff=0.16)
        dilema_eq[1].set_color(MAROON_B)
        dilema_eq[3].set_color(TEAL_C)

        self.play(Write(judul), run_time=1.3)
        self.play(FadeIn(dilema_eq, shift=DOWN * 0.1), run_time=1.3)
        self.wait(1.2)

        # =============================================================
        # TATA LETAK DUA PANEL: Kiri = Fungsi Genap, Kanan = Fungsi Ganjil
        # =============================================================
        ax_even = Axes(
            x_range=[-2.3, 2.3, 1],
            y_range=[-0.8, 5.5, 1],
            x_length=5.6,
            y_length=3.15,
            axis_config={"color": GRAY_C, "stroke_width": 1.5, "include_tip": False},
        ).add_coordinates(font_size=13)
        ax_even.move_to(LEFT * 3.45 + DOWN * 0.25)

        ax_odd = Axes(
            x_range=[-2.3, 2.3, 1],
            y_range=[-2.2, 2.2, 1],
            x_length=5.6,
            y_length=3.15,
            axis_config={"color": GRAY_C, "stroke_width": 1.5, "include_tip": False},
        ).add_coordinates(font_size=13)
        ax_odd.move_to(RIGHT * 3.45 + DOWN * 0.25)

        hdr_even = MathTex(
            r"\text{Fungsi Genap: } f(-x) = f(x)", font_size=22, color=TEAL_C
        ).next_to(ax_even, UP, buff=0.12)
        hdr_odd = MathTex(
            r"\text{Fungsi Ganjil: } g(-x) = -g(x)", font_size=22, color=MAROON_B
        ).next_to(ax_odd, UP, buff=0.12)

        curve_even = ax_even.plot(f_even, x_range=[-2.0, 2.0], color=YELLOW, stroke_width=3.5)
        curve_odd = ax_odd.plot(g_odd, x_range=[-2.0, 2.0], color=YELLOW, stroke_width=3.5)

        lbl_f = MathTex(r"f(x) = \tfrac{1}{2}(x^4 - 2x^2 + 2)", font_size=18, color=YELLOW).move_to(
            ax_even.c2p(1.12, 4.55)
        )
        lbl_g = MathTex(r"g(x) = \tfrac{1}{2}(x^3 - 3x)", font_size=18, color=YELLOW).move_to(
            ax_odd.c2p(-1.15, 1.8)
        )

        # Geser persamaan dilema ke pojok atau perkecil
        self.play(
            FadeOut(dilema_eq),
            Create(ax_even), Create(ax_odd),
            Write(hdr_even), Write(hdr_odd),
            run_time=1.2,
        )
        self.play(
            Create(curve_even), Create(curve_odd),
            FadeIn(lbl_f), FadeIn(lbl_g),
            run_time=1.3,
        )

        # =============================================================
        # BABAK 2: Eksplorasi - Penelusuran cermin -x dan +x
        # =============================================================
        judul2 = Text(
            "Bandingkan nilai fungsi pada pasangan titik simetris -x dan +x",
            font_size=21, color=WHITE,
        ).to_edge(UP, buff=0.2)
        self.play(Transform(judul, judul2), run_time=0.9)

        x_tr = ValueTracker(0.25)

        # Batang pengukur di -x dan +x untuk fungsi genap
        bars_even = always_redraw(lambda: VGroup(
            Line(ax_even.c2p(-x_tr.get_value(), 0), ax_even.c2p(-x_tr.get_value(), f_even(-x_tr.get_value())),
                 color=TEAL_B, stroke_width=3.5),
            Line(ax_even.c2p(x_tr.get_value(), 0), ax_even.c2p(x_tr.get_value(), f_even(x_tr.get_value())),
                 color=TEAL_B, stroke_width=3.5),
            Dot(ax_even.c2p(-x_tr.get_value(), f_even(-x_tr.get_value())), color=TEAL_A, radius=0.055),
            Dot(ax_even.c2p(x_tr.get_value(), f_even(x_tr.get_value())), color=TEAL_A, radius=0.055),
        ))

        # Batang pengukur di -x dan +x untuk fungsi ganjil
        bars_odd = always_redraw(lambda: VGroup(
            Line(ax_odd.c2p(-x_tr.get_value(), 0), ax_odd.c2p(-x_tr.get_value(), g_odd(-x_tr.get_value())),
                 color=BLUE_B, stroke_width=3.5),
            Line(ax_odd.c2p(x_tr.get_value(), 0), ax_odd.c2p(x_tr.get_value(), g_odd(x_tr.get_value())),
                 color=MAROON_B, stroke_width=3.5),
            Dot(ax_odd.c2p(-x_tr.get_value(), g_odd(-x_tr.get_value())), color=BLUE_A, radius=0.055),
            Dot(ax_odd.c2p(x_tr.get_value(), g_odd(x_tr.get_value())), color=RED_A, radius=0.055),
        ))

        # Arsir dinamis dari 0 ke x dan -x ke 0
        area_even_left = always_redraw(lambda: ax_even.get_area(
            curve_even, x_range=[-x_tr.get_value(), 0.0], color=TEAL_D, opacity=0.38
        ))
        area_even_right = always_redraw(lambda: ax_even.get_area(
            curve_even, x_range=[0.0, x_tr.get_value()], color=TEAL_B, opacity=0.38
        ))

        area_odd_left = always_redraw(lambda: ax_odd.get_area(
            curve_odd, x_range=[-x_tr.get_value(), 0.0], color=BLUE_D, opacity=0.42
        ))
        area_odd_right = always_redraw(lambda: ax_odd.get_area(
            curve_odd, x_range=[0.0, x_tr.get_value()], color=MAROON_B, opacity=0.42
        ))

        self.add(area_even_left, area_even_right, area_odd_left, area_odd_right, bars_even, bars_odd)
        self.play(x_tr.animate.set_value(A_LIM), run_time=3.6, rate_func=smooth)
        self.wait(0.8)

        # Animasi pelipatan cermin (mirror fold) pada [-2, 0] -> [0, 2]
        fold_copy_even = ax_even.get_area(curve_even, x_range=[-2.0, 0.0], color=GOLD_B, opacity=0.45)
        fold_copy_odd = ax_odd.get_area(curve_odd, x_range=[-2.0, 0.0], color=BLUE_C, opacity=0.5)

        judul2b = Text(
            "Lipat daerah kiri [-2, 0] ke kanan [0, 2]: menggandakan vs saling menghapus!",
            font_size=20, color=GOLD_B,
        ).to_edge(UP, buff=0.2)
        self.play(Transform(judul, judul2b), FadeIn(fold_copy_even), FadeIn(fold_copy_odd), run_time=0.8)

        # Lipat genap terhadap sumbu-y, dan putar ganjil 180 derajat terhadap titik asalax_odd.c2p(0,0)
        self.play(
            fold_copy_even.animate.stretch(-1, 0, about_point=ax_even.c2p(0, 0)),
            Rotate(fold_copy_odd, angle=PI, about_point=ax_odd.c2p(0, 0)),
            run_time=2.2,
            rate_func=smooth,
        )

        res_even = MathTex(
            r"\int_{-2}^{2} f(x)\,dx = 2\int_{0}^{2} f(x)\,dx = \frac{76}{15}",
            font_size=21, color=TEAL_B,
        ).next_to(ax_even, DOWN, buff=0.28)

        res_odd = MathTex(
            r"\int_{-2}^{2} g(x)\,dx = (+1) + (-1) = 0",
            font_size=21, color=MAROON_B,
        ).next_to(ax_odd, DOWN, buff=0.28)

        self.play(Write(res_even), Write(res_odd), FadeOut(fold_copy_even), FadeOut(fold_copy_odd), run_time=1.2)
        self.wait(1.5)

        # =============================================================
        # BABAK 3: Inversi Sokratik - Mengapa selang harus simetris [-a, a]?
        # =============================================================
        tanya = Text(
            "Pertanyaan Sokratik: Apakah integral fungsi ganjil pada [-1, 2] juga bernilai 0?",
            font_size=20, color=TEAL_A, weight=BOLD,
        ).to_edge(UP, buff=0.2)

        self.play(Transform(judul, tanya), run_time=1.0)
        self.wait(2.5)  # Jeda refleksi Sokratik

        # Tunjukkan bahwa pada [-1, 2], bagian [-1, 1] saling menghapus tetapi [1, 2] tersisa!
        unbalanced_highlight = ax_odd.get_area(curve_odd, x_range=[1.0, 2.0], color=GOLD_B, opacity=0.75)
        warn_odd = MathTex(
            r"\int_{-1}^{2} g(x)\,dx = \underbrace{\int_{-1}^{1} g}_{=\,0} + \int_{1}^{2} g(x)\,dx \neq 0!",
            font_size=20, color=GOLD_B,
        ).move_to(res_odd.get_center())

        self.play(
            FadeIn(unbalanced_highlight),
            ReplacementTransform(res_odd, warn_odd),
            run_time=1.3,
        )
        self.wait(1.8)
        self.play(FadeOut(unbalanced_highlight), run_time=0.6)

        # =============================================================
        # BABAK 4: Kristalisasi - Rumus Teorema Simetri & Solusi Cepat Dilema
        # =============================================================
        judul4 = Text(
            "Teorema Simetri Integral Tentu (via Substitusi u = -x pada [-a, 0])",
            font_size=21, color=GOLD_B, weight=BOLD,
        ).to_edge(UP, buff=0.2)

        card_even_final = VGroup(
            MathTex(r"f(-x) = f(x) \;\text{(Genap)}:", font_size=20, color=TEAL_B),
            MathTex(r"\int_{-a}^{a} f(x)\,dx = 2\int_{0}^{a} f(x)\,dx", font_size=23, color=WHITE),
        ).arrange(DOWN, buff=0.08).move_to(res_even.get_center() + DOWN * 0.08)
        box_even = SurroundingRectangle(
            card_even_final, color=TEAL_C, fill_color=CARD_BG, fill_opacity=0.95, buff=0.14, corner_radius=0.08
        )

        card_odd_final = VGroup(
            MathTex(r"g(-x) = -g(x) \;\text{(Ganjil)}:", font_size=20, color=MAROON_B),
            MathTex(r"\int_{-a}^{a} g(x)\,dx = 0", font_size=23, color=WHITE),
        ).arrange(DOWN, buff=0.08).move_to(warn_odd.get_center() + DOWN * 0.08)
        box_odd = SurroundingRectangle(
            card_odd_final, color=MAROON_B, fill_color=CARD_BG, fill_opacity=0.95, buff=0.14, corner_radius=0.08
        )

        self.play(
            Transform(judul, judul4),
            FadeOut(res_even), FadeOut(warn_odd),
            FadeIn(box_even), Write(card_even_final),
            FadeIn(box_odd), Write(card_odd_final),
            run_time=1.5,
        )
        self.play(
            Circumscribe(card_even_final[1], color=TEAL_A, time_width=0.6),
            Circumscribe(card_odd_final[1], color=RED_A, time_width=0.6),
            run_time=1.4,
        )
        self.wait(3.0)
