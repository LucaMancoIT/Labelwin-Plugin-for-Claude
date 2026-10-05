# Version 4.70 (März 2016)

Pfad: Updatetexte (bisher) > Update 2016 > Version 4.70 (März 2016)
Quelle: handbuch/version_4_70__marz_2016_.htm

|

Version 4.70 (März 2016)

Versionswechsel auf 4.70 - Änderungen März 2016

Statusmeldungen an die Zentrale im mobilen Kundendienst und iDeXs

|

Hinweis: Die nachstehend beschriebenen Möglichkeiten sind

- Bei Mobilkd nur bei der Datenübertragung per Verzeichnis (z.B. Dropbox) möglich.

- Bei iDeXs nur ab der Basis-Version und zunächst nur in der Android-Version. (Ios folgt).

Bei den Statusmeldungen geht es darum, dem Büro mehr Übersicht über die Mitarbeiter zu geben. Die mobilen Mitarbeiter können sehr einfach eine Meldung über ihren ‚Status‘ abgeben und das Büro kann sehen, wer wo ist und was macht. Dabei geht es nicht um Überwachung, sondern darum, die Kommunikation zu verbessern Das Büro kann bei Verspätungen den nächsten Kunden informieren, sehen wo sich ggf. noch ein Noteinsatz einschieben lässt, bei Nachfragen sehen, dass der Mitarbeiter auf dem Weg zurück zum Büro ist (und man ihn deshalb nicht anrufen muss) und vieles mehr.

Die Statusmeldungen sind frei erfassbar. Seit dem Update 4.70 bzw. 5.70 befindet sich ein Grundstandard auf Ihrem Rechner, den Sie beliebig verändern können.

Die Meldungen können im Modul Einstellungen unter den Menüpunkten <Programmbereiche>, <Kundendienst>, <Statusmeldungen> erfasst und verändert werden.

Dort müssen Sie auch festlegen, dass Sie mit den Meldungen arbeiten wollen.

[Bild]

Bei der Wahl der Verwendung legen Sie fest, an welcher Stelle die Meldung angeboten wird. Das ist die die oberste Ebene, an der oft ‚neutrale‘ Meldungen ohne Auftragsbezug abgesetzt werden und im geöffneten Auftrag in der Regel mit Auftragsbezug.

Bei den Meldungsvorlagen können Sie festlegen, bei welchen die Auftragsnummer mit gesendet wird und bei welchen nicht.

Ankreuzfeld ‚Mit Standortaufzeichnung‘:

Mit gesetztem Haken versuchen die verwendeten Geräte den Standort zu bestimmen, an dem die Meldung abgesetzt wird. Dies funktioniert bei einem Smartphone und der App iDeXs fast immer, bei Einsatz des mobilen Kundendienstes per Tablett oder Notebook meist nur auf den neueren Geräten. Auf jeden Fall müssen Sie die Aufzeichnung mit Ihren Mitarbeitern absprechen, da davon die Persönlichkeitsrechte Ihrer Mitarbeiter betroffen sind.

Zusammen mit der neuen Kartenanzeige per Google (Beschreibung unten) können nun die Standorte der letzten Statusmeldung aller Mitarbeiter angezeigt werden.

Abholen der Meldungen:

[Bild]

Zur Nutzung gehört, dass die Meldungen regelmäßig abgeholt werden. Dazu gibt es ein neues Modul, das auf einem Arbeitsplatz oder noch besser auf dem Server selbst gestartet werden muss. Es hat den Namen StatusImport.exe und liegt im Labelwin-Verzeichnis. Am besten erstellen Sie eine Verknüpfung auf die Datei oder binden sie im Startcenter ein. Das Programm sollte nur auf einem Rechner gleichzeitig laufen.

Mit der Zeitsteuerung schaut das Modul regelmäßig nach, ob neue Meldungen von iDeXs oder Mobilkd vorliegen und verarbeitet diese. Die zuletzt abgeholte Meldung wird nur zur Info gezeigt. In der Einführungsphase kann man damit gut testen.

Anwendung im Mobilen Kundendienst

Es gibt 2 Stellen, an denen die Meldungen abgesetzt werden können.

- Von der obersten Ebene im Menü <Datei>

- Aus dem geöffneten Auftrag mit dem Knopf ‚Statusmeldungen‘ für Meldungen mit Bezug zum geöffneten Auftrag.

[Bild]

