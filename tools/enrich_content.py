"""Fill thin product and support pages with fuller Turkish copy + visuals."""
from __future__ import annotations

from apply_chrome import PAGE_META
from apply_quality_rebuild import (
    M,
    SERIES,
    NEWS,
    CASES,
    banner,
    crumbs,
    quote,
    set_main,
    write_page,
)
from series_extra import EXTRA, pack

ROOT = __import__("pathlib").Path(__file__).resolve().parents[1]


def faq(items: list[tuple[str, str]]) -> str:
    rows = "".join(
        f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in items
    )
    return f'<h2>Sık sorulanlar</h2><div class="tl-faq">{rows}</div>'


def split(img: str, alt: str, title: str, paras: list[str], reverse: bool = False) -> str:
    cls = "tl-split reverse" if reverse else "tl-split"
    body = "".join(f"<p>{p}</p>" for p in paras)
    slug = (
        title.lower()
        .replace("ı", "i")
        .replace("ş", "s")
        .replace("ğ", "g")
        .replace("ü", "u")
        .replace("ö", "o")
        .replace("ç", "c")
        .replace(" ", "-")
    )
    return (
        f'<div class="{cls}"><div><h2 id="{slug}">{title}</h2>{body}</div>'
        f'<img src="{img}" alt="{alt}"></div>'
    )


def guides(items: list[tuple[str, str, str, str]]) -> str:
    cards = "".join(
        f'<a class="tl-guide-card" href="{href}"><img src="{img}" alt="{title}">'
        f'<div class="copy"><h3>{title}</h3><p>{text}</p></div></a>'
        for img, title, text, href in items
    )
    return f'<div class="tl-guide-grid">{cards}</div>'


def toc(items: list[tuple[str, str]]) -> str:
    links = "".join(f'<a href="#{i}">{t}</a>' for i, t in items)
    return f'<nav class="tl-toc" aria-label="İçindekiler">{links}</nav>'


def table(headers: list[str], rows: list[list[str]]) -> str:
    th = "".join(f"<th>{h}</th>" for h in headers)
    trs = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return (
        f'<div class="tl-table-wrap"><table class="tl-table"><thead><tr>{th}</tr></thead>'
        f"<tbody>{trs}</tbody></table></div>"
    )


def checks(items: list[str]) -> str:
    lis = "".join(f"<li>{x}</li>" for x in items)
    return f'<ul class="tl-checks">{lis}</ul>'


def related_cards(items: list) -> str:
    if not items:
        return ""
    cards = "".join(
        f'<a class="tl-guide-card" href="/{s["slug"]}/"><img src="{s["hero"]}" alt="{s["title"]}">'
        f'<div class="copy"><h3>{s["title"]}</h3><p>{s["pitch"]} — {s["lead"]}</p></div></a>'
        for s in items
    )
    return f'<h2>İlgili seriler</h2><div class="tl-guide-grid">{cards}</div>'


CAT_MORE = {
    "indoor": [
        "İç mekan parlaklığı ofis ve toplantıda düşük, lobi ve vitrinde daha yüksek tutulur. 7/24 duvarda gece profili, pixel shift ve ısınma derating’i teklife ayrı satır olarak yazılır.",
        "Ön bakımlı kabin dar koridoru kurtarır; arka servis için yaklaşık 80 cm boşluk şarttır. Native çözünürlük slayt ve videoyu piksel-eşler; ölçeklenmiş 4K fine pitch’te yumuşar.",
        "Şişli showroom’da aynı içeriği farklı pitch’te yan yana izlemek teklifi hızlandırır. Q, Mini, NC COB ve CMS film randevuyla canlıdır; ölçü krokinizi getirmeniz yeter.",
    ],
    "rental": [
        "Rental işi sabit duvardan ayrı speclenir: kilit pimi, eğim takozu, flight case adedi ve yüzde 5–10 yedek modül load-in öncesi sayılır. Aynı gece kurulum-söküm penceresi sözleşmenin ilk maddesidir.",
        "İç mekân konser ve TV’de 2.6–2.9 mm, açık hava ve festivalde 3.9 mm sınıfı öne çıkar. Jeneratör gücü, truss yükü ve yağmur planı keşif formuna işlenir.",
        "Yedek PSU, yedek alıcı kart ve yedek kilit pimi saha çantasında durur. Tur işlerinde Erkrath lojistiği Avrupa ayağını, İstanbul stok Türkiye ayağını taşır.",
    ],
    "outdoor": [
        "Dış mekânda nit, IP ve kabin ısısı fiyatı belirler. Güney cephe gündüz yüksek parlaklık ister; tünel ve gece ağırlıklı yayın daha düşük profille çözülür.",
        "Belediye izin, rüzgâr yükü, ankraj ve arka koridor bakımı keşif tutanağının parçasıdır. Uzaktan yayın için fiber veya yedekli SIM ve izleme yazılımı ayrı kalem olabilir.",
        "MG 320×160 ve Outdoor Q/S cadde billboard ile medya cephede yaygındır. Stadyum peri-led’de tribün mesafesi 5–8 mm sınıfını seçtirir.",
    ],
    "acc": [
        "Aksesuar teklifi ekran satırından ayrı yazılır: kabin adedi, PSU yedeği, konnektör ve askı seti. Mevcut duvar genişletmede uyum keşifte doğrulanır.",
        "7/24 işlerde N+1 güç kaynağı, rentalde hot-swap modül oranı ayrı satırdır. İstanbul stok aynı gün kargo veya saha bırakmayı mümkün kılar.",
        "QM ince kasa duvar kalınlığını, V dikey totem yüksekliğini, P serisi güç ve kabloyu tamamlar. Statik yük mimara iletilir.",
    ],
}


def _feat_html(p) -> str:
    if isinstance(p, (list, tuple)):
        return "".join(f"<p>{x}</p>" for x in p)
    return f"<p>{p}</p>"


def series_main(s: dict) -> str:
    extra = EXTRA.get(s["slug"], {})
    slug = s["slug"]
    gal_imgs = extra.get("gallery") or [
        pack(slug, "hero"),
        pack(slug, "studio"),
        pack(slug, "feat-1"),
        pack(slug, "use-1"),
    ]
    gallery = "".join(
        f'<div class="swiper-slide"><a class="product-swiper-i" href="{img}">'
        f'<img src="{img}" alt="{s["title"]}"></a></div>'
        for img in gal_imgs[:4]
    )
    feats_src = extra.get("feats") or s["feats"]
    feats = []
    for i, item in enumerate(feats_src):
        if len(item) < 3:
            raise SystemExit(f"feat missing unique img: {slug} {item[0]}")
        h, p, img = item[0], item[1], item[2]
        side = "fadel" if i % 2 == 0 else "fader"
        feats.append(
            f'<div class="product-model1"><div class="row"><div class="row-i">'
            f'<div class="product-model1-left" hsm="{side}"><div class="product-model1-title items-center">'
            f'<span></span><p class="t1"><strong>{h}</strong></p></div>'
            f'<div class="product-model1-info">{_feat_html(p)}</div></div>'
            f'<div class="product-model1-right img-scale"><img src="{img}" alt="{h}"></div>'
            f"</div></div></div>"
        )
    specs_src = extra.get("specs") or s["specs"]
    specs = "".join(f"<div><span>{k}</span><strong>{v}</strong></div>" for k, v in specs_src)
    body = list(extra.get("body") or [s["lead"]])
    body_html = "".join(f"<p>{p}</p>" for p in body)
    uses = extra.get("uses") or [
        (pack(slug, "use-1"), "Saha kullanımı", s["lead"]),
        (pack(slug, "use-2"), "Kurulum", s["lead"]),
        (pack(slug, "hero"), s["title"], s["lead"]),
    ]
    use_html = ""
    if uses:
        cards = "".join(
            f'<div class="tl-guide-card"><img src="{img}" alt="{t}">'
            f'<div class="copy"><h3>{t}</h3><p>{d}</p></div></div>'
            for img, t, d in uses
        )
        use_html = f'<div class="tl-prose"><h2 id="kullanim">Nerede kullanılır?</h2><div class="tl-guide-grid">{cards}</div></div>'
    peers = [x for x in SERIES if x["catu"] == s["catu"] and x["slug"] != s["slug"]][:3]
    faqs = extra.get(
        "faq",
        [
            (f"{s['title']} hangi pitch ile gelir?", f"Teknik tablodaki aralık geçerlidir: {s['pitch']}. Keşifte izleme mesafesi ölçülüp netleşir."),
            ("Kurulum ve garanti nasıl işler?", "Keşif, montaj ve teslim eğitimi LEDAJANS saha ekibiyle yürür. Sabit işlerde 2 yıl parça-işçilik; rentalde proje bazlı servis."),
            ("Teklif için ne gerekir?", "Yaklaşık ölçü, iç/dış/rental seçimi ve izleme mesafesi yeter. Form veya WhatsApp +90 212 220 40 04."),
            ("Showroom’da bu seriyi görebilir miyim?", "Şişli’de fine pitch, kristal film ve rental kabinler randevuyla canlıdır. +90 212 220 40 04."),
            ("Yedek parça nerede durur?", "İstanbul stok. Erkrath ve Girne işlerinde sevkiyat teklifte görünür."),
            ("İçerik çözünürlüğü nasıl ayarlanır?", "Ekranın native piksel sayısına export edin. Ölçeklenmiş 4K fine pitch’te yumuşar; işlemci girişi keşifte yazılır."),
        ],
    )
    split_img = pack(slug, "studio")
    return f"""
{crumbs([("/products/", "Ürünler"), (s["catu"], s["catn"]), ("", s["title"])])}
<div class="product-b">
  <div class="product-b-top ov">
    <div class="product-b-top-info hsms">
      <h1 class="t1" hsm="fadeup">{s["title"]}</h1>
      <div class="swiper product-swiper" hsm="fadeup">
        <div class="swiper-wrapper" uk-lightbox>{gallery}</div>
        <div class="swiper-pagination"></div>
      </div>
      <div class="t2" hsm="fadeup">{body_html}
      <p><strong>Piksel aralığı:</strong> {s["pitch"]}</p></div>
    </div>
  </div>
  <div class="product-b-type"><div class="row hsms">
    <a class="product-b-type-i cur" href="#i1" data-offset="220" uk-scroll>Tanıtım</a>
    <a class="product-b-type-i" href="#kullanim" data-offset="220" uk-scroll>Kullanım</a>
    <a class="product-b-type-i" href="#kesif" data-offset="220" uk-scroll>Keşif</a>
    <a class="product-b-type-i" href="#i2" data-offset="220" uk-scroll>Teknik Özellikler</a>
  </div></div>
  <div class="product-model1" style="padding-bottom:0"><div class="row">
    <h3 class="product-title" id="i1">Tanıtım</h3></div></div>
  {"".join(feats)}
  {use_html}
  <div class="tl-prose">
    {split(split_img, s["title"] + " keşif", "Keşifte netleşenler", [
        f"{s['title']} teklifi ölçü, izleme mesafesi, güç noktası ve servis yönü olmadan kilitlenmez. {s['catn']} ailesinde kabin ve kontrol aynı tutanakta toplanır.",
        "Foto ve kroki aynı gün yeter; Şişli showroom’da örnek izlemek pitch kararını hızlandırır. Teslimde operatör eğitimi ve 2 yıl garanti maddesi imzalanır.",
    ])}
    <h2 id="kesif">Teklif öncesi kontrol</h2>
    {checks([
        "En × boy ve izleme mesafesi",
        "İç / dış / rental senaryosu",
        "Güç panosu, toprak ve varsa UPS",
        "Askı, duvar veya zemin sehpa",
        "Ön veya arka bakım koridoru",
        "Native içerik çözünürlüğü",
        "Yedek modül / PSU oranı",
        "Kurulum penceresi ve teslim eğitimi",
    ])}
    {related_cards(peers)}
  </div>
  <div class="product-model6"><div class="row">
    <h3 class="product-title" id="i2">Teknik Özellikler</h3>
    <div class="tl-spec-grid">{specs}</div>
  </div></div>
  <div class="tl-prose">{faq(faqs)}</div>
  {quote(s["title"] + " için keşif ve teklif alın.")}
</div>
"""


