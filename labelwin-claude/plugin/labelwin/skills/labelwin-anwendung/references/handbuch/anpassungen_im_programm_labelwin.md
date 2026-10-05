# Anpassungen im Programm Labelwin

Pfad: Dokumentenbearbeitung > Drucken [4] > Dokumente drucken und automatisch im Label ablegen > Anpassungen im Programm Labelwin
Quelle: handbuch/anpassungen_im_programm_labelwin.htm

|

Anpassungen im Programm Labelwin

PDF-Dokumente im Labelwin anmelden

Starten Sie das Programm Einstellungen und wählen die Menüpunkte ‚Vorlagen, Andere Dokumente, Dokumententyp erfassen’ an.

[Bild]

Tragen Sie dann so wie in nebenstehendem Bild eine neue Dokumentenart ein.

[Bild]

Den Programmnamen können Sie suchen lassen, in dem Sie den Knopf ‚Suchen’ betätigen. Sollte auf dem Rechner das Programm zur Anzeige von PDF-Dateien nicht vorhanden sein, können Sie dieses im Internet auf der Seite www.adobe.de herunterladen.

Programmpfad eintragen lassen

Damit die das Labelwin-Programm zur Anlage von Dokumenten und KD-Aufträgen aus der Druckausgabe heraus funktioniert, müssen die vom Druckertreiber nachgeladenen Programme in der richtigen Arbeitsumgebung starten. Die erforderlichen Einträge werden je Rechner abgelegt (je Rechner und nicht je User! ). Für maschinenbezogene Einträge gibt es im Windowsverzeichnis jedes für die Nutzung von Labelwin eingerichteten Rechners eine Datei Labelusr.ini. Damit Sie diese nicht manuell ändern müssen, erfolgt die Eintragung automatisch, wenn Sie einmal im

Modul EINSTELLUNGEN unter dem Menüpunkt <Grundeinstellungen> <Pfade> anwählen und die Maske mit dem Ok-Knopf verlassen.

Da die Eintragung nur so erfolgt, müssen Sie unbedingt einmal diese Punkte anwählen.

Mehrfachinstallation von Labelwin

Bei wenigen Kunden ist Labelwin mehrfach installiert worden, um verschiedene Firmen auch bei den Adressen getrennt zu verwalten. In diesem Fall muss bei der Ablage von Dokumenten gewählt werden, in welches Labelwin-System abgelegt werden soll.

Dazu müssen Sie manuell folgende Einträge in der labelusr.ini (liegt im Windows-Verzeichnis) vornehmen:

In der Gruppe [Grundeinstellungen] muss der Eintrag:

Mehrfachinstall=1

gesetzt werden.

Es muss eine neue Gruppe [Mehrfachinstall] eingerichtet werden:

Für jede Installation muss dann ein Eintrag Namex mit einem verständlichen Namen und ein Eintrag pfadx mit dem Pfad der jeweiligen Installation erstellt werden.

Beispiel:

name1=Heizungsbau KG

name2=Elektro GmbH

pfad1= H:\labelwin \

pfad2=h:\labelwin2\

Bitte lassen Sie diese Änderungen ggf. durch Ihren Labelwin-Betreuer vornehmen.
