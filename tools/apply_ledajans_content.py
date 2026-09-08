# -*- coding: utf-8 -*-
"""Toeled: LEDAJANS iletişim, TR içerik, görsel ve şirket videosu."""
from __future__ import annotations

import hashlib
import re
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MEDIA = ROOT / "public" / "wwwroot" / "media"
VIDEO = ROOT / "public" / "wwwroot" / "video"

IMAGES = [
    "https://ledajans.com/wp-content/uploads/2026/05/Firefly_Gemini-Flash-8.png",
    "https://ledajans.com/wp-content/uploads/2026/04/hero-poster.webp",
    "https://ledajans.com/wp-content/uploads/2026/04/yesil-proje.png",
    "https://ledajans.com/wp-content/uploads/2026/04/la.png",
    "https://ledajans.com/wp-content/uploads/2026/04/lb.png",
    "https://ledajans.com/wp-content/uploads/2026/04/lb-1.png",
    "https://ledajans.com/wp-content/uploads/2026/03/WhatsApp-Image-2026-03-12-at-11.51.08-AM.jpeg",
    "https://ledajans.com/wp-content/uploads/2026/03/WhatsApp-Image-2026-03-12-at-11.50.55-AM.jpeg",
    "https://ledajans.com/wp-content/uploads/2026/02/DisMekanRGBPanel.png",
    "https://ledajans.com/wp-content/uploads/2026/02/IcMekanRGBPanel.png",
    "https://ledajans.com/wp-content/uploads/2023/01/P1.25-2-scaled.jpg",
    "https://ledajans.com/wp-content/uploads/2023/01/P2.5.jpg",
    "https://ledajans.com/wp-content/uploads/2023/01/P3.jpg",
    "https://ledajans.com/wp-content/uploads/2023/01/PH1.53.jpg",
    "https://ledajans.com/wp-content/uploads/2023/01/ec8726e1-1617-438d-927c-6904cf2506f4.jpg",
    "https://ledajans.com/wp-content/uploads/2023/01/fb8143a3-9d69-45a3-859c-2e2db66c334a.jpg",
    "https://ledajans.com/wp-content/uploads/2026/05/signistanbul-3.png",
    "https://rentalekran.com/wp-content/uploads/2023/11/Firefly_Rental-Led-ekranlar-gosterimde-sergileniyor-547514.png",
    "https://ledajans.com/wp-content/uploads/2024/08/p10-full-out-gkgd.jpg",
    "https://ledajans.com/wp-content/uploads/2024/08/p10-full-out-gkgd2.jpg",
    "https://www.gkgd.com/uploads/media/250108/1-2501081A054H3.jpg",
    "https://www.gkgd.com/uploads/media/250108/1-2501081A1101K.jpg",
]

VIDEO_URL = "https://ledajans.com/wp-content/uploads/2026/03/Firefly-548225-1.mp4"

