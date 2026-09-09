import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CSS = (ROOT / "public/wwwroot/css/motion.css").read_text(encoding="utf-8")
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

    def test_layout_css_is_versioned(self):
        for page in PAGES:
            html = page.read_text(encoding="utf-8")
            with self.subTest(page=page.relative_to(ROOT)):
                self.assertIn("motion.css?v=1.1.6", html)

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


if __name__ == "__main__":
    unittest.main()
