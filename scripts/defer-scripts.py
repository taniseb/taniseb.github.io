#!/usr/bin/env python3
"""Add defer to Quarto's render-blocking <script src> tags in <head>.

Quarto emits its bundled JS (nav, search, tippy, bootstrap, site.js) as
plain synchronous <script src> tags, which blocks HTML parsing. None of
them run before DOMContentLoaded in practice, so defer is safe and
preserves execution order. ES module scripts (type="module") are already
deferred by the browser and left untouched.
"""
import re
from pathlib import Path

DOCS_DIR = Path(__file__).resolve().parent.parent / "docs"

SCRIPT_SRC_NO_DEFER = re.compile(
    r'<script(?![^>]*\btype="module")(?![^>]*\bdefer\b)([^>]*\bsrc="[^"]+"[^>]*)>'
)


def add_defer(match: re.Match) -> str:
    attrs = match.group(1)
    return f"<script{attrs} defer>"


def main() -> None:
    for html_path in DOCS_DIR.rglob("*.html"):
        text = html_path.read_text(encoding="utf-8")
        head, sep, rest = text.partition("</head>")
        if not sep:
            continue
        new_head = SCRIPT_SRC_NO_DEFER.sub(add_defer, head)
        if new_head != head:
            html_path.write_text(new_head + sep + rest, encoding="utf-8")


if __name__ == "__main__":
    main()
