"""Inventarisiert das Labelwin-Testsystem-Verzeichnis -> skills/labelwin-technik/references/generated/testsystem-inventory.md
Aufruf: python scripts/scan_testsystem.py "<Pfad zum Testsystem>"
Erfasst: Verzeichnisbaum (Tiefe 3), Dateitypen-Statistik, Konfigurationsdateien (ini/config/xml/json), Reports/Vorlagen, Skripte, Executables.
"""
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "server"))
import lwconfig  # noqa: E402

root = Path(sys.argv[1]) if len(sys.argv) > 1 else lwconfig.home()
out = Path(__file__).parent.parent / "skills/labelwin-technik/references/generated"
out.mkdir(parents=True, exist_ok=True)
CONFIG = {".ini", ".cfg", ".config", ".xml", ".json", ".conf", ".udl", ".reg"}
files = [p for p in root.rglob("*") if p.is_file()]
ext = Counter(p.suffix.lower() or "(ohne)" for p in files)

with open(out / "testsystem-inventory.md", "w", encoding="utf-8") as f:
    f.write(f"# Testsystem-Inventar (generiert)\n\nWurzel: `{root}`\nDateien: {len(files)}\n\n## Dateitypen\n")
    f.write("".join(f"- {e}: {n}\n" for e, n in ext.most_common(40)))
    f.write("\n## Verzeichnisse (Tiefe ≤ 3)\n")
    for d in sorted(p for p in root.rglob("*") if p.is_dir() and len(p.relative_to(root).parts) <= 3):
        f.write(f"- {d.relative_to(root)}/ ({sum(1 for x in d.iterdir() if x.is_file())} Dateien)\n")
    f.write("\n## Konfigurationsdateien\n")
    f.write("".join(f"- {p.relative_to(root)}\n" for p in files if p.suffix.lower() in CONFIG)[:20000])
    f.write("\n## Ausführbare Dateien / Bibliotheken\n")
    f.write("".join(f"- {p.relative_to(root)}\n" for p in files if p.suffix.lower() in {'.exe', '.dll', '.bat', '.cmd', '.ps1'})[:20000])
print("Inventar geschrieben:", out / "testsystem-inventory.md")
