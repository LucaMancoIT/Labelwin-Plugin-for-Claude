# 1. Report-Abfragen

Pfad: Auswertungen / Controlling > Controlling [Modul] > Controlling / Chefknopf > Abfragen erstellen > 1. Report-Abfragen
Quelle: handbuch/1__report_abfragen.htm

|

1. Report-Abfragen

|

Bei den Report-Abfragen geht es in erster Linie darum, die unterschiedlichsten Ausdrucke zentral an einer Stelle auszudrucken.

Ohne die Möglichkeiten in diesem Bereich müssten Sie :

- die Übersicht über die Ausgangsrechnungen im Modul ‚Rechnungsausgang’,

- die Ausgabe der produktiven / unproduktiven Stunden im Modul ‚Zeitwirtschaft’,

- die halbfertigen Arbeiten im Modul ‚Projekt’

usw. ausdrucken.

Um also alle interessanten Druckausgaben für einen Zeitraum zu erzeugen, müssen Sie sonst über das ganze Programm hinweg jeweils die Druckausgaben anwählen, ggf. den Zeitraum eingeben, den richtigen Drucker wählen und dann einzeln ausdrucken.

In diesem Modul sammeln Sie die verschiedenen Ausdrucke jeweils als Reportabfrage und ordnen sie der gleichen Abfragegruppe zu. Eine Abfragegruppe kann dann später auf einen Rutsch gedruckt werden.

Gehen Sie in den Programmbereich, in dem der von Ihnen gewünschte Report üblicherweise ausgedruckt wird. Als Beispiel nehmen wir einen Ausdruck aus dem Rechnungsausgangsbuch. Wählen Sie dort den Punkt ‚Datum von - bis’ an und treffen eine gewünschte Datumseingrenzung. Bei den gespeicherten Abfragen dürfen Sie übrigens nur von - bis Datumsfelder verwenden – Eingaben wie Monat 6/2006 sind nicht möglich. Gegebenenfalls wählen Sie nun eine Sortierung, wie z.B. nach Fälligkeit, an.

[Bild]

Betätigen Sie dann den Drucken-Knopf und wählen das Formular, mit dem auch künftig Ihre gespeicherte Abfrage ausgegeben werden soll.

Bevor Sie nun die eigentliche Ausgabe auslösen betätigen Sie den Knopf ‚SQL-Abfrage’. Damit merkt sich das Programm alle von Ihnen getroffenen Entscheidungen in der Zwischenablage. Ob Sie nun den Ausdruck auslösen oder nicht, ist für die gespeicherte Zwischenabfrage gleichgültig. Sie sollten es höchstens deswegen tun, damit Sie sicher sein können den richtigen Ausdruck gewählt zu haben.

Gehen Sie nun wieder in das Selektieren-Programm und wählen den Menüpunkt ‚Abfragen erstellen (F5)’ an.

[Bild]

Betätigen Sie den Neu-Knopf. Um nun die gespeicherte Abfrage aus der Zwischenablage zu holen, betätigen Sie die Tasten Strg E oder über das Menü die Punkte ‚Einfügen aus Zwischenablage’.

Damit haben Sie die Abfrage erstellt und können sie speichern. Eventuell ist es sinnvoll, den Namen der Abfrage zu ändern, der standardmäßig aus der Reportbeschriftung übernommen worden ist. Sobald irgendwelche Besonderheiten in der Abfrage eingegeben worden sind sollten Sie dies in dem Feld ‚Bemerkung’ eintragen, damit dies bei der späteren Anwendung der Abfrage auffällt.

In dem Bild steht die Abfragegruppe auf ‚Buchhaltung’. Diese ist standardmäßig nicht vorhanden und muss ggf. von Ihnen selbst angelegt werden. Eine Gruppeneinteilung wird eigentlich erst interessant, wenn Sie mehr als 20 Abfragen erfasst haben, vorher ist sie sicherlich überflüssig. Die Zuordnung kann auch im Nachhinein sehr schnell geändert werden.

[Bild]

Die Erstellung weiterer Abfragen erfolgt nach dem gleichen Prinzip.

An dieser Stelle möchten wir Ihnen zeigen, wie Sie bei dem oben beschriebenen Beispiel ein einzelnes Erlöskonto ausklammern können. Gehen Sie erneut ins Rechnungsausgangsbuch und wählen neben der zeitlichen Eingrenzung auch eine Eingrenzung auf ‚bestimmtes Erlöskonto’. Wählen Sie nun das Erlöskonto, das sie später ausklammern möchten. In unserem Beispiel gehen wir vom Konto 4450 aus. Erzeugen Sie dann den SQL-Befehl in der Zwischenablage wie oben beschrieben.

Wenn Sie nun diese Abfrage übernehmen, finden Sie in dem Eingabebereich ‚SQL-Befehl’ eine Stelle mit rgausgang.erloeskonto=4450. Um die Änderung besser vornehmen zu können, sollten Sie ggf. den Knopf ‚Text groß’ betätigen. Ersetzen Sie nun das Gleichheitszeichen durch die Ungleichheitszeichen, wird dieses Konto bei der Druckausgabe ausgeklammert. Nach Ihrer Änderung steht also im SQL-Befehl ‚rgausgang.erloeskonto<>4450.

Testen können Sie jede Abfrage unmittelbar nach der Erstellung mit dem Knopf ‚Testen’

|

|

Einfügen aus Vorlage

Um Ihnen gerade in der Anfangsphase behilflich zu sein, liefert Label einige Musterabfragen aus. Durch Wahl dieses Menüpunktes erscheint eine Liste aller Mustervorlagen und Sie können einzelne markieren und kopieren. Wenn es sich um eine Vorlage für eine Excel-Datei handelt, müssen Sie auch die entsprechende Excel-Datei zur Verfügung haben.

Die Anzahl der Mustervorlagen wird im Laufe der Zeit sicherlich umfangreicher werden.

|

|

Abfrage importieren

Wenn Sie von uns eine speziell für Sie erstellte Abfrage erhalten, können Sie diese hier in Ihr System kopieren. Sinngemäß ist es die gleiche Funktionalität, als wenn Sie eine Abfrage aus der Musterdatenbank übernehmen.

|

|

Abfrage exportieren

Hier können Sie eine von Ihnen erstellte Abfrage in eine Textdatei auslagern, um sie gegebenenfalls uns zur Kontrolle oder einem Kollegen, der ebenfalls Labelwin einsetzt, zur Verfügung zu stellen.
