<script setup lang="ts">
/**
 * TankBoard — pumping water out of an inverted cone tank (height 6, rim radius 3).
 *
 * Left : 3D view (JSXGraph view3d, drag to rotate). Translucent cone, rim circle, one water layer
 *        (disc of radius r at depth y, thickness Δy) and a dashed line showing how far it is lifted.
 * Right: 2D vertical cross-section with the same layer, the depth/lift y, the thickness Δy and r.
 * Below: sliders for y and Δy; "Angkat ke bibir" animates the layer up to the rim (also a manual
 *        slider), leaving a dashed ghost at the original depth; a checkbox shows y, Δy, r and the
 *        distance already lifted.
 *
 * Depth y is measured down from the rim; the radius there is r = (6 - y)/2. The formula is not shown
 * on purpose: finding it is part of the exercise (hints 2–3 on the next slide).
 */
import { ref, computed, onMounted, onUnmounted, watch } from 'vue'

const props = withDefaults(defineProps<{ height?: string }>(), { height: '420px' })

const id3 = `jxg-tank3d-${Math.random().toString(36).slice(2, 9)}`
const id2 = id3.replace('3d', '2d')
const yv = ref(2)
const dyv = ref(0.5)
const showNum = ref(false)

const H = 6
const R = 3
const fmt = (v: number, d = 2) => v.toFixed(d).replace('.', ',')
const dy = computed(() => Math.min(dyv.value, H - yv.value))
const z0 = computed(() => H - yv.value)            // top of the layer, original position
const z1 = computed(() => H - yv.value - dy.value) // bottom of the layer, original position
const r = computed(() => (H - yv.value) / 2)

// lifting: lift = 0 at the original depth, 1 when the top of the layer reaches the rim
const lift = ref(0)
const zTop = computed(() => z0.value + lift.value * yv.value)
const zBot = computed(() => zTop.value - dy.value)
let raf = 0
const stopAnim = () => { if (raf) cancelAnimationFrame(raf); raf = 0 }
const animate = () => {
  stopAnim()
  const from = lift.value >= 0.999 ? 0 : lift.value
  const t0 = performance.now()
  const dur = 1500 * (1 - from)
  const step = (now: number) => {
    const s = Math.min(1, (now - t0) / Math.max(dur, 1))
    const e = s < 0.5 ? 2 * s * s : 1 - Math.pow(-2 * s + 2, 2) / 2   // ease in-out
    lift.value = from + (1 - from) * e
    raf = s < 1 ? requestAnimationFrame(step) : 0
  }
  raf = requestAnimationFrame(step)
}
const resetLift = () => { stopAnim(); lift.value = 0 }

let b3: any = null
let view: any = null
let b2: any = null
const observers: ResizeObserver[] = []
const dynamic: any[] = []

const clear = () => {
  while (dynamic.length) {
    const el = dynamic.pop()
    try { b3.removeObject(el) } catch (e) { /* ignore */ }
  }
}

const build3d = () => {
  if (!b3 || !view) return
  clear()
  const rr = r.value, top = zTop.value, bot = zBot.value
  const att = { strokeColor: '#fb7185', strokeWidth: 0.6, fillColor: '#fb7185', fillOpacity: 0.85, stepsU: 1, stepsV: 28 }
  // ghost of the original position
  if (lift.value > 0.01) {
    for (const zz of [z0.value, z1.value]) {
      dynamic.push(view.create('curve3d', [
        (t: number) => rr * Math.cos(t), (t: number) => rr * Math.sin(t), () => zz, [0, 2 * Math.PI]
      ], { strokeColor: '#fda4af', strokeWidth: 1.5, dash: 2 }))
    }
  }
  if (rr > 0.02 && top - bot > 0.005) {
    dynamic.push(view.create('parametricsurface3d', [
      (u: number, v: number) => rr * Math.cos(v), (u: number, v: number) => rr * Math.sin(v), (u: number) => u,
      [bot, top], [0, 2 * Math.PI]], att))
    for (const zz of [bot, top]) {
      dynamic.push(view.create('parametricsurface3d', [
        (u: number, v: number) => u * Math.cos(v), (u: number, v: number) => u * Math.sin(v), () => zz,
        [0, rr], [0, 2 * Math.PI]], att))
    }
  }
  if (H - top > 0.01) {
    dynamic.push(view.create('curve3d', [
      () => rr, () => 0, (t: number) => top + (H - top) * t, [0, 1]
    ], { strokeColor: '#f5be3c', strokeWidth: 2.5, dash: 2 }))
  }
  b3.update()
}

