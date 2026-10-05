# 1.8 Katalog Grunddaten

Pfad: Artikelstammdaten > Katalog [10] > 1. Einleitung > 1.8 Katalog Grunddaten
Quelle: handbuch/1_8_katalog_grunddaten.htm

|

1.8 Katalog Grunddaten

In diesem Bereich können Sie im Nachhinein den Katalognamen ändern und die Preishistorie ein oder ausschalten. Die Kataloge werden bei Labelwin jeweils in eigenen Datenbanken geführt. Der Name hat für den Programmablauf keinerlei Bedeutung – er wird nur an der Oberfläche zur Auswahl eines Kataloges genutzt. Als Datei haben die Kataloge den Namen KATA*.MDB, wobei der Stern jeweils durch die interne Katalognummer ersetzt wird.

[Bild: 1.8 Katalog Grunddaten]

Bild: Katalogdaten ändern

|
[Bild: 1]

Katalogname

[Bild: 1. Katalogname]

Hier erscheint der Name, den Sie bei der Neuanlage des Katalogs vergeben haben.

|
[Bild: 2]

Kundennummer

[Bild: 2. Kundennummer]

Hier tragen Sie Ihre Kundenummer ein, die Sie von Ihrem Großhändler erhalten haben.

|
[Bild: 3]

Herstellerkürzel

[Bild: 3. Herstellerkürzel]

Zur eindeutigen Identifizierung eines Herstellers oder Großhändlers kennt die Datanorm ein 13-stelliges Herstellerkürzel. Es wird beim Einlesen einer Datanorm Version 5 ggf. automatisch gefüllt.

Dieses Feld wird aber in der Praxis nicht benutzt. Im Rahmen des Energielabels (existiert seit 26.09.2015) wird dieses aber benötigt. Dazu können Sie es hier manuell erfassen. (Hinweis: Für das Energielabel wurde es auf 35 Stellen erweitert.) Mehr Informationen dazu finden Sie im LabelWiki unter der Überschrift "Energielabel" und im Handbuch unter Heizungslabel.

|
[Bild: 4]

Katalognummer

[Bild: 4. Katalognummer]

Jeder Katalog bekommt eine interne und eindeutige Nummer. Sie dient gleichzeitig für den Namen der Katalogdatenbank (KATAxx.MDB) im Verzeichnis \labelwin\datanorm\.

Es wird automatisch die nächste freie Nummer vorgeschlagen.

Achtung: Ein Katalogname kann jederzeit geändert werden. Die Katalognummer sollte sich niemals ändern.

|
[Bild: 5]

Adressdaten

[Bild: 5. Adressdaten]

Tragen Sie hier die Bestelladresse ein.

|
[Bild: 6]

Artikelzugriff URL

[Bild: 6. Artikelzugriff URL]

Tragen Sie hier die URL für den direkten Artikelzugriff auf die Webseite des Großhändlers ein. Dieser Eintrag erfolgt in Zukunft über das Adressmodul.

|
[Bild: 7]

Preishistorie

[Bild: 7. Preishistorie]

Über diesen Schalter wird festgelegt, ob sämtliche Preis- und Minutenänderungen protokolliert werden oder nicht. Wenn er gesetzt ist können Sie in den Stammdaten unter dem jeweiligen Artikel die Änderungen nachlesen. Die Historie ist in der Katalogdatenbank hinterlegt und benötigt nicht viel Speicherplatz.

|
[Bild: 8]

Suche nach niedrigstem EK

[Bild: 8. Suche nach niedrigstem EK]

Wenn Sie hier ein Häkchen setzen, wird dieser Katalog nicht berücksichtigt, wenn Sie nach dem niedrigsten EK für einen bestimmten Artikel suchen.

|
[Bild: 9]

Einkaufspreise per Multi erhöhen

[Bild: 9. Einkaufspreise per Multi erhöhen]

Mit diesem Faktor können Sie die Einkaufspreise beim Einspielen erhöhen (oder auch senken). Hintergrund der Entwicklung ist, dass ein Anwender die Einkaufspreise um ein paar Prozentpunkte erhöhen wollte. Seine Mitarbeiter sollten zwar die Einkaufspreise sehen können, aber nicht die echten Preise. Auch beim Durchlauf Rabatt werden zunächst die richtigen Ek's ermittelt und dann per Faktor ggf. erhöht.

