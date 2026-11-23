<script setup lang="ts">
/**
 * LnAreaBoard — the natural logarithm as an area under y = 1/t (JSXGraph 2D).
 *
 * mode="area"  : slider x; region between t = 1 and t = x is shaded (green for x > 1, coral for
 *                x < 1, i.e. signed area). Readout L(x) = ∫_1^x dt/t. Hidden checkbox draws the
 *                graph of L(x) and the point (x, L(x)).
 * mode="scale" : sliders a, b; shades the area from 1 to a (green) and from b to ab (blue).
 *                The two numbers appear only after ticking "tampilkan luas", so students guess first.
 * mode="graph" : the graph of y = ln x with the vertical asymptote x = 0, the point (1, 0), a point
 *                on the curve moved by slider x (readout ln x), and an optional tangent y = x - 1.
 */
import { onMounted, onUnmounted, useId } from 'vue'

const props = withDefaults(defineProps<{
  mode?: 'area' | 'scale' | 'graph'
  height?: string
}>(), { mode: 'area', height: '340px' })

const id = useId ? useId() : 'ln' + Math.random().toString(36).slice(2, 8)
let board: any = null
let ro: ResizeObserver | null = null
const fmt = (v: number, d = 3) => v.toFixed(d).replace('.', ',').replace('-', '−')
const inv = (t: number) => 1 / t

