<script setup lang="ts">
/**
 * WorkFigure — fixed illustrations for the "Kerja" (work) lecture, drawn as inline SVG.
 * Every figure shows ONE thin slice with its label (Δx for a spring, Δy for a cable or tank layer)
 * so the picture matches the "cut, approximate, add up" argument. No answers are shown.
 *
 * kind:
 *   spring        natural-length spring and the spring stretched by 0,3 m
 *   spring-force  spring on top, force graph F(x) below, same slice Δx in both, ΔW ≈ F(x)·Δx
 *   spring-ex     Stewart example: 10, 15 and 18 cm, x measured from natural length
 *   cable         hanging cable, slice Δy at depth y, lifted a distance y
 *   tank          inverted cone tank, water layer Δy at depth y, radius r
 */
const props = withDefaults(defineProps<{
  kind?: 'spring' | 'spring-force' | 'spring-ex' | 'cable' | 'tank'
  height?: string
  /** cable only: show "berat" and "naik sejauh y" labels. Use false while students are asked for them. */
  reveal?: boolean
}>(), { kind: 'spring', height: 'auto', reveal: true })

// zigzag spring between x0 and x1 on the line y
const zig = (x0: number, x1: number, y: number, n = 8, amp = 13) => {
  const lead = 14
  const a = x0 + lead
  const b = x1 - lead
  let d = `M${x0} ${y} L${a} ${y}`
  for (let i = 0; i < n * 2; i++) {
    const x = a + (i + 0.5) * (b - a) / (n * 2)
    d += ` L${x.toFixed(1)} ${y + (i % 2 === 0 ? -amp : amp)}`
  }
  return d + ` L${b} ${y} L${x1} ${y}`
}

const xm = (v: number) => 60 + v * 1100   // spring-force: metres -> px
</script>

