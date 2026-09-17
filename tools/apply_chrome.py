"""Apply shared head/footer chrome to every live index.html."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

THEME = '<link rel="stylesheet" href="/public/wwwroot/css/toeled-theme.css?v=2.3.0">'
FAVICONS = """<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="icon" type="image/x-icon" href="/favicon.ico">
<link rel="apple-touch-icon" href="/favicon.svg">
<link rel="shortcut icon" href="/favicon.ico" />"""

GTAG_RE = re.compile(
    r"<script>\s*window\.dataLayer[\s\S]*?gtag\('config', ''\);\s*</script>",
    re.I,
)
TITLE_RE = re.compile(r"<title>.*?</title>", re.I | re.S)
DESC_RE = re.compile(r'<meta\s+name="Description"[^>]*>', re.I)
KEYS_RE = re.compile(r'<meta\s+name="Keywords"[^>]*>', re.I)
CANON_RE = re.compile(r'<link\s+rel="canonical"[^>]*>', re.I)
SHORTCUT_RE = re.compile(r'<link\s+rel="shortcut icon"[^>]*>', re.I)
ICON_RE = re.compile(r'<link\s+rel="icon"[^>]*>', re.I)
APPLE_RE = re.compile(r'<link\s+rel="apple-touch-icon"[^>]*>', re.I)
THEME_RE = re.compile(r'<link[^>]+toeled-theme\.css[^>]*>', re.I)
MOTION_RE = re.compile(
    r'(<link rel="stylesheet" href="/public/wwwroot/css/motion\.css[^>]*>)',
    re.I,
)
SOCIAL_RE = re.compile(
    r'<div class="public-footer-site">Sosyal medya</div>'
    r'<div class="icon-b items-center">.*?</div>',
    re.S,
)
QR_RE = re.compile(r'<div class="public-footer-code">.*?</div>', re.S)
CSRF_RE = re.compile(r'<input type="hidden" name="csrf_token"[^>]*>')


PAGE_META = {
    "/": (
        "Toeled | LED Ekran Satış Kiralama Kurulum",
        "İç mekan, dış mekan ve rental LED ekran çözümleri. LEDAJANS çatısında keşif, kurulum ve 2 yıl teknik destek.",
    ),
    "/products/": (
        "LED Ekran Ürünleri | Toeled",
        "İç mekan, kiralama, dış mekan ve aksesuar LED ekran serilerini tek katalogda inceleyin.",
    ),
    "/commercial-display/": (
        "İç Mekan LED Ekran | Toeled",
        "Fine pitch, COB ve kristal film iç mekan LED ekran serileri. Showroom, ofis ve perakende.",
    ),
    "/rental-staging/": (
        "Rental LED Ekran Kiralama | Toeled",
        "Konser, fuar ve sahne için hızlı kurulan rental LED kabin serileri.",
    ),
    "/dooh/": (
        "Dış Mekan LED Ekran | Toeled",
        "Yüksek parlaklık DOOH, billboard ve stadyum LED ekran çözümleri.",
    ),
    "/accessories/": (
        "LED Kabin ve Aksesuar | Toeled",
        "QM, MG, P ve V serisi LED kabin, güç ve montaj aksesuarları.",
    ),
    "/cases/": (
        "LED Ekran Referansları | Toeled",
        "İstanbul, Almanya ve Kıbrıs LED ekran uygulamaları: lobi, sahne, cephe.",
    ),
    "/case-commercial-display/": (
        "İç Mekan LED Referansları | Toeled",
        "Otel, ofis ve perakende iç mekan LED ekran projeleri.",
    ),
    "/case-rental-staging/": (
        "Sahne ve Fuar LED Referansları | Toeled",
        "Konser, lansman ve fuar standı rental LED ekran uygulamaları.",
    ),
    "/case-dooh/": (
        "Dış Mekan LED Referansları | Toeled",
        "Billboard, medya cephe ve stadyum LED ekran referansları.",
    ),
    "/about-us/": (
        "Hakkımızda | Toeled LED Ekran",
        "TAHA LED Dış Ticaret A.Ş. / Toeled, LEDAJANS çatısında LED ekran satış ve kurulum.",
    ),
    "/corporate-culture/": (
        "Kurum Kültürü | Toeled",
        "Keşif, doğru ürün, kurulum ve servis odaklı Toeled çalışma ilkeleri.",
    ),
    "/certificates-honor/": (
        "Sertifikalar | Toeled LED Ekran",
        "ISO ve uygunluk belgelerimiz. Kalite ve güvenlik standartları.",
    ),
    "/news/": (
        "Haberler | Toeled LED Ekran",
        "LED ekran seçimi, kiralama, fuar ve showroom duyuruları.",
    ),
    "/company-news/": (
        "Kurumsal Haberler | Toeled",
        "Toeled ve LEDAJANS duyuruları, fuar ve showroom haberleri.",
    ),
    "/industry-news/": (
        "Sektör Haberleri | Toeled",
        "İç mekan, rental ve dış mekan LED ekran rehberleri.",
    ),
    "/contact-us/": (
        "Teklif Alın | Toeled İletişim",
        "LED ekran keşif ve fiyat teklifi için İstanbul ofisi, WhatsApp ve form.",
    ),
    "/service/": (
        "Servis ve Garanti | Toeled",
        "Keşif, kurulum, 2 yıl parça-işçilik ve 7/24 saha desteği.",
    ),
    "/sales-outlets/": (
        "Satış Noktaları | Toeled",
        "İstanbul, Erkrath ve Girne ofisleri. LEDAJANS satış ağı.",
    ),
    "/knowledge/": (
        "Bilgi Merkezi | Toeled",
        "LED ekran kurulum, kullanım ve bakım rehberleri.",
    ),
    "/debugger/": (
        "Teknik Destek | Toeled",
        "Uzaktan teşhis ve saha desteği için Toeled teknik form.",
    ),
    "/one-click-debug/": (
        "Tek Tıkla Destek | Toeled",
        "Arıza kaydı açın, uzman ekibimiz aynı gün dönüş yapsın.",
    ),
    "/qce-cert-lookup/": (
        "Sertifika Bilgisi | Toeled",
        "Ürün uygunluk ve kalite belgelerine hızlı erişim.",
    ),
}


def url_of(page: Path) -> str:
    rel = page.parent.relative_to(ROOT)
    if rel == Path("."):
        return "/"
    return "/" + rel.as_posix().strip("/") + "/"


def apply_chrome(html: str, url: str, title: str, desc: str) -> str:
    html = TITLE_RE.sub(f"<title>{title}</title>", html, count=1)
    if DESC_RE.search(html):
        html = DESC_RE.sub(f'<meta name="Description" content="{desc}" />', html, count=1)
    else:
        html = html.replace("</title>", f'</title>\n  <meta name="Description" content="{desc}" />', 1)
    html = KEYS_RE.sub(
        '<meta name="Keywords" content="Toeled, LED ekran, LEDAJANS, rental LED, iç mekan LED" />',
        html,
        count=1,
    )
    if CANON_RE.search(html):
        html = CANON_RE.sub(f'<link rel="canonical" href="https://toeled.com{url}">', html, count=1)
    html = GTAG_RE.sub("", html)
    html = ICON_RE.sub("", html)
    html = APPLE_RE.sub("", html)
    html = SHORTCUT_RE.sub(FAVICONS, html, count=1)
    if "favicon.svg" not in html:
        html = html.replace("</title>", "</title>\n" + FAVICONS, 1)
    if THEME_RE.search(html):
        html = THEME_RE.sub(THEME, html, count=1)
    else:
        html, n = MOTION_RE.subn(r"\1\n" + THEME, html, count=1)
        if n == 0:
            html = html.replace("</head>", THEME + "\n</head>", 1)
    if 'property="og:title"' not in html:
        og = (
            f'<meta property="og:title" content="{title}">\n'
            f'<meta property="og:description" content="{desc}">\n'
            f'<meta property="og:type" content="website">\n'
            f'<meta property="og:url" content="https://toeled.com{url}">\n'
            f'<meta property="og:image" content="https://toeled.com/public/wwwroot/media/hero-indoor-led.jpg">'
        )
        html = html.replace("</title>", "</title>\n" + og, 1)
    html = SOCIAL_RE.sub("", html)
    html = QR_RE.sub("", html)
    html = CSRF_RE.sub("", html)
    html = html.replace("/9thpanel.ico", "/favicon.ico")
    return html


def extra_fields(html: str) -> str:
    if 'name="usage"' in html:
        return html
    block = """
        <div class="contact-msg justify-between" hsm="fadeup">
          <div class="contact-msg-i items-center">
            <span>Şirket</span>
            <input class="inputs" type="text" name="company" maxlength="80">
          </div>
          <div class="contact-msg-i items-center">
            <span>Kullanım</span>
            <select class="inputs" name="usage">
              <option value="">Seçin</option>
              <option>İç mekan</option>
              <option>Dış mekan</option>
              <option>Kiralama &amp; Sahne</option>
              <option>DOOH</option>
            </select>
          </div>
        </div>
        <div class="contact-msg-i items-center" style="width: 100%;" hsm="fadeup">
          <span>Yaklaşık ölçü</span>
          <input class="inputs" type="text" name="size" placeholder="ör. 4 x 2,5 m" maxlength="80">
        </div>
"""
    needle = '<div class="contact-msg-i items-center" style="width: 100%;" hsm="fadeup">\n          <span>Telefon / WhatsApp'
    if needle in html:
        html = html.replace(needle, block + needle, 1)
    btn = re.compile(r"(>Gönder\s*</button>|>Teklif Alın\s*</button>)")
    html = btn.sub(">Teklif Alın</button>", html)
    return html


def main() -> None:
    changed = 0
    skip_parts = ("_ref", "tools", "tests", ".superdesign")
    for page in ROOT.rglob("index.html"):
        if any(p in page.parts for p in skip_parts):
            continue
        if any("qiangli" in p.lower() or "9thpanel" in p.lower() for p in page.parts):
            continue
        url = url_of(page)
        text = page.read_text(encoding="utf-8")
        if url in PAGE_META:
            title, desc = PAGE_META[url]
            updated = extra_fields(apply_chrome(text, url, title, desc))
        elif THEME_RE.search(text):
            updated = extra_fields(THEME_RE.sub(THEME, text, count=1))
        else:
            updated = extra_fields(text)
        if updated != text:
            page.write_text(updated, encoding="utf-8", newline="\n")
            changed += 1
    print(f"chrome updated {changed} files")


if __name__ == "__main__":
    main()