Bei den Knöpfen in Gelb ist hinterlegt, dass sie sofort gesendet werden und sich die Maske schließt. Bei den anderen Knöpfen ist eine Texteingabe möglich, die erst mit dem ‚Senden‘-Knopf raus geht.

Da für beide Situationen festgelegt wird, welcher Knopf sichtbar ist, kann die Maske je nach Startpunkt unterschiedlich aussehen.

Anwendung im iDeXs

Auch hier gibt es 2 Stellen, an denen die Meldungen abgesetzt werden können.

- Von der obersten Ebene mit dem Knopf in der Leiste ohne Bezug zu einem Auftrag

- Aus der Maske der Leistungserfassung mit dem gleichen Knopf, für Meldungen mit Bezug zum geöffneten Vorgang

Da für beide Situationen festgelegt wird, welche Meldungen zur Auswahl angeboten werden, können die Auswahllisten je nach Startpunkt unterschiedlich aussehen.

[Bild]

[Bild]

Der Überblick (Nur V5-Version):

Im Kundendienst finden Sie unter <Auswerten> den neuen Punkt <KD-Mobil Status>.

[Bild]

In der oberen Tabelle sehen Sie alle Mitarbeiter mit mobilem Gerät und deren letzte Statusmeldung. In der unteren Tabelle sehen Sie alle noch offenen Aufträge des oben markierten Mitarbeiters.

Diese Maske ist vom sonstigen Programm abgekoppelt, so dass sie dauerhaft geöffnet sein kann.

Anzeige sämtlicher Statusmeldungen

Die Statusmeldungen gibt es schon lange. Auch die Meldungen von TomTom werden im gleichen Bereich abgelegt. Sämtliche Statusmeldungen mit Eingrenzung auf einen Mitarbeiter oder auf einen bestimmten KD-Auftrag können im Kundendienst angezeigt werden. Die Menüpunkte finden Sie unter dem Menüpunkt <Export / Import>

Meldungen aus der Zentrale zum mobilen Gerät:

Auch in der Zentrale können Meldungen / Informationen zum Mitarbeiter geschickt werden. Dies geschieht von der obersten Ebene aus unter den Menüpunkten <Export / Import>, <KD-Meldungen>. Hier gibt der Rückgriff auf Bausteine aber keinen großen Nutzen. Stattdessen ist es möglich, einen Text an beliebig viele Mitarbeiter auf einen Rutsch zu senden.

Adressen suchen

Bei der Vielzahl an Adressen ist es manchmal wünschenswert, bei der Suche auf eine bestimmte Gruppe einzugrenzen. Da der Marketingschlüssel 1 bei nahezu allen Kunden als Klassifizierung festgelegt ist, haben wir diesen in die Auswahlmaske einbezogen. Sobald Sie ein oder mehrere Haken setzen, wird die angezeigte Liste entsprechend eingegrenzt.

[Bild]

Mobiler Kundendienst, Anzeige für neue Aufträge auf mobilem Gerät

In der Maske der Auftragsliste gibt es oben rechts einen Knopf, wenn neue Aufträge aus der Zentrale vorliegen. Dies greift natürlich nur beim Transport der Aufträge über ein Verzeichnis. Beim Email-Transport wird ja die Email selbst angezeigt.

[Bild]

Mit Druck auf den neuen Knopf werden die Daten importiert.

Mobiler Kundendienst, Aufträge an alle beteiligten Monteure per Vorgabe

Bei großen Wartungen schicken manche Betriebe den Auftrag an alle beteiligten Mitarbeiter. Dies war schon lange mit einem Ankreuzfeld beim Exportieren möglich. Um das Vergessen zu verhindern, kann dieser Schalter in den Laptop-Grundeinstellungen der Zentrale vorbelegt werden.

Falls Sie das jetzt neu einführen möchten der Hinweis, dass nur die Daten vom Hauptmonteur zurückkommen. Alle anderen Mitarbeiter erhalten den Auftrag nur zur Information.

Abschlags- und Teilrechnungen hochzählen

Über einen Schalter kann nun festgelegt werden, das Überschriften wie 1.Abschlag, 2 Teilrechnung usw. entstehen. Die Zahl wird je Projekt hochgezählt. Die Nummer wird nirgends gespeichert, sondern unmittelbar vor der Druckausgabe wird die Anzahl der Abschläge mit Rechnungsnummer gezählt.

Die Einstellung erfolgt im Modul Einstellungen unter den Menüpunkten <Programmbereiche>, <Druckausgabe>, <Druck-Überschriften>

