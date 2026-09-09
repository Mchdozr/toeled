## SiteHeader
- Source: `contact-us/index.html` (header block ~99–454)
- Category: layout
- Description: Fixed top nav with TOELED logo, mega menu (Ürünler/Referanslar/Destek/Haberler/Hakkımızda/İletişim), search, email, socials
- Extractable props: activeItem (string, default: "contact")
- Hardcoded: menu labels, logo imgs, mega-menu series links, email `info@ledajans.com`

## SiteFooter
- Source: `contact-us/index.html` (footer ~526–590)
- Category: layout
- Description: Logo, social, product/support/case/contact columns, contact card (email, phones, TR/DE/CY addresses), copyright TAHA LED · Toeled
- Extractable props: none required
- Hardcoded: all column links, contact copy, logo

## FloatInquiry
- Source: `contact-us/index.html` (`.fixed-b` ~591–635)
- Category: layout
- Description: Right-edge float: WhatsApp/top + overlay inquiry form (Ad Soyad, E-posta, Telefon, Mesaj, Gönder)
- Extractable props: none
- Hardcoded: form labels, navy CTA

## ContactInfoCards
- Source: `contact-us/index.html` (`.contact-info` ~483–484)
- Category: basic
- Description: Four icon rows: Telefon, Adres, E-posta, Whatsapp
- Extractable props: none
- Hardcoded: +90 212 220 40 04, Şişli/İstanbul, info@ledajans.com

## ContactForm
- Source: `contact-us/index.html` (`#inqForm` ~486–521)
- Category: basic
- Description: Two-column name/email, phone, message, pill navy Gönder
- Extractable props: none
- Hardcoded: Validform attributes, `.contact-btn` styles
