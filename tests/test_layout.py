import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CSS = (ROOT / "public/wwwroot/css/motion.css").read_text(encoding="utf-8")
HOME = (ROOT / "index.html").read_text(encoding="utf-8")
PAGES = tuple(ROOT.rglob("index.html"))


class LayoutContractTests(unittest.TestCase):
    def test_product_media_is_capped(self):
        self.assertIn(".product-swiper-i > img", CSS)
        self.assertIn(".product-model1-right img", CSS)
        self.assertIn(".product-model6 .row-i img", CSS)
        self.assertIn("max-height: 420px", CSS)
        self.assertIn(".product-model1 .row-i", CSS)

    def test_home_model2_closes_the_text_image_gap(self):
        self.assertIn(".home-model2 .model2-bottom.cur", CSS)
        self.assertIn("gap: 32px", CSS)
        self.assertNotIn("max-width: 420px;\n  margin-left: auto;", CSS)
        self.assertIn(".home-model2 .model2-left .t1", CSS)
        self.assertIn(".home-model2 .model2-top .tab-item-btn", CSS)
        self.assertIn("min-height: 44px", CSS)

    def test_home_model2_top_uses_icon_chips(self):
        self.assertIn(".home-model2 .model2-top .tab-item a.tab-chip", CSS)
        self.assertIn(".home-model2 .model2-top .tab-icon", CSS)
        self.assertIn("display: inline-flex", CSS)
        self.assertIn("padding: 10px 18px", CSS)
        self.assertIn("min-height: 48px", CSS)
        self.assertRegex(
            CSS,
            r"\.home-model2 \.model2-top \.tab-item a\.tab-chip[^{]*\{[^}]*width:\s*auto",
        )
        self.assertIn("width: 44px", CSS)
        self.assertIn("height: 44px", CSS)
        self.assertIn("#112698", CSS)
        self.assertRegex(
            CSS,
            r"\.home-model2 \.model2-top \.tab-item::after\s*\{[^}]*display:\s*none",
        )
        match = re.search(
            r'<div class="model2-top">(.*?)</div>\s*<div class="model2-bottom">',
            HOME,
            re.DOTALL,
        )
        self.assertIsNotNone(match, "model2-top bloğu bulunamadı")
        model2_top = match.group(1)
        self.assertIn('class="tab-chip"', model2_top)
        self.assertIn('href="/commercial-display/"', model2_top)
        self.assertIn('href="/rental-staging/"', model2_top)
        self.assertIn('href="/dooh/"', model2_top)
        self.assertIn('href="/accessories/"', model2_top)
        self.assertNotIn('class="img1"', model2_top)
        self.assertNotIn("/public/wwwroot/media/", model2_top)
        self.assertEqual(model2_top.count("<svg"), 4)

    def test_home_model2_bottom_uses_card_deck_swap(self):
        self.assertRegex(
            CSS,
            r"\.home-model2 \.model2-bottom:not\(\.model2-bottom-item\)\s*\{[^}]*display:\s*grid",
        )
        self.assertRegex(
            CSS,
            r"\.model2-bottom-item\s*\{[^}]*grid-area:\s*1\s*/\s*1",
        )
        self.assertRegex(
            CSS,
            r"\.model2-bottom-item\s*\{[^}]*opacity:\s*0[^}]*pointer-events:\s*none",
        )
        self.assertRegex(
            CSS,
            r"\.model2-bottom-item\.cur\s*\{[^}]*opacity:\s*1[^}]*z-index:\s*2",
        )
        self.assertRegex(
            CSS,
            r"\.model2-bottom-item \.model2-right \.mySwiper\s*\{[^}]*overflow:\s*hidden",
        )
        self.assertRegex(
            CSS,
            r"prefers-reduced-motion:\s*reduce\)\s*\{[^}]*model2-bottom-item",
        )

    def test_shared_page_media_and_buttons_are_normalized(self):
        for selector in (
            ".news-b-con img",
            ".product-list-b-img",
            ".home-model1 .row1 .left > p > .h-more",
            ".home-model3 .caseSwiper .swiper-slide img",
            ".culture-b-list-i .row .row-a .row-a-img",
            ".public-banner",
        ):
            self.assertIn(selector, CSS)

    def test_contact_info_icon_rotates_in_place(self):
        self.assertRegex(
            CSS,
            r"\.contact-info-img\s*\{[^}]*overflow:\s*hidden",
        )
        self.assertRegex(
            CSS,
            r"\.contact-info-i:hover \.contact-info-img\s*\{[^}]*display:\s*flex",
        )
        self.assertRegex(
            CSS,
            r"\.contact-info-i:hover \.contact-info-img\s*\{[^}]*transform:\s*none",
        )
        self.assertRegex(
            CSS,
            r"\.contact-info-img\s*>\s*img\s*\{[^}]*transform-origin:\s*center",
        )
        self.assertRegex(
            CSS,
            r"\.contact-info-i:hover \.contact-info-img\s*>\s*img\s*\{[^}]*transform:\s*rotate\(",
        )

    def test_home_model4_cards_have_equal_layout(self):
        self.assertIn("#i4 .model4-content.cur", CSS)
        self.assertRegex(
            CSS,
            r"#i4 \.model4-content\.cur[^{]*\{[^}]*display:\s*grid",
        )
        self.assertRegex(
            CSS,
            r"#i4 \.model4-content\.cur[^{]*\{[^}]*align-items:\s*stretch",
        )
        self.assertRegex(
            CSS,
            r"#i4 \.model4-content \.card-item-img[^{]*\{[^}]*aspect-ratio:\s*16\s*/\s*10",
        )
        self.assertIn('class="model4-content-l model4-content-l--stack"', HOME)
        self.assertRegex(
            HOME,
            r'<div class="model4-content-l model4-content-l--stack">\s*<a[^>]+class="card-item"[^>]*>\s*<div class="card-item-img img-scale">',
        )
        self.assertRegex(
            HOME,
            r'<div class="card-item-date">7 Şubat 2026</div>\s*<div class="card-item-title">Toeled ISE 2026',
        )
        self.assertRegex(
            HOME,
            r'<div class="card-item-date">28 Kasım 2025</div>\s*<div class="card-item-title">ISE 2026',
        )

    def test_home_model4_card_link_is_compact_cta(self):
        self.assertIn(
            "#i4 .model4-content .card-item-img img",
            CSS,
        )
        self.assertNotIn(
            ".home-model4 .model4-content .model4-content-l img {",
            CSS,
        )
        self.assertRegex(
            CSS,
            r"\.home-model4 \.model4-content \.model4-content-l \.card-link[^{]*\{[^}]*display:\s*inline-flex",
        )
        self.assertRegex(
            CSS,
            r"\.home-model4 \.model4-content \.model4-content-l \.card-link[^{]*\{[^}]*min-height:\s*44px",
        )
        self.assertRegex(
            CSS,
            r"\.home-model4 \.model4-content \.model4-content-l \.card-link[^{]*\{[^}]*white-space:\s*nowrap",
        )
        self.assertRegex(
            CSS,
            r"\.home-model4 \.model4-content \.model4-content-l \.card-link img[^{]*\{[^}]*width:\s*18px",
        )
        self.assertRegex(
            CSS,
            r"\.home-model4 \.model4-content \.model4-content-l \.card-link span[^{]*\{[^}]*margin-left:\s*0",
        )

    def test_home_model4_cards_use_modern_card_style(self):
        self.assertRegex(
            CSS,
            r"#i4\.home-model4\s*\{[^}]*min-height:\s*0\s*!important",
        )
        self.assertRegex(
            CSS,
            r"#i4 \.model4-content \.card-item\s*\{[^}]*border-radius:\s*16px",
        )
        self.assertRegex(
            CSS,
            r"#i4 \.model4-content \.card-item\s*\{[^}]*background:\s*#fff",
        )
        self.assertRegex(
            CSS,
            r"#i4 \.model4-content \.card-item-date\s*\{[^}]*border-radius:\s*999px",
        )
        self.assertRegex(
            CSS,
            r"#i4 \.model4-content \.card-item-title\s*\{[^}]*font-size:\s*20px\s*!important",
        )
        self.assertRegex(
            CSS,
            r"#i4 \.model4-content \.card-item-btn\s*\{[^}]*border-radius:\s*50%",
        )
        self.assertRegex(
            CSS,
            r"#i4 \.model4-content \.model4-content-l:hover \.card-item-btn[^{]*\{[^}]*background:\s*#112698",
        )
        self.assertRegex(
            CSS,
            r"\.home-model4 \.model4-content \.model4-content-l \.card-link[^{]*\{[^}]*background:\s*#112698",
        )
        self.assertNotIn("background-color: red", CSS)
        self.assertNotIn("model4-content-l--stack)::after", CSS)

    def test_layout_css_is_versioned(self):
        for page in PAGES:
            html = page.read_text(encoding="utf-8")
            with self.subTest(page=page.relative_to(ROOT)):
                self.assertIn("motion.css?v=1.1.13", html)

    def test_breadcrumb_home_icon_uses_svg(self):
        icon_svg = ROOT / "public/wwwroot/images/icon-home.svg"
        self.assertTrue(icon_svg.is_file())
        self.assertIn("<svg", icon_svg.read_text(encoding="utf-8"))
        self.assertIn('.public-nav .left > img[src*="icon-home"]', CSS)
        nav_pages = [
            page for page in PAGES
            if "public-nav" in page.read_text(encoding="utf-8")
        ]
        self.assertTrue(nav_pages, "breadcrumb içeren sayfa bulunamadı")
        for page in nav_pages:
            html = page.read_text(encoding="utf-8")
            with self.subTest(page=page.relative_to(ROOT)):
                self.assertNotIn("icon-home.png", html)
                self.assertIn('icon-home.svg" alt="Anasayfa"', html)

    def test_public_nav_scrolls_with_page(self):
        blocks = re.findall(r"\.public-nav\s*\{([^}]+)\}", CSS)
        self.assertTrue(blocks, "motion.css .public-nav kuralı yok")
        joined = "\n".join(blocks)
        self.assertIn("position: static !important", joined)
        self.assertIn("top: auto !important", joined)
        self.assertNotIn("position: sticky", joined)
        self.assertNotIn("position: fixed", joined)

    def test_home_model5_dealer_cards_link_to_maps(self):
        self.assertIn('id="i5"', HOME)
        self.assertIn('class="la-dealer-cards"', HOME)
        self.assertIn(
            'src="/public/wwwroot/images/world-service-map.svg"',
            HOME,
        )
        self.assertTrue(
            (ROOT / "public/wwwroot/images/world-service-map.svg").is_file()
        )
        cards = re.findall(
            r'<a\s+class="la-dealer-card"[^>]*href="([^"]+)"',
            HOME,
        )
        self.assertEqual(len(cards), 3)
        for href in cards:
            self.assertIn("google.com/maps/search/", href)
            self.assertIn("api=1", href)
        self.assertIn("syncDealerHighlight", HOME)
        self.assertIn("#i5.home-model5::after", CSS)
        self.assertIn("#i5 .he_f1p1.la-dealers::before", CSS)
        self.assertRegex(
            CSS,
            r"#i5 \.la-dealer-card\s*\{[^}]*background(?:-color)?:\s*#fff",
        )
        self.assertRegex(
            CSS,
            r"#i5 \.la-dealer-card\s*\{[^}]*opacity:\s*1\s*!important",
        )
        self.assertRegex(
            CSS,
            r"#i5 \.la-dealer-card\s*\{[^}]*filter:\s*none\s*!important",
        )
        self.assertRegex(
            CSS,
            r"#i5 \.la-dealer-card h3\s*\{[^}]*color:\s*#172033[^}]*font-size:\s*(?:16|17|18)px[^}]*font-weight:\s*700",
        )
        self.assertRegex(
            CSS,
            r"#i5 \.la-dealer-card p\s*\{[^}]*color:\s*#172033[^}]*font-size:\s*14px[^}]*opacity:\s*1\s*!important",
        )
        self.assertRegex(
            CSS,
            r"#i5 \.la-dealer-cards\s*\{[^}]*z-index:\s*[3-9]\d",
        )
        self.assertIn("#i5 .la-dealer-card:focus", CSS)

    def test_footer_uses_navy_brand_and_clickable_contact(self):
        self.assertRegex(
            CSS,
            r"\.public-footer-b\s*\{[^}]*background-color:\s*#f5f6f8",
        )
        title_blocks = re.findall(
            r"\.public-footer-b \.public-footer > \.top \.list \.list-i \.title[^{]*\{([^}]+)\}",
            CSS,
        )
        self.assertTrue(title_blocks, "footer column title kuralı yok")
        joined = "\n".join(title_blocks)
        self.assertIn("color: #112698", joined)
        self.assertNotIn("#d96515", joined)
        self.assertRegex(
            CSS,
            r"\.public-footer-b \.contact-card \.contact-item \.contact-item-p1[^{]*\{[^}]*color:\s*#112698",
        )
        self.assertIn('src="/public/wwwroot/images/logo10.svg" alt="TOELED"', HOME)
        self.assertIn('href="mailto:info@ledajans.com"', HOME)
        self.assertIn('href="tel:+902122204004"', HOME)
        self.assertIn('href="tel:+905438795108"', HOME)
        self.assertIn('href="tel:+905304056768"', HOME)
        footer_match = re.search(
            r'<div class="contact-card">(.*?)</div>\s*</div>\s*</div>\s*</div>\s*</footer>',
            HOME,
            re.DOTALL,
        )
        self.assertIsNotNone(footer_match, "contact-card bloğu bulunamadı")
        contact_card = footer_match.group(1)
        map_links = re.findall(r'href="(https://www\.google\.com/maps/search/\?api=1[^"]+)"', contact_card)
        self.assertEqual(len(map_links), 3)
        for href in map_links:
            self.assertIn("api=1", href)
        iletisim_match = re.search(
            r'<a class="title" href="/contact-us/">İletişim</a>\s*'
            r'<div class="public-footer-info">(.*?)</div>',
            HOME,
            re.DOTALL,
        )
        self.assertIsNotNone(iletisim_match, "İletişim sütunu bulunamadı")
        iletisim_links = iletisim_match.group(1)
        self.assertIn('href="/about-us/"', iletisim_links)
        self.assertIn('href="/news/"', iletisim_links)
        self.assertNotIn("title title2", HOME)
        for page in PAGES:
            html = page.read_text(encoding="utf-8")
            with self.subTest(page=page.relative_to(ROOT)):
                self.assertIn('href="mailto:info@ledajans.com"', html)
                self.assertIn("logo10.svg", html)
                self.assertNotIn("title title2", html)


if __name__ == "__main__":
    unittest.main()
