# Key page dependency trees

Static HTML: no JS imports. Each page inlines the same header/footer/float form and links shared CSS/JS.

## / (Home)
Entry: `index.html`
Dependencies:
- `public/wwwroot/css/layout.css`
- `public/wwwroot/css/style.css`
- `public/wwwroot/css/plugin.css`
- `public/wwwroot/plugin/layui/layui.css`
- `public/wwwroot/plugin/uikit/uikit.min.css`
- `public/wwwroot/images/logo.svg`
- `public/wwwroot/images/logo10.svg`
- Shared header (lines ~56–410)
- Hero Swiper (lines ~417–546)
- Company intro `.home-model1` (from ~547)
- Shared footer + `.fixed-b` inquiry widget (from ~2444)

## /contact-us/ (Contact — conversion bottleneck)
Entry: `contact-us/index.html`
Dependencies:
- Same CSS/JS as home
- Header (lines 99–454)
- Banner `.public-banner` + breadcrumb `.public-nav` (456–472)
- Map iframe (Xiamen Qiangli — leftover clone) (474–482)
- Contact info cards: phone, Istanbul address, email, WhatsApp (483–484)
- `#inqForm` name/email/phone/message + `.contact-btn` Gönder (486–521)
- Footer + float form (526–635)
- **Defects in source:** PHP session_start notice dumped above `<!DOCTYPE>`; mixed EN/TR ("Contact", "Online Message"); China map vs Istanbul office.

## /products/ (Product hub)
Entry: `products/index.html`
Dependencies: shared header/footer + product category cards linking to indoor / rental / outdoor / accessories.

## /commercial-display/ (Indoor category)
Entry: `commercial-display/index.html`
Dependencies: shared shell + series cards (CMS, HS, Q Mini, NC, Indoor Q, PDC, MK, Indoor R, CS, N).

Representative sibling for a new quote page: `/contact-us/` (form + contact cards) plus home navy CTA language.
