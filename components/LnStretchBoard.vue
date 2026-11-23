<script setup lang="ts">
/**
 * LnStretchBoard — the area under y = 1/t does not change under a stretch (JSXGraph 2D), Subtopik 6.1.
 *
 * Shows ∫_1^x dt/t = ∫_k^{kx} dt/t. The region under 1/t from 1 to x is mapped by
 * (t, y) ↦ (k·t, y/k): k times wider, 1/k times as tall. The image is exactly the region under
 * 1/t from k to kx, so the area stays the same. With k = a this is L(ax) − L(a) = L(x).
 *
 * Draws: y = 1/t (blue), a faint ghost of the original region, the moving region (green) cut into
 * six strips that stretch with it, one strip outlined in coral ("lebar × k", "tinggi ÷ k"), and
 * endpoint labels 1 → k, x → kx. Props xName / aName rename x and a in labels and the panel. Controls: sliders x, a, k; a button that animates k from 1 to a
 * and back. Area numbers (computed numerically, not from ln) appear only after "tampilkan luas".
 */
import { ref, computed, onMounted, onUnmounted, watch } from 'vue'

const props = withDefaults(defineProps<{ height?: string; initialX?: number; initialA?: number; xName?: string; aName?: string }>(),
  { height: '360px', initialX: 2, initialA: 2, xName: 'x', aName: 'a' })
// names shown for x and a (e.g. xName="eᵇ", aName="eᵃ" for the e^a e^b = e^(a+b) slide)
const kx = props.xName === 'x' ? 'kx' : `k·${props.xName}`

const id = `jxg-lnstretch-${Math.random().toString(36).slice(2, 9)}`
const fmt = (v: number, d = 2) => v.toFixed(d).replace('.', ',').replace('-', '−')
const inv = (t: number) => 1 / t
const N = 6        // strips
const HI = 2       // highlighted strip index

const xv = ref(props.initialX)
const av = ref(props.initialA)
const kv = ref(1)
const showArea = ref(false)
const playing = ref(false)

// Simpson's rule for ∫_p^q dt/t (numerical, so the readout is a genuine check)
const area = (p: number, q: number) => {
  const n = 200, h = (q - p) / n
  let s = inv(p) + inv(q)
  for (let i = 1; i < n; i++) s += (i % 2 ? 4 : 2) * inv(p + i * h)
  return (s * h) / 3
}
const area0 = computed(() => area(1, xv.value))
const areaK = computed(() => area(kv.value, kv.value * xv.value))
const atStart = computed(() => Math.abs(kv.value - 1) < 1e-3)

let board: any = null
let ro: ResizeObserver | null = null
let raf = 0

watch([xv, av, kv, showArea], () => board?.update())

