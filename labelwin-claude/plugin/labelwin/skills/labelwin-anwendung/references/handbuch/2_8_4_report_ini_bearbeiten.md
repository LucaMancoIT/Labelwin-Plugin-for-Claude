# 2.8.4 Report.ini bearbeiten

Pfad: Einrichtungsarbeiten > Einstellungen [14] > 2. Programmbereiche > 2.8 Druckausgabe > 2.8.4 Report.ini bearbeiten
Quelle: handbuch/2_8_4_report_ini_bearbeiten.htm

|

2.8.4 Report.ini bearbeiten

Bei der REPORT.INI handelt es sich um eine Steuerdatei, in der nahezu alle Druckformulare abgelegt sind. Die Druckformulare sind in dem Unterverzeichnis LABELWIN\REPORT abgelegt und haben häufig etwas merkwürdige Namen. An der Oberfläche bieten wir statt der Namen in der Regel einen Beschreibungstext zur Formularauswahl an. In der im Folgenden beschriebenen Maske können die Beschreibungstexte verändert werden. Weiter sind hier einige Einstellungen möglich, die Ihre Betreuer in der Regel vornehmen sollten. Es würde zu weit führen, hier jede Möglichkeit zu erläutern.

In der Auswahlliste Druckart legen Sie fest, in welchem Druckausgabebereich Sie die Formulare betrachten bzw. verändern möchten. Durch das Markieren einer Zeile in der Tabelle wird diese Eintragung in die unteren Datenfelder eingetragen. Hier kann ggf. eine Änderung vorgenommen werden.

[Bild]

Bild: Report.ini bearbeiten

[Bild]

1 Druckart: Hier finden Sie eine Auswahlliste der verschiedenen Druckarten.

[Bild]

2 Liste der hinterlegten Reports: In dieser Liste werden Ihnen die Einträge angezeigt, die der ausgewählten Druckart hinterlegt sind.

[Bild]

3 Laufende Nr.: Hier wird angezeigt, an welcher Stelle in der Auswahlliste das entsprechende Formular angeboten wird. Beachten Sie bitte, dass Lücken in der Nummerierung nicht erlaubt sind.

[Bild]

4 Reportname: Hier handelt es sich um den Dateinamen ohne die Endung .RPT in dem das Formular auf der Festplatte in Verzeichnis LABELWIN\REPORT abgelegt ist.

[Bild]

5 Beschreibung: Dieser Text wird bei der Auswahl von Formularen angeboten. Formulieren Sie in möglichst aussagekräftig, damit auch neue Mitarbeiter auf Anhieb die Bedeutung dieses Formulars verstehen.

[Bild]

6 Druckbreite: Dieses Feld sollten Sie in der Regel auf 40 Zeichen stehen lassen. Die Datanorm basiert auf einer Zeilenbreite von 40 Buchstaben. Wenn Sie hier einen anderen Wert einsetzen, so wird die Druckausgabe evtl. etwas merkwürdig aussehen. Lediglich bei der Druckausgabe von GAEB-LV´s haben wir die Druckbreite auf 55 Zeichen festgelegt. GAEB-Texte werden in der Regel in dieser Zeichenbreite übergeben.

[Bild]

7 Name des Folge-reports: Beim Drucken von Rechnungen, Angeboten und Auftragsbestätigung ist es möglich, einen Report mit einen anderen Aufbau nachzuschalten. Diese Funktion wird von einigen unserer Kunden benutzt, um nach der eigentlichen Angebotsausgabe ein Formular für die eigene Ablage mit den Einkaufspreisen, Artikelnummer usw. auszugeben.

[Bild]

8 Reportüberschrift: In diesem Feld kann eine Vorgabe getroffen werden, welche Bezeichnung auf dem Druckformular stehen soll. Einige unserer Kunden benutzen diese Funktion, um bei Angeboten das Wort Kostenvoranschlag erscheinen zu lassen. Wenn das Feld leer ist, verwendet unser Programm die Standardvorgabe.

[Bild]