REPLACEMENTS = [
    ('lang="en"', 'lang="tr"'),
    ("Commercial Display", "İç Mekan"),
    ("Rental &amp; Staging", "Kiralama &amp; Sahne"),
    ("Rental & Staging", "Kiralama &amp; Sahne"),
    (">Product<", ">Ürünler<"),
    (">Products<", ">Ürünler<"),
    (">Case<", ">Referanslar<"),
    (">Support<", ">Destek<"),
    (">News<", ">Haberler<"),
    (">About<", ">Hakkımızda<"),
    (">Contact<", ">İletişim<"),
    (">Contact Us<", ">İletişim<"),
    (">Position<", ">Konum<"),
    ("View More +", "Daha fazla +"),
    ("READ MORE &gt;", "DEVAMINI OKU &gt;"),
    ("Product Zone &gt;", "Ürünler &gt;"),
    ("Excellent Case", "Seçili Referanslar"),
    ("Service and Support", "Hizmet ve Destek"),
    ("Learn more news and information &gt;&gt;", "Tüm haberler &gt;&gt;"),
    ("News Center", "Haber Merkezi"),
    ("Company News", "Kurumsal Haberler"),
    ("Industry News", "Sektör Haberleri"),
    ("Company Profile", "Kurumsal Profil"),
    ("Development History", "Tarihçe"),
    ("Corporate Culture", "Kurum Kültürü"),
    ("Certificates & Honor", "Sertifikalar"),
    ("Certificates &amp; Honor", "Sertifikalar"),
    ("Sales Outlets", "Satış Noktaları"),
    ("One-Click Debug", "Tek Tıkla Destek"),
    ("Knowledge", "Bilgi Merkezi"),
    ("Debugger", "Teknik Destek"),
    ("QCE Cert. Lookup", "Sertifika Sorgulama"),
    ("Accessories", "Aksesuarlar"),
    ("Enter Product Keywords", "Ürün anahtar kelimesi"),
    ("Application Scenarios", "Uygulama Senaryosu"),
    ("Application Area", "Uygulama Alanı"),
    ("Point Spacing", "Piksel Aralığı"),
    ("Case Location", "Proje Konumu"),
    ("Models", "Modeller"),
    ("Introduction", "Tanıtım"),
    ("Parameters", "Teknik Özellikler"),
    ("Pixel Pitch (mm)", "Piksel aralığı (mm)"),
    ("Social networking sites", "Sosyal medya"),
    ("Contact us", "Bize ulaşın"),
    ("Leave your message here and we will reply", "Mesajınızı bırakın, en kısa sürede dönüş yapalım"),
    ("to you shortly", ""),
    ("Name *", "Ad Soyad *"),
    ("Email *", "E-posta *"),
    ("Phone / WhatsApp / Wechat", "Telefon / WhatsApp"),
    ("Message *", "Mesaj *"),
    ("Submit", "Gönder"),
    ("Please enter your name", "Lütfen adınızı yazın"),
    ("Please enter your email", "Lütfen e-posta adresinizi yazın"),
    ("Please leave your needs and suggestions", "Lütfen ihtiyacınızı yazın"),
    ("within 50 characters", "en fazla 50 karakter"),
    ("Email format error", "E-posta formatı hatalı"),
    ("Accept", "Kabul et"),
    ("Decline", "Reddet"),
    ("Privacy Policy", "Gizlilik Politikası"),
    ("Company", "Kurum"),
    ("Indoor Q Series", "İç Mekan Q Serisi"),
    ("Indoor R Series", "İç Mekan R Serisi"),
    ("Outdoor Q Series", "Dış Mekan Q Serisi"),
    ("Outdoor S Series", "Dış Mekan S Serisi"),
    ("CMS Series Crystal Film Display", "CMS Kristal Film Ekran"),
    ("HS Series Holographic Display", "HS Holografik Ekran"),
    ("Q mini Series", "Q Mini Serisi"),
    ("NC Series", "NC Serisi"),
    ("PDC Series", "PDC Serisi"),
    ("MK Series", "MK Serisi"),
    ("CS Series", "CS Serisi"),
    ("N Series", "N Serisi"),
    ("RW Series", "RW Serisi"),
    ("CG Series", "CG Serisi"),
    ("LN Series", "LN Serisi"),
    ("DM Series", "DM Serisi"),
    ("PM Series", "PM Serisi"),
    ("QM Series", "QM Serisi"),
    ("MG Series", "MG Serisi"),
    ("P Series", "P Serisi"),
    ("V Series", "V Serisi"),
    ("Dynamic Energy Saving", "Dinamik enerji tasarrufu"),
    ("Ultrahigh Refresh Rate", "Yüksek yenileme hızı"),
    ("Ultra High Grayscale", "Yüksek gri tonlama"),
    ("Selective Quality", "Seçici kalite"),
    ("We Are Here To Help", "Size yardımcı olmak için buradayız"),
    ("Office Hours", "Mesai saatleri"),
    ("Pre Sales And In Sales Services", "Satış öncesi ve satış süreci"),
    ("On Site Investigation", "Yerinde keşif"),
    ("On Site Installation", "Yerinde kurulum"),
    ("On Site Services", "Yerinde servis"),
    ("Training Guidance", "Eğitim ve yönlendirme"),
    ("System Debugging", "Sistem devreye alma"),
    ("Technical Support Phone Numbers", "Teknik destek hatları"),
    ("Equipment Operation", "Ekipman işletimi"),
    ("Fault Handling", "Arıza müdahalesi"),
    ("Free Training For Personnel", "Personel eğitimi"),
    ("Indoor", "İç mekan"),
    ("Outdoor", "Dış mekan"),
    ("info@toeled.com", "info@ledajans.com"),
    ("sales@qiangliled.com", "info@ledajans.com"),
    ("+86 19044022069", "+90 212 220 40 04"),
    ("+86 18805067936", "+90 212 220 40 04"),
    ("+86 13559263036", "+90 543 879 51 08"),
    ("+86 13695020121", "+90 530 405 67 68"),
    ("0086-188 0506 2056", "+90 212 220 40 04"),
    ("neeraj@qiangliled.com", "info@ledajans.com"),
]


