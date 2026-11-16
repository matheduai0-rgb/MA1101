<script setup lang="ts">
/**
 * CableSpringBoard — a cable (2 kg/m, so 20 N/m) runs over a pulley 15 m above the floor and is
 * pulled to the right. Its lower end starts on the floor. A spring (natural length 5 m, k = 10 N/m)
 * stands on the floor; at height 5 m the cable end hooks onto the top of the spring and drags it up.
 *
 * Left : schematic — floor, wall with pulley, the hanging cable (length 15 − y), the spring
 *        (relaxed below 5 m, stretched to y above 5 m) and one thin cable piece Δy.
 * Right: graph of the pulling force F(y), hidden behind a cover until "tampilkan grafik F" is ticked so
 *        the prediction is not given away; the area from 0 to y is shaded (= work done so far).
 * Below: slider for y (0–15) and a checkbox with the numbers (hanging length, weights, F).
 *
 * F(y) = 20(15 − y)              for 0 ≤ y ≤ 5
 * F(y) = 10(y − 5) + 20(15 − y)  for 5 ≤ y ≤ 15   (= 250 − 10y)
 */
import { ref, computed, onMounted, onUnmounted, watch } from 'vue'

const props = withDefaults(defineProps<{ height?: string }>(), { height: '400px' })

const idS = `jxg-cs-s-${Math.random().toString(36).slice(2, 9)}`
const idG = idS.replace('-s-', '-g-')
const yv = ref(2)
const showNum = ref(false)
const showGraph = ref(false)

const TOP = 15
const L0 = 5
const K = 10
const W = 20
const fmt = (v: number, d = 1) => v.toFixed(d).replace('.', ',')
const hang = computed(() => TOP - yv.value)
const stretch = computed(() => Math.max(0, yv.value - L0))
const Fc = computed(() => W * hang.value)
const Fs = computed(() => K * stretch.value)
const F = (y: number) => W * (TOP - y) + K * Math.max(0, y - L0)
const work = (y: number) => {
  const a = Math.min(y, L0)
  let w = W * (TOP * a - a * a / 2)
  if (y > L0) w += 250 * (y - L0) - 5 * (y * y - L0 * L0)
  return w
}

let bS: any = null
let bG: any = null
const observers: ResizeObserver[] = []

