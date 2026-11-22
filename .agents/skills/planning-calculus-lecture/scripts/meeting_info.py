#!/usr/bin/env python3
"""
meeting_info.py - read one meeting (pertemuan) from the MA1101 syllabus spreadsheet.

Uses only the standard library (zipfile + xml), because openpyxl is not installed
in this workspace. Handles both inline strings and shared strings.

Usage:
  python3 meeting_info.py 27                 # one meeting
  python3 meeting_info.py --all              # every meeting, one line each
  python3 meeting_info.py 27 --xlsx <path>   # another syllabus file

Default file: 2026/Silabus_MA1101_Matematika_I_2026_2027.xlsx (relative to the
repository root, found by walking up from this script).

Output (one meeting): pekan, pertemuan, hari, tanggal, bab, subtopics [(code, title)],
catatan, kind (lecture | review | exam), and n_subtopics. Use n_subtopics to pick
the agenda template: 2 -> full arc + compressed arc, 1 -> full arc + practice.
"""

import argparse
import json
import re
import sys
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path

NS = {"m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
M = "{%s}" % NS["m"]


def repo_root() -> Path:
    p = Path(__file__).resolve()
    for parent in p.parents:
        if (parent / "AGENTS.md").exists() and (parent / "2026").is_dir():
            return parent
    return Path.cwd()


def read_rows(xlsx: Path, sheet_name: str = "Jadwal Perkuliahan"):
    z = zipfile.ZipFile(xlsx)
    shared = []
    if "xl/sharedStrings.xml" in z.namelist():
        sst = ET.fromstring(z.read("xl/sharedStrings.xml"))
        shared = ["".join(t.text or "" for t in si.iter(M + "t")) for si in sst.findall("m:si", NS)]
    wb = ET.fromstring(z.read("xl/workbook.xml"))
    names = [s.get("name") for s in wb.find("m:sheets", NS)]
    idx = names.index(sheet_name) + 1 if sheet_name in names else 1
    sh = ET.fromstring(z.read(f"xl/worksheets/sheet{idx}.xml"))
    rows = []
    for r in sh.iter(M + "row"):
        cells = {}
        for c in r:
            col = re.match(r"[A-Z]+", c.get("r")).group(0)
            t, v, is_ = c.get("t"), c.find("m:v", NS), c.find("m:is", NS)
            if is_ is not None:
                txt = "".join(x.text or "" for x in is_.iter(M + "t"))
            elif t == "s" and v is not None:
                txt = shared[int(v.text)]
            else:
                txt = v.text if v is not None else ""
            cells[col] = (txt or "").strip()
        rows.append(cells)
    return rows


def parse_subtopics(cell: str):
    out = []
    for part in re.split(r";\s*", cell):
        m = re.match(r"(\d+\.\d+)\.?\s*(.+)", part.strip())
        if m:
            out.append((m.group(1), m.group(2).strip()))
    return out


def meetings(xlsx: Path):
    rows = read_rows(xlsx)
    header_i = next(i for i, r in enumerate(rows) if r.get("B", "").lower().startswith("pertemuan"))
    out = []
    for r in rows[header_i + 1:]:
        if not r.get("B", "").isdigit():
            continue
        sub_cell = r.get("F", "")
        text = (r.get("E", "") + " " + sub_cell).lower()
        kind = "review" if "telaah" in text else ("exam" if re.search(r"\b(uts|uas)\b", text) and not parse_subtopics(sub_cell) else "lecture")
        subs = parse_subtopics(sub_cell)
        out.append(dict(pekan=int(r.get("A") or 0), pertemuan=int(r["B"]), hari=r.get("C", ""),
                        tanggal=r.get("D", ""), bab=r.get("E", ""), subtopics=subs,
                        catatan=r.get("G", ""), kind=kind, n_subtopics=len(subs)))
    return out


def main():
    ap = argparse.ArgumentParser(description="Read one MA1101 meeting from the syllabus xlsx")
    ap.add_argument("meeting", nargs="?", type=int)
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--xlsx", default="")
    a = ap.parse_args()
    xlsx = Path(a.xlsx) if a.xlsx else repo_root() / "2026" / "Silabus_MA1101_Matematika_I_2026_2027.xlsx"
    if not xlsx.exists():
        sys.exit(f"syllabus not found: {xlsx}")
    ms = meetings(xlsx)
    if a.all or a.meeting is None:
        for m in ms:
            codes = ", ".join(c for c, _ in m["subtopics"]) or "-"
            print(f"{m['pertemuan']:>2}  {m['hari']:<6} {m['tanggal']:<12} {m['kind']:<7} {codes}")
        return
    hit = [m for m in ms if m["pertemuan"] == a.meeting]
    if not hit:
        sys.exit(f"meeting {a.meeting} not in syllabus (has {len(ms)} meetings)")
    print(json.dumps(hit[0], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
