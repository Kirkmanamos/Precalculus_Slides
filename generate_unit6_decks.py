from __future__ import annotations

from html import escape
from pathlib import Path
from textwrap import dedent


ROOT = Path(__file__).resolve().parent
UNIT_LABEL = "Unit 6 · Sequences, Series, and Probability"


def clean(text: str) -> str:
    return dedent(text).strip()


def join_blocks(*parts: str) -> str:
    return "\n".join(part for part in parts if part)


def card(title: str, body: str, tone: str = "") -> str:
    klass = "info-card" + (f" {tone}" if tone else "")
    return clean(
        f"""
        <div class="{klass}">
            <div class="card-title">{escape(title)}</div>
            <div class="card-copy">{body}</div>
        </div>
        """
    )


def note_box(title: str, body: str, tone: str = "orange") -> str:
    klass = "note-box" + (f" {tone}" if tone else "")
    return clean(
        f"""
        <div class="{klass}">
            <div class="note-title">{escape(title)}</div>
            <div class="note-copy">{body}</div>
        </div>
        """
    )


def cards_grid(*items: str, klass: str = "cards-grid") -> str:
    return f'<div class="{klass}">' + "".join(items) + "</div>"


def stack(*items: str) -> str:
    return f'<div class="stack">' + "".join(items) + "</div>"


def two_col(left: str, right: str) -> str:
    return clean(
        f"""
        <div class="two-col">
            <div class="col">{left}</div>
            <div class="col">{right}</div>
        </div>
        """
    )


def data_table(headers: list[str], rows: list[list[str]], klass: str = "data-table") -> str:
    head = "".join(f"<th>{cell}</th>" for cell in headers)
    body = []
    for row in rows:
        body.append("<tr>" + "".join(f"<td>{cell}</td>" for cell in row) + "</tr>")
    return clean(
        f"""
        <div class="table-shell">
            <table class="{klass}">
                <thead>
                    <tr>{head}</tr>
                </thead>
                <tbody>
                    {''.join(body)}
                </tbody>
            </table>
        </div>
        """
    )


def formula_grid(rows: list[tuple[str, list[str], str]], note: str = "") -> str:
    body = []
    for label, formulas, tone in rows:
        alt = "".join(f'<div class="fn-alt">{formula}</div>' for formula in formulas[1:])
        body.append(
            clean(
                f"""
                <div class="formula-row {tone}">
                    <div class="fn-label">{escape(label)}</div>
                    <div class="fn-eq-stack">
                        <div>{formulas[0]}</div>
                        {alt}
                    </div>
                </div>
                """
            )
        )
    note_html = f'<div class="formula-note">{note}</div>' if note else ""
    return clean(
        f"""
        <div class="formula-grid">
            {''.join(body)}
        </div>
        {note_html}
        """
    )


def summary_strip(items: list[tuple[str, str]], tone: str = "navy") -> str:
    blocks = []
    for label, value in items:
        blocks.append(
            clean(
                f"""
                <div class="summary-pill {tone}">
                    <div class="summary-label">{escape(label)}</div>
                    <div class="summary-value">{value}</div>
                </div>
                """
            )
        )
    return f'<div class="summary-strip">{"".join(blocks)}</div>'


def pascal_triangle() -> str:
    rows = [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
        [1, 4, 6, 4, 1],
        [1, 5, 10, 10, 5, 1],
    ]
    row_html = []
    for idx, values in enumerate(rows):
        cells = "".join(f'<span class="pascal-cell">{value}</span>' for value in values)
        row_html.append(
            f'<div class="pascal-row"><span class="pascal-index">n = {idx}</span><div class="pascal-values">{cells}</div></div>'
        )
    return clean(
        f"""
        <div class="diagram-shell">
            <div class="diagram-title">Pascal's Triangle</div>
            <div class="pascal-grid">
                {''.join(row_html)}
            </div>
            <div class="diagram-caption">Row <strong>n</strong> gives the coefficients of \\((a+b)^n\\).</div>
        </div>
        """
    )


def venn_diagram(
    left_label: str,
    right_label: str,
    left_only: str,
    overlap: str,
    right_only: str,
    outside: str,
    caption: str,
) -> str:
    return clean(
        f"""
        <div class="diagram-shell">
            <div class="diagram-title">Venn Diagram</div>
            <svg class="diagram" viewBox="0 0 360 220" role="img" aria-label="{escape(caption)}">
                <rect x="8" y="8" width="344" height="204" rx="18" fill="#f8fafc" stroke="#cbd5e1" />
                <circle cx="145" cy="108" r="66" fill="rgba(8,145,178,0.18)" stroke="#0891b2" stroke-width="3" />
                <circle cx="215" cy="108" r="66" fill="rgba(37,99,235,0.18)" stroke="#2563eb" stroke-width="3" />
                <text x="116" y="52" class="svg-label">{escape(left_label)}</text>
                <text x="227" y="52" class="svg-label">{escape(right_label)}</text>
                <text x="108" y="114" class="svg-count">{left_only}</text>
                <text x="176" y="114" class="svg-count">{overlap}</text>
                <text x="244" y="114" class="svg-count">{right_only}</text>
                <text x="28" y="188" class="svg-note">Outside: {outside}</text>
            </svg>
            <div class="diagram-caption">{caption}</div>
        </div>
        """
    )


def tree_diagram(
    title: str,
    branches: list[tuple[str, str, str, str, str, str, str, str]],
    caption: str,
) -> str:
    parts = []
    base_y = 58
    for idx, (
        top_label,
        top_prob,
        upper_label,
        upper_prob,
        lower_label,
        lower_prob,
        joint_top,
        joint_bottom,
    ) in enumerate(branches):
        y = base_y + idx * 74
        parts.append(
            clean(
                f"""
                <line x1="58" y1="110" x2="145" y2="{y}" class="svg-line" />
                <line x1="145" y1="{y}" x2="280" y2="{y - 22}" class="svg-line" />
                <line x1="145" y1="{y}" x2="280" y2="{y + 22}" class="svg-line" />
                <text x="92" y="{y - 8}" class="svg-prob">{top_prob}</text>
                <text x="154" y="{y - 8}" class="svg-label">{escape(top_label)}</text>
                <text x="208" y="{y - 30}" class="svg-prob">{upper_prob}</text>
                <text x="208" y="{y + 20}" class="svg-prob">{lower_prob}</text>
                <text x="287" y="{y - 18}" class="svg-label">{escape(upper_label)}</text>
                <text x="287" y="{y + 30}" class="svg-label">{escape(lower_label)}</text>
                <text x="214" y="{y - 40}" class="svg-joint">{joint_top}</text>
                <text x="214" y="{y + 42}" class="svg-joint">{joint_bottom}</text>
                """
            )
        )
    return clean(
        f"""
        <div class="diagram-shell">
            <div class="diagram-title">{escape(title)}</div>
            <svg class="diagram" viewBox="0 0 360 260" role="img" aria-label="{escape(caption)}">
                <text x="20" y="114" class="svg-label">Start</text>
                {''.join(parts)}
            </svg>
            <div class="diagram-caption">{caption}</div>
        </div>
        """
    )


def standard_slide(label_class: str, label: str, title: str, body: str) -> dict[str, object]:
    return {
        "type": "standard",
        "label_class": label_class,
        "label": label,
        "title": title,
        "body": body,
    }


def concept(title: str, body: str, label: str = "Concept") -> dict[str, object]:
    return standard_slide("concept-label", label, title, body)


def reference(title: str, body: str) -> dict[str, object]:
    return standard_slide("ref-label", "Reference", title, body)


def example(title: str, problem: str, steps: list[dict[str, str]], label: str) -> dict[str, object]:
    return {
        "type": "example",
        "label": label,
        "title": title,
        "problem": problem,
        "steps": steps,
    }


def step(label: str, body: str, color: str = "") -> dict[str, str]:
    return {"label": label, "body": body, "color": color}


