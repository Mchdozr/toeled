# Shared layouts

Duplicated in every `index.html`. Source of truth used here: `contact-us/index.html`.

## SiteHeader
File: `contact-us/index.html` lines 99–454  
Fixed header: desktop mega-nav + mobile drawer. Logo pair, nav (Ürünler, Referanslar, Destek, Haberler, Hakkımızda, İletişim), search, `info@ledajans.com`, social icons.

```html
<header>
  <div class="header md-dn">
    <div class="mauto dflrs items-center">
      <a href="/" class="logo">
        <img class="i1" src="/public/wwwroot/images/logo.svg" alt="Logo">
        <img class="i2" src="/public/wwwroot/images/logo10.svg" alt="Logo">
      </a>
      <nav>
        <ul class="header-ul">
          <li><a href="/products/">Ürünler</a><!-- mega: İç Mekan / Kiralama & Sahne / Dış Mekan / Aksesuarlar + series --></li>
          <li><a href="/cases/">Referanslar</a></li>
          <li><a href="/debugger/">Destek</a></li>
          <li><a href="/news/">Haberler</a></li>
          <li><a href="/about-us/">Hakkımızda</a></li>
          <li><a href="/contact-us/">İletişim</a></li>
        </ul>
      </nav>
      <div class="header-top items-center">
        <div class="search-b"><input id="keywords" type="text"></div>
        <a href="mailto:info@ledajans.com;" class="item items-center">
          <span>info@ledajans.com</span>
        </a>
      </div>
    </div>
  </div>
  <div class="header-m abs dn md-db">
    <a href="/" class="logo"><img src="/public/wwwroot/images/logo10.svg" alt="Logo"></a>
  </div>
</header>
```

Full mega-menu source is in `contact-us/index.html` 99–454 (desktop) and 345–454 (mobile accordion).

## SiteFooter
File: `contact-us/index.html` lines 526–590

```html
<footer>
  <div class="public-footer-b">
    <div class="public-footer">
      <div class="top justify-between">
        <div class="public-footer-i">
          <p><img class="logo" src="/public/wwwroot/images/logo.svg" alt=""/></p>
          <div class="public-footer-site">Sosyal medya</div>
        </div>
        <div class="list justify-between">
          <div class="list-i">
            <a class="title" href="/products/">Ürünler</a>
            <a href="/commercial-display/" class="info">İç Mekan</a>
            <a href="/rental-staging/" class="info">Kiralama &amp; Sahne</a>
            <a href="/dooh/" class="info">Dış Mekan</a>
            <a href="/accessories/" class="info">Aksesuarlar</a>
          </div>
          <div class="list-i">
            <a class="title" href="/sales-outlets/">Destek</a>
            <a class="info" href="/sales-outlets/">Satış Noktaları</a>
            <a class="info" href="/service/">Service</a>
            <a class="info" href="/knowledge/">Bilgi Merkezi</a>
            <a class="info" href="/debugger/">Teknik Destek</a>
          </div>
          <div class="list-i">
            <a class="title" href="/cases/">Referanslar</a>
          </div>
          <div class="list-i">
            <a class="title" href="/contact-us/">İletişim</a>
            <a class="title title2" href="/about-us/">Hakkımızda</a>
            <a class="title title2" href="/news/">Haberler</a>
          </div>
        </div>
        <div class="contact-card">
          <p class="contact-item-p1">E-posta:</p>
          <p class="contact-item-p2">info@ledajans.com</p>
          <p class="contact-item-p1">Telefon:</p>
          <p class="contact-item-p2">+90 212 220 40 04 · +90 543 879 51 08 · +90 530 405 67 68</p>
          <p class="contact-item-p1">Adres:</p>
          <p class="contact-item-p2">TAHA LED Dış Ticaret A.Ş. — Halide Edip Adıvar Mah. Gül 2 Sk. No:10a, 34382 Şişli/İstanbul<br>Almanya: Heinrich-Hertz-Straße 50, 40699 Erkrath<br>Kıbrıs: Karaoğlanoğlu Cad., Girne</p>
        </div>
      </div>
      <div class="public-footer-num">
        <p>Copyright © TAHA LED Dış Ticaret A.Ş. · Toeled. Tüm hakları saklıdır.</p>
      </div>
    </div>
  </div>
</footer>
```

## FloatInquiry
File: `contact-us/index.html` lines 591–635 — right-edge overlay form `#fdForm` with Ad Soyad, E-posta, Telefon / WhatsApp, Mesaj, Gönder.
