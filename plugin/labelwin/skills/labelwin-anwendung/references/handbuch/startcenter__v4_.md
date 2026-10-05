# Startcenter (V4)

Pfad: Einrichtungsarbeiten > Auswertungscenter (V5) / Startcenter (V4) [27] > Startcenter (V4)
Quelle: handbuch/startcenter__v4_.htm

|

Startcenter (V4)

Bei diesem Modul handelt es sich um ein Startprogramm, mit dem sich alle Labelwin-Module und auch Fremdprogramme wie Elo, Outlook usw. starten lassen. Damit ersetzt es den Windowsordner mit seinen Icon’s. Darüber hinaus können dort Statusinformationen wie die Anzahl der offenen Aufgaben, Aufträge, Umsätze usw. auf einen Blick angezeigt werden.

Was im Startcenter zu sehen ist, hängt natürlich von der jeweiligen Einrichtung ab, denn spätestens bei den Umsätzen soll dies nicht jeder Mitarbeiter sehen.

Bei den Statusinformationen haben wir einige Grundmuster entwickelt, die per Schalter freigegeben werden können. Darüber hinaus können weitere Kennzahlen frei eingerichtet werden, wobei die Zusammenstellung selbst leider umfangreiche EDV-Kenntnisse verlangen. Weitere Erläuterungen hierzu finden Sie im Unterkapitel Weitere Auswertungen anlegen.

Bevor wir die Einrichtung beschreiben, ein erstes Bild vom Startcenter, dass bei Ihnen selbst aber wieder ganz anders aussehen kann.

[Bild]

Das Startcenter selbst muss als Verknüpfung an die Oberfläche oder in die Windows-Toolbar geholt werden. Die Verknüpfung muss auf das Programm \labelwin\startcen.exe erstellt werden. Dies kann auch über das Modul Einstellungen unter den Menüpunkten <Serviceprogramme>, <Verknüpfung auf Desktop erstellen> passieren.

Es ist übrigens Absicht, dass das Startcenter mehrfach zu starten ist. Es gibt deshalb keine Probleme und eine Meldung wie ‚Dieses Programm ist bereits aktiv’ stört nur.

Wenn Mitarbeiter zwar den Programmbaum nutzen, aber keine Auswertungen sehen sollen, wird standardmäßig die Internetseite ‚MyLabelwin’ gezeigt, mit der man diverse Kundeninformationen bekommt und ins Label-Wiki starten kann.

Einrichtung:

-

Die Einrichtung des V4 Programmbaums wird nachfolgend erläutert.

-

Die Einrichtung des Auswertungsbereiches wird im Unterkapitel Indivduelle Einrichtungen erläutert.

-

Bei den Auswertungen haben wir einige Standards entwickelt, die in den EINSTELLUNGEN aktiviert werden können. Darüber hinaus können weitere Kennzahlen frei eingerichtet werden, wobei die Zusammenstellung selbst leider umfangreiche EDV-Kenntnisse verlangen. Weitere Erläuterungen hierzu finden Sie im Unterkapitel Weitere Auswertungen anlegen.

Programmbaum Startcenter (V4) einrichten

Es gibt einen Standard-Programmbaum, der für alle Benutzer greift, bei denen kein spezieller Programmbaum vorhanden ist. Bei Neuauslieferungen ist er automatisch aktiv, unsere Update-Kunden müssen ihn in Bearbeitung nehmen und speichern. Dieser Standard-Programmbaum wird bearbeitet im Modul EINSTELLUNGEN unter den Menüpunkten [Grundeinstellungen - Allgemein]. In dieser Maske wählen Sie den Knopf ‚Programmbaum bearbeiten’ an.

|

Hinweis: Bitte beachten Sie, dass diese Änderungen alle Anwender betreffen, für die keine speziellen Anpassungen vorgenommen wurden.

In der Regel dürfte es sinnvoller sein, für jeden Benutzer einen individuellen Programmbaum anzulegen. Das widerum erfolgt in der Rechteverwaltung im Modul EINSTELLUNGEN unter [Optionen - Benutzerrechte vergeben].

Neben den Label-Modulen können Sie auch beliebige andere Programme einbinden. Selbst die Einbindung von Dateien wie z.B. Excelmappen (.xls) oder Wordtexten (.doc) ist möglich, wenn die Bearbeitungsprogramme auf dem Rechner passend eingerichtet sind. Im Standardbaum sollte man auf so etwas verzichten.

[Bild]

Übertragen Sie per Doppelklick (oder mit den Pfeil-Knöpfen in der Mitte) die Module aus der linken Liste in den Programmbaum. Der neue Eintrag wird immer ans Ende angefügt, aber er kann mit den Pfeil-Knöpfen an jede andere Stelle geschoben werden

Der in obiger Maske sichtbare Knopf ‚Vorlage wählen’ ist nur bei der Erfassung der individuellen Einstellungen sichtbar. Hierüber kann der Programmbaum eines anderen Users übernommen werden.

Einrückungen im Programmbaum / Oberpunkte

[Bild]

Oben im Bild sind die Programme für das Rechnungsausgangsbuch und das Rechnungseingangsbuch eingerückt und mit dem Oberpunkt ‚Buchhaltung’ versehen.

Dies erreichen Sie indem Sie den Knopf ‚Neu’ betätigen und die Beschriftung erfassen. Mit dem Knopf ‚Bild suchen’ können Sie auch dazu irgendein Icon auswählen.

Mit den Pfeilknöpfen können Sie dann die Programme zum Unterpunkt machen.

Weitere Programme einbinden

Bei der Erstellung eines Standardbaumes ist dies zwar auch möglich, aber in der Regel nicht sinnvoll. Es gibt kaum ein weiteres Programm, dass für alle Anwender sinnvoll ist.

Weitere Programme werde ebenfalls mit dem Neu-Knopf eingetragen. In diesem Fall müssen Sie aber zusätzlich mit dem Knopf ‚Programm suchen’ Das Programm auswählen. Ob Sie ein Bild dazu wählen, bleibt Ihnen überlassen. Leider ist es bisher nicht möglich, die Icons der Programme selbst zu verwenden. Wenn Sie irgendwo auf der Festplatte ein Bild auswählen, so wird dieses automatisch in das Verzeichnis Labelwin\vorlage\icon kopiert.

Statt eines Programms (.exe) können Sie auch eine Datei wie z.B. eine Excel-Tabelle wählen. Ob der Aufruf später klappt, hängt davon ab, ob der Rechner aufgrund der Extension (.xls) das Bearbeitungsprogramm erkennt. In der Regel ist dies der Fall. Wenn sich bei einem Doppelklick auf die Datei das passende Programm öffnet, klappt es auch im Startcenter.
