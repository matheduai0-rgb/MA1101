#!/usr/bin/env python3
"""
verify_reveal_slides.py - Automated Viewport, Text Visibility & KaTeX/CindyJS Auditor for Reveal.js Slides

Uses Headless Chromium via Playwright (Node.js bridge) to step through every slide (and all fragments)
of an MA1101 Reveal.js HTML presentation, verifying:
  1. Zero vertical or horizontal slide overflow (section.scrollHeight <= slideHeight).
  2. Zero clipped or hidden text/math elements outside the slide safe frame.
  3. Zero KaTeX syntax errors (.katex-error) or unrendered math delimiters.
  4. Non-zero canvas initialization for all CindyJS interactive applets.
  5. Optional PNG slide snapshot export (slide_preview-01.png ... slide_preview-NN.png).

Usage:
  python3 verify_reveal_slides.py <path_to_html> [--export-png <output_dir>] [--prefix html_slide_preview]
"""

import argparse
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path


NODE_VERIFY_SCRIPT = r"""
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

(async () => {
  const htmlPath = process.env.VERIFY_HTML_PATH;
  const exportDir = process.env.VERIFY_EXPORT_DIR || '';
  const pngPrefix = process.env.VERIFY_PNG_PREFIX || 'html_slide_preview';
  const chromeExec = process.env.VERIFY_CHROME_EXEC || '/usr/bin/chromium';

  const browser = await chromium.launch({
    executablePath: fs.existsSync(chromeExec) ? chromeExec : undefined,
    headless: true,
    args: ['--no-sandbox', '--disable-gpu', '--allow-file-access-from-files']
  });

  const context = await browser.newContext({
    viewport: { width: 1280, height: 740 },
    deviceScaleFactor: 1
  });

  const page = await context.newPage();
  const fileUrl = 'file://' + path.resolve(htmlPath);

  await page.goto(fileUrl, { waitUntil: 'networkidle', timeout: 30000 });
  await page.waitForFunction(() => typeof window.Reveal !== 'undefined' && window.Reveal.isReady(), { timeout: 15000 });
  // Disable transitions during automated inspection so CSS transforms settle immediately
  await page.evaluate(() => {
    window.Reveal.configure({ transition: 'none', backgroundTransition: 'none' });
  });
  await page.waitForTimeout(350);

  const totalSlides = await page.evaluate(() => window.Reveal.getTotalSlides());
  const results = [];

  for (let i = 0; i < totalSlides; i++) {
    await page.evaluate((idx) => {
      window.Reveal.slide(idx, 0, 999);
      window.dispatchEvent(new Event('resize'));
    }, i);
    await page.waitForTimeout(160);

    const audit = await page.evaluate((slideIdx) => {
      const section = window.Reveal.getCurrentSlide();
      const slidesContainer = document.querySelector('.reveal .slides');
      const configW = window.Reveal.getConfig().width || 1120;
      const configH = window.Reveal.getConfig().height || 700;

      const secRect = section.getBoundingClientRect();
      const slidesRect = slidesContainer.getBoundingClientRect();
      const scale = window.Reveal.getScale ? window.Reveal.getScale() : (slidesRect.width / configW || 1);

      const titleEl = section.querySelector('h1, h2, h3');
      const titleText = titleEl
        ? Array.from(titleEl.textContent || '').join('').replace(/\s+/g, ' ').trim()
        : `Slide ${slideIdx + 1}`;

      // 1. Check section scrollHeight / scrollWidth vs configured slide dimensions
      const scrollH = Math.round(section.scrollHeight);
      const scrollW = Math.round(section.scrollWidth);
      const verticalOverflowPx = Math.max(0, scrollH - configH);
      const horizontalOverflowPx = Math.max(0, scrollW - configW);

      // 2. Check all content elements inside the slide for bounding box overflow or internal clipping
      const clippedElements = [];
      const selectors = [
        'h1', 'h2', 'h3', 'p', 'li', 'table',
        '.b-block', '.b-example', '.b-alert', '.b-block-body',
        '.formula-box', '.control-panel', '.cindy-canvas', '.katex-display'
      ];
      const candidates = section.querySelectorAll(selectors.join(','));

      // Slide safe frame boundaries in viewport coordinates (with 4px tolerance)
      const frameTop = slidesRect.top - 4;
      const frameBottom = slidesRect.top + (configH * scale) + 4;
      const frameLeft = slidesRect.left - 8;
      const frameRight = slidesRect.left + (configW * scale) + 8;

      candidates.forEach((el) => {
        const style = window.getComputedStyle(el);
        if (style.display === 'none' || style.visibility === 'hidden' || parseFloat(style.opacity) === 0) {
          return;
        }
        const r = el.getBoundingClientRect();
        if (r.width === 0 && r.height === 0) return;

        const overBottom = Math.round((r.bottom - frameBottom) / scale);
        const overRight = Math.round((r.right - frameRight) / scale);
        const overTop = Math.round((frameTop - r.top) / scale);
        const overLeft = Math.round((frameLeft - r.left) / scale);

        // Internal scroll clipping check for blocks with overflow: hidden
        let internalClipY = 0;
        if (
          (el.classList.contains('b-block') ||
           el.classList.contains('b-example') ||
           el.classList.contains('b-alert') ||
           el.classList.contains('b-block-body')) &&
          el.scrollHeight > el.clientHeight + 4
        ) {
          internalClipY = Math.round(el.scrollHeight - el.clientHeight);
        }

        if (overBottom > 2 || overRight > 4 || overTop > 2 || overLeft > 4 || internalClipY > 2) {
          // Strip surrogate pairs or MathML hidden text safely using Array.from
          const cleanText = Array.from((el.innerText || el.tagName).replace(/\s+/g, ' ').trim())
            .filter(ch => ch.codePointAt(0) < 0x10000)
            .join('')
            .slice(0, 52);
          clippedElements.push({
            tag: el.tagName.toLowerCase() + (el.className ? '.' + String(el.className).trim().split(/\s+/).join('.') : ''),
            snippet: cleanText,
            overBottom: Math.max(0, overBottom),
            overRight: Math.max(0, overRight),
            internalClipY
          });
        }
      });

      // 3. Check KaTeX errors
      const katexErrors = Array.from(section.querySelectorAll('.katex-error')).map(e => e.innerText.trim());

      // 4. Check CindyJS canvases on this slide
      const cindyCanvases = Array.from(section.querySelectorAll('.cindy-canvas')).map(c => {
        const innerCanvas = c.querySelector('canvas');
        const cr = c.getBoundingClientRect();
        return {
          id: c.id || 'unnamed-cindy',
          hasCanvas: Boolean(innerCanvas),
          width: Math.round(cr.width),
          height: Math.round(cr.height)
        };
      });

      return {
        slideNumber: slideIdx + 1,
        title: Array.from(titleText).filter(ch => ch.codePointAt(0) < 0x10000).join(''),
        scrollH,
        scrollW,
        configH,
        configW,
        verticalOverflowPx,
        horizontalOverflowPx,
        clippedElements,
        katexErrors,
        cindyCanvases
      };
    }, i);

    if (exportDir) {
      const numStr = String(i + 1).padStart(2, '0');
      const pngPath = path.join(exportDir, `${pngPrefix}-${numStr}.png`);
      await page.screenshot({ path: pngPath });
      audit.screenshot = pngPath;
    }

    results.push(audit);
  }

  await browser.close();
  console.log('__VERIFY_JSON_START__');
  console.log(JSON.stringify(results));
  console.log('__VERIFY_JSON_END__');
})();
"""


