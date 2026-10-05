# Weitere Auswertungen anlegen

Pfad: Einrichtungsarbeiten > Auswertungscenter (V5) / Startcenter (V4) [27] > Weitere Auswertungen anlegen
Quelle: handbuch/weitere_auswertungen_anlegen.htm

|

Weitere Auswertungen anlegen

Wenn Sie über die von uns mitgelieferten Auswertungen hinaus weitere Informationen im Auswertungs- bzw. Startcenter anzeigen möchten, so können individuell weitere Auswertungen eingerichtet werden. Allerdings sind dazu Kenntnisse zur Labelwin Datenbankstruktur und zur SQL Abfragesprache erforderlich, über die der normale Anwender meist nicht verfügt. Die Mitarbeiter von Label und ggf. auch die Labelpartner können Ihnen dazu ein Angebot machen. In der Regel ist es kein großer Aufwand die Anzeige von z.B. der Anzahl Wartungsverträge oder der Anzahl Kundenadressen usw. einzurichten. Im nächsten Unterkapitel finden Sie einige Muster, die Sie kopieren können: Muster Auswertungen.

1. Auswertung erfassen

Wählen Sie in der Maske der Benutzerrechte im Bereich "Startcenter" den Knopf "Auswertung erfassen" an.

[Bild]

|

Hinweis: Eine Vorlage kopieren Sie über den Menüpunkt [Optionen - Auswertungen importieren] ins System.

Damit Sie sich das Ergebnis der Auswertung vorstellen können, hier ein Ausschnitt der gerade gezeigten Einstellung.

Um die Bedeutung der Eingabe ‚Knopfbeschriftung’ zu verdeutlichen, sehen Sie zusätzlich eine Projektauswertung, bei der ein Knopf vorhanden ist.

[Bild]

1) Rahmengestaltung

Zur Überschrift und zum Bild sind sicherlich keine Erklärungen erforderlich.

Sobald Sie im Feld ‚Programmname’ etwas eintragen oder mit dem Suchen-Knopf ein Programm heraussuchen, wird später bei der Auswertung ein Knopf gezeigt. Sie sehen dies im Beispiel mit dem Knopf ‚Projektverwaltung’.

Wenn Sie bei URL eine Internetadresse einsetzen, wird diese Seite statt einer Abfrage (rechte Seite) gezeigt.

2) Abfrage

In einem Rahmen können Sie beliebig viele Abfragen unterbringen. Da die Ausgabe alphabetisch sortiert nach dem Namen erfolgt, haben wir hier einfach Zahlen davor geschrieben.

Sichtbar ist im Startcenter nur die als ‚Vortext’ bezeichnete Beschriftung.

In dem Beispiel sucht das Programm nach allen Kundendienstaufträgen, deren Status < 4, also offen, in Arbeit, Ware bestellt oder erledigt ist. Bei all diesen Aufträgen schaut das Programm in der Zeitwirtschaft nach, ob bereits Zeiten gebucht worden sind und rechnet die Verkaufspreise der Buchungen zusammen. Wenn der Status der Aufträge richtig gepflegt ist, ergibt das die Summe der noch nicht in Rechnung gestellten Löhne.

Dieser SQL-Befehl ist für uns relativ einfach, aber man sieht, das dazu nicht nur EDV-Kenntnisse, sondern auch Insiderwissen erforderlich ist. Im Bedarfsfall sprechen Sie uns oder unsere Partner an.

Hinweis: Es ist bisher nicht möglich, bei solchen zusätzlichen Auswertungen ein Diagramm auszugeben, wie dies bei den Ausgangs- und Eingangsrechnung der Fall ist.

2. Auswertung einbinden

Die hier erfasste weitere Auswertung wird anschließend in der selben Liste wie die standardmäßig mitgelieferten Auswertungen angezeigt und muss bei Bedarf in die Liste der "Angezeigten Auswertungen" aufgenommen werden.

[Bild]
