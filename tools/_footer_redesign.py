import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

CONTACT_OLD = re.compile(
    r'<div class="contact-card">\s*'
    r'<div class="contact-item">\s*'
    r'<p class="contact-item-p1">E-posta:</p>\s*'
    r'<p class="contact-item-p2">info@ledajans\.com</p>\s*'
    r'</div>\s*'
    r'<div class="contact-item">\s*'
    r'<p class="contact-item-p1">Telefon:</p>\s*'
    r'<p class="contact-item-p2">\+90 212 220 40 04 · \+90 543 879 51 08 · \+90 530 405 67 68</p>\s*'
    r'</div>\s*'
    r'<div class="contact-item">\s*'
    r'<p class="contact-item-p1">Adres:</p>\s*'
    r'<p class="contact-item-p2">İstanbul: Gül 2 Sk\. No:10a, Şişli<br>Almanya: Heinrich-Hertz-Str\. 50, Erkrath<br>Kıbrıs: Karaoğlanoğlu Cad\., Girne</p>\s*'
    r'</div>\s*'
    r'</div>',
    re.DOTALL,
)

CONTACT_NEW = """<div class="contact-card">
          <div class="contact-item">
            <p class="contact-item-p1">E-posta:</p>
            <p class="contact-item-p2"><a href="mailto:info@ledajans.com">info@ledajans.com</a></p>
          </div>
          <div class="contact-item">
            <p class="contact-item-p1">Telefon:</p>
            <p class="contact-item-p2"><a href="tel:+902122204004">+90 212 220 40 04</a><span class="footer-phone-sep">·</span><a href="tel:+905438795108">+90 543 879 51 08</a><span class="footer-phone-sep">·</span><a href="tel:+905304056768">+90 530 405 67 68</a></p>
          </div>
          <div class="contact-item">
            <p class="contact-item-p1">Adres:</p>
            <p class="contact-item-p2"><a href="https://www.google.com/maps/search/?api=1&amp;query=Halide+Edip+Ad%C4%B1var+Mah.+G%C3%BCl+2+Sk.+No%3A10a%2C+34382+%C5%9Ei%C5%9Fli%2F%C4%B0stanbul" target="_blank" rel="noopener noreferrer">İstanbul: Gül 2 Sk. No:10a, Şişli</a><br><a href="https://www.google.com/maps/search/?api=1&amp;query=Heinrich-Hertz-Stra%C3%9Fe+50%2C+40699+Erkrath%2C+Germany" target="_blank" rel="noopener noreferrer">Almanya: Heinrich-Hertz-Str. 50, Erkrath</a><br><a href="https://www.google.com/maps/search/?api=1&amp;query=Karao%C4%9Flano%C4%9Flu+Cad.+Yayla+Akti%C4%9Fin+%C4%B0%C5%9F+Han%C4%B1+No%3A6%2C+Girne%2C+K%C4%B1br%C4%B1s" target="_blank" rel="noopener noreferrer">Kıbrıs: Karaoğlanoğlu Cad., Girne</a></p>
          </div>
        </div>"""

CONTACT_COLUMN = re.compile(
    r'<div class="list-i">\s*'
    r'<a class="title" href="/contact-us/">İletişim</a>\s*'
    r'<div class="public-footer-info">\s*'
    r'<a class="info" href="/contact-us/">İletişim</a>\s*'
    r'<a class="info" href="/contact-us/">Konum</a>\s*'
    r'(?:<a class="info" href="/about-us/">Hakkımızda</a>\s*'
    r'<a class="info" href="/news/">Haberler</a>\s*)?'
    r'</div>\s*'
    r'(?:<a class="title title2" href="/about-us/">Hakkımızda</a>\s*'
    r'<a class="title title2" href="/news/">Haberler</a>\s*)?'
    r'</div>',
    re.DOTALL,
)

CONTACT_COLUMN_NEW = """<div class="list-i">
            <a class="title" href="/contact-us/">İletişim</a>
            <div class="public-footer-info">
              <a class="info" href="/contact-us/">İletişim</a>
              <a class="info" href="/contact-us/">Konum</a>
              <a class="info" href="/about-us/">Hakkımızda</a>
              <a class="info" href="/news/">Haberler</a>
            </div>
          </div>"""


def main() -> None:
    changed = 0
    contact_hits = 0
    for page in ROOT.rglob("index.html"):
        text = page.read_text(encoding="utf-8")
        updated = text
        updated = updated.replace("motion.css?v=1.1.10", "motion.css?v=1.1.11")
        updated = updated.replace(
            '<p><img class="logo" src="/public/wwwroot/images/logo.svg" alt=""/>',
            '<p><img class="logo" src="/public/wwwroot/images/logo10.svg" alt="TOELED"/>',
        )
        if CONTACT_OLD.search(updated):
            updated = CONTACT_OLD.sub(CONTACT_NEW, updated, count=1)
            contact_hits += 1
        if CONTACT_COLUMN.search(updated):
            updated = CONTACT_COLUMN.sub(CONTACT_COLUMN_NEW, updated, count=1)
        if updated != text:
            page.write_text(updated, encoding="utf-8", newline="\n")
            changed += 1
    print(f"updated {changed} files, contact-card replaced in {contact_hits} files")


if __name__ == "__main__":
    main()