def cat_page(title: str, intro: list[str], img: str, crumbs_i, series_list, tabs, splits, faqs) -> str:
    tab_html = ""
    for u, n, active in tabs:
        cur = " cur" if active else ""
        tab_html += f'<a href="{u}" class="right-i{cur}"><span>{n}</span></a>'
    cards = "".join(
        f'<a class="product-list-b-i" href="/{s["slug"]}/" hsm="fadeup">'
        f'<div class="product-list-b-img img-scale"><img src="{s["hero"]}" alt="{s["title"]}"></div>'
        f'<div class="product-list-b-info"><p class="t1">{s["title"]}</p>'
        f'<p class="t2">Piksel aralığı: {s["pitch"]}</p>'
        f'<p class="t3">{s["lead"]}</p></div></a>'
        for s in series_list
    )
    intro_html = "".join(f"<p class=\"{'lead' if i == 0 else ''}\">{p}</p>" for i, p in enumerate(intro))
    return f"""
{banner(img, title)}
<div class="public-nav"><div class="row public-tobody justify-between ov">
  <div class="left items-center">{crumbs(crumbs_i).split('<div class="left items-center">')[1].split("</div>")[0]}</div>
  <div class="right items-center">{tab_html}</div>
</div></div>
<div class="tl-prose">
  <h1 class="public-title" style="text-align:left;margin-bottom:12px">{title}</h1>
  {toc([("rehber", "Seçim rehberi"), ("seriler", "Seriler"), ("sss", "Sık sorulanlar")])}
  {intro_html}
  <h2 id="rehber">Seçim rehberi</h2>
  {"".join(splits)}
  <h2 id="seriler">Seriler</h2>
  <p>Aşağıdaki kartlarda pitch, kısa açıklama ve stüdyo/saha görseli vardır. Detay sayfada teknik tablo, kullanım senaryosu ve keşif listesi bulunur.</p>
</div>
<div class="product-list public-tobody">
  <div class="product-list-b flex-wrap justify-between hsms">{cards}</div>
</div>
<div class="tl-prose" id="sss">{faq(faqs)}</div>
{quote()}
"""


def hub_main() -> str:
    cards = [
        ("/commercial-display/", f"{M}/banner-indoor.jpg", "İç Mekan", "Fine pitch, COB, kristal film. Lobi, toplantı ve stüdyo duvarları."),
        ("/rental-staging/", f"{M}/banner-rental.jpg", "Kiralama & Sahne", "Konser, fuar ve lansman için hızlı kilitli kabin."),
        ("/dooh/", f"{M}/banner-outdoor.jpg", "Dış Mekan", "Billboard, cephe ve stadyum. Yüksek nit, IP koruma."),
        ("/accessories/", f"{M}/product-slim-cabinet.jpg", "Aksesuarlar", "QM, MG, P ve V kabin, güç ve montaj setleri."),
    ]
    grid = "".join(
        f'<a class="tl-hub-card" href="{u}"><img src="{img}" alt="{t}">'
        f'<div class="tl-hub-copy"><span>Katalog</span><strong>{t}</strong><em>{d}</em></div></a>'
        for u, img, t, d in cards
    )
    return f"""
{banner(f"{M}/hero-indoor-led.jpg", "Toeled LED ürünleri")}
{crumbs([("/products/", "Ürünler"), ("", "Katalog")])}
<div class="tl-prose">
  <h1 class="public-title" style="text-align:left">LED ekran ürünleri</h1>
  {toc([("katalog", "Katalog"), ("pitch", "Pitch"), ("sabit", "Sabit / rental"), ("kesif", "Keşif")])}
  <p class="lead">İç mekan, rental, dış mekan ve aksesuar serilerini projenize göre seçin. Pitch, kabin, IP ve kontrol keşifte netleşir; teklif LEDAJANS ekibiyle yürür.</p>
  <p>Toeled, TAHA LED Dış Ticaret A.Ş. ürün vitrinidir. İstanbul showroom’da fine pitch, kristal film ve rental kabinleri canlı içerikle görürsünüz. Almanya ve Kıbrıs ofisleri aynı teknik standardı taşır.</p>
  <p>21 seri dört başlıkta toplanır. Kartlara tıklayınca pitch tablosu, kullanım senaryosu, keşif listesi ve SSS açılır. Sahte fabrika turu veya Çin bayi haritası yoktur.</p>
</div>
<div class="tl-hub-grid" id="katalog">{grid}</div>
<div class="tl-prose">
  {split(f"{M}/hero-cob-module.jpg", "Fine pitch seçimi", "Doğru pitch nasıl seçilir?", [
      "Kaba kural: 1 mm piksel aralığı ≈ 1 m minimum izleme. 4 m oturma için 1.5–2.5 mm; stüdyo ve lobi yakınında COB 0.9–1.5 mm öne çıkar.",
      "İçerik native çözünürlüğe uymalıdır. 4K slayt 2 mm duvarda ancak yeterli piksel varsa keskin kalır. Keşifte ölçü ve oturma planı alınır.",
      "Vitrin ve cam işlerinde CMS film, sahne ve fuarda rental kilit, cadde ve stadyumda Outdoor Q/S veya MG seçilir. Karar showroom veya saha fotoğrafıyla kilitlenir.",
  ])}
  {split(f"{M}/banner-rental.jpg", "Rental veya sabit", "Sabit mi rental mi?", [
      "Duvar yıllarca kalacaksa sabit Q / NC / CMS. Her gece sökülecekse RW, CG, LN rental kilit ve flight case gerekir.",
      "Hibrit işlerde (fuar + sonra ofis) iki teklif çıkarılır. Yedek modül oranı rentalde yüzde 5–10’dur.",
      "Kısa süreli etkinlikte kiralık kabin ekonomiktir; 7/24 lobi duvarında sabit kabin daha düşük toplam maliyettir.",
  ], True)}
  <h2 id="pitch">Pitch özeti</h2>
  {table(
      ["Mesafe", "Önerilen sınıf", "Seri örneği"],
      [
          ["2–4 m", "0.9–1.5 mm COB / Mini", "NC, Q Mini"],
          ["4–8 m", "1.8–2.5 mm sabit", "İç Mekan Q"],
          ["Sahne / TV", "2.6–2.9 mm rental", "RW, LN, DM"],
          ["Cadde / cephe", "5–8 mm dış", "Outdoor Q, MG"],
          ["Cam vitrin", "4–10 mm film", "CMS"],
      ],
  )}
  <h2 id="kesif">Keşif adımları</h2>
  {guides([
      (f"{M}/indoor-corporate-lobby-3c5ebf5e.jpg", "1. Ölçü ve mesafe", "En, boy, izleme mesafesi, güç ve askı/duvar.", "/contact-us/"),
      (f"{M}/product-cabinet-studio.jpg", "2. Seri ve pitch", "İç / dış / rental aileleri showroom veya sahada.", "/commercial-display/"),
      (f"{M}/showroom-istanbul.webp", "3. Teklif ve kurulum", "Kabin, kontrol, işçilik, 2 yıl garanti kalemi.", "/service/"),
  ])}
  {faq([
      ("Tüm seriler Türkiye’de kurulur mu?", "Evet. İstanbul ekibi Türkiye geneli; Erkrath ve Girne Avrupa / KKTC işlerini taşır."),
      ("Showroom randevusu nasıl alınır?", "info@ledajans.com veya +90 212 220 40 04. Şişli’de Q, CMS ve rental kabinler canlıdır."),
      ("Teklif kaç günde gelir?", "Ölçü ve foto varsa aynı gün ön teklif; keşif sonrası net kalemler 1–3 iş günü."),
      ("Garanti nedir?", "Sabit işlerde 2 yıl parça-işçilik. Rentalde proje süresince saha servisi."),
  ])}
</div>
{quote("Kataloğu birlikte daraltalım — keşif ve teklif alın.")}
"""


