# Buchen der Artikel

Pfad: Materialwirtschaft > Bestellüberwachung [Modul] > 4. Wareneingang > Buchen der Artikel
Quelle: handbuch/buchen_der_artikel.htm

|

Buchen der Artikel

Schritt 2: Buchen der Positionen

Da die "Wareneingang buchen" Maske je nach Situation verschiedene Elemente an der Oberfläche zeigt, ist eine Beschreibung schwierig. Es gibt 4 Grundsituationen, in denen an der Oberfläche sichtbare Felder wechseln. Dies sind die Situationen

- mit Bestelldokument

- ohne Bestelldokument sowie

- eine Lagerbuchung

- oder Projektbuchung.

Obwohl bei Labelwin über die Dokumentenverwaltung ein Lager auch als Projekt geführt wird, unterscheiden wir hier wirklich die Lager- und die Baustellen-Projekte.

Wenn eine schriftliche Bestellung aus Labelwin heraus vorliegt, so bietet das Programm eine Position nach der anderen zur Einbuchung an. Mit einem Doppelklick kann dann der Artikel gewählt werden.

Als Menge wird immer die noch offene Menge der Bestellung angeboten. Falls der entsprechende Artikel vorher bereits einmal eingebucht wurde, wird nur noch die Restmenge vorgeschlagen. Wenn eine Position bereits einmal mit der kompletten Menge gebucht wurde, wird diese normalerweise nicht mehr vorgeschlagen. Über eine Einstellung in der vorigen Maske (Erledigte Positionen) können zu Korrekturzwecken auch bereits gelieferte Positionen einbezogen werden.

Wenn eine Bestellung komplett erfasst wurde, also alle Mengen entsprechend der Bestellmenge eingebucht wurden, verschwindet die Bestellung aus der Liste der offenen Bestellungen.

Wareneingang auf Lager buchen

Hierauf gehen wir in der Beschreibung des Lagermoduls ein.

Wareneingang auf Projekt (nicht Lager)

[Bild: Buchen der Artikel]

Bild: Wareneingang buchen

|
[Bild: 1]

Bestellnummer und weitere Grunddaten

[Bild: 1. Bestellnummer und weitere Grunddaten]

Im Kopf dieser Maske werden die diesem Wareneingang zugrunde liegenden Werte gezeigt. Eine Veränderung ist nicht möglich.

|
[Bild: 2]

Wareneingang für

[Bild: 2. Wareneingang für]

Hier wird festgelegt, ob die Bestellung als Wareneingang für ein Lager, ein (Baustellen-) Projekt oder auf ein Projekt und ein Lager gebucht werden sollen. Die gebuchten Daten werden in einen Eingangslieferschein übertragen.

|
[Bild: 3]

Auftrag / Projekt

[Bild: 3. Auftrag / Projekt]

So wie Sie bei einer Lagerbuchung zwingend ein Lager wählen müssen, wird hier zwingend ein Projekt verlangt. Bei einer schriftlichen Bestellung wird das Projekt vorgeschlagen, in dem auch die Bestellung liegt. Sie können hier zusätzlich auch noch einen Kundendienst-Auftrag auswählen, wenn die ausgelöste Bestellung für einen Kundendienstauftrag erfolgt ist. Damit wird ein separater Eingangslieferschein für den Kundendienstauftrag angelegt. Dieser ist in der KD-Verwaltung als zugehöriges Dokument sichtbar und kann als Vorlage bei der Rechnungsschreibung genutzt werden.

|

Tipp: Beim Buchen des Wareneinganges auf einen Kundendienstauftrag kann automatisch ein Materialzettel angelegt oder ergänzt werden. Speziell für einen KD-Auftrag gekauftes Material steht damit dem Mitarbeiter auf der Baustelle beim mobilen Kundendienst oder bei Druck auf Papier zur Verfügung. Diese Funktion kann Ihnen das Zusammenkopieren von Eingangslieferscheinen oder gar die manuelle Erfassung ersparen.

