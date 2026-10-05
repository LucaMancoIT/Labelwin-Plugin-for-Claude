# 9.1 Besonderheit beim Auslesen des Scanners

Pfad: Materialwirtschaft > Scannerverarbeitung [Modul] > 9. Datalogic Formula 732/734 > 9.1 Besonderheit beim Auslesen des Scanners
Quelle: handbuch/9_1_besonderheit_beim_auslesen_des_scanners.htm

|

9.1 Besonderheit beim Auslesen des Scanners

Sollten Sie mit Rechnern mit dem Betriebssystem Windows XP Servicepack 3, WindowsVista oder Windows 7 arbeiten, benötigen Sie zum Auslesen der Scannerdateien das Programm systools.exe.

Nehmen Sie in der Datei labelusr.ini (liegt entweder im System C:\windows oder im Labelwin im Modul Einstellungen unter dem Menüpunkt <Grundeinstellungen> <Pfade> im ‚Pfad für fenster.ini’ eingetragenen Unterpfad) im Kapitel [Scannerdaten] folgenden Eintrag vor: Formular732sys=1

Bei Neuauslieferungen der scann.exe ab 2010, haben wir die systools mitgeliefert. Sollten Sie mit das Programm vor 2010 erworben haben und inzwischen einen Rechner mit den o.g. Betriebssystemen haben, melden Sie sich bitte bei uns, damit wir Ihnen die fehlenden Dateien zusenden können.

Kopieren Sie bitte die von uns Datei Systools.zip in das Verzeichnis Labelwin. Gehen Sie danach bitte wie folgt vor – rechte Maustaste – Menüpunkt ‚Extrahiere in den Ordner’ anwählen – es wird Ihnen der Ordner systools vorgeschlagen.

Starten Sie dann aus dem Ordner systools die Datei systools.exe. Lassen Sie diese Datei geöffnet. Sie sehen folgendes Bild:

[Bild]

Drücken Sie dann den Knopf Start.

[Bild]

Gehen Sie danach im Labelwin auf die Scannerverarbeitung und lesen Sie die Daten aus dem Scanner aus.

Das Starten der systools.exe müssen Sie bei jedem Neustart Ihres PC's vornehmen.

Sollte die Datei systools.exe nicht korrekt gestartet oder die Verbindungen zum Scanner nicht ordnungs-gemäß ausgeführt worden sein, kann keine Verbindung aufgebaut werden.

Bei Neuauslieferungen ab Juli 2010 muss zusätzlich ein weiterer Schalter gesetzt werden. Nehmen Sie in der Datei labelusr.ini (liegt entweder im System C:\windows oder im Labelwin im Modul Einstellungen unter dem Menüpunkt <Grundeinstellungen> <Pfade> im ‚Pfad für fenster.ini’ eingetragenen Unterpfad) im Kapitel [Scannerdaten] folgenden Eintrag vor: scannversion=1
