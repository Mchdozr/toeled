# Toeled Design System

## Product
Toeled (toeled.com) is TAHA LED Dış Ticaret A.Ş. / LEDAJANS's B2B LED display site: indoor, outdoor/DOOH, rental & staging sales, install, and support. Offices in Istanbul (Şişli), Erkrath (Germany), and Girne (Cyprus). Contact: info@ledajans.com, +90 212 220 40 04.

The live site is a cloned Qiangli manufacturer template (mega menu, Swiper hero, duplicated header/footer). Visual language is industrial navy + white photography. Conversion is weak: `/contact-us/` dumps a PHP error, embeds a Xiamen China map, and uses a generic "Online Message" form with no project-spec fields.

## JTBD
A venue owner, agency, or integrator needs a quote for LED screen size, indoor vs outdoor vs rental, and gets a same-day callback from Istanbul.

## Key pages
- `/` product storytelling home
- `/products/` + series pages
- `/contact-us/` current contact (to be replaced in conversion quality by `/teklif/`)
- Support: debugger, knowledge, cert lookup

## Brand
- Logo: TOELED wordmark (white on dark, black on light). Never invent a mark or use Qiangli/9thPanel logos.
- Navy `#112698` primary, deep `#001584`, white surfaces, text `#171717` / `#333`
- Accent sparingly: red `#ee1d23`, orange `#d96515`
- Font: Microsoft YaHei / Arial / system sans. No serif, no decorative display fonts.
- CTA: 45px pill, 23px radius, navy fill, white label ("Teklif Alın" / "Gönder")
- Content max ~1600px, generous whitespace, centered 42px navy titles
- Photography: real LED walls / events; no generic stock office people
- Language: Turkish UI. No leftover English ("Online Message") and no China factory map.

## Motion (local — Superdesign’dan kopyalandı, credit harcamadan kullan)
Kaynak: `public/wwwroot/css/motion.css` + `my-js.js` `initToeledMotion`.
- Scroll reveal: mevcut `[hsm]` / `[hsm=fadeup|fadel|fader]` + `.hsms` stagger 80ms
- CTA: navy gradient kayması, `translateY(-1px)`, lacivert gölge
- Kart: `translateY(-4px)` + `rgba(17,38,152,.35)` gölge
- Nav underline: 0.4s ease; mega menü fade + 8px slide
- Input focus: `#112698` ring `0 0 0 3px rgba(17,38,152,.08)`
- Sayfa geçişi: View Transitions API (`navigation: auto`)
- `prefers-reduced-motion` ile hepsi kapanır
Yeni animasyon için Superdesign’a gitme; bu dosyayı genişlet.

## Quote page requirements
Two-column desktop: left trust (phones, Istanbul address, 24s dönüş), right structured form:
Ad Soyad, Şirket, E-posta, Telefon/WhatsApp, kullanım (İç mekan / Dış mekan / Kiralama & Sahne / DOOH), yaklaşık ölçü, mesaj, navy "Teklif Alın".
Keep SiteHeader + SiteFooter shell. İletişim nav item active.
