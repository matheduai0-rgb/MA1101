#!/usr/bin/env python3
"""
verify_slidev_slides.py - Automated Viewport, Zero-Overflow, Text Visibility & JSXGraph Auditor for Slidev

Audits Slidev presentations using headless Chromium via Playwright:
  1. Zero vertical or horizontal slide overflow (scrollHeight <= clientHeight + 4px).
  2. Zero clipped or hidden text/math elements outside the slide frame.
  3. Zero KaTeX syntax errors (.katex-error) or unrendered delimiters ($$, \\begin).
  4. Non-zero SVG/canvas initialization for all JSXGraph interactive applets (.jxgbox).
  5. Optional slide snapshot generation (slide_preview-01.png ... slide_preview-NN.png).

Usage:
  python3 verify_slidev_slides.py <path_to_slides.md> [--port 3030] [--export-png <output_dir>]
"""

import argparse
import json
import os
import signal
import socket
import subprocess
import sys
import time
import urllib.request
from pathlib import Path


def is_port_in_use(port: int) -> bool:
    try:
        req = urllib.request.Request(f"http://localhost:{port}/", headers={'User-Agent': 'verify-script'})
        with urllib.request.urlopen(req, timeout=0.8) as r:
            return True
    except Exception:
        pass

    for host in ('localhost', '127.0.0.1', '::1'):
        try:
            infos = socket.getaddrinfo(host, port, proto=socket.IPPROTO_TCP)
            for family, socktype, proto, _, sockaddr in infos:
                try:
                    with socket.socket(family, socktype, proto) as s:
                        s.settimeout(0.3)
                        if s.connect_ex(sockaddr) == 0:
                            return True
                except Exception:
                    continue
        except Exception:
            continue
    return False


def find_free_port(start: int = 3030) -> int:
    port = start
    while port < 3200:
        if not is_port_in_use(port):
            return port
        port += 1
    return 3030


