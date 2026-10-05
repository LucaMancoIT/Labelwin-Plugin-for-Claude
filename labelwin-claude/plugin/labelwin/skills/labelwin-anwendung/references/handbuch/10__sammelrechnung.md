# 10. Sammelrechnung

Pfad: Kundendienst > Kundendienst [6] > 10. Sammelrechnung
Quelle: handbuch/10__sammelrechnung.htm

|

10. Sammelrechnung

Eine Sammelrechnung kommt immer dann zum Einsatz, wenn mehrere Kundendienstaufträge über eine Rechnung abgerechnet werden sollen. Die Sammelrechnung erscheint als Dokument in dem Projekt, in dem auch der erste Auftrag zugeordnet ist.

Falls bereits eine oder mehrere Sammelrechnungen begonnen wurden, werden diese angeboten. Bei der Wahl einer vorhandenen Sammelrechnung werden die neuen Positionen angehängt.

[Bild]

Bild: Sammelrechnungen

Sobald eine Sammelrechnung gedruckt und dabei im Rechnungsausgangsbuch eingetragen wurde, wird sie nicht mehr angeboten.

Die Möglichkeit mit mehreren Sammelrechnungen haben wir vorgesehen, damit bei regelmäßigen Rechnungsintervallen wie 1mal Programm Woche oder Monat auch schon neue Aufträge abgeschlossen werden können, obwohl von der vorigen Periode noch Aufträge offen sind. In der Auswahlliste werden nur Sammelrechnungen angeboten, die sich auf die gleiche Rechnungsadresse beziehen.

Bei der Anlage einer neuen Sammelrechnung wird eine Bemerkung abgefragt, mit dessen Hilfe sie später wieder gefunden werden kann.

[Bild]

Bild: Sammelrechnungen Zusatzbemerkung

Die bei der Erledigtsetzung eines Kundendienstauftrages zu wählende Vorbemerkung wird in der Sammelrechnung als Textartikel verwendet. Die Struktur einer Sammelrechnung sieht dann z.B. so aus:

|

Textartikel

|

Unser Auftrag..........

|

|

Fahrkosten

|

|

|

Zeiten

|

Monteurstunden...

|

aus Zeitwirtschaft

|

Material

|

................................

|

über Artikelaufruf

|

.

|

|

|

.

|

|

|

.

|

|

|

Textartikel

|

Unser Auftrag.........

|

Aus Vorbemerkung

|

Fahrkosten

|

Anfahrpauschale.....

|

aus Fahrzone

|

etc.

|

etc.

|

etc.

Bei der Druckausgabe als Rechnung mit dem speziell dafür entwickelten Report Rgsamm1 wird automatisch hinter der Artikelliste eines Auftrages eine Zusammenfassung + Mehrwertsteuer ausgewiesen. Aufgrund von Rundungsdifferenzen entsprechen jedoch die Summen der MwSt-Beträge der einzelnen Aufträge meist nicht der am Ende der Rechnung ausgewiesenen Gesamt-Mehrwertsteuer.
