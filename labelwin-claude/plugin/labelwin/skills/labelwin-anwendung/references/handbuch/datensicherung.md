# Datensicherung

Pfad: Installation und Wartung > Datensicherung
Quelle: handbuch/datensicherung.htm

|

Datensicherung

Datensicherung auf lokalem Rechner

|

Hinweis: Diese Datensicherung gilt nicht für Kunden, die bereits auf die SQL-Datenbank umgestellt sind.

Hintergrund

Im Labelwin werden alle wichtigen Daten in einer einzigen Datenbank geführt. Auch wenn täglich (oder nächtlich) eine Sicherung per Streamer durchgeführt wird, sind ggf. bei einem Defekt alle bis dahin erzeugten Daten des Tages verloren. Über einen DOS-Kopiervorgang ist es möglich, diese Datenbank während des vollen Betriebs auf der Festplatte zu sichern. Bei mehreren Arbeitsplätzen sollte gemäß einer Absprache/Betriebsfestlegung jeder Mitarbeiter zu einer bestimmten Zeit den Kopiervorgang auslösen.

Hinweis: Diese Sicherung ersetzt nicht die Streamersicherung, sondern kann zusätzlich stattfinden.

Einrichtung

Stellen Sie sicher, dass auf der lokalen Festplatte ausreichend Speicherplatz frei ist. Es sollten auf der Platte C: mindestens 1,5 GB frei sein. Öffnen Sie dann die Icongruppe Label für Windows und klicken mit der rechter Maustaste in einen freien Bereich dieses Fensters. Wählen Sie den Menüpunkt<Datei> <Neu> <Verknüpfung> und wählen Sie die Datei PROCOPY.BAT im Verzeichnis LABELWIN. Wenn unser Programm also auf der Platte H: abgelegt ist, können Sie H:\labelwin\procopy.bat eingeben und mit Enter bestätigen. Geben Sie als Bezeichnung bitte ‚Sicherung lokal‘ ein. Wenn das Betriebssystem anschließend mehrere Icon zur Auswahl anbietet, wählen Sie sich bitte eines aus. Betätigen Sie den Knopf ‚Fertigstellen‘.

Diesen Vorgang wiederholen Sie für alle Rechner, die genügend freien Plattenplatz haben.

[Bild]

Durchführungsplan

Erstellen Sie eine Tabelle mit allen Mitarbeitern und legen die Uhrzeit fest, zu der die Sicherung erfolgen soll. Eventuell wird durch den Kopiervorgang der Server so belastet, dass das Arbeitstempo darunter leidet. In diesem Fall sollten Sie die Sicherungen einfach in die Frühstücks- und Mittagspause verlegen. Wenn ein Mitarbeiter zu der Zeit nicht anwesend ist, sollte er den Vorgang später nachholen.

Die Sicherung wird per Doppelklick gestartet und kopiert die Hauptdatenbank auf die lokale Platte C: in die oberste Ebene. Nach der Sicherung kann das DOS-Fenster geschlossen werden. Ggf. kann man über die Eigenschaften des Icons den Schalter ‚Nach Beenden schließen‘ setzen.

Plan Fr. Meier 8.00 Uhr

H. Brand 12.00 Uhr

H. Fromme 16.00 Uhr

.

.

Zur Kontrolle kann man die erfolgte Kopie mit der Uhrzeit in ein Protokoll eintragen lassen. Dieses erhöht die Wahrscheinlichkeit erheblich, dass die Sicherung wirklich durchgeführt wird.

Datensicherung Arbeitsbeschreibung

Hintergrund

Mehrfach pro Monat ruft bei uns ein Kunde an, bei dem der Rechner oder die Festplatte kaputt gegangen und keine oder eine sehr alte Datensicherung vorhanden ist.

Die Datensicherung sollte

· täglich,

· auf einem Bandgerät mit wechselnden Bändern für jeden Wochentag,

· immer mit automatisch nachgeschalteter Prüfung (Vergleich) und

· mit einem Protokollausdruck der Prüfung inkl. einer Kontrolle dieses Protokolls erfolgen.

Wenn ein Bandgerät defekt ist, sollte im Netzwerk mindestens eine Sicherung auf einem Arbeitsplatz erfolgen (siehe Beschreibung im vorigen Kapitel).

Wir beraten Sie gerne bei allen Fragen zur Datensicherung – viel lieber als Ihnen sagen zu müssen, dass Ihre Arbeiten verloren sind. Es ist übrigens eine Illusion zu glauben, dass moderne Rechner sichererer sind als die Systeme der Vergangenheit.

Sicherung per CD brennen