Da nun je nach bisheriger Verfahrensweise diese Funktion zu doppelten Einträgen führen kann, muss sie bewusst aktiviert werden. Dies geschieht im Modul EINSTELLUNGEN unter [Programmbereiche - Lager].

Bitte beachten Sie, das die Funktion keine bereits vorhanden Eingangslieferscheine automatisch in den Materialzettel kopiert.

|

[Bild]

|
[Bild: 4]

Suche (Lagerartikelnummer)

[Bild: 4. Suche (Lagerartikelnummer)]

Wenn die Lagernummer nicht bekannt ist, so können Sie sie hier suchen.

Geben Sie einfach ein oder mehrere mit Leerstellen getrennte Suchbegriffe ein und betätigen die Enter-Taste oder den Knopf ‚Suchen’. Gibt es mehrere Artikel mit dem Suchbegriff können Sie über den Knopf ‚Weitersuchen’ zum nächsten Artikel springen. Mit einem Doppelklick oder der Ok-Taste übernehmen Sie die Lager-Artikelnummer.

|
[Bild: 5]

Liste der Bestellartikel

[Bild: 5. Liste der Bestellartikel]

Um aus der Bestellung eine Position heraus zu suchen, wird über diesen Knopf die komplette Liste der n der Bestellung noch offenen Positionen gezeigt. Durch eine Doppelklick oder die Markierung und den Okay-Knopf wird eine Position zum Wareneingang übernommen.

|
[Bild: 6]

Pos.-Nr.

[Bild: 6. Pos.-Nr.]

Wenn Sie mit der Mengenüberwachung arbeiten wollen, sollten Sie hier die Positionsnummer Ihrer ‚Projektbasis’ eintragen. Nur wenn die Positionsnummer einheitlich verwendet wird, können die Mengen von ‚bestellt, geliefert, aufgemessen, berechnet’ usw. verglichen werden. Da die Nummer aus der Bestellung durchgereicht wird, sollten Sie schon bei der Bestellung die Nummer der Basis beibehalten.

|
[Bild: 7]

Artikel Nr. u. Händler

[Bild: 7. Artikel Nr. u. Händler]

Mit Hilfe des Händlers und der Artikelnummer (Feld 9) versucht das Programm den Lagerartikel zu finden. Wenn der Artikel mit einem Lagerartikel verknüpft ist, so wird die Lagernummer automatisch herausgesucht und der Bestand gezeigt. Die Daten werden in den Eingangslieferschein eingetragen. Bei einer mündlichen Bestellung kann mit diesen Informationen der Text für den Eingangslieferschein (Nr. 14) vorgeschlagen werden.

|
[Bild: 8]

Preis

[Bild: 8. Preis]

Wenn Sie hier einen Preis eingeben, wird dieser im Protokoll registriert. Er ist nicht zwingend erforderlich. Als Vorschlag wird der Bestellpreis eingesetzt. Dieser Preis wird als Einkaufswert im Eingangslieferschein verwendet. Es kommt jedoch vor, dass Sie auf den Gesamtpreis einen Rabatt erhalten haben. Dann tragen Sie diesen Preis bei ‚Gesamt’ ein, das Programm errechnet dann automatisch daraus den Einzelpreis.

|
[Bild: 9]

EK in Bestellung

[Bild: 9. EK in Bestellung]

Hier werden die EK-Preise gezeigt, mit denen die Bestellung geschrieben wurde.

|
[Bild: 10]

Stamm EK 1 u. EK 2

[Bild: 10. Stamm EK 1 u. EK 2]

Hier werden Ihnen die Ek-Preise aus den Händlerstammdaten angezeigt.

|
[Bild: 11]

UGL-Datei verarbeiten

[Bild: 11. UGL-Datei verarbeiten]

Wenn Sie mit UGL-Dateien Ihres Großhändlers arbeiten, werden diese durch Betätigen dieses Knopfes entsprechend verarbeitet.

|
[Bild: 12]

Eingang Menge

[Bild: 12. Eingang Menge]

Geben Sie hier die gelieferte Menge ein. Vorgeschlagen wird die noch offene Liefermenge.

