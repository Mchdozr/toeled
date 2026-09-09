"""Mobil (390px) model2-bottom gecis + yukseklik kararliligi kontrolu."""
from playwright.sync_api import sync_playwright

JS = """
() => {
  const items = [...document.querySelectorAll('.home-model2 .model2-bottom-item')];
  const cur = items.find(el => el.classList.contains('cur'));
  const left = cur.querySelector('.model2-left').getBoundingClientRect();
  const right = cur.querySelector('.model2-right').getBoundingClientRect();
  const cs = getComputedStyle(cur);
  const others = items.filter(el => el !== cur).map(el => getComputedStyle(el).opacity);
  return {
    curOpacity: cs.opacity,
    stacked: right.top >= left.bottom - 2,
    others,
    containerH: cur.parentElement.getBoundingClientRect().height,
  };
}
"""

with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 390, "height": 844})
    pg.goto("http://localhost:8765/index.html")
    pg.wait_for_timeout(1500)
    pg.evaluate("document.querySelector('#i2').scrollIntoView({block:'start'})")
    pg.wait_for_timeout(400)
    chips = pg.locator(".home-model2 .model2-top .tab-item")
    hs = []
    for i in range(chips.count()):
        chips.nth(i).click()
        pg.wait_for_timeout(200)
        mid = pg.evaluate(JS)
        pg.wait_for_timeout(500)
        after = pg.evaluate(JS)
        hs.append(round(after["containerH"], 1))
        print("tab", i, "mid:", mid)
        print("tab", i, "after:", after)
    print("container heights:", hs, "stable:", len(set(hs)) <= 2)
    pg.screenshot(path="tests/_model2_bottom_mobile.png")
    b.close()