Zahlungseingang, bei Endrechnungen deren Gesamtsumme anzeigen

In der Maske des Zahlungseingangs wird nun neben der Rechnungssumme auch die Gesamtsumme vor Abzug der Abschläge gezeigt. Bei Skontoangeboten auf die Gesamtsumme ist nicht sofort ersichtlich, warum ein unverhältnismäßig hoher Skontobetrag angeboten wurde.

Rechnungsprüfung, gescannten Eingangslieferschein zeigen

Wenn die Lieferscheine der Lieferanten gescannt werden, kann es manchmal sinnvoll sein, diese bei der Rechnungsprüfung zu betrachten. Da aber nur wenige Anwender hier scannen, haben wir die neue Möglichkeit als Menüpunkt realisiert.

Automatische Artikelverknüpfungen, Funktionen erweitert

Mit den automatischen Artikelverknüpfungen können Beziehungen zwischen Artikeln verschiedener Kataloge / Lieferanten hergestellt werden. Die Möglichkeit gibt es schon lange im Modul Kataloge unter den Menüpunkten <Durchläufe>, <Automatische Artikelverknüpfungen>.

Die Maske wurde nun um die Möglichkeit erweitert, die Herstellernummer als gemeinsames Merkmal zu verwenden.

[Bild]

Zusätzlich kann man nun auf bestimmte Artikelgruppen eingrenzen.

Postboxverteilung, Maske überarbeitet

Mit der Postbox können gescannte oder per Datei eingegangene Pdfs dem entsprechenden Vorgang zugeordnet werden. Um bei einer großen Anzahl von Dateien den Überblick zu behalten, wird nun das Dateidatum in der Tabelle angezeigt. Über einen Doppelklick auf eine Spaltenüberschrift kann nun sortiert werden.

Mit dem Menü der rechten Maustaste kann eine Datei nun auch unbenannt und gelöscht werden.

Zeitwirtschaft, Buchung aller Mitarbeiter mit Sollzeit wg. Feiertag

Bisher war es nicht möglich, bei einer Buchung für alle Monteure mit dem von bis-Datum zu arbeiten. Die Sperre diente dazu, nur schwer wieder zu korrigierende Fehler zu verhindern. Nun ist die Sperre aufgehoben, wenn beim Datum nur ein Tag gebucht wird. Damit ist das Ankreuzfeld ‚Sollzeiten buchen‘ in der Maske erreichbar.

Die Änderung erfolgte, damit man die Sollzeiten aller Mitarbeiter für einen Feiertag buchen kann. Bisher war dies nur über den Trick mit einem Team möglich..

Fehlzeiten wie Urlaub, Krank usw. in Zeitwirtschaft buchen und

im Kundendienst ohne weitere Erfassung anzeigen.

Immer wieder haben wir die Diskussion geführt, dass man im Kundendienst die geplanten und in der Zeitwirtschaft die stattgefundenen Fehlzeiten buchen muss. Wir halten dies weiterhin für richtig, aber wollen die Diskussionen nicht mehr führen.

Nach der Einrichtung können nun die Fehlzeiten in der Zeitwirtschaft gebucht und in den Kalendern im Kundendienst gezeigt werden. Solche Einträge können auch nur in der Zeitwirtschaft geändert werden.

Zur Einrichtung müssen Sie im Modul Einstellungen bei den Stundenarten die Art der Fehlzeit eintragen. Sie finden das unter den Menüpunkten <Programmbereiche>,<Zeitwirtschaft>, <Stundenarten>

Artikelaufruf, Maske in der Höhe veränderbar

Diese Änderung wurde programmiert, damit man z.B. bei Sets mehr vom Kurztext sehen kann. In der Breite ist die Maske nicht änderbar, weil damit keine weiteren Informationen sichtbar würden. Wie bei allen Masken merkt sich das Programm anwenderbezogen die letzte Fenstergröße.

Wareneingang, Startmaske überarbeitet.

Da immer mehr Anwender den Wareneingang per UGL-Dateien buchen, wurde die Maske komplett überarbeitet. Es war z.B. nicht möglich, Kommissionsaufkleber zu drucken, wenn über die UGL-Maske gestartet wurde. Alle aufgrund der UGL gefundenen Zuordnungen wie Bestellnummer, Projekt, Kundendienstauftrag usw. werden nun deutlich gezeigt.

