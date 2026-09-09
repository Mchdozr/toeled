import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

KF_PATTERN = re.compile(
    r'\s*<a href="javascript:;" class="fixed-b-i go-top">\s*\n\s*'
    r'<img src="/public/wwwroot/images/kf\.png" alt>\s*\n\s*</a>\s*\n',
    re.MULTILINE,
)
FOOTER_NUM_PATTERN = re.compile(
    r'\s*<div class="public-footer-num">\s*\n\s*<p>.*?</p>\s*</div>\s*\n',
    re.DOTALL,
)


def main() -> None:
    changed = 0
    for page in ROOT.rglob("index.html"):
        text = page.read_text(encoding="utf-8")
        updated = KF_PATTERN.sub("\n", text)
        updated = FOOTER_NUM_PATTERN.sub("\n", updated)
        if updated != text:
            page.write_text(updated, encoding="utf-8", newline="\n")
            changed += 1
    print(f"updated {changed} files")


if __name__ == "__main__":
    main()
