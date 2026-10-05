# Einrichtung Labelwin-Plugin

Das Plugin ist auf **beliebige Labelwin-Installationen** ausgelegt (Test- oder Kundensystem). Es braucht nur:
1. das Labelwin-Verzeichnis (`LW_HOME`, z.B. `C:\Testlabel5.100`)
2. einen lesenden DB-Zugang.

Server (`sqlservername`) und Datenbank (`sqldatenbank`) liest es selbst aus `<LW_HOME>\global.ini`. Zugangsdaten liest es **nie** aus `global.ini` (dort steht ein Benutzer mit Schreibrechten).

## 1. Voraussetzungen
- Python 3.10+, ODBC-Treiber für SQL Server (Treiber wird automatisch gewählt: 18 → 17 → 13 → "SQL Server")
- `pip install -r server/requirements.txt`

## 2. Schreibgeschützter DB-Benutzer (echte Absicherung)
Möglichst gegen eine **Kopie/Testdatenbank**. Auf dem SQL Server (Datenbank z.B. `projdat`):
```sql
CREATE LOGIN claude_ro WITH PASSWORD = '<starkes Passwort>';
USE projdat;
CREATE USER claude_ro FOR LOGIN claude_ro;
ALTER ROLE db_datareader ADD MEMBER claude_ro;
```
Kein db_datawriter, keine Adminrechte. Alternativ Windows-Authentifizierung (`db_trusted = 1`).
Bei personenbezogenen Daten: Testdaten anonymisieren oder Spalten per DENY sperren.

## 3. Konfiguration
Die Zugangsdaten liegen in `%USERPROFILE%\.claude\labelwin.env`, **außerhalb** des Plugins (alles im Plugin-Ordner wird beim Hochladen mit hochgeladen). Am einfachsten: im Repo `labelwin.env` ausfüllen und `einrichten.bat` starten (siehe README des Repos). Werte: `LW_HOME`, optional `LW_DB_SERVER`/`LW_DB_NAME` (sonst aus `global.ini`), `LW_DB_USER`/`LW_DB_PASSWORD` oder `LW_DB_TRUSTED=1`. Echte Umgebungsvariablen haben Vorrang; ein anderes System per `LW_CONFIG=<Pfad>`.
Kontrolle: MCP-Tool `connection_info` zeigt die aktive Konfiguration (ohne Geheimnisse).

## 4. Plugin laden
Claude-Desktop: **Anpassen → Plugins → Hinzufügen → Plugin hochladen** → `labelwin-plugin.zip` (gebaut mit `werkzeuge/plugin_zip_bauen.py`). Claude Code: `claude --plugin-dir <Pfad>/plugin/labelwin`.

## 5. Wissen aufbauen (pro Installation; bei Update wiederholen)
1. `/labelwin:ingest-handbuch` – lokales Handbuch (`<LW_HOME>\handbuch`) → Markdown (1405 Kapitel, ~9 MB, ~15 s)
2. `/labelwin:scan-testsystem` – Verzeichnisinventar
3. `/labelwin:ingest-schema` – Datenbankstruktur (braucht DB-Zugang)
4. Kundendokumente/Recherche in `skills/labelwin-business/references/` ablegen

Die Ingest-Ergebnisse (`generated/`, `handbuch/`) gehören zur jeweiligen Installation/Version. Für ein weiteres System neu erzeugen; das kuratierte Wissen (`schema-notes.md`, `architektur.md`) versionsspezifisch prüfen.

## 6. Spezialisierte Chats
| Aufgabe | Agent |
|---|---|
| Auswertungen, SQL, Datenfehler | `labelwin-datenanalyst` |
| Fehlerbehebung, Konfiguration, Entwicklung | `labelwin-systemtechniker` |
| Prozessberatung, Konzepte | `labelwin-handwerksberater` |
| Bedienung, Schulung, Anleitungen | `labelwin-anwendungstrainer` |

## Hinweis Claude.ai-Projekt
Claude.ai-Projekte können keine lokale DB anbinden. Dort: `handbuch/`, `generated/` und Skill-Texte als Projektwissen hochladen (statischer Stand).