function animateTo(target: number) {
  cancelAnimationFrame(raf)
  const from = kv.value, dur = 2000, t0 = performance.now()
  playing.value = true
  const step = (now: number) => {
    const u = Math.min(1, (now - t0) / dur)
    const e = u < 0.5 ? 2 * u * u : 1 - Math.pow(-2 * u + 2, 2) / 2   // ease in-out
    kv.value = from + (target - from) * e
    if (u < 1) raf = requestAnimationFrame(step)
    else playing.value = false
  }
  raf = requestAnimationFrame(step)
}
const toggle = () => animateTo(atStart.value ? av.value : 1)

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
    boundingbox: [-0.5, 2.45, 9.7, -1.05], axis: true, showNavigation: false, showCopyright: false,
    keepaspectratio: false, pan: { enabled: false }, zoom: { enabled: false },
    defaultAxes: { x: { strokeColor: '#475569', ticks: tick }, y: { strokeColor: '#475569', ticks: tick } }
  })

  const X = () => xv.value
  const K = () => kv.value

  // region under 1/t between p and q
  const region = (p: () => number, q: () => number, attr: any) => {
    const c = board.create('curve', [[], []], { ...fix, ...attr })
    c.updateDataArray = function () {
      const a = p(), b = q(), n = 80
      const xs = [a], ys = [0]
      for (let i = 0; i <= n; i++) { const t = a + (b - a) * i / n; xs.push(t); ys.push(inv(t)) }
      xs.push(b, a); ys.push(0, 0)
      this.dataX = xs; this.dataY = ys
    }
    return c
  }

  // ghost of the original region (1 to x)
  region(() => 1, X, { fillColor: '#94a3b8', fillOpacity: 0.1, strokeColor: '#94a3b8', strokeWidth: 1.2, dash: 2 })
  // moving region: image under (t, y) -> (k t, y/k) = region from k to kx
  region(K, () => K() * X(), { fillColor: '#34d399', fillOpacity: 0.4, strokeColor: '#34d399', strokeWidth: 1.5 })

  // strip boundaries, stretched with the region
  const edge = (i: number) => K() * (1 + (i * (X() - 1)) / N)
  const strips = board.create('curve', [[], []], { strokeColor: '#0c1018', strokeWidth: 1.5, ...fix })
  strips.updateDataArray = function () {
    const xs: number[] = [], ys: number[] = []
    for (let i = 1; i < N; i++) { const t = edge(i); xs.push(t, t, NaN); ys.push(0, inv(t), NaN) }
    this.dataX = xs; this.dataY = ys
  }
  // one highlighted strip
  region(() => edge(HI), () => edge(HI + 1), { fillColor: '#fb7185', fillOpacity: 0.35, strokeColor: '#fb7185', strokeWidth: 2.5 })
  const midHi = () => (edge(HI) + edge(HI + 1)) / 2
  board.create('text', [midHi, -0.86, 'lebar × k'], { ...cls('jx-coral'), fontSize: 12, anchorX: 'middle', ...fix })
  board.create('text', [() => edge(HI + 1) + 0.08, () => inv(edge(HI + 1)) + 0.2, 'tinggi ÷ k'],
    { ...cls('jx-coral'), fontSize: 12, anchorY: 'bottom', ...fix })

  // curve on top
  board.create('functiongraph', [inv, 0.41, 9.7], { strokeColor: '#50a5fa', strokeWidth: 3, ...fix })
  board.create('text', [0.55, 2.25, 'y = 1/t'], { ...cls('jx-blue'), fontSize: 14, ...fix })
  board.create('text', [3.2, 2.2, () => `(t, y) → (k·t, y/k),   k = ${fmt(K())}`], { ...cls('jx-muted'), fontSize: 13, ...fix })

  // endpoint labels: ghost x (grey; 1 is an axis tick) and moving k, kx (green)
  board.create('text', [X, -0.3, props.xName], { ...cls('jx-muted'), fontSize: 12, anchorX: 'middle', ...fix })
  board.create('text', [K, -0.62, 'k'], { ...cls('jx-green'), fontSize: 13, anchorX: 'middle', visible: () => !atStart.value, ...fix })
  board.create('text', [() => K() * X(), -0.62, kx], { ...cls('jx-green'), fontSize: 13, anchorX: 'middle', visible: () => !atStart.value, ...fix })

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
  cancelAnimationFrame(raf)
  ro?.disconnect()
  const JXG = (window as any).JXG
  try { if (board) JXG?.JSXGraph.freeBoard(board) } catch (e) { /* ignore */ }
  board = null
})
</script>

