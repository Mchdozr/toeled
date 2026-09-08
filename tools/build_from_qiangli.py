# -*- coding: utf-8 -*-
"""Mirror qiangliled architecture onto toeled.com with placeholder media/copy."""
from __future__ import annotations

import hashlib
import os
import re
import shutil
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REF = ROOT / "_ref"
SRC = "https://www.qiangliled.com"
OUT = ROOT

PAGES = [
    "",
    "products",
    "commercial-display",
    "rental-staging",
    "dooh",
    "accessories",
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
    "cases",
    "case-commercial-display",
    "case-rental-staging",
    "case-dooh",
    "news",
    "company-news",
    "industry-news",
    "about-us",
    "corporate-culture",
    "certificates-honor",
    "contact-us",
    "debugger",
    "one-click-debug",
    "sales-outlets",
    "service",
    "knowledge",
    "qce-cert-lookup",
]

ASSETS = [
    "/public/wwwroot/css/layout.css?v=1.0.0",
    "/public/wwwroot/css/style.css?v=1.0.0",
    "/public/wwwroot/css/plugin.css",
    "/public/wwwroot/css/swiper-bundle.min.css",
    "/public/wwwroot/js/plugin.js",
    "/public/wwwroot/js/swiper-bundle.min.js",
    "/public/wwwroot/js/countUp.js",
    "/public/wwwroot/js/jquery.waypoints.min.js",
    "/public/wwwroot/js/my-js.js?v=1.0.1",
    "/public/wwwroot/js/share.js",
    "/public/wwwroot/js/qrcode.min.js",
    "/public/wwwroot/plugin/layui/layui.css",
    "/public/wwwroot/plugin/layui/layui.js",
    "/public/wwwroot/plugin/uikit/uikit.min.css?v=1.0.1",
    "/public/wwwroot/plugin/uikit/uikit.min.js",
    "/public/wwwroot/plugin/uikit/uikit-icons.min.js",
    "/public/wwwroot/plugin/map/animate.min.css",
    "/public/wwwroot/plugin/map/base-v1.4.css",
    "/public/wwwroot/plugin/map/main.css",
    "/public/wwwroot/plugin/map/media.css",
    "/public/wwwroot/plugin/map/slick.min.js",
    "/public/wwwroot/plugin/map/anime.min.js",
    "/public/css/validate.css?v=1.0.0",
    "/scripts/sweet/sweetalert.min.js",
    "/scripts/jquery/jquery.form.min.js",
    "/scripts/jquery/Validform_v5.3.2_min.js",
    "/scripts/jquery/jquery.tmpl.min.js",
    "/scripts/jquery/api.js",
]


def fetch(url: str, dest: Path) -> bool:
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists() and dest.stat().st_size > 100:
        return True
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=30) as r:
            dest.write_bytes(r.read())
        print("ok", dest.stat().st_size, dest.relative_to(ROOT))
        return True
    except Exception as e:
        print("fail", url, e)
        return False


def svg_ph(key: str, w=1600, h=900) -> bytes:
    hsh = hashlib.md5(key.encode()).hexdigest()
    c1 = f"#{hsh[:6]}"
    c2 = f"#{hsh[6:12]}"
    label = Path(key).stem[:18]
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
  <defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0%" stop-color="{c1}"/><stop offset="100%" stop-color="{c2}"/>
  </linearGradient></defs>
  <rect width="100%" height="100%" fill="#0b0d12"/>
  <rect width="100%" height="100%" fill="url(#g)" opacity=".45"/>
  <text x="50%" y="48%" fill="#fff" font-family="Microsoft YaHei,Arial" font-size="42" text-anchor="middle">TOELED</text>
  <text x="50%" y="58%" fill="#cfd6e0" font-family="Microsoft YaHei,Arial" font-size="22" text-anchor="middle">{label}</text>
</svg>""".encode("utf-8")


def logo_svg(light=False) -> bytes:
    fill = "#111" if light else "#fff"
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="220" height="48" viewBox="0 0 220 48">
  <text x="0" y="34" font-family="Microsoft YaHei,Arial" font-size="32" font-weight="700" fill="{fill}">TOELED</text>
</svg>""".encode("utf-8")


