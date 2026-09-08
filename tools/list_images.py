# -*- coding: utf-8 -*-
import re
import urllib.request
from pathlib import Path

ROOT = Path(r"C:\Users\kacma\AppData\Local\Temp\site-scan")
skip = ("logo", "favicon", "icon", "kacmasa", "ledarabul", "colorglight", "-550x", "-300x", "-150x", "powersupply", "untitled")
pat = re.compile(r"https://(?:ledajans|rentalekran)\.com/wp-content/uploads/[^\"']+\.(?:jpg|jpeg|png|webp)", re.I)
out = []
for p in ROOT.glob("*.html"):
    t = p.read_text(encoding="utf-8", errors="ignore")
    for u in pat.findall(t):
        if not any(s in u.lower() for s in skip):
            out.append(u)
uniq = sorted(set(out))
Path(r"C:\Users\kacma\OneDrive\Masaüstü\Toeled\tools\image_urls.txt").write_text("\n".join(uniq), encoding="utf-8")
print(len(uniq))
for u in uniq:
    print(u)
