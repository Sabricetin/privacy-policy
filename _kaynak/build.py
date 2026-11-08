#!/usr/bin/env python3
"""DreamVision sitesini üretir: 4 sayfa × 2 dil (EN varsayılan, TR "-tr").

    python3 _kaynak/build.py

Ortak üst menü, dil anahtarı ve alt bilgi buradan gelir; metinler
_kaynak/content.py içinde. Çıktı HTML dosyaları sitenin köküne yazılır ve
commit'lenir (GitHub Pages doğrudan onları yayınlar). `_` ile başlayan bu
klasör Jekyll tarafından yayınlanmaz.

Adresler sabittir — Play Console ve uygulama bunlara bağlantı veriyor:
privacy-policy.html, terms-conditions.html, delete-account.html, index.html.
"""

import html
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from content import PAGES, UI  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = "https://sabricetin.github.io/privacy-policy/"
ORDER = ["support", "privacy", "terms", "delete"]
FILES = {
    "support": "index",
    "privacy": "privacy-policy",
    "terms": "terms-conditions",
    "delete": "delete-account",
}


def filename(page: str, lang: str) -> str:
    name = FILES[page]
    return f"{name}.html" if lang == "en" else f"{name}-tr.html"


def render(page: str, lang: str) -> str:
    p = PAGES[page][lang]
    ui = UI[lang]
    other = "tr" if lang == "en" else "en"
    nav = "\n".join(
        f'      <a href="{filename(k, lang)}"'
        + (' aria-current="page"' if k == page else "")
        + f">{ui['nav'][k]}</a>"
        for k in ORDER
    )
    foot = " ".join(f'<a href="{filename(k, lang)}">{ui["nav"][k]}</a>' for k in ORDER)
    lang_links = "".join(
        f'<a href="{filename(page, l)}" hreflang="{l}" lang="{l}" data-set-lang="{l}"'
        + (' aria-current="true"' if l == lang else "")
        + f">{l.upper()}</a>"
        for l in ("en", "tr")
    )
    updated = f'\n    <p class="updated">{p["updated"]}</p>' if p.get("updated") else ""
    title = html.escape(p["title"])
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title} — DreamVision</title>
  <meta name="description" content="{html.escape(p['description'])}">
  <meta name="theme-color" content="#1A1233">
  <link rel="canonical" href="{BASE}{filename(page, lang)}">
  <link rel="alternate" hreflang="en" href="{BASE}{filename(page, 'en')}">
  <link rel="alternate" hreflang="tr" href="{BASE}{filename(page, 'tr')}">
  <link rel="alternate" hreflang="x-default" href="{BASE}{filename(page, 'en')}">
  <link rel="icon" href="assets/icon.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="assets/site.css">
  <script src="assets/site.js" defer></script>
</head>
<body>
<a class="skip" href="#main">{ui['skip']}</a>
<header class="topbar">
  <div class="topbar-inner">
    <a class="brand" href="{filename('support', lang)}"><img src="assets/icon.png" alt="" width="34" height="34">DreamVision</a>
    <nav class="nav" aria-label="{ui['nav_label']}">
{nav}
    </nav>
    <div class="lang" role="group" aria-label="{ui['lang_label']}">{lang_links}</div>
  </div>
</header>
<main id="main">
  <div class="hero">
    <div class="mascot" aria-hidden="true"><img src="assets/moon.png" class="moon" alt=""><img src="assets/cloud.png" alt=""></div>
    <p class="eyebrow">{p['eyebrow']}</p>
    <h1>{p['h1']}</h1>
    <p class="lead">{p['lead']}</p>{updated}
  </div>
  <div class="content">
{p['body'].strip()}
  </div>
</main>
<footer>
  <nav aria-label="{ui['footer_label']}">{foot}</nav>
  <p>© 2026 DreamVision · Sabri ÇETİN · <a href="mailto:supportdreamvisionapp@gmail.com">supportdreamvisionapp@gmail.com</a></p>
</footer>
</body>
</html>
"""


def main() -> None:
    for page in ORDER:
        for lang in ("en", "tr"):
            out = os.path.join(ROOT, filename(page, lang))
            with open(out, "w", encoding="utf-8") as f:
                f.write(render(page, lang))
            print("yazıldı:", filename(page, lang))


if __name__ == "__main__":
    main()
