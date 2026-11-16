<script setup lang="ts">
/**
 * PolyaStepper — a one-line progress bar for problem-solving slides.
 *
 * step:    which of Pólya's four phases this slide covers: "1", "3", or a range "1-2".
 * support: how much of the work the slide does for the students
 *            full         worked example, lecturer models every phase
 *            partial      half-finished example, students fill the gaps
 *            independent  students solve; only a hint ladder is offered
 *
 * phases:  4 (default) shows all four phases; 3 drops "Periksa Lagi" for decks that leave it out.
 *
 * Put it directly under the slide title. It is ~28px tall.
 */
import { computed } from 'vue'

const props = withDefaults(defineProps<{
  step?: number | string
  support?: 'full' | 'partial' | 'independent'
  phases?: 3 | 4
}>(), {
  step: '1',
  support: 'full',
  phases: 4
})

const ALL_PHASES = ['Pahami Soal', 'Buat Rencana', 'Kerjakan', 'Periksa Lagi']
const PHASES = computed(() => ALL_PHASES.slice(0, props.phases === 3 ? 3 : 4))
const SUPPORT: Record<string, { label: string; dots: number }> = {
  full: { label: 'Dikerjakan bersama', dots: 3 },
  partial: { label: 'Lengkapi yang kosong', dots: 2 },
  independent: { label: 'Coba sendiri', dots: 1 }
}

const active = computed(() => {
  const parts = String(props.step).split('-').map(s => parseInt(s.trim(), 10)).filter(n => !isNaN(n))
  const lo = parts[0] ?? 1
  const hi = parts[1] ?? lo
  return [1, 2, 3, 4].map(n => n >= lo && n <= hi)
})
const sup = computed(() => SUPPORT[props.support] ?? SUPPORT.full)
</script>

<template>
  <div class="polya">
    <template v-for="(name, i) in PHASES" :key="name">
      <span class="polya-pill" :class="{ on: active[i] }">
        <span class="polya-n">{{ i + 1 }}</span>{{ name }}
      </span>
      <span v-if="i < PHASES.length - 1" class="polya-sep">›</span>
    </template>
    <span class="polya-support" :title="`Tingkat dukungan: ${sup.label}`">
      {{ sup.label }}
      <span class="polya-dots">
        <i v-for="d in 3" :key="d" :class="{ on: d <= sup.dots }" />
      </span>
    </span>
  </div>
</template>

<style>
.polya {
  display: flex;
  align-items: center;
  gap: 0.35rem;
  margin-bottom: 0.55rem;
  font-size: 0.7rem;
  line-height: 1;
}
.polya-pill {
  display: inline-flex;
  align-items: center;
  gap: 0.3rem;
  padding: 0.28rem 0.55rem;
  border-radius: 9999px;
  border: 1px solid #233148;
  color: #64748b;
  white-space: nowrap;
}
.polya-pill.on {
  border-color: #f5be3c;
  color: #f5be3c;
  background-color: rgba(245, 190, 60, 0.12);
  font-weight: 600;
}
.polya-n {
  font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
  opacity: 0.8;
}
.polya-sep { color: #334155; }
.polya-support {
  margin-left: auto;
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  color: #94a3b8;
  font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
  white-space: nowrap;
}
.polya-dots { display: inline-flex; gap: 0.18rem; }
.polya-dots i {
  width: 0.42rem;
  height: 0.42rem;
  border-radius: 9999px;
  background-color: #233148;
}
.polya-dots i.on { background-color: #2dd4bf; }
</style>