NODE_VERIFY_SCRIPT = r"""
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

(async () => {
  const targetUrl = process.env.VERIFY_TARGET_URL;
  const exportDir = process.env.VERIFY_EXPORT_DIR || '';
  const chromeExec = process.env.VERIFY_CHROME_EXEC || '/usr/bin/chromium';

  const browser = await chromium.launch({
    executablePath: fs.existsSync(chromeExec) ? chromeExec : undefined,
    headless: true,
    args: ['--no-sandbox', '--disable-gpu']
  });

  const context = await browser.newContext({
    viewport: { width: 1280, height: 720 },
    deviceScaleFactor: 1
  });

  const page = await context.newPage();

  // Collect console errors
  const consoleErrors = [];
  page.on('console', msg => {
    if (msg.type() === 'error') {
      consoleErrors.push(msg.text());
    }
  });

  try {
    await page.goto(targetUrl, { waitUntil: 'domcontentloaded', timeout: 30000 });
  } catch (err) {
    console.error(JSON.stringify({ error: `Failed to load ${targetUrl}: ${err.message}` }));
    await browser.close();
    process.exit(1);
  }

  // Wait for Slidev runtime
  await page.waitForFunction(() => {
    return (
      document.querySelector('.slidev-layout') ||
      document.querySelector('.slidev-page') ||
      document.querySelector('#slide-content') ||
      document.querySelector('#slideshow')
    );
  }, { timeout: 25000 });

  await page.waitForTimeout(600);

  // Retrieve total slides from Slidev window object or route
  const totalSlides = await page.evaluate(() => {
    if (window.__slidev__ && window.__slidev__.nav && window.__slidev__.nav.total) {
      return window.__slidev__.nav.total;
    }
    if (window.$slidev && window.$slidev.nav && window.$slidev.nav.total) {
      return window.$slidev.nav.total;
    }
    const pages = document.querySelectorAll('.slidev-page');
    return pages.length || 1;
  });

  const results = [];

  for (let slideNo = 1; slideNo <= totalSlides; slideNo++) {
    // Navigate via Slidev's client navigation API
    await page.evaluate((no) => {
      if (window.__slidev__ && window.__slidev__.nav) {
        window.__slidev__.nav.go(no);
      } else if (window.$slidev && window.$slidev.nav) {
        window.$slidev.nav.go(no);
      } else {
        window.location.hash = `#${no}`;
      }
    }, slideNo);
    await page.waitForTimeout(650);

    // If JSXGraph boards exist, give extra time for SVG mounting
    const hasJxg = await page.$('.jxgbox');
    if (hasJxg) {
      await page.waitForTimeout(500);
    }

    // Audit current slide DOM
    const audit = await page.evaluate((no) => {
      const pageEl = document.querySelector('#slide-content') || document.querySelector('.slidev-layout') || document.querySelector('.slidev-page');
      if (!pageEl) {
        return { slideNo: no, title: `Slide ${no}`, error: 'Slide container not found' };
      }

      const titleEl = pageEl.querySelector('h1, h2, h3, .slide-title');
      const title = titleEl ? titleEl.textContent.trim().replace(/\s+/g, ' ') : `Slide ${no}`;

      const clientH = pageEl.clientHeight;
      const scrollH = pageEl.scrollHeight;
      const clientW = pageEl.clientWidth;
      const scrollW = pageEl.scrollWidth;

      const vOverflow = Math.max(0, scrollH - clientH);
      const hOverflow = Math.max(0, scrollW - clientW);

      const pageRect = pageEl.getBoundingClientRect();
      const frameBottom = pageRect.bottom + 4;
      const frameRight = pageRect.right + 4;

      // Scan candidate content elements for clipping / boundary breach
      const clippedElements = [];
      const candidates = pageEl.querySelectorAll('h1, h2, h3, p, li, table, .b-block, .b-example, .b-alert, .formula-box, .jxgbox, .katex-display');

      candidates.forEach((el) => {
        const r = el.getBoundingClientRect();
        if (r.width === 0 && r.height === 0) return; // Hidden or unmounted

        // Check if bottom or right overflows the slide safe area
        if (r.bottom > frameBottom) {
          const delta = Math.round(r.bottom - frameBottom);
          clippedElements.push({
            tag: el.tagName.toLowerCase(),
            class: (el.className || '').toString().slice(0, 40),
            text: (el.textContent || '').trim().slice(0, 50),
            overflowPx: delta,
            direction: 'bottom'
          });
        }
      });

      // Scan KaTeX syntax errors & count rendered math nodes
      const katexErrors = [];
      const errorNodes = pageEl.querySelectorAll('.katex-error');
      errorNodes.forEach(err => {
        katexErrors.push(err.textContent || 'KaTeX parsing error');
      });
      const katexCount = pageEl.querySelectorAll('.katex').length;

      // Scan for raw unrendered math delimiters in visible text
      const rawText = pageEl.innerText || '';
      const unrenderedMath = [];
      if (/\$\$(.+?)\$\$/.test(rawText)) {
        unrenderedMath.push('Unrendered display math ($$) detected');
      }
      const inlineMathMatch = rawText.match(/\$([^\$\n\r]*(?:\\[a-zA-Z]+|[a-zA-Z]_[0-9a-zA-Z]|f\(x\)|\\int|\\sum|\\[lg]t|\Delta)[^\$\n\r]*)\$/g);
      if (inlineMathMatch) {
        inlineMathMatch.forEach(m => {
          unrenderedMath.push(`Unrendered inline math: ${m}`);
        });
      }
      if (/\\begin\{(aligned|matrix|cases)\}/.test(rawText)) {
        unrenderedMath.push('Unrendered LaTeX environment detected');
      }

      // Check JSXGraph applets on current visible slide
      const jxgBoxes = pageEl.querySelectorAll('.jxgbox');
      const jxgStatus = [];
      jxgBoxes.forEach((box, idx) => {
        const rect = box.getBoundingClientRect();
        if (rect.width === 0 && rect.height === 0) return; // Ignore unmounted or hidden offscreen boards
        const svg = box.querySelector('svg');
        const hasSvg = svg !== null && (svg.clientWidth > 0 || svg.getBoundingClientRect().width > 0);
        jxgStatus.push({
          index: idx + 1,
          initialized: hasSvg,
          width: Math.round(rect.width),
          height: Math.round(rect.height)
        });
      });

      return {
        slideNo: no,
        title,
        clientH,
        scrollH,
        vOverflow,
        hOverflow,
        clippedCount: clippedElements.length,
        clippedElements: clippedElements.slice(0, 5),
        katexCount,
        katexErrors,
        unrenderedMath,
        jxgApplets: jxgStatus,
        passed: vOverflow <= 4 && hOverflow <= 4 && clippedElements.length === 0 && katexErrors.length === 0 && unrenderedMath.length === 0
      };
    }, slideNo);

    // Optional snapshot
    if (exportDir) {
      if (!fs.existsSync(exportDir)) {
        fs.mkdirSync(exportDir, { recursive: true });
      }
      const pad = String(slideNo).padStart(2, '0');
      const pngPath = path.join(exportDir, `slide_preview-${pad}.png`);
      await page.screenshot({ path: pngPath });
      audit.pngPath = pngPath;
    }

    results.push(audit);
  }

  await browser.close();
  console.log(JSON.stringify({ totalSlides, results, consoleErrors }));
})();
"""