|
[Bild: 10]

Katalog mit Difa-Artikeln führen

[Bild: 10. Katalog mit Difa-Artikeln führen]

Diese Option hat sich inzwischen überholt (Stand: V5.89, April 2019). DiFa Artikel werden inzwischen anders verwaltet. Bitte lesen Sie das Kapitel DiFa - Direktfakturierung.

|
[Bild: 11]

Such-Index auslagern

[Bild: 11. Such-Index auslagern]

Die maximale Größe der Katalogdateien liegt systembedingt bei 2 GB (GigaByte). Das ist prinzipiell, auch für große Datanorm-Kataloge, ausreichend.

Ein großer Datanorm Katalog mit ca. 450.000 Artikeln belegt etwa 1.6 GB. Bein Einspielen einer Datanorm kann die Datenbank aber kurzfristig größer als 2 GB werden.

Mit diesem Haken wird der Katalog auf 2 Dateien aufgeteilt (der Suchindex kommt in eine eigene Datei). Das hat keinerlei Auswirkungen auf die Funktionalität des Programmes - nur organisatorisch verändert sich etliches.

|
[Bild: 12]

Textvorrang

[Bild: 12. Textvorrang]

Wenn Sie diesen Schalter setzen, bleibt der Text beim Aufruf eines verknüpften Artikels erhalten.

|
[Bild: 13]

Minutenvorrang

[Bild: 13. Minutenvorrang]

Wenn Sie hier ein Häkchen setzen, bleiben die Minuten beim Aufruf eines verknüpften Artikels erhalten, sofern sie ungleich Null sind. Wenn bei dem zunächst aufgerufenen Artikel keine Minuten hinterlegt sind, bei dem damit verknüpften Artikel jedoch Minuten vorhanden sind, werden die Minuten des verknüpften Artikels genommen.

|
[Bild: 14]

Text aus Verknüpfung

[Bild: 14. Text aus Verknüpfung]

Bei verknüpften Artikeln können der Text, die Liefermengeneinheit und die Minuten aus einem anderen Katalog genommen werden. Hier wählen Sie den Katalog für die Texte aus.

Hintergrund: Wenn jemand mit dem TGP-Katalog arbeiten, wird man häufig auf damit verknüpfte Artikel von einzelnen Lieferanten zurückgreifen. Die Artikel können schließlich nicht bei TGP bestellt werden, da es sich hier nur um einen Textkatalog und nicht um einen tatsächlichen Lieferanten handelt. Genau das Gleiche trifft zu, wenn man sich textlich auf einen bestimmten Lieferanten festgelegt hat, der gute Artikelbeschreibungen hat, die Artikel jedoch bei einem anderen Lieferanten gekauft werden. Auch in diesem Fall macht es Sinn, den Textlieferanten entsprechend zu kennzeichnen und immer dessen Texte zu verwenden. Bei einer schriftlichen Bestellung bekommt dann der Lieferant zwar den Text eines anderen Lieferanten bzw. den von TGP, aber das schadet nicht, wenn die Original-Artikelnummer verwendet wird.

|
[Bild: 15]

Web ID

[Bild: 15. Web ID]

Hier wird die Web ID für Datanorm Web angezeigt. Die Web ID erhalten Sie, indem Sie auf den gekennzeichneten Knopf klicken. Es erscheint dann dieses Bild.

[Bild]

Wählen Sie aus der Liste den entsprechenden Großhändler oder Hersteller aus, von dem Sie Ihre Datanorm Daten online erhalten wollen.

|
[Bild: 16]

Zugangsdaten

[Bild: 16. Zugangsdaten ]

Diese Daten erhalten Sie von Ihrem Großhändler.

|
[Bild: 17]

Ablagepfad

[Bild: 17. Ablagepfad]

Hier wird der Ablagepfad angezeigt, unter dem die entsprechende Datanormdateien in Labelwin abgelegt werden.

|
[Bild: 18]

OK

[Bild: 18. OK]

Durch Betätigen dieses Knopfes werden die Änderungen übernommen.

|
[Bild: 19]

Abbruch

[Bild: 19. Abbruch]

Durch Betätigen dieses Knopfes verlassen Sie die Maske. Evtl. vorgenommene Änderungen werden nicht übernommen.