def fetch(url: str, dest: Path) -> bool:
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists() and dest.stat().st_size > 2000:
        return True
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=60) as r:
            dest.write_bytes(r.read())
        print("ok", dest.stat().st_size, dest.name)
        return dest.stat().st_size > 2000
    except Exception as e:
        print("fail", url, e)
        return False


def media_name(url: str) -> str:
    ext = Path(url.split("?")[0]).suffix or ".jpg"
    return hashlib.md5(url.encode()).hexdigest()[:12] + ext


def apply_text(html: str) -> str:
    for a, b in REPLACEMENTS:
        html = html.replace(a, b)
    html = re.sub(
        r"Hey! We like you to know that we use cookies[\s\S]*?see our Gizlilik Politikası\.",
        "Bu sitede deneyiminizi iyileştirmek için çerez kullanıyoruz. Ayrıntılar için Gizlilik Politikası.",
        html,
    )
    html = html.replace(
        "No.5 Yutashi Road, Xiang'an District, Xiamen City, Fujian Province (Toeled LED Display Industrial Park )",
        "Halide Edip Adıvar Mah. Gül 2 Sk. No:10a, 34382 Şişli/İstanbul",
    )
    html = html.replace(
        "Halide Edip Adıvar Mah. Gül 2 Sk. No:10, 34382 Şişli/İstanbul, Türkiye (Toeled LED Display Industrial Park )",
        "Halide Edip Adıvar Mah. Gül 2 Sk. No:10a, 34382 Şişli/İstanbul",
    )
    return html


HOME_ABOUT = """                        <p class="t1 text-line2 " hsm="fadeup">TAHA LED Dış Ticaret A.Ş.<br/>Toeled</p><p class="t2 text-line4" hsm="fadeup">Toeled, LEDAJANS çatısı altında iç ve dış mekan LED ekran satış, kiralama ve kurulum çözümleri sunar. İstanbul, Almanya ve Kıbrıs ofisleriyle keşif, montaj ve teknik desteği aynı standartta yürütürüz.</p><p><a href="/about-us/" class="h-more" hsm="fadeup">
 DEVAMINI OKU &gt; </a></p>"""

STATS = """<div class="card-list-l"><div class="card-item"><h3 class="items-center t1"><span class="a">25</span><span>+</span></h3><p>Yıllık tecrübe</p><div class="bg-card"><h2>25+</h2><span>Yıllık tecrübe</span></div></div><div class="card-item"><h3 class="items-center t1"><span class="a">3</span><span></span></h3><p>Ülke ofisi: Türkiye, Almanya, Kıbrıs</p><div class="bg-card"><h2>3</h2><span>Türkiye, Almanya, Kıbrıs</span></div></div><div class="card-item"><h3 class="items-center t1"><span class="a">2</span><span> yıl</span></h3><p>Parça ve teknik destek garantisi</p><div class="bg-card"><h2>2 yıl</h2><span>Garanti</span></div></div></div><div class="card-list-r"><div class="card-item"><h3 class="items-center t1"><span class="a">7</span><span>/24</span></h3><p>Proje ve saha operasyon desteği</p><div class="bg-card"><h2>7/24</h2><span>Destek</span></div></div><div class="card-item"><h3 class="items-center t1"><span class="a">TR</span><span></span></h3><p>Türkiye geneli kurulum</p><div class="bg-card"><h2>TR</h2><span>Türkiye geneli</span></div></div><div class="card-item"><h3 class="items-center t1"><span class="a">ISO</span><span></span></h3><p>Kalite ve uygunluk belgeleri</p><div class="bg-card"><h2>ISO</h2><span>Belgeler</span></div></div></div>"""

FOOTER_CONTACT = """        <div class="contact-card">
          <div class="contact-item">
            <p class="contact-item-p1">E-posta:</p>
            <p class="contact-item-p2">info@ledajans.com</p>
          </div>
          <div class="contact-item">
            <p class="contact-item-p1">Telefon:</p>
            <p class="contact-item-p2">+90 212 220 40 04 · +90 543 879 51 08 · +90 530 405 67 68</p>
          </div>
          <div class="contact-item">
            <p class="contact-item-p1">Adres:</p>
            <p class="contact-item-p2">TAHA LED Dış Ticaret A.Ş. — Halide Edip Adıvar Mah. Gül 2 Sk. No:10a, 34382 Şişli/İstanbul<br>Almanya: Heinrich-Hertz-Straße 50, 40699 Erkrath · +49 1521 2401915<br>Kıbrıs: Karaoğlanoğlu Cad. Yayla Aktiğin İş Hanı No:6, Girne · +90 533 856 93 71</p>
          </div>
        </div>"""

