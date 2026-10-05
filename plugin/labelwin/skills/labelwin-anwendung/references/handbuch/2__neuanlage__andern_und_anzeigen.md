# 2. Neuanlage, Ändern und Anzeigen

Pfad: Materialwirtschaft > Lager [Modul] > 2. Neuanlage, Ändern und Anzeigen
Quelle: handbuch/2__neuanlage__andern_und_anzeigen.htm

|

2. Neuanlage, Ändern und Anzeigen

Um Artikel in die Lagerverwaltung zu nehmen, müssen sie in den Artikelstammdaten vorhanden sein und im Lager angemeldet werden. Die Anmeldung kann für jeden Artikel einzeln, aber auch für eine beliebig große Artikelmenge auf einen Rutsch erfolgen. Besonders für die Ersteinrichtung spart der Weg ‚auf einen Rutsch’ natürlich viel Arbeit.

Artikel auf einen Rutsch anmelden:

Dazu muss ein Dokument (am Besten mit der Art ‚Freier Text’) angelegt werden, in dem alle anzumeldenden Artikel aufgeführt sind. Die Artikel können ggf. auch auf einen Rutsch in das Dokument gelangen, wenn Sie diese nach gewissen Merkmalen aus den Stammdaten heraus selektieren können. Gehen Sie dazu ins Modul Katalog und aktivieren den Katalog, aus dem die Artikel kommen sollen. Wählen Sie dann den Menüpunkt <Drucken> <Preislisten ausgeben / drucken> an.

[Bild]

Die Artikel müssen dann in eine UGS-Datei einfließen, die im Artikelaufruf dann eingelesen werden kann. Das Einlesen erfolgt unter dem Menüpunkt <Vor-lagen> <UGS-Datei einle-sen>

Anschließend können Sie Artikel entfernen, andere Einfügen usw.

Wenn Sie mit Lagerfächern arbeiten wollen, können Sie diese an Stelle der Positionsnummer einsetzen.

Zum Einlesen dieser Datei lesen Sie bitte im Kapitel Inventur einlesen

Neuanlage, Ändern

Die im Folgenden beschriebene Maske wird mehrfach verwendet. Je nach Anwendungsfall können einige Felder blockiert sein. So ist es z. B. nur bei der Neuanlage möglich, die Artikelnummer zu erfassen. Bei der Anwahl dieser Maske über die Zeigefunktion sind alle Eingaben blockiert.

Wir haben der Einfachheit halber alle Funktionen dieser Maske in dieser Beschreibung erfasst. Gegebenenfalls weisen wir darauf hin, wenn ein Feld im Nachhinein nicht mehr änderbar ist.

Bei der Neuanlage von Artikeln erscheint zunächst die Maske für die Artikelauswahl. Ein Lagerartikel kann hier nur für bereits angelegte Artikel zugewiesen werden. Gegebenenfalls müssen Sie also über das Katalogprogramm zunächst einen Artikel in den Stammdaten ablegen. In diesem Fall empfiehlt es sich über die Windows-Task-Funktion das Katalogprogramm und Lagerprogramm gleichzeitig geöffnet zu haben. So können Artikel angelegt werden und im nächsten Schritt sofort im Lager angemeldet werden. Um bei diesem Verfahren die Artikelnummern nicht doppelt eingeben zu müssen (nämlich bei der Neuanlage und bei der Lagerzuordnung) empfehlen wir Ihnen mit der Windows-Zwischenablage zu arbeiten. Markieren Sie nach der Anlage die Artikelnummer mit der Maus und Betätigen die Taste Steuerung C. Bei der Lagerzuordnung betätigen Sie die Taste Steuerung V.

Die Lager-Artikelnummer wird erst nach der Auswahl des Artikels abgefragt, um Ihnen die Möglichkeit zu geben die gleichen Artikelnummern zu verwenden. Über dieses Verfahren können Sie natürlich auch dem Artikel eine eigene Nummer geben und die Händlerartikelnummer nur für die Zuordnung verwenden.

Neuanlage:

