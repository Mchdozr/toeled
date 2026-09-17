"""HTTP + leftover scan for Toeled quality rebuild."""
from __future__ import annotations

import re
import sys
import urllib.error
import urllib.request
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
BASE = sys.argv[1] if len(sys.argv) > 1 else "http://127.0.0.1:8765"
NS = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
LEFTOVER = re.compile(
    r"Qiangli|9thpanel|GKGD|微软雅黑|Pixel Spacing|Beijing Time|Quanzhou|ChangSha|Xiamen",
    re.I,
)
SKIP_PARTS = {"_ref", "tools", ".git", "node_modules", "plugin"}


def html_pages() -> list[Path]:
    pages = []
    for page in ROOT.rglob("index.html"):
        if any(p in page.parts for p in SKIP_PARTS):
            continue
        if any("qiangli" in p.lower() or "9thpanel" in p.lower() for p in page.parts):
            continue
        pages.append(page)
    return pages


def scan_files() -> list[str]:
    hits = []
    for page in html_pages():
        text = page.read_text(encoding="utf-8", errors="ignore")
        if LEFTOVER.search(text):
            hits.append(str(page.relative_to(ROOT)))
    return hits


def sitemap_paths() -> list[str]:
    tree = ET.parse(ROOT / "sitemap.xml")
    locs = []
    for loc in tree.findall(".//sm:loc", NS):
        url = loc.text or ""
        path = url.replace("https://toeled.com", "") or "/"
        locs.append(path)
    return locs


def fetch(path: str) -> tuple[int, str, str]:
    req = urllib.request.Request(
        BASE + path,
        headers={"User-Agent": "ToeledVerify/1.0"},
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as res:
            body = res.read().decode("utf-8", "ignore")
            title = ""
            m = re.search(r"<title>(.*?)</title>", body, re.I | re.S)
            if m:
                title = re.sub(r"\s+", " ", m.group(1)).strip()
            return res.status, title, body
    except urllib.error.HTTPError as exc:
        return exc.code, "", ""
    except Exception as exc:  # noqa: BLE001
        return 0, str(exc), ""


def main() -> int:
    file_hits = scan_files()
    print(f"HTML leftover files: {len(file_hits)}")
    for h in file_hits:
        print("  HIT", h)

    assets = [
        ROOT / "favicon.ico",
        ROOT / "favicon.svg",
        ROOT / "public/wwwroot/images/logo10.svg",
        ROOT / "public/wwwroot/images/logo.svg",
        ROOT / "public/wwwroot/css/toeled-theme.css",
        ROOT / "public/wwwroot/video/hero-indoor.mp4",
        ROOT / "public/wwwroot/video/hero-rental.mp4",
        ROOT / "public/wwwroot/media/hero-indoor-led.jpg",
    ]
    missing = [str(a.relative_to(ROOT)) for a in assets if not a.exists()]
    print(f"Missing assets: {len(missing)}")
    for m in missing:
        print("  MISS", m)

    paths = sitemap_paths()
    print(f"Sitemap URLs: {len(paths)}")
    bad = 0
    leftover_http = 0
    titles = []
    for path in paths:
        status, title, body = fetch(path)
        ok = status == 200 and title and "Toeled" in title
        if "9thpanel" in body.lower() or "gkgd" in body.lower():
            leftover_http += 1
            ok = False
        if LEFTOVER.search(body) and "redirect" not in title.lower() and "Yönlendiriliyor" not in title:
            leftover_http += 1
            ok = False
        if not ok:
            bad += 1
            print(f"  FAIL {status} {path} {title!r}")
        titles.append(title)
    unique = len(set(titles))
    print(f"HTTP fail: {bad}/{len(paths)}")
    print(f"HTTP leftover pages: {leftover_http}")
    print(f"Unique titles: {unique}/{len(titles)}")

    extra_checks = [
        ("/", ["hero-overlay", "İç Mekan LED Ekran", "hero-indoor.mp4", "favicon.ico"]),
        ("/products/", ["tl-hub-card", "İç Mekan", "Kiralama"]),
        ("/indoor-q-series/", ["İç Mekan Q Serisi", "tl-spec-grid", "Teklif Alın"]),
        ("/cases/", ["İstanbul otel", "tl-case-card", "data-case"]),
        ("/about-us/", ["TAHA LED", "LEDAJANS", "sirket.mp4"]),
        ("/news/", ["ise-2026-toeled-led-ekran"]),
        ("/contact-us/", ["name=\"usage\"", "Teklif alın", "maps"]),
    ]
    extra_fail = 0
    for path, needles in extra_checks:
        _, _, body = fetch(path)
        missing_n = [n for n in needles if n not in body]
        if missing_n:
            extra_fail += 1
            print(f"  CONTENT FAIL {path}: {missing_n}")
        else:
            print(f"  CONTENT OK {path}")

    news_list, _, news_body = fetch("/news/")
    if "qiangli" in news_body.lower() or "9thpanel" in news_body.lower():
        extra_fail += 1
        print("  CONTENT FAIL /news/ still links leftover slugs")
    else:
        print("  CONTENT OK /news/ no leftover slugs")

    print(
        f"SUMMARY leftover_files={len(file_hits)} missing_assets={len(missing)} "
        f"http_fail={bad} extra_fail={extra_fail}"
    )
    return 1 if file_hits or missing or bad or extra_fail else 0


if __name__ == "__main__":
    raise SystemExit(main())
