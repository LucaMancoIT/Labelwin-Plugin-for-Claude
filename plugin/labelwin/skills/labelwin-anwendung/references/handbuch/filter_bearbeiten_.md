# Filter bearbeiten

Pfad: Auswertungen / Controlling > Auswertungen [21] > Projektauswertung > Filter bearbeiten
Quelle: handbuch/filter_bearbeiten_.htm

|

Filter bearbeiten

Mit einem Filter werden bestimmte Projekte ‚weggefiltert‘ so dass nur noch der Rest ausgegeben wird. Das Ganze wird aber hier positiv angewendet - es werden nur solche Projekte ausgegeben, die den hier formulierten Bedingungen entsprechen.

Da die Filter ggf. ziemlich komplex sind, lohnt es sich, diese für die nächste Anwendung zu speichern. Um Ihnen den Einstieg zu erleichtern haben wir Musterdaten hinterlegt, die Sie über das Menü importieren können.

Mit dem Knopf ‚Kontrolle‘ prüft das Programm die Anzahl der Klammern und stellt die Eingrenzung so dar, dass sie für einen EDV-ler verständlich und für den Laien etwas verständlicher wird.

Für gespeicherte Filter sollten Sie unbedingt die Beschreibung ausfüllen und den Sinn des Filters in verständlicher Form eintragen. Mit einem guten Beschreibungstext ist ein Filter auch für ‚Nicht EDV-Menschen anwendbar.

[Bild]

Bild: Filter anlegen / ändern

[Bild]

1 Filtername: In dieser Liste finden sich fertig hergestellte Filters. Wenn Sie hier einen bestimmten Filter anwählen, so wird die abgespeicherte Selektion aktiviert.

[Bild]

2 Beschreibung: Tragen Sie hier eine Beschreibung für den Filter ein und erklären Sie ihn in verständlicher Form.

[Bild]

3 Filter speichern: Durch Betätigen dieses Knopfes wird die aktuelle Selektion abgespeichert. Falls Sie einen gespeicherten Filter aktiviert und geändert haben, wird die ursprüngliche Selektion ohne Nachfrage überschrieben.

[Bild]

4 Speichern als neu: Wenn Sie einen vorhandenen Filter ändern und den ursprünglichen Filter behalten möchten, sollten Sie diesen Knopf betätigen, um die Änderung als neuen Filter zu speichern.

[Bild]

5 Filter löschen: Durch Betätigen dieses Knopfes wird der aktuelle Filter gelöscht.

6 Tabelle: Hier erscheint die Liste der zu selektierenden Merkmale, soweit diese abgelegt worden sind. Wenn in der Tabelle keine Einträge vorhanden sind, werden alle Projekte herausgesucht.

In jeder Zeile der Tabelle wird ein Merkmal hinterlegt, dass für die erfolgreiche Suche erfüllt sein muss. Die Merkmale werden durch Bedingungen wie ‚and‘ und ‚or‘ miteinander verknüpft.

[Bild]

In obigem Beispiel werden nur die Projekte ausgegeben, bei denen beide Merkmale erfüllt sind – also nur die Projekte mit dem Status ‚in Arbeit‘ und mit der einer Projektnummer die mit einer Zahl anfängt ( im EDV Alphabet kommen die Zahlen vor den Buchstaben).

[Bild]

7 Selektionszeilen: Im ersten Feld erscheint automatisch immer das Wort AND. Hierbei handelt es sich um das englische Wort für UND, mit die Merkmale verknüpft werden können. Das Wort AND bedeutet an dieser Stelle, dass die Merkmale die in jeder einzelnen Zeile formuliert sind, gleichzeitig zutreffen müssen. In der Logik wird dieses auch als UND-Verknüpfung bezeichnet. Standardmäßig schreibt unser Programm immer das Wort AND in dieses Feld. Wenn Sie es beispielsweise gegen das Wort OR auswechseln, bedeutet es, dass eines der Merkmale genügt.

