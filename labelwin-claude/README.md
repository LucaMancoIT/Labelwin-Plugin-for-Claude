# Labelwin-Plugin für Claude

Mit diesem Plugin arbeitet Claude mit eurem Labelwin-Testsystem: Es kennt Bedienung, Datenbank und Technik von Labelwin und kann die Datenbank **nur lesend** abfragen.

## Einrichtung in 4 Schritten

**Voraussetzungen:** Windows-Rechner mit Zugriff auf das Labelwin-Testsystem, die [Claude-Desktop-App](https://claude.ai/download) und [Python 3.10+](https://www.python.org/downloads/) (bei der Installation „Add python.exe to PATH“ anhaken).

1. **Repo herunterladen**
   Auf GitHub oben rechts **Code → Download ZIP**, entpacken.

2. **`labelwin.env` ausfüllen**
   Die Datei mit dem Editor öffnen und eintragen:
   | Feld | Bedeutung |
   |---|---|
   | `LW_HOME` | Labelwin-Verzeichnis, z. B. `C:\Testlabel5.100` |
   | `LW_DB_SERVER`, `LW_DB_NAME` | SQL Server und Datenbank (leer = automatisch aus `global.ini`) |
   | `LW_DB_USER`, `LW_DB_PASSWORD` | Lese-Benutzer der Datenbank |

   Noch kein Lese-Benutzer vorhanden? Siehe [Lese-Benutzer anlegen](#lese-benutzer-anlegen-optional).

3. **`einrichten.bat` doppelklicken**
   Installiert die nötigen Python-Pakete, legt die Zugangsdaten an ihren festen Platz und testet die Verbindung. Am Ende muss „Alles bereit“ stehen.

4. **Plugin in Claude hochladen**
   In der Claude-Desktop-App: **Anpassen → Plugins → Hinzufügen → Plugin hochladen** und `labelwin.plugin` hineinziehen (`labelwin-plugin.zip` ist dieselbe Datei als Zip). Den Ordner `plugin` nicht selbst zippen: Dann liegt alles eine Ebene zu tief und der Upload schlägt fehl. Beim ersten Einsatz fragt Claude, ob der lokale Labelwin-Server starten darf: bestätigen.

**Testen:** In einem neuen Chat „Zeig mir die Labelwin-Verbindungsinfo“ eingeben.

## Was passiert mit meinen Zugangsdaten?

```
labelwin.plugin      ──hochladen──►  Claude          (nur Wissen + Programmcode, KEINE Zugangsdaten)
labelwin.env         ──einrichten.bat──►  C:\Users\<Name>\.claude\labelwin.env   (bleibt auf deinem PC)
```

- Die Zugangsdaten werden **nicht** mit hochgeladen. Alles im Plugin-Zip landet bei Claude, deshalb liegt `labelwin.env` bewusst außerhalb.
- Der kleine Labelwin-Server des Plugins läuft **lokal auf deinem PC**. Er liest `labelwin.env` beim Start selbst und baut die Verbindung zur Datenbank auf.
- Claude bekommt nur die **Ergebnisse** der Abfragen zu sehen, nie Benutzer oder Passwort. Das Plugin weist Claude zusätzlich an, `labelwin.env` und `global.ini` nie zu öffnen.
- Der Server lässt nur einzelne `SELECT`-Abfragen zu. Die eigentliche Absicherung ist aber der Lese-Benutzer: Selbst wenn etwas schiefgeht, kann er nichts ändern.
- Nach erfolgreicher Einrichtung darf die ausgefüllte `labelwin.env` im Download-Ordner gelöscht werden.

## Lese-Benutzer anlegen (optional)

Das Skript liegt doppelt vor, als `sql\lesebenutzer_anlegen.sql` und als `sql\lesebenutzer_anlegen.txt` (gleicher Inhalt, zum Öffnen ohne SQL-Programm).

1. In **SQL Server Management Studio** mit einem Administrator-Konto anmelden.
2. Skript öffnen, oben Benutzername, Passwort und Datenbank (`sqldatenbank` aus der `global.ini`) eintragen.
3. **F5** drücken. Danach Benutzer und Passwort in `labelwin.env` eintragen.

Das Skript vergibt nur `db_datareader` und kann mehrfach ausgeführt werden. Unten im Skript steht eine Variante ganz ohne Passwort über eine Windows-/AD-Gruppe (`LW_DB_TRUSTED=1`).

## Häufige Fehler

| Meldung von `einrichten.bat` | Lösung |
|---|---|
| Python nicht gefunden | Python installieren, „Add python.exe to PATH“ anhaken, neu starten |
| Kein ODBC-Treiber | „ODBC Driver 18 for SQL Server“ von Microsoft installieren |
| Anmeldung fehlgeschlagen | Server, Datenbank, Benutzer, Passwort in `labelwin.env` prüfen, `einrichten.bat` erneut starten |
| Warnung „Schreibrechte“ | Eigenen Lese-Benutzer mit dem SQL-Skript anlegen |

## Für Betreuer des Plugins

- Plugin-Quellcode: `plugin/labelwin/`. Nach Änderungen `python werkzeuge/plugin_zip_bauen.py` ausführen und `labelwin.plugin` sowie `labelwin-plugin.zip` mit committen. Die Version in `plugin/labelwin/.claude-plugin/plugin.json` hochzählen.
- Updates erreichen die Kollegen erst, wenn sie die neue `labelwin.plugin` erneut hochladen. `labelwin.env` muss dafür nicht neu angelegt werden.
- **Niemals eine ausgefüllte `labelwin.env` committen.** Wer im Repo-Ordner selbst Daten einträgt, schützt sich mit: `git update-index --skip-worktree labelwin.env`
- Das Repo sollte privat bleiben: Das Plugin enthält das umgewandelte Labelwin-Handbuch und die Schema-Doku des Testsystems.
