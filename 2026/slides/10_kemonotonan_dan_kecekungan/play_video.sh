#!/usr/bin/env bash
# ==============================================================================
# play_video.sh - Play Calculus Animations (Kemonotonan & Kecekungan)
# Usage:
#   ./play_video.sh [1|2|utama|naik]
# ==============================================================================

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CHOICE="${1:-1}"

case "$CHOICE" in
    2|naik|increasing|monoton)
        VIDEO="$DIR/MonotonicIncreasingScene.mp4"
        TITLE="MA1101 - Definisi Fungsi Monoton Naik"
        ;;
    *)
        VIDEO="$DIR/MonotonicityConcavityScene.mp4"
        TITLE="MA1101 - Kemonotonan dan Kecekungan (Master Scene)"
        ;;
esac

if [[ -f "$VIDEO" ]]; then
    echo "🎬 Memutar: $TITLE"
    mpv --title="$TITLE" --loop-file=inf "$VIDEO"
else
    # Fallback to OGV
    OGV_FALLBACK="${VIDEO%.mp4}.ogv"
    if [[ -f "$OGV_FALLBACK" ]]; then
        mpv --title="$TITLE" --loop-file=inf "$OGV_FALLBACK"
    else
        echo "❌ Video tidak ditemukan: $VIDEO"
        exit 1
    fi
fi
