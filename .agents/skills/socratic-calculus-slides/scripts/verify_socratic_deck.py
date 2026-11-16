#!/usr/bin/env python3
"""
verify_socratic_deck.py - structure + render check for Socratic Slidev decks.

Two passes over one slides.md:

  1. STRUCTURE (static, instant). Does the deck actually teach by questioning?
     Hook question up front, a question tied to every applet, presenter notes on
     every question slide, Polya phases, support that fades full -> partial ->
     independent, a hint ladder, an exit reflection.

  2. RENDER (headless Chromium via Playwright). Each slide is opened in its
     fully revealed state (?clicks=99), which is the tallest state and the one
     that overflows, and in its initial state, which must not leak answers.
     Checks: content inside the slide frame, no KaTeX errors, no raw LaTeX left
     as text, JSXGraph boards mounted, no answer/hint visible before a click.
     Writes slide-NN.png and slide-NN-revealed.png for visual review.

Usage:
  python3 verify_socratic_deck.py <slides.md> [--scope deck|segment]
                                  [--png <dir>] [--port N] [--no-render]

  --scope deck     (default) a full lecture deck: every structure rule applies.
  --scope segment  a few slides (one worked example, one applet): only the
                   per-slide rules apply, not the whole-lecture arc.

Exit code 0 when there are no errors. Warnings never fail the run.
"""

import argparse
import json
import os
import re
import signal
import socket
import subprocess
import sys
import time
from pathlib import Path

ASKING = ("question", "predict", "pitfall", "reflect")


# ----------------------------------------------------------------------------
# Static structure pass
# ----------------------------------------------------------------------------

def split_slides(text: str):
    """Split a Slidev markdown file into slide bodies (frontmatter removed)."""
    lines = text.splitlines()
    chunks, cur, in_fence = [], [], False
    for ln in lines:
        if ln.lstrip().startswith("```"):
            in_fence = not in_fence
        if not in_fence and re.fullmatch(r"---\s*", ln):
            chunks.append(cur)
            cur = []
        else:
            cur.append(ln)
    chunks.append(cur)

    def is_frontmatter(chunk):
        body = [l for l in chunk if l.strip()]
        if not body:
            return False
        return all(re.match(r"^(\s+\S|[\w-]+\s*:|#)", l) and not l.startswith("# ") for l in body)

    slides, i = [], 0
    if chunks and not any(l.strip() for l in chunks[0]):
        i = 1  # file starts with '---' (headmatter opener)
    while i < len(chunks):
        if is_frontmatter(chunks[i]) and i + 1 < len(chunks):
            i += 1
        slides.append("\n".join(chunks[i]))
        i += 1
    return [s for s in slides if s.strip()]


def note_of(slide: str) -> str:
    m = re.search(r"<!--(.*?)-->\s*$", slide, re.S)
    return m.group(1).strip() if m else ""


def blocks_of(slide: str):
    """Return [(type, attrs_string)] for each SocraticBlock tag in the slide."""
    out = []
    for m in re.finditer(r"<SocraticBlock\b([^>]*)>", slide):
        attrs = m.group(1)
        t = re.search(r'\btype="(\w+)"', attrs)
        out.append((t.group(1) if t else "question", attrs))
    return out


def steppers_of(slide: str):
    out = []
    for m in re.finditer(r"<PolyaStepper\b([^>]*)/?>", slide):
        attrs = m.group(1)
        step = re.search(r'\bstep="([\d\s-]+)"', attrs)
        sup = re.search(r'\bsupport="(\w+)"', attrs)
        nums = [int(n) for n in re.findall(r"\d", step.group(1))] if step else [1]
        lo, hi = nums[0], nums[-1]
        ph = re.search(r'phases="(\d)"', attrs)
        out.append((set(range(lo, hi + 1)), sup.group(1) if sup else "full", int(ph.group(1)) if ph else 4))
    return out


def has_applet(slide: str) -> bool:
    return bool(re.search(r"<(JSXGraphBoard|Calc\w+|\w+Board)\b", slide))


