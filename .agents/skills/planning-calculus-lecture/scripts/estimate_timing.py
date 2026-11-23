#!/usr/bin/env python3
"""
estimate_timing.py - estimate how many minutes a Socratic Slidev deck takes in class.

Reads slides.md, prices each slide with the constants in references/timing_model.md,
and compares the total with the meeting slot (default 100 minutes) and, if given,
with the segment budgets of an agenda.toml.

Usage:
  python3 estimate_timing.py <slides.md> [--slot 100] [--agenda agenda.toml] [--json]

A meeting split over two decks keeps one agenda; its segments write slides as
"35:2-4" (deck number prefix), and only the segments of the deck being timed are compared.

Slide boundaries come from split_slides() in the socratic skill's verifier, imported
by path, so both tools always agree on slide numbers.

These are estimates of room time, not measurements. Calibrate the constants with
retro.md actuals (see SKILL.md, post-class mode).
"""

import argparse
import importlib.util
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
VERIFIER = HERE.parents[1] / "socratic-calculus-slides" / "scripts" / "verify_socratic_deck.py"

# ---- constants (minutes); keep in sync with references/timing_model.md ----
BASE_SLIDE = 1.0          # lecturer talk, reading the slide, transition
TITLE_SLIDE = 1.5         # big question posed and left open
NO_MODE_QUESTION = 0.75   # a question with no response-mode chip
POLL = 1.0                # "Angkat jari: A / B / C", "Tunjuk di papan"
DEBRIEF = 0.5             # added after a timed think
DISCUSS_DEBRIEF = 1.0     # added after pair or paper work
ANSWER_REVEAL = 0.5       # each answer block discussed
HINT_REVEAL = 0.5         # each hint revealed
APPLET = 2.0              # dragging, pausing at key states
FORMAL_BLOCK = 1.5        # BeamerBlock with Definisi/Teorema/Rumus/Aturan/Sifat
PARTITION_LINE = 1.0      # one PartitionStep line (Partisi / Hampiri / Jumlahkan) worked live
POLYA_EXTRA = {"full": 2.0, "partial": 2.0, "independent": 4.0}  # modelling / solving time beyond the blocks


def load_split_slides():
    if not VERIFIER.exists():
        sys.exit(f"cannot find the socratic verifier at {VERIFIER}")
    spec = importlib.util.spec_from_file_location("verify_socratic_deck", VERIFIER)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def mode_minutes(mode: str) -> float:
    m = mode.lower()
    num = re.search(r"(\d+(?:[.,]\d+)?)\s*(dtk|detik|mnt|menit)", m)
    dur = 0.0
    if num:
        dur = float(num.group(1).replace(",", "."))
        if num.group(2).startswith("d"):
            dur /= 60
    if "angkat jari" in m or "tunjuk" in m or "voting" in m:
        return POLL
    if "diskusi" in m or "kerjakan" in m or "tulis" in m:
        return (dur or 2.0) + DISCUSS_DEBRIEF
    if "pikir" in m:
        return (dur or 0.5) + DEBRIEF
    return NO_MODE_QUESTION


def price_slide(i: int, slide: str, mod, prev_supports=frozenset()):
    items = []
    base = TITLE_SLIDE if i == 1 else BASE_SLIDE
    items.append(("base", base))
    for t, attrs in mod.blocks_of(slide):
        mm = re.search(r'\bmode="([^"]*)"', attrs)
        if t in ("question", "predict", "pitfall", "reflect"):
            items.append((t, mode_minutes(mm.group(1)) if mm else NO_MODE_QUESTION))
        elif t == "answer":
            items.append(("answer", ANSWER_REVEAL))
        elif t == "hint":
            items.append(("hint", HINT_REVEAL))
    if mod.has_applet(slide):
        items.append(("applet", APPLET))
    for _ in re.finditer(r'<BeamerBlock[^>]*title="[^"]*(Definisi|Teorema|Rumus|Aturan|Sifat)', slide):
        items.append(("formal", FORMAL_BLOCK))
    for _ in re.finditer(r"<PartitionStep\b", slide):
        items.append(("partisi-line", PARTITION_LINE))
    for sup in {sup for _, sup, _ in mod.steppers_of(slide)} - set(prev_supports):
        # once per run of consecutive slides at the same support level
        items.append((f"polya-{sup}", POLYA_EXTRA.get(sup, 2.0)))
    title = re.search(r"^#{1,3}\s+(.+)$", slide, re.M) or re.search(r'class="slide-title">\s*<span>([^<]+)</span>', slide)
    return dict(slide=i, title=(title.group(1).strip() if title else "")[:48],
                minutes=round(sum(v for _, v in items), 1),
                parts=", ".join(f"{k} {v:g}" for k, v in items[1:]))


def estimate(slides_md: Path):
    mod = load_split_slides()
    slides = mod.split_slides(slides_md.read_text(encoding="utf-8"))
    rows, prev = [], frozenset()
    for i, s in enumerate(slides, start=1):
        rows.append(price_slide(i, s, mod, prev))
        prev = frozenset(sup for _, sup, _ in mod.steppers_of(s))
    return rows, round(sum(r["minutes"] for r in rows), 1)


def parse_range(r: str):
    nums = [int(x) for x in re.findall(r"\d+", str(r))]
    return range(nums[0], nums[-1] + 1) if nums else range(0)


def main():
    ap = argparse.ArgumentParser(description="Estimate class minutes for a Socratic Slidev deck")
    ap.add_argument("slides")
    ap.add_argument("--slot", type=float, default=100)
    ap.add_argument("--agenda", default="")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    rows, total = estimate(Path(a.slides))
    if a.json:
        print(json.dumps(dict(rows=rows, total=total, slot=a.slot), ensure_ascii=False))
        return
    print(f"\n== Timing estimate: {a.slides} ==\n")
    print(f"{'#':>3}  {'min':>5}  {'title':<48}  parts")
    for r in rows:
        print(f"{r['slide']:>3}  {r['minutes']:>5.1f}  {r['title']:<48}  {r['parts']}")
    print(f"\nTotal ≈ {total:.0f} min for a {a.slot:.0f}-min slot ({total / a.slot:.0%}).")
    if total > a.slot - 5:
        print(f"  warn  over budget: leave at least 5 min of buffer. Cut-able candidates are the slides with the largest "
              f"minutes above that are not the hook, the worked example, or the exit reflection.")
    if a.agenda:
        import tomllib
        ag = tomllib.loads(Path(a.agenda).read_text(encoding="utf-8"))
        by = {r["slide"]: r["minutes"] for r in rows}
        print("\nAgenda segments (budget vs estimate):")
        deck_no = re.match(r"(\d+)", Path(a.slides).resolve().parent.name)
        for seg in ag.get("segment", []):
            if "slides" not in seg:
                continue
            rng = str(seg["slides"])
            pref = re.match(r"\s*(\d+)\s*:(.*)", rng)
            if pref:  # "36:2-4" = slides 2-4 of deck 36; skip segments of the other deck
                if not deck_no or int(pref.group(1)) != int(deck_no.group(1)):
                    continue
                rng = pref.group(2)
            est = round(sum(by.get(k, 0) for k in parse_range(rng)), 1)
            flag = "  <- over" if est > seg.get("minutes", 0) + 2 else ""
            print(f"  {seg.get('name', '?'):<34} {seg.get('minutes', 0):>4} min budget  {est:>5.1f} est  (slides {seg['slides']}){flag}")
    print()


if __name__ == "__main__":
    main()
