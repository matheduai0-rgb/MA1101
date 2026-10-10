#!/usr/bin/env bash
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
if [[ -f "$DIR/MaximumMinimumScene.mp4" ]]; then
    mpv --title="MA1101 - Maksimum dan Minimum" --loop-file=inf "$DIR/MaximumMinimumScene.mp4"
else
    mpv --title="MA1101 - Maksimum dan Minimum" --loop-file=inf "$DIR/MaximumMinimumScene.ogv"
fi