def structure_pass(text: str, scope: str):
    errors, warnings = [], []
    slides = split_slides(text)
    n = len(slides)
    info = [dict(blocks=blocks_of(s), steppers=steppers_of(s), note=note_of(s), applet=has_applet(s)) for s in slides]

    def asks(i):
        return any(t in ASKING for t, _ in info[i]["blocks"])

    # --- per-slide rules (always) ---
    for i, (s, d) in enumerate(zip(slides, info), start=1):
        if asks(i - 1) and len(d["note"]) < 40:
            errors.append(f"slide {i}: poses a question but has no presenter note. The lecturer needs the "
                          f"expected answer and a follow-up for a wrong answer or silence (trailing <!-- --> block).")
        if d["applet"]:
            near = asks(i - 1) or (i >= 2 and asks(i - 2))
            if not near:
                errors.append(f"slide {i}: applet with no question attached. Put a predict/question block on "
                              f"this slide or the one before, so students watch the applet looking for something.")
            elif not any(t == "predict" for t, _ in d["blocks"]) and not (i >= 2 and any(t == "predict" for t, _ in info[i - 2]["blocks"])):
                warnings.append(f"slide {i}: applet has a question but no predict block; a committed guess makes the reveal land.")
        levels = [int(m) for t, a in d["blocks"] if t == "hint" for m in re.findall(r'\blevel="?(\d)', a)]
        if levels and levels != sorted(levels):
            errors.append(f"slide {i}: hint levels are out of order {levels}; a ladder goes 1, 2, 3.")
        for m in re.finditer(r"^\$\$[^\n$]+$", s, re.M):
            if not m.group(0).rstrip().endswith("$$"):
                errors.append(f"slide {i}: multi-line display math must have each $$ on its own line "
                              f"(found '{m.group(0)[:30]}...'); otherwise it renders as raw LaTeX.")
        n_ask = sum(1 for t, _ in d["blocks"] if t in ("question", "predict", "pitfall"))
        if n_ask > 3:
            warnings.append(f"slide {i}: {n_ask} questions on one slide. Each needs wait time; consider splitting.")

    if scope == "segment":
        return errors, warnings, n

    # --- whole-lecture arc (scope == deck) ---
    if n < 6:
        warnings.append(f"deck has only {n} slides; if this is a fragment, run with --scope segment.")
    if not any(asks(i) for i in range(min(2, n))):
        errors.append("no hook: neither of the first two slides poses a question. Open with a problem the "
                      "students can attempt before any definition is shown.")
    first_ask = next((i for i in range(n) if asks(i)), None)
    first_formal = next((i for i, s in enumerate(slides)
                         if re.search(r'<BeamerBlock[^>]*title="[^"]*(Definisi|Teorema|Rumus|Aturan|Sifat)', s)), None)
    if first_formal is not None and (first_ask is None or first_formal < first_ask):
        errors.append(f"slide {first_formal + 1}: a definition/theorem appears before any question has been asked.")

    content = max(1, n - 1)
    ratio = sum(1 for i in range(1, n) if asks(i)) / content
    if ratio < 0.6:
        warnings.append(f"only {ratio:.0%} of content slides pose a question (aim for most of them).")

    seen = {}
    for i, d in enumerate(info):
        for steps, sup, _ in d["steppers"]:
            seen.setdefault(sup, dict(first=i, steps=set()))["steps"] |= steps
    n_phases = min([ph for d in info for _, _, ph in d["steppers"]] or [4])
    required = set(range(1, n_phases + 1))
    for sup, label in (("full", "worked example"), ("partial", "half-finished example"), ("independent", "independent problem")):
        if sup not in seen:
            errors.append(f'no {label}: missing <PolyaStepper support="{sup}">. Support should fade full -> partial -> independent.')
    if "full" in seen and not required <= seen["full"]["steps"]:
        missing = sorted(required - seen["full"]["steps"])
        errors.append(f"worked example does not cover Polya phase(s) {missing} (1 Pahami, 2 Rencanakan, 3 Laksanakan, 4 Periksa Kembali).")
    order = [seen[k]["first"] for k in ("full", "partial", "independent") if k in seen]
    if order != sorted(order):
        errors.append("support does not fade in order: the worked example must come before the half-finished one, which comes before the independent problem.")
    indep = [i for i, d in enumerate(info) if any(sup == "independent" for _, sup, _ in d["steppers"])]
    if indep:
        hints = sum(1 for i in indep for t, _ in info[i]["blocks"] if t == "hint")
        if hints < 2:
            errors.append(f"independent problem (slide {indep[0] + 1}) has {hints} hint(s); give a ladder of at least two, ideally three.")
    if not any(t == "pitfall" for d in info for t, _ in d["blocks"]):
        warnings.append("no pitfall block: one 'Benarkah?' slide diagnosing a common misconception is usually worth its time.")
    if not any(t == "reflect" for d in info[-2:] for t, _ in d["blocks"]):
        errors.append("no exit reflection: one of the last two slides should carry a reflect block (tiket keluar).")
    return errors, warnings, n


# ----------------------------------------------------------------------------
# Render pass
# ----------------------------------------------------------------------------

