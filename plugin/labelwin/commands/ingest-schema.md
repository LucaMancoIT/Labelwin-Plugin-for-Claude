---
description: Liest die Labelwin-Datenbankstruktur aus und erzeugt die Schema-Dokumentation für den Skill labelwin-datenbank
---

1. Prüfe die Verbindung nur über das MCP-Tool `connection_info`. Öffne niemals `labelwin.env` oder `global.ini` und lies keine Umgebungsvariablen mit Zugangsdaten aus. Schlägt die Verbindung fehl: auf `einrichten.bat` im Repo verweisen.
2. Führe aus: `python ${CLAUDE_PLUGIN_ROOT}/scripts/introspect_schema.py`
3. Lies `skills/labelwin-datenbank/references/generated/schema-overview.md` und `relations.md`.
4. Gruppiere die Tabellen nach Fachbereich (Adressen, Artikel, Belege, Zeit, Projekte, Lager, Buchhaltung, System) und befülle die Tabelle in `references/schema-notes.md` als Entwurf. Kennzeichne Vermutungen ausdrücklich mit "(vermutet)".
5. Prüfe unklare Kerntabellen per `describe_table`/`sample_rows` (keine personenbezogenen Daten in die Notizen übernehmen).
6. Fasse zusammen: Anzahl Tabellen, erkannte Bereiche, offene Fragen an den Fachanwender.
