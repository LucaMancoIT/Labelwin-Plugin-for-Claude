# 5.1 Preislisten ausgeben / drucken

Pfad: Artikelstammdaten > Katalog [10] > 5. Drucken > 5.1 Preislisten ausgeben / drucken
Quelle: handbuch/5_1_preislisten_ausgeben___drucken.htm

|

5.1 Preislisten ausgeben / drucken

Sie gelangen in die Maske über den Menüpunkt <Drucken> <Preislisten ausgeben / Drucken

[Bild]

Bild: Preislisten

Im obigen Bild haben wir etwas gemogelt, damit wir Ihnen alle Felder anzeigen können.

[Bild]

1 Auswahlkriterium: Wählen Sie hier aus, welche Artikel auf der Preisliste gedruckt werden sollen. Je nach Auswahl erscheint das Feld 2 oder 3.

[Bild]

2 Von / Bis: Dieses Feld ist nur sichtbar, wenn Sie im Bereich des Auswahlkriteriums ‚Von / bis Artikelnummer’ oder ‚Von / bis eigenes Suchw.’ Wählen.

[Bild]

3 Liste: Dieses Feld ist nur sichtbar, wenn Sie im Bereich des Auswahlkriteriums ‚Beginn Artikelnummer’, ‚Suchwort Anfang’, ‚Rabattgruppen’ oder ‚Warengruppen’ wählen. Je nach Auswahl müssen Sie hier einen entsprechenden Eintrag machen.

[Bild]

4 Weitere Eingrenzungen: Über diese Auswahl können Sie weitere Eingrenzungen wählen.

5 Ausgabeform: An dieser Stelle entscheiden Sie, wie die Preisliste ausgegeben werden soll.

Drucken: Mit Hilfe dieser Funktion können Sie Artikelkataloge ausdrucken. Dies wird sicherlich nur bei selbst erfassten Katalogen zum Einsatz kommen. Über verschiedene Auswahlkriterien können Sie die Liste auf bestimmte Artikelgruppen begrenzen. Bei der Druckausgabe greift das Programm wie immer auf Formulare zurück, die mit dem Crystal-Report erstellt worden sind. Wenn Sie den Report besitzen, können Sie die Formulare selbst verändern.

Standardmäßig haben wir folgende Formulare mitgeliefert:

|

PLBRUTTO

|

Preisliste Brutto

|

PLETIBRU

|

Etiketten mit Brutto-Preis mit Strichcode

|

PLETIOP

|

Etiketten ohne Preis mit Strichcode

|

PLNETTO1

|

Preisliste Netto 1

|

PLNETTO2

|

Preisliste Netto 2

|

PLSWBRUT

|

Preisliste Brutto sortiert nach Suchwort

|

PLSWNET1

|

Preisliste Netto sortiert nach Suchwort

|

PLVK1

|

Preisliste Verkauf 1

|

PLVK2

|

Preisliste Verkauf 2

|

PLMAP

|

Preisliste mit allen Preisen

Tabelle: Liste der Preislistenformulare

Neben der Druckausgabe können die Daten auf in 3 Schnittstellen-Dateien ausgelagert werden.

[Bild]

Ascii-Datei: Hier können die Artikel in eine so genannte ASCII-Datei ausge-geben werden, um sie mit einem beliebigen Texteditor weiterverarbeiten zu können.

Das Programm benötigt dazu eine Vorlagendatei, die im Verzeichnis \labelwin\report muss und die Extension .k2e haben muss. Standardmäßig liefert Label keine Vorlage aus. Die Datei kann z.B. so aussehen:

[VORLAGE]

1 = artnr

2 = kurztext

3 = brutto

4 = netto1

Es müssen jeweils die Feldname aus der Access-Datenbank verwendet werden. Während bei obigem Beispiel der komplette Kurztext ausgegeben wird, kann man über die Schlüsselworte Kurztext1 und Kurztext2 jeweils die erste und zweite Kurztextzeile ausgegeben werden. Die Zahlen vor den Feldnamen müssen zwingend fortlaufend sein.

Als Ergebnis wird eine Datei mit Semikolon als Trennzeichen in dieser Form ausgegeben:

ARTNR;KURZTEXT;BRUTTO;NETTO1

7S-A;Geiger Flachkollektor Sunrise Standard 7S-A ;1095;711,75

1K-3;Aufdachmontage-Set für ersten Kollektor;190;123,5

2K-6;Aufdachmontage-Set für weitere Kollektoren ;146;94,9

Labelright-Schnittstelle: Die Ausgabe läuft genauso ab, wie vorstehend bei der Ascii-Datei beschrieben. Hier handelt es sich um die Übergabe zu einem Etikettenprogramm, das mit uns nichts zu tun hat. Die Namensgebung ist zufällig. Für dieses Programm werden die Umlaute in ue usw. umgewandelt.

[Bild]

UGS-Datei: Eine UGS-Datei enthält nur eine Menge und eine Artikelnummer. Mit Hilfe dieser Dateien werden von einigen Programmen Daten übergeben, die Labelwin zum Artikelaufruf für ein Dokument verwendet. Bei der Übernahme einer UGS-Datei werden alle dort hinterlegten Artikelnummern automatisch hintereinander aufgerufen. An dieser Stelle wurde die Ausgabe als UGS-Datei programmiert um alle Artikel eines Kataloges (oder diejenigen gemäß der obigen Auswahl) in ein Dokument zu bekommen. Dieses Dokument kann dann für die Druckausgabe auf Etiketten oder zur Lagereinrichtung genutzt werden.

Die UGS-Datei wird standardmäßig mit dem Namen Kata, gefolgt von der internen Nummer gespeichert.

Zur Übernahme lesen Sie bitte im Kapitel Datenübernahme.

[Bild]

6 Ok: Durch Betätigen dieses Knopfes wird die entsprechende Ausgabeform gestartet.

[Bild]

7 Abbruch: Durch Betätigen dieses Knopfes wird die Maske geschlossen.
