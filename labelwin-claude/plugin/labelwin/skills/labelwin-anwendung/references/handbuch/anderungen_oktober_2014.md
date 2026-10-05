# Änderungen Oktober 2014

Pfad: Updatetexte (bisher) > Update 2015 > Änderungen Oktober 2014
Quelle: handbuch/anderungen_oktober_2014.htm

|

Änderungen Oktober 2014

Excelausgabe für Aus- und Eingangsrechnungen für Steuerberater mit PDF

Damit der Steuerberater die Daten besser überprüfen kann und Zugriff auf den Ausdruck der Rechnungen hat, wurde die Funktion der Übergabe an Excel geschaffen. Wenn im Excel eine Rechnung markiert wird, kann die PDF per Knopf angezeigt werden. Da alle relevanten Informationen in der Tabelle sind, kann auch nach Konto eingegrenzt werden. Interessant kann dieser Weg auch bei einer Steuerprüfung sein, weil Sie alle Informationen herausgeben können, ohne das der Prüfer in Ihr System muss. Sie finden den Menüpunkt im Modul RECHNUNGSEINGANG unter <Auslagern>, <PDF-Archiv auslagern>.

Der Ausgabezeitraum kann eingegrenzt werden. Die Exceltabelle wird zusammen mit den PDF’s in einem Verzeichnis abgelegt, dass dann z.B. per USB-Stick befördert werden kann. Wegen der Größe ist ein Transport per Email nicht möglich.

Rechte: Da damit ein schneller Zugriff auf wichtige Firmeninformationen möglich ist, kann die Ausgabe über ein spezielles Recht eingegrenzt werden. Normalerweise wird aber die übliche Eingrenzung auf ‚Arbeiten im Rechnungseingang‘ genügen. Das neue Recht ist in der Rechtevergabe unter ‚Auswertungen‘ zu ändern.

Scan-Archiv, scannen hinter Dokumente eines Kundendienstauftrages

Bei geöffneter Dokumentenliste eines Kundendienstauftrages kann nun ein Scan direkt hinterlegt werden. Anzuwählen ist die Funktion über das Menü oder F12.

Hintergrund: Wenn ein Angebot über einen KD-Auftrag erstellt worden ist, kann nun der unterschriebene Auftrag einfach hinterlegt werden. Gleiches gilt für ein Abnahmedokument.

Sie können das Dokument mit Word erstellen und das unterschrieben Dokument dahinter scannen.

Scan-Archiv, Anzeige bei der Artikelliste der Eingangslieferscheine

Die Anzeige von gescannten Eingangslieferscheinen ist nun als Menüpunkt oder mit Strg + F4 möglich.

Kundendienst, Warnung bei auffällig langen Terminen jetzt variabel

Bisher kam immer dann eine Warnung, wenn ein Kundendienstauftrag länger als 28 Tage geplant wurde. Im Grunde genommen ging es darum, Tippfehler zu verhindern. Bevor wir diese Warnung eingeführt haben, konnte ein Tippfehler beim Jahr das System für einige Minuten stilllegen. Da man es aber nie Allen Recht machen kann, mussten wir die Warnschwelle frei einstellbar machen.

Die Warnung kommt nun standardmäßig bei mehr als 20 Tagen, kann aber im Einstellmodul für die Firma selbst festgelegt werden. Eine kürzere Warnschwelle als 5 Tage ist nicht einstellbar.

Kassenbuch, Anzeige des Projektnamens

Bisher war nach der Eingabe einer Projektnummer der Projektname nicht sichtbar. Ein Tippfehler konnte damit nicht auffallen, nun merkt man es sicherlich.

Rechnungseingang / Adressen, neue Zahlungsziel möglich

Neben der normalen Eingabe von Zahlungszielen in Tagen gibt es gewisse Tricks, um Zahlungsziele wie ‚Immer am 15. des Folgemonats‘ einzutragen. Diese Tricks sind nun um eine weitere Variante erweitert worden. Ob außer dem konkreten Fall noch weitere Lieferanten so komische Bedingungen haben, können wir nicht einschätzen – deshalb hier die Dokumentation:

Mit einem Eintrag von 3015 wird erreicht, dass alle Rechnungen mit Datum vor dem 15ten am 30ten bezahlt werden müssen. Alles nach dem 15ten bis einschließlich 30ten wird am 15ten des Folgemonats gezahlt. Nach dieser Logik kommen also Zahlungsfristen zwischen 15 und 30 Tagen zum Einsatz. Falls das jemand braucht – auch mit 2814 würde das funktionieren.

Da man sich so etwas kaum merken kann, bekommen Sie die Info mit dem kleinen Hilfeknopf in der Adressmaske bei dem Erfassen der Zahlungsziele.