Im zweiten Feld können Sie ggf. Klammerzeichen unterbringen, um die Bedingungen voneinander zu trennen. Falls Sie in formaler Logik fit sind, können Sie dort auch Verknüpfungen wie NOT eintragen (negiert die Bedingung).

Im 3. Feld mit der Beschriftung Suchfeld wählen Sie aus der Liste aus, in welchem Datenfeld Sie nach bestimmten Informationen suchen wollen.

Im 4 .Feld mit der Beschriftung Operator wählen Sie aus, ob der im Suchfeld gewählte Begriff größer, kleiner, gleich dem in der Spalte ‚Vergleichstext’ eingetragenen Inhalt sein soll.

Bedeutung der einzelnen Operatoren:

|

= gleich

|

Vergleichstext muss exakt identisch mit dem Inhalt des Suchfeldes sein

|

> größer

|

Inhalt des Suchfeldes muss größer als der Vergleichstext sein. Dabei ist ‚größer’ neben dem Zahlenvergleich auch über die Buchstaben eines Textes definierbar. Wenn ein Buchstabe im Alphabet weither hinten liegt, so ist er größer als dieser. Beispielt: „Berta“ ist größer als „Anton“.

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

<> ungleich

|

Der Inhalt des Suchfeldes muss abweichend zum Vergleichstext sein.

|

LIKE

|

Der Unterschied des Like-Operators zum Gleich-Operator besteht darin, dass hier im Vergleichstext so genannte Joker verwendet werden können:

* Platzhalter für 0 oder mehr beliebige Zahlen

|

Beispiel:

|

Ort LIKE Bie*

Ort LIKE *feld

Ort LIKE *ielefel*

|

liefert alle Orte, die mit ‘Bie’ anfangen

liefert alle Orte, die mit ‚feld’ enden

liefert alle Orte, in dienen dieses Bruchstück vorkommt

|

|

? Platzhalter für ein beliebiges Zeichen

|

Beispiel:

|

Name LIKE M?ller

|

Liefert alle ‚Müller, ‚Möller’ usw., aber nicht Mueller

|

|

[Zeichenkette]

|

Platzhalter für ein Zeichen, dass in der Zeichenkette enthalten ist

|

|

Beispiel:

|

Name LIKE M[ae]ier

|

liefert alle ‘Maier’ und ‘Meier’, aber nicht ‘Meyer’

|

|

|

An dieser Stelle kann auch ein Minus-Zeichen verwendet werden, um ‚von-bis’ auszudrücken

|

|

Beispiel:

|

Name LIKE [A-E]*

|

Liefert alle Kunden, die mit dem Buchstaben zwischen A und E beginnen

|

|

[!Zeichenkette]

|

Platzhalter für ein Zeichen, dass nicht in der Zeichenkette enthalten ist.

|

|

Beispiel:

|

Name LIKE My [!y]er

|

Liefert alle ‘Maier’, ‘Majer’ usw, aber nicht ‘Mayer’

|

|

|

An dieser Stelle kann ebenfalls ein Minus-Zeichen verwendet werden, um ‚von-bis’ auszudrücken.

|

|

Beispiel:

|

Name LIKE [!A-E]*

|

liefert aller Kunden außer denen, deren Namen mit ABCD oder E beginnt

|

NOT LIKE

|

Mit dieser Funktion können Sie alle Merkmale ausschließen, die Sie nicht in der Selektion haben möchten. Ansonsten können Sie mit diesem Operator genauso die „Joker“ einsetzen wie beim Like-Operator.

Tabelle: Operatoren

Im 5. Feld mit der Beschriftung Vergleichstext: geben Sie ein, nach was Sie in dem Suchfeld suchen möchten. Bei dem Vergleichstext muss es sich um eine Information handeln, die in dem Suchfeld vorhanden oder - je nach Operator - größer, kleiner, like ist. Je nach Suchfeld kann es sich um Informationen handeln die Sie selbst frei wählen können, oder auch über Zahlen festgelegt werden. Durch Betätigen des Knopfes ‚Felddaten durchsuchen‘ wird eine Liste aller in der Datenbank vorgefundenen Inhalte gezeigt, aus der Sie einen Eintrag wählen können.

