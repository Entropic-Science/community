"""Build Entropic Science research-community cards.

Output:
 - front.svg / front.png
 - back.svg / back.png
 - entropic_science_card.pdf (two pages, EU 85x55mm, 3mm bleed)

Notes:
 - Brand fonts (EB Garamond, Space Mono) aren't installable in this sandbox,
   so we stand in TeX Gyre Pagella (Palatino-style; same editorial register
   as Garamond) and Nimbus Mono PS for the technical accents. Substitution
   is preserved as a font-family stack so a print shop with the actual
   brand fonts can re-render cleanly from the SVG.
 - QR is rendered from segno's module matrix, so we can punch the
   leaf-hexagon centerpiece while keeping error-correction = H, which
   tolerates a centerpiece up to ~30% of the area.
"""
import base64
import io
import random
import segno
from PIL import Image
import cairosvg

# ── Palette (attached by user) ────────────────────────────────────────────
PLUM   = "#260C1A"   # primary ink
WINE   = "#401631"   # emphasis
OLIVE  = "#3F4029"   # dark olive
GOLD   = "#7E703A"   # mustard olive / highlight
PAPER  = "#F2F2F2"   # surface

# Mid-tones for hairlines and washes
PLUM_50  = "rgba(38,12,26,0.50)"
PLUM_30  = "rgba(38,12,26,0.30)"
OLIVE_30 = "rgba(63,64,41,0.30)"
GOLD_40  = "rgba(126,112,58,0.40)"
WINE_60  = "rgba(64,22,49,0.60)"

# ── Card geometry (mm) ───────────────────────────────────────────────────
BLEED  = 3
TRIM_W = 85
TRIM_H = 55
W = TRIM_W + BLEED * 2   # 91
H = TRIM_H + BLEED * 2   # 61
SAFE = 4                 # 3mm bleed + 1mm safe area inside trim
SAFE_X0, SAFE_Y0 = BLEED + 1, BLEED + 1
SAFE_X1, SAFE_Y1 = W - BLEED - 1, H - BLEED - 1

# Font stack: real brand fonts first, sandbox fallback last
SERIF = "'EB Garamond','Source Serif 4','TeX Gyre Pagella','Palatino Linotype',serif"
SERIF_ITALIC = SERIF
MONO  = "'Space Mono','Nimbus Mono PS','DejaVu Sans Mono',monospace"
SANS  = "'Inter','DejaVu Sans',sans-serif"

URL = "https://entropic.science/labs/apps/quantum-random-llm-chatbot"
LOGO_PATH = "/sessions/pensive-beautiful-davinci/mnt/Entropic-Science/entropic.science/attached_assets/ESlogo_pattern3_nobg.png"


# ── Helpers ──────────────────────────────────────────────────────────────
def b64_image(path: str) -> str:
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("ascii")


LOGO_B64 = b64_image(LOGO_PATH)


def svg_open(title: str) -> str:
    return f"""<svg xmlns="http://www.w3.org/2000/svg"
     xmlns:xlink="http://www.w3.org/1999/xlink"
     width="{W}mm" height="{H}mm"
     viewBox="0 0 {W} {H}">
  <title>{title}</title>
  <defs>
    <!-- Paper texture: very faint stippling on top of the base paper colour -->
    <filter id="grain">
      <feTurbulence type="fractalNoise" baseFrequency="2.4" numOctaves="2" seed="7"/>
      <feColorMatrix values="0 0 0 0 0.149
                             0 0 0 0 0.047
                             0 0 0 0 0.101
                             0 0 0 0.06 0"/>
      <feComposite in2="SourceGraphic" operator="in"/>
    </filter>
    <!-- Soft inner glow used behind the logo and QR -->
    <radialGradient id="vignette" cx="50%" cy="50%" r="65%">
      <stop offset="0%"  stop-color="{PAPER}" stop-opacity="0"/>
      <stop offset="70%" stop-color="{PLUM}"  stop-opacity="0.04"/>
      <stop offset="100%" stop-color="{PLUM}" stop-opacity="0.12"/>
    </radialGradient>
    <!-- Leaf silhouette used for botanical confetti in corners -->
    <symbol id="leaf" viewBox="-10 -16 20 32" overflow="visible">
      <path d="M0,-15 C 8,-8 8,8 0,15 C -8,8 -8,-8 0,-15 Z" fill="currentColor"/>
      <path d="M0,-13 L0,13" stroke="{PAPER}" stroke-width="0.4" fill="none" opacity="0.5"/>
    </symbol>
    <!-- Sketchy hand-drawn underline -->
    <symbol id="handline" viewBox="0 0 100 4" overflow="visible">
      <path d="M0,2 C 12,1 22,3 36,2 C 50,1 64,3 80,2 C 88,1.5 96,2.5 100,2"
            fill="none" stroke="currentColor" stroke-width="0.35" stroke-linecap="round"/>
    </symbol>
  </defs>
"""


