<script setup lang="ts">
/**
 * ShellBoard3D — cylindrical shell method in 3D (JSXGraph view3d).
 *
 * Region under y = f(x) = 2x^2 - x^3, 0 <= x <= 2, rotated about the vertical axis (z in the view).
 * Drag the canvas to rotate the view. A thin vertical strip (red) at x, width dx, height f(x), is turned
 * about the axis with the "putar irisan" slider; at 0° only the flat strip is visible (so a prediction
 * about the shape is not given away), at 360° it has become a cylindrical shell.
 *
 * Controls:
 *   putar irisan         sweep the strip from 0° to 360°
 *   x, dx slider         move and thicken the shell
 *   tampilkan ukuran     radius, height and thickness segments
 *   bentangkan           the shell cut open is a flat rectangle 2πx by f(x), drawn to scale in the panel
 *   jumlahkan semua kulit n nested shells and their total next to the exact 16π/5
 *
 * Pattern follows DiscMethodYAxis3DBoard.vue (view3d, parametricsurface3d, rebuild on change).
 */
import { ref, computed, onMounted, onUnmounted, watch } from 'vue'

const props = withDefaults(defineProps<{ height?: string }>(), { height: '350px' })

const id = `jxg-shell3d-${Math.random().toString(36).slice(2, 9)}`
const xv = ref(1.0)
const dxv = ref(0.2)
const nv = ref(6)
const rot = ref(0)          // degrees the strip has been turned about the vertical axis
const showDim = ref(false)
const showUnroll = ref(false)
const showSum = ref(false)

const B = 2
const EXACT = 16 * Math.PI / 5
const f = (x: number) => 2 * x * x - x * x * x
const fmt = (v: number, d = 2) => v.toFixed(d).replace('.', ',')

const w = computed(() => Math.min(dxv.value, B - xv.value))
const height = computed(() => f(xv.value))
const length = computed(() => 2 * Math.PI * xv.value)
const dV = computed(() => length.value * height.value * w.value)
const shellSum = computed(() => {
  const n = nv.value
  const d = B / n
  let s = 0
  for (let i = 0; i < n; i++) {
    const xm = (i + 0.5) * d
    s += 2 * Math.PI * xm * f(xm) * d
  }
  return s
})

// flat-rectangle inset: scale so the longest possible side (2π·2) fits 200 px
const SC = 200 / (2 * Math.PI * B)
const rectW = computed(() => length.value * SC)
const rectH = computed(() => Math.max(height.value * SC, 2))

let board: any = null
let view: any = null
let resizeObserver: ResizeObserver | null = null
const dynamic: any[] = []

const clear = () => {
  while (dynamic.length) {
    const el = dynamic.pop()
    try { board.removeObject(el) } catch (e) { /* ignore */ }
  }
}

const surf = (X: any, Y: any, Z: any, ur: number[], vr: number[], attr: any) => {
  const s = view.create('parametricsurface3d', [X, Y, Z, ur, vr], attr)
  dynamic.push(s)
  return s
}
const seg = (a: number[], b: number[], attr: any) => {
  const c = view.create('curve3d', [
    (t: number) => a[0] + (b[0] - a[0]) * t,
    (t: number) => a[1] + (b[1] - a[1]) * t,
    (t: number) => a[2] + (b[2] - a[2]) * t,
    [0, 1]
  ], attr)
  dynamic.push(c)
}

// thin cylindrical shell between radii r0 and r1, from z = 0 to z = h, swept from angle 0 to vEnd
const shell = (r0: number, r1: number, h: number, color: string, opacity: number, steps: number, vEnd = 2 * Math.PI) => {
  if (vEnd < 0.02) return
  const base = { strokeColor: color, strokeWidth: 0.6, fillColor: color, fillOpacity: opacity, stepsU: 1, stepsV: Math.max(2, Math.round(steps * vEnd / (2 * Math.PI))) }
  surf((u: number, v: number) => r1 * Math.cos(v), (u: number, v: number) => r1 * Math.sin(v), (u: number) => u, [0, h], [0, vEnd], base)
  if (r0 > 0.02) {
    surf((u: number, v: number) => r0 * Math.cos(v), (u: number, v: number) => r0 * Math.sin(v), (u: number) => u, [0, h], [0, vEnd], base)
  }
  surf((u: number, v: number) => u * Math.cos(v), (u: number, v: number) => u * Math.sin(v), () => h, [r0, r1], [0, vEnd], base)
}

