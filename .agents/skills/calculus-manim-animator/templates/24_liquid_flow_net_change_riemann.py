"""
Template: Akumulasi Laju Alir Fluida & Teorema Perubahan Total via Limit Jumlah Riemann
Topik: MA1101 Kalkulus I - Subtopik 4.2 (Jumlah Riemann & Integral Tentu) / 4.4 (Teorema Perubahan Total)
Gaya: Grant Sanderson (3Blue1Brown) & Pedagogi Sokratik 4 Babak
Deskripsi:
  Visualisasi komprehensif dua panel yang menyandingkan tangki fluida fisik (kiri)
  dengan grafik laju alir kontinu r(t) = dV/dt (kanan).
  
  Babak 1: Dilema Fisik - Tangki dialiri air dengan laju yang berubah-ubah r(t).
           Tantangan: Bagaimana menghitung perubahan volume total Delta V jika laju alir tak konstan?
  Babak 2: Eksplorasi Geometris - Membagi waktu menjadi irisan kecil Delta t.
           Dalam setiap irisan, laju dianggap konstan r(t_i*).
           Volume per irisan Delta V_i ~ r(t_i*) * Delta t (luas persegi panjang Riemann!).
           Masing-masing persegi panjang terpetakan langsung ke lapisan air di dalam tangki.
  Babak 3: Inversi Sokratik - Apa yang terjadi jika partisi waktu diperhalus (Delta t -> 0)?
           Penyangatan mesh: n = 4 -> 10 -> 24 -> 60.
           Lapisan air bertingkat menghalus menjadi kolom fluida mulus tanpa galat.
  Babak 4: Kristalisasi Formal - Batas jumlah Riemann menghasilkan integral tentu:
           Delta V = V(T) - V(0) = lim_{n -> infty} sum r(t_i*) Delta t = int_0^T r(t) dt.
           Teorema Perubahan Total (Net Change Theorem).

Render Cepat:
  .agents/skills/calculus-manim-animator/scripts/preview_scene.sh \\
    .agents/skills/calculus-manim-animator/templates/24_liquid_flow_net_change_riemann.py \\
    LiquidFlowRiemannNetChangeScene -s
"""

from manim import *
import numpy as np


def rate_func_flow(t):
    """
    Laju alir kontinu r(t) dalam liter/menit.
    r(t) = 1.0 + 3.0 * sin^2(pi * t / 5.0) pada t in [0, 5].
    Integral analitik pada [0, 5] = 12.5 Liter.
    """
    return 1.0 + 3.0 * (np.sin(np.pi * t / 5.0) ** 2)


CARD_BG = "#111827"
TANK_BORDER_COLOR = "#94A3B8"
WATER_COLOR = "#0284C7"
WATER_HIGHLIGHT = "#38BDF8"
ACCENT_GOLD = "#F59E0B"


