"""
Template: Laju yang Berkaitan - Tangga Meluncur (MA1101)
Subtopik: 2.8 Laju yang Berkaitan (Related Rates)
Bahasa: Indonesia
Gaya: Grant Sanderson (3Blue1Brown) & Metode Sokratik
"""

from manim import *
import numpy as np

class SlidingLadderScene(Scene):
    def construct(self):
        # -------------------------------------------------------------
        # AKSI 1: Tantangan / Misteri Awal (The Pique)
        # -------------------------------------------------------------
        judul = Text(
            "Saat ujung atas tangga meluncur ke bawah,\nbagaimana gerak ujung bawahnya?",
            font_size=28,
            line_spacing=1.2
        ).to_edge(UP, buff=0.4)
        
        self.play(Write(judul))
        self.wait(1.5)

        # Dinding dan Lantai
        dinding = Line(UP * 3 + LEFT * 3.5, DOWN * 2.5 + LEFT * 3.5, stroke_width=4, color=GRAY_B)
        lantai = Line(DOWN * 2.5 + LEFT * 3.5, DOWN * 2.5 + RIGHT * 4.5, stroke_width=4, color=GRAY_B)
        sudut_siku = RightAngle(
            Line(DOWN * 2.5 + LEFT * 3.5, UP * 3 + LEFT * 3.5),
            Line(DOWN * 2.5 + LEFT * 3.5, DOWN * 2.5 + RIGHT * 4.5),
            length=0.4,
            color=GRAY_A
        )

        label_dinding = Text("Dinding", font_size=20, color=GRAY_C).next_to(dinding, LEFT, buff=0.2)
        label_lantai = Text("Lantai", font_size=20, color=GRAY_C).next_to(lantai, DOWN, buff=0.2)

        self.play(Create(dinding), Create(lantai), Create(sudut_siku), FadeIn(label_dinding), FadeIn(label_lantai))
        self.wait(1)

        # Panjang tangga L = 5 meter (skala visual)
        L = 5.0
        sudut_awal = 75 * DEGREES
        sudut_tracker = ValueTracker(sudut_awal)

        p_sudut = DOWN * 2.5 + LEFT * 3.5

        def get_top():
            theta = sudut_tracker.get_value()
            return p_sudut + UP * (L * np.sin(theta))

        def get_bottom():
            theta = sudut_tracker.get_value()
            return p_sudut + RIGHT * (L * np.cos(theta))

        tangga = always_redraw(lambda:
            Line(get_top(), get_bottom(), stroke_width=8, color=YELLOW)
        )
        ujung_atas = always_redraw(lambda: Dot(get_top(), color=RED_C, radius=0.09))
        ujung_bawah = always_redraw(lambda: Dot(get_bottom(), color=TEAL_C, radius=0.09))

        label_y = always_redraw(lambda:
            MathTex(r"y(t)", color=RED_C, font_size=28).next_to(
                (p_sudut + get_top()) / 2, LEFT, buff=0.15
            )
        )
        label_x = always_redraw(lambda:
            MathTex(r"x(t)", color=TEAL_C, font_size=28).next_to(
                (p_sudut + get_bottom()) / 2, DOWN, buff=0.15
            )
        )
        label_L = MathTex(r"L = 5\text{ m}", color=YELLOW, font_size=26).shift(LEFT * 1.5 + DOWN * 0.5)

        self.play(Create(tangga), FadeIn(ujung_atas), FadeIn(ujung_bawah), Write(label_y), Write(label_x), Write(label_L))
        self.wait(1.5)

        # -------------------------------------------------------------
        # AKSI 2: Eksplorasi Visual (Meluncur Dinamis)
        # -------------------------------------------------------------
        # Vektor kecepatan visual
        panah_vy = always_redraw(lambda:
            Arrow(get_top(), get_top() + DOWN * 0.8, color=RED_C, buff=0, stroke_width=3, max_tip_length_to_length_ratio=0.35)
        )
        panah_vx = always_redraw(lambda:
            Arrow(get_bottom(), get_bottom() + RIGHT * (0.8 * np.tan(sudut_tracker.get_value())), color=TEAL_C, buff=0, stroke_width=3, max_tip_length_to_length_ratio=0.35)
        )

        label_dy = MathTex(r"\frac{dy}{dt} < 0", color=RED_C, font_size=24).next_to(panah_vy, RIGHT, buff=0.1)
        label_dx = MathTex(r"\frac{dx}{dt} > 0", color=TEAL_C, font_size=24).next_to(panah_vx, UP, buff=0.1)

        self.play(FadeIn(panah_vy), FadeIn(panah_vx), Write(label_dy), Write(label_dx))
        self.wait(1)

        # -------------------------------------------------------------
        # AKSI 3: Pertanyaan Sokratik (Socratic Pause)
        # -------------------------------------------------------------
        pertanyaan_sokratik = Text(
            "Ketika ujung atas hampir menyentuh lantai (y -> 0),\napakah ujung bawah melambat atau makin cepat?",
            font_size=24,
            color=TEAL_A,
            line_spacing=1.2
        ).to_edge(UP, buff=0.4)

        self.play(Transform(judul, pertanyaan_sokratik))
        self.wait(1.5)

        # Animate tangga meluncur turun ke sudut yang sangat kecil
        self.play(
            sudut_tracker.animate.set_value(18 * DEGREES),
            run_time=4.5,
            rate_func=linear
        )
        self.wait(1.5)

        # -------------------------------------------------------------
        # AKSI 4: Kristalisasi Matematis Formal
        # -------------------------------------------------------------
        persamaan_pythagoras = MathTex(r"x^2 + y^2 = L^2", font_size=28).to_corner(UR, buff=0.5)
        turunan_implisit = MathTex(
            r"2x\frac{dx}{dt} + 2y\frac{dy}{dt} = 0",
            font_size=28
        ).next_to(persamaan_pythagoras, DOWN, buff=0.25)
        
        relasi_laju = MathTex(
            r"\frac{dx}{dt}",
            r"=",
            r"-\frac{y}{x}",
            r"\frac{dy}{dt}",
            font_size=32
        ).next_to(turunan_implisit, DOWN, buff=0.3)
        relasi_laju[0].set_color(TEAL_C)
        relasi_laju[2].set_color(YELLOW)
        relasi_laju[3].set_color(RED_C)

        kotak_kesimpulan = SurroundingRectangle(relasi_laju, color=BLUE_B, buff=0.15)
        catatan = Text("Saat y -> 0 dan x -> L, laju dx/dt -> 0 (berhenti sesaat)", font_size=18, color=GRAY_A)
        catatan.next_to(kotak_kesimpulan, DOWN, buff=0.2)

        self.play(Write(persamaan_pythagoras))
        self.wait(0.8)
        self.play(Write(turunan_implisit))
        self.wait(0.8)
        self.play(Write(relasi_laju), Create(kotak_kesimpulan), FadeIn(catatan))
        self.wait(2.5)