Wählen Sie zunächst mit der Artikelsuchfunktion den zuzuordnenden Artikel aus. Dies geschieht auf die gleiche Weise, in der bei unserem Programm immer Artikel aufgerufen werden. Auf die Beschreibung verzichten wir an dieser Stelle. Nach der Auswahl schlägt das Programm die gewählte Händlerartikelnummer als Lagerartikelnummer vor. Sie können diese Nummer nach Ihren eigenen Wünschen abändern. Als Kurztext und Langtext schlägt das Programm ebenfalls den Text des gewählten Artikels vor. Er kann wiederum nach eigenen Wünschen abgeändert werden. Da die Großhändlertexte manchmal unbrauchbar sind, verwenden wir sie hier nur als Vorlage. Bitte bedenken Sie, dass dieser Text bei Lagerlisten, Etiketten und dergleichen zur Anwendung kommen kann.

Nach der Eingabe der Mengen, Lagerorte, Gruppenzuordnung und dergleichen muss der Artikel abgespeichert werden. Erst danach ist die Zuordnung weiterer Großhändlerartikel auf den gleichen Lagerartikel möglich. Die Zuordnung kann auch jederzeit im Nachhinein erweitert werden.

[Bild]

Bild: Lager Neuanlage, Ändern und Anzeigen

[Bild] 1 Lagerartikelnummer: Bei der Neuanlage können Sie hier eine bis zu 15stellige Artikelbezeichnung eingeben. Es ist möglich Buchstaben und Zahlen zu verwenden. Die Lagerartikelnummer ist im Nachhinein nicht mehr änderbar. Sie ist im Grund genommen ziemlich überflüssig, da da Ein- und Ausbuchen immer mit der Nummer des Lieferanten erfolgt.

[Bild] 2 Kurz(text): In diesem Feld geben Sie den Kurztext Ihres Lagerartikels ein. Bei der Neuanlage wird der Kurztext des Großhändlerartikels vorgeschlagen. Da dieser Text in der Regel auf Lageretiketten platziert wird, haben wir nur eine Zeile mit 40 Buchstaben vorgesehen.

[Bild] 3 Lang(text): In diesem Feld können Sie eine Langbeschreibung Ihres Lagerartikels unterbringen. Bei der Neuanlage wird der Langtext des Händlerartikels vorgeschlagen. Sie können diesen Langtext nach eigenen Wünschen abändern. Der Langtext kommt nur dann zum Einsatz, wenn Sie dies auf einem Formular oder Etikett vorgesehen haben. Standardmäßig arbeitet unser Programm mit den Kurztexten.

[Bild] 4 Bemerkung: In diesem Memofeld können Sie zu dem Artikel bis zu 32.000 Zeichen Anmerkung eintragen. Wir haben dieses Feld für hausinterne Anmerkungen konzipiert. So kann dort z. B. eingetragen werden, dass der Artikel immer bei Sonderaktionen eingekauft wird, direkt beim Hersteller bezogen wird oder ähnliches. Dies Feld wird standardmäßig auf keinem Ausdruck angezeigt. Wenn Sie es wünschen, können die Ausgaben selbstverständlich daraufhin angepasst werden.

[Bild] 5 Erste Zuordnung + Katalog: In diesem Feld wird die Artikelnummer des ersten zugeordneten Artikels angezeigt. Die Anzeige erfolgt erst nach dem Abspeichern eines Artikels.

[Bild] 6 Gesamtmenge, Mindestbestand, Bestellvorschlag: Hier werden die gesamten Mengen des Artikels über alle Lager hinweg angezeigt.

[Bild] 7 Einheit: Tragen Sie hier die Einheit wie Stck., lfdm. usw. für den Artikel ein

[Bild] 8 Preise: Hier wird der Bruttopreis aus den Stammdaten des Haupthändlers gezeigt und die Eingabe des Einkaufswertes ermöglicht. Der Einkaufswert wird nur für die Ermittlung des Lagerwertes verwendet. Wenn im Feld 13 (Bewerteten EK separat eingeben’) ein Kreuz gesetzt ist, kann ein speziell für diesen Artikel bewerteter Preis eingesetzt werden.

[Bild] 9 Letzte Bewegung: In diesem Feld wird die letzte Nutzung des Artikels angezeigt. Die letzte Nutzung kann sowohl eine Ein- oder Ausbuchung als auch eine Bestandskorrektur sein. Das Datum ist hier nicht änderbar. Es dient lediglich zur besseren Identifizierung von Ladenhütern.

