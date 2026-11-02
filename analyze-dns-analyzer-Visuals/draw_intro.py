#!/usr/bin/env python3
"""analyze-dns-analyzer intro: Vespa club scramble at dawn, scenery only, no text.
Foreground mirror reflecting a fogged road curve, swarm at rest in double file, sea and headland."""
import math, random, sys
from PIL import Image, ImageDraw, ImageFilter
random.seed(11)
V1 = "--v1" in sys.argv
W, H = 1200, 520
FOG = (232, 236, 233); SILVER = (198, 204, 208); FOREST = (18, 32, 24); RED = (206, 34, 30)
img = Image.new("RGB", (W, H), FOG); d = ImageDraw.Draw(img, "RGBA")
# pale early sky, top quarter
for y in range(0, 130):
    t = y / 130; d.line([(0, y), (W, y)], fill=(int(226 - 8*t), int(232 - 6*t), int(230 + 4*t)))
# far headland, flat forest black shape, right side beyond sea
d.polygon([(760, 128), (960, 96), (1200, 118), (1200, 168), (760, 168)], fill=(30, 46, 38))
# sea, flat and pale, right
d.rectangle([700, 168, W, 300], fill=(196, 208, 208))
for _ in range(40):
    x, y = random.uniform(720, 1180), random.uniform(180, 290); d.line([(x, y), (x + random.uniform(14, 44), y)], fill=(214, 224, 222), width=1)
# stone verge left of road
d.polygon([(0, 168), (700, 168), (700, 300), (0, 330)], fill=(168, 170, 160))
for _ in range(260):
    x, y = random.uniform(0, 680), random.uniform(176, 320); d.point((x, y), fill=random.choice([(148, 150, 140), (186, 188, 178)]))
# ground strip closing the gap under the sea and verge, drawn before the road so the road sits on it
d.rectangle([0, 296, W, 432], fill=(150, 152, 144))
# coast road: dark strip sweeping from midground to foreground
d.polygon([(330, 250), (620, 250), (900, 520), (120, 520)], fill=(42, 46, 44))
d.polygon([(330, 250), (620, 250), (640, 268), (352, 268)], fill=(58, 62, 60))
for i in range(9):  # broken centre line, perspective
    t = i / 9; y = 268 + t * 240; x = 470 + t * 90; wdt = 4 + t * 10
    d.line([(x, y), (x + 6 + t * 18, y + 16)], fill=(232, 232, 226), width=int(wdt * 0.55))
# fog lying in the hollow, midground band, soft and behind the swarm
for i in range(14):
    x, y = random.uniform(240, 820), random.uniform(218, 252)
    d.ellipse([x, y, x + random.uniform(110, 220), y + random.uniform(12, 22)], fill=(238, 240, 238, 55))
def scooter(x, y, s, flip=1):
    """Small scooter side view: leg shield, saddle, two wheels, mirror dot, basket."""
    d.ellipse([x - 13*s, y + 8*s, x - 3*s, y + 18*s], outline=(24, 28, 26), width=max(1, int(2.4*s)))  # rear wheel
    d.ellipse([x + 12*s, y + 8*s, x + 22*s, y + 18*s], outline=(24, 28, 26), width=max(1, int(2.4*s)))  # front wheel
    d.polygon([(x + 4*s, y + 12*s), (x + 14*s, y - 14*s), (x + 20*s, y - 12*s), (x + 17*s, y + 12*s)], fill=(112, 128, 120))  # leg shield
    d.rectangle([x - 12*s, y - 6*s, x + 6*s, y - 1*s], fill=(52, 58, 54))  # saddle
    d.rectangle([x - 20*s, y - 12*s, x - 11*s, y - 3*s], outline=(96, 84, 62), width=max(1, int(2*s)))  # picnic basket
    for cx in (x - 19*s, x - 15*s, x - 12*s):
        d.line([(cx, y - 12*s), (cx, y - 3*s)], fill=(140, 124, 92), width=1)
    d.ellipse([x - 4*s, y - 18*s, x + 6*s, y - 9*s], fill=(70, 76, 72))  # rider torso hint, no marks
    d.line([(x + 15*s, y - 13*s), (x + 20*s, y - 22*s)], fill=SILVER, width=max(1, int(1.8*s)))  # mirror stalk
    d.ellipse([x + 17*s, y - 27*s, x + 24*s, y - 20*s], fill=SILVER, outline=(90, 96, 100))  # mirror glass point of light
    d.point((x - 14*s, y + 2*s), fill=RED)  # tail lamp
    if random.random() < 0.8:
        d.ellipse([x - 15*s, y + 3*s, x - 11*s, y + 7*s], fill=RED)  # tail lamp glow block
