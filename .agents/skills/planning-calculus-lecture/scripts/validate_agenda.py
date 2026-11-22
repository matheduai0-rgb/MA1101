#!/usr/bin/env python3
"""
validate_agenda.py - check an MA1101 lecture agenda (agenda.toml) before slides are written.

The agenda format is TOML because Python's standard library reads it (tomllib) and
PyYAML is not installed in this workspace. Schema: references/agenda_schema.md.

Usage:
  python3 validate_agenda.py <agenda.toml>

Errors (exit 1) mean the agenda cannot drive a lecture as written. Warnings are
prompts to reconsider. Every message says what to change.
"""

import re
import sys
import tomllib
from pathlib import Path

PRIVATE = re.compile(r"(/K\d+/|/Ujian/|/2025/|Daftar Peserta|Pembagian Kelompok|nilai|kunci)", re.I)
NIM = re.compile(r"\b1\d{7}\b")  # ITB student numbers are 8 digits
OBSERVABLE = ("menghitung", "menentukan", "menjelaskan", "menurunkan", "mengintegralkan", "membuktikan",
              "menggambar", "memeriksa", "menyelesaikan", "membandingkan", "memodelkan", "mengenali",
              "menafsirkan", "menaksir", "menyusun", "mencari", "menuliskan", "membedakan", "menerapkan",
              "menggunakan", "mengubah", "memilih", "menunjukkan", "mendiagnosis", "membuat sketsa")
VAGUE = ("memahami", "mengetahui", "mengerti", "mengenal konsep")
STUDENT_MODES = ("pikir", "diskusi", "kerjakan", "angkat jari", "tulis", "tunjuk", "coba", "pasangan", "kuis")
TEMPLATES = {"two-subchapter": 2, "one-subchapter": 1, "review": 0}