onMounted(async () => {
  const mod = await import('jsxgraph')
  const JXG = (mod as any).default || (window as any).JXG || mod
  if (!document.getElementById('jsxgraph-css')) {
    const link = document.createElement('link')
    link.id = 'jsxgraph-css'
    link.rel = 'stylesheet'
    link.href = 'https://cdn.jsdelivr.net/npm/jsxgraph/distrib/jsxgraph.css'
    document.head.appendChild(link)
  }
  const tickLabel = { label: { strokeColor: '#94a3b8' } }
  const sliderStyle = (c: string) => ({
    size: 4, baseline: { strokeColor: '#475569' }, highline: { strokeColor: c },
    fillColor: c, strokeColor: c, label: { strokeColor: '#e2e8f0' }
  })
  // region under 1/t between t0 and t1 (works for t1 < t0 too)
  const region = (b: any, t0: () => number, t1: () => number, attr: any) => {
    const c = b.create('curve', [[], []], { fillOpacity: 0.45, strokeWidth: 1.2, highlight: false, ...attr })
    c.updateDataArray = function () {
      const a = t0(), e = t1(), n = 60
      const xs = [a], ys = [0]
      for (let i = 0; i <= n; i++) { const t = a + (e - a) * i / n; xs.push(t); ys.push(inv(t)) }
      xs.push(e, a); ys.push(0, 0)
      this.dataX = xs; this.dataY = ys
    }
    return c
  }

  if (props.mode === 'area') {
    board = JXG.JSXGraph.initBoard(id, {
      boundingbox: [-0.6, 3.5, 6.9, -2.3], axis: true, showNavigation: false, showCopyright: false,
      keepaspectratio: false, pan: { enabled: false }, zoom: { enabled: false },
      defaultAxes: { x: { ticks: tickLabel }, y: { ticks: tickLabel } }
    })
    board.create('functiongraph', [inv, 0.29, 6.4], { strokeColor: '#50a5fa', strokeWidth: 3 })
    board.create('text', [0.32, 3.25, 'y = 1/t'], { color: '#50a5fa', fontSize: 14, fixed: true })
    const sx = board.create('slider', [[2.4, -1.85], [5.6, -1.85], [0.2, 2, 6]], { name: 'x', snapWidth: 0.05, withLabel: false, ...sliderStyle('#f5be3c') })
    board.create('text', [5.75, -1.85, () => 'x = ' + fmt(sx.Value(), 2)], { fontSize: 14, color: '#f5be3c', anchorY: 'middle', fixed: true })
    const X = () => sx.Value()
    region(board, () => 1, X, {
      fillColor: () => (X() >= 1 ? '#34d399' : '#fb7185'),
      strokeColor: () => (X() >= 1 ? '#34d399' : '#fb7185')
    })
    board.create('segment', [[1, 0], [1, 1]], { strokeColor: '#94a3b8', dash: 2, strokeWidth: 1, fixed: true, highlight: false })
    board.create('text', [1.04, -0.45, 't = 1'], { color: '#94a3b8', fontSize: 12, fixed: true })
    board.create('text', [2.4, 3.15, () => 'L(x) = ∫ dari 1 sampai x  ≈ ' + fmt(Math.log(X()))], { fontSize: 15, color: '#e2e8f0', fixed: true })
    const show = board.create('checkbox', [2.4, 2.7, 'tampilkan grafik L(x)'], { fontSize: 13 })
    const vis = () => show.Value()
    board.create('functiongraph', [Math.log, 0.2, 6.4], { strokeColor: '#f5be3c', strokeWidth: 2.5, dash: 2, visible: vis, highlight: false })
    board.create('point', [X, () => Math.log(X())], { name: '', size: 4, color: '#f5be3c', fixed: true, visible: vis })
  } else if (props.mode === 'graph') {
    board = JXG.JSXGraph.initBoard(id, {
      boundingbox: [-1.2, 3.2, 8.6, -4.2], axis: true, showNavigation: false, showCopyright: false,
      keepaspectratio: false, pan: { enabled: false }, zoom: { enabled: false },
      defaultAxes: { x: { ticks: tickLabel }, y: { ticks: tickLabel } }
    })
    board.create('segment', [[0, -4.2], [0, 3.2]], { strokeColor: '#fb7185', strokeWidth: 2.5, dash: 3, fixed: true, highlight: false })
    board.create('text', [0.15, -3.6, 'asimtot tegak x = 0'], { color: '#fb7185', fontSize: 13, fixed: true })
    board.create('functiongraph', [Math.log, 0.015, 8.5], { strokeColor: '#50a5fa', strokeWidth: 3 })
    board.create('text', [6.9, 1.45, 'y = ln x'], { color: '#50a5fa', fontSize: 15, fixed: true })
    board.create('point', [1, 0], { name: '(1, 0)', size: 4, color: '#f5be3c', fixed: true, label: { offset: [6, -14], strokeColor: '#f5be3c' } })
    const show = board.create('checkbox', [3.3, 2.75, 'garis singgung di (1, 0)'], { fontSize: 13 })
    const vis = () => show.Value()
    board.create('line', [[1, 0], [2, 1]], { strokeColor: '#34d399', strokeWidth: 2, dash: 2, visible: vis, highlight: false, fixed: true })
    board.create('text', [3.3, 2.3, 'kemiringan 1, sebab ln′(1) = 1'], { color: '#34d399', fontSize: 13, visible: vis, fixed: true })
    const sx = board.create('slider', [[3.3, -2.6], [7.4, -2.6], [0.1, 4, 8]], { name: 'x', snapWidth: 0.01, withLabel: false, ...sliderStyle('#f5be3c') })
    const X = () => sx.Value()
    board.create('segment', [[X, 0], [X, () => Math.log(X())]], { strokeColor: '#f5be3c', dash: 2, strokeWidth: 1.2, fixed: true, highlight: false })
    board.create('point', [X, () => Math.log(X())], { name: '', size: 4, color: '#f5be3c', fixed: true })
    board.create('text', [3.3, -3.2, () => 'x = ' + fmt(X(), 2) + '    ln x ≈ ' + fmt(Math.log(X()))], { fontSize: 14, color: '#f5be3c', fixed: true })
  } else {
    board = JXG.JSXGraph.initBoard(id, {
      boundingbox: [-1.0, 2.5, 9.7, -0.85], axis: true, showNavigation: false, showCopyright: false,
      keepaspectratio: false, pan: { enabled: false }, zoom: { enabled: false },
      defaultAxes: { x: { ticks: tickLabel }, y: { ticks: tickLabel } }
    })
    board.create('functiongraph', [inv, 0.42, 9.6], { strokeColor: '#50a5fa', strokeWidth: 3 })
    const sa = board.create('slider', [[0.3, -0.6], [3.3, -0.6], [1.5, 2, 3]], { name: 'a', snapWidth: 0.25, withLabel: false, ...sliderStyle('#34d399') })
    const sb = board.create('slider', [[5.0, -0.6], [8.0, -0.6], [1, 2, 3]], { name: 'b', snapWidth: 0.25, withLabel: false, ...sliderStyle('#50a5fa') })
    const A = () => sa.Value(), Bv = () => sb.Value()
    board.create('text', [3.5, -0.6, () => 'a = ' + fmt(A(), 2)], { fontSize: 13, color: '#34d399', anchorY: 'middle', fixed: true })
    board.create('text', [8.2, -0.6, () => 'b = ' + fmt(Bv(), 2)], { fontSize: 13, color: '#93c5fd', anchorY: 'middle', fixed: true })
    region(board, () => 1, A, { fillColor: '#34d399', strokeColor: '#34d399' })
    region(board, Bv, () => A() * Bv(), { fillColor: '#60a5fa', strokeColor: '#93c5fd', fillOpacity: 0.4 })
    board.create('text', [() => (1 + A()) / 2, 0.75, '1 → a'], { anchorX: 'middle', color: '#34d399', fontSize: 12, fixed: true })
    board.create('text', [() => (Bv() + A() * Bv()) / 2, () => 1.15 / Bv() + 0.12, 'b → ab'], { anchorX: 'middle', color: '#93c5fd', fontSize: 12, fixed: true })
    const show = board.create('checkbox', [4.2, 2.25, 'tampilkan luas'], { fontSize: 13 })
    const vis = () => show.Value()
    board.create('text', [4.2, 1.9, () => 'luas dari 1 sampai a  ≈ ' + fmt(Math.log(A()))], { fontSize: 14, color: '#34d399', visible: vis, fixed: true })
    board.create('text', [4.2, 1.6, () => 'luas dari b sampai ab ≈ ' + fmt(Math.log(A() * Bv()) - Math.log(Bv()))], { fontSize: 14, color: '#93c5fd', visible: vis, fixed: true })
  }

  const el = document.getElementById(id)
  if (el) (el as any).__jxgBoard = board   // handle for automated checks
  if (el && typeof ResizeObserver !== 'undefined') {
    ro = new ResizeObserver(() => { board.resizeContainer(el.clientWidth, el.clientHeight, true); board.update() })
    ro.observe(el)
  }
})

onUnmounted(() => {
  ro?.disconnect(); ro = null
  const JXG = (window as any).JXG
  try { if (board) JXG?.JSXGraph.freeBoard(board) } catch (e) { /* ignore */ }
  board = null
})
</script>

<template>
  <div :id="id" class="jxgbox rounded-xl border border-slate-700/70 shadow-2xl overflow-hidden bg-[#0c1018]" :style="{ width: '100%', height: props.height }"></div>
</template>

<style>
.jxgbox { background-color: #0c1018 !important; }
.jxgbox svg { background-color: #0c1018 !important; }
.jxgbox .JXGtext, .jxgbox .JXGtext * { color: #e2e8f0 !important; }
.jxgbox label { color: #e2e8f0 !important; }
</style>
