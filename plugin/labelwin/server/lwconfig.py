"""Gemeinsame Konfiguration für MCP-Server und Skripte – funktioniert für beliebige Labelwin-Installationen.

Auflösung (höchste Priorität zuerst): Umgebungsvariablen, dann Datei labelwin.env.
Suchreihenfolge: LW_CONFIG, %USERPROFILE%\\.claude\\labelwin.env (Standard, wird von einrichten.bat angelegt), Plugin-Ordner (Altfall).
Die Datei liegt bewusst AUSSERHALB des Plugins: alles im Plugin-Ordner wird beim Hochladen mit hochgeladen.

  LW_HOME          Installationsverzeichnis des Labelwin-Systems (Test- oder Produktivsystem, z.B. C:\\Testlabel5.100)
  LW_DB_SERVER     sonst: Schlüssel 'sqlservername' aus <LW_HOME>\\global.ini
  LW_DB_NAME       sonst: Schlüssel 'sqldatenbank'  aus <LW_HOME>\\global.ini
  LW_DB_USER / LW_DB_PASSWORD   Zugangsdaten (NIE aus global.ini gelesen – dort liegt meist ein Schreib-Benutzer)
  LW_DB_TRUSTED=1  Windows-Authentifizierung statt Benutzer/Passwort
  LW_DB_DRIVER     sonst: neuester installierter SQL-Server-ODBC-Treiber
Werte, die wie ein nicht aufgelöster Platzhalter aussehen ('${...}') oder leer sind, gelten als nicht gesetzt.
"""
import os
import re
from pathlib import Path


def _load_env_file() -> None:
    """Lädt labelwin.env (LW_CONFIG, sonst Benutzerordner\\.claude, sonst Plugin-Ordner). Bereits gesetzte Umgebungsvariablen haben Vorrang."""
    candidates = [os.environ.get("LW_CONFIG"), Path.home() / ".claude" / "labelwin.env", Path(__file__).parent.parent / "labelwin.env"]
    f = next((Path(c) for c in candidates if c and Path(c).is_file()), None)
    if f is None:
        return
    for line in f.read_text(encoding="utf-8-sig").splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1)
            k, v = k.strip(), v.strip().strip('"').strip("'")
            if v and not os.environ.get(k, "").strip():
                os.environ[k] = v


_load_env_file()


def env(name: str, default: str = "") -> str:
    v = os.environ.get(name, "").strip()
    return default if not v or v.startswith("${") else v


def home() -> Path:
    h = env("LW_HOME") or env("LW_TEST_SYSTEM_DIR")
    if not h:
        raise RuntimeError("LW_HOME nicht gesetzt (Labelwin-Installationsverzeichnis, z.B. C:\\Testlabel5.100).")
    p = Path(h)
    if not p.is_dir():
        raise RuntimeError(f"LW_HOME existiert nicht: {p}")
    return p


def ini_value(key: str) -> str:
    """Liest genau einen Schlüssel aus <LW_HOME>/global.ini (ohne die restliche Datei zu parsen)."""
    ini = home() / "global.ini"
    if not ini.is_file():
        return ""
    pat = re.compile(rf"^\s*{re.escape(key)}\s*=\s*(.*?)\s*$", re.IGNORECASE)
    for line in ini.read_text(encoding="cp1252", errors="replace").splitlines():
        m = pat.match(line)
        if m and m.group(1):
            return m.group(1)
    return ""


def pick_driver() -> str:
    d = env("LW_DB_DRIVER")
    if d:
        return d
    import pyodbc

    for cand in ("ODBC Driver 18 for SQL Server", "ODBC Driver 17 for SQL Server", "ODBC Driver 13 for SQL Server", "SQL Server"):
        if cand in pyodbc.drivers():
            return cand
    raise RuntimeError("Kein SQL-Server-ODBC-Treiber gefunden (pyodbc.drivers()).")


def connection_string() -> str:
    server = env("LW_DB_SERVER") or ini_value("sqlservername")
    db = env("LW_DB_NAME") or ini_value("sqldatenbank")
    if not server or not db:
        raise RuntimeError("DB-Server/-Name unbekannt: LW_DB_SERVER/LW_DB_NAME setzen oder LW_HOME mit global.ini angeben.")
    parts = [f"DRIVER={{{pick_driver()}}}", f"SERVER={server}", f"DATABASE={db}", "ApplicationIntent=ReadOnly"]
    if env("LW_DB_TRUSTED") == "1":
        parts.append("Trusted_Connection=yes")
    else:
        user, pw = env("LW_DB_USER"), env("LW_DB_PASSWORD")
        if not user or not pw:
            raise RuntimeError("LW_DB_USER/LW_DB_PASSWORD fehlen (oder LW_DB_TRUSTED=1 setzen).")
        parts += [f"UID={user}", f"PWD={pw}"]
    if "ODBC Driver" in parts[0]:
        parts += ["TrustServerCertificate=yes", "Encrypt=optional"]
    return ";".join(parts)


def describe() -> dict:
    """Nicht-geheime Konfigurationsübersicht (für Diagnose)."""
    return {
        "home": str(home()),
        "server": env("LW_DB_SERVER") or ini_value("sqlservername"),
        "database": env("LW_DB_NAME") or ini_value("sqldatenbank"),
        "server_typ": ini_value("sqlservertyp"),
        "auth": "windows" if env("LW_DB_TRUSTED") == "1" else "sql-login",
    }