NODE_AUDIT = r"""
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');
(async () => {
  const base = process.env.SQ_URL, out = process.env.SQ_PNG || '';
  const exe = process.env.SQ_CHROME;
  const browser = await chromium.launch({ executablePath: exe && fs.existsSync(exe) ? exe : undefined, headless: true, args: ['--no-sandbox', '--disable-gpu'] });
  const page = await browser.newPage({ viewport: { width: 1280, height: 720 } });
  const consoleErrors = [];
  page.on('pageerror', e => consoleErrors.push(String(e.message).slice(0, 200)));
  const open = async (n, clicks) => {
    await page.goto(`${base}/${n}${clicks ? '?clicks=99' : ''}`, { waitUntil: 'load' });
    await page.waitForSelector(`.slidev-page-${n}`, { timeout: 30000 });
    await page.waitForTimeout(900);
    if (await page.$(`.slidev-page-${n} .jxgbox`)) await page.waitForTimeout(900);
  };
  await open(1, false);
  const total = await page.evaluate(() => (window.__slidev__ && window.__slidev__.nav.total) || 1);
  if (out) fs.mkdirSync(out, { recursive: true });
  const results = [];
  for (let n = 1; n <= total; n++) {
    const pad = String(n).padStart(2, '0');
    await open(n, false);
    const initial = await page.evaluate((n) => {
      const pg = document.querySelector(`.slidev-page-${n}`);
      const leaks = [...pg.querySelectorAll('.sq-answer, .sq-hint')]
        .filter(el => !el.closest('.slidev-vclick-hidden'))
        .map(el => (el.querySelector('.sq-title')?.textContent || el.className).trim());
      const nav = window.__slidev__ && window.__slidev__.nav;
      const themed = getComputedStyle(pg.querySelector('.slidev-layout') || pg).backgroundColor;
      return { leaks, clicksTotal: nav ? nav.clicksTotal : 0, bg: themed };
    }, n);
    if (out) await page.screenshot({ path: path.join(out, `slide-${pad}.png`) });
    await open(n, true);
    const full = await page.evaluate((n) => {
      const pg = document.querySelector(`.slidev-page-${n}`);
      const frame = pg.getBoundingClientRect();
      const clipped = [];
      pg.querySelectorAll('h1, h2, h3, p, li, table, svg, img, .sq, .polya, .b-block, .b-example, .b-alert, .jxgbox, .katex-display').forEach(el => {
        const r = el.getBoundingClientRect();
        if (!r.width && !r.height) return;
        const over = Math.max(r.bottom - frame.bottom, r.right - frame.right, frame.top - r.top, frame.left - r.left);
        if (over > 3) clipped.push({ px: Math.round(over), what: (el.className || el.tagName).toString().slice(0, 30), text: (el.textContent || '').trim().replace(/\s+/g, ' ').slice(0, 50) });
      });
      const walker = document.createTreeWalker(pg, NodeFilter.SHOW_TEXT);
      const raw = [];
      while (walker.nextNode()) {
        const t = walker.currentNode;
        const host = t.parentElement;
        if (!host || host.closest('.katex, script, style, .jxgbox, code, pre')) continue;
        if (/\$\$|\\(begin|end|frac|lim|int|sum|sqrt|boxed|left|right)\b/.test(t.textContent)) raw.push(t.textContent.trim().slice(0, 60));
      }
      const katexErrors = [...pg.querySelectorAll('.katex-error')].map(e => (e.textContent || '').slice(0, 60));
      const boards = [...pg.querySelectorAll('.jxgbox')].map(b => { const s = b.querySelector('svg'); return !!s && s.getBoundingClientRect().width > 0; });
      const stillHidden = pg.querySelectorAll('.slidev-vclick-hidden').length;
      return { clipped, raw, katexErrors, boards, stillHidden };
    }, n);
    if (out && initial.clicksTotal > 0) await page.screenshot({ path: path.join(out, `slide-${pad}-revealed.png`) });
    results.push({ n, ...initial, ...full });
  }
  await browser.close();
  console.log(JSON.stringify({ total, results, consoleErrors }));
})().catch(e => { console.log(JSON.stringify({ fatal: String(e) })); process.exit(1); });
"""


def port_open(port: int) -> bool:
    for host in ("127.0.0.1", "::1"):
        fam = socket.AF_INET6 if ":" in host else socket.AF_INET
        try:
            with socket.socket(fam, socket.SOCK_STREAM) as s:
                s.settimeout(0.3)
                if s.connect_ex((host, port)) == 0:
                    return True
        except OSError:
            pass
    return False


