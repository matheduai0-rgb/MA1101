"""
Template: Aturan Parabolik / Simpson & Batas Galat (MA1101 Subtopik 4.6)
Subtopik: 4.6 Integrasi Numerik
Bahasa: Indonesia
Gaya: Grant Sanderson (3Blue1Brown) & Metode Sokratik
Deskripsi:
  Visualisasi 4 babak untuk Aturan Parabolik (Aturan Simpson, S_n):
  Mengapa kita memasangkan 2 subselang (3 titik) dengan busur parabola P_2(x),
  mengapa n WAJIB genap, dan bagaimana muncul pola koefisien 1 - 4 - 2 - 4 - ... - 4 - 1.
  Fungsi uji: f(x) = 2 + sin(x) + 0.15*x^2 pada [a, b] = [0, 4], n = 4 (h = 1).
    - Pasangan parabola 1 pada [0, 2] melalui (x_0, y_0), (x_1, y_1), (x_2, y_2):
        Luas_1 = (h/3) * (y_0 + 4*y_1 + y_2)
    - Pasangan parabola 2 pada [2, 4] melalui (x_2, y_2), (x_3, y_3), (x_4, y_4):
        Luas_2 = (h/3) * (y_2 + 4*y_3 + y_4)
    - Total S_4 = (h/3) * (y_0 + 4*y_1 + 2*y_2 + 4*y_3 + y_4).

  Babak 1 (Dilema)      : Garis lurus trapesium kaku mengikuti kurva melengkung.
                          Bagaimana jika kita memakai busur parabola? Berapa titik menentukan 1 parabola?
  Babak 2 (Eksplorasi)  : Keping parabola 1 pada [0, 2] (bobot 1-4-1) dan keping parabola 2 pada [2, 4]
                          (bobot 1-4-1) dijumlahkan -> titik batas dalam x_2 mendapat bobot 1+1 = 2!
  Babak 3 (Inversi)     : Mengapa n pada Aturan Simpson WAJIB genap?
                          Dan mengapa S_n bernilai EKSAK (galat = 0) untuk polinom derajat <= 3?
  Babak 4 (Kristalisasi): Rumus lengkap S_n dan batas galat |E_{S_n}| <= M_4(b-a)^5 / (180 n^4).

Render:
  ../scripts/preview_scene.sh 29_simpsons_parabolic_rule.py SimpsonsParabolicRuleScene -s
"""

from manim import *
import numpy as np


A_START = 0.0
B_END = 4.0
N_SUB = 4
H_STEP = 1.0
CARD_BG = "#141B28"


def f_func(x):
    return 1.8 + 1.1 * np.sin(1.1 * x) + 0.12 * (x - 1.5) ** 2


def lagrange_parabola(x0, y0, x1, y1, x2, y2):
    def p(x):
        l0 = ((x - x1) * (x - x2)) / ((x0 - x1) * (x0 - x2))
        l1 = ((x - x0) * (x - x2)) / ((x1 - x0) * (x1 - x2))
        l2 = ((x - x0) * (x - x1)) / ((x2 - x0) * (x2 - x1))
        return y0 * l0 + y1 * l1 + y2 * l2
    return p


