"""
Template: Teorema Nilai Rata-rata untuk Turunan (MA1101)
Subtopik: 3.6 Teorema Nilai Rata-rata (Mean Value Theorem)
Bahasa: Indonesia
Gaya: Grant Sanderson (3Blue1Brown) & Metode Sokratik
"""

from manim import *

class MeanValueTheoremScene(Scene):
    def construct(self):
        # -------------------------------------------------------------
        # AKSI 1: Tantangan Sokratik (The Pique)
        # -------------------------------------------------------------
        judul = Text(
            "Jika laju rata-rata Anda 80 km/jam,\nadakah saat spidometer Anda tepat 80 km/jam?",
            font_size=26,
            line_spacing=1.2
        ).to_edge(UP, buff=0.4)
        
        self.play(Write(judul))
        self.wait(1.5)

        axes = Axes(
            x_range=[0, 6, 1],
            y_range=[0, 6, 1],
            x_length=8.5,
            y_length=5,
            axis_config={"color": GRAY_C}
        ).add_coordinates()
        axes.shift(DOWN * 0.4)

        # Kurva f(x) mulus dan kontinu
        f = lambda x: -0.18 * (x - 1.2) * (x - 5.5)**2 + 0.5 * x + 1.2
        curve = axes.plot(f, x_range=[0.8, 5.2], color=YELLOW, stroke_width=3.5)
        curve_label = MathTex(r"f(x)", color=YELLOW, font_size=28).next_to(axes.c2p(4.8, f(4.8)), UR)

        a, b = 1.2, 5.0
        fa, fb = f(a), f(b)

        pt_a = Dot(axes.c2p(a, fa), color=YELLOW, radius=0.08)
        pt_b = Dot(axes.c2p(b, fb), color=YELLOW, radius=0.08)
        label_a = MathTex(r"(a, f(a))", color=YELLOW, font_size=24).next_to(pt_a, DL, buff=0.15)
        label_b = MathTex(r"(b, f(b))", color=YELLOW, font_size=24).next_to(pt_b, UR, buff=0.15)

        self.play(Create(axes), Create(curve), FadeIn(curve_label), run_time=2)
        self.play(FadeIn(pt_a), FadeIn(pt_b), Write(label_a), Write(label_b))
        self.wait(1)

        # -------------------------------------------------------------
        # AKSI 2: Eksplorasi Visual (Garis Sekan)
        # -------------------------------------------------------------
        # Kemiringan garis sekan m_sec = (f(b) - f(a)) / (b - a)
        m_sec = (fb - fa) / (b - a)
        secant_line = Line(
            axes.c2p(a - 0.5, fa - 0.5 * m_sec),
            axes.c2p(b + 0.5, fb + 0.5 * m_sec),
            color=BLUE_C,
            stroke_width=2.5
        )
        secant_label = MathTex(
            r"m_{\text{sekan}} = \frac{f(b) - f(a)}{b - a}",
            color=BLUE_C,
            font_size=26
        ).to_corner(UL, buff=0.6)

        self.play(Create(secant_line), Write(secant_label))
        self.wait(1.5)

        # -------------------------------------------------------------
        # AKSI 3: Pertanyaan Sokratik (Pergeseran Sejajar)
        # -------------------------------------------------------------
        pertanyaan = Text(
            "Jika garis sekan digeser sejajar,\nkapankah ia menyinggung kurva f(x)?",
            font_size=24,
            color=TEAL_A,
            line_spacing=1.2
        ).to_edge(UP, buff=0.4)

        self.play(Transform(judul, pertanyaan))
        self.wait(1.5)

        # Titik c di mana f'(c) = m_sec (secara visual c ≈ 2.85)
        c_val = 2.85
        fc = f(c_val)
        pt_c = Dot(axes.c2p(c_val, fc), color=RED_C, radius=0.08)
        dot_c_axis = Dot(axes.c2p(c_val, 0), color=RED_C, radius=0.06)
        line_drop_c = axes.get_vertical_line(axes.c2p(c_val, fc), color=RED_C).set_stroke(width=1.5, opacity=0.7)
        label_c = MathTex(r"c", color=RED_C, font_size=26).next_to(dot_c_axis, DOWN)

        tangent_line = Line(
            axes.c2p(c_val - 1.5, fc - 1.5 * m_sec),
            axes.c2p(c_val + 1.5, fc + 1.5 * m_sec),
            color=RED_C,
            stroke_width=3
        )

        # Animate transiting parallel line upwards from secant to tangent
        ghost_line = secant_line.copy().set_color(TEAL_C).set_stroke(opacity=0.7)
        self.play(Transform(ghost_line, tangent_line), run_time=3, rate_func=smooth)
        self.play(FadeIn(pt_c), Create(line_drop_c), FadeIn(dot_c_axis), Write(label_c))
        self.wait(1.5)

        # -------------------------------------------------------------
        # AKSI 4: Kristalisasi Matematis Formal (TNR)
        # -------------------------------------------------------------
        tnr_formula = MathTex(
            r"f'(c)",
            r"=",
            r"\frac{f(b) - f(a)}{b - a}",
            font_size=32
        ).to_corner(UR, buff=0.6)
        tnr_formula[0].set_color(RED_C)
        tnr_formula[2].set_color(BLUE_C)

        box = SurroundingRectangle(tnr_formula, color=BLUE_B, buff=0.15)
        label_teorema = Text("Teorema Nilai Rata-rata (TNR)", font_size=20, color=WHITE)
        label_teorema.next_to(box, UP, buff=0.2)
        syarat = MathTex(r"f \text{ kontinu pada } [a, b], \text{ terdiferensialkan pada } (a, b)", font_size=20, color=GRAY_B)
        syarat.next_to(box, DOWN, buff=0.2)

        self.play(FadeIn(label_teorema), Write(tnr_formula), Create(box), Write(syarat))
        self.wait(2.5)