watch(yv, () => { bS?.update(); bG?.update() })

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

  // ---------- schematic ----------
  bS = JXG.JSXGraph.initBoard(idS, {
    boundingbox: [-5.4, 17.7, 5.2, -1.2], axis: false, showNavigation: false, showCopyright: false,
    keepaspectratio: false, pan: { enabled: false }, zoom: { enabled: false }
  })
  const WALL = 1.3
  // floor and wall
  bS.create('segment', [[-5, 0], [5, 0]], { strokeColor: '#64748b', strokeWidth: 2, ...fix })
  bS.create('segment', [[WALL, 0], [WALL, 14.2]], { strokeColor: '#94a3b8', strokeWidth: 3, ...fix })
  bS.create('segment', [[WALL, 14.2], [5, 14.2]], { strokeColor: '#94a3b8', strokeWidth: 3, ...fix })
  // pulley
  bS.create('circle', [[0.55, 15.05], 0.55], { strokeColor: '#cbd5e1', strokeWidth: 2, fillColor: '#1e293b', fillOpacity: 1, ...fix })
  // cable over the pulley and to the right (pulled)
  bS.create('segment', [[0.55, 15.6], [4.6, 15.6]], { strokeColor: '#f5be3c', strokeWidth: 3, ...fix })
  bS.create('segment', [[2.4, 16.35], [4.6, 16.35]], { strokeColor: '#f5be3c', strokeWidth: 1.5, dash: 2, lastArrow: true, ...fix })
  bS.create('text', [2.4, 17.15, 'ditarik'], { color: '#f5be3c', cssClass: 'JXGtext jx-gold', highlightCssClass: 'JXGtext jx-gold', fontSize: 11, anchorY: 'middle', ...fix })
  // spring: relaxed (length 5) until the cable end passes 5 m, then stretched to y
  const sTop = () => Math.max(L0, yv.value)
  const N = 9
  bS.create('curve', [
    (t: number) => 0.55 * Math.sin(2 * Math.PI * N * t),
    (t: number) => sTop() * t,
    0, 1
  ], { strokeColor: '#2dd4bf', strokeWidth: 2, numberPointsHigh: 600, numberPointsLow: 300, ...fix })
  bS.create('point', [0, 0], { size: 4, color: '#2dd4bf', name: '', ...fix })
  // hanging cable from the pulley down to the end at height y
  bS.create('segment', [[0, TOP], [0, () => yv.value]], {
    strokeColor: '#f5be3c', strokeWidth: 3.5, visible: () => hang.value > 0.02, ...fix
  })
  bS.create('point', [0, () => yv.value], { size: 3.5, color: '#f5be3c', name: '', ...fix })
  // one thin cable piece Δy
  const DY = 0.9
  const mid = () => (yv.value + TOP) / 2
  const hasPiece = () => hang.value > 2.2
  bS.create('segment', [[0, () => mid() - DY / 2], [0, () => mid() + DY / 2]], {
    strokeColor: '#fb7185', strokeWidth: 7, visible: hasPiece, ...fix
  })
  bS.create('text', [-0.55, () => mid(), 'Δy'], { color: '#fb7185', cssClass: 'JXGtext jx-coral', highlightCssClass: 'JXGtext jx-coral', fontSize: 13, anchorX: 'right', anchorY: 'middle', visible: hasPiece, ...fix })
  bS.create('text', [-0.55, () => mid() - 1.1, 'berat ≈ 20 Δy N'], { color: '#fda4af', cssClass: 'JXGtext jx-pink', highlightCssClass: 'JXGtext jx-pink', fontSize: 10.5, anchorX: 'right', anchorY: 'middle', visible: hasPiece, ...fix })
  // hanging length (right of the cable, between cable and wall)
  bS.create('segment', [[0.85, TOP], [0.85, () => yv.value]], {
    strokeColor: '#f5be3c', strokeWidth: 1.3, firstArrow: true, lastArrow: true, visible: () => hang.value > 1.2, ...fix
  })
  // height marks on the left
  for (const h of [0, 5, 15]) {
    bS.create('segment', [[-4.5, h], [-4.1, h]], { strokeColor: '#64748b', strokeWidth: 1.5, ...fix })
    bS.create('text', [-4.7, h, String(h)], { color: '#94a3b8', cssClass: 'JXGtext jx-muted', highlightCssClass: 'JXGtext jx-muted', fontSize: 11, anchorX: 'right', anchorY: 'middle', ...fix })
  }
  bS.create('segment', [[-4.3, 0], [-4.3, TOP]], { strokeColor: '#475569', strokeWidth: 1, ...fix })
  bS.create('segment', [[-4.1, 5], [-0.6, 5]], { strokeColor: '#475569', strokeWidth: 1, dash: 2, ...fix })
  // height y of the cable end
  bS.create('segment', [[-3.3, 0], [-3.3, () => yv.value]], {
    strokeColor: '#e2e8f0', strokeWidth: 1.5, firstArrow: true, lastArrow: true, visible: () => yv.value > 0.8, ...fix
  })
  bS.create('text', [-3.1, () => yv.value / 2, 'y'], { color: '#e2e8f0', fontSize: 14, anchorY: 'middle', visible: () => yv.value > 0.8, ...fix })
  bS.create('segment', [[-3.3, () => yv.value], [-0.1, () => yv.value]], { strokeColor: '#e2e8f0', strokeWidth: 1, dash: 1, ...fix })

  // ---------- graph of F(y) ----------
  bG = JXG.JSXGraph.initBoard(idG, {
    boundingbox: [-2.6, 345, 16.3, -45], axis: false, showNavigation: false, showCopyright: false,
    keepaspectratio: false, pan: { enabled: false }, zoom: { enabled: false }
  })
  const axAtt = (dist: number) => ({
    strokeColor: '#64748b', highlight: false,
    ticks: { ticksDistance: dist, insertTicks: false, minorTicks: 0, strokeColor: '#475569', majorHeight: 6, drawLabels: true,
      label: { strokeColor: '#94a3b8', fontSize: 10, offset: [-4, -10] } }
  })
  bG.create('axis', [[0, 0], [1, 0]], axAtt(5))
  bG.create('axis', [[0, 0], [0, 1]], { ...axAtt(100), ticks: { ...axAtt(100).ticks, label: { strokeColor: '#94a3b8', fontSize: 10, offset: [-24, 0], anchorY: 'middle' } } })
  bG.create('text', [15.9, 22, 'y'], { color: '#cbd5e1', cssClass: 'JXGtext jx-soft', highlightCssClass: 'JXGtext jx-soft', fontSize: 13, anchorX: 'right', ...fix })
  bG.create('text', [0.3, 330, 'F (N)'], { color: '#cbd5e1', cssClass: 'JXGtext jx-soft', highlightCssClass: 'JXGtext jx-soft', fontSize: 12, ...fix })
  bG.create('segment', [[5, 0], [5, 200]], { strokeColor: '#475569', strokeWidth: 1, dash: 2, ...fix })
  // shaded area 0..y
  const area = bG.create('curve', [[], []], { strokeWidth: 0, fillColor: '#f5be3c', fillOpacity: 0.22, highlight: false })
  area.updateDataArray = function () {
    const y = yv.value
    const xs = [0, 0]
    const ys = [0, F(0)]
    if (y > L0) { xs.push(L0); ys.push(F(L0)) }
    xs.push(y, y, 0)
    ys.push(F(y), 0, 0)
    this.dataX = xs
    this.dataY = ys
  }
  bG.create('functiongraph', [(x: number) => F(x), 0, TOP], { strokeColor: '#2dd4bf', strokeWidth: 2.5, ...fix })
  bG.create('point', [() => yv.value, () => F(yv.value)], { size: 4, color: '#f5be3c', name: '', ...fix })
  bG.create('text', [() => Math.max(yv.value / 2, 0.4), 40, () => yv.value > 3 ? 'kerja = luas' : ''], {
    color: '#f5be3c', cssClass: 'JXGtext jx-gold', highlightCssClass: 'JXGtext jx-gold', fontSize: 11, anchorX: 'middle', ...fix
  })

  for (const [id, bd] of [[idS, bS], [idG, bG]] as const) {
    const el = document.getElementById(id)
    if (!el) continue
    ;(el as any).__jxgBoard = bd
    if (typeof ResizeObserver !== 'undefined') {
      const ro = new ResizeObserver(() => { bd.resizeContainer(el.clientWidth, el.clientHeight, true); bd.update() })
      ro.observe(el)
      observers.push(ro)
    }
  }
})

