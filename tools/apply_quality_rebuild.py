"""Rewrite Toeled page bodies: hero, products, cases, about, news, support."""
from __future__ import annotations

import re
import shutil
from pathlib import Path

from apply_chrome import PAGE_META, apply_chrome, extra_fields, url_of

ROOT = Path(__file__).resolve().parents[1]
M = "/public/wwwroot/media"

SERIES = [
    dict(slug="cms-series-crystal-film-display", title="CMS Kristal Film Ekran", cat="indoor", catn="İç Mekan", catu="/commercial-display/", pitch="CMS4 · CMS5 · CMS6 · CMS8 · CMS10", lead="Cam ve vitrin yüzeylerinde şeffaflığı koruyan kristal film LED. Mağaza cephesi ve showroom için.", hero=f"{M}/hero-crystal-film.jpg", g=[f"{M}/hero-crystal-film.jpg", f"{M}/indoor-crystal-film-b4d899d5.jpg"], feats=[("Yüksek şeffaflık", "Camı kapatmadan gece-gündüz içerik yayınlar.", f"{M}/hero-crystal-film.jpg"), ("İnce film yapı", "Mevcut cam cepheye düşük yükle uygulanır.", f"{M}/indoor-crystal-film-b4d899d5.jpg"), ("Canlı renk", "Vitrin vitrin reklamında yüksek kontrast.", f"{M}/banner-indoor.jpg"), ("Kolay servis", "Modüler tamir, kısa kesinti.", f"{M}/product-slim-cabinet.jpg")], specs=[("Piksel aralığı", "4 / 5 / 6 / 8 / 10 mm"), ("Kullanım", "İç mekan cam, vitrin"), ("Şeffaflık", "Yüksek"), ("Kurulum", "Film / cam yüzeyi"), ("Garanti", "2 yıl")]),
    dict(slug="hs-series-holographic-display", title="HS Holografik Ekran", cat="indoor", catn="İç Mekan", catu="/commercial-display/", pitch="HS3.9 · HS6.2 · HS10.4", lead="Şeffaf mesh holografik LED. Ürün lansmanı ve deneyim alanları için derinlik hissi.", hero=f"{M}/product-holographic.jpg", g=[f"{M}/product-holographic.jpg", f"{M}/hero-crystal-film.jpg"], feats=[("Mesh yapı", "Arkası görünen şeffaf LED perde.", f"{M}/product-holographic.jpg"), ("Sahne etkisi", "Lansman ve deneyim odalarında 3B his.", f"{M}/hero-rental-stage.jpg"), ("Hafif kabin", "Askı ve truss kurulumuna uygun.", f"{M}/product-slim-cabinet.jpg"), ("Yüksek yenileme", "Kamera çekiminde titreme yok.", f"{M}/hero-cob-module.jpg")], specs=[("Piksel aralığı", "3.9 / 6.2 / 10.4 mm"), ("Kullanım", "İç mekan sahne / deneyim"), ("Yapı", "Holografik mesh"), ("Refresh", "3840 Hz+"), ("Garanti", "2 yıl")]),
    dict(slug="q-mini-series", title="Q Mini Serisi", cat="indoor", catn="İç Mekan", catu="/commercial-display/", pitch="Q Mini 1.2 · 1.5 · 1.8", lead="Kompakt kabinli fine pitch iç mekan duvarı. Toplantı ve kontrol odaları.", hero=f"{M}/hero-cob-module.jpg", g=[f"{M}/hero-cob-module.jpg", f"{M}/banner-indoor.jpg"], feats=[("İnce pitch", "Yakın izleme mesafesinde keskin görüntü.", f"{M}/hero-cob-module.jpg"), ("Küçük kabin", "Dar niş ve toplantı odasına sığar.", f"{M}/product-cabinet-studio.jpg"), ("Sessiz çalışma", "Ofis ortamına uygun termal tasarım.", f"{M}/banner-indoor.jpg"), ("16 bit gri", "Düşük parlaklıkta homojenlik.", f"{M}/indoor-corporate-lobby-3c5ebf5e.jpg")], specs=[("Piksel aralığı", "1.2 / 1.5 / 1.8 mm"), ("Kullanım", "İç mekan sabit"), ("Refresh", "3840 Hz"), ("Kabin", "Mini die-cast"), ("Garanti", "2 yıl")]),
    dict(slug="nc-series", title="NC COB Serisi", cat="indoor", catn="İç Mekan", catu="/commercial-display/", pitch="NC0.9 · NC1.2", lead="COB paketleme ile darbeye dayanıklı fine pitch. Stüdyo ve lobi duvarları.", hero=f"{M}/hero-cob-module.jpg", g=[f"{M}/hero-cob-module.jpg", f"{M}/product-cabinet-studio.jpg"], feats=[("COB yüzey", "Çarpma ve toza karşı korumalı modül.", f"{M}/hero-cob-module.jpg"), ("Ortak anot/katot", "Düşük ısı, yüksek enerji verimi.", f"{M}/product-cabinet-studio.jpg"), ("Stüdyo uyumu", "Yayın kameralarında siyah seviyesi.", f"{M}/banner-indoor.jpg"), ("Uzun ömür", "Tek tip LED seçimi.", f"{M}/indoor-showroom-acfc9661.jpg")], specs=[("Piksel aralığı", "0.9 / 1.2 mm"), ("Paket", "COB"), ("Kullanım", "İç mekan stüdyo / lobi"), ("Koruma", "Darbeye dayanıklı yüzey"), ("Garanti", "2 yıl")]),
    dict(slug="indoor-q-series", title="İç Mekan Q Serisi", cat="indoor", catn="İç Mekan", catu="/commercial-display/", pitch="Q0.8 – Q4", lead="Ofis, fuar, stüdyo ve perakendede en çok tercih edilen iç mekan sabit LED ailesi.", hero=f"{M}/indoor-corporate-lobby-3c5ebf5e.jpg", g=[f"{M}/indoor-corporate-lobby-3c5ebf5e.jpg", f"{M}/banner-indoor.jpg", f"{M}/product-cabinet-studio.jpg"], feats=[("Dinamik enerji", "PWM sürücü ve akıllı karartma ile tasarruf.", f"{M}/hero-cob-module.jpg"), ("Yüksek yenileme", "Titreşimsiz, kamera dostu görüntü.", f"{M}/banner-indoor.jpg"), ("Geniş gri ton", "Düşük ışıklı sahnede detay.", f"{M}/indoor-corporate-lobby-3c5ebf5e.jpg"), ("Tek batch LED", "Renk ve parlaklık homojenliği.", f"{M}/product-cabinet-studio.jpg")], specs=[("Piksel aralığı", "0.8 – 4 mm"), ("Kullanım", "İç mekan sabit duvar"), ("Refresh", "3840–7680 Hz"), ("Gri ton", "16 bit"), ("Garanti", "2 yıl")]),
    dict(slug="pdc-series", title="PDC Serisi", cat="indoor", catn="İç Mekan", catu="/commercial-display/", pitch="PDC0.9 Pro · PDC1.2 Pro · PDC1.5 Pro", lead="Komuta ve kontrol odaları için yüksek doluluk, 7/24 çalışan fine pitch.", hero=f"{M}/banner-indoor.jpg", g=[f"{M}/banner-indoor.jpg", f"{M}/hero-cob-module.jpg"], feats=[("7/24 çalışma", "Kontrol odası parlaklık profili.", f"{M}/banner-indoor.jpg"), ("Pro pitch", "0.9 / 1.2 / 1.5 mm seçenekleri.", f"{M}/hero-cob-module.jpg"), ("Servis önden", "Dar koridorlarda bakım.", f"{M}/product-cabinet-studio.jpg"), ("Düşük ısınma", "Sessiz soğutma.", f"{M}/indoor-hotel-reception-bf0db49.jpg")], specs=[("Piksel aralığı", "0.9 / 1.2 / 1.5 mm Pro"), ("Kullanım", "Kontrol / toplantı"), ("Çalışma", "7/24"), ("Servis", "Ön bakım"), ("Garanti", "2 yıl")]),
    dict(slug="mk-series", title="MK Serisi", cat="indoor", catn="İç Mekan", catu="/commercial-display/", pitch="MK iç mekan", lead="Kavis ve köşe uygulamalarına uygun esnek iç mekan LED.", hero=f"{M}/indoor-mall-atrium-8903fa23.jpg", g=[f"{M}/indoor-mall-atrium-8903fa23.jpg", f"{M}/product-cabinet-studio.jpg"], feats=[("Kavis", "İçbükey-dışbükey duvar.", f"{M}/indoor-mall-atrium-8903fa23.jpg"), ("Köşe birleşim", "Kesintisiz 90° dönüş.", f"{M}/indoor-corporate-lobby-3c5ebf5e.jpg"), ("Perakende", "AVM atrium ve marka duvarı.", f"{M}/case-mall-facade.jpg"), ("Hızlı kurulum", "Manyetik modül.", f"{M}/product-slim-cabinet.jpg")], specs=[("Uygulama", "Kavis / köşe"), ("Kullanım", "İç mekan perakende"), ("Montaj", "Manyetik modül"), ("Garanti", "2 yıl")]),
    dict(slug="indoor-r-series", title="İç Mekan R Serisi", cat="indoor", catn="İç Mekan", catu="/commercial-display/", pitch="R iç mekan", lead="Toplantı, eğitim ve devlet projelerinde sabit iç mekan kabin.", hero=f"{M}/indoor-corporate-lobby-3c5ebf5e.jpg", g=[f"{M}/indoor-corporate-lobby-3c5ebf5e.jpg", f"{M}/banner-indoor.jpg"], feats=[("Kurumsal", "Toplantı ve eğitim salonları.", f"{M}/banner-indoor.jpg"), ("Stabil kabin", "Duvar ve zemin sehpa.", f"{M}/product-cabinet-studio.jpg"), ("Renk kalibrasyonu", "Çoklu duvar eşlemesi.", f"{M}/hero-cob-module.jpg"), ("Yedek parça", "Türkiye stoklu servis.", f"{M}/showroom-istanbul.webp")], specs=[("Kullanım", "İç mekan sabit"), ("Senaryo", "Toplantı / eğitim"), ("Servis", "TR yedek parça"), ("Garanti", "2 yıl")]),
    dict(slug="cs-series", title="CS Serisi", cat="indoor", catn="İç Mekan", catu="/commercial-display/", pitch="CS iç mekan", lead="Sinema ve sahne izleme için yüksek kontrast iç mekan duvarı.", hero=f"{M}/indoor-hotel-reception-bf0db49.jpg", g=[f"{M}/indoor-hotel-reception-bf0db49.jpg", f"{M}/hero-indoor-led.jpg"], feats=[("Yüksek kontrast", "Karanlık salonlarda siyah seviyesi.", f"{M}/hero-indoor-led.jpg"), ("Geniş açı", "Salon oturma düzenine uygun.", f"{M}/indoor-hotel-reception-bf0db49.jpg"), ("Sessiz", "Sinema salonu gürültü eşiği.", f"{M}/banner-indoor.jpg"), ("İçerik", "HDR uyumlu işleme.", f"{M}/hero-cob-module.jpg")], specs=[("Kullanım", "Sinema / salon"), ("Kontrast", "Yüksek"), ("Kullanım yeri", "İç mekan"), ("Garanti", "2 yıl")]),
    dict(slug="n-series", title="N Serisi", cat="indoor", catn="İç Mekan", catu="/commercial-display/", pitch="N iç mekan", lead="Narrow pixel, yayın ve stüdyo LED zemini / duvarı.", hero=f"{M}/indoor-mall-atrium-2c3839d5.jpg", g=[f"{M}/indoor-mall-atrium-2c3839d5.jpg", f"{M}/hero-cob-module.jpg"], feats=[("Yayın", "Stüdyo kamera uyumu.", f"{M}/hero-cob-module.jpg"), ("Dar pitch", "Yakın çekim.", f"{M}/hero-indoor-led.jpg"), ("Zemin seçeneği", "LED floor opsiyonu.", f"{M}/product-cabinet-studio.jpg"), ("Kalibrasyon", "Modül eşleme.", f"{M}/banner-indoor.jpg")], specs=[("Kullanım", "Stüdyo / yayın"), ("Pitch", "Fine / N serisi"), ("Garanti", "2 yıl")]),
    dict(slug="rw-series", title="RW Serisi", cat="rental", catn="Kiralama & Sahne", catu="/rental-staging/", pitch="İç RW2.6 · RW2.9 · Dış RW3.9", lead="İç-dış rental kabin. Konser ve tur için hızlı kilitli bağlantı.", hero=f"{M}/hero-rental-stage.jpg", g=[f"{M}/hero-rental-stage.jpg", f"{M}/rental-concert-stage-84bd91a8.jpg"], feats=[("Hızlı kilit", "Curving ve düz duvar aynı gece.", f"{M}/banner-rental.jpg"), ("İç-dış", "2.6 / 2.9 iç, 3.9 dış.", f"{M}/hero-rental-stage.jpg"), ("Flight case", "Tur lojistiğine uygun.", f"{M}/rental-flight-cases-fd0c4e92.jpg"), ("Yüksek refresh", "Yayın ve konser kamerası.", f"{M}/rental-concert-stage-84bd91a8.jpg")], specs=[("Piksel aralığı", "2.6 / 2.9 / 3.9 mm"), ("Kullanım", "Rental iç / dış"), ("Kabin", "Hızlı kilit"), ("Garanti", "Kiralama süresi + servis")]),
    dict(slug="cg-series", title="CG Serisi", cat="rental", catn="Kiralama & Sahne", catu="/rental-staging/", pitch="CG rental", lead="Hafif carbon-görünümlü rental kabin, truss askı ve zemin stack.", hero=f"{M}/banner-rental.jpg", g=[f"{M}/banner-rental.jpg", f"{M}/rental-exhibition-booth-326747a9.jpg"], feats=[("Hafif", "Askı yükünü düşürür.", f"{M}/product-slim-cabinet.jpg"), ("Fuar", "Stand üç cephe duvar.", f"{M}/rental-exhibition-booth-326747a9.jpg"), ("Hızlı söküm", "Gece kurulum.", f"{M}/banner-rental.jpg"), ("Yedek", "Sahada hot-swap modül.", f"{M}/rental-flight-cases-e7055c60.jpg")], specs=[("Kullanım", "Rental / fuar"), ("Ağırlık", "Hafif kabin"), ("Garanti", "Proje bazlı")]),
    dict(slug="ln-series", title="LN Serisi", cat="rental", catn="Kiralama & Sahne", catu="/rental-staging/", pitch="LN rental", lead="Lineer sahne LED, ana ekran ve kanatlar için.", hero=f"{M}/rental-concert-stage-84bd91a8.jpg", g=[f"{M}/rental-concert-stage-84bd91a8.jpg", f"{M}/hero-rental-stage.jpg"], feats=[("Sahne", "Ana ekran ve IMAG.", f"{M}/hero-rental-stage.jpg"), ("Kanat", "Lineer uzatma.", f"{M}/rental-concert-stage-84bd91a8.jpg"), ("IP opsiyon", "Açık hava festival.", f"{M}/banner-outdoor.jpg"), ("Hız", "Hızlı kilit.", f"{M}/banner-rental.jpg")], specs=[("Kullanım", "Konser / festival"), ("Kurulum", "Stack / fly"), ("Garanti", "Proje bazlı")]),
    dict(slug="dm-series", title="DM Serisi", cat="rental", catn="Kiralama & Sahne", catu="/rental-staging/", pitch="DM rental", lead="Çizgisel kasa tasarımıyla modern rental duvar; tur ve TV çekimi.", hero=f"{M}/rental-exhibition-booth-326747a9.jpg", g=[f"{M}/rental-exhibition-booth-326747a9.jpg", f"{M}/product-cabinet-studio.jpg"], feats=[("Modern kasa", "İnce çerçeve, sahne estetiği.", f"{M}/product-cabinet-studio.jpg"), ("TV çekimi", "Yüksek refresh.", f"{M}/hero-rental-stage.jpg"), ("Hafif", "Ekip taşıma yükü düşük.", f"{M}/product-slim-cabinet.jpg"), ("Servis", "Ön-arka bakım.", f"{M}/banner-rental.jpg")], specs=[("Kullanım", "Rental / yayın"), ("Kasa", "İnce çerçeve"), ("Garanti", "Proje bazlı")]),
    dict(slug="pm-series", title="PM Serisi", cat="rental", catn="Kiralama & Sahne", catu="/rental-staging/", pitch="PM rental", lead="Panel-modül rental, yedekleme ve hızlı değişim odaklı.", hero=f"{M}/rental-flight-cases-fd0c4e92.jpg", g=[f"{M}/rental-flight-cases-fd0c4e92.jpg", f"{M}/banner-rental.jpg"], feats=[("Modül yedek", "Sahada dakika içinde değişim.", f"{M}/rental-flight-cases-fd0c4e92.jpg"), ("Tur", "Flight case set.", f"{M}/rental-flight-cases-e7055c60.jpg"), ("Kilit", "Hızlı kilit pim.", f"{M}/banner-rental.jpg"), ("Karışık pitch", "İç-dış set.", f"{M}/hero-rental-stage.jpg")], specs=[("Kullanım", "Rental yedekleme"), ("Lojistik", "Flight case"), ("Garanti", "Proje bazlı")]),
    dict(slug="outdoor-q-series", title="Dış Mekan Q Serisi", cat="outdoor", catn="Dış Mekan", catu="/dooh/", pitch="Q5 · Q6.6 · Q8", lead="Cadde, AVM cephe ve otobüs durakları için yüksek parlaklık dış mekan LED.", hero=f"{M}/hero-outdoor-dooh.jpg", g=[f"{M}/hero-outdoor-dooh.jpg", f"{M}/outdoor-billboard-city-277519d0.jpg"], feats=[("Yüksek nit", "Güneş altında okunur.", f"{M}/hero-outdoor-dooh.jpg"), ("IP koruma", "Yağmur ve toz.", f"{M}/banner-outdoor.jpg"), ("Uzaktan yayın", "DOOH içerik.", f"{M}/outdoor-billboard-day-adc08566.jpg"), ("Alüminyum kabin", "Dış ortam ısısı.", f"{M}/product-cabinet-studio.jpg")], specs=[("Piksel aralığı", "5 / 6.6 / 8 mm sınıfı"), ("Parlaklık", "Yüksek nit"), ("IP", "Dış mekan"), ("Garanti", "2 yıl")]),
    dict(slug="outdoor-s-series", title="Dış Mekan S Serisi", cat="outdoor", catn="Dış Mekan", catu="/dooh/", pitch="S5 · S6.6 · S8", lead="Stadyum, peri-led ve büyük format DOOH için S serisi kabin.", hero=f"{M}/banner-outdoor.jpg", g=[f"{M}/banner-outdoor.jpg", f"{M}/outdoor-stadium-d9483c4a.jpg"], feats=[("Stadyum", "Uzun izleme mesafesi.", f"{M}/outdoor-stadium-d9483c4a.jpg"), ("Dayanım", "Rüzgar ve titreşim.", f"{M}/banner-outdoor.jpg"), ("Servis", "Arka koridor bakım.", f"{M}/product-cabinet-studio.jpg"), ("Yüksek parlaklık", "Gündüz maç yayını.", f"{M}/hero-outdoor-dooh.jpg")], specs=[("Piksel aralığı", "5 / 6.6 / 8 mm"), ("Kullanım", "Stadyum / DOOH"), ("IP", "Dış mekan"), ("Garanti", "2 yıl")]),
    dict(slug="qm-series", title="QM Serisi", cat="acc", catn="Aksesuarlar", catu="/accessories/", pitch="640×480 çok amaçlı kabin", lead="İnce alüminyum 640×480 kabin; iç-dış çok amaçlı duvar ve kolon.", hero=f"{M}/product-slim-cabinet.jpg", g=[f"{M}/product-slim-cabinet.jpg", f"{M}/product-cabinet-studio.jpg"], feats=[("İnce kasa", "Duvar kalınlığını düşürür.", f"{M}/product-slim-cabinet.jpg"), ("640×480", "Standart modül uyumu.", f"{M}/product-cabinet-studio.jpg"), ("Çok amaç", "İç ve yarı açık alan.", f"{M}/banner-indoor.jpg"), ("Hafif", "Asma tavan / duvar.", f"{M}/product-modular-cabinets-9ef30032.jpg")], specs=[("Kabin", "640×480 mm"), ("Malzeme", "Alüminyum"), ("Kullanım", "Çok amaçlı"), ("Garanti", "2 yıl")]),
    dict(slug="mg-series", title="MG Serisi", cat="outdoor", catn="Aksesuarlar", catu="/accessories/", pitch="Q/S5 · Q/S6.6 · Q/S8", lead="Dış mekan döküm alüminyum kabin, 320×160 modül, cadde reklamı.", hero=f"{M}/product-cabinet-studio.jpg", g=[f"{M}/product-cabinet-studio.jpg", f"{M}/outdoor-billboard-city-71e8a6fe.jpg"], feats=[("Döküm kabin", "Dış ortam su ve toz.", f"{M}/product-cabinet-studio.jpg"), ("320×160", "Yaygın dış mekan modül.", f"{M}/hero-outdoor-dooh.jpg"), ("Cadde", "Billboard ve durak.", f"{M}/outdoor-billboard-city-277519d0.jpg"), ("Servis", "Arka kapak bakım.", f"{M}/banner-outdoor.jpg")], specs=[("Modül", "320×160 mm"), ("Pitch", "5 / 6.6 / 8 mm"), ("Kullanım", "Dış mekan reklam"), ("Garanti", "2 yıl")]),
    dict(slug="p-series", title="P Serisi", cat="acc", catn="Aksesuarlar", catu="/accessories/", pitch="P kabin / güç", lead="Güç kaynağı ve kabin aksesuar ailesi. Proje setini tamamlar.", hero=f"{M}/product-modular-cabinets-b6353441.jpg", g=[f"{M}/product-modular-cabinets-b6353441.jpg", f"{M}/product-slim-cabinet.jpg"], feats=[("Güç", "Yedekli PSU seçenekleri.", f"{M}/product-slim-cabinet.jpg"), ("Kabin uyumu", "Q / rental aileleri.", f"{M}/product-cabinet-studio.jpg"), ("Kablolama", "Hızlı konnektör.", f"{M}/rental-flight-cases-fd0c4e92.jpg"), ("Stok", "İstanbul yedek.", f"{M}/showroom-istanbul.webp")], specs=[("Tip", "Kabin / güç aksesuar"), ("Uyum", "Toeled serileri"), ("Garanti", "2 yıl")]),
    dict(slug="v-series-", title="V Serisi", cat="acc", catn="Aksesuarlar", catu="/accessories/", pitch="V kabin", lead="Dikey ve yaratıcı ekran kurulumları için V serisi aksesuar kabin.", hero=f"{M}/product-slim-cabinet.jpg", g=[f"{M}/product-slim-cabinet.jpg", f"{M}/product-holographic.jpg"], feats=[("Dikey", "Sütun ve totem.", f"{M}/product-slim-cabinet.jpg"), ("Yaratıcı", "Özel form destek.", f"{M}/product-holographic.jpg"), ("Hafif", "İç mekan asma.", f"{M}/banner-indoor.jpg"), ("Servis", "Hızlı klips.", f"{M}/product-cabinet-studio.jpg")], specs=[("Kullanım", "Totem / dikey"), ("Kabin", "V serisi"), ("Garanti", "2 yıl")]),
]

