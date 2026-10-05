# Version 4.66 (November 2015)

Pfad: Updatetexte (bisher) > Update 2016 > Version 4.66 (November 2015)
Quelle: handbuch/version_4_66__november_2015_.htm

|

Version 4.66 (November 2015)

Versionswechsel auf 4.66 - Änderungen November 2015

Kundendienst, Menüpunkte für Schnittstellen geändert

Die Menüpunkte zur Übergabe an und Einlesen von diversen Programmen war durch die vielen Möglichkeiten unter dem Hauptpunkt ‚Optionen‘ mittlerweile unübersichtlich geworden. Es gibt deshalb einen neuen Haupt-Menüpunkt Export/Import, unter dem alles zu finden ist, was mit mobilen Lösungen zu tun hat.

KdMobil, Priorität bei zurück gekommenen Aufträgen und Folgearbeiten

Um die zurückgekommenen Aufträge besonders deutlich darzustellen, können Sie nun die Priorität umsetzen lassen. Damit wird die ursprüngliche Priorität des Auftrages überschrieben, aber sie wird in die Anmerkung des KD-Auftrages geschrieben.

Folgearbeiten: Mit einer weiteren, anderen Priorität können Sie Aufträge mit erforderlichen Folgearbeiten kennzeichnen. Wenn bei einem Auftrag Folgearbeiten im Büro erforderlich sind, wird auf der Laptop-Seite das Merkmal 'Büro-Folgearbeiten erforderlich ' gesetzt und der Begründungstext in die Büroinfo geschrieben.

Bei der entsprechenden Farbgebung der Prioritäten kann ein solcher Auftrag dann in einer grellen Farbe gezeigt werden.

Die Einrichtung erfolgt im Modul Einstellungen unter den Menüpunkten <Programmbereiche>, <Kundendienst>, <Laptop Grundeinstellungen>.

Kundendienstauswertung, Lohn aus Eingangsrechnungen

In der Auswertung werden nun auch die Stunden und Lohnkosten aus Eingangsrechnungen (Leiharbeiter) berücksichtigt. In der V4-Version werden die Stunden einfach aufaddiert, in der V5-Version in getrennten Feldern dargestellt. Der Deckungsbeitrag je Std. wird aber standardmäßig nur mit den Stunden aus der Zeitwirtschaft berechnet, weil der üblicherweise nur mit den Stunden der eigenen Mitarbeiter berechnet wird. Wenn Sie bei der Berechnung auch die Stunden aus den Eingangsrechnungen berücksichtigen wollen, können Sie dazu einen Schalter setzen. Der Schalter findet sich im Modul Einstellungen unter den Menüpunkten <Programmbereiche>, <Kundendienst>, <Grundeinstellungen> auf der Karteiseite 'Allgemein".

Schnittstelle IDS-Shop mit Vorgabe um EK-Preise nicht aus dem Shop zu nehmen

Bisher war die Vorgabe bei der Übernahme von Artikel aus dem Shopsystem, dass die Einkaufspreise vom Shop in das gerade aktive Dokument übernommen wurden. Da manche Lieferanten im Shopsystem jedoch nicht die richtigen (individuell vereinbarten) Preise führen, konnten damit die korrekten Preise vernichtet werden. Nun kann man je Shopsystem festlegen, ob der Schalter für die Übernahme der EK-Preise als Vorgabe gesetzt oder nicht gesetzt ist. Die Einrichtung erfolgt im Modul Adressen nach Aufruf der Lieferantenadresse im Menü unter Bearbeiten, Stammdaten UGL (oder mit Strg O)

Folien auf PDF auch ohne gekauftes Scanarchiv

Kunden, die das Modul Scanarchiv nicht erworben hatten, konnten keine Folien verwenden, weil ihnen die Einstellung des Hilfsprogramms pdftk.exe fehlte. Die Einträge können nun auch über die Menüpunkte <Programmbereiche>, <Druckausgabe>, <Pdf-Archiv> erfolgen.

Dokumenten / Bestellzerlegung nach Arbeitsbereichen

Diese neue Option macht nur Sinn, wenn Sie Arbeitsbereiche ja nach Baufortschritt definieren und die Baustelle eine gewisse Laufzeit hat. Nach der Zerlegung kann dann das Material für die einzelnen Bauabschnitte zeitlich passend bestellt werden. .

[Bild]

Hinterlegung von Wartungsmaterial immer in ‚neuer‘ Maske

Bisher wurde durch einen Schalter festgelegt, ob eine einfache Maske für die Hinterlegung von Artikel genutzt wurde oder die hier abgebildete. Wir haben nun die alte Maske entfernt, so dass nun alle Anwender die umfangreicheren Möglichkeiten nutzen können. Über den Hintergrund der Materialhinterlegung lesen Sie im LabelWiki unter dem Stichwort Abrechnungsmethoden von Wartungen

[Bild]

Suchfunktion in UGL-Dateien

Da immer mehr UGL-Dateien zum Einsatz kommen, wird es leicht unübersichtlich. Über eine Suchfunktion mit Strg F kann nun in den Dateien gesucht werden. Dies ist z.B. sinnvoll, wenn eine bestimmte UGL-Rechnung eingebucht werden soll.

Farbanzeige der Bereitschaftszeit frei festlegbar (nur V5-Version)

In der Kalenderansicht kann nun die Farbe für die Bereitschaft frei definiert werden. Wer es nicht weiß: Bereitschaftszeiten können in der Maske der Fehlzeiteneingabe eingetragen werden.

Die Farbe wird über das Menü oder einen Klick auf die Legendenanzeige geändert.

[Bild]

Katalogmodul, Import von CSV-Dateien überarbeitet

Manche Lieferanten können keine Datanorm liefern. Deshalb gibt es im Katalogmodul schon lange die Möglichkeit, beliebige CSV-Dateien einzulesen. Nun gibt es die Möglichkeit, als Wiedererkennungsmerkmal auch die EAN / GTin Nummer oder das Herstellerkennzeichen und Kürzel zu verwenden.

Eingangslieferscheine einscannen mit nachträglichen Seiten möglich

Bisher gab es keine Möglichkeit, im Nachhinein weitere Blätter hinter einen bereits gescannten Eingangslieferschein anzuhängen. Dazu muss der Eingangslieferschein über die Projektverwaltung markiert sein und mit der F12-Taste ein Scan ausgelöst werden. Voraussetzung ist aber die Einrichtung vom Programm pdftk.exe. Ohne diese Einrichtung können im Scanarchiv überhaupt keine Seiten an ein vorhandenes Pdf angehängt werden.
