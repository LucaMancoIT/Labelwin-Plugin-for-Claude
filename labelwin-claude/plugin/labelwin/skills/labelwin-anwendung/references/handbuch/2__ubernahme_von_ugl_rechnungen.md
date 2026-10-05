# 2. Übernahme von UGL-Rechnungen

Pfad: Buchhaltung > UGL Rechnungsimport [Modul] > 2. Übernahme von UGL-Rechnungen
Quelle: handbuch/2__ubernahme_von_ugl_rechnungen.htm

|

2. Übernahme von UGL-Rechnungen

Wenn Sie Rechnungs-UGL-Dateien im vorgesehenen Verzeichnis abgelegt haben, starten Sie im Rechnungseingangs-Modul den Menüpunkt <Bearbeiten> <UGL-Rechnungen importieren>. Das Gleiche erreichen Sie mit der Taste F7.

Wählen Sie den Lieferanten und betätigen dann den Knopf ‚Liste neu aufbauen‘.

|

Tipp: Wenn Sie die Daten hauptsächlich von einem Lieferanten bekommen, können Sie diesen als Vorgabe festlegen. Damit startet die Maske sofort mit der Liste der Rechnungen. Die Vorgabe wird über das Menü in dieser Maske eingestellt.

Interpretation der UGL-Datei:

Labelwin versucht die UGL-Datei zu interpretieren, was leider aufgrund der beim Lieferanten erfassten Daten nicht immer klappt. Zum Wiedererkennen der Bestellung ist in der UGL ein Feld ‚Vorgangsnummer des Handwerkers‘ vorgesehen. Wenn dieses vom Lieferanten so gefüllt wird, dass die Bestellung im Labelwin eindeutig erkannt wird, kann die Erfass-Maske optimal vorbelegt werden.

Leider findet sich die Bestellnummer manchmal im Feld ‚Bemerkung‘, manchmal steht dort nur ein Kundenname (besonders bei Abholungen von der Lieferantentheke) usw. Besondere Probleme gibt es natürlich bei telefonischen Bestellungen. Wenn diese aus der Zentrale erfolgen, können Sie übrigens die Bestellnummer sofort bei der Dokumentenanlage erzeugen und dem Lieferanten mitteilen.

Optimal wird das Feld Vorgangsnummer so interpretiert:

|

Feld ‚Vorgangsnummer‘

|

Erklärung

|

#1234

|

Unsere interne Dokumentennummer wird bei Bestellungen per UGL so übergeben und vom Lieferanten zurückgereicht

|

34567

|

Bestellnummer aus Labelwin, schriftlich oder telefonisch mitgeteilt

|

k 13-12345 oder

k13-12345

|

Kundendienstauftragsnummer, sollte bei Abholungen oder telefonischen Bestellungen von der Baustelle aus so mitgeteilt werden

|

P 13-789 oder

p13-789

|

Projektnummer, sollte bei Abholungen oder telefonischen Bestellungen von der Baustelle aus so mitgeteilt werden

Auf der nächsten Seite sehen Sie eine Maske mit UGL-Rechnungen, an denen die Probleme beispielhaft sichtbar sind.

[Bild]

In dieser Maske haben wir verschiedene UGL-Rechnungen dargestellt, bei denen wir die Bedeutung der Vorgangsnummer zeigen können:

1) und 2) wurde per UGL bestellt. Dies erkennt man daran, dass im Feld ‚Dokum‘ der Inhalt mit Best….. beginnt. Labelwin hat eindeutig die dazu gehörenden Bestellungen gefunden

3) kann nicht automatisiert zugeordnet werden, da vom Lieferanten das Feld der Vorgangsnummer / Kommissionsnummer leer gelassen wurde. Entweder es gibt keine Bestellung oder sie muss manuell zugeordnet werden. Das Projekt oder der Kundendienstauftrag muss manuell zugeordnet werden.

4) kann ebenfalls nicht automatisiert zugeordnet werden, da vom Lieferanten das Feld der Vorgangsnummer / Kommissionsnummer mit kd … beginnt. Labelwin erkennt als Kennzeichen für Kundendienstaufträge nur ein ‚k‘ am Anfang (oder P bei Projektnummern)

5) offensichtlich handelt es sich um eine Abholung ohne Bestellung. Um die Belastung / Zuordnung zu dem richtigen Auftrag zu ermöglichen, wurde die Auftragsnummer angegeben und vom Lieferanten in das richtige Feld geschrieben. Dieser Vorgang kann passabel verarbeitet werden.

6) es handelt sich um eine Bestellung mit der Nummer 151, die jedoch im Labelwin nicht existiert . Die Verteilmaske kann nicht passend gefüllt werden.

7) es handelt sich um eine Abholung ohne Bestellung für ein Projekt 13-00123.

8) kann nicht automatisiert zugeordnet werden, da vom Lieferanten das Feld der Vorgangsnummer mit dem Text ‚Lager‘ gefüllt wurde. Wenn es sich um ein Projekt mit der Projektnummer ‚Lager‘ handelt, hätte das p davor gehört. Entweder es gibt keine Bestellung oder sie muss manuell zugeordnet werden.

_______________________________________________________

Um den Import einer Rechnung vorzunehmen, markieren Sie die zu importierende Rechnung und betätigen den Knopf ‚Ok übernehmen‘

Zahlungsbedingungen

Je nach Einstellung erscheint dann die Maske für den Vergleich der Zahlungsbedingungen. Sie erscheint nur dann, wenn die Zahlungsbedingungen der Rechnung und die bei der Adresse hinterlegten Bedingungen unterschiedlich sind.

Sie erscheint auch nicht, wenn Sie in den Grundeinstellungen angekreuzt haben, dass Sie immer die ‚eigenen‘ Zahlungsbedingungen nehmen wollen.

[Bild]

Mit den Knöpfen entscheiden Sie, ob die ‚eigene Zahlungsbedingung aus der Adresse oder die aus der Rechnung genommen werden soll. Um Ihnen die Entscheidung leichter zu machen, werden für Sie positive Werte der Datei in Grün und negative Werte in Rot markiert. Das Skonto wird bei Abweichung als Betrag und nicht in Prozent ausgewiesen, damit Sie bei geringen Beträgen erkennen, dass es sich nicht lohnt, sich darum zu kümmern.

Nun wird die Rechnung importiert und deren Artikel im oben beschriebenen Labelwin-Dokument abgelegt.

Genau wie bei einer Papierrechnung können beliebig viele Vorgänge (Lieferscheine) in der UGL enthalten sein. Im Folgenden bezeichnen wir dies als einen Block. Jeder Block gehört zu einem Projekt oder Kundendienstauftrag und wird daher mindestens einen Verteilsatz erzeugen.
