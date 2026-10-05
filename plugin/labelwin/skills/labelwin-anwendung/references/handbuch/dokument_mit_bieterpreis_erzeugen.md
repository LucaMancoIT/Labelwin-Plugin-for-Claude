# Dokument mit Bieterpreis erzeugen

Pfad: Dokumentenbearbeitung > Preisspiegel [26] > Dokument mit Bieterpreis erzeugen
Quelle: handbuch/dokument_mit_bieterpreis_erzeugen.htm

|

Dokument mit Bieterpreis erzeugen

Diese Funktion wird auf der Planerseite als Bieter-LV bezeichnet. Im Grunde genommen geht es darum, ein neues Dokument anzulegen, in dem die Preise eines bestimmten Bieters oder des so genannten Bestbieters eingetragen werden. Der Bestbieter ist ein fiktiver Bieter, bei dem die jeweils niedrigsten Preise eingesetzt werden.

|

Hinweis: Neben der hier beschriebenen Funktion können auch die Preise von einzelnen Positionen in ein Dokument übernommen werden. Lesen Sie dazu bitte im Kapitel Preisauswahl im Artikelaufruf.

Wenn der Preisspiegel zu einem Großhändlervergleich genutzt wird, wird bei der Übergabe mit den optimalen Preisen der jeweils niedrigste Bieterwert als Einkaufswert eingetragen. Werte mit Null werden in diesem Fall jedoch nicht übertragen, sondern in diesem Fall wird der niedrigste mit einem Preis ungleich Null genommen.

Das neue Dokument wird in dem gleichen Projekt angelegt, in dem auch das Ursprungsdokument liegt.

[Bild: Dokument mit Bieterpreis erzeugen]

Bild: Auswertung Bieter-LV

|
[Bild: 1]

Preisfestlegung

[Bild: 1. Preisfestlegung]

Hier legen Sie fest, ob die Preise als Verkaufspreis oder Einkaufswert eingesetzt werden. Ein Planer wird hier das Erste wählen, während bei einem Preisvergleich von Lieferanten der Einkaufspreis eingesetzt wird. Hier müssen Sie dann weiter entscheiden, ob die Einkaufspreise als Material EK, Fremdleistung EK oder Sonstige Kosten EK eingetragen werden sollen.

|
[Bild: 2]

Preise eintragen

[Bild: 2. Preise eintragen]

Hier legen Sie fest welche Preise in das Dokument geschrieben werden sollen

-

von bestimmten Bieter: Bei dieser Variante, werden die Preise des in Feld "Bieter" [Nr.3] gewählten Bieter genommen.

-

vom Bestbieter: Durch Aktivieren dieses Feldes wird die Bieterauswahl [Nr.3] ausgeblendet und bei jeder Position der jeweils günstigste Preis eingetragen. Dies wird auch als Idealangebot oder Bestbieter-LV bezeichnet. Als günstigster wird jeweils der Bieter mit dem niedrigsten Preis pro Position angesehen, wobei Positionen mit dem Preis Null nicht berücksichtigt werden. Sollte also wirklich mal jemand etwas verschenken, so müssen Sie diese Position später ändern oder im Preisspiegel mit 0,01 eingeben.

-

gemäß Bieterfestlegung: Diese Variante greift auf Ihre Bieterfestlegung zurück, die Sie unter <Auswertungen - Preisübersicht/ Bieterfestlegung> vorgenommen haben.

|
[Bild: 3]

Bieter

[Bild: 3. Bieter]

Wenn Sie im Bereich "Preise eintragen" [Nr.2] die Option "von bestimmtem Bieter" aktiviert haben, kann hier der Bieter gewählt werden, dessen Preise übertragen werden sollen.

|
[Bild: 4]

Anmerkung

[Bild: 4. Anmerkung]

Der hier eingesetzte Text wird als Kommentar zum neuen Dokument genommen. Er wird je nach gewählter Einstellung vorgeschlagen, kann aber auch individuell eingetragen werden.

|
[Bild: 5]

Positionen mit Preis 0

[Bild: 5. Positionen mit Preis 0]

Hier wird festgelegt, was mit Positionen passieren soll, deren zu übertragener Preis Null ist.

Dieser Bereich sieht etwas anders aus, wenn Sie ein Bieter-LV mit ‚optimalen Preisen‘ erzeugen. Die Abfrage bezieht sich dann nur noch auf die Situation, dass einer Position alle Bieter keinen Wert eingetragen haben.

-

Artikel nicht übertragen: Wenn dieses Feld aktiviert ist, werden Artikel mit Wert Null nicht in das neue Dokument ausgenommen. Diese Position fehlt dann einfach

-

Menge auf Null setzen: In den neuen Dokument wird die Menge dieser Position auf Null gesetzt. In der Dokumentenbearbeitung können dann solche Positionen ggf. mit der Funktion ‚Artikel mit Menge 0 entfernen‘ gelöscht werden

-

Einkaufpreis aus Ursprungsdokument verwenden: Hiermit wird in dem neuen Dokument bei dieser Position der Preis des alten Dokumentes übernommen.

|

Sollten bei einzelnen Positionen keine Preise eingesetzt werden, weil z.B. der Bieter den Preis Null stehen lassen hat, werden diese Positionen am Schluss aufgelistet.

|
[Bild: 6]

OK

[Bild: 6. OK]

Mit diesem Knopf wird die Dokumentenerstellung gestartet.

|
[Bild: 7]

Ende

[Bild: 7. Ende]

Die Maske wird ohne Dokumentenanlage verlassen.
