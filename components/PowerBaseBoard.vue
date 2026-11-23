<script setup lang="ts">
/**
 * PowerBaseBoard — y = aˣ for any base a > 0 (JSXGraph 2D), Subtopik 6.4.
 *
 * Two sliders: the base a and the point x. The board draws y = aˣ (gold), a faint reference
 * y = eˣ, the tangent at (x, aˣ) and the slope triangle "1 ke kanan, naik …". The numbers
 * (height aˣ, measured slope, slope ÷ height, and ln a) appear only after "tampilkan angka"
 * is ticked, so the room predicts first. The punchline: slope ÷ height is the same for every
 * x and equals ln a; it is 1 exactly when a = e.
 */
import { ref, computed, onMounted, onUnmounted, watch } from 'vue'

const props = withDefaults(defineProps<{ height?: string; initialA?: number }>(), { height: '360px', initialA: 2 })

const id = `jxg-powbase-${Math.random().toString(36).slice(2, 9)}`
const fmt = (v: number, d = 2) => v.toFixed(d).replace('.', ',').replace('-', '−')

const av = ref(props.initialA)
const xv = ref(0)
const showNum = ref(false)
const f = (x: number) => Math.pow(av.value, x)
const height = computed(() => f(xv.value))
const slope = computed(() => { const h = 1e-4; return (f(xv.value + h) - f(xv.value - h)) / (2 * h) })
const ratio = computed(() => slope.value / height.value)

let board: any = null
let ro: ResizeObserver | null = null

watch([av, xv, showNum], () => board?.update())

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
  const tick = { strokeColor: '#334155', label: { strokeColor: '#94a3b8', fontSize: 10 }, minorTicks: 0 }
  board = JXG.JSXGraph.initBoard(id, {
    boundingbox: [-2.6, 6.4, 2.6, -0.9], axis: true, showNavigation: false, showCopyright: false,
    keepaspectratio: false, pan: { enabled: false }, zoom: { enabled: false },
    defaultAxes: { x: { strokeColor: '#475569', ticks: tick }, y: { strokeColor: '#475569', ticks: tick } }
  })
  board.create('functiongraph', [(x: number) => Math.exp(x), -2.6, 1.9], { strokeColor: '#64748b', strokeWidth: 1.5, dash: 2, ...fix })
  board.create('text', [1.45, 5.9, 'eˣ'], { ...cls('jx-muted'), fontSize: 12, ...fix })
  board.create('functiongraph', [f, -2.6, 2.6], { strokeColor: '#f5be3c', strokeWidth: 3, ...fix })
  board.create('text', [-2.45, 5.9, () => `y = ${fmt(av.value)}ˣ`], { ...cls('jx-gold'), fontSize: 13, ...fix })
  const X = () => xv.value
  const Y = () => f(xv.value)
  const S = () => slope.value
  board.create('line', [[X, Y], [() => X() + 1, () => Y() + S()]], { strokeColor: '#cbd5e1', strokeWidth: 1.5, ...fix })
  board.create('segment', [[X, 0], [X, Y]], { strokeColor: '#2dd4bf', strokeWidth: 3.5, ...fix })
  board.create('text', [() => X() - 0.1, () => Y() / 2, 'tinggi'], { ...cls('jx-teal'), fontSize: 12, anchorX: 'right', anchorY: 'middle', ...fix })
  board.create('segment', [[X, Y], [() => X() + 1, Y]], { strokeColor: '#fb7185', strokeWidth: 2, ...fix })
  board.create('segment', [[() => X() + 1, Y], [() => X() + 1, () => Y() + S()]], { strokeColor: '#fb7185', strokeWidth: 3, dash: 2, ...fix })
  board.create('text', [() => X() + 0.5, () => Y() - 0.28, '1'], { ...cls('jx-coral'), fontSize: 12, anchorX: 'middle', ...fix })
  board.create('text', [() => X() + 1.08, () => Y() + S() / 2, 'naik'], { ...cls('jx-coral'), fontSize: 12, anchorY: 'middle', ...fix })
  board.create('point', [X, Y], { name: '', size: 4.5, color: '#f5be3c', ...fix })

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
  <div class="pb flex flex-col gap-2 w-full" :style="{ height: props.height }">
    <div :id="id" class="jxgbox pb-box"></div>
    <div class="pb-panel">
      <label class="pb-row">
        <span>alas a = <b>{{ fmt(av) }}</b></span>
        <input type="range" min="0.3" max="4" step="0.05" v-model.number="av" />
      </label>
      <label class="pb-row">
        <span>titik x = <b>{{ fmt(xv) }}</b></span>
        <input type="range" min="-2" max="1.2" step="0.05" v-model.number="xv" />
      </label>
      <div class="pb-foot">
        <label class="pb-check"><input type="checkbox" v-model="showNum" /> tampilkan angka</label>
        <span v-if="showNum" class="pb-num">tinggi = <b class="teal">{{ fmt(height, 3) }}</b> · kemiringan = <b>{{ fmt(slope, 3) }}</b> · kemiringan ÷ tinggi = <b class="gold">{{ fmt(ratio, 3) }}</b> · ln a = <b class="gold">{{ fmt(Math.log(av), 3) }}</b></span>
        <span v-else class="pb-legend"><i class="sw sw-t"></i> tinggi &nbsp; <i class="sw sw-c"></i> naik sejauh 1 ke kanan &nbsp; <i class="sw sw-m"></i> eˣ</span>
      </div>
    </div>
  </div>
</template>

<style>
.pb { font-size: 0.78rem; color: #e2e8f0; }
.pb-box { flex: 1 1 auto; min-height: 0; border-radius: 0.75rem; border: 1px solid #334155; overflow: hidden; background-color: #0c1018 !important; }
.pb .jxgbox svg { background-color: #0c1018 !important; }
.pb .jxgbox .JXGtext.jx-gold { color: #f5be3c !important; }
.pb .jxgbox .JXGtext.jx-coral { color: #fb7185 !important; }
.pb .jxgbox .JXGtext.jx-teal { color: #2dd4bf !important; }
.pb .jxgbox .JXGtext.jx-muted { color: #94a3b8 !important; }
.pb-panel { background: #141b28; border: 1px solid #233148; border-radius: 0.75rem; padding: 0.4rem 0.7rem; display: flex; flex-direction: column; gap: 0.25rem; }
.pb-row { display: flex; align-items: center; gap: 0.5rem; }
.pb-row span { white-space: nowrap; color: #cbd5e1; font-family: ui-monospace, monospace; min-width: 7.5rem; }
.pb-row b { color: #fb7185; }
.pb-row input { flex: 1; accent-color: #fb7185; min-width: 0; }
.pb-foot { display: flex; align-items: center; gap: 0.9rem; flex-wrap: wrap; }
.pb-check { display: flex; align-items: center; gap: 0.35rem; cursor: pointer; white-space: nowrap; }
.pb-check input { accent-color: #f5be3c; }
.pb-num { font-family: ui-monospace, monospace; color: #cbd5e1; font-size: 0.68rem; }
.pb-num b { color: #fb7185; }
.pb-num b.teal { color: #2dd4bf; }
.pb-num b.gold { color: #f5be3c; }
.pb-legend { color: #94a3b8; display: flex; align-items: center; gap: 0.3rem; font-size: 0.7rem; }
.pb .sw { display: inline-block; width: 0.9rem; height: 0.3rem; border-radius: 2px; }
.pb .sw-t { background: #2dd4bf; }
.pb .sw-c { background: #fb7185; }
.pb .sw-m { background: #64748b; }
</style>
