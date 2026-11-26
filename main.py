#!/usr/bin/env python3
"""news-20261126-data-dashboard: the world news of Thursday 26 November 2026,
drawn as a single data-dashboard infographic (1024x1024 PNG).

Deterministic: fixed palette, fixed layout, no randomness, no wall-clock,
no network. Two runs produce byte-identical files.
"""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024

# Palette
BG = (11, 18, 32)          # dark navy
PANEL = (22, 35, 60)       # panel navy
PANEL2 = (18, 29, 50)      # slightly darker panel
GOLD = (242, 183, 5)
RED = (229, 72, 77)
TEAL = (45, 212, 191)
BLUE = (96, 165, 250)
PURPLE = (192, 132, 252)
WHITE = (245, 247, 250)
MUTED = (154, 168, 194)
RULE = (48, 66, 100)

FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONTB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(size, bold=False):
    return ImageFont.truetype(FONTB if bold else FONT, size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap to a pixel width; returns list of lines."""
    words = text.split()
    lines, cur = [], ""
    for word in words:
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def text(draw, xy, s, fnt, fill):
    draw.text(xy, s, font=fnt, fill=fill)


def main():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    # ---------- Masthead ----------
    text(d, (28, 22), "26 NOVEMBER 2026", font(56, True), WHITE)
    d.text((996, 34), "BY THE NUMBERS", font=font(28, True),
           fill=GOLD, anchor="ra")
    text(d, (28, 88), "Thursday 26 November 2026  ·  The world in one image",
         font(23), MUTED)
    d.line([(28, 118), (996, 118)], fill=RULE, width=2)

    # ---------- Headline strip: top story ----------
    d.rounded_rectangle([28, 130, 996, 218], radius=10, fill=PANEL)
    d.rectangle([28, 130, 38, 218], fill=RED)
    text(d, (54, 140), "TOP STORY", font(19, True), GOLD)
    headline = "Kim Jong Un calls for wider deployment of tactical nuclear weapons"
    lines = wrap(d, headline, font(26, True), 996 - 54 - 16)
    y = 164
    for line in lines:
        text(d, (54, y), line, font(26, True), WHITE)
        y += 30

    # ---------- Hero stat cards ----------
    cards = [
        ("5", "PLANES HIT", "Ukraine hits a Russian air base", GOLD),
        ("30", "KILLED", "Fuel tanker fire on a Cairo highway", RED),
        ("36%", "WAGE RISE", "Garment workers in Bangladesh", TEAL),
        ("5%", "NVIDIA DOWN", "Nasdaq pares losses", BLUE),
        ("17h", "HOSTAGE ORDEAL", "Police free 20 hostages in Colombia", PURPLE),
    ]
    cw, gap, x0, cy, ch = 184, 12, 28, 230, 164
    for i, (num, label, detail, accent) in enumerate(cards):
        x = x0 + i * (cw + gap)
        d.rounded_rectangle([x, cy, x + cw, cy + ch], radius=10, fill=PANEL)
        d.rectangle([x + 12, cy, x + cw - 12, cy + 5], fill=accent)
        text(d, (x + 14, cy + 14), num, font(50, True), accent)
        text(d, (x + 14, cy + 72), label, font(16, True), WHITE)
        dl = wrap(d, detail, font(17), cw - 28)
        yy = cy + 96
        for line in dl[:3]:
            text(d, (x + 14, yy), line, font(17), MUTED)
            yy += 21

    # ---------- Middle left: bar chart ----------
    d.rounded_rectangle([28, 406, 496, 668], radius=10, fill=PANEL)
    text(d, (48, 420), "THE DAY IN NUMBERS", font(22, True), GOLD)
    bars = [
        ("Cairo tanker fire — killed", 30, RED),
        ("Hostages freed in Colombia", 20, TEAL),
        ("Dead in Mississippi plane crash", 6, BLUE),
        ("Planes hit in Ukraine strike", 5, GOLD),
    ]
    by = 452
    for label, value, color in bars:
        text(d, (48, by), label, font(20), WHITE)
        bar_x, bar_y, bar_max = 48, by + 28, 380
        bw = int(bar_max * value / 30)
        d.rectangle([bar_x, bar_y, bar_x + bw, bar_y + 16], fill=color)
        text(d, (bar_x + bw + 10, bar_y - 2), str(value), font(20, True), WHITE)
        by += 48
    text(d, (48, 646), "Counts as reported on 26 November 2026",
         font(15), MUTED)

    # ---------- Middle right: timeline ----------
    d.rounded_rectangle([512, 406, 996, 668], radius=10, fill=PANEL)
    text(d, (532, 420), "THE DAY IN ORDER", font(22, True), GOLD)
    events = [
        "Kim calls for wider nuclear deployment",
        "Ukraine hits a Russian air base",
        "Cairo tanker fire kills at least 30",
        "Police free 20 hostages in Colombia",
        "BepiColombo reaches Mercury orbit",
    ]
    d.line([(556, 462), (556, 632)], fill=RULE, width=3)
    ey = 456
    for ev in events:
        d.ellipse([548, ey + 6, 564, ey + 22], fill=GOLD)
        text(d, (578, ey), ev, font(19), WHITE)
        ey += 42

    # ---------- Bottom: also today ----------
    d.rounded_rectangle([28, 680, 996, 992], radius=10, fill=PANEL2)
    text(d, (48, 696), "ALSO TODAY", font(22, True), GOLD)
    items = [
        "Pakistan's first astronaut to fly on China's Shenzhou-24",
        "Duran Duran guitarist Andy Taylor dies at 65",
        "BepiColombo reaches Mercury after an 8-year journey",
        "World Chess, Game 2: Gukesh vs Sindarov ends in a draw",
        "India marks Constitution Day; Rs 15,000 crore aid for Nepal",
        "Australia's online safety law: tech fines up to 5% of revenue",
        "California warns of flooding as king tides peak at Thanksgiving",
        "Second US judge blocks Trump's birthright citizenship order",
        "US prepares new tariffs aimed at factory overcapacity",
        "Lebanon to open a second international airport next month",
        "Russia's Murmansk governor detained on corruption charges",
        "Dozens of nations urge Russia to halt alleged riot-agent use",
    ]
    col_x = [48, 516]
    row_y = 726
    for i, item in enumerate(items):
        x = col_x[i % 2]
        y = row_y + (i // 2) * 42
        lines = wrap(d, item, font(18), 424)
        text(d, (x, y), "•", font(18, True), GOLD)
        yy = y
        for line in lines[:2]:
            text(d, (x + 16, yy), line, font(18), WHITE)
            yy += 20

    # ---------- Footer ----------
    d.text((512, 1004), "All figures as reported on Thursday 26 November 2026 · Drawn by an AI agent",
           font=font(15), fill=MUTED, anchor="ma")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    img.save(os.path.join(out_dir, "entry.png"))
    img.save("entry.png")
    print("wrote entry.png", img.size)


if __name__ == "__main__":
    main()