watch([yv, dyv], () => { resetLift(); build3d(); b2?.update() })
watch(lift, () => { build3d(); b2?.update() })

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

  // ---------- 3D ----------
  b3 = JXG.JSXGraph.initBoard(id3, {
    boundingbox: [-3, 3, 3, -3], axis: false, showNavigation: false, showCopyright: false,
    pan: { enabled: false }, zoom: { enabled: false }
  })
  view = b3.create('view3d', [[-2.1, -2.7], [4.2, 4.7], [[-3.2, 3.2], [-3.2, 3.2], [0, 6.2]]], {
    projection: 'parallel',
    az: { slider: { visible: false, start: 5.4 }, continuous: true },
    el: { slider: { visible: false, start: 0.35 }, continuous: true },
    bank: { slider: { visible: false } },
    xPlaneRear: { visible: false }, yPlaneRear: { visible: false }, zPlaneRear: { visible: false },
    xPlaneFront: { visible: false }, yPlaneFront: { visible: false },
    xAxis: { visible: false }, yAxis: { visible: false }, zAxis: { visible: false }
  })
  view.create('parametricsurface3d', [
    (u: number, v: number) => (u / 2) * Math.cos(v), (u: number, v: number) => (u / 2) * Math.sin(v), (u: number) => u,
    [0, H], [0, 2 * Math.PI]
  ], { strokeColor: '#50a5fa', strokeWidth: 0.5, strokeOpacity: 0.3, fillColor: '#50a5fa', fillOpacity: 0.1, stepsU: 8, stepsV: 28 })
  view.create('curve3d', [
    (t: number) => R * Math.cos(t), (t: number) => R * Math.sin(t), () => H, [0, 2 * Math.PI]
  ], { strokeColor: '#f5be3c', strokeWidth: 2.5 })
  build3d()

  // ---------- 2D cross-section ----------
  b2 = JXG.JSXGraph.initBoard(id2, {
    boundingbox: [-4.6, 7.2, 4.6, -0.6], axis: false, showNavigation: false, showCopyright: false,
    keepaspectratio: false, pan: { enabled: false }, zoom: { enabled: false }
  })
  const fix = { fixed: true, highlight: false }
  b2.create('polygon', [[-R, H], [R, H], [0, 0]], {
    fillColor: '#50a5fa', fillOpacity: 0.18, borders: { strokeColor: '#50a5fa', strokeWidth: 2.5 }, vertices: { visible: false }, ...fix
  })
  b2.create('segment', [[-R - 0.4, H], [R + 0.4, H]], { strokeColor: '#f5be3c', strokeWidth: 2.5, ...fix })
  b2.create('text', [-1.5, H + 0.5, 'bibir tangki'], { anchorX: 'middle', color: '#94a3b8', fontSize: 12, ...fix })
  b2.create('segment', [[0, 0], [0, H]], { strokeColor: '#475569', dash: 2, strokeWidth: 1, ...fix })
  const lifted = () => lift.value > 0.01
  // ghost of the original position
  b2.create('polygon', [
    [() => -r.value, () => z1.value], [() => r.value, () => z1.value],
    [() => r.value, () => z0.value], [() => -r.value, () => z0.value]
  ], { fillColor: '#fb7185', fillOpacity: 0.08, borders: { strokeColor: '#fda4af', strokeWidth: 1.2, dash: 2 }, vertices: { visible: false }, visible: lifted, ...fix })
  // moving layer
  const layer = b2.create('polygon', [
    [() => -r.value, () => zBot.value], [() => r.value, () => zBot.value],
    [() => r.value, () => zTop.value], [() => -r.value, () => zTop.value]
  ], { fillColor: '#fb7185', fillOpacity: 0.85, borders: { strokeColor: '#fb7185', strokeWidth: 1.5 }, vertices: { visible: false }, ...fix })
  ;(layer as any).__isLayer = true
  // distance already travelled (left edge of the layer)
  b2.create('segment', [[() => -r.value - 0.25, () => z0.value], [() => -r.value - 0.25, () => zTop.value]], {
    strokeColor: '#fb7185', strokeWidth: 2.5, lastArrow: true, visible: lifted, ...fix
  })
  // r
  b2.create('segment', [[0, () => zTop.value], [() => r.value, () => zTop.value]], { strokeColor: '#34d399', strokeWidth: 3, ...fix })
  b2.create('text', [() => r.value / 2, () => zTop.value + 0.3, 'r'], { anchorX: 'middle', color: '#34d399', fontSize: 15, ...fix })
  // depth / lift y (left)
  b2.create('segment', [[-3.9, H], [-3.9, () => z0.value]], { strokeColor: '#f5be3c', strokeWidth: 2, firstArrow: true, lastArrow: true, ...fix })
  b2.create('segment', [[-3.9, () => z0.value], [() => -r.value, () => z0.value]], { strokeColor: '#f5be3c', dash: 2, strokeWidth: 1, ...fix })
  b2.create('text', [-4.4, () => (H + z0.value) / 2, 'y'], { color: '#f5be3c', fontSize: 15, anchorY: 'middle', ...fix })
  // thickness (right)
  b2.create('segment', [[() => r.value + 0.35, () => zBot.value], [() => r.value + 0.35, () => zTop.value]], { strokeColor: '#fb7185', strokeWidth: 2, ...fix })
  b2.create('text', [() => r.value + 0.55, () => (zTop.value + zBot.value) / 2, 'Δy'], { color: '#fb7185', fontSize: 14, anchorY: 'middle', ...fix })
  // remaining lift on the right edge of the layer
  b2.create('segment', [[() => r.value, () => zTop.value], [() => r.value, H]], {
    strokeColor: '#f5be3c', dash: 2, strokeWidth: 2, lastArrow: true, visible: () => H - zTop.value > 0.05, ...fix
  })

  for (const [id, bd] of [[id3, b3], [id2, b2]] as const) {
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
  stopAnim()
  observers.forEach(o => o.disconnect())
  clear()
  const JXG = (window as any).JXG
  for (const bd of [b3, b2]) { try { if (bd) JXG?.JSXGraph.freeBoard(bd) } catch (e) { /* ignore */ } }
  b3 = null; b2 = null; view = null
})
</script>

