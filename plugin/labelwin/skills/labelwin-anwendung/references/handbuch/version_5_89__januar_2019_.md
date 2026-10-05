# Version 5.89 (Januar 2019)

Pfad: Updatetexte (bisher) > Update 2019 > Version 5.89 (Januar 2019)
Quelle: handbuch/version_5_89__januar_2019_.htm

|

Version 5.89 (Januar 2019)

Versionswechsel auf 5.89 - Änderungen Januar 2019

Kundendienst, nächster Wartungstermin der Objektadresse immer sichtbar

Bisher wurde ein Wartungstermin erst angezeigt, wenn eine Adresse gewählt worden ist. Das hat den Nachteil, dass man bei einer ‚normalen‘ Reparatur, vielleicht sogar bei einer Anlage mit Wartungstermin, nicht sieht, dass eine Wartung an der Adresse ansteht. Einzustellen ist dies im Einstell-Modul unter <Programmbereiche> <Kundendienst> <Grundeinstellungen>.

[Bild]

Angezeigt wird der Termin zusammen mit einer ggf. vorhandenen Kundendienst-Anmerkung in einem neuen Rahmen auf der rechten Seite im geöffneten Auftrag.

Kundendienst, mehrere Aufträge in anderes Projekt verschieben

Dazu können in der Projektverwaltung mehrere Aufträge markiert werden und mit dem Menü ‚Rechte Maustaste‘ in ein anderes Projekt verschoben werden. Folgeaufträge und zugeordnete Dokumente werden automatisch mit verschoben.

Im Kundendienst ist die gleiche Möglichkeit unter dem Ribbon (dieser Begriff ist noch nicht so verbreitet, gemeint ist das Icon im Menü) ‚Auftrag‘ mit ‚Projekt ändern‘ zu finden.

Dokumenten-/Bestellzerlegung, Maske überarbeitet

In dieser Maske wurde ‚aufgeräumt‘ damit die Funktionen wieder übersichtlich und verständlich sind. Dabei wurde eine Option eingebaut, dass auch bei vorhandenen Sets das Quell-Dokument unverändert bleibt. Für die Lager-Packliste ist nun eine Sortierung nach Lagerfach möglich. Details im Kapitel Dokumenten-/Bestellzerlegung.

Kundendienst, ‚Verantwortlich‘ als neues Kennzeichen eingeführt

[Bild]

Manchmal ist es sinnvoll, bei einem Auftrag auch festzulegen, wer im Büro dafür verantwortlich ist. Wenn dieses Feld nicht benötigt wird, können Sie es einfach ignorieren. Es ist also nicht wegschaltbar, sondern immer da. Gefüllt wird die Auswahlliste mit den Verwaltungsmitarbeitern.

Natürlich kann in der Hauptmaske auf den Verantwortlichen eingegrenzt werden.

Wareneingang, Startmaske überarbeitet

Neben dem ‚Aufräumen‘ sind neue Funktionen dazu gekommen, die vielleicht auch für Ihren Betrieb interessant sind.

-

Bestellung drucken: Wenn eine Bestellung gefunden wurde, kann man diese in Kurzform ausdrucken. Dies erfolgt mit den Formularen, die auch in der Bestellüberwachung anwendbar sind. Mit diesem Druck kann ggf. der Wareneingang ohne PC direkt mit der Bestellung verglichen werden.

-

Kommissionsetikett: Bei einer Baustellenbestellung kann ein Aufkleber (oder auch eine A4-Seite) gedruckt werden, der zur Palette gelegt wird.

Die komplette Beschreibung der Wareineingang Maske finden Sie im Kapitel

Scanarchiv, unberechtigte Lesezugriffe per Explorer verhindern.

Bisher war es so, dass die Rechte im Labelwin nicht verhindern konnten, dass man von der Explorerseite aus darauf zugreifen konnte. Mit der seit etwa Anfang 2018 verfügbaren Verschlüsselung kann zwar niemand mehr in die gescannten Pdf’s reinschauen, aber das Löschen wäre immer noch möglich. So etwas muss man natürlich als Sabotage verbuchen, aber sicherer ist es, auch das zu verhindern.

