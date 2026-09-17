"""Seri sayfası: benzersiz paket görseli + dolu tanıtım metni."""
from __future__ import annotations

M = "/public/wwwroot/media"


def pack(slug: str, key: str) -> str:
    return f"{M}/series/{slug}/{key}.jpg"


def _extra(slug: str, *, body: list[str], feats: list[tuple[str, list[str]]], uses: list[tuple[str, str, str]], specs: list[tuple[str, str]]):
    return dict(
        body=body,
        feats=[(t, paras, pack(slug, f"feat-{i}")) for i, (t, paras) in enumerate(feats, 1)],
        uses=[(pack(slug, k), t, d) for k, t, d in uses],
        specs=specs,
    )


EXTRA = {
    "cms-series-crystal-film-display": _extra(
        "cms-series-crystal-film-display",
        body=[
            "CMS kristal film, camı kapatmadan LED yayın yapmanız gereken vitrin, showroom cephesi ve atrium camlarında kullanılır. Film kalınlığı düşüktür; mevcut cephe statik yükünü ciddi artırmaz.",
            "Gündüz vitrin stoğu görünür kalır, gece ise yüksek kontrastlı içerik öne çıkar. Toeled keşifte cam tipi, yapıştırma yönü, güç noktası ve uzaktan yayın senaryosunu aynı tutanakta toplar.",
            "Nişantaşı ve AVM vitrinlerinde film, ağır kabin askısı olmadan mevcut cama uygulanır. Laminasyon, silikon ve kenar kapatma detayı teslim kontrol listesindedir.",
            "İçerik zamanlayıcısı gündüz düşük parlaklık, gece yüksek nit profiline ayrılır. LEDAJANS Şişli’de film örneğini cam üzerinde canlı gösterir.",
            "Serviste hasarlı şerit sökülüp yenisiyle değişir; tüm cepheyi yenilemeniz gerekmez. Yedek şerit oranı keşifte cam metrajına yazılır.",
        ],
        feats=[
            ("Yüksek şeffaflık", [
                "Camı kapatmadan gece-gündüz içerik yayınlar. İzleyici vitrin stoğunu ve LED’i aynı anda görür; perakende ve otomotiv showroom’da stok kaybı olmaz.",
                "Gündüz ışığında film neredeyse kaybolur; gece grafik öne çıkar. Şeffaflık oranı cam tipi ve pitch ile keşifte netleşir.",
                "Plaza lobi camında bilgi bandı, mağazada tam cephe — aynı aile, farklı kesim.",
            ]),
            ("İnce film yapı", [
                "Mevcut cam cepheye düşük yükle uygulanır. Ağır kabin askısı ve çelik karkas gerekmez.",
                "Keşifte cam kalınlığı, derz ve silikon/laminasyon detayı milimetreyle işlenir. Statikçiye iletilen yük kabinden çok daha düşüktür.",
                "Kenar kapatma ve güç girişi teslimde fotoğraflanır; sonraki bakım aynı detaydan yürür.",
            ]),
            ("Canlı renk", [
                "Vitrin reklamında yüksek kontrast. Gündüz düşük parlaklık profili, gece yüksek nit ile aynı içerik okunur kalır.",
                "Otomatik ışık sensörü önerilir; cadde yansıması ve vitrin aydınlatması keşif notuna yazılır.",
                "İçerik siyah zeminle çalışınca ürün silüeti camın arkasında durur.",
            ]),
            ("Kolay servis", [
                "Modüler tamir, kısa kesinti. Hasarlı şerit sökülüp yenisiyle değiştirilir.",
                "Tüm cepheyi sökmeden gece bakımı mümkündür; yedek şerit İstanbul stoktan çıkar.",
                "Servis kaydı WhatsApp hattına düşer; aynı gün saha veya kargo planlanır.",
            ]),
        ],
        uses=[
            ("use-1", "Otomotiv showroom", "Cam arkasındaki araç görünür; film gece lansman duvarına dönüşür."),
            ("use-2", "Otel atrium camı", "Lobi camında ince şeffaf bilgi bandı."),
            ("hero", "Mağaza vitrini", "Nişantaşı ve AVM cephesinde gece-gündüz vitrin."),
        ],
        specs=[
            ("Piksel aralığı", "4 / 5 / 6 / 8 / 10 mm"),
            ("Kullanım", "İç mekan cam, vitrin, atrium"),
            ("Şeffaflık", "Yüksek; cam stoğu görünür"),
            ("Kurulum", "Film / cam yüzeyi, düşük yük"),
            ("Kontrol", "Uzaktan içerik, zamanlayıcı"),
            ("Garanti", "2 yıl parça ve işçilik"),
        ],
    ),
    "hs-series-holographic-display": _extra(
        "hs-series-holographic-display",
        body=[
            "HS holografik mesh, ürünün arkada durduğu lansman, deneyim odası ve sahne önünde derinlik hissi verir. Perde şeffaftır; ışık ve sahne dekoru LED’in arkasından okunur.",
            "Askı ve truss kurulumuna uygun hafif kabinle fuar ve lansmanda aynı gece kurulur. Kamera çekiminde yüksek yenileme titremeyi keser.",
            "İçerik siyah zeminle çalışınca nesne havada duruyor gibi okunur. Otomotiv ve moda lansmanında bu kural teklif notuna yazılır.",
            "Kabin ağırlığı truss hesabına girer; LEDAJANS saha ekibi fly / frame seçimini keşifte kilitler.",
            "Showroom’da mesh örneği ürün plinth’inin önünde izlenir; randevu +90 212 220 40 04.",
        ],
        feats=[
            ("Mesh yapı", [
                "Arkası görünen şeffaf LED perde. Sahne ışığı ve ürün silüeti kaybolmaz; holografik etki içerikten gelir.",
                "Tel aralığı ve pitch, izleme mesafesine göre seçilir. Yakın deneyim odasında daha sık mesh istenir.",
                "Makro yüzeyde piksel tel üzerinde durur; stüdyo kalibrasyonu teslim kriteridir.",
            ]),
            ("Sahne etkisi", [
                "Lansman ve deneyim odalarında 3B his. Modeller ve araç mesh’in arkasından geçer.",
                "Siyah zemin içerik kuralı yönetmene yazılı verilir; aksi halde şeffaflık kaybolur.",
                "Pop-up marka odasında plinth + mesh aynı günde kurulur.",
            ]),
            ("Hafif kabin", [
                "Askı ve truss kurulumuna uygun. Fuar standında zemin yükünü düşürür, söküm hızlanır.",
                "Klip ve tırabzan detayı keşif krokisine işlenir. Boş salonda truss testi önerilir.",
                "Taşıma kasası tur ve fuar lojistiğine sığar.",
            ]),
            ("Yüksek yenileme", [
                "Kamera çekiminde titreme yok. 3840 Hz+ sınıfı yayın ve sosyal medya kaydı için uygundur.",
                "Shutter değeri ile refresh aynı teklif satırında eşlenir.",
                "Çok kameralı sette rolling shutter moiresi mesh’te ayrıca kontrol edilir.",
            ]),
        ],
        uses=[
            ("use-1", "Otomotiv reveal", "Karanlık showroom’da mesh arkasından araç silüeti."),
            ("use-2", "Marka deneyim odası", "Plinth’teki ürün mesh’in arkasında durur."),
            ("hero", "Lansman sahnesi", "Spot ve perde ile aynı gece kurulum."),
        ],
        specs=[
            ("Piksel aralığı", "3.9 / 6.2 / 10.4 mm"),
            ("Kullanım", "İç mekan sahne / deneyim"),
            ("Yapı", "Holografik mesh perde"),
            ("Refresh", "3840 Hz+"),
            ("Kurulum", "Askı / truss / frame"),
            ("Garanti", "2 yıl"),
        ],
    ),
    "q-mini-series": _extra(
        "q-mini-series",
        body=[
            "Q Mini, dar niş ve toplantı odalarına sığan kompakt kabinli fine pitch ailedir. 1.2–1.8 mm aralığı 3–6 m izleme mesafesinde keskin görüntü verir.",
            "Sessiz soğutma ofis standartlarına uyar. LEDAJANS keşifte oturma düzeni, native çözünürlük ve kontrol odası mesafesini ölçüp pitch önerir.",
            "Klasik 500 mm kabinden küçük kesim, cam kapı kenarı ve kolon nişine oturur. Ön bakım opsiyonu dar koridoru kurtarır.",
            "16 bit gri, karartılmış salonda bantlaşmayı keser. Slayt şablonu native çözünürlüğe yazılır; ölçeklenmiş 4K yumuşar.",
            "Showroom’da Mini yanına büyük Q duvarı konur; müşteri pitch farkını aynı içerikle görür.",
        ],
        feats=[
            ("İnce pitch", [
                "Yakın izleme mesafesinde keskin görüntü. 4 m oturma için 1.5 mm sınıfı; slayt metni piksel piksel okunur.",
                "1.2 mm daha yakın masa, 1.8 mm 5–6 m oda için speclenir. Keşifte ilk sıra ölçülür.",
                "Makro yüzeyde homojen siyah; ölü piksel teslimde tarama ile kapanır.",
            ]),
            ("Küçük kabin", [
                "Dar niş ve toplantı odasına sığar. Cam kapı kenarı ve kolon giydirmede Mini öne çıkar.",
                "Kesim ritmi büyük Q’dan farklıdır; köşe birleşimi keşif krokisine işlenir.",
                "Taşıma ve kat montajı ofis asansörüne sığar.",
            ]),
            ("Sessiz çalışma", [
                "Ofis ortamına uygun termal tasarım. Fan gürültüsü toplantıyı bölmez.",
                "HVAC yükü keşifte paylaşılır; 7/24 nişte derating yazılır.",
                "Kontrol odası operatör masasıyla aynı odada kalabilir.",
            ]),
            ("16 bit gri", [
                "Düşük parlaklıkta homojenlik. Karartılmış salonda bantlaşma olmaz.",
                "Gece lobi demosu ve gündüz slayt aynı duvarda profil değiştirir.",
                "Kalibrasyon dosyası teslimde verilir.",
            ]),
        ],
        uses=[
            ("use-1", "Kontrol nişi", "Kompakt duvar ve operatör masası."),
            ("use-2", "Showroom karşılaştırması", "Mini kabin büyük duvarın yanında."),
            ("hero", "Toplantı odası", "6 kişilik masada keskin slayt."),
        ],
        specs=[
            ("Piksel aralığı", "1.2 / 1.5 / 1.8 mm"),
            ("Kullanım", "İç mekan sabit, toplantı"),
            ("Refresh", "3840 Hz"),
            ("Kabin", "Mini die-cast"),
            ("Servis", "Ön bakım opsiyonu"),
            ("Garanti", "2 yıl"),
        ],
    ),
    "nc-series": _extra(
        "nc-series",
        body=[
            "NC COB, LED çipin yüzeyde kapsüllendiği darbeye dayanıklı fine pitch’tir. Stüdyo, lobi ve yakın izleme duvarlarında parmak izi ve çarpma SMD’ye göre daha az iz bırakır.",
            "Ortak anot/katot seçenekleri ısıyı düşürür. Yayın kameralarında siyah seviyesi ve 7/24 çalışma profili teklife yazılır.",
            "0.9 / 1.2 mm Pro yakın çekimde sunucu 1–2 m’de durunca öne çıkar. Lobi yürüyüşünde kapsül yüzey ölü piksel riskini keser.",
            "Kalite kontrolde aynı batch karo ızgarası teslim öncesi fotoğraflanır. Renk kayması sınırlı tutulur.",
            "Şişli’de COB örnek duvar randevuyla izlenir; kamera testini yanınızda getirmeniz yeter.",
        ],
        feats=[
            ("COB yüzey", [
                "Çarpma ve toza karşı korumalı modül. Lobi ve stüdyoda SMD’ye göre daha az ölü piksel riski.",
                "Parmak teması kapsülü çizmez; temizlik prosedürü teslimde verilir.",
                "Yakın yürüyüş mesafesinde izleyici duvara yaklaşabilir.",
            ]),
            ("Enerji profili", [
                "Düşük ısı, yüksek verim. 7/24 duvarda soğutma ve elektrik faturası keşifte hesaplanır.",
                "Kabin arkası ısı yolu sade tutulur; HVAC paylaşımı mimara iletilir.",
                "Gece profili parlaklığı düşürür, ömür uzar.",
            ]),
            ("Stüdyo uyumu", [
                "Yayın kameralarında siyah seviyesi. Yüksek refresh ile rolling shutter titremesi kesilir.",
                "Shutter ve refresh aynı satırda eşlenir; moire testi çekimde yapılır.",
                "Sanal set zemin-duvar birleşimi N serisiyle birlikte düşünülür.",
            ]),
            ("Uzun ömür", [
                "Tek tip LED seçimi. Renk kayması batch kontrolüyle sınırlanır.",
                "Teslimde eşleşme raporu ve yedek karo aynı sevkiyatta çıkar.",
                "İstanbul stok arıza süresini kısaltır.",
            ]),
        ],
        uses=[
            ("use-1", "Kurumsal lobi", "Yakın yürüyüşte darbeye dayanıklı COB duvar."),
            ("use-2", "Haber stüdyosu", "Zemin-duvar sanal set."),
            ("hero", "Yayın stüdyosu", "Kamera önünde düşük yansıma."),
        ],
        specs=[
            ("Piksel aralığı", "0.9 / 1.2 mm"),
            ("Paket", "COB"),
            ("Kullanım", "Stüdyo, lobi, yakın izleme"),
            ("Koruma", "Darbeye dayanıklı yüzey"),
            ("Refresh", "3840–7680 Hz sınıfı"),
            ("Garanti", "2 yıl"),
        ],
    ),
    "indoor-q-series": _extra(
        "indoor-q-series",
        body=[
            "İç Mekan Q, ofis, fuar, stüdyo ve perakendede en çok tercih edilen sabit LED ailesidir. Q0.8–Q4 aralığı aynı kabin diliminde ince pitch’ten genel lobi duvarına kadar çıkar.",
            "PWM sürücü, 16 bit gri ve tek batch LED ile renk duvar boyunca homojen kalır. İstanbul showroom’da 1.8 ve 2.5 mm örnekleri yan yana izlenir; keşifte izleme mesafesi ölçülüp pitch kilitlenir.",
            "Otel lobisinde gündüz okunurluk, fuarda kamera refresh’i, perakende atriumda geniş açı aynı ailede speclenir. Native çözünürlük slayt şablonuna yazılır.",
            "Ön bakımlı kabin dar koridoru kurtarır; arka servis için yaklaşık 80 cm boşluk şarttır. 7/24 duvarda gece profili ve ısınma derating’i teklife ayrı satır olur.",
            "LEDAJANS ölçü krokinizle aynı gün keşif randevusu açar. Teslimde operatör eğitimi ve 2 yıl parça-işçilik imzalanır.",
        ],
        feats=[
            ("Dinamik enerji", [
                "PWM sürücü ve akıllı karartma ile tasarruf. Ofiste gündüz düşük nit, lansmanda kısa süreli yüksek parlaklık aynı duvarda yönetilir.",
                "7/24 profil, gece derating ve pano gücü keşif satırına yazılır. Q ailesinde bu üçü aynı kabin diliminde kalır.",
                "Işık sensörü lobide önerilir; tünel ve vitrin içi ayrı kalibre edilir.",
            ]),
            ("Yüksek yenileme", [
                "Titreşimsiz, kamera dostu görüntü. Fuar ve stüdyo çekimlerinde 3840–7680 Hz sınıfı tercih edilir.",
                "Sosyal medya kaydı ve yayın kamerası aynı işlemci diliminde çalışır.",
                "Scan line şikâyeti teslim testinde kapanır; shutter değeri not edilir.",
            ]),
            ("Geniş gri ton", [
                "Düşük ışıklı sahnede detay. 16 bit işleme karanlık salon ve lobi akşamında bantlaşmayı keser.",
                "Otel bar ve sinema köşesinde Q, CS kadar iddialı siyah vermez ama lobi-ofis karışığında yeterlidir.",
                "İçerik mastering’i native’e export edilir.",
            ]),
            ("Tek batch LED", [
                "Renk ve parlaklık homojenliği. Çoklu duvar ve ekspansiyonlarda kalibrasyon dosyası teslim edilir.",
                "Yedek modül aynı batch’ten ayrılır; depo etiketi teslim dosyasına girer.",
                "Renk sapması şikâyeti saha kalibrasyonuyla kapanır.",
            ]),
        ],
        uses=[
            ("use-1", "Plaza karşılama", "8 metre izlemede lobi duvarı."),
            ("use-2", "Perakende atrium", "Geniş açı, alt kottan okunur duvar."),
            ("hero", "Otel lobisi", "Boğaz ışığında gündüz okunur sanat içeriği."),
        ],
        specs=[
            ("Piksel aralığı", "0.8 – 4 mm (Q ailesi)"),
            ("Kullanım", "İç mekan sabit duvar"),
            ("Refresh", "3840–7680 Hz"),
            ("Gri ton", "16 bit"),
            ("Servis", "Ön / arka bakım seçenekli"),
            ("Garanti", "2 yıl"),
        ],
    ),
    "pdc-series": _extra(
        "pdc-series",
        body=[
            "PDC Pro, komuta-kontrol ve 7/24 çalışan toplantı duvarları için yüksek doluluklu fine pitch’tir. 0.9 / 1.2 / 1.5 mm Pro seçenekleri dar koridorda önden servis görür.",
            "Parlaklık profili gece-gündüz ayrı kurgulanır. Isınma, yedek PSU ve sinyal yedekliliği keşif tutanağına yazılır.",
            "Operatör 2–4 m’de oturuyorsa 0.9–1.2 öne çıkar. Pixel shift ve zamanlayıcı panel ömrünü uzatır.",
            "Sessiz soğutma kontrol odası HVAC yükünü paylaşır. Trafik ve kriz masasında harita-kamera ızgarası native çözünürlüğe oturur.",
            "Ön bakım, arkası duvara yaslı nişlerde tek seçenektir. LEDAJANS yedek PSU oranını N+1 yazar.",
        ],
        feats=[
            ("7/24 çalışma", [
                "Kontrol odası parlaklık profili. Pixel shift ve zamanlayıcı önerilir; panel ömrü teklifte hesaplanır.",
                "Gece düşük nit, gündüz vardiya yüksek okunurluk aynı duvarda profil değiştirir.",
                "İzleme yazılımı ve uzaktan alarm ayrı kalem olabilir.",
            ]),
            ("Pro pitch", [
                "0.9 / 1.2 / 1.5 mm. Operatör 2–4 m’de oturuyorsa 0.9–1.2 öne çıkar.",
                "Harita yazısı piksel-eşlenir; ölçeklenmiş 4K yumuşar.",
                "Üç pitch örnek modül showroom’da yan yana durur.",
            ]),
            ("Servis önden", [
                "Dar koridorlarda bakım. Arkası duvara yaslı nişlerde kritikdir.",
                "Teknisyen önden karo sökerek arızayı kapatır; yayın kesintisi dakikadır.",
                "Yedek karo oranı keşifte yazılır.",
            ]),
            ("Düşük ısınma", [
                "Sessiz soğutma. Kontrol odası HVAC yükü keşifte paylaşılır.",
                "Kabin arkası fan kükremesi olmaz; operatör konforu şartnamede durur.",
                "Yaz derating tablosu teslim dosyasındadır.",
            ]),
        ],
        uses=[
            ("use-1", "Trafik kontrol", "Harita ve kamera ızgarası, 7/24."),
            ("use-2", "Kriz masası", "Yakın oturma, Pro pitch."),
            ("hero", "Komuta odası", "Yoğun fine pitch videowall."),
        ],
        specs=[
            ("Piksel aralığı", "0.9 / 1.2 / 1.5 mm Pro"),
            ("Kullanım", "Kontrol / toplantı 7/24"),
            ("Servis", "Ön bakım"),
            ("Sinyal", "Yedekli kontrol önerilir"),
            ("Garanti", "2 yıl"),
        ],
    ),
    "mk-series": _extra(
        "mk-series",
        body=[
            "MK, kavis ve 90° köşe birleşimleri gereken perakende ve atrium işlerindedir. Manyetik modül sökümü vitrin ve fuar standında süreyi kısaltır.",
            "İçbükey-dışbükey yarıçap keşifte maketle doğrulanır. LEDAJANS köşe kitini ve yedek modülü aynı sevkiyatta planlar.",
            "AVM kolon şeridi ve flagship içbükey duvar aynı ailede çözülür. İzleme açısı yürüyüş aksına göre seçilir.",
            "Gece vitrin bakımı tornavida turunu kısaltır. Manyetik tutucular teslim envanterindedir.",
            "Müze iç kavisinde immersif koridor MK ile çizilir; yarıçap mimara milimetreyle iletilir.",
        ],
        feats=[
            ("Kavis", [
                "İçbükey-dışbükey duvar. Yarıçap ve izleme açısı keşifte çizilir.",
                "Esnek modül stüdyoda eğilerek doğrulanır; sahada aynı yarıçap uygulanır.",
                "Kolon şeridi ve ada vitrin aynı ritimde birleşir.",
            ]),
            ("Köşe birleşim", [
                "Kesintisiz 90° dönüş. İki duvar tek içerik gibi okunur.",
                "Köşe kiti ayrı sipariş satırıdır; boşluk kalibrasyonu teslim testidir.",
                "Plaza lobi köşesinde yürüyüş aksı kırılmaz.",
            ]),
            ("Perakende", [
                "AVM atrium ve marka duvarı. Geniş açı oturma ve yürüyüş aksına göre pitch seçilir.",
                "Manyetik karo vitrin içinde gece değişir.",
                "İçerik marka duvarına native export edilir.",
            ]),
            ("Hızlı kurulum", [
                "Manyetik modül. Gece vitrin bakımında tornavida turu kısalır.",
                "Kurulum ekibi karoyu tıklatarak ilerler; karkas önceden hazırlanır.",
                "Yedek karo aynı kutuyla gelir.",
            ]),
        ],
        uses=[
            ("use-1", "Lüks ada vitrin", "Dairesel LED, ürün adasının çevresi."),
            ("use-2", "Müze iç kavis", "İmmersif koridor."),
            ("hero", "AVM atrium", "Kolon şeridi kavisli LED."),
        ],
        specs=[
            ("Uygulama", "Kavis / köşe"),
            ("Kullanım", "İç mekan perakende"),
            ("Montaj", "Manyetik modül"),
            ("Servis", "Ön söküm"),
            ("Garanti", "2 yıl"),
        ],
    ),
    "indoor-r-series": _extra(
        "indoor-r-series",
        body=[
            "İç Mekan R, toplantı, eğitim ve kamu projelerinde sabit kabin ailesidir. Duvar ve zemin sehpa senaryoları aynı seri içinde çözülür.",
            "Çoklu duvar renk eşlemesi ve Türkiye yedek parça stoğu ihalelerde teslim süresini öngörülebilir kılar.",
            "Üniversite amfisi ve meclis salonu geniş açı oturmada R ile speclenir. Native slayt şablonu şartnameye yazılır.",
            "Duvar askı ve sehpa aynı kabin dilimidir. İhale maddesindeki statik ve bakım yönü keşifte kapanır.",
            "Kampüs setlerinde aynı kalibrasyon profili birden fazla salona kopyalanır. Yedek kutu İstanbul’dan çıkar.",
        ],
        feats=[
            ("Kurumsal", [
                "Toplantı ve eğitim salonları. Native çözünürlük slayt şablonuna yazılır.",
                "Amfi ve mecliste yan sıra izleme açısı pitch’i seçtirir.",
                "Kamu şartnamesindeki parlaklık ve ses eşiği keşifte ölçülür.",
            ]),
            ("Stabil kabin", [
                "Duvar ve zemin sehpa. İhale şartnamesindeki askı/duvar maddesi karşılanır.",
                "Sehpa senaryosu taşınır salonlar içindir; dübel planı mimara iletilir.",
                "Kurumsal gri kasa kamera kadrajında sade durur.",
            ]),
            ("Renk kalibrasyonu", [
                "Çoklu duvar eşlemesi. Kampüs ve salon setlerinde aynı profil.",
                "İki bitişik duvar teslimde aynı dosyadan boyanır.",
                "Yıllık kalibrasyon bakımı teklife opsiyon yazılır.",
            ]),
            ("Yedek parça", [
                "Türkiye stoklu servis. Arıza kaydı İstanbul tekniğe düşer.",
                "Depo raflarında etiketli karo ve PSU bekler.",
                "İhale süresi boyunca yedek oranı sözleşmede durur.",
            ]),
        ],
        uses=[
            ("use-1", "Kurumsal eğitim", "U atölye masa, slayt duvarı."),
            ("use-2", "Belediye salonu", "Gündüz stor, sabit LED."),
            ("hero", "Konferans salonu", "Bayraklı kamu düzeni, stabil duvar."),
        ],
        specs=[
            ("Kullanım", "İç mekan sabit"),
            ("Senaryo", "Toplantı / eğitim / kamu"),
            ("Servis", "TR yedek parça"),
            ("Garanti", "2 yıl"),
        ],
    ),
    "cs-series": _extra(
        "cs-series",
        body=[
            "CS, sinema ve karanlık salon izleme için yüksek kontrast iç mekan duvarıdır. Siyah seviyesi ve sessiz soğutma salon gürültü eşiğinin altında kalır.",
            "Geniş açı, yan oturma sıralarında renk kaymasını sınırlar. HDR içerik işleme keşifte oynatıcı ve LED işlemciyle birlikte seçilir.",
            "Projeksiyon fanı yoktur; salon akustik raporu LED lehine döner. Otel balo ve kurumsal screening aynı ailede çözülür.",
            "Karanlık sahnede gerçek siyah, vurgu ışığında patlama olmadan tutulur. Mastering native’e export edilir.",
            "Showroom’da karartılmış köşede CS örneği izlenir; randevu şarttır.",
        ],
        feats=[
            ("Yüksek kontrast", [
                "Karanlık salonlarda siyah seviyesi. Film ve marka filmi detayı kaybolmaz.",
                "Gece sahnesi gerçek siyah kalır; lobi Q’sundan fark burada görünür.",
                "Kalibrasyon sinema eğrisine göre teslim edilir.",
            ]),
            ("Geniş açı", [
                "Salon oturma düzenine uygun. Yan sıra izleyicide renk sapması sınırlıdır.",
                "Amfi genişliğinde pitch ve kabin ritmi keşifte çizilir.",
                "Kenar koltuk testi teslim kriteridir.",
            ]),
            ("Sessiz", [
                "Sinema salonu gürültü eşiği. Fan profili keşifte ölçülür.",
                "Projeksiyon odası kaybolur; makine dairesi HVAC’ye iner.",
                "Gala ve baloda konuşma netliği artar.",
            ]),
            ("İçerik", [
                "HDR uyumlu işleme. Oynatıcı ve işlemci aynı teklifte eşlenir.",
                "Highlight ve gölge aynı karede tutulur.",
                "Dağıtım sunucusu native çözünürlüğe kilitlenir.",
            ]),
        ],
        uses=[
            ("use-1", "Otel gala sineması", "Karanlık drape, geniş LED."),
            ("use-2", "Kurumsal screening", "Deri koltuk, özel salon."),
            ("hero", "Özel sinema", "Yüksek kontrast, geniş koltuk."),
        ],
        specs=[
            ("Kullanım", "Sinema / salon"),
            ("Kontrast", "Yüksek"),
            ("Kullanım yeri", "İç mekan karanlık salon"),
            ("Ses", "Düşük gürültü soğutma"),
            ("Garanti", "2 yıl"),
        ],
    ),
    "n-series": _extra(
        "n-series",
        body=[
            "N serisi, yayın ve stüdyo için dar pitch duvar ve opsiyonel LED zemin ailesidir. Yakın kamera çekiminde modül eşlemesi ve kalibrasyon teslim kriteridir.",
            "Zemin seçeneği yürüyüş yükü ve IP sınıfıyla ayrıca keşfedilir. Stüdyo ısısı ve kamera shutter değerleri teklif notuna yazılır.",
            "Sunucu 1–2 m’de durunca N / COB öne çıkar. Moire testi çekim günü yapılır.",
            "LED floor dans ve spor stüdyosunda yük hesabıyla gelir. Derz ve temizlik prosedürü ayrı maddedir.",
            "Sanal prodüksiyon hacminde duvar-tavan birleşimi N ile çizilir. Kalibrasyon jig’i teslim raporuna girer.",
        ],
        feats=[
            ("Yayın", [
                "Stüdyo kamera uyumu. Refresh ve shutter birlikte seçilir.",
                "Yakın çekimde moire kontrolü teslim testidir.",
                "Çok kameralı sette aynı profil kopyalanır.",
            ]),
            ("Dar pitch", [
                "Yakın çekim. Sunucu 1–2 m’de durunca N / COB öne çıkar.",
                "Makro piksel yoğunluğu stüdyo ışığında homojen kalır.",
                "Yedek karo aynı batch’ten ayrılır.",
            ]),
            ("Zemin seçeneği", [
                "LED floor opsiyonu. Yük, derz ve temizlik prosedürü ayrı maddedir.",
                "Dans prova ve spor stüdyosu yük sınıfı keşifte yazılır.",
                "Zemin IP’si duvar IP’sinden ayrı speclenir.",
            ]),
            ("Kalibrasyon", [
                "Modül eşleme. Teslimde ölçüm raporu verilir.",
                "Jig üzerinde kamera taraması yapılır.",
                "Yıllık tekrar kalibrasyon bakıma yazılır.",
            ]),
        ],
        uses=[
            ("use-1", "Sanal prodüksiyon", "Duvar ve tavan LED hacmi."),
            ("use-2", "Spor stüdyosu", "LED zemin grafik, sunucu."),
            ("hero", "Yayın zemini", "Sunucu LED floor üzerinde."),
        ],
        specs=[
            ("Kullanım", "Stüdyo / yayın"),
            ("Pitch", "Fine / N serisi"),
            ("Opsiyon", "LED zemin"),
            ("Garanti", "2 yıl"),
        ],
    ),
    "rw-series": _extra(
        "rw-series",
        body=[
            "RW, iç-dış rental kabindir. 2.6 / 2.9 iç, 3.9 dış sınıfları konser ve turda aynı kilit diliyle çalışır. Eğim (curve), uçuş kasası ve yüzde 5–10 yedek modül kiralama paketinin parçasıdır.",
            "Aynı gece kurulum-söküm için kilit pimi ve power/data loop keşif formunda çizilir. Jeneratör gücü ve truss yükü LEDAJANS saha ekibiyle netleşir.",
            "Açık hava festivalde IP sınıfı dış kabin seçilir. Yağmur planı sözleşmenin ilk maddelerindendir.",
            "IMAG ve ana duvar aynı işlemci diliminde çalışır. 3840 Hz sınıfı yayın kamerasını titretmez.",
            "Flight case etiketleme ve envanter teslimde paylaşılır. Erkrath lojistiği Avrupa, İstanbul stok Türkiye ayağını taşır.",
        ],
        feats=[
            ("Hızlı kilit", [
                "Curving ve düz duvar aynı gece. Pim ve açı takozu saha çantasında gelir.",
                "Load-in’de eller pimi kilitler; eğim takozu sete dahildir.",
                "Söküm penceresi sözleşmeye saat olarak yazılır.",
            ]),
            ("İç-dış", [
                "2.6 / 2.9 iç, 3.9 dış. Yağmurda IP sınıfı dış kabin seçilir.",
                "Depoda iç ve dış duvar yan yana kıyaslanır; pitch kararı burada kilitlenir.",
                "Karışık sette işlemci katmanı ayrılır.",
            ]),
            ("Flight case", [
                "Tur lojistiğine uygun. Kasa etiketleme ve envanter teslimde paylaşılır.",
                "Backstage kasa sırası load-out hızını belirler.",
                "Kasa ağırlığı araç planına girer.",
            ]),
            ("Yüksek refresh", [
                "Yayın ve konser kamerası. IMAG ve ana duvar aynı işlemci diliminde çalışır.",
                "Scan line sahne kaydında kapanır.",
                "Yönetmen native çözünürlüğü overlay’e yazar.",
            ]),
        ],
        uses=[
            ("use-1", "Festival ana sahne", "Truss fly, gece konser."),
            ("use-2", "İç mekân kavis", "Kapalı konser, eğimli duvar."),
            ("hero", "Açık hava konser", "Hızlı kilitli ana LED."),
        ],
        specs=[
            ("Piksel aralığı", "2.6 / 2.9 / 3.9 mm"),
            ("Kullanım", "Rental iç / dış"),
            ("Kabin", "Hızlı kilit"),
            ("Yedek", "Modül %5–10 önerilir"),
            ("Garanti", "Kiralama süresi + servis"),
        ],
    ),
    "cg-series": _extra(
        "cg-series",
        body=[
            "CG, hafif rental kabindir; truss askı ve zemin stack’te yükü düşürür. Fuar standında üç cephe duvar iki günde kurulur, gece sökülür.",
            "Hot-swap modül sahada dakika içinde değişir. LEDAJANS yedek seti stand planına işler.",
            "Karbon görünümlü ince kasa stüdyo tartısında hafif durur. Truss hesabı keşifte paylaşılır.",
            "Otomotiv ve teknoloji fuarında ada standı asılı LED ile çözülür. Köşe ve kapı boşlukları plana işlenir.",
            "Fuar yönetmeliği saatine uyum için söküm ekibi gece vardiyasına yazılır.",
        ],
        feats=[
            ("Hafif", [
                "Askı yükünü düşürür. Truss hesabı keşifte paylaşılır.",
                "Karbon görünümlü kasa tartıda rakipten düşük kalır.",
                "Fly senaryosunda motor kapasitesi rahatlar.",
            ]),
            ("Fuar", [
                "Stand üç cephe duvar. Köşe ve kapı boşlukları plana işlenir.",
                "İki günlük kurulum penceresi sözleşmeye yazılır.",
                "Ada standı asılı şeritlerle tamamlanır.",
            ]),
            ("Hızlı söküm", [
                "Gece kurulum. Fuar yönetmeliği saatine uyum.",
                "Strike ekibi kasa etiketine göre yükler.",
                "Ertesi gün başka standa aynı set gidebilir.",
            ]),
            ("Yedek", [
                "Sahada hot-swap modül. Envanter listesi teslimde imzalanır.",
                "Arızalı karo saniyeler içinde çıkar.",
                "Yedek oranı stand metrajına yazılır.",
            ]),
        ],
        uses=[
            ("use-1", "Otomotiv fuarı", "Hafif rental, üç cephe."),
            ("use-2", "Teknoloji adası", "Asılı LED şeritler."),
            ("hero", "Fuar standı", "İki gün kurulum, gece söküm."),
        ],
        specs=[
            ("Kullanım", "Rental / fuar"),
            ("Ağırlık", "Hafif kabin"),
            ("Kurulum", "Stack / fly"),
            ("Garanti", "Proje bazlı"),
        ],
    ),
    "ln-series": _extra(
        "ln-series",
        body=[
            "LN, lineer sahne LED’idir: ana ekran, kanat ve IMAG aynı ailede uzar. Açık hava festivalde IP opsiyonu seçilir.",
            "Stack ve fly senaryosu rüzgar ve truss yüküyle birlikte hesaplanır. Otomotiv lansmanında 40 m² sınıfı örnek referanslarımızdadır.",
            "Yönetmen native çözünürlüğü ana duvar ve kanatlara ayrı yazar. Simetri aynı kilit dilinde kalır.",
            "Yağmur kılıfı ve IP kabin festival keşif maddesidir. Motor fly açık havada rüzgar notu ister.",
            "Hızlı kilit load-in penceresini kısaltır. LEDAJANS saha çantası pim ve takozu getirir.",
        ],
        feats=[
            ("Sahne", [
                "Ana ekran ve IMAG. Yönetmen çözünürlüğü native’e yazılır.",
                "Kanatlar ana duvarla aynı ailede uzar.",
                "Konser kaydı titremesiz çıkar.",
            ]),
            ("Kanat", [
                "Lineer uzatma. Simetri ve eğim aynı kilit dilinde.",
                "Sahne çizgisi temiz kalır; boşluk kalibrasyonu teslim testidir.",
                "Lansman arenasında backdrop + kanat tek set.",
            ]),
            ("IP opsiyon", [
                "Açık hava festival. Yağmur planı keşif maddesidir.",
                "Kılıf ve conta teslim kontrolündedir.",
                "Jeneratör ve toprak ayrı satırdır.",
            ]),
            ("Hız", [
                "Hızlı kilit. Load-in penceresi sözleşmeye yazılır.",
                "Stack kabinler sahne önünde kilitlenir.",
                "Fly motor zamanı teknik rider’a girer.",
            ]),
        ],
        uses=[
            ("use-1", "Otomotiv lansman", "Lineer backdrop."),
            ("use-2", "Festival fly", "Motorlu asılı ana duvar."),
            ("hero", "Ana sahne + IMAG", "Kanatlı gece konser."),
        ],
        specs=[
            ("Kullanım", "Konser / festival / lansman"),
            ("Kurulum", "Stack / fly"),
            ("IP", "Opsiyonel dış"),
            ("Garanti", "Proje bazlı"),
        ],
    ),
    "dm-series": _extra(
        "dm-series",
        body=[
            "DM, ince çerçeveli modern rental kasadır. TV çekimi ve turda sahne estetiği ile yüksek refresh bir arada istenir.",
            "Ön-arka bakım, ekip taşıma yükünü ve yayın molasını kısaltır.",
            "Kamera kadrajında kalın çerçeve kaybolur. Fashion ve talk-show setinde DM öne çıkar.",
            "Hafif kasa günlük load-in sayısını artırır. Tur kasasına sığan incelik lojistiği rahatlatır.",
            "Studio shutter ile refresh teklifte eşlenir. LEDAJANS yedek karoyu set planına işler.",
        ],
        feats=[
            ("Modern kasa", [
                "İnce çerçeve, sahne estetiği. Kamera kadrajında kalın çerçeve kaybolur.",
                "Kenar profili stüdyo çekiminde sade durur.",
                "Moda seti ışığında kasa görünmez.",
            ]),
            ("TV çekimi", [
                "Yüksek refresh. Studio shutter ile eşlenir.",
                "Monitörde titreme olmaz; çok kamera aynı profili kullanır.",
                "Talk-show izleyici koltukları önünde backdrop temiz kalır.",
            ]),
            ("Hafif", [
                "Ekip taşıma yükü düşük. Günlük load-in sayısı artar.",
                "Stüdyo koridorunda iki kişi kabini taşır.",
                "Tur seti ince kasa ile daha çok metraj sığdırır.",
            ]),
            ("Servis", [
                "Ön-arka bakım. Yayın arasında modül değişimi.",
                "Mola süresinde karo çıkar; yayın devam eder.",
                "Yedek set kasa içinde bekler.",
            ]),
        ],
        uses=[
            ("use-1", "Talk-show backdrop", "İzleyici koltukları, ince çerçeve."),
            ("use-2", "Tur TV seti", "İnce kabinler kasada."),
            ("hero", "TV sahnesi", "Bezel’siz modern duvar."),
        ],
        specs=[
            ("Kullanım", "Rental / yayın"),
            ("Kasa", "İnce çerçeve"),
            ("Servis", "Ön ve arka"),
            ("Garanti", "Proje bazlı"),
        ],
    ),
    "pm-series": _extra(
        "pm-series",
        body=[
            "PM, panel-modül rental ve yedekleme odaklıdır. Karışık pitch iç-dış setlerde hot-swap ve flight case envanteri öne çıkar.",
            "Turda kilit pimi ve yedek PSU oranı keşif formunun ilk sayfasındadır.",
            "Canlı duvarda karo saniyeler içinde değişir. Arıza kaydı WhatsApp hattına düşer.",
            "Kasa köpük kesimi modüle göredir. Tır rampa ve depo rafları aynı etiket dilini kullanır.",
            "İç-dış karışık stack aynı dükkânda hazırlanır. LEDAJANS envanteri teslimde imzalatır.",
        ],
        feats=[
            ("Modül yedek", [
                "Sahada dakika içinde değişim. Arıza kaydı WhatsApp hattına düşer.",
                "Canlı duvarda hot-swap; yayın kesintisi saniyedir.",
                "Yedek oranı metraja yazılır.",
            ]),
            ("Tur", [
                "Flight case set. Kasa ağırlığı araç planına yazılır.",
                "Köpük kesimli kasa tır rampa yüklemesini hızlandırır.",
                "Etiket dili depo ve saha arasında aynıdır.",
            ]),
            ("Kilit", [
                "Hızlı kilit pim. Eğim takozu sete dahildir.",
                "Pim makro çekimi saha eğitimine girer.",
                "Kayıp pim yedeği çantada durur.",
            ]),
            ("Karışık pitch", [
                "İç-dış set. İşlemci katmanı keşifte ayrılır.",
                "Aynı dükkânda iç ve dış stack yan yana durur.",
                "Tur paketi iki pitch’i ayrı kasa rengine boyar.",
            ]),
        ],
        uses=[
            ("use-1", "Venue load-in", "Yedek ağırlıklı kiralama paketi."),
            ("use-2", "Tur tırı", "PM flight case dolu."),
            ("hero", "Rental depo", "Panel, yedek, etiketli kasa."),
        ],
        specs=[
            ("Kullanım", "Rental yedekleme / tur"),
            ("Lojistik", "Flight case"),
            ("Yedek", "Modül + PSU"),
            ("Garanti", "Proje bazlı"),
        ],
    ),
    "outdoor-q-series": _extra(
        "outdoor-q-series",
        body=[
            "Dış Mekan Q, cadde, AVM cephe ve durak DOOH için yüksek parlaklık ailesidir. Q5 / Q6.6 / Q8 sınıfı güneş altında okunur; IP ve alüminyum kabin yağmur-toza karşı kapanır.",
            "Uzaktan yayın (SIM/fiber) ve parlaklık profili (güney cephe vs tünel) fiyatı belirler. Keşifte rüzgar, bakım koridoru ve belediye izin notu toplanır.",
            "Güney cephe öğle güneşinde hâlâ okunur kalır. Otomatik ışık sensörü önerilir.",
            "Conta, drenaj ve kapak detayı teslim kontrolündedir. Yaz-kış derating tablosu paylaşılır.",
            "DOOH izleme yazılımı ve yedekli SIM teklife ayrı kalem olabilir. LEDAJANS keşif tutanağını statikçiyle paylaşır.",
        ],
        feats=[
            ("Yüksek nit", [
                "Güneş altında okunur. Güney cephe için parlaklık sınıfı keşifte ölçülür.",
                "Öğle vakti AVM cephesi hâlâ grafik taşır.",
                "Tünel ve gece profili ayrı kalibre edilir.",
            ]),
            ("IP koruma", [
                "Yağmur ve toz. Conta, drenaj ve kabin kapak detayı teslim kontrolündedir.",
                "Yağmur taneleri conta üzerinde kalır; iç modül ıslanmaz.",
                "Yıllık conta kontrolü bakıma yazılır.",
            ]),
            ("Uzaktan yayın", [
                "DOOH içerik. Fiber veya yedekli SIM, izleme yazılımı teklife eklenir.",
                "Kontrol odası ekranları uzaktaki billboard’u izler.",
                "Zamanlayıcı gece-gündüz profilini değiştirir.",
            ]),
            ("Alüminyum kabin", [
                "Dış ortam ısısı. Yaz-kış derating tablosu paylaşılır.",
                "Isı kanatları stüdyo çekiminde görünür; sahada aynı kasa durur.",
                "Arka kapak bakım platformu keşif maddesidir.",
            ]),
        ],
        uses=[
            ("use-1", "Durak LED", "Yaya ve gündüz okunurluk."),
            ("use-2", "AVM medya cephe", "Alacakaranlık, yüksek nit."),
            ("hero", "Cadde billboard", "İstanbul caddesi, güneş altı."),
        ],
        specs=[
            ("Piksel aralığı", "5 / 6.6 / 8 mm sınıfı"),
            ("Parlaklık", "Yüksek nit, gündüz profili"),
            ("IP", "Dış mekan"),
            ("Kabin", "Alüminyum, arka bakım"),
            ("Garanti", "2 yıl"),
        ],
    ),
    "outdoor-s-series": _extra(
        "outdoor-s-series",
        body=[
            "Dış Mekan S, stadyum peri-led ve büyük format DOOH için dayanımlı kabindir. Rüzgar, titreşim ve tribün mesafesi pitch seçimini belirler.",
            "Arka koridor bakım ve gündüz maç yayını için yüksek parlaklık aynı seride toplanır.",
            "5–8 mm sınıfı üst tribünden okunur. Çelik konstrüksiyon işverenin statikçisiyle eşlenir.",
            "Maç günü erişim prosedürü yazılıdır. Otomatik ışık sensörü gündüz maçta önerilir.",
            "Peri-led çim çevresi ve yol kenarı büyük format aynı ailede speclenir. LEDAJANS rüzgar notunu keşfe işler.",
        ],
        feats=[
            ("Stadyum", [
                "Uzun izleme mesafesi. 5–8 mm sınıfı tribün okuma mesafesine göre seçilir.",
                "Üst tribünden skor ve grafik okunur.",
                "Peri-led çim çevresinde ayrı metrajdır.",
            ]),
            ("Dayanım", [
                "Rüzgar ve titreşim. Çelik konstrüksiyon işverenin statikçisiyle eşlenir.",
                "Gantry üzerindeki kabinler rüzgâr yüküne göre ankrajlanır.",
                "Titreşim keşif notuna yazılır.",
            ]),
            ("Servis", [
                "Arka koridor bakım. Maç günü erişim prosedürü yazılır.",
                "Teknisyen koridordan PSU’ya ulaşır.",
                "Emniyet planı kuruluma eklenir.",
            ]),
            ("Yüksek parlaklık", [
                "Gündüz maç yayını. Otomatik ışık sensörü önerilir.",
                "Güneşli öğle maçında grafik solmaz.",
                "Gece maç profili ayrıca kaydedilir.",
            ]),
        ],
        uses=[
            ("use-1", "Peri-led", "Çim çevresi, gündüz."),
            ("use-2", "Yol kenarı DOOH", "S kabin, büyük format."),
            ("hero", "Stadyum LED", "Maç günü, peri + ana ekran."),
        ],
        specs=[
            ("Piksel aralığı", "5 / 6.6 / 8 mm"),
            ("Kullanım", "Stadyum / büyük DOOH"),
            ("IP", "Dış mekan"),
            ("Bakım", "Arka koridor"),
            ("Garanti", "2 yıl"),
        ],
    ),
    "qm-series": _extra(
        "qm-series",
        body=[
            "QM, 640×480 ince alüminyum çok amaçlı kabindir. İç ve yarı açık duvar, kolon ve asma tavan işlerinde duvar kalınlığını düşürür.",
            "Standart modül uyumu yedeklemeyi kolaylaştırır. İstanbul stoklu PSU ve kablo seti aynı siparişte çıkar.",
            "Sıva ile neredeyse aynı düzlemde durur; mimari milimetre keşifte işlenir.",
            "Yarı açık saçak ve müze asma şerit aynı kasa ritmindedir. IP beklentisi ayrı spece yazılır.",
            "Kolon giydirme 640×480 adımıyla döner. LEDAJANS askı yükünü statikçiye iletir.",
        ],
        feats=[
            ("İnce kasa", [
                "Duvar kalınlığını düşürür. Mimari detay keşifte milimetreyle işlenir.",
                "Alçıpan ile neredeyse aynı düzlem; niş derinliği kısalır.",
                "Yan profil stüdyoda inceliği gösterir.",
            ]),
            ("640×480", [
                "Standart modül uyumu. Yedek stok planı sadeleşir.",
                "Açık arka kasa modül oturuşunu gösterir.",
                "PSU ve kart aynı ritimde durur.",
            ]),
            ("Çok amaç", [
                "İç ve yarı açık alan. IP beklentisi ayrı spece yazılır.",
                "Saçak altı gündüz yayını QM ile çözülür.",
                "Müze asma şerit aynı kasayı kullanır.",
            ]),
            ("Hafif", [
                "Asma tavan / duvar. Askı yükü statikçiye iletilir.",
                "Kolon wrap lobi içinde döner.",
                "Perakende nişinde askı görünmez.",
            ]),
        ],
        uses=[
            ("use-1", "Kolon wrap", "Lobi içinde ince QM."),
            ("use-2", "Perakende niş", "İnce duvar, askıda ürün."),
            ("hero", "Mimari slot", "640×480 ince alüminyum duvar."),
        ],
        specs=[
            ("Kabin", "640×480 mm"),
            ("Malzeme", "Alüminyum"),
            ("Kullanım", "Çok amaçlı iç / yarı açık"),
            ("Garanti", "2 yıl"),
        ],
    ),
    "mg-series": _extra(
        "mg-series",
        body=[
            "MG, dış mekan döküm alüminyum kabin ve 320×160 modül ailesidir. Cadde billboard ve durak işlerinde Q/S 5–8 mm ile birlikte speclenir.",
            "Arka kapak bakım ve su-toz contası teslim kontrol listesindedir.",
            "Yaygın 320×160 saha yedeğini kolaylaştırır. Conta değişim aralığı bakıma yazılır.",
            "Belediye izin ve aydınlatma yönetmeliği keşif notudur. Platform ve emniyet planı kuruluma eklenir.",
            "Otoyol billboard ve meydan totem aynı döküm kasayı kullanır. LEDAJANS PSU kapak servisini arka kapıdan yapar.",
        ],
        feats=[
            ("Döküm kabin", [
                "Dış ortam su ve toz. Conta değişim aralığı bakıma yazılır.",
                "Açık arka kapak stüdyoda conta hattını gösterir.",
                "Kış-yaz conta kontrolü sözleşmeye girer.",
            ]),
            ("320×160", [
                "Yaygın dış mekan modül. Saha yedeği kolay bulunur.",
                "Izgara tezgâhında yedek karo sayılır.",
                "Pitch 5 / 6.6 / 8 mm aynı modül dilimidir.",
            ]),
            ("Cadde", [
                "Billboard ve durak. Belediye izin ve aydınlatma yönetmeliği keşif notudur.",
                "Trafik bokeh’inde totem ve durak yan yana durur.",
                "İçerik uzaktan zamanlanır.",
            ]),
            ("Servis", [
                "Arka kapak bakım. Platform ve emniyet planı kuruluma eklenir.",
                "Teknisyen PSU’yu kapaktan değiştirir.",
                "Yedek PSU İstanbul stoktan çıkar.",
            ]),
        ],
        uses=[
            ("use-1", "Otoyol billboard", "Altın saat, MG kabin."),
            ("use-2", "Meydan totem", "Yaya trafiği, döküm kasa."),
            ("hero", "Cadde billboard", "320×160 kenarda görünür."),
        ],
        specs=[
            ("Modül", "320×160 mm"),
            ("Pitch", "5 / 6.6 / 8 mm"),
            ("Kullanım", "Dış mekan reklam"),
            ("Kabin", "Döküm alüminyum"),
            ("Garanti", "2 yıl"),
        ],
    ),
    "p-series": _extra(
        "p-series",
        body=[
            "P serisi güç kaynağı ve kabin aksesuar ailesidir. Q ve rental duvarların yedekli PSU, konnektör ve kablolama setini tamamlar.",
            "İstanbul yedek stoku arıza süresini kısaltır. Teklifte ekranla birlikte PSU adedi ve yedek oranı yazılır.",
            "7/24 işlerde N+1 güç kaynağı ayrı satırdır. Yanlış konnektör riski keşifte kapanır.",
            "Rental sökümde hızlı konnektör kablo hasarını azaltır. Depo rafları sevkiyata hazır bekler.",
            "Mevcut duvar genişletmede uyum keşifte doğrulanır. LEDAJANS aynı gün kargo veya saha bırakır.",
        ],
        feats=[
            ("Güç", [
                "Yedekli PSU seçenekleri. 7/24 duvarda N+1 önerilir.",
                "Çift PSU slotu kabinde yan yana durur.",
                "Derating tablosu teslim dosyasındadır.",
            ]),
            ("Kabin uyumu", [
                "Q / rental aileleri. Yanlış konnektör riski keşifte kapanır.",
                "İç ve rental kabin yanında eşleşen parça fotoğraflanır.",
                "Genişletme işinde eski kasa ölçülür.",
            ]),
            ("Kablolama", [
                "Hızlı konnektör. Rental sökümde kablo hasarı azalır.",
                "Power/data kangal teslim setindedir.",
                "Etiket dili saha ile depo arasında aynıdır.",
            ]),
            ("Stok", [
                "İstanbul yedek. Aynı gün kargo veya saha bırakma.",
                "Raf fotoğrafı sevkiyat listesine bağlanır.",
                "Kritik duvarda yedek PSU önceden ayrılır.",
            ]),
        ],
        uses=[
            ("use-1", "7/24 arka kasa", "N+1 PSU takılı."),
            ("use-2", "Rental yedek çanta", "PSU kasası venue’de."),
            ("hero", "Proje yedek kiti", "PSU, kablo, konnektör tezgâhı."),
        ],
        specs=[
            ("Tip", "Kabin / güç aksesuar"),
            ("Uyum", "Toeled serileri"),
            ("Yedek", "İstanbul stok"),
            ("Garanti", "2 yıl"),
        ],
    ),
    "v-series-": _extra(
        "v-series-",
        body=[
            "V serisi dikey totem, sütun ve yaratıcı form aksesuar kabinidir. İç mekan asma ve klipsli servis, vitrin totemlerinde öne çıkar.",
            "URL /v-series-/ korunur; vitrinde başlık V Serisi’dir. Özel form için çizim keşifte alınır.",
            "Otel girişi ve AVM yürüyüş aksında çift totem yönlendirme verir. İzleme yüksekliği keşifte işaretlenir.",
            "Düzensiz marka duvarı özel karkas ister; üretim çizim onayından sonra başlar.",
            "Vitrin içi bakım klipsle kısa kesilir. LEDAJANS askı detayını mimarla paylaşır.",
        ],
        feats=[
            ("Dikey", [
                "Sütun ve totem. İzleme yüksekliği keşifte işaretlenir.",
                "Otel girişi çift totemle simetrik durur.",
                "AVM yürüyüş aksında creative dikey içerik native export edilir.",
            ]),
            ("Yaratıcı", [
                "Özel form destek. Çizim onayından sonra üretim.",
                "Düzensiz marka duvarı karkasla birleşir.",
                "Kesim toleransı teslim kontrolündedir.",
            ]),
            ("Hafif", [
                "İç mekan asma. Askı detayı mimarla paylaşılır.",
                "Cam atrium içinde asılı dikey şerit süzülür.",
                "Yük hesabı statikçiye iletilir.",
            ]),
            ("Servis", [
                "Hızlı klips. Vitrin içi bakım kısa kesilir.",
                "Mağaza vitrininde totem kapağı saniyede açılır.",
                "Yedek karo vitrin deposunda durur.",
            ]),
        ],
        uses=[
            ("use-1", "Yönlendirme totem", "Hol içinde dikey bilgi."),
            ("use-2", "Vitrin totem", "Gece cadde, mağaza camı."),
            ("hero", "AVM dikey", "Yürüyüş aksı, creative totem."),
        ],
        specs=[
            ("Kullanım", "Totem / dikey / özel form"),
            ("Kabin", "V serisi"),
            ("Kurulum", "İç asma / zemin"),
            ("Garanti", "2 yıl"),
        ],
    ),
}