onUnmounted(() => {
  observers.forEach(o => o.disconnect())
  const JXG = (window as any).JXG
  for (const bd of [bS, bG]) { try { if (bd) JXG?.JSXGraph.freeBoard(bd) } catch (e) { /* ignore */ } }
  bS = null; bG = null
})
</script>

<template>
  <div class="cs flex flex-col gap-2 w-full" :style="{ height: props.height }">
    <div class="flex gap-2" style="flex: 1 1 auto; min-height: 0;">
      <div class="cs-cell" style="flex: 0.85 1 0;">
        <div :id="idS" class="jxgbox cs-box"></div>
        <div class="cs-cap">katrol 15 m · pegas 5 m</div>
      </div>
      <div class="cs-cell">
        <div class="cs-wrap">
          <div :id="idG" class="jxgbox cs-box"></div>
          <div v-show="!showGraph" class="cs-cover">grafik F(y) disembunyikan<br />— tebak dulu bentuknya —</div>
        </div>
        <div class="cs-cap">gaya tarik F terhadap y</div>
      </div>
    </div>
    <div class="cs-panel">
      <label class="cs-row">
        <span>ujung kabel y = <b>{{ fmt(yv) }}</b> m</span>
        <input type="range" min="0" max="15" step="0.1" v-model.number="yv" />
      </label>
      <div class="cs-foot">
        <label class="cs-check"><input type="checkbox" v-model="showNum" /> tampilkan angka</label>
        <label class="cs-check"><input type="checkbox" v-model="showGraph" /> tampilkan grafik F</label>
      </div>
      <div v-if="showNum" class="cs-num">
        kabel tergantung <b>{{ fmt(hang) }}</b> m → <b>{{ fmt(Fc, 0) }}</b> N ·
        pegas teregang <b>{{ fmt(stretch) }}</b> m → <b>{{ fmt(Fs, 0) }}</b> N ·
        F = <b class="cs-F">{{ fmt(Fc + Fs, 0) }}</b> N<template v-if="showGraph"> · luas = <b>{{ fmt(work(yv), 0) }}</b> J</template>
      </div>
      <div v-else class="cs-legend"><i class="sw sw-c"></i> kabel &nbsp; <i class="sw sw-s"></i> pegas &nbsp; <i class="sw sw-p"></i> potongan Δy</div>
    </div>
  </div>
