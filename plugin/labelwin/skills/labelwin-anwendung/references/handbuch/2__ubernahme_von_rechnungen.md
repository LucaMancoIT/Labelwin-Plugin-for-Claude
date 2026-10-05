# 2. Übernahme von Rechnungen

Pfad: Buchhaltung > Rechnungsimport [Modul] > 2. Übernahme von Rechnungen
Quelle: handbuch/2__ubernahme_von_rechnungen.htm

|

2. Übernahme von Rechnungen

Wenn Sie digitale Rechnungsdateien im vorgesehenen Verzeichnis abgelegt haben, starten Sie im Rechnungseingangs-Modul den Menüpunkt <Bearbeiten> <Zugferd/GAEB/UGL-Rechnung>. Das Gleiche erreichen Sie mit der Taste F7.

Wählen Sie den Lieferanten und betätigen dann den Knopf ‚Liste neu aufbauen‘.

|

Tipp: Wenn Sie die Daten hauptsächlich von einem Lieferanten bekommen, können Sie diesen als Vorgabe festlegen. Damit startet die Maske sofort mit der Liste der Rechnungen. Die Vorgabe wird über das Menü in dieser Maske eingestellt.

Interpretation der digitalen Rechnung:

Labelwin versucht die digitale Rechnung zu interpretieren, was leider aufgrund der beim Lieferanten erfassten Daten nicht immer klappt. Zum Wiedererkennen der Bestellung ist in der Datei ein Feld ‚Vorgangsnummer des Handwerkers‘ vorgesehen. Wenn dieses vom Lieferanten so gefüllt wird, dass die Bestellung im Labelwin eindeutig erkannt wird, kann die Erfass-Maske optimal vorbelegt werden.

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

Auf der nächsten Seite sehen Sie eine Maske mit den digitalen Rechnungen, an denen die Probleme beispielhaft sichtbar sind.

[Bild]

Um den Import einer Rechnung vorzunehmen, markieren Sie die zu importierende Rechnung und betätigen den Knopf ‚Ok übernehmen‘

Zahlungsbedingungen

Je nach Einstellung erscheint dann die Maske für den Vergleich der Zahlungsbedingungen. Sie erscheint nur dann, wenn die Zahlungsbedingungen der Rechnung und die bei der Adresse hinterlegten Bedingungen unterschiedlich sind.

Sie erscheint auch nicht, wenn Sie in den Grundeinstellungen angekreuzt haben, dass Sie immer die ‚eigenen‘ Zahlungsbedingungen nehmen wollen.

[Bild]

Mit den Knöpfen entscheiden Sie, ob die ‚eigene Zahlungsbedingung aus der Adresse oder die aus der Rechnung genommen werden soll. Um Ihnen die Entscheidung leichter zu machen, werden für Sie positive Werte der Datei in Grün und negative Werte in Rot markiert. Das Skonto wird bei Abweichung als Betrag und nicht in Prozent ausgewiesen, damit Sie bei geringen Beträgen erkennen, dass es sich nicht lohnt, sich darum zu kümmern.

Nun wird die Rechnung importiert und deren Artikel im oben beschriebenen Labelwin-Dokument abgelegt.

Genau wie bei einer Papierrechnung können beliebig viele Vorgänge (Lieferscheine) in der UGL enthalten sein. Im Folgenden bezeichnen wir dies als einen Block. Jeder Block gehört zu einem Projekt oder Kundendienstauftrag und wird daher mindestens einen Verteilsatz erzeugen.