YOUTUBE_MODAL = """
<div id="toeledVideoModal" class="fix-wrap fix-video" style="display:none;position:fixed;inset:0;background:rgba(0,0,0,.82);z-index:9999;align-items:center;justify-content:center;">
  <div style="position:relative;width:min(960px,92vw);aspect-ratio:16/9;background:#000;">
    <button type="button" id="toeledVideoClose" style="position:absolute;right:-8px;top:-36px;color:#fff;font-size:28px;background:none;border:0;cursor:pointer;">×</button>
    <iframe id="toeledYoutubeFrame" title="Toeled şirket videosu" style="width:100%;height:100%;border:0;" allow="autoplay; encrypted-media" allowfullscreen></iframe>
  </div>
</div>
<script>
$(function(){
  function openV(){
    $('#toeledYoutubeFrame').attr('src','https://www.youtube.com/embed/riOY6kz7cv4?autoplay=1');
    $('#toeledVideoModal').css('display','flex');
  }
  function closeV(){
    $('#toeledVideoModal').hide();
    $('#toeledYoutubeFrame').attr('src','');
  }
  $(document).on('click','.home-play, .js-sirket-video', function(e){ e.preventDefault(); openV(); });
  $('#toeledVideoClose, #toeledVideoModal').on('click', function(e){
    if (e.target === this || $(e.target).is('#toeledVideoClose')) closeV();
  });
});
</script>
"""


def cycle_images(html: str, locals_: list[str]) -> str:
    if not locals_:
        return html
    i = {"n": 0}

    def next_src(_m=None) -> str:
        src = locals_[i["n"] % len(locals_)]
        i["n"] += 1
        return src

    def repl_src(m):
        return f'src="{next_src()}"'

    html = re.sub(r'src="/public/UserFiles/ph/[^"]+"', repl_src, html)
    html = re.sub(r'data-img="/public/UserFiles/ph/[^"]+"', lambda m: f'data-img="{next_src()}"', html)
    html = re.sub(r'href="/public/UserFiles/ph/[^"]+"', lambda m: f'href="{next_src()}"', html)
    return html


