"""
Template: Teorema Dasar Kalkulus Kedua (MA1101 Subtopik 4.4)
Subtopik: 4.4 Teorema Dasar Kalkulus Kedua dan Metode Substitusi
Bahasa: Indonesia
Gaya: Grant Sanderson (3Blue1Brown) & Metode Sokratik
Deskripsi:
  Visualisasi 4 babak mengapa  int_a^b f(x) dx = F(b) - F(a)  untuk SEBARANG antiturunan F,
  melalui pendekatan  A(x) = F(x) + C.
  Fungsi: f(t) = t^2/2 - 2t + 3 = (t - 2)^2/2 + 1  (selalu positif), selang [a, b] = [1, 4].
  Antiturunan sederhana: F(x) = x^3/6 - x^2 + 3x,  F(1) = 13/6,  F(4) = 20/3.
  Fungsi akumulasi:      A(x) = int_1^x f(t) dt = F(x) - 13/6.
  Jawaban:               int_1^4 f(t) dt = 20/3 - 13/6 = 9/2.

  Babak 1 (Dilema)      : luas pada [1, 4] lewat limit jumlah Riemann itu melelahkan. Adakah jalan pintas?
  Babak 2 (Eksplorasi)  : batas atas dijadikan peubah -> A(x) ditelusuri; antiturunan F(x) digambar.
                          Garis singgung A dan F di x yang sama selalu sejajar (A' = f = F').
  Babak 3 (Inversi)     : celah tegak F(x) - A(x) konstan -> A(x) = F(x) + C. Berapa C? Petunjuk A(1) = 0.
  Babak 4 (Kristalisasi): F digeser turun sejauh F(1) hingga berimpit dengan A; kenaikan F dari 1 ke 4
                          sama dengan luas yang diarsir; antiturunan lain G = F + 2 punya kenaikan sama
                          (konstanta saling menghapus)  ->  int_a^b f(x) dx = F(b) - F(a) = [F(x)]_a^b.

Render:
  ../scripts/preview_scene.sh 25_second_fundamental_theorem_of_calculus.py SecondFTCScene -s
"""

from manim import *
import numpy as np


A_START = 1.0
B_END = 4.0


def f_func(t):
    return 0.5 * t ** 2 - 2.0 * t + 3.0


def F_func(x):
    return x ** 3 / 6.0 - x ** 2 + 3.0 * x


F_A = F_func(A_START)          # 13/6
F_B = F_func(B_END)            # 20/3
EXACT = F_B - F_A              # 9/2


def A_func(x):
    return F_func(x) - F_A


G_SHIFT = 2.0


def G_func(x):
    return F_func(x) + G_SHIFT


CARD_BG = "#141B28"


