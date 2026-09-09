from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OLD = '/public/wwwroot/images/icon-home.png" alt=""'
NEW = '/public/wwwroot/images/icon-home.svg" alt="Anasayfa"'

count = 0
for page in ROOT.rglob("index.html"):
    text = page.read_text(encoding="utf-8")
    if OLD not in text:
        continue
    page.write_text(text.replace(OLD, NEW), encoding="utf-8", newline="\n")
    count += 1

print(f"icon replaced in {count} files")
