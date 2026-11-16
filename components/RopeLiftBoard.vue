<script setup lang="ts">
/**
 * RopeLiftBoard — solution picture for "pull the cable end from the floor up to 5 m" by slicing the
 * ROPE (as in the hanging-cable example), without the spring.
 *
 * The cable (20 N/m) hangs from a pulley 15 m above the floor; its end starts on the floor. Pulling
 * the end up by t moves every piece up by t; pieces that pass the pulley run along the roof
 * (horizontal: no work, gravity on the horizontal cable is ignored).
 *
 *   case 1 (teal): pieces that start at 10 ≤ y ≤ 15 end on the roof; each rises 15 − y.
 *   case 2 (blue): pieces that start at 0 ≤ y ≤ 10 keep hanging; each rises 5.
 *
 * Controls: slider for the slice's starting height y, "▶ Tarik ke 5 m" (animated) with a manual
 * slider for the pull t, and a checkbox with the numbers. The work total is not shown.
 */
import { ref, computed, onMounted, onUnmounted, watch } from 'vue'

const props = withDefaults(defineProps<{ height?: string }>(), { height: '400px' })

const id = `jxg-rope-${Math.random().toString(36).slice(2, 9)}`
const y0 = ref(12)        // starting height of the slice (bottom)
const tv = ref(0)         // how far the end has been pulled
const showNum = ref(false)

const TOP = 15
const PULL = 5
const BOUND = TOP - PULL  // 10
const DY = 0.5
const RS = 0.9            // horizontal compression on the roof
const PX = 0.55           // pulley x
const ROOF = 15.6
const fmt = (v: number, d = 1) => v.toFixed(d).replace('.', ',')

const case1 = computed(() => y0.value >= BOUND)
const rise = computed(() => case1.value ? TOP - y0.value : PULL)
const risen = computed(() => Math.min(tv.value, TOP - y0.value))

// position of the piece that started at height h, after pulling by t
const pos = (h: number, t: number): [number, number] => {
  const z = h + t
  return z <= TOP ? [0, z] : [PX + RS * (z - TOP), ROOF]
}

let raf = 0
const stopAnim = () => { if (raf) cancelAnimationFrame(raf); raf = 0 }
const animate = () => {
  stopAnim()
  const from = tv.value >= PULL - 0.001 ? 0 : tv.value
  const t0 = performance.now()
  const dur = 2000 * (1 - from / PULL)
  const step = (now: number) => {
    const s = Math.min(1, (now - t0) / Math.max(dur, 1))
    const e = s < 0.5 ? 2 * s * s : 1 - Math.pow(-2 * s + 2, 2) / 2
    tv.value = from + (PULL - from) * e
    raf = s < 1 ? requestAnimationFrame(step) : 0
  }
  raf = requestAnimationFrame(step)
}
const reset = () => { stopAnim(); tv.value = 0 }

let board: any = null
let ro: ResizeObserver | null = null

