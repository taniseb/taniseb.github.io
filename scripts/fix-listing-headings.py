#!/usr/bin/env python3
"""Fix Quarto's grid-listing heading level skip (h1 -> h5).

Quarto's grid listing template renders each card title as <h5
class="... card-title listing-title">, regardless of the page's own
heading depth. On a page whose only other heading is the h1, that
skips levels 2-4 and breaks the document outline for screen readers.
Promote it to h2, the correct next level after the page's h1.
"""
import re
from pathlib import Path

DOCS_DIR = Path(__file__).resolve().parent.parent / "docs"

CARD_TITLE = re.compile(
    r'<h5(\s+class="[^"]*\bcard-title\b[^"]*")>(.*?)</h5>', re.S
)


def fix(text: str) -> str:
    return CARD_TITLE.sub(r"<h2\1>\2</h2>", text)


def main() -> None:
    for html_path in DOCS_DIR.rglob("*.html"):
        text = html_path.read_text(encoding="utf-8")
        if "card-title" not in text:
            continue
        new_text = fix(text)
        if new_text != text:
            html_path.write_text(new_text, encoding="utf-8")


if __name__ == "__main__":
    main()
