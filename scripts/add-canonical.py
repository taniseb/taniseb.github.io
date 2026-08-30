#!/usr/bin/env python3
"""Insert <link rel="canonical"> into every rendered HTML page.

Quarto's open-graph/twitter-card support doesn't emit a canonical tag on
its own, so this runs as a project post-render step to add one derived
from each file's path under docs/, matching site-url in _quarto.yml.
"""
import re
from pathlib import Path

SITE_URL = "https://taniseb.github.io"
DOCS_DIR = Path(__file__).resolve().parent.parent / "docs"


def canonical_url(html_path: Path) -> str:
    rel = html_path.relative_to(DOCS_DIR).as_posix()
    if rel == "index.html":
        return f"{SITE_URL}/"
    return f"{SITE_URL}/{rel}"


def main() -> None:
    for html_path in DOCS_DIR.rglob("*.html"):
        text = html_path.read_text(encoding="utf-8")
        if 'rel="canonical"' in text:
            continue
        url = canonical_url(html_path)
        tag = f'<link rel="canonical" href="{url}">\n'
        new_text, count = re.subn(r"(<head>)", r"\1\n" + tag, text, count=1)
        if count:
            html_path.write_text(new_text, encoding="utf-8")


if __name__ == "__main__":
    main()
