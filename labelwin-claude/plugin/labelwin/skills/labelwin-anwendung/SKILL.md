---
name: labelwin-anwendung
description: Bedienung des Programms Labelwin – Menüs, Masken, Arbeitsabläufe Schritt für Schritt, abgeleitet aus der Bedienungsanleitung. Nutzen für Anwenderanleitungen, Schulungen, Prozessdefinition und die Frage "Wie mache ich X in Labelwin?".
---

# Labelwin Anwendungs-Kontext

## Quellen
- Bedienungsanleitung im Projektwissen bzw. `references/handbuch/` (per `/labelwin:ingest-handbuch` aus `<LW_HOME>/handbuch` in Markdown-Kapitel konvertiert; Einstieg: `references/handbuch/INDEX.md`, dort Hierarchie und Dateinamen; gezielt per Grep durchsuchen, nicht komplett laden).
- Testsystem zum Nachvollziehen (nur dort ausprobieren).

## Arbeitsweise
1. Antworten mit Handbuchkapitel/Seite belegen. Nicht Belegtes als "nicht belegt – im Testsystem prüfen" markieren.
2. Anleitungen als nummerierte Schritte mit Menüpfad und Feldnamen exakt wie in der Oberfläche.
3. Aus Bedienabläufen Prozesse ableiten: Auslöser → Schritte → Ergebnis → beteiligte Rollen → Datenfluss (welche Tabellen; Verknüpfung mit `labelwin-datenbank`).
4. Bedienschritte im Testsystem gegen die DB prüfen (Datensatz vor/nach) und Abweichungen zum Handbuch dokumentieren.