CASES = [
    dict(id="ist-otel", title="İstanbul otel lobisi", city="İstanbul", cat="indoor", img=f"{M}/indoor-corporate-lobby-3c5ebf5e.jpg", product="İç Mekan Q 1.8", area="32 m²", text="5 yıldızlı otel karşılama duvarı. Fine pitch, gündüz lobisinde okunur içerik."),
    dict(id="ist-showroom", title="Şişli showroom duvarı", city="İstanbul", cat="indoor", img=f"{M}/showroom-istanbul.webp", product="Q Mini 1.5", area="18 m²", text="LEDAJANS showroom ana duvarı. Müşteri keşif toplantılarında canlı demo."),
    dict(id="ank-ofis", title="Ankara toplantı salonu", city="Ankara", cat="indoor", img=f"{M}/banner-indoor.jpg", product="NC 1.2 COB", area="12 m²", text="Kurumsal toplantı odası. COB yüzey, yakın oturma mesafesi."),
    dict(id="izm-magaza", title="İzmir mağaza vitrini", city="İzmir", cat="indoor", img=f"{M}/hero-crystal-film.jpg", product="CMS Kristal Film", area="9 m²", text="Cam vitrinde şeffaf LED film. Vitrin stoğu görünür kalır."),
    dict(id="ist-konser", title="İstanbul konser sahnesi", city="İstanbul", cat="rental", img=f"{M}/rental-concert-stage-84bd91a8.jpg", product="RW 2.9", area="80 m²", text="Açık hava konser ana ekranı. Aynı gece kurulum-söküm."),
    dict(id="fuar-tr", title="Fuar standı LED", city="İstanbul", cat="rental", img=f"{M}/rental-exhibition-booth-326747a9.jpg", product="CG Serisi", area="24 m²", text="Üç cepheli fuar standı. İki günde kurulum."),
    dict(id="lansman", title="Ürün lansmanı", city="İstanbul", cat="rental", img=f"{M}/hero-rental-stage.jpg", product="LN Serisi", area="40 m²", text="Otomotiv lansmanı IMAG ve ana duvar."),
    dict(id="erkrath", title="Erkrath ofis duvarı", city="Erkrath", cat="indoor", img=f"{M}/indoor-showroom-696ea4ce.jpg", product="İç Mekan Q 2.5", area="10 m²", text="Almanya ofisi toplantı ekranı."),
    dict(id="girne", title="Girne vitrin LED", city="Girne", cat="indoor", img=f"{M}/indoor-hotel-reception-5bfd9e63.jpg", product="Q Mini 1.8", area="8 m²", text="Kıbrıs showroom vitrin duvarı."),
    dict(id="ist-cephe", title="İstanbul medya cephe", city="İstanbul", cat="dooh", img=f"{M}/case-mall-facade.jpg", product="Dış Mekan Q5", area="64 m²", text="AVM cephe DOOH. Uzaktan içerik."),
    dict(id="ank-billboard", title="Ankara billboard", city="Ankara", cat="dooh", img=f"{M}/hero-outdoor-dooh.jpg", product="MG 6.6", area="48 m²", text="Cadde billboard, yüksek nit."),
    dict(id="stadyum", title="Stadyum peri-led", city="İstanbul", cat="dooh", img=f"{M}/outdoor-stadium-d9483c4a.jpg", product="Dış Mekan S", area="120 m²", text="Tribün çevresi bilgilendirme ve reklam."),
]

