# 4.2 Nummernkreise

Pfad: Einrichtungsarbeiten > Einstellungen [14] > 4. Grundeinstellungen > 4.2 Nummernkreise
Quelle: handbuch/4_2_nummernkreise.htm

|

4.2 Nummernkreise

In dieser Maske werden die Nummernkreise für die Ausdrucke festgelegt. Die hier festgelegten Werte gelten global für die ganze Firma.

Bei einigen Nummernkreisen bietet das Programm die Möglichkeit, die Werte einzeln hoch zu zählen.

[Bild]

Bild: Grundeinstellungen – Nummernkreise

[Bild]

1 Projektspezifische Nummernkreise: In diesem Feld legen Sie fest, ob die Nummernkreise für Angebote, Lieferscheine, Bestellungen, Auftragsbestätigungen und Preisanfragen für jedes Projekt separat gezählt werden sollen, oder über alle Projekte hinweg. Bei der projektspezifischen Nummernvergabe bekommt das erste Angebot des Projektes die Nummer 1, das nächste die Nummer 2 usw.

[Bild]

2 Abteilungsbezogene Nummernkreise: Durch Aktivieren dieses Feldes können Sie die Felder 8 – 16 pro Abteilung mit einem eigenen Nummernkreis versehen. Die Abteilung muss entsprechend gewählt werden. Eine Auswahlliste der Abteilungen erscheint, sobald das Feld aktiviert ist.

[Bild]

3 Projektnummer: Hier haben Sie die Möglichkeit, nach bestimmten Regeln eine Projektnummer zu vergeben. Für Labelwin ist die Projektnummer relativ gleichgültig. Die einzigen Einschränkungen sind, dass sie einmalig sein müssen und keine Sonderzeichen enthalten dürfen.

Es gibt jedoch Kunden, die in der Nummer eine Auswertungslogik hinterlegen möchten. In Labelwin geschieht das über die frei zu gestaltenden Zusatzfelder im Datenblatt.

Ein weiterer Grund für eine Logik in der Projektnummer ist, dass die Mitarbeiter an der Nummer sofort erkennen sollen, zu welchem Bereich und ggf. zu welchem Mandanten das Projekt gehört.

Die Projektnummer kann nach eigenen Regeln automatisiert vergeben werden.

Nummer fortlaufend: Die erste und verbreiteteste ist eine Nummer, die je Projekt und ggf. auch Mandanten übergreifend hochgezählt wird.

Nummer je Abteilung zählen: Diese Methode ist nur anwendbar, wenn Sie mit Abteilungen arbeiten. Bei diesen müssen dann ein Projektkürzel und die jeweils letzte verwendete Nummer eingetragen sein. Je nach gewählter Abteilung wird dann das Projektkürzel und die nächste abteilungslaufende Nummer verwendet. Wie die Projektnummer gestaltet wird, hängt auch vom verwendeten Schema ab.

Nummer je Auswahl zählen: Diese Methode ist nur anwendbar, wenn Sie eine eigene Auswahl möglicher Projektkennzeichen festgelegt haben. Dies geschieht mit dem Knopf 'Auswahl'. Wenn Sie bei einem Auswahlpunkt die letzte Nummer hinterlegen - also jene Nummer ab der hochgezählt werden soll, dann wird für jede Auswahl ein eigener Nummernkreis geführt.

Auch feste Buchstaben oder Zahlen können im Schema eingetragen werden. Der bisherige Standard ist vorgegeben.

[Bild]

Für einige Anwender ist sicherlich auf der Auswahlkreis interessant. Zur Erfassung betätigen Sie den Knopf ‚Auswahlkreis‘. Bei der Anlage eines neuen Projekts werden Sie dann gefragt, in welchem Bereich das Projekt angelegt werden soll. Hier im Beispiel also die Wahl zwischen Dauerprojekten und Kleinaufträgen. Je nach Wahl wird dann das Kürzel genommen und ggf. auch der dort festgelegte Nummernkreis.

[Bild]

4 Letzte Nummer: An dieser Stelle geben Sie die letzte laufende Projektnummer ein. Bei der Vergabe setzt das Programm später automatisch das Jahr und einen Bindestrich vor die Nummer.

