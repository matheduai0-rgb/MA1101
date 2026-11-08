"""
Template: Teorema Nilai Rata-rata untuk Turunan (MA1101 Subtopik 3.6)
Subtopik: 3.6 Teorema Nilai Rata-rata (The Mean Value Theorem for Derivatives)
Bahasa: Indonesia
Gaya: Grant Sanderson (3Blue1Brown) & Metode Sokratik
Deskripsi:
  Visualisasi intuitif garis sekan rata-rata dan pergeseran sejajar menyinggung
  kurva mulus di c1 dan c2. Dilengkapi formulasi formal TNR dan kaitannya
  dengan Teorema Rolle sebagai kasus khusus saat f(a) = f(b).
"""

from manim import *
import numpy as np

class MeanValueTheoremScene(Scene):
    def construct(self):
        # -------------------------------------------------------------
        # AKSI 1: Tantangan Sokratik (The Pique) & Kurva f(x)
        # -------------------------------------------------------------
        judul = Text(
            "Jika kelajuan rata-rata Anda 70 km/jam,\nadakah saat spidometer Anda tepat 70 km/jam?",
            font_size=23,
            line_spacing=1.2,
            color=WHITE
        ).to_edge(UP, buff=0.35)

        self.play(Write(judul), run_time=1.2)
        self.wait(0.5)

        axes = Axes(
            x_range=[0, 6, 1],
            y_range=[0, 5, 1],
            x_length=9.0,
            y_length=4.5,
            axis_config={"color": GRAY_C}
        ).add_coordinates()
        axes.shift(DOWN * 0.45)

        # Kurva f(x) kubik bergelombang mulus
        f = lambda x: 0.16 * (x - 3.0)**3 - 0.75 * (x - 3.0) + 0.5 * x + 1.3
        curve = axes.plot(f, x_range=[0.7, 5.3], color=YELLOW, stroke_width=3.5)
        curve_label = MathTex(r"y = f(x)", color=YELLOW, font_size=22).next_to(axes.c2p(2.2, f(2.2)), UP, buff=0.3)

        a, b = 1.0, 5.0
        fa, fb = f(a), f(b)

        pt_a = Dot(axes.c2p(a, fa), color=YELLOW, radius=0.08)
        pt_b = Dot(axes.c2p(b, fb), color=YELLOW, radius=0.08)
        label_a = MathTex(r"A(a, f(a))", color=YELLOW, font_size=20).next_to(pt_a, UL, buff=0.12)
        label_b = MathTex(r"B(b, f(b))", color=YELLOW, font_size=20).next_to(pt_b, DR, buff=0.12)

        self.play(Create(axes), Create(curve), FadeIn(curve_label), run_time=1.4)
        self.play(FadeIn(pt_a), FadeIn(pt_b), Write(label_a), Write(label_b), run_time=0.8)
        self.wait(0.4)

        # -------------------------------------------------------------
        # AKSI 2: Eksplorasi Visual (Garis Sekan Rata-Rata)
        # -------------------------------------------------------------
        m_sec = (fb - fa) / (b - a)
        secant_line = Line(
            axes.c2p(a - 0.4, fa - 0.4 * m_sec),
            axes.c2p(b + 0.4, fb + 0.4 * m_sec),
            color=BLUE_C,
            stroke_width=2.5
        )
        secant_label = MathTex(
            r"m_{\text{sekan}} = \frac{f(b) - f(a)}{b - a}",
            color=BLUE_C,
            font_size=21
        ).to_corner(UL, buff=0.45)

        self.play(Create(secant_line), Write(secant_label), run_time=1.0)
        self.wait(0.5)

        # -------------------------------------------------------------
        # AKSI 3: Pertanyaan Sokratik (Pergeseran Sejajar & Titik c)
        # -------------------------------------------------------------
        pertanyaan = Text(
            "Jika garis sekan digeser sejajar,\nkapankah ia menyinggung kurva f(x)?",
            font_size=22,
            color=TEAL_A,
            line_spacing=1.2
        ).to_edge(UP, buff=0.35)

        self.play(Transform(judul, pertanyaan), run_time=1.0)
        self.wait(0.5)

        # Titik c1 dan c2 di mana f'(c) = m_sec
        c1 = 3.0 - 2.0 / np.sqrt(3)  # ≈ 1.845
        c2 = 3.0 + 2.0 / np.sqrt(3)  # ≈ 4.155
        fc1 = f(c1)
        fc2 = f(c2)

        pt_c1 = Dot(axes.c2p(c1, fc1), color=RED_C, radius=0.08)
        dot_c1_axis = Dot(axes.c2p(c1, 0), color=RED_C, radius=0.06)
        line_drop_c1 = axes.get_vertical_line(axes.c2p(c1, fc1), color=RED_C).set_stroke(width=1.5, opacity=0.7)
        label_c1 = MathTex(r"c_1", color=RED_C, font_size=20).next_to(dot_c1_axis, DOWN, buff=0.08)

        tangent_1 = Line(
            axes.c2p(c1 - 1.2, fc1 - 1.2 * m_sec),
            axes.c2p(c1 + 1.2, fc1 + 1.2 * m_sec),
            color=RED_C,
            stroke_width=2.5
        )
        lbl_tan1 = MathTex(r"f'(c_1) = m_{\text{sekan}}", color=RED_C, font_size=17).next_to(tangent_1, UL, buff=0.05)

        pt_c2 = Dot(axes.c2p(c2, fc2), color=GREEN_C, radius=0.08)
        dot_c2_axis = Dot(axes.c2p(c2, 0), color=GREEN_C, radius=0.06)
        line_drop_c2 = axes.get_vertical_line(axes.c2p(c2, fc2), color=GREEN_C).set_stroke(width=1.5, opacity=0.7)
        label_c2 = MathTex(r"c_2", color=GREEN_C, font_size=20).next_to(dot_c2_axis, DOWN, buff=0.08)

        tangent_2 = Line(
            axes.c2p(c2 - 1.2, fc2 - 1.2 * m_sec),
            axes.c2p(c2 + 1.2, fc2 + 1.2 * m_sec),
            color=GREEN_C,
            stroke_width=2.5
        )
        lbl_tan2 = MathTex(r"f'(c_2) = m_{\text{sekan}}", color=GREEN_C, font_size=17).next_to(tangent_2, DR, buff=0.05)

        # Geser garis sekan ke c1
        ghost_line = secant_line.copy().set_color(RED_C).set_stroke(opacity=0.8)
        self.play(Transform(ghost_line, tangent_1), run_time=1.8, rate_func=smooth)
        self.play(FadeIn(pt_c1), Create(line_drop_c1), FadeIn(dot_c1_axis), Write(label_c1), FadeIn(lbl_tan1), run_time=0.8)
        self.wait(0.4)

        # Geser garis sekan ke c2
        ghost_line_2 = secant_line.copy().set_color(GREEN_C).set_stroke(opacity=0.8)
        self.play(Transform(ghost_line_2, tangent_2), run_time=1.8, rate_func=smooth)
        self.play(FadeIn(pt_c2), Create(line_drop_c2), FadeIn(dot_c2_axis), Write(label_c2), FadeIn(lbl_tan2), run_time=0.8)
        self.wait(0.6)

        # -------------------------------------------------------------
        # AKSI 4: Kristalisasi Matematis Formal (TNR)
        # -------------------------------------------------------------
        judul_kristal = Text(
            "Teorema Nilai Rata-rata untuk Turunan (TNR)",
            font_size=21,
            color=GOLD_B
        ).to_edge(UP, buff=0.35)

        tnr_formula = MathTex(
            r"f'(c)",
            r"=",
            r"\frac{f(b) - f(a)}{b - a}",
            font_size=24
        ).to_corner(UR, buff=0.45)
        tnr_formula[0].set_color(RED_C)
        tnr_formula[2].set_color(BLUE_C)

        box = SurroundingRectangle(tnr_formula, color=BLUE_B, buff=0.1, stroke_width=1.5)

        syarat = MathTex(
            r"f \text{ kontinu pada } [a, b] \\",
            r"f \text{ terturunkan pada } (a, b)",
            font_size=18,
            color=GRAY_A
        ).next_to(box, DOWN, buff=0.15)

        kesimpulan = Text(
            "Terdapat minimal satu c di (a, b) dengan kemiringan garis singgung = laju rata-rata!",
            font_size=13,
            color=GOLD_A
        ).next_to(axes, DOWN, buff=0.25)

        self.play(
            Transform(judul, judul_kristal),
            Write(tnr_formula),
            Create(box),
            Write(syarat),
            Write(kesimpulan),
            run_time=1.4
        )
        self.wait(2.5)
