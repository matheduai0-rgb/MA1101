#!/usr/bin/env bash
# ==============================================================================
# play_video.sh - Play Socratic Manim Video (Subtopik 5.1 Luas Daerah pada Bidang)
# Usage: ./play_video.sh [tegak|mendatar]
# ==============================================================================

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MODE="${1:-tegak}"

if [[ "$MODE" == "mendatar" ]]; then
    VIDEO_FILE="$DIR/AreaHorizontalVsVerticalScene.mp4"
    TITLE="Strategi Pias Mendatar (Δy) vs Pias Tegak (Δx)"
else
    VIDEO_FILE="$DIR/AreaBetweenCurvesVerticalScene.mp4"
    TITLE="Luas Daerah di Antara Dua Kurva — Pias Tegak (Δx)"
fi

if [[ ! -f "$VIDEO_FILE" ]]; then
    echo "❌ Berkas video tidak ditemukan: $VIDEO_FILE"
    exit 1
fi

echo "🎬 Memutar Animasi Sokratik: $TITLE..."

if command -v mpv &>/dev/null; then
    mpv --loop=inf "$VIDEO_FILE"
elif command -v vlc &>/dev/null; then
    vlc --loop "$VIDEO_FILE"
elif command -v xdg-open &>/dev/null; then
    xdg-open "$VIDEO_FILE"
else
    echo "⚠️ Pemutar video tidak ditemukan. Silakan buka manual: $VIDEO_FILE"
fi