# swarm at rest, loose double file along the road
rows = [(0.55, 264), (0.66, 282), (0.78, 302), (0.92, 326), (1.08, 354)]
for (s, y) in rows:
    for k in range(4):
        scooter(360 + k * 78 * s + random.uniform(-5, 5), y + random.uniform(-3, 3), s)
        if V1 and k > 1: break
# foreground: tarmac at wheel height, damp edges
d.rectangle([0, 430, W, H], fill=(52, 56, 54))
for _ in range(900):
    x, y = random.uniform(0, W), random.uniform(430, H); d.point((x, y), fill=random.choice([(66, 70, 68), (44, 48, 46)]))
d.polygon([(0, 430), (W, 430), (W, 448), (0, 452)], fill=(88, 94, 92, 120))  # damp sheen
# THE foreground mirror, lower left, dominating
mx, my, mr = 204, 342, 104
d.line([(mx - 30, my + 96), (mx + 6, my + 34)], fill=SILVER, width=16)  # bent stalk
d.line([(mx - 30, my + 96), (mx + 6, my + 34)], fill=(90, 96, 100), width=5)
d.ellipse([mx - 44, my + 88, mx - 10, my + 112], fill=(70, 76, 80))  # mounting clamp
d.ellipse([mx - mr, my - mr, mx + mr, my + mr], fill=(160, 168, 172))  # rim
d.ellipse([mx - mr + 10, my - mr + 10, mx + mr - 10, my + mr - 10], fill=(206, 216, 216))  # glass
# reflected blurred curve of road inside the glass
clip = Image.new("L", (W, H), 0); cd = ImageDraw.Draw(clip); cd.ellipse([mx - mr + 12, my - mr + 12, mx + mr - 12, my + mr - 12], fill=255)
refl = Image.new("RGB", (W, H), (206, 216, 216)); rd = ImageDraw.Draw(refl)
rd.polygon([(mx - 100, my + 60), (mx + 10, my - 80), (mx + 52, my - 80), (mx - 20, my + 90)], fill=(70, 76, 74))
rd.line([(mx - 56, my + 40), (mx + 22, my - 60)], fill=(238, 238, 232), width=5)
rd.ellipse([mx - 62, my + 18, mx - 34, my + 42], fill=(226, 70, 60))  # red lamp glow one
rd.ellipse([mx + 28, my - 48, mx + 48, my - 30], fill=(226, 90, 78))  # red lamp glow two
refl = refl.filter(ImageFilter.GaussianBlur(5))
img.paste(refl, (0, 0), clip); d = ImageDraw.Draw(img, "RGBA")
d.ellipse([mx - mr, my - mr, mx + mr, my + mr], outline=SILVER, width=7)
d.line([(mx - mr + 4, my + mr - 34), (mx + mr - 4, my + mr - 52)], fill=(120, 84, 60), width=9)  # picnic basket strap across lower rim
img = img.filter(ImageFilter.GaussianBlur(0.4))
out = "scratch/intro-v1.png" if V1 else "intro-banner.png"
img.save(__file__.rsplit("/", 1)[0] + "/" + out); print("saved", out)
