"""
Template: Antiturunan & Keluarga Kurva F(x) + C (MA1101 Subtopik 3.8)
Subtopik: 3.8 Antiturunan (Antiderivatives & Indefinite Integrals)
Bahasa: Indonesia
Gaya: Grant Sanderson (3Blue1Brown) & Metode Sokratik
Deskripsi:
  Visualisasi 4 babak mengenai masalah kebalikan turunan: merekonstruksi
  keluarga kurva antiturunan F(x) + C dari medan kemiringan f(x), melihat
  kesejajaran garis singgung pada absis x yang sama, memilih satu kurva
  spesifik melalui titik awal P(x0, y0), serta kristalisasi notasi
  integral tak tentu Leibniz.
"""

from manim import *
import numpy as np


class AntiderivativeFamilyScene(Scene):
    def construct(self):
        # -------------------------------------------------------------
        # AKSI 1: Tantangan Sokratik (The Pique) & Medan Kemiringan
        # -------------------------------------------------------------
        judul = Text(
            "Jika kita hanya tahu kemiringan f(x) di setiap titik,\ndapatkah kita merekonstruksi kurva asalnya F(x)?",
            font_size=22,
            line_spacing=1.2,
            color=WHITE
        ).to_edge(UP, buff=0.3)

        self.play(Write(judul), run_time=1.3)
        self.wait(0.4)

        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-4, 4, 1],
            x_length=7.4,
            y_length=4.7,
            axis_config={"color": GRAY_C, "stroke_width": 1.5}
        ).add_coordinates(font_size=16)
        axes.shift(LEFT * 2.1 + DOWN * 0.45)

        axis_labels = axes.get_axis_labels(
            x_label=MathTex("x", font_size=20, color=GRAY_B),
            y_label=MathTex("y", font_size=20, color=GRAY_B)
        )

        # Fungsi turunan f(x) = 3/4 x^2 - 3/2 dan antiturunan dasar F0(x) = 1/4 x^3 - 3/2 x
        f_deriv = lambda x: 0.75 * (x ** 2) - 1.5
        F_base = lambda x: 0.25 * (x ** 3) - 1.5 * x

        # Medan elemen garis singgung (slope field)
        slope_segments = VGroup()
        for xv in np.linspace(-2.6, 2.6, 11):
            for yv in np.linspace(-3.2, 3.2, 9):
                m = f_deriv(xv)
                dx = 0.22 / np.sqrt(1 + m ** 2)
                dy = m * dx
                seg = Line(
                    axes.c2p(xv - dx, yv - dy),
                    axes.c2p(xv + dx, yv + dy),
                    color=BLUE_D,
                    stroke_width=1.6,
                    stroke_opacity=0.55
                )
                slope_segments.add(seg)

        info_panel_pos = RIGHT * 3.55 + UP * 1.35
        diketahui_card = VGroup(
            Text("Informasi Kemiringan:", font_size=16, color=BLUE_B),
            MathTex(r"F'(x) = f(x) = \frac{3}{4}x^2 - \frac{3}{2}", font_size=22, color=BLUE_C)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.14).move_to(info_panel_pos)
        diketahui_box = SurroundingRectangle(
            diketahui_card, color=BLUE_D, fill_color= "#141B28", fill_opacity=0.9, buff=0.18, corner_radius=0.1
        )

        self.play(Create(axes), FadeIn(axis_labels), run_time=1.0)
        self.play(
            LaggedStart(*[Create(s) for s in slope_segments], lag_ratio=0.01),
            FadeIn(diketahui_box),
            Write(diketahui_card),
            run_time=1.6
        )
        self.wait(0.6)

        # -------------------------------------------------------------
        # AKSI 2: Eksplorasi Visual (Translasi Vertikal Keluarga F(x) + C)
        # -------------------------------------------------------------
        c_tracker = ValueTracker(0.0)

        active_curve = always_redraw(lambda:
            axes.plot(
                lambda x: F_base(x) + c_tracker.get_value(),
                x_range=[-2.65, 2.65],
                color=YELLOW,
                stroke_width=3.8
            )
        )

        # Titik uji kemiringan pada x0 = -1.0 (di mana f(-1) = -0.75)
        x0 = -1.0
        m0 = f_deriv(x0)

        active_tangent = always_redraw(lambda:
            Line(
                axes.c2p(x0 - 0.75, F_base(x0) + c_tracker.get_value() - 0.75 * m0),
                axes.c2p(x0 + 0.75, F_base(x0) + c_tracker.get_value() + 0.75 * m0),
                color=RED_C,
                stroke_width=3.0
            )
        )
        active_dot = always_redraw(lambda:
            Dot(axes.c2p(x0, F_base(x0) + c_tracker.get_value()), color=RED_C, radius=0.07)
        )

        c_readout = always_redraw(lambda:
            MathTex(
                r"F(x) = \frac{1}{4}x^3 - \frac{3}{2}x",
                f"{c_tracker.get_value():+.1f}",
                font_size=22,
                color=YELLOW
            ).next_to(diketahui_box, DOWN, buff=0.28)
        )

        self.play(Create(active_curve), FadeIn(active_dot), Create(active_tangent), Write(c_readout), run_time=1.2)
        self.wait(0.4)

        # Jejak keluarga kurva untuk C = -2, -1, 0, 1, 2
        c_values = [-2.0, -1.0, 0.0, 1.0, 2.0]
        family_colors = [TEAL_D, TEAL_C, GREEN_C, MAROON_B, GOLD_B]
        family_curves = VGroup()
        family_tangents = VGroup()

        vert_guide = DashedLine(
            axes.c2p(x0, -3.7),
            axes.c2p(x0, 3.65),
            color=RED_B,
            stroke_width=1.4,
            stroke_opacity=0.6
        )
        m_badge = MathTex(
            r"m = f(-1) = -\frac{3}{4}",
            font_size=17,
            color=RED_B
        ).next_to(vert_guide, UP, buff=0.08)
        lbl_parallel = Text(
            "Pada x yang sama,\ngaris singgung sejajar!",
            font_size=14,
            color=RED_B,
            line_spacing=1.15
        ).next_to(c_readout, DOWN, buff=0.22)

        self.play(Create(vert_guide), FadeIn(m_badge), FadeIn(lbl_parallel), run_time=0.8)

        for c_val, col in zip(c_values, family_colors):
            self.play(c_tracker.animate.set_value(c_val), run_time=0.75, rate_func=smooth)
            ghost_c = axes.plot(
                lambda x, c=c_val: F_base(x) + c,
                x_range=[-2.65, 2.65],
                color=col,
                stroke_width=2.0,
                stroke_opacity=0.65
            )
            ghost_t = Line(
                axes.c2p(x0 - 0.5, F_base(x0) + c_val - 0.5 * m0),
                axes.c2p(x0 + 0.5, F_base(x0) + c_val + 0.5 * m0),
                color=RED_C,
                stroke_width=2.0,
                stroke_opacity=0.55
            )
            family_curves.add(ghost_c)
            family_tangents.add(ghost_t)
            self.add(ghost_c, ghost_t)

        self.wait(0.5)

        # -------------------------------------------------------------
        # AKSI 3: Pertanyaan Sokratik (Mengunci 1 Kurva via Titik Awal)
        # -------------------------------------------------------------
        pertanyaan = Text(
            "Mengapa ada tak hingga kurva antiturunan,\ndan bagaimana memilih tepat satu kurva?",
            font_size=21,
            color=TEAL_A,
            line_spacing=1.2
        ).to_edge(UP, buff=0.3)

        self.play(Transform(judul, pertanyaan), run_time=1.0)
        self.wait(1.6)

        # Syarat titik awal P(2, 1) -> F0(2) = 0.25(8) - 3 = -1 => -1 + C = 1 => C = 2
        xp, yp = 2.0, 1.0
        pt_p = Dot(axes.c2p(xp, yp), color=GREEN_B, radius=0.09)
        ring_p = Circle(radius=0.18, color=GREEN_B, stroke_width=2.5).move_to(axes.c2p(xp, yp))
        lbl_p = MathTex(r"P(2, 1)", color=GREEN_B, font_size=19).next_to(ring_p, UP, buff=0.08).shift(LEFT * 0.15)

        syarat_awal_text = MathTex(
            r"\text{Syarat Awal: } F(2) = 1 \implies C = 2",
            font_size=19,
            color=GREEN_B
        ).next_to(lbl_parallel, DOWN, buff=0.25)

        self.play(
            c_tracker.animate.set_value(-1.5),
            FadeIn(pt_p),
            Create(ring_p),
            Write(lbl_p),
            run_time=0.9
        )
        self.play(
            c_tracker.animate.set_value(2.0),
            Indicate(ring_p, color=YELLOW, scale_factor=1.3),
            Write(syarat_awal_text),
            run_time=1.6,
            rate_func=smooth
        )
        self.wait(0.8)

        # -------------------------------------------------------------
        # AKSI 4: Kristalisasi Formal (Notasi Integral Tak Tentu Leibniz)
        # -------------------------------------------------------------
        judul_kristal = Text(
            "Antiturunan Umum & Integral Tak Tentu (Notasi Leibniz)",
            font_size=21,
            color=GOLD_B
        ).to_edge(UP, buff=0.3)

        rumus_leibniz = MathTex(
            r"\int",
            r"f(x)\,dx",
            r"=",
            r"F(x)",
            r"+",
            r"C",
            font_size=28
        )
        rumus_leibniz[0].set_color(GOLD_B)
        rumus_leibniz[1].set_color(BLUE_C)
        rumus_leibniz[3].set_color(YELLOW)
        rumus_leibniz[5].set_color(GREEN_B)

        syarat_equiv = MathTex(
            r"\Longleftrightarrow \quad F'(x) = f(x) \text{ pada selang } I",
            font_size=19,
            color=GRAY_A
        )

        kristal_group = VGroup(rumus_leibniz, syarat_equiv).arrange(DOWN, buff=0.15)
        kristal_group.move_to(RIGHT * 3.55 + DOWN * 2.15)
        kristal_box = SurroundingRectangle(
            kristal_group, color=GOLD_B, fill_color="#141B28", fill_opacity=0.95, buff=0.18, corner_radius=0.1
        )

        self.play(
            Transform(judul, judul_kristal),
            FadeOut(lbl_parallel),
            FadeIn(kristal_box),
            Write(rumus_leibniz),
            Write(syarat_equiv),
            run_time=1.5
        )
        self.wait(2.5)
