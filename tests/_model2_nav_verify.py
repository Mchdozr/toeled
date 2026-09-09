"""Verify model2 swiper nav buttons: no overlap + screenshot."""
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1440, "height": 1000})
    pg.goto("http://localhost:8765/index.html", wait_until="networkidle")
    pg.evaluate("document.querySelector('.home-model2').scrollIntoView({block:'center'})")
    pg.wait_for_timeout(800)

    panels = pg.locator(".home-model2 .model2-bottom-item .mySwiper .page-box")
    n = panels.count()
    print("page-box count:", n)
    ok = True
    for i in range(n):
        box = panels.nth(i)
        if not box.is_visible():
            continue
        prev = box.locator(".swiper-button-prev").bounding_box()
        nxt = box.locator(".swiper-button-next").bounding_box()
        gap = nxt["y"] - (prev["y"] + prev["height"])
        print(f"panel {i}: prev y={prev['y']:.0f} h={prev['height']:.0f} | next y={nxt['y']:.0f} h={nxt['height']:.0f} | gap={gap:.0f}px")
        if gap < 10:
            ok = False
            print(f"  OVERLAP/FAIL in panel {i}")

    # screenshot first visible panel's page-box region
    vis = panels.first
    vis.screenshot(path="tests/_model2_nav_buttons.png")

    # hover state shot (next btn is enabled; force to bypass interception)
    nxt_btn = vis.locator(".swiper-button-next")
    nxt_btn.hover(force=True)
    pg.wait_for_timeout(400)
    vis.screenshot(path="tests/_model2_nav_buttons_hover.png")

    b.close()
    print("RESULT:", "PASS" if ok else "FAIL")
