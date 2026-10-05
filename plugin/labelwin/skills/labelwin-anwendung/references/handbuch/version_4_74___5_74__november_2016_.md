# Version 4.74 / 5.74 (November 2016)

Pfad: Updatetexte (bisher) > Update 2017 > Version 4.74 / 5.74 (November 2016)
Quelle: handbuch/version_4_74___5_74__november_2016_.htm

|

Version 4.74 / 5.74 (November 2016)

Versionswechsel auf 4.74 / 5.74 - Änderungen November 2016

Postbox-Verteiler mit Wareneingang

Mit der Postbox (gehört zum Modul Scan-Archiv) können nun auf Pdfs mit Eingangslieferschein als Wareneingang gebucht werden. In diesem Zusammenhang haben wir alle dort angebotenen Funktionen mit einem kleinen Hilfetext versehen, um die Handhabung zu erleichtern. Beim Knopf Wareneingang stehen die Hintergründe dieser neuen Funktion.

Manuell erfassten Set im Katalog speichern

Diese Routine wurde noch mal überarbeitet. Der Setkopf muss markiert werden und dann im ‚Rechte-Maustaste-Menü‘ der Punkt <Set in Katalog speichern> angewählt werden. Es startet die Maske der Artikelstammdaten und Sie können Änderungen vornehmen.

Angebotsnummer in Vor- und Nachbemerkungen

Wenn die Angebotsnummer verwendet werden soll, um dem Kunden z.B. nur eine Seite für die Auftragserteilung zur Verfügung zu stellen, war dies bisher nicht möglich. Nun wird bei Verwendung des Schlüsselwortes #nummer# die erst im letzten Moment gezogene Nummer in die Vor- oder Nachbemerkung eingetragen. Das gilt auch für Rechnungen und Auftragsbestätigungen, obwohl es dort sicherlich selten eingesetzt wird.

UGL-Datei einlesen, Merker bei Artikeln, die nicht in den Stammdaten sind.

Wenn Sie ein UGL-Angebot vom Großhändler einspielen, wollen Sie manchmal Daten aus den Stammdaten dazu mischen, wie z.B. die kalkulierten Minuten. Nun kann das Programm bei den Positionen, bei denen ein Artikel nicht in den Stammdaten ist, einen Merker setzen. Mit der Suchfunktion können Sie dann die Positionen mit gesetztem Merker anspringen, um diese manuell zu bearbeiten.

In der Maske der UGL-Auswahl finden Sie dazu das Ankreuzfeld ‚Merker setzen, wenn Artnr nicht vorhanden‘

Wartungsrechnungen an Mieter statt an Vermieter stellen

Bei Heizungsanlagen in Mietwohnungen kommt es immer wieder vor, dass der Mieter die Wartung der Heizung selber bezahlen muss. In der Terminmaske können Sie nun ankreuzen, dass der Mieter diese Rechnung übernimmt. Bei der Selektion der Wartungstermine wird dann die Objektadresse auch als Rechnungsadresse gesetzt. Bei allen anderen Aufträgen wird weiterhin die hinterlegte Adresse des Vermieters genommen.

[Bild]

Positionserfassung / Bearbeitung mit diversen Änderungen

Hier haben einige Änderungen stattgefunden, die besonders für die Bearbeitung von Ausschreibungen interessant sind.

[Bild]

1) Mit dem neuen Knopf kann der komplette Langtext sichtbar geschaltet werden. Wenn kein Langtext vorhanden ist, steht dort der Kurztext (dann mit Überschrift ‚Kurztext‘. Diese Anzeige ist wichtig, wenn man z.B. per Änderungslauf Minuten oder Preise eingeben möchte

2) Neuer Knopf um alle Positionen bis auf die Set-Ebene ausklappen möchte. Damit bleiben nur die Bestandteile unsichtbar

3) Blockänderung: Hier sind einige Änderungen möglich, die aber weiterhin auch in der Blockbearbeitung zur Verfügung stehen. Es geht darum, den Positionen schneller z.B. einen Arbeitsbereich zuzuordnen. Man kann mehrere Positionen markieren und mit einem Doppelklick auf den Eintrag oder dem Knopf ‚Zuordnen‘ die Eigenschaft auf die Positionen übertragen.

4) Schnelländerung mit Alternativ, Eventual, Merker.

[Bild]

Diese Änderungsmöglichkeiten beim Durchlauf sind besonders bei Ausschreibungen interessant. Zusammen mit der erweiterten Suchfunktion können die Artikel sehr schnell geändert werden.

5) Erweiterte Suchfunktion

[Bild]