Dies ist mit einer Methode möglich, bei dem der Systembetreuer leider auch zum Einsatz kommen muss. Hier nur die grobe Beschreibung:

Man muss ein zweites Verzeichnis einrichten, bei dem die Anwender nur Leserechte haben. Beim Scannen wird wie bisher in das ‚normale‘ Verzeichnis geschrieben. Ein Programm wie Robocopy kopiert regelmäßig die Daten in das neue Lese-Verzeichnis und löscht sie im bisherigen Pfad. Das einzurichten ist der Part Ihres Systembetreuers, der von uns dazu eine Anleitung bekommen kann. Die Anzeige im Labelwin, bei der dann wie bisher alle Rechte und Schlösser greifen, holt die anzuzeigende Pdf dann aus dem Lesebereich und zeigt sie. Manipulationen sind damit ausgeschlossen, was im Sinne der DSGVO sicherlich auch wichtig ist.

Hinweis: Um damit eine Revisionssicherheit zu erreichen, müssen Sie dennoch mit dem Finanzamt reden und vor allem eine revisionssichere Datensicherung aufbauen.

iDeXs, Datenimport mit Auftrags-PDF

Für Kundendienstaufträge ist es nun möglich, eine PDF mit den Auftragsdaten mit zu importieren und im Archiv abzulegen. Die PDF ist exakt die gleiche, die man im iDeXs-Web erzeugen kann. Der Schalter um diese Funktion zu aktivieren findet sich im Modul Einstellungen unter den iDeXs-Grundeinstellungen auf der Karteseite ‚Anwendungs-Optionen‘.

Für die Projektleistungen gibt es diese Funktion bisher nicht. Wenn man bei jeder gebuchten Leistung eine PDF erzeugen würde, erstickt die Projektverwaltung an Dokumenten. Langfristig werden wir eine Funktion einbauen, die ein Formular für ein bestimmtes Projekt und einen zu wählenden Zeitraum erzeugt. Wer hier eine PDF haben will, muss zunächst weiter ins iDeXs-Web gehen.

iDeXs, Zeitbuchungen mit Anmerkung in Zeitwirtschaft

Im Zuge der Programmierung der Zeit-Prüfmaske wurde ein neues Feld ‚Anmerkung‘ eingeführt. Dieses Feld kann nun in der Android-Version auch vom Mitarbeiter im iDeXs gefüllt werden. In der ios-Version wird es noch ca. 4 Wochen dauern.

Das Feld dient dazu, dass der Mitarbeiter bei seiner Buchung eine Anmerkung wie ‚Auslösung‘, Nachtzuschlag oder ähnliches dazu schreiben kann.

DiFa-Maske und Funktionen erneut überarbeitet

Vorab für diejenigen, denen unser Stichwort DiFa nichts sagt. Es steht für Direkt-Fakturierung und ist ursprünglich entwickelt worden, um eine Abrechnung vor Ort beim Kunden zu ermöglichen. Der DiFa-Katalog kann im iDeXs und im mobilen Kundendienst zum Einsatz kommen.

Die letzten Überarbeitungen waren für die Anwender letztlich zu komplex in den Möglichkeiten. Neben der einfachen und übersichtlicheren Gestaltung wurde auch die interne Datenspeicherung geändert. Bisher war das Kennzeichen beim Artikel in den Katalog-Stammdaten gespeichert, während es nun eine separate Tabelle gibt. Damit ist die Verarbeitung auch wesentlich schneller geworden.

Sie finden die Funktion wie zuvor im Modul Einstellungen unter dem Menüpunkt <Mobil>.

Möglicherweise ist die Funktion auch für Anwender interessant, die nicht im mobilen Kundendienst unterwegs sind. Man kann nämlich nun einen eigenen (DiFa-)Katalog mit den Daten füllen, die man die letzten Jahre verkauft hat.