def default_student_minutes(mode: str, mins: float) -> float:
    """Minutes students spend working in a segment when 'student_minutes' is not given.
    A segment usually holds two or three such moments, so the chip's duration is
    counted for about half the segment, never more than the segment itself."""
    m = mode.lower()
    if not any(w in m for w in STUDENT_MODES):
        return 0.0
    num = re.search(r"(\d+(?:[.,]\d+)?)\s*(dtk|detik|mnt|menit)", m)
    dur = float(num.group(1).replace(",", ".")) / (60 if num and num.group(2).startswith("d") else 1) if num else 1.0
    if "angkat jari" in m or "tunjuk" in m:
        dur = 1.0
    return min(mins, max(dur * 2, 0.4 * mins))


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    path = Path(sys.argv[1])
    if PRIVATE.search(str(path.resolve())):
        sys.exit(f"refusing to read {path}: the path looks like a roster, grade, exam or key location.")
    raw = path.read_text(encoding="utf-8")
    try:
        ag = tomllib.loads(raw)
    except tomllib.TOMLDecodeError as e:
        sys.exit(f"ERROR  {path} is not valid TOML: {e}. Strings need double quotes; lists use [ ].")
    errors, warns = [], []

    if NIM.search(raw):
        errors.append("the agenda contains what looks like a student number (8 digits starting with 1). "
                      "Agendas hold no student data; remove it.")

    for key in ("meeting", "slot_minutes", "template"):
        if key not in ag:
            errors.append(f"missing top-level key '{key}'. See references/agenda_schema.md.")
    slot = ag.get("slot_minutes", 100)
    buffer = ag.get("buffer_minutes", 5)
    tpl = ag.get("template", "")
    if tpl and tpl not in TEMPLATES:
        errors.append(f"template '{tpl}' unknown; use one of {', '.join(TEMPLATES)}.")

    subs = ag.get("subchapter", [])
    codes = [s.get("code", "") for s in subs]
    if tpl in TEMPLATES and tpl != "review" and len(subs) != TEMPLATES[tpl]:
        errors.append(f"template '{tpl}' expects {TEMPLATES[tpl]} [[subchapter]] table(s), found {len(subs)}.")
    misconceptions = []
    for s in subs:
        c = s.get("code", "?")
        for key in ("code", "title", "goal", "big_question"):
            if not s.get(key):
                errors.append(f"subchapter {c}: missing '{key}'.")
        goal = s.get("goal", "").lower()
        if goal and any(v in goal for v in VAGUE):
            warns.append(f"subchapter {c}: goal uses a verb you cannot observe ('{next(v for v in VAGUE if v in goal)}'). "
                         f"Say what students will do, e.g. 'menghitung (f⁻¹)′(b) tanpa rumus invers'.")
        elif goal and not any(v in goal for v in OBSERVABLE):
            warns.append(f"subchapter {c}: goal has no observable verb (menghitung, menentukan, menjelaskan, ...).")
        if s.get("big_question") and not s["big_question"].rstrip().endswith("?"):
            warns.append(f"subchapter {c}: big_question should be a question (end with '?').")
        ms = s.get("misconceptions", [])
        if not ms:
            warns.append(f"subchapter {c}: no misconceptions listed; pick one or two from question-craft.md's bank.")
        if not s.get("purcell"):
            warns.append(f"subchapter {c}: no Purcell section ('purcell'); cite the textbook section the lecturer uses.")
        misconceptions += [(c, m) for m in ms]

    segs = ag.get("segment", [])
    if not segs:
        errors.append("no [[segment]] tables: the agenda needs timed segments.")
    total = 0.0
    student = 0.0
    for k, seg in enumerate(segs, start=1):
        name = seg.get("name", f"segment {k}")
        mins = seg.get("minutes")
        if not isinstance(mins, (int, float)) or mins <= 0:
            errors.append(f"segment '{name}': 'minutes' must be a positive number.")
            continue
        total += mins
        stage = seg.get("stage")
        if stage is not None and not (isinstance(stage, int) and 0 <= stage <= 10):
            errors.append(f"segment '{name}': stage {stage!r} must be 0–10 (0 = buffer/admin, 1–10 = arc stage).")
        if seg.get("subchapter") and seg["subchapter"] not in codes:
            errors.append(f"segment '{name}': subchapter '{seg['subchapter']}' is not one of {codes}.")
        default = default_student_minutes(seg.get("mode", ""), mins)
        if seg.get("stage") in (8, 9):  # half-finished / independent practice: students work most of it
            default = max(default, 0.8 * mins)
        student += min(mins, seg.get("student_minutes", default))
        if mins > 15:
            warns.append(f"segment '{name}' is {mins} min; split it so the room responds at least every ~10–12 min.")

    limit = slot - buffer
    if total > limit:
        over = total - limit
        cuts = [s.get("name") for s in segs if s.get("cut")]
        errors.append(f"segments sum to {total:g} min, over the {slot:g}-min slot minus {buffer:g} min buffer by {over:g} min. "
                      f"Shorten or drop: {', '.join(cuts) if cuts else 'mark cut-able segments with cut = true first'}.")
    elif total < 0.85 * slot:
        warns.append(f"segments sum to only {total:g} of {slot:g} min; add a practice block or a second applet.")
    if total and student / total < 0.5:
        warns.append(f"only {student / total:.0%} of planned time has students working (mode with pikir/diskusi/kerjakan/...). "
                     f"Equity gains appear at high active-learning intensity; aim for 55–65%.")

    cuts = [s for s in segs if s.get("cut")]
    if len(cuts) < 2:
        errors.append(f"{len(cuts)} cut-able segment(s); mark at least 2 with cut = true so the run-sheet has cut-points "
                      f"when the lecture runs late (never the hook, the worked example, or the exit ticket).")
    for s in cuts:
        if s.get("stage") in (1, 7, 10):
            warns.append(f"segment '{s.get('name')}' is stage {s['stage']} but marked cut-able; keep hook (1), "
                         f"worked example (7) and exit (10), cut elsewhere.")

    if segs and segs[0].get("stage") not in (1, 0):
        warns.append("the first segment is not the big question (stage 1).")
    if segs and segs[-1].get("stage") != 10:
        errors.append("the last segment must be the exit ticket / bridge question (stage 10).")

    targeted = " ".join(" ".join(s.get("targets", [])) for s in segs).lower()
    for c, m in misconceptions:
        key = m.lower()[:40]
        if key not in targeted:
            errors.append(f"misconception '{m}' ({c}) is not targeted by any segment; add it to the 'targets' list of the "
                          f"'Apakah Ini Benar?' segment (stage 6) or a predict segment (stage 3).")

    et = ag.get("exit_ticket", {})
    if not et:
        errors.append("missing [exit_ticket] table (prompt, goal, bridge).")
    else:
        if et.get("goal") not in codes:
            errors.append(f"exit_ticket.goal '{et.get('goal')}' must name a subchapter code from {codes}, so the ticket checks a goal.")
        for key in ("prompt", "bridge"):
            if not et.get(key):
                errors.append(f"exit_ticket: missing '{key}'.")

    print(f"\n== Agenda check: {path} ==")
    print(f"meeting {ag.get('meeting', '?')}, {tpl or '?'}, {len(segs)} segments, {total:g}/{slot:g} min "
          f"(buffer {buffer:g}), student work {student / total:.0%}" if total else "")
    for e in errors:
        print(f"  ERROR  {e}")
    for w in warns:
        print(f"  warn   {w}")
    print("\nRESULT: " + ("PASS" if not errors else f"FAIL ({len(errors)} error(s))") + "\n")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
