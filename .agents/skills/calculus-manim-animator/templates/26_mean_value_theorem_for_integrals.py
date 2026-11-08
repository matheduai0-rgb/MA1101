"""
Template: Teorema Nilai Rata-rata untuk Integral (MA1101 Subtopik 4.5)
Subtopik: 4.5 Teorema Nilai Rata-rata untuk Integral dan Penggunaan Simetri
Bahasa: Indonesia
Gaya: Grant Sanderson (3Blue1Brown) & Metode Sokratik
Deskripsi:
  Visualisasi 4 babak untuk Nilai Rata-rata Fungsi f_bar dan Teorema Nilai Rata-rata untuk Integral:
    f_bar = (1 / (b - a)) int_a^b f(x) dx = f(c)   untuk suatu c in (a, b).
  Fungsi: f(x) = 3x - x^2 + 1 pada selang [a, b] = [0, 3].
  Integral eksak: int_0^3 (3x - x^2 + 1) dx = [3x^2/2 - x^3/3 + x]_0^3 = 27/2 - 9 + 3 = 15/2 = 7.5.
  Lebar selang: b - a = 3  =>  Nilai rata-rata f_bar = (1/3) * 7.5 = 5/2 = 2.5.
  Titik c dengan f(c) = 2.5: 3c - c^2 + 1 = 2.5  <=>  2c^2 - 6c + 3 = 0
    => c_1 = (3 - sqrt(3))/2 ≈ 0.634,   c_2 = (3 + sqrt(3))/2 ≈ 2.366.

  Babak 1 (Dilema)      : Bagaimana merata-ratakan tak hingga banyaknya nilai f(x) pada [0, 3]?
                          Rata-rata sampel diskrit (1/n) sum f(x_i) = (1/(b-a)) sum f(x_i) dx -> integral.
  Babak 2 (Eksplorasi)  : Garis mendatar pengukur tinggi y = h membentuk persegi panjang luas 3h.
                          Saat h digeser naik-turun, amati luas "bukit" (di atas h) vs "lembah" (di bawah h).
  Babak 3 (Inversi)     : Pada tinggi h berapakah luas bukit tepat menambal luas lembah?
                          Apakah kurva kontinu f pasti memotong garis tinggi rata-rata itu?
  Babak 4 (Kristalisasi): Saat h = f_bar = 2.5, luas bukit = luas lembah <=> luas persegi panjang (b-a)f(c)
                          sama dengan int_a^b f(x) dx, dengan titik potong c_1, c_2 in (0, 3).

Render:
  ../scripts/preview_scene.sh 26_mean_value_theorem_for_integrals.py MeanValueTheoremIntegralScene -s
"""

from manim import *
import numpy as np


A_START = 0.0
B_END = 3.0
SPAN = B_END - A_START           # 3.0
EXACT_INT = 7.5                  # 15/2
F_BAR = EXACT_INT / SPAN         # 2.5
C1 = (3.0 - np.sqrt(3.0)) / 2.0  # ~0.63397
C2 = (3.0 + np.sqrt(3.0)) / 2.0  # ~2.36603

CARD_BG = "#141B28"


def f_func(x):
    return 3.0 * x - x ** 2 + 1.0


def F_antideriv(x):
    return 1.5 * x ** 2 - (x ** 3) / 3.0 + x


_TRAPZ = getattr(np, "trapezoid", getattr(np, "trapz", None))


def excess_above_h(h, num_pts=300):
    xs = np.linspace(A_START, B_END, num_pts)
    vals = np.maximum(f_func(xs) - h, 0.0)
    return float(_TRAPZ(vals, xs))


def deficit_below_h(h, num_pts=300):
    xs = np.linspace(A_START, B_END, num_pts)
    vals = np.maximum(h - f_func(xs), 0.0)
    return float(_TRAPZ(vals, xs))