[Bild]

5 Schema: Mit dem Schema kann eine generierte Projektnummer erzeugt werden. In dem Schema kann eines der folgenden Schlüsselworte enthalten sein:

$jahr$ = die letzten beiden Stellen des aktuellen Jahres

$nummer$ = nächste laufende Nummer des Projektes.

$abt$ = Projektkürzel beim Arbeiten mit Abteilungen

$auswahl$ = bei einer Auswahl hinterlegtes Kürzel

Beispiele für Schemata:

$jahr$ - $nummer$ daraus entsteht z.B. 12-1234 (wobei 1233 die letze verwendete Nummer war)

$abt$ - $nummer$ bei einem Abteilungskürzel abc entsteht z.B. abc-1234

$jahr$ $abt$ - $nummer$ bei einem Abteilungskürzel abc entsteht z.B. 12abc-1234

M1 - $jahr$ - $nummer$ daraus entsteht z.B. M1-12-1234

$auswahl$ - $jahr$- $nummer$ wenn in der Auswahl ein Eintrag mit Kürzel 120 gewählt wird, entsteht z.B. 120-12.-1234

[Bild]

6 Debitorennummer: Bei der Neuanlage von Adressen kann über die Eingabe einer 0 vom Programm die nächste Debitorennummer vorgeschlagen werden. An dieser Stelle legen Sie fest, welches die letzte Debitorennummer war. Bitte beachten Sie, dass das Programm bei der Adresseingabe keine Prüfung auf bereits vorhandene Debitorennummern durchführt. Wegen Debitorennummern für "diverse" Kunden haben wir die Mehrfachvergabe zugelassen.

[Bild]

7 Kreditorennummer: Hier gilt das gleiche wie bei der Debitorennummer.

[Bild]

8 Wartungsvertrag: Der hier hinterlegte Nummernkreis kommt dann zum Einsatz, wenn im Erfassmodul der Menüpunkt ‚Neuer Vertrag‘ angewählt wird.

[Bild]

9 Eingangsrechnungen: Dieser Zähler ist der interne Eingangsrechnungszähler. Er ist unabhängig von der Rechnungsnummer Ihres Großhändlers zu sehen. Wenn Sie die Belege kontinuierlich einbuchen, so können Sie die jeweils vom Programm vergebene Eingangsrechnungsnummer auf der Rechnung vermerken.

[Bild]

10 Rechnungsnummer: Geben Sie hier die letzte Rechnungsnummer ein, ab der das Programm automatisch weiter hoch zählen soll. Bitte beachten Sie, dass die Rechnungsnummer nicht automatisch das Jahr enthält. Wenn gewünscht, so müssten Sie 20120000 eingeben, damit Sie im Jahr 2012 9999 Rechnungen schreiben können.

[Bild]

11 Kundendienstauftrag: An dieser Stelle geben Sie die letzte Auftragsnummer ein. Bitte beachten Sie, dass das Programm automatisch die Jahreszahl mit einem Bindestrich vor die Kundendienstauftragsnummer voranstellt.

[Bild]

12 KDA-Nr. Folgejahr: Normalerweise setzen Sie zum Jahresanfang den Nummernkreis wieder auf 0 (oder eine andere kleine Zahl) zurück.

Wenn Sie aber am Ende eines Jahres (z.B. im Dezember), über das Modul Selektion schon Wartungsaufträge für das kommende Jahr schreiben, können Sie mit diesem Feld dafür sorgen, dass schon die Nummern des nächsten Jahres benutzt werden, z.B. 11-00001.

Beim Erstellen der Kundendienstaufträge für Wartungstermine haben Sie ein Ankreuzfeld, um die Aufträge mit dem Nummernkreis des Folgejahres anzulegen.

|

Wichtig: Am Jahresanfang müssen Sie aber dennoch die Startnummer für KD-Aufträge des aktuellen Jahres per Hand auf den richtigen Wert setzen!

[Bild]

13 Eigener Nummernkreis für Abschlags-rechnungen: Durch diesen Schalter bekommen die Abschlagsrechnungen einen anderen Nummernkreis. Wir halten dies zwar für überflüssig, aber einige Steuerberater wollten es so.

