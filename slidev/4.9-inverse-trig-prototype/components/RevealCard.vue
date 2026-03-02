<template>
  <button
    class="reveal-card"
    :class="{ 'reveal-card--open': open }"
    type="button"
    :aria-expanded="String(open)"
    @click="open = !open"
  >
    <div class="reveal-card__prompt">
      <slot name="prompt" />
    </div>

    <div class="reveal-card__footer">
      <span class="reveal-card__cue" aria-hidden="true">
        {{ open ? '▲ hide' : '▼ tap to reveal' }}
      </span>
    </div>

    <Transition name="rc">
      <div v-if="open" class="reveal-card__answer">
        <slot name="answer" />
      </div>
    </Transition>
  </button>
</template>

<script setup lang="ts">
import { ref } from 'vue'
const open = ref(false)
</script>

<style scoped>
.reveal-card {
  display: block;
  width: 100%;
  padding: 0.9rem 1rem 0.75rem;
  text-align: left;
  cursor: pointer;
  border: 1px solid var(--deck-line);
  border-radius: 16px;
  background: var(--deck-bg-elevated);
  color: var(--deck-text-primary);
  font-family: var(--deck-font-body);
  transition: border-color 0.2s ease, background 0.2s ease;
}

.reveal-card:hover {
  border-color: color-mix(in srgb, var(--deck-accent) 40%, var(--deck-line));
  background: color-mix(in srgb, var(--deck-accent) 4%, var(--deck-bg-elevated));
}

.reveal-card--open {
  border-color: color-mix(in srgb, var(--deck-accent) 50%, var(--deck-line));
  background: color-mix(in srgb, var(--deck-accent) 7%, var(--deck-bg-elevated));
}

.reveal-card__prompt {
  font-weight: 600;
  font-size: 0.9rem;
  line-height: 1.4;
  color: var(--deck-text-primary);
}

.reveal-card__footer {
  margin-top: 0.4rem;
}

.reveal-card__cue {
  font-size: 0.68rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--deck-accent);
  font-weight: 700;
}

.reveal-card__answer {
  margin-top: 0.55rem;
  padding-top: 0.55rem;
  border-top: 1px solid var(--deck-line);
  color: var(--deck-text-muted);
  font-size: 0.86rem;
  line-height: 1.55;
}

/* Vue Transition */
.rc-enter-active {
  transition: opacity 0.22s ease, transform 0.22s ease;
}
.rc-leave-active {
  transition: opacity 0.14s ease;
}
.rc-enter-from {
  opacity: 0;
  transform: translateY(-5px);
}
.rc-leave-to {
  opacity: 0;
}

@media (prefers-reduced-motion: reduce) {
  .reveal-card,
  .rc-enter-active,
  .rc-leave-active {
    transition: none;
  }
}
</style>
