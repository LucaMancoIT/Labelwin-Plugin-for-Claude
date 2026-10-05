# Schema-Notizen Labelwin (kuratiert)

> Stand: 2026-09-30, Erstentwurf aus Tabellen-/Spaltennamen der Testdatenbank `projdat` (MSSQL2014, 377 Tabellen).
> **(vermutet)** = aus Namen abgeleitet, noch nicht per Daten/Handbuch bestätigt. Beim Bestätigen Markierung entfernen.
> Neue Erkenntnisse hier mit Datum ergänzen. Vollständige Spaltenlisten: `generated/tables/<tabelle>.md`.

## Allgemeine Eigenschaften der DB
- **Praktisch keine Fremdschlüssel** (nur 3 in der DB) – Beziehungen sind reine Konvention über gleichnamige Spalten und müssen hier dokumentiert werden.
- Tabellen- und Spaltennamen klein geschrieben, ohne Präfixe. Fast jede Tabelle hat `lfdnr` als Primärschlüssel.
- Wiederkehrende Spalten (vermutet): `mandant` (Mandantentrennung – bei Auswertungen immer beachten), `filialnr`, `externenr`, `tkzue0/1/2`, `tkzzu0/1/2` (Filial-/Replikationskennung bzw. Zusatzfelder), `loeschen`/`schloss` (Löschkennzeichen/Sperre).
- Spalten mit Präfix `erf…` (z.B. `erfnetto`, `erfbrutto` in `rgausgang`, `eingangsrg`) sind vermutlich Beträge in Erfassungswährung, ohne Präfix in Hauswährung, `waekz…` = Währungskennzeichen. (vermutet)
- Spalten mit Suffix `euro` in `artikel1` (z.B. `epeuro`) deuten auf Altbestand DM/Euro-Umstellung (vermutet).
- Auch neben SQL Server existieren Access-Dateien (`.mdb`) für Kataloge, Vorlagen, Aufmaß, Datanorm (siehe `labelwin-technik`).

