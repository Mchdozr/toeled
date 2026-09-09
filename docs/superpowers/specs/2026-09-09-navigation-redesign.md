# Toeled Üst Menü Tasarımı

## Hedef
Eski, görsel üzerine binen ve hizası bozulan navigasyonu; tüm sayfalarda aynı çalışan, aydınlık, okunur ve erişilebilir bir mega menüyle değiştirmek.

## Tasarım
- 76px opak beyaz header, ince lacivert ayraç ve kontrollü gölge.
- Masaüstünde ortalanmış ana bağlantılar; sağda lacivert “Teklif Al” CTA.
- Ürünler için kategori, seri ve görsel/CTA alanlarından oluşan üç kolonlu mega panel.
- Referanslar, Destek ve Haberler için daha küçük iki kolonlu paneller.
- Mobilde hamburger ile açılan tam ekran panel ve yerel `details` akordeonları.
- Hover, tıklama, dışarı tıklama ve Escape davranışları; `aria-expanded` ve `aria-hidden` durumları.

## Teknik yaklaşım
Statik sayfalardaki tekrar eden eski `<header>` blokları tek standart HTML şablonuyla mekanik olarak değiştirilecek. Görsel katman `motion.css`, erişilebilir etkileşim `my-js.js` içinde ve yalnızca `tl-` isim alanında tutulacak.
