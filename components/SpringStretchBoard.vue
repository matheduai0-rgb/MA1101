<script setup lang="ts">
/**
 * SpringStretchBoard — interactive version of WorkFigure kind="spring".
 *
 * Top   : dimmed reference — spring at natural length with its block ("panjang alami").
 * Bottom: the same spring stretched by x (0 to 0,3 m). Drag the block or use the slider; "▶ Tarik"
 *         animates the pull from 0 to 0,3 m. The coral force arrow grows with F = 100x and its label
 *         shows the current value, so students see that the force is not one number during the pull.
 * The work itself is not shown: finding it is the point of the next slides.
 */
import { ref, onMounted, onUnmounted, watch } from 'vue'

const props = withDefaults(defineProps<{ height?: string; k?: number; xmax?: number }>(),
  { height: '250px', k: 100, xmax: 0.3 })

const id = `jxg-ss-${Math.random().toString(36).slice(2, 9)}`
const xv = ref(0.3)
const fmt = (v: number, d = 2) => v.toFixed(d).replace('.', ',')

// drawing units: natural length L, block width BW; x is drawn 1:1
const L = 0.42
const BW = 0.07
const BH = 0.11
const YT = 0.72   // top spring line
const YB = 0.36   // bottom spring line

let raf = 0
const stopAnim = () => { if (raf) cancelAnimationFrame(raf); raf = 0 }
const pull = () => {
  stopAnim()
  const t0 = performance.now()
  const dur = 2000
  const step = (now: number) => {
    const s = Math.min(1, (now - t0) / dur)
    xv.value = Math.round(props.xmax * s * 1000) / 1000
    raf = s < 1 ? requestAnimationFrame(step) : 0
  }
  xv.value = 0
  raf = requestAnimationFrame(step)
}

let board: any = null
let glider: any = null
let ro: ResizeObserver | null = null
let dragging = false

// zigzag between x0 and x1 on line y (as data arrays)
const zig = (x0: number, x1: number, y: number, n = 8, amp = 0.05) => {
  const lead = 0.03
  const a = x0 + lead
  const b = Math.max(a + 0.01, x1 - lead)
  const xs = [x0, a]
  const ys = [y, y]
  for (let i = 0; i < n * 2; i++) {
    xs.push(a + (i + 0.5) * (b - a) / (n * 2))
    ys.push(y + (i % 2 === 0 ? amp : -amp))
  }
  xs.push(b, x1)
  ys.push(y, y)
  return [xs, ys]
}

watch(xv, (v) => {
  if (!board) return
  if (!dragging && glider) glider.moveTo([L + BW / 2 + v, YB])
  board.update()
})