<template>
  <svg class="wf" :style="{ height: props.height }" :viewBox="props.kind === 'spring' ? '0 0 440 235'
    : props.kind === 'spring-force' ? '0 0 440 395'
    : props.kind === 'spring-ex' ? '0 0 440 265'
    : props.kind === 'cable' ? '0 0 300 285'
    : '0 0 250 200'" role="img" preserveAspectRatio="xMidYMid meet">
    <defs>
      <marker id="wf-a-gold" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
        <path d="M0 0 L10 5 L0 10 z" fill="#f5be3c" />
      </marker>
      <marker id="wf-a-coral" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
        <path d="M0 0 L10 5 L0 10 z" fill="#fb7185" />
      </marker>
      <marker id="wf-a-grey" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
        <path d="M0 0 L10 5 L0 10 z" fill="#64748b" />
      </marker>
      </defs>

    <!-- ============ spring ============ -->
    <g v-if="props.kind === 'spring'">
      <line x1="30" y1="40" x2="30" y2="170" class="wall" />
      <path :d="zig(30, 170, 62)" class="coil" />
      <rect x="170" y="48" width="28" height="28" class="block" />
      <text x="212" y="66" class="note">panjang alami</text>

      <path :d="zig(30, 330, 140)" class="coil" />
      <rect x="330" y="126" width="28" height="28" class="block" />
      <line x1="362" y1="140" x2="420" y2="140" class="force" marker-end="url(#wf-a-coral)" />
      <text x="364" y="126" class="lab coral">F = 100x</text>

      <line x1="170" y1="86" x2="170" y2="215" class="guide" />
      <line x1="330" y1="164" x2="330" y2="215" class="guide" />
      <line x1="171" y1="205" x2="329" y2="205" class="dim" marker-start="url(#wf-a-gold)" marker-end="url(#wf-a-gold)" />
      <text x="250" y="198" class="lab gold" text-anchor="middle">x = 0,3 m</text>
      <text x="170" y="226" class="note" text-anchor="middle">x = 0</text>
    </g>

    <!-- ============ spring + force graph ============ -->
    <g v-else-if="props.kind === 'spring-force'">
      <line x1="30" y1="45" x2="30" y2="100" class="wall" />
      <path :d="zig(30, xm(0.3), 72)" class="coil" />
      <rect :x="xm(0.3)" y="58" width="28" height="28" class="block" />
      <line :x1="xm(0)" y1="44" :x2="xm(0)" y2="350" class="guide" />
      <text :x="xm(0) + 4" y="40" class="note">x = 0 (panjang alami)</text>

      <line :x1="xm(0)" y1="106" :x2="xm(0.3)" y2="106" class="axis" />
      <rect :x="xm(0.18)" y="98" :width="xm(0.21) - xm(0.18)" height="16" class="slice" />
      <text :x="(xm(0.18) + xm(0.21)) / 2" y="132" class="lab coral" text-anchor="middle">Δx</text>
      <line :x1="xm(0.18)" y1="114" :x2="xm(0.18)" y2="269" class="guide coralline" />
      <line :x1="xm(0.21)" y1="114" :x2="xm(0.21)" y2="269" class="guide coralline" />

      <line x1="52" y1="350" x2="412" y2="350" class="axis" marker-end="url(#wf-a-grey)" />
      <line x1="60" y1="352" x2="60" y2="190" class="axis" marker-end="url(#wf-a-grey)" />
      <text x="410" y="378" class="note" text-anchor="end">x (m)</text>
      <text x="68" y="196" class="note">F (N)</text>
      <line x1="60" y1="350" :x2="xm(0.3)" y2="215" class="curve" />
      <text :x="xm(0.3) - 4" y="205" class="lab blue" text-anchor="end">F(x) = 100x</text>
      <text x="60" y="368" class="note" text-anchor="middle">0</text>
      <text :x="xm(0.3)" y="368" class="note" text-anchor="middle">0,3</text>

      <rect :x="xm(0.18)" y="269" :width="xm(0.21) - xm(0.18)" height="81" class="area" />
      <text :x="xm(0.18)" y="368" class="note" text-anchor="middle">x</text>
      <line :x1="xm(0.18) - 10" y1="269" :x2="xm(0.18) - 10" y2="350" class="dim" marker-start="url(#wf-a-gold)" marker-end="url(#wf-a-gold)" />
      <text :x="xm(0.18) - 16" y="314" class="lab gold" text-anchor="end">F(x)</text>
      <text :x="(xm(0.18) + xm(0.21)) / 2" y="384" class="lab coral" text-anchor="middle">Δx</text>
      <text x="70" y="282" class="lab gold">ΔW ≈ F(x) · Δx</text>
      <line x1="178" y1="278" :x2="xm(0.18) + 4" y2="300" class="leader" />
    </g>

    <!-- ============ Stewart spring example ============ -->
    <g v-else-if="props.kind === 'spring-ex'">
      <line x1="20" y1="20" x2="20" y2="200" class="wall" />
      <path :d="zig(20, 140, 45, 7, 11)" class="coil" />
      <rect x="140" y="33" width="24" height="24" class="block" />
      <text x="182" y="50" class="note">panjang alami 10 cm</text>

      <path :d="zig(20, 200, 110, 9, 11)" class="coil" />
      <rect x="200" y="98" width="24" height="24" class="block" />
      <line x1="228" y1="110" x2="270" y2="110" class="force" marker-end="url(#wf-a-coral)" />
      <text x="276" y="114" class="lab coral">40 N</text>
      <text x="276" y="132" class="note">panjang 15 cm</text>

      <path :d="zig(20, 236, 175, 10, 11)" class="coil" />
      <rect x="236" y="163" width="24" height="24" class="block" />
      <text x="276" y="180" class="note">panjang 18 cm</text>

      <rect x="200" y="206" width="36" height="12" class="area greenfill" />
      <line x1="140" y1="212" x2="260" y2="212" class="axis" />
      <line x1="140" y1="64" x2="140" y2="226" class="guide" />
      <line x1="200" y1="130" x2="200" y2="226" class="guide" />
      <line x1="236" y1="187" x2="236" y2="226" class="guide" />
      <text x="140" y="240" class="note" text-anchor="middle">x = 0</text>
      <text x="200" y="240" class="lab gold" text-anchor="middle">0,05</text>
      <text x="236" y="256" class="lab gold" text-anchor="middle">0,08</text>
      <text x="272" y="216" class="lab green">kerja yang dicari</text>
    </g>

    <!-- ============ cable ============ -->
    <g v-else-if="props.kind === 'cable'">
      <line x1="95" y1="20" x2="205" y2="20" class="wall" />
      <line x1="150" y1="20" x2="150" y2="258" class="cablel" />
      <rect x="143" y="116" width="14" height="24" class="slice" />
      <line x1="112" y1="20" x2="112" y2="116" class="dim" marker-start="url(#wf-a-gold)" marker-end="url(#wf-a-gold)" />
      <text x="104" y="72" class="lab gold" text-anchor="end">y</text>
      <line x1="112" y1="116" x2="143" y2="116" class="guide" />
      <path d="M162 116 H170 V140 H162" class="dim" />
      <text x="178" y="133" class="lab coral">Δy</text>
      <line x1="200" y1="112" x2="200" y2="26" class="force lift" marker-end="url(#wf-a-coral)" />
      <text v-if="props.reveal" x="208" y="70" class="note">naik sejauh y</text>
      <text v-if="props.reveal" x="170" y="162" class="note">berat ≈ 20 · Δy N</text>
      <text x="150" y="276" class="note" text-anchor="middle">panjang kabel 30 m</text>
    </g>

    <!-- ============ cone tank ============ -->
    <g v-else>
      <polygon points="35,30 215,30 125,150" class="water" />
      <polygon points="77,70 173,70 149,86 101,86" class="slice solid" />
      <line x1="35" y1="30" x2="215" y2="30" class="axis" />
      <text x="125" y="20" class="note" text-anchor="middle">bibir tangki</text>
      <line x1="20" y1="31" x2="20" y2="69" class="dim" marker-start="url(#wf-a-gold)" marker-end="url(#wf-a-gold)" />
      <text x="12" y="55" class="lab gold" text-anchor="end">y</text>
      <line x1="20" y1="70" x2="77" y2="70" class="guide" />
      <line x1="184" y1="70" x2="184" y2="86" class="dim" marker-start="url(#wf-a-gold)" marker-end="url(#wf-a-gold)" />
      <text x="192" y="83" class="lab coral">Δy</text>
      <line x1="125" y1="78" x2="173" y2="78" class="guide" />
      <text x="140" y="104" class="lab green">r</text>
      <text x="125" y="172" class="note" text-anchor="middle">lapisan setebal Δy pada kedalaman y</text>
      <text x="125" y="190" class="note" text-anchor="middle">jari-jari lapisan: r</text>
    </g>
  </svg>
