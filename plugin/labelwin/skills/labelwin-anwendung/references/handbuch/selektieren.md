# Selektieren

Pfad: Adressverwaltung > Adressen [5] > 8. Adressen selektieren > Selektieren
Quelle: handbuch/selektieren.htm

|

Selektieren

Obwohl es sich hier um die Eingrenzung auf bestimmte Adressen handelt, wird von anderen Stellen im Handbuch immer wieder auf diese Seite verwiesen. Alle Suchfunktionen in den Stammdaten wie z.B. die Selektion von Anlagen, Wartungsverträgen, Projektstatistiken, Auftragsauswertungen usw. finden auf die gleiche Art statt. Es unterscheiden sich lediglich die Suchfelder und damit natürlich auch die Inhalte der Datenbankfelder (= Vergleichstext)

[Bild: Selektieren]

|
[Bild: 1]

Tabelle

[Bild: 1. Tabelle]

Hier erscheint die Liste der zu selektierenden Merkmale, soweit diese abgelegt worden sind. Wenn in der Tabelle keine Einträge vorhanden sind, werden alle Adressen herausgesucht.

In jeder Zeile der Tabelle wird ein Merkmal hinterlegt, dass für die erfolgreiche Suche erfüllt sein muss. Die Merkmale werden durch Bedingungen wie ‚and‘ und ‚or‘ miteinander verknüpft.

In obigem Beispiel werden nur die Adressen ausgegeben, bei denen beide Merkmale erfüllt sind – also nur die Adressen mit L am Anfang des Suchwortes und mit der Eintragung ‚Präsent‘ im Marketingschlüssel 5. (Zur Erinnerung: Die Beschriftung der Marketingschlüssel ist frei verfügbar und beim Verfasser des Handbuches mit ‚Weihnachten‘ belegt.)

Im Kapitel Selektieren von Wartungsterminen finden Sie eine kompliziertere Selektion mit der Verwendung der ODER- Verknüpfung und dem Einsatz von Klammern.

|
[Bild: 2]

Selektionszeile

[Bild: 2. Selektionszeile]

Im ersten Feld erscheint automatisch immer das Wort AND. Hierbei handelt es sich um das englische Wort für UND, mit die Merkmale verknüpft werden können. Das Wort AND bedeutet an dieser Stelle, dass die Merkmale die in jeder einzelnen Zeile formuliert sind, gleichzeitig zutreffen müssen. In der Logik wird dieses auch als UND-Verknüpfung bezeichnet. Standardmäßig schreibt unser Programm immer das Wort AND in dieses Feld. Wenn Sie es beispielsweise gegen das Wort OR auswechseln, bedeutet es, dass eines der Merkmale genügt.

Im 2. Feld können Sie ggf. Klammerzeichen unterbringen, um die Bedingungen voneinander zu trennen. Falls Sie in formaler Logik fit sind, können Sie dort auch Verknüpfungen wie NOT eintragen (negiert die Bedingung).

Im 3. Feld mit der Beschriftung Suchfeld wählen Sie aus der Liste aus, in welchem Datenfeld Sie nach bestimmten Informationen suchen wollen.

Im 4 .Feld mit der Beschriftung Operator: wählen Sie aus, ob der im Suchfeld gewählte Begriff größer, kleiner, gleich.... dem in der Spalte ‚Vergleichstext’ eingetragenen Inhalt sein soll.

Im 5. Feld mit der Beschriftung ‚Vergleichstext’: geben Sie ein, nach was Sie in dem Suchfeld suchen möchten. Bei dem Vergleichstext muss es sich um eine Information handeln, die in dem Suchfeld vorhanden oder - je nach Operator - größer, kleiner, like ist. Je nach Suchfeld kann es sich um Informationen handeln die Sie selbst frei wählen können, oder auch über Zahlen festgelegt werden. Durch Betätigen des Knopfes ‚Felddaten durchsuchen‘ wird eine Liste aller in der Datenbank vorgefundenen Inhalte gezeigt, aus der Sie einen Eintrag wählen können.

Im 6. Feld können Sie eigentlich nur geschlossene Klammern eintragen oder es leer lassen.

|
[Bild: 3]

Zeile einfügen

[Bild: 3. Zeile einfügen]

Durch Betätigen dieses Knopfes wird die aktuelle Zeile in die Tabelle eingetragen. Die Eintragung erfolgt vor der markierten Zeile (in der Regel also vor dem ‚Auswahlende‘)

|
[Bild: 4]

Zeile ändern

[Bild: 4. Zeile ändern]

Durch Betätigen dieses Knopfes wird die in der Tabelle markierte Zeile in die Eingabefelder eingetragen und kann dort verändert werden. Die gleiche Funktion erreichen Sie durch einen Doppelklick in der Tabellenzeile.

|
[Bild: 5]

Zeile löschen

[Bild: 5. Zeile löschen]

Durch Betätigen dieses Knopfes wird die in der Tabelle markierte Zeile gelöscht.

|
[Bild: 6]

Operator