NEWS = [
    dict(
        slug="ise-2026-toeled-led-ekran",
        date="7 Şubat 2026",
        kind="company",
        title="ISE 2026’da Toeled LED ekran çözümleri",
        desc="Barcelona ISE’de iç mekan, rental ve DOOH serilerimizi iş ortaklarıyla paylaştık.",
        img=f"{M}/hero-rental-stage.jpg",
        body="""<p>Toeled, LEDAJANS çatısında ISE 2026’da iç mekan fine pitch, rental sahne ve dış mekan DOOH çözümlerini sergiledi. Keşif ve teklif süreçlerimizi Avrupa entegratörleriyle aynı masada yürüttük; ölçü, pitch ve garanti maddesi fuar standında da aynı dildi.</p>
<p>Öne çıkanlar: NC COB yakın izleme, RW rental hızlı kilit ve yüksek parlaklık dış mekan kabinleri. Kamera önünde 3840 Hz+ sınıfı yayın, stüdyo ve IMAG işlerinde titremeyi kesti. CMS kristal film vitrin demosu cam stoğunu kapatmadan gece içeriğini gösterdi.</p>
<p>Fuar sonrası kurulum talepleri İstanbul, Erkrath ve Girne ofislerine düştü. Türkiye işleri Şişli showroom ve saha ekibiyle, AB işleri Erkrath lojistiğiyle, KKTC işleri Girne keşfiyle yürür. Sahte bayi haritası veya Çin saat dilimi teklifte yoktur.</p>
<p>ISE’de konuşulan specler <a href="/products/">ürün kataloğunda</a> duruyor. Randevu ve keşif için <a href="/contact-us/">teklif formu</a> veya +90 212 220 40 04.</p>""",
    ),
    dict(
        slug="istanbul-led-ekran-showroom",
        date="12 Mart 2026",
        kind="company",
        title="İstanbul LED ekran showroom’u yenilendi",
        desc="Şişli’de fine pitch, kristal film ve rental kabinleri yan yana deneyin.",
        img=f"{M}/showroom-istanbul.webp",
        body="""<p>Halide Edip Adıvar’daki showroom’da İç Mekan Q, CMS kristal film ve rental kabinleri canlı içerikle görürsünüz. Aynı slaytı 1.5 mm Mini ile 2.5 mm Q üzerinde yan yana izlemek pitch kararını spekülasyondan çıkarır.</p>
<p>NC COB yüzey yakın yürüyüş ve stüdyo demosu içindir. Rental kabin ve flight case load-in konuşması için salondadır. Ölçü krokinizi getirin; aynı gün ön teklif kalemleri (kabin, kontrol, işçilik, garanti) çıkarılır.</p>
<p>Randevu: info@ledajans.com veya +90 212 220 40 04. Adres: Gül 2 Sk. No:10a, Şişli. Erkrath ve Girne müşterileri de İstanbul demosunu video veya saha keşfiyle tamamlar.</p>
<p>Katalog ve keşif süreci <a href="/sales-outlets/">satış noktaları</a> ve <a href="/knowledge/">bilgi merkezi</a> sayfalarında yazılıdır.</p>""",
    ),
    dict(
        slug="odeme-guvenligi-uyarisi",
        date="14 Ekim 2025",
        kind="company",
        title="Ödeme güvenliği uyarısı",
        desc="Ödemeleri yalnızca TAHA LED Dış Ticaret A.Ş. unvanına yapın.",
        img=f"{M}/banner-indoor.jpg",
        body="""<p>TAHA LED Dış Ticaret A.Ş. / Toeled olarak ödemeleri yalnızca şirket unvanımıza ait hesaplara kabul ederiz. Personel adı, kişisel IBAN veya “acil havale” taleplerini işleme almayın; satış temsilcinizi arayın.</p>
<p>Doğrulama kanalları: +90 212 220 40 04 ve info@ledajans.com. Sözleşme ve proforma unvanı TAHA LED Dış Ticaret A.Ş. olmalıdır. Farklı unvan veya yurt dışı şahıs hesabı Toeled ödemesi değildir.</p>
<p>Şüpheli mail, WhatsApp veya sahte fatura görürseniz transfer etmeden önce ofisi arayın. Bu duyuru ISE ve fuar dönemlerinde de geçerlidir.</p>
<p>Teklif ve fatura süreci <a href="/contact-us/">iletişim</a> formundan yürür.</p>""",
    ),
    dict(
        slug="ic-mekan-led-ekran-nasil-secilir",
        date="4 Nisan 2026",
        kind="industry",
        title="İç mekan LED ekran nasıl seçilir?",
        desc="İzleme mesafesi, pitch, parlaklık ve kabin: tekliften önce netleşmesi gerekenler.",
        img=f"{M}/hero-indoor-led.jpg",
        body="""<p>İç mekan LED ekranda doğru pitch, izleme mesafesinin kabaca 1 mm ≈ 1 m kuralıyla başlar. 4 m oturma için 1.5–2.5 mm; stüdyo ve lobi yakınında COB 0.9–1.5 mm öne çıkar. Bu kural slayt metni ve video için geçerlidir; kamera çekiminde refresh ayrıca speclenir.</p>
<p>Parlaklık ofiste düşük tutulur; vitrin ve gündüz lobisinde daha yüksek profil gerekir. 7/24 çalışan duvarda ısınma, pixel shift ve servis yönü (ön/arka) teklife yazılır. Dar koridorda ön bakımlı kabin, arka serviste yaklaşık 80 cm boşluk şarttır.</p>
<p>Native çözünürlük içerik iş akışını kilitler. Ölçeklenmiş 4K fine pitch’te yumuşar. Küçük toplantıda laptop yeter; büyük lobi ve yayın işinde ayrı oynatıcı + LED işlemci önerilir.</p>
<p>Toeled keşifte ölçü, içerik ve kontrolü birlikte önerir. Seriler: <a href="/indoor-q-series/">İç Mekan Q</a>, <a href="/q-mini-series/">Q Mini</a>, <a href="/nc-series/">NC COB</a>, <a href="/cms-series-crystal-film-display/">CMS film</a>. Kılavuz: <a href="/knowledge/">bilgi merkezi</a>.</p>""",
    ),
    dict(
        slug="rental-led-ekran-sahne-kiralama",
        date="18 Mayıs 2026",
        kind="industry",
        title="Rental LED ekran: sahne kiralama rehberi",
        desc="Konser ve fuarda kabin, kilit, flight case ve yedek parça.",
        img=f"{M}/hero-rental-stage.jpg",
        body="""<p>Rental LED ekran, sabit duvardan farklı olarak her gece sökülür. Hızlı kilit, eğim (curve), uçuş kasası ve yüzde 5–10 yedek modül şarttır. Load-in penceresi sözleşmenin ilk maddesidir; aynı gece kurulum-söküm konser işinin gerçeğidir.</p>
<p>İç mekan 2.6–2.9 mm, açık hava 3.9 mm sınıfı RW/LN aileleri konser ve fuarda kullanılır. CG hafif kabin fuar askı yükünü düşürür. DM ince çerçeve TV çekimine yakındır. PM yedekleme ve hot-swap odaklıdır.</p>
<p>Jeneratör gücü, truss yükü ve yağmur planı keşif formuna eklenir. Saha çantasında yedek PSU, alıcı kart ve kilit pimi durur. Tur işlerinde Erkrath lojistiği Avrupa ayağını, İstanbul stok Türkiye ayağını taşır.</p>
<p>Seriler: <a href="/rw-series/">RW</a>, <a href="/cg-series/">CG</a>, <a href="/ln-series/">LN</a>. Süreç: <a href="/rental-staging/">kiralama &amp; sahne</a> ve <a href="/service/">servis</a>.</p>""",
    ),
    dict(
        slug="dis-mekan-led-ekran-parlaklik",
        date="9 Haziran 2026",
        kind="industry",
        title="Dış mekan LED ekran parlaklığı",
        desc="Gündüz okunurluk, IP ve DOOH uzaktan yayın.",
        img=f"{M}/hero-outdoor-dooh.jpg",
        body="""<p>Dış mekan LED ekranda parlaklık (nit), IP ve kabin ısısı üçlüsü fiyatı belirler. Güney cephe billboard gündüz yüksek nit ister; tünel ve gece ağırlıklı yayın daha düşük profille çözülür. Gece derating hem komşuluk hem kabin ömrü içindir.</p>
<p>MG ve Outdoor Q/S serilerinde 320×160 modül ve döküm kabin cadde projelerinde yaygındır. Stadyum peri-led’de tribün mesafesi 5–8 mm sınıfını seçtirir. Arka koridor bakım ve conta/drenaj teslim maddesidir.</p>
<p>Uzaktan içerik için kontrol, fiber veya yedekli SIM keşifte netleşir. Belediye izin notu ve rüzgâr yükü tutanağa yazılır. İzleme yazılımı ayrı kalem olabilir.</p>
<p>Seriler: <a href="/outdoor-q-series/">Outdoor Q</a>, <a href="/outdoor-s-series/">Outdoor S</a>, <a href="/mg-series/">MG</a>. Keşif: <a href="/dooh/">dış mekan</a> ve <a href="/contact-us/">iletişim</a>.</p>""",
    ),
]

