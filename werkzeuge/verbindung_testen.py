"""Prueft die Plugin-Konfiguration (wird von einrichten.bat aufgerufen).

Liest %USERPROFILE%\\.claude\\labelwin.env ueber dieselbe Logik wie das Plugin.
Gibt nie Passwoerter oder Verbindungszeichenfolgen aus.
"""
import os
import sys
from pathlib import Path

ENV_DATEI = Path.home() / ".claude" / "labelwin.env"
os.environ["LW_CONFIG"] = str(ENV_DATEI)
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "plugin" / "labelwin" / "server"))


def ok(text):
    print(f"  [OK]     {text}")


def fehler(text, tipp=""):
    print(f"  [FEHLER] {text}")
    if tipp:
        print(f"           -> {tipp}")
    sys.exit(1)


print("\nVerbindung wird geprueft ...")

if sys.version_info < (3, 10):
    fehler(f"Python {sys.version.split()[0]} ist zu alt.", "Python 3.10 oder neuer installieren.")
ok(f"Python {sys.version.split()[0]}")

try:
    import pyodbc  # noqa: F401
    import mcp  # noqa: F401
except ImportError as e:
    fehler(f"Paket fehlt: {e.name}", "einrichten.bat erneut ausfuehren.")
ok("Pakete mcp und pyodbc vorhanden")

if not ENV_DATEI.is_file():
    fehler(f"{ENV_DATEI} nicht gefunden.", "einrichten.bat erneut ausfuehren.")

import lwconfig  # noqa: E402

try:
    info = lwconfig.describe()
except Exception as e:  # noqa: BLE001
    fehler(str(e), "LW_HOME in labelwin.env pruefen.")
ok(f"Labelwin-Verzeichnis: {info['home']}")
if not info["server"] or not info["database"]:
    fehler("SQL-Server oder Datenbank unbekannt.", "LW_DB_SERVER und LW_DB_NAME in labelwin.env eintragen.")
ok(f"Server: {info['server']}  Datenbank: {info['database']}  Anmeldung: {info['auth']}")

try:
    driver = lwconfig.pick_driver()
except Exception as e:  # noqa: BLE001
    fehler(str(e), "'ODBC Driver 18 for SQL Server' von Microsoft installieren.")
ok(f"ODBC-Treiber: {driver}")

try:
    conn = pyodbc.connect(lwconfig.connection_string(), timeout=10)
except Exception as e:  # noqa: BLE001
    msg = str(e).split("(SQLDriverConnect")[0]
    fehler(f"Anmeldung an der Datenbank fehlgeschlagen: {msg}",
           "Server/Datenbank, Benutzer und Passwort pruefen (Benutzer anlegen: sql\\lesebenutzer_anlegen.sql).")

cur = conn.cursor()
anzahl = cur.execute("SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES").fetchone()[0]
ok(f"Verbunden, {anzahl} Tabellen sichtbar")

darf_schreiben = cur.execute(
    "SELECT CASE WHEN IS_ROLEMEMBER('db_owner') = 1 OR IS_ROLEMEMBER('db_datawriter') = 1 "
    "OR HAS_PERMS_BY_NAME(DB_NAME(), 'DATABASE', 'INSERT') = 1 "
    "OR HAS_PERMS_BY_NAME(DB_NAME(), 'DATABASE', 'UPDATE') = 1 "
    "OR HAS_PERMS_BY_NAME(DB_NAME(), 'DATABASE', 'DELETE') = 1 THEN 1 ELSE 0 END"
).fetchone()[0]
conn.close()

if darf_schreiben:
    print("  [WARNUNG] Dieser Benutzer hat SCHREIBRECHTE auf die Datenbank.")
    print("            Das Plugin fragt zwar nur lesend ab, sicher ist aber nur ein reiner Lese-Benutzer.")
    print("            -> Benutzer mit sql\\lesebenutzer_anlegen.sql anlegen und in labelwin.env eintragen.")
else:
    ok("Benutzer hat nur Leserechte")

print("\nAlles bereit. Jetzt in Claude: Anpassen > Plugins > Hinzufuegen > Plugin hochladen")
print("und die Datei labelwin.plugin hineinziehen.\n")
