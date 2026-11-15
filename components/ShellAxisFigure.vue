<script setup lang="ts">
/**
 * ShellAxisFigure — radius of a shell when the axis of rotation is NOT the y-axis.
 *
 * Region under y = 2x^2 - x^3 on [0, 2], one vertical strip (width Δx) at x = 1,1.
 * The axis of rotation is the vertical line x = `axis` (default -1).
 *   coral arrow: distance from the y-axis to the strip  (what a student wrongly uses: x)
 *   gold arrow : distance from the axis of rotation to the strip (the true radius)
 *
 * reveal = false -> the gold arrow is labeled "?"; reveal = true -> it shows "x + 1".
 * In a slide use :reveal="$clicks >= 1" so the label changes when the answer block appears.
 */
import { computed } from 'vue'

const props = withDefaults(defineProps<{
  axis?: number
  reveal?: boolean
  height?: string
}>(), { axis: -1, reveal: false, height: 'auto' })

const X = (x: number) => 110 + 70 * x
const Y = (y: number) => 205 - 95 * y
const f = (x: number) => 2 * x * x - x * x * x

const curve = computed(() => {
  let d = ''
  for (let i = 0; i <= 40; i++) {
    const x = i * 0.05
    d += (i === 0 ? 'M' : ' L') + X(x).toFixed(1) + ' ' + Y(f(x)).toFixed(1)
  }
  return d
})
const region = computed(() => curve.value + ` L${X(2)} ${Y(0)} L${X(0)} ${Y(0)} Z`)

const x0 = 1.1
const dx = 0.2
const radiusLabel = computed(() => {
  if (!props.reveal) return 'jarak ke sumbu putar = ?'
  if (props.axis < 0) return `x + ${-props.axis}   (jarak sebenarnya)`
  return `${props.axis} − x   (jarak sebenarnya)`
})
</script>

<template>
  <svg class="sa" :style="{ height: props.height }" viewBox="0 0 320 284" role="img" preserveAspectRatio="xMidYMid meet">
    <defs>
      <marker id="sa-gold" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
        <path d="M0 0 L10 5 L0 10 z" fill="#f5be3c" />
      </marker>
      <marker id="sa-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
        <path d="M0 0 L10 5 L0 10 z" fill="#50a5fa" />
      </marker>
      <marker id="sa-coral" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
        <path d="M0 0 L10 5 L0 10 z" fill="#fb7185" />
      </marker>
    </defs>

    <line :x1="X(-1.15)" :y1="Y(0)" :x2="X(2.25)" :y2="Y(0)" class="base" />
    <path :d="region" class="area" />
    <path :d="curve" class="curve" />

    <!-- axis of rotation -->
    <line :x1="X(props.axis)" y1="40" :x2="X(props.axis)" y2="254" class="rot" />
    <text :x="X(props.axis)" y="14" class="lab gold" text-anchor="middle">sumbu putar</text>
    <text :x="X(props.axis)" y="30" class="lab gold" text-anchor="middle">x = {{ String(props.axis).replace('-', '−') }}</text>

    <!-- y-axis -->
    <line :x1="X(0)" y1="62" :x2="X(0)" y2="234" class="yax" />
    <text :x="X(0) + 5" y="62" class="note">sumbu-y</text>

    <!-- strip -->
    <rect :x="X(x0)" :y="Y(f(x0))" :width="X(x0 + dx) - X(x0)" :height="Y(0) - Y(f(x0))" class="strip" />
    <text :x="X(x0 + dx) + 6" :y="Y(0) + 17" class="lab coral">Δx</text>
    <line :x1="X(x0 + dx) + 9" :y1="Y(f(x0))" :x2="X(x0 + dx) + 9" :y2="Y(0)" class="dimb" marker-start="url(#sa-blue)" marker-end="url(#sa-blue)" />
    <text :x="X(x0 + dx) + 15" :y="Y(0) - 12" class="lab blue">f(x)</text>

    <!-- guide from strip down -->
    <line :x1="X(x0)" :y1="Y(0)" :x2="X(x0)" y2="254" class="guide" />

    <!-- Dani's distance: y-axis to strip -->
    <line :x1="X(0) + 1" y1="232" :x2="X(x0) - 1" y2="232" class="dimc" marker-start="url(#sa-coral)" marker-end="url(#sa-coral)" />
    <text :x="(X(0) + X(x0)) / 2" y="224" class="lab coral" text-anchor="middle">x</text>

    <!-- true radius: axis of rotation to strip -->
    <line :x1="X(props.axis) + 1" y1="254" :x2="X(x0) - 1" y2="254" class="dimg" marker-start="url(#sa-gold)" marker-end="url(#sa-gold)" />
    <text :x="(X(props.axis) + X(x0)) / 2" y="278" class="lab gold" text-anchor="middle">{{ radiusLabel }}</text>
  </svg>
</template>

<style>
.sa { width: 100%; display: block; font-family: inherit; }
.sa .base { stroke: #64748b; stroke-width: 1.6; }
.sa .area { fill: rgba(80, 165, 250, 0.2); }
.sa .curve { fill: none; stroke: #50a5fa; stroke-width: 3; stroke-linejoin: round; }
.sa .rot { stroke: #f5be3c; stroke-width: 4; stroke-linecap: round; }
.sa .yax { stroke: #94a3b8; stroke-width: 1.5; stroke-dasharray: 5 4; }
.sa .strip { fill: rgba(251, 113, 133, 0.7); stroke: #fb7185; stroke-width: 1.5; }
.sa .guide { stroke: #475569; stroke-width: 1.2; stroke-dasharray: 4 4; }
.sa .dimc { stroke: #fb7185; stroke-width: 2; }
.sa .dimg { stroke: #f5be3c; stroke-width: 2; }
.sa .dimb { stroke: #50a5fa; stroke-width: 1.6; }
.sa text { fill: #cbd5e1; font-size: 12px; }
.sa .note { fill: #94a3b8; font-size: 12px; }
.sa .lab { font-size: 14px; font-weight: 600; }
.sa .gold { fill: #f5be3c; }
.sa .coral { fill: #fb7185; }
.sa .blue { fill: #50a5fa; }
</style>
