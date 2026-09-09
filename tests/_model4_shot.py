"""Screenshot helper for model4 news section (before/after verification)."""
import sys
from playwright.sync_api import sync_playwright

OUT = sys.argv[1] if len(sys.argv) > 1 else "tests/_model4.png"
WIDTH = int(sys.argv[2]) if len(sys.argv) > 2 else 1440
TAB = sys.argv[3] if len(sys.argv) > 3 else "kurumsal"

with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": WIDTH, "height": 1000})
    pg.goto("http://localhost:8765/index.html", wait_until="networkidle")
    pg.evaluate("document.querySelector('#i4').scrollIntoView({block:'start'})")
    pg.wait_for_timeout(600)
    if TAB == "sektor":
        pg.click(".home-model4 .model4-btn-list .btn-item:nth-child(2)")
        pg.wait_for_timeout(500)
    el = pg.locator("#i4")
    el.screenshot(path=OUT)
    b.close()
print("saved", OUT)