class LiquidFlowRiemannNetChangeScene(Scene):
    def construct(self):
        # =====================================================================
        # PENGATURAN TATA LETAK & DUA PANEL
        # =====================================================================
        # Panel Kiri: Tangki Fluida Fisik (x in [-6.5, -1.8])
        # Panel Kanan: Sumbu Grafik r(t) (x in [-1.0, 6.4])
        # Bawah: Kartu Telemetri / Rumus
        # Atas: Judul & Pertanyaan Sokratik
        
        # ---------------------------------------------------------------------
        # BABAK 1: DILEMA FISIK (Laju Alir yang Berfluktuasi)
        # ---------------------------------------------------------------------
        header_title = Text(
            "Bagaimana menghitung perubahan volume total jika laju alir terus berubah?",
            font_size=21,
            color=WHITE,
            weight=BOLD,
        ).to_edge(UP, buff=0.28)
        
        self.play(Write(header_title), run_time=1.6)
        self.wait(1.0)

        # 1. Konstruksi Tangki Air (Panel Kiri)
        tank_width = 2.4
        tank_height = 3.6
        tank_center = np.array([-4.2, -0.2, 0])
        tank_bottom = tank_center[1] - tank_height / 2
        tank_left = tank_center[0] - tank_width / 2
        tank_right = tank_center[0] + tank_width / 2
        tank_top = tank_center[1] + tank_height / 2

        # Rangka kaca tangki (U-shape)
        tank_walls = VMobject(color=TANK_BORDER_COLOR, stroke_width=3.5)
        tank_walls.set_points_as_corners([
            np.array([tank_left, tank_top, 0]),
            np.array([tank_left, tank_bottom, 0]),
            np.array([tank_right, tank_bottom, 0]),
            np.array([tank_right, tank_top, 0]),
        ])

        # Pipa pengisi di atas tangki
        pipe_nozzle = VMobject(color=GRAY_B, stroke_width=3.0)
        pipe_nozzle.set_points_as_corners([
            np.array([tank_center[0] - 0.25, tank_top + 0.65, 0]),
            np.array([tank_center[0] - 0.25, tank_top + 0.15, 0]),
            np.array([tank_center[0] + 0.25, tank_top + 0.15, 0]),
            np.array([tank_center[0] + 0.25, tank_top + 0.65, 0]),
        ])
        pipe_lbl = Text("Pipa Alir", font_size=13, color=GRAY_A).next_to(pipe_nozzle, UP, buff=0.08)

        # Skala graduasi tangki (0 L, 5 L, 10 L, 15 L)
        grad_ticks = VGroup()
        max_liters = 15.0
        scale_height = tank_height * 0.88  # ketinggian untuk 15 Liter
        for lit in [0, 5, 10, 15]:
            y_pos = tank_bottom + (lit / max_liters) * scale_height
            tick = Line(
                np.array([tank_right, y_pos, 0]),
                np.array([tank_right + 0.14, y_pos, 0]),
                color=GRAY_A,
                stroke_width=1.5,
            )
            txt = MathTex(f"{lit}\\,\\text{{L}}", font_size=13, color=GRAY_B).next_to(tick, RIGHT, buff=0.06)
            grad_ticks.add(tick, txt)

        tank_label = Text("Tangki Penampung", font_size=16, color=BLUE_B).next_to(tank_walls, DOWN, buff=0.25)
        tank_group = VGroup(tank_walls, pipe_nozzle, pipe_lbl, grad_ticks, tank_label)

        # 2. Konstruksi Sumbu Koordinat Laju Alir (Panel Kanan)
        axes = Axes(
            x_range=[0, 5.5, 1],
            y_range=[0, 5.0, 1],
            x_length=6.0,
            y_length=3.4,
            axis_config={
                "color": GRAY_C,
                "stroke_width": 1.5,
                "include_tip": True,
                "tip_width": 0.12,
                "tip_height": 0.12,
            },
        ).add_coordinates(font_size=13)
        axes.move_to(np.array([2.8, -0.25, 0]))

        x_axis_lbl = MathTex(r"t\text{ (menit)}", font_size=16, color=GRAY_A).next_to(axes.x_axis.get_end(), RIGHT, buff=0.1)
        y_axis_lbl = MathTex(r"r(t)\text{ (L/menit)}", font_size=16, color=GRAY_A).next_to(axes.y_axis.get_top(), UP, buff=0.12)
        axes_labels = VGroup(x_axis_lbl, y_axis_lbl)

        # Kurva r(t)
        t_max = 5.0
        graph_r = axes.plot(rate_func_flow, x_range=[0, t_max], color=YELLOW, stroke_width=3.2)
        curve_label = MathTex(r"r(t) = \frac{dV}{dt}", font_size=20, color=YELLOW).next_to(
            axes.c2p(2.5, rate_func_flow(2.5)), UP, buff=0.18
        )

        # Tampilkan tangki dan sistem sumbu
        self.play(
            Create(tank_walls),
            Create(pipe_nozzle),
            FadeIn(pipe_lbl),
            FadeIn(grad_ticks),
            Write(tank_label),
            run_time=1.4,
        )
        self.play(Create(axes), Write(axes_labels), run_time=1.3)
        self.play(Create(graph_r), Write(curve_label), run_time=1.5)
        self.wait(1.5)

        # ---------------------------------------------------------------------
        # BABAK 2: EKSPLORASI GEOMETRIS (Partisi Waktu & Irisan Persegi Panjang)
        # ---------------------------------------------------------------------
        header_act2 = Text(
            "Strategi: Bagi waktu menjadi selang kecil Δt. Anggap laju konstan pada tiap selang!",
            font_size=19,
            color=TEAL_A,
        ).to_edge(UP, buff=0.28)
        self.play(Transform(header_title, header_act2), run_time=1.2)
        self.wait(1.0)

        n_coarse = 4
        dt_coarse = t_max / n_coarse  # 1.25 menit
        t_nodes = [i * dt_coarse for i in range(n_coarse + 1)]

        # Hitung volume perkiraan tiap irisan (Left Riemann Sum)
        slice_volumes = []
        for i in range(n_coarse):
            t_left = t_nodes[i]
            r_val = rate_func_flow(t_left)
            vol_i = r_val * dt_coarse
            slice_volumes.append(vol_i)

        # Persegi panjang Riemann kasar (n=4)
        rects_n4 = axes.get_riemann_rectangles(
            graph_r,
            x_range=[0, t_max],
            dx=dt_coarse,
            input_sample_type="left",
            stroke_width=1.5,
            stroke_color=WHITE,
            fill_opacity=0.45,
            color=(BLUE_C, TEAL_C),
        )

        # Lapisan air bertingkat di dalam tangki yang berkorespondensi 1-ke-1
        water_slabs = VGroup()
        current_y = tank_bottom
        inner_w = tank_width - 0.08

        for i, vol in enumerate(slice_volumes):
            slab_h = (vol / max_liters) * scale_height
            slab = Rectangle(
                width=inner_w,
                height=slab_h,
                fill_color=WATER_COLOR,
                fill_opacity=0.65,
                stroke_color=WATER_HIGHLIGHT,
                stroke_width=1.2,
            )
            # Tempatkan tepat di atas lapisan sebelumnya
            slab.move_to(np.array([tank_center[0], current_y + slab_h / 2, 0]))
            water_slabs.add(slab)
            current_y += slab_h

        # Telemetri / Penjelasan rumus
        formula_box = VGroup()
        formula_step1 = MathTex(
            r"\Delta t = \frac{T}{n} = \frac{5}{4} = 1.25\text{ menit}",
            font_size=19,
            color=WHITE,
        )
        formula_step2 = MathTex(
            r"\Delta V_i \approx r(t_i^*) \cdot \Delta t \quad \text{(Volume irisan ke-}i\text{)}",
            font_size=19,
            color=ACCENT_GOLD,
        )
        formula_sum = MathTex(
            r"\Delta V \approx \sum_{i=1}^{4} r(t_i^*)\,\Delta t = 12.5\text{ Liter}",
            font_size=21,
            color=BLUE_B,
        )
        card_content = VGroup(formula_step1, formula_step2, formula_sum).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        card_content.move_to(np.array([0.0, -3.15, 0]))
        card_bg = SurroundingRectangle(
            card_content,
            color=BLUE_D,
            fill_color=CARD_BG,
            fill_opacity=0.92,
            buff=0.18,
            corner_radius=0.08,
        )
        telemetry_card = VGroup(card_bg, card_content)

        self.play(FadeIn(telemetry_card), run_time=1.0)
        self.wait(0.8)

        # Munculkan satu per satu persegi panjang Riemann dan lapisan air yang bersesuaian!
        # Berikan efek aliran air dari pipa ke tangki
        stream_line = Line(
            np.array([tank_center[0], tank_top + 0.15, 0]),
            np.array([tank_center[0], tank_bottom, 0]),
            color=WATER_HIGHLIGHT,
            stroke_width=4.0,
            stroke_opacity=0.8,
        )

        for i in range(n_coarse):
            target_rect = rects_n4[i]
            target_slab = water_slabs[i]

            # Sorot persegi panjang dengan warna emas
            highlight_rect = target_rect.copy().set_fill(ACCENT_GOLD, opacity=0.8).set_stroke(YELLOW, 2.0)
            highlight_slab = target_slab.copy().set_fill(ACCENT_GOLD, opacity=0.8).set_stroke(YELLOW, 2.0)

            # Busur transfer visual dari persegi panjang ke lapisan air di tangki
            transfer_arrow = CurvedArrow(
                target_rect.get_top(),
                target_slab.get_right(),
                angle=-0.4,
                color=ACCENT_GOLD,
                stroke_width=2.5,
            )
            slice_tag = MathTex(
                rf"\Delta V_{{{i+1}}} \approx {slice_volumes[i]:.2f}\,\text{{L}}",
                font_size=15,
                color=ACCENT_GOLD,
            ).next_to(transfer_arrow, UP, buff=0.04)

            # Update panjang stream line ke permukaan air saat ini
            slab_top_y = target_slab.get_top()[1]
            stream_step = Line(
                np.array([tank_center[0], tank_top + 0.15, 0]),
                np.array([tank_center[0], slab_top_y, 0]),
                color=WATER_HIGHLIGHT,
                stroke_width=4.0,
                stroke_opacity=0.8,
            )

            self.play(
                Create(target_rect),
                Create(stream_step),
                run_time=0.6,
            )
            self.play(
                Create(transfer_arrow),
                Write(slice_tag),
                FadeIn(target_slab),
                run_time=0.8,
            )
            self.wait(0.6)
            self.play(
                FadeOut(transfer_arrow),
                FadeOut(slice_tag),
                FadeOut(stream_step),
                run_time=0.4,
            )

        self.wait(1.5)

        # ---------------------------------------------------------------------
        # BABAK 3: INVERSI SOKRATIK (Refinement: Apa yang Terjadi saat Δt -> 0?)
        # ---------------------------------------------------------------------
        header_act3 = Text(
            "Apa yang terjadi jika partisi waktu dibuat sangat tipis (Δt → 0)?",
            font_size=20,
            color=YELLOW,
            weight=BOLD,
        ).to_edge(UP, buff=0.28)
        self.play(Transform(header_title, header_act3), run_time=1.2)
        self.wait(2.0)

        # Kartu telemetri dinamis saat mesh diperhalus
        lbl_mesh_n = MathTex(r"n = 4", font_size=21, color=WHITE)
        lbl_mesh_dt = MathTex(r"\Delta t = 1.25", font_size=21, color=GRAY_A)
        lbl_mesh_type = Text("Hampiran Kasar (Tangga Bertingkat)", font_size=15, color=MAROON_B)
        mesh_row = VGroup(lbl_mesh_n, lbl_mesh_dt, lbl_mesh_type).arrange(RIGHT, buff=0.25)
        mesh_row.move_to(card_content.get_center())

        self.play(
            FadeOut(card_content),
            FadeIn(mesh_row),
            run_time=0.8,
        )

        current_rects = rects_n4
        current_water = water_slabs

        refinement_steps = [
            (10, 0.50, "Mulai Menghaluskan Galat", TEAL_B),
            (25, 0.20, "Galat Undakan Semakin Hilang", TEAL_A),
            (60, 0.083, "Hampir Mulus Sempurna", GREEN_B),
        ]

        total_exact_vol = 12.5
        exact_water_h = (total_exact_vol / max_liters) * scale_height

        for n_val, dt_val, desc, desc_color in refinement_steps:
            new_rects = axes.get_riemann_rectangles(
                graph_r,
                x_range=[0, t_max],
                dx=dt_val,
                input_sample_type="left",
                stroke_width=0.4 if n_val > 20 else 1.0,
                stroke_color=WHITE if n_val < 30 else BLUE_B,
                fill_opacity=0.55,
                color=(BLUE_C, TEAL_C),
            )

            new_mesh_n = MathTex(rf"n = {n_val}", font_size=21, color=WHITE)
            new_mesh_dt = MathTex(rf"\Delta t = {dt_val:.3f}\text{{ min}}", font_size=21, color=GRAY_A)
            new_mesh_type = Text(desc, font_size=15, color=desc_color)
            new_mesh_row = VGroup(new_mesh_n, new_mesh_dt, new_mesh_type).arrange(RIGHT, buff=0.25)
            new_mesh_row.move_to(card_content.get_center())

            self.play(
                Transform(current_rects, new_rects),
                Transform(mesh_row, new_mesh_row),
                run_time=1.4,
                rate_func=smooth,
            )
            self.wait(0.8)

        # Transisi ke kolom air kontinu mulus di tangki dan daerah mulus di bawah r(t)
        continuous_water = Rectangle(
            width=inner_w,
            height=exact_water_h,
            fill_color=WATER_COLOR,
            fill_opacity=0.8,
            stroke_color=WATER_HIGHLIGHT,
            stroke_width=2.0,
        )
        continuous_water.move_to(np.array([tank_center[0], tank_bottom + exact_water_h / 2, 0]))

        continuous_integral_area = axes.get_area(
            graph_r,
            x_range=[0, t_max],
            color=(BLUE_D, TEAL_D),
            opacity=0.6,
        )

        water_surface_line = Line(
            np.array([tank_left + 0.04, tank_bottom + exact_water_h, 0]),
            np.array([tank_right - 0.04, tank_bottom + exact_water_h, 0]),
            color=WHITE,
            stroke_width=2.5,
        )
        vol_label = MathTex(r"V(T) - V(0) = 12.5\,\text{L}", font_size=16, color=WHITE).next_to(
            water_surface_line, UP, buff=0.08
        )

        self.play(
            FadeTransform(current_rects, continuous_integral_area),
            FadeTransform(current_water, continuous_water),
            Create(water_surface_line),
            Write(vol_label),
            run_time=2.0,
            rate_func=smooth,
        )
        self.wait(1.5)

        # ---------------------------------------------------------------------
        # BABAK 4: KRISTALISASI FORMAL (Teorema Perubahan Total / TDK)
        # ---------------------------------------------------------------------
        header_act4 = Text(
            "Teorema Perubahan Total: Integral Laju Alir Adalah Perubahan Volume Bersih!",
            font_size=19,
            color=GREEN_A,
            weight=BOLD,
        ).to_edge(UP, buff=0.28)
        self.play(Transform(header_title, header_act4), run_time=1.2)
        self.wait(1.0)

        # Formulasi Teorema Perubahan Total
        final_formula_1 = MathTex(
            r"\Delta V",
            r"=",
            r"\lim_{n \to \infty} \sum_{i=1}^n r(t_i^*)\,\Delta t",
            r"=",
            r"\int_0^T r(t)\,dt",
            font_size=23,
        )
        final_formula_1[0].set_color(BLUE_B)
        final_formula_1[2].set_color(TEAL_B)
        final_formula_1[4].set_color(YELLOW)

        final_formula_2 = MathTex(
            r"\text{Karena } r(t) = \frac{dV}{dt}: \quad \int_0^T \frac{dV}{dt}\,dt = V(T) - V(0) = 12.5\text{ Liter}",
            font_size=20,
            color=WHITE,
        )
        final_content = VGroup(final_formula_1, final_formula_2).arrange(DOWN, buff=0.14)
        final_content.move_to(np.array([0.0, -2.98, 0]))

        final_box = SurroundingRectangle(
            final_content,
            color=GREEN_B,
            fill_color=CARD_BG,
            fill_opacity=0.95,
            buff=0.18,
            corner_radius=0.1,
        )

        self.play(
            FadeOut(mesh_row),
            FadeOut(card_bg),
            FadeIn(final_box),
            Write(final_formula_1),
            run_time=1.6,
        )
        self.wait(1.2)
        self.play(Write(final_formula_2), run_time=1.5)
        self.wait(1.0)

        # Sorot kaitan integral pada kurva r(t) dan volume tangki
        glow_curve = graph_r.copy().set_color(GREEN_A).set_stroke(width=5.0)
        glow_water = continuous_water.copy().set_stroke(color=GREEN_A, width=3.5)

        self.play(
            ShowPassingFlash(glow_curve, run_time=2.0, time_width=0.4),
            ShowPassingFlash(glow_water, run_time=2.0, time_width=0.4),
        )
        self.wait(3.0)