</template>

<style>
.wf { width: 100%; display: block; font-family: inherit; }
.wf .wall { stroke: #64748b; stroke-width: 5; stroke-linecap: round; }
.wf .coil { fill: none; stroke: #94a3b8; stroke-width: 2.5; stroke-linejoin: round; }
.wf .block { fill: #1e293b; stroke: #94a3b8; stroke-width: 2; }
.wf .axis { stroke: #64748b; stroke-width: 1.8; fill: none; }
.wf .guide { stroke: #475569; stroke-width: 1.2; stroke-dasharray: 4 4; }
.wf .guide.coralline { stroke: #fb7185; opacity: 0.7; }
.wf .dim { stroke: #f5be3c; stroke-width: 1.8; fill: none; }
.wf .force { stroke: #fb7185; stroke-width: 2.6; fill: none; }
.wf .force.lift { stroke-dasharray: 5 4; }
.wf .curve { stroke: #50a5fa; stroke-width: 3; fill: none; }
.wf .leader { stroke: #f5be3c; stroke-width: 1.3; }
.wf .cablel { stroke: #94a3b8; stroke-width: 4; stroke-linecap: round; }
.wf .slice { fill: rgba(251, 113, 133, 0.55); stroke: #fb7185; stroke-width: 1.5; }
.wf .slice.solid { fill: rgba(251, 113, 133, 0.8); }
.wf .area { fill: rgba(245, 190, 60, 0.4); stroke: #f5be3c; stroke-width: 1.5; }
.wf .area.greenfill { fill: rgba(52, 211, 153, 0.45); stroke: #34d399; }
.wf .water { fill: rgba(80, 165, 250, 0.22); stroke: #50a5fa; stroke-width: 2.5; stroke-linejoin: round; }
.wf text { font-size: 13px; fill: #cbd5e1; }
.wf .note { font-size: 12px; fill: #94a3b8; }
.wf .lab { font-size: 15px; font-weight: 600; }
.wf .gold { fill: #f5be3c; }
.wf .coral { fill: #fb7185; }
.wf .blue { fill: #50a5fa; }
.wf .green { fill: #34d399; }
</style>
