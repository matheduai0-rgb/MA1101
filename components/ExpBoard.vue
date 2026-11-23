<script setup lang="ts">
/**
 * ExpBoard — the natural exponential function (JSXGraph 2D).
 *
 * mode="reflect" : y = ln x and y = eˣ, mirror line y = x, the fixed pairs (1, 0)/(0, 1) and
 *                  (e, 1)/(1, e), and a slider s moving the mirror pair (s, eˢ)/(eˢ, s). The two
 *                  asymptotes appear only after "tampilkan asimtot" is ticked (they are the guess).
 * mode="slope"   : y = eˣ with a slider x, the tangent line at (x, eˣ), the height from the x-axis and
 *                  the slope triangle "1 ke kanan, naik …". The numbers (height and a measured slope,
 *                  central difference) appear only after "tampilkan angka" is ticked.
 */
import { ref, computed, onMounted, onUnmounted, watch } from 'vue'

const props = withDefaults(defineProps<{ mode?: 'reflect' | 'slope'; height?: string }>(),
  { mode: 'reflect', height: '360px' })

const id = `jxg-exp-${Math.random().toString(36).slice(2, 9)}`
const fmt = (v: number, d = 2) => v.toFixed(d).replace('.', ',').replace('-', '−')
const E = Math.E

const sv = ref(0.5)
const showAsym = ref(false)
const xv = ref(1)
const showNum = ref(false)
const height = computed(() => Math.exp(xv.value))
const slope = computed(() => { const h = 1e-4; return (Math.exp(xv.value + h) - Math.exp(xv.value - h)) / (2 * h) })

let board: any = null
let ro: ResizeObserver | null = null

