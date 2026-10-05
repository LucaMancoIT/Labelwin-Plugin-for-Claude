# 4. Wareneingang (Lager)

Pfad: Materialwirtschaft > Lager [Modul] > 4. Wareneingang (Lager)
Quelle: handbuch/4__wareneingang__lager_.htm

|

4. Wareneingang (Lager)

Unabhängig davon, ob eine Bestellung mündlich oder über ein in Labelwin hinterlegtes Bestelldokument erfolgt, können die Waren hier eingebucht werden.

Bei der Buchung auf ein Lager können nicht vorhandene Artikelnummern ‚nebenher’ im Lager angemeldet werden.

Die Erfassung von Wareneingang besteht im Grunde aus zwei Schritten:

(1) Zuerst muss die Bestellung, zu der Ware eingegangen ist, ausgewählt werden (bzw. festgelegt werden, dass keine Bestellung in Labelwin existiert)

(2) und dann müssen die gelieferten Positionen und Mengen eingetragen werden.

(3) Optional kann abschließend der Kunde über den Wareneingang informiert werden (> Kunde informieren).

Schritt 1: Bestellung suchen / keine schriftliche Bestellung

Beim Wareneingang muss zunächst festgelegt werden, ob die Bestellung schriftlich aus Labelwin heraus oder telefonisch ohne Bestelldokument erfolgt ist.

Bei einer mündlichen Bestellung (also ohne Labelwin Bestelldokument) entfällt im Wesentlichen nur die Vorgabe der Daten aufgrund der Bestellung.

[Bild]

Eine detaillierte Beschreibung der Maske "Wareneingang" erfolgte bereits im Kapitel Bestellüberwachung. Sollten einzelne Punkte der Maske nicht direkt verständlich sein, schauen Sie bitte im Kapitel Bestellüberwachung - Wareneingang nach.

Schritt 2: Buchen der Artikel:

Da die "Wareneingang buchen" Maske je nach Situation verschiedene Elemente an der Oberfläche zeigt, ist eine Beschreibung schwierig. Es gibt 4 Grundsituationen, in denen an der Oberfläche sichtbare Felder wechseln. Dies sind die Situationen mit und ohne Bestelldokument sowie eine Lager- oder Projektbuchung. Obwohl bei Labelwin über die Dokumentenverwaltung ein Lager auch als Projekt geführt wird, unterscheiden wir hier wirklich die Lager- und die Baustellen-Projekte.

Wenn eine schriftliche Bestellung aus Labelwin heraus vorliegt, so bietet das Programm eine Position nach der anderen zur Einbuchung an. Mit einem Doppelklick kann dann der Artikel gewählt werden.

Als Menge wird immer die noch offene Menge der Bestellung angeboten. Falls der entsprechende Artikel vorher bereits einmal eingebucht wurde, wird nur noch die Restmenge vorgeschlagen. Wenn eine Position bereits einmal mit der kompletten Menge gebucht wurde, wird diese normalerweise nicht mehr vorgeschlagen. Über eine Einstellung in der vorigen Maske (Erledigte Positionen) können zu Korrekturzwecken auch bereits gelieferte Positionen einbezogen werden.

Wenn eine Bestellung komplett erfasst wurde, also alle Mengen entsprechend der Bestellmenge eingebucht wurden, verschwindet die Bestellung aus der Liste der offenen Bestellungen.

Eine detaillierte Beschreibung der Maske "Wareneingang buchen" erfolgte ebenfalls bereits im Kapitel Bestellüberwachung. Sollten einzelne Punkte dieser Maske nicht verständlich sein, schauen Sie bitte im Kapitel Bestellüberwachung - Buchen der Artikel nach. Hier sollen daher nur die Felder beschrieben werden, die nur bei Einsatz des Lagermoduls vorhanden sind.

(1) Wareneingang auf Lager:

[Bild: 4. Wareneingang (Lager)]

|
[Bild: 1]

Lagernummer

[Bild: 1. Lagernummer]

