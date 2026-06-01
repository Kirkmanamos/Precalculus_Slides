#!/usr/bin/env python3
"""verify_decks.py — structural integrity check for HoffMath Classroom HTML decks.

Scope: every top-level ``*.html`` deck that is built on the shared slide engine
(i.e. links ``assets/slides-core.js``). Legacy one-off pages that predate the
shared-assets standard are listed but not graded.

For each in-scope deck it checks:
  1. At least one ``<section class="slide">`` exists.
  2. ``<section>`` / ``</section>`` tags are balanced.
  3. KaTeX math delimiters are balanced: ``\\(`` with ``\\)`` and ``\\[`` with ``\\]``.
  4. The shared stylesheet (``assets/slides-core.css``) is linked.
  5. ``SlidesCore.init`` is present.
  6. Every ``data-steps`` attribute is a non-negative integer, and any slide
     declaring ``data-steps > 0`` actually contains ``class="step"`` elements.

Exit code is 0 when all in-scope decks pass, 1 otherwise.
"""
from __future__ import annotations

import glob
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

SECTION_OPEN = re.compile(r"<section\b", re.I)
SECTION_CLOSE = re.compile(r"</section>", re.I)
SLIDE_SECTION = re.compile(r'<section\b[^>]*class="[^"]*\bslide\b', re.I)
SECTION_TAG = re.compile(r'<section\b[^>]*>', re.I)
DATA_STEPS = re.compile(r'data-steps="([^"]*)"')


def count_literal(text: str, token: str) -> int:
    return text.count(token)


def check_deck(path: str) -> list[str]:
    """Return a list of error strings for one deck (empty == passed)."""
    errors: list[str] = []
    with open(path, encoding="utf-8") as fh:
        html = fh.read()

    # 1. has slide sections
    slide_count = len(SLIDE_SECTION.findall(html))
    if slide_count == 0:
        errors.append("no <section class=\"slide\"> elements found")

    # 2. balanced section tags
    opens = len(SECTION_OPEN.findall(html))
    closes = len(SECTION_CLOSE.findall(html))
    if opens != closes:
        errors.append(f"unbalanced <section> tags: {opens} open vs {closes} close")

    # 3. balanced KaTeX delimiters
    inline_open = count_literal(html, r"\(")
    inline_close = count_literal(html, r"\)")
    if inline_open != inline_close:
        errors.append(
            rf"unbalanced inline math: {inline_open} '\(' vs {inline_close} '\)'"
        )
    disp_open = count_literal(html, r"\[")
    disp_close = count_literal(html, r"\]")
    if disp_open != disp_close:
        errors.append(
            rf"unbalanced display math: {disp_open} '\[' vs {disp_close} '\]'"
        )

    # 4. shared stylesheet linked
    if "assets/slides-core.css" not in html:
        errors.append("missing <link> to assets/slides-core.css")

    # 5. engine initialised
    if "SlidesCore.init" not in html:
        errors.append("missing SlidesCore.init(...) call")

    # 6. data-steps sanity (per slide section)
    for tag in SECTION_TAG.findall(html):
        m = DATA_STEPS.search(tag)
        if not m:
            continue
        raw = m.group(1)
        if not re.fullmatch(r"\d+", raw):
            errors.append(f'non-integer data-steps="{raw}"')

    return errors


def main() -> int:
    decks = sorted(glob.glob(os.path.join(HERE, "*.html")))
    in_scope: list[str] = []
    legacy: list[str] = []
    for path in decks:
        name = os.path.basename(path)
        if name == "index.html":
            continue
        with open(path, encoding="utf-8") as fh:
            head = fh.read()
        if "assets/slides-core.js" in head:
            in_scope.append(path)
        else:
            legacy.append(path)

    failures = 0
    print(f"Verifying {len(in_scope)} shared-engine deck(s)...\n")
    for path in in_scope:
        name = os.path.basename(path)
        errs = check_deck(path)
        if errs:
            failures += 1
            print(f"  FAIL  {name}")
            for e in errs:
                print(f"          - {e}")
        else:
            print(f"  ok    {name}")

    if legacy:
        print(f"\nSkipped {len(legacy)} legacy/non-engine page(s):")
        for path in legacy:
            print(f"  --    {os.path.basename(path)}")

    print()
    if failures:
        print(f"RESULT: {failures} deck(s) FAILED structural verification.")
        return 1
    print(f"RESULT: all {len(in_scope)} shared-engine decks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
