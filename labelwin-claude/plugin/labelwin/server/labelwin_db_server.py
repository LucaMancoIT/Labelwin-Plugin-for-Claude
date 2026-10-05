"""Schreibgeschützter MCP-Server für die Labelwin-MSSQL-Datenbank.

Sicherheit (mehrstufig):
1. Dedizierter DB-Benutzer mit nur db_datareader (siehe SETUP.md) - das ist die eigentliche Absicherung.
2. ApplicationIntent=ReadOnly, Query-Timeout.
3. Dieser Server lässt nur ein einzelnes SELECT/WITH-Statement zu und begrenzt die Zeilenzahl.
"""
import json
import os
import re
from pathlib import Path

import sys
sys.path.insert(0, str(Path(__file__).parent))
import lwconfig  # noqa: E402
import pyodbc  # noqa: E402
from mcp.server.fastmcp import FastMCP  # noqa: E402

mcp = FastMCP("labelwin-db")

MAX_ROWS = 500
FORBIDDEN = re.compile(
    r"\b(insert|update|delete|merge|drop|alter|create|truncate|exec|execute|grant|revoke|"
    r"into|xp_\w+|sp_\w+|openrowset|opendatasource|bulk|waitfor|shutdown)\b",
    re.IGNORECASE,
)


def _conn():
    c = pyodbc.connect(lwconfig.connection_string(), timeout=10)
    c.timeout = 30
    return c


def _rows(sql: str, params=()):
    with _conn() as c:
        cur = c.cursor()
        cur.execute(sql, params)
        cols = [d[0] for d in cur.description]
        data = cur.fetchmany(MAX_ROWS)
    return [dict(zip(cols, [str(v) if v is not None and not isinstance(v, (int, float, str)) else v for v in r])) for r in data]


@mcp.tool()
def list_tables(name_filter: str = "") -> str:
    """Listet Tabellen mit Zeilenanzahl. name_filter = Teilstring (z.B. 'ARTIKEL')."""
    sql = """
    SELECT s.name AS [schema], t.name AS [table], SUM(p.rows) AS row_count
    FROM sys.tables t JOIN sys.schemas s ON s.schema_id = t.schema_id
    JOIN sys.partitions p ON p.object_id = t.object_id AND p.index_id IN (0,1)
    WHERE t.name LIKE ? GROUP BY s.name, t.name ORDER BY t.name"""
    return json.dumps(_rows(sql, (f"%{name_filter}%",)), ensure_ascii=False, default=str)


@mcp.tool()
def describe_table(table: str) -> str:
    """Spalten, Datentypen, Primärschlüssel und Fremdschlüssel einer Tabelle."""
    cols = _rows(
        """SELECT c.COLUMN_NAME, c.DATA_TYPE, c.CHARACTER_MAXIMUM_LENGTH AS len, c.IS_NULLABLE
           FROM INFORMATION_SCHEMA.COLUMNS c WHERE c.TABLE_NAME = ? ORDER BY c.ORDINAL_POSITION""",
        (table,),
    )
    fks = _rows(
        """SELECT fk.name AS fk_name, cp.name AS column_name, tr.name AS ref_table, cr.name AS ref_column
           FROM sys.foreign_key_columns fkc
           JOIN sys.foreign_keys fk ON fk.object_id = fkc.constraint_object_id
           JOIN sys.tables tp ON tp.object_id = fkc.parent_object_id
           JOIN sys.columns cp ON cp.object_id = tp.object_id AND cp.column_id = fkc.parent_column_id
           JOIN sys.tables tr ON tr.object_id = fkc.referenced_object_id
           JOIN sys.columns cr ON cr.object_id = tr.object_id AND cr.column_id = fkc.referenced_column_id
           WHERE tp.name = ?""",
        (table,),
    )
    pks = _rows(
        """SELECT kcu.COLUMN_NAME FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS tc
           JOIN INFORMATION_SCHEMA.KEY_COLUMN_USAGE kcu ON kcu.CONSTRAINT_NAME = tc.CONSTRAINT_NAME
           WHERE tc.CONSTRAINT_TYPE = 'PRIMARY KEY' AND tc.TABLE_NAME = ?""",
        (table,),
    )
    return json.dumps({"columns": cols, "primary_key": pks, "foreign_keys": fks}, ensure_ascii=False, default=str)


@mcp.tool()
def search_columns(pattern: str) -> str:
    """Findet Spalten, deren Name den Teilstring enthält (z.B. 'MWST', 'KUNDE'). Nützlich: 'Wo steht X?'"""
    return json.dumps(
        _rows(
            """SELECT TABLE_NAME, COLUMN_NAME, DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS
               WHERE COLUMN_NAME LIKE ? ORDER BY TABLE_NAME, ORDINAL_POSITION""",
            (f"%{pattern}%",),
        ),
        ensure_ascii=False,
        default=str,
    )


@mcp.tool()
def sample_rows(table: str, n: int = 5) -> str:
    """Beispielzeilen einer Tabelle (max. 20) - um Inhalte/Codes zu verstehen. Personenbezogene Daten beachten!"""
    if not re.fullmatch(r"[A-Za-z0-9_]+", table):
        return "Ungültiger Tabellenname"
    return json.dumps(_rows(f"SELECT TOP {min(max(n,1),20)} * FROM [{table}]"), ensure_ascii=False, default=str)


@mcp.tool()
def run_select(sql: str) -> str:
    """Führt eine einzelne schreibgeschützte SELECT-/WITH-Abfrage aus (max. 500 Zeilen)."""
    s = sql.strip().rstrip(";")
    if ";" in s or not re.match(r"^(select|with)\b", s, re.IGNORECASE) or FORBIDDEN.search(s):
        return "Abgelehnt: nur ein einzelnes SELECT/WITH ohne Schreib-/Systembefehle erlaubt."
    return json.dumps(_rows(s), ensure_ascii=False, default=str)


@mcp.tool()
def list_install_files(subpath: str = "", pattern: str = "*") -> str:
    """Listet Dateien im Labelwin-Installationsverzeichnis (LW_HOME), read-only."""
    base = lwconfig.home().resolve()
    target = (base / subpath).resolve()
    if base not in target.parents and target != base:
        return "Pfad außerhalb des Testsystems."
    return json.dumps(
        [str(p.relative_to(base)) for p in sorted(target.rglob(pattern))[:1000]], ensure_ascii=False
    )


@mcp.tool()
def connection_info() -> str:
    """Zeigt die aktive (nicht geheime) Konfiguration: LW_HOME, Server, Datenbank, Authentifizierung."""
    return json.dumps(lwconfig.describe(), ensure_ascii=False)


if __name__ == "__main__":
    mcp.run()
