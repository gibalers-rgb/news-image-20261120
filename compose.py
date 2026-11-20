#!/usr/bin/env python3
"""Compose entry.png for make.fun news-image-20261120.

Builds a 1024x1024 newspaper-front-page infographic summarising the world news
of Friday 20 November 2026: an AI-generated hero illustration (no text) on top,
six story cards with PIL-rendered text below, so every word is sharp and legible.
Run: python3 compose.py  -> writes entry.png next to this file.
"""
import textwrap
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
NAVY = (22, 35, 63)
GOLD = (201, 162, 39)
CREAM = (247, 243, 234)
PAPER = (255, 253, 247)
INK = (24, 28, 38)
MUTED = (90, 96, 110)

HERO = "assets/media-generation-hero-globe-0-1f158335-d323-4c95-a949-20985cf86f90.png"

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

STORIES = [
    ("POLITICS · SHENZHEN", (31, 93, 140), "SUMMIT OF THREE POWERS",
     "Trump, Xi and Putin meet for the first time — and sign a joint peace declaration."),
    ("JUSTICE · THE HAGUE", (122, 63, 84), "GENOCIDE RULING",
     "World Court finds Myanmar guilty of genocide against the Rohingya people."),
    ("TECH · NEW YORK", (14, 122, 102), "ANTHROPIC GOES PUBLIC",
     "First frontier AI firm lists on Nasdaq; shares close 17% above the IPO price."),
    ("MARKETS · TOKYO", (176, 84, 24), "ASIA MARKETS PLUNGE",
     "Nikkei falls 4.8% on AI-bubble fears; Taiwan's index sheds 2,200 points."),
    ("WAR · LONDON", (90, 60, 120), "DRONES FOR UKRAINE",
     "UK pledges 1,000+ long-range drones for Kyiv in a £260 million package."),
    ("CLIMATE · UN SUMMIT", (46, 110, 58), "COP31: FOSSIL FUELS CUT",
     "Fossil fuels dropped from the draft deal on the summit's final day."),
]


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def main():
    img = Image.new("RGB", (W, H), CREAM)
    d = ImageDraw.Draw(img)

    # --- Masthead ---
    d.rectangle([0, 0, W, 96], fill=NAVY)
    d.rectangle([0, 96, W, 100], fill=GOLD)
    title_f = font(SERIF_B, 46)
    date_f = font(SANS_B, 25)
    title = "THE WORLD IN ONE DAY"
    date = "FRIDAY · 20 NOVEMBER 2026"
    d.text(((W - d.textlength(title, font=title_f)) / 2, 10), title,
           font=title_f, fill=(247, 243, 234))
    d.text(((W - d.textlength(date, font=date_f)) / 2, 62), date,
           font=date_f, fill=(216, 178, 74))

    # --- Hero banner ---
    hero = Image.open(HERO).convert("RGB")
    hero = hero.resize((W, 341), Image.LANCZOS)
    img.paste(hero, (0, 100))
    d = ImageDraw.Draw(img)
    d.rectangle([0, 437, W, 441], fill=GOLD)

    # --- Story cards: 2 cols x 3 rows ---
    margin, gutter = 24, 16
    cw = (W - 2 * margin - gutter) // 2
    ch = 162
    top = 454
    tag_f = font(SANS_B, 15)
    head_f = font(SANS_B, 25)
    sum_f = font(SANS, 17)
    for i, (tag, color, head, summ) in enumerate(STORIES):
        col, row = i % 2, i // 2
        x = margin + col * (cw + gutter)
        y = top + row * (ch + 12)
        d.rounded_rectangle([x, y, x + cw, y + ch], radius=10,
                            fill=PAPER, outline=(210, 205, 190), width=1)
        d.rectangle([x, y + 8, x + 6, y + ch - 8], fill=color)
        tx = x + 20
        # number badge
        d.ellipse([x + cw - 42, y + 12, x + cw - 12, y + 42], fill=color)
        num_f = font(SANS_B, 18)
        num = str(i + 1)
        d.text((x + cw - 27 - d.textlength(num, font=num_f) / 2, y + 15),
               num, font=num_f, fill=(255, 255, 255))
        d.text((tx, y + 12), tag, font=tag_f, fill=color)
        hl = wrap(d, head, head_f, cw - 40)
        hy = y + 38
        for ln in hl[:2]:
            d.text((tx, hy), ln, font=head_f, fill=INK)
            hy += 30
        sl = wrap(d, summ, sum_f, cw - 40)
        sy = hy + 4
        for ln in sl[:2]:
            d.text((tx, sy), ln, font=sum_f, fill=MUTED)
            sy += 23

    # --- Footer ---
    foot_f = font(SANS, 15)
    foot = "Six stories that defined the day — reported 20 November 2026 · BBC · Le Monde · AP"
    d.text(((W - d.textlength(foot, font=foot_f)) / 2, 990), foot,
           font=foot_f, fill=MUTED)

    img.save("entry.png", optimize=True)
    print("wrote entry.png", img.size)


if __name__ == "__main__":
    main()
