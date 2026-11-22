<script setup lang="ts">
withDefaults(defineProps<{
  type?: 'block' | 'example' | 'alert'
  title?: string
}>(), {
  type: 'block',
  title: ''
})
</script>

<template>
  <div :class="`b-${type}`">
    <div v-if="title" class="b-block-title">{{ title }}</div>
    <div class="b-block-body">
      <slot />
    </div>
  </div>
</template>