Die Suche einer Bestellung über die Projekt- oder Auftragsnummer ist nun möglich.

[Bild]

Wareneingang per UGL, Korrekturbuchungen jetzt möglich

Bisher war es nicht möglich, die Mengen bei der Einbuchung von UGL-Lieferscheinen zu ändern. Nun können markierte Zeilen per Knopf aktiviert und eine Korrekturmenge eingetragen werden. Wenn also 2 Teile zu wenig geliefert worden sind, muss man -2 eingeben. Die Korrekturen werden immer am Ende angehängt. Dies zeigt deutlich die Abweichungen und war auch aufgrund der Programmstruktur erforderlich.

Wareneingang von mündlicher Bestellung, Bemerkung Eingangslieferschein

Bisher wurde der Bemerkungstext des entstehenden Dokuments Eingangslieferschein immer automatisch mit ‚mündliche Bestellung …‘ belegt. Nun können Sie vor der ersten Buchung den Text selber belegen.

Wenn Sie nichts eingeben, greift der alte Automatismus.

[Bild]

Die Eingabe geschieht in der Maske, in der die Artikel aufgerufen werden.

Rechnungsausgang, Umsatz in Adresse eintragen nutzt jetzt Leistungswerte

Beim Eintragen der Umsatzzahlen in die Adresse wurden bisher einfach die Rechnungssummen eingetragen. Bei Ist-Versteuerten Abschlagsrechnungen sind diese Werte jedoch falsch, weil dort ja nur die Zahlsumme berücksichtigt wird und die Rechnungssumme damit ggf. zu hoch ist. Mit den Leistungswerten haben wir die richtige Zahl. Bei deren Einführung haben wir an diese Situation nicht gedacht.

Hinweis: Die Eintragung in den Adressen erfolgt, um z.B. die umsatzstärksten Kunden zu ermitteln.

Rechnungsprüfung mit Anzeige des gescannten Kundendienst-Auftrags

Je mehr Anwender die Rechnungsprüfung nutzen, desto mehr Wünsche tauchen auf. Wenn eine Eingangsrechnung auf einen Kundendienstauftrag gebucht ist, kann man über das Menü schon seit längerem den Auftrag ansehen. Neu ist nun, dass man mit dem nächsten Menüpunkt unter <Anzeige> auch den Scan betrachten kann.

Personalerfassung, Eingabefelder verschoben

Da die Maske im Bereich für den mobilen Kundendienst zu eng wurde, haben wir einige Felder auf andere Karteiseiten verschoben. Wer etwas vermisst, möge auf den anderen Seiten mal schauen – wir möchten die Leser hier nicht mit unwichtigen Details belästigen.

Kundendienstaufträge aus Outlook mit neuer V5-Version

Wenn Aufträge aufgrund einer Email aus Outlook heraus angelegt werden, startet standardmäßig noch die ‚alte‘ Maske. Mit einem Schalter können Sie dies jetzt ändern. Es gilt aber für die ganze Firma. Allerdings gibt es aus unserer Sicht ohnehin keinen Grund mehr, noch mit der alten Version zu arbeiten.

Den Schalter finden Sie im Modul Einstellungen unter den Menüpunkten <Grundeinstellungen>, <Allgemein> auf der Seite ‚Allgemein‘ unter der Outlookeinrichtung.

Um die Nachfrage zu sparen: Das geht noch nicht bei den Aufgaben – wir arbeiten daran.

Einfache Maske zur Erfassung von Notdienstaufträgen

Zu Recht behaupten Kunden, dass die Maske der Auftragserfassung für Mitarbeiter, die nicht ständig damit arbeiten, zu kompliziert sei.

Speziell für den Notdienst haben wir nun eine einfache Maske entwickelt. Im optimalen Fall genügt die Eingabe der Anlagennummer. Dies für Firmen, die die Anlagennummer beim Endkunden auf das Gerät kleben.

Man kann aber auch eine Adresse aufrufen und ggf. eine Anlage dazu wählen.

Das Modul hat den Namen kdNot.exe und liegt im Labelwin-Verzeichnis.

[Bild]

Mit dem Knopf Notdienst wird der Mitarbeiter vorgeschlagen, der im ‚normalen‘ Notdienst an der Reihe ist. Diese Einstellungen finden Sie im Modul Einstellungen unter den Menüpunkten <Programmbereiche>, <Kundendienst>, <Kd-Notdienst>

