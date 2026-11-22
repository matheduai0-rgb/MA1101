<script setup lang="ts">
/**
 * GrowthBoard — exponential growth (JSXGraph 2D), Subtopik 6.5.
 *
 * mode="race"     : A(t) = 1000 + 500t (linear, teal) against B(t) = 10·2^t (doubling, gold) for
 *                   0 ≤ t ≤ 12 hours. A slider t draws both curves up to t; the vertical window
 *                   follows the larger value so the early hours stay readable. The rates
 *                   (A' = 500, B' = ln 2 · B ≈ 0,693 B) appear only after "tampilkan laju" is
 *                   ticked: that is the discovery "laju sebanding banyaknya".
 * mode="compound" : 1 juta at 100% per year, interest added n times a year. A slider steps
 *                   through n = 1, 2, 4, 12, 52, 365, 8760, 525600 and plots (1 + 1/n)^n. The
 *                   line y = e appears only after "tampilkan garis e" is ticked.
 */
import { ref, computed, onMounted, onUnmounted, watch } from 'vue'

const props = withDefaults(defineProps<{ mode?: 'race' | 'compound'; height?: string }>(),
  { mode: 'race', height: '360px' })

const id = `jxg-growth-${Math.random().toString(36).slice(2, 9)}`
const fmt = (v: number, d = 2) => v.toFixed(d).replace('.', ',').replace('-', '−')
const grp = (v: number) => Math.round(v).toLocaleString('id-ID')

const A = (t: number) => 1000 + 500 * t
const B = (t: number) => 10 * Math.pow(2, t)
const tv = ref(4)
const showRate = ref(false)

const NS = [1, 2, 4, 12, 52, 365, 8760, 525600]
const NAMES = ['tahunan', 'tiap 6 bulan', 'tiap 3 bulan', 'bulanan', 'mingguan', 'harian', 'tiap jam', 'tiap menit']
const ni = ref(0)
const showE = ref(false)
const val = (n: number) => Math.pow(1 + 1 / n, n)
const cur = computed(() => val(NS[ni.value]))

let board: any = null
let ro: ResizeObserver | null = null

function fitRace() {
  if (!board || props.mode !== 'race') return
  const top = Math.max(A(tv.value), B(tv.value), 2000) * 1.15
  board.setBoundingBox([-0.9, top, 12.8, -top * 0.09], false)
}

