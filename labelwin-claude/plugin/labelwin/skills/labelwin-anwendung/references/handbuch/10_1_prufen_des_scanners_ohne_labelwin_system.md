# 10.1 Prüfen des Scanners ohne Labelwin-System

Pfad: Materialwirtschaft > Scannerverarbeitung [Modul] > 10. Einrichten des Scanners Scanpal2 > 10.1 Prüfen des Scanners ohne Labelwin-System
Quelle: handbuch/10_1_prufen_des_scanners_ohne_labelwin_system.htm

|

10.1 Prüfen des Scanners ohne Labelwin-System

Falls es Probleme mit dem Einscannen gibt, ist es sinnvoll, diese eventuell ohne das Labelwin-System einzugrenzen. Vom Hersteller des Scanners wird ein Programm namens 232read.exe mitgeliefert. Dieses befindet sich im Verzeichnis Labelwin. Es dient dazu, die Scannerdaten auszulesen und in eine von uns bestimmte Textdatei zu schreiben. Genau dieses Programm wird später auch beim Scannvorgang vom Labelwin-System aufgerufen.

Um den Scanner direkt zu prüfen, starten Sie also im Verzeichnis Labelwin das Programm 232.read.exe.

[Bild]

Normalerweise müssten die Einstellungen für Ihr System bereits richtig eingestellt sein. Wenn nicht, kontrollieren Sie bitte den Eintrag ‚Directory'. Unser System erwartet hier später ein Zwischenverzeichnis, welches für jeden Benutzer individuell festgelegt ist. Auf dem Einzelplatz handelt es sich in der Regel um das Verzeichnis C:\labeltmp\. Setzen Sie in diesem Programm den untersten Eintrag ‚always show this dialogbox', versetzen den Scanner in den Auslesemodus und betätigen den OK-Knopf des Programms. Wenn alle Einstellungen richtig sind, werden nun die Daten ausgelesen und anschließend wird die Möglichkeit angeboten, diese Daten direkt zu betrachten. Wenn dieser Vorgang nicht geklappt hat, hat auch das Labelwin-System keine Chance, die Scannerdaten richtig einzulesen. Kontrollieren Sie die Pfade auf Existenz und vergleichen den Eintrag mit jenem Zwischenverzeichnis-Eintrag im Labelwin-System. Im Labelwin-System finden Sie die Information im Programmmodul EINSTELLUNGEN unter den Menüpunkten ‚Grundeinstellungen’, ‚Pfade'. In dieser Maske ist es der Eintrag Nr. 10 (temp).
