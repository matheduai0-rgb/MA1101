"""
Template: Teorema Dasar Kalkulus Pertama (MA1101 Subtopik 4.3)
Subtopik: 4.3 Teorema Dasar Kalkulus Pertama (The First Fundamental Theorem of Calculus)
Bahasa: Indonesia
Gaya: Grant Sanderson (3Blue1Brown) & Metode Sokratik
Deskripsi:
  Visualisasi 4 babak mengenai fungsi akumulasi A(x) = int_0^x f(t) dt untuk
  f(t) = t^2/2 - 3t + 4 = (t - 2)(t - 4)/2 pada [0, 5].
  Dua sistem sumbu bertumpuk: atas memperlihatkan luas bertanda di bawah f,
  bawah menelusuri grafik A(x) = x^3/6 - 3x^2/2 + 4x secara reaktif.

  Babak 1 (Tantangan) : luas menumpuk saat garis-x bergerak -> seberapa CEPAT bertambah?
  Babak 2 (Eksplorasi) : grafik A naik / turun / naik mengikuti tanda f; pita tipis
                         selebar h memiliki luas ~ f(x) * h.
  Babak 3 (Inversi)    : apa yang terjadi pada [A(x+h) - A(x)] / h saat h -> 0?
                         garis singgung A: kemiringan A'(x) = tinggi f(x).
  Babak 4 (Kristalisasi): TDK I  d/dx int_a^x f(t) dt = f(x)  + varian aturan rantai.

Render:
  ../scripts/preview_scene.sh 22_first_fundamental_theorem_of_calculus.py FirstFTCAccumulationScene -s
"""

from manim import *
import numpy as np


def f_func(t):
    return 0.5 * t ** 2 - 3.0 * t + 4.0


def A_func(x):
    return x ** 3 / 6.0 - 1.5 * x ** 2 + 4.0 * x


CARD_BG = "#141B28"