watch([tv, showRate, ni, showE], () => { fitRace(); board?.update() })

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

  if (props.mode === 'race') {
    board = JXG.JSXGraph.initBoard(id, {
      boundingbox: [-0.9, 6000, 12.8, -500], axis: true, showNavigation: false, showCopyright: false,
      keepaspectratio: false, pan: { enabled: false }, zoom: { enabled: false },
      defaultAxes: { x: { strokeColor: '#475569', ticks: { ...tick, ticksDistance: 2 } }, y: { strokeColor: '#475569', ticks: tick } }
    })
    const T = () => tv.value
    board.create('functiongraph', [A, 0, T], { strokeColor: '#2dd4bf', strokeWidth: 3, ...fix })
    board.create('functiongraph', [B, 0, T], { strokeColor: '#f5be3c', strokeWidth: 3, ...fix })
    board.create('point', [T, () => A(T())], { name: '', size: 4.5, color: '#2dd4bf', ...fix })
    board.create('point', [T, () => B(T())], { name: '', size: 4.5, color: '#f5be3c', ...fix })
    board.create('text', [() => T() + 0.15, () => A(T()), 'A'], { ...cls('jx-teal'), fontSize: 14, anchorY: 'bottom', ...fix })
    board.create('text', [() => T() + 0.15, () => B(T()), 'B'], { ...cls('jx-gold'), fontSize: 14, anchorY: 'top', ...fix })
    board.create('text', [0.2, () => board.getBoundingBox()[1] * 0.93, 't (jam) →'], { ...cls('jx-muted'), fontSize: 11, ...fix })
  } else {
    board = JXG.JSXGraph.initBoard(id, {
      boundingbox: [-1.3, 2.95, 7.6, 1.72], axis: false, showNavigation: false, showCopyright: false,
      keepaspectratio: false, pan: { enabled: false }, zoom: { enabled: false }
    })
    board.create('segment', [[-0.6, 2], [7.5, 2]], { strokeColor: '#475569', strokeWidth: 1, ...fix })
    board.create('segment', [[-0.6, 2], [-0.6, 2.9]], { strokeColor: '#475569', strokeWidth: 1, lastArrow: true, ...fix })
    ;[2, 2.2, 2.4, 2.6, 2.8].forEach((v) => {
      board.create('segment', [[-0.6, v], [7.5, v]], { strokeColor: '#1e293b', strokeWidth: 1, ...fix })
      board.create('text', [-0.7, v, fmt(v, 1)], { ...cls('jx-muted'), fontSize: 10, anchorX: 'right', anchorY: 'middle', ...fix })
    })
    NS.forEach((n, i) => {
      board.create('segment', [[i, 2], [i, val(n)]], { strokeColor: '#2dd4bf', strokeWidth: 10, strokeOpacity: 0.55, visible: () => i <= ni.value, ...fix })
      board.create('point', [i, val(n)], { name: '', size: 4, color: '#2dd4bf', visible: () => i <= ni.value, ...fix })
      board.create('text', [i, 1.93, n.toLocaleString('id-ID')], { ...cls('jx-muted'), fontSize: 10, anchorX: 'middle', ...fix })
    })
    board.create('point', [() => ni.value, () => cur.value], { name: '', size: 5, color: '#fb7185', ...fix })
    board.create('text', [3.5, 1.84, 'n = berapa kali bunga ditambahkan dalam setahun'], { ...cls('jx-muted'), fontSize: 10, anchorX: 'middle', ...fix })
    board.create('line', [[0, Math.E], [1, Math.E]], { strokeColor: '#f5be3c', strokeWidth: 2, dash: 3, visible: () => showE.value, ...fix })
    board.create('text', [5.4, Math.E + 0.07, 'e ≈ 2,71828'], { ...cls('jx-gold'), fontSize: 12, visible: () => showE.value, ...fix })
  }

  const el = document.getElementById(id)
  if (el) {
    ;(el as any).__jxgBoard = board
    if (typeof ResizeObserver !== 'undefined') {
      ro = new ResizeObserver(() => { board.resizeContainer(el.clientWidth, el.clientHeight, true); fitRace(); board.update() })
      ro.observe(el)
    }
  }
  fitRace()
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
  <div class="gr flex flex-col gap-2 w-full" :style="{ height: props.height }">
    <div :id="id" class="jxgbox gr-box"></div>
    <div class="gr-panel">
      <template v-if="props.mode === 'race'">
        <label class="gr-row">
          <span>t = <b>{{ fmt(tv, 1) }}</b> jam</span>
          <input type="range" min="0" max="12" step="0.1" v-model.number="tv" />
        </label>
        <div class="gr-foot">
          <span class="gr-num"><i class="sw sw-t"></i> A = 1000 + 500t = <b class="teal">{{ grp(A(tv)) }}</b> &nbsp; <i class="sw sw-g"></i> B = 10·2^t = <b class="gold">{{ grp(B(tv)) }}</b></span>
          <label class="gr-check"><input type="checkbox" v-model="showRate" /> tampilkan laju</label>
        </div>
        <div v-if="showRate" class="gr-num">laju A = <b class="teal">500</b> per jam · laju B = <b class="gold">{{ grp(Math.LN2 * B(tv)) }}</b> per jam = <b class="gold">0,693</b> × B</div>
      </template>
      <template v-else>
        <label class="gr-row">
          <span>bunga ditambahkan <b>{{ NAMES[ni] }}</b></span>
          <input type="range" min="0" :max="NS.length - 1" step="1" v-model.number="ni" />
        </label>
        <div class="gr-foot">
          <span class="gr-num">n = <b>{{ NS[ni].toLocaleString('id-ID') }}</b> · (1 + 1/n)ⁿ = <b class="teal">{{ fmt(cur, 5) }}</b> juta</span>
          <label class="gr-check"><input type="checkbox" v-model="showE" /> tampilkan garis e</label>
        </div>
      </template>
    </div>
  </div>
</template>

<style>
.gr { font-size: 0.78rem; color: #e2e8f0; }
.gr-box { flex: 1 1 auto; min-height: 0; border-radius: 0.75rem; border: 1px solid #334155; overflow: hidden; background-color: #0c1018 !important; }
.gr .jxgbox svg { background-color: #0c1018 !important; }
.gr .jxgbox .JXGtext.jx-gold { color: #f5be3c !important; }
.gr .jxgbox .JXGtext.jx-teal { color: #2dd4bf !important; }
.gr .jxgbox .JXGtext.jx-muted { color: #94a3b8 !important; }
.gr-panel { background: #141b28; border: 1px solid #233148; border-radius: 0.75rem; padding: 0.4rem 0.7rem; display: flex; flex-direction: column; gap: 0.3rem; }
.gr-row { display: flex; align-items: center; gap: 0.5rem; }
.gr-row span { white-space: nowrap; color: #cbd5e1; font-family: ui-monospace, monospace; }
.gr-row b { color: #fb7185; }
.gr-row input { flex: 1; accent-color: #fb7185; min-width: 0; }
.gr-foot { display: flex; align-items: center; gap: 0.9rem; flex-wrap: wrap; }
.gr-check { display: flex; align-items: center; gap: 0.35rem; cursor: pointer; white-space: nowrap; }
.gr-check input { accent-color: #f5be3c; }
.gr-num { font-family: ui-monospace, monospace; color: #cbd5e1; font-size: 0.7rem; display: flex; align-items: center; gap: 0.3rem; flex-wrap: wrap; }
.gr-num b { color: #fb7185; }
.gr-num b.teal { color: #2dd4bf; }
.gr-num b.gold { color: #f5be3c; }
.gr .sw { display: inline-block; width: 0.9rem; height: 0.3rem; border-radius: 2px; }
.gr .sw-t { background: #2dd4bf; }
.gr .sw-g { background: #f5be3c; }
</style>