watch([y0, tv], () => board?.update())

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
  board = JXG.JSXGraph.initBoard(id, {
    boundingbox: [-5.6, 17.9, 6.6, -1.2], axis: false, showNavigation: false, showCopyright: false,
    keepaspectratio: false, pan: { enabled: false }, zoom: { enabled: false }
  })
  const WALL = 1.3
  // floor, wall, roof, pulley
  board.create('segment', [[-5, 0], [6.3, 0]], { strokeColor: '#64748b', strokeWidth: 2, ...fix })
  board.create('segment', [[WALL, 0], [WALL, 14.2]], { strokeColor: '#94a3b8', strokeWidth: 3, ...fix })
  board.create('segment', [[WALL, 14.2], [6.3, 14.2]], { strokeColor: '#94a3b8', strokeWidth: 3, ...fix })
  board.create('text', [3.8, 13.5, 'atap'], { color: '#94a3b8', ...cls('jx-muted'), fontSize: 11, anchorX: 'middle', ...fix })
  board.create('circle', [[PX, 15.05], 0.55], { strokeColor: '#cbd5e1', strokeWidth: 2, fillColor: '#1e293b', fillOpacity: 1, ...fix })
  // cable that already lies on the roof (pulled by hand)
  board.create('segment', [[() => PX + RS * tv.value, ROOF], [6.3, ROOF]], { strokeColor: '#475569', strokeWidth: 3, ...fix })
  board.create('segment', [[4.3, 16.4], [6.2, 16.4]], { strokeColor: '#f5be3c', strokeWidth: 1.5, dash: 2, lastArrow: true, ...fix })
  board.create('text', [4.3, 17.15, 'ditarik'], { color: '#f5be3c', ...cls('jx-gold'), fontSize: 11, anchorY: 'middle', ...fix })

  // height marks
  for (const h of [0, 5, 10, 15]) {
    board.create('segment', [[-4.7, h], [-4.3, h]], { strokeColor: '#64748b', strokeWidth: 1.5, ...fix })
    board.create('text', [-4.9, h, String(h)], { color: '#94a3b8', ...cls('jx-muted'), fontSize: 11, anchorX: 'right', anchorY: 'middle', ...fix })
  }
  board.create('segment', [[-4.5, 0], [-4.5, TOP]], { strokeColor: '#475569', strokeWidth: 1, ...fix })
  board.create('segment', [[-4.3, BOUND], [-0.2, BOUND]], { strokeColor: '#475569', strokeWidth: 1, dash: 2, ...fix })
  board.create('text', [-4.2, BOUND + 0.55, 'batas kasus (posisi awal)'], { color: '#94a3b8', ...cls('jx-muted'), fontSize: 10, ...fix })

  // rope, two colours by starting height
  const ropePart = (h0: number, h1: number, color: string) => {
    const c = board.create('curve', [[], []], { strokeColor: color, strokeWidth: 4, highlight: false })
    c.updateDataArray = function () {
      const t = tv.value
      const xs: number[] = []
      const ys: number[] = []
      const n = 40
      for (let i = 0; i <= n; i++) {
        const h = h0 + (h1 - h0) * i / n
        const [x, y] = pos(h, t)
        xs.push(x); ys.push(y)
      }
      this.dataX = xs
      this.dataY = ys
    }
    return c
  }
  ropePart(0, BOUND, '#60a5fa')
  ropePart(BOUND, TOP, '#2dd4bf')
  board.create('point', [() => pos(0, tv.value)[0], () => pos(0, tv.value)[1]], { size: 3.5, color: '#60a5fa', name: '', ...fix })

  // the slice: ghost at the start, solid where it is now
  board.create('segment', [[-0.45, () => y0.value], [-0.45, () => y0.value + DY]], { strokeColor: '#fb7185', strokeOpacity: 0.4, strokeWidth: 6, ...fix })
  const slice = board.create('curve', [[], []], { strokeColor: '#fb7185', strokeWidth: 8, highlight: false })
  slice.updateDataArray = function () {
    const xs: number[] = []
    const ys: number[] = []
    for (let i = 0; i <= 8; i++) {
      const [x, y] = pos(y0.value + DY * i / 8, tv.value)
      xs.push(x); ys.push(y)
    }
    this.dataX = xs
    this.dataY = ys
  }
  board.create('text', [-0.75, () => y0.value + DY / 2, 'Δy'], { color: '#fb7185', ...cls('jx-coral'), fontSize: 13, anchorX: 'right', anchorY: 'middle', ...fix })
  // rise so far (vertical part only)
  board.create('arrow', [[-1.6, () => y0.value], [-1.6, () => y0.value + risen.value]], {
    strokeColor: '#f5be3c', strokeWidth: 2, visible: () => risen.value > 0.15, ...fix
  })
  board.create('text', [-1.8, () => y0.value + Math.max(risen.value, 0.6) / 2 - 0.9,
    () => case1.value ? `naik 15 − y = ${fmt(rise.value)}` : 'naik 5'], {
    color: '#f5be3c', ...cls('jx-gold'), fontSize: 11, anchorX: 'right', anchorY: 'middle', ...fix
  })
  // case label
  board.create('text', [-5.3, 17.15, 'Kasus 1 · pindah ke atap'], {
    color: '#2dd4bf', ...cls('jx-teal'), fontSize: 13, anchorY: 'middle', visible: () => case1.value, ...fix
  })
  board.create('text', [-5.3, 17.15, 'Kasus 2 · tetap menggantung'], {
    color: '#60a5fa', ...cls('jx-blue'), fontSize: 13, anchorY: 'middle', visible: () => !case1.value, ...fix
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
  board = null
})
</script>

