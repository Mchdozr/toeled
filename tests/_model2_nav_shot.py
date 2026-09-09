"""High-DPI screenshots of model2 nav buttons (default + hover)."""
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1440, "height": 1000}, device_scale_factor=6)
    pg.goto("http://localhost:8765/index.html", wait_until="networkidle")
    pg.evaluate("document.querySelector('.home-model2').scrollIntoView({block:'center'})")
    pg.wait_for_timeout(800)
    vis = pg.locator(".home-model2 .model2-bottom-item .mySwiper .page-box").first
    vis.screenshot(path="tests/_model2_nav_buttons.png")
    vis.locator(".swiper-button-next").hover(force=True)
    pg.wait_for_timeout(400)
    vis.screenshot(path="tests/_model2_nav_buttons_hover.png")
    b.close()
print("done")