Die Sicherung per CD ist keine brauchbare Lösung, weil die Daten nicht alle auf eine CD passen. Die Sicherung erfolgt wegen dem Aufwand dann auch nicht täglich und bei der Rückspielung entstehen große Probleme, weil die Dateien dann auf ‚schreibgeschützt‘ stehen.

Plattenspiegelung

Beim Thema Datensicherung empfehlen Hardwarebetreuer oft das ‚Spiegeln’ der Festplatte. Dabei werden die Daten immer sofort auf 2 Festplatten geschrieben, so dass diese immer identisch sind. Diese Spiegelung hilft ausschließlich beim ‚Festplattencrash’, der heutzutage äußerst selten ist. Selbst beim Datenverlust durch Stromausfall nutzen diese Spiegelungen meistens nichts, da die fehlerhaften Daten dann auf beiden Platten sind. Viel häufiger werden Daten zerstört bei Fehlfunktionen der Hardware, des Betriebssystems, des Programms oder Fehlbedienungen des Anwenders. Dagegen helfen nur Datensicherungen auf mehrere externe Medien, also auf Streamer Bänder.

|

Einen Rechner ohne Datensicherung zu betreiben, ist wie Auto fahren ohne Bremsen. Es sollte daher in Ihrem Sinne sein, dass Sie Ihre Daten täglich sichern.

Grundlagen

Die Datensicherung erfolgt jeden Tag mit sämtlichen auf dem Server befindlichen Daten.

Sicherungsmedien

Es sollten 9 Bänder benutzt werden mit der Beschriftung

Mo

Di

Mi

Do

Fr.1

Fr.2

Fr.3

Fr.4

Fr.5

Falls ein Band defekt ist, empfiehlt es sich, ein weiteres Band in Reserve zu haben.

Ablauf der Sicherung, Protokollierung

Das Band wird jeweils an dem Tag mit dem gleichen Namen eingelegt. Die Sicherung mit dem Datenbestand vom Montagabend befindet sich also auf dem Band mit der Beschriftung ‚Mo‘. Das Montagsband wird am Dienstagmorgen heraus genommen und das Dienstagband eingelegt. Am ersten Freitag des Monats wird das Band ‚Fr.1‘ eingelegt, am 2. Freitag das Band ‚Fr.2‘ usw.

Wichtig: Die Datensicherung muss mit anschließendem Datenvergleich erfolgen (Compare).

Täglich wird beim Wechsel des Bandes das Sicherungsprotokoll ausgedruckt und sollte im Ordner „DS“ abgeheftet werden. Das Protokoll sollte geprüft und mit den Namen des Prüfers abgezeichnet werden.

Lagerung außerhalb des Betriebs

Das jeweilig letzte Fr.-Band sollte vom Betriebsleiter oder einem Bevollmächtigten mit nach Hause genommen und anschließend das vorherige Band wieder in den Betrieb zurückgebracht werden. Hinweis: Einem unserer Kunden wurde die komplette Rechneranlage mit der Sicherung gestohlen. Weil er ein Band zu Hause hatte, konnte er nach 3 Tagen wieder normal arbeiten. Auch bei einem Brand kann man froh sein, wenn die Daten zu Hause gesichert aufbewahrt werden.

Sicherungsprüfung

Es ist zwingend erforderlich, dass mindestens 1 Mitarbeiter in der Lage ist, einzelne Daten vom Sicherungsband zurück zu holen. Der entsprechende Mitarbeiter muss mindestens 1 x je Monat eine Rücksicherung vornehmen um sicherzustellen, dass die Daten wirklich rekonstruierbar sind.

Hinweis: Label hat schon einige Fälle erlebt, bei denen trotz automatischer Prüfung nach der Sicherung keine Daten rekonstruiert werden konnten. Der Schaden war jeweils enorm.

Vorgehensweise

Am ersten Arbeitstag eines Monats wird eine vorhandene Datei wie z.B. \Labelwin\user.ini gesichert in user.sik (DOS-Ebene: copy user.ini *.sik ) und gelöscht

( DOS-Ebene DEL user.ini ). Anschließend wird diese Datei von einem der letzten Bänder zurückgesichert. Die Rücksicherung erfolgt im Monat1 vom ‚Montagsband‘, im Monat 2 vom ‚Dienstagsband‘ usw.

Nach Erreichen des letzten Bandes beginnt der Zyklus neu.

Die Datei sollte möglichst mit dem DOS-Befehl Fc user.ini user.sik geprüft werden. Die Prüfung sollte mit Namen und Datum im Ordner „DS“ protokolliert werden.