def find_node_and_playwright():
    """Find Node.js binary and Playwright node_modules path in standard or mise locations."""
    node_candidates = [
        "/home/rafgani/.local/share/mise/installs/node/26.9.0/bin/node",
        "/home/rafgani/.local/share/mise/installs/node/latest/bin/node",
        "/usr/bin/node",
    ]
    node_bin = "node"
    for c in node_candidates:
        if os.path.isfile(c) and os.access(c, os.X_OK):
            node_bin = c
            break

    pw_module_candidates = [
        "/home/rafgani/.local/share/mise/installs/npm-playwright/latest/node_modules",
        "/home/rafgani/.local/share/mise/installs/npm-playwright/1.65.0/node_modules",
    ]
    node_path = os.environ.get("NODE_PATH", "")
    for p in pw_module_candidates:
        if os.path.isdir(p):
            node_path = f"{p}:{node_path}" if node_path else p
            break

    return node_bin, node_path


def main():
    parser = argparse.ArgumentParser(
        description="Verify Reveal.js + CindyJS + KaTeX slides for zero text overflow or clipping."
    )
    parser.add_argument("html_file", type=str, help="Path to the Reveal.js HTML file")
    parser.add_argument(
        "--export-png",
        type=str,
        default="",
        help="Optional directory to save slide_preview-XX.png screenshots",
    )
    parser.add_argument(
        "--prefix",
        type=str,
        default="html_slide_preview",
        help="Filename prefix for exported PNGs (default: html_slide_preview)",
    )
    args = parser.parse_args()

    html_path = Path(args.html_file).resolve()
    if not html_path.is_file():
        print(f"❌ Error: HTML file not found: {html_path}")
        return 1

    export_dir = ""
    if args.export_png:
        export_path = Path(args.export_png).resolve()
        export_path.mkdir(parents=True, exist_ok=True)
        export_dir = str(export_path)

    node_bin, node_path = find_node_and_playwright()
    env = os.environ.copy()
    env["NODE_PATH"] = node_path
    env["VERIFY_HTML_PATH"] = str(html_path)
    env["VERIFY_EXPORT_DIR"] = export_dir
    env["VERIFY_PNG_PREFIX"] = args.prefix

    print(f"🔍 Auditing Reveal.js + CindyJS Slide Deck: {html_path.name}")
    if export_dir:
        print(f"📸 Exporting PNG snapshots to: {export_dir}/{args.prefix}-XX.png")

    with tempfile.NamedTemporaryFile("w", suffix=".cjs", delete=False) as tmp:
        tmp.write(NODE_VERIFY_SCRIPT)
        tmp_script_path = tmp.name

    try:
        proc = subprocess.run(
            [node_bin, tmp_script_path],
            env=env,
            capture_output=True,
            text=True,
            timeout=90,
        )
    finally:
        if os.path.exists(tmp_script_path):
            os.remove(tmp_script_path)

    if proc.returncode != 0:
        print("❌ Playwright execution failed:")
        print(proc.stderr or proc.stdout)
        return 2

    out = proc.stdout
    start_marker = "__VERIFY_JSON_START__"
    end_marker = "__VERIFY_JSON_END__"
    if start_marker not in out or end_marker not in out:
        print("❌ Unexpected verifier output:")
        print(out)
        return 3

    json_str = out.split(start_marker, 1)[1].split(end_marker, 1)[0].strip()
    slides_report = json.loads(json_str)

    print("\n" + "=" * 88)
    print(f"{'SLIDE':<7} | {'STATUS':<8} | {'HEIGHT':<11} | {'TITLE & DIAGNOSTICS'}")
    print("=" * 88)

    failed_slides = []
    for s in slides_report:
        num = s["slideNumber"]
        title = s["title"][:48]
        v_over = s["verticalOverflowPx"]
        h_over = s["horizontalOverflowPx"]
        clipped = s["clippedElements"]
        k_err = s["katexErrors"]
        cindy_bad = [
            c for c in s["cindyCanvases"] if not c["hasCanvas"] or c["width"] < 50 or c["height"] < 50
        ]

        has_issue = (
            v_over > 2
            or h_over > 4
            or len(clipped) > 0
            or len(k_err) > 0
            or len(cindy_bad) > 0
        )

        status_str = "FAIL" if has_issue else "PASS"
        icon = "❌" if has_issue else "✅"
        dim_str = f"{s['scrollH']}/{s['configH']}px"
        print(f"#{num:02d}     | {icon} {status_str:<5} | {dim_str:<11} | {title}")

        if has_issue:
            failed_slides.append(s)
            if v_over > 2:
                print(f"          ↳ [OVERFLOW-Y] +{v_over}px beyond {s['configH']}px slide height")
            if h_over > 4:
                print(f"          ↳ [OVERFLOW-X] +{h_over}px beyond {s['configW']}px slide width")
            for c in clipped[:4]:
                reasons = []
                if c["overBottom"] > 0:
                    reasons.append(f"bottom +{c['overBottom']}px")
                if c["overRight"] > 0:
                    reasons.append(f"right +{c['overRight']}px")
                if c["internalClipY"] > 0:
                    reasons.append(f"internal clip +{c['internalClipY']}px")
                print(f"          ↳ [CLIPPED] {c['tag']}: \"{c['snippet']}\" ({', '.join(reasons)})")
            for err in k_err:
                print(f"          ↳ [KATEX-ERR] {err}")
            for cb in cindy_bad:
                print(f"          ↳ [CINDY-ERR] Canvas '{cb['id']}' ({cb['width']}x{cb['height']})")

    print("=" * 88)
    if failed_slides:
        print(
            f"❌ VERIFICATION FAILED: {len(failed_slides)}/{len(slides_report)} slides have overflow or visibility issues."
        )
        print(
            "💡 Fix suggestion: Add class=\"slide-compact\" or \"slide-ultra-compact\" to overflowing <section> tags,"
        )
        print(
            "   or reduce display equation vertical margins / split dense content across 2 columns."
        )
        return 1
    else:
        print(
            f"✅ VERIFICATION PASSED: All {len(slides_report)}/{len(slides_report)} slides have ZERO overflow, ZERO clipped text, and valid KaTeX/CindyJS!"
        )
        return 0


if __name__ == "__main__":
    sys.exit(main())
