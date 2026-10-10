#!/usr/bin/env bash
# ==============================================================================
# present.sh - Launch Presentation with Native Video Playback (Diferensial & Hampiran)
# ==============================================================================

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PDF_FILE="$DIR/diferensial_dan_hampiran.pdf"
VIDEO_FILE="$DIR/DifferentialsApproximationScene.mp4"

# Source mise environment if available
if command -v mise &>/dev/null; then
    eval "$(mise env -s bash 2>/dev/null)" || true
fi

if command -v pympress &>/dev/null; then
    echo "🎓 Membuka presentasi dengan Pympress (video embedded otomatis)..."
    pympress "$PDF_FILE"
elif command -v pdfpc &>/dev/null; then
    echo "🎓 Membuka presentasi dengan PDFPC..."
    pdfpc "$PDF_FILE"
else
    echo "📄 Membuka slide dengan Evince..."
    evince "$PDF_FILE" &
    echo "🎬 Tips: Putar video menggunakan MPV:"
    echo "   mpv $VIDEO_FILE"
fi