Mit dem Knopf ‚Speichern‘ wird der Auftrag nur angelegt und die neue Nummer in einer Box verkündet. Bei dem Knopf ‚An Mobil‘ wird der Auftrag angelegt und sofort an das beim Mitarbeiter hinterlegte Gerät (iDeXs oder mobiler Kundendienst) übertragen. Die Ankreuzfelder Email-Info und SMS geziehen sich auch auf die beim Mitarbeiter hinterlegten mobilen Daten. Es sind also sinngemäß die Kreuze, die sonst bei der Übertragung von Aufträgen an Mobil vorhanden sind. Beim einfachen ‚Speichern‘ haben sie keine Wirkung.

Auf die Anzeige der Karteikarte, Vertragsdaten und Historie der Einsätze haben wir bewußt verzichtet.

Die Möglichkeiten, per Mail einen Auftrag auszulösen, der dann auch an das mobile Gerät geht, besteht weiterhin. Diese Maske ist eine Alternative, bei der man sehen kann, welche Adressen und Anlagen es gibt.

Diese Maske läuft nicht direkt im Web, aber die Systembetreuer haben bei entsprechender Hardwarekonstellation die Möglichkeit, bei Einwahl des Mitarbeiters sofort diese Maske zu starten und ihn sonst nirgends arbeiten zu lassen.

Eingangsrechnungen per Gaeb

Vor etwa 1,5 Jahren wurde das Verfahren eingeführt, mit dem Rechnungen per UGL vom Lieferanten in digitaler Form eingelesen werden können. Schon damals war absehbar, dass auf die Dauer die GAEB-Rechnung als Standard eingeführt wird. Die Testphase ist erfolgreich verlaufen, so dass Labelwin nun beides – UGL und GAEB – verarbeiten kann.

Voraussetzung ist allerdings der Erwerb des Modul ‚Rechnungsimport‘ (295 € + MwSt)

|

Wichtig: Die bisherige Verarbeitung von UGL-Rechnungen steht noch zur Verfügung, um Ihnen die Umstellung zu erleichtern. Allerdings mit dem Tastaturkürzel STRG F7.

Mit der F7-Taste nutzen Sie das neue Verfahren.

Vorteil des Gaeb-Verfahrens:

- die Rechnung als PDF ist immer dabei. Bei UGL ist dies nicht verpflichtend und da die Namensgebung der PDF nicht normiert ist, gibt es hier manchmal Probleme.

- Es ist zu erwarten, dass sich über kurz oder lang alle Lieferanten im SHK-Bereich und sicherlich auch in anderen Gewerken dem GAEB-Verfahren anschließen. Aus politischen Gründen ist dies bei der UGL nicht der Fall.

- Der Lieferant bekommt eine Empfangsbestätigung, so dass er sie als garantiert zugestellt betrachten kann.

-

Was ändert sich ?

Wir haben die Chance genutzt, die unterschiedlichen Formen der Dateien in eine gemeinsame Oberfläche zusammen zu führen. Über weitgehend automatisierte Abhol-Prozeduren werden alle digitalen Rechnungen aller Lieferanten eingesammelt – quasi in einer zentralen Sammelstelle. Für die Vorstellung ist es vielleicht hilfreich, an eine große Kiste zu denken, in die man die ganze Rechnungspost hinein wirft.

Dabei entsteht ein Inhaltsverzeichnis, in dem auch die Zuordnungen zum Projekt, zum Kundendienstauftrag, zur Bestellung und zum Eingangslieferschein aufgeführt werden. Mit diesen Zuordnungen steht und fällt der Komfort bei der späteren Buchung im Rechnungseingangsbuch.

In dieser Sammelstelle können auf die Dauer auch weitere künftige Formate verarbeitet werden. Schon jetzt ist es möglich, eine einfache PDF-Rechnung wie von der Telekom per Drag&Drop abzulegen, wobei dann der Lieferant manuell dazu erfasst werden muss.

Beim UGL-Verfahren wurde jeweils im Bereich eines Lieferanten gearbeitet und die Buchung durch Anklicken einer Datei gestartet. Nun findet die Buchung aus diesem Inhaltsverzeichnis mit allen Lieferanten statt. Man kann aber die Auswahl auch auf einen Lieferanten eingrenzen.

Transport der Rechnungen

