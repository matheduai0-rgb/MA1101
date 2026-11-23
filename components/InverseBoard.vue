<script setup lang="ts">
/**
 * InverseBoard — inverse functions (JSXGraph 2D).
 *
 * mode="test"    : horizontal-line test. Buttons pick f(x) = x², x³ − 3x or x³ + x; a slider moves the
 *                  line y = c; its intersections with the graph are marked and counted. The verdict
 *                  ("punya invers?") stays hidden until "tampilkan kesimpulan" is ticked.
 * mode="reflect" : f(x) = x³ + x, the mirror line y = x, a slider a with the points (a, f(a)) and
 *                  (f(a), a) and the tangent lines there. The graph of f⁻¹ and the two slopes
 *                  (f'(a) and 1/f'(a)) appear only when their checkboxes are ticked.
 */
import { ref, computed, onMounted, onUnmounted, watch } from 'vue'

const props = withDefaults(defineProps<{ mode?: 'test' | 'reflect'; height?: string }>(),
  { mode: 'test', height: '360px' })

const id = `jxg-inv-${Math.random().toString(36).slice(2, 9)}`
const fmt = (v: number, d = 2) => v.toFixed(d).replace('.', ',').replace('-', '−')

// ---------- test mode ----------
const FUNS = [
  { key: 'sq', label: 'x²', f: (x: number) => x * x, inv: false },
  { key: 'cub3', label: 'x³ − 3x', f: (x: number) => x * x * x - 3 * x, inv: false },
  { key: 'cubx', label: 'x³ + x', f: (x: number) => x * x * x + x, inv: true }
]
const fsel = ref(0)
const cv = ref(1)
const showVerdict = ref(false)
const fun = computed(() => FUNS[fsel.value])

// roots of f(x) = c on [-3, 3]: sign changes on a fine grid, refined by bisection; touching roots
// (local extremum exactly at c) are caught by a small tolerance
const roots = computed(() => {
  const f = fun.value.f
  const c = cv.value
  const g = (x: number) => f(x) - c
  const out: number[] = []
  const N = 6000
  let prev = g(-3)
  for (let i = 1; i <= N; i++) {
    const x = -3 + (6 * i) / N
    const cur = g(x)
    if (Math.abs(cur) < 1e-7) {
      if (!out.length || Math.abs(out[out.length - 1] - x) > 0.01) out.push(x)
    } else if (prev * cur < 0 && Math.abs(prev) >= 1e-7) {
      let lo = x - 6 / N
      let hi = x
      for (let k = 0; k < 40; k++) {
        const m = (lo + hi) / 2
        if (g(lo) * g(m) <= 0) hi = m
        else lo = m
      }
      const r = (lo + hi) / 2
      if (!out.length || Math.abs(out[out.length - 1] - r) > 0.01) out.push(r)
    }
    prev = cur
  }
  return out
})

// ---------- reflect mode ----------
const fr = (x: number) => x * x * x + x
const dfr = (x: number) => 3 * x * x + 1
const av = ref(1)
const showInv = ref(false)
const showSlope = ref(false)
const m1 = computed(() => dfr(av.value))
const m2 = computed(() => 1 / dfr(av.value))

let board: any = null
let ro: ResizeObserver | null = null

