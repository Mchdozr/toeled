"""Regression teshisi: sayfa yuklenir yuklenmez (scroll YOK) model2-bottom durumu."""
from playwright.sync_api import sync_playwright

DIAG_JS = """
() => {
  const container = document.querySelector('.home-model2 .model2-bottom:not(.model2-bottom-item)');
  const items = [...document.querySelectorAll('.home-model2 .model2-bottom-item')];
  const out = { containerExists: !!container, itemCount: items.length, items: [] };
  if (container) {
    const cs = getComputedStyle(container);
    const r = container.getBoundingClientRect();
    out.container = { display: cs.display, w: r.width, h: r.height };
  }
  for (const el of items) {
    const cs = getComputedStyle(el);
    const r = el.getBoundingClientRect();
    const left = el.querySelector('.model2-left');
    const leftCs = left ? getComputedStyle(left) : null;
    const hsm = el.querySelector('[hsm]');
    const hsmCs = hsm ? getComputedStyle(hsm) : null;
    out.items.push({
      cls: el.className,
      display: cs.display, opacity: cs.opacity, visibility: cs.visibility,
      zIndex: cs.zIndex, transform: cs.transform, position: cs.position,
      w: Math.round(r.width), h: Math.round(r.height),
      leftOpacity: leftCs ? leftCs.opacity : null,
      hsmOpacity: hsmCs ? hsmCs.opacity : null,
      hsmTransform: hsmCs ? hsmCs.transform : null,
      parentIsContainer: el.parentElement === container,
    });
  }
  return out;
}
"""

with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1440, "height": 900})
    pg.goto("http://localhost:8765/index.html")
    pg.wait_for_timeout(2500)
    print("=== LOAD (no scroll) ===")
    import json
    print(json.dumps(pg.evaluate(DIAG_JS), indent=1, ensure_ascii=False))
    pg.evaluate("document.querySelector('#i2').scrollIntoView({block:'start'})")
    pg.wait_for_timeout(1200)
    print("=== AFTER SCROLL TO #i2 ===")
    print(json.dumps(pg.evaluate(DIAG_JS), indent=1, ensure_ascii=False))
    b.close()