[Bild] 10 Gruppe: Lagerartikel lassen sich verschiedenen Gruppen zuordnen. Die Gruppenzuordnung dient in erster Linie der Analyse. Ebenso ist es jedoch möglich, die Lagerartikel aufgrund der hier getroffenen Gruppenzuordnung auszudrucken. So können Preislisten nach Gruppen sortiert erstellt werden. Die Gruppenerfassung geschieht in der Hauptmaske unter dem Menüpunkt Option. Ein Artikel kann jeweils nur einer Gruppe zugeordnet werden. Die Anzahl der verwendbaren Gruppen ist unbegrenzt, Sie sollten sich jedoch im eigenen Interesse auf möglichst wenig Gruppen begrenzen. Statt für einen Artikel eine eigene Gruppe aufzumachen sollten Sie dann lieber eine Gruppe wie „Diverse“ oder „Restliche“ anlegen.

11 Tabelle: Die Tabelle dient nur der Anzeige der bereits auf einem Lager erfassten Artikel.

[Bild]

[Bild] 12 Artikel bei Bestand 0 entfernen: Wenn Sie hier ein Kreuz einsetzen, so wird der Artikel bei einem 0-Bestand aus der Lagerliste entfernt. Dies Feld ist konzeptuell für die Ladenhüter vorgesehen, damit diese nicht immer wieder neu bestellt werden.

[Bild] 13 Bewerteten EK separat festlegen: Wenn Sie hier ein Kreuz einsetzen, so kann dem Artikel ein bewerteter Einkaufswert zu geordnet werden. Über diese Möglichkeit können Ladenhüter entsprechend abgewertet werden.

[Bild] 14 Eingabe einzelnes Lager: Da das Programm mit mehreren Lagern umgehen kann, erfolgt die Dateneingabe für jedes Lager in diesem Bereich und wird nach dem Speichern in der Tabelle Nr. 11 angezeigt. Mit einem Doppelklick auf einen Eintrag dieser Tabelle können die Daten korrigiert werden.

14-A Lager Projekt: Wählen Sie hier aus der Liste der angelegten Lager aus. Es werden nur die Projekte angezeigt, in deren Datenblatt das Kennzeichen ‚als Lager führen’ gesetzt ist.

14-B Lagerfach: In diesem Feld können Sie eine Beschreibung des Regalplatzes oder ähnlichem eingeben. Die Eingabe kann bis zu 20 Stellen lang sein.

14-C Bestand: Geben Sie in diesem Feld den Bestand Ihres Artikels. Sie können hier auch die Zahl 0 einsetzen, wenn Sie die ersten Bestände über ein Inventurdokument einlesen wollen.

14-D Mindestbestand: Aufgrund der hier eingetragenen Zahlen erarbeitet das Programm Bestellvorschläge. Sobald der Mindestbestand unterschritten ist, wird der Artikel in die Bestell- Vorschlagsliste aufgenommen.

14-E Bestellmenge: Tragen Sie hier die Menge für den Bestellvorschlag ein. Die Menge kann in der Bestellvorschlagsliste bei der Bearbeitung wieder verändert werden. Bei der Erstellung eines Bestellvorschlages erstellt unser Programm lediglich ein Dokument, der mit den normalen Änderungsfunktionen bearbeitet werden kann. In dem Anmerkungsfeld der Artikel ist bei der Bearbeitung der Vorschlagsliste jeweils der Bestand und Mindestbestand sichtbar. Sie können also bei der Bearbeitung für jeden Artikel die tatsächliche Bestellmenge Ihren Wünschen anpassen.

14-F bis 14-H: Mit diesen Knöpfen steuern Sie die Eingabe. Beim Speichern werden nur die Eingaben für das jeweilige Lager gesichert – zuletzt muss der Gesamtartikel noch mit dem Knopf Nr. 17 abgespeichert werden.

[Bild] 15 Neuer Artikel: Durch Betätigen dieses Knopfes können Sie einen neuen Artikel anlegen.

[Bild] 16 Artikelzuordnung: Sobald ein Artikel gespeichert ist, erscheint unten ein weiterer Knopf mit ‚Artikel Zuordnung’. Über ihn lassen sich weitere Großhändlerartikel dem aktuellen Lagerartikel zuordnen. Sobald dann eine Bestandsänderung des Großhändlerartikels aktiviert wird, wird der entsprechende Lagerartikel verändert. Die genaue Funktion dieses Bereiches lesen Sie im folgenden Kapitel Artikelzuordnung.

[Bild] 17 Speichern: Bei der Neuanlage oder Änderung eines Artikels muss dieser Knopf betätigt werden, um die Änderungen in den Stammdaten dauerhaft zu vollziehen.

[Bild] 18 Ende: Durch Betätigen dieses Knopfes wird die Maske verlassen.
