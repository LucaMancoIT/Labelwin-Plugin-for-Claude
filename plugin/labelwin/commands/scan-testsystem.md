---
description: Inventarisiert das Labelwin-Installationsverzeichnis (LW_HOME) und befüllt den Technik-Skill
argument-hint:
- Pfad
- optional – Standard LW_HOME
---

1. Führe aus: `python ${CLAUDE_PLUGIN_ROOT}/scripts/scan_testsystem.py $ARGUMENTS`
2. Lies `skills/labelwin-technik/references/generated/testsystem-inventory.md`.
3. Sichte Konfigurationsdateien (ini/xml/config) lesend; **Passwörter und Verbindungsstrings nicht in Notizen kopieren**.
4. Befülle `references/architektur.md` (Installationspfade, DB-Verbindung, Vorlagen/Reports, Schnittstellen, Logs) mit Quellenangabe je Zeile; Unbelegtes bleibt TODO.
5. Liste offene Fragen auf.