OLD_NEWS_REDIRECT = {
    "qiangli-led-successfully-concludes-ise-2026": "ise-2026-toeled-led-ekran",
    "join-us-at-ise-spain-2026-to-explore-the-future-of-led-display-technology": "ise-2026-toeled-led-ekran",
    "-qiangli-jucai-overseas-order-payment-account-statement-": "odeme-guvenligi-uyarisi",
    "celebrating-the-successful-conclusion-of-qiangli-led-s-20th-anniversary-event": "istanbul-led-ekran-showroom",
    "qiangli-jucai-has-landed-on-the-nasdaq-screen-in-times-square-new-york": "istanbul-led-ekran-showroom",
    "qiangli-jucai-deepens-middle-east-layout-secures-strategic-cooperation-on-led-display-with-jordan-s-al-bahhar-est-": "ic-mekan-led-ekran-nasil-secilir",
    "the-9thpanel-made-a-successful-debut-at-the-ise-show-in-spain-receiving-a-flood-of-positive-feedback-from-customers-": "ise-2026-toeled-led-ekran",
    "topping-sales-again-strong-giant-color-captures-the-first-place-in-led-display-sales-demonstrating-the-kingly-demeanor-with-channel-advantages-": "dis-mekan-led-ekran-parlaklik",
}

SWEEP = [
    ("微软雅黑, Microsoft YaHei", "Figtree, sans-serif"),
    ("Microsoft YaHei", "Figtree"),
    ("Pixel Spacing", "Piksel aralığı"),
    ("Common Anode", "Ortak anot"),
    ("Common Cathode", "Ortak katot"),
    ("Beijing Time, For Other Time, Please Arrange With Sales In Advance, Thank You", "Türkiye saati. Diğer saat dilimleri için satış ekibiyle planlayın."),
    ("Installation Services", "Kurulum hizmetleri"),
    ("Scheme Customization", "Çözüm tasarımı"),
    ("Bidding Cooperation", "İhale desteği"),
    ("lnstallation and debugging", "Kurulum ve ayar"),
    ("Usage Guide", "Kullanım kılavuzu"),
    ("Repair and maintenance", "Onarım ve bakım"),
    ("Please Enter Keywords For Search", "Anahtar kelime arayın"),
    ("Entry Name", "Proje adı"),
    ("Application Products", "Kullanılan ürün"),
    ("Project Area", "Proje alanı"),
    ("Previous Case", "Önceki referans"),
    ("Next Case", "Sonraki referans"),
    ("HS Series", "HS Serisi"),
    ("Mk Series", "MK Serisi"),
    ("Exhibition and Display", "Fuar ve sergi"),
    ("Smart Meeting", "Toplantı"),
    ("Dış mekan media", "Dış mekan medya"),
    ("Toeled was founded in Quanzhou, Fujian", "Toeled, LEDAJANS çatısında İstanbul merkezli LED ekran çözümleri sunar."),
    ("VR Visit to Qiangli Industrial Park", "Showroom ziyareti"),
    ("Create a World-class Great Kurum", "Türkiye, Almanya ve Kıbrıs’ta güvenilir LED partneri olmak"),
    ("User first, beautiful display, with the mission of popularizing LED displays, creating a better life for employees", "Doğru ürün, net görüntü, keşiften servise kadar müşterinin yanında olmak."),
    ("Integrity and win-win, seeking truth from facts, and earning respect", "Dürüst keşif, gerçekçi teklif, sahada tutulan söz."),
    ("Putting fighters first, creating value, and sharing value", "Saha ekibini önceleyerek değer üretmek ve paylaşmak."),
    ("It is widely used in commercial office spaces, indoor halls, television studios, exhibition halls, cinemas, government departments, conference rooms, entertainment venues, hospitals, performing arts centers, etc., and occupies a prominent position in these fields.", "Ofis, fuar, stüdyo, toplantı salonu, sahne ve perakende alanlarında kullanılır."),
    ("The new outer frame design with a sense of technology", "Yeni kasa tasarımı; sahne ve yayın estetiğine uygun çizgiler."),
    ("The QM series is a newly launched 640*480", "QM serisi 640×480 ince alüminyum kabindir;"),
    ("Using dynamic energy-saving high refresh rate PWM-SS chip and 4.2V power supply to save more power. Turning off the screen dynamically makes the energy saving intelligently", "Dinamik enerji tasarruflu PWM sürücü ve akıllı karartma ile güç tüketimi düşer."),
    ("The refresh rate is high meanwhile the picture is flicker-free, which makes the screen is capable to present a smoother and clearer picture effect.", "Yüksek yenileme hızı titreşimsiz, kamera dostu görüntü sağlar."),
    ("High grayscale, high-fidelity view, clear and delicate display; wide color gamut, uniform in color", "Yüksek gri ton ve geniş renk gamı; homojen, net görüntü."),
    ("Strictly select every LED lamp. The band and batch are unified to high standards. The uniformity of the display achieves the high quality", "LED’ler aynı batch’ten seçilir; renk ve parlaklık homojen kalır."),
]