def knowledge_main() -> str:
    return f"""
{banner(f"{M}/banner-indoor.jpg", "Bilgi merkezi")}
{crumbs([("/knowledge/", "Destek"), ("", "Bilgi merkezi")])}
<div class="tl-prose">
  <h1 class="public-title" style="text-align:left">Bilgi merkezi</h1>
  {toc([
      ("kurulum", "Kurulum"),
      ("kullanim", "Kullanım"),
      ("bakim", "Bakım"),
      ("pitch", "Pitch tablosu"),
      ("guc", "Güç ve sinyal"),
      ("karsilastirma", "Sabit / rental / dış"),
      ("sss", "SSS"),
  ])}
  <p class="lead">Kurulum, kullanım ve bakım: sahada işe yarayan kılavuz. Toeled / LEDAJANS keşif tutanağı bu maddelerin üzerine yazılır; ihale şartnamesi ve teslim check-list’i aynı dili konuşur.</p>
  <p>Aşağıdaki başlıklar saha teslimi ve 2 yıl garanti sürecinde referans olsun diye derlendi. Projenize özel çizim, güç hesabı ve native çözünürlük için <a href="/contact-us/">teklif formunu</a> veya WhatsApp +90 212 220 40 04 hattını kullanın. Şişli showroom’da aynı içeriği farklı pitch’te canlı izlersiniz.</p>
  {guides([
      (f"{M}/product-cabinet-studio.jpg", "Kurulum", "Duvar, truss, güç, sinyal ve teslim listesi.", "#kurulum"),
      (f"{M}/hero-indoor-led.jpg", "Kullanım", "Native çözünürlük, parlaklık ve 7/24 profil.", "#kullanim"),
      (f"{M}/rental-flight-cases-fd0c4e92.jpg", "Bakım", "Aylık kontrol, kalibrasyon, yedek parça.", "#bakim"),
  ])}
  {split(f"{M}/indoor-corporate-lobby-3c5ebf5e.jpg", "LED duvar kurulumu", "Kurulum", [
      "Keşifte duvar veya truss kararı, askı yükü, ankraj ve yangın durdurucu detayı netleşir. Kabin terazisi milimetre kaçışını keser; ilk sıra referans kabul edilir.",
      "Güç hattı, ayrı sigorta, topraklama ve varsa UPS teslim tutanağına yazılır. Sinyal fiber veya CAT; uzun hatlarda fiber tercih edilir. Modül kilidi ve power/data loop teslim kontrol listesindedir.",
      "İç mekanda ön bakımlı kabin dar koridoru kurtarır. Dış mekanda IP conta, drenaj ve arka koridor emniyeti ayrıca imzalanır. Rentalde kilit pimi, eğim takozu ve flight case envanteri load-in öncesi sayılır.",
      "Teslim günü operatöre aç-kapa, parlaklık, içerik atama ve basit arıza gösterilir. İmzalı check-list garanti başlangıcıdır; eğitim notu PDF olarak bırakılır.",
  ])}
  {split(f"{M}/hero-cob-module.jpg", "LED ekran kullanımı", "Kullanım", [
      "İçerik çözünürlüğü ekranın native piksel sayısına oturmalıdır. Ölçeklenmiş 4K, fine pitch duvarda yumuşar. Slayt ve videoyu işlemci girişine göre export edin.",
      "Parlaklık ofiste düşük, vitrin ve dış mekanda yüksek profilde kalır. 7/24 duvarda gece-gündüz zamanlayıcı, pixel shift ve ısınma derating’i önerilir. Kamera çekiminde refresh değerini shutter ile eşleyin.",
      "Uzaktan yayın (DOOH) için yedek hat ve izleme yazılımı teklife eklenir. Showroom’da canlı demo ile parlaklık ve gri tonu yerinde görün.",
      "Küçük toplantı duvarında laptop yeter; büyük lobi ve 7/24 işlerde ayrı oynatıcı + LED işlemci önerilir. Playlist ve acil mesaj senaryosu teslimde kaydedilir.",
  ], True)}
  {split(f"{M}/product-slim-cabinet.jpg", "LED bakım", "Bakım", [
      "Aylık: ölü piksel, fan, kablo ve vida torku görsel kontrol. Toz, lobi ve stüdyoda COB/SMD yüzeyde birikir; kuru bez, üretici yasağına uygun.",
      "Yıllık: renk kalibrasyonu, PSU ve kontrol yedek testi. Yedek modül ve PSU oranı sabit işlerde yüzde 2–5, rentalde yüzde 5–10 civarı tutulur.",
      "Arızada WhatsApp +90 212 220 40 04 veya <a href=\"/debugger/\">teknik destek formu</a>. Kayıt İstanbul ekibine düşer; sahte fabrika yazılımı yoktur.",
      "Kritik 7/24 duvarda yedek PSU sahada durur. Rental load-in öncesi yedek sayımı saha çantasıyla yapılır; eksik parça İstanbul stoktan aynı gün çıkar.",
  ])}
  <h2 id="pitch">Pitch ve izleme mesafesi</h2>
  <p>Kaba kural: 1 mm piksel aralığı yaklaşık 1 m minimum izleme mesafesidir. Bu tablo teklif öncesi yön gösterir; keşifte oturma planı ve içerik türü (slayt, video, kamera) pitch’i kilitler.</p>
  {table(
      ["İzleme", "Pitch sınıfı", "Tipik yer", "Seri"],
      [
          ["2–4 m", "0.9–1.5 mm", "Stüdyo, toplantı, lobi yakını", "NC COB, Q Mini"],
          ["4–8 m", "1.8–2.5 mm", "Otel lobisi, fuar duvarı, ofis", "İç Mekan Q"],
          ["Sahne / TV", "2.6–2.9 mm", "Konser IMAG, lansman, fuar standı", "RW, LN, DM, CG"],
          ["Cadde / cephe", "5–8 mm", "Billboard, medya cephe, durak", "Outdoor Q, MG"],
          ["Stadyum", "5–10 mm", "Peri-led, tribün çevresi", "Outdoor S"],
          ["Cam vitrin", "4–10 mm film", "Mağaza, plaza atrium", "CMS"],
      ],
  )}
  <h2 id="guc">Güç, sinyal ve içerik</h2>
  {split(f"{M}/product-cabinet-studio.jpg", "LED güç ve sinyal", "Güç ve sinyal", [
      "Ayrı sigorta, topraklama ve varsa UPS teslim maddesidir. Kabin tüketimi keşifte m² ve parlaklık profiline göre hesaplanır; jeneratör rental sahnede ayrıca yazılır.",
      "Kısa hat CAT, uzun hat ve bina geçişlerinde fiber. Power/data loop ve yedek alıcı kart 7/24 işlerde standart öneridir.",
      "İçerik native çözünürlükte export edilir. HDR ve yüksek frame stüdyo işlerinde işlemci kapasitesi teklife girer.",
  ])}
  <h2>Keşifte yanınızda olsun</h2>
  {checks([
      "Duvar / truss ölçüleri ve foto",
      "İzleme mesafesi ve oturma planı",
      "İç, dış veya rental senaryosu",
      "Güç panosu ve toprak noktası",
      "Ön veya arka bakım koridoru",
      "İçerik kaynağı (PC, oynatıcı, yayın)",
      "Kurulum penceresi ve gece çalışması",
      "Yedek parça oranı beklentisi",
  ])}
  <h2 id="karsilastirma">Sabit, rental ve dış mekan</h2>
  {table(
      ["Konu", "Sabit iç", "Rental", "Dış mekan"],
      [
          ["Kabin", "Die-cast / ön bakım", "Hızlı kilit + flight case", "IP döküm, arka koridor"],
          ["Yedek", "%2–5 modül/PSU", "%5–10 + saha çantası", "PSU ve conta yedeği"],
          ["Süre", "1–7 gün kurulum", "Aynı gece load-in", "İskele + izin takvimi"],
          ["Garanti", "2 yıl parça-işçilik", "Proje süresince saha", "2 yıl + IP teslim"],
      ],
  )}
  <h2>İlgili sayfalar</h2>
  {guides([
      (f"{M}/banner-indoor.jpg", "Servis süreci", "Keşif, kurulum, 2 yıl garanti.", "/service/"),
      (f"{M}/hero-indoor-led.jpg", "İç mekan seçimi", "Pitch rehberi ve seriler.", "/news/ic-mekan-led-ekran-nasil-secilir/"),
      (f"{M}/hero-rental-stage.jpg", "Rental kılavuz", "Sahne kiralama, kilit, yedek.", "/news/rental-led-ekran-sahne-kiralama/"),
  ])}
  <div id="sss">{faq([
      ("Kurulum kaç gün sürer?", "Oda ölçeği 1–3 gün; 30 m²+ lobi 3–7 gün; konser rental aynı gece load-in. Keşifte pencere yazılır."),
      ("İçerik bilgisayarımızdan mı gider?", "Küçük duvarda evet. Büyük ve 7/24 işlerde ayrı oynatıcı + LED işlemci önerilir."),
      ("Yedek parça nerede durur?", "İstanbul stok. Erkrath ve Girne işlerinde sevkiyat planı teklifte görünür."),
      ("Eğitim var mı?", "Teslimde operatör eğitimi standarttır: aç-kapa, parlaklık, içerik atama, basit arıza."),
      ("Pitch’i nasıl seçerim?", "Yukarıdaki tablo başlangıçtır. 4 m oturma için 1.5–2.5 mm; stüdyo yakınında COB. Showroom’da yan yana bakın."),
      ("Dış mekanda yağmur ne olur?", "IP conta, drenaj ve kabin sınıfı teslim maddesidir. Rental açık havada yağmur planı sözleşmeye yazılır."),
      ("7/24 duvar özel midir?", "Evet: düşük parlaklık profili, pixel shift, N+1 PSU ve yıllık kalibrasyon. PDC ve NC bu işe yakındır."),
      ("Belge ve ISO istersek?", "<a href=\"/certificates-honor/\">Sertifikalar</a> sayfası ve teklif PDF’i. Sahte QR sorgusu yoktur."),
  ])}</div>
</div>
{quote("Kurulum veya bakım için keşif isteyin.")}
"""