def transform(html: str) -> str:
    html = html.replace("https://www.qiangliled.com", "")
    html = html.replace("http://www.qiangliled.com", "")
    html = html.replace("www.qiangliled.com", "toeled.com")
    html = html.replace("qiangliled.com", "toeled.com")
    html = html.replace("Qiangli LED", "Toeled")
    html = html.replace("Qiangli Led", "Toeled")
    html = html.replace("Qiangli jucai", "Toeled")
    html = html.replace("Qiangli Jucai", "Toeled")
    html = html.replace("Xiamen Qiangli Jucai opto-Electronic Technology Co.,Ltd.", "Toeled")
    html = html.replace("Xiamen Qiangli Jucai Opto-electronic Technoloy Co., Ltd.", "Toeled")
    html = html.replace("Xiamen Qiangli Jucai Opto-Electronic Technology Co., Ltd.", "Toeled")
    html = html.replace("sales@qiangliled.com", "info@toeled.com")
    html = html.replace("neeraj@qiangliled.com", "info@toeled.com")
    html = re.sub(
        r"<!-- Google tag[\s\S]*?</script>",
        "",
        html,
        flags=re.I,
    )
    html = re.sub(
        r'src="(/public/UserFiles/[^"]+)"',
        lambda m: f'src="{placeholder_path(m.group(1))}"',
        html,
    )
    html = re.sub(
        r"src='(/public/UserFiles/[^']+)'",
        lambda m: f"src='{placeholder_path(m.group(1))}'",
        html,
    )
    html = re.sub(
        r'data-img="(/public/UserFiles/[^"]+)"',
        lambda m: f'data-img="{placeholder_path(m.group(1))}"',
        html,
    )
    html = re.sub(
        r'href="(/public/UserFiles/[^"]+)"',
        lambda m: f'href="{placeholder_path(m.group(1))}"',
        html,
    )
    html = re.sub(
        r'src="(/public/UserFiles/video/[^"]+)"',
        '/public/wwwroot/images/ph-video.svg',
        html,
    )
    html = html.replace("/public/wwwroot/images/logo.png", "/public/wwwroot/images/logo.svg")
    html = html.replace("/public/wwwroot/images/logo10.png", "/public/wwwroot/images/logo10.svg")
    html = html.replace("/public/wwwroot/images/logo-1.png", "/public/wwwroot/images/logo.svg")
    html = html.replace('url="/Feedback/submit"', 'url="#"')
    html = html.replace("G-5VTPD3VL98", "")
    return html


def placeholder_path(src: str) -> str:
    ext = ".svg"
    name = hashlib.md5(src.encode()).hexdigest()[:12] + ext
    rel = f"/public/UserFiles/ph/{name}"
    dest = OUT / rel.lstrip("/")
    dest.parent.mkdir(parents=True, exist_ok=True)
    if not dest.exists():
        dest.write_bytes(svg_ph(src))
    return rel


def collect_local_urls(text: str) -> set[str]:
    urls = set(re.findall(r'(?:url\(|src=|href=)["\']?(/public/wwwroot/[^"\')\s]+)', text))
    urls |= set(re.findall(r'url\((?:["\']?)(/public/wwwroot/plugin/map/[^"\')\s]+)', text))
    return urls