class FirstFTCAccumulationScene(Scene):
    def construct(self):
        # =============================================================
        # BABAK 1: Tantangan Sokratik (Luas yang Terus Menumpuk)
        # =============================================================
        judul = Text(
            "Luas di bawah f dari 0 sampai x bergantung pada x.\nSeberapa CEPAT luas itu bertambah ketika x bergeser?",
            font_size=22,
            line_spacing=1.15,
            color=WHITE,
        ).to_edge(UP, buff=0.22)

        ax_f = Axes(
            x_range=[0, 5.4, 1],
            y_range=[-1, 4.5, 1],
            x_length=7.2,
            y_length=2.85,
            axis_config={"color": GRAY_C, "stroke_width": 1.5, "include_tip": False},
        ).add_coordinates(font_size=14)
        ax_f.move_to(LEFT * 2.75 + UP * 0.95)

        ax_A = Axes(
            x_range=[0, 5.4, 1],
            y_range=[0, 4.2, 1],
            x_length=7.2,
            y_length=2.3,
            axis_config={"color": GRAY_C, "stroke_width": 1.5, "include_tip": False},
        ).add_coordinates(font_size=14)
        ax_A.move_to(LEFT * 2.75 + DOWN * 2.4)

        lbl_f_ax = MathTex("t", font_size=20, color=GRAY_B).next_to(ax_f.x_axis.get_end(), RIGHT, buff=0.08)
        lbl_A_ax = MathTex("x", font_size=20, color=GRAY_B).next_to(ax_A.x_axis.get_end(), RIGHT, buff=0.08)

        graph_f = ax_f.plot(f_func, x_range=[0, 5.2], color=YELLOW, stroke_width=3.4)
        graph_f_lbl = MathTex(r"y = f(t)", font_size=22, color=YELLOW).next_to(ax_f.c2p(0.35, 4.0), RIGHT, buff=0.15)

        x_tr = ValueTracker(0.01)
        h_tr = ValueTracker(0.0)

        def seg(a, b, col, op=0.45):
            if b - a < 1e-3:
                return VMobject()
            return ax_f.get_area(graph_f, x_range=[a, b], color=col, opacity=op)

        def acc_area():
            xv = x_tr.get_value()
            return VGroup(
                seg(0.0, min(xv, 2.0), BLUE_D),
                seg(2.0, min(xv, 4.0), MAROON_B, 0.55),
                seg(4.0, xv, BLUE_D),
            )

        area = always_redraw(acc_area)
        x_line = always_redraw(lambda: DashedLine(
            ax_f.c2p(x_tr.get_value(), -1.0),
            ax_f.c2p(x_tr.get_value(), 4.3),
            color=WHITE, stroke_width=1.6, dash_length=0.08,
        ))
        x_lbl = always_redraw(lambda: MathTex("x", font_size=22, color=WHITE).next_to(
            ax_f.c2p(x_tr.get_value(), -1.0), DOWN, buff=0.06
        ))

        # Kartu telemetri (kanan)
        def readout(tex, color, getter, decimals=3):
            lbl = MathTex(tex, font_size=24, color=color)
            num = DecimalNumber(getter(), num_decimal_places=decimals, font_size=24, color=color,
                                include_sign=False)
            num.add_updater(lambda m: m.set_value(getter()).next_to(lbl, RIGHT, buff=0.12))
            num.next_to(lbl, RIGHT, buff=0.12)
            return VGroup(lbl, num)

        r_x = readout(r"x =", WHITE, lambda: x_tr.get_value(), 2)
        r_A = readout(r"A(x) =", BLUE_B, lambda: A_func(x_tr.get_value()))
        r_f = readout(r"f(x) =", YELLOW, lambda: f_func(x_tr.get_value()))
        defn = MathTex(r"A(x) = \int_0^{x} f(t)\,dt", font_size=26, color=BLUE_B)
        card_rows = VGroup(defn, r_x, r_A, r_f).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        card_rows.move_to(RIGHT * 3.75 + UP * 1.55)
        card_box = SurroundingRectangle(card_rows, color=BLUE_D, fill_color=CARD_BG, fill_opacity=0.92,
                                        buff=0.2, corner_radius=0.1)
        
        self.play(Write(judul), run_time=1.6)
        self.play(Create(ax_f), FadeIn(lbl_f_ax), run_time=1.0)
        self.play(Create(graph_f), Write(graph_f_lbl), run_time=1.3)
        self.add(area)
        self.play(Create(x_line), FadeIn(x_lbl), FadeIn(card_box), Write(card_rows), run_time=1.3)
        self.wait(0.8)
        self.play(x_tr.animate.set_value(1.5), run_time=4.5, rate_func=smooth)
        self.wait(2.5)

        # =============================================================
        # BABAK 2: Eksplorasi Visual (Grafik A(x) & Pita Tipis)
        # =============================================================
        judul2 = Text(
            "Gambar A(x) sebagai fungsi tersendiri: kapan naik, kapan turun?",
            font_size=22, color=WHITE,
        ).to_edge(UP, buff=0.3)
        self.play(Transform(judul, judul2), run_time=1.0)

        graph_A = always_redraw(lambda: ax_A.plot(
            A_func, x_range=[0, max(x_tr.get_value(), 0.02)], color=TEAL_C, stroke_width=3.4
        ))
        dot_A = always_redraw(lambda: Dot(ax_A.c2p(x_tr.get_value(), A_func(x_tr.get_value())),
                                          color=TEAL_A, radius=0.06))
        link = always_redraw(lambda: DashedLine(
            ax_f.c2p(x_tr.get_value(), -1.0),
            ax_A.c2p(x_tr.get_value(), A_func(x_tr.get_value())),
            color=GRAY_B, stroke_width=1.0, stroke_opacity=0.6, dash_length=0.06,
        ))
        graph_A_lbl = MathTex(r"y = A(x)", font_size=22, color=TEAL_C).next_to(ax_A.c2p(0.25, 3.9), RIGHT, buff=0.1)

        self.play(Create(ax_A), FadeIn(lbl_A_ax), run_time=1.0)
        self.add(graph_A, link, dot_A)
        self.play(Write(graph_A_lbl), run_time=0.8)
        self.wait(0.5)

        self.play(x_tr.animate.set_value(2.0), run_time=3.0, rate_func=smooth)
        note_pos = Text("f > 0  →  luas bertambah  →  A naik", font_size=18, color=BLUE_B)
        note_neg = Text("f < 0  →  luas bertanda berkurang  →  A turun", font_size=18, color=MAROON_B)
        note_pos2 = Text("f > 0 lagi  →  A naik lagi", font_size=18, color=BLUE_B)
        notes = VGroup(note_pos, note_neg, note_pos2).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        notes.move_to(RIGHT * 3.75 + DOWN * 1.2)
        self.play(FadeIn(note_pos, shift=UP * 0.15), run_time=0.8)
        self.wait(1.0)
        prediksi = Text(
            "Prediksi dulu: setelah x = 2, f bernilai negatif. Apa yang terjadi pada A?",
            font_size=22, color=TEAL_A,
        ).to_edge(UP, buff=0.3)
        self.play(Transform(judul, prediksi), run_time=1.0)
        self.wait(2.5)  # waktu berpikir
        self.play(x_tr.animate.set_value(4.0), run_time=5.0, rate_func=smooth)
        self.play(FadeIn(note_neg, shift=UP * 0.15), run_time=0.8)
        self.wait(0.6)
        self.play(x_tr.animate.set_value(5.0), run_time=3.0, rate_func=smooth)
        self.play(FadeIn(note_pos2, shift=UP * 0.15), run_time=0.8)
        self.wait(2.0)

        # Kembali ke x = 1.2 untuk menyelidiki pita tipis
        self.play(FadeOut(notes), x_tr.animate.set_value(1.2), run_time=2.0, rate_func=smooth)

        judul3 = Text(
            "Geser x sedikit sejauh h. Berapa luas pita tipis yang bertambah?",
            font_size=22, color=WHITE,
        ).to_edge(UP, buff=0.3)
        self.play(Transform(judul, judul3), run_time=1.0)
        h_tr.set_value(0.0)

        strip = always_redraw(lambda: seg(x_tr.get_value(), x_tr.get_value() + h_tr.get_value(), RED_C, 0.8))
        rect = always_redraw(lambda: Polygon(
            ax_f.c2p(x_tr.get_value(), 0),
            ax_f.c2p(x_tr.get_value() + h_tr.get_value(), 0),
            ax_f.c2p(x_tr.get_value() + h_tr.get_value(), f_func(x_tr.get_value())),
            ax_f.c2p(x_tr.get_value(), f_func(x_tr.get_value())),
            color=WHITE, stroke_width=1.6, fill_opacity=0,
        ) if h_tr.get_value() > 1e-3 else VMobject())

        def rise_marks():
            xv, hv = x_tr.get_value(), h_tr.get_value()
            if hv < 1e-3:
                return VGroup()
            p0 = ax_A.c2p(xv, A_func(xv))
            p1 = ax_A.c2p(xv + hv, A_func(xv))
            p2 = ax_A.c2p(xv + hv, A_func(xv + hv))
            return VGroup(
                Line(p0, p1, color=GRAY_B, stroke_width=1.6),
                Line(p1, p2, color=RED_C, stroke_width=3.0),
            )

        rise = always_redraw(rise_marks)
        h_lbl = always_redraw(lambda: MathTex("h", font_size=20, color=RED_C).next_to(
            ax_f.c2p(x_tr.get_value() + 0.5 * h_tr.get_value(), 0), DOWN, buff=0.28
        ) if h_tr.get_value() > 0.15 else VMobject())

        self.add(strip, rect, rise, h_lbl)
        self.play(h_tr.animate.set_value(0.8), run_time=1.6, rate_func=smooth)
        self.wait(0.5)

        approx_eq = MathTex(
            r"A(x+h) - A(x)", r"\approx", r"f(x)", r"\cdot", r"h",
            font_size=28,
        )
        approx_eq[0].set_color(RED_C)
        approx_eq[2].set_color(YELLOW)
        approx_eq.move_to(RIGHT * 3.75 + DOWN * 0.75)
        approx_note = Text("luas pita  ≈  persegi panjang (tinggi f(x), lebar h)", font_size=16,
                           color=GRAY_A).next_to(approx_eq, DOWN, buff=0.2)
        self.play(Write(approx_eq), FadeIn(approx_note), run_time=1.5)
        self.wait(1.5)

        self.play(h_tr.animate.set_value(0.12), run_time=4.5, rate_func=smooth)
        approx_note2 = Text("Semakin tipis pita, semakin akurat hampiran ini!", font_size=16,
                            color=GREEN_B).move_to(approx_note)
        self.play(Transform(approx_note, approx_note2), run_time=0.8)
        self.wait(1.5)

        # =============================================================
        # BABAK 3: Inversi Sokratik (Limit h -> 0)
        # =============================================================
        tanya = VGroup(
            Text("Apa yang terjadi pada", font_size=24, color=TEAL_A),
            MathTex(r"\frac{A(x+h)-A(x)}{h}", font_size=30, color=TEAL_A),
            Text("ketika  h → 0 ?", font_size=24, color=TEAL_A),
        ).arrange(RIGHT, buff=0.2).to_edge(UP, buff=0.18)
        self.play(FadeOut(judul), FadeIn(tanya), run_time=1.0)
        self.wait(2.5)  # waktu berpikir

        quot_eq = MathTex(
            r"\frac{A(x+h) - A(x)}{h}", r"\approx", r"f(x)",
            font_size=30,
        ).move_to(approx_eq)
        quot_eq[0].set_color(RED_C)
        quot_eq[2].set_color(YELLOW)
        self.play(TransformMatchingTex(approx_eq, quot_eq), FadeOut(approx_note), run_time=1.5)
        self.wait(1.0)

        lim_eq = MathTex(
            r"A'(x)", r"=", r"\lim_{h \to 0}", r"\frac{A(x+h) - A(x)}{h}", r"=", r"f(x)",
            font_size=28,
        ).move_to(quot_eq)
        lim_eq[0].set_color(TEAL_C)
        lim_eq[3].set_color(RED_C)
        lim_eq[5].set_color(YELLOW)
        self.play(h_tr.animate.set_value(0.0), TransformMatchingTex(quot_eq, lim_eq), run_time=2.0)
        self.remove(strip, rect, rise, h_lbl)
        self.wait(2.0)

        # Garis singgung A: kemiringan = tinggi f
        def tangent():
            xv = x_tr.get_value()
            m = f_func(xv)
            y0 = A_func(xv)
            d = 0.55 / np.sqrt(1 + (m * 2.3 / 4.2 / (7.2 / 5.4)) ** 2)
            return Line(ax_A.c2p(xv - d, y0 - m * d), ax_A.c2p(xv + d, y0 + m * d),
                        color=RED_C, stroke_width=3.0)

        tan_line = always_redraw(tangent)
        f_bar = always_redraw(lambda: Line(
            ax_f.c2p(x_tr.get_value(), 0), ax_f.c2p(x_tr.get_value(), f_func(x_tr.get_value())),
            color=YELLOW, stroke_width=5,
        ))
        r_slope = readout(r"\text{kemiringan } A'(x) =", RED_C, lambda: f_func(x_tr.get_value()))
        r_slope.next_to(r_f, DOWN, aligned_edge=LEFT, buff=0.2)
        card_box2 = SurroundingRectangle(VGroup(card_rows, r_slope), color=BLUE_D, fill_color=CARD_BG,
                                         fill_opacity=0.92, buff=0.2, corner_radius=0.1)
        
        tanya2 = Text("Bandingkan: kemiringan grafik A  vs  tinggi grafik f",
                      font_size=22, color=TEAL_A).to_edge(UP, buff=0.3)
        self.play(FadeOut(tanya), FadeIn(tanya2), Transform(card_box, card_box2), run_time=1.0)
        self.play(Create(tan_line), Create(f_bar), FadeIn(r_slope), run_time=1.2)
        self.wait(1.0)

        self.play(x_tr.animate.set_value(2.0), run_time=3.0, rate_func=smooth)
        mark_max = VGroup(
            Dot(ax_A.c2p(2.0, A_func(2.0)), color=GREEN_B, radius=0.06),
            MathTex(r"f(2)=0 \Rightarrow A \text{ maks. lokal}", font_size=18, color=GREEN_B),
        )
        mark_max[1].next_to(mark_max[0], UP, buff=0.12)
        self.play(FadeIn(mark_max), run_time=0.8)
        self.wait(1.5)

        self.play(x_tr.animate.set_value(3.0), run_time=2.5, rate_func=smooth)
        tanya3 = Text("Di sini f(x) < 0. Apakah A naik atau turun?", font_size=22,
                      color=TEAL_A).to_edge(UP, buff=0.3)
        self.play(Transform(tanya2, tanya3), run_time=0.8)
        self.wait(2.0)
        jawab3 = Text("Kemiringan A negatif: A TURUN, persis selaju f(x).", font_size=22,
                      color=MAROON_B).to_edge(UP, buff=0.3)
        self.play(Transform(tanya2, jawab3), run_time=0.8)
        self.wait(1.5)

        self.play(x_tr.animate.set_value(4.0), run_time=2.5, rate_func=smooth)
        mark_min = VGroup(
            Dot(ax_A.c2p(4.0, A_func(4.0)), color=GREEN_B, radius=0.06),
            MathTex(r"A \text{ min. lokal}", font_size=18, color=GREEN_B),
        )
        mark_min[1].next_to(mark_min[0], DOWN, buff=0.12)
        self.play(FadeIn(mark_min), run_time=0.8)
        self.wait(1.0)
        self.play(x_tr.animate.set_value(4.8), run_time=2.5, rate_func=smooth)
        self.wait(2.0)

        # =============================================================
        # BABAK 4: Kristalisasi Formal (TDK I)
        # =============================================================
        judul4 = Text("Teorema Dasar Kalkulus Pertama", font_size=28, color=GOLD_B).to_edge(UP, buff=0.3)
        self.play(
            FadeOut(tanya2),
            FadeOut(card_box), FadeOut(card_rows), FadeOut(r_slope), FadeOut(lim_eq),
            FadeIn(judul4),
            run_time=1.2,
        )

        hyp = Tex(r"Jika $f$ kontinu pada $[a,b]$ dan $x \in (a,b)$, maka", font_size=24, color=GRAY_A)
        ftc = MathTex(
            r"\frac{d}{dx}\left[\int_a^{x} f(t)\,dt\right]", r"=", r"f(x)",
            font_size=36,
        )
        ftc[0].set_color(BLUE_B)
        ftc[2].set_color(YELLOW)
        ftc_grp = VGroup(hyp, ftc).arrange(DOWN, buff=0.3)
        ftc_grp.move_to(RIGHT * 3.75 + UP * 1.6)
        ftc_box = SurroundingRectangle(ftc_grp, color=GOLD_B, fill_color=CARD_BG, fill_opacity=0.95,
                                       buff=0.22, corner_radius=0.1)
        self.play(FadeIn(ftc_box), Write(hyp), run_time=1.2)
        self.play(Write(ftc), run_time=1.8)
        self.play(Indicate(ftc[2], color=YELLOW), run_time=1.2)
        self.wait(2.0)

        chain_title = Text("Batas atas berupa fungsi g(x)? Aturan Rantai:", font_size=18, color=TEAL_A)
        chain = MathTex(
            r"\frac{d}{dx}\int_a^{g(x)} f(t)\,dt", r"=", r"f\big(g(x)\big)", r"\cdot", r"g'(x)",
            font_size=28,
        )
        chain[2].set_color(YELLOW)
        chain[4].set_color(RED_C)
        moral = Text("Turunan dari akumulasi = laju yang diakumulasi.", font_size=18, color=GREEN_B)
        chain_grp = VGroup(chain_title, chain, moral).arrange(DOWN, buff=0.25)
        chain_grp.move_to(RIGHT * 3.75 + DOWN * 1.3)
        chain_box = SurroundingRectangle(chain_grp, color=TEAL_C, fill_color=CARD_BG, fill_opacity=0.92,
                                         buff=0.2, corner_radius=0.1)
        self.play(FadeIn(chain_box), Write(chain_title), run_time=1.0)
        self.play(Write(chain), run_time=1.8)
        self.wait(1.0)
        self.play(FadeIn(moral, shift=UP * 0.1), run_time=1.0)
        self.wait(4.0)