## Kernbereiche
| Fachbereich | Tabellen | Schlüssel | Hinweise |
|---|---|---|---|
| Adressen (Kunden/Lieferanten/Bauherren) | `adstamm` (874 Zeilen, 160 Spalten), `adtel`, `adindex`, `aderw`, `adkred`, `adrkrit`, `adrkundeninfo`, `admail`, `weitereadr`, `adresslink` | `adstamm.adnr` | `debi` (Debitorennr.), `kredit`/`kredinr` (Kreditor), `selektion1–6`, `marketing1–10`, `zahlbed`, `mwstschluessel`, `sammelrechnungsgruppe`. Kunde und Lieferant liegen (vermutet) im gleichen Stamm, unterschieden über `debi`/`kredit`. |
| Projekte / Baustellen | `projgrund` (Projektstamm), `projzusatz`, `projekttage`, `projraeume`, `projvereinbarungen`, `projgrundsel`, `prstand`, `prkostenplan`, `vorkalk*` | `projgrund.projektnr` | `ad1nr…ad5nr` verweisen (vermutet) auf `adstamm.adnr` (Rollen wie Bauherr, Rechnungsempfänger …). `status`, `kostenstelle`, `mandant`, `hauptprojektnr` (Unterprojekte). |
| Belegkopf (Angebot, AB, Lieferschein, Bestellung, LV …) | `textkopf` (9.062 Zeilen, 186 Spalten) | `textkopf.projektnummer` + `textzaehler` (vermutet) | `art`/`arttext` = Belegart. Summen: `gesamtnetto`, `gesamtlohn`, `gesamtek`, `gesamtzeit`, MwSt-Aufteilung. Flags `zangebot`, `zrechnung`, `zab`, `zlieferschein`, `zbestellung`, `zlv` … (zugelassene Belegarten). |
| Belegpositionen | `artikel1` (139.533 Zeilen, 111 Spalten) | `artzaehler`; Verknüpfung `textnummer` → `textkopf.textzaehler` (vermutet) | Preise: `ep`, `gp`, `ek`, `lp`, `matvk`, `lohnpr`, `menge`, `mwst`. `posnummer`, `reihenfolge`, `kurztext`, `langrtext`. Steuerung: `alternativ`, `eventual`, `textart`, `fremdleistung`, `pauschal`. |
| Rechnungsausgang | `rgausgang`, `srgausgang` (Schlussrechnung?), `rgausgangvert`, `rgausgzahlein`, `rgauswart`, `rgmahn`, `mahnen`, `mahnzins`, `mahnausgabe` | `rgausgang.rgnummer`/`lfdnr` | `projektnr`+`textnr` verweisen auf Beleg. `netto`, `brutto`, `mwst`, `mwst7`, `ek`, `lohn`; Zahlung: `zahlbetrag`, `zahldatum`, `zahlziel`, `skonto*`; Mahnwesen: `mahnstufe`, `mahndatum`. `status`, `rechnungsart`, `teilleistung`, `kumulierend`. |
| Rechnungseingang | `eingangsrg`, `einrgname`, `einrgvert`, `einrgzahlplan`, `einrgbezahleinzel`, `eingzahlen`, `zahlungslauf`, `zahlungslaufteil` | `eingangsrg.lfdnr` | `lieferant` → `adstamm.adnr` (vermutet), `netto15/7/0`, `mwst15/7`, `brutto`, `zahlziel1–3`, `skonto1–2`, `bezahltdatum`, `status`. |
| Service/Wartung | `kd` (1.603), `kdstatus*`, `kdcheck`, `kdbelegt*`, `kdterminabgleich`, `termine`, `terminarbeit`, `termintaetigkeit`, `wartvert`, `wartart`, `anlagen`, `anlagenart`, `anlagencheck`, `material` | `kd.lfdnr` (Kundendienst-/Serviceauftrag, `auftrnr`) | `kd`: `monteur`, `status`, `rgnr`, `wartlohn`, `wartmaterial`, `anlagennr`, `projektnummer`, `textkopfnr`. `material` = Materialverbrauch am Serviceauftrag (`terminnr` → `kd.terminnummer`, vermutet). `anlagen` = Anlagenakte beim Kunden. |
| Zeiterfassung / Personal | `zeiterfassung` (2.337), `zeitauswert`, `zeitkorrektur`, `zeitpausch`, `zeitstempel`, `zeitzulagen`, `stundenart*`, `personal`, `personalgruppe`, `personalquali`, `persteam`, `personalzeit`, `lohnart`, `lohngruppe`, `lohnlauf` | `zeiterfassung.lfdnr`; `personal.montnr` | `zeiterfassung.montnr` → `personal.montnr`; `projekt` = Projektnr., `kdauftrag` = Serviceauftrag, `std`/`stdart`, Kosten `kostenstdsk/vr`. |
| Artikel / Preise / Kataloge | `artikel1` (Belegpos.!), `artikel2`, `artrefkopf`/`artrefpos`, `preisspiegel`, `preislistekopf/-zeile`, `kataloge`, `katzuordnung`, `datanormonline`, `evu*`, `gruppenkalk*` | | **Achtung:** `artikel1` ist *nicht* der Artikelstamm, sondern die Positionen der Belege. Der Artikelstamm liegt (vermutet) in den Katalogen (`.mdb`/`kataloge`). Noch klären. |
| Vorkalkulation | `vorkalk2*`, `vorkalkulationen`, `vorkalkgruppen`, `kalktb`, `kalkgruppennamen`, `projvorkalk2*` | | Kalkulationsgrundlagen (vermutet). |
| Fibu / Konten | `kontenplan`, `erloeskonten`, `kostenstellen`, `kostenart`, `bilanzgruppe`, `fibulauf`, `bankdaten`, `mwst`, `zahlbed` | | |
| Geräte / Werkzeug | `geraetestamm`, `geraetegruppe`, `geraetelager`, `geraetelog`, `persgeraete` | | |
| Checklisten / Protokolle | `checklisten` (2.657), `checklisteneintrag`, `checklistenname`, `kdcheck`, `protokoll` (23.964), `infoprotokoll` | | |
| System / Konfiguration | `ini`, `einstell`, `schalter`, `userrechte`, `userzuordnung`, `aktuelleuser`, `kennwort`, `dbversion`, `nummerkreis`, `nummern`, `mandant`, `abfragen*` (gespeicherte Abfragen des Programms), `reportini*`, `repliste` | | `kennwort`, `userrechte` enthalten sicherheitsrelevante Daten – **nicht auslesen/ausgeben**. |
| Herstellerintegrationen | `bosch*`, `junkers`, `vendon*`, `mareon*`, `dnweb_supplier`, `shop*` | | Schnittstellen zu Bosch, Vendon, Mareon (Marktplatz), Datanorm-Web, Shop. |

## Belegkette (Hypothese, zu verifizieren)
Adresse (`adstamm`) → Projekt (`projgrund`) → Belegkopf (`textkopf`, Art = Angebot/AB/LS/…) → Positionen (`artikel1`) → Rechnung (`rgausgang`, über `projektnr`+`textnr`).
Service: Anlage (`anlagen`) → Serviceauftrag (`kd`) → Material (`material`) + Zeit (`zeiterfassung.kdauftrag`) → Rechnung (`kd.rgnr` → `rgausgang.rgnummer`).

## Statuscodes & Enumerationen
_TODO: Werte von `textkopf.art`, `projgrund.status`, `rgausgang.status`/`rechnungsart`, `kd.status` per `SELECT status, COUNT(*) … GROUP BY` ermitteln und gegen Handbuch abgleichen._

## Fallstricke
- Immer `mandant` prüfen (vermutet: Mandantentrennung in derselben Tabelle).
- Löschkennzeichen (`loeschen`, `schloss`, `ausgelagert`) beachten – noch verifizieren.
- Stornierte/Teilrechnungen (`teilleistung`, `kumulierend`) nicht doppelt summieren.
- Keine FKs: Joins immer über Konvention prüfen und Zeilenzahl vor/nach dem Join vergleichen.
- Personenbezogene Daten in `adstamm`, `personal` (u.a. Sozialversicherungsnr., Geburtsdatum), `kennwort` nicht in Auswertungen/Chats ausgeben.

## Offene Fragen an den Fachanwender
1. Wo liegt der Artikelstamm (Tabelle oder `.mdb`-Katalog)?
2. Bedeutung von `textkopf.art` – Liste der Belegarten.
3. Wie werden Kunden vs. Lieferanten in `adstamm` unterschieden?
4. Rolle der Spalten `tkzue*`/`tkzzu*`/`externenr`/`filialnr`.