def render_pass(slides_file: Path, port: int, png_dir: str, chrome: str):
    root = next((p for p in [slides_file.parent, *slides_file.parents] if (p / "package.json").exists()), slides_file.parent)
    if not port:
        port = next(p for p in range(3350, 3600) if not port_open(p))
    elif port_open(port):
        return [f"port {port} is already in use; a server there may be showing a different deck. Omit --port to pick a free one."], [], 0
    errors, warnings = [], []
    if not (slides_file.parent / "styles").exists():
        errors.append(f"{slides_file.parent}/styles is missing, so the dark theme will not load and BeamerBlocks render unstyled on white. "
                      f"Symlink or copy the repo's styles/ folder next to slides.md.")
    proc = subprocess.Popen(["npx", "slidev", str(slides_file), "--port", str(port), "--no-open"], cwd=str(root),
                            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, start_new_session=True)
    try:
        t0 = time.time()
        while time.time() - t0 < 60 and not port_open(port):
            time.sleep(0.5)
        if not port_open(port):
            return errors + [f"Slidev did not start on port {port} within 60s (run `npx slidev {slides_file}` to see why)."], warnings, 0
        time.sleep(1.5)
        env = dict(os.environ, SQ_URL=f"http://localhost:{port}", SQ_PNG=str(Path(png_dir).resolve()) if png_dir else "", SQ_CHROME=chrome)
        res = subprocess.run(["node", "-e", NODE_AUDIT], cwd=str(root), env=env, capture_output=True, text=True, timeout=600)
    finally:
        try:
            os.killpg(os.getpgid(proc.pid), signal.SIGTERM)
        except ProcessLookupError:
            pass
    try:
        data = json.loads(res.stdout.strip().splitlines()[-1])
    except (ValueError, IndexError):
        return errors + [f"render audit produced no result. stderr: {res.stderr.strip()[:400]}"], warnings, 0
    if "fatal" in data:
        return errors + [f"render audit crashed: {data['fatal'][:400]}"], warnings, 0

    for r in data["results"]:
        n = r["n"]
        for c in r["clipped"][:4]:
            errors.append(f"slide {n}: content runs {c['px']}px outside the frame when fully revealed [{c['what']}] \"{c['text']}\". "
                          f"Hidden v-click content still takes space: shorten, add class slide-compact, or split the slide.")
        for t in r["raw"][:3]:
            errors.append(f"slide {n}: raw LaTeX shown as text: \"{t}\". Usual causes: $$ not on its own line, or math inside a raw HTML block without blank lines.")
        for t in r["katexErrors"][:3]:
            errors.append(f"slide {n}: KaTeX error: {t}")
        for k, ok in enumerate(r["boards"], start=1):
            if not ok:
                errors.append(f"slide {n}: JSXGraph board #{k} did not mount (check the :init function for a JS error).")
        for leak in r["leaks"]:
            errors.append(f"slide {n}: \"{leak}\" is visible before any click. Answers and hints need v-click so the question gets its wait time.")
    if data["results"] and data["results"][0]["bg"] in ("rgba(0, 0, 0, 0)", "rgb(255, 255, 255)"):
        errors.append("slides render on a white/transparent background: styles/index.css is not being loaded.")
    for e in data.get("consoleErrors", [])[:5]:
        warnings.append(f"browser error: {e}")
    return errors, warnings, data["total"]


def main():
    ap = argparse.ArgumentParser(description="Structure + render check for Socratic Slidev decks")
    ap.add_argument("slides")
    ap.add_argument("--scope", choices=("deck", "segment"), default="deck")
    ap.add_argument("--png", default="", help="directory for slide-NN.png / slide-NN-revealed.png")
    ap.add_argument("--port", type=int, default=0, help="port for the temporary Slidev server (default: first free port from 3350)")
    ap.add_argument("--no-render", action="store_true", help="structure pass only")
    ap.add_argument("--chrome", default="/usr/bin/chromium")
    a = ap.parse_args()

    f = Path(a.slides).resolve()
    if not f.exists():
        sys.exit(f"not found: {f}")
    s_err, s_warn, n = structure_pass(f.read_text(encoding="utf-8"), a.scope)
    r_err, r_warn, rendered = ([], [], 0) if a.no_render else render_pass(f, a.port, a.png, a.chrome)

    print(f"\n== Socratic deck check: {f.name} ({n} slides, scope={a.scope}) ==")
    for title, errs, warns in (("STRUCTURE", s_err, s_warn), ("RENDER" + ("" if not a.no_render else " (skipped)"), r_err, r_warn)):
        print(f"\n[{title}] {len(errs)} error(s), {len(warns)} warning(s)")
        for e in errs:
            print(f"  ERROR  {e}")
        for w in warns:
            print(f"  warn   {w}")
    if not a.no_render and rendered and rendered != n:
        print(f"\n  warn   structure pass counted {n} slides but Slidev rendered {rendered}; check the '---' separators.")
    if a.png and not a.no_render:
        print(f"\nScreenshots: {Path(a.png).resolve()}  (look at them: a passing check does not mean a readable slide)")
    total = len(s_err) + len(r_err)
    print("\nRESULT: " + ("PASS" if total == 0 else f"FAIL ({total} error(s))") + "\n")
    sys.exit(0 if total == 0 else 1)


if __name__ == "__main__":
    main()