watch([fsel, cv, av, showInv, showSlope], () => board?.update())

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
  const cls = (c: string) => ({ cssClass: `JXGtext ${c}`, highlightCssClass: `JXGtext ${c}` })
  const axes = {
    x: { strokeColor: '#475569', ticks: { strokeColor: '#334155', label: { strokeColor: '#94a3b8', fontSize: 10 }, minorTicks: 0 } },
    y: { strokeColor: '#475569', ticks: { strokeColor: '#334155', label: { strokeColor: '#94a3b8', fontSize: 10 }, minorTicks: 0 } }
  }

  if (props.mode === 'test') {
    board = JXG.JSXGraph.initBoard(id, {
      boundingbox: [-3.2, 4.4, 3.2, -4.4], axis: true, defaultAxes: axes, showNavigation: false, showCopyright: false,
      keepaspectratio: false, pan: { enabled: false }, zoom: { enabled: false }
    })
    board.create('functiongraph', [(x: number) => fun.value.f(x), -3.2, 3.2], { strokeColor: '#2dd4bf', strokeWidth: 3, ...fix })
    board.create('line', [[0, () => cv.value], [1, () => cv.value]], { strokeColor: '#f5be3c', strokeWidth: 2, dash: 2, ...fix })
    board.create('text', [2.15, () => cv.value + 0.35, () => `y = ${fmt(cv.value, 1)}`], { color: '#f5be3c', ...cls('jx-gold'), fontSize: 12, ...fix })
    for (let i = 0; i < 3; i++) {
      board.create('point', [() => roots.value[i] ?? 0, () => cv.value], {
        name: '', size: 5, fillColor: '#fb7185', strokeColor: '#fff', strokeWidth: 1.5,
        visible: () => roots.value.length > i, ...fix
      })
    }
  } else {
    board = JXG.JSXGraph.initBoard(id, {
      boundingbox: [-3.4, 3.4, 3.4, -3.4], axis: true, defaultAxes: axes, showNavigation: false, showCopyright: false,
      keepaspectratio: true, pan: { enabled: false }, zoom: { enabled: false }
    })
    board.create('line', [[0, 0], [1, 1]], { strokeColor: '#64748b', strokeWidth: 1.5, dash: 2, ...fix })
    board.create('text', [2.35, 2.75, 'y = x'], { color: '#94a3b8', ...cls('jx-muted'), fontSize: 12, ...fix })
    board.create('functiongraph', [fr, -1.6, 1.6], { strokeColor: '#2dd4bf', strokeWidth: 3, ...fix })
    board.create('text', [-2.7, -2.7, 'y = f(x)'], { color: '#2dd4bf', ...cls('jx-teal'), fontSize: 12, ...fix })
    board.create('curve', [(t: number) => fr(t), (t: number) => t, -1.6, 1.6], {
      strokeColor: '#60a5fa', strokeWidth: 3, visible: () => showInv.value, ...fix
    })
    board.create('text', [3.5, 0.7, 'y = f⁻¹(x)'], { color: '#60a5fa', ...cls('jx-blue'), fontSize: 12, visible: () => showInv.value, ...fix })
    const P = () => [av.value, fr(av.value)]
    const Q = () => [fr(av.value), av.value]
    board.create('segment', [[() => P()[0], () => P()[1]], [() => Q()[0], () => Q()[1]]], { strokeColor: '#475569', strokeWidth: 1, dash: 1, ...fix })
    // tangents: half-length L along the line direction
    const L = 0.9
    const tan = (pt: () => number[], m: () => number, color: string) => {
      const d = () => { const n = Math.sqrt(1 + m() * m()); return [L / n, (L * m()) / n] }
      board.create('segment', [
        [() => pt()[0] - d()[0], () => pt()[1] - d()[1]], [() => pt()[0] + d()[0], () => pt()[1] + d()[1]]
      ], { strokeColor: color, strokeWidth: 2.5, ...fix })
    }
    tan(P, () => m1.value, '#f5be3c')
    tan(Q, () => m2.value, '#fb7185')
    board.create('point', [() => P()[0], () => P()[1]], { name: '', size: 4.5, color: '#f5be3c', ...fix })
    board.create('point', [() => Q()[0], () => Q()[1]], { name: '', size: 4.5, color: '#fb7185', ...fix })
    board.create('text', [() => P()[0] - 0.25, () => P()[1] + 0.35, () => `(a, f(a))`], { color: '#f5be3c', ...cls('jx-gold'), fontSize: 12, anchorX: 'right', ...fix })
    board.create('text', [() => Q()[0] + 0.15, () => Q()[1] - 0.4, () => `(f(a), a)`], { color: '#fb7185', ...cls('jx-coral'), fontSize: 12, ...fix })
  }

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
  ro?.disconnect()
  const JXG = (window as any).JXG
  try { if (board) JXG?.JSXGraph.freeBoard(board) } catch (e) { /* ignore */ }
  board = null
})
</script>

