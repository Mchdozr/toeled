"""Copy generated assets/{prefix}-{key}.jpg into public series packs."""
from __future__ import annotations

import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASSETS = Path(r"C:\Users\kacma\.cursor\projects\c-Users-kacma-OneDrive-Masa-st-Toeled\assets")
DEST = ROOT / "public" / "wwwroot" / "media" / "series"
KEYS = ("hero", "studio", "feat-1", "feat-2", "feat-3", "feat-4", "use-1", "use-2")
PREFIX = {
    "cms": "cms-series-crystal-film-display",
    "hs": "hs-series-holographic-display",
    "qmini": "q-mini-series",
    "nc": "nc-series",
    "iq": "indoor-q-series",
    "pdc": "pdc-series",
    "mk": "mk-series",
    "ir": "indoor-r-series",
    "cs": "cs-series",
    "n": "n-series",
    "rw": "rw-series",
    "cg": "cg-series",
    "ln": "ln-series",
    "dm": "dm-series",
    "pm": "pm-series",
    "oq": "outdoor-q-series",
    "os": "outdoor-s-series",
    "qm": "qm-series",
    "mg": "mg-series",
    "p": "p-series",
    "v": "v-series-",
}


def main() -> None:
    copied = 0
    missing = []
    for prefix, slug in PREFIX.items():
        folder = DEST / slug
        folder.mkdir(parents=True, exist_ok=True)
        for key in KEYS:
            src = ASSETS / f"{prefix}-{key}.jpg"
            dst = folder / f"{key}.jpg"
            if src.exists():
                shutil.copy2(src, dst)
                copied += 1
            elif not dst.exists():
                missing.append(f"{prefix}-{key}.jpg -> {slug}/{key}.jpg")
    print(f"copied={copied} missing={len(missing)}")
    for row in missing:
        print("MISSING", row)


if __name__ == "__main__":
    main()
