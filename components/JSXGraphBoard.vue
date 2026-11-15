<script setup lang="ts">
import { ref, onMounted, onUnmounted, useId } from 'vue'

const props = withDefaults(defineProps<{
  boundingbox?: number[]
  axis?: boolean
  showNavigation?: boolean
  showCopyright?: boolean
  height?: string
  width?: string
  init: (board: any, JXG: any) => void
}>(), {
  boundingbox: () => [-5, 5, 5, -5],
  axis: true,
  showNavigation: false,
  showCopyright: false,
  height: '320px',
  width: '100%'
})

const containerId = useId ? useId() : `jxgbox-${Math.random().toString(36).slice(2, 9)}`
let board: any = null
let resizeObserver: ResizeObserver | null = null

onMounted(async () => {
  if (typeof window === 'undefined') return

  // Dynamically import JSXGraph on the client side
  const mod = await import('jsxgraph')
  const JXG = mod.default || (window as any).JXG || mod

  // Ensure JSXGraph CSS is loaded
  if (!document.getElementById('jsxgraph-css')) {
    const link = document.createElement('link')
    link.id = 'jsxgraph-css'
    link.rel = 'stylesheet'
    link.type = 'text/css'
    link.href = 'https://cdn.jsdelivr.net/npm/jsxgraph/distrib/jsxgraph.css'
    document.head.appendChild(link)
  }

  // Initialize board
  board = JXG.JSXGraph.initBoard(containerId, {
    boundingbox: props.boundingbox,
    axis: props.axis,
    showNavigation: props.showNavigation,
    showCopyright: props.showCopyright,
    keepaspectratio: false,
    pan: { enabled: true, needShift: false },
    zoom: { enabled: true, needShift: false }
  })

  // Hook user initialization logic
  if (props.init) {
    props.init(board, JXG)
  }

  // Handle slide scale & viewport changes
  const el = document.getElementById(containerId)
  if (el && typeof ResizeObserver !== 'undefined') {
    resizeObserver = new ResizeObserver(() => {
      if (board) {
        board.resizeContainer(el.clientWidth, el.clientHeight, true)
        board.update()
      }
    })
    resizeObserver.observe(el)
  }
})

onUnmounted(() => {
  if (resizeObserver) {
    resizeObserver.disconnect()
    resizeObserver = null
  }
  if (board) {
    const JXG = (window as any).JXG
    if (JXG && JXG.JSXGraph) {
      JXG.JSXGraph.freeBoard(board)
    }
    board = null
  }
})
</script>

<template>
  <div 
    :id="containerId" 
    class="jxgbox rounded-xl border border-slate-700/70 shadow-2xl overflow-hidden bg-[#0c1018]" 
    :style="{ width: props.width, height: props.height }"
  ></div>
</template>

<style>
/* 3Blue1Brown Obsidian styling for JSXGraph controls */
.jxgbox {
  background-color: #0c1018 !important;
}
.jxgbox svg {
  background-color: #0c1018 !important;
}
.jxgbox .JXGtext {
  font-family: inherit !important;
  color: #e2e8f0 !important;
}
</style>
