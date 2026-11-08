"""
Template: Integral Tentu, Jumlah Riemann & Luas Bertanda (MA1101 Subtopik 4.2)
Subtopik: 4.2 Integral Tentu (The Definite Integral — Riemann Sums & Signed Area)
Bahasa: Indonesia
Gaya: Grant Sanderson (3Blue1Brown) & Metode Sokratik
Deskripsi:
  Visualisasi 4 babak mengenai Jumlah Riemann dan Integral Tentu pada fungsi
  f(x) = x^2 - 1 di selang [0, 2] yang memotong sumbu-x di x = 1.
  Memperlihatkan bagaimana persegi panjang di bawah sumbu-x (f(x_i) < 0) memberi
  kontribusi negatif (-A_bawah) dan di atas sumbu-x (f(x_i) > 0) memberi kontribusi
  positif (+A_atas), penghalusan partisi saat ||P|| -> 0 (n = 4 -> 8 -> 16 -> 32 -> 64),
  serta kristalisasi formal menuju nilai eksak A_atas - A_bawah = 4/3 - 2/3 = +2/3.
"""

from manim import *
import numpy as np


class DefiniteIntegralSignedAreaScene(Scene):
    def construct(self):
        # -------------------------------------------------------------
        # AKSI 1: Tantangan Sokratik (Kurva Menyelam di Bawah Sumbu-x)
        # -------------------------------------------------------------
        judul = Text(
            "Apa arti Jumlah Riemann jika sebagian kurva f(x)\nberada di BAWAH sumbu-x (bernilai negatif)?",
            font_size=22,
            line_spacing=1.2,
            color=WHITE
        ).to_edge(UP, buff=0.28)

        self.play(Write(judul), run_time=1.3)
        self.wait(0.4)

        axes = Axes(
            x_range=[0, 2.35, 0.5],
            y_range=[-1.4, 3.4, 1.0],
            x_length=6.5,
            y_length=4.6,
            axis_config={"color": GRAY_C, "stroke_width": 1.6},
            x_axis_config={"decimal_number_config": {"num_decimal_places": 1}},
            y_axis_config={"decimal_number_config": {"num_decimal_places": 0}},
        ).add_coordinates(font_size=16)
        axes.shift(LEFT * 2.5 + DOWN * 0.48)

        axis_labels = axes.get_axis_labels(
            x_label=MathTex("x", font_size=20, color=GRAY_B),
            y_label=MathTex("y", font_size=20, color=GRAY_B)
        )

        func = lambda x: (x ** 2) - 1.0
        curve = axes.plot(func, x_range=[0.0, 2.08], color=YELLOW, stroke_width=3.6)
        curve_lbl = MathTex(r"f(x) = x^2 - 1", font_size=21, color=YELLOW).next_to(
            axes.c2p(1.62, 1.62), UP + LEFT, buff=0.12
        )

        bound_line = axes.get_vertical_line(axes.c2p(2.0, 3.0), color=GRAY_B, stroke_width=1.6)
        root_dot = Dot(axes.c2p(1.0, 0.0), color=WHITE, radius=0.065)

        self.play(Create(axes), FadeIn(axis_labels), run_time=0.9)
        self.play(
            Create(curve),
            Write(curve_lbl),
            Create(bound_line),
            FadeIn(root_dot),
            run_time=1.2
        )
        self.wait(0.4)

        # Helper pembuat persegi panjang Jumlah Riemann (titik tengah) dengan warna bertanda
        def make_signed_riemann(n_slices):
            dx = 2.0 / n_slices
            sw = 1.4 if n_slices <= 8 else (0.8 if n_slices <= 16 else (0.35 if n_slices <= 32 else 0.15))
            rects = VGroup()
            pos_sum = 0.0
            neg_sum = 0.0
            for i in range(n_slices):
                x_left = i * dx
                x_right = (i + 1) * dx
                x_mid = 0.5 * (x_left + x_right)
                y_val = func(x_mid)
                area_i = y_val * dx
                if y_val >= 0:
                    pos_sum += area_i
                    col = TEAL_C
                    scol = TEAL_A
                else:
                    neg_sum += area_i
                    col = MAROON_B
                    scol = MAROON_A

                p1 = axes.c2p(x_left, 0)
                p2 = axes.c2p(x_right, 0)
                p3 = axes.c2p(x_right, y_val)
                p4 = axes.c2p(x_left, y_val)
                rect = Polygon(
                    p1, p2, p3, p4,
                    fill_color=col,
                    fill_opacity=0.55,
                    stroke_color=scol,
                    stroke_width=sw
                )
                rects.add(rect)
            return rects, pos_sum, neg_sum

        rects_4, pos_4, neg_4 = make_signed_riemann(4)

        sign_minus = MathTex(r"-", font_size=30, color=MAROON_A).move_to(axes.c2p(0.42, -0.45))
        sign_plus = MathTex(r"+", font_size=30, color=TEAL_A).move_to(axes.c2p(1.62, 0.72))

        info_card = VGroup(
            Text("Jumlah Riemann (Luas Bertanda):", font_size=15, color=GOLD_B),
            MathTex(r"R_P = \sum_{i=1}^{n} f(\bar{x}_i)\,\Delta x_i", font_size=19, color=WHITE),
            MathTex(r"\bullet\; f(\bar{x}_i) > 0 \implies +(\text{Luas di Atas})", font_size=16, color=TEAL_B),
            MathTex(r"\bullet\; f(\bar{x}_i) < 0 \implies -(\text{Luas di Bawah})", font_size=16, color=MAROON_B),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.10).move_to(RIGHT * 3.35 + UP * 1.55)

        info_box = SurroundingRectangle(
            info_card, color=BLUE_D, fill_color="#141B28", fill_opacity=0.92, buff=0.16, corner_radius=0.1
        )

        self.play(
            Create(rects_4),
            FadeIn(sign_minus),
            FadeIn(sign_plus),
            FadeIn(info_box),
            Write(info_card),
            run_time=1.5
        )
        self.wait(0.6)

        # -------------------------------------------------------------
        # AKSI 2: Eksplorasi Visual (Penghalusan Partisi & Telemetri R_P)
        # -------------------------------------------------------------
        def make_telemetry(n_val, pos_v, neg_v):
            net_v = pos_v + neg_v
            dx_val = 2.0 / n_val
            grp = VGroup(
                MathTex(rf"n = {n_val} \;\;\; (\|P\| = \Delta x = {dx_val:.3f})", font_size=17, color=YELLOW),
                MathTex(rf"\text{{Suku Positif }} (+) = +{pos_v:.3f}, \;\;\; \text{{Negatif }} (-) = {neg_v:.3f}", font_size=16, color=WHITE),
                MathTex(rf"\text{{Total }} R_P = {pos_v:.3f} - {abs(neg_v):.3f} = {net_v:+.3f}", font_size=18, color=GREEN_B),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.10).move_to(RIGHT * 3.35 + DOWN * 0.22)
            box = SurroundingRectangle(
                grp, color=TEAL_C, fill_color="#141B28", fill_opacity=0.92, buff=0.15, corner_radius=0.1
            )
            return VGroup(box, grp)

        telemetry = make_telemetry(4, pos_4, neg_4)
        self.play(FadeIn(telemetry), run_time=0.8)
        self.wait(0.6)

        for n_step, rt in [(8, 1.1), (16, 1.1), (32, 1.1)]:
            new_rects, p_v, n_v = make_signed_riemann(n_step)
            new_tel = make_telemetry(n_step, p_v, n_v)
            self.play(
                Transform(rects_4, new_rects),
                Transform(telemetry, new_tel),
                run_time=rt,
                rate_func=smooth
            )
            self.wait(0.35)

        # -------------------------------------------------------------
        # AKSI 3: Pertanyaan Sokratik (Konvergensi Saat ||P|| -> 0)
        # -------------------------------------------------------------
        pertanyaan = Text(
            "Saat lebar partisi ||P|| menuju 0, bagaimana hubungan antara\nnilai Integral Tentu dengan luas di atas dan di bawah sumbu-x?",
            font_size=20,
            color=TEAL_A,
            line_spacing=1.2
        ).to_edge(UP, buff=0.28)

        self.play(Transform(judul, pertanyaan), run_time=1.0)
        self.wait(1.6)

        rects_64, p_64, n_64 = make_signed_riemann(64)
        tel_64 = make_telemetry(64, p_64, n_64)
        self.play(
            Transform(rects_4, rects_64),
            Transform(telemetry, tel_64),
            run_time=1.2,
            rate_func=smooth
        )
        self.wait(0.4)

        area_neg = axes.get_area(curve, x_range=[0.0, 1.0], color=MAROON_B, opacity=0.65)
        area_pos = axes.get_area(curve, x_range=[1.0, 2.0], color=TEAL_C, opacity=0.65)
        continuous_regions = VGroup(area_neg, area_pos)

        lbl_bawah = MathTex(r"-A_{\text{bawah}} = -\frac{2}{3}", font_size=18, color=MAROON_A).move_to(
            axes.c2p(0.52, -1.18)
        )
        lbl_atas = MathTex(r"+A_{\text{atas}} = +\frac{4}{3}", font_size=19, color=TEAL_A).move_to(
            axes.c2p(1.52, 0.58)
        )
        lbl_atas_bg = BackgroundRectangle(lbl_atas, fill_color="#0C1018", fill_opacity=0.82, buff=0.07)

        self.play(
            FadeOut(sign_minus),
            FadeOut(sign_plus),
            ReplacementTransform(rects_4, continuous_regions),
            Write(lbl_bawah),
            FadeIn(lbl_atas_bg),
            Write(lbl_atas),
            run_time=1.4
        )
        self.wait(0.6)

        # -------------------------------------------------------------
        # AKSI 4: Kristalisasi Formal (Definisi Integral Tentu Riemann)
        # -------------------------------------------------------------
        judul_kristal = Text(
            "Definisi Integral Tentu: Limit Jumlah Riemann & Luas Bertanda",
            font_size=21,
            color=GOLD_B
        ).to_edge(UP, buff=0.28)

        kristal_card = VGroup(
            MathTex(
                r"\int_{a}^{b} f(x)\,dx = \lim_{\|P\|\to 0} \sum_{i=1}^{n} f(\bar{x}_i)\,\Delta x_i = A_{\text{atas}} - A_{\text{bawah}}",
                font_size=17,
                color=WHITE
            ),
            MathTex(
                r"\int_{0}^{2} (x^2 - 1)\,dx = \lim_{n\to\infty} \left(\frac{8}{n^3}\sum_{i=1}^{n} i^2 - \frac{2}{n}\sum_{i=1}^{n} 1\right)",
                font_size=17,
                color=TEAL_B
            ),
            MathTex(
                r"= \frac{8}{3} - 2 = \frac{4}{3} - \frac{2}{3} = +\frac{2}{3} \approx 0.667",
                font_size=19,
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
