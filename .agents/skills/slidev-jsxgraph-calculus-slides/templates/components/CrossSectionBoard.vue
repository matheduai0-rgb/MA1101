<script setup lang="ts">
import { ref, onMounted, onUnmounted, useId } from 'vue'

const props = withDefaults(defineProps<{
  height?: string
  radius?: number
}>(), {
  height: '320px',
  radius: 3
})

const containerId = `jxg-cross-${Math.random().toString(36).slice(2, 9)}`
const xVal = ref<number>(1.2)
const shape = ref<'square' | 'semicircle' | 'triangle'>('square')
const chordLen = ref<number>(0)
const areaVal = ref<number>(0)

let board: any = null
let chordSeg: any = null
let pTop: any = null
let pBot: any = null

const computeChord = (x: number, r: number) => 2 * Math.sqrt(Math.max(0, r * r - x * x))

const updateCalculations = () => {
  const x = xVal.value
  const r = props.radius
  const s = computeChord(x, r)
  chordLen.value = parseFloat(s.toFixed(3))

  let c = 1.0
  if (shape.value === 'square') c = 1.0
  else if (shape.value === 'semicircle') c = Math.PI / 8
  else if (shape.value === 'triangle') c = Math.sqrt(3) / 4

  areaVal.value = parseFloat((c * s * s).toFixed(3))

  const yHalf = s / 2
  if (board) {
    if (pTop) pTop.moveTo([x, yHalf])
    if (pBot) pBot.moveTo([x, -yHalf])
    if (chordSeg) {
      chordSeg.point1.moveTo([x, -yHalf])
      chordSeg.point2.moveTo([x, yHalf])
    }
    board.update()
  }
}

const setShape = (s: 'square' | 'semicircle' | 'triangle') => {
  shape.value = s
  updateCalculations()
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
    boundingbox: [-3.8, 3.8, 3.8, -3.8],
    axis: true,
    showNavigation: false,
    showCopyright: false,
    keepaspectratio: true
  })

  // Circle base
  const origin = board.create('point', [0, 0], { visible: false })
  board.create('circle', [origin, props.radius], {
    strokeColor: '#50a5fa',
    strokeWidth: 2.5,
    fillColor: '#50a5fa',
    fillOpacity: 0.1
  })

  // Chord segment
  const yH = computeChord(xVal.value, props.radius) / 2
  pTop = board.create('point', [xVal.value, yH], {
    name: 'T',
    color: '#2dd4bf',
    size: 2.5,
    label: { visible: false }
  })
  pBot = board.create('point', [xVal.value, -yH], {
    name: 'B',
    color: '#2dd4bf',
    size: 2.5,
    label: { visible: false }
  })
  chordSeg = board.create('segment', [pBot, pTop], {
    strokeColor: '#2dd4bf',
    strokeWidth: 5
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
        <span class="text-slate-400 font-medium">Irisan $x$:</span>
        <input 
          type="range" 
          min="-2.8" 
          max="2.8" 
          step="0.1" 
          v-model.number="xVal" 
          @input="updateCalculations" 
          class="w-24 accent-cyan-400 cursor-pointer"
        />
        <span class="font-mono text-cyan-300 font-bold w-9">{{ xVal.toFixed(1) }}</span>
      </div>

      <div class="flex items-center gap-1">
        <button 
          @click="setShape('square')"
          :class="shape === 'square' ? 'bg-cyan-600 text-white' : 'bg-slate-800 text-slate-300'"
          class="px-2 py-0.5 rounded text-2xs transition-colors hover:bg-cyan-500"
        >Bujursangkar</button>
        <button 
          @click="setShape('semicircle')"
          :class="shape === 'semicircle' ? 'bg-cyan-600 text-white' : 'bg-slate-800 text-slate-300'"
          class="px-2 py-0.5 rounded text-2xs transition-colors hover:bg-cyan-500"
        >½ Lingkaran</button>
        <button 
          @click="setShape('triangle')"
          :class="shape === 'triangle' ? 'bg-cyan-600 text-white' : 'bg-slate-800 text-slate-300'"
          class="px-2 py-0.5 rounded text-2xs transition-colors hover:bg-cyan-500"
        >Δ Sama Sisi</button>
      </div>

      <div class="flex items-center gap-3 font-mono text-xs">
        <span class="text-teal-300">s(x) = {{ chordLen }}</span>
        <span class="text-slate-600">|</span>
        <span class="text-amber-400 font-bold">A(x) = {{ areaVal }}</span>
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