def copy_asset_tree():
    mapping = {
        REF / "public_wwwroot_css_layout.css": OUT / "public/wwwroot/css/layout.css",
        REF / "public_wwwroot_css_style.css": OUT / "public/wwwroot/css/style.css",
        REF / "public_wwwroot_css_plugin.css": OUT / "public/wwwroot/css/plugin.css",
        REF / "public_wwwroot_css_swiper-bundle.min.css": OUT / "public/wwwroot/css/swiper-bundle.min.css",
        REF / "public_wwwroot_plugin_layui_layui.css": OUT / "public/wwwroot/plugin/layui/layui.css",
        REF / "public_wwwroot_plugin_uikit_uikit.min.css": OUT / "public/wwwroot/plugin/uikit/uikit.min.css",
        REF / "public_wwwroot_js_plugin.js": OUT / "public/wwwroot/js/plugin.js",
        REF / "public_wwwroot_js_my-js.js": OUT / "public/wwwroot/js/my-js.js",
        REF / "public_wwwroot_js_countUp.js": OUT / "public/wwwroot/js/countUp.js",
        REF / "assets/public_wwwroot_js_swiper-bundle.min.js": OUT / "public/wwwroot/js/swiper-bundle.min.js",
        REF / "assets/public_wwwroot_js_jquery.waypoints.min.js": OUT / "public/wwwroot/js/jquery.waypoints.min.js",
        REF / "assets/public_wwwroot_plugin_uikit_uikit.min.js": OUT / "public/wwwroot/plugin/uikit/uikit.min.js",
        REF / "assets/public_wwwroot_plugin_uikit_uikit-icons.min.js": OUT / "public/wwwroot/plugin/uikit/uikit-icons.min.js",
        REF / "assets/public_wwwroot_plugin_layui_layui.js": OUT / "public/wwwroot/plugin/layui/layui.js",
        REF / "assets/public_wwwroot_plugin_map_animate.min.css": OUT / "public/wwwroot/plugin/map/animate.min.css",
        REF / "assets/public_wwwroot_plugin_map_base-v1.4.css": OUT / "public/wwwroot/plugin/map/base-v1.4.css",
        REF / "assets/public_wwwroot_plugin_map_main.css": OUT / "public/wwwroot/plugin/map/main.css",
        REF / "assets/public_wwwroot_plugin_map_media.css": OUT / "public/wwwroot/plugin/map/media.css",
        REF / "assets/public_wwwroot_plugin_map_slick.min.js": OUT / "public/wwwroot/plugin/map/slick.min.js",
        REF / "assets/public_wwwroot_plugin_map_anime.min.js": OUT / "public/wwwroot/plugin/map/anime.min.js",
        REF / "assets/public_wwwroot_js_share.js": OUT / "public/wwwroot/js/share.js",
        REF / "assets/public_wwwroot_js_qrcode.min.js": OUT / "public/wwwroot/js/qrcode.min.js",
        REF / "public_css_validate.css": OUT / "public/css/validate.css",
    }
    for src, dest in mapping.items():
        if src.exists():
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dest)


def write_page(slug: str, html: str):
    html = transform(html)
    if slug == "":
        dest = OUT / "index.html"
    else:
        dest = OUT / slug / "index.html"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(html, encoding="utf-8")
    print("page", dest.relative_to(ROOT), dest.stat().st_size)


def main():
    copy_asset_tree()
    img_dir = OUT / "public/wwwroot/images"
    img_dir.mkdir(parents=True, exist_ok=True)
    (img_dir / "logo.svg").write_bytes(logo_svg(False))
    (img_dir / "logo10.svg").write_bytes(logo_svg(True))
    (img_dir / "ph-video.svg").write_bytes(svg_ph("video", 1920, 1080))

    # fetch remaining scripts
    for a in ASSETS:
        rel = a.split("?")[0].lstrip("/")
        fetch(SRC + a, OUT / rel)

    # pages
    html_cache = {}
    home = REF / "home.html"
    if home.exists():
        html_cache[""] = home.read_text(encoding="utf-8", errors="ignore")
    for slug in PAGES:
        if slug == "":
            continue
        local = REF / "pages" / f"{slug}.html"
        dest_tmp = REF / "pages" / f"{slug}.html"
        if not local.exists() or local.stat().st_size < 1000:
            fetch(f"{SRC}/{slug}/", dest_tmp)
        if dest_tmp.exists() and dest_tmp.stat().st_size > 1000:
            html_cache[slug] = dest_tmp.read_text(encoding="utf-8", errors="ignore")

    # UI images from html+css
    urls: set[str] = set()
    for html in html_cache.values():
        urls |= collect_local_urls(html)
    for css in (OUT / "public").rglob("*.css"):
        urls |= collect_local_urls(css.read_text(encoding="utf-8", errors="ignore"))

    for u in sorted(urls):
        if "/UserFiles/" in u:
            continue
        if u.endswith(".svg") and "logo" in u:
            continue
        fetch(SRC + u, OUT / u.lstrip("/"))

    for slug, html in html_cache.items():
        write_page(slug, html)

    # stub missing form scripts
    api = OUT / "scripts/jquery/api.js"
    if not api.exists() or api.stat().st_size < 20:
        api.parent.mkdir(parents=True, exist_ok=True)
        api.write_text("window.api=window.api||{};\n", encoding="utf-8")

    ht = OUT / ".htaccess"
    ht.write_text(
        "DirectoryIndex index.html\nRewriteEngine On\n"
        "RewriteCond %{REQUEST_FILENAME} !-f\n"
        "RewriteCond %{REQUEST_FILENAME} !-d\n"
        "RewriteRule ^(.+)/$ $1/index.html [L]\n",
        encoding="utf-8",
    )
    print("done pages", len(html_cache))


if __name__ == "__main__":
    main()