class SecondFTCScene(Scene):
    def construct(self):
        # Pemeriksaan numerik (menjaga konsistensi angka di layar)
        assert abs(F_A - 13.0 / 6.0) < 1e-12 and abs(F_B - 20.0 / 3.0) < 1e-12
        assert abs(EXACT - 4.5) < 1e-12

        # =============================================================
        # TATA LETAK: sumbu f (atas-kiri), sumbu A & F (bawah-kiri), kartu (kanan)
        # =============================================================
        ax_f = Axes(
            x_range=[0, 4.7, 1],
            y_range=[0, 5.5, 1],
            x_length=6.4,
            y_length=2.75,
            axis_config={"color": GRAY_C, "stroke_width": 1.5, "include_tip": False},
        ).add_coordinates(font_size=14)
        ax_f.move_to(LEFT * 3.2 + UP * 1.0)

        ax_A = Axes(
            x_range=[0, 4.7, 1],
            y_range=[-3, 12, 3],
            x_length=6.4,
            y_length=2.75,
            axis_config={"color": GRAY_C, "stroke_width": 1.5, "include_tip": False},
        ).add_coordinates(font_size=14)
        ax_A.move_to(LEFT * 3.2 + DOWN * 2.25)

        lbl_t = MathTex("t", font_size=20, color=GRAY_B).next_to(ax_f.x_axis.get_end(), RIGHT, buff=0.08)
        lbl_x = MathTex("x", font_size=20, color=GRAY_B).next_to(ax_A.x_axis.get_end(), RIGHT, buff=0.08)

        graph_f = ax_f.plot(f_func, x_range=[0, 4.6], color=YELLOW, stroke_width=3.4)
        graph_f_lbl = MathTex(r"y = f(t)", font_size=22, color=YELLOW).next_to(
            ax_f.c2p(0.15, 4.9), RIGHT, buff=0.1
        )
        formula_f = MathTex(r"f(t) = \tfrac{1}{2}t^2 - 2t + 3", font_size=20, color=YELLOW).next_to(
            graph_f_lbl, DOWN, aligned_edge=LEFT, buff=0.1
        )

        # =============================================================
        # BABAK 1: Dilema - Haruskah selalu lewat limit jumlah Riemann?
        # =============================================================
        judul = Text(
            "Berapa luas di bawah f pada selang [1, 4]?\nHaruskah kita selalu menghitung limit jumlah Riemann?",
            font_size=22, line_spacing=1.15, color=WHITE,
        ).to_edge(UP, buff=0.2)

        self.play(Write(judul), run_time=1.6)
        self.play(Create(ax_f), FadeIn(lbl_t), run_time=1.0)
        self.play(Create(graph_f), Write(graph_f_lbl), FadeIn(formula_f), run_time=1.3)

        target_area = ax_f.get_area(graph_f, x_range=[A_START, B_END], color=BLUE_D, opacity=0.35)
        a_mark = MathTex("a=1", font_size=18, color=GRAY_A).next_to(ax_f.c2p(A_START, 0), UP + LEFT, buff=0.05)
        b_mark = MathTex("b=4", font_size=18, color=GRAY_A).next_to(ax_f.c2p(B_END, 0), UP + RIGHT, buff=0.05)
        q_int = MathTex(r"\int_1^4 f(t)\,dt = \;?", font_size=30, color=BLUE_B).move_to(RIGHT * 3.75 + UP * 1.6)
        self.play(FadeIn(target_area), FadeIn(a_mark), FadeIn(b_mark), Write(q_int), run_time=1.2)
        self.wait(1.0)

        def riemann_sum(n):
            dx = (B_END - A_START) / n
            return sum(f_func(A_START + (i + 0.5) * dx) for i in range(n)) * dx

        def riemann(n):
            sw = 1.2 if n <= 8 else 0.5
            return ax_f.get_riemann_rectangles(
                graph_f, x_range=[A_START, B_END], dx=(B_END - A_START) / n,
                input_sample_type="center", stroke_width=sw, stroke_color=WHITE,
                fill_opacity=0.55, color=(BLUE_D, TEAL_C),
            )

        def riemann_card(n):
            rows = VGroup(
                MathTex(rf"n = {n}", font_size=24, color=WHITE),
                MathTex(rf"\sum_{{i=1}}^{{{n}}} f(\bar t_i)\,\Delta t \approx {riemann_sum(n):.4f}",
                        font_size=24, color=TEAL_B),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.15).move_to(RIGHT * 3.75 + UP * 0.1)
            return rows

        rects = riemann(4)
        r_card = riemann_card(4)
        self.play(FadeOut(target_area), Create(rects), FadeIn(r_card), run_time=1.3)
        self.wait(0.8)
        for n in [8, 16, 48]:
            self.play(Transform(rects, riemann(n)), Transform(r_card, riemann_card(n)), run_time=1.0)
            self.wait(0.5)

        lelah = Text("Tiap fungsi baru = rumus jumlah baru...\nmelelahkan!", font_size=18,
                     color=MAROON_B, line_spacing=1.1).move_to(RIGHT * 3.75 + DOWN * 1.3)
        self.play(FadeIn(lelah, shift=UP * 0.15), run_time=0.8)
        self.wait(2.0)
        self.play(FadeOut(rects), FadeOut(r_card), FadeOut(lelah), FadeOut(q_int), run_time=1.0)

        # =============================================================
        # BABAK 2: Eksplorasi - fungsi akumulasi A(x) dan antiturunan F(x)
        # =============================================================
        judul2 = Text(
            "Ide: jadikan batas atas peubah, lalu amati fungsi akumulasinya",
            font_size=22, color=WHITE,
        ).to_edge(UP, buff=0.3)
        self.play(Transform(judul, judul2), run_time=1.0)

        x_tr = ValueTracker(A_START + 0.001)

        area = always_redraw(lambda: ax_f.get_area(
            graph_f, x_range=[A_START, max(x_tr.get_value(), A_START + 0.002)], color=BLUE_D, opacity=0.4
        ))
        x_line = always_redraw(lambda: DashedLine(
            ax_f.c2p(x_tr.get_value(), 0), ax_f.c2p(x_tr.get_value(), 5.3),
            color=WHITE, stroke_width=1.5, dash_length=0.08,
        ))
        x_lbl = always_redraw(lambda: MathTex("x", font_size=20, color=WHITE).next_to(
            ax_f.c2p(x_tr.get_value(), 5.3), UP, buff=0.04
        ))

        graph_A = always_redraw(lambda: ax_A.plot(
            A_func, x_range=[A_START, max(x_tr.get_value(), A_START + 0.01)], color=BLUE_C, stroke_width=3.6
        ))
        dot_A = always_redraw(lambda: Dot(ax_A.c2p(x_tr.get_value(), A_func(x_tr.get_value())),
                                          color=BLUE_A, radius=0.055))
        link = always_redraw(lambda: DashedLine(
            ax_f.c2p(x_tr.get_value(), 0),
            ax_A.c2p(x_tr.get_value(), A_func(x_tr.get_value())),
            color=GRAY_B, stroke_width=1.0, stroke_opacity=0.5, dash_length=0.06,
        ))

        # Kartu telemetri (kanan)
        def readout(tex, color, getter, decimals=3):
            lbl = MathTex(tex, font_size=24, color=color)
            num = DecimalNumber(getter(), num_decimal_places=decimals, font_size=24, color=color)
            num.next_to(lbl, RIGHT, buff=0.12)
            num.add_updater(lambda m: m.set_value(getter()).next_to(lbl, RIGHT, buff=0.12))
            return VGroup(lbl, num)

        defn_A = MathTex(r"A(x) = \int_1^{x} f(t)\,dt", font_size=26, color=BLUE_B)
        r_x = readout(r"x =", WHITE, lambda: x_tr.get_value(), 2)
        r_A = readout(r"A(x) =", BLUE_B, lambda: A_func(x_tr.get_value()))
        card = VGroup(defn_A, r_x, r_A).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        card.move_to(RIGHT * 3.75 + UP * 1.55)

        self.play(Create(ax_A), FadeIn(lbl_x), Write(card), FadeIn(area), Create(x_line), FadeIn(x_lbl),
                  run_time=1.3)
        self.add(graph_A, link, dot_A)
        graph_A_lbl = MathTex(r"y = A(x)", font_size=22, color=BLUE_C).next_to(
            ax_A.c2p(2.6, A_func(2.6)), DOWN + RIGHT, buff=0.05
        )
        self.play(x_tr.animate.set_value(B_END), run_time=5.0, rate_func=smooth)
        self.play(Write(graph_A_lbl), run_time=0.7)
        self.wait(1.0)

        # Antiturunan F
        judul2b = Text(
            "Kita juga punya antiturunan yang mudah dari f:",
            font_size=22, color=WHITE,
        ).to_edge(UP, buff=0.3)
        graph_F = ax_A.plot(F_func, x_range=[0, 4.6], color=TEAL_C, stroke_width=3.4)
        F_formula = MathTex(r"F(x) = \tfrac{x^3}{6} - x^2 + 3x", font_size=26, color=TEAL_C)
        r_F = readout(r"F(x) =", TEAL_C, lambda: F_func(x_tr.get_value()))
        F_rows = VGroup(F_formula, r_F).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        F_rows.next_to(card, DOWN, aligned_edge=LEFT, buff=0.3)
        graph_F_lbl = MathTex(r"y = F(x)", font_size=22, color=TEAL_C).next_to(
            ax_A.c2p(3.0, F_func(3.0)), UP + LEFT, buff=0.08
        )
        dot_F = always_redraw(lambda: Dot(ax_A.c2p(x_tr.get_value(), F_func(x_tr.get_value())),
                                          color=TEAL_A, radius=0.055))
        self.play(Transform(judul, judul2b), run_time=0.9)
        self.play(Create(graph_F), Write(graph_F_lbl), Write(F_rows), FadeIn(dot_F), run_time=1.6)
        self.wait(1.5)

        # Garis singgung sejajar
        def tangent_seg(func, xv, color, length=1.3):
            p = ax_A.c2p(xv, func(xv))
            q = ax_A.c2p(xv + 0.3, func(xv) + 0.3 * f_func(xv))
            d = (q - p) / np.linalg.norm(q - p)
            return Line(p - d * length / 2, p + d * length / 2, color=color, stroke_width=3.2)

        tan_A = always_redraw(lambda: tangent_seg(A_func, x_tr.get_value(), RED_C))
        tan_F = always_redraw(lambda: tangent_seg(F_func, x_tr.get_value(), RED_C))

        judul2c = Text(
            "Bandingkan kemiringan A dan F pada x yang sama...",
            font_size=22, color=WHITE,
        ).to_edge(UP, buff=0.3)
        slope_note = MathTex(
            r"A'(x) = f(x)", r"\;\;(\text{TDK I})", r"\qquad F'(x) = f(x)",
            font_size=24,
        ).move_to(RIGHT * 3.75 + DOWN * 1.15)
        slope_note[0].set_color(BLUE_B)
        slope_note[1].set_color(GRAY_B)
        slope_note[2].set_color(TEAL_C)
        self.play(Transform(judul, judul2c), FadeIn(tan_A), FadeIn(tan_F), run_time=1.0)
        self.play(x_tr.animate.set_value(2.0), run_time=2.5, rate_func=smooth)
        self.play(Write(slope_note), run_time=1.0)
        self.play(x_tr.animate.set_value(3.6), run_time=2.5, rate_func=smooth)
        sejajar = Text("Garis singgungnya selalu sejajar!", font_size=19, color=RED_B).next_to(
            slope_note, DOWN, buff=0.2
        )
        self.play(FadeIn(sejajar, shift=UP * 0.1), run_time=0.7)
        self.wait(1.8)

        # =============================================================
        # BABAK 3: Inversi Sokratik - celahnya konstan; berapa C?
        # =============================================================
        gap_arrow = always_redraw(lambda: DoubleArrow(
            ax_A.c2p(x_tr.get_value(), A_func(x_tr.get_value())),
            ax_A.c2p(x_tr.get_value(), F_func(x_tr.get_value())),
            buff=0.0, color=GOLD_B, stroke_width=3, tip_length=0.14, max_tip_length_to_length_ratio=0.3,
        ))
        r_gap = readout(r"F(x) - A(x) =", GOLD_B, lambda: F_func(x_tr.get_value()) - A_func(x_tr.get_value()))
        r_gap.move_to(RIGHT * 3.75 + DOWN * 1.15)

        judul3 = Text(
            "Kemiringan sama  ⇒  celah tegak antara F dan A tetap!",
            font_size=22, color=GOLD_A,
        ).to_edge(UP, buff=0.3)
        self.play(Transform(judul, judul3), FadeOut(tan_A), FadeOut(tan_F), FadeOut(sejajar),
                  FadeOut(slope_note), run_time=1.0)
        self.add(gap_arrow)
        self.play(FadeIn(r_gap), run_time=0.8)
        self.play(x_tr.animate.set_value(1.5), run_time=2.5, rate_func=smooth)
        self.play(x_tr.animate.set_value(4.4), run_time=3.0, rate_func=smooth)
        self.wait(0.8)

        tanya = Text(
            "Jadi A(x) = F(x) + C.  Berapa nilai C?",
            font_size=24, color=TEAL_A, weight=BOLD,
        ).to_edge(UP, buff=0.3)
        self.play(Transform(judul, tanya), run_time=1.0)
        self.wait(2.5)  # jeda refleksi Sokratik

        petunjuk = MathTex(r"\text{Petunjuk: } A(1) = \int_1^{1} f(t)\,dt = \;?", font_size=24, color=WHITE)
        petunjuk.move_to(RIGHT * 3.75 + DOWN * 2.0)
        self.play(Write(petunjuk), x_tr.animate.set_value(A_START), run_time=2.0, rate_func=smooth)
        self.wait(2.0)  # jeda kedua

        jawab = MathTex(
            r"A(1) = 0 = F(1) + C \;\Rightarrow\; C = -F(1) = -\tfrac{13}{6}",
            font_size=22, color=GOLD_B,
        ).move_to(petunjuk.get_center())
        self.play(ReplacementTransform(petunjuk, jawab), run_time=1.2)
        self.wait(2.0)

        # =============================================================
        # BABAK 4: Kristalisasi - A(x) = F(x) - F(a) sehingga int_a^b f = F(b) - F(a)
        # =============================================================
        judul4 = Text(
            "Geser F turun sejauh F(1): grafiknya tepat berimpit dengan A",
            font_size=22, color=WHITE,
        ).to_edge(UP, buff=0.3)
        self.play(Transform(judul, judul4), FadeOut(gap_arrow), FadeOut(dot_F), run_time=1.0)

        full_A = ax_A.plot(A_func, x_range=[0, 4.6], color=BLUE_C, stroke_width=3.6)
        shift_vec = ax_A.c2p(0, 0) - ax_A.c2p(0, F_A)
        F_moving = graph_F.copy()
        graph_F.set_stroke(opacity=0.35)
        self.play(F_moving.animate.shift(shift_vec), run_time=2.5, rate_func=smooth)
        self.play(Create(full_A), run_time=1.0)
        self.play(FadeOut(F_moving), run_time=0.6)
        self.wait(1.0)

        # Tampilkan x = b = 4
        self.play(x_tr.animate.set_value(B_END), run_time=2.5, rate_func=smooth)
        graph_F.set_stroke(opacity=1.0)

        judul4b = Text(
            "Luas pada [1, 4] = kenaikan F dari x = 1 ke x = 4",
            font_size=22, color=WHITE,
        ).to_edge(UP, buff=0.3)

        # Kenaikan F (segmen tegak merah) pada grafik F asli
        p1 = ax_A.c2p(A_START, F_A)
        p_corner = ax_A.c2p(B_END, F_A)
        p4 = ax_A.c2p(B_END, F_B)
        run_line = DashedLine(p1, p_corner, color=GRAY_A, stroke_width=1.6, dash_length=0.07)
        rise_line = Line(p_corner, p4, color=RED_C, stroke_width=5)
        rise_brace = Brace(rise_line, direction=RIGHT, buff=0.08, color=RED_B)
        rise_lbl = MathTex(r"F(4) - F(1)", font_size=20, color=RED_B).next_to(rise_brace, RIGHT, buff=0.06)
        dots_F = VGroup(Dot(p1, color=TEAL_A, radius=0.06), Dot(p4, color=TEAL_A, radius=0.06))

        area_lbl = MathTex(r"\tfrac{9}{2}", font_size=28, color=WHITE).move_to(ax_f.c2p(2.5, 0.6))

        self.play(Transform(judul, judul4b), FadeIn(dots_F), Create(run_line), run_time=1.0)
        self.play(Create(rise_line), GrowFromCenter(rise_brace), Write(rise_lbl), run_time=1.3)
        self.play(Write(area_lbl), Indicate(rise_line, color=RED_A), run_time=1.3)

        hitung = MathTex(
            r"F(4) - F(1) = \tfrac{20}{3} - \tfrac{13}{6} = \tfrac{9}{2}",
            font_size=24, color=RED_B,
        ).move_to(RIGHT * 3.75 + DOWN * 1.15)
        self.play(FadeOut(r_gap), FadeOut(jawab), Write(hitung), run_time=1.2)
        self.wait(2.0)

        # Antiturunan lain G = F + 2: kenaikannya sama
        judul4c = Text(
            "Antiturunan lain, G(x) = F(x) + 2? Kenaikannya sama: C saling menghapus",
            font_size=20, color=WHITE,
        ).to_edge(UP, buff=0.3)
        graph_G = ax_A.plot(G_func, x_range=[0, 4.4], color=GREEN_C, stroke_width=3.0)
        graph_G_lbl = MathTex(r"y = G(x)", font_size=20, color=GREEN_C).next_to(
            ax_A.c2p(1.9, G_func(1.9)), UP + LEFT, buff=0.05
        )
        g_shift = ax_A.c2p(0, G_SHIFT) - ax_A.c2p(0, 0)
        rise_G = rise_line.copy().set_color(GREEN_B).shift(g_shift + LEFT * 0.08)
        run_G = run_line.copy().shift(g_shift)
        cancel = MathTex(
            r"\big(F(4) + 2\big) - \big(F(1) + 2\big) = F(4) - F(1)",
            font_size=20, color=GREEN_B,
        ).next_to(hitung, DOWN, buff=0.22)
        self.play(Transform(judul, judul4c), Create(graph_G), Write(graph_G_lbl), run_time=1.5)
        self.play(Create(run_G), Create(rise_G), run_time=1.0)
        self.play(Write(cancel), run_time=1.3)
        self.wait(2.0)

        # Kartu teorema akhir
        judul_final = Text(
            "Teorema Dasar Kalkulus Kedua",
            font_size=26, color=GOLD_B, weight=BOLD,
        ).to_edge(UP, buff=0.3)
        teorema = VGroup(
            MathTex(r"\int_a^b f(x)\,dx = F(b) - F(a) = \Big[F(x)\Big]_a^b", font_size=28, color=WHITE),
            Tex(r"$f$ kontinu pada $[a,b]$, $F$ antiturunan \emph{sebarang} dari $f$",
                font_size=22, color=GRAY_A),
        ).arrange(DOWN, buff=0.2)
        teorema.move_to(RIGHT * 3.6 + UP * 0.4)
        teorema_box = SurroundingRectangle(teorema, color=GOLD_B, fill_color=CARD_BG, fill_opacity=0.96,
                                           buff=0.2, corner_radius=0.1)
        # pastikan kartu tetap di dalam bingkai
        overflow = teorema_box.get_right()[0] - (config.frame_width / 2 - 0.15)
        if overflow > 0:
            VGroup(teorema_box, teorema).shift(LEFT * overflow)

        self.play(
            Transform(judul, judul_final),
            FadeOut(card), FadeOut(F_rows), FadeOut(hitung), FadeOut(cancel),
            run_time=1.0,
        )
        self.play(FadeIn(teorema_box), Write(teorema), run_time=1.8)
        self.play(Circumscribe(teorema[0], color=GOLD_A, time_width=0.6), run_time=1.6)
        self.wait(3.0)