COMMON_CSS = clean(
    r"""
    <style>
        :root {
            --navy: #1a365d;
            --blue-accent: #2563eb;
            --green-accent: #16a34a;
            --teal-accent: #0891b2;
            --orange-accent: #d97706;
            --red-accent: #dc2626;
            --grid-line: #dbeafe;
            --bg-white: #ffffff;
            --text: #1e293b;
            --text-muted: #64748b;
            --blue-light: #eff6ff;
            --green-light: #f0fdf4;
            --teal-light: #f0fdfa;
            --orange-light: #fffbeb;
            --navy-light: #e8edf5;
            --slate-line: #cbd5e1;
        }

        * { margin: 0; padding: 0; box-sizing: border-box; }

        html, body {
            width: 100%;
            height: 100%;
            min-height: 100dvh;
            overflow: hidden;
            font-family: 'Source Sans 3', sans-serif;
            font-size: 28px;
            background: var(--navy);
        }

        body {
            color: var(--text);
        }

        .slides-wrapper {
            width: 100vw;
            height: 100vh;
            height: 100dvh;
            position: relative;
            overflow: hidden;
        }

        .slide {
            position: absolute;
            inset: 0;
            display: flex;
            flex-direction: column;
            padding-top: 5rem;
            padding-bottom: 3rem;
            padding-left: max(3rem, calc((100% - 1120px) / 2));
            padding-right: max(3rem, calc((100% - 1120px) / 2));
            opacity: 0;
            transform: translateX(60px);
            transition: opacity 0.5s ease, transform 0.5s ease;
            pointer-events: none;
        }

        .slide.active {
            opacity: 1;
            transform: translateX(0);
            pointer-events: all;
        }

        .slide.exit-left {
            opacity: 0;
            transform: translateX(-60px);
        }

        .slide-body {
            flex: 1;
            display: flex;
            flex-direction: column;
            justify-content: center;
        }

        .slide-body.top-layout {
            justify-content: flex-start;
            gap: 0.85rem;
            overflow-y: auto;
            min-height: 0;
            padding-bottom: 3.5rem;
        }

        .slide-body:has(.steps-area) {
            justify-content: flex-start;
            overflow: hidden;
        }

        .title-slide {
            background: var(--navy);
            color: white;
            justify-content: center;
        }

        .grid-bg {
            background-color: var(--bg-white);
            background-image:
                linear-gradient(var(--grid-line) 1px, transparent 1px),
                linear-gradient(90deg, var(--grid-line) 1px, transparent 1px);
            background-size: 30px 30px;
        }

        .title-section-label {
            font-size: 0.62em;
            font-weight: 700;
            letter-spacing: 0.12em;
            text-transform: uppercase;
            color: #60a5fa;
            margin-bottom: 0.75rem;
        }

        .title-main {
            font-size: 2em;
            font-weight: 700;
            line-height: 1.16;
            color: white;
            margin-bottom: 0.55rem;
        }

        .title-objective {
            font-size: 0.72em;
            color: #bfdbfe;
            line-height: 1.6;
            margin-top: 0.75rem;
            max-width: 26rem;
        }

        .identity-chips {
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
            margin-top: 1.2rem;
            max-width: 32rem;
        }

        .chip {
            background: rgba(255,255,255,0.12);
            border: 1px solid rgba(255,255,255,0.18);
            border-radius: 999px;
            padding: 0.2em 0.75em;
            font-size: 0.58em;
            color: #e2e8f0;
        }

        .slide-header {
            display: flex;
            align-items: center;
            gap: 1rem;
            margin-bottom: 1.2rem;
            flex-shrink: 0;
        }

        .slide-title {
            font-size: 1em;
            font-weight: 700;
            color: var(--navy);
        }

        .example-label,
        .concept-label,
        .ref-label {
            font-size: 0.6em;
            font-weight: 700;
            padding: 0.2em 0.75em;
            border-radius: 6px;
            letter-spacing: 0.05em;
            text-transform: uppercase;
            color: white;
        }

        .example-label { background: var(--green-accent); }
        .concept-label { background: var(--teal-accent); }
        .ref-label { background: var(--navy); }

        .problem-statement {
            background: var(--navy-light);
            border-left: 5px solid var(--navy);
            border-radius: 10px;
            padding: 0.65em 1.2em;
            margin-bottom: 0.9rem;
            flex-shrink: 0;
            font-weight: 600;
            color: var(--navy);
            font-size: 0.9em;
        }

        .problem-statement .katex-display,
        .step-math .katex-display,
        .card-copy .katex-display,
        .fn-eq-stack .katex-display,
        .summary-value .katex-display,
        .diagram-caption .katex-display,
        .note-copy .katex-display {
            margin: 0.12em 0;
        }

        .body-lead {
            background: var(--navy-light);
            border-left: 4px solid var(--navy);
            border-radius: 10px;
            padding: 0.58em 0.95em;
            font-size: 0.78em;
            font-weight: 600;
            color: var(--navy);
            line-height: 1.5;
        }

        .stack {
            display: grid;
            gap: 0.75rem;
        }

        .two-col {
            display: grid;
            grid-template-columns: 1.15fr 0.95fr;
            gap: 0.85rem;
            align-items: start;
        }

        .col {
            min-width: 0;
        }

        .cards-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
            gap: 0.75rem;
        }

        .info-card,
        .diagram-shell,
        .table-shell,
        .note-box {
            background: rgba(255,255,255,0.94);
            border: 1px solid rgba(203,213,225,0.86);
            border-left: 4px solid var(--blue-accent);
            border-radius: 12px;
            padding: 0.72em 0.9em;
            box-shadow: 0 10px 24px rgba(15, 23, 42, 0.06);
        }

        .info-card.teal,
        .note-box.teal,
        .formula-row.teal {
            background: var(--teal-light);
            border-left-color: var(--teal-accent);
        }

        .info-card.green,
        .note-box.green,
        .formula-row.green {
            background: var(--green-light);
            border-left-color: var(--green-accent);
        }

        .info-card.orange,
        .note-box.orange,
        .formula-row.orange {
            background: var(--orange-light);
            border-left-color: var(--orange-accent);
        }

        .info-card.navy,
        .note-box.navy {
            background: var(--navy);
            border-left-color: #60a5fa;
            color: white;
        }

        .info-card.navy .card-title,
        .note-box.navy .note-title {
            color: #bfdbfe;
        }

        .card-title,
        .note-title,
        .diagram-title {
            font-size: 0.58em;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            color: var(--text-muted);
            margin-bottom: 0.28rem;
        }

        .card-copy,
        .note-copy,
        .diagram-caption {
            font-size: 0.78em;
            line-height: 1.5;
        }

        .formula-grid {
            display: grid;
            grid-template-columns: 1fr;
            gap: 0.7rem;
        }

        .formula-row {
            background: var(--blue-light);
            border-left: 5px solid var(--blue-accent);
            border-radius: 10px;
            padding: 0.5em 1em;
            display: flex;
            align-items: center;
            gap: 1rem;
        }

        .formula-row.blue {
            background: var(--blue-light);
            border-left-color: var(--blue-accent);
        }

        .fn-label {
            min-width: 4rem;
            font-size: 0.62em;
            font-weight: 700;
            letter-spacing: 0.05em;
            text-transform: uppercase;
            color: var(--text-muted);
            flex-shrink: 0;
        }

        .fn-eq-stack {
            display: flex;
            flex-direction: column;
            gap: 0.18rem;
            flex: 1;
            font-size: 0.82em;
        }

        .fn-alt {
            color: var(--text-muted);
        }

        .formula-note {
            margin-top: 0.75rem;
            font-size: 0.64em;
            font-weight: 600;
            color: var(--orange-accent);
            background: var(--orange-light);
            border-left: 4px solid var(--orange-accent);
            border-radius: 8px;
            padding: 0.55em 0.9em;
        }

        .table-shell {
            padding: 0.45em 0.55em;
        }

        .data-table {
            width: 100%;
            border-collapse: collapse;
            font-size: 0.72em;
            background: white;
            overflow: hidden;
            border-radius: 10px;
        }

        .data-table th,
        .data-table td {
            border: 1px solid #cbd5e1;
            padding: 0.48em 0.52em;
            text-align: center;
            vertical-align: middle;
        }

        .data-table th {
            background: var(--navy);
            color: white;
            font-weight: 700;
        }

        .data-table tr:nth-child(even) td {
            background: #f8fafc;
        }

        .steps-area {
            display: flex;
            flex-direction: column;
            overflow-y: auto;
            flex: 1;
            min-height: 0;
            padding-bottom: 3.5rem;
        }

        .step { display: none; }

        .step.visible {
            display: block;
            animation: stepReveal 0.4s ease both;
            margin-bottom: 0.45rem;
        }

        .step.visible:last-child {
            margin-bottom: 0;
        }

        @keyframes stepReveal {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .step-box {
            background: var(--blue-light);
            border-left: 4px solid var(--blue-accent);
            border-radius: 10px;
            padding: 0.46em 1em;
        }

        .step-box.teal {
            background: var(--teal-light);
            border-color: var(--teal-accent);
        }

        .step-box.green {
            background: var(--green-light);
            border-color: var(--green-accent);
        }

        .step-box.orange {
            background: var(--orange-light);
            border-color: var(--orange-accent);
        }

        .step-box.dark {
            background: var(--navy);
            border-color: #60a5fa;
            color: white;
        }

        .step-label {
            font-size: 0.58em;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            color: var(--text-muted);
            margin-bottom: 0.12rem;
        }

        .step-box.dark .step-label {
            color: #bfdbfe;
        }

        .step-math,
        .step-copy {
            font-size: 0.84em;
            line-height: 1.6;
            padding: 0.12em 0;
        }

        .step-math {
            text-align: center;
        }

        .step-copy ul,
        .card-copy ul,
        .note-copy ul {
            padding-left: 1.1rem;
        }

        .step-copy li,
        .card-copy li,
        .note-copy li {
            margin-bottom: 0.22rem;
        }

        .step-box.dark .step-math,
        .step-box.dark .step-copy,
        .step-box.dark .katex {
            color: white;
        }

        .step-math.has-annotation {
            display: flex;
            align-items: center;
            gap: 2rem;
            text-align: left;
        }

        .step-eq {
            flex: 1;
            text-align: center;
        }

        .annotation {
            flex: 0 0 34%;
            color: var(--blue-accent);
            font-size: 0.72em;
            font-weight: 600;
            line-height: 1.45;
            text-align: left;
            border-left: 3px solid #93c5fd;
            padding-left: 0.9rem;
        }

        .summary-strip {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(190px, 1fr));
            gap: 0.75rem;
        }

        .summary-pill {
            border-radius: 10px;
            padding: 0.52em 0.8em;
            background: var(--navy);
            color: white;
        }

        .summary-pill.green {
            background: #14532d;
        }

        .summary-label {
            font-size: 0.56em;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            color: #bfdbfe;
            margin-bottom: 0.12rem;
        }

        .summary-value {
            font-size: 0.82em;
            line-height: 1.45;
            text-align: center;
        }

        .diagram-shell {
            border-left-color: var(--teal-accent);
            background: white;
        }

        .diagram {
            width: 100%;
            height: auto;
            display: block;
        }

        .svg-line {
            stroke: #475569;
            stroke-width: 2.5;
            fill: none;
        }

        .svg-label {
            font: 600 16px 'Source Sans 3', sans-serif;
            fill: #0f172a;
        }

        .svg-count {
            font: 700 26px 'Source Sans 3', sans-serif;
            fill: #0f172a;
            text-anchor: middle;
        }

        .svg-note,
        .svg-prob,
        .svg-joint {
            font: 600 14px 'Source Sans 3', sans-serif;
            fill: #2563eb;
        }

        .pascal-grid {
            display: grid;
            gap: 0.36rem;
        }

        .pascal-row {
            display: grid;
            grid-template-columns: 3.5rem 1fr;
            gap: 0.5rem;
            align-items: center;
        }

        .pascal-index {
            font-size: 0.62em;
            font-weight: 700;
            color: var(--text-muted);
            text-transform: uppercase;
            letter-spacing: 0.06em;
        }

        .pascal-values {
            display: flex;
            flex-wrap: wrap;
            gap: 0.35rem;
        }

        .pascal-cell {
            min-width: 1.9rem;
            padding: 0.2rem 0.38rem;
            border-radius: 999px;
            background: var(--blue-light);
            border: 1px solid #bfdbfe;
            text-align: center;
            font-size: 0.72em;
            font-weight: 700;
            color: var(--navy);
        }

        .nav-dots {
            position: fixed;
            right: 1.2rem;
            top: 50%;
            transform: translateY(-50%);
            display: flex;
            flex-direction: column;
            gap: 8px;
            z-index: 100;
        }

        .nav-dot {
            width: 8px;
            height: 8px;
            border-radius: 50%;
            background: rgba(255,255,255,0.3);
            border: none;
            cursor: pointer;
            transition: all 0.3s;
        }

        .nav-dot.active {
            background: var(--blue-accent);
            transform: scale(1.4);
        }

        .progress-bar {
            position: fixed;
            top: 0;
            left: 0;
            height: 3px;
            background: linear-gradient(90deg, var(--blue-accent), var(--teal-accent));
            transition: width 0.4s ease;
            z-index: 100;
        }

        .click-hint {
            position: fixed;
            bottom: 1.5rem;
            left: 50%;
            transform: translateX(-50%);
            font-size: 0.45em;
            color: rgba(100,116,139,0.6);
            letter-spacing: 0.1em;
            text-transform: uppercase;
            animation: pulse 2s ease-in-out infinite;
            z-index: 100;
        }

        @keyframes pulse {
            0%, 100% { opacity: 0.4; }
            50% { opacity: 1; }
        }

        @media (prefers-reduced-motion: reduce) {
            .slide { transition: opacity 0.3s ease; transform: none !important; }
            .step.visible { animation: none; opacity: 1; }
        }

        @media (max-width: 1100px), (max-height: 900px) {
            html, body { font-size: 22px; }

            .slide {
                padding-top: max(2.4rem, calc(1.25rem + env(safe-area-inset-top)));
                padding-right: max(1.25rem, calc((100% - 960px) / 2));
                padding-bottom: calc(4.75rem + env(safe-area-inset-bottom));
                padding-left: max(1.25rem, calc((100% - 960px) / 2));
            }

            .slide-header {
                align-items: flex-start;
                flex-wrap: wrap;
                gap: 0.7rem;
                margin-bottom: 0.8rem;
            }

            .steps-area,
            .slide-body.top-layout {
                padding-bottom: calc(5.5rem + env(safe-area-inset-bottom));
            }
        }

        @media (max-width: 900px) {
            .two-col,
            .step-math.has-annotation {
                grid-template-columns: 1fr;
                flex-direction: column;
                align-items: stretch;
            }

            .annotation {
                flex: 0 1 auto;
                width: 100%;
                border-left: none;
                border-top: 3px solid #93c5fd;
                padding-left: 0;
                padding-top: 0.55rem;
            }
        }

        @media (max-width: 768px) {
            html, body {
                font-size: 18px !important;
                width: 100%;
                height: 100%;
                min-height: 100dvh;
            }

            .slide {
                padding-top: max(16px, env(safe-area-inset-top)) !important;
                padding-right: 12px !important;
                padding-bottom: calc(80px + env(safe-area-inset-bottom)) !important;
                padding-left: 12px !important;
                overflow-y: auto !important;
                -webkit-overflow-scrolling: touch;
            }

            .problem-statement {
                font-size: 0.95em !important;
                padding: 0.48em 0.66em !important;
                margin-bottom: 0.55rem !important;
            }

            .steps-area,
            .slide-body.top-layout {
                padding-bottom: calc(86px + env(safe-area-inset-bottom)) !important;
            }

            .example-label,
            .concept-label,
            .ref-label {
                font-size: 0.52em !important;
                padding: 0.22em 0.6em !important;
            }

            .click-hint {
                bottom: calc(10px + env(safe-area-inset-bottom)) !important;
                font-size: 0.5em !important;
                max-width: 92vw;
                text-align: center;
            }

            .nav-dots {
                display: none !important;
            }

            svg {
                max-width: 100%;
                height: auto;
            }
        }

        @media (max-width: 420px) {
            html, body { font-size: 16px !important; }
            .slide {
                padding-right: 10px !important;
                padding-left: 10px !important;
            }
        }
    </style>
    """
)


