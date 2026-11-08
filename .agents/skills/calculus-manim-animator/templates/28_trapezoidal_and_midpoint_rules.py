"""
Template: Aturan Trapesium & Aturan Titik Tengah (MA1101 Subtopik 4.6)
Subtopik: 4.6 Integrasi Numerik
Bahasa: Indonesia
Gaya: Grant Sanderson (3Blue1Brown) & Metode Sokratik
Deskripsi:
  Visualisasi 4 babak untuk membandingkan Jumlah Riemann Kiri/Kanan (L_n, R_n),
  Aturan Trapesium (T_n), dan Aturan Titik Tengah (M_n) beserta peran kecekungan f''(x).
  Fungsi uji cekung ke atas: f(x) = x^2 / 4 + 1/2 pada selang [a, b] = [0, 4], n = 4 (h = 1).
  Nilai eksak: int_0^4 (x^2/4 + 1/2) dx = [x^3/12 + x/2]_0^4 = 16/3 + 2 = 22/3 ≈ 7.3333.
  Pada n = 4 (h = 1):
    - L_4 = 0.5 + 0.75 + 1.5 + 2.75 = 5.5000          (E_L = +1.8333)
    - R_4 = 0.75 + 1.5 + 2.75 + 4.5 = 9.5000          (E_R = -2.1667)
    - T_4 = (h/2)[y_0 + 2y_1 + 2y_2 + 2y_3 + y_4] = 7.5000 (E_T = -1/6 ≈ -0.1667, overestimate)
    - M_4 = h[f(0.5)+f(1.5)+f(2.5)+f(3.5)] = 7.2500   (E_M = +1/12 ≈ +0.0833, underestimate)

  Babak 1 (Dilema)      : Banyak integral (mis. int e^{-x^2} dx) tak punya antiturunan elementer.
                          Mengapa persegi panjang kiri/kanan (L_n, R_n) menyisakan segitiga galat besar?
  Babak 2 (Eksplorasi)  : Dua cara meruncingkan hampiran pada tiap pias:
                          (1) Aturan Trapesium T_n: hubungkan titik ujung dengan tali busur sekan.
                          (2) Aturan Titik Tengah M_n: ambil tinggi di titik tengah, lalu putar tutup
                              mendatarnya menjadi trapesium garis singgung (luasnya tetap sama!).
  Babak 3 (Inversi)     : Manakah yang lebih akurat: Trapesium T_4 atau Titik Tengah M_4?
                          Bagaimana kecekungan f'' > 0 menentukan arah kelebihan/kekurangan?
  Babak 4 (Kristalisasi): Tabel perbandingan galat |E_M| ≈ (1/2)|E_T| dan rumus umum T_n, M_n
                          beserta batas galat O(1/n^2).

Render:
  ../scripts/preview_scene.sh 28_trapezoidal_and_midpoint_rules.py TrapezoidalMidpointScene -s
"""

from manim import *
import numpy as np


A_START = 0.0
B_END = 4.0
N_SUB = 4
H_STEP = (B_END - A_START) / N_SUB  # 1.0
EXACT_VAL = 22.0 / 3.0              # 7.3333...

CARD_BG = "#141B28"


def f_func(x):
    return 0.25 * (x ** 2) + 0.5


def df_func(x):
    return 0.5 * x