Im 6. Feld können Sie eigentlich nur geschlossene Klammern eintragen oder es leer lassen.

[Bild] 8 Zeile einfügen: Durch Betätigen dieses Knopfes wird die aktuelle Zeile in die Tabelle eingetragen. Die Eintragung erfolgt vor der markierten Zeile (in der Regel also vor dem ‚Auswahlende‘)

[Bild] 9 Suchen: Durch Betätigen dieses Knopfes wird die Datenbank nach allen in dem entsprechenden Suchfeld vorkommenden Inhalten durchsucht und in einer Liste dargestellt. In dieser Liste kann ein Eintrag markiert und automatisch mit dem Okay-Knopf übernommen werden. Die gleiche Funktion ist mit einem Doppelklick auf den Eintrag zu erreichen.

[Bild]

Nutzen Sie diese Funktion möglichst immer dann, wenn Sie nach einem bestimmten Inhalt mit dem Gleich Operator ( = Zeichen) suchen. Besonders interessant ist auch, dass man über diesen Weg oft falsche Eingaben sieht, die sonst nicht sichtbar geworden wären. Selbst bei der Suche mit dem Like-Operator kann man die Suche gut gebrauchen. Wählen Sie einfach einen Inhalt aus, löschen ggf. die letzen Zeichen und tragen das * Zeichen dahinter.

[Bild]

10 Zeile löschen: Durch Betätigen dieses Knopfes wird die in der Tabelle markierte Zeile gelöscht

[Bild]

11 Zeile ändern: Durch Betätigen dieses Knopfes wird die in der Tabelle markierte Zeile in die Eingabefelder eingetragen und kann dort verändert werden. Die gleiche Funktion erreichen Sie durch einen Doppelklick in der Tabellenzeile.

[Bild]

12 Kontrolle: Durch Betätigen dieses Knopfes prüft das Programm die Anzahl der Klammern und stellt die Eingrenzung verständlich dar.

[Bild]

13 OK / Fertig: Durch Betätigen dieses Knopfes wird die Ausgabe gestartet.

Mögliche Inhalte in der Tabellenspalte Suchfeld:

|

Suchfeld

|

Beschreibung

|

Anmerkung

|

Projektnummer

|

Inhalt entsprechend der von Ihnen verwendeten Projektnummer

|

nur Großbuchstaben

|

Abteilung

|

Inhalt entsprechend der von Ihnen verwendeten Abteilung

|

Nur Großbuchstaben

|

Bezeichnung

|

Inhalt entsprechend der von Ihnen verwendeten Projektbezeichnung

|

Groß-/Kleinschrift

|

Ort

|

Enthält die von Ihnen vergebenen Ortsnamen

|

|

Suchbegriff

|

Enthält die von Ihnen vergebenen Suchbegriffe

|

|

Anlagedatum

|

Inhalt entsprechend dem von Ihnen einge-tragenen Anlagedatum

|

Eingabe TT.MM.JJJJ

|

Beginndatum

|

Inhalt entsprechend dem von Ihnen einge-tragenen Beginndatum

|

Eingabe TT.MM.JJJJ

|

Fertigdatum

|

Inhalt entsprechend dem von Ihnen einge-tragenen Fertigstellungsdatum

|

Eingabe TT.MM.JJJJ

|

Status

|

1 = Anfrage, 2 = Angebotsphase, 3 = Auftrag,

4 = in_Arbeit, 5 = erledigt, 6 = zurückgestellt

7 = gesperrt

|

|

Bemerkung

|

Inhalt entsprechend der von Ihnen verwendeten Bemerkung

|

Groß-/Kleinschrift wie im Original, keine Suche mit dem ‚Like’-Operator möglich!