def set_main(html: str, inner: str) -> str:
    return re.sub(r"<main\b[^>]*>.*?</main>", f"<main>\n{inner}\n</main>", html, count=1, flags=re.S)


def crumbs(items: list[tuple[str, str]]) -> str:
    parts = ['<img src="/public/wwwroot/images/icon-home.svg" alt="Anasayfa">']
    for href, label in items:
        parts.append("<em>&gt;</em>")
        if href:
            parts.append(f'<a href="{href}" class="t1">{label}</a>')
        else:
            parts.append(f'<a class="t1">{label}</a>')
    return (
        '<div class="public-nav"><div class="row public-tobody justify-between ov">'
        f'<div class="left items-center">{"".join(parts)}</div></div></div>'
    )


def banner(img: str, alt: str) -> str:
    return f'<div class="public-banner"><img src="{img}" alt="{alt}"></div>'


def quote(text: str = "Bu ürün için keşif ve fiyat teklifi alın.") -> str:
    return (
        f'<div class="tl-quote-bar"><p>{text}</p>'
        '<a href="/contact-us/">Teklif Alın</a></div>'
    )


def write_page(page: Path, html: str, url: str, title: str, desc: str) -> None:
    PAGE_META[url] = (title, desc)
    html = extra_fields(apply_chrome(html, url, title, desc))
    page.parent.mkdir(parents=True, exist_ok=True)
    page.write_text(html, encoding="utf-8", newline="\n")


def shell_from(sample: Path) -> str:
    return sample.read_text(encoding="utf-8")


def series_main(s: dict) -> str:
    gallery = "".join(
        f'<div class="swiper-slide"><a class="product-swiper-i" href="{img}">'
        f'<img src="{img}" alt="{s["title"]}"></a></div>'
        for img in s["g"]
    )
    feats = []
    for i, (h, p, img) in enumerate(s["feats"]):
        side = "fadel" if i % 2 == 0 else "fader"
        feats.append(
            f'<div class="product-model1"><div class="row"><div class="row-i">'
            f'<div class="product-model1-left" hsm="{side}"><div class="product-model1-title items-center">'
            f'<span></span><p class="t1"><strong>{h}</strong></p></div>'
            f'<div class="product-model1-info">{p}</div></div>'
            f'<div class="product-model1-right img-scale"><img src="{img}" alt="{h}"></div>'
            f"</div></div></div>"
        )
    specs = "".join(f"<div><span>{k}</span><strong>{v}</strong></div>" for k, v in s["specs"])
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
      <div class="t2" hsm="fadeup"><p>{s["lead"]}</p>
      <p>Piksel aralığı: {s["pitch"]}</p></div>
    </div>
  </div>
  <div class="product-b-type"><div class="row hsms">
    <a class="product-b-type-i cur" href="#i1" data-offset="220" uk-scroll>Tanıtım</a>
    <a class="product-b-type-i" href="#i2" data-offset="220" uk-scroll>Teknik Özellikler</a>
  </div></div>
  <div class="product-model1" style="padding-bottom:0"><div class="row">
    <h3 class="product-title" id="i1">Tanıtım</h3></div></div>
  {"".join(feats)}
  <div class="product-model6"><div class="row">
    <h3 class="product-title" id="i2">Teknik Özellikler</h3>
    <div class="tl-spec-grid">{specs}</div>
  </div></div>
  {quote(s["title"] + " için keşif ve teklif alın.")}
</div>
"""


def cat_main(title: str, intro: str, img: str, crumbs_i, series_list, tabs) -> str:
    tab_html = ""
    for u, n, active in tabs:
        cur = " cur" if active else ""
        tab_html += f'<a href="{u}" class="right-i{cur}"><span>{n}</span></a>'
    cards = "".join(
        f'<a class="product-list-b-i" href="/{s["slug"]}/" hsm="fadeup">'
        f'<div class="product-list-b-img img-scale"><img src="{s["hero"]}" alt="{s["title"]}"></div>'
        f'<div class="product-list-b-info"><p class="t1">{s["title"]}</p>'
        f'<p class="t2">Piksel aralığı: {s["pitch"]}</p></div></a>'
        for s in series_list
    )
    return f"""
{banner(img, title)}
<div class="public-nav"><div class="row public-tobody justify-between ov">
  <div class="left items-center">{crumbs(crumbs_i).split('<div class="left items-center">')[1].split("</div>")[0]}</div>
  <div class="right items-center">{tab_html}</div>
</div></div>
<div class="product-list public-tobody">
  <p class="t2" style="margin:12px 0 24px">{intro}</p>
  <div class="product-list-b flex-wrap justify-between hsms">{cards}</div>
</div>
{quote()}
"""


def hub_main() -> str:
    cards = [
        ("/commercial-display/", f"{M}/banner-indoor.jpg", "İç Mekan", "Fine pitch, COB, kristal film ve lobi duvarları."),
        ("/rental-staging/", f"{M}/banner-rental.jpg", "Kiralama & Sahne", "Konser, fuar ve lansman için hızlı kilitli kabin."),
        ("/dooh/", f"{M}/banner-outdoor.jpg", "Dış Mekan", "Billboard, cephe ve stadyum yüksek parlaklık LED."),
        ("/accessories/", f"{M}/product-slim-cabinet.jpg", "Aksesuarlar", "Kabin, güç ve montaj setleri."),
    ]
    grid = "".join(
        f'<a class="tl-hub-card" href="{u}"><img src="{img}" alt="{t}">'
        f'<div class="tl-hub-copy"><span>Katalog</span><strong>{t}</strong><em>{d}</em></div></a>'
        for u, img, t, d in cards
    )
    return f"""
{banner(f"{M}/hero-indoor-led.jpg", "Toeled LED ürünleri")}
{crumbs([("/products/", "Ürünler"), ("", "Katalog")])}
<div class="public-tobody"><h1 class="public-title">LED ekran ürünleri</h1>
<p class="t2" style="text-align:center;max-width:720px;margin:0 auto 8px">İç mekan, rental, dış mekan ve aksesuar serilerini projenize göre seçin. Keşif ve teklif LEDAJANS ekibiyle yürür.</p></div>
<div class="tl-hub-grid">{grid}</div>
{quote()}
"""


def cases_main(title: str, cat_filter: str | None, img: str) -> str:
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
    return f"""
{banner(img, title)}
{crumbs([("/cases/", "Referanslar"), ("", title)])}
<div class="public-tobody"><h1 class="public-title">{title}</h1>
<p class="t2" style="text-align:center">Türkiye, Almanya ve Kıbrıs uygulamalarından örnekler.</p></div>
<div class="tl-case-grid">{cards}</div>
{dialogs}
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


def news_list_main(kind: str | None, heading: str) -> str:
    items = [n for n in NEWS if kind is None or n["kind"] == kind]
    cards = "".join(
        f'<a class="tl-news-item" href="/news/{n["slug"]}/">'
        f'<img src="{n["img"]}" alt="{n["title"]}">'
        f'<div><p class="t1">{n["date"]}</p><h2>{n["title"]}</h2><p>{n["desc"]}</p></div></a>'
        for n in items
    )
    return f"""
{banner(f"{M}/hero-indoor-led.jpg", heading)}
{crumbs([("/news/", "Haberler"), ("", heading)])}
<div class="public-tobody"><h1 class="public-title">{heading}</h1></div>
<div class="tl-news-list">{cards}</div>
"""


def news_article_main(n: dict) -> str:
    return f"""
{crumbs([("/news/", "Haberler"), ("", n["title"])])}
<article class="tl-article">
  <img class="hero" src="{n["img"]}" alt="{n["title"]}">
  <p class="t1">{n["date"]}</p>
  <h1>{n["title"]}</h1>
  {n["body"]}
  {quote()}
</article>
"""