class SimpsonsParabolicRuleScene(Scene):
    def construct(self):
        xs = [A_START + i * H_STEP for i in range(N_SUB + 1)]
        ys = [f_func(x) for x in xs]

        p1 = lagrange_parabola(xs[0], ys[0], xs[1], ys[1], xs[2], ys[2])
        p2 = lagrange_parabola(xs[2], ys[2], xs[3], ys[3], xs[4], ys[4])

        # =============================================================
        # TATA LETAK: Sumbu utama di kiri, kartu Sokratik di kanan
        # =============================================================
        ax = Axes(
            x_range=[-0.3, 4.4, 1],
            y_range=[0, 4.2, 1],
            x_length=6.2,
            y_length=4.5,
            axis_config={"color": GRAY_C, "stroke_width": 1.6, "include_tip": False},
        ).add_coordinates(font_size=15)
        ax.move_to(LEFT * 3.2 + DOWN * 0.35)

        lbl_x = MathTex("x", font_size=21, color=GRAY_B).next_to(ax.x_axis.get_end(), RIGHT, buff=0.08)
        lbl_y = MathTex("y", font_size=21, color=GRAY_B).next_to(ax.y_axis.get_end(), UP, buff=0.08)

        graph_f = ax.plot(f_func, x_range=[0.0, 4.15], color=YELLOW, stroke_width=3.8)
        graph_lbl = MathTex(r"y = f(x)", font_size=22, color=YELLOW).next_to(
            ax.c2p(1.3, f_func(1.3)), UP, buff=0.18
        )

        # Garis vertikal dan titik simpul x_0 .. x_4
        v_lines = VGroup()
        dots = VGroup()
        x_tags = VGroup()
        for i, (xv, yv) in enumerate(zip(xs, ys)):
            v_lines.add(DashedLine(ax.c2p(xv, 0), ax.c2p(xv, yv), color=GRAY_B, stroke_width=1.5, dash_length=0.07))
            dots.add(Dot(ax.c2p(xv, yv), color=WHITE, radius=0.06))
            x_tags.add(MathTex(rf"y_{i}", font_size=19, color=WHITE).next_to(ax.c2p(xv, yv), UP, buff=0.1))

        # =============================================================
        # BABAK 1: Dilema - Dari Garis Lurus ke Busur Parabola (3 Titik)
        # =============================================================
        judul = Text(
            "Aturan Parabolik (Simpson): mengganti tutup garis lurus dengan busur parabola!",
            font_size=20, color=WHITE,
        ).to_edge(UP, buff=0.22)

        self.play(Write(judul), run_time=1.4)
        self.play(Create(ax), FadeIn(lbl_x), FadeIn(lbl_y), run_time=0.9)
        self.play(Create(graph_f), Write(graph_lbl), Create(v_lines), FadeIn(dots), FadeIn(x_tags), run_time=1.3)

        card_b1 = VGroup(
            Tex(r"\textbf{Ide Dasar Aturan Simpson:}", font_size=21, color=GOLD_B),
            Tex(r"Satu parabola $P_2(x) = Ax^2 + Bx + C$ ditentukan", font_size=18, color=GRAY_A),
            Tex(r"secara tunggal oleh \textbf{3 titik} (2 subselang).", font_size=18, color=WHITE),
            MathTex(
                r"\int_{x_{2i-2}}^{x_{2i}} P_2(x)\,dx = \frac{h}{3}\big(y_{2i-2} + 4y_{2i-1} + y_{2i}\big)",
                font_size=20, color=TEAL_B,
            ),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.12).move_to(RIGHT * 3.55 + UP * 1.65)
        box_b1 = SurroundingRectangle(
            card_b1, color=TEAL_C, fill_color=CARD_BG, fill_opacity=0.94, buff=0.16, corner_radius=0.09
        )
        self.play(FadeIn(box_b1), Write(card_b1), run_time=1.3)
        self.wait(1.2)

        # =============================================================
        # BABAK 2: Eksplorasi - Menyusun Pasangan Parabola & Bobot 1-4-2-4-1
        # =============================================================
        judul2 = Text(
            "Pasangan 1 pada [x₀, x₂] dan Pasangan 2 pada [x₂, x₄]: perhatikan bobot di x₂!",
            font_size=20, color=TEAL_A,
        ).to_edge(UP, buff=0.22)

        parab1_curve = ax.plot(p1, x_range=[xs[0], xs[2]], color=TEAL_B, stroke_width=3.6)
        parab1_area = ax.get_area(parab1_curve, x_range=[xs[0], xs[2]], color=TEAL_D, opacity=0.42)

        parab2_curve = ax.plot(p2, x_range=[xs[2], xs[4]], color=BLUE_B, stroke_width=3.6)
        parab2_area = ax.get_area(parab2_curve, x_range=[xs[2], xs[4]], color=BLUE_D, opacity=0.42)

        eq_pair1 = MathTex(
            r"A_1 = \frac{h}{3}\big(\mathbf{1}\,y_0 + \mathbf{4}\,y_1 + \mathbf{1}\,y_2\big)",
            font_size=20, color=TEAL_B,
        )
        eq_pair2 = MathTex(
            r"A_2 = \frac{h}{3}\big(\mathbf{1}\,y_2 + \mathbf{4}\,y_3 + \mathbf{1}\,y_4\big)",
            font_size=20, color=BLUE_B,
        )
        eq_sum = MathTex(
            r"S_4 = \frac{h}{3}\big(\mathbf{1}\,y_0 + \mathbf{4}\,y_1 + \mathbf{2}\,y_2 + \mathbf{4}\,y_3 + \mathbf{1}\,y_4\big)",
            font_size=20, color=GOLD_B,
        )
        weights_group = VGroup(eq_pair1, eq_pair2, eq_sum).arrange(
            DOWN, aligned_edge=LEFT, buff=0.14
        ).move_to(RIGHT * 3.55 + DOWN * 0.25)

        self.play(Transform(judul, judul2), run_time=0.9)
        self.play(FadeIn(parab1_area), Create(parab1_curve), Write(eq_pair1), run_time=1.3)
        self.wait(0.8)
        self.play(FadeIn(parab2_area), Create(parab2_curve), Write(eq_pair2), run_time=1.3)
        self.wait(0.8)

        # Label bobot 1 - 4 - 2 - 4 - 1 langsung pada sumbu-x
        w_vals = ["1", "4", "2", "4", "1"]
        w_cols = [GRAY_A, GOLD_B, RED_B, GOLD_B, GRAY_A]
        w_badges = VGroup()
        for xv, w_str, col in zip(xs, w_vals, w_cols):
            b = MathTex(rf"\times {w_str}", font_size=20, color=col).next_to(ax.c2p(xv, 0), DOWN, buff=0.52)
            w_badges.add(b)

        self.play(
            Write(eq_sum),
            FadeIn(w_badges, shift=UP * 0.1),
            Indicate(dots[2], color=RED_A, scale_factor=1.5),
            run_time=1.4,
        )
        self.wait(1.6)

        # =============================================================
        # BABAK 3: Inversi Sokratik - Mengapa n wajib genap & derajat 3 eksak?
        # =============================================================
        tanya = Text(
            "Pertanyaan Sokratik: Mengapa jumlah subselang n WAJIB genap pada Aturan Simpson?",
            font_size=20, color=TEAL_A, weight=BOLD,
        ).to_edge(UP, buff=0.22)
        self.play(Transform(judul, tanya), run_time=1.0)
        self.wait(2.5)  # Jeda refleksi Sokratik

        # =============================================================
        # BABAK 4: Kristalisasi - Rumus Umum S_n & Batas Galat O(1/n^4)
        # =============================================================
        judul4 = Text(
            "Kristalisasi: Aturan Parabolik (Simpson) & Batas Galat Orde Keempat O(1/n⁴)",
            font_size=20, color=GOLD_B, weight=BOLD,
        ).to_edge(UP, buff=0.22)

        final_card = VGroup(
            Tex(r"\textbf{Aturan Parabolik / Simpson ($n$ genap):}", font_size=20, color=GOLD_B),
            MathTex(
                r"S_n = \frac{b-a}{3n}\Big[y_0 + 4y_1 + 2y_2 + 4y_3 + \dots + 2y_{n-2} + 4y_{n-1} + y_n\Big]",
                font_size=18, color=WHITE,
            ),
            MathTex(
                r"|E_{S_n}| \le \frac{M_4\,(b-a)^5}{180\,n^4}, \qquad |f^{(4)}(x)| \le M_4",
                font_size=21, color=TEAL_B,
            ),
            Tex(
                r"$\star$ Jika $n$ digandakan ($2\times$), batas galat turun $\mathbf{16\times}$! "
                r"Eksak ($E_S=0$) untuk polinom derajat $\le 3$.",
                font_size=17, color=GREEN_B,
            ),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.12).move_to(RIGHT * 3.55 + DOWN * 2.15)
        final_box = SurroundingRectangle(
            final_card, color=GOLD_B, fill_color=CARD_BG, fill_opacity=0.96, buff=0.16, corner_radius=0.09
        )

        overflow = final_box.get_right()[0] - (config.frame_width / 2 - 0.15)
        if overflow > 0:
            VGroup(final_box, final_card).shift(LEFT * overflow)

        self.play(
            Transform(judul, judul4),
            FadeIn(final_box), Write(final_card),
            run_time=1.6,
        )
        self.play(Circumscribe(final_card[2], color=GOLD_A, time_width=0.6), run_time=1.4)
        self.wait(3.0)
