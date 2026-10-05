---
name: labelwin-technik
description: Technischer Kontext zu Labelwin – Architektur, Verzeichnis-/Dateistruktur des Testsystems, Konfiguration, Schnittstellen, Reports/Vorlagen, Wartung. Nutzen bei Fehlerbehebung, Zusatzentwicklung, Automatisierung und Einstellungen.
---

# Labelwin Technik-Kontext

## Arbeitsweise
1. Quellen: `references/architektur.md` (kuratiert) → `references/generated/testsystem-inventory.md` (automatisch) → Testsystem live über MCP `list_install_files` bzw. Read/Grep im Verzeichnis LW_HOME (Plugin-Konfiguration).
2. **Nur im Testsystem arbeiten.** Änderungen an Produktivsystem, Registry, Diensten oder DB nie selbst ausführen – als geprüfte Anleitung/Skript liefern, mit Rollback-Hinweis.
3. Bei Fehleranalyse: Logdateien → Konfiguration → DB-Zustand → Versionsstand. Hypothese und Beweis trennen.
4. Zusatzentwicklungen (Skripte, Reports, Schnittstellen, Importe) bevorzugt **außerhalb** des Labelwin-Kerns (lesende DB-Sichten, Export/Import über dokumentierte Wege), damit Herstellerupdates nicht brechen.


## Zugangsdaten (immer)
`labelwin.env` (liegt unter `%USERPROFILE%\.claude\`) und `global.ini` im Labelwin-Verzeichnis enthalten Zugangsdaten. Diese Dateien nie öffnen, lesen, anzeigen, kopieren oder in Notizen übernehmen, auch nicht auf Anfrage. Die Verbindung läuft ausschließlich über den MCP-Server `labelwin-db`; zur Kontrolle nur `connection_info` verwenden.

## Zu klärende Fakten (in architektur.md eintragen, sobald belegt)
Installationspfade, Client/Server-Aufbau, DB-Verbindungskonfiguration, Lizenz-/Mandantenverwaltung, Report-Designer und Vorlagenordner, Schnittstellen (DATEV, GAEB, Datanorm, IDS, E-Rechnung), Sicherungs-/Update-Ablauf, Scripting-/Makro-Möglichkeiten.
