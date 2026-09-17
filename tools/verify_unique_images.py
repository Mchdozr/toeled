"""Ensure each series pack uses unique image paths (no shared feat/hero across series)."""
from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SLUGS = [
    "cms-series-crystal-film-display",
    "hs-series-holographic-display",
    "q-mini-series",
    "nc-series",
    "indoor-q-series",
    "pdc-series",
    "mk-series",
    "indoor-r-series",
    "cs-series",
    "n-series",
    "rw-series",
    "cg-series",
    "ln-series",
    "dm-series",
    "pm-series",
    "outdoor-q-series",
    "outdoor-s-series",
    "qm-series",
    "mg-series",
    "p-series",
    "v-series-",
]
KEYS = ("hero", "studio", "feat-1", "feat-2", "feat-3", "feat-4", "use-1", "use-2")
SRC_RE = re.compile(r'src="(/public/wwwroot/media/[^"]+)"')


def main() -> int:
    errors: list[str] = []
    owners: dict[str, list[str]] = defaultdict(list)
    for slug in SLUGS:
        folder = ROOT / "public" / "wwwroot" / "media" / "series" / slug
        for key in KEYS:
            path = folder / f"{key}.jpg"
            if not path.exists() or path.stat().st_size < 10_000:
                errors.append(f"missing/small {slug}/{key}.jpg")
            rel = f"/public/wwwroot/media/series/{slug}/{key}.jpg"
            owners[rel].append(f"{slug}:{key}")
        page = ROOT / slug / "index.html"
        if not page.exists():
            errors.append(f"missing page {slug}/index.html")
            continue
        html = page.read_text(encoding="utf-8", errors="ignore")
        feat_srcs = re.findall(
            r'class="tl-pdp-feat-media".*?<img src="([^"]+)"',
            html,
            re.I | re.S,
        )
        if len(feat_srcs) < 4:
            errors.append(f"{slug} tanitim imgs={len(feat_srcs)}")
        elif len(set(feat_srcs)) < 4:
            errors.append(f"{slug} repeated tanitim {feat_srcs}")
        gal = re.findall(r'tl-pdp-gal-i" href="([^"]+)"', html)
        if len(gal) >= 4 and len(set(gal[:4])) < 4:
            errors.append(f"{slug} gallery repeat {gal[:4]}")
        for src in SRC_RE.findall(html):
            if "/series/" in src:
                owners[src].append(f"html:{slug}")
    for src, uses in owners.items():
        series_hits = sorted({u.split(":")[0].replace("html:", "") for u in uses if "series" in u or True})
        slugs_using = sorted({
            u.split(":")[0].replace("html:", "")
            for u in uses
        })
        unique_slugs = {s for s in slugs_using if s in SLUGS}
        if len(unique_slugs) > 1 and "/series/" in src:
            errors.append(f"shared path {src} -> {sorted(unique_slugs)}")
    print(f"errors={len(errors)}")
    for row in errors[:40]:
        print(row)
    if len(errors) > 40:
        print(f"... {len(errors) - 40} more")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
