"""
Shared helpers for 5.5 Double & Half-Angle Manim scenes.

3Blue1Brown-inspired style:
  - Large centered visuals (unit circle dominates)
  - Organic text positioning (contextual, near what it describes)
  - 3b1b color palette (BLUE, YELLOW, GREEN, RED, TEAL)
  - Semi-transparent fills, smooth transforms, LaggedStart

Import at the top of every 5.5 scene file:
    from shared.helpers import *
"""

from manim import *

# ─────────────────────────────────────────────────────────────────────────────
# 3b1b-inspired color palette (overrides project defaults for these scenes)
# ─────────────────────────────────────────────────────────────────────────────
BG_3B1B      = "#1C1C2E"       # Dark blue-charcoal (3b1b signature)
TEXT_PRIMARY  = WHITE
TEXT_SECONDARY = GREY_B
TEXT_TERTIARY  = GREY_C

# Triangle side colors (3b1b-ish)
SIDE_A_COLOR = BLUE            # horizontal leg
SIDE_B_COLOR = RED             # vertical leg
SIDE_C_COLOR = GREEN           # hypotenuse

# Quadrant accent colors
QI_COLOR  = GREEN
QII_COLOR = TEAL
QIII_COLOR = RED
QIV_COLOR = GOLD

ANSWER_COLOR = YELLOW          # final answers, key results
FORMULA_COLOR = BLUE_B         # formula templates
LABEL_COLOR  = GREY_A          # axis labels, small annotations

# ─────────────────────────────────────────────────────────────────────────────
# Layout — organic, centered (NOT rigid panels)
# ─────────────────────────────────────────────────────────────────────────────
FRAME_W = config.frame_width           # 14.222
FRAME_H = config.frame_height          # 8.0

# Unit circle: large, centered (or slightly left to leave equation room)
# UC_SCALE = how many screen units = 1 on the axes (controls overall size)
UC_SCALE = 2.5                         # big — dominates the scene
UC_CENTER = ORIGIN + LEFT * 0.8        # slightly left of center
UC_CENTER_SOLO = ORIGIN                # when there's no side content

# Equation area: right side, organic
EQ_X = 4.2                            # right-of-center for step equations
EQ_TOP_Y = 2.5                        # starting y for equation stacks


# ─────────────────────────────────────────────────────────────────────────────
# Unit circle builder
# ─────────────────────────────────────────────────────────────────────────────
def build_unit_circle(center=None, radius=None, show_ticks=True):
    """
    Build a large unit circle diagram. Returns (group, axes).

    `radius` = screen-space distance from center to the "1" mark.
    The circle passes exactly through the ±1 tick marks.
    Axes extend to ±1.5 so tips are visible beyond the circle.
    """
    if center is None:
        center = UC_CENTER
    if radius is None:
        radius = UC_SCALE

    # axis_len maps [-1.5, 1.5] (span=3). We want "1" at `radius` from center.
    # So axis_len = radius * 3  (since 1 unit = axis_len / 3)
    axis_len = radius * 3.0

    axes = Axes(
        x_range=[-1.5, 1.5, 1],
        y_range=[-1.5, 1.5, 1],
        x_length=axis_len,
        y_length=axis_len,
        axis_config={
            "color": GREY_C,
            "include_tip": True,
            "tip_length": 0.16,
            "stroke_width": 1.8,
        },
    ).move_to(center)

    # Circle radius = exactly the distance from origin to "1" on the axes
    circle = Circle(
        radius=radius,
        color=GREY_B,
        stroke_width=2.2,
        fill_opacity=0.03,
        fill_color=BLUE,
    ).move_to(center)

    parts = [axes, circle]

    if show_ticks:
        for val, label_str in [(1, "1"), (-1, "-1")]:
            xt = MathTex(label_str, font_size=18, color=LABEL_COLOR).next_to(
                axes.c2p(val, 0), DOWN, buff=0.15
            )
            yt = MathTex(label_str, font_size=18, color=LABEL_COLOR).next_to(
                axes.c2p(0, val), LEFT, buff=0.15
            )
            parts.extend([xt, yt])

    group = VGroup(*parts)
    return group, axes


# ─────────────────────────────────────────────────────────────────────────────
# Angle arc
# ─────────────────────────────────────────────────────────────────────────────
def build_angle_arc(axes, angle_rad, color, arc_radius=0.4,
                    label_tex=None, label_font_size=24, label_buff=0.18):
    """Arc from +x-axis to angle. Positioned relative to axes origin."""
    origin = axes.c2p(0, 0)
    unit_len = np.linalg.norm(np.array(axes.c2p(1, 0)) - np.array(origin))
    px_radius = arc_radius * unit_len

    arc = Arc(
        radius=px_radius,
        start_angle=0,
        angle=angle_rad,
        arc_center=origin,
        color=color,
        stroke_width=3,
    )

    parts = [arc]

    if label_tex:
        mid_angle = angle_rad / 2
        lr = px_radius + label_buff + 0.18
        label_pos = origin + lr * np.array([
            np.cos(mid_angle), np.sin(mid_angle), 0
        ])
        label = MathTex(label_tex, font_size=label_font_size, color=color)
        label.move_to(label_pos)
        parts.append(label)

    return VGroup(*parts)