class TrapezoidalMidpointScene(Scene):
    def construct(self):
        xs = [A_START + i * H_STEP for i in range(N_SUB + 1)]
        mids = [A_START + (i + 0.5) * H_STEP for i in range(N_SUB)]

        L4 = H_STEP * sum(f_func(x) for x in xs[:-1])
        R4 = H_STEP * sum(f_func(x) for x in xs[1:])
        T4 = 0.5 * H_STEP * (f_func(xs[0]) + 2.0 * sum(f_func(x) for x in xs[1:-1]) + f_func(xs[-1]))
        M4 = H_STEP * sum(f_func(m) for m in mids)

        assert abs(L4 - 5.5) < 1e-12 and abs(R4 - 9.5) < 1e-12
        assert abs(T4 - 7.5) < 1e-12 and abs(M4 - 7.25) < 1e-12

        # =============================================================
        # TATA LETAK: Sumbu utama di kiri, panel kartu Sokratik di kanan
        # =============================================================
        ax = Axes(
            x_range=[-0.3, 4.4, 1],
            y_range=[0, 5.2, 1],
            x_length=6.3,
            y_length=4.7,
            axis_config={"color": GRAY_C, "stroke_width": 1.6, "include_tip": False},
        ).add_coordinates(font_size=15)
        ax.move_to(LEFT * 3.15 + DOWN * 0.45)

        lbl_x = MathTex("x", font_size=21, color=GRAY_B).next_to(ax.x_axis.get_end(), RIGHT, buff=0.08)
        lbl_y = MathTex("y", font_size=21, color=GRAY_B).next_to(ax.y_axis.get_end(), UP, buff=0.08)

        graph_f = ax.plot(f_func, x_range=[0.0, 4.15], color=YELLOW, stroke_width=3.8)
        graph_lbl = MathTex(r"f(x) = \tfrac{1}{4}x^2 + \tfrac{1}{2}", font_size=22, color=YELLOW).move_to(
            ax.c2p(1.45, 3.65)
        )

        # =============================================================
        # BABAK 1: Dilema - Keterbatasan Persegi Panjang Kiri/Kanan
        # =============================================================
        judul = Text(
            "Jika antiturunan tidak ditemukan, bagaimana menghampiri integral dengan akurat?",
            font_size=20, color=WHITE,
        ).to_edge(UP, buff=0.22)

        self.play(Write(judul), run_time=1.4)
        self.play(Create(ax), FadeIn(lbl_x), FadeIn(lbl_y), run_time=0.9)
        self.play(Create(graph_f), Write(graph_lbl), run_time=1.2)

        rects_left = ax.get_riemann_rectangles(
            graph_f, x_range=[A_START, B_END], dx=H_STEP,
            input_sample_type="left", stroke_width=1.4, stroke_color=WHITE,
            fill_opacity=0.35, color=BLUE_D,
        )
        card_b1 = VGroup(
            MathTex(r"I = \int_0^4 \left(\tfrac{1}{4}x^2 + \tfrac{1}{2}\right)dx = \frac{22}{3} \approx 7{,}3333",
                    font_size=21, color=YELLOW),
            MathTex(r"L_4 = h\sum_{i=0}^{3} f(x_i) = 5{,}5000 \;\;(\text{kurang } 1{,}83)",
                    font_size=20, color=BLUE_B),
            MathTex(r"R_4 = h\sum_{i=1}^{4} f(x_i) = 9{,}5000 \;\;(\text{lebih } 2{,}17)",
                    font_size=20, color=MAROON_B),
            Text("Tutup mendatar kiri/kanan menyisakan\nsegitiga galat yang besar!", font_size=17,
                 color=GRAY_A, line_spacing=1.15),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.16).move_to(RIGHT * 3.55 + UP * 0.9)

        self.play(Create(rects_left), FadeIn(card_b1), run_time=1.3)
        self.wait(1.4)

        # =============================================================
        # BABAK 2: Eksplorasi - Aturan Trapesium (T_4) vs Titik Tengah (M_4)
        # =============================================================
        judul2 = Text(
            "Ide 1 (Aturan Trapesium T_n): hubungkan titik ujung dengan tali busur lurus",
            font_size=20, color=TEAL_B,
        ).to_edge(UP, buff=0.22)

        trapezoids = VGroup()
        secant_tops = VGroup()
        node_dots = VGroup()
        for i in range(N_SUB):
            x0, x1 = xs[i], xs[i + 1]
            y0, y1 = f_func(x0), f_func(x1)
            trap = Polygon(
                ax.c2p(x0, 0), ax.c2p(x0, y0), ax.c2p(x1, y1), ax.c2p(x1, 0),
                stroke_color=TEAL_B, stroke_width=1.8, fill_color=TEAL_D, fill_opacity=0.38,
            )
            trapezoids.add(trap)
            secant_tops.add(Line(ax.c2p(x0, y0), ax.c2p(x1, y1), color=TEAL_A, stroke_width=3.0))
        for x in xs:
            node_dots.add(Dot(ax.c2p(x, f_func(x)), color=TEAL_A, radius=0.055))

        card_trap = VGroup(
            Tex(r"\textbf{Aturan Trapesium ($T_n$)}", font_size=22, color=TEAL_B),
            MathTex(r"T_n = \frac{h}{2}\Big[y_0 + 2y_1 + 2y_2 + \dots + 2y_{n-1} + y_n\Big]",
                    font_size=20, color=WHITE),
            MathTex(r"\text{Pola bobot: } 1 - 2 - 2 - \dots - 2 - 1", font_size=19, color=TEAL_A),
            MathTex(r"T_4 = \frac{1}{2}(L_4 + R_4) = 7{,}5000 \;\;(E_{T_4} = -0{,}1667)",
                    font_size=20, color=GOLD_B),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.14).move_to(RIGHT * 3.55 + UP * 1.45)
        box_trap = SurroundingRectangle(
            card_trap, color=TEAL_C, fill_color=CARD_BG, fill_opacity=0.94, buff=0.16, corner_radius=0.09
        )

        self.play(
            Transform(judul, judul2),
            ReplacementTransform(rects_left, trapezoids),
            Create(secant_tops),
            FadeIn(node_dots),
            FadeOut(card_b1),
            FadeIn(box_trap), Write(card_trap),
            run_time=1.5,
        )
        self.wait(1.6)

        # Sekarang tampilkan Aturan Titik Tengah M_4 dan putar tutupnya menjadi garis singgung!
        judul2b = Text(
            "Ide 2 (Aturan Titik Tengah M_n): putar tutup persegi panjang menjadi garis singgung!",
            font_size=20, color=GOLD_B,
        ).to_edge(UP, buff=0.22)

        mid_rects = VGroup()
        tangent_traps = VGroup()
        mid_dots = VGroup()
        for m in mids:
            x0, x1 = m - 0.5 * H_STEP, m + 0.5 * H_STEP
            ym = f_func(m)
            slope = df_func(m)
            y_left_tan = ym - 0.5 * H_STEP * slope
            y_right_tan = ym + 0.5 * H_STEP * slope

            r_rect = Polygon(
                ax.c2p(x0, 0), ax.c2p(x0, ym), ax.c2p(x1, ym), ax.c2p(x1, 0),
                stroke_color=GOLD_B, stroke_width=1.8, fill_color=BLUE_D, fill_opacity=0.32,
            )
            t_trap = Polygon(
                ax.c2p(x0, 0), ax.c2p(x0, y_left_tan), ax.c2p(x1, y_right_tan), ax.c2p(x1, 0),
                stroke_color=GOLD_B, stroke_width=2.0, fill_color=BLUE_D, fill_opacity=0.32,
            )
            mid_rects.add(r_rect)
            tangent_traps.add(t_trap)
            mid_dots.add(Dot(ax.c2p(m, ym), color=RED_A, radius=0.06))

        card_mid = VGroup(
            Tex(r"\textbf{Aturan Titik Tengah ($M_n$)}", font_size=22, color=GOLD_B),
            MathTex(r"M_n = h\sum_{i=1}^{n} f(\bar{x}_i), \quad \bar{x}_i = \frac{x_{i-1}+x_i}{2}",
                    font_size=20, color=WHITE),
            Tex(r"Segitiga kiri \& kanan saling menambal $\Rightarrow$", font_size=18, color=GRAY_A),
            Tex(r"Luas persegi panjang $=$ Luas trapesium singgung!", font_size=18, color=GOLD_A),
            MathTex(r"M_4 = 7{,}2500 \;\;(E_{M_4} = +0{,}0833)", font_size=20, color=GREEN_B),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.12).move_to(RIGHT * 3.55 + DOWN * 1.45)
        box_mid = SurroundingRectangle(
            card_mid, color=GOLD_B, fill_color=CARD_BG, fill_opacity=0.94, buff=0.16, corner_radius=0.09
        )

        # Redupkan trapesium sekan agar trapesium garis singgung terlihat jelas
        self.play(
            Transform(judul, judul2b),
            trapezoids.animate.set_fill(opacity=0.12).set_stroke(opacity=0.35),
            FadeIn(mid_rects), FadeIn(mid_dots),
            FadeIn(box_mid), Write(card_mid),
            run_time=1.4,
        )
        self.wait(1.0)
        # Animasi kunci: memutar tutup persegi panjang titik tengah menjadi trapesium garis singgung!
        self.play(Transform(mid_rects, tangent_traps), run_time=2.0, rate_func=smooth)
        self.wait(1.5)

        # =============================================================
        # BABAK 3: Inversi Sokratik - Mengapa |E_M| = (1/2)|E_T|?
        # =============================================================
        tanya = Text(
            "Pertanyaan Sokratik: Mengapa galat Titik Tengah (0,083) tepat SETENGAH galat Trapesium (0,167)?",
            font_size=19, color=TEAL_A, weight=BOLD,
        ).to_edge(UP, buff=0.22)
        self.play(Transform(judul, tanya), run_time=1.0)
        self.wait(2.5)  # Jeda refleksi Sokratik

        # =============================================================
        # BABAK 4: Kristalisasi - Rumus & Batas Galat O(1/n^2)
        # =============================================================
        judul4 = Text(
            "Kristalisasi: Aturan Trapesium & Titik Tengah (Orde Konvergensi O(1/n²))",
            font_size=21, color=GOLD_B, weight=BOLD,
        ).to_edge(UP, buff=0.22)

        summary_card = VGroup(
            Tex(r"\textbf{Perbandingan Galat pada Kurva Cekung ke Atas ($f'' > 0$):}", font_size=19, color=GOLD_B),
            MathTex(r"\bullet\;\; T_n \text{ (tali busur di atas kurva)}: \text{kelebihan } (E_{T_n} < 0)",
                    font_size=19, color=TEAL_B),
            MathTex(r"\bullet\;\; M_n \text{ (garis singgung di bawah kurva)}: \text{kekurangan } (E_{M_n} > 0)",
                    font_size=19, color=GREEN_B),
            MathTex(
                r"|E_{T_n}| \le \frac{M_2(b-a)^3}{12n^2}, \qquad |E_{M_n}| \le \frac{M_2(b-a)^3}{24n^2}",
                font_size=21, color=WHITE,
            ),
            Tex(r"dengan $|f''(x)| \le M_2$ pada $[a, b]$ dan $h = \dfrac{b-a}{n}$", font_size=18, color=GRAY_A),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.13).move_to(RIGHT * 3.55 + DOWN * 1.55)
        summary_box = SurroundingRectangle(
            summary_card, color=GOLD_B, fill_color=CARD_BG, fill_opacity=0.96, buff=0.16, corner_radius=0.09
        )

        overflow = summary_box.get_right()[0] - (config.frame_width / 2 - 0.15)
        if overflow > 0:
            VGroup(summary_box, summary_card).shift(LEFT * overflow)

        self.play(
            Transform(judul, judul4),
            FadeOut(box_mid), FadeOut(card_mid),
            FadeIn(summary_box), Write(summary_card),
            run_time=1.5,
        )
        self.play(Circumscribe(summary_card[3], color=GOLD_A, time_width=0.6), run_time=1.4)
        self.wait(3.0)
