"""
Template: Masalah Pengoptimuman Terapan - Kotak Karton (MA1101)
Subtopik: 3.1 & 3.4 Maksimum/Minimum dan Pemodelan Matematika
Bahasa: Indonesia
Gaya: Grant Sanderson (3Blue1Brown) & Metode Sokratik
Deskripsi:
  Visualisasi lengkap pemotongan karton 6 x 6 dm, pembentukan jaring-jaring
  kotak tanpa tutup (bentuk salib/cross), pelipatan menjadi kotak 3D terbuka,
  serta keterhubungannya dengan grafik volume V(x) = x(6 - 2x)^2 dan titik kritis V'(x) = 0.
"""

from manim import *
import numpy as np

class BoxOptimizationScene(Scene):
    def construct(self):
        # -------------------------------------------------------------
        # AKSI 1: Tantangan Sokratik (The Pique) & Pemotongan Karton
        # -------------------------------------------------------------
        judul = Text(
            "Berapa ukuran potongan sudut x\nagar volume kotak tanpa tutup maksimum?",
            font_size=22,
            line_spacing=1.2,
            color=WHITE
        ).to_edge(UP, buff=0.35)
        
        self.play(Write(judul), run_time=1.2)
        self.wait(0.4)

        # Parameter Geometri
        net_center = LEFT * 4.4 + DOWN * 1.55
        scale_net = 0.48  # 6.0 dm * 0.48 = 2.88 visual units
        H_sheet = 3.0 * scale_net  # 1.44 units (setengah sisi karton)

        box_center = LEFT * 4.4 + UP * 1.45
        scale_3d = 0.38

        x_tracker = ValueTracker(1.0)

        # Karton awal 6 x 6 dm
        sheet_full = Square(
            side_length=6.0 * scale_net,
            stroke_color=GRAY_B,
            stroke_width=1.5,
            fill_color=DARK_GRAY,
            fill_opacity=0.25
        ).move_to(net_center)

        brace_karton = Brace(sheet_full, LEFT, buff=0.1, color=GRAY_A)
        brace_label = MathTex(r"6\text{ dm}", font_size=18, color=GRAY_A).next_to(brace_karton, LEFT, buff=0.08)

        # 4 Sudut awal yang akan dipotong
        init_x = 1.0
        w_x_init = init_x * scale_net
        corners_init = VGroup()
        offsets = [
            (-H_sheet + w_x_init / 2.0, -H_sheet + w_x_init / 2.0),
            (H_sheet - w_x_init / 2.0, -H_sheet + w_x_init / 2.0),
            (-H_sheet + w_x_init / 2.0, H_sheet - w_x_init / 2.0),
            (H_sheet - w_x_init / 2.0, H_sheet - w_x_init / 2.0),
        ]
        dirs = [DL, DR, UL, UR]
        for (ox, oy), d in zip(offsets, dirs):
            c_sq = Rectangle(
                width=w_x_init, height=w_x_init,
                fill_color=RED_E, fill_opacity=0.6,
                stroke_color=RED_C, stroke_width=1.5
            ).move_to(net_center + np.array([ox, oy, 0]))
            c_lbl = MathTex(r"x", font_size=16, color=RED_A).move_to(c_sq.get_center())
            corners_init.add(VGroup(c_sq, c_lbl))

        self.play(FadeIn(sheet_full), Create(brace_karton), Write(brace_label), FadeIn(corners_init), run_time=1.2)
        self.wait(0.4)

        # Animasi Pemotongan: 4 sudut meluncur keluar dan memudar (Dipotong & Dibuang!)
        anim_cuts = []
        for c_grp, d in zip(corners_init, dirs):
            anim_cuts.append(c_grp.animate.shift(d * 0.4).set_opacity(0))

        # Fungsi pembuat Jaring-Jaring 2D dinamis (Bentuk Salib / Cross)
        def get_net(x_val):
            group = VGroup()
            s_base = (6.0 - 2.0 * x_val) * scale_net
            s_x = x_val * scale_net

            # Ghost outline karton asli 6x6
            sheet_ghost = Square(
                side_length=6.0 * scale_net,
                stroke_color=GRAY_C,
                stroke_width=1.0,
                stroke_opacity=0.35,
                fill_opacity=0
            ).move_to(net_center)
            group.add(sheet_ghost)

            # 4 Sudut kosong / void potongan (garis batas tipis merah)
            cur_offsets = [
                (-H_sheet + s_x / 2.0, -H_sheet + s_x / 2.0),
                (H_sheet - s_x / 2.0, -H_sheet + s_x / 2.0),
                (-H_sheet + s_x / 2.0, H_sheet - s_x / 2.0),
                (H_sheet - s_x / 2.0, H_sheet - s_x / 2.0),
            ]
            for ox, oy in cur_offsets:
                void_sq = Rectangle(
                    width=s_x, height=s_x,
                    stroke_color=RED_E, stroke_width=1.0, stroke_opacity=0.45,
                    fill_opacity=0
                ).move_to(net_center + np.array([ox, oy, 0]))
                group.add(void_sq)

            # Alas Kotak (Teal)
            base = Rectangle(
                width=s_base, height=s_base,
                fill_color=TEAL_E, fill_opacity=0.8,
                stroke_color=TEAL_B, stroke_width=2.0
            ).move_to(net_center)
            group.add(base)

            # 4 Dinding Lipatan (Biru)
            b_flap = Rectangle(
                width=s_base, height=s_x,
                fill_color=BLUE_E, fill_opacity=0.55,
                stroke_color=BLUE_C, stroke_width=1.5
            ).move_to(net_center + np.array([0, -s_base/2.0 - s_x/2.0, 0]))

            t_flap = Rectangle(
                width=s_base, height=s_x,
                fill_color=BLUE_E, fill_opacity=0.55,
                stroke_color=BLUE_C, stroke_width=1.5
            ).move_to(net_center + np.array([0, s_base/2.0 + s_x/2.0, 0]))

            l_flap = Rectangle(
                width=s_x, height=s_base,
                fill_color=BLUE_E, fill_opacity=0.55,
                stroke_color=BLUE_C, stroke_width=1.5
            ).move_to(net_center + np.array([-s_base/2.0 - s_x/2.0, 0, 0]))

            r_flap = Rectangle(
                width=s_x, height=s_base,
                fill_color=BLUE_E, fill_opacity=0.55,
                stroke_color=BLUE_C, stroke_width=1.5
            ).move_to(net_center + np.array([s_base/2.0 + s_x/2.0, 0, 0]))

            group.add(b_flap, t_flap, l_flap, r_flap)

            # Garis Lipatan Putus-Putus (Emas) mengelilingi alas
            dl_b = DashedLine(
                net_center + np.array([-s_base/2.0, -s_base/2.0, 0]),
                net_center + np.array([s_base/2.0, -s_base/2.0, 0]),
                color=GOLD_A, stroke_width=2.0, dash_length=0.05
            )
            dl_t = DashedLine(
                net_center + np.array([-s_base/2.0, s_base/2.0, 0]),
                net_center + np.array([s_base/2.0, s_base/2.0, 0]),
                color=GOLD_A, stroke_width=2.0, dash_length=0.05
            )
            dl_l = DashedLine(
                net_center + np.array([-s_base/2.0, -s_base/2.0, 0]),
                net_center + np.array([-s_base/2.0, s_base/2.0, 0]),
                color=GOLD_A, stroke_width=2.0, dash_length=0.05
            )
            dl_r = DashedLine(
                net_center + np.array([s_base/2.0, -s_base/2.0, 0]),
                net_center + np.array([s_base/2.0, s_base/2.0, 0]),
                color=GOLD_A, stroke_width=2.0, dash_length=0.05
            )
            group.add(dl_b, dl_t, dl_l, dl_r)

            # Label di dalam alas bila ruangan cukup
            if s_base > 0.8:
                t_alas = Text("Alas", font_size=11, color=WHITE).move_to(net_center + UP * 0.08)
                t_dim = MathTex(r"6-2x", font_size=12, color=TEAL_A).next_to(t_alas, DOWN, buff=0.04)
                group.add(t_alas, t_dim)

            if s_x > 0.25:
                t_x = MathTex(r"x", font_size=13, color=YELLOW_A).move_to(
                    net_center + np.array([s_base/2.0 + s_x/2.0, 0, 0])
                )
                group.add(t_x)

            return group

        # Fungsi pembuat Kotak 3D Terbuka dinamis
        def get_3d_box(x_val):
            W = 6.0 - 2.0 * x_val
            L = 6.0 - 2.0 * x_val
            H = x_val

            ux = np.array([1.0, 0.0, 0.0])
            uy = np.array([0.55 * np.cos(35 * DEGREES), 0.55 * np.sin(35 * DEGREES), 0.0])
            uz = np.array([0.0, 1.0, 0.0])

            offset = box_center - scale_3d * (W/2.0 * ux + L/2.0 * uy + H/2.0 * uz)

            def project(x, y, z):
                return offset + scale_3d * (x * ux + y * uy + z * uz)

            p000 = project(0, 0, 0)
            p100 = project(W, 0, 0)
            p110 = project(W, L, 0)
            p010 = project(0, L, 0)

            p001 = project(0, 0, H)
            p101 = project(W, 0, H)
            p111 = project(W, L, H)
            p011 = project(0, L, H)

            group = VGroup()

            # Dinding dalam (belakang & kiri)
            back_w = Polygon(p010, p110, p111, p011,
                             fill_color=BLUE_E, fill_opacity=0.6,
                             stroke_color=BLUE_D, stroke_width=1.2)
            left_w = Polygon(p000, p010, p011, p001,
                             fill_color=BLUE_E, fill_opacity=0.7,
                             stroke_color=BLUE_D, stroke_width=1.2)
            # Dasar kotak dalam (Alas - Teal)
            floor = Polygon(p000, p100, p110, p010,
                            fill_color=TEAL_E, fill_opacity=0.85,
                            stroke_color=TEAL_B, stroke_width=1.8)
            # Dinding luar (depan & kanan)
            front_w = Polygon(p000, p100, p101, p001,
                              fill_color=BLUE_D, fill_opacity=0.5,
                              stroke_color=BLUE_B, stroke_width=1.8)
            right_w = Polygon(p100, p110, p111, p101,
                              fill_color=BLUE_E, fill_opacity=0.6,
                              stroke_color=BLUE_B, stroke_width=1.8)
            # Bibir atas kotak (Emas - Terbuka tanpa tutup!)
            rim = Polygon(p001, p101, p111, p011,
                          fill_opacity=0, stroke_color=GOLD_B, stroke_width=2.4)

            group.add(back_w, left_w, floor, front_w, right_w, rim)

            # Dimensi depan & tinggi
            brace_depan = BraceBetweenPoints(p000, p100, buff=0.08)
            lbl_depan = MathTex(r"6-2x", font_size=15, color=TEAL_A).next_to(brace_depan, DOWN, buff=0.06)

            brace_tinggi = BraceBetweenPoints(p100, p101, buff=0.08)
            lbl_tinggi = MathTex(r"x", font_size=15, color=YELLOW_A).next_to(brace_tinggi, RIGHT, buff=0.06)

            group.add(brace_depan, lbl_depan, brace_tinggi, lbl_tinggi)
            return group

        net_dynamic = always_redraw(lambda: get_net(x_tracker.get_value()))
        box_dynamic = always_redraw(lambda: get_3d_box(x_tracker.get_value()))

        label_net = Text("Jaring-Jaring Kotak", font_size=13, color=GOLD_B).next_to(net_center, DOWN, buff=1.65)
        label_box = Text("Kotak Tanpa Tutup (3D)", font_size=13, color=GOLD_B).move_to(box_center + UP * 1.1)

        arrow_fold = CurvedArrow(
            LEFT * 2.7 + DOWN * 0.5,
            LEFT * 2.7 + UP * 0.7,
            angle=-TAU/6,
            color=GOLD_C,
            stroke_width=2.0
        )
        t_fold = Text("Dilipat ke atas", font_size=13, color=GOLD_A).next_to(arrow_fold, RIGHT, buff=0.1)

        self.play(
            *anim_cuts,
            FadeOut(sheet_full),
            FadeIn(net_dynamic),
            Write(label_net),
            run_time=1.2
        )
        self.play(
            Create(arrow_fold),
            Write(t_fold),
            FadeIn(box_dynamic),
            Write(label_box),
            run_time=1.2
        )
        self.wait(0.5)

        # Di sebelah kanan: Grafik Volume V(x) = x * (6 - 2x)^2
        axes = Axes(
            x_range=[0, 3.2, 1],
            y_range=[0, 18, 5],
            x_length=4.8,
            y_length=3.8,
            axis_config={"color": GRAY_C}
        ).add_coordinates()
        axes.shift(RIGHT * 3.4 + DOWN * 0.6)

        V_fn = lambda x: x * (6.0 - 2.0 * x)**2
        V_curve = axes.plot(V_fn, x_range=[0, 3], color=TEAL_C, stroke_width=3)
        V_label = MathTex(r"V(x) = x(6 - 2x)^2", color=TEAL_C, font_size=20).next_to(axes.c2p(2.0, V_fn(2.0)), UR, buff=0.15)

        self.play(Create(axes), Create(V_curve), FadeIn(V_label), run_time=1.4)

        # -------------------------------------------------------------
        # AKSI 2: Eksplorasi Visual Reaktif (x, Jaring-Jaring, & Kotak 3D)
        # -------------------------------------------------------------
        dot_V = always_redraw(lambda:
            Dot(axes.c2p(x_tracker.get_value(), V_fn(x_tracker.get_value())), color=RED_C, radius=0.08)
        )
        line_drop_V = always_redraw(lambda:
            axes.get_vertical_line(axes.c2p(x_tracker.get_value(), V_fn(x_tracker.get_value())), color=RED_C).set_stroke(width=1.5, opacity=0.7)
        )

        label_x_val = always_redraw(lambda:
            MathTex(
                rf"x = {x_tracker.get_value():.2f}\text{{ dm}}",
                r"\implies",
                rf"V = {V_fn(x_tracker.get_value()):.1f}\text{{ liter}}",
                font_size=21
            ).move_to(RIGHT * 3.4 + UP * 2.3)
        )

        self.play(FadeIn(dot_V), Create(line_drop_V), Write(label_x_val), run_time=0.8)

        # -------------------------------------------------------------
        # AKSI 3: Pertanyaan Sokratik (Mencari Titik Puncak)
        # -------------------------------------------------------------
        pertanyaan = Text(
            "Perhatikan jaring-jaring & kotak 3D:\ndi manakah volume kotak mencapai maksimum?",
            font_size=21,
            color=TEAL_A,
            line_spacing=1.2
        ).to_edge(UP, buff=0.35)

        self.play(Transform(judul, pertanyaan), run_time=1.0)
        self.wait(0.5)

        # Variasi x_tracker: 1.0 -> 0.3 (ceper) -> 2.5 (cerobong sempit) -> 1.0 (optimum)
        self.play(x_tracker.animate.set_value(0.3), run_time=2.2, rate_func=smooth)
        self.wait(0.8)
        self.play(x_tracker.animate.set_value(2.5), run_time=2.5, rate_func=smooth)
        self.wait(0.8)
        self.play(x_tracker.animate.set_value(1.0), run_time=2.0, rate_func=smooth)
        self.wait(0.8)

        # -------------------------------------------------------------
        # AKSI 4: Kristalisasi Matematis Formal (Titik Kritis)
        # -------------------------------------------------------------
        judul_kristalisasi = Text(
            "Volume Maksimum Tercapai:",
            font_size=21,
            color=GOLD_B
        ).to_edge(UP, buff=0.35).shift(LEFT * 2.2)

        garis_puncak = Line(
            axes.c2p(0.3, 16),
            axes.c2p(1.7, 16),
            color=YELLOW,
            stroke_width=2.5
        )
        label_tangent_nol = MathTex(r"V'(x) = 0", color=YELLOW, font_size=20).next_to(axes.c2p(1.0, 16), UR, buff=0.08)

        kristalisasi = MathTex(
            r"V(x) &= 36x - 24x^2 + 4x^3 \\",
            r"V'(x) &= 36 - 48x + 12x^2 = 0 \\",
            r"12(x-1)(x-3) &= 0 \implies \mathbf{x = 1\text{ dm}}",
            font_size=19
        ).to_corner(UR, buff=0.35)
        kristalisasi[1].set_color(YELLOW)
        kristalisasi[2].set_color(GREEN_C)

        box_kristal = SurroundingRectangle(kristalisasi, color=BLUE_B, buff=0.1, stroke_width=1.5)

        self.play(
            Transform(judul, judul_kristalisasi),
            Create(garis_puncak),
            Write(label_tangent_nol),
            Write(kristalisasi),
            Create(box_kristal),
            run_time=1.4
        )
        self.wait(2.5)
