#!/usr/bin/env bash
# ==============================================================================
# preview_scene.sh - Rapid Headless Test Renderer for Manim Scenes
# Usage: ./preview_scene.sh <path_to_script.py> [SceneName] [options]
# Options:
#   -s, --snapshot     Render only the last frame (instant image check)
#   -m, --medium       Render at medium quality (720p30)
#   -h, --high         Render at high quality (1080p60)
#   -o, --open         Attempt to open output image/video with system viewer
# ==============================================================================

set -euo pipefail

# Automatically load mise environment if present (ensures tinytex & python/manim are in PATH)
if command -v mise &>/dev/null; then
    eval "$(mise env -s bash 2>/dev/null)" || true
fi

# Ensure dvisvgm is discoverable
if ! command -v dvisvgm &>/dev/null; then
    for p in /home/rafgani/.local/share/mise/installs/tinytex/*/bin/x86_64-linux; do
        if [[ -x "$p/dvisvgm" ]]; then
            export PATH="$p:$PATH"
            break
        fi
    done
fi

# Ensure manim packages are discoverable
if [[ -d "/home/rafgani/.local/share/mise/installs/python/3.14.7/lib/python3.14/site-packages" ]]; then
    export PYTHONPATH="${PYTHONPATH:-}:/home/rafgani/.local/share/mise/installs/python/3.14.7/lib/python3.14/site-packages"
fi
if ! command -v manim &>/dev/null && [[ -x "/home/rafgani/.local/share/mise/installs/python/3.14.7/bin/manim" ]]; then
    export PATH="/home/rafgani/.local/share/mise/installs/python/3.14.7/bin:$PATH"
fi

SCRIPT_FILE="${1:-}"
SCENE_NAME="${2:-}"
QUALITY_FLAG="-ql" # Default: low quality 480p15 for fast feedback
SNAPSHOT_FLAG=""
AUTO_OPEN=false

if [[ -z "$SCRIPT_FILE" ]]; then
    echo "❌ Error: Missing script file."
    echo "Usage: $0 <path_to_script.py> [SceneName] [-s|--snapshot] [-m|--medium] [-h|--high] [-o|--open]"
    exit 1
fi

if [[ ! -f "$SCRIPT_FILE" ]]; then
    echo "❌ Error: File not found: $SCRIPT_FILE"
    exit 1
fi

# Parse remaining arguments
shift 2 2>/dev/null || shift 1 2>/dev/null || true
while [[ $# -gt 0 ]]; do
    case "$1" in
        -s|--snapshot)
            SNAPSHOT_FLAG="-s"
            shift
            ;;
        -m|--medium)
            QUALITY_FLAG="-qm"
            shift
            ;;
        -h|--high)
            QUALITY_FLAG="-qh"
            shift
            ;;
        -o|--open)
            AUTO_OPEN=true
            shift
            ;;
        *)
            if [[ -z "$SCENE_NAME" ]]; then
                SCENE_NAME="$1"
            fi
            shift
            ;;
    esac
done

# Locate Manim command (CLI binary or python module)
MANIM_CMD=""
if command -v manim &>/dev/null; then
    MANIM_CMD="manim"
elif python3 -m manim --version &>/dev/null; then
    MANIM_CMD="python3 -m manim"
else
    echo "⚠️  Manim is not detected in your current PATH or Python environment."
    echo "👉 Install Manim Community Edition:"
    echo "    pip install manim"
    echo "    sudo apt install ffmpeg libpango1.0-dev (Linux dependencies)"
    exit 127
fi

echo "🎬 Rendering Manim scene..."
echo "   Script:  $SCRIPT_FILE"
echo "   Scene:   ${SCENE_NAME:-[All / Default]}"
echo "   Quality: $QUALITY_FLAG $SNAPSHOT_FLAG"

RENDER_CMD=($MANIM_CMD $QUALITY_FLAG $SNAPSHOT_FLAG "$SCRIPT_FILE")
if [[ -n "$SCENE_NAME" ]]; then
    RENDER_CMD+=("$SCENE_NAME")
fi

echo "⚙️  Executing: ${RENDER_CMD[*]}"
"${RENDER_CMD[@]}"

echo "✅ Render completed successfully."
