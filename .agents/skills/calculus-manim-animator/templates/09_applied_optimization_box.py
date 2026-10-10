"""
Template: Masalah Pengoptimuman Terapan - Kotak Karton (MA1101)
Subtopik: 3.1 & 3.4 Maksimum/Minimum dan Pemodelan Matematika
Bahasa: Indonesia
Gaya: Grant Sanderson (3Blue1Brown) & Metode Sokratik
"""

from manim import *

class BoxOptimizationScene(Scene):
    def construct(self):
        # -------------------------------------------------------------
        # AKSI 1: Tantangan Sokratik (The Pique)
        # -------------------------------------------------------------
        judul = Text(
            "Berapa ukuran potongan sudut x\nagar volume kotak yang dilipat maksimum?",
            font_size=26,
            line_spacing=1.2
        ).to_edge(UP, buff=0.4)
        
        self.play(Write(judul))
        self.wait(1.5)

        # Karton persegi ukuran 6 x 6 dm
        # Ditampilkan di sebelah kiri: x in [-6, -1], y in [-2, 3]
        karton = Square(side_length=3.6, color=YELLOW, fill_color=YELLOW_E, fill_opacity=0.3)
        karton.shift(LEFT * 3.6 + DOWN * 0.4)
        label_karton = Text("Karton 6 x 6", font_size=20, color=YELLOW).next_to(karton, DOWN, buff=0.2)

        self.play(Create(karton), FadeIn(label_karton))
        self.wait(1)

        # Di sebelah kanan: Grafik Volume V(x) = x * (6 - 2x)^2
        # x in (0, 3), max di x = 1 (V = 16)
        axes = Axes(
            x_range=[0, 3.2, 1],
            y_range=[0, 18, 5],
            x_length=5.0,
            y_length=4.2,
            axis_config={"color": GRAY_C}
        ).add_coordinates()
        axes.shift(RIGHT * 3.2 + DOWN * 0.4)

        V_fn = lambda x: x * (6 - 2*x)**2
        V_curve = axes.plot(V_fn, x_range=[0, 3], color=TEAL_C, stroke_width=3)
        V_label = MathTex(r"V(x) = x(6 - 2x)^2", color=TEAL_C, font_size=24).next_to(axes.c2p(1.5, 17), UP)

        self.play(Create(axes), Create(V_curve), FadeIn(V_label), run_time=2)
        self.wait(1)

        # -------------------------------------------------------------
        # AKSI 2: Eksplorasi Visual (Mengubah Ukuran Potongan x)
        # -------------------------------------------------------------
        x_tracker = ValueTracker(0.2)

        # Visual titik pada kurva volume
        dot_V = always_redraw(lambda:
            Dot(axes.c2p(x_tracker.get_value(), V_fn(x_tracker.get_value())), color=RED_C, radius=0.08)
        )
        line_drop_V = always_redraw(lambda:
            axes.get_vertical_line(axes.c2p(x_tracker.get_value(), V_fn(x_tracker.get_value())), color=RED_C).set_stroke(width=1.5, opacity=0.7)
        )

        label_x_val = always_redraw(lambda:
            MathTex(
                rf"x = {x_tracker.get_value():.2f}",
                rf"\implies V = {V_fn(x_tracker.get_value()):.1f}",
                font_size=24
            ).next_to(karton, UP, buff=0.2)
        )

        self.play(FadeIn(dot_V), Create(line_drop_V), Write(label_x_val))
        self.wait(1)

        # -------------------------------------------------------------
        # AKSI 3: Pertanyaan Sokratik (Mencari Titik Puncak)
        # -------------------------------------------------------------
        pertanyaan = Text(
            "Perhatikan kemiringan kurva V(x):\ndi manakah laju perubahan volume tepat bernilai nol?",
            font_size=24,
            color=TEAL_A,
            line_spacing=1.2
        ).to_edge(UP, buff=0.4)

        self.play(Transform(judul, pertanyaan))
        self.wait(1.5)

        # Animate x tracker smoothly through the peak (x = 1.0) and down towards 2.8
        self.play(x_tracker.animate.set_value(1.0), run_time=3, rate_func=smooth)
        self.wait(1.5)
        self.play(x_tracker.animate.set_value(2.6), run_time=3, rate_func=smooth)
        self.wait(1)
        self.play(x_tracker.animate.set_value(1.0), run_time=2, rate_func=smooth)
        self.wait(1)

        # -------------------------------------------------------------
        # AKSI 4: Kristalisasi Matematis Formal (Titik Kritis)
        # -------------------------------------------------------------
        garis_puncak = Line(
            axes.c2p(0.3, 16),
            axes.c2p(1.7, 16),
            color=YELLOW,
            stroke_width=2.5
        )
        label_tangent_nol = MathTex(r"V'(x) = 0", color=YELLOW, font_size=24).next_to(axes.c2p(1.0, 16), UR)

        kristalisasi = MathTex(
            r"V(x) &= 36x - 24x^2 + 4x^3 \\",
            r"V'(x) &= 36 - 48x + 12x^2 = 0 \\",
            r"12(x - 1)(x - 3) &= 0 \implies x = 1\text{ (Maksimum!)}",
            font_size=22
        ).to_corner(UR, buff=0.5)
        kristalisasi[1].set_color(YELLOW)
        kristalisasi[2].set_color(GREEN_C)

        box = SurroundingRectangle(kristalisasi, color=BLUE_B, buff=0.15)

        self.play(Create(garis_puncak), Write(label_tangent_nol), Write(kristalisasi), Create(box))
        self.wait(2.5)
