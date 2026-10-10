#!/usr/bin/env bash
# ==============================================================================
# play_video.sh - Play Calculus Animation (Ekstrem Lokal & Ekstrem Selang Buka)
# Usage:
#   ./play_video.sh
# ==============================================================================

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VIDEO="$DIR/LocalExtremaOpenIntervalScene.mp4"
TITLE="MA1101 - Ekstrem Lokal & Ekstrem pada Selang Buka (Master Scene)"

if [[ -f "$VIDEO" ]]; then
    echo "🎬 Memutar: $TITLE"
    mpv --title="$TITLE" --loop-file=inf "$VIDEO"
else
    # Fallback to OGV
    OGV_FALLBACK="$DIR/LocalExtremaOpenIntervalScene.ogv"
    if [[ -f "$OGV_FALLBACK" ]]; then
        mpv --title="$TITLE" --loop-file=inf "$OGV_FALLBACK"
    else
        echo "❌ Video tidak ditemukan: $VIDEO"
        exit 1
    fi
fi