|

Zusatz1

|

Das erste von Ihnen selbst zu vergebene Zusatzfeld im Datenblatt

|

|

Zusatz2

|

|

|

Zusatz3

|

|

|

Zusatz4

|

|

|

Zusatz5

|

|

|

Zusatz6

|

|

|

Zusatz7

|

|

|

Zusatz8

|

|

|

Mandant

|

Diese Eingrenzung muss bei Firmen mit mehreren Mandanten unbedingt getroffen werden!

|

Nummer 1 oder 2 oder…

|

Basis vorhanden

|

Damit können nur die Projekte mit vorhandener Basis herausgesucht werden.

|

Suche nach Basis eingeben

|

Adresse 1 Debitor

|

Über diese Suche mit der Debitorennummer der 1. Adresse im Datenblatt (Auftraggeber) können die Projekte einer bestimmten Adresse heraus gefiltert werden.

|

|

Adresse 2 Debitor

|

Objektadresse

|

|

Adresse 3 Debitor

|

Planeradresse

|

|

Adresse 4 Debitor

|

Architekt

|

|

Adresse 5 Debitor

|

Rechnungsempfänger (in der Regel leer)

|

|

Umsatz Rg.-Ausgang

|

Eingrenzung auf die Umsatzssumme im Rechnungsausgangsbuch

|

|

Umsatz Rg.-Eingang

|

Eingrenzung auf die Umsatzsumme im Rechnungseingangsbuch

|

|

Stunden in Zeitwirtschaft

|

Eingrenzung Stundenanzahl in der Zeitwirtschaft

|

|

Kosten Lagerentnahme

|

Eingrenzung Material-EK in Lagerentnahmen

|

|

Verantwortlich

|

Eingrenzung auf Projekte, die einem bestimmten Verantwortlichen zugeordnet sind

|

|

Datum der Endrechnung

|

Eingrenzung auf Projekte, deren Endrechnung ein bestimmtes Datum haben

|

Eingabe TT.MM.JJJJ

|

Nettosumme AZ

|

Eingrenzung auf Nettosummen Abschlags-rechnungen

|

|

Nettosumme TR

|

Eingrenzung auf Nettosummen Teilrechnungen

|

|

SR gedruckt

|

Eingrenzung auf Schlussrechnungen

0 = nicht geschrieben 1 = geschrieben

|

|

Pr. Status erledigt am

|

Eingrenzung auf Projekte mit Status erledigt am

|

Eingabe TT.MM.JJJJ

|

Pr. Status in Arbeit am

|

Eingrenzung auf Projekte mit Status in Arbeit am

|

Eingabe TT.MM.JJJJ

|

Pr. Status zurückgestellt am

|

Eingrenzung auf Projekte mit Status zurückgestellt am

|

Eingabe TT.MM.JJJJ

|

Pr. Status gesperrt am

|

Eingrenzung auf Projekte mit Status gesperrt am

|

Eingabe TT.MM.JJJJ

|

Kst. Projekt Datenblatt

|

Eingrenzung auf Projekte mit einer bestimmten Kostenstelle (Vorgabe aus Datenblatt)

|

Bei der Druckausgabe sind wieder beliebige Formulare anzuwählen.

Standardmäßig mitgeliefert werden folgende Formulare:

|

Name

|

Auslieferung

|

Reportdatum

|

Beschreibung

|

gl1.rpt

|

ja

|

09.07.1980

|

Angebot/Rechnung sort. nach Status mit Auftraggeber

|

gl2.rpt

|

ja

|

08.07.1980

|

Angebot/Rechnung sortiert nach Status

|

gl3.rpt

|

ja

|

08.07.1980

|

Angeot mit Projektbez. und Suchwort sort. nach Abteilung und Status

|

gl4. rpt

|

ja

|

09.07.1980

|

Basis, Angebot und Rechnung mit Projektbez. und Suchwort sortiert

|

