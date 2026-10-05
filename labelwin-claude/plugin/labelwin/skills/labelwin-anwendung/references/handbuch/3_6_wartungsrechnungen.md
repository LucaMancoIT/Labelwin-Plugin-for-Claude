# 3.6 Wartungsrechnungen

Pfad: Einrichtungsarbeiten > Einstellungen [14] > 3. Vorlagen > 3.6 Wartungsrechnungen
Quelle: handbuch/3_6_wartungsrechnungen.htm

|

3.6 Wartungsrechnungen

Wartungsrechnungen können als Einzelrechnung in dem Modul ADRESSEN unter dem Knopf ‚Verträge’ und dort unter dem Menüpunkt <Bearbeiten> <Rechnung erstellen> erstellt werden.

Der Seriendruck von Wartungsrechnungen erfolgt im Modul KUNDENDIENST unter dem Menüpunkt <Optionen> <Wartungsrechnungen schreiben>. In beiden Fällen kann auf die gleichen Muster-Rechnungen zugegriffen werden. Anmerken möchten wir noch, dass es sich hier nicht um die Abrechnung nach der Ausführung der Wartung, sondern aufgrund des erreichten und im Wartungsvertrag hinterlegten Termins handelt. Die Abrechnung nach Aufwand wird lediglich bei den Wartungsterminen hinterlegt.

[Bild]

Bild: Vorlagen Wartungsrechnungen

Bei der Erstellung von Wartungsrechnungen greift das Programm zwingend auf eine Musterrechnung zurück.

In unserer standardmäßig mitgelieferten Musterrechnung ist nur ein Artikel mit ‚Wartungspauschale’ enthalten.

Durch die nachfolgend beschriebenen Verfahren können in der Rechnung alle Daten aus dem Wartungsvertrag eingesetzt werden. In der Regel setzt man die entsprechenden Informationen in die Vorbemerkung, man kann sie jedoch auch in den ersten Artikel eintragen lassen. Im zweiten Artikel der Musterrechnung können alle Daten der Anlagen des betreffenden Vertrages eingesetzt werden. Wenn dem Wartungsvertrag mehrere Anlagen zugeordnet sind, wird der 2. Artikel mit den Anlagedaten für jede Anlage kopiert. Eine Wartungsrechnung mit 3 Anlagen enthält dann also 4 Positionen, nämlich die Wartungspauschale und für jede Anlage einen Textartikel, in dem die Anlagedaten über Schlüsselwort eingesetzt sind.

Als erstes müssen in einer Muster-Wartungsrechnung die Artikel u. Vorbemerkungen eingestellt werden.

· Starten des Programms Einstellungen

· Vorlagen

· Wartungsrechnungen wählen

· Gewünschten Eintrag markieren

· Ok bearbeiten

· Vorbemerkung schreiben wie z.B.

[Bild]

Bild: Vorbemerkung in Musterrechnung

· anschließend einen Artikel mit der Artikelart ‚Wartungspauschale’ anlegen.

· ggf. Text mit Schlüsselworten aus dem Vertrag versehen wie z.B.

[Bild]

Bild: Beispiel für Artikel-Kurztext Wartungspauschale

(in der Artikelmaske kann man mit F6 in diesem Fenster schreiben)

· falls Anlagedaten ausgegeben werden sollen, als 2. Artikel einen neuen Artikel anlegen mit der Artikelart ‚Textartikel’ mit F6 die Anlage-Schlüsselworte in den Kurztext schreiben wie z.B.

[Bild]

Bild: Beispiel für Textartikel

Dieser Artikel muss der 2. Artikel sein

Anmerkung: Ggf. sehen Ihre Masken etwas anders aus. Das liegt daran, dass wir die Bildschirmausdrucke mit einer Labelwin-Version erstellt haben, die bereits auf RTF umgestellt wurde.

Wenn Sie Näheres über die RTF-Formatierung erfahren möchten, lesen Sie hierzu bitte im Handbuch unter Formatierte Texte (RTF) und Bilddruck.

Nachfolgend sehen Sie die wichtigsten Schlüsselworte. Statt diese abzuschreiben, starten Sie besser das Modul SCHLÜSSELWORTE und wählen dort aus. Das Modul ist von vielen Stellen aus mit dem Knopf ‚Schlüsselworte’ zu aktivieren, kann aber auch durch eine Verknüpfung auf die Datei labelwin/schlüsselwort.exe gestartet werden.

Anlagen-Schlüsselworte:

Nur im 2. Artikel mit der Artikelart ‚Textartikel’ verwendbar.

|

Name

|

Beschreibung

|

@ANLLFDNR@

|

Laufende (nicht änderbare) Nummer der Anlage

|

@ANLANLAGENNAME@

|

Name der Anlage

|

@ANLANFAHRTZONE@

|

Anfahrtzone der Anlage

|

@ANLKM@

|

Kilometerzahl aus der Anlage

|

@ANLVERTRAGSNUMMER@

|

Vertragsnummer der Anlage

|

@ANLSTANDORTTEXT@

|

Standortbeschreibung der Anlage

|

@ANLZUSATZ1@

|

Zusatz 1

|

@ANLZUSATZ2@

|

Zusatz 2

|

@ANLZUSATZ3@

|

Zusatz 3

|

@ANLBESITZERANREDE@

|

Anrede aus der Besitzeradresse

|

@ANLBESITZERNAME@

|

Name aus der Besitzeradresse

|

@ANLBESITZERNAME1@

|

Name1 aus der Besitzeradresse

|

@ANLBESITZERSTRASSE@

|

Straße aus der Besitzeradresse

|

@ANLBESITZERPLZ@

|

Postleitzahl aus der Besitzeradresse

|

@ANLBESITZERORT@

|

Ort aus der Besitzeradresse

|

@ANLBESITZERTELEFON@

|

Telefon aus der Besitzeradresse

|

@ANLBESITZERFAX@

|

Faxnummer aus der Besitzeradresse

|

@ANLBESITZERDEBI@

|

Debitornummer aus der Besitzeradresse

|

@ANLBESITZERBRIEFANREDE@

|

Briefanrede aus der Besitzeradresse

|

@ANLBESITZERSUCHWORT1@

|

Suchwort aus der Besitzeradresse

|

@ANLSTANDORTANREDE@

|

Anrede aus der Standortadresse

|

@ANLSTANDORTNAME@

|

Name aus der Standortadresse

|

@ANLSTANDORTNAME1@

|

Name1 aus der Standortadresse

|

@ANLSTANDORTSTRASSE@

|

Straße aus der Standortadresse

|

@ANLSTANDORTPLZ@

|

Postleitzahl aus der Standortadresse

|

@ANLSTANDORTORT@

|

Ort aus der Standortadresse

|

@ANLSTANDORTTELEFON@

|

Telefon aus der Standortadresse

|

@ANLSTANDORTFAX@

|

Faxnummer aus der Standortadresse

|

@ANLSTANDORTDEBI@

|

Debitornummer aus der Standortadresse

|

@ANLSTANDORTBRIEFANREDE@

|

Briefanrede aus der Standortadresse

|

@ANLSTANDORTSUCHWORT1@

|

Suchwort aus der Standortadresse

|

@ANLSTANDORTLFDNR@

|

Interne lfd. Nr.

|

@ANLHAUSMEISTERANREDE@

|

Anrede aus der Hausmeisteradresse

|

@ANLHAUSMEISTERNAME@

|

Name aus der Hausmeisteradresse

|

@ANLHAUSMEISTERNAME1@

|

Name1 aus der Hausmeisteradresse

|

@ANLHAUSMEISTERSTRASSE@

|

Straße aus der Hausmeisteradresse

|

@ANLHAUSMEISTERPLZ@

|

Postleitzahl aus der Hausmeisteradresse

|

@ANLHAUSMEISTERORT@

|

Ort aus der Hausmeisteradresse

|

@ANLHAUSMEISTERTELEFON@

|

Telefon aus der Hausmeisteradresse

|

@ANLHAUSMEISTERFAX@

|

Faxnummer aus der Hausmeisteradresse

|

@ANLHAUSMEISTERDEBI@

|

Debitornummer aus der Hausmeisteradresse

|

@ANLHAUSMEISTERBRIEFANREDE@

|

Briefanrede aus der Hausmeisteradresse

|

@ANLHAUSMEISTERSUCHWORT1@

|

Suchwort aus der Hausmeisteradresse

|

@ANLRECHNUNGANREDE@

|

Anrede aus der Rechnungsadresse

|

@ANLRECHNUNGNAME@

|

Name aus der Rechnungsadresse

|

@ANLRECHNUNGNAME1@

|

Name1 aus der Rechnungsadresse

|

@ANLRECHNUNGSTRASSE@

|

Straße aus der Rechnungsadresse

|

@ANLRECHNUNGPLZ@

