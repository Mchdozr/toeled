import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PAGES = tuple(ROOT.rglob("index.html"))


class NavigationContractTests(unittest.TestCase):
    def test_every_page_uses_the_new_navigation(self):
        for page in PAGES:
            html = page.read_text(encoding="utf-8")
            with self.subTest(page=page.relative_to(ROOT)):
                self.assertEqual(html.count('class="tl-site-header"'), 1)
                self.assertIn('class="tl-desktop-nav"', html)
                self.assertIn('class="tl-mega tl-mega-panel tl-mega-products"', html)
                self.assertIn('class="tl-mega tl-mega-panel tl-mega-cases"', html)
                self.assertIn('class="tl-mega tl-mega-panel tl-mega-support"', html)
                self.assertIn('class="tl-mega tl-mega-panel tl-mega-news"', html)
                self.assertIn('class="tl-nav-link" href="/">Anasayfa</a>', html)
                self.assertIn('class="tl-mobile-nav"', html)
                self.assertNotIn('class="header md-dn', html)

    def test_navigation_assets_are_versioned(self):
        for page in PAGES:
            html = page.read_text(encoding="utf-8")
            with self.subTest(page=page.relative_to(ROOT)):
                self.assertIn("motion.css?v=1.1.6", html)
                self.assertIn("my-js.js?v=1.1.0", html)

    def test_navigation_has_accessible_controls(self):
        html = (ROOT / "index.html").read_text(encoding="utf-8")
        self.assertIn('aria-controls="tl-products-menu"', html)
        self.assertIn('aria-expanded="false"', html)
        self.assertIn('aria-label="Menüyü aç"', html)

    def test_navigation_styles_and_behavior_exist(self):
        css = (ROOT / "public/wwwroot/css/motion.css").read_text(encoding="utf-8")
        js = (ROOT / "public/wwwroot/js/my-js.js").read_text(encoding="utf-8")
        self.assertIn(".tl-site-header", css)
        self.assertIn(".tl-mega-panel", css)
        self.assertIn(".tl-mega-products", css)
        self.assertIn("grid-template-columns: 1fr auto 1fr", css)
        self.assertIn(".tl-mobile-nav", css)
        self.assertIn("initToeledNavigation", js)
        self.assertIn("Escape", js)


if __name__ == "__main__":
    unittest.main()