COMMON_JS = clean(
    r"""
    <script src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"></script>
    <script>
        renderMathInElement(document.body, {
            delimiters: [
                { left: '\\[', right: '\\]', display: true  },
                { left: '\\(', right: '\\)', display: false }
            ],
            throwOnError: false
        });

        document.querySelectorAll('.step-math').forEach(stepMath => {
            const annotation = stepMath.querySelector('.annotation');
            if (!annotation) return;
            const eqDiv = document.createElement('div');
            eqDiv.className = 'step-eq';
            const before = [];
            for (const node of stepMath.childNodes) {
                if (node === annotation) break;
                before.push(node);
            }
            before.forEach(node => eqDiv.appendChild(node));
            stepMath.insertBefore(eqDiv, annotation);
            stepMath.classList.add('has-annotation');
        });

        class SlidePresentation {
            constructor() {
                this.slides = Array.from(document.querySelectorAll('.slide'));
                this.current = 0;
                this.total = this.slides.length;
                this.progressBar = document.getElementById('progressBar');
                this.navDotsEl = document.getElementById('navDots');
                this.clickHint = document.getElementById('clickHint');
                this._buildNav();
                this._activate(0);
                this._bindEvents();
            }

            _buildNav() {
                this.slides.forEach((_, index) => {
                    const dot = document.createElement('button');
                    dot.className = 'nav-dot';
                    dot.setAttribute('aria-label', `Go to slide ${index + 1}`);
                    dot.addEventListener('click', event => {
                        event.stopPropagation();
                        this._goTo(index);
                    });
                    this.navDotsEl.appendChild(dot);
                });
                this.dots = Array.from(this.navDotsEl.querySelectorAll('.nav-dot'));
            }

            _sync() {
                this.dots.forEach((dot, index) => dot.classList.toggle('active', index === this.current));
                this.progressBar.style.width = ((this.current + 1) / this.total * 100) + '%';
                const slide = this.slides[this.current];
                const max = parseInt(slide.dataset.steps || 0, 10);
                const cur = parseInt(slide.dataset.currentStep ?? -1, 10);
                this.clickHint.textContent =
                    cur < max - 1 ? 'click to advance'
                    : this.current < this.total - 1 ? 'click for next slide'
                    : '';
            }

            _activate(index) {
                this.slides[index].classList.add('active');
                this._sync();
            }

            _goTo(index) {
                if (index === this.current) return;
                const out = this.slides[this.current];
                out.classList.add('exit-left');
                out.classList.remove('active');
                setTimeout(() => out.classList.remove('exit-left'), 500);
                this.current = index;
                this.slides[index].classList.add('active');
                this._sync();
            }

            _advanceStep(slide) {
                const max = parseInt(slide.dataset.steps || 0, 10);
                let cur = parseInt(slide.dataset.currentStep ?? -1, 10);
                if (cur < max - 1) {
                    cur++;
                    slide.dataset.currentStep = cur;
                    const step = slide.querySelector(`#${slide.id}-step-${cur}`);
                    if (step) {
                        step.classList.add('visible');
                        step.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
                    }
                    this._sync();
                    return true;
                }
                return false;
            }

            _retreatStep(slide) {
                let cur = parseInt(slide.dataset.currentStep ?? -1, 10);
                if (cur < 0) return false;
                slide.querySelector(`#${slide.id}-step-${cur}`)?.classList.remove('visible');
                slide.dataset.currentStep = cur - 1;
                this._sync();
                return true;
            }

            _next() {
                if (!this._advanceStep(this.slides[this.current]) && this.current < this.total - 1) {
                    this._goTo(this.current + 1);
                }
            }

            _prev() {
                if (!this._retreatStep(this.slides[this.current]) && this.current > 0) {
                    this._goTo(this.current - 1);
                }
            }

            _bindEvents() {
                document.addEventListener('keydown', event => {
                    if (['ArrowRight', 'ArrowDown', ' '].includes(event.key)) {
                        event.preventDefault();
                        this._next();
                    } else if (['ArrowLeft', 'ArrowUp'].includes(event.key)) {
                        event.preventDefault();
                        this._prev();
                    }
                });

                document.addEventListener('click', event => {
                    if (!event.target.closest('.nav-dot')) {
                        this._next();
                    }
                });

                let touchX = 0;
                document.addEventListener('touchstart', event => {
                    touchX = event.touches[0].clientX;
                }, { passive: true });

                document.addEventListener('touchend', event => {
                    const delta = event.changedTouches[0].clientX - touchX;
                    if (Math.abs(delta) > 50) {
                        delta < 0 ? this._next() : this._prev();
                    }
                }, { passive: true });
            }
        }

        new SlidePresentation();
    </script>
    """
)


def render_title_slide(deck: dict[str, object]) -> str:
    chips = "".join(f'<span class="chip">{escape(chip)}</span>' for chip in deck["chips"])
    return clean(
        f"""
        <section class="slide title-slide" id="slide-0">
            <div class="title-section-label">{escape(UNIT_LABEL)}</div>
            <div class="title-main">{escape(deck['section'])} {escape(deck['title'])}</div>
            <div class="title-objective">Objective: {escape(deck['objective'])}</div>
            <div class="identity-chips">{chips}</div>
        </section>
        """
    )


def render_standard_slide(slide_id: int, slide: dict[str, object]) -> str:
    return clean(
        f"""
        <section class="slide grid-bg" id="slide-{slide_id}">
            <div class="slide-header">
                <div class="{slide['label_class']}">{escape(str(slide['label']))}</div>
                <div class="slide-title">{escape(str(slide['title']))}</div>
            </div>
            <div class="slide-body top-layout">
                {slide['body']}
            </div>
        </section>
        """
    )


