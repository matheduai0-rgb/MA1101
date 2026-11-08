"""
Animasi Sokratik: Pemodelan Matematika - Lintasan Pipa Lepas Pantai (MA1101)
Subtopik: 3.4 Pemodelan Matematika & Optimasi Terapan (Pipeline Cost Optimization)
Bahasa: Indonesia
Gaya: Grant Sanderson (3Blue1Brown) & Pedagogi Sokratik
"""

from manim import *
import numpy as np

class PipelineOptimizationScene(Scene):
    def construct(self):
        # -------------------------------------------------------------
        # AKSI 1: Dilema Dunia Nyata (The Pique / Dilemma)
        # -------------------------------------------------------------
        judul = Text(
            "Mengapa garis lurus terpendek BUKAN lintasan termurah?",
            font_size=23,
            color=WHITE
        ).to_edge(UP, buff=0.35)

        self.play(Write(judul), run_time=1.3)
        self.wait(0.8)

        # Visual Peta Fisik di sisi kiri (x in [-6, -0.5], y in [-3, 2.5])
        # Laut di bagian atas, Daratan di bagian bawah
        sea_zone = Rectangle(
            width=5.6, height=2.4,
            color=BLUE_E, fill_color="#0a2236", fill_opacity=0.6, stroke_width=0
        ).move_to(LEFT * 3.4 + UP * 1.0)

        land_zone = Rectangle(
            width=5.6, height=2.6,
            color=GRAY_D, fill_color="#182318", fill_opacity=0.6, stroke_width=0
        ).move_to(LEFT * 3.4 + DOWN * 1.5)

        coastline = Line(
            LEFT * 6.2 + DOWN * 0.2, LEFT * 0.6 + DOWN * 0.2,
            color=GOLD_C, stroke_width=3
        )
        coast_label = Text("Garis Pantai", font_size=14, color=GOLD_C).next_to(coastline, DOWN, buff=0.1).shift(LEFT * 1.8)

        # Posisi Kilang Minyak R (Laut): koordinat lokal (x=0, y=3 km offshore)
        # Posisi Stasiun Tangki T (Darat): (x=8 km sepanjang pantai, y=0)
        # Skala peta: 1 km = 0.5 unit manim
        map_origin = LEFT * 5.8 + DOWN * 0.2
        p_scale = 0.55

        pos_rig = map_origin + UP * (3.0 * p_scale)
        pos_tank = map_origin + RIGHT * (8.0 * p_scale)

        rig_dot = Dot(pos_rig, color=YELLOW, radius=0.1)
        rig_label = Text("Kilang Minyak R\n(3 km di laut)", font_size=13, color=YELLOW).next_to(rig_dot, UL, buff=0.1)

        tank_dot = Dot(pos_tank, color=GREEN_C, radius=0.1)
        tank_label = Text("Tangki Darat T\n(8 km)", font_size=13, color=GREEN_C).next_to(tank_dot, DR, buff=0.1)

        cost_info = VGroup(
            Text("Biaya Pipa Laut: 5 juta / km", font_size=13, color=BLUE_B),
            Text("Biaya Pipa Darat: 3 juta / km", font_size=13, color=GREEN_B),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1).move_to(LEFT * 3.4 + DOWN * 2.2)

        self.play(
            FadeIn(sea_zone), FadeIn(land_zone),
            Create(coastline), FadeIn(coast_label),
            Create(rig_dot), Write(rig_label),
            Create(tank_dot), Write(tank_label),
            FadeIn(cost_info),
            run_time=1.8
        )
        self.wait(1.0)

        # -------------------------------------------------------------
        # AKSI 2: Eksplorasi Visual & Grafik Biaya C(x)
        # -------------------------------------------------------------
        # Sumbu koordinat fungsi biaya di sisi kanan
        # Domain x in [0, 8], Biaya C(x) in [30, 45]
        axes = Axes(
            x_range=[0, 8.5, 2],
            y_range=[32, 45, 4],
            x_length=5.6,
            y_length=4.8,
            axis_config={"color": GRAY_C, "stroke_width": 2},
            tips=True
        ).add_coordinates()
        axes.shift(RIGHT * 3.4 + DOWN * 0.2)

        # Fungsi Biaya C(x) = 5 * sqrt(9 + x^2) + 3 * (8 - x)
        C_fn = lambda x: 5.0 * np.sqrt(9.0 + x**2) + 3.0 * (8.0 - x)
        C_curve = axes.plot(C_fn, x_range=[0, 8], color=TEAL_C, stroke_width=3.5)
        curve_title = MathTex(r"C(x) = 5\sqrt{9 + x^2} + 3(8 - x)", color=TEAL_C, font_size=19).move_to(RIGHT * 3.4 + UP * 2.5)

        self.play(Create(axes), Create(C_curve), Write(curve_title), run_time=1.6)

        # -------------------------------------------------------------
        # AKSI 3: Pergeseran Titik Pendaratan x & Pertanyaan Sokratik
        # -------------------------------------------------------------
        x_tracker = ValueTracker(0.0)

        # Garis pipa dinamis di peta fisik
        def get_water_pipe():
            xv = x_tracker.get_value()
            landing_pos = map_origin + RIGHT * (xv * p_scale)
            return Line(pos_rig, landing_pos, color=BLUE_B, stroke_width=3.5)

        def get_land_pipe():
            xv = x_tracker.get_value()
            landing_pos = map_origin + RIGHT * (xv * p_scale)
            return Line(landing_pos, pos_tank, color=GREEN_C, stroke_width=3.5)

        def get_landing_dot():
            xv = x_tracker.get_value()
            landing_pos = map_origin + RIGHT * (xv * p_scale)
            return Dot(landing_pos, color=GOLD_B, radius=0.08)

        water_pipe = always_redraw(get_water_pipe)
        land_pipe = always_redraw(get_land_pipe)
        landing_dot = always_redraw(get_landing_dot)

        # Indikator kurva biaya di kanan
        dot_curve = always_redraw(lambda:
            Dot(axes.c2p(x_tracker.get_value(), C_fn(x_tracker.get_value())), color=RED_C, radius=0.08)
        )
        line_drop = always_redraw(lambda:
            axes.get_vertical_line(axes.c2p(x_tracker.get_value(), C_fn(x_tracker.get_value())), color=RED_C).set_stroke(width=1.5, opacity=0.7)
        )

        label_telemetry = always_redraw(lambda:
            MathTex(
                rf"x = {x_tracker.get_value():.2f}\text{{ km}} \implies C = {C_fn(x_tracker.get_value()):.2f}\text{{ jt}}",
                color=GOLD_B,
                font_size=19
            ).move_to(RIGHT * 3.4 + DOWN * 2.3)
        )

        self.play(
            Create(water_pipe), Create(land_pipe), Create(landing_dot),
            FadeIn(dot_curve), Create(line_drop), Write(label_telemetry),
            run_time=1.2
        )
        self.wait(0.8)

        # Pertanyaan Sokratik
        pertanyaan = Text(
            "Di mana titik keseimbangan saat laju biaya air = laju biaya darat?",
            font_size=21,
            color=TEAL_A
        ).to_edge(UP, buff=0.35)
        self.play(Transform(judul, pertanyaan), run_time=1.0)

        # Animasikan pergeseran x dari 0 -> 8 -> titik optimal 2.25
        self.play(x_tracker.animate.set_value(8.0), run_time=3.5, rate_func=smooth)
        self.wait(1.0)
        self.play(x_tracker.animate.set_value(2.25), run_time=3.0, rate_func=smooth)
        self.wait(1.2)

        # -------------------------------------------------------------
        # AKSI 4: Kristalisasi Formal (Titik Kritis & Keseimbangan Marjinal)
        # -------------------------------------------------------------
        final_judul = Text(
            "Optimum Mutlak di x = 2.25 km: Biaya Minimum Rp 36,00 Juta!",
            font_size=20,
            color=GOLD_B
        ).to_edge(UP, buff=0.35)
        self.play(Transform(judul, final_judul), run_time=0.9)

        # Tangent mendatar di x = 2.25
        tangent_min = Line(
            axes.c2p(1.2, 36.0), axes.c2p(3.3, 36.0),
            color=GOLD_B, stroke_width=3
        )
        lbl_tangent = MathTex(r"C'(x) = 0", color=GOLD_B, font_size=18).next_to(tangent_min, UP, buff=0.1)

        # Kotak pembuktian turunan
        deriv_box = VGroup(
            MathTex(r"C'(x) = \frac{5x}{\sqrt{9+x^2}} - 3 = 0", font_size=18, color=YELLOW),
            MathTex(r"5x = 3\sqrt{9+x^2} \implies 16x^2 = 81", font_size=17, color=WHITE),
            MathTex(r"\mathbf{x = 2.25\text{ km}} \implies C_{\min} = \mathbf{36\text{ juta}}", font_size=18, color=GREEN_C)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.12)
        deriv_box.move_to(RIGHT * 3.4 + UP * 1.2)

        box_rect = SurroundingRectangle(deriv_box, color=BLUE_B, fill_color="#0e1420", fill_opacity=0.9, buff=0.15)

        self.play(
            Create(tangent_min), Write(lbl_tangent),
            FadeIn(box_rect), Write(deriv_box),
            Flash(dot_curve, color=GOLD_B),
            run_time=2.0
        )
        self.wait(2.5)
