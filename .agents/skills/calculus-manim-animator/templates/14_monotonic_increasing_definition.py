"""
Animasi Sokratik: Definisi Fungsi Monoton Naik (MA1101)
Subtopik: 3.2 Kemonotonan dan Kecekungan
Bahasa: Indonesia
Gaya: Grant Sanderson (3Blue1Brown) & Pedagogi Sokratik
"""

from manim import *
import numpy as np

class MonotonicIncreasingScene(Scene):
    def construct(self):
        # -------------------------------------------------------------
        # AKSI 1: Tantangan Sokratik (The Pique)
        # -------------------------------------------------------------
        judul = Text(
            "Apa makna matematis yang tepat saat kita mengatakan\nsebuah kurva 'selalu menanjak' (monoton naik)?",
            font_size=24,
            color=WHITE,
            line_spacing=1.2
        ).to_edge(UP, buff=0.35)

        self.play(Write(judul), run_time=1.5)
        self.wait(1.0)

        # Sumbu koordinat
        axes = Axes(
            x_range=[-0.5, 5.5, 1],
            y_range=[-0.5, 4.5, 1],
            x_length=7.2,
            y_length=4.8,
            axis_config={"color": GRAY_C, "stroke_width": 2},
            tips=True
        ).add_coordinates()
        axes.shift(LEFT * 2.8 + DOWN * 0.4)

        # Fungsi monoton naik tegas: f(x) = 0.08*x^3 - 0.3*x^2 + 0.9*x + 0.6
        f = lambda x: 0.08 * x**3 - 0.3 * x**2 + 0.9 * x + 0.6

        curve = axes.plot(f, x_range=[0.0, 4.8], color=YELLOW, stroke_width=3.5)
        curve_label = MathTex(r"y = f(x)", color=YELLOW, font_size=22)
        curve_label.next_to(axes.c2p(4.5, f(4.5)), UR, buff=0.1)

        self.play(Create(axes), Create(curve), FadeIn(curve_label), run_time=1.8)
        self.wait(1.0)

        # -------------------------------------------------------------
        # AKSI 2: Eksplorasi Visual (Dua Titik x1 < x2 dan Proyeksi)
        # -------------------------------------------------------------
        x1_tracker = ValueTracker(1.2)
        x2_tracker = ValueTracker(3.2)

        # Titik pada kurva
        dot1 = always_redraw(lambda:
            Dot(axes.c2p(x1_tracker.get_value(), f(x1_tracker.get_value())), color=TEAL_C, radius=0.08)
        )
        dot2 = always_redraw(lambda:
            Dot(axes.c2p(x2_tracker.get_value(), f(x2_tracker.get_value())), color=GOLD_B, radius=0.08)
        )

        # Garis proyeksi x1
        v_line1 = always_redraw(lambda:
            DashedLine(
                axes.c2p(x1_tracker.get_value(), 0),
                axes.c2p(x1_tracker.get_value(), f(x1_tracker.get_value())),
                color=TEAL_C, stroke_width=2, dash_length=0.08
            )
        )
        h_line1 = always_redraw(lambda:
            DashedLine(
                axes.c2p(0, f(x1_tracker.get_value())),
                axes.c2p(x1_tracker.get_value(), f(x1_tracker.get_value())),
                color=TEAL_C, stroke_width=2, dash_length=0.08
            )
        )

        # Garis proyeksi x2
        v_line2 = always_redraw(lambda:
            DashedLine(
                axes.c2p(x2_tracker.get_value(), 0),
                axes.c2p(x2_tracker.get_value(), f(x2_tracker.get_value())),
                color=GOLD_B, stroke_width=2, dash_length=0.08
            )
        )
        h_line2 = always_redraw(lambda:
            DashedLine(
                axes.c2p(0, f(x2_tracker.get_value())),
                axes.c2p(x2_tracker.get_value(), f(x2_tracker.get_value())),
                color=GOLD_B, stroke_width=2, dash_length=0.08
            )
        )

        # Label x1 dan x2 di sumbu x
        label_x1 = always_redraw(lambda:
            MathTex(r"x_1", color=TEAL_C, font_size=20).next_to(axes.c2p(x1_tracker.get_value(), 0), DOWN, buff=0.15)
        )
        label_x2 = always_redraw(lambda:
            MathTex(r"x_2", color=GOLD_B, font_size=20).next_to(axes.c2p(x2_tracker.get_value(), 0), DOWN, buff=0.15)
        )

        # Label f(x1) dan f(x2) di sumbu y
        label_fx1 = always_redraw(lambda:
            MathTex(r"f(x_1)", color=TEAL_C, font_size=20).next_to(axes.c2p(0, f(x1_tracker.get_value())), LEFT, buff=0.15)
        )
        label_fx2 = always_redraw(lambda:
            MathTex(r"f(x_2)", color=GOLD_B, font_size=20).next_to(axes.c2p(0, f(x2_tracker.get_value())), LEFT, buff=0.15)
        )

        # Garis Tali Busur (Secant Line) antara titik 1 dan 2
        secant_line = always_redraw(lambda:
            Line(
                axes.c2p(x1_tracker.get_value(), f(x1_tracker.get_value())),
                axes.c2p(x2_tracker.get_value(), f(x2_tracker.get_value())),
                color=GREEN_C, stroke_width=2.5
            )
        )

        # Panel Telemetri Definisi di Kanan
        panel_box = Rectangle(
            width=5.0, height=4.8,
            color=GRAY_D, stroke_width=1.5,
            fill_color="#0d1117", fill_opacity=0.85
        ).move_to(RIGHT * 3.8 + DOWN * 0.4)

        panel_title = Text("Uji Definisi Formal", font_size=20, color=BLUE_B).move_to(RIGHT * 3.8 + UP * 1.6)

        # Indikator x1 < x2 menggunakan DecimalNumber
        syarat_x = MathTex(r"\textbf{Premis Domain: } x_1 < x_2", font_size=19, color=WHITE).move_to(RIGHT * 3.8 + UP * 0.95)
        
        x1_num = DecimalNumber(1.2, num_decimal_places=2, font_size=18, color=TEAL_C)
        x1_num.add_updater(lambda d: d.set_value(x1_tracker.get_value()))
        lt_sym1 = MathTex(r"<", font_size=18, color=WHITE)
        x2_num = DecimalNumber(3.2, num_decimal_places=2, font_size=18, color=GOLD_B)
        x2_num.add_updater(lambda d: d.set_value(x2_tracker.get_value()))
        dx_label = MathTex(r"\implies \Delta x > 0", font_size=18, color=GREEN_C)

        group_dx = VGroup(x1_num, lt_sym1, x2_num, dx_label).arrange(RIGHT, buff=0.12).move_to(RIGHT * 3.8 + UP * 0.45)

        divider1 = Line(LEFT * 2.1, RIGHT * 2.1, color=GRAY_D, stroke_width=1).move_to(RIGHT * 3.8 + UP * 0.08)

        # Indikator f(x1) < f(x2) menggunakan DecimalNumber
        kesimpulan_y = MathTex(r"\textbf{Konsekuensi Nilai: } f(x_1) < f(x_2)", font_size=19, color=WHITE).move_to(RIGHT * 3.8 + DOWN * 0.3)
        
        fx1_num = DecimalNumber(f(1.2), num_decimal_places=2, font_size=18, color=TEAL_C)
        fx1_num.add_updater(lambda d: d.set_value(f(x1_tracker.get_value())))
        lt_sym2 = MathTex(r"<", font_size=18, color=WHITE)
        fx2_num = DecimalNumber(f(3.2), num_decimal_places=2, font_size=18, color=GOLD_B)
        fx2_num.add_updater(lambda d: d.set_value(f(x2_tracker.get_value())))
        dy_label = MathTex(r"\implies \Delta y > 0", font_size=18, color=GREEN_C)

        group_dy = VGroup(fx1_num, lt_sym2, fx2_num, dy_label).arrange(RIGHT, buff=0.12).move_to(RIGHT * 3.8 + DOWN * 0.75)

        divider2 = Line(LEFT * 2.1, RIGHT * 2.1, color=GRAY_D, stroke_width=1).move_to(RIGHT * 3.8 + DOWN * 1.15)

        # Kemiringan Sekan (Rasio Perubahan)
        slope_sekan = MathTex(
            r"m_{\text{sekan}} = \frac{f(x_2) - f(x_1)}{x_2 - x_1} > 0",
            font_size=18, color=YELLOW_B
        ).move_to(RIGHT * 3.8 + DOWN * 1.65)

        self.play(
            FadeIn(panel_box), Write(panel_title),
            Write(syarat_x), FadeIn(group_dx),
            Create(divider1),
            Write(kesimpulan_y), FadeIn(group_dy),
            Create(divider2),
            FadeIn(slope_sekan),
            Create(v_line1), Create(h_line1), FadeIn(label_x1), FadeIn(label_fx1), FadeIn(dot1),
            Create(v_line2), Create(h_line2), FadeIn(label_x2), FadeIn(label_fx2), FadeIn(dot2),
            Create(secant_line),
            run_time=2.0
        )
        self.wait(1.0)

        # -------------------------------------------------------------
        # AKSI 3: Inversi Sokratik (Uji Bergerak di Seluruh Domain)
        # -------------------------------------------------------------
        pertanyaan = Text(
            "Melangkah ke kanan (x1 < x2) SELALU menaikkan ketinggian (f(x1) < f(x2)).\nApakah sifat ini bertahan di mana pun kita memilih titik?",
            font_size=20,
            color=TEAL_A,
            line_spacing=1.2
        ).to_edge(UP, buff=0.25)

        self.play(Transform(judul, pertanyaan), run_time=1.5)
        self.wait(1.0)

        # Gerakkan x2 menjauh ke kanan
        self.play(x2_tracker.animate.set_value(4.4), run_time=2.5, rate_func=smooth)
        self.wait(0.8)

        # Gerakkan kedua titik bersamaan menelusuri kurva
        self.play(
            x1_tracker.animate.set_value(2.2),
            x2_tracker.animate.set_value(4.5),
            run_time=3.5, rate_func=smooth
        )
        self.wait(0.8)

        # Rapatkan x2 mendekati x1 (menuju konsep turunan)
        self.play(
            x1_tracker.animate.set_value(1.8),
            x2_tracker.animate.set_value(2.0),
            run_time=3.0, rate_func=smooth
        )
        self.wait(1.0)

        # -------------------------------------------------------------
        # AKSI 4: Kristalisasi Matematis Formal
        # -------------------------------------------------------------
        kristal_title = Text("Sintesis Definisi Formal", font_size=20, color=GOLD_B).move_to(RIGHT * 3.8 + UP * 1.6)

        kotak_definisi = MathTex(
            r"\forall x_1, x_2 \in I: \\",
            r"x_1 < x_2 \implies f(x_1) < f(x_2)",
            font_size=21
        ).move_to(RIGHT * 3.8 + UP * 0.7)
        kotak_definisi[1].set_color(GREEN_C)

        teorema_turunan = MathTex(
            r"\textbf{Uji Turunan Pertama:}\\",
            r"\lim_{x_2 \to x_1} \frac{f(x_2) - f(x_1)}{x_2 - x_1} = f'(x) \\",
            r"f'(x) > 0 \implies \text{Monoton Naik}",
            font_size=19
        ).move_to(RIGHT * 3.8 + DOWN * 0.7)
        teorema_turunan[2].set_color(GREEN_C)

        box_highlight = SurroundingRectangle(kotak_definisi, color=BLUE_B, buff=0.15)

        self.play(
            FadeOut(panel_title),
            FadeOut(syarat_x), FadeOut(group_dx),
            FadeOut(divider1),
            FadeOut(kesimpulan_y), FadeOut(group_dy),
            FadeOut(divider2),
            FadeOut(slope_sekan),
            FadeIn(kristal_title),
            Write(kotak_definisi),
            Create(box_highlight),
            Write(teorema_turunan),
            run_time=2.0
        )
        self.wait(3.0)