def render_example_slide(slide_id: int, slide: dict[str, object]) -> str:
    step_html = []
    for index, item in enumerate(slide["steps"]):
        color = f" {item['color']}" if item["color"] else ""
        step_html.append(
            clean(
                f"""
                <div class="step" id="slide-{slide_id}-step-{index}">
                    <div class="step-box{color}">
                        <div class="step-label">{escape(item['label'])}</div>
                        {item['body']}
                    </div>
                </div>
                """
            )
        )
    return clean(
        f"""
        <section class="slide grid-bg" id="slide-{slide_id}" data-steps="{len(slide['steps'])}">
            <div class="slide-header">
                <div class="example-label">{escape(str(slide['label']))}</div>
                <div class="slide-title">{escape(str(slide['title']))}</div>
            </div>
            <div class="slide-body">
                <div class="problem-statement">{slide['problem']}</div>
                <div class="steps-area">
                    {''.join(step_html)}
                </div>
            </div>
        </section>
        """
    )


def render_deck(deck: dict[str, object]) -> str:
    slides = [render_title_slide(deck)]
    for slide_id, slide in enumerate(deck["slides"], start=1):
        if slide["type"] == "example":
            slides.append(render_example_slide(slide_id, slide))
        else:
            slides.append(render_standard_slide(slide_id, slide))

    title = f"{deck['section']} - {deck['title']}"
    return "\n".join(
        [
            "<!DOCTYPE html>",
            "<html lang=\"en\">",
            "<head>",
            "    <meta charset=\"UTF-8\">",
            "    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">",
            f"    <title>{escape(title)}</title>",
            "    <link rel=\"stylesheet\" href=\"https://fonts.googleapis.com/css2?family=Source+Sans+3:wght@300;400;500;600;700&display=swap\">",
            "    <link rel=\"stylesheet\" href=\"https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css\">",
            COMMON_CSS,
            "</head>",
            "<body>",
            "<div class=\"progress-bar\" id=\"progressBar\"></div>",
            "<nav class=\"nav-dots\" id=\"navDots\" aria-label=\"Slide navigation\"></nav>",
            "<div class=\"click-hint\" id=\"clickHint\">click to advance</div>",
            "<div class=\"slides-wrapper\">",
            *slides,
            "</div>",
            COMMON_JS,
            "</body>",
            "</html>",
        ]
    )


def build_sequences_deck() -> dict[str, object]:
    notation_table = data_table(
        ["Position", "1", "2", "3", "4"],
        [["Term", "3", "7", "11", "15"], ["Notation", r"\(a_1\)", r"\(a_2\)", r"\(a_3\)", r"\(a_4\)"]],
    )
    slides = [
        concept(
            "What Is a Sequence?",
            join_blocks(
                '<div class="body-lead">A sequence is an ordered list. Each term has a position, so subscript notation lets us talk about where a value appears.</div>',
                two_col(
                    stack(
                        card("Definition", r"A sequence can be viewed as a function whose domain is the positive integers."),
                        card("Finite Sequence", r"A finite sequence stops after a fixed number of terms.", "teal"),
                        card("Infinite Sequence", r"An infinite sequence continues forever, so we show that with an ellipsis <strong>...</strong>.", "green"),
                    ),
                    stack(
                        note_box("Subscript Notation", r"The numbers are the <strong>terms</strong>, and the subscripts record their <strong>positions</strong>.", "navy"),
                        notation_table,
                    ),
                ),
            ),
        ),
        concept(
            "Infinite Sequences",
            join_blocks(
                '<div class="body-lead">The big question for an infinite sequence is whether the terms settle near one value.</div>',
                cards_grid(
                    card("Convergent", r"If the terms approach a single number, the sequence is <strong>convergent</strong>.", "green"),
                    card("Divergent", r"If the terms do not approach one value, the sequence is <strong>divergent</strong>.", "orange"),
                    card("Oscillation", r"Some divergent sequences bounce back and forth, such as \((-1)^n\).", "teal"),
                ),
                data_table(
                    ["Sequence", "Behavior", "Conclusion"],
                    [
                        [r"\(a_n = \dfrac{1}{n}\)", r"\(1,\dfrac12,\dfrac13,\dots\)", r"Converges to \(0\)"],
                        [r"\(a_n = n\)", r"\(1,2,3,4,\dots\)", r"Diverges to infinity"],
                        [r"\(a_n = (-1)^n\)", r"\(-1,1,-1,1,\dots\)", r"Diverges by oscillation"],
                    ],
                ),
            ),
        ),
        example(
            "Writing an Explicit Rule",
            r"Write an explicit formula for the sequence \(1, 3, 5, 7, \dots\).",
            [
                step(
                    "Organize Position and Term",
                    data_table(
                        [r"Position \(n\)", "1", "2", "3", "4"],
                        [[r"Term \(a_n\)", "1", "3", "5", "7"]],
                    ),
                    "teal",
                ),
                step(
                    "Look for the Pattern",
                    r"""
                    <div class="step-math">
                        \[\text{Each term is }1\text{ less than twice its position.}\]
                        <div class="annotation">\(2(1)-1 = 1,\ 2(2)-1 = 3,\ 2(3)-1 = 5\)</div>
                    </div>
                    """,
                ),
                step(
                    "Write the Explicit Rule",
                    r"""
                    <div class="step-math">
                        \[a_n = 2n - 1\]
                    </div>
                    """,
                    "dark",
                ),
            ],
            label="Example 1",
        ),
        example(
            "Recognizing a Quadratic Pattern",
            r"Write an explicit formula for the sequence \(2, 5, 10, 17, \dots\).",
            [
                step(
                    "Compare Terms to Familiar Values",
                    data_table(
                        [r"\(n\)", "1", "2", "3", "4"],
                        [[r"\(n^2\)", "1", "4", "9", "16"], [r"\(a_n\)", "2", "5", "10", "17"]],
                    ),
                    "teal",
                ),
                step(
                    "Describe the Pattern",
                    r"""
                    <div class="step-math">
                        \[\text{Each term is }1\text{ more than }n^2.\]
                        <div class="annotation">The second differences are constant, so a quadratic rule makes sense.</div>
                    </div>
                    """,
                ),
                step(
                    "Write the Explicit Rule",
                    r"""
                    <div class="step-math">
                        \[a_n = n^2 + 1\]
                    </div>
                    """,
                    "dark",
                ),
            ],
            label="Example 2",
        ),
        concept(
            "Recursive Rules and Factorial",
            join_blocks(
                '<div class="body-lead">Recursive rules tell you how to get the next term from the previous term. Factorial notation is a compact way to write long products of consecutive integers.</div>',
                cards_grid(
                    card(
                        "Recursive Example",
                        join_blocks(
                            r"<p>Suppose \(a_1 = 4\) and \(a_n = a_{n-1} + 3\).</p>",
                            r"<p>The first four terms are \(4, 7, 10, 13\).</p>",
                        ),
                        "teal",
                    ),
                    card(
                        "Factorial Definition",
                        join_blocks(
                            r"<p>\(n! = n(n-1)(n-2)\cdots 2\cdot 1\)</p>",
                            r"<p>By definition, \(0! = 1\).</p>",
                        ),
                        "green",
                    ),
                    card(
                        "Factorial Simplification",
                        r"\[\dfrac{7!}{5!} = \dfrac{7\cdot6\cdot5!}{5!} = 42\]",
                        "orange",
                    ),
                ),
            ),
        ),
        example(
            "Summation Notation and Partial Sums",
            r"Evaluate \(\displaystyle \sum_{n=1}^{4}(n^2+1)\).",
            [
                step(
                    "Identify the Summand",
                    join_blocks(
                        r'<div class="step-copy"><ul><li>The index is \(n\).</li><li>The lower limit is \(1\).</li><li>The upper limit is \(4\).</li><li>The summand is \(n^2+1\).</li></ul></div>'
                    ),
                    "teal",
                ),
                step(
                    "Write the First Four Terms",
                    r"""
                    <div class="step-math">
                        \[(1^2+1) + (2^2+1) + (3^2+1) + (4^2+1)\]
                        <div class="annotation">Substitute \(n=1,2,3,4\)</div>
                    </div>
                    """,
                ),
                step(
                    "Simplify and Add",
                    r"""
                    <div class="step-math">
                        \[2 + 5 + 10 + 17 = 34\]
                    </div>
                    """,
                ),
                step(
                    "Answer",
                    r"""
                    <div class="step-math">
                        \[\sum_{n=1}^{4}(n^2+1) = 34\]
                    </div>
                    """,
                    "dark",
                ),
            ],
            label="Example 3",
        ),
    ]
    return {
        "filename": "6.1-sequences.html",
        "section": "6.1",
        "title": "Sequences",
        "objective": "Define sequences, write explicit and recursive rules, and evaluate factorial and sigma notation.",
        "chips": ["subscript notation", "finite vs. infinite", "explicit rules", "recursive rules", "factorial and sigma notation"],
        "slides": slides,
    }


