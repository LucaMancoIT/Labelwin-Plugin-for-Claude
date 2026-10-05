# Anwendung

Pfad: Adressverwaltung > Versand per Email > Anwendung
Quelle: handbuch/anwendung_1.htm

|

Anwendung

Erfassen Sie ein Dokument für eine Adresse, bei der Sie die Einrichtung vorgenommen haben. Sobald Sie dann in die Druckmaske starten und die Bedingungen sind erfüllt, wird das Ankreuzfeld E-Mail sichtbar und ggf. auch das Ankreuzfeld, um einen gescannten Kundendienst-Arbeitsbericht mit zu senden.

[Bild]

Der eingestellte Papierdrucker darf nicht umgestellt werden. Je nach gewählter Anzahl der Exemplare erfolgen weitere Drucke auf diesem Drucker.

Die per E-Mail versandte PDF ersetzt also das erste Exemplar. Alles weitere mit Folgeexemplaren auf anderem Drucker usw. funktioniert wie bisher.

Im Hintergrund erfolgt die Druckausgabe an den Druckertreiber EDoc und startet zuletzt automatisch in die Email-Maske, die mit den hinterlegten Daten bereits vollständig ausgefüllt ist.

Wenn Sie den Haken entfernen, wird ohne Email-Versand gedruckt.

|

Achtung: Ein Problem ist möglicherweise, dass Sie ein Formular für Firmenpapier benutzen. Dann würde auf der PDF der Briefkopf fehlen. Dazu können Sie aber mit einer Folie arbeiten, die nach der Erzeugung der PDF auf die Rechnung aufgelegt wird. Wenn Sie eine Folie wählen, wird diese auch beim Druckarchiv / Scanarchiv verwendet. Voraussetzung ist die Installation des Programmes PDFTK.exe

Hinterlegung einer Folie für den PDF-Druck beim E-Mail Versand

1. Es muss eine Folie erzeugt und in einem fest definierten Unterordner von Labelwin abgelegt werden. So eine Folie ist eine PDF Datei von Ihrem Firmenpapier. Der Zielordner dieser Datei lautet z.B. L:\labelwin\Vorlage\layer\

2. Die Folie muss in der report.ini beim Formular hinterlegt werden. Die entsprechende Einstellung befindet sich im Modul EINSTELLUNGEN unter [Programmbereiche - Druckausgabe - report.ini bearbeiten].

[Bild]

3. Das PDF Toolkit (PDFTK) muss installiert sein. Die Anleitung hierzu finden Sie im Kapitel PDFTK einrichten.
