#!/usr/bin/env python3
"""analyze-dns-analyzer wordmark banner: dawn coast road bend, swarm, oversized foreground mirror,
name painted in Aubrey in autobahn silver on the lead scooter leg shield only."""
import math, random, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter
random.seed(23)
V1 = "--v1" in sys.argv
W, H = 1200, 420
SILVER = (198, 204, 208); FOREST = (18, 32, 24); RED = (206, 34, 30)
img = Image.new("RGB", (W, H), (228, 233, 231)); d = ImageDraw.Draw(img, "RGBA")
for y in range(0, 110):
    d.line([(0, y), (W, y)], fill=(226, 232, 230))
d.rectangle([820, 108, W, 250], fill=(194, 206, 206))  # sea flat and pale, right
d.polygon([(880, 108), (1040, 84), (1200, 100), (1200, 140), (880, 140)], fill=(34, 50, 42))  # headland
d.polygon([(0, 150), (1200, 130), (1200, 420), (0, 420)], fill=(44, 48, 46))  # tarmac bend
d.polygon([(0, 150), (560, 140), (760, 250), (360, 420), (0, 420)], fill=(52, 56, 54))  # left hand bend sweep
for i in range(10):
    t = i / 10; x = 90 + t * 700; y = 380 - t * 190
    d.line([(x, y), (x + 30, y - 16)], fill=(234, 234, 228), width=max(2, int(3 + t * 2)))
# headland redrawn above the road line on the right, then fog in the dip ahead, soft
d.polygon([(920, 108), (1050, 86), (1200, 100), (1200, 132), (920, 138)], fill=(34, 50, 42))
for i in range(12):
    x, y = random.uniform(640, 1020), random.uniform(128, 196)
    d.ellipse([x, y, x + random.uniform(110, 220), y + 20], fill=(240, 242, 240, 55))
def scooter(x, y, s, lead=False):
    d.ellipse([x - 14*s, y + 9*s, x - 3*s, y + 20*s], outline=(20, 24, 22), width=max(1, int(3*s)))
    d.ellipse([x + 13*s, y + 9*s, x + 24*s, y + 20*s], outline=(20, 24, 22), width=max(1, int(3*s)))
    d.polygon([(x + 3*s, y + 13*s), (x + 15*s, y - 16*s), (x + 22*s, y - 13*s), (x + 18*s, y + 13*s)], fill=(126, 142, 132) if not lead else (92, 116, 104))
    d.rectangle([x - 13*s, y - 7*s, x + 7*s, y - 1*s], fill=(50, 56, 52))
    d.rectangle([x - 22*s, y - 13*s, x - 12*s, y - 3*s], outline=(100, 86, 62), width=max(1, int(2*s)))  # basket
    d.line([(x - 22*s, y - 8*s), (x - 12*s, y - 8*s)], fill=(216, 210, 190), width=max(1, int(2*s)))  # checked cloth lift
    d.ellipse([x - 5*s, y - 20*s, x + 6*s, y - 10*s], fill=(72, 78, 74))
    d.line([(x + 16*s, y - 14*s), (x + 22*s, y - 25*s)], fill=SILVER, width=max(1, int(2*s)))
    d.ellipse([x + 19*s, y - 30*s, x + 27*s, y - 22*s], fill=(226, 232, 232), outline=(100, 106, 110))  # mirror point of light
    d.ellipse([x - 16*s, y + 2*s, x - 11*s, y + 7*s], fill=RED)
    d.line([(x - 10*s, y + 20*s), (x - 30*s, y + 27*s)], fill=(24, 28, 26, 110), width=max(1, int(3*s)))  # long dawn shadow
# swarm pouring around the bend
for i in range(14 if not V1 else 6):
    t = i / 14; x = 620 - t * 430 + math.sin(i * 2.1) * 26; y = 168 + t * 150; s = 0.55 + t * 0.95
    scooter(x, y, s)
# lead scooter, large, lower left, name painted on its leg shield
scooter(150, 300, 2.6, lead=True)
try:
    f = ImageFont.truetype(__file__.rsplit("/", 1)[0] + "/fonts/Aubrey.ttf", 15)
except Exception:
    f = ImageFont.load_default()
# the lead machine leg shield itself, redrawn at perspective size, name painted on it in silver
d.polygon([(166, 334), (202, 230), (250, 238), (240, 334)], fill=(70, 92, 84))
d.text((209, 254), "analyze", font=f, fill=SILVER, anchor="mm")
d.text((209, 276), "dns", font=f, fill=SILVER, anchor="mm")
d.text((209, 298), "analyzer", font=f, fill=SILVER, anchor="mm")
# oversized foreground mirror, right foreground, reflected lamps at changing spacing
mx, my, mr = 1020, 300, 92
d.line([(mx + 30, my + 110), (mx + 4, my + 40)], fill=SILVER, width=13)
d.ellipse([mx - mr, my - mr, mx + mr, my + mr], fill=SILVER)
d.ellipse([mx - mr + 9, my - mr + 9, mx + mr - 9, my + mr - 9], fill=(204, 214, 214))
d.polygon([(mx - 70, my + 70), (mx + 4, my - 60), (mx + 34, my - 60), (mx - 6, my + 80)], fill=(64, 70, 68))
for (lx, ly, ls) in [(mx - 44, my + 36, 11), (mx - 28, my + 16, 8), (mx + 14, my - 28, 6), (mx + 26, my - 44, 5)]:
    d.ellipse([lx - ls, ly - ls, lx + ls, ly + ls], fill=(228, 80, 66) if ls > 9 else (240, 230, 196))
img = img.filter(ImageFilter.GaussianBlur(0.4))
out = "scratch/banner-v1.png" if V1 else "banner.png"
img.save(__file__.rsplit("/", 1)[0] + "/" + out); print("saved", out)
