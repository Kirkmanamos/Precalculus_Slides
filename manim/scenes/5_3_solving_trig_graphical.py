"""
Graphical analysis of tan²θ - 3 = 0 for 0 ≤ θ < 2π.

Shows y = tan(θ) with horizontal reference lines y = ±√3,
dropping vertical lines at each of the four solutions and
labeling the quadrant where each intersection lives.

Render (from the manim/ directory):
    manim -pql scenes/5_3_solving_trig_graphical.py TanEquationGraphicalAnalysis
    manim -pqh scenes/5_3_solving_trig_graphical.py TanEquationGraphicalAnalysis
"""

from manim import *
import sys, os

# Allow running from repo root OR from manim/ directory
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from shared.colors import *

# ── constants ─────────────────────────────────────────────────────────────────
SQRT3   = np.sqrt(3)
EPS     = 0.07          # gap either side of tan asymptotes
ASYM_C  = "#3d5a73"     # muted blue-grey for asymptote dashes


class TanEquationGraphicalAnalysis(Scene):
    """
    Animated graphical solution of  tan²θ − 3 = 0  on [0, 2π).

    Narrative arc
    ─────────────
    1. Title + algebraic bridge  (tan²θ=3 → tanθ=±√3)
    2. Build axes, draw y=tan θ (three branches around asymptotes)
    3. Drop y = √3  → reveal π/3 (QI) and 4π/3 (QIII)
    4. Drop y = −√3 → reveal 2π/3 (QII) and 5π/3 (QIV)
    5. Solution banner: θ = π/3, 2π/3, 4π/3, 5π/3
    """

    # ── main entry point ──────────────────────────────────────────────────────
    def construct(self):
        self.camera.background_color = BG_COLOR

        self._phase_intro()
        self._phase_axes()
        self._phase_curve()
        self._phase_positive_root()
        self._phase_negative_root()
        self._phase_solution_banner()

    # ── Phase 1 : title + algebraic bridge ───────────────────────────────────
    def _phase_intro(self):
        title = MathTex(
            r"\text{Graphical Analysis:}\quad \tan^2\!\theta - 3 = 0",
            font_size=34,
            color=TEXT_COLOR,
        ).to_edge(UP, buff=0.25)

        bridge = MathTex(
            r"\tan^2\!\theta = 3",
            r"\quad\Longrightarrow\quad",
            r"\tan\theta = \pm\sqrt{3}",
            font_size=30,
            color=TEXT_COLOR,
        )
        bridge[2].set_color(HIGHLIGHT)          # ±√3 in gold
        bridge.next_to(title, DOWN, buff=0.22)

        self.play(Write(title), run_time=1.0)
        self.play(Write(bridge), run_time=1.3)
        self.wait(0.5)

        self.title  = title
        self.bridge = bridge

    # ── Phase 2 : coordinate axes ────────────────────────────────────────────
    def _phase_axes(self):
        axes = Axes(
            x_range=[0, 2 * PI + 0.2, PI / 2],
            y_range=[-4, 4, 1],
            x_length=9.8,
            y_length=5.2,
            axis_config={
                "color":        AXIS_COLOR,
                "include_tip":  True,
                "tip_length":   0.17,
                "stroke_width": 1.8,
            },
            y_axis_config={
                "include_numbers":   True,
                "numbers_to_include": [-3, -2, -1, 1, 2, 3],
                "font_size":         18,
            },
        ).shift(DOWN * 0.85)

        # ── θ-axis custom labels ───────────────────────────────────────────
        x_vals = [0,    PI / 2,             PI,    3 * PI / 2,          2 * PI]
        x_strs = [r"0", r"\frac{\pi}{2}", r"\pi", r"\frac{3\pi}{2}", r"2\pi"]
        x_lbls = VGroup(*[
            MathTex(s, font_size=20, color=TICK_COLOR)
              .next_to(axes.c2p(v, 0), DOWN, buff=0.22)
            for v, s in zip(x_vals, x_strs)
        ])

        theta_lbl = MathTex(r"\theta", font_size=26, color=AXIS_COLOR).next_to(
            axes.x_axis.get_right(), RIGHT, buff=0.12)
        y_lbl = MathTex(r"y", font_size=26, color=AXIS_COLOR).next_to(
            axes.y_axis.get_top(), UP, buff=0.10)

        # ── ±√3 tick labels on y-axis (colored) ───────────────────────────
        self._sqrt3_lbl = MathTex(
            r"\sqrt{3}", font_size=19, color=Q1_COLOR
        ).next_to(axes.c2p(0, SQRT3), LEFT, buff=0.14)

        self._neg_sqrt3_lbl = MathTex(
            r"-\!\sqrt{3}", font_size=19, color=Q3_COLOR
        ).next_to(axes.c2p(0, -SQRT3), LEFT, buff=0.14)

        self.play(Create(axes), run_time=1.2)
        self.play(
            LaggedStart(*[Write(l) for l in x_lbls], lag_ratio=0.12),
            Write(theta_lbl), Write(y_lbl),
            run_time=0.9,
        )

        self.axes = axes       # store for later phases

    # ── Phase 3 : asymptotes + tan curve ─────────────────────────────────────
    def _phase_curve(self):
        axes = self.axes

        # asymptote dashed lines
        asym1 = DashedLine(
            axes.c2p(PI / 2,     -3.85), axes.c2p(PI / 2,     3.85),
            color=ASYM_C, dash_length=0.12, stroke_width=1.4,
        )
        asym2 = DashedLine(
            axes.c2p(3 * PI / 2, -3.85), axes.c2p(3 * PI / 2, 3.85),
            color=ASYM_C, dash_length=0.12, stroke_width=1.4,
        )
        asym_lbl1 = MathTex(
            r"\theta=\tfrac{\pi}{2}", font_size=16, color=ASYM_C
        ).next_to(axes.c2p(PI / 2, 3.85), UP, buff=0.05)
        asym_lbl2 = MathTex(
            r"\theta=\tfrac{3\pi}{2}", font_size=16, color=ASYM_C
        ).next_to(axes.c2p(3 * PI / 2, 3.85), UP, buff=0.05)

        self.play(
            LaggedStart(
                AnimationGroup(Create(asym1), Create(asym2)),
                AnimationGroup(Write(asym_lbl1), Write(asym_lbl2)),
                lag_ratio=0.3,
            ),
            run_time=0.9,
        )

        # tan curve — three branches (avoids the two asymptotes)
        br_kw = dict(color=ACCENT_TEAL, stroke_width=3)
        b1 = axes.plot(np.tan, x_range=[0,            PI / 2     - EPS, 0.01], **br_kw)
        b2 = axes.plot(np.tan, x_range=[PI / 2  + EPS, 3 * PI / 2 - EPS, 0.01], **br_kw)
        b3 = axes.plot(np.tan, x_range=[3 * PI / 2 + EPS, 2 * PI,        0.01], **br_kw)

        curve_lbl = MathTex(r"y = \tan\theta", font_size=22, color=ACCENT_TEAL).next_to(
            axes.c2p(PI * 0.16, np.tan(PI * 0.16)), UR, buff=0.15)

        self.play(
            LaggedStart(Create(b1), Create(b2), Create(b3), lag_ratio=0.2),
            run_time=2.5,
        )
        self.play(Write(curve_lbl), run_time=0.7)
        self.wait(0.5)

    # ── Phase 4 : y = √3 and positive solutions ───────────────────────────────
    def _phase_positive_root(self):
        axes = self.axes

        # horizontal reference line y = √3
        pos_hline = DashedLine(
            axes.c2p(0,       SQRT3),
            axes.c2p(2 * PI,  SQRT3),
            color=Q1_COLOR, dash_length=0.16, stroke_width=2.5,
        )
        pos_hline_lbl = MathTex(
            r"y = \sqrt{3}", font_size=22, color=Q1_COLOR
        ).next_to(axes.c2p(PI / 5, SQRT3), UP, buff=0.12)

        self.play(
            Create(pos_hline),
            Write(self._sqrt3_lbl),
            run_time=1.0,
        )
        self.play(Write(pos_hline_lbl), run_time=0.55)
        self.wait(0.3)

        # tan θ = +√3  →  θ = π/3 (QI),  θ = 4π/3 (QIII)
        self._mark_solution(
            axes, PI / 3,     SQRT3,  Q1_COLOR,
            r"\dfrac{\pi}{3}",  "QI",   UR,
        )
        self._mark_solution(
            axes, 4 * PI / 3, SQRT3,  Q1_COLOR,
            r"\dfrac{4\pi}{3}", "QIII", UL,
        )
        self.wait(0.5)

    # ── Phase 5 : y = −√3 and negative solutions ─────────────────────────────
    def _phase_negative_root(self):
        axes = self.axes

        # horizontal reference line y = −√3
        neg_hline = DashedLine(
            axes.c2p(0,       -SQRT3),
            axes.c2p(2 * PI,  -SQRT3),
            color=Q3_COLOR, dash_length=0.16, stroke_width=2.5,
        )
        neg_hline_lbl = MathTex(
            r"y = -\sqrt{3}", font_size=22, color=Q3_COLOR
        ).next_to(axes.c2p(PI / 5, -SQRT3), DOWN, buff=0.12)

        self.play(
            Create(neg_hline),
            Write(self._neg_sqrt3_lbl),
            run_time=1.0,
        )
        self.play(Write(neg_hline_lbl), run_time=0.55)
        self.wait(0.3)

        # tan θ = -√3  →  θ = 2π/3 (QII),  θ = 5π/3 (QIV)
        self._mark_solution(
            axes, 2 * PI / 3, -SQRT3, Q3_COLOR,
            r"\dfrac{2\pi}{3}",  "QII", UR,
        )
        self._mark_solution(
            axes, 5 * PI / 3, -SQRT3, Q3_COLOR,
            r"\dfrac{5\pi}{3}",  "QIV", UL,
        )
        self.wait(0.6)

    # ── Phase 6 : solution summary banner ─────────────────────────────────────
    def _phase_solution_banner(self):
        banner = RoundedRectangle(
            corner_radius=0.14,
            width=9.0, height=0.86,
            fill_color="#0b1d2e", fill_opacity=0.96,
            stroke_color=HIGHLIGHT, stroke_width=2.5,
        ).to_edge(DOWN, buff=0.16)

        sol = MathTex(
            r"\theta = \dfrac{\pi}{3},\quad"
            r"\dfrac{2\pi}{3},\quad"
            r"\dfrac{4\pi}{3},\quad"
            r"\dfrac{5\pi}{3}",
            font_size=30,
            color=HIGHLIGHT,
        ).move_to(banner)

        self.play(DrawBorderThenFill(banner), run_time=0.65)
        self.play(Write(sol), run_time=1.3)
        self.wait(2.5)

    # ── helper ────────────────────────────────────────────────────────────────
    def _mark_solution(self, axes, theta, y_val, color, theta_str, quad, q_dir):
        """
        Animate one solution intersection:
          • vertical dashed drop-line from (θ, y_val) to x-axis
          • glowing gold dot at the intersection
          • θ-label below the x-axis tick
          • quadrant tag next to the dot
        """
        pt    = axes.c2p(theta, y_val)
        foot  = axes.c2p(theta, 0)

        vline = DashedLine(pt, foot, color=color, dash_length=0.10, stroke_width=2.0)
        dot   = Dot(pt, radius=0.11, color=HIGHLIGHT, z_index=5)
        xlbl  = MathTex(theta_str, font_size=20, color=HIGHLIGHT).next_to(foot, DOWN, buff=0.18)
        qlbl  = Tex(quad, font_size=17, color=color).next_to(dot, q_dir, buff=0.09)

        self.play(
            Create(vline),
            FadeIn(dot, scale=1.7),
            Write(xlbl),
            Write(qlbl),
            run_time=0.95,
        )
        self.wait(0.15)
