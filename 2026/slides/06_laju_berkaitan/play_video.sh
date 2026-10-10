#!/usr/bin/env bash
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
if [[ -f "$DIR/SlidingLadderScene.mp4" ]]; then
    mpv --title="MA1101 - Tangga Meluncur" --loop-file=inf "$DIR/SlidingLadderScene.mp4"
else
    mpv --title="MA1101 - Tangga Meluncur" --loop-file=inf "$DIR/SlidingLadderScene.ogv"
fi
