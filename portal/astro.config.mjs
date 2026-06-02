// @ts-check
import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';

// The portal is served from https://kirkmanamos.github.io/Precalculus_Slides/
// `base` MUST match the repo name so every internal link resolves correctly.
// https://astro.build/config
export default defineConfig({
  site: 'https://kirkmanamos.github.io',
  base: '/Precalculus_Slides',
  vite: {
    plugins: [tailwindcss()],
  },
  markdown: {
    // Lets you write $...$ / $$...$$ in any Markdown page and have it
    // rendered to HTML+CSS at build time (zero client JS).
    remarkPlugins: [remarkMath],
    rehypePlugins: [rehypeKatex],
  },
});
