"""
Template: Selisih Jumlah Riemann A(S_n) - A(R_n) Menuju Nol (MA1101 Subtopik 4.1 & 4.2)
Subtopik: 4.1 Luas Daerah & Jumlah Riemann (Poligon Dalam vs Poligon Luar & Menara Teleskopik)
Bahasa: Indonesia
Gaya: Grant Sanderson (3Blue1Brown) & Metode Sokratik
Deskripsi:
  Visualisasi 4 babak yang membuktikan secara geometris mengapa selisih antara
  Poligon Luar A(S_n) dan Poligon Dalam A(R_n) lenyap ke nol saat n -> tak hingga.
  Blok-blok galat selisih dari setiap pias digeser horizontal membentuk satu menara
  persegi panjang tunggal setinggi [f(b) - f(a)] dan selebar Delta x.
  Saat n membesar, ketebalan menara memipih ke 0, sehingga membuktikan
  lim [A(S_n) - A(R_n)] = 0 dan A(R) = 8/3 lewat Teorema Apit tanpa rumus aljabar rumit.
"""

from manim import *
import numpy as np


class RiemannDifferenceTelescopingScene(Scene):
    def construct(self):
        # =============================================================
        # BABAK 1: Dilema Sokratik & Penjepitan Daerah Luas
        # =============================================================
        judul = Text(
            "Mengapa Selisih Poligon Luar dan Poligon Dalam Menuju Nol Saat n -> inf?",
            font_size=21,
            color=WHITE,
            weight=BOLD
        ).to_edge(UP, buff=0.25)

        self.play(Write(judul), run_time=1.2)
        self.wait(0.3)

        # Sumbu koordinat
        axes = Axes(
            x_range=[0, 2.7, 0.5],
            y_range=[0, 4.6, 1.0],
            x_length=6.0,
            y_length=4.4,
            axis_config={"color": GRAY_C, "stroke_width": 1.6},
            x_axis_config={"decimal_number_config": {"num_decimal_places": 1}},
            y_axis_config={"decimal_number_config": {"num_decimal_places": 0}},
        ).add_coordinates(font_size=15)
        axes.shift(LEFT * 3.3 + DOWN * 0.55)

        axis_labels = axes.get_axis_labels(
            x_label=MathTex("x", font_size=19, color=GRAY_B),
            y_label=MathTex("y", font_size=19, color=GRAY_B)
        )

        func = lambda x: x ** 2
        curve = axes.plot(func, x_range=[0, 2.06], color=YELLOW, stroke_width=3.4)
        curve_lbl = MathTex(r"y = x^2", font_size=20, color=YELLOW).next_to(
            axes.c2p(1.45, 2.1), UP + LEFT, buff=0.1
        )

        bound_line = axes.get_vertical_line(axes.c2p(2.0, 4.0), color=GRAY_B, stroke_width=1.5)
        target_area = axes.get_area(curve, x_range=[0.0, 2.0], color=BLUE_E, opacity=0.30)
        region_lbl = MathTex(r"R", font_size=26, color=BLUE_B).move_to(axes.c2p(1.35, 0.75))

        self.play(Create(axes), FadeIn(axis_labels), run_time=0.9)
        self.play(
            Create(curve),
            Write(curve_lbl),
            Create(bound_line),
            FadeIn(target_area),
            FadeIn(region_lbl),
            run_time=1.1
        )
        self.wait(0.4)

        # Fungsi pembuat poligon
        def make_inner_outer(n_slices):
            dx = 2.0 / n_slices
            sw = 1.2 if n_slices <= 8 else (0.7 if n_slices <= 16 else 0.25)
            outer_rects = axes.get_riemann_rectangles(
                curve,
                x_range=[0.0, 2.0],
                dx=dx,
                input_sample_type="right",
                stroke_width=sw,
                stroke_color=MAROON_B,
                fill_opacity=0.32,
                color=(MAROON_C, GOLD_C)
            )
            inner_rects = axes.get_riemann_rectangles(
                curve,
                x_range=[0.0, 2.0],
                dx=dx,
                input_sample_type="left",
                stroke_width=sw,
                stroke_color=TEAL_A,
                fill_opacity=0.60,
                color=(BLUE_D, TEAL_C)
            )
            return inner_rects, outer_rects

        # Fungsi pembuat blok selisih S_n \ R_n
        def make_difference_blocks(n_slices, x_pos=None):
            dx = 2.0 / n_slices
            blocks = VGroup()
            for i in range(1, n_slices + 1):
                x_left = (i - 1) * dx
                x_right = i * dx
                y_bot = func(x_left)
                y_top = func(x_right)

                target_x_left = x_left if x_pos is None else x_pos
                target_x_right = x_right if x_pos is None else (x_pos + dx)

                p1 = axes.c2p(target_x_left, y_bot)
                p2 = axes.c2p(target_x_right, y_bot)
                p3 = axes.c2p(target_x_right, y_top)
                p4 = axes.c2p(target_x_left, y_top)

                sw = 1.0 if n_slices <= 8 else (0.6 if n_slices <= 16 else 0.2)
                poly = Polygon(
                    p1, p2, p3, p4,
                    color=GREEN_A,
                    fill_color=GREEN_D,
                    fill_opacity=0.75,
                    stroke_width=sw
                )
                blocks.add(poly)
            return blocks

        # Tampilkan poligon untuk n = 4
        inner_4, outer_4 = make_inner_outer(4)

        intro_card = VGroup(
            Text("Penjepitan Luas Daerah:", font_size=15, color=GOLD_B, weight=BOLD),
            MathTex(r"R_n \subseteq R \subseteq S_n", font_size=17, color=WHITE),
            MathTex(r"A(R_n) \le A(R) \le A(S_n)", font_size=18, color=YELLOW),
            MathTex(r"\text{Celah Galat: } A(S_n) - A(R_n)", font_size=16, color=GREEN_B),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.10).move_to(RIGHT * 3.35 + UP * 1.85)

        intro_box = SurroundingRectangle(
            intro_card, color=BLUE_D, fill_color="#141B28", fill_opacity=0.92, buff=0.15, corner_radius=0.1
        )

        self.play(
            FadeOut(target_area),
            FadeOut(region_lbl),
            Create(outer_4),
            FadeIn(intro_box),
            Write(intro_card),
            run_time=1.2
        )
        self.play(Create(inner_4), run_time=0.9)
        self.wait(0.5)

        # =============================================================
        # BABAK 2: Eksplorasi Visual & Menara Selisih Teleskopik
        # =============================================================
        subjudul_2 = Text(
            "Celah Galat: Blok Selisih Antara S_n dan R_n",
            font_size=18,
            color=GREEN_B,
            weight=BOLD
        ).next_to(judul, DOWN, buff=0.15)

        diff_blocks_orig = make_difference_blocks(4)
        self.play(
            FadeIn(subjudul_2),
            Create(diff_blocks_orig),
            run_time=1.1
        )
        self.wait(0.5)

        # Geser blok-blok selisih secara horizontal ke x = 2.15
        x_tower = 2.15
        diff_blocks_tower = make_difference_blocks(4, x_pos=x_tower)

        keterangan_geser = Text(
            "Geser setiap blok selisih secara horizontal ke samping...",
            font_size=15,
            color=GOLD_A,
            slant=ITALIC
        ).move_to(RIGHT * 3.35 + UP * 0.45)

        self.play(Write(keterangan_geser), run_time=0.8)

        # Animasi geser horizontal blok
        self.play(
            ReplacementTransform(diff_blocks_orig, diff_blocks_tower),
            run_time=1.6,
            rate_func=smooth
        )
        self.wait(0.4)

        # Beri label dan kurung kurawal pada Menara Selisih
        brace_h = Brace(diff_blocks_tower, direction=RIGHT, buff=0.1, color=YELLOW)
        brace_h_lbl = MathTex(
            r"\text{Tinggi} = f(2)-f(0) = 4",
            font_size=15,
            color=YELLOW
        ).next_to(brace_h, RIGHT, buff=0.1)

        brace_w = Brace(diff_blocks_tower, direction=DOWN, buff=0.1, color=GREEN_B)
        brace_w_lbl = MathTex(
            r"\text{Lebar} = \Delta x = \frac{2}{n}",
            font_size=15,
            color=GREEN_B
        ).next_to(brace_w, DOWN, buff=0.1)

        menara_lbl = Text("Menara Selisih Teleskopik", font_size=15, color=GREEN_A, weight=BOLD).next_to(
            diff_blocks_tower, UP, buff=0.2
        )

        self.play(
            Create(brace_h),
            Write(brace_h_lbl),
            Create(brace_w),
            Write(brace_w_lbl),
            Write(menara_lbl),
            run_time=1.2
        )
        self.wait(0.6)

        # Kartu perhitungan geometri menara
        def calc_areas(n_val):
            dx = 2.0 / n_val
            r_val = (8.0 / 3.0) - (4.0 / n_val) + (4.0 / (3.0 * (n_val ** 2)))
            s_val = (8.0 / 3.0) + (4.0 / n_val) + (4.0 / (3.0 * (n_val ** 2)))
            gap = s_val - r_val
            return r_val, s_val, gap, dx

        def make_telemetry_card(n_val):
            r_val, s_val, gap, dx = calc_areas(n_val)
            card = VGroup(
                MathTex(rf"n = {n_val} \quad (\Delta x = \frac{{2}}{{{n_val}}} = {dx:.3f})", font_size=16, color=YELLOW),
                MathTex(rf"A(R_{{{n_val}}}) = {r_val:.3f} \;\le\; A(R) \;\le\; A(S_{{{n_val}}}) = {s_val:.3f}", font_size=16, color=WHITE),
                MathTex(rf"\mathbf{{\text{{Luas Menara}} = 4 \cdot \Delta x = \frac{{8}}{{{n_val}}} = {gap:.3f}}}", font_size=16, color=GREEN_B),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.10).move_to(RIGHT * 3.35 + DOWN * 1.55)
            box = SurroundingRectangle(
                card, color=TEAL_C, fill_color="#141B28", fill_opacity=0.95, buff=0.15, corner_radius=0.1
            )
            return VGroup(box, card)

        telemetry = make_telemetry_card(4)
        self.play(
            FadeOut(keterangan_geser),
            FadeIn(telemetry),
            run_time=0.9
        )
        self.wait(0.6)

        # =============================================================
        # BABAK 3: Pertanyaan Sokratik & Penyusutan Menara saat n -> inf
        # =============================================================
        pertanyaan_sokratik = Text(
            "Apa yang terjadi pada menara selisih ini saat n -> tak hingga?",
            font_size=18,
            color=TEAL_A,
            weight=BOLD
        ).to_edge(UP, buff=0.25)

        self.play(
            Transform(judul, pertanyaan_sokratik),
            FadeOut(subjudul_2),
            run_time=1.0
        )
        self.wait(1.8)  # Jeda refleksi Sokratik

        # Evolusi n = 8, 16, 32
        for n_val in [8, 16, 32]:
            new_in, new_out = make_inner_outer(n_val)
            new_tower = make_difference_blocks(n_val, x_pos=x_tower)
            new_tel = make_telemetry_card(n_val)

            new_brace_w = Brace(new_tower, direction=DOWN, buff=0.1, color=GREEN_B)
            new_brace_w_lbl = MathTex(
                rf"\Delta x = \frac{{2}}{{{n_val}}}",
                font_size=15,
                color=GREEN_B
            ).next_to(new_brace_w, DOWN, buff=0.1)

            self.play(
                Transform(outer_4, new_out),
                Transform(inner_4, new_in),
                Transform(diff_blocks_tower, new_tower),
                Transform(telemetry, new_tel),
                Transform(brace_w, new_brace_w),
                Transform(brace_w_lbl, new_brace_w_lbl),
                run_time=1.1,
                rate_func=smooth
            )
            self.wait(0.35)

        # Evolusi ke n = 64
        new_in_64, new_out_64 = make_inner_outer(64)
        new_tower_64 = make_difference_blocks(64, x_pos=x_tower)
        new_tel_64 = make_telemetry_card(64)
        new_brace_w_64 = Brace(new_tower_64, direction=DOWN, buff=0.1, color=GREEN_B)
        new_brace_w_lbl_64 = MathTex(
            r"\Delta x = \frac{2}{64} \to 0",
            font_size=15,
            color=GREEN_B
        ).next_to(new_brace_w_64, DOWN, buff=0.1)

        self.play(
            Transform(outer_4, new_out_64),
            Transform(inner_4, new_in_64),
            Transform(diff_blocks_tower, new_tower_64),
            Transform(telemetry, new_tel_64),
            Transform(brace_w, new_brace_w_64),
            Transform(brace_w_lbl, new_brace_w_lbl_64),
            run_time=1.3,
            rate_func=smooth
        )
        self.wait(0.6)

        # =============================================================
        # BABAK 4: Kristalisasi Formal & Teorema Apit
        # =============================================================
        judul_kristal = Text(
            "Kristalisasi Formal: Deret Teleskopik & Teorema Apit",
            font_size=19,
            color=GOLD_B,
            weight=BOLD
        ).to_edge(UP, buff=0.25)

        kristal_card = VGroup(
            MathTex(
                r"A(S_n) - A(R_n) = \sum_{i=1}^{n} [f(x_i) - f(x_{i-1})]\,\Delta x",
                font_size=16,
                color=WHITE
            ),
            MathTex(
                r"= \Delta x \cdot \underbrace{\sum_{i=1}^{n} [f(x_i) - f(x_{i-1})]}_{\text{Jumlah Teleskopik}} = \Delta x \cdot [f(2) - f(0)]",
                font_size=15,
                color=GREEN_B
            ),
            MathTex(
                r"= \frac{2}{n} \cdot (4 - 0) = \frac{8}{n} \;\xrightarrow{n\to\infty}\; 0",
                font_size=16,
                color=YELLOW
            ),
            MathTex(
                r"\implies \lim_{n\to\infty} A(R_n) = \lim_{n\to\infty} A(S_n) = A(R) = \frac{8}{3}",
                font_size=17,
                color=GOLD_B
            ),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.10).move_to(RIGHT * 3.35 + DOWN * 0.45)

        kristal_box = SurroundingRectangle(
            kristal_card, color=GOLD_B, fill_color="#101522", fill_opacity=0.96, buff=0.15, corner_radius=0.1
        )

        exact_curve_area = axes.get_area(curve, x_range=[0.0, 2.0], color=(BLUE_D, TEAL_C), opacity=0.75)
        exact_badge = MathTex(r"A(R) = \frac{8}{3}", font_size=22, color=YELLOW).move_to(
            axes.c2p(1.3, 0.75)
        )
        exact_badge_bg = BackgroundRectangle(exact_badge, fill_color="#0C1018", fill_opacity=0.85, buff=0.08)

        self.play(
            Transform(judul, judul_kristal),
            FadeOut(intro_box),
            FadeOut(intro_card),
            FadeOut(telemetry),
            FadeIn(kristal_box),
            Write(kristal_card),
            FadeOut(outer_4),
            ReplacementTransform(inner_4, exact_curve_area),
            FadeIn(exact_badge_bg),
            Write(exact_badge),
            run_time=1.8
        )
        self.wait(2.5)
