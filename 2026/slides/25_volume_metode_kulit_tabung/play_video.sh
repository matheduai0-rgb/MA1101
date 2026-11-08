#!/usr/bin/env bash
# ==============================================================================
# play_video.sh - Play Socratic Manim Video (Subtopik 5.3 Metode Kulit Tabung)
# Usage: ./play_video.sh [bentang|geser]
# ==============================================================================

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MODE="${1:-bentang}"

if [[ "$MODE" == "geser" ]]; then
    VIDEO_FILE="$DIR/ShellsVsWashersShiftedAxisScene.mp4"
    TITLE="Subbab 5.3: Kulit Tabung Antara Dua Kurva & Sumbu Putar Bergeser (x = k)"
else
    VIDEO_FILE="$DIR/CylindricalShellsUnrollingScene.mp4"
    TITLE="Subbab 5.3: Metode Kulit Tabung & Pembentangan Balok (2πrh Δx)"
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