[Bild: 6. Operator]

Bedeutung der einzelnen Operatoren:

|

= gleich

|

Vergleichstext muss exakt identisch mit Inhalt des Suchfeldes sein

|

> größer

|

Inhalt des Suchfeldes muss größer als der Vergleichstext sein. Dabei ist ‚größer’ neben dem Zahlenvergleich auch über die Buchstaben eines Textes definierbar. Wenn ein Buchstabe im Alphabet weiter hinten liegt, so ist er größer als dieser. Beispiel: „Berta“ ist größer als „Anton“

|

< kleiner

|

Der Inhalt des Suchfeldes muss kleiner als der Vergleichstext sein.

|

<= kleiner-gleich

|

Der Inhalt des Suchfeldes muss kleiner oder gleich dem Vergleichstext sein.

|

>= größer-gleich

|

Der Inhalt des Suchfeldes muss größer oder gleich dem Vergleichstext sein.

|

Like

|

Der Unterschied des Like-Operators zum Gleich-Operator besteht darin, dass hier im Vergleichstext sogenannte Joker verwendet werden können:

* Platzhalter für 0 oder mehr beliebige Zeichen

Beispiel: Ort LIKE Bie* liefert alle Orte, die mit ‘Bie’ anfangen

Ort LIKE *feld liefert alle Orte, die mit ´feld´enden.

Ort LIKE *ielefel* liefert alle Orte, in denen dieses

Bruchstück vorkommt.

? Platzhalter für ein beliebiges Zeichen

Beispiel: Name LIKE M?ller liefert alle ‘Müller’, ‘Möller’,

usw, aber nicht Mueller.

# Platzhalter für eine beliebige Ziffer

Beispiel: Plz LIKE 336## liefert alle Postleitzahlen, die mit 336

anfangen

[Zeichenkette] Platzhalter für ein Zeichen, dass in der Zeichenkette

enthalten ist.

Beispiel: Name LIKE M[ae]ier liefert alle

‘Maier’ und ‘Meier’, nicht aber ‘Meyer’

An dieser Stelle kann auch ein Minus-Zeichen

verwendet werden, um ‘von-bis’ auszudrücken.

Beispiel: Name LIKE [A-E]* liefert alle Kunden,

die mit einem Buchstaben zwischen A und E

beginnen.

[!Zeichenkette] Platzhalter für ein Zeichen, das nicht in der

Zeichenkette enthalten ist

Beispiel: Name LIKE Ma[!y]er liefert alle

‘Maier’, ‘Majer’, usw, nicht aber ‘Mayer’

An dieser Stelle kann ebenfalls ein Minus-Zeichen

verwendet werden, um ‘von-bis’ auszudrücken.

Beispiel: Name LIKE [!A-E]* liefert alle Kunden,

außer denen, deren Namen mit ABCD oder beginnt.

|
[Bild: 7]

Felddaten durchsuchen

[Bild: 7. Felddaten durchsuchen]

Durch Betätigen dieses Knopfes wird die Datenbank nach allen in dem entsprechenden Suchfeld vorkommenden Inhalten durchsucht und in einer Liste dargestellt. In dieser Liste kann ein Eintrag

markiert und automatisch mit dem Okay-Knopf übernommen werden. Die gleiche Funktion ist mit einem Doppelklick auf den Eintrag zu erreichen.

[Bild]

Nutzen Sie diese Funktion möglichst immer dann, wenn Sie nach einem bestimmten Inhalt mit dem Gleich Operator ( = Zeichen) suchen. Besonders interessant ist auch, dass man über diesen Weg oft falsche Eingaben sieht, die sonst nicht sichtbar geworden wären. Selbst bei der Suche mit dem Like-Operator kann man die Suche gut gebrauchen. Wählen Sie einfach einen Inhalt aus, löschen ggf. die letzen Zeichen und tragen das * Zeichen dahinter.

|
[Bild: 8]

Suchschema speichern

[Bild: 8. Suchschema speichern]

Durch Betätigen dieses Knopfes wird die aktuelle Selektion abgespeichert. Falls Sie ein gespeichertes Suchschema aktiviert haben, erfolgt die Frage, ob Sie dieses überschreiben wollen. Beantworten Sie diese Frage mit Nein, so können Sie ein neues eintragen. Im Suchschema wird neben der Selektion auch eine gewählte Sortierung abgespeichert.

|
[Bild: 9]

Suchschema löschen

[Bild: 9. Suchschema löschen]

Durch Betätigen dieses Knopfes wird das aktuell gewählte Suchschema gelöscht.

|
[Bild: 10]

Ok Ausgeben

[Bild: 10. Ok Ausgeben]

Durch Betätigen dieses Knopfes wird die Ausgabe gestartet.

|
[Bild: 11]

Ende

[Bild: 11. Ende]

Durch Betätigen dieses Knopfes wird die Selektionsmaske geschlossen. Falls Sie ein kompliziertes Suchschema zusammengestellt haben, denken Sie bitte rechtzeitig darüber nach es abzuspeichern.