def service_main() -> str:
    return f"""
{banner(f"{M}/banner-indoor.jpg", "Servis")}
{crumbs([("/service/", "Destek"), ("", "Servis")])}
<div class="tl-prose">
  <h1 class="public-title" style="text-align:left">Servis ve garanti</h1>
  {toc([("surec", "Süreç"), ("kesif", "Keşif"), ("kurulum", "Kurulum"), ("sss", "SSS")])}
  <p class="lead">Keşif, kurulum, teslim eğitimi ve 2 yıl parça-işçilik. Mesai 7 gün, Türkiye saati; Almanya ve Kıbrıs ofisleri yerel saatle aynı süreci yürütür.</p>
  <p>Toeled sahası LEDAJANS ekibidir. Beijing saati veya ihale “bidding cooperation” dili yoktur. Ölçü, güç, askı ve içerik senaryosu tek tutanakta toplanır. Yedek parça İstanbul stokludur; Erkrath ve Girne sevkiyatı teklifte görünür.</p>
</div>
<div class="service-b" id="surec"><div class="model1 public-tobody hsms">
  <div class="model1-info-list flex-wrap justify-between hsms">
    <div class="model1-info-list-i"><div class="model1-info-list-i-con"><p class="t1">Yerinde keşif</p><p class="t2">Ölçü, izleme mesafesi, güç, HVAC ve askı/duvar analizi. Foto ve kroki tutanağa eklenir.</p></div></div>
    <div class="model1-info-list-i"><div class="model1-info-list-i-con"><p class="t1">Çözüm tasarımı</p><p class="t2">Pitch, kabin, kontrol, native çözünürlük ve yedek oranı. Showroom’da örnek izlenir.</p></div></div>
    <div class="model1-info-list-i"><div class="model1-info-list-i-con"><p class="t1">Kurulum</p><p class="t2">Montaj, sinyal, kalibrasyon, teslim eğitimi ve imzalı check-list.</p></div></div>
    <div class="model1-info-list-i"><div class="model1-info-list-i-con"><p class="t1">Garanti</p><p class="t2">2 yıl parça ve işçilik; yedek stok İstanbul. Rentalde proje süresince saha.</p></div></div>
  </div>
</div></div>
<div class="tl-prose">
  {split(f"{M}/showroom-istanbul.webp", "LED keşif", "Keşifte ne bakılır?", [
      "İzleme mesafesi pitch’i kilitler. Güç panosu, topraklama ve varsa jeneratör/UPS notu elektrik kalemini belirler.",
      "İç mekanda ön/arka servis yönü, dış mekanda IP ve rüzgar, rentalde load-in saati. Bu üçü teklifin omurgasıdır.",
      "Foto, kroki ve kullanım senaryosu (slayt, yayın, DOOH) aynı gün yeter. Randevu +90 212 220 40 04.",
  ])}
  {split(f"{M}/rental-concert-stage-84bd91a8.jpg", "Saha kurulumu", "Kurulum günü", [
      "Kabin terazisi, modül kilidi, power/data loop ve işlemci girişi teslim maddeleridir.",
      "Operatöre aç-kapa, parlaklık, içerik ve basit arıza anlatılır. İmzalı tutanak garanti başlangıcıdır.",
      "Rentalde flight case sayımı ve yedek çanta load-out’ta tekrar imzalanır. Sabit işte yıllık kalibrasyon hatırlatması mail ile gider.",
  ], True)}
  <h2>Garanti kapsamı</h2>
  {checks([
      "Normal kullanımda parça ve işçilik",
      "Teslim eğitimi ve check-list",
      "İstanbul yedek stok koordinasyonu",
      "Kritik arızada telefon / WhatsApp",
      "Rentalde proje süresince saha",
      "Yıllık kalibrasyon randevusu (sabit)",
  ])}
  <div id="sss">{faq([
      ("Garanti neleri kapsar?", "Normal kullanımda parça ve işçilik. Fiziksel darbe, su baskını ve yetkisiz müdahale dışındadır; poliçe teklif ekinde."),
      ("7/24 ne demek?", "Kritik arızada telefon/WhatsApp hattı. Planlı bakım mesai içinde randevulanır."),
      ("Kurulum Türkiye geneli mi?", "Evet. 81 il; büyük işlerde saha ekibi İstanbul’dan mobilize olur."),
      ("Yedek ne kadar sürede gelir?", "İstanbul stoklu kalemler aynı gün veya ertesi iş günü. Özel modülde süre teklifte yazılır."),
      ("Eğitim tekrarlanır mı?", "Teslimde bir tur standarttır; ek eğitim saatlik kalem olarak eklenir."),
  ])}</div>
</div>
{quote("Keşif randevusu ve servis kaydı açın.")}
"""


def outlets_main() -> str:
    return f"""
{banner(f"{M}/showroom-istanbul.webp", "Satış noktaları")}
{crumbs([("/sales-outlets/", "Destek"), ("", "Satış noktaları")])}
<div class="tl-prose">
  <h1 class="public-title" style="text-align:left">Satış noktaları</h1>
  <p class="lead">Üç ofis, tek standart. Çin bayi haritası yoktur; sizinle İstanbul, Erkrath ve Girne konuşur. Showroom randevusu ve keşif aynı e-posta ve telefonlardan yürür.</p>
  <p>Teklif, kurulum ve yedek parça LEDAJANS süreçleriyle aynı kalır. Avrupa işlerinde Erkrath lojistik ayağı, KKTC’de Girne saha koordinasyonu, Türkiye genelinde İstanbul ekibi devrededir.</p>
</div>
<div class="tl-offices">
  <div class="tl-office-card"><h3>İstanbul</h3><p>Halide Edip Adıvar Mah. Gül 2 Sk. No:10a, Şişli</p><p>+90 212 220 40 04</p><p>Showroom: fine pitch, CMS, rental kabin. Keşif ve teklif merkezi.</p></div>
  <div class="tl-office-card"><h3>Erkrath</h3><p>Heinrich-Hertz-Straße 50, 40699 Erkrath</p><p>+49 1521 2401915</p><p>Almanya ve AB işleri: keşif, lojistik, Avrupa saha koordinasyonu.</p></div>
  <div class="tl-office-card"><h3>Girne</h3><p>Karaoğlanoğlu Cad. Yayla Aktiğin İş Hanı No:6</p><p>+90 533 856 93 71</p><p>KKTC vitrin, otel ve sahne işleri. İstanbul stoklu yedek.</p></div>
</div>
<div class="tl-prose">
  {split(f"{M}/indoor-showroom-acfc9661.jpg", "İstanbul showroom", "Şişli showroom", [
      "Q Mini, İç Mekan Q, NC COB ve CMS film aynı salonda yan yana. Randevuyla canlı içerik ve parlaklık profili izlenir.",
      "Ölçünüzü getirin; aynı gün ön teklif kalemleri (kabin, kontrol, işçilik, garanti) çıkarılır.",
      "Rental kabin ve flight case de showroom’dadır. Load-in senaryosunu yerinde konuşmak teklifi netleştirir.",
  ])}
  {split(f"{M}/hero-outdoor-dooh.jpg", "Avrupa ve Kıbrıs ofis", "Erkrath ve Girne", [
      "Erkrath, AB lojistiği ve Almanca keşif notu içindir. Standart pitch ve garanti maddesi İstanbul ile aynıdır.",
      "Girne otel, vitrin ve sahne işlerinde yerinde keşif yapar; yedek parça İstanbul stoktan planlanır.",
  ], True)}
  {guides([
      (f"{M}/hero-indoor-led.jpg", "Ürün seçimi", "İç / rental / dış katalog.", "/products/"),
      (f"{M}/banner-indoor.jpg", "Servis", "Kurulum ve 2 yıl garanti.", "/service/"),
      (f"{M}/hero-outdoor-dooh.jpg", "İletişim", "Harita, form, WhatsApp.", "/contact-us/"),
  ])}
  {faq([
      ("Bayilik var mı?", "Satış LEDAJANS ofisleri üzerinden yürür. Bölgesel iş ortaklığı için iletişime geçin; haritada sahte Çin dealer noktası yoktur."),
      ("Showroom ücretsiz mi?", "Evet, randevulu. +90 212 220 40 04."),
      ("Hangi ofisten teklif alırım?", "Türkiye işleri İstanbul; AB Erkrath; KKTC Girne. Form tek, ekip yönlendirir."),
      ("Showroom’da ne var?", "Fine pitch, kristal film, rental kabin ve örnek içerik. Pitch karşılaştırması yerinde yapılır."),
  ])}
</div>
{quote("Ofis veya showroom randevusu alın.")}
"""


