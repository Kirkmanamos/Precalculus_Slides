// Helpers for building links that respect the GitHub Pages base path
// (/Precalculus_Slides). BASE_URL always has a trailing slash in Astro.
const BASE = import.meta.env.BASE_URL.replace(/\/$/, '');

/** Build an internal URL, e.g. site('playgrounds/') or site('4.3-...html'). */
export function site(path = ''): string {
  const p = path.replace(/^\//, '');
  return p ? `${BASE}/${p}` : `${BASE}/`;
}

/** True for full external URLs (http/https). */
export function isExternal(href = ''): boolean {
  return /^https?:\/\//.test(href);
}
