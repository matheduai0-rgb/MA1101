"""
Template: Kecekungan dan Titik Belok (MA1101)
Subtopik: 3.2 & 3.3 Kemonotonan, Kecekungan, dan Titik Belok
Bahasa: Indonesia
Gaya: Grant Sanderson (3Blue1Brown) & Metode Sokratik
"""

from manim import *

class ConcavityInflectionScene(Scene):
    def construct(self):
        # -------------------------------------------------------------
        # AKSI 1: Tantangan Sokratik (The Pique)
        # -------------------------------------------------------------
        judul = Text(
            "Bagaimana membedakan kurva yang 'menampung air'\nversus yang 'menumpahkan air'?",
            font_size=26,
            line_spacing=1.2
        ).to_edge(UP, buff=0.4)
        
        self.play(Write(judul))
        self.wait(1.5)

        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-4, 4, 2],
            x_length=8.5,
            y_length=5,
            axis_config={"color": GRAY_C}
        ).add_coordinates()
        axes.shift(DOWN * 0.4)

        # Kurva f(x) = 0.3 * (x^3 - 3x) memiliki titik belok tepat di x = 0
        f = lambda x: 0.3 * (x**3 - 3*x)
        f_prime = lambda x: 0.3 * (3*x**2 - 3)
        
        curve = axes.plot(f, x_range=[-2.6, 2.6], color=YELLOW, stroke_width=3.5)
        curve_label = MathTex(r"f(x) = \frac{3}{10}(x^3 - 3x)", color=YELLOW, font_size=26)
        curve_label.next_to(axes.c2p(2.2, f(2.2)), UR)

        self.play(Create(axes), Create(curve), FadeIn(curve_label), run_time=2)
        self.wait(1)

        # -------------------------------------------------------------
        # AKSI 2: Eksplorasi Visual (Garis Singgung Menjelajah)
        # -------------------------------------------------------------
        x_tracker = ValueTracker(-2.2)

        # Tangent line length 3.0
        def get_tangent_line():
            xv = x_tracker.get_value()
            yv = f(xv)
            m = f_prime(xv)
            dx_half = 1.0
            p1 = axes.c2p(xv - dx_half, yv - dx_half * m)
            p2 = axes.c2p(xv + dx_half, yv + dx_half * m)
            return Line(p1, p2, color=TEAL_C, stroke_width=3)

        tangent = always_redraw(get_tangent_line)
        tangent_dot = always_redraw(lambda:
            Dot(axes.c2p(x_tracker.get_value(), f(x_tracker.get_value())), color=RED_C, radius=0.08)
        )

        label_kecekungan = always_redraw(lambda:
            Text(
                "Cekung ke Bawah (f'' < 0)" if x_tracker.get_value() < -0.05 else
                ("Titik Belok (f'' = 0)" if abs(x_tracker.get_value()) <= 0.05 else "Cekung ke Atas (f'' > 0)"),
                font_size=22,
                color=RED_C if x_tracker.get_value() < -0.05 else (YELLOW if abs(x_tracker.get_value()) <= 0.05 else GREEN_C)
            ).to_corner(UL, buff=0.6)
        )

        self.play(Create(tangent), FadeIn(tangent_dot), FadeIn(label_kecekungan))
        self.wait(1)

        # -------------------------------------------------------------
        # AKSI 3: Pertanyaan Sokratik (Arah Rotasi Garis Singgung)
        # -------------------------------------------------------------
        pertanyaan = Text(
            "Perhatikan rotasi garis singgung: searah jarum jam,\nlalu berbalik arah. Di manakah titik perbalikannya?",
            font_size=24,
            color=TEAL_A,
            line_spacing=1.2
        ).to_edge(UP, buff=0.4)

        self.play(Transform(judul, pertanyaan))
        self.wait(1.5)

        # Animate tangent across the curve from -2.2 to 2.2
        self.play(x_tracker.animate.set_value(2.2), run_time=6, rate_func=smooth)
        self.wait(1.5)

        # -------------------------------------------------------------
        # AKSI 4: Kristalisasi Matematis Formal (Titik Belok)
        # -------------------------------------------------------------
        pt_belok = Dot(axes.c2p(0, 0), color=PINK, radius=0.1)
        label_belok = Text("Titik Belok (0, 0)", font_size=20, color=PINK).next_to(pt_belok, UR, buff=0.2)

        kristalisasi = MathTex(
            r"f''(x) > 0 &\implies \text{Cekung ke Atas (tangent di bawah kurva)} \\",
            r"f''(x) < 0 &\implies \text{Cekung ke Bawah (tangent di atas kurva)} \\",
            r"f''(c) = 0 &\implies \text{Titik Belok (perubahan kecekungan)}",
            font_size=24
        ).to_corner(UR, buff=0.5)
        kristalisasi[0].set_color(GREEN_C)
        kristalisasi[1].set_color(RED_C)
        kristalisasi[2].set_color(PINK)

        box = SurroundingRectangle(kristalisasi, color=BLUE_B, buff=0.15)

        self.play(FadeIn(pt_belok), Write(label_belok), Write(kristalisasi), Create(box))
        self.wait(2.5)
