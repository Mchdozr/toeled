# -*- coding: utf-8 -*-
import re
import urllib.request
from pathlib import Path

OUT = Path(r"C:\Users\kacma\AppData\Local\Temp\site-scan")
OUT.mkdir(exist_ok=True)
urls = [
    "https://ledajans.com/",
    "https://ledajans.com/hakkimizda/",
    "https://ledajans.com/projeler/",
    "https://rentalekran.com/",
    "https://www.gkgd.com/",
    "https://www.gkgd.com/cases",
]
img_re = re.compile(r"https?://[^\"'\s>]+\.(?:jpg|jpeg|png|webp|mp4)(?:\?[^\"'\s>]*)?", re.I)
vid_re = re.compile(r"youtube|youtu\.be|mp4|vimeo", re.I)
found_img = []
found_vid = []
for u in urls:
    try:
        req = urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"})
        html = urllib.request.urlopen(req, timeout=25).read().decode("utf-8", "ignore")
        (OUT / (u.replace("https://", "").replace("/", "_") + ".html")).write_text(html, encoding="utf-8")
        found_img += img_re.findall(html)
        if vid_re.search(html):
            found_vid += [m.group(0) for m in re.finditer(r"(https?://[^\"'\s>]*(?:youtube|youtu\.be|vimeo)[^\"'\s>]*)|(?:src|href)=[\"']([^\"']+\.mp4[^\"']*)", html, re.I)]
        print("ok", u, len(html), "imgs", len(img_re.findall(html)))
    except Exception as e:
        print("fail", u, e)
print("VID")
for v in found_vid[:40]:
    print(v)
print("IMG SAMPLE")
for i in sorted(set(found_img))[:60]:
    print(i)
