#!/usr/bin/env python3
"""
build_lecture_pack.py - Batch Render and Slide Asset Exporter for MA1101 Calculus Animations
Usage:
    python3 build_lecture_pack.py [--quality low|med|high] [--snapshot] [--output-dir DIR] [scene_files...]
"""

import os
import sys
import argparse
import subprocess
import time
from pathlib import Path

TEMPLATES_DIR = Path(__file__).resolve().parent.parent / "templates"
PREVIEW_SCRIPT = Path(__file__).resolve().parent / "preview_scene.sh"

SCENE_REGISTRY = [
    ("01_limits_and_continuity.py", "EpsilonDeltaLimitScene", "Bab 1: Definisi Limit Epsilon-Delta"),
    ("02_derivative_local_linearity.py", "LocalLinearityZoomScene", "Bab 2: Kelinieran Lokal Turunan"),
    ("03_riemann_sums_and_integral.py", "SocraticRiemannScene", "Bab 4: Jumlah Riemann & Integral Tentu"),
    ("04_fundamental_theorem_of_calculus.py", "SocraticFTCScene", "Bab 4: Teorema Dasar Kalkulus I"),
    ("05_taylor_polynomials.py", "SocraticTaylorScene", "Bab 6: Polinomial Taylor cos(x)"),
    ("06_related_rates_sliding_ladder.py", "SlidingLadderScene", "Bab 2: Laju yang Berkaitan (Tangga Meluncur)"),
    ("07_mean_value_theorem.py", "MeanValueTheoremScene", "Bab 3: Teorema Nilai Rata-rata (TNR)"),
    ("08_concavity_and_inflection.py", "ConcavityInflectionScene", "Bab 3: Kecekungan & Titik Belok"),
    ("09_applied_optimization_box.py", "BoxOptimizationScene", "Bab 3: Pengoptimuman Kotak Karton"),
    ("10_implicit_differentiation.py", "ImplicitDifferentiationScene", "Bab 2: Turunan Implisit (Lingkaran & Garis Singgung)"),
    ("11_differentials_and_linear_approximation.py", "DifferentialsApproximationScene", "Bab 2: Diferensial dan Hampiran (Δy vs dy & L(x))"),
    ("12_maximum_and_minimum.py", "MaximumMinimumScene", "Bab 3: Nilai Ekstrem & Titik Kritis (EVT)"),
    ("13_monotonicity_and_concavity.py", "MonotonicityConcavityScene", "Bab 3: Kemonotonan, Kecekungan & Titik Belok"),
    ("14_monotonic_increasing_definition.py", "MonotonicIncreasingScene", "Bab 3: Definisi Fungsi Monoton Naik"),
    ("15_local_extrema_and_open_intervals.py", "LocalExtremaOpenIntervalScene", "Bab 3: Ekstrem Lokal & Ekstrem pada Selang Buka"),
    ("16_curve_sketching_with_calculus.py", "CurveSketchingScene", "Bab 3: Grafik Fungsi dengan Kalkulus (Asimtot, Kemonotonan & Kecekungan)"),
    ("17_mathematical_modeling_pipeline.py", "PipelineOptimizationScene", "Bab 3: Pemodelan Matematika & Optimasi Terapan (Lintasan Pipa Biaya Minimum)"),
    ("18_antiderivatives_family_of_curves.py", "AntiderivativeFamilyScene", "Bab 3: Antiturunan & Keluarga Kurva F(x) + C"),
    ("19_differential_equations_separable.py", "SeparableODEScene", "Bab 3: Pengantar Persamaan Diferensial & Pemisahan Peubah"),
    ("20_area_polygon_exhaustion.py", "PolygonAreaExhaustionScene", "Bab 4: Luas Daerah (Poligon Dalam, Poligon Luar & Limit Notasi Sigma)"),
    ("21_definite_integral_signed_area.py", "DefiniteIntegralSignedAreaScene", "Bab 4: Integral Tentu (Jumlah Riemann & Luas Bertanda)"),
    ("22_first_fundamental_theorem_of_calculus.py", "FirstFTCAccumulationScene", "Bab 4: Teorema Dasar Kalkulus Pertama (Fungsi Akumulasi A'(x) = f(x))"),
    ("23_riemann_difference_telescoping.py", "RiemannDifferenceTelescopingScene", "Bab 4: Selisih Jumlah Riemann A(S_n)-A(R_n) Menuju Nol (Menara Teleskopik)"),
    ("24_liquid_flow_net_change_riemann.py", "LiquidFlowRiemannNetChangeScene", "Bab 4: Laju Alir Fluida & Teorema Perubahan Total"),
    ("25_second_fundamental_theorem_of_calculus.py", "SecondFTCScene", "Bab 4: Teorema Dasar Kalkulus Kedua (A(x) = F(x) + C)"),
    ("26_mean_value_theorem_for_integrals.py", "MeanValueTheoremIntegralScene", "Bab 4: Teorema Nilai Rata-rata untuk Integral (f_bar = f(c))"),
    ("27_symmetry_in_definite_integrals.py", "SymmetryDefiniteIntegralScene", "Bab 4: Penggunaan Simetri pada Integral Tentu (Fungsi Genap & Ganjil)"),
    ("28_trapezoidal_and_midpoint_rules.py", "TrapezoidalMidpointScene", "Bab 4: Integrasi Numerik (Aturan Trapesium vs Titik Tengah & Kecekungan)"),
    ("29_simpsons_parabolic_rule.py", "SimpsonsParabolicRuleScene", "Bab 4: Integrasi Numerik (Aturan Parabolik Simpson & Batas Galat)"),
    ("30_area_between_curves_vertical.py", "AreaBetweenCurvesVerticalScene", "Bab 5: Luas Daerah di Antara Dua Kurva (Pias Tegak Δx & Kurva Berpotongan)"),
    ("31_area_horizontal_vs_vertical_slicing.py", "AreaHorizontalVsVerticalScene", "Bab 5: Luas Daerah pada Bidang (Pias Mendatar Δy vs Pias Tegak Δx)"),
    ("32_volumes_disk_and_washer_method.py", "DiskAndWasherVolumeScene", "Bab 5: Volume Benda Putar (Metode Cakram & Metode Cincin)"),
    ("33_volumes_parallel_cross_sections.py", "ParallelCrossSectionsVolumeScene", "Bab 5: Volume Benda Pejal (Metode Irisan Sejajar / Lempeng)"),
    ("34_volumes_cylindrical_shells_unrolling.py", "CylindricalShellsUnrollingScene", "Bab 5: Volume Benda Putar (Metode Kulit Tabung & Pembentangan)"),
    ("35_shells_vs_washers_and_shifted_axis.py", "ShellsVsWashersShiftedAxisScene", "Bab 5: Metode Kulit Tabung Antara Dua Kurva & Sumbu Putar x = k"),
]