const build = () => {
  if (!board || !view) return
  clear()
  if (showSum.value) {
    const n = nv.value
    const d = B / n
    for (let i = 0; i < n; i++) {
      const xm = (i + 0.5) * d
      shell(Math.max(xm - d / 2, 0), xm + d / 2, f(xm), i % 2 ? '#fb7185' : '#f59e0b', 0.7, 16)
    }
  } else {
    // the strip itself (where the rotation starts), then the shell it sweeps out
    surf((u: number) => u, () => 0, (u: number, v: number) => v, [xv.value, xv.value + w.value], [0, height.value],
      { strokeColor: '#fb7185', strokeWidth: 1.5, fillColor: '#fb7185', fillOpacity: 0.95, stepsU: 1, stepsV: 1 })
    shell(xv.value, xv.value + w.value, height.value, '#fb7185', 0.8, 28, rot.value * Math.PI / 180)
    if (showDim.value) {
      const x = xv.value, h = height.value, ww = w.value
      seg([0, 0, 0], [x, 0, 0], { strokeColor: '#ffffff', strokeWidth: 3 })
      seg([x, 0, 0], [x, 0, h], { strokeColor: '#f5be3c', strokeWidth: 3 })
      seg([x, 0, h], [x + ww, 0, h], { strokeColor: '#2dd4bf', strokeWidth: 4 })
    }
  }
  board.update()
}

watch([xv, dxv, nv, rot, showDim, showSum], build)

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
  board = JXG.JSXGraph.initBoard(id, {
    boundingbox: [-3, 3, 3, -3], axis: false, showNavigation: false, showCopyright: false,
    pan: { enabled: false }, zoom: { enabled: false }
  })
  view = board.create('view3d', [[-3.1, -3.1], [6.2, 6.2], [[-2.3, 2.3], [-2.3, 2.3], [0, 1.6]]], {
    projection: 'parallel',
    az: { slider: { visible: false, start: 5.4 }, continuous: true },
    el: { slider: { visible: false, start: 0.62 }, continuous: true },
    bank: { slider: { visible: false } },
    xPlaneRear: { visible: false }, yPlaneRear: { visible: false }, zPlaneRear: { visible: false },
    xPlaneFront: { visible: false }, yPlaneFront: { visible: false },
    xAxis: { strokeColor: '#475569', strokeWidth: 1, name: '' },
    yAxis: { strokeColor: '#475569', strokeWidth: 1, name: '' },
    zAxis: { strokeColor: '#f5be3c', strokeWidth: 3, name: '' }
  })

  // the solid of revolution (curve y = f(x) turned about the vertical axis) and its base
  view.create('parametricsurface3d', [
    (u: number, v: number) => u * Math.cos(v), (u: number, v: number) => u * Math.sin(v), (u: number) => f(u),
    [0, B], [0, 2 * Math.PI]
  ], { strokeColor: '#50a5fa', strokeWidth: 0.5, strokeOpacity: 0.28, fillColor: '#50a5fa', fillOpacity: 0.08, stepsU: 10, stepsV: 28 })
  view.create('parametricsurface3d', [
    (u: number, v: number) => u * Math.cos(v), (u: number, v: number) => u * Math.sin(v), () => 0,
    [0, B], [0, 2 * Math.PI]
  ], { strokeColor: '#475569', strokeWidth: 0.4, strokeOpacity: 0.5, fillColor: '#334155', fillOpacity: 0.12, stepsU: 1, stepsV: 36 })

  build()

  const el = document.getElementById(id)
  if (el && typeof ResizeObserver !== 'undefined') {
    resizeObserver = new ResizeObserver(() => { board.resizeContainer(el.clientWidth, el.clientHeight, true); board.update() })
    resizeObserver.observe(el)
  }
})

onUnmounted(() => {
  resizeObserver?.disconnect(); resizeObserver = null
  clear()
  const JXG = (window as any).JXG
  try { if (board) JXG?.JSXGraph.freeBoard(board) } catch (e) { /* ignore */ }
  board = null; view = null
})
</script>