def svg_close() -> str:
    return "</svg>"


def base_layer() -> str:
    """Paper, vignette, very subtle grain. Bleed-to-bleed."""
    return f"""
  <!-- Bleed -->
  <rect x="0" y="0" width="{W}" height="{H}" fill="{PAPER}"/>
  <rect x="0" y="0" width="{W}" height="{H}" fill="url(#vignette)"/>
  <rect x="0" y="0" width="{W}" height="{H}" filter="url(#grain)" opacity="0.55"/>
"""


def trim_marks() -> str:
    """Thin crop marks at the corners outside the trim. Removed on print."""
    L = 1.6
    OFF = 0.6
    c = "rgba(38,12,26,0.55)"
    marks = []
    for cx, cy, sx, sy in [
        (BLEED, BLEED, -1, 0), (BLEED, BLEED, 0, -1),
        (W - BLEED, BLEED, 1, 0), (W - BLEED, BLEED, 0, -1),
        (BLEED, H - BLEED, -1, 0), (BLEED, H - BLEED, 0, 1),
        (W - BLEED, H - BLEED, 1, 0), (W - BLEED, H - BLEED, 0, 1),
    ]:
        x1 = cx + sx * OFF
        y1 = cy + sy * OFF
        x2 = cx + sx * (OFF + L)
        y2 = cy + sy * (OFF + L)
        marks.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{c}" stroke-width="0.15"/>')
    return "<g class=\"crop\">\n  " + "\n  ".join(marks) + "\n  </g>"


