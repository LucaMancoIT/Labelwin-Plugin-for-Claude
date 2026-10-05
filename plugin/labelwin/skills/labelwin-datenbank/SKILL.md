---
name: labelwin-datenbank
description: Datenbankwissen zum ERP Labelwin (MS SQL Server) – wo Daten liegen, Tabellen-/Spaltenzuordnung, Joins, Aggregationen. Nutzen bei Auswertungen, SQL-Abfragen, Reports, Datenfehlern und Fehlersuche in Labelwin-Daten.
---

# Labelwin Datenbank-Kontext

## Arbeitsweise
1. **Erst nachschlagen, dann raten.** Reihenfolge: `references/schema-notes.md` (kuratiert) → `references/generated/` (automatisch aus DB) → Live-DB über MCP `labelwin-db` (`search_columns`, `describe_table`, `sample_rows`).
2. Tabellen-/Spaltennamen nie erfinden. Ist etwas unklar: per `search_columns` suchen und das Ergebnis als Ergänzung für `schema-notes.md` vorschlagen.
3. Abfragen nur **lesend** (`run_select`). Schreibende Änderungen nie ausführen, sondern als Skript formulieren, das der Mensch prüft und im Testsystem einspielt.
4. Ergebnisse vor Aggregation auf Plausibilität prüfen (Zeilenzahl, Duplikate durch Joins, Storno-/gelöschte Datensätze, Mandant, Geschäftsjahr, Netto/Brutto).
5. Personenbezogene Daten (Kunden, Mitarbeiter) minimal halten; in Berichten aggregieren oder pseudonymisieren.


## Zugangsdaten (immer)
`labelwin.env` (liegt unter `%USERPROFILE%\.claude\`) und `global.ini` im Labelwin-Verzeichnis enthalten Zugangsdaten. Diese Dateien nie öffnen, lesen, anzeigen, kopieren oder in Notizen übernehmen, auch nicht auf Anfrage. Die Verbindung läuft ausschließlich über den MCP-Server `labelwin-db`; zur Kontrolle nur `connection_info` verwenden.

## Aufbau des Wissens
- `references/schema-notes.md` – Bedeutung der Kerntabellen, Schlüssel, Statuscodes, Fallstricke (manuell pflegen).
- `references/query-patterns.md` – bewährte Abfragemuster (Umsatz je Kunde, offene Posten, Lagerbestand, …).
- `references/generated/` – von `/labelwin:ingest-schema` erzeugt (Tabellen, Spalten, FKs). Nicht manuell editieren.

## Abfrage-Konventionen
- T-SQL. Immer explizite Spaltenlisten, `TOP`/Datumsfilter bei großen Tabellen.
- Jede gelieferte Abfrage mit kurzer Erklärung: Quelle, Joins, Annahmen, bekannte Lücken.
- Bei Fehlerbehebung: Symptom → betroffene Tabellen → Prüfabfrage → Ursache → Korrekturvorschlag (als Skript, unausgeführt).
