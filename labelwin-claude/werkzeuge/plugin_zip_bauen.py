"""Baut labelwin.plugin (zum Hochladen in Claude) und dieselbe Datei als labelwin-plugin.zip aus plugin/labelwin.

Wichtig: plugin.json muss im Archiv ganz oben unter .claude-plugin/ liegen. Ein per Rechtsklick
"Senden an > ZIP-komprimierter Ordner" gepackter Ordner liegt eine Ebene zu tief und wird abgelehnt.

Nach jeder Aenderung am Plugin ausfuehren:  python werkzeuge/plugin_zip_bauen.py
labelwin.env wird NIE mit eingepackt.
"""
import os
import zipfile
from pathlib import Path

repo = Path(__file__).resolve().parent.parent
quelle = repo / "plugin" / "labelwin"
ziel = repo / "labelwin-plugin.zip"
AUSLASSEN_ORDNER = {"__pycache__", ".git"}
AUSLASSEN_DATEIEN = {"labelwin.env", ".DS_Store", "Thumbs.db"}

with zipfile.ZipFile(ziel, "w", zipfile.ZIP_DEFLATED) as z:
    for ordner, unterordner, dateien in os.walk(quelle):
        unterordner[:] = sorted(d for d in unterordner if d not in AUSLASSEN_ORDNER)
        for name in sorted(dateien):
            if name in AUSLASSEN_DATEIEN or name.endswith(".env"):
                continue
            pfad = Path(ordner) / name
            z.write(pfad, pfad.relative_to(quelle).as_posix())

namen = zipfile.ZipFile(ziel).namelist()
assert ".claude-plugin/plugin.json" in namen, "plugin.json fehlt im Zip"
assert not any(n.endswith(".env") for n in namen), "env-Datei im Zip!"
(repo / "labelwin.plugin").write_bytes(ziel.read_bytes())
print(f"labelwin.plugin + {ziel.name}: {len(namen)} Dateien, {ziel.stat().st_size // 1024} KB")
