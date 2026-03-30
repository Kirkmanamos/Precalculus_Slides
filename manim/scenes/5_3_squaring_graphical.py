"""
Graphical analysis of  cos x + 1 = sin x  — solve in [0, 2π).

Narrative arc
─────────────
1. Title + equation + "[0, 2π)" domain badge
2. Algebra steps: square both sides → Pythagorean sub → factor → ZPP
   • Warning: squaring can introduce extraneous solutions
   • Candidates: π/2, 3π/2, π
3. Single full-scene graph: y = cos x + 1  vs  y = sin x  on [0, 2π]
   • Two TRUE intersections at π/2 and π (green dots + ✓)
   • One EXTRANEOUS candidate at 3π/2 (red ✗ + gap annotation)
4. Solution banner: x = π/2, x = π

Key insight: at x = 3π/2, cos(3π/2)+1 = 1 but sin(3π/2) = -1 → gap of 2.
Graphically obvious the curves don't meet there.

Render (from the manim/ directory):
    manim -pql scenes/5_3_squaring_graphical.py SquaringGraphicalAnalysis
    manim -pqh scenes/5_3_squaring_graphical.py SquaringGraphicalAnalysis
"""

from manim import *
import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from shared.colors import *

# ── 3b1b palette override ────────────────────────────────────────────────────
BG_COLOR    = "#1C1C2E"
TEXT_COLOR   = WHITE
TEXT_MUTED   = GREY_B
AXIS_COLOR   = GREY_C
TICK_COLOR   = GREY_A
HIGHLIGHT    = YELLOW
ACCENT_TEAL  = TEAL
ACCENT_BLUE  = BLUE_B
ACCENT_RED   = RED
Q1_COLOR     = GREEN
Q3_COLOR     = RED