def build_arithmetic_deck() -> dict[str, object]:
    slides = [
        reference(
            "Arithmetic Sequence Formulas",
            formula_grid(
                [
                    ("difference", [r"\[d = a_n - a_{n-1}\]"], "teal"),
                    ("nth term", [r"\[a_n = a_1 + (n-1)d\]"], "blue"),
                    ("finite sum", [r"\[S_n = \dfrac{n}{2}(a_1 + a_n)\]", r"\[S_n = \dfrac{n}{2}\bigl(2a_1 + (n-1)d\bigr)\]"], "green"),
                ],
                note=r"Arithmetic sequences behave like linear functions: the common difference \(d\) acts like the slope.",
            ),
        ),
        example(
            "Finding an Explicit Formula",
            r"Find an explicit formula for the arithmetic sequence with first term \(66\) and common difference \(-11\).",
            [
                step("Use the nth-Term Formula", r'<div class="step-math">\[a_n = a_1 + (n-1)d\]</div>', "teal"),
                step(
                    "Substitute the Given Values",
                    r"""
                    <div class="step-math">
                        \[a_n = 66 + (n-1)(-11)\]
                    </div>
                    """,
                ),
                step(
                    "Simplify",
                    r"""
                    <div class="step-math">
                        \[a_n = 66 - 11n + 11 = 77 - 11n\]
                    </div>
                    """,
                ),
                step("Answer", r'<div class="step-math">\[a_n = 77 - 11n\]</div>', "dark"),
            ],
            label="Example 1",
        ),
        example(
            "Using Two Known Terms",
            r"The 4th term of an arithmetic sequence is \(24\) and the 13th term is \(87\). Write the first five terms.",
            [
                step(
                    "Find the Common Difference",
                    r"""
                    <div class="step-math">
                        \[d = \dfrac{87 - 24}{13 - 4} = \dfrac{63}{9} = 7\]
                        <div class="annotation">There are \(9\) equal jumps from term 4 to term 13.</div>
                    </div>
                    """,
                    "teal",
                ),
                step(
                    "Back Up to the First Term",
                    r"""
                    <div class="step-math">
                        \[a_1 = 24 - 3(7) = 3\]
                    </div>
                    """,
                ),
                step(
                    "List the First Five Terms",
                    r"""
                    <div class="step-math">
                        \[3,\ 10,\ 17,\ 24,\ 31\]
                    </div>
                    """,
                    "dark",
                ),
            ],
            label="Example 2",
        ),
        example(
            "Arithmetic Means",
            r"Insert three arithmetic means between \(21\) and \(45\).",
            [
                step(
                    "Count the Equal Jumps",
                    r"""
                    <div class="step-math">
                        \[21,\ \square,\ \square,\ \square,\ 45\]
                        <div class="annotation">Five terms create four equal jumps.</div>
                    </div>
                    """,
                    "teal",
                ),
                step(
                    "Compute the Common Difference",
                    r"""
                    <div class="step-math">
                        \[d = \dfrac{45 - 21}{4} = 6\]
                    </div>
                    """,
                ),
                step(
                    "Fill in the Means",
                    r"""
                    <div class="step-math">
                        \[21,\ 27,\ 33,\ 39,\ 45\]
                    </div>
                    """,
                    "dark",
                ),
            ],
            label="Example 3",
        ),
        concept(
            "Finite Arithmetic Series",
            join_blocks(
                '<div class="body-lead">A finite arithmetic series adds the terms of an arithmetic sequence. Pairing the first and last terms reveals a fast pattern.</div>',
                cards_grid(
                    card("Gauss Pairing", r"\[(1+100),\ (2+99),\ (3+98), \dots\]", "teal"),
                    card("Same Sum Every Time", r"Each pair adds to \(101\).", "green"),
                    card("How Many Pairs?", r"There are \(50\) pairs, so \(S_{100} = 50(101) = 5050\).", "orange"),
                ),
                note_box("Takeaway", r"If the first and last terms are easy to find, \(S_n = \dfrac{n}{2}(a_1+a_n)\) is the fastest formula.", "navy"),
            ),
        ),
        example(
            "Finding a Large Partial Sum",
            r"Find the 101st partial sum of the arithmetic sequence \(7, 9.5, 12, \dots\).",
            [
                step(
                    "Identify the Sequence Data",
                    r"""
                    <div class="step-copy">
                        <ul>
                            <li>\(a_1 = 7\)</li>
                            <li>\(d = 2.5\)</li>
                            <li>\(n = 101\)</li>
                        </ul>
                    </div>
                    """,
                    "teal",
                ),
                step(
                    "Find the 101st Term",
                    r"""
                    <div class="step-math">
                        \[a_{101} = 7 + 100(2.5) = 257\]
                    </div>
                    """,
                ),
                step(
                    "Use the Sum Formula",
                    r"""
                    <div class="step-math">
                        \[S_{101} = \dfrac{101}{2}(7 + 257) = \dfrac{101}{2}(264) = 13332\]
                    </div>
                    """,
                    "dark",
                ),
            ],
            label="Example 4",
        ),
        example(
            "Arithmetic-Series Application",
            r"A business sells \(\$20{,}000\) during its first year and increases sales by \(\$15{,}000\) each year for 19 more years. Find the total sales over the first 20 years.",
            [
                step(
                    "Model the Annual Sales",
                    r"""
                    <div class="step-copy">
                        <ul>
                            <li>\(a_1 = 20000\)</li>
                            <li>\(d = 15000\)</li>
                            <li>\(n = 20\)</li>
                        </ul>
                    </div>
                    """,
                    "teal",
                ),
                step(
                    "Find the 20th Year",
                    r"""
                    <div class="step-math">
                        \[a_{20} = 20000 + 19(15000) = 305000\]
                    </div>
                    """,
                ),
                step(
                    "Add the First 20 Terms",
                    r"""
                    <div class="step-math">
                        \[S_{20} = \dfrac{20}{2}(20000 + 305000) = 10(325000) = 3250000\]
                    </div>
                    """,
                ),
                step("Answer", r'<div class="step-math">\[\$3{,}250{,}000\]</div>', "dark"),
            ],
            label="Example 5",
        ),
    ]
    return {
        "filename": "6.2-arithmetic-sequences.html",
        "section": "6.2",
        "title": "Arithmetic Sequences",
        "objective": "Write nth-term formulas, find arithmetic means, and evaluate finite arithmetic series.",
        "chips": ["common difference", "nth term", "arithmetic means", "finite sums", "applications"],
        "slides": slides,
    }


def build_geometric_deck() -> dict[str, object]:
    slides = [
        reference(
            "Geometric Sequence Formulas",
            formula_grid(
                [
                    ("ratio", [r"\[r = \dfrac{a_n}{a_{n-1}}\]"], "teal"),
                    ("nth term", [r"\[a_n = a_1r^{\,n-1}\]"], "blue"),
                    ("finite sum", [r"\[S_n = \dfrac{a_1(1-r^n)}{1-r}, \quad r \ne 1\]"], "green"),
                    ("infinite sum", [r"\[S_{\infty} = \dfrac{a_1}{1-r}, \quad |r| < 1\]"], "orange"),
                ],
                note=r"The geometric mean between two positive numbers \(a\) and \(b\) is \(\sqrt{ab}\).",
            ),
        ),
        example(
            "Recognizing a Geometric Rule",
            r"Write an explicit formula for the sequence \(3, 6, 12, 24, \dots\).",
            [
                step(
                    "Find the Common Ratio",
                    r"""
                    <div class="step-math">
                        \[\dfrac{6}{3} = \dfrac{12}{6} = \dfrac{24}{12} = 2\]
                    </div>
                    """,
                    "teal",
                ),
                step(
                    "Use the nth-Term Formula",
                    r"""
                    <div class="step-math">
                        \[a_n = a_1r^{n-1} = 3(2)^{n-1}\]
                    </div>
                    """,
                ),
                step("Answer", r'<div class="step-math">\[a_n = 3\cdot 2^{n-1}\]</div>', "dark"),
            ],
            label="Example 1",
        ),
        example(
            "Growth by a Percent Ratio",
            r"Find the 15th term of the geometric sequence with \(a_1 = 20\) and \(r = 1.05\).",
            [
                step("Use the nth-Term Formula", r'<div class="step-math">\[a_{15} = 20(1.05)^{14}\]</div>', "teal"),
                step(
                    "Evaluate",
                    r"""
                    <div class="step-math">
                        \[a_{15} \approx 39.60\]
                    </div>
                    """,
                ),
                step("Answer", r'<div class="step-math">\[a_{15} \approx 39.60\]</div>', "dark"),
            ],
            label="Example 2",
        ),
        example(
            "Geometric Means",
            r"Find three geometric means between \(3.12\) and \(49.92\).",
            [
                step(
                    "Set Up the Five-Term Sequence",
                    r"""
                    <div class="step-math">
                        \[3.12,\ \square,\ \square,\ \square,\ 49.92\]
                        <div class="annotation">Five terms create four equal ratio jumps.</div>
                    </div>
                    """,
                    "teal",
                ),
                step(
                    "Solve for the Ratio",
                    r"""
                    <div class="step-math">
                        \[3.12r^4 = 49.92 \quad \Rightarrow \quad r^4 = 16 \quad \Rightarrow \quad r = 2\]
                    </div>
                    """,
                ),
                step(
                    "Fill in the Means",
                    r"""
                    <div class="step-math">
                        \[3.12,\ 6.24,\ 12.48,\ 24.96,\ 49.92\]
                    </div>
                    """,
                    "dark",
                ),
            ],
            label="Example 3",
        ),
        concept(
            "Finite and Infinite Geometric Sums",
            join_blocks(
                '<div class="body-lead">Multiplying a geometric sum by the common ratio makes almost every term line up, which is why the finite-sum formula works so cleanly.</div>',
                cards_grid(
                    card("Finite Sum", r"\[S_n = a_1 + a_1r + a_1r^2 + \dots + a_1r^{n-1}\]", "teal"),
                    card("Subtract the Shifted Copy", r"\[(1-r)S_n = a_1 - a_1r^n\]", "green"),
                    card("Infinite Sum", r"When \(|r|<1\), the term \(a_1r^n\) approaches \(0\), so the sum approaches a finite value.", "orange"),
                ),
            ),
        ),
        example(
            "Summing a Finite Geometric Series",
            r"Find the exact sum of the first 12 terms of \(8, 4, 2, \dots\).",
            [
                step(
                    "Identify the Data",
                    r"""
                    <div class="step-copy">
                        <ul>
                            <li>\(a_1 = 8\)</li>
                            <li>\(r = \dfrac{1}{2}\)</li>
                            <li>\(n = 12\)</li>
                        </ul>
                    </div>
                    """,
                    "teal",
                ),
                step(
                    "Use the Finite-Sum Formula",
                    r"""
                    <div class="step-math">
                        \[S_{12} = \dfrac{8\left(1-\left(\frac12\right)^{12}\right)}{1-\frac12}\]
                    </div>
                    """,
                ),
                step(
                    "Simplify Exactly",
                    r"""
                    <div class="step-math">
                        \[S_{12} = 16\left(1 - \dfrac{1}{4096}\right) = \dfrac{4095}{256}\]
                    </div>
                    """,
                    "dark",
                ),
            ],
            label="Example 4",
        ),
        example(
            "Solving for the Number of Terms",
            r"A geometric series has first term \(1\), common ratio \(3\), and finite sum \(29524\). Find \(n\).",
            [
                step(
                    "Write the Sum Formula",
                    r"""
                    <div class="step-math">
                        \[29524 = \dfrac{1(1-3^n)}{1-3} = \dfrac{3^n - 1}{2}\]
                    </div>
                    """,
                    "teal",
                ),
                step(
                    r"Solve for \(3^n\)",
                    r"""
                    <div class="step-math">
                        \[59048 = 3^n - 1 \quad \Rightarrow \quad 59049 = 3^n\]
                    </div>
                    """,
                ),
                step(
                    "Recognize the Power",
                    r"""
                    <div class="step-math">
                        \[59049 = 3^{10}\]
                    </div>
                    """,
                ),
                step("Answer", r'<div class="step-math">\[n = 10\]</div>', "dark"),
            ],
            label="Example 5",
        ),
        example(
            "Infinite Geometric Series",
            r"Find the sum of the infinite geometric series \(6 + 3 + 1.5 + 0.75 + \dots\).",
            [
                step(
                    "Check the Ratio",
                    r"""
                    <div class="step-math">
                        \[r = \dfrac{3}{6} = \dfrac12\]
                        <div class="annotation">\(|r| < 1\), so the infinite sum exists.</div>
                    </div>
                    """,
                    "teal",
                ),
                step(
                    "Use the Infinite-Sum Formula",
                    r"""
                    <div class="step-math">
                        \[S_{\infty} = \dfrac{a_1}{1-r} = \dfrac{6}{1-\frac12}\]
                    </div>
                    """,
                ),
                step("Answer", r'<div class="step-math">\[S_{\infty} = 12\]</div>', "dark"),
            ],
            label="Example 6",
        ),
    ]
    return {
        "filename": "6.3-geometric-sequences.html",
        "section": "6.3",
        "title": "Geometric Sequences",
        "objective": "Write geometric nth-term formulas, use geometric means, and evaluate finite and infinite geometric series.",
        "chips": ["common ratio", "nth term", "geometric mean", "finite sums", "infinite sums"],
        "slides": slides,
    }


