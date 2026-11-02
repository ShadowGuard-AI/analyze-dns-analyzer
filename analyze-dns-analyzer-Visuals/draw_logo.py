#!/usr/bin/env python3
"""analyze-dns-analyzer logo: one round scooter mirror head on; road and three lamps in the glass."""
import sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter
V1 = "--v1" in sys.argv
W, H = 900, 520
SILVER = (198, 204, 208); FOREST = (14, 26, 20); RED = (216, 36, 30)
img = Image.new("RGB", (W, H), FOREST); d = ImageDraw.Draw(img, "RGBA")
cx, cy, r = 450, 208, 148 if not V1 else 168
# bent stalk and clamp below the mirror
d.line([(cx - 118, 500), (cx - 8, cy + r - 6)], fill=SILVER, width=20)
d.line([(cx - 118, 500), (cx - 8, cy + r - 6)], fill=(96, 102, 106), width=7)
d.rectangle([cx - 140, 478, cx - 94, 506], fill=(120, 128, 132))  # mounting clamp
# rim, autobahn silver, forest black shadow on underside
d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=SILVER)
d.arc([cx - r, cy - r, cx + r, cy + r], 20, 160, fill=(40, 52, 46), width=10)
gr = r - 14
d.ellipse([cx - gr, cy - gr, cx + gr, cy + gr], fill=(188, 202, 202))
# coast road curving away inside the glass
d.polygon([(cx - 96, cy + gr), (cx + 6, cy - 60), (cx + 44, cy - 60), (cx - 8, cy + gr)], fill=(52, 58, 56))
d.line([(cx - 48, cy + 90), (cx + 22, cy - 44)], fill=(236, 236, 230), width=4)
# pale fog wash across the upper glass, a single soft band clipped by the rim curve
d.pieslice([cx - gr + 26, cy - gr + 8, cx + gr - 26, cy - gr + 58], 180, 360, fill=(240, 242, 240, 60))
# three scooter lamps shrinking along the road; nearest is tail light red
lamps = [(cx - 38, cy + 62, 17, RED), (cx + 2, cy + 4, 11, (238, 226, 190)), (cx + 22, cy - 38, 7, (232, 226, 200))]
if V1: lamps = lamps[:1]
for (x, y, s, col) in lamps:
    d.ellipse([x - s, y - s, x + s, y + s], fill=col)
    d.ellipse([x - s * 2, y - s * 2, x + s * 2, y + s * 2], outline=col + (70,), width=3)
# picnic basket strap across lower edge of rim
d.line([(cx - r + 8, cy + r - 40), (cx + r - 8, cy + r - 66)], fill=(132, 104, 66), width=12)
d.line([(cx - r + 8, cy + r - 34), (cx + r - 8, cy + r - 60)], fill=(104, 80, 50), width=3)
try:
    f = ImageFont.truetype(__file__.rsplit("/", 1)[0] + "/fonts/Aubrey.ttf", 44)
except Exception:
    f = ImageFont.load_default()
txt = "analyze-dns-analyzer"
d.text((cx, 428), txt, font=f, fill=SILVER, anchor="mm", stroke_width=0)
img = img.filter(ImageFilter.GaussianBlur(0.3))
out = "scratch/logo-v1.png" if V1 else "logo.png"
img.save(__file__.rsplit("/", 1)[0] + "/" + out)
# 64px legibility check on the shipped version
if not V1:
    img.resize((64, 37)).save(__file__.rsplit("/", 1)[0] + "/scratch/logo64-ship.png")
print("saved", out)
