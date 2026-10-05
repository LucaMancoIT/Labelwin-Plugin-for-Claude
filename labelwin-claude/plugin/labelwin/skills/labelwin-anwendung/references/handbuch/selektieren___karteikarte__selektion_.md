# Selektieren - Karteikarte "Selektion"

Pfad: Kundendienst > Kundendienst [6] > 9. Selektieren von Wartungsterminen > Selektieren - Karteikarte "Selektion"
Quelle: handbuch/selektieren___karteikarte__selektion_.htm

|

Selektieren - Karteikarte "Selektion"

[Bild: Selektieren - Karteikarte "Selektion"]

Bild: Selektion

|
[Bild: 1]

Selektion

[Bild: 1. Selektion]

Hier erscheint die Liste der zu selektierenden Merkmale, soweit diese abgelegt worden sind. Wenn in der Tabelle keine Einträge vorhanden sind, werden alle Wartungstermine herausgesucht.

In jeder Zeile der Tabelle wird ein Merkmal hinterlegt, dass für die erfolgreiche Suche erfüllt sein muss. Die Merkmale werden durch Bedingungen wie ‚AND‘ und ‚OR‘ miteinander verknüpft.

Die Klammern müssen gesetzt werden, weil der Termin nur ausgegeben werden soll, wenn er auf 10.2018 eingetragen ist. Ohne Klammern würden alle gefunden, die (Merkmal 1 und Merkmal 2) oder Merkmal 3 erfüllen. Die Ursache liegt in der Regel, dass ein ‚ODER‘ Vorrang vor einem ‚UND' hat. Vielleicht kennen Sie aus der Mathematik noch die Regel ‚Punktrechnung vor Strichrechnung‘ – das gleiche gibt es in der Logik auch.

Unser Beispiel oben bedeutet im Klartext übrigens, dass alle auszuführenden Wartungstermine herausgesucht werden, die im Monat 10.2018 an der Reihe sind und entweder noch nie ausgeführt wurden (letzte Übernahme in die Auftragsliste ist leer / Null) oder deren letzte Übernahme in die Auftragsliste vor dem 01.01.2018 stattgefunden hat. Damit sollen die Termine ausgefiltert werden, die in der letzten Zeit manuell in einen Kundendienstauftrag übernommen wurden.

|

Hinweis: Wenn Sie die Selektionsergebnisse auf Papier ausgeben wollen, müssen Sie eine Abfrage mit ‚ = null’ bei Oder-Abfragen voranstellen (so wie im Beispiel). Leider hat das Druckmodul Crystal Report eine kleine Macke und druckt sonst zu wenig Termine aus.

Es könnte sonst passieren, dass der Monteur den Zettel noch nicht zurückgebracht hat und der Auftrag ein zweites Mal ausgeführt hat. Wenn der Auftrag schon auf erledigt gesetzt wäre, wäre übrigens der Termin selber schon weiter gesetzt, so dass die Bedingung 10.2018 nicht mehr erfüllt wäre.

|
[Bild: 2]

Selektionszeile

[Bild: 2. Selektionszeile]

Im ersten Feld erscheint automatisch immer das Wort AND. Hierbei handelt es sich um das englische Wort für UND, mit dem Bedingungen verknüpft werden können. Das Wort AND bedeutet an dieser Stelle, dass die Bedingungen die in jeder einzelnen Zeile formuliert sind, gleichzeitig zutreffen müssen. In der Logik wird dieses auch als UND-Verknüpfung bezeichnet. Standardmäßig schreibt unser Programm immer das Wort AND in dieses Feld. Wenn Sie es beispielsweise gegen das Wort OR auswechseln, bedeutet es, dass eine der Bedingungen genügt.

Im zweiten Feld können Sie ggf. Klammerzeichen unterbringen, um die Bedingungen voneinander zu trennen. Falls Sie in formaler Logik fit sind, können Sie dort auch Verknüpfungen wie NOT eintragen (negiert die Bedingung).

Im 3. Feld mit der Beschriftung Suchfeld wählen Sie aus der Liste aus, in welchem Datenfeld Sie nach bestimmten Informationen suchen wollen.

Im 4 .Feld mit der Beschriftung Operator wählen Sie aus, ob der im Suchfeld gewählte Begriff größer, kleiner, gleich.... dem in der Spalte ‚Vergleichstext’ eingetragenen Inhalt sein soll.

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

Platzhalter für 0 oder mehr beliebige Zeichen

Beispiel: Ort LIKE Bie* liefert alle Orte, die mit ‘Bie’ anfangen

Ort LIKE *feld liefert alle Orte, die mit ´feld´ enden.

Ort LIKE *ielefel* liefert alle Orte, in denen dieses

Bruchstück vorkommt.

? Platzhalter für ein beliebiges Zeichen

Beispiel: Name LIKE M?ller liefert alle ‘Müller’, ‘Möller’,

usw, aber nicht Mueller.

# Platzhalter für eine beliebige Ziffer

Beispiel: Plz LIKE 336## liefert alle Postleitzahlen, die

mit 336 anfangen

[Zeichenkette] Platzhalter für ein Zeichen, dass in der Zeichenkette

enthalten ist.

Beispiel: Name LIKE M[ae]ier liefert alle

‘Maier’ usw, ‘Meier’, nicht aber ‘Meyer’

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

außer denen, deren Namen mit ABCD oder E

beginnt.

Tabelle: Operatoren

Im 5. Feld mit der Beschriftung Vergleichstext geben Sie ein, nach was Sie in dem Suchfeld suchen möchten. Bei dem Vergleichstext muss es sich um eine Information handeln, die in dem Suchfeld vorhanden oder - je nach Operator - größer, kleiner, like ist. Je nach Suchfeld kann es sich um Informationen handeln die Sie selbst frei wählen können, oder auch über Zahlen festgelegt werden. Durch Betätigen des Knopfes ‚Felddaten durchsuchen‘ wird eine Liste aller in der Datenbank vorgefundenen Inhalte gezeigt, aus der Sie einen Eintrag wählen können.

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

Felddaten durchsuchen

[Bild: 6. Felddaten durchsuchen]

Durch Betätigen dieses Knopfes wird die Datenbank nach allen in dem entsprechenden Suchfeld vorkommenden Inhalten durchsucht und in einer Liste dargestellt.

In dieser Liste kann ein Eintrag markiert und automatisch mit dem Okay-Knopf übernommen werden. Die gleiche Funktion ist mit einem Doppelklick auf den Eintrag zu erreichen.
