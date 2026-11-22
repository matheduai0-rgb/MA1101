<script setup lang="ts">
import { ref, onMounted, onUnmounted, useId } from 'vue'

const props = withDefaults(defineProps<{
  height?: string
}>(), {
  height: '320px'
})

const containerId = `jxg-washer-${Math.random().toString(36).slice(2, 9)}`
const xVal = ref<number>(0.60)
const rOuter = ref<number>(0)
const rInner = ref<number>(0)
const areaVal = ref<number>(0)

let board: any = null
let sliceLine: any = null
let ptOuter: any = null
let ptInner: any = null

const fOuter = (x: number) => Math.sqrt(Math.max(0, x))
const fInner = (x: number) => x * x

const updateCalculations = () => {
  const x = xVal.value
  const R = Math.sqrt(x)
  const r = x * x
  rOuter.value = parseFloat(R.toFixed(3))
  rInner.value = parseFloat(r.toFixed(3))
  const A = Math.PI * (R * R - r * r)
  areaVal.value = parseFloat(A.toFixed(3))

  if (board) {
    if (ptOuter) ptOuter.moveTo([x, R])
    if (ptInner) ptInner.moveTo([x, r])
    if (sliceLine) sliceLine.point1.moveTo([x, r])
    if (sliceLine) sliceLine.point2.moveTo([x, R])
    board.update()
  }
}

onMounted(async () => {
  if (typeof window === 'undefined') return

  const mod = await import('jsxgraph')
  const JXG = mod.default || (window as any).JXG || mod

  if (!document.getElementById('jsxgraph-css')) {
    const link = document.createElement('link')
    link.id = 'jsxgraph-css'
    link.rel = 'stylesheet'
    link.type = 'text/css'
    link.href = 'https://cdn.jsdelivr.net/npm/jsxgraph/distrib/jsxgraph.css'
    document.head.appendChild(link)
  }

  board = JXG.JSXGraph.initBoard(containerId, {
    boundingbox: [-0.2, 1.25, 1.25, -0.2],
    axis: true,
    showNavigation: false,
    showCopyright: false,
    keepaspectratio: false
  })

  // Plot curves
  board.create('functiongraph', [fOuter, 0, 1], { strokeColor: '#50a5fa', strokeWidth: 3 })
  board.create('functiongraph', [fInner, 0, 1], { strokeColor: '#fb7185', strokeWidth: 3 })

  // Fill region between curves
  board.create('curve', [
    (t: number) => t,
    (t: number) => fInner(t)
  ], { strokeColor: 'transparent', fillColor: '#2dd4bf', fillOpacity: 0.15 })

  // Representative slice
  const p1 = board.create('point', [() => xVal.value, () => fInner(xVal.value)], { visible: false })
  const p2 = board.create('point', [() => xVal.value, () => fOuter(xVal.value)], { visible: false })
  sliceLine = board.create('segment', [p1, p2], { strokeColor: '#2dd4bf', strokeWidth: 6 })

  ptOuter = board.create('point', [() => xVal.value, () => fOuter(xVal.value)], {
    name: 'R(x)',
    color: '#50a5fa',
    size: 3,
    label: { offset: [-15, 12], strokeColor: '#50a5fa' }
  })

  ptInner = board.create('point', [() => xVal.value, () => fInner(xVal.value)], {
    name: 'r(x)',
    color: '#fb7185',
    size: 3,
    label: { offset: [8, -8], strokeColor: '#fb7185' }
  })

  updateCalculations()
})

onUnmounted(() => {
  if (board) {
    const JXG = (window as any).JXG
    if (JXG && JXG.JSXGraph) JXG.JSXGraph.freeBoard(board)
    board = null
  }
})
</script>

<template>
  <div class="flex flex-col gap-2 w-full">
    <!-- Controls Bar -->
    <div class="flex items-center justify-between bg-[#141b28] px-3 py-1.5 rounded-lg border border-slate-700 text-xs">
      <div class="flex items-center gap-2">
        <span class="text-slate-400 font-medium">Posisi Irisan $x$:</span>
        <input 
          type="range" 
          min="0.05" 
          max="0.95" 
          step="0.01" 
          v-model.number="xVal" 
          @input="updateCalculations" 
          class="w-28 accent-cyan-400 cursor-pointer"
        />
        <span class="font-mono text-cyan-300 font-bold w-10">{{ xVal.toFixed(2) }}</span>
      </div>

      <div class="flex items-center gap-3 font-mono text-xs">
        <span class="text-blue-400">R = {{ rOuter }}</span>
        <span class="text-slate-600">|</span>
        <span class="text-rose-400">r = {{ rInner }}</span>
        <span class="text-slate-600">|</span>
        <span class="text-amber-400 font-bold">A(x) = π(R² - r²) ≈ {{ areaVal }}</span>
      </div>
    </div>

    <!-- JSXGraph Container -->
    <div 
      :id="containerId" 
      class="jxgbox rounded-xl border border-slate-700/70 shadow-xl overflow-hidden bg-[#0c1018]" 
      :style="{ width: '100%', height: props.height }"
    ></div>
  </div>
</template>
