<script setup lang="ts">
/**
 * PartitionStep — one labelled line of the "Partisi · Hampiri · Jumlahkan" pattern used to solve
 * applications of the definite integral (work, volume, area, ...).
 *
 *   n = 1  Partisi    cut the interval / object into thin pieces Δx (or Δy)
 *   n = 2  Hampiri    on ONE piece, approximate the quantity (ΔW ≈ F(x) Δx, ΔV ≈ A(x) Δx, ...)
 *   n = 3  Jumlahkan  add the pieces (Σ), then let the pieces get thinner: the sum becomes ∫
 *
 * Put the content in the default slot with blank lines around it so Markdown and KaTeX render:
 *
 *   <PartitionStep n="2">
 *
 *   $\Delta W \approx F(x)\,\Delta x$
 *
 *   </PartitionStep>
 *
 * `compact` drops the small caption under the label (for tight slides).
 */
import { computed } from 'vue'

const props = withDefaults(defineProps<{ n?: number | string; compact?: boolean }>(), { n: 1, compact: false })

const STEPS = [
  { name: 'Partisi', cap: 'potong', color: '#2dd4bf' },
  { name: 'Hampiri', cap: 'satu potongan', color: '#f5be3c' },
  { name: 'Jumlahkan', cap: 'Σ → ∫', color: '#fb7185' }
]
const step = computed(() => STEPS[Math.min(3, Math.max(1, Number(props.n))) - 1])
const num = computed(() => ['①', '②', '③'][Math.min(3, Math.max(1, Number(props.n))) - 1])
</script>

<template>
  <div class="pstep" :class="{ 'pstep-compact': props.compact }" :style="{ '--pc': step.color }">
    <div class="pstep-tag">
      <span class="pstep-name">{{ num }} {{ step.name }}</span>
      <span v-if="!props.compact" class="pstep-cap">{{ step.cap }}</span>
    </div>
    <div class="pstep-body"><slot /></div>
  </div>
</template>

<style>
.pstep {
  display: flex;
  align-items: flex-start;
  gap: 0.7rem;
  padding: 0.3rem 0 0.3rem 0.6rem;
  margin: 0.25rem 0;
  border-left: 3px solid var(--pc);
}
.pstep-tag {
  flex: 0 0 6.4rem;
  display: flex;
  flex-direction: column;
  gap: 0.1rem;
  padding-top: 0.15rem;
}
.pstep-compact .pstep-tag { flex-basis: 5.6rem; }
.pstep-name {
  color: var(--pc);
  font-weight: 700;
  font-size: 0.8rem;
  white-space: nowrap;
}
.pstep-cap {
  color: #64748b;
  font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
  font-size: 0.62rem;
  white-space: nowrap;
}
.pstep-body { flex: 1 1 auto; min-width: 0; }
.pstep-body > p:first-child { margin-top: 0; }
.pstep-body > p:last-child { margin-bottom: 0; }
.pstep-body .katex-display { margin: 0.25rem 0; }
</style>