|

Postleitzahl aus der Rechnungsadresse

|

@ANLRECHNUNGORT@

|

Ort aus der Rechnungsadresse

|

@ANLRECHNUNGTELEFON@

|

Telefon aus der Rechnungsadresse

|

@ANLRECHNUNGFAX@

|

Faxnummer aus der Rechnungsadresse

|

@ANLRECHNUNGDEBI@

|

Debitornummer aus der Rechnungsadresse

|

@ANLRECHNUNGBRIEFANREDE@

|

Briefanrede aus der Rechnungsadresse

|

@ANLRECHNUNGSUCHWORT1@

|

Suchwort aus der Rechnungsadresse

Wartungsvertrag Schlüsselworte

Diese sind in der Vorbemerkung und dem 1. Artikel der Wartungsrechnung verwendbar

|

Name

|

Beschreibung

|

@WVSLFDNR@

|

Laufende Nummer des Wartungsvertrages

|

@WVSVERTRAGSNUMMER@

|

Vertragsnummer

|

@WVSVERTRAGSBEGINN@

|

Vertragsbeginn

|

@WVSVERTRAGSBEGINN@

|

Vertragsdauer

|

@WVSRGSUMME@

|

Rechnungssumme

|

@WVSRGMONAT@

|

Rechnungs-Monat

|

@WVSKOMMENTAR@

|

Kommentartext

|

@WVSKOMMENTARGROSS@

|

Kommentartext großes Feld (32000 Zeichen)

|

@WVSALLESTOERUNGEN@

|

„Alle Störungen“-Schalter

|

@WVSANMATERIALKOMPLETT@

|

„Material komplett“-Schalter

|

@WVSMATERIALSUMME@

|

Materialsumme

|

@WVSSAMMELRG@

|

„Sammelrechnung“-Schalter

|

@WVSVERTRAGSART@

|

Nummer der Vertragsart

|

@WVSARTIKELTEXT@

|

Artikeltext

|

@WVSFAHRTKOSTEN@

|

Fahrtkosten

|

@WVSPROJEKTNR@

|

Projektnr

|

@WVSLETZTERECHNUNG@

|

Datum der letzten Rechnung

|

@WVSPREISDATUM@

|

Preisdatum

|

@WVSRGSUMMEALT@

|

alte Rechnungsssumme

|

@WVSPREISDATUMALT@

|

altes Preisdatum

|

@WVSRECHNUNGANREDE@

|

Anrede aus der Rechnungsadresse

|

@WVSRECHNUNGNAME@

|

Name aus der Rechnungsadresse

|

@WVSRECHNUNGNAME1@

|

Name1 aus der Rechnungsadresse

|

@WVSRECHNUNGSTRASSE@

|

Straße aus der Rechnungsadresse

|

@WVSRECHNUNGPLZ@

|

Postleitzahl aus der Rechnungsadresse

|

@WVSRECHNUNGORT@

|

Ort aus der Rechnungsadresse

|

@WVSRECHNUNGTELEFON@

|

Telefon aus der Rechnungsadresse

|

@WVSRECHNUNGFAX@

|

Faxnummer aus der Rechnungsadresse

|

@WVSRECHNUNGDEBI@

|

Debitornummer aus der Rechnungsadresse

|

@WVSRECHNUNGSUCHWORT1@

|

Briefanrede aus der Rechnungsadresse

|

@WVSRECHNUNGSUCHWORT1@

|

Suchwort aus der Rechnungsadresse

|

@WVSBESITZERANREDE@

|

Anrede aus der Besitzeradresse

|

@WVSBESITZERNAME@

|

Name aus der Besitzeradresse

|

@WVSBESITZERNAME1@

|

Name1 aus der Besitzeradresse

|

@WVSBESITZERSTRASSE@

|

Straße aus der Besitzeradresse

|

@WVSBESITZERPLZ@

|

Postleitzahl aus der Besitzeradresse

|

@WVSBESITZERORT@

|

Ort aus der Besitzeradresse

|

@WVSBESITZERTELEFON@

|

Telefon aus der Besitzeradresse

|

@WVSBESITZERFAX@

|

Faxnummer aus der Besitzeradresse

|

@WVSBESITZERDEBI@

|

Debitornummer aus der Besitzeradresse

|

@WVSBESITZERBRIEFANREDE@

|

Briefanrede aus der Besitzeradresse

|

@WVSBESITZERSUCHWORT1@

|

Suchwort aus der Besitzeradresse
