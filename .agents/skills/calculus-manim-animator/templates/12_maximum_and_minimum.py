"""
Template: Maksimum dan Minimum (MA1101)
Subtopik: 3.1 Maksimum dan Minimum (Teorema Nilai Ekstrem & Titik Kritis)
Bahasa: Indonesia
Gaya: Grant Sanderson (3Blue1Brown) & Metode Sokratik
"""

from manim import *
import numpy as np

class MaximumMinimumScene(Scene):
    def construct(self):
        # -------------------------------------------------------------
        # AKSI 1: Tantangan Sokratik (The Pique)
        # -------------------------------------------------------------
        judul = Text(
            "Di mana puncak tertinggi & lembah terendah fungsi pada [a, b]?",
            font_size=25,
            color=WHITE
        ).to_edge(UP, buff=0.35)

        self.play(Write(judul))
        self.wait(1.5)

        # Sumbu koordinat di sisi kiri
        # f(x) = 2x^3 - 3x^2 - 12x + 1 pada [-2, 3]
        # x in [-2.5, 3.5], y in [-22, 12]
        axes = Axes(
            x_range=[-2.5, 3.5, 1],
            y_range=[-24, 14, 5],
            x_length=5.6,
            y_length=5.2,
            axis_config={"color": GRAY_C, "stroke_width": 2},
            tips=True
        ).add_coordinates()
        axes.shift(LEFT * 3.3 + DOWN * 0.2)

        f = lambda x: 2 * x**3 - 3 * x**2 - 12 * x + 1
        f_prime = lambda x: 6 * x**2 - 6 * x - 12

        # Kurva f(x) pada selang tertutup [-2, 3]
        curve = axes.plot(
            f,
            x_range=[-2.0, 3.0],
            color=YELLOW,
            stroke_width=3.5
        )
        label_curve = MathTex(r"f(x) = 2x^3 - 3x^2 - 12x + 1", color=YELLOW, font_size=18)
        label_curve.next_to(axes.c2p(0.6, 9), UR, buff=0.15)

        self.play(Create(axes), Create(curve), Write(label_curve), run_time=1.8)
        self.wait(1)

        # -------------------------------------------------------------
        # AKSI 2: Eksplorasi Visual (Garis Singgung & Titik Kritis)
        # -------------------------------------------------------------
        subjudul_kritis = Text(
            "Teorema Titik Kritis: Calon Ekstrem Hanya Muncul di 3 Tempat",
            font_size=23,
            color=TEAL_A
        ).to_edge(UP, buff=0.35)
        self.play(Transform(judul, subjudul_kritis))

        # Titik Ujung Selang (End Points): x = -2 dan x = 3
        pt_ujung_kiri = axes.c2p(-2.0, f(-2.0))
        dot_ujung_kiri = Dot(pt_ujung_kiri, color=BLUE_C, radius=0.08)
        lbl_ujung_kiri = MathTex(r"x = -2", color=BLUE_C, font_size=18).next_to(dot_ujung_kiri, DL, buff=0.1)

        pt_ujung_kanan = axes.c2p(3.0, f(3.0))
        dot_ujung_kanan = Dot(pt_ujung_kanan, color=BLUE_C, radius=0.08)
        lbl_ujung_kanan = MathTex(r"x = 3", color=BLUE_C, font_size=18).next_to(dot_ujung_kanan, DR, buff=0.1)

        self.play(
            FadeIn(dot_ujung_kiri), Write(lbl_ujung_kiri),
            FadeIn(dot_ujung_kanan), Write(lbl_ujung_kanan)
        )
        self.wait(1)

        # Garis singgung dinamis dengan ValueTracker
        x_track = ValueTracker(-1.8)

        tangent_line = always_redraw(lambda:
            axes.plot(
                lambda x: f(x_track.get_value()) + f_prime(x_track.get_value()) * (x - x_track.get_value()),
                x_range=[x_track.get_value() - 0.7, x_track.get_value() + 0.7],
                color=TEAL_C,
                stroke_width=3
            )
        )
        tangent_dot = always_redraw(lambda:
            Dot(axes.c2p(x_track.get_value(), f(x_track.get_value())), color=WHITE, radius=0.07)
        )

        self.play(Create(tangent_line), FadeIn(tangent_dot))

        # Gerakkan kursor ke titik stasioner 1: x = -1 (Puncak)
        self.play(x_track.animate.set_value(-1.0), run_time=2, rate_func=smooth)
        self.wait(0.8)

        dot_max = Dot(axes.c2p(-1.0, f(-1.0)), color=GREEN_C, radius=0.09)
        lbl_max = MathTex(r"f'(-1) = 0", color=GREEN_C, font_size=18).next_to(dot_max, UL, buff=0.1)
        self.play(FadeIn(dot_max), Write(lbl_max))
        self.wait(0.8)

        # Gerakkan kursor ke titik stasioner 2: x = 2 (Lembah)
        self.play(x_track.animate.set_value(2.0), run_time=2.5, rate_func=smooth)
        self.wait(0.8)

        dot_min = Dot(axes.c2p(2.0, f(2.0)), color=RED_C, radius=0.09)
        lbl_min = MathTex(r"f'(2) = 0", color=RED_C, font_size=18).next_to(dot_min, DR, buff=0.1)
        self.play(FadeIn(dot_min), Write(lbl_min))
        self.wait(1)

        # Hapus garis singgung dinamis agar layar bersih
        self.play(FadeOut(tangent_line), FadeOut(tangent_dot))

        # Panel Tiga Habitat Titik Kritis di kanan
        panel_titik1 = MathTex(r"\mathbf{1.\ Titik\ Ujung:}\ x = -2,\ x = 3", font_size=20, color=BLUE_C)
        panel_titik2 = MathTex(r"\mathbf{2.\ Titik\ Stasioner:}\ f'(c) = 0 \implies x = -1,\ 2", font_size=20, color=GREEN_C)
        panel_titik3 = MathTex(r"\mathbf{3.\ Titik\ Singular:}\ f'(c)\ \text{tidak ada}\ (\emptyset)", font_size=20, color=GRAY_A)

        grup_habitat = VGroup(panel_titik1, panel_titik2, panel_titik3).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        grup_habitat.move_to(RIGHT * 3.3 + UP * 0.8)

        self.play(Write(grup_habitat), run_time=2)
        self.wait(1.5)

        # -------------------------------------------------------------
        # AKSI 3: Inversi Sokratik (Teorema Nilai Ekstrem - EVT)
        # -------------------------------------------------------------
        subjudul_evt = Text(
            "Teorema Nilai Ekstrem (EVT): Jaminan Ekstrem Mutlak",
            font_size=23,
            color=YELLOW_B
        ).to_edge(UP, buff=0.35)
        self.play(Transform(judul, subjudul_evt))

        teks_evt = Text(
            "Jika f kontinu pada selang tertutup [a, b],\nmaka f DIJAMIN mencapai nilai\nmaksimum mutlak & minimum mutlak.",
            font_size=18,
            color=WHITE,
            line_spacing=1.2
        ).next_to(grup_habitat, DOWN, buff=0.3, aligned_edge=LEFT)

        box_evt = SurroundingRectangle(teks_evt, color=YELLOW, buff=0.12)
        self.play(FadeIn(teks_evt), Create(box_evt))
        self.wait(2)

        # -------------------------------------------------------------
        # AKSI 4: Kristalisasi Matematis (Metode Selang Tertutup)
        # -------------------------------------------------------------
        subjudul_kristal = Text(
            "Metode Selang Tertutup: Evaluasi Calon Titik Kritis",
            font_size=23,
            color=WHITE
        ).to_edge(UP, buff=0.35)

        self.play(
            Transform(judul, subjudul_kristal),
            FadeOut(grup_habitat),
            FadeOut(teks_evt),
            FadeOut(box_evt)
        )

        turunan_teks = MathTex(
            r"f'(x) = 6(x - 2)(x + 1) = 0",
            font_size=21,
            color=TEAL_C
        )
        baris1 = MathTex(r"f(-2) = 2(-8) - 3(4) - 12(-2) + 1 = \mathbf{-3}", font_size=19)
        baris2 = MathTex(r"f(-1) = 2(-1) - 3(1) - 12(-1) + 1 = \mathbf{8}", font_size=20, color=GREEN_C)
        baris3 = MathTex(r"f(2) = 2(8) - 3(4) - 12(2) + 1 = \mathbf{-19}", font_size=20, color=RED_C)
        baris4 = MathTex(r"f(3) = 2(27) - 3(9) - 12(3) + 1 = \mathbf{-8}", font_size=19)

        grup_eval = VGroup(turunan_teks, baris1, baris2, baris3, baris4).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        grup_eval.move_to(RIGHT * 3.3 + UP * 0.5)

        hasil_max = MathTex(r"\text{Maksimum Mutlak} = \mathbf{8}\ \ (\text{di } x = -1)", font_size=21, color=GREEN_C)
        hasil_min = MathTex(r"\text{Minimum Mutlak} = \mathbf{-19}\ \ (\text{di } x = 2)", font_size=21, color=RED_C)
        grup_kesimpulan = VGroup(hasil_max, hasil_min).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        grup_kesimpulan.next_to(grup_eval, DOWN, buff=0.25, aligned_edge=LEFT)
        box_kesimpulan = SurroundingRectangle(grup_kesimpulan, color=YELLOW, buff=0.12)

        self.play(Write(turunan_teks))
        self.play(Write(baris1))
        self.play(Write(baris2))
        self.play(Write(baris3))
        self.play(Write(baris4))
        self.play(Write(grup_kesimpulan), Create(box_kesimpulan))
        self.wait(3)