Die markierten Suchmöglichkeiten sind dazu gekommen, um Ausschreibungen schneller zu bearbeiten. Die Suchrichtung steht nun als Vorgabe auf Anfang. Beim Weitersuchen mit F3 geht die Suche selbstverständlich dann nach unten weiter.

Wer es nicht kennt: Angewählt wird die Suche mit Strg F

6) Artikelabgleich mit Übernahme aus anderem Dokument

Bei einer Ausschreibung können Angebote vom Lieferanten als UGL oder Gaeb zu den Positionen dazu gemischt werden. Diese Möglichkeit besteht schon lange. Dabei werden die Positionen der Ausschreibung in Sets gewandelt und die Artikel des Lieferanten als Setbestandteile eingefügt. Dieser Vorgang läuft aber auf einen Rutsch ab und man hat keine Möglichkeit, einzelne Bereiche auszulassen.

[Bild]

Mit der neuen Möglichkeit können Sie die UGL oder die Gaeb in ein neues Dokument einfließen lassen und dieser kontrollieren und ggf. bearbeiten. Erst danach wählen Sie den Artikelabgleich unter den Menüpunkten <Durchläufe>, <Artikelabgleich mit anderem Dokument> an. Nach dem Betätigen des Okay-Knopfes wählen Sie das andere Dokument, aus dem die Artikel übernommen werden sollen.

7) UGL einlesen, neues Ankreuzfeld ‚Preis aus Stammdaten nehmen‘

Bei gesetztem Haken wird geprüft, ob der per UGL gekommene Artikel auch in den Katalog-Stammdaten vorhanden ist. Wenn das der Fall ist, wird der Einkaufspreis und der Listenpreis nicht aus der UGL-Datei, sondern aus den Stammdaten verwendet. Diese Option ist nur dann sinnvoll, wenn Daten aus einer Schnittstelle z.B. einem Auslegungsprogramm per UGL übertragen werden. Bei Lieferantendateien dagegen sollen ja gerade die Preise aus der UGL-Datei verwendet werden.

Aufgaben, Vorgabetext aufgrund der gewählten Tätigkeit

Um auch die Textfelder einer neuen Aufgabe vor zu belegen, können Sie nun bei den Tätigkeiten Vorgaben hinterlegen. Sie kommen aber nur bei neuen Aufgaben zum Einsatz. Wählen Sie als erstes dann die Tätigkeit aus, werden die Texte eingetragen

Die Eintragung erfolgt im Modul Einstellungen unter den Menüpunkten <Programmbereiche>, <Aufgaben>,<Tätigkeiten>

[Bild]

Kundendienst, unterschiedliche Bausteine für Rechnung bei Privatkunden und Rechnungsadressen

Wenn eine Rechnung aus dem Kundendienst geschrieben wird, schägt das Programm einen Baustein für die Vorbemerkung der Rechnung vor. Dieser Baustein kann nun unterschiedlich sein, wenn beide Adressen des Auftrags identisch oder unterschiedlich sind. Bei Privatkunden ist es ja sinnvoll, einen Baustein zu verwenden, der nicht noch mal auf die Objektadresse hinweist.

Die Einstellung finden Sie im Modul Einstellungen unter den Menüpunkten <Programmbereiche>, <Kundendienst>, <Grundeinstellungen> im Bereich ‚Abrechnung‘

Kundendienst, Prüfen der Rechnung auf Mindestmulti oder Mindest-Deckungsbeitrag je Std.

Diese Faktoren können Sie im Einstellmodul unter den Kundendienst-Grundeinstellungen hinterlegen. Die Prüfung findet in der Druckmaske vor dem Rechnungsdruck statt. Wenn einer dieser Werte unterschritten wird, erfolgt eine Warnung. Zur Berechnung werden nur in dem Dokument verwendete Positionen verwendet und nicht z.B. die Zeiten aus der Zeitwirtschaft.

Wenn diese Werte auf 0 stehen (Vorgabe) erfolgt keine Prüfung.

Anmerkungen zu einer Ausgangsrechnung in der Dokumentliste möglich

Obwohl manche Anwender kein Recht im Rechnungsausgangsbuch haben, sollten sie Anmerkungen zu einer Rechnung schreiben können. Deshalb gibt es nun an allen Stellen, in denen das Textdokument der Rechnung sichtbar ist (also bei jeder Dokumentenliste) den Menüpunkt, um die Anmerkung zu schreiben oder eine vorhandene Anmerkung zu erweitern.

Knopf für Fotos jetzt im Kundendienst, Projekt, Labelcrm und Adressen (V5)

