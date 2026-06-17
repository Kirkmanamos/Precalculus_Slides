#!/usr/bin/env python3
"""Stamp shared-asset URLs so browsers refetch slides-core.{css,js} when they change.

Every shared-engine deck links the same ``assets/slides-core.css`` and
``assets/slides-core.js``. Browsers cache those aggressively, so after you edit
a shared asset a deck can render against a stale copy (e.g. an unstyled Quick
Check). This script rewrites each deck's ``<link>``/``<script>`` reference to
``...slides-core.css|js?v=<hash>``, where ``<hash>`` is a short content hash of
the two shared files. Because the version is derived from the file contents:

  * it changes only when a shared asset actually changes, and
  * re-running with unchanged assets is a no-op (no spurious diffs).

Usage::

    python3 stamp_assets.py [DIR]      # DIR defaults to this script's folder

Run it after editing ``assets/slides-core.css`` or ``assets/slides-core.js``,
then commit the restamped decks. The deploy workflow also runs it on the
assembled site (``python3 stamp_assets.py _site``) as a safety net, so the live
site is always consistent even if a local run was forgotten.
"""
from __future__ import annotations

import glob
import hashlib
import os
import re
import sys

SHARED_ASSETS = ("assets/slides-core.css", "assets/slides-core.js")

# Matches a quoted href/src to a shared asset, plus any existing ?v=... query,
# so we replace both unstamped and previously-stamped references. Anchoring to
# the surrounding quote keeps us from stamping bare mentions in comments/prose.
PATTERN = re.compile(r'(["\'])(assets/slides-core\.(?:css|js))(?:\?v=[^"\']*)?\1')


def asset_version(root: str) -> str:
    h = hashlib.sha256()
    for name in SHARED_ASSETS:
        with open(os.path.join(root, name), "rb") as fh:
            h.update(fh.read())
    return h.hexdigest()[:8]


def stamp(root: str, version: str) -> list[str]:
    changed: list[str] = []
    for path in sorted(glob.glob(os.path.join(root, "*.html"))):
        with open(path, encoding="utf-8") as fh:
            html = fh.read()
        # Only touch decks built on the shared engine.
        if "assets/slides-core.js" not in html:
            continue
        new = PATTERN.sub(rf"\1\2?v={version}\1", html)
        if new != html:
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(new)
            changed.append(os.path.basename(path))
    return changed


def main() -> int:
    root = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.abspath(__file__))
    missing = [n for n in SHARED_ASSETS if not os.path.exists(os.path.join(root, n))]
    if missing:
        print(f"error: shared asset(s) not found under {root!r}: {', '.join(missing)}")
        return 1
    version = asset_version(root)
    changed = stamp(root, version)
    print(f"shared-asset version: {version}")
    print(f"stamped {len(changed)} deck(s)" + (":" if changed else " (all already current)"))
    for name in changed:
        print(f"  {name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