<template>
  <div class="tk flex flex-col gap-2 w-full" :style="{ height: props.height }">
    <div class="flex gap-2" style="flex: 1 1 auto; min-height: 0;">
      <div class="tk-cell">
        <div :id="id3" class="jxgbox tk-box"></div>
        <div class="tk-cap">3D · seret untuk memutar</div>
      </div>
      <div class="tk-cell">
        <div :id="id2" class="jxgbox tk-box"></div>
        <div class="tk-cap">penampang tegak</div>
      </div>
    </div>
    <div class="tk-panel">
      <label class="tk-row">
        <span>kedalaman y</span>
        <input type="range" min="0" max="5.8" step="0.1" v-model.number="yv" />
      </label>
      <label class="tk-row">
        <span>tebal Δy</span>
        <input type="range" min="0.1" max="1" step="0.05" v-model.number="dyv" />
      </label>
      <div class="tk-lift">
        <button type="button" class="tk-btn" @click="animate">▶ Angkat ke bibir</button>
        <button type="button" class="tk-btn tk-btn-sm" title="kembalikan ke kedalaman asal" @click="resetLift">↺</button>
        <input type="range" min="0" max="1" step="0.01" v-model.number="lift" aria-label="angkat lapisan" />
        <span class="tk-pct">{{ Math.round(lift * 100) }}%</span>
      </div>
      <div class="tk-foot">
        <label class="tk-check"><input type="checkbox" v-model="showNum" /> tampilkan ukuran</label>
        <span v-if="showNum" class="tk-num">y = <b>{{ fmt(yv) }}</b> · Δy = <b>{{ fmt(dy) }}</b> · r = <b>{{ fmt(r) }}</b> · sudah naik <b>{{ fmt(lift * yv) }}</b> m dari y = {{ fmt(yv) }} m</span>
        <span v-else class="tk-legend"><i class="sw sw-r"></i> lapisan air &nbsp; <i class="sw sw-y"></i> jarak angkat</span>
      </div>
    </div>
  </div>
</template>

<style>
.tk { font-size: 0.78rem; color: #e2e8f0; }
.tk-cell { flex: 1 1 0; min-width: 0; display: flex; flex-direction: column; }
.tk-box { flex: 1 1 auto; min-height: 0; border-radius: 0.75rem; border: 1px solid #334155; overflow: hidden; background-color: #0c1018 !important; }
.tk .jxgbox svg { background-color: #0c1018 !important; }
.tk .jxgbox .JXGtext { color: #e2e8f0 !important; }
.tk-cap { font-size: 0.66rem; color: #64748b; text-align: center; margin-top: 0.15rem; }
.tk-panel { background: #141b28; border: 1px solid #233148; border-radius: 0.75rem; padding: 0.45rem 0.7rem; display: grid; grid-template-columns: 1fr 1fr; gap: 0.25rem 1rem; }
.tk-row { display: flex; align-items: center; gap: 0.5rem; }
.tk-row span { white-space: nowrap; color: #cbd5e1; }
.tk-row input { flex: 1; accent-color: #f5be3c; min-width: 0; }
.tk-foot { grid-column: 1 / -1; display: flex; align-items: center; gap: 0.8rem; }
.tk-lift { grid-column: 1 / -1; display: flex; align-items: center; gap: 0.5rem; }
.tk-lift input { flex: 1; accent-color: #fb7185; min-width: 0; }
.tk-btn { background: rgba(251, 113, 133, 0.15); color: #fda4af; border: 1px solid rgba(251, 113, 133, 0.5); border-radius: 0.4rem; padding: 0.1rem 0.55rem; font-size: 0.74rem; cursor: pointer; white-space: nowrap; }
.tk-btn:hover { background: rgba(251, 113, 133, 0.28); }
.tk-btn-sm { padding: 0.1rem 0.4rem; }
.tk-pct { font-family: ui-monospace, monospace; color: #94a3b8; width: 2.6rem; text-align: right; }
.tk-check { display: flex; align-items: center; gap: 0.35rem; cursor: pointer; white-space: nowrap; }
.tk-check input { accent-color: #2dd4bf; }
.tk-num { font-family: ui-monospace, monospace; color: #cbd5e1; font-size: 0.7rem; }
.tk-num b { color: #34d399; }
.tk-legend { color: #94a3b8; display: flex; align-items: center; gap: 0.3rem; }
.tk .sw { display: inline-block; width: 0.9rem; height: 0.55rem; border-radius: 2px; }
.tk .sw-r { background: #fb7185; }
.tk .sw-y { border-top: 2px dashed #f5be3c; height: 0; }
</style>
