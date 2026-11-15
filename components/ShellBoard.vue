<script setup lang="ts">
/**
 * ShellBoard — cylindrical shell method, 2D "unrolling" applet (JSXGraph).
 *
 * Top board: region under y = f(x) on [0, b], rotated about the y-axis. One vertical strip at x
 * (width dx) is drawn, with its mirror image to hint at the rotation.
 * Bottom board: the shell that strip becomes, cut open and unrolled into a flat rectangle of
 * length 2*pi*x and height f(x) (thickness dx).
 *
 * Hidden until ticked (so the lecturer reveals after students answer):
 *   - "tampilkan ukuran": labels 2πx, f(x), Δx
 *   - "jumlahkan semua kulit": sum of n shells and the exact volume
 *
 * Default curve: f(x) = 2x^2 - x^3 on [0, 2], exact volume 16π/5.
 */
import { onMounted, onUnmounted, useId } from 'vue'

const props = withDefaults(defineProps<{
  height?: string
}>(), { height: '400px' })

const idTop = (useId ? useId() : 'sb' + Math.random().toString(36).slice(2, 8)) + '-top'
const idBot = idTop.replace('-top', '-bot')
let boards: any[] = []
let observers: ResizeObserver[] = []

const f = (x: number) => 2 * x * x - x * x * x
const B = 2
const EXACT = 16 * Math.PI / 5
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
  const common = { axis: false, showNavigation: false, showCopyright: false, keepaspectratio: false, pan: { enabled: false }, zoom: { enabled: false } }

  // ---------- top board: region and strip ----------
  const t = JXG.JSXGraph.initBoard(idTop, { ...common, boundingbox: [-2.7, 1.75, 2.7, -0.5] })
  t.create('axis', [[0, 0], [1, 0]], { strokeColor: '#64748b', ticks: { visible: false } })
  t.create('axis', [[0, 0], [0, 1]], { strokeColor: '#f5be3c', strokeWidth: 3, ticks: { visible: false } })
  t.create('text', [0.08, 1.62, 'sumbu putar'], { color: '#f5be3c', fontSize: 12, fixed: true })
  t.create('functiongraph', [f, 0, B], { strokeColor: '#50a5fa', strokeWidth: 3 })
  t.create('functiongraph', [(x: number) => f(-x), -B, 0], { strokeColor: '#50a5fa', strokeWidth: 2, dash: 2, highlight: false })
  const sx = t.create('slider', [[-2.5, -0.3], [-1.0, -0.3], [0.1, 1, 1.95]], { name: 'x', snapWidth: 0.05, size: 4, baseline: { strokeColor: '#475569' }, highline: { strokeColor: '#fb7185' }, fillColor: '#fb7185', strokeColor: '#fb7185', label: { strokeColor: '#e2e8f0' } })
  const sd = t.create('slider', [[0.2, -0.3], [1.5, -0.3], [0.05, 0.2, 0.5]], { name: 'Δx', snapWidth: 0.05, size: 4, baseline: { strokeColor: '#475569' }, highline: { strokeColor: '#2dd4bf' }, fillColor: '#2dd4bf', strokeColor: '#2dd4bf', label: { strokeColor: '#e2e8f0' } })
  const X = () => sx.Value()
  const W = () => Math.min(sd.Value(), B - sx.Value())
  const strip = (sign: number, dashed: boolean) => t.create('polygon', [
    [() => sign * X(), 0], [() => sign * (X() + W()), 0],
    [() => sign * (X() + W()), () => f(X())], [() => sign * X(), () => f(X())]
  ], { fillColor: sign > 0 ? '#fb7185' : '#fb7185', fillOpacity: sign > 0 ? 0.75 : 0.25, borders: { strokeColor: '#fb7185', strokeWidth: 1, dash: dashed ? 2 : 0 }, vertices: { visible: false }, highlight: false, fixed: true })
  strip(1, false); strip(-1, true)

  // ---------- bottom board: unrolled shell ----------
  const u = JXG.JSXGraph.initBoard(idBot, { ...common, boundingbox: [-1.2, 2.35, 13.8, -1.7] })
  u.create('polygon', [
    [0, 0], [() => 2 * Math.PI * X(), 0], [() => 2 * Math.PI * X(), () => f(X())], [0, () => f(X())]
  ], { fillColor: '#fb7185', fillOpacity: 0.55, borders: { strokeColor: '#fb7185', strokeWidth: 2 }, vertices: { visible: false }, highlight: false, fixed: true })
  u.create('text', [0.1, 2.1, () => 'Kulit dibentangkan:  ΔV ≈ ' + fmt(2 * Math.PI * X() * f(X()) * W(), 3)], { fontSize: 14, color: '#e2e8f0', fixed: true })

  const showDim = u.create('checkbox', [9.0, 2.1, 'tampilkan ukuran'], { fontSize: 12 })
  const showSum = u.create('checkbox', [9.0, 1.6, 'jumlahkan semua kulit'], { fontSize: 12 })
  const vis = (cb: any) => () => cb.Value()
  u.create('text', [() => Math.PI * X(), -0.28, '2πx'], { anchorX: 'middle', fontSize: 14, color: '#f5be3c', visible: vis(showDim), fixed: true })
  u.create('text', [() => 2 * Math.PI * X() + 0.15, () => f(X()) / 2, 'f(x)'], { fontSize: 14, color: '#2dd4bf', visible: vis(showDim), fixed: true })
  u.create('text', [() => 2 * Math.PI * X() + 0.15, () => f(X()) + 0.08, () => 'tebal Δx = ' + fmt(W(), 2)], { fontSize: 12, color: '#94a3b8', visible: vis(showDim), fixed: true })

  const sn = u.create('slider', [[0.2, -1.3], [5.2, -1.3], [1, 4, 40]], { name: 'n', snapWidth: 1, digits: 0, size: 4, baseline: { strokeColor: '#475569' }, fillColor: '#50a5fa', strokeColor: '#50a5fa', visible: vis(showSum), label: { strokeColor: '#e2e8f0' } })
  const shellSum = () => {
    const n = Math.round(sn.Value()); const d = B / n; let s = 0
    for (let i = 0; i < n; i++) { const xm = (i + 0.5) * d; s += 2 * Math.PI * xm * f(xm) * d }
    return s
  }
  u.create('text', [0.2, -0.85, () => 'Σ ' + Math.round(sn.Value()) + ' kulit ≈ ' + fmt(shellSum(), 3) + '    eksak 16π/5 ≈ ' + fmt(EXACT, 3)], { fontSize: 13, color: '#34d399', visible: vis(showSum), fixed: true })

  boards = [t, u]
  for (const id of [idTop, idBot]) {
    const el = document.getElementById(id)
    if (el && typeof ResizeObserver !== 'undefined') {
      const ro = new ResizeObserver(() => boards.forEach(b => { const c = b.containerObj; b.resizeContainer(c.clientWidth, c.clientHeight, true); b.update() }))
      ro.observe(el); observers.push(ro)
    }
  }
})

onUnmounted(() => {
  observers.forEach(o => o.disconnect()); observers = []
  const JXG = (window as any).JXG
  boards.forEach(b => { try { JXG?.JSXGraph.freeBoard(b) } catch (e) { /* ignore */ } })
  boards = []
})
</script>

<template>
  <div class="flex flex-col gap-2" :style="{ height: props.height }">
    <div :id="idTop" class="jxgbox rounded-xl border border-slate-700/70 overflow-hidden bg-[#0c1018]" style="flex: 1 1 48%; min-height: 0;"></div>
    <div :id="idBot" class="jxgbox rounded-xl border border-slate-700/70 overflow-hidden bg-[#0c1018]" style="flex: 1 1 52%; min-height: 0;"></div>
  </div>
</template>

<style>
.jxgbox { background-color: #0c1018 !important; }
.jxgbox svg { background-color: #0c1018 !important; }
.jxgbox .JXGtext, .jxgbox .JXGtext * { color: #e2e8f0 !important; }
.jxgbox label { color: #e2e8f0 !important; }
</style>