HOMESWIPER = f"""
        <div class="swiper home-swiper">
            <div class="swiper-wrapper">
                <div class="swiper-slide">
                    <div class="home-swiper-b">
                        <video class="home-swiper-video" autoplay muted loop playsinline poster="{M}/hero-indoor-led.jpg">
                            <source src="/public/wwwroot/video/hero-indoor.mp4" type="video/mp4">
                        </video>
                    </div>
                    <div class="hero-overlay"><div class="hero-overlay-inner">
                        <span class="hero-kicker">İç mekan</span>
                        <h2>İç Mekan LED Ekran</h2>
                        <p>Fine pitch ve COB duvarlar. Lobi, toplantı ve stüdyo için net görüntü.</p>
                        <p class="hero-pitch">Q0.8 – Q4 · NC COB · CMS kristal film</p>
                        <ul class="hero-specs"><li>3840 Hz+</li><li>16 bit gri</li><li>2 yıl garanti</li></ul>
                        <a class="hero-cta" href="/contact-us/">Teklif Alın</a>
                        <a class="hero-cta ghost" href="/commercial-display/">Serileri incele</a>
                    </div></div>
                </div>
                <div class="swiper-slide">
                    <div class="home-swiper-b">
                        <video class="home-swiper-video" autoplay muted loop playsinline poster="{M}/hero-rental-stage.jpg">
                            <source src="/public/wwwroot/video/hero-rental.mp4" type="video/mp4">
                        </video>
                    </div>
                    <div class="hero-overlay"><div class="hero-overlay-inner">
                        <span class="hero-kicker">Rental</span>
                        <h2>Kiralama ve Sahne</h2>
                        <p>Konser, fuar ve lansman için hızlı kilitli rental LED kabin.</p>
                        <p class="hero-pitch">RW · CG · LN · DM · PM</p>
                        <ul class="hero-specs"><li>Hızlı kilit</li><li>Flight case</li><li>Yedek modül</li></ul>
                        <a class="hero-cta" href="/contact-us/">Teklif Alın</a>
                        <a class="hero-cta ghost" href="/rental-staging/">Rental seriler</a>
                    </div></div>
                </div>
                <div class="swiper-slide">
                    <div class="home-swiper-b">
                        <img class="home-swiper-img tl-kenburns" src="{M}/hero-crystal-film.jpg" alt="CMS kristal film LED ekran" width="1920" height="898">
                    </div>
                    <div class="hero-overlay"><div class="hero-overlay-inner">
                        <span class="hero-kicker">Kristal film</span>
                        <h2>Şeffaf LED Cam</h2>
                        <p>Vitrin ve cephe camında şeffaflığı koruyan CMS serisi.</p>
                        <p class="hero-pitch">CMS4 · CMS5 · CMS6 · CMS8 · CMS10</p>
                        <ul class="hero-specs"><li>Yüksek şeffaflık</li><li>İnce film</li><li>Vitrin uyumu</li></ul>
                        <a class="hero-cta" href="/cms-series-crystal-film-display/">CMS Serisi</a>
                    </div></div>
                </div>
                <div class="swiper-slide">
                    <div class="home-swiper-b">
                        <img class="home-swiper-img tl-kenburns" src="{M}/hero-outdoor-dooh.jpg" alt="Dış mekan LED billboard" width="1920" height="898">
                    </div>
                    <div class="hero-overlay"><div class="hero-overlay-inner">
                        <span class="hero-kicker">DOOH</span>
                        <h2>Dış Mekan LED Ekran</h2>
                        <p>Billboard, medya cephe ve stadyum için yüksek parlaklık.</p>
                        <p class="hero-pitch">Outdoor Q · S · MG</p>
                        <ul class="hero-specs"><li>Yüksek nit</li><li>IP koruma</li><li>Uzaktan yayın</li></ul>
                        <a class="hero-cta" href="/dooh/">Dış mekan seriler</a>
                    </div></div>
                </div>
                <div class="swiper-slide">
                    <div class="home-swiper-b">
                        <img class="home-swiper-img tl-kenburns" src="{M}/hero-cob-module.jpg" alt="COB fine pitch LED modül" width="1920" height="898">
                    </div>
                    <div class="hero-overlay"><div class="hero-overlay-inner">
                        <span class="hero-kicker">Fine pitch</span>
                        <h2>COB ve Yakın İzleme</h2>
                        <p>Stüdyo ve lobi için darbeye dayanıklı COB yüzey.</p>
                        <p class="hero-pitch">NC0.9 · NC1.2 · Q Mini</p>
                        <ul class="hero-specs"><li>COB</li><li>Yakın izleme</li><li>7/24 uygun</li></ul>
                        <a class="hero-cta" href="/nc-series/">NC Serisi</a>
                    </div></div>
                </div>
            </div>
            <div class="swiper-pagination"></div>
            <a class="swiper-bottom-btn slide-animation" href="#i1" data-offset="80" uk-scroll>
                <img src="/public/wwwroot/images/home_199.png" alt="">
            </a>
        </div>
"""


def patch_homepage(html: str) -> str:
    html = re.sub(
        r'<div class="swiper home-swiper">.*?<a class="swiper-bottom-btn slide-animation" href="#i1".*?</a>\s*</div>',
        HOMESWIPER,
        html,
        count=1,
        flags=re.S,
    )
    html = html.replace(
        '<img src="/public/wwwroot/media/c160a43072ba.jpg" alt="">',
        f'<img src="{M}/hero-indoor-led.jpg" alt="Toeled kurumsal video">',
        1,
    )
    html = html.replace(
        '<img src="/public/wwwroot/media/59aa287c7dca.jpg" alt="">',
        f'<img src="{M}/showroom-istanbul.webp" alt="İstanbul LED showroom">',
        1,
    )
    html = html.replace(
        '<img src="/public/wwwroot/media/add066dc8f3c.png" alt="">',
        f'<img src="{M}/banner-rental.jpg" alt="Rental LED sahne">',
        1,
    )
    html = html.replace(
        '<img src="/public/wwwroot/media/d4d364d59387.jpg" alt="">',
        f'<img src="{M}/hero-outdoor-dooh.jpg" alt="Dış mekan LED ekran">',
        1,
    )
    # cases
    case_slides = "".join(
        f'''<div class="swiper-slide"><div class="swiper-info">
            <h3 class="text-line1">{c["title"]}</h3>
            <p>{c["city"]} · {c["product"]} · {c["area"]}. {c["text"]}</p>
            </div>
            <a class="img-scale" href="/cases/">
            <img src="{c["img"]}" alt="{c["title"]}"></a></div>'''
        for c in CASES[:8]
    )
    html = re.sub(
        r'(<div class="swiper-wrapper">)\s*(<div class="swiper-slide ">\s*<div class="swiper-info">.*?)(</div>\s*<div class="page-box">)',
        lambda m: m.group(0),
        html,
        count=1,
        flags=re.S,
    )
    html = re.sub(
        r'(<div class="home-model3 template1080" id="i3">[\s\S]*?<div class="swiper-wrapper">)[\s\S]*?(</div>\s*<div class="swiper-pagination">)',
        r"\1" + case_slides + r"\2",
        html,
        count=1,
    )
    # news
    n0, n1, n2 = NEWS[0], NEWS[1], NEWS[3]
    news_html = f"""
                    <div class="model4-content cur">
                        <a href="/news/{n0["slug"]}/" class="model4-content-l">
                            <div class="card-item">
                                <div class="card-item-img img-scale"><img src="{n0["img"]}" alt="{n0["title"]}"></div>
                                <div class="card-item-text">
                                    <div class="card-item-date">{n0["date"]}</div>
                                    <div class="card-item-title">{n0["title"]}</div>
                                    <div class="card-item-desc">{n0["desc"]}</div>
                                </div>
                                <div class="card-item-btn"><i class="layui-icon layui-icon-right"></i></div>
                            </div>
                        </a>
                        <div class="model4-content-l model4-content-l--stack">
                            <a href="/news/{n1["slug"]}/" class="card-item">
                                <div class="card-item-img img-scale"><img src="{n1["img"]}" alt="{n1["title"]}"></div>
                                <div class="card-item-text">
                                    <div class="card-item-date">{n1["date"]}</div>
                                    <div class="card-item-title">{n1["title"]}</div>
                                    <div class="card-item-desc">{n1["desc"]}</div>
                                </div>
                                <div class="card-item-btn"><i class="layui-icon layui-icon-right"></i></div>
                            </a>
                            <a href="/company-news/" class="card-link"><span>Daha fazla haber</span></a>
                        </div>
                    </div>
                    <div class="model4-content">
                        <a href="/news/{n2["slug"]}/" class="model4-content-l">
                            <div class="card-item">
                                <div class="card-item-img img-scale"><img src="{n2["img"]}" alt="{n2["title"]}"></div>
                                <div class="card-item-text">
                                    <div class="card-item-date">{n2["date"]}</div>
                                    <div class="card-item-title">{n2["title"]}</div>
                                    <div class="card-item-desc">{n2["desc"]}</div>
                                </div>
                                <div class="card-item-btn"><i class="layui-icon layui-icon-right"></i></div>
                            </div>
                        </a>
                        <div class="model4-content-l model4-content-l--stack">
                            <a href="/news/{NEWS[4]["slug"]}/" class="card-item">
                                <div class="card-item-img img-scale"><img src="{NEWS[4]["img"]}" alt="{NEWS[4]["title"]}"></div>
                                <div class="card-item-text">
                                    <div class="card-item-date">{NEWS[4]["date"]}</div>
                                    <div class="card-item-title">{NEWS[4]["title"]}</div>
                                    <div class="card-item-desc">{NEWS[4]["desc"]}</div>
                                </div>
                                <div class="card-item-btn"><i class="layui-icon layui-icon-right"></i></div>
                            </a>
                            <a href="/industry-news/" class="card-link"><span>Daha fazla haber</span></a>
                        </div>
                    </div>
    """
    html = re.sub(
        r'<div class="model4-content-b">[\s\S]*?</div>\s*<a class="swiper-bottom-btn slide-animation" href="#i5"',
        '<div class="model4-content-b">' + news_html + '</div>\n            <a class="swiper-bottom-btn slide-animation" href="#i5"',
        html,
        count=1,
    )
    # replace China leftover map dots already hidden; keep 3 offices
    html = re.sub(
        r"MG serisi, dış mekana uygun alüminyum döküm kabindir;[^<]*",
        "Proje bazlı LED ekran uygulaması. Keşif ve kurulum Toeled ekibiyle.",
        html,
    )
    html = html.replace("Mingyue series indoor TS3.9", "İç mekan toplantı duvarı")
    html = html.replace("Dış mekan Full-Color Q5", "Dış mekan LED ekran")
    html = html.replace("Dış mekan full-color Q5", "Dış mekan LED ekran")
    html = html.replace("İç mekan Q3-Pro", "İç mekan LED duvar")
    html = html.replace("İç mekan Full-Color Q2", "İç mekan LED duvar")
    html = html.replace("İç mekan Full-Color Q1.8", "İç mekan LED duvar")
    html = html.replace("İç mekan Full-Color Q2.5", "İç mekan LED duvar")
    html = html.replace("İç mekan Full-Color Q1.8Pro", "İç mekan LED duvar")
    html = html.replace("Dış mekan Full-Color Q4", "Dış mekan LED ekran")
    html = html.replace("/news/-qiangli-jucai-overseas-order-payment-account-statement-/", "/news/odeme-guvenligi-uyarisi/")
    html = html.replace("/news/qiangli-led-successfully-concludes-ise-2026/", "/news/ise-2026-toeled-led-ekran/")
    html = html.replace(
        "/news/topping-sales-again-strong-giant-color-captures-the-first-place-in-led-display-sales-demonstrating-the-kingly-demeanor-with-channel-advantages-/",
        "/news/dis-mekan-led-ekran-parlaklik/",
    )
    html = html.replace(
        "/news/join-us-at-ise-spain-2026-to-explore-the-future-of-led-display-technology/",
        "/news/ise-2026-toeled-led-ekran/",
    )
    return html


