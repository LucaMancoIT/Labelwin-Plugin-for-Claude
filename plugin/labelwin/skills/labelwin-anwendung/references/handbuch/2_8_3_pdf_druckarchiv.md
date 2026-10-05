# 2.8.3 Pdf-Druckarchiv

Pfad: Einrichtungsarbeiten > Einstellungen [14] > 2. Programmbereiche > 2.8 Druckausgabe > 2.8.3 Pdf-Druckarchiv
Quelle: handbuch/2_8_3_pdf_druckarchiv.htm

|

2.8.3 Pdf-Druckarchiv

Mit dem Pdf-Archiv können Rechnungen, Angebote usw. unmittelbar nach dem Druck zusätzlich als Pdf-Datei gedruckt und in einem speziell dafür vorgesehenen Verzeichnis abgelegt werden. Dabei ersetzt das Archiv nicht die Elo-Ablage, sondern kann sie ggf. ergänzen. Die Ablage im Elo ist nur auf Plätzen möglich, auf denen Elo installiert ist.

[Bild]

[Bild]

1 Zu archivierende Dokumente: Aktivieren Sie hier, bei welchen Druckvorgängen zusätzlich eine PDF-Datei erzeugt werden soll.

[Bild]

2 Elo-Registername: Diese Felder müssen nur dann ausgefüllt werden, wenn eine Übernahme in Elo erfolgen soll.

[Bild]

3 struktierte Ablage: Von diesem Schalter hängt ab, ob die Pdf-Dateien direkt im angegebenen Verzeichnis oder in einer Struktur mit einem Ordner für Rechnungen, einem Ordner für Angebote usw. abgelegt werden. Nur wenn das Verzeichnis dazu dient, alle Dateien weiterzuleiten und dann zu löschen, kann auf die strukturierte Ablage verzichtet werden.

[Bild]

4 Pdf ggf. überschreiben: Wenn dieser Schalter gesetzt ist, wird eine vorhandene Pdf-Datei ohne Nachfrage überschrieben, wenn ein Dokument erneut ausgedruckt wird. Bei nicht gesetztem Schalter wird eine neue Datei angelegt, die sich nur im letzten Teil des Namens unterscheidet. Dort wird in Klammern eine Nummer eingetragen, die sich mit jeder Druckausgabe erhöht. Die Erhöhung gilt aber für alle im Labelwin gedruckten Dokumente, so dass die beim Nachdruck einen x-beliebige, aber andere Nummer im Namen eingetragen wird. Über diese Nummer identifiziert Labelwin bei der Anzeige die richtige Datei (z.B. bei der Wahl aus dem Rechnungsausgangsbuch)

[Bild]

5 Ablagepfad: Die Ablage erfolgt immer in weiteren Unterverzeichnissen, die bei Bedarf automatisch angelegt werden. Hier wird also nur der Hauptbereich der Ablagestruktur festgelegt.

Der hier festgelegte Pfad wird beim Speichern in dieser Maske automatisch angelegt.

Es gibt es 2 Wege, damit auch in Peer to Peer-Netzwerken mit unterschiedlichen Laufwerksbuchstaben gearbeitet werden kann:

1. Absoluter Pfad: Geben Sie Verzeichnisnamen wie D:\xyz oder L:\labelwin\pdfarchiv an.

2. 2) Relativer Pfad: Wenn Sie z.B. nur pdfarchiv eintragen, so wird der Pfad des Labelwin-Systems später automatisch davor gestellt.

Wenn also z.B. Labelwin im Pfad x:\labelwin\ liegt, wird ein Pfad x:\labelwin\pdfarchiv erzeugt.

Wenn der Labelwin-Pfad von einem anderen Rechner dann z.B. K:\labelwin\ heißt, erfolgt die Ablage dennoch im gleichen Verzeichnis.

Egal, welchen Pfad Sie nehmen, bedenken Sie bitte, dass alle Anwender darauf Schreibrechte haben müssen und dieser Bereich gesichert werden sollte.

[Bild] Unter dem von Ihnen festgelegten Pfad werden automatisch weitere Unterverzeichnisse für die Druckarten und ein Ordner je Jahr angelegt.

[Bild]

6 Eigener Edoc: Es muss der PDF-Druckertreiber Edoc auf allen Arbeitsplätzen installiert sein. Die Beschreibung dazu finden Sie im Label-Wiki mit dem Stichwort Edoc. Sollten Sie den edoc-Drucker bereits installiert haben, ist es erforderlich, dass die Einstellungen geprüft und ggf. angepasst werden. Eine ausführliche Beschreibung hierzu finden Sie im Handbuch unter PDF Ablage und PDF Druckertreiber.
