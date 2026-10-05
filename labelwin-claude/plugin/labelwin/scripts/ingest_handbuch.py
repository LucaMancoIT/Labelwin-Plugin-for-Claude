"""Konvertiert das lokale Labelwin-Handbuch (<LW_HOME>/handbuch, DrExplain-HTML) in Markdown.

Aufruf:  python scripts/ingest_handbuch.py [handbuch-ordner] [zielordner]
Standard: <LW_HOME>/handbuch  ->  skills/labelwin-anwendung/references/handbuch/
Ergebnis: eine .md je Kapitel (Titel, Brotkrumen-Pfad, Text) + INDEX.md (Hierarchie) + _text_only_ Hinweis zu Bildern.
Nur Standardbibliothek. Der Inhalt steckt in den *_print.htm-Dateien, die Hierarchie in den Brotkrumen der normalen .htm-Dateien.
"""
import html
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "server"))
import lwconfig  # noqa: E402

src = Path(sys.argv[1]) if len(sys.argv) > 1 else lwconfig.home() / "handbuch"
dst = Path(sys.argv[2]) if len(sys.argv) > 2 else Path(__file__).parent.parent / "skills/labelwin-anwendung/references/handbuch"
dst.mkdir(parents=True, exist_ok=True)

BLOCK = {"p", "div", "br", "tr", "li", "h1", "h2", "h3", "h4", "table"}


class Text(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out, self.skip, self.in_body = [], 0, False

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style"):
            self.skip += 1
        if tag == "body":
            self.in_body = True
        if tag == "li":
            self.out.append("\n- ")
        elif tag in ("td", "th"):
            self.out.append(" | ")
        elif tag in BLOCK:
            self.out.append("\n")
        if tag == "img":
            alt = dict(attrs).get("alt") or ""
            self.out.append(f" [Bild{': ' + alt if alt else ''}] ")

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self.skip -= 1
        elif tag in BLOCK:
            self.out.append("\n")

    def handle_data(self, data):
        if self.in_body and not self.skip:
            self.out.append(data)


def read(p: Path) -> str:
    b = p.read_bytes()
    try:
        return b.decode("utf-8")
    except UnicodeDecodeError:
        return b.decode("cp1252", errors="replace")


def to_md(raw: str) -> str:
    t = Text()
    t.feed(raw)
    s = "".join(t.out).replace("\xa0", " ")
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r" ?\n ?", "\n", s)
    return re.sub(r"\n{3,}", "\n\n", s).strip()


def title_of(raw: str) -> str:
    m = re.search(r"<title>(.*?)</title>", raw, re.S | re.I)
    return re.sub(r"^Labelwin\s*-\s*", "", html.unescape(m.group(1)).strip()) if m else ""


def crumbs(raw: str) -> list:
    m = re.search(r'class="b-breadCrumbs__items">(.*?)</ul>', raw, re.S)
    if not m:
        return []
    return [html.unescape(re.sub(r"<[^>]+>", "", x)).strip() for x in re.findall(r"<li[^>]*>(.*?)</li>", m.group(1), re.S)]


entries, skipped = [], 0
for p in sorted(src.glob("*.htm")):
    if p.name.endswith("_print.htm"):
        continue
    pr = src / (p.stem + "_print.htm")
    if not pr.exists():
        skipped += 1
        continue
    raw_print = read(pr)
    body = to_md(raw_print)
    path = crumbs(read(p))
    title = title_of(raw_print) or p.stem
    (dst / f"{p.stem}.md").write_text(
        f"# {title}\n\nPfad: {' > '.join(path) or title}\nQuelle: handbuch/{p.name}\n\n{body}\n", encoding="utf-8"
    )
    entries.append((path, title, p.stem, len(body)))

entries.sort(key=lambda e: [x.lower() for x in e[0]] or [e[1].lower()])
with open(dst / "INDEX.md", "w", encoding="utf-8") as f:
    f.write(f"# Handbuch-Index (generiert, {len(entries)} Kapitel)\n\nFormat: `Pfad` → Datei (Zeichen)\n\n")
    for path, title, stem, n in entries:
        f.write(f"{'  ' * max(len(path) - 1, 0)}- {title} → `{stem}.md` ({n})\n")
print(f"{len(entries)} Kapitel geschrieben nach {dst} ({skipped} ohne Print-Version übersprungen)")