def patch_home(html: str, video_rel: str) -> str:
    html = re.sub(
        r'(<video class="home-swiper-video" src=")[^"]+(")',
        rf'\1{video_rel}\2 poster="/public/wwwroot/media/hero-poster.webp"',
        html,
        count=1,
    )
    html = re.sub(
        r'<p class="t1 text-line2 " hsm="fadeup">[\s\S]*?READ MORE[\s\S]*?</a></p>',
        HOME_ABOUT,
        html,
        count=1,
    )
    html = re.sub(
        r'<div class="card-list-l">[\s\S]*?</div></div></div>\s*</div>\s*</div>\s*</div>\s*</div>',
        '<div class="model1-card">' + STATS + "</div>",
        html,
        count=1,
    )
    html = re.sub(
        r'<div class="contact-card">[\s\S]*?</div>\s*</div>\s*</div>\s*<div class="public-footer-num">',
        FOOTER_CONTACT + '\n      </div>\n      <div class="public-footer-num">',
        html,
        count=1,
    )
    html = html.replace(
        '<a href="/about-us/" class="right img-scale img-scale" hsm="fader">',
        '<a href="javascript:;" class="right img-scale img-scale js-sirket-video home-play" hsm="fader">',
        1,
    )
    html = html.replace("</body>", YOUTUBE_MODAL + "\n</body>")
    html = html.replace(
        '<p class="public-footer-num">',
        '<div class="public-footer-num">',
    )
    # map keep 3 offices
    html = html.replace(
        '<p style="font-size: 12px;white-space: nowrap;color: #000;">Istanbul</p>',
        '<p style="font-size: 12px;white-space: nowrap;color: #000;">İstanbul</p>',
    )
    html = html.replace("<p>Istanbul</p>", "<p>İstanbul</p>")
    html = html.replace("<p>Turkey</p>", "<p>Türkiye · Şişli</p>")
    html = html.replace("<p>Chicago</p>", "<p>Erkrath</p>")
    html = html.replace("<p>Korea</p>", "<p>Girne</p>")
    html = html.replace("<p>Indian -North</p>", "<p>İstanbul</p>")
    html = re.sub(
        r'(<div class="he_ghdot"[^>]*data-dotx="5")',
        r'\1 class="he_ghdot la-keep" style="left: 51.2%;top: 37.4%;"',
        html,
        count=1,
    )
    html = re.sub(
        r'(<div class="he_ghdot"[^>]*data-dotx="7")',
        r'\1 class="he_ghdot la-keep"',
        html,
        count=1,
    )
    html = re.sub(
        r'(<div class="he_ghdot"[^>]*data-dotx="8")',
        r'\1 class="he_ghdot la-keep" style="left: 55.4%;top: 43.6%;"',
        html,
        count=1,
    )
    html = html.replace(
        '<div class="he_f1p1nli fl wow g_fadeup1" data-num="5">',
        '<div class="he_f1p1nli fl wow g_fadeup1 la-keep" data-num="5">',
        1,
    )
    html = html.replace(
        '<div class="he_f1p1nli fl wow g_fadeup1" data-num="7">',
        '<div class="he_f1p1nli fl wow g_fadeup1 la-keep" data-num="7">',
        1,
    )
    html = html.replace(
        '<div class="he_f1p1nli fl wow g_fadeup1" data-num="8">',
        '<div class="he_f1p1nli fl wow g_fadeup1 la-keep" data-num="8">',
        1,
    )
    # Chicago card title already replaced via Chicago->Erkrath in dots; list item p Chicago
    html = html.replace("<p>Chicago</p>", "<p>Erkrath</p>")
    html = html.replace("<p>Korea</p>", "<p>Girne</p>")
    html = html.replace(
        "<p>United States</p>",
        "<p>Almanya · +49 1521 2401915</p>",
    )
    html = html.replace("<p>Turkey</p>", "<p>Türkiye · +90 212 220 40 04</p>")
    style = """<style>
.he_ghdot:not(.la-keep){display:none!important}
.he_f1p1nli:not(.la-keep){display:none!important}
.home-play{position:relative;display:block}
.home-play:after{content:'';position:absolute;left:50%;top:50%;width:56px;height:56px;margin:-28px 0 0 -28px;background:url(/public/wwwroot/images/icon-play.png) center/contain no-repeat;z-index:3;pointer-events:none}
</style>
"""
    html = html.replace("</head>", style + "</head>")
    html = html.replace(
        "<p>Copyright &copy; Toeled. All Rights Reserved</p>",
        "<p>Copyright &copy; TAHA LED Dış Ticaret A.Ş. · Toeled. Tüm hakları saklıdır.</p>",
    )
    html = re.sub(
        r"Copyright &copy; Toeled[\s\S]*?All Rights Reserved",
        "Copyright &copy; TAHA LED Dış Ticaret A.Ş. · Toeled. Tüm hakları saklıdır.",
        html,
    )
    return html


def patch_footer_all(html: str) -> str:
    html = re.sub(
        r'<div class="contact-card">[\s\S]*?</div>\s*</div>\s*</div>\s*<div class="public-footer-num">',
        FOOTER_CONTACT + "\n      </div>\n      <div class=\"public-footer-num\">",
        html,
        count=1,
    )
    html = re.sub(
        r"Copyright &copy;[\s\S]*?All Rights Reserved",
        "Copyright &copy; TAHA LED Dış Ticaret A.Ş. · Toeled. Tüm hakları saklıdır.",
        html,
    )
    return html


def main():
    MEDIA.mkdir(parents=True, exist_ok=True)
    VIDEO.mkdir(parents=True, exist_ok=True)
    local_imgs = []
    for url in IMAGES:
        dest = MEDIA / media_name(url)
        if fetch(url, dest):
            local_imgs.append("/public/wwwroot/media/" + dest.name)
    # aliases
    hero = MEDIA / "hero-poster.webp"
    src_hero = MEDIA / media_name("https://ledajans.com/wp-content/uploads/2026/04/hero-poster.webp")
    if src_hero.exists() and not hero.exists():
        hero.write_bytes(src_hero.read_bytes())

    vdest = VIDEO / "sirket.mp4"
    fetch(VIDEO_URL, vdest)
    video_rel = "/public/wwwroot/video/sirket.mp4" if vdest.exists() and vdest.stat().st_size > 10000 else VIDEO_URL

    htmls = [ROOT / "index.html"] + list(ROOT.glob("*/index.html")) + list(ROOT.glob("news/*/index.html"))
    for p in htmls:
        if "_ref" in p.parts:
            continue
        t = p.read_text(encoding="utf-8")
        t = apply_text(t)
        t = cycle_images(t, local_imgs)
        t = patch_footer_all(t)
        if p.name == "index.html" and p.parent == ROOT:
            t = patch_home(t, video_rel)
        p.write_text(t, encoding="utf-8")
        print("html", p.relative_to(ROOT))


if __name__ == "__main__":
    main()
