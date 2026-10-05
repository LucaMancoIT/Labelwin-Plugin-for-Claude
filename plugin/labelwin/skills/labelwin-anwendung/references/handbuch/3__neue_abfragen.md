# 3. Neue Abfragen

Pfad: Auswertungen / Controlling > Controlling [Modul] > Controlling / Chefknopf > Abfragen erstellen > 3. Neue Abfragen
Quelle: handbuch/3__neue_abfragen.htm

|

3. Neue Abfragen

Je nach Ausgabeart, ob Report, Bildschirmtabelle oder Excel-Datei sieht die Erfassmaske von Abfragen etwas unterschiedlich aus. Hier erklären wir die umfangreichste Erfassung bei der Ausgabe in eine Excel-Datei. Die Besonderheit ist, dass eine Abfrage für Excel aus beliebig vielen Abfragen, quasi Unterabfragen, bestehen kann. Dies ist erforderlich, weil in eine Exceltabelle beliebig viele Blätter haben kann und sie nur bei der ersten (Unter-)Abfrage kopiert wird. Alle folgenden Abfragen sollen die Daten an die gleiche Exceltabelle liefern.

Damit die Maske so erscheint, wie unten abgebildet, müssen Sie nach der Betätigung des Knopfes ‚Neue Abfrage’ als erstes die Ausgabeart mit ‚Excel’ wählen und die erste Abfrage gespeichert haben. Erst dann erscheint die Tabelle mit den Unterabfragen.

[Bild]

1 Abfragegruppe: Legen Sie hier fest, in welcher Abfragegruppe diese Abfrage gezeigt werden soll.

2 Schloss: Diese Auswahl ist nur sichtbar, wenn Sie die Schlossverwaltung aktiv haben. Sie können damit festlegen, welche Abfrage von welchem Mitarbeiter ausgelöst werden dürfen.

3 Abfrageart: Legen Sie hier fest, ob es sich bei der Abfrage um einen Ausdruck, eine Bildschirmtabelle oder eine Ausgabe an Excel handelt. Die Festlegung kann nur bei neuen Abfragen erfolgen, sie ist im Nachhinein nicht mehr änderbar. Sollten Sie einen Fehler gemacht haben, so können Sie ggf. den Text der Abfrage in die normale Zwischenablage nehmen und in die neue Abfrage hinein kopieren.

4 Name: Geben Sie hier der Abfrage einen allgemein verständlichen Namen, so dass später der Sinn der Abfrage sofort erkennbar ist. Der Name einer Abfrage ist einmalig, er kann kein zweites Mal verwendet werden.

5 Bemerkung: Hier können Sie die Abfrage mit beliebigen Erklärungen versehen, die später in der Auswahl der verschiedenen Abfragen angezeigt werden. Dieses Feld gibt nur für solche Abfragen Sinn, die auf Grund des nur 50 Zeichen langen Namens nicht ausreichend beschrieben sind. Sollten bei einer Abfrage bestimmte Eingrenzungen vorhanden sein, so sollten Sie unbedingt in diesem Feld darauf hinweisen.

6 Exceldatei / Reportname: Je nach Abfrageart wird hier der Name des Reports oder der Exceldatei abgefragt. Die Datei muss zwingend existieren, da dies beim Speichern der Abfrage geprüft wird. Ein Report wird im Verzeichnis Labelwin\report gesucht, eine Exceldatei im Verzeichnis labelwin\excel\vorlage Bei Exceldateien können Sie mit dem Knopf Nr. 7 ‚Suchen’ die Datei anwählen.

7 Suchen-Knopf: Statt der Eingabe des Excel-Dateinamens können Sie diesen heraussuchen lassen.

8 Tabelle Excelabfrage: Sobald Sie eine erste Excelabfrage gespeichert haben, wird diese hier in der Tabelle angezeigt. Danach kann man mit dem Neu-Knopf (Nr.19) weitere Unterabfragen zu der gleichen Exceldatei erfasssen.

Anklicken einer Abfrage werden dessen Daten unten in die Eingabefelder geschrieben und können gegebenenfalls verändert werden.

9 Abfrage: Tragen Sie hier den gewünschten Abfragetext gemäß den SQL- oder Crystal-Regeln ein. Die Erstellung von komplexen Abfragen ist eine Sache für Spezialisten – bitte haben Sie Verständnis dafür, dass unsere Hotline dafür nicht zur Verfügung steht, bzw. eine Abrechnung erfolgt.

Meist empfiehlt es sich, die Eingabe in einem großen Textfenster vorzunehmen. Drücken Sie dazu den Knopf ‚Text groß’ (Nr.10).

9a Text groß-Knopf: Mit diesem Knopf können Sie den Text der Abfrage in einem großen Eingabefenster erfassen. Dies gibt meist Sinn, da man dann den kompletten Text sehen kann. Etwas ähnliches geht übrigens auch über den Menüpunkt ‚Bearbeiten, Strukturanzeige (F6). Dort wird der Text mit Umbrüchen an den wichtigsten Stellen gezeigt, so dass er etwas strukturierter erscheint..

Noch mal der Hinweis: Die Erstellung von komplexen Abfragen ist eine Sache für Spezialisten.

10 Inhalt: In dieses Feld sollten Sie eine Beschreibung über die Funktion des Befehls eintragen.

