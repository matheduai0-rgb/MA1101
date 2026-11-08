"""
Template: Luas Daerah dengan Poligon Dalam, Poligon Luar & Notasi Sigma (MA1101 Subtopik 4.1)
Subtopik: 4.1 Luas Daerah (Area — Inscribed & Circumscribed Polygons, Sigma Notation)
Bahasa: Indonesia
Gaya: Grant Sanderson (3Blue1Brown) & Metode Sokratik
Deskripsi:
  Visualisasi 4 babak mengenai penghampiran luas daerah R di bawah parabola y = x^2
  pada selang [0, 2] menggunakan Poligon Dalam (R_n) dan Poligon Luar (S_n).
  Memperlihatkan penjepitan luas A(R_n) <= A(R) <= A(S_n), penyusutan celah galat
  A(S_n) - A(R_n) = 8/n saat n membesar (4 -> 8 -> 16 -> 32 -> 64), serta
  kristalisasi formal dengan rumus jumlah kuadrat Sigma menuju nilai eksak 8/3.
"""

from manim import *
import numpy as np


class PolygonAreaExhaustionScene(Scene):
    def construct(self):
        # -------------------------------------------------------------
        # AKSI 1: Tantangan Sokratik (Poligon Dalam vs Poligon Luar)
        # -------------------------------------------------------------
        judul = Text(
            "Bagaimana menghitung luas daerah melengkung secara eksak\njika kita hanya tahu rumus luas persegi panjang?",
            font_size=22,
            line_spacing=1.2,
            color=WHITE
        ).to_edge(UP, buff=0.28)

        self.play(Write(judul), run_time=1.3)
        self.wait(0.4)

        axes = Axes(
            x_range=[0, 2.35, 0.5],
            y_range=[0, 4.6, 1.0],
            x_length=6.6,
            y_length=4.5,
            axis_config={"color": GRAY_C, "stroke_width": 1.6},
            x_axis_config={"decimal_number_config": {"num_decimal_places": 1}},
            y_axis_config={"decimal_number_config": {"num_decimal_places": 0}},
        ).add_coordinates(font_size=16)
        axes.shift(LEFT * 2.45 + DOWN * 0.52)

        axis_labels = axes.get_axis_labels(
            x_label=MathTex("x", font_size=20, color=GRAY_B),
            y_label=MathTex("y", font_size=20, color=GRAY_B)
        )

        func = lambda x: x ** 2
        curve = axes.plot(func, x_range=[0, 2.08], color=YELLOW, stroke_width=3.6)
        curve_lbl = MathTex(r"y = f(x) = x^2", font_size=21, color=YELLOW).next_to(
            axes.c2p(1.55, 2.4), UP + LEFT, buff=0.12
        )

        bound_line = axes.get_vertical_line(axes.c2p(2.0, 4.0), color=GRAY_B, stroke_width=1.6)
        target_area = axes.get_area(curve, x_range=[0.0, 2.0], color=BLUE_E, opacity=0.28)
        region_lbl = MathTex(r"R", font_size=28, color=BLUE_B).move_to(axes.c2p(1.35, 0.75))

        self.play(Create(axes), FadeIn(axis_labels), run_time=0.9)
        self.play(
            Create(curve),
            Write(curve_lbl),
            Create(bound_line),
            FadeIn(target_area),
            FadeIn(region_lbl),
            run_time=1.3
        )
        self.wait(0.5)

        # Helper pembuat poligon dalam (left) & poligon luar (right) pada [0, 2]
        def make_polygons(n_slices):
            dx = 2.0 / n_slices
            sw = 1.3 if n_slices <= 8 else (0.75 if n_slices <= 16 else (0.35 if n_slices <= 32 else 0.15))

            outer_rects = axes.get_riemann_rectangles(
                curve,
                x_range=[0.0, 2.0],
                dx=dx,
                input_sample_type="right",
                stroke_width=sw,
                stroke_color=MAROON_A,
                fill_opacity=0.35,
                color=(MAROON_C, GOLD_C)
            )
            inner_rects = axes.get_riemann_rectangles(
                curve,
                x_range=[0.0, 2.0],
                dx=dx,
                input_sample_type="left",
                stroke_width=sw,
                stroke_color=TEAL_A,
                fill_opacity=0.58,
                color=(BLUE_D, TEAL_C)
            )
            return inner_rects, outer_rects

        def calc_bounds(n_slices):
            # A(R_n) = 8/3 - 4/n + 4/(3n^2), A(S_n) = 8/3 + 4/n + 4/(3n^2)
            r_n = (8.0 / 3.0) - (4.0 / n_slices) + (4.0 / (3.0 * (n_slices ** 2)))
            s_n = (8.0 / 3.0) + (4.0 / n_slices) + (4.0 / (3.0 * (n_slices ** 2)))
            return r_n, s_n

        inner_4, outer_4 = make_polygons(4)

        info_card = VGroup(
            Text("Metode Jepit Archimedes:", font_size=15, color=GOLD_B),
            MathTex(r"R_n \text{ (Poligon Dalam)} \le R \le S_n \text{ (Poligon Luar)}", font_size=17, color=WHITE),
            MathTex(r"A(R_n) = \sum_{i=1}^{n} f(x_{i-1})\,\Delta x \quad (\text{Batas Bawah})", font_size=17, color=TEAL_B),
            MathTex(r"A(S_n) = \sum_{i=1}^{n} f(x_i)\,\Delta x \quad (\text{Batas Atas})", font_size=17, color=MAROON_B),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.11).move_to(RIGHT * 3.35 + UP * 1.55)

        info_box = SurroundingRectangle(
            info_card, color=BLUE_D, fill_color="#141B28", fill_opacity=0.92, buff=0.16, corner_radius=0.1
        )

        self.play(
            FadeOut(target_area),
            FadeOut(region_lbl),
            Create(outer_4),
            FadeIn(info_box),
            Write(info_card),
            run_time=1.4
        )
        self.play(Create(inner_4), run_time=1.1)
        self.wait(0.6)

        # -------------------------------------------------------------
        # AKSI 2: Eksplorasi Visual (Penghalusan Partisi & Penyusutan Celah)
        # -------------------------------------------------------------
        def make_telemetry(n_val):
            r_val, s_val = calc_bounds(n_val)
            gap_val = s_val - r_val
            dx_val = 2.0 / n_val
            grp = VGroup(
                MathTex(rf"n = {n_val} \;\;\; (\Delta x = 2/{n_val} = {dx_val:.3f})", font_size=18, color=YELLOW),
                MathTex(rf"A(R_{{{n_val}}}) = {r_val:.3f} \;\le\; A(R) \;\le\; A(S_{{{n_val}}}) = {s_val:.3f}", font_size=18, color=WHITE),
                MathTex(rf"\text{{Celah Galat: }} A(S_{{{n_val}}}) - A(R_{{{n_val}}}) = \frac{{8}}{{{n_val}}} = {gap_val:.3f}", font_size=17, color=GREEN_B),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.10).move_to(RIGHT * 3.35 + DOWN * 0.22)
            box = SurroundingRectangle(
                grp, color=TEAL_C, fill_color="#141B28", fill_opacity=0.92, buff=0.15, corner_radius=0.1
            )
            return VGroup(box, grp)

        telemetry = make_telemetry(4)
        self.play(FadeIn(telemetry), run_time=0.8)
        self.wait(0.6)

        for n_step, rt in [(8, 1.1), (16, 1.1), (32, 1.1)]:
            new_in, new_out = make_polygons(n_step)
            new_tel = make_telemetry(n_step)
            self.play(
                Transform(outer_4, new_out),
                Transform(inner_4, new_in),
                Transform(telemetry, new_tel),
                run_time=rt,
                rate_func=smooth
            )
            self.wait(0.35)

        # -------------------------------------------------------------
        # AKSI 3: Pertanyaan Sokratik (Apa yang Terjadi Saat n -> tak hingga?)
        # -------------------------------------------------------------
        pertanyaan = Text(
            "Apa yang terjadi pada celah antara Poligon Luar dan Poligon Dalam\nsaat jumlah irisan n menuju tak hingga?",
            font_size=21,
            color=TEAL_A,
            line_spacing=1.2
        ).to_edge(UP, buff=0.28)

        self.play(Transform(judul, pertanyaan), run_time=1.0)
        self.wait(1.6)

        new_in_64, new_out_64 = make_polygons(64)
        new_tel_64 = make_telemetry(64)
        self.play(
            Transform(outer_4, new_out_64),
            Transform(inner_4, new_in_64),
            Transform(telemetry, new_tel_64),
            run_time=1.2,
            rate_func=smooth
        )
        self.wait(0.4)

        exact_area = axes.get_area(curve, x_range=[0.0, 2.0], color=(BLUE_D, TEAL_C), opacity=0.68)
        exact_label = MathTex(r"A(R) = \frac{8}{3} \approx 2.667", font_size=22, color=YELLOW).move_to(
            axes.c2p(1.32, 0.72)
        )
        exact_label_bg = BackgroundRectangle(exact_label, fill_color="#0C1018", fill_opacity=0.82, buff=0.08)

        self.play(
            FadeOut(outer_4),
            ReplacementTransform(inner_4, exact_area),
            FadeIn(exact_label_bg),
            Write(exact_label),
            run_time=1.4
        )
        self.wait(0.6)

        # -------------------------------------------------------------
        # AKSI 4: Kristalisasi Formal (Notasi Sigma & Limit Jumlah Khusus)
        # -------------------------------------------------------------
        judul_kristal = Text(
            "Definisi Luas Daerah: Limit Poligon & Rumus Jumlah Kuadrat Sigma",
            font_size=21,
            color=GOLD_B
        ).to_edge(UP, buff=0.28)

        kristal_card = VGroup(
            MathTex(
                r"A(S_n) = \sum_{i=1}^{n} \left(\frac{2i}{n}\right)^2 \frac{2}{n} = \frac{8}{n^3}\sum_{i=1}^{n} i^2",
                font_size=18,
                color=WHITE
            ),
            MathTex(
                r"= \frac{8}{n^3}\cdot\frac{n(n+1)(2n+1)}{6} = \frac{8}{3} + \frac{4}{n} + \frac{4}{3n^2}",
                font_size=18,
                color=TEAL_B
            ),
            MathTex(
                r"A(R) = \lim_{n\to\infty} A(R_n) = \lim_{n\to\infty} A(S_n) = \frac{8}{3}",
                font_size=20,
                color=GOLD_B
            ),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.11).move_to(RIGHT * 3.35 + DOWN * 2.12)

        kristal_box = SurroundingRectangle(
            kristal_card, color=GOLD_B, fill_color="#141B28", fill_opacity=0.95, buff=0.15, corner_radius=0.1
        )

        self.play(
            Transform(judul, judul_kristal),
            FadeIn(kristal_box),
            Write(kristal_card),
            run_time=1.6
        )
        self.wait(2.5)