Werkzeugverwaltung

Wenn bisher ein Werkzeug gesucht wurde, musste entweder die komplette Nummer bekannt sein, oder man musste sich über die Gruppe ran tasten. Wenn Sie eine Logik über den Anfang der Inventarnummer aufgebaut haben, können Sie nun auch einfach den Anfang tippen und Enter betätigen. Übrigens kann die Inventar’Nummer‘ auch Buchstaben enthalten. Wer die Nummer im Nachhinein ändern will, kann dies problemlos machen.

[Bild]

Werkzeugverwaltung, Warnung bei Projektstatus ‚erledigt‘ und fehlendem Werkzeug

Wenn bei der Umsetzung des Projektstatus auf ‚erledigt‘ noch Werkzeug ausgeliehen ist, erscheint nun ein Warnhinweis.

Beim Wartungstermin hinterlegtes Material in Rechnung übernehmen

Bei der automatischen Anlage von Aufträgen aufgrund von Wartungsterminen werden Materialien als Materialzettel hinterlegt. Bei der manuellen Auftragsanlage mit gewähltem Wartungstermin bestand diese Möglichkeit bisher nicht. Nun kann in der Maske des Artikelaufrufs unter <Vorlage> das Material in die Rechnung oder einen Materialzettel übernommen werden. Der Zugriff erfolgt dann über den beim Auftrag gewählten Wartungstermin.

Wartungstermine selektieren, Termine sofort weitersetzen

Bisher wurde ein Wartungstermin erst weiter gesetzt, wenn der Kundendienstauftrag auf erledigt gesetzt wurde. Dieses Verfahren hat 3 Nachteile:

-

Wenn die Aufträge schon für einige Monate im Voraus erzeugt worden sind und neue Termine über neue Verträge entstehen, ist die Selektion sehr schwierig. Sie ist zwar möglich, aber nur schwer verständlich.

-

Wenn ein Mitarbeiter die Frage mit ‚Termin weitersetzen‘ falsch beantwortet (vielleicht weil er sie nicht versteht), wird der Termin nicht weiter gesetzt, obwohl die Wartung ausgeführt wurde.

-

Im mobilen Kundendienst wird die Frage ggf. vom Kundendiensttechniker beantwortet, der dies eventuell falsch entscheidet.

Auslöser der beschriebenen Entwicklung war eine Firma, bei der viele Wartungstermine falsch waren, weil die Termine nach der Ausführung nicht umgesetzt worden sind.

Nun können die Termine sofort bei der Erzeugung der Aufträge umgesetzt werden. Dazu müssen Sie aber im Modul Einstellungen in den Kundendienst Grundeinstellungen einen Schalter setzen. Obwohl wir die neue Methode für besser halten, können wir diese für die Betriebe, die sich auf die alte Methode festgelegt haben, nicht einfach ändern. Für die Übergangszeit gibt es bei einer Umstellung keine Probleme, da ein KD-Auftrag ‚weiß‘, ob sein Wartungstermin schon weiter gesetzt worden ist. Wenn das der Fall ist (neue Methode) wird in der Maske nur noch für die Erfassung von Zusatzarbeiten gezeigt, die bei der nächsten Wartung erledigt werden sollen.

Auch wenn Sie einen Wartungstermin manuell wählen (statt per Selektion) kann der Termin sofort weiter gesetzt werden.

Umkalkulation von Stundenlohn-Positionen ermöglicht

In der Umkalkulation können in der Maske 'Andere Multis' nun auch Stundenlohnpositionen geändert werden.

UGL einlesen, Einstellung ‚Langform‘ wurde nicht berücksichtigt

Wenn eine Artikelliste vom Lieferanten per UGL kam, wurde das Kennzeichen ‚Langform‘ aus der Kalkulationseinstellung nicht berücksichtigt. Diese Änderung bedeutet für jene, die die Artikel weiterhin in Kurzform übernehmen möchten, dass sie die Kalkulationseinstellung (F11) ggf. vorher ändern müssen.

Kundendienst, Planquadrat auf Erfassmaske sichtbar

Wer mit Planquadraten arbeitet, kann dieses jetzt schon bei der Erfassung eines Auftrages sehen. Angezeigt wird es hinter dem Suchwort der Objektadresse. Besonders deutlich wird die Zone, wenn Sie entsprechende Farben zugeordnet haben.

Kundendienst-Checkliste, Knopf zum Bearbeiten der Karteikarte

Um beim Ausfüllen / Ankreuzen der Checkliste schnell mal eine Änderung in der Karteikarte vornehmen zu können, gibt es nun einen Knopf zum Öffnen der Anlagen-Karteikarte. Natürlich nur dann, wenn die Checkliste zu einer Anlage gehört.

