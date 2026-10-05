# 8. Datalogic Scanpal2

Pfad: Materialwirtschaft > Scannerverarbeitung [Modul] > 8. Datalogic Scanpal2
Quelle: handbuch/8__datalogic_scanpal2.htm

|

8. Datalogic Scanpal2

Programmierung der Bildschirmmaske zum Scannen

Der Bildschirm des Scanners ist innerhalb gewisser Grenzen programmierbar. Im ersten Schritt passen wir die Oberfläche so an, dass die Befehle in deutscher Sprache erscheinen.

[Bild]

Die dazu erforderlichen Dateien werden von Label auf einer Diskette geliefert. Um bei der Einrichtung von weiteren Rechnern nicht suchen zu müssen, empfehlen wir eine Kopie in ein von Ihnen anzulegendes Verzeichnis Labelwin\scanpal2 abzulegen.

Starten Sie nun in diesem Verzeichnis oder von der Diskette das Programm AG40_SP2.EXE .

Betätigen Sie die rechte Maustaste und wählen im Menü den Punkt ‚OPEN’ . In den angebotenen Dateien bitte labelscann.atx auswählen.

In der nun erscheinenden Maske sollten Sie keine Änderungen vornehmen und sie sofort mit dem Okay-Knopf verlassen.

Kontrolle bestimmter Einstellungen vor dem Übertragen des Programms

Bevor mit der eigentlichen Einrichtung des Scanpals begonnen wird, sollten folgende Punkte kontrolliert werden:

3. Utilities – enter – 1. System Settings – enter – 1. Set Upload Port – enter. Hier muss der schwarze Balken auf RS-232 / Cradle stehen – mit enter bestätigen. Das Programm springt dann wieder in System Settings. Unter 2. Set Download Port – enter – auch hier muss der schwarze Balken auf RS 232 / Cradle stehen – mit enter bestätigen. Unter 3. Transmission Speed – mit enter bestätigen – muss die baud rate auf 115200 bps eingestellt werden (Pfeiltasten nach oben/nach unten). Mit enter bestätigen. Mit der Taste Esc kommt man dann wieder in die nächsthöhere Ebene.

Der Scanner muss jetzt erst einmal ausgeschaltet werden.

Übertragen des Programms auf den Scanpal2

Nun müssen Sie den Scanpal mit dem Rechner verbinden. Dabei ist es egal, ob Sie die COM-Schnittstelle 1 oder 2 verwenden. Sollte die im folgenden beschrieben Übertragung nicht klappen, stecken Sie ihn an den anderen Port. Schalten Sie nun den Scanner ein. Falls der Scanner nicht auf der obersten Menüebene steht, betätigen Sie die ESC-Taste. Mit Drücken der Taste 3.den Punkt Utilities und dann mit der Taste 6 den Punkt Download Programm anwählen und Enter.

Auf dem Rechner nun die rechte Maustaste betätigen und im Menü den Punkt ‚Download Programm’ und ,Via RS232’ anwählen.

Damit ist der Scannpal2 fertig programmiert.

Programm zum Einlesen des Scanners einrichten:

Labelwin benötigt zwei Programme. Falls die Erstinstallation von Labelwin nach dem 1.1.2002 erfolgt ist, befinden sich beide bereits im Verzeichnis Labelwin. Anderenfalls muss die Datei 232_read.exe von der Diskette in das Verzeichnis Labelwin kopiert werden.

Die Datei Scann.exe ist immer im Labelwin-Verzeichnis vorhanden und sollte mit einer Verknüpfung an die Oberfläche geholt werden. Mit diesem Programm erfolgt das Auslesen des Scanners.

Übertragen der gescannten Daten in den Rechner

Starten Sie das Programm Scann.exe. Stellen Sie in der Oberfläche den Scanntyp Metrologic ein und wählen den Com-Port aus, an den der Scanner angeschlossen ist. Zur weiteren Vorgehensweise lesen Sie bitte in den Unterlagen zum Programm-Modul Scanner. Das Programm merkt sich diese Einstellung und startet nun immer mit dieser Einstellung.
