"""model2-bottom tab gecisi dogrulamasi: tum chip'lere tikla, overlap kontrolu yap."""
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
URL = "http://localhost:8765/index.html"
SHOT = ROOT / "tests" / "_model2_bottom_transition.png"

OVERLAP_JS = """
() => {
  const items = [...document.querySelectorAll('.home-model2 .model2-bottom-item')];
  const cur = items.find(el => el.classList.contains('cur'));
  if (!cur) return { error: 'cur panel yok' };
  const left = cur.querySelector('.model2-left').getBoundingClientRect();
  const img = cur.querySelector('.model2-right .swiper-slide-active img')
           || cur.querySelector('.model2-right img');
  const right = img.getBoundingClientRect();
  // diger paneller gorunur mu?
  const othersVisible = items.filter(el => el !== cur).map(el => {
    const cs = getComputedStyle(el);
    return { opacity: cs.opacity, visibility: cs.visibility };
  });
  return {
    overlap: right.left < left.right - 1,
    leftRight: left.right,
    imgLeft: right.left,
    curOpacity: getComputedStyle(cur).opacity,
    othersVisible,
  };
}
"""

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1440, "height": 900})
    page.goto(URL)
    page.wait_for_timeout(1500)

    chips = page.locator(".home-model2 .model2-top .tab-item")
    count = chips.count()
    results = []
    for i in range(count):
        chips.nth(i).click()
        page.wait_for_timeout(150)  # gecis ortasi
        mid = page.evaluate(OVERLAP_JS)
        page.wait_for_timeout(500)  # gecis sonrasi
        after = page.evaluate(OVERLAP_JS)
        results.append((i, mid, after))
        print(f"tab {i}: mid={mid}")
        print(f"tab {i}: after={after}")

    page.locator("#i2").scroll_into_view_if_needed()
    page.wait_for_timeout(400)
    page.screenshot(path=str(SHOT), full_page=False)
    browser.close()

bad = [r for r in results if r[1].get("overlap") or r[2].get("overlap")]
if bad:
    print("OVERLAP TESPIT:", bad)
    sys.exit(1)
print("OK: hicbir geciste metin/gorsel overlap yok ->", SHOT)