class MeanValueTheoremIntegralScene(Scene):
    def construct(self):
        # Pemeriksaan konsistensi numerik
        assert abs((F_antideriv(B_END) - F_antideriv(A_START)) - EXACT_INT) < 1e-12
        assert abs(f_func(C1) - F_BAR) < 1e-12 and abs(f_func(C2) - F_BAR) < 1e-12

        # =============================================================
        # TATA LETAK: Sumbu utama di kiri, panel kartu Sokratik di kanan
        # =============================================================
        ax = Axes(
            x_range=[-0.3, 3.5, 1],
            y_range=[0, 4.0, 1],
            x_length=6.5,
            y_length=4.7,
            axis_config={"color": GRAY_C, "stroke_width": 1.6, "include_tip": False},
        ).add_coordinates(font_size=16)
        ax.move_to(LEFT * 3.1 + DOWN * 0.45)

        lbl_x = MathTex("x", font_size=22, color=GRAY_B).next_to(ax.x_axis.get_end(), RIGHT, buff=0.1)
        lbl_y = MathTex("y", font_size=22, color=GRAY_B).next_to(ax.y_axis.get_end(), UP, buff=0.1)

        graph_f = ax.plot(f_func, x_range=[0.0, 3.0], color=YELLOW, stroke_width=3.8)
        graph_lbl = MathTex(r"f(x) = 3x - x^2 + 1", font_size=24, color=YELLOW).next_to(
            ax.c2p(1.5, 3.25), UP, buff=0.18
        )

        # =============================================================
        # BABAK 1: Dilema - Bagaimana merata-ratakan fungsi kontinu?
        # =============================================================
        judul = Text(
            "Bagaimana menghitung 'nilai rata-rata' dari fungsi kontinu f(x) pada [0, 3]?",
            font_size=21, color=WHITE,
        ).to_edge(UP, buff=0.22)

        self.play(Write(judul), run_time=1.5)
        self.play(Create(ax), FadeIn(lbl_x), FadeIn(lbl_y), run_time=1.0)
        self.play(Create(graph_f), Write(graph_lbl), run_time=1.3)

        def sample_stems_and_card(n):
            dx = SPAN / n
            xs = [A_START + (i + 0.5) * dx for i in range(n)]
            avg_val = sum(f_func(x) for x in xs) / n

            stems = VGroup()
            dots = VGroup()
            for x in xs:
                p0 = ax.c2p(x, 0)
                p1 = ax.c2p(x, f_func(x))
                stems.add(Line(p0, p1, color=TEAL_C, stroke_width=2.8 if n <= 12 else 1.5))
                if n <= 18:
                    dots.add(Dot(p1, color=TEAL_A, radius=0.045))

            rects = ax.get_riemann_rectangles(
                graph_f,
                x_range=[A_START, B_END],
                dx=dx,
                input_sample_type="center",
                stroke_width=1.0 if n <= 12 else 0.4,
                stroke_color=WHITE,
                fill_opacity=0.28,
                color=(BLUE_D, TEAL_C),
            )

            card = VGroup(
                Text(f"Sampel diskrit: n = {n} titik", font_size=19, color=GRAY_A),
                MathTex(
                    r"\bar{y}_n = \frac{1}{n}\sum_{i=1}^{n} f(x_i)"
                    r"= \frac{1}{b-a}\sum_{i=1}^{n} f(x_i)\,\Delta x",
                    font_size=21, color=TEAL_B,
                ),
                MathTex(rf"\bar{{y}}_{{{n}}} \approx {avg_val:.4f}", font_size=25, color=GOLD_B),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.16)
            card.move_to(RIGHT * 3.55 + UP * 1.15)
            return VGroup(rects, stems, dots), card

        grp_s, card_s = sample_stems_and_card(3)
        self.play(FadeIn(grp_s), FadeIn(card_s), run_time=1.2)
        self.wait(0.8)

        for n_val in [6, 12, 36]:
            new_grp, new_card = sample_stems_and_card(n_val)
            self.play(Transform(grp_s, new_grp), Transform(card_s, new_card), run_time=0.95)
            self.wait(0.45)

        limit_box_content = VGroup(
            Text("Saat n → ∞, rata-rata sampel menjadi:", font_size=18, color=WHITE),
            MathTex(
                r"\bar{f} = \frac{1}{b-a}\int_a^b f(x)\,dx = \frac{1}{3}\cdot\frac{15}{2} = 2{,}5",
                font_size=23, color=GOLD_B,
            ),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.14).move_to(RIGHT * 3.55 + DOWN * 1.2)
        self.play(FadeIn(limit_box_content, shift=UP * 0.15), run_time=1.0)
        self.wait(1.8)
        self.play(FadeOut(grp_s), FadeOut(card_s), FadeOut(limit_box_content), run_time=0.9)

        # =============================================================
        # BABAK 2: Eksplorasi - Meratakan bukit ke dalam lembah (y = h)
        # =============================================================
        judul2 = Text(
            "Tafsiran Geometris: meratakan 'bukit' di atas garis y = h ke dalam 'lembah'",
            font_size=21, color=WHITE,
        ).to_edge(UP, buff=0.22)
        self.play(Transform(judul, judul2), run_time=1.0)

        h_tr = ValueTracker(1.55)

        # Kurva bantu garis mendatar y = h
        def get_excess_deficit_fills():
            h = h_tr.get_value()
            xs = np.linspace(A_START, B_END, 160)
            # Poligon kelebihan (f(x) > h) berwarna EMAS/HIJAU
            pts_above = [ax.c2p(A_START, h)]
            for x in xs:
                pts_above.append(ax.c2p(x, max(f_func(x), h)))
            pts_above.append(ax.c2p(B_END, h))
            poly_above = Polygon(
                *pts_above,
                stroke_width=0,
                fill_color=TEAL_C,
                fill_opacity=0.48,
            )

            # Poligon kekurangan (f(x) < h) berwarna MERAH KORAL
            pts_below = [ax.c2p(A_START, h)]
            for x in xs:
                pts_below.append(ax.c2p(x, min(f_func(x), h)))
            pts_below.append(ax.c2p(B_END, h))
            poly_below = Polygon(
                *pts_below,
                stroke_width=0,
                fill_color=MAROON_B,
                fill_opacity=0.52,
            )

            # Persegi panjang dasar dari y = 0 ke y = h
            rect_h = Polygon(
                ax.c2p(A_START, 0),
                ax.c2p(A_START, h),
                ax.c2p(B_END, h),
                ax.c2p(B_END, 0),
                stroke_color=BLUE_B,
                stroke_width=2.0,
                fill_color=BLUE_D,
                fill_opacity=0.18,
            )
            return VGroup(rect_h, poly_below, poly_above)

        dynamic_regions = always_redraw(get_excess_deficit_fills)

        h_line = always_redraw(lambda: DashedLine(
            ax.c2p(-0.15, h_tr.get_value()),
            ax.c2p(3.25, h_tr.get_value()),
            color=GOLD_B, stroke_width=2.8, dash_length=0.1,
        ))
        h_lbl = always_redraw(lambda: MathTex(
            rf"y = h = {h_tr.get_value():.2f}", font_size=20, color=GOLD_B
        ).next_to(ax.c2p(3.02, h_tr.get_value()), UP, buff=0.08))

        # Kartu telemetri di kanan
        def metric_row(label_tex, color, fn):
            lbl = MathTex(label_tex, font_size=22, color=color)
            num = DecimalNumber(fn(), num_decimal_places=2, font_size=22, color=color)
            num.next_to(lbl, RIGHT, buff=0.12)
            num.add_updater(lambda m: m.set_value(fn()).next_to(lbl, RIGHT, buff=0.12))
            return VGroup(lbl, num)

        r_h = metric_row(r"\text{Tinggi uji } h =", GOLD_B, lambda: h_tr.get_value())
        r_rect = metric_row(r"\text{Luas persegi panjang } 3h =", BLUE_B, lambda: SPAN * h_tr.get_value())
        r_int = MathTex(r"\text{Luas kurva } \int_0^3 f(x)\,dx = 7{,}50", font_size=22, color=YELLOW)
        r_above = metric_row(r"\text{Luas bukit (di atas } h\text{)} =", TEAL_C,
                             lambda: excess_above_h(h_tr.get_value()))
        r_below = metric_row(r"\text{Luas lembah (di bawah } h\text{)} =", MAROON_B,
                             lambda: deficit_below_h(h_tr.get_value()))

        telemetry = VGroup(r_h, r_rect, r_int, r_above, r_below).arrange(
            DOWN, aligned_edge=LEFT, buff=0.18
        ).move_to(RIGHT * 3.55 + UP * 1.1)
        telemetry_box = SurroundingRectangle(
            telemetry, color=BLUE_D, fill_color=CARD_BG, fill_opacity=0.92, buff=0.2, corner_radius=0.1
        )

        self.add(dynamic_regions, graph_f, h_line, h_lbl)
        self.play(FadeIn(telemetry_box), FadeIn(telemetry), run_time=1.0)
        self.wait(0.8)

        # Geser h terlalu tinggi (3.05) lalu terlalu rendah (1.85)
        self.play(h_tr.animate.set_value(3.05), run_time=2.6, rate_func=smooth)
        self.wait(0.7)
        self.play(h_tr.animate.set_value(1.80), run_time=2.4, rate_func=smooth)
        self.wait(0.8)

        # =============================================================
        # BABAK 3: Inversi Sokratik - Kapan bukit = lembah & apakah memotong kurva?
        # =============================================================
        tanya = Text(
            "Pada tinggi h berapakah luas bukit = luas lembah?\nApakah kurva kontinu f pasti memotong garis itu?",
            font_size=20, color=TEAL_A, line_spacing=1.15,
        ).to_edge(UP, buff=0.18)

        petunjuk_sokratik = VGroup(
            Tex(r"Syarat keseimbangan luas:", font_size=21, color=WHITE),
            MathTex(r"\text{Luas Bukit} = \text{Luas Lembah}", font_size=22, color=GOLD_B),
            MathTex(r"\iff (b-a)\,h = \int_0^3 f(x)\,dx = 7{,}50", font_size=22, color=BLUE_B),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.12).move_to(RIGHT * 3.55 + DOWN * 1.95)

        self.play(Transform(judul, tanya), FadeIn(petunjuk_sokratik), run_time=1.1)
        self.wait(2.5)  # Jeda refleksi Sokratik

        # Gerakkan h tepat ke F_BAR = 2.50
        self.play(h_tr.animate.set_value(F_BAR), run_time=2.8, rate_func=smooth)
        seimbang_badge = Text(
            "Seimbang! Luas bukit (0,87) = Luas lembah (0,87)",
            font_size=17, color=GREEN_B,
        ).next_to(petunjuk_sokratik, DOWN, buff=0.15)
        self.play(FadeIn(seimbang_badge, shift=UP * 0.1), run_time=0.8)
        self.wait(1.8)

        # =============================================================
        # BABAK 4: Kristalisasi - Titik c in (a,b) dan TNR Integral
        # =============================================================
        judul4 = Text(
            "Teorema Nilai Rata-rata untuk Integral: terdapat c ∈ (a, b) dengan f(c) = f̄",
            font_size=21, color=GOLD_B, weight=BOLD,
        ).to_edge(UP, buff=0.22)

        dot_c1 = Dot(ax.c2p(C1, F_BAR), color=RED_A, radius=0.075)
        dot_c2 = Dot(ax.c2p(C2, F_BAR), color=RED_A, radius=0.075)
        v_c1 = DashedLine(ax.c2p(C1, 0), ax.c2p(C1, F_BAR), color=RED_C, stroke_width=2.2, dash_length=0.08)
        v_c2 = DashedLine(ax.c2p(C2, 0), ax.c2p(C2, F_BAR), color=RED_C, stroke_width=2.2, dash_length=0.08)
        lbl_c1 = MathTex(r"c_1", font_size=22, color=RED_B).next_to(ax.c2p(C1, 0), DOWN, buff=0.12)
        lbl_c2 = MathTex(r"c_2", font_size=22, color=RED_B).next_to(ax.c2p(C2, 0), DOWN, buff=0.12)

        self.play(
            Transform(judul, judul4),
            FadeOut(petunjuk_sokratik),
            FadeOut(seimbang_badge),
            run_time=0.9,
        )
        self.play(
            Create(v_c1), Create(v_c2),
            FadeIn(dot_c1, scale=1.4), FadeIn(dot_c2, scale=1.4),
            Write(lbl_c1), Write(lbl_c2),
            run_time=1.4,
        )
        self.play(Indicate(dot_c1, color=YELLOW), Indicate(dot_c2, color=YELLOW), run_time=1.0)

        # Kartu kristalisasi teorema di kanan bawah
        teorema_content = VGroup(
            Tex(r"\textbf{Teorema Nilai Rata-rata Integral}", font_size=22, color=GOLD_B),
            Tex(r"Jika $f$ kontinu pada $[a,b]$, terdapat $c \in (a,b)$:", font_size=19, color=GRAY_A),
            MathTex(
                r"f(c) = \bar{f} = \frac{1}{b-a}\int_a^b f(x)\,dx",
                font_size=24, color=WHITE,
            ),
            MathTex(
                r"\int_a^b f(x)\,dx = f(c)\,(b-a)",
                font_size=24, color=TEAL_B,
            ),
            MathTex(
                r"c = \frac{3 \pm \sqrt{3}}{2} \in (0, 3), \quad f(c) = \frac{5}{2}",
                font_size=20, color=RED_B,
            ),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.12)
        teorema_content.move_to(RIGHT * 3.55 + DOWN * 1.75)
        teorema_box = SurroundingRectangle(
            teorema_content, color=GOLD_B, fill_color=CARD_BG, fill_opacity=0.96, buff=0.18, corner_radius=0.1
        )
        overflow = teorema_box.get_right()[0] - (config.frame_width / 2 - 0.15)
        if overflow > 0:
            VGroup(teorema_box, teorema_content).shift(LEFT * overflow)

        self.play(FadeIn(teorema_box), Write(teorema_content), run_time=1.8)
        self.play(Circumscribe(teorema_content[2], color=GOLD_A, time_width=0.6), run_time=1.4)
        self.wait(3.0)