9 Felder setzen: Bei vielen Standardreports werden die hinterlegten Firmendaten aufs Papier gedruckt. Über eine Eingabe in diesem Feld ist steuerbar, ob die Felder tatsächlich ausgedruckt werden. Bitte beachten Sie, dass dies zusätzlich davon abhängig ist, ob die Datenfelder auf dem Report vorhanden sind. Durch die Eingabe von Einsen und Nullen werden die Felder sichtbar bzw. unsichtbar geschaltet. Die Reihenfolge der Einsen und Nullen entspricht der Erfassreihenfolge bei den Firmendaten. Wenn z. B. zu die Absenderzeile ausgegeben werden soll und alle anderen Kopfdaten nicht gedruckt werden sollen, weil diese bereits fest auf dem Firmenpapier stehen, so müssen als Eingabe 000000010000 eingetragen werden. Die Absenderzeile ist das 8. Feld und dementsprechend muss an der 8. Stelle eine 1 eingeben werden. Bitte denken Sie über diese Möglichkeit nicht lange nach – es lediglich für uns bei der Installation eine kleine Vereinfachung.

[Bild]

Mit Hilfe dieser Funktion und der Möglichkeit über den Menüpunkt <Programmbereiche> <Druckausgabe> <Report aktualisieren> können die Formulare häufig angepasst werden, ohne das Programm Crystal-Report zu nutzen.

[Bild]

10 Report für Titel-zusammenstellung: Wenn Sie bei einer Druckausgabe eine Titelzusammenstellung erstellen möchten, so müssen Sie hier den entsprechenden Reportnamen eintragen. Damit wird das Grundformular mit der Titelzusammenstellung verbunden. Sie müssen hier die Originaldateinamen wie TITELZU1, TITELZU2 usw. verwenden.

[Bild]

11 Papierausrichtung: Tragen Sie hier ein, ob es sich um ein Quer- oder Hochformat handelt. Standardmäßig steht hier der Eintrag auf ‚unbekannt’.

[Bild]

12 Bildergrößen: Speziell angepasste Dokumentenfor-mulare (Angebote, Rechnun-gen, etc.) können mit Bildern ausgedruckt werden. Die Voraussetzungen dafür stehen am Ende dieses Textes. Wenn keine Angaben erfolgen, werden die Bilder in der maximalen Standardgröße gedruckt (bzw. kleiner). Eingebundene Bilder werden wenn nötig verkleinert, aber nie vergrößert.

Bild unter der Positionsnummer:

Maximale Größe 100 * 100 (Breite * Höhe)

Bild unter Kurztext:

Maximale Größe 470 * 470 (Breite * Höhe)

Bild über volle Breite:

Maximale Größe 470 * 470 (Breite * Höhe)

Folgende Voraussetzungen müssen für das Ausdrucken von Bildern erfüllt sein:

1. Umstellung auf RTF und Crystal Report Version 10/XI

2. Aktivierung der Bildverarbeitung (Modul Positionserfassung, Menü Datei, Bildverarbeitung aktivieren)

3. Speziell anpasste Formulare

[Bild]

13 Report gilt für: Nutzer der Mandantenversion können die Reports mandantenabhängig unsichtbar schalten. Mit dieser Funktion können Sie entscheiden, ob der Report für alle Mandanten oder nur für einen speziellen Mandanten gelten soll. Wenn der Report nur für bestimmte Mandanten gültig ist, muss der Mandant in dem entsprechenden Feld eingetragen werden.

[Bild]

14 Report zur Druckauswahl nicht anbieten: An einigen Stellen im Programm kann man auf viele Reports zurückgreifen. Wenn Ihnen aus der Liste nur einige Reports benötigen, können Sie durch Aktivieren dieses Feldes unterbinden, dass dieser Report in der Druckausgabe in der Reportliste erscheint. Löschen würde nichts nutzen, da das Formular beim nächsten Update wieder da wäre.

[Bild]

15 Neuer Eintrag: Durch Betätigen dieses Knopfes können Sie einen neuen Eintrag vornehmen.

[Bild]

16 Eintrag löschen: Durch Betätigen dieses Knopfes können Sie einen aktiv markierten Eintrag in der Liste (Nr.2) löschen.

[Bild]

17 Eintrag speichern: Durch Betätigen dieses Knopfes wird ein neuer Eintrag oder eine Änderung in der Liste (Nr.2) gespeichert.

[Bild]

18 Änderung in Datei speichern: Erst durch Betätigen dieses Knopfes erfolgt der Eintrag in der Report.ini

[Bild]

19 Ende: Durch Betätigen dieses Knopfes wird die Maske geschlossen.
