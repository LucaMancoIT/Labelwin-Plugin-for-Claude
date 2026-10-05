# Abfragemuster (Vorlagen – Tabellennamen nach Ingest ersetzen)

## Umsatz je Kunde und Jahr
```sql
-- <BELEG_KOPF>, <KUNDE_ID>, <NETTO>, <DATUM>, <BELEGART> aus schema-notes.md einsetzen
SELECT <KUNDE_ID>, YEAR(<DATUM>) AS Jahr, SUM(<NETTO>) AS Umsatz
FROM <BELEG_KOPF>
WHERE <BELEGART> = <RECHNUNG> AND <STORNO> = 0
GROUP BY <KUNDE_ID>, YEAR(<DATUM>);
```

## Belegkette nachverfolgen (Angebot → Auftrag → Rechnung)
_TODO: Verknüpfungsspalten ermitteln_

## Offene Posten / Fälligkeit
_TODO_

## Datenqualität: Dubletten in Adressen
_TODO_