In den meisten angesprochenen Bereichen waren über iDeXs importierte oder manuell abgelegte Fotos nur über das Menü oder einen kleinen Knopf in der Toolbar erreichbar. Nun gibt es dort einen großen Knopf mit rotem Strich, wenn Bilder hinterlegt sind.Auch wenn keine hinterlegt sind, ist der Knopf verfügbar, damit Sie ggf. per Drag and Drop noch Fotos hinterlegen können.

E-Mail, Maske mit Baustein-Auswahl (V5)

Unter dem Hintergrund, dass mit der Kundeninfo aus dem Kundendienst heraus verstärkt Bausteine zum Einsatz kommen, haben wir die Bausteinauswahl direkt in die E-Mailmaske genommen. Bei einer großen Auswahl an Bausteinen ist die Filterzeile sehr hilfreich.

Wechsel der Anzeige im Rg-Ausgang per umschaltbarer TAB-Datei

TAB-Dateien dienen dazu, die Anzeigen in Tabellen individuell zu gestalten. Seit der Version 4.72 / 5.72 gibt es eine Möglichkeit, TAB-Dateien selber zu verändern. Nun kann auch im Rg-Ausgang eine TAB-Datei mit mehreren Blöcken verwendet werden. Welche Daten sichtbar sind, kann dann in der geöffneten Maske umgeschaltet werden.

Wie Sie solche TAB-Dateien erstellen und einrichten, sehen Sie in einem kurzen Tutorial Video im Label-Wiki oder im Handbuch Kapitel TAB Dateien bearbeiten.

[Bild]

Neue Dokumente (V5)

Vor- und Nachbemerkungen können nun schon in der Dokumenten-Anlagemaske erstellt werden.

[Bild]

Eingangsrechnungen, Prüfmaske überarbeitet, weitere Anzeigen (V5)

Hinzugekommen ist die Möglichkeit, einen archivierte Arbeitsbericht eines KD-Auftrags und einen ggf. gescannten Eingangslieferschein anzuzeigen. Bei den Knöpfen mit dem Listensymbol werden die Artikel im Label-Format gezeigt. Der Knopf ‚Rechnungsartikel‘ kann nur zum Einsatz kommen, wenn die Rechnung per UGL oder Gaeb gekommen ist.

Neu sind die Knöpfe Projekt und Kd-Auftrag unten links. Damit kann der Prüfer eine falsche Zuordnung ändern. Da die Buchhaltung von der Zuordnung zum Kostenträger nicht betroffen ist, halten wir es für sinnvoll, wenn der Prüfer dies ändern kann.

[Bild]

Projektsuche mit Favoriten (V5)

Etwas störend war bisher, dass die Projektauswahl über die Favoriten bisher nur in der Projektverwaltung selber möglich war, nicht aber an anderen Stellen, in denen man ein Projekt sucht. Nun gibt es in der Suchmaske ein Ankreuzfeld zur Umschaltung.

[Bild]

Kundendienst, Priorität als Pflichtfeld definierbar.

Wenn Sie diese Möglichkeit nutzen wollen, müssen Sie dies nur im Modul Einstellungen unter den Kundendienst-Grundeinstellungen festlegen.

Rücknahmen mit Nachverfolgung bis zur Gutschrift

Nach entsprechender Einrichtung im Einstellmodul unter Projektverwaltung, Grundeinstellungen können Rücknahmen komfortabel in ein Dokument geschrieben werden. Das erfolgt in der Projektverwaltung unter den Menüpunkten <Projekt>, <Rücknahmen>.

Bisher wurde immer eine Lagerentnahme angelegt, damit das Projekt sofort entlastet wurde. Nun kann auch eine Bestellung oder ein Eingangslieferschein erzeugt werden. Natürlich enthalten alle Dokumente Artikel mit negativer Menge. Bei diesem Weg gibt es aber keine Kontrolle, ob die Gutschrift jemals eingeht.

