# Elo-Drucker einrichten

Pfad: Archivierung > ELO Dokumentenarchivierung [Modul] > 2. Label-spezifische Installation ELO > Elo-Drucker einrichten
Quelle: handbuch/elo_drucker_einrichten.htm

|

Elo-Drucker einrichten

Der installierte Elo-Drucker erzeugt die Tif-Dateien in einen vorgegebenen Pfad. Dieser wird aber leider nicht richtig vom Betriebssystem erkannt. Sie müssen im Elo unter <Konfiguration> auf der Karteikarte ‚Postbox‘ den Tiffdruckerpfad ändern.

[Bild]

Dieser Eintrag muss auf einen Pfad zeigen, der existiert und mit allen Rechten des Users ausgestattet ist. (z.B.: c:\elotmp). Dieser Pfad muss manuell angelegt werden, der Eintrag im Elo legt diesen Pfad nicht automatisch an.

Bitte benutzen Sie auf keinen Fall den Ordner ‚labeltmp‘. Legen Sie ggf. einen neuen Ordner ‚elotmp‘ an.

[Bild]

Starten Sie dann aus dem Elo-Verzeichnis das Programm EloArcConnect.exe. Aktivieren Sie hier das Feld ‚Im Grafikformat speichern‘.

[Bild]

Danach muss aus dem Elo-Verzeichnis das Programm PinterConfiguration.exe gestartet werden. Auf der Karteikaten ‚Optionen‘ muss der Haken bei ‚Der Druck erfolgt direkt ins ELO-Archiv‘ entfernt werden.

[Bild]

Damit sind im ELO alle erforderlichen Einstellungen vorgenommen.

Problemfall Elo-Drucker

Der ELO-Drucker und der Fritzdrucker von AVM benutzen die gleichen Treiber. Wenn Sie zunächst den ELO-Drucker und dann Fritz installieren, gibt es keine Probleme. Im umgekehrten Fall haben wir unten die Antworten von ELO zusammengestellt.

|

Win 2000/XP: Der ELO-Drucker lässt sich nicht installieren.

|

Falls die Installation des ELO Druckers unter Win 2000 bzw. Win-XP misslingt, kann es daran liegen, dass Sie eine Fritzkarte auf Ihren Rechner installiert haben. Diese Karte hat einen nicht ganz einwandfreien Treiber, der vom Betriebssystem Windows 2000 nicht richtig erkannt wird und verhindert dadurch die Installation von virtuellen Druckern. AVM hat bereits ein Update zu Verfügung gestellt, auch das "Service Pack 1" von Microsoft soll Abhilfe schaffen. Wir empfehlen Ihnen, den "Fritzport.dll"-Treiber zuerst umzubenennen, dann den ELO Drucker zu installieren und danach den AVM Treiber wieder zurück zu benennen. Den ELO-Drucker können Sie nachinstallieren, indem Sie ELO benutzerdefiniert und hier nur die Druckertreiber installieren.

|

|

Kommt ELOoffice mit KEN von AVM nicht zurecht?

|

Diese Probleme beruhen auf der auch für die Schwierigkeiten bei der ELO-Drucker-Installation gelegentlich verantwortlichen Fritzport.dll - wir empfehlen Ihnen, den "Fritzport.dll"-Treiber zuerst umzubenennen, dann den ELO Drucker zu installieren und danach den AVM-Treiber wieder zurück zu benennen. Den ELO-Drucker können Sie nachinstallieren, indem Sie ELO benutzerdefiniert und hier nur die Druckertreiber installieren.

|

Der ELO-Drucker lässt sich ab Windows Server 2003 nicht installieren.

|

Lösung: Damit die Installation möglich ist, muss Windows die Installation von Druckern mit KernelModus-Treibern zulassen.

Dies erreichen Sie durch folgende Vorgehensweise:

- Eingabe unter „Start - Ausführen": gpedit.msc

- Computerkonfiguration anklicken

- Administrative Vorlagen

- Drucker

- Deaktiviere: Installation von Druckern, die Kernelmodustreiber verwenden, nicht zulassen
