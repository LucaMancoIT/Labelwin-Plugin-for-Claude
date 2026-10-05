# 1. Einrichtungsarbeiten

Pfad: Archivierung > PDF-Druckarchiv [Modul] > 1. Einrichtungsarbeiten
Quelle: handbuch/1__einrichtungsarbeiten_4.htm

|

1. Einrichtungsarbeiten

Ggf. ist eine Anpassung der Formulare erforderlich, die zusammen mit einer Titelzusammenstellung gedruckt werden. Früher musste die Titelzusammenstellung als separate Datei erstellt werden, während sie heute in das Hauptformular eingebunden werden kann. Diese Einbindung ist bei Anwendung der Archivfunktion erforderlich. Klären Sie dies bitte mit Ihrem zuständigen Betreuer oder direkt mit Label Software ab.

Bevor die Einrichtung erfolgen kann, muss der PDF-Druckertreiber Edoc auf allen Arbeitsplätzen installiert sein. Sollten Sie den edoc-Drucker bereits installiert haben, ist es erforderlich, dass die Einstellungen geprüft und ggf. angepasst werden. Eine ausführliche Beschreibung hierzu finden Sie im Handbuch unter PDF Ablage und PDF Druckertreiber.

Wählen Sie im Modul EINSTELLUNGEN den Menüpunkt [Programmbereiche - Druckausgabe - PDF-Archiv].

[Bild: 1. Einrichtungsarbeiten]

|
[Bild: 1]

Zu archivierende Dokumente

[Bild: 1. Zu archivierende Dokumente]

Kreuzen Sie an, bei welchen Druckvorgängen zusätzlich eine PDF-Datei erzeugt werden soll. Für die weiteren Informationen können Sie die kleinen Fragezeichen-Knöpfe nutzen.

|
[Bild: 2]

ELO Ablage

[Bild: 2. ELO Ablage]

Wenn die PDF-Dateien erzeugt werden, um sie später ins ELO zu übernehmen, muss hinter jedem Ausgabebereich der entsprechende Elo-Registername eingetragen werden.

Die Übernahme muss dann von einem Platz aus erfolgen, der Elo-Schreibrechte hat. Legen Sie eine Verknüpfung auf das Programm labelwin\eloablag.exe an oder tragen Sie diese im Startcenter ein.

Hinweis: Dieser Bereich ist nur sichtbar, wenn das Zusatzmodul ELO im EInsatz ist.

|
[Bild: 3]

Pfad der pdftk.exe

[Bild: 3. Pfad der pdftk.exe]

Das Programm PDF Toolkit (kurz PDFTK) wird benötigt, wenn PDF-Dateien an bereits vorhandene Scans oder PDF's angehängt werden sollen. Details zur Einrichtung können Sie unter PDFTK einrichten nachlesen.

|
[Bild: 4]

Optionen

[Bild: 4. Optionen]

-

strukturierte Ablage

Von diesem Schalter hängt ab, ob die Pdf-Dateien direkt im angegebenen Verzeichnis oder in einer Struktur mit einem Ordner für Rechnungen, einem Ordner für Angebote usw. abgelegt werden. Nur wenn das Verzeichnis dazu dient, alle Dateien weiterzuleiten und dann zu löschen, kann auf die strukturierte Ablage verzichtet werden.

-

Pdf bei Nachdruck ggf. überschreiben

Wenn dieser Schalter gesetzt ist, wird eine vorhandene Pdf-Datei ohne Nachfrage überschrieben, wenn ein Dokument erneut ausgedruckt wird. Bei nicht gesetztem Schalter wird eine neue Datei angelegt, die sich nur im letzten Teil des Namens unterscheidet. Dort wird in Klammern eine Nummer eingetragen, die sich mit jeder Druckausgabe erhöht. Die Erhöhung gilt aber für alle im Labelwin gedruckten Dokumente, so dass die beim Nachdruck einen x-beliebige, aber andere Nummer im Namen eingetragen wird. Über diese Nummer identifiziert Labelwin bei der Anzeige die richtige Datei (z.B. bei der Wahl aus dem Rechnungs-ausgangsbuch)

-

Archivbelege beim Erzeugen verschlüsseln

Es wurden immer wieder Anforderungen an uns gestellt, dass ein gescanntes Dokument nicht von jedem Mitarbeiter einsehbar sein soll. Im Labelwin-System konnte dieses bereits seit langer Zeit über die Schlossverwaltung geregelt werden. Im Windows-System konnte man sich die Datei jedoch über den Explorer heraussuchen und anschauen. Dieses kann jetzt durch eine Verschlüsselung verhindert werden.

Zum Einschalten der Funktion müssen Sie hier den Haken setzen. Alle neuen Belege werden ab dann verschlüsselt und sind nur noch aus Labelwin heraus anzuschauen.

Beim Versand aus Labelwin per Email oder beim dem Export an den Steuerberaten werden alle Dokumente entschlüsselt und der Empfänger kann das Dokument sofort öffnen.

Während der Anzeige ist kann das Dokument ebenfalls unverschlüsselt gespeichert werden, indem Sie die Funktion ‚Speichern als ..‘ nutzen.

Bereits bestehende Dokumente werden nicht automatisch nachverschlüsselt. Ein Löschen über den Windowsexplorer wird über diese Funktion nicht verhindert, sondern muss über die Datensicherung gewährleistet werden..

|
[Bild: 5]

Ablagepfad

[Bild: 5. Ablagepfad]

Die Ablage erfolgt immer in weiteren Unterverzeichnissen, die bei Bedarf automatisch angelegt werden. Hier wird also nur der Hauptbereich der Ablagestruktur festgelegt.

Der hier festgelegte Pfad wird beim Speichern in dieser Maske automatisch angelegt.

Es gibt es 2 Wege, damit auch in Peer to Peer-Netzwerken mit unterschiedlichen Laufwerksbuchstaben gearbeitet werden kann:

1) Absoluter Pfad: Geben Sie Verzeichnisnamen wie D:\xyz oder L:\labelwin\pdfarchiv an.

2) Relativer Pfad: Wenn Sie z.B. nur pdfarchiv eintragen, so wird der Pfad des Labelwin-Systems später automatisch davor gestellt.

Wenn also z.B. Labelwin im Pfad x:\labelwin\ liegt, wird ein Pfad x:\labelwin\pdfarchiv erzeugt.

Wenn der Labelwin-Pfad von einem anderen Rechner dann z.B. K:\labelwin\ heißt, erfolgt die Ablage dennoch im gleichen Verzeichnis.

Egal, welchen Pfad Sie nehmen, bedenken Sie bitte, dass alle Anwender darauf Schreibrechte haben müssen und dieser Bereich gesichert werden sollte.

[Bild]

Unter dem von Ihnen festgelegten Pfad werden automatisch weitere Unterverzeichnisse für die Druckarten und ein Ordner je Jahr angelegt.