def main():
    parser = argparse.ArgumentParser(description="Batch Render MA1101 Socratic Manim Scenes")
    parser.add_argument("-q", "--quality", choices=["low", "med", "high"], default="low",
                        help="Render quality: low (480p15), med (720p30), high (1080p60)")
    parser.add_argument("-s", "--snapshot", action="store_true",
                        help="Render only the last frame (fast PNG keyframe export)")
    parser.add_argument("-f", "--filter", type=str, default="",
                        help="Filter scene filenames by substring (e.g. 'ladder', '06', 'optimization')")
    parser.add_argument("--list", action="store_true", help="List registered calculus scenes and exit")

    args = parser.parse_args()

    if args.list:
        print("\n🎓 MA1101 Registered Socratic Calculus Scenes:")
        print("=" * 70)
        for filename, scene_name, desc in SCENE_REGISTRY:
            print(f" • [{filename}] {scene_name:<28} -> {desc}")
        print("=" * 70)
        return 0

    quality_flag_map = {
        "low": "-ql",
        "med": "-m",
        "high": "-h"
    }
    q_flag = quality_flag_map[args.quality]

    scenes_to_render = [
        item for item in SCENE_REGISTRY
        if not args.filter or args.filter.lower() in item[0].lower() or args.filter.lower() in item[1].lower()
    ]

    if not scenes_to_render:
        print(f"❌ No scenes matched filter '{args.filter}'.")
        return 1

    print(f"\n🚀 Launching Batch Render ({len(scenes_to_render)} scenes)")
    print(f"   Quality:   {args.quality.upper()} ({q_flag})")
    print(f"   Snapshot:  {'Yes (PNG keyframe only)' if args.snapshot else 'No (Full animation video)'}\n")

    start_total = time.time()
    success_count = 0

    for idx, (filename, scene_name, desc) in enumerate(scenes_to_render, start=1):
        script_path = TEMPLATES_DIR / filename
        if not script_path.exists():
            print(f"⚠️  [{idx}/{len(scenes_to_render)}] File not found: {filename}")
            continue

        print(f"🎬 [{idx}/{len(scenes_to_render)}] Rendering {scene_name} ({desc})...")
        cmd = [str(PREVIEW_SCRIPT), str(script_path), scene_name, q_flag]
        if args.snapshot:
            cmd.append("-s")

        t0 = time.time()
        res = subprocess.run(cmd)
        elapsed = time.time() - t0

        if res.returncode == 0:
            print(f"   ✅ Done in {elapsed:.1f}s\n")
            success_count += 1
        else:
            print(f"   ❌ Failed with code {res.returncode}\n")

    total_time = time.time() - start_total
    print("=" * 70)
    print(f"🏁 Batch complete: {success_count}/{len(scenes_to_render)} scenes rendered successfully in {total_time:.1f}s.")
    print("=" * 70)
    return 0 if success_count == len(scenes_to_render) else 1

if __name__ == "__main__":
    sys.exit(main())