onMounted(async () => {
  if (typeof window === 'undefined') return
  const mod = await import('jsxgraph')
  const JXG = (mod as any).default || (window as any).JXG || mod
  if (!document.getElementById('jsxgraph-css')) {
    const link = document.createElement('link')
    link.id = 'jsxgraph-css'
    link.rel = 'stylesheet'
    link.href = 'https://cdn.jsdelivr.net/npm/jsxgraph/distrib/jsxgraph.css'
    document.head.appendChild(link)
  }
  const fix = { fixed: true, highlight: false }
  const xmax = props.xmax
  board = JXG.JSXGraph.initBoard(id, {
    boundingbox: [-0.05, 0.9, L + BW + xmax + 0.36, -0.07], axis: false, showNavigation: false, showCopyright: false,
    keepaspectratio: false, pan: { enabled: false }, zoom: { enabled: false }
  })

  // wall
  board.create('segment', [[0, 0.2], [0, 0.85]], { strokeColor: '#94a3b8', strokeWidth: 5, ...fix })

  // reference: natural length (dimmed)
  const [tx, ty] = zig(0, L, YT)
  board.create('curve', [tx, ty], { strokeColor: '#64748b', strokeWidth: 2, ...fix })
  board.create('polygon', [[L, YT - BH / 2], [L + BW, YT - BH / 2], [L + BW, YT + BH / 2], [L, YT + BH / 2]], {
    fillColor: '#334155', fillOpacity: 1, borders: { strokeColor: '#64748b', strokeWidth: 1.5 }, vertices: { visible: false }, ...fix
  })
  board.create('text', [L + BW + 0.04, YT, 'panjang alami'], { color: '#94a3b8', fontSize: 12, anchorY: 'middle', ...fix })

  // x = 0 guide
  board.create('segment', [[L, YT - BH / 2 - 0.02], [L, 0.06]], { strokeColor: '#475569', strokeWidth: 1, dash: 2, ...fix })
  board.create('text', [L, 0.0, 'x = 0'], { color: '#94a3b8', fontSize: 11, anchorX: 'middle', anchorY: 'middle', ...fix })

  // stretched spring
  const spring = board.create('curve', [[], []], { strokeColor: '#cbd5e1', strokeWidth: 2.2, highlight: false })
  spring.updateDataArray = function () {
    const [xs, ys] = zig(0, L + xv.value, YB)
    this.dataX = xs
    this.dataY = ys
  }
  const bx = () => L + xv.value
  board.create('polygon', [
    [bx, YB - BH / 2], [() => bx() + BW, YB - BH / 2], [() => bx() + BW, YB + BH / 2], [bx, YB + BH / 2]
  ], { fillColor: '#475569', fillOpacity: 1, borders: { strokeColor: '#e2e8f0', strokeWidth: 1.5 }, vertices: { visible: false }, ...fix })

  // draggable handle on top of the block
  const track = board.create('segment', [[L + BW / 2, YB], [L + BW / 2 + xmax, YB]], { visible: false, fixed: true })
  glider = board.create('glider', [L + BW / 2 + xv.value, YB, track], {
    name: '', size: 14, face: 'square', strokeOpacity: 0, fillOpacity: 0, highlightStrokeOpacity: 0, highlightFillOpacity: 0, showInfobox: false
  })
  glider.on('down', () => { stopAnim(); dragging = true })
  glider.on('up', () => { dragging = false })
  glider.on('drag', () => {
    const v = Math.min(xmax, Math.max(0, glider.X() - L - BW / 2))
    xv.value = Math.round(v * 100) / 100
  })

  // force arrow: length grows with F = kx
  const aLen = () => 0.34 * xv.value / xmax
  const ax0 = () => bx() + BW + 0.012
  board.create('arrow', [[ax0, YB], [() => ax0() + aLen(), YB]], {
    strokeColor: '#fb7185', strokeWidth: 3.5, visible: () => xv.value > 0.004, ...fix
  })
  board.create('text', [() => bx() + BW + 0.015, YB + BH / 2 + 0.08,
    () => `F = ${props.k}x = ${fmt(props.k * xv.value, 0)} N`], { color: '#fb7185', fontSize: 14, cssClass: 'JXGtext jx-coral', highlightCssClass: 'JXGtext jx-coral', cssStyle: 'font-weight:600', ...fix })

  // dimension x
  board.create('segment', [[bx, YB - BH / 2 - 0.02], [bx, 0.06]], { strokeColor: '#475569', strokeWidth: 1, dash: 2, ...fix })
  board.create('arrow', [[L, 0.12], [bx, 0.12]], { strokeColor: '#f5be3c', strokeWidth: 2, firstArrow: true, lastArrow: true, visible: () => xv.value > 0.02, ...fix })
  board.create('text', [() => L + xv.value / 2, 0.19, () => `x = ${fmt(xv.value)} m`], {
    color: '#f5be3c', fontSize: 13, anchorX: 'middle', cssClass: 'JXGtext jx-gold', highlightCssClass: 'JXGtext jx-gold', cssStyle: 'font-weight:600', ...fix
  })

  const el = document.getElementById(id)
  if (el) {
    ;(el as any).__jxgBoard = board
    if (typeof ResizeObserver !== 'undefined') {
      ro = new ResizeObserver(() => { board.resizeContainer(el.clientWidth, el.clientHeight, true); board.update() })
      ro.observe(el)
    }
  }
  board.update()
})

onUnmounted(() => {
  stopAnim()
  ro?.disconnect()
  const JXG = (window as any).JXG
  try { if (board) JXG?.JSXGraph.freeBoard(board) } catch (e) { /* ignore */ }
  board = null; glider = null
})
</script>

<template>
  <div class="ss flex flex-col gap-2 w-full" :style="{ height: props.height }">
    <div :id="id" class="jxgbox ss-box"></div>
    <div class="ss-panel">
      <button type="button" class="ss-btn" @click="pull">▶ Tarik</button>
      <label class="ss-row">
        <span>x</span>
        <input type="range" min="0" :max="props.xmax" step="0.01" v-model.number="xv" @input="stopAnim" />
      </label>
      <span class="ss-num">x = <b>{{ fmt(xv) }}</b> m · F = <b class="ss-F">{{ fmt(props.k * xv, 0) }}</b> N</span>
    </div>
  </div>
</template>

<style>
.ss { font-size: 0.78rem; color: #e2e8f0; margin-bottom: 0.6rem; }
.ss-box { flex: 1 1 auto; min-height: 0; border-radius: 0.75rem; border: 1px solid #334155; overflow: hidden; background-color: #0c1018 !important; }
.ss .jxgbox svg { background-color: #0c1018 !important; }
.ss .jxgbox .JXGtext.jx-coral { color: #fb7185 !important; }
.ss .jxgbox .JXGtext.jx-gold { color: #f5be3c !important; }
.ss-panel { background: #141b28; border: 1px solid #233148; border-radius: 0.75rem; padding: 0.35rem 0.7rem; display: flex; align-items: center; gap: 0.8rem; }
.ss-row { flex: 1; display: flex; align-items: center; gap: 0.5rem; }
.ss-row span { color: #cbd5e1; font-family: ui-monospace, monospace; }
.ss-row input { flex: 1; accent-color: #f5be3c; min-width: 0; }
.ss-btn { background: rgba(251, 113, 133, 0.15); color: #fda4af; border: 1px solid rgba(251, 113, 133, 0.5); border-radius: 0.4rem; padding: 0.1rem 0.55rem; font-size: 0.74rem; cursor: pointer; white-space: nowrap; }
.ss-btn:hover { background: rgba(251, 113, 133, 0.28); }
.ss-num { font-family: ui-monospace, monospace; color: #cbd5e1; font-size: 0.72rem; white-space: nowrap; }
.ss-num b { color: #f5be3c; }
.ss-num b.ss-F { color: #fb7185; }
</style>
