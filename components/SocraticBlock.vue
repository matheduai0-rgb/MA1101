<script setup lang="ts">
/**
 * SocraticBlock — a callout for the questioning layer of a lecture slide.
 *
 * type:
 *   question  (gold)    a question the lecturer poses to the class
 *   predict   (violet)  students commit to a guess before an applet/result is shown
 *   hint      (cyan)    one rung of a hint ladder; pass `level` (1, 2, 3)
 *   answer    (emerald) the resolution of a question; always revealed by click
 *   pitfall   (coral)   a common wrong idea, posed for students to diagnose
 *   reflect   (blue)    look-back / exit-ticket prompt
 *
 * mode: optional chip telling the room how to respond, e.g. "Pikir 30 dtk",
 *       "Diskusi berpasangan · 1 mnt", "Angkat jari: A / B / C".
 *
 * Styles are self-contained so the block renders identically in every deck.
 * Leave a blank line before and after the slot content so Markdown + KaTeX parse.
 */
import { computed } from 'vue'

const props = withDefaults(defineProps<{
  type?: 'question' | 'predict' | 'hint' | 'answer' | 'pitfall' | 'reflect'
  title?: string
  level?: number | string
  mode?: string
}>(), {
  type: 'question',
  title: '',
  level: 0,
  mode: ''
})

const META: Record<string, { icon: string; label: string; color: string }> = {
  question: { icon: '?', label: 'Pertanyaan', color: '#f5be3c' },
  predict: { icon: '◔', label: 'Tebak Dulu', color: '#c4a7fa' },
  hint: { icon: '↗', label: 'Petunjuk', color: '#2dd4bf' },
  answer: { icon: '✓', label: 'Jawaban', color: '#34d399' },
  pitfall: { icon: '!', label: 'Benarkah?', color: '#fb7185' },
  reflect: { icon: '↺', label: 'Rangkum', color: '#50a5fa' }
}

const meta = computed(() => META[props.type] ?? META.question)
const heading = computed(() => {
  if (props.title) return props.title
  if (props.type === 'hint' && Number(props.level) > 0) return `${meta.value.label} ${props.level}`
  return meta.value.label
})
</script>

<template>
  <div class="sq" :class="`sq-${type}`" :style="{ '--sq': meta.color }">
    <div class="sq-head">
      <span class="sq-icon">{{ meta.icon }}</span>
      <span class="sq-title">{{ heading }}</span>
      <span v-if="mode" class="sq-mode">{{ mode }}</span>
    </div>
    <div class="sq-body">
      <slot />
    </div>
  </div>
</template>

<style>
.sq {
  background-color: #141b28;
  border: 1px solid color-mix(in srgb, var(--sq) 35%, #233148);
  border-left: 4px solid var(--sq);
  border-radius: 0.5rem;
  margin-bottom: 0.6rem;
  overflow: hidden;
}
.sq-head {
  display: flex;
  align-items: center;
  gap: 0.45rem;
  padding: 0.3rem 0.7rem;
  background-color: color-mix(in srgb, var(--sq) 12%, transparent);
  border-bottom: 1px solid color-mix(in srgb, var(--sq) 22%, transparent);
  color: var(--sq);
  font-size: 0.82rem;
  font-weight: 600;
}
.sq-icon {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 1.15rem;
  height: 1.15rem;
  border-radius: 9999px;
  border: 1.5px solid var(--sq);
  font-size: 0.72rem;
  font-weight: 700;
  line-height: 1;
  flex: none;
}
.sq-mode {
  margin-left: auto;
  font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
  font-size: 0.66rem;
  font-weight: 500;
  padding: 0.05rem 0.45rem;
  border-radius: 9999px;
  border: 1px solid color-mix(in srgb, var(--sq) 45%, transparent);
  white-space: nowrap;
}
.sq-body {
  padding: 0.45rem 0.7rem;
  font-size: 0.85rem;
  line-height: 1.45;
  color: #e2e8f0;
}
.sq-body > p:first-child { margin-top: 0; }
.sq-body > p:last-child { margin-bottom: 0; }
.sq-question .sq-body { font-size: 0.95rem; }
.slide-compact .sq-body { font-size: 0.8rem; line-height: 1.35; }
.slide-compact .sq-question .sq-body { font-size: 0.88rem; }
</style>
