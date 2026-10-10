"""
Template: Diferensial dan Hampiran (MA1101)
Subtopik: 2.9 Diferensial dan Hampiran (Differentials and Linear Approximations)
Bahasa: Indonesia
Gaya: Grant Sanderson (3Blue1Brown) & Metode Sokratik
"""

from manim import *
import numpy as np

class DifferentialsApproximationScene(Scene):
    def construct(self):
        # -------------------------------------------------------------
        # AKSI 1: Tantangan Sokratik (The Pique)
        # -------------------------------------------------------------
        judul = Text(
            "Bagaimana cara menghitung √4.08 tanpa kalkulator?",
            font_size=26,
            color=WHITE
        ).to_edge(UP, buff=0.35)

        self.play(Write(judul))
        self.wait(1.5)

        # Sumbu koordinat di sisi kiri
        axes = Axes(
            x_range=[0, 6, 1],
            y_range=[0, 3, 1],
            x_length=5.8,
            y_length=4.8,
            axis_config={"color": GRAY_C, "stroke_width": 2},
            tips=True
        ).add_coordinates()
        axes.shift(LEFT * 3.3 + DOWN * 0.5)

        # Kurva f(x) = sqrt(x)
        curve = axes.plot(
            lambda x: np.sqrt(x),
            x_range=[0.05, 5.4],
            color=YELLOW,
            stroke_width=3.5
        )
        label_curve = MathTex(r"f(x) = \sqrt{x}", color=YELLOW, font_size=20)
        label_curve.next_to(axes.c2p(2.8, np.sqrt(2.8)), DR, buff=0.15)

        # Titik acuan P(4, 2)
        x0 = 4.0
        y0 = 2.0
        pt_P = axes.c2p(x0, y0)
        dot_P = Dot(pt_P, color=BLUE_C, radius=0.08)
        label_P = MathTex(r"P(4, 2)", color=BLUE_C, font_size=20).next_to(dot_P, UL, buff=0.12)

        self.play(Create(axes), Create(curve), Write(label_curve), run_time=1.8)
        self.play(FadeIn(dot_P), Write(label_P))
        self.wait(1)

        # Garis singgung di P(4, 2): f'(4) = 1/(2*sqrt(4)) = 0.25
        # y - 2 = 0.25(x - 4) => y = 0.25x + 1
        m_tan = 0.25
        tangent_fn = lambda x: y0 + m_tan * (x - x0)
        tangent_line = axes.plot(
            tangent_fn,
            x_range=[1.2, 5.4],
            color=TEAL_C,
            stroke_width=3
        )
        label_tan = MathTex(r"\text{Garis Singgung } L(x)", color=TEAL_C, font_size=18)
        label_tan.next_to(axes.c2p(1.8, tangent_fn(1.8)), UL, buff=0.1)

        self.play(Create(tangent_line), Write(label_tan), run_time=1.5)
        self.wait(1.2)

        # -------------------------------------------------------------
        # AKSI 2: Eksplorasi Visual (Geometri: Δy vs dy)
        # -------------------------------------------------------------
        pertanyaan_geo = Text(
            "Geometri Kelinieran Lokal: Perubahan Nyata (Δy) vs Diferensial (dy)",
            font_size=23,
            color=TEAL_A
        ).to_edge(UP, buff=0.35)
        self.play(Transform(judul, pertanyaan_geo))

        # Gunakan ValueTracker untuk delta_x agar dinamis
        # Mulai dari 1.3 agar segitiga diferensial terlihat jelas
        dx_val = ValueTracker(1.3)

        # Titik pada garis singgung & kurva
        pt_Q_curve = always_redraw(lambda: Dot(
            axes.c2p(x0 + dx_val.get_value(), np.sqrt(x0 + dx_val.get_value())),
            color=RED_C,
            radius=0.07
        ))
        pt_R_tan = always_redraw(lambda: Dot(
            axes.c2p(x0 + dx_val.get_value(), tangent_fn(x0 + dx_val.get_value())),
            color=GREEN_C,
            radius=0.07
        ))

        # Garis horizontal dx = Delta x
        dx_line = always_redraw(lambda: Line(
            pt_P,
            axes.c2p(x0 + dx_val.get_value(), y0),
            color=WHITE,
            stroke_width=2.5
        ))
        dx_label = always_redraw(lambda: MathTex(r"\Delta x = dx", font_size=18, color=WHITE).next_to(
            dx_line, DOWN, buff=0.12
        ))

        # Garis vertikal dy (sepanjang garis singgung)
        dy_line = always_redraw(lambda: Line(
            axes.c2p(x0 + dx_val.get_value(), y0),
            axes.c2p(x0 + dx_val.get_value(), tangent_fn(x0 + dx_val.get_value())),
            color=GREEN_C,
            stroke_width=3
        ))
        dy_label = always_redraw(lambda: MathTex(r"dy", font_size=20, color=GREEN_C).next_to(
            dy_line, RIGHT, buff=0.1
        ))

        # Garis vertikal galat (selisih antara kurva dan garis singgung)
        error_line = always_redraw(lambda: Line(
            axes.c2p(x0 + dx_val.get_value(), tangent_fn(x0 + dx_val.get_value())),
            axes.c2p(x0 + dx_val.get_value(), np.sqrt(x0 + dx_val.get_value())),
            color=RED_C,
            stroke_width=3
        ))

        self.play(
            Create(dx_line),
            Write(dx_label),
            Create(dy_line),
            Write(dy_label),
            FadeIn(pt_R_tan),
            FadeIn(pt_Q_curve),
            Create(error_line),
            run_time=1.8
        )
        self.wait(1.5)

        # Panel penjelasan komponen di sisi kanan
        legenda_dx = MathTex(r"\bullet\ dx = \Delta x \text{ (perubahan input)}", font_size=20, color=WHITE)
        legenda_dy = MathTex(r"\bullet\ dy = f'(a)dx \text{ (naik pada garis singgung)}", font_size=20, color=GREEN_C)
        legenda_dy_nyata = MathTex(r"\bullet\ \Delta y = f(a+\Delta x) - f(a) \text{ (naik kurva)}", font_size=20, color=YELLOW)
        legenda_galat = MathTex(r"\bullet\ \text{Galat} = |\Delta y - dy| \text{ (celah merah)}", font_size=20, color=RED_C)

        grup_legenda = VGroup(legenda_dx, legenda_dy, legenda_dy_nyata, legenda_galat).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        grup_legenda.move_to(RIGHT * 3.3 + UP * 0.8)

        self.play(Write(grup_legenda), run_time=2)
        self.wait(1.5)

        # -------------------------------------------------------------
        # AKSI 3: Inversi Sokratik (Penyusutan Δx -> 0)
        # -------------------------------------------------------------
        pertanyaan_sokratik = Text(
            "Apa yang terjadi pada celah galat ketika Δx mendekati 0?",
            font_size=23,
            color=YELLOW_B
        ).to_edge(UP, buff=0.35)
        self.play(Transform(judul, pertanyaan_sokratik))
        self.wait(1.5)

        # Animasikan dx_val menyusut mendekati 0.15
        self.play(
            dx_val.animate.set_value(0.18),
            run_time=3.5,
            rate_func=smooth
        )
        self.wait(1.5)

        kesimpulan_zoom = Text(
            "Celah galat menyusut jauh lebih cepat!\nKurva dan garis singgung hampir berimpit.",
            font_size=18,
            color=GRAY_A,
            line_spacing=1.2
        ).next_to(grup_legenda, DOWN, buff=0.35, aligned_edge=LEFT)

        self.play(FadeIn(kesimpulan_zoom))
        self.wait(2)

        # -------------------------------------------------------------
        # AKSI 4: Kristalisasi Matematis Formal (Hampiran √4.08)
        # -------------------------------------------------------------
        judul_kristal = Text(
            "Kristalisasi Matematis: Menaksir Nilai √4.08",
            font_size=23,
            color=WHITE
        ).to_edge(UP, buff=0.35)

        self.play(
            Transform(judul, judul_kristal),
            FadeOut(grup_legenda),
            FadeOut(kesimpulan_zoom)
        )

        rumus_linier = MathTex(
            r"L(x) = f(a) + f'(a)(x - a)",
            font_size=22,
            color=TEAL_C
        )
        langkah1 = MathTex(
            r"f(x) = \sqrt{x} \implies f'(x) = \frac{1}{2\sqrt{x}}",
            font_size=21
        )
        langkah2 = MathTex(
            r"a = 4 \implies f(4) = 2,\ f'(4) = \frac{1}{4} = 0.25",
            font_size=21
        )
        langkah3 = MathTex(
            r"dx = 4.08 - 4 = 0.08",
            font_size=21
        )
        langkah4 = MathTex(
            r"dy = f'(4)\,dx = 0.25 \times 0.08 = \mathbf{0.02}",
            font_size=22,
            color=GREEN_C
        )
        hasil = MathTex(
            r"\sqrt{4.08} \approx 2 + 0.02 = \mathbf{2.02}",
            font_size=24,
            color=YELLOW
        )
        grup_kristal = VGroup(
            rumus_linier,
            langkah1,
            langkah2,
            langkah3,
            langkah4,
            hasil
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        grup_kristal.move_to(RIGHT * 3.3 + UP * 0.35)

        box_hasil = SurroundingRectangle(hasil, color=YELLOW, buff=0.12)

        kalkulator = Text(
            "Nilai kalkulator: 2.019901...\n(Galat < 0.0001, akurasi > 99.99%!)",
            font_size=16,
            color=GRAY_A,
            line_spacing=1.2
        ).next_to(grup_kristal, DOWN, buff=0.25, aligned_edge=LEFT)

        self.play(Write(rumus_linier))
        self.play(Write(langkah1))
        self.play(Write(langkah2))
        self.play(Write(langkah3))
        self.play(Write(langkah4))
        self.play(Write(hasil), Create(box_hasil))
        self.play(FadeIn(kalkulator))
        self.wait(3)