# ─────────────────────────────────────────────────────────────────────────────
# Reference triangle
# ─────────────────────────────────────────────────────────────────────────────
def build_reference_triangle(axes, x_val, y_val,
                              x_label=None, y_label=None, r_label=None,
                              label_font_size=22,
                              x_color=None, y_color=None, r_color=None):
    """
    Right triangle from origin → (x,0) → (x,y).
    Colors default to SIDE_A/B/C (3b1b-style blue/red/green).
    """
    xc = x_color or SIDE_A_COLOR
    yc = y_color or SIDE_B_COLOR
    rc = r_color or SIDE_C_COLOR

    origin = np.array(axes.c2p(0, 0))
    pt_x   = np.array(axes.c2p(x_val, 0))
    pt_xy  = np.array(axes.c2p(x_val, y_val))

    x_leg = Line(origin, pt_x, color=xc, stroke_width=4)
    y_leg = Line(pt_x, pt_xy, color=yc, stroke_width=4)
    hyp   = Line(origin, pt_xy, color=rc, stroke_width=4)

    # Right angle marker
    ms = 0.17
    y_dir = np.array([0, 1 if y_val > 0 else -1, 0])
    x_dir = np.array([-1 if x_val > 0 else 1, 0, 0])
    rm = VGroup(
        Line(pt_x + ms * y_dir, pt_x + ms * y_dir + ms * x_dir,
             color=GREY_C, stroke_width=1.5),
        Line(pt_x + ms * x_dir, pt_x + ms * y_dir + ms * x_dir,
             color=GREY_C, stroke_width=1.5),
    )

    parts = [x_leg, y_leg, hyp, rm]
    group = VGroup(*parts)
    group.x_leg = x_leg
    group.y_leg = y_leg
    group.hyp = hyp
    group.right_angle_mark = rm

    def _label(tex, pos, direction, color):
        if tex is None:
            return None
        lbl = MathTex(tex, font_size=label_font_size, color=color)
        lbl.next_to(pos, direction, buff=0.14)
        group.add(lbl)
        return lbl

    mid_x = (origin + pt_x) / 2
    group.x_lbl = _label(x_label, mid_x, DOWN, xc)

    mid_y = (pt_x + pt_xy) / 2
    y_dir_lbl = RIGHT if x_val > 0 else LEFT
    group.y_lbl = _label(y_label, mid_y, y_dir_lbl, yc)

    mid_r = (origin + pt_xy) / 2
    r_dir_lbl = UL if (x_val > 0 and y_val > 0) else (DL if (x_val > 0 and y_val < 0) else UR)
    group.r_lbl = _label(r_label, mid_r, r_dir_lbl, rc)

    return group


# ─────────────────────────────────────────────────────────────────────────────
# Terminal point on unit circle
# ─────────────────────────────────────────────────────────────────────────────
def build_terminal_point(axes, angle_rad, color=YELLOW, radius=0.10):
    """Glowing dot at (cos θ, sin θ) on the unit circle."""
    x = np.cos(angle_rad)
    y = np.sin(angle_rad)
    pt = axes.c2p(x, y)
    glow = Dot(pt, radius=radius * 2.5, color=color, fill_opacity=0.2, z_index=4)
    dot = Dot(pt, radius=radius, color=color, z_index=5)
    return VGroup(glow, dot)


# ─────────────────────────────────────────────────────────────────────────────
# Quadrant highlight
# ─────────────────────────────────────────────────────────────────────────────
def build_quadrant_highlight(axes, quadrant, color, opacity=0.12):
    """Semi-transparent rectangle covering one quadrant. 1=QI, 2=QII, etc."""
    x_ranges = {1: (0, 1.4), 2: (-1.4, 0), 3: (-1.4, 0), 4: (0, 1.4)}
    y_ranges = {1: (0, 1.4), 2: (0, 1.4), 3: (-1.4, 0), 4: (-1.4, 0)}

    xr, yr = x_ranges[quadrant], y_ranges[quadrant]
    bl = np.array(axes.c2p(xr[0], yr[0]))
    tr = np.array(axes.c2p(xr[1], yr[1]))

    return Rectangle(
        width=abs(tr[0] - bl[0]),
        height=abs(tr[1] - bl[1]),
        fill_color=color,
        fill_opacity=opacity,
        stroke_width=0,
    ).move_to((bl + tr) / 2)


# ─────────────────────────────────────────────────────────────────────────────
# Result box (3b1b-style SurroundingRectangle)
# ─────────────────────────────────────────────────────────────────────────────
def surround_answer(mobject, color=YELLOW, buff=0.2):
    """SurroundingRectangle in 3b1b style — just a clean colored border."""
    return SurroundingRectangle(
        mobject, color=color, buff=buff,
        stroke_width=2.5, corner_radius=0.1,
    )
