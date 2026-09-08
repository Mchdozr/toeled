# -*- coding: utf-8 -*-
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
p = ROOT / "about-us" / "index.html"
t = p.read_text(encoding="utf-8")
start = "visual intelligent display effects"
end = "200+engineering distributors</p></div></div>"
i = t.find(start)
j = t.find(end)
if i != -1 and j != -1:
    t = t[:i] + t[j + len(end) :]
    t = t.replace(
        "</p></div><div class=\"left-type",
        "</p></div><div class=\"left-type",
        1,
    )
    block = (
        '</p></div><div class="left-type flex-wrap justify-between hsms ov">'
        '<div class="left-type-i items-center" hsm="fadel"><img src="/public/wwwroot/images/icon-cp1.png" alt=""/><p class="t1">25+ yıl tecrübe</p></div>'
        '<div class="left-type-i items-center" hsm="fadel"><img src="/public/wwwroot/images/icon-cp2.png" alt=""/><p class="t1">Türkiye, Almanya, Kıbrıs</p></div>'
        '<div class="left-type-i items-center" hsm="fadel"><img src="/public/wwwroot/images/icon-cp3.png" alt=""/><p class="t1">Türkiye geneli kurulum</p></div>'
        '<div class="left-type-i items-center" hsm="fadel"><img src="/public/wwwroot/images/icon-cp4.png" alt=""/><p class="t1">2 yıl garanti</p></div>'
        '<div class="left-type-i items-center" hsm="fadel"><img src="/public/wwwroot/images/icon-cp5.png" alt=""/><p class="t1">ISO belgeler</p></div>'
        '<div class="left-type-i items-center" hsm="fadel"><img src="/public/wwwroot/images/icon-cp6.png" alt=""/><p class="t1">Keşif, kurulum, servis</p></div></div>'
    )
    t = t.replace(
        '</p></div><div class="left-type flex-wrap justify-between hsms ov">',
        block,
        1,
    )
    p.write_text(t, encoding="utf-8")
    print("about patched")
else:
    print("about markers missing", i, j)

fixes = [
    ("cookieKabul eted", "cookieAccepted"),
    ("DOOH", "Dış Mekan"),
    ("Product Zone >", "Ürünler >"),
    ("sales@toeled.com", "info@ledajans.com"),
    ('<p class="t1">Phone</p>', '<p class="t1">Telefon</p>'),
    ('<p class="t1">Address</p>', '<p class="t1">Adres</p>'),
    ('<p class="t1">Email</p>', '<p class="t1">E-posta</p>'),
]
n = 0
for f in ROOT.rglob("*.html"):
    if "_ref" in f.parts:
        continue
    s = f.read_text(encoding="utf-8")
    o = s
    for a, b in fixes:
        s = s.replace(a, b)
    if s != o:
        f.write_text(s, encoding="utf-8")
        n += 1
print("files", n)
