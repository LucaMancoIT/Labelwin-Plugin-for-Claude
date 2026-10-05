# 1. Maske Scan-Modul

Pfad: Materialwirtschaft > Scannerverarbeitung [Modul] > 1. Maske Scan-Modul
Quelle: handbuch/1__maske_scan_modul.htm

|

1. Maske Scan-Modul

Hinweis: Die hier beschriebene neue Maske muss zuerst über den Eintrag scannneu=1 in der global.ini aktiviert werden. Dies wird in der Regel bei der Ersteinrichtung durch die Label Hotline oder den Vertriebspartner erledigt.

Sollten Sie eine andere Maske sehen, ist bei Ihnen noch die alte Oberfläche im Einsatz. Die alte Maske wird im nachfolgenden Unterkapitel beschrieben.

[Bild: 1. Maske Scan-Modul]

Eine Scannerverarbeitung besteht aus vier Schritten. Die Schritte 1 bis 3 betreffen das Auslesen des Scanners und die Interpretation der Scannerdatei. Hierbei handelt es sich um Grundeinstellungen, die in den Einstellungen (14) vorgenommen werden und in einer Vorlage (2) gespeichert werden. Ist die Vorlage einmal passend eingerichtet, braucht man sich nicht mehr um die ersten Schritte kümmern.

Im vierten Schritt wird festgelegt wie die Scannerdaten in Labelwin weiterverarbeitet werden sollen. Da das bei jedem Scannvorgang variieren kann, ist dieser Schritt direkt auf der Hauptmaske konfigurierbar. Die letzte gewählte Einstellung merkt sich die Scannerveraerbeitung für den nächsten Programmstart.

|
[Bild: 1]

Menüleiste

[Bild: 1. Menüleiste]

Die Menüleiste enthält einige Befehle, die am Ende dieser Seite erläutert werden.

|
[Bild: 2]

Vorlage

[Bild: 2. Vorlage]

Hier kann eine Vorlage mit hinterlegten Einstellungen (14) zur Scannerauslesung gewählt werden. Es sollte unbedingt eine Vorlage eingerichtet sein.

|
[Bild: 3]

Aktionen

[Bild: 3. Aktionen]

Die Scannerverarbeitung arbeitet 4 Schritte nacheinander ab. Wenn alles passend eingerichtet ist, werden alle 4 Schritte automatisch nacheinander abgearbeitet. Dazu müssen alle Haken gesetzt sein.

Bei der Einrichtung der Scannerverarbeitung kann es hilfreich sein einen oder mehrere Schritte auszulassen.

|
[Bild: 4]

UGS Dateien erzeugen

[Bild: 4. UGS Dateien erzeugen]

Im Schritt 4 ist festzulegen was mit den Scannerdaten geschehen soll. Die erste Option ist es ein UGS-Datei anlegen zu lassen, die dann in jedes Label Dokument per Menüpunkt "Vorlage - UGS Datei übernehmen" eingelesen werden kann.

|
[Bild: 5]

an offenes Dokument anhängen

[Bild: 5. an offenes Dokument anhängen]

Bei dieser Option, werden die gescannten Artikel in einem Dokument eingetragen. Existiert im Zielprojekt bereits ein Dokument der unter Punkt (6) gewählten Dokumentenart, werden die Artikel angehangen. Gibt es noch kein Dokument des Typs, erfolgt eine Neuanlage.

|
[Bild: 6]

neues Dokument anlegen

[Bild: 6. neues Dokument anlegen]

Bei dieser Variante, wird immer ein Dokument im Zielprojekt angelegt. Auch wenn bereits ein Dokument der gewählten Art besteht.

Wählen Sie auch die Dokumentenart aus. Im Normalfall wird es ein Dokument vom Typ "Lagerentnahme" sein.

Hinweis: Es wird kein Dokument angelegt, wenn in den Scannerdaten keine Projektnummer oder Kundendienstauftragsnummer enthalten ist. In so einem Fall wird immer eine UGS-Datei erzeugt.

|
[Bild: 7]

Lagerabbuchung

[Bild: 7. Lagerabbuchung]

Ist das Lagermodul im Einsatz kann hiermit eine sofortige Lagerabbuchung veranlasst werden. Wählen Sie dazu das entsprechende Lager..

Beachten Sie, dass die Abbuchung nur bei Lagerartikeln erfolgt.

Diese Option ist nur verfügbar, wenn Punkt 6 gewählt wurde und als Dokumententyp "Lagerentnahme" ausgewählt ist.

|
[Bild: 8]

Lieferscheine sofort drucken

[Bild: 8. Lieferscheine sofort drucken]

Mit dieser Option erfolgt ein automatisierter Lieferscheindruck am Ende der Scannerverarbeitung.

