# Serienbriefe mit Word

Pfad: Dokumentenbearbeitung > Textverarbeitung (Word), E-Mail [17] > Serienbriefe mit Word
Quelle: handbuch/serienbriefe_mit_word.htm

|

Serienbriefe mit Word

|

Hinweis: Labelwin beinhaltet auch einen eigenen Briefeditor mit dem man Serienbriefe ohne Fremdprogramm (wie z.B. MS-Word) erstellen kann. Allerdings möchten wir den Weg hier nicht weiter beschreiben, da er nicht mehr zeitgemäß ist. Der Labelwin eigene Briefeditor kennt keine Formatierungen (fett etc.), so dass das Ergebnis des Ausdrucks nicht mehr den heutigen optischen Anforderungen entspricht.

Das Schreiben von Serienbriefen in Labelwin erfolgt in Zusammenarbeit mit einer externenen Textverarbeitung, z.B. MS Word. Es sind drei Schritte erforderlich:

1. Adressen selektieren (in Label)

2. Serienbrief erstellen (in MS Word)

3. Serienbrief und selektierte Adressen zusammenführen und drucken (in MS Word)

1. Adressen selektieren

Es gibt zwei Wege Adressdaten aus Label für einen Word Serienbrief zu generieren:

1. Erstellen einer Word Steuerdatei

2. Excel Export einer Adressselektion

Wir empfehlen übrigens den Excel Export.

Variante 1: Word Steuerdatei

|

Um eine Worsteuerdatei für Serienbriefe zu erzeugen, wählen Sie im Modul ADRESSEN den Menüpunkt <Optionen> <Selektieren>. Es erscheint nebenstehende Maske.

Wählen Sie unter Ausgabe in ‚Word Steuerdatei‘ und ändern ggf. das Ziel für die Steuerdatei. Da es an sich egal ist, in welchem Pfad die Datei mit den selektierten Adressen liegt, lassen Sie am besten unsere Vorgabe stehen. Über den Knopf ‚Durchsuchen‘ können Sie auch einen bestimmten (bereits vorhandenen) Dateinamen anklicken.

Man sollte sich unbedingt den Pfad der Steuerdatei merken (hier c:\labelwin\stapel\) da man diesen später benötigt, um die erzeugte Datei in den Word Serienbrief als Datenquelle einzulesen.

Die Vorlage der Steuerdatei muss normalerweise nicht geändert werden, da die Label Vorgabe "Adresteu.txt" bereits alle wichtigen Adressfelder enthält.

In der Regel sollen nicht alle Adressen an Word übergeben werden, sondern nur solche mit bestimmten Merkmalen. Bitte lesen Sie im Kapitel Adressen selektieren nach, wie mit der Karteikarte ‚Selektion‘ Adressen mit bestimmten Merkmalen herausgefiltert werden können.

Sobald alles richtig eingestellt ist, wählen Sie ‚Ok / Ausgeben‘, um die Adressliste zu erzeugen. In diesem Beispiel liegt dann eine Datei mit allen selektierten Adressen unter C:\LABELWIN\STAPEL\SEL-LIST.TXT vor.

|

[Bild]

Bild: Adressen selektieren

Variante 2: Excel Export

|

Der Export von selektierten Label Adressen nach Excel funktioniert ähnlich der oben beschriebenen Methode. Auch bei dieser Variante müssen auf dem Reiter "Selektion" die gewünschten Selektionszeilen erfasst werden.

Der entscheidende Unterschied bei dieser Verfahrensweise ist, dass auf dem "Ausgabe"-Reiter die "Bildschirmtabelle" angewählt wird. Geht man nun auf "Ok Ausgeben", wird eine Adressliste auf dem Bildschirm angezeigt.

|

[Bild]

|

Die angezeigten Spalten der Selektionsausgabe lassen sich Ihren Bedürfnissen entsprechend anpassen. Gehen Sie dazu über den Menüpunkt "Spalte" und hängen eine Spalte an oder fügen eine ein. Per Rechtsklick auf die neue leere Spalte können Sie mittels der "Spalten Eigenschaften" bestimmen mit welchem Feld die Spalte gefüllt werden soll.

Die von Ihnen erzeugte Tabellenstruktur können Sie über den Menüpunkt "Tabellen" abspeichern.

Achtung: Sollte Ihre Labelwin Installation mit einem SQL-Server betrieben werden, ist zu beachten, dass die Spalten "Briefanrede" nicht verwendet werden können. Wird eine dieser Spalten für Ihren Serienbrief benötigt, so müssten Sie bitte Variante 1 "Word Steuerdatei" verwenden.

|

[Bild]

|

Die Adressliste übergeben Sie nun an Excel. Dies geschieht über die Schaltfläche "Excel Tabelle". Sie werden aufgefordert einen Namen zu vergeben. Die generierte TXT Datei muss anschließend in Excel geöffnet werden. Es erfolgt direkt eine Abfrage, die mit Ja zu bestätigen ist.

Excel startet automatisch mit einem neuen Excel Dokument, die Ihre selektierten Adressdaten enthält. Sie können nun noch Änderungen vornehmen. Speichen Sie zum Abschluß die Excel Tabelle und merken sich den Pfad und Dateinamen.

|

[Bild]

2.+3. Serienbrief erstellen und mit selektierte Adressen zusammenführen und drucken

Wie Serienbriefe erstellt werden, hängt von der genutzten Textverarbeitung und deren Version ab. Microsoft hat in der Vergangenheit oft die Menüpunkte geändert, so dass wir über die Handhabung in Word keine zuverlässigen Aussagen treffen können. Es ist eigentlich auch nicht unser Betreuungsbereich. In den nächsten Unterkapiteln haben wir aber mal beispielhaft die Handhabung in MS Word 2007 und 2010 beschrieben.