11 Text groß-Knopf: Mit diesem Knopf können Sie den Text der Inhaltsbeschreibung in einem großen Fenster editieren.

11 Excelblatt: In dieses Feld müssen Sie den Namen des Excelblattes eintragen, auf dem die Daten platziert werden sollen. Wenn Sie hier einen falschen Namen eintragen, werden die Daten ins Nirwana geschickt.

11 Suchen-Knopf (Lupe): Statt den Namen des Excelblattes einzugeben, können Sie ihn auch aus einer Liste der vorhandenen Blätter auswählen. Da dabei Excel nicht geöffnet sein darf, erfolgt zuvor eine Warnung

12 Zeile: Hier legen Sie fest, in welcher Zeile die Anzeige der Daten beginnen soll. Die Zeilennummer bezieht sich auf die Zeile, in der die Überschrift stehen soll oder bereits steht. Wenn die Ausgabe also in der Zelle A4 erfolgen soll, müssen Sie hier eine 4 eingeben.

13 Reihenfolge: Bei Excel-Unterabfragen legen Sie hier die Reihenfolge fest, in der die Daten übertragen werden. In der Regel ist die Reihenfolge egal, aber es gibt eine Möglichkeit, Abfragen zu erstellen, die auf einer anderen Abfrage aufbauen. Nur in diesem Fall ist die Reihenfolge wichtig.

14 Formel erfassen: Lesen Sie dazu bitte im separaten Kapitel ‚Formeln’.

15 Hilfe-Knopf: Mit diesem Knopf bekommen Sie eine Information über die Schlüsselworte und können diese markeiren um sie per Zwischenablage zu kopieren.

16 Datenbank: Hier wählen Sie die Datenbank, aus der die Daten kommen. Je nach Wahl erscheinen ggf. ein Eingabefeld oder die Katalogauswahl

17 Frage erfassen: Lesen Sie dazu bitte im separaten Kapitel ‚Fragen’.

18 Neu-Knopf: Mit diesem Knopf starten Sie die Erfassung von neuen Abfragen – egal ob es sich um einen Report oder Exceleintrag handelt. Beachten Sie auch den Menüpunkt ‚Neu mit Vorlage’

19 Neu-Excel-Knopf: Mit diesem Knopf legen Sie eine neue Excel-Unterabfrage an.

20 Speichern-Knopf: Die Abfrage wird gespeichert.

21 Löschen-Knopf: Die in der Tabelle der Abfragen markierte Abfrage wird gelöscht.

22 Testen-Knopf: Mit diesem Knopf kann die gerade aktive Abfrage getestet werden. Die letzten Änderungen werden automatisch gespeichert und die Ausführen-Maske geöffnet. Dort können Sie Datumseingaben machen und ggf. Variablen belegen. Nach Betätigen des Ausführen-Knopfes erfolgt die Ausgabe.

23 Ende-Knopf: Die Erfassung von Abfragen wird beendet.

Menüpunkte

|

|

Abfragen

|

|

Neue Abfrage

Nach Wahl dieses Menüpunktes erstellen Sie eine neue Abfrage. Es ist die gleiche Funktionalität, als wenn Sie den entsprechenden Knopf betätigen.

|

|

Neu mit Vorlage

Hier wird die gerade angezeigte Abfrage als Vorlage für eine neue Abfrage genommen. Sinngemäß verhält es sich so, als wenn Sie den Knopf ‚Neue Abfrage’ betätigen und die Daten der vorherigen Abfrage stehen bleiben. Nur beim Kopieren von Excel-Abfragen verhält sich das Programm anders. Hier wird der neue Name der Abfrage eingegeben und dann die komplette Abfrage mit ihren gegebenenfalls vorhandenen Unterabfragen gespeichert.

|

|

Speichern

Hier handelt es sich um die gleiche Funktionalität, als wenn Sie den Speichern-Knopf betätigen.

|

|

Bearbeiten

|

|

Frage erfassen

Hier handelt es sich um die gleiche Funktionalität, wie beim Knopf ‚Frage erfassen’.

|

|

Strukturanzeige

Hier wird der Abfragetext in einem großen Fenster strukturiert dargestellt. Ein Zeilenumbruch befindet sich dann bei den Schlüsselworten From und Where und bei jedem Klammer öffnen und Klammer schließen. Es handelt sich einfach um eine andere Art der Darstellung, bei der die Struktur der SQL-Abfrage besser sichtbar ist.

|

|

Text groß

Dieser Menüpunkt hat die gleiche Funktionalität, wie der Knopf an der Oberfläche. Der Abfragetext erscheint in einem großen Fenster und kann damit besser geändert und eingesehen werden.

|

|

Formeln bearbeiten

Hier ist die gleiche Funktionalität hinterlegt, wie bei Betätigen des Knopfes ‚Formel’.

|

|

Option

|

|

Einfügen aus Zwischenablage

Wenn Sie bei der Druckausgabe in einem x-beliebigen Bereich des Labelwin-Programms den Knopf ‚SQL-Abfrage’ betätigt haben, können Sie das Formular und die entsprechenden Befehle für eine neue Abfrage übernehmen. Vor Wahl dieses Menüpunktes sollten Sie unbedingt den Knopf für die neue Abfrage betätigen, da anderenfalls die vorhandene Abfrage überschrieben wird.