watch([sv, showAsym, xv, showNum], () => board?.update())

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

  if (props.mode === 'reflect') {
    board = JXG.JSXGraph.initBoard(id, {
      boundingbox: [-3.6, 4.2, 4.6, -3.6], axis: true, defaultAxes: axes, showNavigation: false, showCopyright: false,
      keepaspectratio: true, pan: { enabled: false }, zoom: { enabled: false }
    })
    board.create('line', [[0, 0], [1, 1]], { strokeColor: '#64748b', strokeWidth: 1.5, dash: 2, ...fix })
    board.create('text', [3.2, 3.75, 'y = x'], { color: '#94a3b8', ...cls('jx-muted'), fontSize: 12, ...fix })
    board.create('functiongraph', [(x: number) => Math.exp(x), -3.6, 1.5], { strokeColor: '#f5be3c', strokeWidth: 3, ...fix })
    board.create('text', [-2.9, 1.0, 'y = eˣ'], { color: '#f5be3c', ...cls('jx-gold'), fontSize: 13, ...fix })
    board.create('functiongraph', [(x: number) => Math.log(x), 0.02, 4.6], { strokeColor: '#2dd4bf', strokeWidth: 3, ...fix })
    board.create('text', [3.3, 1.75, 'y = ln x'], { color: '#2dd4bf', ...cls('jx-teal'), fontSize: 13, ...fix })
    // fixed pairs
    const pair = (a: number[], b: number[], la: string, lb: string, oa: number[], ob: number[]) => {
      board.create('segment', [a, b], { strokeColor: '#334155', strokeWidth: 1, dash: 1, ...fix })
      board.create('point', a, { name: '', size: 3.5, color: '#2dd4bf', ...fix })
      board.create('point', b, { name: '', size: 3.5, color: '#f5be3c', ...fix })
      board.create('text', [a[0] + oa[0], a[1] + oa[1], la], { color: '#2dd4bf', ...cls('jx-teal'), fontSize: 11, ...fix })
      board.create('text', [b[0] + ob[0], b[1] + ob[1], lb], { color: '#f5be3c', ...cls('jx-gold'), fontSize: 11, ...fix })
    }
    pair([1, 0], [0, 1], '(1, 0)', '(0, 1)', [0.1, -0.4], [-1.05, 0.25])
    pair([E, 1], [1, E], '(e, 1)', '(1, e)', [0.12, -0.38], [-1.05, 0.2])
    // moving mirror pair
    const P = () => [sv.value, Math.exp(sv.value)]
    const Q = () => [Math.exp(sv.value), sv.value]
    board.create('segment', [[() => P()[0], () => P()[1]], [() => Q()[0], () => Q()[1]]], { strokeColor: '#fb7185', strokeWidth: 1.5, dash: 2, ...fix })
    board.create('point', [() => P()[0], () => P()[1]], { name: '', size: 5, color: '#fb7185', ...fix })
    board.create('point', [() => Q()[0], () => Q()[1]], { name: '', size: 5, color: '#fb7185', ...fix })
    // asymptotes (hidden until ticked)
    board.create('line', [[0, 0], [1, 0]], { strokeColor: '#f5be3c', strokeWidth: 2, dash: 3, strokeOpacity: 0.8, visible: () => showAsym.value, ...fix })
    board.create('line', [[0, 0], [0, 1]], { strokeColor: '#2dd4bf', strokeWidth: 2, dash: 3, strokeOpacity: 0.8, visible: () => showAsym.value, ...fix })
    board.create('text', [-3.4, -0.45, 'asimtot eˣ: y = 0'], { color: '#f5be3c', ...cls('jx-gold'), fontSize: 11, visible: () => showAsym.value, ...fix })
    board.create('text', [0.12, -3.1, 'asimtot ln x: x = 0'], { color: '#2dd4bf', ...cls('jx-teal'), fontSize: 11, visible: () => showAsym.value, ...fix })
  } else {
    board = JXG.JSXGraph.initBoard(id, {
      boundingbox: [-2.6, 6.4, 2.9, -0.9], axis: true, defaultAxes: axes, showNavigation: false, showCopyright: false,
      keepaspectratio: false, pan: { enabled: false }, zoom: { enabled: false }
    })
    board.create('functiongraph', [(x: number) => Math.exp(x), -2.6, 2.9], { strokeColor: '#f5be3c', strokeWidth: 3, ...fix })
    board.create('text', [-2.3, 1.15, 'y = eˣ'], { color: '#f5be3c', ...cls('jx-gold'), fontSize: 13, ...fix })
    const X = () => xv.value
    const Y = () => Math.exp(xv.value)
    // tangent line through (X, Y) with slope Y
    board.create('line', [[X, Y], [() => X() + 1, () => Y() + Y()]], { strokeColor: '#cbd5e1', strokeWidth: 1.5, straightFirst: true, straightLast: true, ...fix })
    // height
    board.create('segment', [[X, 0], [X, Y]], { strokeColor: '#2dd4bf', strokeWidth: 3.5, ...fix })
    board.create('text', [() => X() - 0.12, () => Y() / 2, 'tinggi'], { color: '#2dd4bf', ...cls('jx-teal'), fontSize: 12, anchorX: 'right', anchorY: 'middle', ...fix })
    // slope triangle: 1 to the right, rise Y
    board.create('segment', [[X, Y], [() => X() + 1, Y]], { strokeColor: '#fb7185', strokeWidth: 2, ...fix })
    board.create('segment', [[() => X() + 1, Y], [() => X() + 1, () => 2 * Y()]], { strokeColor: '#2dd4bf', strokeWidth: 3.5, dash: 2, ...fix })
    board.create('text', [() => X() + 0.5, () => Y() - 0.3, '1'], { color: '#fb7185', ...cls('jx-coral'), fontSize: 12, anchorX: 'middle', ...fix })
    board.create('text', [() => X() + 1.1, () => 1.5 * Y(), 'naik'], { color: '#2dd4bf', ...cls('jx-teal'), fontSize: 12, anchorY: 'middle', ...fix })
    board.create('point', [X, Y], { name: '', size: 4.5, color: '#f5be3c', ...fix })
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
  <div class="ex flex flex-col gap-2 w-full" :style="{ height: props.height }">
    <div :id="id" class="jxgbox ex-box"></div>
    <div class="ex-panel">
      <template v-if="props.mode === 'reflect'">
        <label class="ex-row">
          <span>titik cermin s = <b>{{ fmt(sv) }}</b></span>
          <input type="range" min="-3" max="1.4" step="0.05" v-model.number="sv" />
        </label>
        <div class="ex-foot">
          <span class="ex-num">(s, eˢ) = (<b>{{ fmt(sv) }}</b>; <b>{{ fmt(Math.exp(sv)) }}</b>) ↔ (eˢ, s) = (<b>{{ fmt(Math.exp(sv)) }}</b>; <b>{{ fmt(sv) }}</b>)</span>
          <label class="ex-check"><input type="checkbox" v-model="showAsym" /> tampilkan asimtot</label>
        </div>
      </template>
      <template v-else>
        <label class="ex-row">
          <span>x = <b>{{ fmt(xv) }}</b></span>
          <input type="range" min="-2" max="1.1" step="0.05" v-model.number="xv" />
        </label>
        <div class="ex-foot">
          <label class="ex-check"><input type="checkbox" v-model="showNum" /> tampilkan angka</label>
          <span v-if="showNum" class="ex-num">tinggi eˣ = <b class="teal">{{ fmt(height, 3) }}</b> · kemiringan garis singgung = <b class="teal">{{ fmt(slope, 3) }}</b></span>
          <span v-else class="ex-legend"><i class="sw sw-t"></i> tinggi &nbsp; <i class="sw sw-c"></i> 1 ke kanan &nbsp; <i class="sw sw-t sw-d"></i> naiknya garis singgung</span>
        </div>
      </template>
    </div>
  </div>
</template>

<style>
.ex { font-size: 0.78rem; color: #e2e8f0; }
.ex-box { flex: 1 1 auto; min-height: 0; border-radius: 0.75rem; border: 1px solid #334155; overflow: hidden; background-color: #0c1018 !important; }
.ex .jxgbox svg { background-color: #0c1018 !important; }
.ex .jxgbox .JXGtext.jx-gold { color: #f5be3c !important; }
.ex .jxgbox .JXGtext.jx-coral { color: #fb7185 !important; }
.ex .jxgbox .JXGtext.jx-teal { color: #2dd4bf !important; }
.ex .jxgbox .JXGtext.jx-muted { color: #94a3b8 !important; }
.ex-panel { background: #141b28; border: 1px solid #233148; border-radius: 0.75rem; padding: 0.4rem 0.7rem; display: flex; flex-direction: column; gap: 0.3rem; }
.ex-row { display: flex; align-items: center; gap: 0.5rem; }
.ex-row span { white-space: nowrap; color: #cbd5e1; font-family: ui-monospace, monospace; }
.ex-row b { color: #fb7185; }
.ex-row input { flex: 1; accent-color: #fb7185; min-width: 0; }
.ex-foot { display: flex; align-items: center; gap: 0.9rem; flex-wrap: wrap; }
.ex-check { display: flex; align-items: center; gap: 0.35rem; cursor: pointer; white-space: nowrap; }
.ex-check input { accent-color: #2dd4bf; }
.ex-num { font-family: ui-monospace, monospace; color: #cbd5e1; font-size: 0.7rem; }
.ex-num b { color: #fb7185; }
.ex-num b.teal { color: #2dd4bf; }
.ex-legend { color: #94a3b8; display: flex; align-items: center; gap: 0.3rem; font-size: 0.7rem; }
.ex .sw { display: inline-block; width: 0.9rem; height: 0.3rem; border-radius: 2px; }
.ex .sw-t { background: #2dd4bf; }
.ex .sw-c { background: #fb7185; }
.ex .sw-d { opacity: 0.6; }
</style>