def certs_main() -> str:
    return f"""
{banner(f"{M}/banner-indoor.jpg", "Sertifikalar")}
{crumbs([("/about-us/", "Hakkımızda"), ("", "Sertifikalar")])}
<div class="tl-prose">
  <h1 class="public-title" style="text-align:left">Sertifikalar ve uygunluk</h1>
  <p class="lead">Projelerde ISO kalite süreçleri, CE/uygunluk ve 2 yıl garanti teklife yazılır. Sahte ödül vitrini veya QR ürün sorgusu yoktur; belge kopyası talep üzerine iletilir.</p>
  <p>İhale dosyasına girecek ISO, CE ve ürün uygunluk özetini satış temsilciniz PDF olarak gönderir. QCE “cert no” makinesi yoktur; <a href="/qce-cert-lookup/">sertifika bilgisi</a> sayfası sizi buraya ve iletişime yönlendirir.</p>
  <p>Kamu, stadyum ve havalimanı işlerinde ek test raporu istenirse süre keşifte yazılır. Belge üretici dosyası ve Toeled / LEDAJANS teslim tutanağıyla izlenir.</p>
</div>
<div class="tl-spec-grid" style="margin:0 auto 40px">
  <div><span>Kalite</span><strong>ISO süreçleri</strong></div>
  <div><span>Ürün</span><strong>CE / uygunluk</strong></div>
  <div><span>Garanti</span><strong>2 yıl parça ve işçilik</strong></div>
  <div><span>Servis</span><strong>Türkiye geneli kurulum</strong></div>
</div>
<div class="tl-prose">
  {split(f"{M}/product-cabinet-studio.jpg", "LED uygunluk", "Teklife hangi belge girer?", [
      "Ürün ailesine göre CE/uygunluk özeti, montaj kılavuzu ve garanti maddesi.",
      "Kamu ve stadyum işlerinde ek test raporu istenirse süre keşifte yazılır.",
      "Teslimde seri/lot listesi tutanağa eklenir. Sahada QR okutma yoktur.",
  ])}
  {guides([
      (f"{M}/banner-indoor.jpg", "Servis", "Kurulum ve garanti maddesi.", "/service/"),
      (f"{M}/showroom-istanbul.webp", "Teklif", "İhale eki PDF talebi.", "/contact-us/"),
      (f"{M}/hero-indoor-led.jpg", "Bilgi merkezi", "Kurulum ve bakım kılavuzu.", "/knowledge/"),
  ])}
  {faq([
      ("Belgeyi ne zaman alırım?", "Teklif onayından sonra veya ihale ekinde. Acil talepte aynı gün PDF."),
      ("Sahada QR okutma var mı?", "Yok. Ürün kimliği teslim tutanağı ve seri/lot ile izlenir."),
      ("ISO numarası sitede neden yok?", "Belge kopyası proje dosyasına eklenir; vitrin QR’si kullanılmaz."),
      ("Kim düzenler?", "TAHA LED Dış Ticaret A.Ş. / Toeled satış; üretici uygunluk dosyasından gelir."),
  ])}
</div>
{quote("Belge ve teknik dosya talep edin.")}
"""


def qce_main() -> str:
    return f"""
{banner(f"{M}/banner-indoor.jpg", "Sertifika")}
{crumbs([("/qce-cert-lookup/", "Destek"), ("", "Sertifika")])}
<div class="tl-prose">
  <h1 class="public-title" style="text-align:left">Sertifika bilgisi</h1>
  <p class="lead">Sahte ürün kodu sorgusu yoktur. ISO/CE ve proje belgelerini <a href="/certificates-honor/">sertifikalar</a> sayfasından veya teklif dosyasından isteyin.</p>
  <p>Eski QCE arama kutusu kaldırıldı. Belge ihtiyacınız ihale, gümrük veya saha teslimi içindir; formu doldurun, İstanbul ofisi PDF ile döner.</p>
  <p>Ürün kimliği teslim tutanağı ve seri/lot listesiyle izlenir. Vitrin QR’si veya “cert no” makinesi Toeled sürecinin parçası değildir.</p>
  {split(f"{M}/product-cabinet-studio.jpg", "Sertifika talebi", "Nasıl belge istersiniz?", [
      "İhale eki, gümrük veya saha teslimi için ISO/CE özeti ve garanti maddesi PDF olarak gider.",
      "Acil taleplerde aynı gün dönüş hedefi vardır. Proje adı ve ürün ailesini yazmanız yeter.",
  ])}
  {guides([
      (f"{M}/banner-indoor.jpg", "Sertifika özeti", "ISO süreç, CE, 2 yıl garanti.", "/certificates-honor/"),
      (f"{M}/showroom-istanbul.webp", "Teklif ve belge", "Proje dosyasına eklenecek PDF.", "/contact-us/"),
      (f"{M}/product-cabinet-studio.jpg", "Servis", "Kurulum ve uygunluk sahada.", "/service/"),
  ])}
  {faq([
      ("Numara girip sorgulayabilir miyim?", "Hayır. Bu sayfa yönlendirme ve açıklama içindir."),
      ("Kim düzenler?", "TAHA LED Dış Ticaret A.Ş. / Toeled satış; belge üretici ve uygunluk dosyasından gelir."),
      ("Hangi belgeler gelir?", "CE/uygunluk özeti, montaj notu, garanti maddesi. Ek test raporu keşifte yazılır."),
      ("Eski QCE linkim var?", "Bu sayfa onun yerine geçer. Form veya sertifikalar sayfasını kullanın."),
  ])}
</div>
{quote("Belge talebi için yazın.")}
"""


def support_form_main(title: str, lead: str) -> str:
    return f"""
{banner(f"{M}/banner-indoor.jpg", title)}
{crumbs([("/debugger/", "Destek"), ("", title)])}
<div class="tl-prose">
  <h1 class="public-title" style="text-align:left">{title}</h1>
  <p class="lead">{lead}</p>
  <p>Kayıt İstanbul teknik ekibine düşer. Fabrika uzaktan yazılım taklidi yoktur. Foto, seri/lot ve kısa arıza tarifi teşhisi hızlandırır.</p>
  <p>Planlı bakım, yedek siparişi ve keşif <a href="/service/">servis</a> sayfasındandır. Acil saha için WhatsApp +90 212 220 40 04. Formdaki arıza tarifi mümkün olduğunca net olsun: hangi kabin, hangi semptom, ne zamandan beri.</p>
  {split(f"{M}/product-cabinet-studio.jpg", "Teknik teşhis", "Ne zaman yazın?", [
      "Ölü piksel, renk kayması, sinyal kopması, PSU ve uzaktan yayın kesintisi bu forma girer. Rental load-in öncesi yedek sayımı da aynı hat.",
      "Yanıt hedefi mesai içinde aynı gün; gece kritik arızada WhatsApp. Planlı bakım için <a href='/service/'>servis</a> sayfasını kullanın.",
      "Fotoğraf: ekranın tamamı + yakın arıza. Mümkünse kabin arkası PSU ve alıcı kart da ekleyin.",
  ])}
  {guides([
      (f"{M}/hero-cob-module.jpg", "Modül / ölü piksel", "Yakın foto ve kabin konumu yeter.", "/knowledge/#bakim"),
      (f"{M}/banner-rental.jpg", "Rental saha", "Load-in öncesi yedek ve kilit.", "/news/rental-led-ekran-sahne-kiralama/"),
      (f"{M}/hero-outdoor-dooh.jpg", "Dış mekan", "IP, güç ve uzaktan yayın hattı.", "/news/dis-mekan-led-ekran-parlaklik/"),
  ])}
  <h2>Formu doldururken</h2>
  {checks([
      "Ad, telefon ve şirket",
      "İç / dış / rental ve şehir",
      "Arıza tarifi (renk, sinyal, güç)",
      "Yakın ve genel foto",
      "Seri/lot veya teslim tarihi (varsa)",
      "Acil mi, planlı bakım mı",
  ])}
  <p><a class="contact-btn" href="https://wa.me/902122204004" target="_blank" rel="noopener">WhatsApp destek</a></p>
</div>
<div class="culture-b public-tobody">
  <form id="inqForm" name="inqForm" url="#">
    <div class="model2">
      <div class="contact-msg-i items-center" style="width:100%"><span>Ad Soyad *</span>
        <input class="inputs" name="name" datatype="*1-50" nullmsg="Adınızı yazın"></div>
      <div class="contact-msg-i items-center" style="width:100%"><span>Telefon *</span>
        <input class="inputs" name="telphone" datatype="*1-40"></div>
      <div class="contact-msg-i flex" style="width:100%"><span>Arıza / ihtiyaç *</span>
        <textarea class="inputs textarea" name="content" datatype="*1-500"></textarea></div>
      <button type="submit" class="contact-btn">Gönder</button>
    </div>
  </form>
</div>
{quote("Saha kaydı veya uzaktan teşhis isteyin.")}
"""


