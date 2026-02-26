<template>
  <button
    class="theme-toggle"
    type="button"
    :aria-label="`Switch to ${nextModeLabel} mode`"
    @click="toggleTheme"
  >
    <span class="theme-toggle__label">Theme</span>
    <span class="theme-toggle__value">{{ modeLabel }}</span>
  </button>
</template>

<script setup lang="ts">
import { computed, onMounted, onUnmounted, ref } from 'vue'

type ThemeMode = 'dark' | 'light'

const STORAGE_KEY = 'precalc-slidev-theme'
const mode = ref<ThemeMode>('dark')
let mediaQuery: MediaQueryList | null = null
let mediaListener: ((event: MediaQueryListEvent) => void) | null = null
let followsSystem = true

function applyTheme(next: ThemeMode, persist: boolean) {
  mode.value = next
  document.documentElement.dataset.precalcTheme = next
  if (persist) {
    localStorage.setItem(STORAGE_KEY, next)
    followsSystem = false
  }
}

function detectSystemTheme(): ThemeMode {
  return window.matchMedia('(prefers-color-scheme: light)').matches ? 'light' : 'dark'
}

function initializeTheme() {
  const saved = localStorage.getItem(STORAGE_KEY)
  if (saved === 'dark' || saved === 'light') {
    applyTheme(saved, false)
    followsSystem = false
  } else {
    applyTheme(detectSystemTheme(), false)
    followsSystem = true
  }

  mediaQuery = window.matchMedia('(prefers-color-scheme: light)')
  mediaListener = (event: MediaQueryListEvent) => {
    if (!followsSystem) return
    applyTheme(event.matches ? 'light' : 'dark', false)
  }
  mediaQuery.addEventListener?.('change', mediaListener)
}

function toggleTheme() {
  applyTheme(mode.value === 'dark' ? 'light' : 'dark', true)
}

const modeLabel = computed(() => (mode.value === 'dark' ? 'Dark' : 'Light'))
const nextModeLabel = computed(() => (mode.value === 'dark' ? 'light' : 'dark'))

onMounted(() => {
  initializeTheme()
})

onUnmounted(() => {
  if (mediaQuery && mediaListener) {
    mediaQuery.removeEventListener?.('change', mediaListener)
  }
})
</script>

