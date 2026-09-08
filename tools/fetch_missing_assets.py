# -*- coding: utf-8 -*-
import re
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = "https://www.qiangliled.com"


def fetch(url: str, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists() and dest.stat().st_size > 50:
        return
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=25) as r:
            dest.write_bytes(r.read())
        print("ok", dest.stat().st_size, dest.relative_to(ROOT).as_posix())
    except Exception as e:
        print("fail", url, e)


def main():
    for css in ROOT.joinpath("public").rglob("*.css"):
        text = css.read_text(encoding="utf-8", errors="ignore")
        for raw in re.findall(r"url\((?:['\"]?)([^)'\"]+)", text):
            if raw.startswith("data:") or raw.startswith("http"):
                continue
            path = (css.parent / raw.split("?")[0]).resolve()
            try:
                rel = path.relative_to(ROOT).as_posix()
            except ValueError:
                continue
            fetch(SRC + "/" + rel, path)

    extras = [
        "/public/wwwroot/images/img-hp1.png",
        "/9thpanel.ico",
        "/favicon.ico",
        "/public/wwwroot/plugin/layui/font/iconfont.woff2",
        "/public/wwwroot/plugin/layui/font/iconfont.woff",
        "/public/wwwroot/plugin/layui/font/iconfont.ttf",
        "/public/wwwroot/plugin/layui/font/iconfont.eot",
        "/public/wwwroot/plugin/layui/font/iconfont.svg",
    ]
    for u in extras:
        fetch(SRC + u, ROOT / u.lstrip("/"))


if __name__ == "__main__":
    main()