<template>
  <div class="iv flex flex-col gap-2 w-full" :style="{ height: props.height }">
    <div :id="id" class="jxgbox iv-box"></div>
    <div class="iv-panel">
      <template v-if="props.mode === 'test'">
        <div class="iv-row">
          <span>f(x) =</span>
          <button v-for="(F, i) in FUNS" :key="F.key" type="button" class="iv-btn" :class="{ on: fsel === i }" @click="fsel = i">{{ String.fromCharCode(65 + i) }}. {{ F.label }}</button>
        </div>
        <label class="iv-row">
          <span>garis y = <b>{{ fmt(cv, 1) }}</b></span>
          <input type="range" min="-4" max="4" step="0.1" v-model.number="cv" />
        </label>
        <div class="iv-foot">
          <span class="iv-num">memotong grafik <b>{{ roots.length }}</b> kali</span>
          <label class="iv-check"><input type="checkbox" v-model="showVerdict" /> tampilkan kesimpulan</label>
          <span v-if="showVerdict" class="iv-num">{{ fun.label }}: <b :class="fun.inv ? 'ok' : 'no'">{{ fun.inv ? 'punya invers' : 'tidak punya invers' }}</b></span>
        </div>
      </template>
      <template v-else>
        <label class="iv-row">
          <span>a = <b>{{ fmt(av) }}</b></span>
          <input type="range" min="-1.3" max="1.3" step="0.05" v-model.number="av" />
        </label>
        <div class="iv-foot">
          <label class="iv-check"><input type="checkbox" v-model="showInv" /> tampilkan grafik f⁻¹</label>
          <label class="iv-check"><input type="checkbox" v-model="showSlope" /> tampilkan kemiringan</label>
        </div>
        <div v-if="showSlope" class="iv-num">kemiringan f di (a, f(a)) = <b class="gold">{{ fmt(m1) }}</b> · kemiringan f⁻¹ di (f(a), a) = <b class="coral">{{ fmt(m2) }}</b></div>
      </template>
    </div>
  </div>
</template>

<style>
.iv { font-size: 0.78rem; color: #e2e8f0; }
.iv-box { flex: 1 1 auto; min-height: 0; border-radius: 0.75rem; border: 1px solid #334155; overflow: hidden; background-color: #0c1018 !important; }
.iv .jxgbox svg { background-color: #0c1018 !important; }
.iv .jxgbox .JXGtext.jx-gold { color: #f5be3c !important; }
.iv .jxgbox .JXGtext.jx-coral { color: #fb7185 !important; }
.iv .jxgbox .JXGtext.jx-teal { color: #2dd4bf !important; }
.iv .jxgbox .JXGtext.jx-blue { color: #60a5fa !important; }
.iv .jxgbox .JXGtext.jx-muted { color: #94a3b8 !important; }
.iv-panel { background: #141b28; border: 1px solid #233148; border-radius: 0.75rem; padding: 0.4rem 0.7rem; display: flex; flex-direction: column; gap: 0.3rem; }
.iv-row { display: flex; align-items: center; gap: 0.5rem; }
.iv-row span { white-space: nowrap; color: #cbd5e1; font-family: ui-monospace, monospace; }
.iv-row b { color: #f5be3c; }
.iv-row input { flex: 1; accent-color: #f5be3c; min-width: 0; }
.iv-btn { background: #0c1018; color: #cbd5e1; border: 1px solid #334155; border-radius: 0.4rem; padding: 0.1rem 0.5rem; font-size: 0.74rem; cursor: pointer; white-space: nowrap; }
.iv-btn.on { border-color: #2dd4bf; color: #2dd4bf; background: rgba(45, 212, 191, 0.12); }
.iv-foot { display: flex; align-items: center; gap: 0.9rem; flex-wrap: wrap; }
.iv-check { display: flex; align-items: center; gap: 0.35rem; cursor: pointer; white-space: nowrap; }
.iv-check input { accent-color: #2dd4bf; }
.iv-num { font-family: ui-monospace, monospace; color: #cbd5e1; font-size: 0.7rem; }
.iv-num b { color: #fb7185; }
.iv-num b.ok { color: #34d399; }
.iv-num b.no { color: #fb7185; }
.iv-num b.gold { color: #f5be3c; }
.iv-num b.coral { color: #fb7185; }
</style>