<template>
  <div class="s3 flex gap-3 w-full" :style="{ height: props.height }">
    <div style="flex: 1 1 0; min-width: 0;">
      <div :id="id" class="jxgbox w-full rounded-xl border border-slate-700/80 overflow-hidden bg-[#0c1018]" style="aspect-ratio: 1 / 1; max-height: 100%;"></div>
      <div class="s3-hint">Seret gambar untuk memutar</div>
    </div>

    <div class="s3-panel">
      <label v-if="!showSum" class="s3-row">
        <span>putar irisan: <b>{{ Math.round(rot) }}°</b></span>
        <input type="range" min="0" max="360" step="5" v-model.number="rot" />
      </label>
      <label class="s3-row">
        <span>x = <b>{{ fmt(xv, 2) }}</b></span>
        <input type="range" min="0.1" max="1.95" step="0.05" v-model.number="xv" />
      </label>
      <label class="s3-row">
        <span>Δx = <b>{{ fmt(w, 2) }}</b></span>
        <input type="range" min="0.05" max="0.5" step="0.05" v-model.number="dxv" />
      </label>

      <label class="s3-check"><input type="checkbox" v-model="showDim" :disabled="showSum" /> tampilkan ukuran</label>
      <div v-if="showDim && !showSum" class="s3-legend">
        <span style="color:#ffffff">━ jari-jari x</span>
        <span style="color:#f5be3c">━ tinggi f(x)</span>
        <span style="color:#2dd4bf">━ tebal Δx</span>
      </div>

      <label class="s3-check"><input type="checkbox" v-model="showUnroll" /> bentangkan kulit</label>
      <div v-if="showUnroll" class="s3-unroll">
        <svg width="100%" :viewBox="`0 0 ${200 + 4} ${rectH + 4}`" :style="{ height: rectH + 4 + 'px' }" preserveAspectRatio="xMinYMin meet">
          <rect x="2" y="2" :width="rectW" :height="rectH" class="s3-rect" />
        </svg>
        <div class="s3-note">persegi panjang {{ fmt(length, 2) }} × {{ fmt(height, 2) }}, yaitu 2πx × f(x)</div>
      </div>

      <label class="s3-check"><input type="checkbox" v-model="showSum" /> jumlahkan semua kulit</label>
      <label v-if="showSum" class="s3-row">
        <span>n = <b>{{ nv }}</b></span>
        <input type="range" min="1" max="40" step="1" v-model.number="nv" />
      </label>

      <div class="s3-out">
        <template v-if="!showSum">
          <div>ΔV ≈ 2π · x · f(x) · Δx = <b>{{ fmt(dV, 3) }}</b></div>
        </template>
        <template v-else>
          <div>Σ {{ nv }} kulit ≈ <b>{{ fmt(shellSum, 3) }}</b></div>
          <div class="s3-exact">eksak 16π/5 ≈ {{ fmt(EXACT, 3) }}</div>
        </template>
      </div>
    </div>
  </div>
</template>

<style>
.s3 { font-size: 0.78rem; color: #e2e8f0; }
.s3 .jxgbox { background-color: #0c1018 !important; }
.s3 .jxgbox svg { background-color: #0c1018 !important; }
.s3-hint { margin-top: 0.25rem; font-size: 0.68rem; color: #64748b; text-align: center; }
.s3-panel { flex: 0 0 215px; width: 215px; box-sizing: border-box; display: flex; flex-direction: column; gap: 0.35rem; background: #141b28; border: 1px solid #233148; border-radius: 0.75rem; padding: 0.55rem 0.7rem; min-width: 0; overflow: hidden; }
.s3-row { display: flex; flex-direction: column; gap: 0.1rem; }
.s3-row input[type=range] { width: 100%; accent-color: #f5be3c; }
.s3-row b { color: #f5be3c; font-family: ui-monospace, monospace; }
.s3-check { display: flex; align-items: center; gap: 0.4rem; cursor: pointer; }
.s3-check input { accent-color: #2dd4bf; }
.s3-legend { display: flex; flex-wrap: wrap; gap: 0.2rem 0.6rem; font-size: 0.7rem; font-family: ui-monospace, monospace; padding-left: 1.2rem; }
.s3-unroll { padding-left: 1.2rem; }
.s3-rect { fill: rgba(251, 113, 133, 0.55); stroke: #fb7185; stroke-width: 1.5; }
.s3-note { font-size: 0.68rem; color: #94a3b8; margin-top: 0.15rem; }
.s3-out { margin-top: auto; padding-top: 0.4rem; border-top: 1px solid #233148; font-family: ui-monospace, monospace; }
.s3-out b { color: #34d399; }
.s3-exact { color: #94a3b8; font-size: 0.7rem; }
</style>
