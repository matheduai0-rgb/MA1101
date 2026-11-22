<script setup lang="ts">
import { ref, onMounted, onUnmounted, useId } from 'vue'

const props = withDefaults(defineProps<{
  initialN?: number
  height?: string
  a?: number
  b?: number
}>(), {
  initialN: 6,
  height: '310px',
  a: 0.5,
  b: 4.5
})

const containerId = useId ? useId() : `riemann-${Math.random().toString(36).slice(2, 9)}`
const nValue = ref(props.initialN)
const sumType = ref<'left' | 'middle' | 'right'>('middle')
const sumValue = ref<number>(0)
const exactValue = ref<number>(0)

let board: any = null
let riemannSumElement: any = null
let curveElement: any = null

// Target function: f(x) = -0.2 * (x - 2)^2 + 3.2
const f = (x: number) => -0.2 * Math.pow(x - 2, 2) + 3.2

// Exact analytical integral of -0.2*(x-2)^2 + 3.2 from a to b
const computeExact = (a: number, b: number) => {
  const F = (x: number) => (-0.2 / 3) * Math.pow(x - 2, 3) + 3.2 * x
  return F(b) - F(a)
}

const updateRiemann = () => {
  if (!board || !riemannSumElement) return
  board.update()
  if (typeof riemannSumElement.Value === 'function') {
    sumValue.value = parseFloat(riemannSumElement.Value().toFixed(4))
  }
}

const setType = (type: 'left' | 'middle' | 'right') => {
  sumType.value = type
  if (riemannSumElement) {
    riemannSumElement.setType(type)
    updateRiemann()
  }
}

onMounted(async () => {
  if (typeof window === 'undefined') return
  exactValue.value = parseFloat(computeExact(props.a, props.b).toFixed(4))

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
    boundingbox: [-0.5, 4.2, 5.5, -0.8],
    axis: true,
    showNavigation: false,
    showCopyright: false,
    keepaspectratio: false
  })

  // Plot curve f(x)
  curveElement = board.create('functiongraph', [f, -0.5, 5.5], {
    strokeColor: '#50a5fa',
    strokeWidth: 3
  })

  // Create dynamic Riemann sum
  riemannSumElement = board.create('riemannsum', [
    f,
    () => nValue.value,
    () => sumType.value,
    props.a,
    props.b
  ], {
    fillColor: '#2dd4bf',
    fillOpacity: 0.35,
    strokeColor: '#14b8a6',
    strokeWidth: 1.5
  })

  // Integral bounds markers
  board.create('point', [props.a, 0], { name: 'a', fixed: true, size: 2, color: '#f5be3c' })
  board.create('point', [props.b, 0], { name: 'b', fixed: true, size: 2, color: '#f5be3c' })

  updateRiemann()
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
    <!-- Interactive Controls Bar -->
    <div class="flex items-center justify-between bg-[#141b28] px-3 py-1.5 rounded-lg border border-slate-700 text-xs">
      <div class="flex items-center gap-2">
        <span class="text-slate-400 font-medium">Partisi $n$:</span>
        <input 
          type="range" 
          min="2" 
          max="60" 
          step="1" 
          v-model.number="nValue" 
          @input="updateRiemann" 
          class="w-28 accent-cyan-400 cursor-pointer"
        />
        <span class="font-mono text-cyan-300 font-bold w-6">{{ nValue }}</span>
      </div>

      <div class="flex items-center gap-1">
        <button 
          @click="setType('left')"
          :class="sumType === 'left' ? 'bg-cyan-600 text-white' : 'bg-slate-800 text-slate-300'"
          class="px-2 py-0.5 rounded text-2xs transition-colors hover:bg-cyan-500"
        >Kiri</button>
        <button 
          @click="setType('middle')"
          :class="sumType === 'middle' ? 'bg-cyan-600 text-white' : 'bg-slate-800 text-slate-300'"
          class="px-2 py-0.5 rounded text-2xs transition-colors hover:bg-cyan-500"
        >Tengah</button>
        <button 
          @click="setType('right')"
          :class="sumType === 'right' ? 'bg-cyan-600 text-white' : 'bg-slate-800 text-slate-300'"
          class="px-2 py-0.5 rounded text-2xs transition-colors hover:bg-cyan-500"
        >Kanan</button>
      </div>

      <div class="flex items-center gap-3 font-mono">
        <span class="text-emerald-400">∑ = {{ sumValue }}</span>
        <span class="text-slate-500">|</span>
        <span class="text-amber-400">∫ = {{ exactValue }}</span>
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