Erzeugung einer Bestellung: Die Bestellung sollten Sie drucken (ggf. mit speziell angepasstem Formular mit ‚Rückgabe‘. Damit ist die Abholung über die Bestellüberwachung zu kontrollieren. Nach der Abholung erfassen Sie den ‚Wareneingang‘ und erzeugen dann den Eingangslieferschein (immer noch mit negativen Mengen und Gesamtsumme

Erzeugung eines Eingangslieferscheins: Im Vergleich zur Bestellung fehlt nur die Überwachung der Abholung und die Info an den Lieferanten. Im Gegenzug ersparen Sie sich den Wareneingang.

Der Eingangslieferschein entlastet das Projekt (weil ja negativer Wert). Bei der Buchung der Gutschrift wird der Eingangslieferschein auf erledigt gesetzt und die Gutschrift entlastet das Projekt. Solange im Wert negative Eingangslieferscheine offen sind, sind nicht alle Gutschriften eingegangen.

Postbox, jetzt mit Zuordnung einer Eingangsrechnung zur Buchung

Bisher sind wir davon ausgegangen, dass die Eingangsrechnung hier nach dem Scannen erfasst wird. Einige Anwender jedoch buchen die Eingangsrechnung erst ein und scannen sie erst im Nachgang. Dazu gibt es nun einen neuen Knopf, mit dem der Scan zugeordnet werden kann. Auch das Anhängen an einen vorhandenen Scan ist damit möglich.

GoBD – Ausgangsrechnungen nach Druck mit Nummer nicht mehr veränderbar

|

Nachtrag 9. April 2017:

Solange eine Rechnung das Haus nicht verlassen hat, kann sie auf ‚ungültig‘ gesetzt werden und mit gleicher Nummer wieder gedruckt werden. Die ausführliche Beschreibung finden Sie unter Korrektur von Ausgangsrechnungen.

Die schon lange angekündigten Änderungen wg. der GoBD sind in dieser Version umgesetzt. Zunächst die (leider) erforderlichen Sperren:

|

- Eine Rechnung mit Nummer und Eintragung im Rechnungsausgangsbuch kann nicht mehr gelöscht oder geändert werden.

- Bei einem Nachdruck muss immer das Wort Kopie drauf stehen.

|

- Da man ja Fehler nie ausschließen kann, haben wir das Stornieren und Ändern der Rechnung besonders einfach gemacht. Mit Markieren des Rechnungsdokumentes und der rechten Maustaste erscheint ein Menüpunkt ‚Dokument kopieren, Rechnungstorno‘.

Dieser Punkt erscheint in der Projektverwaltung und allen Masken mit ‚Zugeordnete Dokumente‘

|

[Bild]

Stornorechnung

Zunächst erscheint eine Maske, in der Sie entscheiden müssen, ob die Rechnung wirklich storniert werden soll, oder eine Stornorechnung erzeugt werden soll. Eine Stornorechnung muss immer dann erzeugt werden, wenn die Rechnung das Haus schon verlassen hat. Das hat also letztlich mit GoBD nicht zu tun, sondern war schon immer erforderlich. Bisher musste man aber in einem neuen Dokument die alte Rg. als Vorlage wählen und den Mengenmulti auf -1 setzen. Mit der neuen Funktion haben wir es also viel einfacher gemacht.

Egal ob Sie eine neue Rechnung oder eine Stornorechnung anlegen wollen, erscheint erscheint die Maske zur Anlage von neuen Dokumenten, in der alle Werte der ‚alten‘ Rechnung vorbelegt sind. Ggf. können Sie hier Änderungen vornehmen.

Bei der Stornierung erscheint dann danach ein Fenster, in dem Sie den Grund der Stornierung eingeben können. Dieser Text kommt ins Rechnungsausgangsbuch als Anmerkung. Zusätzlich wird in die Bemerkung der Rechnung das Wort ‚Storno‘ vorangestellt.

Die Bearbeitung der neuen Rechnung erfolgt dann wie gewohnt.

Der Storniervorgang:

Ob die Stornierung abgeschlossen ist, hängt von den Rechten des Anwenders ab und ob im Betrieb das Modul ‚Fibuerfassung‘ eingesetzt wird.

|

Wichtig: Bei Nutzung der Fibuerfassung muss dort eine Verrechnungsbank eingetragen werden. Dies geschieht unter den Menüpunkten <Optionen>, <Einstellungen>.

Bei dem Recht geht es um den Bereich ‚Rechnungen‘, ‚gebuchte Rechnungen erneut ausdrucken‘. Wer dieses Recht in der Vergangenheit hatte, durfte im Rechnungsausgang eingetragene Rechnungen ändern und neu drucken / eintragen lassen. Wer dieses Recht hat, darf nun komplett stornieren, allerdings ohne deshalb ins Rechnungsausgangsbuch zu gehen.

Storniervorgang ohne Nutzung der Fibuerfassung

1. Rechte ‚Darf alles‘:

Die Rechnung wird storniert – im Rechnungsausgang fertig, Die Stornierung muss in der Fibu beim Steuerberater zusätzlich erfolgen.

2. Recht ‚Darf nicht stornieren (Recht fehlt)

Nur Eintragung im RA-Buch im Feld ‚Bemerkung „Zu stornieren‘ mit Name und Datum/Uhrzeit. Die Stornierung im Rechnungsausgangsbuch muss später von jemand berechtigtem vorgenommen werden. Zur Suche wird der Filter mit dem Text ‚Storno‘ eingesetzt.

Storniervorgang mit Nutzung der Fibuerfassung

1. Rechte ‚Darf alles‘:

Die Rechnung wird im Rechnungsausgang storniert und in den Datensätzen der Fibuerfasssung die Umkehrbuchungen erzeugt – damit ist wirklich alles fertig, der Steuerberater braucht nichts mehr machen.

2. Recht ‚Darf nicht stornieren (Recht fehlt)

Nur Eintragung im RA-Buch im Feld ‚Bemerkung „Zu stornieren‘ mit Name und Datum/Uhrzeit. Der Stornovorgang erfolgt in der Fibuerfassung wie bisher: Anwahl von ‚ Rechnung bezahlen‘, Summe 0, Rest ausbuchen und damit stornieren.

Sonstiges

Wer die Stornierung komplett automatisiert stattfindet erfolgt eine Generalumkehr, die Ausbuchung erfolgt negativ auf dem Erlöskonto. Wenn jemand diese auf einem speziellen Konto haben möchte, kann er dieses bei den Erlöskonten hinterlegen. In der Regel ist aber die Generalumkehr der richtige Weg und Sie brauchen nichts zu machen.

In der Druckmaske gibt es einen Knopf ‚Prüfdruck, mit der Druck ohne Nummer erfolgt. Sinngemäß so wie beim Bildschirmdruck, aber eben auf den vorgesehenen Drucker und mit Rechnungsnummer 0 und vor dem Text ‚Rechnung‘ steht ‚Entwurf‘, um die Probedrucke deutlich zu kennzeichnen.

Die Adresse der Rechnung steht nun in der Rechnung selbst. Bei einem Nachdruck wird darauf zugegriffen und nicht auf eine ggf. geänderte Adresse in den Stammdaten.

Da gleiche gilt für die Zahlungsbedingen.

Nur das erste Exemplar sieht so aus wie bisher, beim zweiten muss schon das Wort KOPIE drauf stehen. Dazu sind ggf. Formularänderungen erforderlich, die bei vielen Anwendern aber schon stattgefunden haben. Wer ein Formular ohne diese Möglichkeit verwendet, wird jedesmal darauf hingewiesen, dass dies nach GoBD nicht zulässig ist.

Zum Arbeitsablauf:

Wer bisher die Rechnungen einfach ausgedruckt hat, danach geprüft und ggf. dann geändert und neu gedruckt hat, sollte dies unserer Meinung nach mindestens bei den Kundendienstrechnungen weiter so machen. Mit dem Unterschied allerdings, dass der oben beschriebene Kopier- und Stornovorgang ausgelöst werden muss. Je nach ‚Fehlerquote‘ gibt es dann halt ein paar stornierte Rechnungen. Diese sollten Sie auch in den Rechnungsordner heften und als ‚Storniert‘ kennzeichnen. Der Grund steht ja im Rechnungsausgangsbuch, das sollte bei einer Buchprüfung reichen.

Damit findet ein Buchprüfer einige Stornierungen und kann seine Zeit damit verbringen, diese zu prüfen.

Projektdatenblatt, Gewährleistung

Man kann nun bei einem Projekt eintragen, wann die Gewährleitung endet. Wenn ein Kundendienstauftrag zu einer Objekt-Adresse angelegt wird und diese Adresse in einem Projekt mit aktiver Gewährleistung als Objektadresse verwendet wird, erfolgt eine Warnung.

Hintergrund ist eine Situation, bei der ein Mitarbeiter ganz stolz dem Kunden eine Pumpe gegen eine hochwertige Energiespar-Pumpe verkauft und ausgetauscht hat. Leider lief das noch unter Garantie und die Kosten gingen zu Lasten des Betriebs. So etwas kann nun besser verhindert werden.

Aufgabenverwaltung, verschieben in neues Projekt

Im Menü einer Aufgabe gibt es nun die Möglichkeit, mit der Aufgabe und den zugeordneten Dokumenten ein neues Projekt anzulegen. Bei Anwahl kommt die Maske zur Anlage eines neuen Projektes. Nach der Erfassung wird die Aufgabe und deren zugeordneten Dokumente in das neue Projekt verschoben.

Hintergrund: Wenn eine Aufgabe genutzt wird, um ein Angebot und ggf. auch weitere Dokumente dazu zu verwalten, kann man nun im Falle des vorliegenden Auftrags ein neues Projekt anlegen. Die Analogie mit einem KD-Auftrag gab es schon länger.