def about_main() -> str:
    years = [
        ("2000’ler", "Sektörde LED ekran satış, kiralama ve saha kurulumu tecrübesi birikir."),
        ("İstanbul ofis", "Şişli’de showroom ve operasyon merkezi; keşif-teklif aynı çatıda."),
        ("Almanya & Kıbrıs", "Erkrath ve Girne ofisleriyle Avrupa ve KKTC projeleri."),
        ("Toeled", "TAHA LED Dış Ticaret A.Ş. ürün vitrini: iç, rental, DOOH katalog."),
        ("Bugün", "2 yıl garanti, Türkiye geneli kurulum, ISO uygunluk ve 7/24 saha desteği."),
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
      <p class="t2">Toeled, LEDAJANS çatısında iç ve dış mekan LED ekran, rental, kontrol ve kurulum sunar. İstanbul, Almanya ve Kıbrıs ofisleriyle keşif, montaj ve servisi aynı standartta yürütürüz.</p></div>
    </div>
    <div class="right"><div class="img-scale right-img">
      <img src="{M}/hero-indoor-led.jpg" alt="Toeled LED showroom">
    </div></div>
  </div>
  <div class="model2 public-tobody">
    <p class="public-title1">Tarihçe</p>
    <div class="swiper model3-swiper"><div class="swiper-wrapper hsms">{tl}</div></div>
  </div>
  <div class="public-tobody" style="padding-bottom:48px">
    <h2 class="public-title1">Kurumsal video</h2>
    <video controls poster="{M}/hero-indoor-led.jpg" style="width:100%;max-width:960px;border-radius:16px">
      <source src="/public/wwwroot/video/sirket.mp4" type="video/mp4">
    </video>
  </div>
</div>
"""


def culture_main() -> str:
    items = [
        ("Vizyon", "Türkiye, Almanya ve Kıbrıs’ta güvenilir LED ekran partneri olmak.", f"{M}/hero-indoor-led.jpg"),
        ("Misyon", "Doğru pitch, sağlam kabin, keşiften servise net süreç.", f"{M}/banner-rental.jpg"),
        ("Değerler", "Dürüst keşif, gerçekçi teklif, sahada tutulan söz.", f"{M}/hero-outdoor-dooh.jpg"),
        ("Servis", "2 yıl parça-işçilik, yedek stok, 7/24 saha.", f"{M}/showroom-istanbul.webp"),
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
<div class="culture-b public-tobody"><h1 class="public-title1">Kurum Kültürü</h1>
<div class="culture-b-list flex-wrap hsms">{cards}</div></div>
"""


def certs_main() -> str:
    return f"""
{banner(f"{M}/banner-indoor.jpg", "Sertifikalar")}
{crumbs([("/about-us/", "Hakkımızda"), ("", "Sertifikalar")])}
<div class="public-tobody">
  <h1 class="public-title">Sertifikalar ve uygunluk</h1>
  <p class="t2">Projelerde ISO kalite süreçleri, CE/uygunluk ve 2 yıl garanti teklife yazılır. Belge kopyası için iletişime geçin.</p>
  <div class="tl-spec-grid">
    <div><span>Kalite</span><strong>ISO süreçleri</strong></div>
    <div><span>Ürün</span><strong>CE / uygunluk</strong></div>
    <div><span>Garanti</span><strong>2 yıl parça ve işçilik</strong></div>
    <div><span>Servis</span><strong>Türkiye geneli kurulum</strong></div>
  </div>
  {quote("Belge ve teknik dosya talep edin.")}
</div>
"""


def service_main() -> str:
    return f"""
{banner(f"{M}/banner-indoor.jpg", "Servis")}
{crumbs([("/service/", "Destek"), ("", "Servis")])}
<div class="service-b"><div class="model1 public-tobody hsms">
  <h1 class="public-title">Servis</h1>
  <p class="t2">Keşif, kurulum, eğitim ve 2 yıl teknik destek. Mesai 7 gün; Türkiye saati.</p>
  <div class="model1-info-list flex-wrap justify-between hsms">
    <div class="model1-info-list-i"><div class="model1-info-list-i-con"><p class="t1">Yerinde keşif</p><p class="t2">Ölçü, izleme mesafesi, güç ve askı/duvar analizi.</p></div></div>
    <div class="model1-info-list-i"><div class="model1-info-list-i-con"><p class="t1">Çözüm tasarımı</p><p class="t2">Pitch, kabin, kontrol ve içerik senaryosu.</p></div></div>
    <div class="model1-info-list-i"><div class="model1-info-list-i-con"><p class="t1">Kurulum</p><p class="t2">Montaj, sinyal, kalibrasyon ve teslim eğitimi.</p></div></div>
    <div class="model1-info-list-i"><div class="model1-info-list-i-con"><p class="t1">Garanti</p><p class="t2">2 yıl parça ve işçilik; yedek stok İstanbul.</p></div></div>
  </div>
</div></div>
{quote()}
"""


def outlets_main() -> str:
    return f"""
{banner(f"{M}/showroom-istanbul.webp", "Satış noktaları")}
{crumbs([("/sales-outlets/", "Destek"), ("", "Satış noktaları")])}
<div class="public-tobody"><h1 class="public-title">Satış noktaları</h1>
<p class="t2" style="text-align:center">Üç ofis, tek standart. Çin bayi haritası yok; sizinle İstanbul, Erkrath ve Girne konuşur.</p></div>
<div class="tl-offices">
  <div class="tl-office-card"><h3>İstanbul</h3><p>Halide Edip Adıvar Mah. Gül 2 Sk. No:10a, Şişli</p><p>+90 212 220 40 04</p></div>
  <div class="tl-office-card"><h3>Erkrath</h3><p>Heinrich-Hertz-Straße 50, 40699 Erkrath</p><p>+49 1521 2401915</p></div>
  <div class="tl-office-card"><h3>Girne</h3><p>Karaoğlanoğlu Cad. Yayla Aktiğin İş Hanı No:6</p><p>+90 533 856 93 71</p></div>
</div>
{quote()}
"""


def knowledge_main() -> str:
    return f"""
{banner(f"{M}/banner-indoor.jpg", "Bilgi merkezi")}
{crumbs([("/knowledge/", "Destek"), ("", "Bilgi merkezi")])}
<div class="public-tobody"><h1 class="public-title">Bilgi merkezi</h1>
<h2 id="kurulum">Kurulum</h2>
<p>Duvar veya truss, güç hattı, sinyal (fiber/CAT) ve topraklama keşif tutanağına yazılır. Kabin terazisi ve modül kilidi teslim kontrol listesindedir.</p>
<h2 id="kullanim">Kullanım</h2>
<p>İçerik çözünürlüğü ekran native pitch’ine uymalıdır. Parlaklık ofiste düşük, dış mekanda yüksek profilde kalır. 7/24 duvarda pixel shift ve zamanlayıcı önerilir.</p>
<h2 id="bakim">Bakım</h2>
<p>Aylık görsel kontrol, yıllık kalibrasyon, yedek PSU/modül stoku. Arızada WhatsApp +90 212 220 40 04.</p>
</div>
{quote()}
"""


def support_form_main(title: str, lead: str) -> str:
    return f"""
{banner(f"{M}/banner-indoor.jpg", title)}
{crumbs([("/debugger/", "Destek"), ("", title)])}
<div class="culture-b public-tobody">
  <h1 class="public-title">{title}</h1>
  <p class="t2">{lead} Uzaktan teşhis ve saha kaydı İstanbul teknik ekibine düşer.</p>
  <p><a class="contact-btn" href="https://wa.me/902122204004" target="_blank" rel="noopener">WhatsApp destek</a></p>
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
"""


def qce_main() -> str:
    return f"""
{banner(f"{M}/banner-indoor.jpg", "Sertifika")}
{crumbs([("/qce-cert-lookup/", "Destek"), ("", "Sertifika")])}
<div class="public-tobody"><h1 class="public-title">Sertifika bilgisi</h1>
<p class="t2">Sahte ürün kodu sorgusu yoktur. ISO/CE ve proje belgelerini <a href="/certificates-honor/">sertifikalar</a> sayfasından veya teklif dosyasından isteyin.</p>
{quote("Belge talebi için yazın.")}
</div>
"""


def contact_patch(html: str) -> str:
    html = extra_fields(html)
    html = html.replace(">Gönder<", ">Teklif Alın<")
    html = html.replace("<h1 class=\"public-title\" hsm=\"fadeup\">Mesaj Bırakın</h1>",
                        "<h1 class=\"public-title\" hsm=\"fadeup\">Teklif alın</h1>")
    return html


def redirect_html(to: str) -> str:
    return f"""<!DOCTYPE html><html lang="tr"><head>
<meta charset="utf-8"><meta http-equiv="refresh" content="0;url={to}">
<link rel="canonical" href="https://toeled.com{to}">
<title>Yönlendiriliyor | Toeled</title></head>
<body><p>Bu haber taşındı. <a href="{to}">Yeni sayfaya gidin</a>.</p></body></html>
"""


def sweep(html: str) -> str:
    for a, b in SWEEP:
        html = html.replace(a, b)
    return html


def htaccess() -> None:
    p = ROOT / ".htaccess"
    text = p.read_text(encoding="utf-8")
    block = "\n# Toeled news 301\n"
    for old, new in OLD_NEWS_REDIRECT.items():
        rule = f"Redirect 301 /news/{old}/ /news/{new}/\n"
        if rule not in text:
            block += rule
    if "certificates-honor/2" not in text:
        block += "Redirect 301 /certificates-honor/2/ /certificates-honor/\n"
    if "Toeled news 301" not in text:
        p.write_text(text.rstrip() + "\n" + block, encoding="utf-8", newline="\n")


def sitemap() -> None:
    urls = [
        "/", "/products/", "/commercial-display/", "/rental-staging/", "/dooh/", "/accessories/",
        "/cases/", "/case-commercial-display/", "/case-rental-staging/", "/case-dooh/",
        "/about-us/", "/corporate-culture/", "/certificates-honor/",
        "/news/", "/company-news/", "/industry-news/",
        "/contact-us/", "/service/", "/sales-outlets/", "/knowledge/",
        "/debugger/", "/one-click-debug/", "/qce-cert-lookup/",
    ]
    urls += [f"/{s['slug']}/" for s in SERIES]
    urls += [f"/news/{n['slug']}/" for n in NEWS]
    body = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<urlset xmlns=\"http://www.sitemaps.org/schemas/sitemap/0.9\">\n"
    for u in urls:
        pri = "1.0" if u == "/" else "0.8"
        body += f"  <url><loc>https://toeled.com{u}</loc><lastmod>2026-09-17</lastmod><changefreq>weekly</changefreq><priority>{pri}</priority></url>\n"
    body += "</urlset>\n"
    (ROOT / "sitemap.xml").write_text(body, encoding="utf-8", newline="\n")


def main() -> None:
    sample = ROOT / "contact-us" / "index.html"
    base = sample.read_text(encoding="utf-8")

    # homepage
    home = ROOT / "index.html"
    h = patch_homepage(home.read_text(encoding="utf-8"))
    t, d = PAGE_META["/"]
    write_page(home, sweep(h), "/", t, d)

    # series
    for s in SERIES:
        page = ROOT / s["slug"] / "index.html"
        html = set_main(shell_from(page if page.exists() else sample), series_main(s))
        write_page(page, sweep(html), f"/{s['slug']}/", f"{s['title']} | Toeled LED Ekran", s["lead"][:155])

    # hub + cats
    tabs_prod = [
        ("/commercial-display/", "İç Mekan", False),
        ("/rental-staging/", "Kiralama & Sahne", False),
        ("/dooh/", "Dış Mekan", False),
        ("/accessories/", "Aksesuarlar", False),
    ]
    mapping = {
        "products": ("LED ekran ürünleri", hub_main, "/products/", PAGE_META["/products/"]),
        "commercial-display": (
            "İç Mekan LED Ekran",
            lambda: cat_main("İç Mekan LED Ekran", "Fine pitch, COB ve kristal film serileri.", f"{M}/banner-indoor.jpg",
                             [("/products/", "Ürünler"), ("", "İç Mekan")],
                             [x for x in SERIES if x["cat"] == "indoor"],
                             [("/commercial-display/", "İç Mekan", True), ("/rental-staging/", "Kiralama & Sahne", False), ("/dooh/", "Dış Mekan", False), ("/accessories/", "Aksesuarlar", False)]),
            "/commercial-display/", PAGE_META["/commercial-display/"],
        ),
        "rental-staging": (
            "Rental",
            lambda: cat_main("Kiralama & Sahne", "Konser, fuar ve lansman rental kabinleri.", f"{M}/banner-rental.jpg",
                             [("/products/", "Ürünler"), ("", "Kiralama & Sahne")],
                             [x for x in SERIES if x["cat"] == "rental"],
                             [("/commercial-display/", "İç Mekan", False), ("/rental-staging/", "Kiralama & Sahne", True), ("/dooh/", "Dış Mekan", False), ("/accessories/", "Aksesuarlar", False)]),
            "/rental-staging/", PAGE_META["/rental-staging/"],
        ),
        "dooh": (
            "DOOH",
            lambda: cat_main("Dış Mekan LED Ekran", "Billboard, cephe ve stadyum.", f"{M}/banner-outdoor.jpg",
                             [("/products/", "Ürünler"), ("", "Dış Mekan")],
                             [x for x in SERIES if x["cat"] in ("outdoor",) and x["slug"] in ("outdoor-q-series", "outdoor-s-series")],
                             [("/commercial-display/", "İç Mekan", False), ("/rental-staging/", "Kiralama & Sahne", False), ("/dooh/", "Dış Mekan", True), ("/accessories/", "Aksesuarlar", False)]),
            "/dooh/", PAGE_META["/dooh/"],
        ),
        "accessories": (
            "Aksesuar",
            lambda: cat_main("Aksesuarlar", "Kabin, güç ve montaj.", f"{M}/product-slim-cabinet.jpg",
                             [("/products/", "Ürünler"), ("", "Aksesuarlar")],
                             [x for x in SERIES if x["slug"] in ("qm-series", "mg-series", "p-series", "v-series-")],
                             [("/commercial-display/", "İç Mekan", False), ("/rental-staging/", "Kiralama & Sahne", False), ("/dooh/", "Dış Mekan", False), ("/accessories/", "Aksesuarlar", True)]),
            "/accessories/", PAGE_META["/accessories/"],
        ),
    }
    for folder, (label, fn, url, meta) in mapping.items():
        page = ROOT / folder / "index.html"
        html = set_main(shell_from(page), fn() if folder != "products" else hub_main())
        write_page(page, sweep(html), url, meta[0], meta[1])

    # cases
    for folder, title, filt, img, url in [
        ("cases", "Referanslar", None, f"{M}/hero-indoor-led.jpg", "/cases/"),
        ("case-commercial-display", "İç mekan referansları", "indoor", f"{M}/banner-indoor.jpg", "/case-commercial-display/"),
        ("case-rental-staging", "Sahne ve fuar referansları", "rental", f"{M}/banner-rental.jpg", "/case-rental-staging/"),
        ("case-dooh", "Dış mekan referansları", "dooh", f"{M}/banner-outdoor.jpg", "/case-dooh/"),
    ]:
        page = ROOT / folder / "index.html"
        html = set_main(shell_from(page), cases_main(title, filt, img))
        write_page(page, sweep(html), url, *PAGE_META[url])

    # about family
    for folder, fn, url in [
        ("about-us", about_main, "/about-us/"),
        ("corporate-culture", culture_main, "/corporate-culture/"),
        ("certificates-honor", certs_main, "/certificates-honor/"),
        ("service", service_main, "/service/"),
        ("sales-outlets", outlets_main, "/sales-outlets/"),
        ("knowledge", knowledge_main, "/knowledge/"),
        ("qce-cert-lookup", qce_main, "/qce-cert-lookup/"),
    ]:
        page = ROOT / folder / "index.html"
        html = set_main(shell_from(page), fn())
        write_page(page, sweep(html), url, *PAGE_META[url])

    cert2 = ROOT / "certificates-honor" / "2" / "index.html"
    if cert2.exists():
        write_page(cert2, redirect_html("/certificates-honor/"), "/certificates-honor/2/", "Sertifikalar | Toeled", PAGE_META["/certificates-honor/"][1])

    page = ROOT / "debugger" / "index.html"
    html = set_main(shell_from(page), support_form_main("Teknik destek", "Uzaktan teşhis ve saha kaydı."))
    write_page(page, sweep(html), "/debugger/", *PAGE_META["/debugger/"])
    page = ROOT / "one-click-debug" / "index.html"
    html = set_main(shell_from(page), support_form_main("Tek tıkla destek", "Kısa form, aynı gün dönüş."))
    write_page(page, sweep(html), "/one-click-debug/", *PAGE_META["/one-click-debug/"])

    # contact
    cpage = ROOT / "contact-us" / "index.html"
    write_page(cpage, sweep(contact_patch(cpage.read_text(encoding="utf-8"))), "/contact-us/", *PAGE_META["/contact-us/"])

    # news lists
    for folder, kind, url, heading in [
        ("news", None, "/news/", "Haber Merkezi"),
        ("company-news", "company", "/company-news/", "Kurumsal Haberler"),
        ("industry-news", "industry", "/industry-news/", "Sektör Haberleri"),
    ]:
        page = ROOT / folder / "index.html"
        html = set_main(shell_from(page), news_list_main(kind, heading))
        write_page(page, sweep(html), url, *PAGE_META[url])

    for n in NEWS:
        page = ROOT / "news" / n["slug"] / "index.html"
        html = set_main(base, news_article_main(n))
        write_page(page, sweep(html), f"/news/{n['slug']}/", f"{n['title']} | Toeled", n["desc"][:155])

    for old, new in OLD_NEWS_REDIRECT.items():
        page = ROOT / "news" / old / "index.html"
        page.parent.mkdir(parents=True, exist_ok=True)
        page.write_text(redirect_html(f"/news/{new}/"), encoding="utf-8", newline="\n")

    # leftover sweep all html
    for page in ROOT.rglob("index.html"):
        if any(p in page.parts for p in ("_ref", "tools", "tests", ".superdesign")):
            continue
        text = page.read_text(encoding="utf-8")
        upd = sweep(text)
        upd = upd.replace("Qiangli", "Toeled")
        upd = upd.replace("qiangli", "toeled")
        upd = upd.replace("9thpanel", "toeled")
        upd = upd.replace("9thPanel", "Toeled")
        upd = upd.replace("GKGD", "Toeled")
        if upd != text:
            page.write_text(upd, encoding="utf-8", newline="\n")

    htaccess()
    sitemap()
    print("rebuild done")


if __name__ == "__main__":
    main()
