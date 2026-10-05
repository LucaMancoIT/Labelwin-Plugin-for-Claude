# Seriennummern-Verwaltung [Modul]

Pfad: Artikelstammdaten > Seriennummern-Verwaltung [Modul]
Quelle: handbuch/seriennummern_verwaltung__modul_.htm

|

Seriennummern-Verwaltung [Modul]

Stand: 23.11.2018

(V5.87)

THEMA

|

Mit Seriennummern werden Produkte gekennzeichnet, um sie eindeutig zuordnen zu können. Damit haben Sie die Möglichkeit, bei einer möglichen Reklamation oder Rückgabe schnell zu erkennen, wann und bei wem Sie das Produkt erworben haben.

Die Funktion der Seriennummernverwaltung ist mit und ohne Lagerverwaltung nutzbar. Es gibt eine Tabelle der Seriennummern, in der unter der Artikelnummer und der Katalognummer beliebig viele Seriennummern eingetragen werden können. Jeder Eintrag hat einen Status ‚Vorhanden‘, ‚Ausgeliefert‘ oder ‚Defekt‘. Die Zugänge werden über den Wareneingang gebucht, können aber auch direkt über das Lager oder die Artikelstammdaten eingetragen werden. Die Abgänge werden je nach Einstellung beim Drucken der Rechnung oder beim Drucken des Lieferscheins (also ggf. auch Lagerentnahmen) gebucht.

Im Modul ADRESSEN können Sie nach einer bestimmten Seriennummer suchen. Damit finden Sie sehr schnell den Großhändler, bei dem Sie das Produkt gekauft haben und den Kunden, an den Sie das Produkt geliefert haben.

EINRICHTUNG

|

Die Seriennummern-Verwaltung ist ein kostenpflichtiges Modul und steht nur nach entsprechender Freischaltung zur Verfügung.

Zum einfacheren Testen kann es zunächst auch per Schalter in der Global.ini aktiviert werden.

Bereich [Grundeinstellungen1] (Mandant 1)

Eintrag: SeriennrAktiv=1

Über einen weiteren Schalter wird festgelegt, bei welcher Dokumentenart die Abbuchung der Seriennummern beim Drucken passiert. Auch Lagerentnahmen müssen gedruckt werden, damit die Nummern ausgetragen werden.

Bereich [Grundeinstellungen1] (Mandant 1)

Eintrag: SeriennrDoku =1 (Abbuchung bei Druck Lieferschein)

oder

Eintrag: SeriennrDoku =2 (Abbuchung bei Druck einer Rechnung, Abschlag usw.)

ANWENDUNG

|

Schritt 1: Kennzeichnen der Artikel mit Seriennummern-Verwaltung

Um einem Artikel Seriennummern zuordnen zu können, muss zunächst das Kennzeichen gesetzt werden. Dieses geschieht im Artikelstamm oder im Lagermodul.

|

Artikelstamm:

Nach Aufruf des Artikels finden Sie auf der Karteiseite ‚Zuordnungen‘ unten rechts ein Ankreuzfeld mit dem Sie kennzeichnen, dass dieser Artikel mit Seriennummern geführt werden soll.

[Bild]

|

Lager:

Im Lager in der Maske in der Lagerartikel angelegt und geändert werden.

[Bild]

Sobald die Daten in der Maske gespeichert sind, kann man mit dem Knopf ‚Seriennummern‘ die Nummern erfassen, ändern und ggf. auch löschen.

Schritt 2: Erfassen der Seriennummern

Bei allen Artikeln, die das Kennzeichen zur Seriennummern-Verwaltung haben, können die Seriennummern hinterlegt werden. Die Erfassung der Nummern kann entweder im Artikelstamm oder im Lager erfolgen.

Die Erfassmaske wird im nächsten Unterkapitel detailliert vorgestellt.

Hinweis: Beim Erfassen von Wareneingang (nur möglich mit dem Zusatzmodul LAGER oder BESTELLÜBERWACHUNG) erfolgt die Hinterlegung der Seriennnummern etwas anders - und zwar einfacher.

Sobald der Eingang von Artikeln mit dem Kennzeichen gebucht wird, erzwingt das Programm die Eingabe der Seriennummern. Damit dies schnell geht, ist es nicht erforderlich, diese Nummern in der Erfassmaske einzugeben, sondern kann direkt in der Maske des Wareneingangs erfolgen. Damit ist auch die Eingabe per Tastaturscanner möglich, wenn der Knopf ‚Text groß‘ gedrückt wird.

[Bild]

Schritt 3: Ausgang erfassen

Beim Artikelaufruf in der Dokumentenerfassung und in der Ladenkasse verlangt das Programm nach Aufruf eines Artikels mit Kennzeichen ‚Seriennummer‘ die Wahl der Nummern.

Die genauer Vorgehensweise wird im Unterkapitel Ausgang erfassen erklärt.

Schritt 4: Drucken

Bei der Druckausgabe erfolgt eine Prüfung, ob die Anzahl der Seriennummern mit der Menge in der Position übereinstimmt. Bei allen Positionen mit Seriennummern erscheint als letzte Zeile(n) das Wort "Seriennummer: …" und eine Komma getrennte Liste der Nummern. Das gleiche passiert in der Ladenkasse, wenn dort Artikel mit Seriennummern aufgerufen worden sind.

Beispiel:

[Bild]

Schritt 5: Suchen

Über das Modul ADRESSEN können Sie unter dem Menüpunkt [Suchen - Seriennummern suchen] gezielt nach einer Seriennummer suchen.

[Bild]

Sie erhalten die entsprechenden Informationen zur gesuchten Nummer. In unserem Beispiel wurde der Artikel ausgeliefert an Herrn Brackwede und es existiert hierzu ein Lieferschein.

[Bild]

Die Suchfunktion kann jederzeit genutzt werden, dürfte aber nur bei einer Reklamation wirklich interessant sein.
