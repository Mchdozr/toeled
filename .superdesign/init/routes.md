# Toeled Routes

Static folder-per-page HTML (Plesk `/httpdocs`). No SPA router. Each route is `<folder>/index.html`. Shared header + footer duplicated in every file.

| URL | File | Summary |
|---|---|---|
| `/` | `index.html` | Home: full-bleed Swiper hero, company intro, product grids, cases, news |
| `/products/` | `products/index.html` | Product hub |
| `/commercial-display/` | `commercial-display/index.html` | Indoor LED category |
| `/rental-staging/` | `rental-staging/index.html` | Rental & staging |
| `/dooh/` | `dooh/index.html` | Outdoor / DOOH |
| `/accessories/` | `accessories/index.html` | Accessories |
| `/cases/` | `cases/index.html` | Case studies hub |
| `/contact-us/` | `contact-us/index.html` | Contact: PHP error dump + China map + generic form |
| `/about-us/` | `about-us/index.html` | About |
| `/news/` | `news/index.html` | News list |
| `/debugger/` `/one-click-debug/` `/service/` `/knowledge/` `/qce-cert-lookup/` `/sales-outlets/` | support pages | Support cluster |

Product series (indoor/outdoor/rental): `cms-series-crystal-film-display`, `hs-series-holographic-display`, `q-mini-series`, `nc-series`, `indoor-q-series`, `pdc-series`, `mk-series`, `indoor-r-series`, `cs-series`, `n-series`, `rw-series`, `cg-series`, `ln-series`, `dm-series`, `pm-series`, `outdoor-q-series`, `outdoor-s-series`, `qm-series`, `mg-series`, `p-series`, `v-series-`.

**Missing (business gap):** dedicated `/teklif/` LED quote landing with project-spec fields. Current `/contact-us/` is a cloned manufacturer contact page (Xiamen map, "Online Message", no indoor/outdoor/size fields).