Im UGL-Bereich werden die Rechnungen wie bisher über das FTP-Verfahren abgeholt. Dabei werden alle beim Lieferanten bereitgestellten Dateien in jeweils ein Verzeichnis geholt. Neu ist, dass sie nun von dort in jene ‚Kiste‘ verschoben werden, dabei in ein Inhaltsverzeichnis eingetragen werden.

Der Abholen bei einem Lieferanten erfolgt indem die Anzeige auf einen eingegrenzt wird und dann der Knopf ‚Abholen‘ gedrückt wird.

Rundruf

Um die angesprochene Sammelstelle / Kiste mit allen Rechnungen zu füllen, gibt es einen Menüpunkt ‚Rundruf‘. Dabei werden alle bereit gestellten Daten von allen Lieferanten abgeholt und die Rechnungen und dazu gehörende PDFs sofort in die Kiste geschoben.

Andere Dateien wie Lieferscheine, Auftragsbestätigungen und Preisauskünfte bleiben in dem bisherigen Pfad und können dort wie bisher abgearbeitet werden.

Gestartet wird der Rundruf über das Menü.

[Bild]

Verarbeitung:

Die Buchung der Eingangsrechnungen erfolgt aus dem ‚Inhaltsverzeichnis‘ heraus.

Das Handbuch / Bedienungsanleitung für diese Maske ist erstmalig nur im LabelWiki hinterlegt. In den richtigen Bereich gelangen Sie mit dem kleinen blauen Knopf oben rechts.

Markieren Sie die erste Rechnung. Unten sehen Sie die Interpretationen der gefundenen Bestellnummer, der zugeordneten Projekt- und Kundennummer.

Betätigen den Knopf ‚Rechnung buchen.‘

Je nach Einstellung (Modul Einstellungen, Menüpunkte <Programmbereiche>, <Eingangsrechnungen>, <Grundeinstellungen> wird die Zahlungsbedingung gezeigt, wenn die der Rechnung von der in der Adresse hinterlegten abweicht.

[Bild]

Die eigentliche Buchung erfolgt wie bei einer manuellen Erfassung. Der entscheidende Vorteil ist, dass die Maske bereits weitgehend ausgefüllt ist. Im Idealfall muss die Buchung nur noch bestätigt werden.

Einrichten der GAEB-Rechnungen:

Bevor Sie mit GAEB-Rechnungen arbeiten können, müssen Sie dies mit Ihrem Lieferanten abklären. Im Moment (April 2016) kann dies nur die GC-Gruppe und Labelwin, weil wir die Pilotphase durchgeführt hat. In absehbarer Zeit werden weitere Lieferanten dazu kommen.

Im Adressmodul müssen wie bei den UGL-Rechnungen die Zugangsdaten des Lieferanten hinterlegt werden. Aktivieren Sie die Adresse und gehen mit STRG O in die Erfassung der Online-Daten.

[Bild]

Drucken Fotodokumentation

In der Bildanzeige der V5-Version gibt es jetzt eine Möglichkeit, die hinterlegten Fotos zusammen mit den wichtigsten Auftragsinformationen oder Projektdaten zu drucken. Dazu befindet sich nach dem Update für jeden Bereich der Bildanzeige ein Standard-Report. Die Druckausgabe gibt es als Menüpunkt in der Maske der Bildanzeige unter <Datei>

Kartenansicht KD-Aufträge und ‚wo sind die Mitarbeiter‘

Mit diesem Modul können Sie sich die Orte von Kundendienstaufträgen und – bei Nutzung der Statusmeldungen mit KdMobil oder iDeXs – auch die letzten Standorte der Techniker anzeigen lassen.

Das Modul hat keinen Kaufpreis, sondern nur eine Nutzungsgebühr je nach Anzahl der PC-Arbeitsplätze zwischen 24 und 84 € im Jahr.

[Bild]

Mit einer Google-Karte können Sie gleichzeitig beliebig viele KD-Aufträge in GoogleMap anzeigen. Die Flaggen (Pins) haben einen Tooltip und eine Infobox, wenn man darauf klickt. Die Flaggen können unterschiedliche Farben bekommen - entweder pro Monteur/Techniker oder je nach Kundendienst-Priorität.

Bei Nutzung von KDMobil oder iDeXs kann die Kartendarstellung auch die letzte gemeldete GPS-Position der mobilen Techniker anzeigen. Damit ist eine optimale Einsatzplanung , Umplanung und Notdienstplanung möglich.

Das Modul Google-Karte ist nur in die Labelwin V5-Version integriert und benötigt das Modul „Kundendienst“.