def culture_main() -> str:
    items = [
        ("Vizyon", "Türkiye, Almanya ve Kıbrıs’ta ölçülebilir, keşfi dürüst LED ekran partneri olmak. Showroom’da gördüğünüz ile sahada kurulan aynı standarttır.", f"{M}/hero-indoor-led.jpg"),
        ("Misyon", "Doğru pitch, sağlam kabin, keşiften servise net süreç. Teklifte olmayan iş sahada sürpriz olmaz.", f"{M}/banner-rental.jpg"),
        ("Değerler", "Dürüst keşif, gerçekçi teklif, sahada tutulan söz. Müşteri, kurulum ekibi ve servis aynı maddeleri okur.", f"{M}/hero-outdoor-dooh.jpg"),
        ("Servis", "2 yıl parça-işçilik, yedek stok, 7/24 saha hattı. Arıza kaydı İstanbul’a düşer.", f"{M}/showroom-istanbul.webp"),
    ]
    cards = "".join(
        f'<div class="culture-b-list-i"><div class="row"><div class="row-a">'
        f'<img class="row-a-img" src="{img}" alt="{t}"><p class="t1">{t}</p></div>'
        f'<div class="row-b"><p class="t1">{t}</p><div class="t2"><p>{d}</p></div></div></div></div>'
        for t, d, img in items
    )
    return f"""
{banner(f"{M}/banner-indoor.jpg", "Kurum kültürü")}
{crumbs([("/about-us/", "Hakkımızda"), ("", "Kurum kültürü")])}
<div class="tl-prose">
  <h1 class="public-title" style="text-align:left">Kurum kültürü</h1>
  <p class="lead">Müşteri, keşif, kurulum ve servis. İngilizce Vision/Mission metinleri kalkmıştır; çalışma ilkeleri Türkçe ve sahaya yazılıdır.</p>
</div>
<div class="culture-b public-tobody"><div class="culture-b-list flex-wrap hsms">{cards}</div></div>
<div class="tl-prose">
  {split(f"{M}/indoor-corporate-lobby-3c5ebf5e.jpg", "Saha ekibi", "Sahada nasıl çalışırız?", [
      "Keşif tutanağı teklifin ekidir. Kabin, pitch, güç ve işçilik kalemleri müşteriyle aynı PDF’te kalır.",
      "Teslimde eğitim ve check-list imzalanır. Garanti bu imzayla başlar.",
      "Showroom’da gördüğünüz parlaklık ve pitch, sahada kurulanla aynı standarttır. Sürpriz kalem yoksa sürpriz iş de yoktur.",
  ])}
  {faq([
      ("İngilizce vizyon metni nerede?", "Kalkmıştır. İlkeler Türkçe ve saha dilindedir."),
      ("Müşteri kimle konuşur?", "LEDAJANS keşif ve satış; Toeled ürün vitrini. Aynı ekip, aynı tutanak."),
  ])}
</div>
{quote("Ekiple tanışmak için showroom randevusu alın.")}
"""


def about_main() -> str:
    years = [
        ("2000’ler", "Sektörde LED ekran satış, kiralama ve saha kurulumu tecrübesi birikir. Sahne ve sabit iş aynı ekip dilinde yürür."),
        ("İstanbul ofis", "Şişli’de showroom ve operasyon merkezi; keşif-teklif aynı çatıda. Türkiye geneli kurulum buradan planlanır."),
        ("Almanya & Kıbrıs", "Erkrath ve Girne ofisleriyle Avrupa ve KKTC projeleri. Lojistik ve saha koordinasyonu yerel saatte."),
        ("Toeled", "TAHA LED Dış Ticaret A.Ş. ürün vitrini: iç, rental, DOOH katalog. LEDAJANS çatısında keşif ve servis."),
        ("Bugün", "2 yıl garanti, Türkiye geneli kurulum, ISO uygunluk ve 7/24 saha desteği. Çin fabrika parkı veya VR turu yoktur."),
    ]
    tl = "".join(
        f'<div class="swiper-slide"><div class="model3-swiper-i"><p class="t1">{y}</p>'
        f'<div class="t3"><p>{t}</p></div></div></div>'
        for y, t in years
    )
    return f"""
{banner(f"{M}/showroom-istanbul.webp", "Toeled Hakkımızda")}
{crumbs([("/about-us/", "Hakkımızda"), ("", "Kurum")])}
<div class="introduce-b">
  <div class="model1 public-tobody flex">
    <div class="left hsms ov">
      <p class="public-title1">Kurumsal Profil</p>
      <div class="left-info"><p class="t1">TAHA LED Dış Ticaret A.Ş. · Toeled</p>
      <p class="t2">Toeled, LEDAJANS çatısında iç ve dış mekan LED ekran, rental, kontrol ve kurulum sunar. İstanbul, Almanya ve Kıbrıs ofisleriyle keşif, montaj ve servisi aynı standartta yürütürüz.</p>
      <p class="t2">Katalog 21 seriyi kapsar: kristal film ve COB’dan rental kilitli kabine, cadde DOOH’a kadar. Satış vaadi stüdyo fotoğrafı değil; ölçü, pitch ve 2 yıl garanti maddesidir.</p>
      <p class="t2">Showroom Şişli’dedir. Fine pitch, CMS film ve rental kabinleri canlı içerikle görürsünüz. Teklif kabin, kontrol, işçilik ve garanti kalemlerini ayırır.</p></div>
    </div>
    <div class="right"><div class="img-scale right-img">
      <img src="{M}/hero-indoor-led.jpg" alt="Toeled LED showroom">
    </div></div>
  </div>
  <div class="model2 public-tobody">
    <p class="public-title1">Tarihçe</p>
    <div class="swiper model3-swiper"><div class="swiper-wrapper hsms">{tl}</div></div>
  </div>
</div>
<div class="tl-prose">
  {split(f"{M}/banner-rental.jpg", "LED kiralama ve satış", "Ne satar, ne kurarız?", [
      "Sabit iç mekan (Q, NC, CMS, Mini), rental (RW, CG, LN), dış mekan (Outdoor Q/S, MG) ve aksesuar (QM, P, V).",
      "Keşif ücretsiz randevulanır. Teklif kabin + kontrol + işçilik + garanti kalemlerini ayırır.",
  ])}
  {guides([
      (f"{M}/hero-indoor-led.jpg", "Kültür", "Vizyon, misyon, saha ilkeleri.", "/corporate-culture/"),
      (f"{M}/banner-indoor.jpg", "Sertifika", "ISO / CE özeti.", "/certificates-honor/"),
      (f"{M}/showroom-istanbul.webp", "Ofisler", "İstanbul, Erkrath, Girne.", "/sales-outlets/"),
  ])}
</div>
<div class="public-tobody" style="padding-bottom:48px">
  <h2 class="public-title1">Kurumsal video</h2>
  <video controls poster="{M}/hero-indoor-led.jpg" style="width:100%;max-width:960px;border-radius:16px">
    <source src="/public/wwwroot/video/sirket.mp4" type="video/mp4">
  </video>
</div>
"""


def news_list_rich(kind: str | None, heading: str) -> str:
    items = [n for n in NEWS if kind is None or n["kind"] == kind]
    cards = "".join(
        f'<a class="tl-news-item" href="/news/{n["slug"]}/">'
        f'<img src="{n["img"]}" alt="{n["title"]}">'
        f'<div><p class="t1">{n["date"]}</p><h2>{n["title"]}</h2><p>{n["desc"]}</p></div></a>'
        for n in items
    )
    leads = {
        None: (
            "Kurumsal duyurular ve saha rehberleri. ISE, showroom, ödeme güvenliği; iç mekan pitch, rental kiralama ve dış mekan parlaklık yazıları aynı arşivde.",
            "Her yazıda görsel, bağlamsal link ve keşif çağrısı vardır. Çinçe bildiri ve sahte fuar metni yoktur.",
        ),
        "company": (
            "Fuar, showroom ve ödeme güvenliği duyuruları. Toeled / LEDAJANS resmi kanalları buradadır.",
            "Teklif ve fatura unvanı TAHA LED Dış Ticaret A.Ş. Saha keşfi İstanbul, Erkrath ve Girne ofisleriyle yürür.",
        ),
        "industry": (
            "Pitch seçimi, rental kiralama ve dış mekan parlaklığı. Rehberler keşif tutanağıyla aynı dili konuşur.",
            "Detaylı kılavuz <a href='/knowledge/'>bilgi merkezinde</a>; seri specleri ürün sayfalarındadır.",
        ),
    }
    a, b = leads[kind]
    return f"""
{banner(f"{M}/hero-indoor-led.jpg", heading)}
{crumbs([("/news/", "Haberler"), ("", heading)])}
<div class="tl-prose">
  <h1 class="public-title" style="text-align:left">{heading}</h1>
  <p class="lead">{a}</p>
  <p>{b}</p>
</div>
<div class="tl-news-list">{cards}</div>
<div class="tl-prose">
  {guides([
      (f"{M}/hero-indoor-led.jpg", "Katalog", "İç, rental, dış seriler.", "/products/"),
      (f"{M}/banner-indoor.jpg", "Bilgi merkezi", "Kurulum ve bakım.", "/knowledge/"),
      (f"{M}/showroom-istanbul.webp", "Showroom", "Şişli randevu.", "/sales-outlets/"),
  ])}
</div>
{quote("Haberdeki ürün için keşif isteyin.")}
"""