class SquaringGraphicalAnalysis(Scene):
    """
    Single-panel graph — both sides plotted, extraneous candidate highlighted.
    """

    FULL_CTR = DOWN * 0.55

    def construct(self):
        self.camera.background_color = BG_COLOR
        self._phase_intro()
        self._phase_math_steps()
        self._phase_graph()
        self._phase_banner()

    # ── Phase 1 : title + domain badge ──────────────────────────────────────
    def _phase_intro(self):
        title = MathTex(
            r"\text{Graphical Analysis:}\quad"
            r"\cos x + 1 = \sin x",
            font_size=34, color=TEXT_COLOR,
        ).to_edge(UP, buff=0.28)

        subtitle = MathTex(
            r"\text{Solve in } [0,\, 2\pi)"
            r"\text{ --- restricted domain}",
            font_size=26, color=ACCENT_BLUE,
        ).next_to(title, DOWN, buff=0.20)
        sub_box = SurroundingRectangle(
            subtitle, color=ACCENT_BLUE, stroke_width=1.5,
            fill_color="#141428", fill_opacity=0.50,
            buff=0.13, corner_radius=0.08,
        )

        title.set_z_index(10)
        self.play(Write(title), run_time=1.1)
        self.play(Write(subtitle), run_time=0.9)
        self.play(Create(sub_box), run_time=0.40)
        self.wait(1.5)

        self.title    = title
        self.subtitle = VGroup(sub_box, subtitle)

    # ── Phase 2 : algebra steps ─────────────────────────────────────────────
    def _phase_math_steps(self):
        """
        Four algebra rows + warning + ZPP split + candidates + bridge.
        """

        s0 = MathTex(
            r"\cos x + 1 = \sin x",
            font_size=34, color=TEXT_COLOR,
        )
        s1 = MathTex(
            r"(\cos x + 1)^2 = \sin^2\!x",
            font_size=34, color=TEXT_COLOR,
        )
        s2 = MathTex(
            r"2\cos^2\!x + 2\cos x = 0",
            font_size=34, color=TEXT_COLOR,
        )
        s3 = MathTex(
            r"2\cos x\,(\cos x + 1) = 0",
            font_size=34, color=TEXT_COLOR,
        )

        ann0 = Tex(r"original equation",                    font_size=21, color=TEXT_MUTED)
        ann1 = Tex(r"square both sides",                     font_size=21, color=TEXT_MUTED)
        ann2 = Tex(r"expand, $\sin^2\!x = 1 - \cos^2\!x$", font_size=21, color=TEXT_MUTED)
        ann3 = Tex(r"factor",                                 font_size=21, color=TEXT_MUTED)

        steps_col = VGroup(s0, s1, s2, s3).arrange(
            DOWN, buff=0.45, aligned_edge=LEFT,
        )
        steps_col.next_to(self.subtitle, DOWN, buff=0.35).to_edge(LEFT, buff=1.0)

        for step, ann in [(s0, ann0), (s1, ann1), (s2, ann2), (s3, ann3)]:
            ann.next_to(step, RIGHT, buff=0.45)

        arr1 = MathTex(r"\Downarrow", font_size=24, color=TEXT_MUTED).move_to(
            (s0.get_bottom() + s1.get_top()) / 2)
        arr2 = MathTex(r"\Downarrow", font_size=24, color=TEXT_MUTED).move_to(
            (s1.get_bottom() + s2.get_top()) / 2)
        arr3 = MathTex(r"\Downarrow", font_size=24, color=TEXT_MUTED).move_to(
            (s2.get_bottom() + s3.get_top()) / 2)

        # ── warning box ─────────────────────────────────────────────────
        warn_tex = Tex(
            r"\textbf{[!] Squaring can introduce extraneous solutions"
            r" --- must verify!}",
            font_size=21, color=ACCENT_RED,
        )
        warn_box = SurroundingRectangle(
            warn_tex, color=ACCENT_RED, stroke_width=1.5,
            fill_color="#2a1420", fill_opacity=0.55,
            buff=0.13, corner_radius=0.08,
        )
        warn_grp = VGroup(warn_box, warn_tex)
        warn_tex.move_to(warn_box)
        warn_grp.next_to(s3, DOWN, buff=0.28)

        # ── ZPP split ──────────────────────────────────────────────────
        zpp_lbl = Tex(
            r"\textbf{Zero Product Property:}",
            font_size=25, color=TEXT_MUTED,
        )
        case1 = MathTex(r"\cos x = 0",  font_size=32, color=Q1_COLOR)
        or_tx = Tex(r"\textbf{or}",     font_size=25, color=TEXT_MUTED)
        case2 = MathTex(r"\cos x = -1", font_size=32, color=ACCENT_BLUE)
        cases_row = VGroup(case1, or_tx, case2).arrange(RIGHT, buff=0.50)

        zpp_grp = VGroup(zpp_lbl, cases_row).arrange(DOWN, buff=0.20)
        zpp_grp.next_to(warn_grp, DOWN, buff=0.22)

        # ── bridge ──────────────────────────────────────────────────────
        bridge = Tex(
            r"Candidates: $\tfrac{\pi}{2},\;\pi,\;\tfrac{3\pi}{2}$"
            r"\quad --- verify graphically $\longrightarrow$",
            font_size=24, color=HIGHLIGHT,
        ).to_edge(DOWN, buff=0.38)

        # ── animate ─────────────────────────────────────────────────────
        self.play(FadeIn(s0, shift=RIGHT * 0.1), FadeIn(ann0), run_time=0.70)
        self.wait(0.20)

        self.play(Write(arr1), run_time=0.25)
        self.play(FadeIn(s1, shift=RIGHT * 0.1), FadeIn(ann1), run_time=0.70)
        self.wait(0.20)

        self.play(Write(arr2), run_time=0.25)
        self.play(FadeIn(s2, shift=RIGHT * 0.1), FadeIn(ann2), run_time=0.70)
        self.wait(0.20)

        self.play(Write(arr3), run_time=0.25)
        self.play(FadeIn(s3, shift=RIGHT * 0.1), FadeIn(ann3), run_time=0.70)
        self.wait(0.25)

        self.play(FadeIn(warn_grp, shift=UP * 0.08), run_time=0.60)
        self.wait(0.8)

        self.play(Write(zpp_lbl), run_time=0.50)
        self.play(
            LaggedStart(Write(case1), Write(or_tx), Write(case2), lag_ratio=0.25),
            run_time=1.0,
        )
        self.wait(0.25)

        self.play(Write(bridge), run_time=0.65)
        self.wait(0.6)

        self.play(
            FadeOut(VGroup(
                self.subtitle,
                s0, s1, s2, s3,
                ann0, ann1, ann2, ann3,
                arr1, arr2, arr3,
                warn_grp, zpp_grp, bridge,
            )),
            run_time=0.85,
        )

    # ── Phase 3 : graph — both sides on one set of axes ─────────────────────
    def _phase_graph(self):
        axes = Axes(
            x_range=[0, 2 * PI + 0.2, PI / 2],
            y_range=[-1.5, 2.3, 0.5],
            x_length=10.2,
            y_length=5.6,
            axis_config={
                "color": AXIS_COLOR, "include_tip": True,
                "tip_length": 0.16, "stroke_width": 1.8,
            },
            y_axis_config={
                "include_numbers": True,
                "numbers_to_include": [-1, 1, 2],
                "font_size": 22,
            },
        ).move_to(self.FULL_CTR)

        # x-tick labels
        xv = [0, PI / 2, PI, 3 * PI / 2, 2 * PI]
        xs = [r"0", r"\tfrac{\pi}{2}", r"\pi",
              r"\tfrac{3\pi}{2}", r"2\pi"]
        x_lbls = VGroup(*[
            MathTex(s, font_size=21, color=TICK_COLOR)
              .next_to(axes.c2p(v, 0), DOWN, buff=0.22)
            for v, s in zip(xv, xs)
        ])
        xe = MathTex(r"x", font_size=25, color=AXIS_COLOR).next_to(
            axes.x_axis.get_right(), RIGHT, buff=0.09)
        ye = MathTex(r"y", font_size=25, color=AXIS_COLOR).next_to(
            axes.y_axis.get_top(), UP, buff=0.08)

        # ── plot both curves ────────────────────────────────────────────
        # LHS: y = cos x + 1
        lhs_curve = axes.plot(
            lambda x: np.cos(x) + 1,
            x_range=[0, 2 * PI],
            color=ACCENT_TEAL, stroke_width=3,
        )
        lhs_lbl = MathTex(
            r"y = \cos x + 1", font_size=25, color=ACCENT_TEAL,
        ).next_to(axes.c2p(0.3, np.cos(0.3) + 1), UL, buff=0.12)

        # RHS: y = sin x
        rhs_curve = axes.plot(
            lambda x: np.sin(x),
            x_range=[0, 2 * PI],
            color=Q3_COLOR, stroke_width=3,
        )
        rhs_lbl = MathTex(
            r"y = \sin x", font_size=25, color=Q3_COLOR,
        ).next_to(axes.c2p(PI / 2 + 0.2, 1), UR, buff=0.12)

        # ── animate axes + curves ───────────────────────────────────────
        self.play(Create(axes), run_time=1.0)
        self.play(
            LaggedStart(*[Write(l) for l in x_lbls], lag_ratio=0.09),
            Write(xe), Write(ye), run_time=0.85,
        )
        self.play(Create(lhs_curve), Write(lhs_lbl), run_time=1.2)
        self.play(Create(rhs_curve), Write(rhs_lbl), run_time=1.2)
        self.wait(0.5)

        # ── mark TRUE intersections ─────────────────────────────────────
        # x = π/2: cos(π/2)+1 = 1, sin(π/2) = 1 → match ✓
        pt_half = axes.c2p(PI / 2, 1)
        dot_half = Dot(pt_half, radius=0.12, color=Q1_COLOR)
        lbl_half = MathTex(
            r"\tfrac{\pi}{2}", font_size=24, color=Q1_COLOR,
        ).next_to(pt_half, UL, buff=0.14)
        chk_half = MathTex(
            r"\checkmark", font_size=28, color=Q1_COLOR,
        ).next_to(dot_half, DR, buff=0.08)

        self.play(
            FadeIn(dot_half, scale=1.7), Write(lbl_half), Write(chk_half),
            run_time=0.80,
        )
        self.wait(0.25)

        # x = π: cos(π)+1 = 0, sin(π) = 0 → match ✓
        pt_pi = axes.c2p(PI, 0)
        dot_pi = Dot(pt_pi, radius=0.12, color=Q1_COLOR)
        lbl_pi = MathTex(
            r"\pi", font_size=24, color=Q1_COLOR,
        ).next_to(pt_pi, DL, buff=0.14)
        chk_pi = MathTex(
            r"\checkmark", font_size=28, color=Q1_COLOR,
        ).next_to(dot_pi, UR, buff=0.08)

        self.play(
            FadeIn(dot_pi, scale=1.7), Write(lbl_pi), Write(chk_pi),
            run_time=0.80,
        )
        self.wait(0.25)

        # ── mark EXTRANEOUS candidate at 3π/2 ──────────────────────────
        # cos(3π/2)+1 = 1 (teal curve), sin(3π/2) = -1 (pink curve)
        pt_top = axes.c2p(3 * PI / 2, 1)     # on teal curve
        pt_bot = axes.c2p(3 * PI / 2, -1)    # on pink curve

        dot_top = Dot(pt_top, radius=0.10, color=ACCENT_RED)
        dot_bot = Dot(pt_bot, radius=0.10, color=ACCENT_RED)

        # vertical gap arrow between the two values
        gap_line = DashedLine(
            pt_top, pt_bot,
            color=ACCENT_RED, dash_length=0.10, stroke_width=2.5,
        )
        gap_lbl = MathTex(
            r"\text{gap} = 2", font_size=22, color=ACCENT_RED,
        ).next_to(gap_line, RIGHT, buff=0.12)

        x_lbl_ext = MathTex(
            r"\tfrac{3\pi}{2}", font_size=24, color=ACCENT_RED,
        ).next_to(pt_bot, DOWN, buff=0.18)
        x_mark = MathTex(
            r"\times", font_size=28, color=ACCENT_RED,
        ).next_to(dot_top, UL, buff=0.06)

        self.play(
            FadeIn(dot_top, scale=1.5), FadeIn(dot_bot, scale=1.5),
            Create(gap_line), Write(gap_lbl),
            Write(x_lbl_ext), Write(x_mark),
            run_time=1.1,
        )
        self.wait(0.4)

        # Extraneous annotation
        ext_note = VGroup(
            Tex(r"\textbf{Extraneous!}", font_size=26, color=ACCENT_RED),
            MathTex(
                r"\cos\!\tfrac{3\pi}{2}+1 = 1 \;\neq\; "
                r"\sin\!\tfrac{3\pi}{2} = -1",
                font_size=22, color=ACCENT_RED,
            ),
        ).arrange(DOWN, buff=0.10).next_to(
            axes.c2p(3 * PI / 2, -1), DOWN, buff=0.30,
        )

        self.play(Write(ext_note), run_time=0.90)
        self.wait(1.0)

        # Store graph VGroup for potential use
        self.graph_vg = VGroup(
            axes, x_lbls, xe, ye,
            lhs_curve, lhs_lbl, rhs_curve, rhs_lbl,
            dot_half, lbl_half, chk_half,
            dot_pi, lbl_pi, chk_pi,
            dot_top, dot_bot, gap_line, gap_lbl,
            x_lbl_ext, x_mark, ext_note,
        )

    # ── Phase 4 : solution banner ───────────────────────────────────────────
    def _phase_banner(self):
        banner = RoundedRectangle(
            corner_radius=0.14,
            width=9.0, height=0.95,
            fill_color="#12122a", fill_opacity=0.97,
            stroke_color=HIGHLIGHT, stroke_width=2.5,
        ).to_edge(DOWN, buff=0.18)

        sol = MathTex(
            r"x = \dfrac{\pi}{2},\quad x = \pi",
            font_size=38, color=HIGHLIGHT,
        ).move_to(banner)

        self.play(DrawBorderThenFill(banner), run_time=0.60)
        self.play(Write(sol), run_time=1.25)
        self.wait(2.5)
