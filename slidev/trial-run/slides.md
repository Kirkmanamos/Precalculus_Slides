---
theme: default
title: Slidev Trial Run
info: Minimal starter deck for testing Slidev in this repository.
class: text-center
drawings:
  persist: false
transition: slide-left
mdc: true
---

# Slidev Trial Run

Precalculus Slides Repo

Use this deck to validate the Slidev workflow before creating real lessons.

---
layout: two-cols
---

# What this tests

- Markdown-based slide authoring
- Speaker notes support
- Code blocks and layout helpers
- Fast iteration via local dev server

::right::

```js
const points = [-2, -1, 0, 1, 2]
const f = (x) => 2 * x + 3

console.table(points.map(x => ({ x, y: f(x) })))
```

---

# Math Check (Exact Values)

Special-angle values for a quick formatting test:

- `sin(30°) = 1/2`
- `cos(45°) = sqrt(2)/2`
- `tan(60°) = sqrt(3)`

---

# Next Steps

1. Install dependencies (`npm install`)
2. Run the preview (`npm run dev`)
3. Duplicate this folder for a real deck

<!--
Speaker note:
If Slidev opens correctly, we can create a themed precalculus prototype here next.
-->