<template>
  <div class="ls flex flex-col gap-2 w-full" :style="{ height: props.height }">
    <div :id="id" class="jxgbox ls-box"></div>
    <div class="ls-panel">
      <div class="ls-grid">
        <label class="ls-row">
          <span>{{ props.xName }} = <b>{{ fmt(xv) }}</b></span>
          <input type="range" min="1.2" max="3" step="0.05" v-model.number="xv" />
        </label>
        <label class="ls-row">
          <span>{{ props.aName }} = <b>{{ fmt(av) }}</b></span>
          <input type="range" min="0.5" max="3" step="0.05" v-model.number="av" />
        </label>
        <label class="ls-row">
          <span>k = <b class="green">{{ fmt(kv) }}</b></span>
          <input type="range" min="0.5" max="3" step="0.01" v-model.number="kv" :disabled="playing" />
        </label>
        <button class="ls-btn" :disabled="playing" @click="toggle">{{ atStart ? `▶ regangkan sampai k = ${props.aName}` : '↺ kembali ke k = 1' }}</button>
      </div>
      <div class="ls-foot">
        <label class="ls-check"><input type="checkbox" v-model="showArea" /> tampilkan luas</label>
        <span v-if="showArea" class="ls-num">∫ dari 1 sampai {{ props.xName }} ≈ <b class="muted">{{ fmt(area0, 4) }}</b> · ∫ dari k sampai {{ kx }} ≈ <b class="green">{{ fmt(areaK, 4) }}</b><template v-if="Math.abs(area0 - areaK) &lt; 5e-4"> · <b class="gold">sama!</b></template></span>
        <span v-else class="ls-legend"><i class="sw sw-g"></i> daerah awal &nbsp; <i class="sw sw-m"></i> daerah setelah diregangkan &nbsp; <i class="sw sw-c"></i> satu pita</span>
      </div>
    </div>
  </div>
</template>

<style>
.ls { font-size: 0.78rem; color: #e2e8f0; }
.ls-box { flex: 1 1 auto; min-height: 0; border-radius: 0.75rem; border: 1px solid #334155; overflow: hidden; background-color: #0c1018 !important; }
.ls .jxgbox svg { background-color: #0c1018 !important; }
.ls .jxgbox .JXGtext.jx-blue { color: #50a5fa !important; }
.ls .jxgbox .JXGtext.jx-green { color: #34d399 !important; }
.ls .jxgbox .JXGtext.jx-coral { color: #fb7185 !important; }
.ls .jxgbox .JXGtext.jx-muted { color: #94a3b8 !important; }
.ls-panel { background: #141b28; border: 1px solid #233148; border-radius: 0.75rem; padding: 0.4rem 0.7rem; display: flex; flex-direction: column; gap: 0.3rem; }
.ls-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 0.25rem 1rem; align-items: center; }
.ls-row { display: flex; align-items: center; gap: 0.5rem; }
.ls-row span { white-space: nowrap; color: #cbd5e1; font-family: ui-monospace, monospace; min-width: 5.5rem; }
.ls-row b { color: #f5be3c; }
.ls-row b.green { color: #34d399; }
.ls-row input { flex: 1; accent-color: #f5be3c; min-width: 0; }
.ls-btn { justify-self: start; background: #1f2a3d; border: 1px solid #34d399; color: #34d399; border-radius: 0.5rem; padding: 0.15rem 0.7rem; cursor: pointer; font-size: 0.75rem; }
.ls-btn:disabled { opacity: 0.5; cursor: default; }
.ls-foot { display: flex; align-items: center; gap: 0.9rem; flex-wrap: wrap; }
.ls-check { display: flex; align-items: center; gap: 0.35rem; cursor: pointer; white-space: nowrap; }
.ls-check input { accent-color: #f5be3c; }
.ls-num { font-family: ui-monospace, monospace; color: #cbd5e1; font-size: 0.7rem; }
.ls-num b.muted { color: #cbd5e1; }
.ls-num b.green { color: #34d399; }
.ls-num b.gold { color: #f5be3c; }
.ls-legend { color: #94a3b8; display: flex; align-items: center; gap: 0.3rem; font-size: 0.7rem; }
.ls .sw { display: inline-block; width: 0.9rem; height: 0.3rem; border-radius: 2px; }
.ls .sw-g { background: #94a3b8; }
.ls .sw-m { background: #34d399; }
.ls .sw-c { background: #fb7185; }
</style>
