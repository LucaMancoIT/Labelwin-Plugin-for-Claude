---
description: Konvertiert das lokale Labelwin-Handbuch (<LW_HOME>/handbuch) in durchsuchbare Markdown-Kapitel für den Skill labelwin-anwendung
argument-hint:
- Handbuch-Ordner
- optional – Standard <LW_HOME>/handbuch
---

1. Führe aus: `python ${CLAUDE_PLUGIN_ROOT}/scripts/ingest_handbuch.py $ARGUMENTS` (LW_HOME kommt aus der Plugin-Konfiguration).
2. Lies `skills/labelwin-anwendung/references/handbuch/INDEX.md`.
3. Ergänze `handbuch/PROZESSE.md`: Kernprozesse (Adresse anlegen, Angebot → Auftrag → Lieferschein → Rechnung, Zeiterfassung, Bestellwesen, Mahnwesen, …) aus den Kapiteln abgeleitet – jeweils Auslöser → Schritte → Ergebnis, mit Kapitelverweis. Handbuchtext nicht verändern; Eigenes kennzeichnen.
4. Meldung: Anzahl Kapitel, größte Themenbereiche, Lücken (Kapitel ohne Text, nur Bilder).
