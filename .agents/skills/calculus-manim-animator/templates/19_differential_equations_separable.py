"""
Template: Pengantar Persamaan Diferensial & Pemisahan Peubah (MA1101 Subtopik 3.9)
Subtopik: 3.9 Pengantar Persamaan Diferensial (Introduction to Differential Equations)
Bahasa: Indonesia
Gaya: Grant Sanderson (3Blue1Brown) & Metode Sokratik
Deskripsi:
  Visualisasi 4 babak mengenai Persamaan Diferensial Terpisahkan (Soal Bab 3 No. 26c):
  dy/dx = (6x - x^3)/(2y) dengan syarat awal y(0) = 3. Memperlihatkan medan arah 2D
  yang bergantung pada (x, y), mekanisme pemisahan peubah 2y dy = (6x - x^3) dx,
  keluarga kurva solusi umum, serta pemilihan solusi khusus Masalah Nilai Awal (MNA).
"""

from manim import *
import numpy as np


class SeparableODEScene(Scene):
    def construct(self):
        # -------------------------------------------------------------
        # AKSI 1: Tantangan Sokratik (Medan Arah Bergantung pada x dan y)
        # -------------------------------------------------------------
        judul = Text(
            "Bagaimana jika kemiringan kurva dy/dx bergantung\npada posisi x DAN ketinggian y sekaligus?",
            font_size=22,
            line_spacing=1.2,
            color=WHITE
        ).to_edge(UP, buff=0.3)

        self.play(Write(judul), run_time=1.3)
        self.wait(0.4)

        axes = Axes(
            x_range=[-3.5, 3.5, 1],
            y_range=[0, 5.2, 1],
            x_length=7.3,
            y_length=4.6,
            axis_config={"color": GRAY_C, "stroke_width": 1.5}
        ).add_coordinates(font_size=16)
        axes.shift(LEFT * 2.15 + DOWN * 0.48)

        axis_labels = axes.get_axis_labels(
            x_label=MathTex("x", font_size=20, color=GRAY_B),
            y_label=MathTex("y", font_size=20, color=GRAY_B)
        )

        # Medan arah untuk dy/dx = (6x - x^3) / (2y)
        slope_func = lambda x, y: (6.0 * x - x ** 3) / (2.0 * max(y, 0.35))

        slope_segments = VGroup()
        for xv in np.linspace(-3.0, 3.0, 13):
            for yv in np.linspace(0.55, 4.75, 9):
                m = slope_func(xv, yv)
                dx = 0.21 / np.sqrt(1.0 + m ** 2)
                dy = m * dx
                seg = Line(
                    axes.c2p(xv - dx, yv - dy),
                    axes.c2p(xv + dx, yv + dy),
                    color=BLUE_D,
                    stroke_width=1.6,
                    stroke_opacity=0.58
                )
                slope_segments.add(seg)

        info_pos = RIGHT * 3.55 + UP * 1.45
        ode_card = VGroup(
            Text("PD Terpisahkan (Soal 26c):", font_size=15, color=BLUE_B),
            MathTex(r"\frac{dy}{dx} = \frac{6x - x^3}{2y}", font_size=23, color=BLUE_C),
            MathTex(r"\implies 2y\,dy = (6x - x^3)\,dx", font_size=19, color=TEAL_B)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.12).move_to(info_pos)
        ode_box = SurroundingRectangle(
            ode_card, color=BLUE_D, fill_color="#141B28", fill_opacity=0.92, buff=0.16, corner_radius=0.1
        )

        self.play(Create(axes), FadeIn(axis_labels), run_time=1.0)
        self.play(
            LaggedStart(*[Create(s) for s in slope_segments], lag_ratio=0.01),
            FadeIn(ode_box),
            Write(ode_card),
            run_time=1.6
        )
        self.wait(0.6)

        # -------------------------------------------------------------
        # AKSI 2: Eksplorasi Visual (Integrasi Kedua Ruas & Keluarga Kurva)
        # -------------------------------------------------------------
        c_tracker = ValueTracker(4.0)

        # Solusi eksplisit cabang y > 0: y(x) = sqrt(3x^2 - 0.25 x^4 + C)
        y_sol = lambda x, c: np.sqrt(max(3.0 * (x ** 2) - 0.25 * (x ** 4) + c, 0.05))

        active_curve = always_redraw(lambda:
            axes.plot(
                lambda x: y_sol(x, c_tracker.get_value()),
                x_range=[-3.15, 3.15],
                color=YELLOW,
                stroke_width=3.8
            )
        )

        sol_umum_readout = always_redraw(lambda:
            MathTex(
                r"y^2 = 3x^2 - \frac{1}{4}x^4",
                f"{c_tracker.get_value():+.1f}",
                font_size=21,
                color=YELLOW
            ).next_to(ode_box, DOWN, buff=0.24)
        )

        self.play(Create(active_curve), Write(sol_umum_readout), run_time=1.1)
        self.wait(0.4)

        # Jejak keluarga kurva untuk C = 1.0, 3.0, 5.5, 9.0
        c_list = [1.0, 3.0, 5.5, 9.0]
        c_colors = [TEAL_D, TEAL_B, GREEN_C, MAROON_B]
        family_curves = VGroup()

        for c_val, col in zip(c_list, c_colors):
            self.play(c_tracker.animate.set_value(c_val), run_time=0.7, rate_func=smooth)
            ghost_curve = axes.plot(
                lambda x, c=c_val: y_sol(x, c),
                x_range=[-3.15, 3.15],
                color=col,
                stroke_width=2.0,
                stroke_opacity=0.65
            )
            family_curves.add(ghost_curve)
            self.add(ghost_curve)

        self.wait(0.5)

        # -------------------------------------------------------------
        # AKSI 3: Pertanyaan Sokratik (Masalah Nilai Awal y(0) = 3)
        # -------------------------------------------------------------
        pertanyaan = Text(
            "Kurva manakah yang memenuhi syarat awal y = 3 di x = 0,\ndan di mana puncak tertingginya?",
            font_size=21,
            color=TEAL_A,
            line_spacing=1.2
        ).to_edge(UP, buff=0.3)

        self.play(Transform(judul, pertanyaan), run_time=1.0)
        self.wait(1.5)

        # Titik awal P(0, 3) -> y(0)^2 = C => 3^2 = 9 => C = 9
        pt_init = Dot(axes.c2p(0.0, 3.0), color=GREEN_B, radius=0.09)
        ring_init = Circle(radius=0.18, color=GREEN_B, stroke_width=2.5).move_to(axes.c2p(0.0, 3.0))
        lbl_init = MathTex(r"y(0) = 3", color=GREEN_B, font_size=19).next_to(ring_init, UP, buff=0.12).shift(RIGHT * 0.55)

        mna_text = MathTex(
            r"\text{MNA: } y(0)=3 \implies C = 3^2 = 9",
            font_size=19,
            color=GREEN_B
        ).next_to(sol_umum_readout, DOWN, buff=0.22)

        self.play(
            c_tracker.animate.set_value(2.0),
            FadeIn(pt_init),
            Create(ring_init),
            Write(lbl_init),
            run_time=0.8
        )
        self.play(
            c_tracker.animate.set_value(9.0),
            Indicate(ring_init, color=YELLOW, scale_factor=1.3),
            Write(mna_text),
            run_time=1.5,
            rate_func=smooth
        )

        # Luncurkan titik uji dari x = 0 menuju puncak x = sqrt(6) ≈ 2.45 (di mana dy/dx = 0)
        x_glide = ValueTracker(0.0)
        glide_dot = always_redraw(lambda:
            Dot(axes.c2p(x_glide.get_value(), y_sol(x_glide.get_value(), 9.0)), color=RED_C, radius=0.08)
        )
        glide_tangent = always_redraw(lambda:
            Line(
                axes.c2p(
                    x_glide.get_value() - 0.65,
                    y_sol(x_glide.get_value(), 9.0) - 0.65 * slope_func(x_glide.get_value(), y_sol(x_glide.get_value(), 9.0))
                ),
                axes.c2p(
                    x_glide.get_value() + 0.65,
                    y_sol(x_glide.get_value(), 9.0) + 0.65 * slope_func(x_glide.get_value(), y_sol(x_glide.get_value(), 9.0))
                ),
                color=RED_C,
                stroke_width=2.8
            )
        )

        self.play(FadeIn(glide_dot), Create(glide_tangent), run_time=0.6)
        self.play(x_glide.animate.set_value(np.sqrt(6.0)), run_time=1.8, rate_func=smooth)

        peak_label = MathTex(
            r"x = \sqrt{6},\; y = \sqrt{18}",
            font_size=17,
            color=RED_B
        ).next_to(axes.c2p(np.sqrt(6.0), np.sqrt(18.0)), UP, buff=0.14).shift(LEFT * 0.15)
        self.play(FadeIn(peak_label), run_time=0.6)
        self.wait(0.6)

        # -------------------------------------------------------------
        # AKSI 4: Kristalisasi Formal (Metode Pemisahan Peubah & Solusi Khusus)
        # -------------------------------------------------------------
        judul_kristal = Text(
            "Metode Pemisahan Peubah & Masalah Nilai Awal (MNA)",
            font_size=21,
            color=GOLD_B
        ).to_edge(UP, buff=0.3)

        rumus_umum = MathTex(
            r"\int h(y)\,dy = \int g(x)\,dx + C",
            font_size=22,
            color=GOLD_B
        )
        solusi_khusus = MathTex(
            r"y(x) = \sqrt{3x^2 - \frac{1}{4}x^4 + 9}",
            font_size=22,
            color=YELLOW
        )

        kristal_group = VGroup(rumus_umum, solusi_khusus).arrange(DOWN, buff=0.14)
        kristal_group.move_to(RIGHT * 3.55 + DOWN * 2.15)
        kristal_box = SurroundingRectangle(
            kristal_group, color=GOLD_B, fill_color="#141B28", fill_opacity=0.95, buff=0.16, corner_radius=0.1
        )

        self.play(
            Transform(judul, judul_kristal),
            FadeIn(kristal_box),
            Write(rumus_umum),
            Write(solusi_khusus),
            run_time=1.5
        )
        self.wait(2.5)
