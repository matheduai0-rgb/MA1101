#!/usr/bin/env bash
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
if [[ -f "$DIR/DifferentialsApproximationScene.mp4" ]]; then
    mpv --title="MA1101 - Diferensial dan Hampiran" --loop-file=inf "$DIR/DifferentialsApproximationScene.mp4"
else
    mpv --title="MA1101 - Diferensial dan Hampiran" --loop-file=inf "$DIR/DifferentialsApproximationScene.ogv"
fi
