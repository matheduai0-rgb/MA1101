<script setup lang="ts">
/**
 * WorkForceBoard — work as area under the force-position graph (JSXGraph).
 *
 * F(x) = k x (spring), x from 0 to b. The slider n cuts [0, b] into n pieces; on each piece the
 * force is treated as constant (value at the left end), so each rectangle is the work on that piece.
 * Hidden until ticked: the exact area (triangle) and its value, so students predict first.
 *
 * Defaults: k = 100 N/m, b = 0.3 m  ->  exact W = k b^2 / 2 = 4.5 J.
 */
import { onMounted, onUnmounted, useId } from 'vue'

const props = withDefaults(defineProps<{
  k?: number
  b?: number
  initialN?: number
  height?: string
}>(), { k: 100, b: 0.3, initialN: 3, height: '330px' })

const id = useId ? useId() : 'wf' + Math.random().toString(36).slice(2, 8)
let board: any = null
let ro: ResizeObserver | null = null
const fmt = (v: number, d = 2) => v.toFixed(d).replace('.', ',')

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
  const { k, b } = props
  const Fmax = k * b
  board = JXG.JSXGraph.initBoard(id, {
    boundingbox: [-0.12 * b, Fmax * 1.45, b * 1.18, -Fmax * 0.28],
    defaultAxes: { x: { ticks: { label: { strokeColor: '#94a3b8' } } }, y: { ticks: { label: { strokeColor: '#94a3b8' } } } },
    axis: true, showNavigation: false, showCopyright: false, keepaspectratio: false,
    pan: { enabled: false }, zoom: { enabled: false }
  })
  const F = (x: number) => k * x
  board.create('functiongraph', [F, 0, b * 1.05], { strokeColor: '#50a5fa', strokeWidth: 3 })
  board.create('text', [b * 1.02, Fmax * 1.08, 'F(x)'], { color: '#50a5fa', fontSize: 14, fixed: true })
  board.create('text', [b * 1.0, -Fmax * 0.1, 'x (m)'], { color: '#94a3b8', fontSize: 12, fixed: true })

  const sn = board.create('slider', [[b * 0.05, -Fmax * 0.2], [b * 0.6, -Fmax * 0.2], [1, props.initialN, 30]], {
    name: 'n', snapWidth: 1, digits: 0, size: 4, baseline: { strokeColor: '#475569' }, fillColor: '#f5be3c', strokeColor: '#f5be3c', label: { strokeColor: '#e2e8f0' }
  })
  const N = () => Math.round(sn.Value())
  board.create('riemannsum', [F, N, 'left', 0, b], { fillColor: '#fb7185', fillOpacity: 0.45, strokeColor: '#fb7185', strokeWidth: 1 })
  const sum = () => { const n = N(); const d = b / n; let s = 0; for (let i = 0; i < n; i++) s += F(i * d) * d; return s }
  board.create('text', [b * 0.04, Fmax * 1.32, () => 'Jumlah usaha tiap potongan = ' + fmt(sum(), 3) + ' J'], { fontSize: 15, color: '#e2e8f0', fixed: true })

  const show = board.create('checkbox', [b * 0.04, Fmax * 1.17, 'tampilkan usaha sebenarnya'], { fontSize: 13 })
  const vis = () => show.Value()
  board.create('polygon', [[0, 0], [b, 0], [b, Fmax]], { fillColor: '#34d399', fillOpacity: 0.18, borders: { strokeColor: '#34d399', strokeWidth: 2, dash: 2 }, vertices: { visible: false }, visible: vis, highlight: false, fixed: true })
  board.create('text', [b * 0.04, Fmax * 1.02, () => 'W sebenarnya = ' + fmt(k * b * b / 2, 3) + ' J'], { fontSize: 14, color: '#34d399', visible: vis, fixed: true })

  const el = document.getElementById(id)
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