Wer diesen Weg geht, sucht die Artikel zwar im eigenen Katalog, aber sie bekommen das Händlerkennzeichen von dem Lieferanten, aus dessen Katalog der Artikel wirklich stammt.

Eine ausführlich Beschreibung findet sich unter DiFa - Direktfakturierung.

Zeitbuchungen, Monatsübersicht mit weiterer Anzeige

Wenn Sie in der Monatsübersicht (F8-Taste) auf einen Tag klicken, werden nun auch Details der Buchung gezeigt.

[Bild]

Postbox-Ablage um Kassenbuchungen erweitert

Nachdem wir vor kurzem auch das Archivieren von Belegen im KASSENBUCH über das SCAN-ARCHIV eingeführt haben, haben wir nun auch die Möglichkeit geschaffen dies über die Postbox zu realisieren. Dazu wurden zwei neue Button eingeführt.

[Bild]

Rechnungsausgang prüfen, Artikel ohne Verkaufspreis

|

Bei der Prüfung gibt es nun auch einen roten Hinweis, wenn sich in der Rechnung Artikel ohne Verkaufspreis befinden. Das kann durchaus beabsichtigt sein, aber wenn das versehentlich passiert ist, kann der Hinweis einen Verlust verhindern.

|

[Bild]

Auswertungscenter, Anzeige fehlerhaft geprüfter Ausgangsrechnungen

Neben der Anzeige der Anzahl der zu prüfenden Rechnungen wird im Auswertungscenter nun auch die Anzahl der als fehlerhaft geprüften Rechnungen gezeigt.

Projektverwaltung, Dokument, Anzeige des zugehörenden KD-Auftrages

Normalerweise schaut man bei einem Auftrag nach den zugeordneten Dokumenten. Nun kann man auch mit dem Menü der rechten Maustaste den Auftrag öffnen, zu dem das gerade markierte Dokument gehört. Der neue Menüpunkt hat die Beschriftung „KD-Auftrag zu Dokument“

Dokumentenliste im CRM, Versand der PDF als Emailanhang

Wenn im CRM nun ein Dokument markiert wird, zu dem eine PDF im Archiv hinterlegt ist, kann diese über das Menü mit der rechte Maustaste sehr schnell versendet werden.

Dokumentenliste mit Anzeige der KD-Auftragsnummer

Wie bei vielen Tabellenansichten können Sie auch bei einer Dokumentenliste (im Projekt oder wo auch immer) die angezeigten Inhalte selbst festlegen. Das geschieht über eine sogenannte TAB-Datei. Einzurichten im Modul EINSTELLUNGEN unter dem Menüpunkt <Optionen><TAB Dateien bearbeiten>.

Nun kann man sich in der Tabelle auch die zugeordnete KD-Auftragsnummer und die ausgeführten Arbeiten anzeigen lassen. Letzteres ist sicherlich meist nicht sinnvoll, aber wir haben es auf Kundenwunsch eingeführt.

Zeitbuchungen prüfen, Menüpunkt um iDeXs-Daten zu importieren

Die Prüfmaske ist weiter oben beschrieben. Nun wurde sie um einen Menüpunkt erweitert, mit dem die Zeiten aus iDeXs geholt werden können. Das ging bisher nur an anderer Stelle, aber es ist oft sicherlich sinnvoll, vor der Prüfung alle Daten zu aktualisieren.

Zeitbuchungen, Neuen Datensatz per Kopie erzeugen

Wenn in der Zentrale eine weitere Zulage erfasst werden muss, die in den aktuellen Datensatz nicht mehr passt, kann man nun mit einem Ankreuzfeld eine Kopie erstellen, in die man dann die weitere Zulage eintragen kann.

Zeitbuchungen, Luftlinie zwischen Firma und Objektadresse

Unter ‚Auswerten‘ kann nun die Luftlinie zwischen diesen Adressen angezeigt werden. Der Hintergrund ist eine Firma, bei denen die Auslösungen aufgrund der Luftlinien-Entfernung berechnet werden. Langfristig wird es eine Lösung geben, bei den die Auslösungen dann automatisiert gebucht werden können.