Hintergrund: Gerade im mobilen Kundendienst per Tablett-PC sollten möglich schnell Änderungen möglich sein.

Liste der Dokumente mit unterschiedlichen Farben

Im Einstellmodul können Sie nun für jede Dokumentenart eine Farbe festlegen. Im Projekt sehen Sie dann die Dokumente in der gewählten Farbe. Da diese Farben nur in der V5-Version konsequent zum Einsatz kommen, kann es sein, dass Sie an manchen Stellen die Dokumente ohne die Farbkennzeichnung sehen. Die Farben werden zwar standardmäßig für die ganze Firma festgelegt, aber können auch für jeden Mitarbeiter abgeschaltet oder individuell anders festgelegt werden. Sobald Sie die Firmenfarben festgelegt haben, sind diese als Standard bei allen Anwendern sichtbar. Die Einrichtung erfolgt im Modul Einstellungen unter den Menüpunkten <Programmbereiche>, <Dokumentenerstellung>

, <Grundeinstellung>

[Bild]

Mit dem Knopf ‚Farben‘ gelangen Sie in die eigentliche Festlegung.

[Bild]

Eine Farbeinstellung kann durchaus auch Nachteile haben. Wenn alles schrecklich bunt ist, kann das auch stören. Farbe erhöht nicht automatisch die Übersichtlichkeit.

Controlling-Modul, Kalkulationen mit Excel, Export und Import

Wenn bei Ihnen das Controlling-Modul im Einsatz ist, können Sie nun auch Angebote und sonstige Dokumente mit Artikeln in eine Exceldatei exportieren.

Obwohl Labelwin alle Änderungen der Kalkulation komfortabel über die Schnelländerung, die Blockbearbeitung und die ‚große‘ Umkalkulation ermöglicht, gibt es Situationen, in denen die Erfassung und Änderung mit Excel sinnvoll ist. Beim Export werden alle Daten in eine Mustertabelle eingetragen. Je nach Muster können dort bestimmte Kalkulationsdaten erfasst oder geändert werden. So kann man z.B. die Einkaufspreise eintragen, die Lohnminuten oder auch den gewünschten Verkaufspreis. Beim späteren Import wird festgelegt, welche Felder in das Dokument zurückgeholt werden. Wenn ein Dokument kopiert wird, ist es auch möglich die Preise in die Kopie einzutragen.

Hintergrund der Entwicklung:

- Das Angebot kann als Exceltabelle zur Auftragsvergabe mitgenommen werden.

- Ein Mitarbeiter ist nicht in der Lage, Labelwin zu bedienen und kann aber gut kalkulieren (ja, solche Leute gibt es)

- Man kann die Einkaufspreise von einer Hilfskraft eintragen lassen, die Labelwin nicht beherrschen muss.

- Die Eingabe der Preise und Minuten ist so sehr übersichtlich und schnell möglich

- Ein Subunternehmer soll seine Preise selber eingeben

- Man kann verschiedene Kalkulations-Vorgänge durchspielen, ohne sich um Sicherungen Gedanken zu machen

Angewählt wird der Export in der Projektverwaltung unter den Menüpunkten <Extern>, <Kalkulation Excel-Export>, der Import mit dem Menüpunkt darunter < Excel-Kalkulation importieren>

|

Die ausführliche Beschreibung finden Sie im Bereich Handbuch unter Kalkualtion mit Excel.

Ladenkasse, Druckausgabe an A4-Drucker anwählbar

Wenn die Ausgabe üblicherweise mit einem kleinen Bon-Drucker erfolgt, gibt es das Bedürfnis manchmal auf einem A4-Drucker zu drucken. Wer immer mit DIN A4 arbeitet, hat das Problem natürlich nicht.

Zum Umschalten musste bisher in den Grundeinstellungen das Formular und der Drucker umgesetzt werden und später wieder alles zurückgesetzt werden.

Umgestaltet wurden die Grundeinstellungen, damit man auf der ersten Seite das Formular und den neuen Drucker vorgeben kann. Die Druckmaske sieht auch etwas anders aus. Wir haben sie wesentlich übersichtlicher gestaltet und mit einem neuen Knopf für die neue Druckausgabe versehenen.

Neu ist auch ein Schalter in den Einstellungen, mit dem nach Eingabe einer Adresse auf die Kalkulationseinstellung dieser Adresse umgeschaltet wird. Es kann sein, dass der Schalter bei Ihnen schon immer gesetzt war aber er war nicht an der Oberfläche. Der Schalter befindet sich auf der Karteiseite 'Allgemein'. Lesen Sie ggf. mit dem kleinen Fragzeichen-Knopf den Hilfetext.