def build_binomial_deck() -> dict[str, object]:
    slides = [
        concept(
            "Patterns in Binomial Expansions",
            join_blocks(
                r'<div class="body-lead">Before using a formula, it helps to notice what always happens in an expansion of \((a+b)^n\).</div>',
                cards_grid(
                    card("Number of Terms", r"There are always \(n+1\) terms.", "teal"),
                    card("Exponents", r"The exponent on the first factor decreases while the exponent on the second factor increases.", "green"),
                    card("Coefficients", r"The coefficients are symmetric and match Pascal's Triangle.", "orange"),
                ),
                note_box(
                    "Sample Pattern",
                    r"\[(a+b)^4 = a^4 + 4a^3b + 6a^2b^2 + 4ab^3 + b^4\]",
                    "navy",
                ),
            ),
        ),
        reference(
            "Pascal's Triangle and Combinations",
            join_blocks(
                pascal_triangle(),
                cards_grid(
                    card("Combination Formula", r"\[\binom{n}{r} = \dfrac{n!}{r!(n-r)!}\]", "teal"),
                    card("Calculator", r"On many calculators, use <strong>nCr</strong> to find \(\binom{n}{r}\).", "green"),
                    card("Row 4 Example", r"Row \(4\) gives \(1, 4, 6, 4, 1\), which are the coefficients of \((a+b)^4\).", "orange"),
                ),
            ),
        ),
        example(
            "Expanding with Pascal's Triangle",
            r"Use Pascal's Triangle to expand \((2x + y)^4\).",
            [
                step(
                    "Choose the Row of Coefficients",
                    r"""
                    <div class="step-math">
                        \[1,\ 4,\ 6,\ 4,\ 1\]
                        <div class="annotation">Row \(4\) matches the exponent \(4\).</div>
                    </div>
                    """,
                    "teal",
                ),
                step(
                    "Match the Power Pattern",
                    r"""
                    <div class="step-math">
                        \[(2x)^4,\ (2x)^3y,\ (2x)^2y^2,\ (2x)y^3,\ y^4\]
                    </div>
                    """,
                ),
                step(
                    "Multiply the Coefficients In",
                    r"""
                    <div class="step-math">
                        \[(2x+y)^4 = 16x^4 + 32x^3y + 24x^2y^2 + 8xy^3 + y^4\]
                    </div>
                    """,
                    "dark",
                ),
            ],
            label="Example 1",
        ),
        reference(
            "The Binomial Theorem",
            join_blocks(
                formula_grid(
                    [
                        ("theorem", [r"\[(a+b)^n = \sum_{r=0}^{n}\binom{n}{r}a^{\,n-r}b^r\]"], "blue"),
                        ("term", [r"\[T_{r+1} = \binom{n}{r}a^{\,n-r}b^r\]"], "teal"),
                    ],
                    note=r"The term number is always one more than \(r\), so the 6th term uses \(r=5\).",
                )
            ),
        ),
        example(
            "Expanding with the Binomial Theorem",
            r"Use the Binomial Theorem to expand \((x - 3)^5\).",
            [
                step(
                    r"Identify \(a\), \(b\), and \(n\)",
                    r"""
                    <div class="step-math">
                        \[a = x,\qquad b = -3,\qquad n = 5\]
                    </div>
                    """,
                    "teal",
                ),
                step(
                    "Apply the Theorem",
                    r"""
                    <div class="step-math">
                        \[(x-3)^5 = \sum_{r=0}^{5}\binom{5}{r}x^{5-r}(-3)^r\]
                    </div>
                    """,
                ),
                step(
                    "Simplify Each Term",
                    r"""
                    <div class="step-math">
                        \[(x-3)^5 = x^5 - 15x^4 + 90x^3 - 270x^2 + 405x - 243\]
                    </div>
                    """,
                    "dark",
                ),
            ],
            label="Example 2",
        ),
        example(
            "Finding a Specific Term",
            r"Find the 6th term of \((2x - y)^8\).",
            [
                step(
                    r"Match the Term Number to \(r\)",
                    r"""
                    <div class="step-math">
                        \[\text{6th term} \Rightarrow r = 5\]
                    </div>
                    """,
                    "teal",
                ),
                step(
                    "Use the General Term",
                    r"""
                    <div class="step-math">
                        \[T_6 = \binom{8}{5}(2x)^{8-5}(-y)^5\]
                    </div>
                    """,
                ),
                step(
                    "Simplify",
                    r"""
                    <div class="step-math">
                        \[T_6 = 56(2x)^3(-y)^5 = 56(8x^3)(-y^5) = -448x^3y^5\]
                    </div>
                    """,
                    "dark",
                ),
            ],
            label="Example 3",
        ),
        example(
            "Finding a Coefficient",
            r"Find the coefficient of \(x^2\) in the expansion of \((2x + 3)^5\).",
            [
                step(
                    r"Identify Which Power of \(3\) You Need",
                    r"""
                    <div class="step-math">
                        \[x^2 \text{ means } 5-r = 2 \Rightarrow r = 3\]
                    </div>
                    """,
                    "teal",
                ),
                step(
                    "Use the Matching Term",
                    r"""
                    <div class="step-math">
                        \[\binom{5}{3}(2x)^2(3)^3 = 10 \cdot 4x^2 \cdot 27\]
                    </div>
                    """,
                ),
                step("Answer", r'<div class="step-math">\[\text{Coefficient of }x^2 = 1080\]</div>', "dark"),
            ],
            label="Example 4",
        ),
    ]
    return {
        "filename": "6.4-binomial-theorem.html",
        "section": "6.4",
        "title": "The Binomial Theorem",
        "objective": "Use Pascal's Triangle, combinations, and the Binomial Theorem to expand expressions and find specific terms.",
        "chips": ["Pascal's Triangle", "binomial coefficients", "full expansions", "specific terms", "coefficients"],
        "slides": slides,
    }