|
[Bild: 13]

Rest stornieren

[Bild: 13. Rest stornieren]

Dies ist die einzige Möglichkeit, auf den Wareneingang einer einzelnen Position oder einer Teilmenge zu verzichten. Ansonsten bleibt die Bestellung so lange als offen stehen, bis alle Mengen eingegangen sind. Wenn Sie eine Position komplett kippen wollen, so stellen Sie die Menge auf Null und setzen diesen Schalter. Wenn Sie eine Menge kleiner als die Bestellmenge eingeben, so wird durch diesen Schalter auf den Rest verzichtet. Intern wird übrigens die Bestellmenge so reduziert, dass sie ausgebucht werden kann. Auch bei einer Menge Null erfolgt die Eintragung im Eingangslieferschein.

|
[Bild: 14]

Einheit

[Bild: 14. Einheit]

Hier wird Ihnen die Einheit des zu buchenden Artikels angezeigt, wie z.B. Stck., lfdm. usw.

|
[Bild: 15]

Artikeletikett

[Bild: 15. Artikeletikett]

Legen Sie hier fest, ob Sie für den gebuchten Artikel ein Artikeletikett drucken möchten.

|
[Bild: 16]

Preisetikett

[Bild: 16. Preisetikett]

Wenn Sie diese Optionen aktivieren, können Sie für den gebuchten Artikel Preisetiketten drucken. Durch die Aktivierung öffnet sich ein weiteres Feld, in dem die Stückzahl der Etiketten eingetragen wird.

|
[Bild: 17]

Buchen

[Bild: 17. Buchen]

Obwohl an der Oberfläche nicht sichtbar passiert hier ein Menge:

Bei Lagerbuchung:

Prüfung, ob alle wichtigen Daten ausgefüllt sind (Lagernummer vorhanden, Menge ungleich Null, der Preis darf Null sein). Ggf. wird die Buchung abgewiesen.

Wenn der Artikel zwar im Lager angemeldet, aber im gewählten Lager bisher nicht geführt wird, erfolgt eine Warnung mit der Möglichkeit, in dort anzumelden.

Die Lagerbuchung wird ausgeführt.

Immer:

Prüfung, ob im (Lager-) Projekt bereits ein Eingangslieferschein mit dieser Lieferadresse, der Lieferscheinnummer und dem Lieferscheindatum vorhanden ist. Wenn nicht, wird dieser angelegt.

Der Artikel wird in dem Eingangslieferschein an das Ende angehängt.

Bei schriftlicher Bestellung:

In der Bestellung wird der Liefereingang für die gewählte Position entsprechend erhöht.

Wenn in der Bestellung keine Fehlmengen mehr vorhanden sind, erfolgt ein Hinweis und die Wareneinbuchung wird beendet.

Es wird automatisch die nächste Position angefahren und zur Buchung angeboten.

|
[Bild: 18]

Artikeltext für Eingangslieferschein

[Bild: 18. Artikeltext für Eingangslieferschein]

Da bei der Buchung automatisch ein Eingangslieferschein geschrieben wird, benötigt das Programm einen Artikeltext. Dieser wird möglichst aus der Bestellung vorgeschlagen, er kann aber auch verändert werden.

|
[Bild: 19]

Freie Erfassung

[Bild: 19. Freie Erfassung]

Anstatt die Artikel der Bestellung zu nehmen, können Sie über diesen Knopf auch eine freie Erfassung vornehmen.

|
[Bild: 20]

Rest einbuchen

[Bild: 20. Rest einbuchen]

Alle noch offenen Positionen der Bestellung werden mit den Bestellmengen gebucht. Diesen Vorgang können Sie nicht mehr rückgängig machen. Sie haben nur die Möglichkeit, Korrekturbuchungen mit negativen Mengen vorzunehmen

|
[Bild: 21]

Ende

[Bild: 21. Ende]

Mit diesem Knopf verlassen Sie die Erfassung, wenn die Bestellung noch nicht komplett erledigt ist. Sobald sie keine offenen Positionen mehr enthält wird sie automatisch verlassen.