Voraussetzung für diese Option ist, dass in den EINSTELLUNGEN unter [Programmbereiche - Druckausgabe - Sammeldruck-Einstellung] eine "Scanner_Lagerentnahme" definiert ist und der Punkt 6 gewählt ist.

Details zur Einrichtung werden im nächsten Abschnitt erläutert: Lagerentnahme als Lieferschein drucken

|
[Bild: 9]

Ohne KD-spez. Preisabfrage

[Bild: 9. Ohne KD-spez. Preisabfrage]

Diese Option ist nur verfügbar, wenn ein Dokument erzeugt wird - also Punkt 5 oder 6 gewählt ist. Beim Erzeugen des Dokumentes erfolgt eine Preisprüfung auf kundenhistorische Preise, wenn im Datenblatt des Zielprojekt eine Adresse hinterlegt ist und in der Adresse unter Zusatzdaten "kundenhistorische Preise vergleichen" angehakt ist. Wird so eine Preisprüfung nicht gewünscht, kann sie mit dieser Option deaktiviert werden.

|
[Bild: 10]

Textartikel als Geheimtext

[Bild: 10. Textartikel als Geheimtext]

Werden die Scannerdaten in eine Dokument geschrieben, erhält das Dokument an erster Stelle immer eine Textposition mit dem Datum und Uhrzeit der Erzeugung. Soll dieser Text auf Ausdrucken nicht erscheinen, kann bereits hier veranlasst werden, dass dieser Text als Geheimtext geschrieben wird.

|
[Bild: 11]

Keine Warnng fehlendes Projekt

[Bild: 11. Keine Warnng fehlendes Projekt]

Sollte die Anlage oder das Füllen eines Dokumentes nicht möglich sein, weil keine Projektnummer gescannt wurde, dann wird ersatzweise eine UGS Datei angelegt.

Dieses Problem wird jedesmal in einem Meldungsfenster gemeldet. Wenn das öfters passiert und man eh sein UGS-Verzeichnis regelmäßig abarbeitet, kann man diese Warnung auch abschalten.

|
[Bild: 12]

zus. Lieferschein je Lieferant

[Bild: 12. zus. Lieferschein je Lieferant]

Wenn Lagerentnahmen geschrieben werden, können gleichzeitig Lieferscheine geschrieben werden, die getrennt nach Artikellieferant angelegt werden (hinterlegte Adresse im Katalog bzw. hinterlegte Adresse beim Artikel).

|
[Bild: 13]

Hilfe

[Bild: 13. Hilfe]

Über den Hilfe Button gelangt man in das LabelWiki in das Kapitel, das die Einrichtung der Scannerverarbeitung für verschiedenste Scannermodelle beschreibt.

|
[Bild: 14]

Einstellung

[Bild: 14. Einstellung]

In der Einstellung werden die Schritte 1 bis 3 konfiguriert.

|
[Bild: 15]

Timer-Start

[Bild: 15. Timer-Start]

Mittels Timer-Start kann die Scannerverarbeitung automatisiert im 15 Sekunden Intervall gestartet werden.

|
[Bild: 16]

Start

[Bild: 16. Start]

Der Start-Knopf löst die Scannerverarbeitung aus.

|
[Bild: 17]

Ende

[Bild: 17. Ende]

Der Ende-Knopf schließt die Scannerverarbeitung.

Die Menüpunkte im Einzelnen:

|

Datei

Start

Gleiche Funktion wie der Start Button (Nr. 16).

Einstellung

Man gelangt in die Einstellungen von Schritt 1 bis 3, Gleiche Funktion wie Button Nr. 14.

Scanner-Textdatei öffnen (aus Schritt 1)

Durch Anwahl dieses Menüpunktes wird die Scannerdatei per Texteditor geöffnet. Diese Funktion kann bei der Ersteinrichtung der Schritte 1 bis 3 hilfreich sein.

XML-Datei öffnen (aus Schritt 2 bzw. 3)

Durch Anwahl dieses Menüpunktes wird die von Labelwin generierte XML-Datei angezeigt. Diese Funktion kann bei der Ersteinrichtung der Schritte 1 bis 3 hilfreich sein.

Protokoll (komplett)

Im Protokoll sind alle bisher ausgeführten Scannauslesevorgänge protokolliert.

Ende

Gleiche Funktion wie der Ende-Button (Nr. 17)

|

Optionen

detailliertes Protokoll führen

Wird diese Option aktiviert, werden alle Scannauslesevorgänge genauer protokolliert. Es werden z.B. alle Zeilen der Scanndatei aufgeführt.

|

Info

Dieser Menüpunkt beinhaltet wie alle Hauptmodule den Zugang zum Handbuch, zur Version und das Erstellungsdatum des Moduls, zur Maske für eine Supportanfrage sowie zum MyLabelwin Wiki.