def build_counting_deck() -> dict[str, object]:
    slides = [
        concept(
            "The Fundamental Counting Principle",
            join_blocks(
                r'<div class="body-lead">If one choice can happen in \(m\) ways and the next choice can happen in \(n\) ways, then the two-step process can happen in \(mn\) ways.</div>',
                two_col(
                    stack(
                        card("Sandwich Choices", r"Bill chooses one of \(4\) meats and one of \(3\) breads.", "teal"),
                        card("Multiply the Choices", r"\[4 \cdot 3 = 12\text{ sandwiches}\]", "green"),
                    ),
                    stack(
                        note_box("General Rule", r"\[\text{Total outcomes} = (\text{ways for step 1})(\text{ways for step 2})\]", "navy"),
                        card("When to Use It", r"Use the counting principle when a problem is built from sequential decisions.", "orange"),
                    ),
                ),
            ),
        ),
        concept(
            "Quick Counting-Principle Examples",
            join_blocks(
                cards_grid(
                    card(
                        "Airport Codes",
                        r"""
                        <p>Three-letter airport codes allow repetition.</p>
                        \[26 \cdot 26 \cdot 26 = 17576\]
                        """,
                        "teal",
                    ),
                    card(
                        "Phone Numbers",
                        r"""
                        <p>The first digit cannot be \(0\) or \(1\), so it has \(8\) choices.</p>
                        \[8 \cdot 10^6 = 8000000\]
                        """,
                        "green",
                    ),
                )
            ),
        ),
        reference(
            "Permutations",
            join_blocks(
                formula_grid(
                    [
                        ("meaning", [r"\[\text{Order matters}\]"], "teal"),
                        ("formula", [r"\[{}_nP_r = \dfrac{n!}{(n-r)!}\]"], "blue"),
                    ],
                    note=r"A permutation is an arrangement in a specific order, so changing the order creates a different outcome.",
                ),
                cards_grid(
                    card("Ribbon Example", r"Awarding blue, red, white, and yellow ribbons to four students gives \(4! = 24\) possible orders.", "orange"),
                ),
            ),
        ),
        example(
            "Ranking Horses in a Race",
            r"Eight horses are running in a race. In how many ways can the horses finish 1st, 2nd, and 3rd?",
            [
                step(
                    "Order Matters",
                    r"""
                    <div class="step-copy">
                        <ul>
                            <li>1st place is different from 2nd place.</li>
                            <li>2nd place is different from 3rd place.</li>
                        </ul>
                    </div>
                    """,
                    "teal",
                ),
                step(
                    "Use a Permutation",
                    r"""
                    <div class="step-math">
                        \[{}_8P_3 = 8 \cdot 7 \cdot 6 = 336\]
                    </div>
                    """,
                ),
                step(
                    "If All Eight Are Ranked",
                    r"""
                    <div class="step-math">
                        \[{}_8P_8 = 8! = 40320\]
                    </div>
                    """,
                    "green",
                ),
                step("Answer", r'<div class="step-math">\[\text{Top three finishes: }336\]</div>', "dark"),
            ],
            label="Example 1",
        ),
        reference(
            "Combinations",
            join_blocks(
                formula_grid(
                    [
                        ("meaning", [r"\[\text{Order does not matter}\]"], "teal"),
                        ("formula", [r"\[\binom{n}{r} = \dfrac{n!}{r!(n-r)!}\]"], "blue"),
                    ],
                    note=r"Use combinations when you are selecting a group, not arranging a lineup.",
                ),
                cards_grid(
                    card("Combination Examples", r"Committees, pizza toppings, and lottery numbers are all combination situations.", "green"),
                    card("Permutation Examples", r"Lineups, shelf order, and race results are permutation situations.", "orange"),
                ),
            ),
        ),
        concept(
            "Combination Examples",
            join_blocks(
                cards_grid(
                    card(
                        "Pizza Special",
                        r"""
                        <p>Choose \(4\) toppings from \(12\).</p>
                        \[\binom{12}{4} = 495\]
                        """,
                        "teal",
                    ),
                    card(
                        "Packing T-Shirts",
                        r"""
                        <p>Choose \(5\) shirts from \(16\).</p>
                        \[\binom{16}{5} = 4368\]
                        """,
                        "green",
                    ),
                )
            ),
        ),
        example(
            "Committee Counting",
            r"A committee of \(6\) people will be formed from \(7\) students and \(5\) teachers. Find the number of committees if (a) any \(6\) people may be chosen and (b) exactly four members must be students.",
            [
                step(
                    "Part (a): Any Six People",
                    r"""
                    <div class="step-math">
                        \[\binom{12}{6} = 924\]
                    </div>
                    """,
                    "teal",
                ),
                step(
                    "Part (b): Split the Choice by Group",
                    r"""
                    <div class="step-math">
                        \[\binom{7}{4}\binom{5}{2}\]
                        <div class="annotation">Choose \(4\) students and \(2\) teachers.</div>
                    </div>
                    """,
                ),
                step(
                    "Multiply the Independent Choices",
                    r"""
                    <div class="step-math">
                        \[\binom{7}{4}\binom{5}{2} = 35 \cdot 10 = 350\]
                    </div>
                    """,
                    "dark",
                ),
            ],
            label="Example 2",
        ),
        example(
            "Non-Distinct Permutations",
            r"How many distinguishable arrangements of the letters in <strong>TATTOOS</strong> are possible?",
            [
                step(
                    "Count the Repeated Letters",
                    r"""
                    <div class="step-copy">
                        <ul>
                            <li>Total letters: \(7\)</li>
                            <li>\(T\) appears \(3\) times.</li>
                            <li>\(O\) appears \(2\) times.</li>
                        </ul>
                    </div>
                    """,
                    "teal",
                ),
                step(
                    r"Start with \(7!\) and Divide Out the Repeats",
                    r"""
                    <div class="step-math">
                        \[\dfrac{7!}{3!\,2!}\]
                    </div>
                    """,
                ),
                step(
                    "Simplify",
                    r"""
                    <div class="step-math">
                        \[\dfrac{5040}{12} = 420\]
                    </div>
                    """,
                    "dark",
                ),
            ],
            label="Example 3",
        ),
    ]
    return {
        "filename": "6.5-counting-principles.html",
        "section": "6.5",
        "title": "Counting Principles",
        "objective": "Use the counting principle, permutations, combinations, and non-distinct permutations to count outcomes efficiently.",
        "chips": ["counting principle", "permutations", "combinations", "order matters", "non-distinct objects"],
        "slides": slides,
    }


def build_probability_deck() -> dict[str, object]:
    chemistry_venn = venn_diagram(
        "Chemistry",
        "History",
        "5",
        "15",
        "4",
        "3",
        "Five students take only Chemistry, fifteen take both, four take only History, and three take neither.",
    )
    slides = [
        concept(
            "Probability Vocabulary",
            join_blocks(
                '<div class="body-lead">Probability starts with clear language: experiment, sample space, and event.</div>',
                cards_grid(
                    card("Experiment", r"An experiment is any process that leads to a well-defined outcome, such as rolling a die or drawing a card.", "teal"),
                    card("Sample Space", r"The sample space \(S\) is the set of all possible outcomes.", "green"),
                    card("Event", r"An event \(E\) is any subset of the sample space.", "orange"),
                ),
                data_table(
                    ["Situation", "Sample Space"],
                    [
                        ["Rolling a six-sided die", r"\(\{1,2,3,4,5,6\}\)"],
                        ["Flipping two coins", r"\(\{HH, HT, TH, TT\}\)"],
                    ],
                ),
            ),
        ),
        concept(
            "Basic Probability and Experimental Probability",
            join_blocks(
                cards_grid(
                    card("Probability Forms", r"Probabilities can be written as fractions, decimals, or percents.", "teal"),
                    card("Impossible vs. Certain", r"If \(P(E)=0\), the event is impossible. If \(P(E)=1\), the event is certain.", "green"),
                    card("Theoretical vs. Experimental", r"Theoretical probability is based on reasoning. Experimental probability is based on actual trials.", "orange"),
                ),
                note_box(
                    "Example",
                    r"A fair die has theoretical probability \(\dfrac{1}{6}\) of landing on \(3\). If a coin lands heads \(47\) times in \(100\) flips, the experimental probability is \(\dfrac{47}{100}\).",
                    "navy",
                ),
            ),
        ),
        reference(
            "Addition Rule",
            formula_grid(
                [
                    ("mutually exclusive", [r"\[P(A \text{ or } B) = P(A) + P(B)\]"], "teal"),
                    ("inclusive", [r"\[P(A \text{ or } B) = P(A) + P(B) - P(A \text{ and } B)\]"], "blue"),
                ],
                note=r"The addition rule finds the probability that at least one of the events occurs.",
            ),
        ),
        concept(
            "Addition Rule Examples",
            join_blocks(
                cards_grid(
                    card(
                        "Mutually Exclusive",
                        r"""
                        <p>In a class of \(30\) students, \(18\) were born in the United States and \(3\) were born in India.</p>
                        \[P(\text{U.S. or India}) = \dfrac{18+3}{30} = \dfrac{7}{10}\]
                        """,
                        "teal",
                    ),
                    card(
                        "Inclusive",
                        join_blocks(
                            chemistry_venn,
                            r"<p>\[P(\text{Chemistry or History}) = \dfrac{20+19-15}{27} = \dfrac{24}{27} = \dfrac{8}{9}\]</p>",
                        ),
                        "green",
                    ),
                )
            ),
        ),
        reference(
            "Multiplication Rule",
            formula_grid(
                [
                    ("independent", [r"\[P(A \text{ and } B) = P(A)P(B)\]"], "teal"),
                    ("dependent", [r"\[P(A \text{ and } B) = P(A)P(B\mid A)\]"], "blue"),
                ],
                note=r"The multiplication rule finds the probability that multiple events all occur.",
            ),
        ),
        example(
            "Independent vs. Dependent Events",
            r"There are \(9\) brown boxes and \(6\) blue boxes on a shelf. Find the probability that Ana and Sebastian both choose brown if (a) Ana replaces her box and (b) Ana keeps her box.",
            [
                step(
                    "With Replacement",
                    r"""
                    <div class="step-math">
                        \[P(\text{both brown}) = \dfrac{9}{15}\cdot\dfrac{9}{15} = \dfrac{9}{25}\]
                    </div>
                    """,
                    "teal",
                ),
                step(
                    "Without Replacement",
                    r"""
                    <div class="step-math">
                        \[P(\text{both brown}) = \dfrac{9}{15}\cdot\dfrac{8}{14} = \dfrac{12}{35}\]
                    </div>
                    """,
                ),
                step(
                    "Why the Answers Differ",
                    r"""
                    <div class="step-copy">
                        <ul>
                            <li>Replacing keeps the second draw independent.</li>
                            <li>Not replacing changes the sample space for the second draw.</li>
                        </ul>
                    </div>
                    """,
                    "green",
                ),
            ],
            label="Example 1",
        ),
        concept(
            "Probability with Permutations and Combinations",
            join_blocks(
                cards_grid(
                    card(
                        "Exactly 2 Red Marbles",
                        r"""
                        <p>From \(8\) red and \(6\) blue marbles, choose \(4\).</p>
                        \[\dfrac{\binom{8}{2}\binom{6}{2}}{\binom{14}{4}} = \dfrac{60}{143}\]
                        """,
                        "teal",
                    ),
                    card(
                        "No Repeated Digits in a 4-Digit PIN",
                        r"""
                        <p>Any of the \(10\) digits may appear in each spot.</p>
                        \[\dfrac{{}_{10}P_4}{10^4} = \dfrac{10\cdot9\cdot8\cdot7}{10000} = \dfrac{63}{125}\]
                        """,
                        "green",
                    ),
                    card(
                        "Odd First Digit",
                        r"""
                        <p>A 4-digit PIN uses digits \(1\)-\(9\) without repetition.</p>
                        \[\dfrac{5\cdot8\cdot7\cdot6}{{}_9P_4} = \dfrac{5}{9}\]
                        """,
                        "orange",
                    ),
                )
            ),
        ),
        reference(
            "Complement Rule",
            join_blocks(
                formula_grid(
                    [("complement", [r"\[P(E') = 1 - P(E)\]"], "orange")],
                    note=r"When a problem asks for <em>at least one</em>, it is often easier to find the probability of <em>none</em> and subtract from \(1\).",
                ),
                cards_grid(
                    card(
                        "At Least One Yellow",
                        r"""
                        <p>A jar has \(8\) blue and \(4\) yellow marbles. Choose \(3\).</p>
                        \[1 - \dfrac{\binom{8}{3}}{\binom{12}{3}} = 1 - \dfrac{56}{220} = \dfrac{41}{55}\]
                        """,
                        "teal",
                    ),
                    card(
                        "Two Dice, Sum Greater Than 3",
                        r"""
                        <p>The complement is sum \(\le 3\): \((1,1), (1,2), (2,1)\).</p>
                        \[1 - \dfrac{3}{36} = \dfrac{11}{12}\]
                        """,
                        "green",
                    ),
                ),
            ),
        ),
    ]
    return {
        "filename": "6.6-probability.html",
        "section": "6.6",
        "title": "Probability",
        "objective": "Classify events, use the addition and multiplication rules, and solve counting-based probability problems.",
        "chips": ["sample space", "addition rule", "multiplication rule", "counting-based probability", "complements"],
        "slides": slides,
    }