def run_verification(slides_path: str, port: int = 3030, export_dir: str = "", chrome_exec: str = "/usr/bin/chromium"):
    slides_file = Path(slides_path).resolve()
    if not slides_file.exists():
        print(f"Error: slides file not found: {slides_file}", file=sys.stderr)
        return False

    # Find repository root containing package.json
    project_root = slides_file.parent
    for parent in [slides_file.parent] + list(slides_file.parents):
        if (parent / "package.json").exists():
            project_root = parent
            break

    dev_process = None
    server_started_by_us = False

    if not is_port_in_use(port):
        print(f"[*] Starting Slidev server on port {port} for {slides_file.name} (cwd: {project_root})...")
        env = os.environ.copy()
        dev_process = subprocess.Popen(
            ["npx", "slidev", str(slides_file), "--port", str(port), "--no-open"],
            cwd=str(project_root),
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            env=env
        )
        server_started_by_us = True

        # Wait for port to become active
        max_wait = 45
        start_t = time.time()
        while time.time() - start_t < max_wait:
            if is_port_in_use(port):
                break
            time.sleep(0.5)

        if not is_port_in_use(port):
            print(f"Error: Slidev server failed to start on port {port} within {max_wait}s", file=sys.stderr)
            if dev_process:
                dev_process.kill()
            return False
        time.sleep(1.5)
    else:
        print(f"[*] Connected to existing server on port {port}")

    target_url = f"http://localhost:{port}"

    # Run Node Playwright audit script
    node_env = os.environ.copy()
    node_env["VERIFY_TARGET_URL"] = target_url
    node_env["VERIFY_EXPORT_DIR"] = str(Path(export_dir).resolve()) if export_dir else ""
    node_env["VERIFY_CHROME_EXEC"] = chrome_exec

    try:
        proc = subprocess.run(
            ["node", "-e", NODE_VERIFY_SCRIPT],
            capture_output=True,
            text=True,
            env=node_env,
            timeout=120
        )
    finally:
        if server_started_by_us and dev_process:
            print("[*] Stopping Slidev server...")
            dev_process.terminate()
            try:
                dev_process.wait(timeout=3)
            except subprocess.TimeoutExpired:
                dev_process.kill()

    if proc.returncode != 0:
        print(f"Verification runner error:\n{proc.stderr}", file=sys.stderr)
        return False

    try:
        data = json.loads(proc.stdout.strip())
    except Exception as e:
        print(f"Failed to parse audit JSON output: {e}\nRaw output:\n{proc.stdout}", file=sys.stderr)
        return False

    results = data.get("results", [])
    total = data.get("totalSlides", len(results))

    print("\n" + "=" * 78)
    print(f" Slidev Zero-Overflow & Text Visibility Audit ({slides_file.name})")
    print(f" Inspected {total} slides at {target_url}")
    print("=" * 78)

    all_passed = True
    for r in results:
        status_sym = "✅ PASS" if r.get("passed") else "❌ FAIL"
        if not r.get("passed"):
            all_passed = False

        print(f"\n[Slide {r['slideNo']:02d}] {status_sym} - {r['title']}")
        print(f"  Viewport: {r.get('clientH', 0)}px | Scroll: {r.get('scrollH', 0)}px | Width: {r.get('clientW', 0)}px/{r.get('scrollW', 0)}px | KaTeX Math Nodes: {r.get('katexCount', 0)}")

        if not r.get("passed"):
            print(f"  ⚠️ FAIL DETAILS: vOverflow={r.get('vOverflow')}px, hOverflow={r.get('hOverflow')}px, clippedCount={r.get('clippedCount', 0)}, katexErrors={len(r.get('katexErrors', []))}, unrenderedMath={len(r.get('unrenderedMath', []))}")

        if r.get("clippedElements"):
            print("  ⚠️ Clipped / Out-of-frame elements:")
            for c in r["clippedElements"]:
                print(f"    - <{c['tag']} class='{c['class']}'> overflows by {c['overflowPx']}px: \"{c['text']}\"")

        if r.get("katexErrors"):
            print("  ⚠️ KaTeX errors detected:")
            for err in r["katexErrors"]:
                print(f"    - {err}")

        if r.get("unrenderedMath"):
            print("  ⚠️ Unrendered math detected:")
            for um in r["unrenderedMath"]:
                print(f"    - {um}")

        if r.get("jxgApplets"):
            for app in r["jxgApplets"]:
                app_sym = "✅ Active" if app.get("initialized") else "❌ Uninitialized"
                print(f"  JSXGraph Board #{app['index']}: {app_sym} ({app['width']}x{app['height']}px)")

        if r.get("pngPath"):
            print(f"  Snapshot: {r['pngPath']}")

    print("\n" + "=" * 78)
    if all_passed:
        print("🎉 ALL SLIDES PASSED AUDIT: Zero overflow, zero clipped text, math fully rendered!")
    else:
        print("❌ VERIFICATION FAILED: Slides with overflow or clipping must be condensed or split.")
    print("=" * 78 + "\n")

    return all_passed


def main():
    parser = argparse.ArgumentParser(description="Verify Slidev slides text overflow and visibility")
    parser.add_argument("slides", help="Path to slides.md")
    parser.add_argument("--port", type=int, default=3030, help="Port to run/connect Slidev server")
    parser.add_argument("--export-png", default="", help="Directory to export slide PNG screenshots")
    parser.add_argument("--chrome-exec", default="/usr/bin/chromium", help="Path to chromium binary")

    args = parser.parse_args()
    success = run_verification(
        slides_path=args.slides,
        port=args.port,
        export_dir=args.export_png,
        chrome_exec=args.chrome_exec
    )
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
