# Shared UI primitives (static HTML, not React)

Toeled has no component library. Repeated patterns live as copy-pasted HTML + `layout.css`.

## ContactBtn (CTA)
Path: CSS `.contact-btn` in `public/wwwroot/css/layout.css`
Navy pill submit used on `/contact-us/` and the float form.

```html
<button type="submit" class="contact-btn trans-up">Gönder</button>
```

```css
.contact-btn {
    max-width: 180px; width: 100%; height: 45px;
    background: #112698; border-radius: 23px;
    display: flex; align-items: center; justify-content: center;
    font-size: 16px; color: #FFFFFF; margin: auto; margin-top: 20px;
}
```

## PublicTitle
```html
<h1 class="public-title">Bize ulaşın</h1>
```
```css
.public-title { font-weight: bold; font-size: 42px; color: #112698; text-align: center; }
```

## ContactInfoCard
```html
<div class="contact-info-i items-center">
  <div class="contact-info-img"><img src="/public/wwwroot/images/icon-lx1.png" alt=""/></div>
  <div class="contact-info-msg">
    <p class="t1">Telefon</p>
    <p class="t2">+90 212 220 40 04</p>
  </div>
</div>
```

## InquiryForm fields
Labels: Ad Soyad *, E-posta *, Telefon / WhatsApp, Mesaj *.
Inputs: `.inputs` text / `.inputs.textarea`. Validform `datatype` / `nullmsg` on each field.

## Header logo
```html
<a href="/" class="logo">
  <img class="i1" src="/public/wwwroot/images/logo.svg" alt="Logo">
  <img class="i2" src="/public/wwwroot/images/logo10.svg" alt="Logo">
</a>
```
`.i1` white wordmark on dark/transparent hero; `.i2` black wordmark on scrolled white header.

## Home CTA
```html
<a href="/about-us/" class="h-more">DEVAMINI OKU &gt;</a>
<a href="..." class="btn1">Daha fazla +</a>
```
Hero `.btn1` sits on full-bleed product photography.
