# GAEB

Pfad: Dokumentenbearbeitung > Dokumentenerstellung [3] > GAEB
Quelle: handbuch/gaeb.htm

|

GAEB

GAEB steht für Gemeinsamer Ausschuss Elektronik im Bauwesen. Unter GAEB versteht man üblicherweise aber das Datenformat zum Austausch von Leistungsverzeichnissen, Angeboten, Preisanfragen, Bestellungen usw. Es diente früher ausschließlich zum Datenaustausch zwischen Planern und Bauämtern, später auch zwischen Planern und Handwerkern und inzwischen auch zwischen Handwerkern und Großhändlern.

GAEB Versionen

GAEB 90 Version von 1990. Basiert auf einer zeilenorientierten Textdatei mit fester Satzlänge. Obwohl veraltet und sehr chaotisch wird es immer noch sehr stark benutzt

GAEB DA 2000 Version von 2000. Basiert auf einer schlüsselwort-orientierten Textdatei. Ab dieser Version wurde auch der Austausch zwischen Handwerk und Großhandel eingeführt. DA steht übrigens für ‚Datenaustausch’.

GAEB DA XML Die aktuellste Version im modernen XML Dateiformat. Sie wird sich recht schnell durchsetzen. Manche Bundesländer lesen und schreiben schon seit Anfang 2008 nur noch GAEB DA XML Dateien.

Labelwin kann alle drei GAEB Versionen verarbeiten – lesen sowohl als auch schreiben.

GAEB Datenaustauschphasen

Für den Datenaustausch wurde Phasen entwickelt. Für jede Phase gibt es ein leicht angepasstes Datenformat und Regelungen, welche Daten die Dateien beinhalten.

80er Phase: Austausch Planer – Handwerker – Planer

80 LV Katalog - neutrales nach Gewerken gegliedertes Anwender-Leistungsverzeichnis

81 Leistungsbeschreibung

82 Kostenanschlag - Leistungsverzeichnis mit geschätzten Preisen

83 Angebotsaufforderung - Aufforderung zur Angebotsabgabe an den Handwerker

84 Angebotsabgabe - Die bepreiste Antwort auf eine Phase 83

85 Nebenangebot - Zusätzliche, ggf. alternative oder eventuale, Positionen des Handwerkers an den Planer

86 Auftragsvergabe - Kann vom Handwerker als Auftragsbestätigung eingelesen werden

89 Rechnung - wird von GAEB nicht mehr unterstützt. Kann mit Labelwin nicht verarbeitet werden

90er Phase: Austausch Handwerker – Großhändler – Handwerker

93 Preisanfrage - Preisanfrage des Handwerkers an den GH

94 Preisangebot - Bepreiste Preisanfrage des GH für den Handwerker

96 Bestellung - Bestellung des Handwerkers an den GH

97 Auftragsbestätigung des GH an den Handwerker

Dateinamen Endungen

Die Dateiendungen von GAEB Dateien beginnen mit einem Buchstaben für die Version, gefolgt von der 2-stelligen Phase

Dnn - Format GAEB 90 (von 1990) (nur die 80er Phasen)

Pnn - Format GAEB 2000 (von 2000)

Xnn - Format GAEB XML (aktuellste Version)

z.B. „NeubauKindergarten.P83“

Das Benutzen der oben beschriebenen Dateiendungen ist nicht zwingend vorgeschrieben, sollte aber als Erleichterung für alle Teilnehmer möglichst strikt eingehalten werden.