</template>

<style>
.cs { font-size: 0.78rem; color: #e2e8f0; }
.cs-cell { flex: 1 1 0; min-width: 0; display: flex; flex-direction: column; }
.cs-wrap { position: relative; flex: 1 1 auto; min-height: 0; display: flex; }
.cs-box { flex: 1 1 auto; min-height: 0; border-radius: 0.75rem; border: 1px solid #334155; overflow: hidden; background-color: #0c1018 !important; }
.cs .jxgbox svg { background-color: #0c1018 !important; }
.cs .jxgbox .JXGtext { color: #e2e8f0 !important; }
.cs .jxgbox .JXGtext.jx-coral { color: #fb7185 !important; }
.cs .jxgbox .JXGtext.jx-pink { color: #fda4af !important; }
.cs .jxgbox .JXGtext.jx-gold { color: #f5be3c !important; }
.cs .jxgbox .JXGtext.jx-muted { color: #94a3b8 !important; }
.cs .jxgbox .JXGtext.jx-soft { color: #cbd5e1 !important; }
.cs-cover { position: absolute; inset: 0; border-radius: 0.75rem; background: #111826; border: 1px dashed #334155; display: flex; align-items: center; justify-content: center; text-align: center; color: #64748b; font-size: 0.72rem; line-height: 1.5; }
.cs-cap { font-size: 0.66rem; color: #64748b; text-align: center; margin-top: 0.15rem; }
.cs-panel { background: #141b28; border: 1px solid #233148; border-radius: 0.75rem; padding: 0.45rem 0.7rem; display: flex; flex-direction: column; gap: 0.3rem; }
.cs-row { display: flex; align-items: center; gap: 0.6rem; }
.cs-row span { white-space: nowrap; color: #cbd5e1; font-family: ui-monospace, monospace; }
.cs-row b { color: #f5be3c; }
.cs-row input { flex: 1; accent-color: #f5be3c; min-width: 0; }
.cs-foot { display: flex; align-items: center; gap: 1.2rem; }
.cs-check { display: flex; align-items: center; gap: 0.35rem; cursor: pointer; white-space: nowrap; }
.cs-check input { accent-color: #2dd4bf; }
.cs-num { font-family: ui-monospace, monospace; color: #cbd5e1; font-size: 0.68rem; }
.cs-num b { color: #34d399; }
.cs-num b.cs-F { color: #f5be3c; }
.cs-legend { color: #94a3b8; display: flex; align-items: center; gap: 0.3rem; font-size: 0.7rem; }
.cs .sw { display: inline-block; width: 0.9rem; height: 0.3rem; border-radius: 2px; }
.cs .sw-c { background: #f5be3c; }
.cs .sw-s { background: #2dd4bf; }
.cs .sw-p { background: #fb7185; }
</style>
