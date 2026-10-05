# 2. Anpassungen in Labelwin

Pfad: Einrichtungsarbeiten > PDF Ablage und PDF Druckertreiber (eDocPrintPro) > 2. Anpassungen in Labelwin
Quelle: handbuch/2__anpassungen_in_labelwin.htm

|

2. Anpassungen in Labelwin

Erkannt wird der eDoc Drucker normalerweise über den Namensanfang "eDoc…".

In größeren Betrieben kann es Probleme geben, dass Labelwin nicht den ‚eigenen‘ eDoc Drucker erwischt, sondern einen freigegebenen eDoc Drucker vom Kollegen.

[Bild]

Dann funktioniert die PDF-Ablage natürlich nicht. Deshalb wurde eine Möglichkeit geschaffen, den Namen des Edoc-Treibers auf dem eigenen Rechner fest einzutragen. Die Eintragung erfolgt im Modul EINSTELLUNGEN unter [Programmbereiche - Druckausgabe - Pdf-Druckarchiv].

[Bild]

Dokumententypen erfassen

Starten Sie das Programm Einstellungen und wählen den Menüpunkt [Vorlagen - Andere Dokumente - Dokumententypen erfassen] an.

[Bild]

Tragen Sie dann so wie hier zu sehen eine neue Dokumentenart ein.

[Bild]

Den Programmnamen können Sie suchen lassen, in dem Sie den Knopf "Suchen’"betätigen. Sie können den EIntrag aber auch leer lassen, dann nimmt Labelwin die in Windows registrierte Standardanwendung für diesen Dateityp.

Sollte auf dem Rechner das Programm zur Anzeige von PDF-Dateien nicht vorhanden sein, können Sie dieses im Internet auf der Seite www.adobe.de herunterladen.

Sonderfall: Mehrfachinstallation von Labelwin

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
