#!/usr/bin/env bash
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
if [[ -f "$DIR/ImplicitDifferentiationScene.mp4" ]]; then
    mpv --title="MA1101 - Turunan Implisit" --loop-file=inf "$DIR/ImplicitDifferentiationScene.mp4"
else
    mpv --title="MA1101 - Turunan Implisit" --loop-file=inf "$DIR/ImplicitDifferentiationScene.ogv"
fi