|

ACHTUNG! Die Nummernkreise für Rechnungen und Abschlagsrechnungen müssen weit auseinander liegen! Überschneidungen dürfen auf keinen Fall auftreten.

[Bild]

14 Eigener Nummernkeis für Null-Rechnungen: Durch diesen Schalten bekommen Null-Rechnungen einen anderen Nummernkreis. Wenn Sie diese Option wählen, müssen die Nummernkreise für Rechnungen, Abschlagsrechnungen und Null-Rechnungen weit auseinander liegen. Es darf keine Überschneidungen geben.

[Bild]

15 Bedarfsmeldungen mit Nummer: Wenn Sie dieses Feld aktivieren, wird bei jeder ‚Bedarfsanforderung' sofort eine Nummer vergeben. Anders als bei Rechnungen, Angeboten und Bestellungen wird die Nummer schon bei der Anlage einer Bedarfsanforderung bestimmt, da diese in der Regel nicht gedruckt werden.

Eine Bedarfsanforderung dient dazu, dass der Bauleiter seine benötigten Materialien zusammenstellen kann, aber nicht selbst bestellt.

[Bild]

16 Angebotsnummer: Dieses Feld ist nur sichtbar, wenn Sie keine projektspezifischen Nummernkreise geschaltet haben. Geben Sie hier die letzte Nummer ein, mit der das Programm weiterzählen soll. Wenn Sie die Jahreszahl mit in der Angebotsnummer haben möchten und zum Jahresanfang den Nummernkreis wieder auf 0 setzen, müssen Sie an dieser Stelle 20120000 eingeben. Sie können dann im Jahr 9999 Angebote schreiben.

[Bild]

17 Lieferscheine: Die Eingabe ist nur dann aktiv, wenn Sie keine projektspezifischen Nummernkreise geschaltet haben Geben Sie hier die letzte Nummer ein, mit der das Programm weiterzählen soll. Wenn Sie die Jahreszahl mit in der Lieferscheinnummer haben möchten und zum Jahresanfang den Nummernkreis wieder auf 0 setzen, müssen Sie an dieser Stelle 20120000 eingeben. Sie können dann im Jahr 9999 Lieferscheine ausstellen.

[Bild]

18 Bestellungen: Dieses Feld ist nicht sichtbar, wenn Sie keine projektspezifischen Nummernkreise geschaltet haben. Geben Sie an dieser Stelle die letzte Bestellnummer ein. Die Nummer wird vom Programm unverändert angewendet. Wenn Sie die Jahreszahl mit in die Nummer hinein haben wollen, so sollten Sie mit 2012 beginnen und dann die entsprechenden Ziffern, mit der der Nummernkreis zählen soll.

[Bild]

19 Auftragsbestätigung: Dieses Feld ist nur sichtbar, wenn Sie keine projektspezifischen Nummernkreise geschaltet haben. Geben Sie hier die letzte Nummer ein, mit der das Programm weiterzählen soll. Wenn Sie die Jahreszahl mit in der Auftragsbestätigung haben möchten und zum Jahresanfang den Nummernkreis wieder auf 0 setzen, müssen Sie an dieser Stelle 20120000 eingeben. Sie können dann im Jahr 9999 Auftragsbestätigungen schreiben.

[Bild]

20 Preisanfragen: Die Eingabe ist nur dann aktiv, wenn Sie keine projektspezifischen Nummernkreise geschaltet haben. Geben Sie an dieser Stelle die letzte Preisanfragennummer ein. Die Nummer wird vom Programm unverändert angewendet. Wenn Sie die Jahreszahl mit in die Nummer hinein haben wollen, so sollten Sie mit 2012 beginnen und dann die entsprechenden Ziffern, mit der der Nummernkreis zählen soll.

[Bild]

21 Ok: Durch Betätigen dieses Knopfes werden die vorgenommenen Einstellungen abgespeichert.

[Bild]

22 Abbruch: Durch Betätigen dieses Knopfes werden alle ggf. vorgenommenen Änderungen verworfen und die bisherigen Nummernkreise bleiben erhalten.
