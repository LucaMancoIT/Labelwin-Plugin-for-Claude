# 5. Fehlerbehebung / Struktur einer Scannerdatei

Pfad: Materialwirtschaft > Scannerverarbeitung [Modul] > 5. Fehlerbehebung / Struktur einer Scannerdatei
Quelle: handbuch/5__fehlerbehebung___struktur_einer_scannerdatei.htm

|

5. Fehlerbehebung / Struktur einer Scannerdatei

Diese Beschreibung ist für die Insider gedacht, falls einmal Probleme auftreten sollten.

Die Scannerdatei wird üblicherweise zunächst mit dem Namen STRICH.TXT im Verzeichnis Labelwin abgelegt. Nach dem Scannen wird diese geprüft und wenn sie in Ordnung ist in einzelne UGS-Dateien zerlegt. Falls die Prüfung Fehler findet, fällt die Zerlegung komplett aus. Solche Fehler sind meistens die vergessene Projektnummer am Anfang der Scannliste. Über den Knopf ‚Daten bearbeiten’ wird die Datei mit Notepad in Bearbeitung genommen und man ggf. die fehlende Nummer per Hand eintragen. Über die Anwahl ‚in UGS verteilen’ und ‚Übertragung starten’ kann dann die Verteilung nachträglich gestartet werden.

Für den Fall, dass die Strich.txt komplett zerstört oder warum auch immer verloren gegangen ist, werden alle Daten zusätzlich in der Datei SCANNPROT.TX im Verzeichnis UGS abgelegt. Durch Ausschneiden des passenden Bereiches kann ggf. die Datei Strich.txt neu aufgebaut werden.

Aufbau

#96-50002 Zeile 1

02.HKZUB Zeile 2

$96$50002 Zeile 3

02.HKZUB Zeile 4

X0533092 Zeile 5

-$LAGER Zeile 6

02.09857 Zeile 7

3 Zeile 8

*0000733 Zeile 9

06.34676 Zeile 10

Der Text Zeile 1 usw. ist nicht Bestandteil der Datei, sondern wird nur für die folgende Erklärung benötigt.

Zeile 1: Projektnummer 96-5002, per Hand eingegeben, da ein – Zeichen nicht per Strichcode zu drucken ist. Es könnte auch ein Semikolon oder $.Zeichen vor die Nummer gestellt werden.

Zeile 2: Artikel hkzub aus Katalog mit interner Nr. 02

Zeile 3: Projektnummer 96-50002 gescannt, der Bindestrich kann nicht als Strichcode gedruckt werden und wird bei der Verteilung auf UGS-Dateien automatisch umgesetzt.

Zeile 4: Artikelnummer

Zeile 5: Artikel X0533092 ohne internes Katalogkennzeichen

Zeile 6: getipptes Minus– Zeichen, ohne anschließendes Enter, gescannte Projektnummer LAGER, die folgenden Artikel bis zur nächsten Projekt oder Auftragsnummer werden negativ gebucht

Zeile 7: Artikelnummer

Zeile 8: Menge 3 zu vorigem Artikel

Zeile 9: Kundendienst-Auftragsnummer, erkennbar am * - Zeichen

Zeile 10: Artikelnummer

Aus obigem Beispiel entstehen 3 UGS-Dateien:

96-50002.ugs mit 1 x HKZUB Katalog 2

1 x HKZUB Katalog 2

1 x X0533092

Lager.ugs mit 3 x 09857 Katalog 2

00000733.ugs mit 1 x 34676 Katalog 6