<template>
  <div class="rl flex flex-col gap-2 w-full" :style="{ height: props.height }">
    <div :id="id" class="jxgbox rl-box"></div>
    <div class="rl-panel">
      <label class="rl-row">
        <span>irisan mula-mula di y = <b>{{ fmt(y0) }}</b> m</span>
        <input type="range" min="0" max="14.5" step="0.5" v-model.number="y0" />
      </label>
      <div class="rl-row">
        <button type="button" class="rl-btn" @click="animate">▶ Tarik ke 5 m</button>
        <button type="button" class="rl-btn rl-btn-sm" title="kembali ke awal" @click="reset">↺</button>
        <input type="range" min="0" max="5" step="0.05" v-model.number="tv" aria-label="tarikan" @input="stopAnim" />
        <span class="rl-t">{{ fmt(tv) }} m</span>
      </div>
      <div class="rl-foot">
        <label class="rl-check"><input type="checkbox" v-model="showNum" /> tampilkan angka</label>
        <span v-if="showNum" class="rl-num">kasus <b>{{ case1 ? 1 : 2 }}</b> · naik <b>{{ fmt(rise) }}</b> m · ΔW ≈ 20 Δy · <b>{{ fmt(rise) }}</b></span>
        <span v-else class="rl-legend"><i class="sw sw-t"></i> kasus 1 &nbsp; <i class="sw sw-b"></i> kasus 2 &nbsp; <i class="sw sw-c"></i> irisan Δy</span>
      </div>
    </div>
  </div>
</template>

<style>
.rl { font-size: 0.78rem; color: #e2e8f0; }
.rl-box { flex: 1 1 auto; min-height: 0; border-radius: 0.75rem; border: 1px solid #334155; overflow: hidden; background-color: #0c1018 !important; }
.rl .jxgbox svg { background-color: #0c1018 !important; }
.rl .jxgbox .JXGtext.jx-coral { color: #fb7185 !important; }
.rl .jxgbox .JXGtext.jx-gold { color: #f5be3c !important; }
.rl .jxgbox .JXGtext.jx-muted { color: #94a3b8 !important; }
.rl .jxgbox .JXGtext.jx-teal { color: #2dd4bf !important; font-weight: 600; }
.rl .jxgbox .JXGtext.jx-blue { color: #60a5fa !important; font-weight: 600; }
.rl-panel { background: #141b28; border: 1px solid #233148; border-radius: 0.75rem; padding: 0.4rem 0.7rem; display: flex; flex-direction: column; gap: 0.25rem; }
.rl-row { display: flex; align-items: center; gap: 0.55rem; }
.rl-row span { white-space: nowrap; color: #cbd5e1; font-family: ui-monospace, monospace; }
.rl-row b { color: #fb7185; }
.rl-row input { flex: 1; accent-color: #fb7185; min-width: 0; }
.rl-btn { background: rgba(245, 190, 60, 0.15); color: #f5be3c; border: 1px solid rgba(245, 190, 60, 0.5); border-radius: 0.4rem; padding: 0.1rem 0.55rem; font-size: 0.74rem; cursor: pointer; white-space: nowrap; }
.rl-btn:hover { background: rgba(245, 190, 60, 0.28); }
.rl-btn-sm { padding: 0.1rem 0.4rem; }
.rl-t { width: 3rem; text-align: right; color: #94a3b8 !important; }
.rl-foot { display: flex; align-items: center; gap: 0.9rem; }
.rl-check { display: flex; align-items: center; gap: 0.35rem; cursor: pointer; white-space: nowrap; }
.rl-check input { accent-color: #2dd4bf; }
.rl-num { font-family: ui-monospace, monospace; color: #cbd5e1; font-size: 0.7rem; }
.rl-num b { color: #f5be3c; }
.rl-legend { color: #94a3b8; display: flex; align-items: center; gap: 0.3rem; font-size: 0.7rem; }
.rl .sw { display: inline-block; width: 0.9rem; height: 0.3rem; border-radius: 2px; }
.rl .sw-t { background: #2dd4bf; }
.rl .sw-b { background: #60a5fa; }
.rl .sw-c { background: #fb7185; }
</style>