def build_conditional_probability_deck() -> dict[str, object]:
    transport_table = data_table(
        ["", "9th", "10th", "11th", "12th", "Total"],
        [
            ["Walk/Bike", "26", "19", "14", "11", "70"],
            ["Car", "14", "26", "39", "45", "124"],
            ["Bus", "36", "31", "26", "13", "106"],
            ["Total", "76", "76", "79", "69", "300"],
        ],
    )
    ride_table = data_table(
        ["", "Child", "Adult", "Total"],
        [
            ["Liked", "51", "26", "77"],
            ["Disliked", "22", "31", "53"],
            ["Total", "73", "57", "130"],
        ],
    )
    emma_tree = tree_diagram(
        "Emma's Study Tree",
        [
            ("Bedroom", "0.4", "Math", "0.7", "English", "0.3", "Joint: 0.28", "Joint: 0.12"),
            ("Library", "0.6", "Math", "0.5", "English", "0.5", "Joint: 0.30", "Joint: 0.30"),
        ],
        "Emma studies in her bedroom 40 percent of the time and at the library 60 percent of the time. We compare the joint probabilities that end in Math.",
    )
    basket_tree = tree_diagram(
        "Basket Selection Tree",
        [
            ("Basket A", "4/6", "Red", "3/5", "White", "2/5", "Joint: 2/5", "Joint: 4/15"),
            ("Basket B", "2/6", "Red", "4/5", "White", "1/5", "Joint: 4/15", "Joint: 1/15"),
        ],
        "A weighted die chooses Basket A or Basket B before a ticket is drawn.",
    )
    slides = [
        reference(
            "Conditional Probability",
            join_blocks(
                formula_grid(
                    [
                        ("definition", [r"\[P(A\mid B) = \dfrac{P(A \cap B)}{P(B)}\]"], "teal"),
                        ("reading", [r"\[\text{Read }P(A\mid B)\text{ as 'the probability of }A\text{ given }B'}\]"], "blue"),
                    ],
                    note=r"The denominator changes because once \(B\) is known, the sample space shrinks to only the outcomes in \(B\).",
                ),
                cards_grid(
                    card("Backward Probability", r"Conditional probability answers questions like: <em>If we know something already happened, how does that change the chance of another event?</em>", "green"),
                    card("Intersection First", r"Find the overlap for the numerator, then divide by the restricted total.", "orange"),
                ),
            ),
        ),
        example(
            "Conditional Probability from a Two-Way Table",
            r"A survey of \(300\) students recorded transportation and grade level. Find (a) the probability that a student is a 12th grader who drives a car and (b) the probability that a student rides the bus, given that the student is in 9th grade.",
            [
                step("Read the Table", transport_table, "teal"),
                step(
                    "Joint Probability",
                    r"""
                    <div class="step-math">
                        \[P(\text{12th and Car}) = \dfrac{45}{300} = \dfrac{3}{20}\]
                    </div>
                    """,
                ),
                step(
                    "Conditional Probability",
                    r"""
                    <div class="step-math">
                        \[P(\text{Bus}\mid \text{9th}) = \dfrac{36}{76} = \dfrac{9}{19}\]
                    </div>
                    """,
                    "dark",
                ),
            ],
            label="Example 1",
        ),
        example(
            "Theme Park Survey",
            r"People exiting a new ride were asked whether they liked or disliked the ride. Find the probability that a randomly selected rider is an adult given that the rider disliked the ride.",
            [
                step("Organize the Survey", ride_table, "teal"),
                step(
                    "Restrict the Sample Space",
                    r"""
                    <div class="step-math">
                        \[\text{Given disliked} \Rightarrow \text{look only at the 53 riders who disliked the ride}\]
                    </div>
                    """,
                ),
                step(
                    "Form the Conditional Probability",
                    r"""
                    <div class="step-math">
                        \[P(\text{Adult}\mid \text{Disliked}) = \dfrac{31}{53}\]
                    </div>
                    """,
                    "dark",
                ),
            ],
            label="Example 2",
        ),
        example(
            "Conditional Probability from a Venn Diagram",
            r"In a class of \(25\) students, \(14\) use Instagram and \(16\) use TikTok. One student uses neither platform and six students use both. Find the probability that a randomly selected student uses Instagram given that the student uses TikTok.",
            [
                step(
                    "Build the Venn Diagram",
                    venn_diagram(
                        "Instagram",
                        "TikTok",
                        "8",
                        "6",
                        "10",
                        "1",
                        "TikTok users are the restricted sample space, so we look inside the TikTok circle only.",
                    ),
                    "teal",
                ),
                step(
                    "Restrict to TikTok Users",
                    r"""
                    <div class="step-math">
                        \[P(\text{Instagram}\mid \text{TikTok}) = \dfrac{6}{16}\]
                    </div>
                    """,
                ),
                step("Answer", r'<div class="step-math">\[P(\text{Instagram}\mid \text{TikTok}) = \dfrac{3}{8}\]</div>', "dark"),
            ],
            label="Example 3",
        ),
        example(
            "Fruit Preferences",
            r"In a class of \(40\) students, \(34\) like bananas, \(22\) like pineapples, and \(2\) dislike both fruits. Find (a) the probability that a student likes bananas given that the student likes pineapples and (b) the probability that a student dislikes pineapples given that the student likes bananas.",
            [
                step(
                    "Find the Overlap First",
                    join_blocks(
                        venn_diagram(
                            "Bananas",
                            "Pineapples",
                            "16",
                            "18",
                            "4",
                            "2",
                            r"Since 2 students like neither, 38 students like at least one fruit. The overlap is \(34 + 22 - 38 = 18\).",
                        )
                    ),
                    "teal",
                ),
                step(
                    "Part (a): Bananas Given Pineapples",
                    r"""
                    <div class="step-math">
                        \[P(B\mid P) = \dfrac{18}{22} = \dfrac{9}{11}\]
                    </div>
                    """,
                ),
                step(
                    "Part (b): Not Pineapples Given Bananas",
                    r"""
                    <div class="step-math">
                        \[P(P'\mid B) = \dfrac{16}{34} = \dfrac{8}{17}\]
                    </div>
                    """,
                    "dark",
                ),
            ],
            label="Example 4",
        ),
        example(
            "Conditional Probability from a Tree Diagram",
            r"Emma studies in her bedroom \(40\%\) of the time and at the library \(60\%\) of the time. In her bedroom she does math \(70\%\) of the time; at the library she does math \(50\%\) of the time. If Emma is doing math, what is the probability she is in her bedroom?",
            [
                step("Draw the Tree", emma_tree, "teal"),
                step(
                    "Find the Math Outcomes",
                    r"""
                    <div class="step-math">
                        \[P(\text{Bedroom and Math}) = 0.4(0.7) = 0.28\]
                    </div>
                    <div class="step-math">
                        \[P(\text{Math}) = 0.28 + 0.30 = 0.58\]
                    </div>
                    """,
                ),
                step(
                    "Form the Conditional Probability",
                    r"""
                    <div class="step-math">
                        \[P(\text{Bedroom}\mid \text{Math}) = \dfrac{0.28}{0.58} = \dfrac{14}{29}\]
                    </div>
                    """,
                    "dark",
                ),
            ],
            label="Example 5",
        ),
        example(
            "Weighted Basket Choice",
            r"Basket A contains \(3\) red and \(2\) white tickets. Basket B contains \(4\) red and \(1\) white ticket. A die with four faces marked A and two faces marked B chooses the basket. Given that the selected ticket is red, find the probability that it came from Basket B.",
            [
                step("Draw the Weighted Tree", basket_tree, "teal"),
                step(
                    "Find the Red Outcomes",
                    r"""
                    <div class="step-math">
                        \[P(B \cap R) = \dfrac{2}{6}\cdot\dfrac{4}{5} = \dfrac{4}{15}\]
                    </div>
                    <div class="step-math">
                        \[P(R) = \dfrac{4}{6}\cdot\dfrac{3}{5} + \dfrac{2}{6}\cdot\dfrac{4}{5} = \dfrac{2}{5} + \dfrac{4}{15} = \dfrac{2}{3}\]
                    </div>
                    """,
                ),
                step(
                    "Form the Conditional Probability",
                    r"""
                    <div class="step-math">
                        \[P(B\mid R) = \dfrac{\frac{4}{15}}{\frac{2}{3}} = \dfrac{2}{5}\]
                    </div>
                    """,
                    "dark",
                ),
            ],
            label="Example 6",
        ),
    ]
    return {
        "filename": "6.7-conditional-probability.html",
        "section": "6.7",
        "title": "Conditional Probability",
        "objective": "Use tables, Venn diagrams, and tree diagrams to compute probabilities under given conditions.",
        "chips": ["given that", "two-way tables", "Venn diagrams", "tree diagrams", "restricted sample space"],
        "slides": slides,
    }


DECK_BUILDERS = [
    build_sequences_deck,
    build_arithmetic_deck,
    build_geometric_deck,
    build_binomial_deck,
    build_counting_deck,
    build_probability_deck,
    build_conditional_probability_deck,
]


def main() -> None:
    for builder in DECK_BUILDERS:
        deck = builder()
        html = render_deck(deck)
        (ROOT / deck["filename"]).write_text(html + "\n", encoding="utf-8")
        print(f"Wrote {deck['filename']}")


if __name__ == "__main__":
    main()