def news_article_rich(n: dict) -> str:
    return f"""
{crumbs([("/news/", "Haberler"), ("", n["title"])])}
<article class="tl-article">
  <img class="hero" src="{n["img"]}" alt="{n["title"]}">
  <p class="t1">{n["date"]}</p>
  <h1>{n["title"]}</h1>
  {n["body"]}
</article>
<div class="tl-prose">
  {guides([
      (f"{M}/hero-indoor-led.jpg", "Ürünler", "21 seri, pitch ve keşif listesi.", "/products/"),
      (f"{M}/banner-indoor.jpg", "Bilgi merkezi", "Kurulum, kullanım, bakım.", "/knowledge/"),
      (f"{M}/showroom-istanbul.webp", "Teklif", "Form ve WhatsApp.", "/contact-us/"),
  ])}
</div>
{quote()}
"""


def cases_rich(title: str, cat_filter: str | None, img: str) -> str:
    items = [c for c in CASES if cat_filter is None or c["cat"] == cat_filter]
    cards = "".join(
        f'<button class="tl-case-card" data-case="{c["id"]}" type="button">'
        f'<img src="{c["img"]}" alt="{c["title"]}">'
        f'<div class="copy"><h3>{c["title"]}</h3><p>{c["city"]} · {c["product"]} · {c["area"]}</p></div></button>'
        for c in items
    )
    dialogs = "".join(
        f'<dialog class="tl-case-modal" id="case-{c["id"]}">'
        f'<img src="{c["img"]}" alt="{c["title"]}">'
        f'<div class="body"><h2>{c["title"]}</h2>'
        f'<p>Konum: {c["city"]}<br>Ürün: {c["product"]}<br>Alan: {c["area"]}</p>'
        f'<p>{c["text"]}</p>'
        f'<form method="dialog"><button class="contact-btn">Kapat</button></form>'
        f'<p><a href="/contact-us/">Benzer proje için teklif alın</a></p></div></dialog>'
        for c in items
    )
    leads = {
        None: "İstanbul, Ankara, İzmir, Erkrath ve Girne’den sabit, rental ve DOOH örnekleri. Kartlara tıklayınca ürün, alan ve kısa saha notu açılır.",
        "indoor": "Otel lobisi, showroom, toplantı ve vitrin. Fine pitch ve kristal film işleri.",
        "rental": "Konser, fuar ve lansman. Aynı gece kurulum-söküm ve yedek oranıyla speclenen işler.",
        "dooh": "Medya cephe, billboard ve stadyum peri-led. Nit, IP ve uzaktan yayın keşifte kilitlenir.",
    }
    lead = leads[cat_filter]
    return f"""
{banner(img, title)}
{crumbs([("/cases/", "Referanslar"), ("", title)])}
<div class="tl-prose">
  <h1 class="public-title" style="text-align:left">{title}</h1>
  <p class="lead">{lead}</p>
  <p>Her iş keşif tutanağı, teslim check-list ve 2 yıl garanti (rentalde proje servisi) ile yürür. Çin lokasyonları ve sahte ödül vitrini yoktur. Benzer ölçü için <a href="/contact-us/">teklif formu</a> yeter.</p>
  {split(img, title, "Saha notu", [
      "Karttaki m² ve ürün, keşifte netleşen spece yakındır. Pitch ve kabin proje ölçüsüne göre değişebilir.",
      "Fotoğraf stüdyo veya saha çekimidir. Canlı demo için Şişli showroom randevusu +90 212 220 40 04.",
  ])}
</div>
<div class="tl-case-grid">{cards}</div>
{dialogs}
<div class="tl-prose">
  {guides([
      (f"{M}/hero-indoor-led.jpg", "İç mekan seriler", "Q, Mini, NC, CMS.", "/commercial-display/"),
      (f"{M}/hero-rental-stage.jpg", "Rental seriler", "RW, CG, LN, DM, PM.", "/rental-staging/"),
      (f"{M}/hero-outdoor-dooh.jpg", "Dış mekan", "Outdoor Q/S, MG.", "/dooh/"),
  ])}
  {faq([
      ("Bu işleri yerinde görebilir miyim?", "Showroom demosu Şişli’de. Saha referansı müşteri izniyle paylaşılır."),
      ("Aynı ürünü başka şehirde kurar mısınız?", "Evet, 81 il. Erkrath ve Girne Avrupa / KKTC işlerini taşır."),
      ("Teklif için ne gerekir?", "Ölçü, iç/dış/rental ve izleme mesafesi. Foto yeter, keşif randevulanır."),
  ])}
</div>
{quote("Benzer bir LED ekran projesi mi planlıyorsunuz?")}
<script>
document.querySelectorAll("[data-case]").forEach(function(btn){{
  btn.addEventListener("click", function(){{
    var d=document.getElementById("case-"+btn.getAttribute("data-case"));
    if(d) d.showModal();
  }});
}});
</script>
"""


TABS = [
    ("/commercial-display/", "İç Mekan"),
    ("/rental-staging/", "Kiralama & Sahne"),
    ("/dooh/", "Dış Mekan"),
    ("/accessories/", "Aksesuarlar"),
]


def tabs(active: str):
    return [(u, n, u == active) for u, n in TABS]


