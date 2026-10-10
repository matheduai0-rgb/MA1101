"""
Animasi Sokratik: Kemonotonan dan Kecekungan (MA1101)
Subtopik: 3.2 Kemonotonan, Kecekungan, dan Titik Belok
Bahasa: Indonesia
Gaya: Grant Sanderson (3Blue1Brown) & Pedagogi Sokratik
"""

from manim import *
import numpy as np

class MonotonicityConcavityScene(Scene):
    def construct(self):
        # -------------------------------------------------------------
        # AKSI 1: Tantangan Sokratik (The Pique)
        # -------------------------------------------------------------
        judul = Text(
            "Kapan sebuah kurva menanjak, menurun,\natau melengkung menampung air?",
            font_size=25,
            color=WHITE,
            line_spacing=1.2
        ).to_edge(UP, buff=0.35)

        self.play(Write(judul), run_time=1.5)
        self.wait(1.0)

        # Sumbu koordinat di sisi kiri
        axes = Axes(
            x_range=[-2.8, 2.8, 1],
            y_range=[-2.5, 2.5, 1],
            x_length=6.4,
            y_length=5.0,
            axis_config={"color": GRAY_C, "stroke_width": 2},
            tips=True
        ).add_coordinates()
        axes.shift(LEFT * 3.2 + DOWN * 0.3)

        # Kurva kubik f(x) = 0.35 * (x^3 - 3x)
        f = lambda x: 0.35 * (x**3 - 3 * x)
        f_prime = lambda x: 0.35 * (3 * x**2 - 3)
        f_double_prime = lambda x: 2.1 * x

        curve = axes.plot(f, x_range=[-2.35, 2.35], color=YELLOW, stroke_width=3.5)
        curve_label = MathTex(r"f(x) = \frac{7}{20}(x^3 - 3x)", color=YELLOW, font_size=20)
        curve_label.next_to(axes.c2p(1.7, f(1.7)), UR, buff=0.1)

        self.play(Create(axes), Create(curve), FadeIn(curve_label), run_time=2.0)
        self.wait(1.0)

        # -------------------------------------------------------------
        # AKSI 2: Eksplorasi Visual (Garis Singgung Dinamis & Telemetri)
        # -------------------------------------------------------------
        x_tracker = ValueTracker(-2.1)

        # Garis singgung dinamis
        def get_tangent_line():
            xv = x_tracker.get_value()
            yv = f(xv)
            m = f_prime(xv)
            dx = 0.8
            p1 = axes.c2p(xv - dx, yv - dx * m)
            p2 = axes.c2p(xv + dx, yv + dx * m)
            return Line(p1, p2, color=TEAL_C, stroke_width=3.5)

        tangent = always_redraw(get_tangent_line)
        dot = always_redraw(lambda:
            Dot(axes.c2p(x_tracker.get_value(), f(x_tracker.get_value())), color=RED_C, radius=0.08)
        )

        # Panel Telemetri Kalkulus di Sisi Kanan
        telemetry_title = Text("Telemetri Turunan", font_size=22, color=BLUE_B).move_to(RIGHT * 3.5 + UP * 2.3)
        telemetry_box = Rectangle(
            width=5.8,
            height=4.8,
            color=GRAY_D,
            stroke_width=1.5,
            fill_color="#0d1117",
            fill_opacity=0.85
        ).move_to(RIGHT * 3.5 + DOWN * 0.3)

        # Indikator x dengan DecimalNumber
        x_lbl = MathTex(r"x =", font_size=22).move_to(RIGHT * 3.0 + UP * 1.5)
        x_val = DecimalNumber(-2.1, num_decimal_places=2, font_size=22)
        x_val.next_to(x_lbl, RIGHT, buff=0.15)
        x_val.add_updater(lambda d: d.set_value(x_tracker.get_value()))

        # Indikator f'(x)
        slope_lbl = MathTex(r"m = f'(x) =", font_size=22).move_to(RIGHT * 2.8 + UP * 0.8)
        slope_val = DecimalNumber(f_prime(-2.1), num_decimal_places=2, font_size=22)
        slope_val.next_to(slope_lbl, RIGHT, buff=0.15)
        slope_val.add_updater(lambda d: d.set_value(f_prime(x_tracker.get_value())))

        mono_pos = RIGHT * 3.5 + UP * 0.25
        status_mono = always_redraw(lambda:
            Text(
                "Kurva Naik (f' > 0)" if f_prime(x_tracker.get_value()) > 0.08 else
                ("Kurva Turun (f' < 0)" if f_prime(x_tracker.get_value()) < -0.08 else "Titik Stasioner (f' ≈ 0)"),
                font_size=18,
                color=GREEN_C if f_prime(x_tracker.get_value()) > 0.08 else
                (RED_C if f_prime(x_tracker.get_value()) < -0.08 else YELLOW)
            ).move_to(mono_pos)
        )

        divider_line = Line(LEFT * 2.5, RIGHT * 2.5, color=GRAY_D, stroke_width=1).move_to(RIGHT * 3.5 + DOWN * 0.3)

        # Indikator f''(x)
        fpp_lbl = MathTex(r"f''(x) =", font_size=22).move_to(RIGHT * 2.9 + DOWN * 0.8)
        fpp_val = DecimalNumber(f_double_prime(-2.1), num_decimal_places=2, font_size=22)
        fpp_val.next_to(fpp_lbl, RIGHT, buff=0.15)
        fpp_val.add_updater(lambda d: d.set_value(f_double_prime(x_tracker.get_value())))

        concav_pos = RIGHT * 3.5 + DOWN * 1.35
        status_concav = always_redraw(lambda:
            Text(
                "Cekung ke Bawah (f'' < 0)" if f_double_prime(x_tracker.get_value()) < -0.15 else
                ("Cekung ke Atas (f'' > 0)" if f_double_prime(x_tracker.get_value()) > 0.15 else "Titik Belok (f'' ≈ 0)"),
                font_size=17,
                color=ORANGE if f_double_prime(x_tracker.get_value()) < -0.15 else
                (TEAL_B if f_double_prime(x_tracker.get_value()) > 0.15 else PINK)
            ).move_to(concav_pos)
        )

        # Tampilkan elemen telemetri secara terpisah
        self.play(
            FadeIn(telemetry_box),
            Write(telemetry_title),
            Write(x_lbl),
            FadeIn(x_val),
            Write(slope_lbl),
            FadeIn(slope_val),
            FadeIn(status_mono),
            Create(divider_line),
            Write(fpp_lbl),
            FadeIn(fpp_val),
            FadeIn(status_concav),
            Create(tangent),
            FadeIn(dot),
            run_time=1.5
        )
        self.wait(1.0)

        # -------------------------------------------------------------
        # AKSI 3: Pertanyaan Sokratik (Arah Rotasi & Titik Belok)
        # -------------------------------------------------------------
        pertanyaan = Text(
            "Perhatikan arah rotasi garis singgung:\nsearah jarum jam (f'' < 0), lalu berbalik arah (f'' > 0).\nDi manakah titik pergantian kelengkungan kurva?",
            font_size=21,
            color=TEAL_A,
            line_spacing=1.2
        ).to_edge(UP, buff=0.25)

        self.play(Transform(judul, pertanyaan), run_time=1.5)
        self.wait(1.0)

        # Gerakkan titik menelusuri kurva dari -2.1 hingga 2.1
        self.play(x_tracker.animate.set_value(2.1), run_time=8.0, rate_func=smooth)
        self.wait(1.5)

        # Kembalikan titik ke x = 0 (Titik Belok)
        self.play(x_tracker.animate.set_value(0.0), run_time=2.0, rate_func=smooth)
        self.wait(1.0)

        # -------------------------------------------------------------
        # AKSI 4: Kristalisasi Matematis Formal
        # -------------------------------------------------------------
        pt_belok = Dot(axes.c2p(0, 0), color=PINK, radius=0.12)
        glow_belok = Dot(axes.c2p(0, 0), color=PINK, radius=0.25, fill_opacity=0.35)
        label_belok = Text("Titik Belok (0, 0)", font_size=18, color=PINK).next_to(pt_belok, UR, buff=0.15)

        self.play(FadeIn(glow_belok), FadeIn(pt_belok), Write(label_belok))
        self.wait(1.0)

        # Kartu Teorema Formal
        kristalisasi_group = VGroup()
        judul_kristal = Text("Sintesis Teorema Kalkulus", font_size=20, color=GOLD_B).move_to(RIGHT * 3.5 + UP * 1.8)

        teorema_1 = MathTex(
            r"\textbf{Kemonotonan } (f'): \\",
            r"f'(x) > 0 &\implies \text{Kurva Naik} \\",
            r"f'(x) < 0 &\implies \text{Kurva Turun}",
            font_size=20
        ).move_to(RIGHT * 3.5 + UP * 0.7)
        teorema_1[1].set_color(GREEN_C)
        teorema_1[2].set_color(RED_C)

        teorema_2 = MathTex(
            r"\textbf{Kecekungan } (f''): \\",
            r"f''(x) > 0 &\implies \text{Cekung ke Atas } (\cup) \\",
            r"f''(x) < 0 &\implies \text{Cekung ke Bawah } (\cap)",
            font_size=20
        ).move_to(RIGHT * 3.5 + DOWN * 0.6)
        teorema_2[1].set_color(TEAL_B)
        teorema_2[2].set_color(ORANGE)

        teorema_3 = MathTex(
            r"\textbf{Titik Belok: } \text{Perubahan tanda } f'' \text{ di } (c, f(c))",
            font_size=18,
            color=PINK
        ).move_to(RIGHT * 3.5 + DOWN * 1.8)

        kristalisasi_group.add(judul_kristal, teorema_1, teorema_2, teorema_3)

        self.play(
            FadeOut(telemetry_title),
            FadeOut(x_lbl), FadeOut(x_val),
            FadeOut(slope_lbl), FadeOut(slope_val), FadeOut(status_mono),
            FadeOut(divider_line),
            FadeOut(fpp_lbl), FadeOut(fpp_val), FadeOut(status_concav),
            FadeIn(kristalisasi_group),
            run_time=1.5
        )
        self.wait(3.0)