gl5.rpt

|

ja

|

09.07.1980

|

Basis mit Projektbez. und Suchwort sort. nach Abteilung und Status

|

glabt.rpt

|

ja

|

10.07.1980

|

Abteilung, Status Summe Ang., Rg, Ek, Zeit

|

glabt2.rpt

|

ja

|

11.07.1980

|

Abteilung, Status Summe Basis, Rg, Ek, Zeit

|

glpb.rpt

|

ja

|

09.07.1980

|

1 Projekt je Seite

|

glcontr.rpt

|

ja

|

16.07.1980

|

Mit DB aus Rg

|

glhalbf.rpt

|

ja

|

17.07.1980

|

Quer, halbfertige Arbeiten

|

gl-liste.rpt

|

ja

|

06.07.1980

|

Einfach Liste mit Name, Ort, Status

|

glzeit.rpt

|

ja

|

09.07.1980

|

Vergleich Zeit Angebot/Zeiterfassung

|

glzeitba.rpt

|

ja

|

10.07.1980

|

Vergleich Zeit Basis/Zeiterfassung

|

glhalb2.rpt

|

ja

|

12.07.1980

|

Halbfertige Arbeiten unbewertet

|

glkedb.rpt

|

ja

|

09.07.1980

|

Kosten Erlöse DB/Std

Erläuterung des oben abgebildeten Suchschemas:

Bei dem oben aufgeführten Beispiel sucht das Programm in dem Datenfeld Status alle Projekte heraus, die ‚in Arbeit’ sind. Als zweite Bedingung werden nur die Projekte herausgefiltert, deren Nummer mit einer Zahl beginnt. Das sieht vielleicht etwas merkwürdig aus, aber im Computeralphabet liegen die Zahlen vor den Buchstaben. Wir wollten mit dieser Bedingung erreichen, dass das Projekt AUFTRÄGE nicht einbezogen wird.

Diese beiden Bedingungen werden über das AND-Symbol miteinander verknüpft. Das bedeutet, es werden nur die Projekte herausgefiltert, bei denen beide Bedingungen erfüllt sind. Wenn Sie in der zweiten Zeile statt des Wörtchens AND das Wörtchen OR verwendet hätten, so würde das Programm alle Projekte herausfiltern, bei denen eine dieser beiden Bedingungen erfüllt ist. Über das Setzen von Klammern in der ersten und letzten Zeile der Tabelle können die Bedingungen beliebig kombiniert werden.

|

Wichtig: Irritierend für einen Nicht-EDVler ist am Anfang, dass in der Sprache die Bedeutung von „und“ und „oder“ entgegengesetzt der Bedeutung in der EDV ist. Wir sagen, wir möchten alle Kunden im Ort Bielefeld und Paderborn anschreiben und müssen in der EDV „or“ (oder) verwenden, weil die Logik heißt „Alle Kunden mit dem Merkmal Bielefeld oder dem Merkmal Paderborn“. Mit dem „And“ (und) werden nur die Kunden gefiltert, bei denen beide Bedingungen zutreffen. Da in einer Adresse nicht gleichzeitig zwei Orte eingetragen sein können, würde bei „and“ nichts gefunden.

Es folgen einige Beispiele:

[Bild]

Bei diesem Beispiel würden alle die Projekte herausgefiltert, die als Projektort Bielefeld oder Paderborn eingetragen haben und vor oder am 01.01.2011 begonnen wurden. Die Klammern sind wichtig, um das Datum für beide vorigen Eingrenzungen gelten zu lassen.

[Bild]

Bei diesem Beispiel würden alle die Projekte herausgefiltert, die sich im Angebotsstadium befinden und innerhalb des 1. Quartals 2012 begonnen wurden.

[Bild]

Bei diesem Beispiel würden alle die Projekte herausgefiltert, die als Ort ‚KÖLN’ eingetragen haben und bei denen der Suchbegriff mit ‚SAMMEL’ beginnt.