def main() -> None:
    n = 0
    for s in SERIES:
        page = ROOT / s["slug"] / "index.html"
        html = set_main(page.read_text(encoding="utf-8"), series_main(s))
        extra = EXTRA.get(s["slug"], {})
        desc = (extra.get("body") or [s["lead"]])[0][:155]
        write_page(page, html, f"/{s['slug']}/", f"{s['title']} | Toeled LED Ekran", desc)
        n += 1

    indoor = [x for x in SERIES if x["cat"] == "indoor"]
    rental = [x for x in SERIES if x["cat"] == "rental"]
    outdoor = [x for x in SERIES if x["slug"] in ("outdoor-q-series", "outdoor-s-series")]
    acc = [x for x in SERIES if x["slug"] in ("qm-series", "mg-series", "p-series", "v-series-")]

    cats = [
        (
            "products",
            "/products/",
            hub_main,
            PAGE_META["/products/"],
        ),
        (
            "commercial-display",
            "/commercial-display/",
            lambda: cat_page(
                "İç Mekan LED Ekran",
                [
                    "Fine pitch, COB ve kristal film serileri. Lobi, toplantı, stüdyo ve vitrin aynı katalogda; pitch izleme mesafesine göre kilitlenir.",
                    "Showroom’da Q, Mini, NC ve CMS’i yan yana görün. Teklif ölçü, native çözünürlük ve ön/arka servis yönüyle çıkar.",
                    "Ofiste düşük parlaklık, lobide gündüz okunurluk, stüdyoda kamera refresh’i ayrı speclenir. 7/24 duvarda PDC veya NC öne çıkar.",
                    "Kartlardaki kısa metin giriş içindir; seri sayfasında teknik tablo, kullanım senaryosu, keşif listesi ve SSS bulunur.",
                ],
                f"{M}/banner-indoor.jpg",
                [("/products/", "Ürünler"), ("", "İç Mekan")],
                indoor,
                tabs("/commercial-display/"),
                [
                    split(f"{M}/hero-cob-module.jpg", "COB fine pitch", "Yakın izleme", [
                        "0.9–1.5 mm COB ve Mini, stüdyo ve lobi yürüyüş mesafesinde darbeye dayanıklı yüzey ister.",
                        "4 m oturma için Mini 1.5 veya Q 1.8; daha yakın çekimde NC 0.9–1.2 önerilir.",
                    ]),
                    split(f"{M}/hero-crystal-film.jpg", "Kristal film", "Cam ve vitrin", [
                        "CMS film camı kapatmaz. Perakende ve plaza cephesinde stoğu görünür bırakır.",
                        "Gündüz vitrin, gece reklam duvarı aynı filmle çözülür. Cam tipi keşifte not edilir.",
                    ], True),
                    split(f"{M}/indoor-corporate-lobby-3c5ebf5e.jpg", "Lobi ve ofis duvarı", "Lobi ve ofis", [
                        "İç Mekan Q 1.8–2.5 otel ve plaza lobisinde en sık speclenen aralıktır.",
                        "Toplantı odasında sessiz soğutma ve 16 bit gri, karartılmış salonda bantlaşmayı keser.",
                    ]),
                ],
                [
                    ("Hangi seri lobi için?", "4–8 m izlemede İç Mekan Q 1.8–2.5; daha yakınsa Mini veya NC."),
                    ("Kristal film iç mekana mı?", "Evet, cam vitrin ve atrium. Dış cephe DOOH ayrı seridir."),
                    ("COB ne zaman şart?", "Yakın yürüyüş, stüdyo ve çarpma riski olan lobi. NC yüzey kapalı pakettir."),
                    ("7/24 kontrol odası?", "PDC Pro ve NC. Gece profili ve N+1 PSU teklife yazılır."),
                    ("Showroom’da hangileri var?", "Q, Mini, NC ve CMS randevuyla canlı. +90 212 220 40 04."),
                ],
            ),
            PAGE_META["/commercial-display/"],
        ),
        (
            "rental-staging",
            "/rental-staging/",
            lambda: cat_page(
                "Kiralama & Sahne",
                [
                    "Konser, fuar ve lansman rental kabinleri. Hızlı kilit, flight case ve yedek modül paketin parçasıdır.",
                    "İç 2.6–2.9 mm, açık hava 3.9 mm sınıfı RW/LN aileleri load-in penceresine göre speclenir.",
                    "Aynı gece kurulum-söküm, truss yükü ve jeneratör gücü keşif formunun ilk sayfasındadır. Yedek yüzde 5–10 saha çantasında durur.",
                    "Tur işlerinde Erkrath lojistiği Avrupa ayağını taşır. İstanbul stok Türkiye konser ve fuar takvimini besler.",
                ],
                f"{M}/banner-rental.jpg",
                [("/products/", "Ürünler"), ("", "Kiralama & Sahne")],
                rental,
                tabs("/rental-staging/"),
                [
                    split(f"{M}/hero-rental-stage.jpg", "Rental sahne", "Aynı gece kurulum", [
                        "Kilit pimi, eğim ve truss yükü keşif formunun ilk sayfasındadır. Yedek yüzde 5–10.",
                        "Kamera çekiminde 3840 Hz+ sınıfı refresh titremeyi keser. IMAG ve ana duvar ayrı speclenebilir.",
                    ]),
                    split(f"{M}/rental-exhibition-booth-326747a9.jpg", "Fuar standı", "Üç cephe stand", [
                        "CG hafif kabin askı yükünü düşürür. İki günde kurulum, gece söküm.",
                        "Stand üç cephe + totem için V veya Mini hibrit teklif çıkarılabilir.",
                    ], True),
                ],
                [
                    ("Sabit duvarı kiralık kabinle yapar mıyız?", "Kısa süreli evet; uzun ömürlü işte sabit Q/NC daha ekonomiktir."),
                    ("Dış mekan rental var mı?", "RW 3.9 ve LN IP opsiyonu. Yağmur planı sözleşmeye yazılır."),
                    ("Yedek oranı nedir?", "Yüzde 5–10 modül, yedek PSU ve kilit pimi saha çantasında."),
                    ("Load-in ne kadar sürer?", "Oda ölçeği birkaç saat; 80 m² konser aynı gece. Pencere sözleşmede."),
                ],
            ),
            PAGE_META["/rental-staging/"],
        ),
        (
            "dooh",
            "/dooh/",
            lambda: cat_page(
                "Dış Mekan LED Ekran",
                [
                    "Billboard, medya cephe ve stadyum. Yüksek nit, IP ve kabin ısısı fiyatı belirler.",
                    "Güney cephe gündüz ayrı parlaklık ister; tünel ve gece işi daha düşük profille çözülür. Uzaktan yayın keşifte netleşir.",
                    "Belediye izin, rüzgâr ve ankraj keşif tutanağına yazılır. Arka koridor bakım olmadan dış kabin teslim edilmez.",
                    "Outdoor Q cadde ve AVM cephe, S stadyum, MG 320×160 reklam işlerinde öne çıkar.",
                ],
                f"{M}/banner-outdoor.jpg",
                [("/products/", "Ürünler"), ("", "Dış Mekan")],
                outdoor,
                tabs("/dooh/"),
                [
                    split(f"{M}/hero-outdoor-dooh.jpg", "DOOH billboard", "Cadde ve cephe", [
                        "Outdoor Q ve MG 320×160 cadde işlerinde yaygındır. Belediye izin notu keşfe eklenir.",
                        "Uzaktan içerik fiber veya yedekli SIM ile gider. İzleme yazılımı ayrı kalem olabilir.",
                    ]),
                    split(f"{M}/outdoor-stadium-d9483c4a.jpg", "Stadyum LED", "Stadyum S serisi", [
                        "Peri-led ve tribün mesafesi 5–8 mm sınıfını seçtirir. Arka koridor bakım şarttır.",
                        "Gündüz maç yayını yüksek nit ister; gece derating profili kabini korur.",
                    ], True),
                ],
                [
                    ("IP ne kadar önemli?", "Yağmur ve tozda conta + drenaj teslim maddesidir. Kabin sınıfı teklifte görünür."),
                    ("İçerik uzaktan mı?", "Evet, fiber veya yedekli SIM. İzleme yazılımı ayrı kalem olabilir."),
                    ("Hangi pitch cadde için?", "Yaya mesafesine göre 5–8 mm. Showroom’da örnek nit izlenir, saha güneşi ayrıca ölçülür."),
                    ("İzin Toeled mi alır?", "Keşif notu ve teknik çizim verilir; belediye başvurusu müşteri veya ajansladır, desteklenir."),
                ],
            ),
            PAGE_META["/dooh/"],
        ),
        (
            "accessories",
            "/accessories/",
            lambda: cat_page(
                "Aksesuarlar",
                [
                    "Kabin, güç ve montaj setleri. QM ince kasa, MG dış döküm, P güç ve V dikey form ekran ailesini tamamlar.",
                    "Yedek PSU ve konnektör İstanbul stokludur. Ekran teklifine aksesuar adedi yazılır.",
                    "Mevcut duvar genişletme ve yedek siparişte uyum keşifte doğrulanır. Yanlış pitch/konnektör riski bu yüzden ayrı satırdır.",
                    "Statik yük ve askı detayı mimara iletilir. Totem yüksekliği V serisinde keşif ölçüsüdür.",
                ],
                f"{M}/product-slim-cabinet.jpg",
                [("/products/", "Ürünler"), ("", "Aksesuarlar")],
                acc,
                tabs("/accessories/"),
                [
                    split(f"{M}/product-slim-cabinet.jpg", "İnce kabin", "QM ve V", [
                        "Duvar kalınlığı ve totem yüksekliği mimari detaydır. Askı yükü statikçiye iletilir.",
                    ]),
                    split(f"{M}/product-modular-cabinets-b6353441.jpg", "Güç ve modül", "P serisi yedek", [
                        "7/24 duvarda N+1 PSU. Rentalde yedek modül oranı ayrı satırdır.",
                    ], True),
                ],
                [
                    ("Aksesuar tek başına satılır mı?", "Evet, mevcut duvar genişletme ve yedek için. Uyum keşifte doğrulanır."),
                    ("V Serisi URL neden tireli?", "Eski slug /v-series-/ SEO için korunur; başlık V Serisi’dir."),
                    ("N+1 PSU ne demek?", "7/24 duvarda bir PSU arızasında yayın kesilmesin diye yedek güç. P serisi kalemidir."),
                    ("MG neden aksesuar ve dış mekan?", "MG döküm kabin cadde reklamını tamamlar; katalogda aksesuar ve DOOH ile çapraz bağlanır."),
                ],
            ),
            PAGE_META["/accessories/"],
        ),
    ]
    for folder, url, fn, meta in cats:
        page = ROOT / folder / "index.html"
        write_page(page, set_main(page.read_text(encoding="utf-8"), fn()), url, meta[0], meta[1])
        n += 1

    others = [
        ("knowledge", knowledge_main, "/knowledge/"),
        ("service", service_main, "/service/"),
        ("sales-outlets", outlets_main, "/sales-outlets/"),
        ("certificates-honor", certs_main, "/certificates-honor/"),
        ("qce-cert-lookup", qce_main, "/qce-cert-lookup/"),
        ("corporate-culture", culture_main, "/corporate-culture/"),
        ("about-us", about_main, "/about-us/"),
        (
            "debugger",
            lambda: support_form_main(
                "Teknik destek",
                "Uzaktan teşhis ve saha kaydı. Formunuz İstanbul teknik ekibine düşer; WhatsApp +90 212 220 40 04.",
            ),
            "/debugger/",
        ),
        (
            "one-click-debug",
            lambda: support_form_main(
                "Tek tıkla destek",
                "Kısa form, aynı gün dönüş hedefi. Foto ve arıza tarifi teşhisi hızlandırır.",
            ),
            "/one-click-debug/",
        ),
    ]
    for folder, fn, url in others:
        page = ROOT / folder / "index.html"
        title, desc = PAGE_META[url]
        write_page(page, set_main(page.read_text(encoding="utf-8"), fn()), url, title, desc)
        n += 1

    for nitem in NEWS:
        page = ROOT / "news" / nitem["slug"] / "index.html"
        html = set_main(page.read_text(encoding="utf-8"), news_article_rich(nitem))
        write_page(page, html, f"/news/{nitem['slug']}/", f"{nitem['title']} | Toeled", nitem["desc"])
        n += 1
    lists = [
        ("news", None, "Haberler", "/news/"),
        ("company-news", "company", "Kurumsal Haberler", "/company-news/"),
        ("industry-news", "industry", "Sektör Haberleri", "/industry-news/"),
    ]
    for folder, kind, heading, url in lists:
        page = ROOT / folder / "index.html"
        title, desc = PAGE_META[url]
        write_page(page, set_main(page.read_text(encoding="utf-8"), news_list_rich(kind, heading)), url, title, desc)
        n += 1

    case_pages = [
        ("cases", None, "Referanslar", f"{M}/indoor-corporate-lobby-3c5ebf5e.jpg", "/cases/"),
        ("case-commercial-display", "indoor", "İç Mekan Referansları", f"{M}/banner-indoor.jpg", "/case-commercial-display/"),
        ("case-rental-staging", "rental", "Kiralama Referansları", f"{M}/banner-rental.jpg", "/case-rental-staging/"),
        ("case-dooh", "dooh", "Dış Mekan Referansları", f"{M}/banner-outdoor.jpg", "/case-dooh/"),
    ]
    for folder, kind, heading, img, url in case_pages:
        page = ROOT / folder / "index.html"
        title, desc = PAGE_META[url]
        write_page(page, set_main(page.read_text(encoding="utf-8"), cases_rich(heading, kind, img)), url, title, desc)
        n += 1

    print("enriched", n)


if __name__ == "__main__":
    main()
