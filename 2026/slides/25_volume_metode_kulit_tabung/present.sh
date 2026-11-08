#!/usr/bin/env bash
# ==============================================================================
# present.sh - Launch Interactive Reveal.js + CindyJS + Manim Presentation (5.3)
# Usage:
#   ./present.sh         # Open interactive HTML5 slide deck in default browser
#   ./present.sh --pdf   # Fallback: Open legacy Beamer PDF in pympress/pdfpc
# ==============================================================================

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
HTML_FILE="$DIR/interactive_cindyjs_reveal.html"
PDF_FILE="$DIR/volume_metode_kulit_tabung.pdf"
VIDEO_FILE="$DIR/CylindricalShellsUnrollingScene.mp4"

if [[ "${1:-}" == "--pdf" ]]; then
    if command -v pympress &>/dev/null; then
        echo "🎓 Membuka PDF Beamer dengan Pympress..."
        pympress "$PDF_FILE"
    elif command -v pdfpc &>/dev/null; then
        echo "🎓 Membuka PDF Beamer dengan PDFPC..."
        pdfpc "$PDF_FILE"
    else
        echo "📄 Membuka PDF dengan Evince..."
        evince "$PDF_FILE" &
    fi
    exit 0
fi

echo "🚀 Membuka Presentasi Interaktif (Reveal.js + KaTeX + CindyJS + Manim):"
echo "   $HTML_FILE"

if command -v xdg-open &>/dev/null; then
    xdg-open "$HTML_FILE" >/dev/null 2>&1 &
elif command -v chromium &>/dev/null; then
    chromium "$HTML_FILE" >/dev/null 2>&1 &
elif command -v google-chrome &>/dev/null; then
    google-chrome "$HTML_FILE" >/dev/null 2>&1 &
else
    echo "Silakan buka berkas berikut di peramban web Anda: $HTML_FILE"
fi