def scatter(seed: int, n: int, x0: float, y0: float, x1: float, y1: float,
            color: str = GOLD, max_r: float = 0.45, alpha: float = 0.55) -> str:
    """Brownian-style scatter dots inside a rectangle."""
    rnd = random.Random(seed)
    out = []
    for _ in range(n):
        x = rnd.uniform(x0, x1)
        y = rnd.uniform(y0, y1)
        r = rnd.uniform(0.10, max_r)
        a = rnd.uniform(0.25, alpha)
        out.append(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{r:.2f}" fill="{color}" opacity="{a:.2f}"/>')
    return "<g class=\"scatter\">\n  " + "\n  ".join(out) + "\n  </g>"


import math


def wave_grid(seed: int, x0: float, y0: float, x1: float, y1: float,
              step: float = 4.0, amplitude: float = 0.9, color: str = OLIVE,
              opacity: float = 0.22, stroke: float = 0.10) -> str:
    """Static rendition of EntropySignal's waving copper grid.
    Each gridline is sampled into a sinusoidal polyline so the texture reads
    as 'measurement field' rather than 'graph paper'.
    """
    rnd = random.Random(seed)
    phase_x = rnd.uniform(0, 6.28)
    phase_y = rnd.uniform(0, 6.28)
    lines = []
    # vertical-ish lines
    x = x0
    while x <= x1:
        pts = []
        y = y0
        while y <= y1:
            dx = math.sin(y * 0.42 + phase_x + x * 0.21) * amplitude
            pts.append(f"{x + dx:.2f},{y:.2f}")
            y += 1.0
        lines.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{color}" stroke-width="{stroke}" opacity="{opacity}"/>')
        x += step
    # horizontal-ish lines
    y = y0
    while y <= y1:
        pts = []
        x = x0
        while x <= x1:
            dy = math.cos(x * 0.42 + phase_y + y * 0.21) * amplitude
            pts.append(f"{x:.2f},{y + dy:.2f}")
            x += 1.0
        lines.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{color}" stroke-width="{stroke}" opacity="{opacity}"/>')
        y += step
    return "<g class=\"wave-grid\">\n  " + "\n  ".join(lines) + "\n  </g>"


def sine_wave(seed: int, x0: float, x1: float, y_mid: float,
              amplitude: float = 2.2, frequency: float = 0.32,
              color: str = WINE, opacity: float = 0.35, stroke: float = 0.18,
              jitter: float = 0.6) -> str:
    """Aubergine-style sinusoid with a touch of measurement jitter — the
    'collapse waveform' line that drifts across the landing-page hero."""
    rnd = random.Random(seed)
    phase = rnd.uniform(0, 6.28)
    pts = []
    x = x0
    while x <= x1:
        y = y_mid + math.sin(x * frequency + phase) * amplitude + rnd.uniform(-jitter, jitter) * 0.3
        pts.append(f"{x:.2f},{y:.2f}")
        x += 0.8
    return (
        f'<polyline points="{" ".join(pts)}" fill="none" '
        f'stroke="{color}" stroke-width="{stroke}" opacity="{opacity}" stroke-linecap="round"/>'
    )


def flares(seed: int, n: int, x0: float, y0: float, x1: float, y1: float,
           color: str = GOLD) -> str:
    """A few brighter scatter points — 'collapse flares' from the EntropySignal."""
    rnd = random.Random(seed)
    out = []
    for _ in range(n):
        x = rnd.uniform(x0, x1); y = rnd.uniform(y0, y1)
        r = rnd.uniform(0.32, 0.55)
        out.append(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{r:.2f}" fill="{color}" opacity="0.85"/>')
        # halo
        out.append(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{r*2.4:.2f}" fill="{color}" opacity="0.18"/>')
    return "<g class=\"flares\">\n  " + "\n  ".join(out) + "\n  </g>"


def hex_path(cx: float, cy: float, R: float) -> str:
    """SVG path for a pointy-top regular hexagon, circumradius R, centered (cx,cy)."""
    sqrt3 = 1.7320508
    verts = [
        (cx, cy - R),
        (cx + R * sqrt3 / 2, cy - R / 2),
        (cx + R * sqrt3 / 2, cy + R / 2),
        (cx, cy + R),
        (cx - R * sqrt3 / 2, cy + R / 2),
        (cx - R * sqrt3 / 2, cy - R / 2),
    ]
    pts = " L ".join(f"{x:.3f},{y:.3f}" for x, y in verts)
    return f"M {pts} Z"


def in_hex(x: float, y: float, R: float) -> bool:
    """Point-in-hex test for a pointy-top hex at origin with circumradius R."""
    sqrt3 = 1.7320508
    if abs(x) > R * sqrt3 / 2 + 1e-6:
        return False
    if abs(x / sqrt3 + y) > R + 1e-6:
        return False
    if abs(x / sqrt3 - y) > R + 1e-6:
        return False
    return True


def drifted_text(x: float, y: float, text: str, font_family: str, font_size: float,
                 fill: str, seed: int = 0, drift_y: float = 0.55,
                 color_idx=None, color_alt: str = None, weight: int = 500,
                 letter_spacing: float = -0.15) -> str:
    """Render text letter-by-letter with a per-letter vertical micro-drift.
    Each letter sits at the baseline plus a small dy chosen by the seeded PRNG —
    a frozen-frame echo of the landing page's Stagger / OffGrid primitives,
    here standing in for the italic-as-emphasis we removed from the title.

    color_idx (int) marks one letter to render in `color_alt` — the
    "measurement-chosen" letter, a tiny visual reference to which outcome
    the quantum process picked. Pass None to skip the highlight.
    """
    rnd = random.Random(seed)
    spans = []
    prev_dy = 0.0
    for i, ch in enumerate(text):
        target_dy = (rnd.random() - 0.5) * 2 * drift_y
        delta = target_dy - prev_dy
        prev_dy = target_dy
        attrs = ''
        if color_idx is not None and i == color_idx and color_alt:
            attrs = f' fill="{color_alt}"'
        # Escape XML special chars
        c = ch.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        spans.append(f'<tspan dy="{delta:.3f}"{attrs}>{c}</tspan>')
    return (
        f'<text x="{x}" y="{y}" font-family="{font_family}" font-size="{font_size}" '
        f'fill="{fill}" font-weight="{weight}" letter-spacing="{letter_spacing}">'
        + ''.join(spans) + '</text>'
    )


def ghost_text(x: float, y: float, text: str, font_family: str, font_size: float,
               color: str = OLIVE, offset_x: float = 0.7, offset_y: float = 0.4,
               opacity: float = 0.18, weight: int = 500,
               letter_spacing: float = -0.15) -> str:
    """A faint phantom copy of the title, offset by a fraction of a millimetre.
    Reads as the 'superposition' before measurement — the other outcome that
    the quantum coin didn't land on this time. Place BEFORE the main title.
    """
    return (
        f'<text x="{x + offset_x}" y="{y + offset_y}" font-family="{font_family}" '
        f'font-size="{font_size}" fill="{color}" opacity="{opacity}" '
        f'font-weight="{weight}" letter-spacing="{letter_spacing}">{text}</text>'
    )


# ── FRONT ────────────────────────────────────────────────────────────────
def build_front() -> str:
    """
    Layout (mm):
      [BLEED 3 | trim 85 | BLEED 3]
      Left column: leaf-hexagon logo, 30mm, vertically centered, x≈4..34
      Right column: text block from x≈38..85, two-line title stacked
    """
    """Front: a clean editorial layout.
    - Left column: leaf-hexagon logo, upright, vertically centered.
    - Right column: title, subtitle, divider, contact block — all on a single
      column with conventional left alignment.
    """
    body = []
    body.append(base_layer())

    # A very faint wave-grid stays behind everything as a subtle paper texture.
    body.append(wave_grid(seed=51, x0=BLEED, y0=BLEED, x1=W - BLEED, y1=H - BLEED,
                          step=8.0, amplitude=0.5, color=OLIVE, opacity=0.07, stroke=0.06))

    # ── Logo: upright, vertically centered on the left ──────────────────
    logo_size = 36
    logo_cx = BLEED + 3 + logo_size / 2
    logo_cy = H / 2
    body.append(
        f'<image href="data:image/png;base64,{LOGO_B64}" '
        f'x="{logo_cx - logo_size/2:.2f}" y="{logo_cy - logo_size/2:.2f}" '
        f'width="{logo_size}" height="{logo_size}" '
        f'preserveAspectRatio="xMidYMid meet"/>'
    )

    # Right column geometry
    rx0 = BLEED + 41                            # text column starts at 44mm
    rx1 = W - BLEED - 3                         # text column ends at 85mm

    # ── Title ────────────────────────────────────────────────────────────
    # "Entropic Science" stacked across two lines, both upright, normal weight.
    title_y = BLEED + 18
    title_size = 9.4
    body.append(
        f'<text x="{rx0}" y="{title_y}" font-family="{SERIF}" font-size="{title_size}" '
        f'fill="{PLUM}" font-weight="500" letter-spacing="-0.15">Entropic</text>'
    )
    body.append(
        f'<text x="{rx0}" y="{title_y + 8.6}" font-family="{SERIF}" font-size="{title_size}" '
        f'fill="{PLUM}" font-weight="500" letter-spacing="-0.15">Science</text>'
    )

    # ── Subtitle: research community ────────────────────────────────────
    sub_y = title_y + 14.4
    body.append(
        f'<text x="{rx0}" y="{sub_y}" font-family="{SERIF}" font-style="italic" '
        f'font-size="3.6" fill="{WINE}" letter-spacing="0.02">research community</text>'
    )

    # Divider rule between subtitle and contact block
    rule_y = sub_y + 4.6
    body.append(
        f'<line x1="{rx0}" y1="{rule_y}" x2="{rx0 + 26}" y2="{rule_y}" '
        f'stroke="{OLIVE}" stroke-width="0.22" opacity="0.55"/>'
    )

    # ── Contact block: clean left-aligned column ────────────────────────
    c_y = rule_y + 4.0
    body.append(
        f'<text x="{rx0}" y="{c_y}" font-family="{SERIF}" font-size="3.1" '
        f'fill="{PLUM}" font-weight="500">Ing. Jáchym Fibír, MSc</text>'
    )
    body.append(
        f'<text x="{rx0}" y="{c_y + 3.6}" font-family="{SERIF}" font-size="2.8" '
        f'fill="{WINE}">jachym@entropic.science</text>'
    )
    body.append(
        f'<text x="{rx0}" y="{c_y + 6.8}" font-family="{SERIF}" font-style="italic" '
        f'font-size="2.6" fill="{OLIVE}">entropic.science</text>'
    )

    # Crop marks last
    body.append(trim_marks())

    return svg_open("Entropic Science card — front") + "\n".join(body) + svg_close()


# ── BACK ─────────────────────────────────────────────────────────────────
def build_qr_group(cx: float, cy: float, size: float) -> str:
    """Render the QR with a CLEAN hexagonal cutout centerpiece.

    The cutout is sharp because we draw the QR modules through an SVG mask
    that subtracts a hex polygon — module corners that fall on the hex edge
    are clipped at the hex line, so the resulting hole is a true crisp
    hexagon, not a stepped circle made of square modules.

    The leaf-pattern logo is placed inside the cutout, sized so its visible
    hex matches the cutout hex.
    """
    qr = segno.make(URL, error="h")
    matrix = list(qr.matrix)
    n = len(matrix)
    module = size / n
    x0 = cx - size / 2
    y0 = cy - size / 2

    def in_finder(r: int, c: int) -> bool:
        return (r < 7 and c < 7) or (r < 7 and c >= n - 7) or (r >= n - 7 and c < 7)

    # Hex circumradius (mm). ~22% of QR width keeps us comfortably inside
    # the ~30% masking tolerance for error-correction level H.
    hex_R = size * 0.22
    mask_id = "qrHexCut"
    clip_id = "qrLogoHex"

    parts = []
    # Mask: white = show, black = hide. We hide a hex hole through the modules.
    parts.append(
        f'<defs>'
        f'<mask id="{mask_id}" maskUnits="userSpaceOnUse">'
        f'<rect x="{x0-1:.3f}" y="{y0-1:.3f}" width="{size+2:.3f}" height="{size+2:.3f}" fill="white"/>'
        f'<path d="{hex_path(cx, cy, hex_R)}" fill="black"/>'
        f'</mask>'
        f'<clipPath id="{clip_id}"><path d="{hex_path(cx, cy, hex_R)}"/></clipPath>'
        f'</defs>'
    )

    # All QR modules drawn inside a masked group — the hex hole punches a
    # sharp polygonal cutout through them.
    parts.append(f'<g mask="url(#{mask_id})">')
    for r in range(n):
        for c in range(n):
            if not matrix[r][c]:
                continue
            color = WINE if in_finder(r, c) else PLUM
            parts.append(
                f'<rect x="{x0 + c*module:.3f}" y="{y0 + r*module:.3f}" '
                f'width="{module:.3f}" height="{module:.3f}" fill="{color}"/>'
            )
    parts.append('</g>')

    # The leaf-pattern logo, sized to fill the hex cutout. The PNG's visible
    # hex extends to ~95% horizontally and ~89% vertically of its 407x407
    # frame, so to make the visible hex match a cutout of width=2*hex_R*sqrt(3)/2
    # we scale the image accordingly. Slight oversize + hex clip ensures the
    # leaves reach exactly to the cutout edge with no paper gap.
    logo_size = hex_R * 2.35
    parts.append(
        f'<g clip-path="url(#{clip_id})">'
        f'<image href="data:image/png;base64,{LOGO_B64}" '
        f'x="{cx - logo_size/2:.3f}" y="{cy - logo_size/2:.3f}" '
        f'width="{logo_size:.3f}" height="{logo_size:.3f}" '
        f'preserveAspectRatio="xMidYMid meet"/>'
        f'</g>'
    )
    # Thin crisp outline to articulate the hex edge.
    parts.append(
        f'<path d="{hex_path(cx, cy, hex_R)}" fill="none" '
        f'stroke="{PLUM}" stroke-width="0.20" stroke-opacity="0.55"/>'
    )

    return "<g class=\"qr\">\n  " + "\n  ".join(parts) + "\n  </g>"


def build_back() -> str:
    """Back of the card.

    Left half: the question, drifted across four lines with italic
    quantum-random as the DriftingWord.
    Right half, stacked: SCAN caption on top, QR centered (no bg wash),
    URL below.
    """
    """Back: clean two-column layout.
    - Left column: the question, wrapped naturally across three lines.
    - Right column: SCAN caption, QR with hex cutout, URL — stacked centered.
    - Marginal note in italic at the very bottom of the left column.
    """
    body = []
    body.append(base_layer())

    # A very faint wave-grid as paper texture — nothing else from the noise kit.
    body.append(wave_grid(seed=61, x0=BLEED, y0=BLEED, x1=W - BLEED, y1=H - BLEED,
                          step=8.0, amplitude=0.5, color=OLIVE, opacity=0.07, stroke=0.06))

    # ── Question — three-line wrap, left column, upright with italic emphasis ──
    qx = BLEED + 3
    qy = BLEED + 13
    line_h = 6.4
    fs = 5.6
    body.append(
        f'<text x="{qx}" y="{qy}" font-family="{SERIF}" font-size="{fs}" '
        f'fill="{PLUM}" font-weight="500">'
        f'<tspan x="{qx}" dy="0">Want to chat with a</tspan>'
        f'<tspan x="{qx}" dy="{line_h}" font-style="italic" fill="{WINE}">quantum-random</tspan>'
        f'<tspan x="{qx}" dy="{line_h}">LLM?</tspan>'
        f'</text>'
    )

    # Marginal note — italic, small, lower-left.
    body.append(
        f'<text x="{qx}" y="{H - BLEED - 7.0}" font-family="{SERIF}" font-style="italic" '
        f'font-size="2.5" fill="{PLUM}" opacity="0.65">'
        f'<tspan x="{qx}" dy="0">LLM sampling tokens based on physical</tspan>'
        f'<tspan x="{qx}" dy="2.9">quantum-indeterminate events.</tspan>'
        f'</text>'
    )

    # ── Right column: SCAN caption → QR → URL, vertically stacked, centered ──
    qr_size = 30
    qr_cx = W - BLEED - 2.5 - qr_size / 2
    qr_cy = H / 2 + 0.5

    cap_y = qr_cy - qr_size / 2 - 2.8
    body.append(
        f'<text x="{qr_cx}" y="{cap_y}" text-anchor="middle" '
        f'font-family="{MONO}" font-size="2.0" letter-spacing="0.5" '
        f'fill="{OLIVE}">SCAN TO TRY THE CHATBOT</text>'
    )

    body.append(build_qr_group(qr_cx, qr_cy, qr_size))

    url_y = qr_cy + qr_size / 2 + 3.8
    body.append(
        f'<text x="{qr_cx}" y="{url_y}" text-anchor="middle" '
        f'font-family="{MONO}" font-size="1.95" fill="{WINE}">'
        f'entropic.science/labs/apps/</text>'
    )
    body.append(
        f'<text x="{qr_cx}" y="{url_y + 2.8}" text-anchor="middle" '
        f'font-family="{MONO}" font-size="1.95" fill="{WINE}" opacity="0.85">'
        f'quantum-random-llm-chatbot</text>'
    )

    body.append(trim_marks())
    return svg_open("Entropic Science card — back") + "\n".join(body) + svg_close()


def for_preview(svg: str) -> str:
    s = svg.replace(
        "'EB Garamond','Source Serif 4','TeX Gyre Pagella','Palatino Linotype',serif",
        "'TeX Gyre Pagella','EB Garamond','Source Serif 4','Palatino Linotype',serif",
    )
    s = s.replace(
        "'Space Mono','Nimbus Mono PS','DejaVu Sans Mono',monospace",
        "'Nimbus Mono PS','Space Mono','DejaVu Sans Mono',monospace",
    )
    return s


def main():
    out_dir = "/sessions/pensive-beautiful-davinci/mnt/outputs"

    front_svg = build_front()
    back_svg = build_back()

    with open(f"{out_dir}/front.svg", "w") as f:
        f.write(front_svg)
    with open(f"{out_dir}/back.svg", "w") as f:
        f.write(back_svg)

    DPI = 300
    px_w = int(W * DPI / 25.4)
    cairosvg.svg2png(bytestring=for_preview(front_svg).encode("utf-8"),
                     write_to=f"{out_dir}/front.png",
                     output_width=px_w)
    cairosvg.svg2png(bytestring=for_preview(back_svg).encode("utf-8"),
                     write_to=f"{out_dir}/back.png",
                     output_width=px_w)

    front_pdf = cairosvg.svg2pdf(bytestring=for_preview(front_svg).encode("utf-8"))
    back_pdf = cairosvg.svg2pdf(bytestring=for_preview(back_svg).encode("utf-8"))
    with open(f"{out_dir}/front.pdf", "wb") as f:
        f.write(front_pdf)
    with open(f"{out_dir}/back.pdf", "wb") as f:
        f.write(back_pdf)

    print("Built front.svg/back.svg, front.png/back.png, front.pdf/back.pdf")


if __name__ == "__main__":
    main()