Änderungen April 2019

Zeitkontostand jetzt auch auf Monteurauswertung druckbar

|

Bisher konnten die Zeitkonto-Stände nur über den Punkt ‚Zeitkonto / Urlaub auswerten‘ gedruckt werden. Nun können diese Informationen auch bei der Liste der Buchungen für den Monteur mit gedruckt werden.

Dazu sind aber Formularanpassungen erforderlich. Unsere Standardformulare werden in Kürze angepasst, aber leider gibt es bei unseren Anwendern viele angepasste Formulare, die jeweils einzeln geändert werden müssen. Aber natürlich nur dann, wenn Sie auf dem Bericht der Zeitkontostand abgebildet haben möchten. Die Änderungen können von uns oder Ihrem Labelwin-Betreuer gegen Abrechnung vorgenommen werden.

Damit die Kontostände ausgerechnet werden, müssen Sie den Haken bei ‚incl. Zeitkonto‘ setzen. Mit einem kurzen Durchlauf werden dann die Kontenstände in die Personaltabelle eingetragen und können somit in der Druckausgabe mit ausgegeben werden.

Die Daten werden übrigens aufgrund des Von und Bis-Datums erzeugt. Die Druckausgabe beinhaltet also den Kontenstand am Anfang des Monats und am Ende des Monats.

|

[Bild]

Eingangsrechnungen mit Kennzeichen für fehlenden Wareneingang

|

Wenn in einer Firma der Wareneingang gebucht wird (Modul Bestellüberwachung oder Lager) wird der entstehende Eingangslieferschein zum Vergleich der Eingangsrechnung genommen.

Durch die PDF-Rechnungen und besonders durch die ZUGFeRD-Rechnungen werden die Rechnungen manchmal schon vor dem Wareneingang gebucht.

In diesem Fall kann die Prüfung natürlich noch nicht stattfinden und wenn später die Wareneinbuchung erfolgt ist, merkt man es nicht, dass die Prüfung noch stattfinden muss.

Deshalb kann man nun dem Rechnungsverteilsatz ein Kennzeichen geben, wenn der Wareneingang fehlt. Natürlich darf man dies nur dann setzen, wenn die Ware später auch eingebucht wird. Ein solches Kennzeichen z.B. bei einer Versicherungsrechnung zu setzen, wäre unsinnig.

Sobald eine Lieferscheinnummer zugeordnet wird, verschwindet das Kreuz bei ‚Wareneingang fehlt‘

Später muss man bei den Rechnungen, bei denen der Wareneingang fehlt, die Buchung nachholen. Damit man jene Rechnungen erkennt, kann man das Kennzeichen in der Rechnungsliste anzeigen. Dazu muss mit einer TAB-Datei gearbeitet werden. (In einer TAB-Datei kann jeder festlegen, welche Felder er in der Tabelle sehen will).

In der Prüfmaske wird das Kennzeichen, dass der Wareneingang fehlt, ebenfalls gezeigt.

|

[Bild]

Projektsuche, anderes Projekt wählen

Seit der Umstellung auf die neue Menüfunktion in der Projektverwaltung gibt es eine Funktion, um sehr schnell ein anderes Projekt zu aktivieren. Da wir in der Hotline festgestellt haben, dass dies nicht sehr bekannt ist, hier eine kurze Beschreibung.

Zunächst der Hinweis, dass es weiterhin die Maske ‚Anderes Projekt‘.gibt. Zu finden unter dem Karteireiter ‚Projekt‘ als 3. Bild. Dort kann nach bestimmten Merkmalen eingegrenzt werden.

Am besten aber klickt man in die neue Suchzeile, die auch mit Strg F erreicht werden kann.

[Bild]

Es klappt eine Liste mit allen Projekten aus, die sich eingrenzt, sobald man etwas in die Suchzeile eingibt. Dabei ist es egal, in welchem Feld der Text zu finden ist.

[Bild]
