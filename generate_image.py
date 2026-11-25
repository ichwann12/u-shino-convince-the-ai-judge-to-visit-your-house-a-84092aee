"""Deterministically draw the invitation letter image (1024x1024 PNG).

No network, no wall clock, no randomness. Reads letter.txt from the
repository root and renders it on a warm paper background with a small
hand-drawn house doodle, using only fonts shipped with the system.
"""

import os
import textwrap

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
SIZE = 1024
PAPER = (253, 246, 227)      # warm cream
INK = (43, 33, 24)           # dark brown ink
ACCENT = (176, 92, 44)       # terracotta
SOFT = (122, 96, 66)         # soft brown
ROOF = (176, 92, 44)
WALL = (250, 224, 178)
DOOR = (122, 74, 44)

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SERIF_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF_ITALIC = "/usr/share/fonts/truetype/noto/NotoSerif-Italic.ttf"


def wrap(draw, text, font, max_width):
    """Wrap text to fit max_width, measuring with the real font."""
    lines = []
    for paragraph in text.split("\n"):
        if not paragraph.strip():
            lines.append("")
            continue
        words = paragraph.split()
        current = ""
        for word in words:
            trial = (current + " " + word).strip()
            if draw.textlength(trial, font=font) <= max_width:
                current = trial
            else:
                if current:
                    lines.append(current)
                current = word
        if current:
            lines.append(current)
    return lines


def draw_house(draw):
    """A small friendly house doodle, centred near the top."""
    cx = SIZE // 2
    top = 78
    # sun
    sun_x, sun_y, sun_r = 830, 120, 34
    draw.ellipse([sun_x - sun_r, sun_y - sun_r, sun_x + sun_r, sun_y + sun_r],
                 fill=(244, 196, 84), outline=ACCENT, width=4)
    for angle in range(0, 360, 45):
        import math
        a = math.radians(angle)
        x1 = sun_x + int((sun_r + 10) * math.cos(a))
        y1 = sun_y + int((sun_r + 10) * math.sin(a))
        x2 = sun_x + int((sun_r + 22) * math.cos(a))
        y2 = sun_y + int((sun_r + 22) * math.sin(a))
        draw.line([x1, y1, x2, y2], fill=ACCENT, width=4)
    # chimney smoke: three soft puffs, kept inside the paper frame
    for i, (sx, sy, sr) in enumerate([(cx + 118, top + 10, 11),
                                     (cx + 130, top - 6, 13),
                                     (cx + 144, top - 20, 14)]):
        draw.ellipse([sx - sr, sy - sr, sx + sr, sy + sr],
                     outline=SOFT, width=3)
    # chimney
    draw.rectangle([cx + 92, top + 18, cx + 124, top + 78],
                   fill=(198, 132, 96), outline=INK, width=3)
    # roof
    draw.polygon([(cx - 150, top + 92), (cx + 150, top + 92), (cx, top - 6)],
                 fill=ROOF, outline=INK, width=3)
    # walls
    draw.rectangle([cx - 118, top + 92, cx + 118, top + 212],
                   fill=WALL, outline=INK, width=3)
    # door
    draw.rectangle([cx - 26, top + 140, cx + 26, top + 212],
                   fill=DOOR, outline=INK, width=3)
    draw.ellipse([cx + 12, top + 178, cx + 20, top + 186], fill=(253, 246, 227))
    # windows
    for wx in (cx - 92, cx + 52):
        draw.rectangle([wx, top + 118, wx + 40, top + 158],
                       fill=(186, 222, 235), outline=INK, width=3)
        draw.line([wx + 20, top + 118, wx + 20, top + 158], fill=INK, width=2)
        draw.line([wx, top + 138, wx + 40, top + 138], fill=INK, width=2)
    # ground line
    draw.line([cx - 170, top + 212, cx + 170, top + 212], fill=SOFT, width=3)


def main():
    with open(os.path.join(HERE, "letter.txt"), encoding="utf-8") as f:
        letter = f.read().strip()

    img = Image.new("RGB", (SIZE, SIZE), PAPER)
    draw = ImageDraw.Draw(img)

    # double paper frame
    draw.rectangle([28, 28, SIZE - 28, SIZE - 28], outline=ACCENT, width=4)
    draw.rectangle([44, 44, SIZE - 44, SIZE - 44], outline=SOFT, width=2)

    draw_house(draw)

    title_font = ImageFont.truetype(SERIF_BOLD, 66)
    title = "You're Invited!"
    tw = draw.textlength(title, font=title_font)
    draw.text(((SIZE - tw) / 2, 322), title, font=title_font, fill=INK)
    draw.line([220, 412, SIZE - 220, 412], fill=ACCENT, width=4)
    draw.ellipse([SIZE // 2 - 6, 406, SIZE // 2 + 6, 418], fill=ACCENT)

    body_font = ImageFont.truetype(SERIF, 42)
    margin = 112
    max_width = SIZE - 2 * margin
    lines = wrap(draw, letter, body_font, max_width)
    line_height = 66
    y = 452
    for line in lines:
        if line.startswith("—"):
            sign_font = ImageFont.truetype(SERIF_ITALIC, 42)
            draw.text((margin, y), line, font=sign_font, fill=INK)
        else:
            draw.text((margin, y), line, font=body_font, fill=INK)
        y += line_height

    ps_font = ImageFont.truetype(SERIF_ITALIC, 36)
    ps = "P.S. The kettle is already on — and the good chair is saved for you."
    ps_lines = wrap(draw, ps, ps_font, max_width)
    y += 30
    for line in ps_lines:
        draw.text((margin, y), line, font=ps_font, fill=ACCENT)
        y += 52

    out = os.path.join(HERE, "entry.png")
    img.save(out, format="PNG")
    print("wrote", out, os.path.getsize(out), "bytes")


if __name__ == "__main__":
    main()
