"""
Template: Turunan Implisit (MA1101)
Subtopik: 2.7 Turunan Implisit (Implicit Differentiation)
Bahasa: Indonesia
Gaya: Grant Sanderson (3Blue1Brown) & Metode Sokratik
"""

from manim import *
import numpy as np

class ImplicitDifferentiationScene(Scene):
    def construct(self):
        # -------------------------------------------------------------
        # AKSI 1: Tantangan Sokratik (The Pique)
        # -------------------------------------------------------------
        judul = Text(
            "Kurva ini gagal uji garis vertikal (bukan fungsi y = f(x)).\nBagaimana cara mencari gradien garis singgungnya?",
            font_size=26,
            line_spacing=1.2
        ).to_edge(UP, buff=0.4)
        
        self.play(Write(judul))
        self.wait(1.5)

        axes = Axes(
            x_range=[-6, 6, 2],
            y_range=[-6, 6, 2],
            x_length=6.0,
            y_length=6.0,
            axis_config={"color": GRAY_C}
        ).add_coordinates()
        axes.shift(LEFT * 2.8 + DOWN * 0.3)

        # Kurva implisit: Lingkaran x^2 + y^2 = 25 (r = 5)
        r = 5.0
        lingkaran = Circle(
            radius=axes.c2p(r, 0)[0] - axes.c2p(0, 0)[0],
            color=YELLOW,
            stroke_width=3.5
        ).move_to(axes.c2p(0, 0))

        label_lingkaran = MathTex(r"x^2 + y^2 = 25", color=YELLOW, font_size=26)
        label_lingkaran.next_to(lingkaran, UL, buff=0.2)

        self.play(Create(axes), Create(lingkaran), Write(label_lingkaran), run_time=2)
        self.wait(1)

        # -------------------------------------------------------------
        # AKSI 2: Eksplorasi Visual (Titik Uji & Garis Singgung Geometri)
        # -------------------------------------------------------------
        # Titik P(3, 4)
        x0, y0 = 3.0, 4.0
        pt_P = axes.c2p(x0, y0)
        dot_P = Dot(pt_P, color=RED_C, radius=0.09)
        label_P = MathTex(r"P(3, 4)", color=RED_C, font_size=24).next_to(dot_P, UR, buff=0.15)

        # Vektor jari-jari dari pusat ke P
        jari_jari = Line(axes.c2p(0, 0), pt_P, color=BLUE_C, stroke_width=2.5)
        label_r = MathTex(r"m_{\text{jari-jari}} = \frac{4}{3}", color=BLUE_C, font_size=22)
        label_r.next_to(axes.c2p(1.5, 2.0), DR, buff=0.1)

        self.play(FadeIn(dot_P), Write(label_P), Create(jari_jari), Write(label_r))
        self.wait(1)

        # Garis singgung geometri (tegak lurus jari-jari: m = -3/4)
        m_tan = -3.0 / 4.0
        garis_singgung = Line(
            axes.c2p(x0 - 2.8, y0 - 2.8 * m_tan),
            axes.c2p(x0 + 2.8, y0 + 2.8 * m_tan),
            color=TEAL_C,
            stroke_width=3.5
        )
        siku_siku = RightAngle(
            jari_jari,
            garis_singgung,
            length=0.3,
            color=WHITE
        )
        label_m_tan = MathTex(r"m = -\frac{3}{4}", color=TEAL_C, font_size=24).next_to(axes.c2p(5.0, 2.5), UR)

        self.play(Create(garis_singgung), Create(siku_siku), Write(label_m_tan))
        self.wait(1.5)

        # -------------------------------------------------------------
        # AKSI 3: Pertanyaan Sokratik (Peran Aturan Rantai)
        # -------------------------------------------------------------
        pertanyaan = Text(
            "Secara aljabar, y adalah fungsi dari x: y = y(x).\nBerapakah turunan d/dx [ y² ] ? Apakah 2y atau 2y (dy/dx)?",
            font_size=22,
            color=TEAL_A,
            line_spacing=1.2
        ).to_edge(UP, buff=0.4)

        self.play(Transform(judul, pertanyaan))
        self.wait(1.5)

        # Kotak pengingat aturan rantai di sisi kanan
        kotak_aturan_rantai = MathTex(
            r"\frac{d}{dx}\left[ y^2 \right] = \underbrace{\frac{d}{dy}[y^2]}_{2y} \cdot \frac{dy}{dx}",
            font_size=26,
            color=BLUE_B
        ).to_corner(UR, buff=0.6)
        
        self.play(Write(kotak_aturan_rantai))
        self.wait(1.5)

        # -------------------------------------------------------------
        # AKSI 4: Kristalisasi Matematis Formal (Diferensiasi Implisit)
        # -------------------------------------------------------------
        langkah1 = MathTex(
            r"\frac{d}{dx}[x^2] + \frac{d}{dx}[y^2] &= \frac{d}{dx}[25]",
            font_size=26
        ).next_to(kotak_aturan_rantai, DOWN, buff=0.4, aligned_edge=LEFT)

        langkah2 = MathTex(
            r"2x + 2y \frac{dy}{dx} &= 0",
            font_size=26
        ).next_to(langkah1, DOWN, buff=0.25, aligned_edge=LEFT)

        langkah3 = MathTex(
            r"\frac{dy}{dx} &= -\frac{x}{y}",
            font_size=30
        ).next_to(langkah2, DOWN, buff=0.3, aligned_edge=LEFT)
        langkah3.set_color_by_tex(r"\frac{dy}{dx}", TEAL_C)

        evaluasi = MathTex(
            r"\left. \frac{dy}{dx} \right|_{(3, 4)} &= -\frac{3}{4}",
            font_size=30,
            color=GREEN_C
        ).next_to(langkah3, DOWN, buff=0.3, aligned_edge=LEFT)

        box_eval = SurroundingRectangle(evaluasi, color=GREEN_C, buff=0.15)
        kesimpulan = Text("Persis sama dengan gradien geometri tegak lurus!", font_size=18, color=GRAY_A)
        kesimpulan.next_to(box_eval, DOWN, buff=0.2)

        self.play(Write(langkah1))
        self.wait(0.8)
        self.play(Write(langkah2))
        self.wait(0.8)
        self.play(Write(langkah3))
        self.wait(1)
        self.play(Write(evaluasi), Create(box_eval), FadeIn(kesimpulan))
        self.wait(2.5)
