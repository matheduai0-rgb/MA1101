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
