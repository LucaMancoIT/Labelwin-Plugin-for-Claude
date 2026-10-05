# 4. Erstellung von Bildschirmtabellen

Pfad: Auswertungen / Controlling > Controlling [Modul] > Controlling / Chefknopf > Abfragen erstellen > 4. Erstellung von Bildschirmtabellen
Quelle: handbuch/4__erstellung_von_bildschirmtabellen.htm

|

4. Erstellung von Bildschirmtabellen

Hier müssen Sie ‚normale’ SQL-Befehle eingeben. Für die Bildung von solchen Abfragen kann Ihnen unser Programm kaum eine Hilfestellung geben, da diese zwar normal im Programm verwendet werden, ein Herausreichen dieser Abfragen jedoch in der Regel keinen Sinn gibt. Einzig bei der Bildschirmanzeige von Selektionen können Sie über den Menüpunkt ‚Tabellen, SQL zeigen’ den Befehl in die Zwischenablage übernehmen. Im Grunde genommen können solche Abfragen nur von EDV versierten Personen erstellt werden, die unser Datenbanksystem und die Inhalte der entsprechenden Datenfelder kennen.

Im Auslieferungsstand sind einige Musterabfragen, die Sie in Ihr System hineinkopieren können. Die Beschreibung dazu finden Sie weiter hinten.

Um eine Bildschirmtabelle auszugeben müssen Sie unmittelbar nach Betätigung des Knopfes ‚Neue Abfrage’ in der Auswahlbox ‚Ausgabe als’ den Punkt Bildschirm anwählen. Sobald eine Abfrage gespeichert ist, kann die Ausgaberichtung nicht mehr geändert werden.

Als Beispiel wollen wir eine Bildschirmtabelle mit Adressen erzeugen. Die Adressen sind im wesentlichen in der Tabelle adstamm abgelegt.

[Bild]

Alle Abfragen müssen mit ‚Select’ anfangen, andere Befehle sind nicht zugelassen. Eine SQL-Abfrage besteht im wesentlichen aus 3 oder 4 Elementen. Hinter dem Wort SELECT wird angegeben, welche Datenbankfelder gezeigt werden sollen. Ein * (Stern oder Mal-Zeichen) zeigt alle Felder. Hinter dem Wort FROM muss der Tabellenname geschrieben werden, aus dem die Daten kommen. Wenn nicht alle Datensätze gezeigt werden sollen, muss man nun hinter dem Wort WHERE die Bedingung angeben. Um eine Sortierung zu erreichen kann man den Feldnamen hinter ORDER BY eintragen.

Der Befehl

SELECT * FROM adstamm

gibt alle Adressen mit allen Daten in einer großen Tabelle aus.

Probieren Sie es. Vor dem Testen müssen Sie die Abfrage speichern. In diesem Fall müssen Sie in der Ausführenmaske kein Datum eingeben, da die Adressen nichts damit zu tun haben. Bei den Überschriften in der Tabelle handelt es sich um die Namen, die wir den Feldern gegeben haben. Sie sind nicht immer geistreich, aber im Nachhinein können wir sie nicht mehr ändern.

Mit Wissen über unsere Datenstruktur könnte es so aussehen:

SELECT anrede, name, name1, strasse, plz, ort FROM adstamm WHERE debi>’0’ ORDER BY ort, strasse

Hier müssen Sie wissen, dass die Debitornummer im Feld debi steht, dass es ein Textfeld ist (muss in einfache Häkchen eingeschlossen werden) und dass die Sortierfelder ort und strasse heißen.

Probieren Sie es einfach auch damit aus.

Wenn Sie in der Bildschirmtabelle den Knopf Excel betätigen, können Sie das Ergebnis in einer neuen Excel-Tabelle abspeichern.

[Bild]
