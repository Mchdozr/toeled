# Toeled Navigasyon İmplementasyon Planı

> **Agentic çalışanlar için:** `executing-plans` kuralını uygula.

**Hedef:** Tüm statik sayfalarda ortak, erişilebilir ve responsive mega menü kurmak.
**Mimari:** Tek HTML şablonu 52 sayfaya uygulanacak; stiller ve davranış mevcut ortak asset dosyalarında tutulacak.
**Teknoloji:** HTML, CSS, vanilla JavaScript, Python unittest.

### Görev 1: Navigasyon sözleşmesi
- [x] `tests/test_navigation.py` ile yeni işaretleme, asset sürümü, stil ve klavye davranışı beklentilerini tanımla.
- [x] Testi çalıştırıp mevcut yapıda başarısız olduğunu doğrula.

### Görev 2: Ortak işaretleme
- [ ] Eski desktop/mobile header bloklarını `tl-site-header` şablonuyla değiştir.
- [ ] Ürünler, Referanslar, Destek ve Haberler panellerini ekle.
- [ ] Mobil akordeon ve teklif CTA’sını ekle.

### Görev 3: Görsel ve davranış
- [ ] Eski navigasyon override’larını kaldırıp `tl-` isim alanlı stilleri yaz.
- [ ] Hover, tıklama, Escape, dışarı tıklama ve mobil aç/kapat davranışını yaz.
- [ ] Asset sürümlerini `1.1.0` yap.

### Görev 4: Doğrulama
- [ ] `python -m unittest tests.test_navigation -v`
- [ ] HTML içinde eski header kalmadığını doğrula.
- [ ] Desktop ve mobil tarayıcı kontrollerini yap.
