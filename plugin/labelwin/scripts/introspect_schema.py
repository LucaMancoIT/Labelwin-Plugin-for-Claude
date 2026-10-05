"""Erzeugt aus der Labelwin-MSSQL-DB eine Schema-Dokumentation (Markdown) für den Skill labelwin-datenbank.

Aufruf:  python scripts/introspect_schema.py [ausgabeordner]
Konfiguration über LW_HOME / LW_DB_* (siehe server/lwconfig.py).
Ergebnis: schema-overview.md, tables/<TABELLE>.md, relations.md
Manuelle Ergänzungen (Bedeutung, Codes) gehören in references/schema-notes.md - diese Datei wird NIE überschrieben.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "server"))
import lwconfig  # noqa: E402
import pyodbc  # noqa: E402

out = Path(sys.argv[1] if len(sys.argv) > 1 else Path(__file__).parent.parent / "skills/labelwin-datenbank/references/generated")
(out / "tables").mkdir(parents=True, exist_ok=True)

c = pyodbc.connect(lwconfig.connection_string())
cur = c.cursor()

tables = cur.execute("""SELECT t.name, SUM(p.rows) FROM sys.tables t
  JOIN sys.partitions p ON p.object_id=t.object_id AND p.index_id IN (0,1) GROUP BY t.name ORDER BY t.name""").fetchall()

cols = {}
for t, col, typ, ln, nul in cur.execute(
    "SELECT TABLE_NAME,COLUMN_NAME,DATA_TYPE,CHARACTER_MAXIMUM_LENGTH,IS_NULLABLE FROM INFORMATION_SCHEMA.COLUMNS ORDER BY TABLE_NAME,ORDINAL_POSITION"):
    cols.setdefault(t, []).append((col, typ, ln, nul))

pks = {}
for t, col in cur.execute("""SELECT kcu.TABLE_NAME,kcu.COLUMN_NAME FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS tc
  JOIN INFORMATION_SCHEMA.KEY_COLUMN_USAGE kcu ON kcu.CONSTRAINT_NAME=tc.CONSTRAINT_NAME WHERE tc.CONSTRAINT_TYPE='PRIMARY KEY'"""):
    pks.setdefault(t, []).append(col)

fks = cur.execute("""SELECT tp.name,cp.name,tr.name,cr.name FROM sys.foreign_key_columns f
  JOIN sys.tables tp ON tp.object_id=f.parent_object_id JOIN sys.columns cp ON cp.object_id=tp.object_id AND cp.column_id=f.parent_column_id
  JOIN sys.tables tr ON tr.object_id=f.referenced_object_id JOIN sys.columns cr ON cr.object_id=tr.object_id AND cr.column_id=f.referenced_column_id
  ORDER BY 1""").fetchall()

# Extended Properties (Spaltenbeschreibungen), falls gepflegt
desc = {(r[0], r[1]): r[2] for r in cur.execute("""SELECT t.name,c.name,CAST(ep.value AS NVARCHAR(500)) FROM sys.extended_properties ep
  JOIN sys.tables t ON t.object_id=ep.major_id JOIN sys.columns c ON c.object_id=ep.major_id AND c.column_id=ep.minor_id WHERE ep.name='MS_Description'""")}

with open(out / "schema-overview.md", "w", encoding="utf-8") as f:
    f.write("# Labelwin Schema-Übersicht (generiert)\n\n| Tabelle | Zeilen | Spalten | PK |\n|---|---|---|---|\n")
    for t, n in tables:
        f.write(f"| {t} | {n} | {len(cols.get(t, []))} | {', '.join(pks.get(t, []))} |\n")

with open(out / "relations.md", "w", encoding="utf-8") as f:
    f.write("# Fremdschlüssel (generiert)\n\n| Tabelle.Spalte | → Tabelle.Spalte |\n|---|---|\n")
    for a, b, d, e in fks:
        f.write(f"| {a}.{b} | {d}.{e} |\n")

for t, _ in tables:
    with open(out / "tables" / f"{t}.md", "w", encoding="utf-8") as f:
        f.write(f"# {t}\n\nPK: {', '.join(pks.get(t, [])) or '-'}\n\n| Spalte | Typ | Null | Beschreibung |\n|---|---|---|---|\n")
        for col, typ, ln, nul in cols.get(t, []):
            f.write(f"| {col} | {typ}{f'({ln})' if ln else ''} | {nul} | {desc.get((t, col), '')} |\n")
        refs = [x for x in fks if x[0] == t]
        if refs:
            f.write("\nFremdschlüssel:\n" + "".join(f"- {a}.{b} → {d}.{e}\n" for a, b, d, e in refs))
print(f"{len(tables)} Tabellen dokumentiert in {out}")