Geben Sie hier die Nummer ein, unter dem der Artikel im Lager geführt wird. In der Abbildung ist die Nummer identisch mit der Artikelnummer des Großhändlers. Das ist jedoch nicht zwingend so, da Sie die Nummer unabhängig von der Großhändlernummer vergeben können. Wenn der einzubuchende Artikel mit einem Lagerartikel verknüpft ist (Thema ‚Zuordnungen’) wird die Lagernummer automatisch vorgeschlagen. Mit dem Knopf ‚Suchen’ (Nr. 14) können Sie einen Lagerartikel aufgrund von Textbestandteilen suchen.

|
[Bild: 2]

Anzeige Lagerartikel

[Bild: 2. Anzeige Lagerartikel]

Durch diese Anzeige wird signalisiert, dass der Großhändlerartikel mit dem Lager verknüpft ist.

|
[Bild: 3]

Bestand

[Bild: 3. Bestand]

Hier wird der Bestand des Lagers angezeigt, auf das Sie die Buchungen vornehmen. Bei Gesamt wird Ihnen der Gesamtbestand des Artikels über alle Lager angezeigt.

|
[Bild: 4]

Lagerfach

[Bild: 4. Lagerfach]

Hier wird das Lagerfach des Artikels im Lager angezeigt.

|
[Bild: 5]

Neuer Lagerartikel

[Bild: 5. Neuer Lagerartikel]

Mit diesem Knopf kommen Sie in die Neuanlage. Die Funktionalität ist exakt die gleiche, wie bei der Neuanlage von der Hauptmaske aus.

|
[Bild: 6]

Neue Zuordnung

[Bild: 6. Neue Zuordnung]

Mit diesem Knopf können Sie zwischen einem Großhändlerartikel und einem bereits im Lager angemeldeten Artikel eine neue Verknüpfung aufbauen. Von da an findet das Programm auch bei der Eingabe dieser Nummer den Lagerartikel und den Bestand. Die Funktionalität ist exakt die gleiche, als wenn Sie über die Hauptmaske mit ‚Artikel Verknüpfung’ eine weitere Verknüpfung aufbauen.

(2) Wareneingang auf Projekt (nicht Lager)

Der Wareneingang auf ein Projekt ist nur dann möglich, wenn Sie im Modul EINSTELLUNGEN unter dem Menüpunkt <Programmbereiche> <Lager> das Feld ‚Lagerartikel zwingend auf Lager buchen’ nicht aktiviert haben.

Im Wesentlichen sind die Eingaben ähnlich der oben beschriebenen Lagerbuchung. Wir verzichten hier deshalb auf eine genaue Beschreibung. Im Kapitel Bestellüberwachung - Buchen der Artikel ist dieser Fall genau erläutert.

(3) Wareneingang Lager + Projekt

Dieser Punkt ist nur anwählbar, wenn Sie zuvor im Modul EINSTELUNGEN unter dem Menüpunkt <Programmbereiche> <Lager> das Feld ‚Ja, auch auf Lager buchen’ aktiviert haben. Dadurch werden Projektbestellungen auch auf das Lager gebucht.

[Bild]

Beispiel: Der Wareneingang wird nur über das Projekt gebucht. Beim Lieferschein- oder Rechnungsdruck wird jedoch vom Lager abgebucht. Damit ist der Buchungsbestand geringer als der tatsächliche Bestand, und es wird zu früh nachbestellt.

Wenn Sie jedoch auf Lager + Projekt buchen aktivieren, wird in jedem Fall auf das Lager gebucht und somit eine zu früh ausgelöste Bestellung verhindert.

[Bild]

(4) Wareneingang Lager, ohne hinterlegte Bestellung

Bei einer solchen Bestellung entfällt im Wesentlichen nur die Vorgabe der Daten aufgrund der Bestellung.

[Bild]

Bei einer Lagerbuchung muss zwingend die Lagernummer eingegeben oder gesucht werden. Der Text wird dann aus dem Lagerartikel genommen. Wie zuvor beschrieben kann auch hier über den Großhändler und dessen Artikelnummer ein Lagerartikel gefunden werden.

[Bild]
