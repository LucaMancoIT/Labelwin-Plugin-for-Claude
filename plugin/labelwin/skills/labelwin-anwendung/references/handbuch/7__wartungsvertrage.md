# 7. Wartungsverträge

Pfad: Adressverwaltung > Adressen [5] > 7. Wartungsverträge
Quelle: handbuch/7__wartungsvertrage.htm

|

7. Wartungsverträge

Wartungsverträge werden immer der Eigentümeradresse zugeordnet.

Ein Wartungsvertrag kann beliebig vielen Anlagen zugeordnet werden. Die Zuordnung geschieht dabei immer über die Anlage. In der Anlagenmaske wird unter dem Menüpunkt ‚Verträge’, ‚Zuordnen’ der Anlage einem Wartungsvertrag zugeordnet. Da dieser Weg beliebig oft wiederholt werden kann, können beliebig viele Anlagen einem Wartungsvertrag zugeordnet werden.

Da bei vielen Firmen die Wartung unmittelbar nach Ausführung berechnet wird, ist meist keine Erfassung der Wartungsverträge erforderlich. Es genügt dann, die Termine zu erfassen und dort ‚Berechnung nach Ausführung’ anzukreuzen.

Die Rechnungsstellung der Wartungsverträge kann per Durchlauf erfolgen, wobei die Selektion außer dem Rechnungsmonat über beliebige weitere Vertragsdaten erfolgen kann. Der automatische Rechnungslauf erfolgt über das Modul KUNDENDIENST unter dem Menüpunkt <Optionen> <Wartungsrechnungen schreiben>. Die Rechnungssummen können sowohl dem Vertrag oder einzelnen Wartungsterminen zugeordnet werden. Dabei dürfte der Regelfall sicherlich die Zuordnung bei den Wartungsverträgen sein. Der andere Weg ist in erster Linie für Firmen interessant, die Wartungen nach Aufwand abrechnen.

Damit Wartungen erfolgreich nachkalkuliert werden können, ist es erforderlich die Rechnungsstellung der Wartung mit einem besonderen Kennzeichen erfolgen zu lassen. Als Kennzeichen muss der Artikel mit dem Wartungspreis eine besondere Artikelart sein. In der Liste der Artikelarten wie z. B. Leistungspositionen, Prozentpositionen, Titel usw. gibt es eine Artikelart Wartungspauschale. Diese Wartungspauschale muss in der Wartungsrechnung verwendet werden, damit das Programm die Einnahmen dem Wartungsvertrag zuordnen kann.

[Bild: 7. Wartungsverträge]

Die Felder im roten Kasten sind nur sichtbar, wenn bei der Abrechnungsart [Nr.9] "nach Vertrag" angehakt ist.

|
[Bild: 1]

Menüleiste

[Bild: 1. Menüleiste]

Alle verfügbaren Menüpunkte werden im nächsten Abschnitt Wartungsverträge - Alle Menüpunkte beschrieben.

|
[Bild: 2]

Filterzeile

[Bild: 2. Filterzeile]

Hierbei handelt es sich um die gewohnte Filterzeile. Hier lässt sich die Liste der Verträge eingrenzen.

|
[Bild: 3]

Vertragsliste

[Bild: 3. Vertragsliste]

In dieser Liste werden alle Verträge eines Kunden angezeigt. Der Regelfall dürfte sein, dass nur ein Wartungsvertrag eingetragen ist. Wenn mehr Wartungsverträge eingetragen werden, als in der Liste darstellbar sind, so erscheint ein Laufbalken, mit dem geblättert werden kann. Alle Details des gerade aktiv markierten Wartungsvertrages sind in der Maske sichtbar.

|
[Bild: 4]

Laufende Nummer

[Bild: 4. Laufende Nummer]

Die laufende Nummer wird automatisch vom System vergeben. Sie haben auf diese Nummer keinen Einfluss.

|
[Bild: 5]

Vertragsnummer

[Bild: 5. Vertragsnummer]

In diesem Feld können Sie Ihre eigene Vertragsnummer einsetzen. Dabei erfolgt jedoch keine Prüfung, ob die Vertragsnummer bereits vergeben worden ist. Wir haben dieses Feld geschaffen, um Ihre bereits geschlossenen Wartungsverträge mit der damals zugeordneten Nummer eintragen zu können. Im Modul EINSTELLUNGEN unter dem Menüpunkt <Grundeinstellungen> <Nummernkreise> können Sie eine Anfangsvertragsnummer hinterlegen. Wenn Sie dann bei der Vertragsnummer nichts eingetragen, wird die nächst höhere Nummer automatisch eingetragen.

|
[Bild: 6]

Vertragsbeginn

[Bild: 6. Vertragsbeginn]

Tragen Sie hier den Beginn des Wartungsvertrags ein.

|
[Bild: 7]

Vertragsdauer

[Bild: 7. Vertragsdauer]

Wenn Sie in diesem Feld ein Kreuz eintragen, so gilt der Vertrag unbegrenzt. Das Kennzeichen dient in erster Linie der Selektion, um zeitlich begrenzt und zeitlich unbegrenzt laufende Verträge unterscheiden zu können.

|
[Bild: 8]

Gekündigt

[Bild: 8. Gekündigt]

Statt einen Vertrag zu löschen, können Sie ihn auf gekündigt setzen.

|
[Bild: 9]

Abrechnungsart

[Bild: 9. Abrechnungsart]

Legen Sie hier fest, wann der Wartungsvertrag berechnet werden soll. Viele Handwerker stellen die Wartungsrechnung nach der Ausführung der Wartung. In diesem Fall braucht von unserem Programm her kein Wartungsvertrag eingetragen werden. Wenn Sie dann noch einen Wartungsvertrag eintragen, so müssen Sie hier das Kreuz ‚nach Ausführung setzen’. In diesem Fall sind weitere Eingabefelder ausgeblendet, da die Erfassung der Daten dann keinen Sinn ergibt.

|
[Bild: 10]

Vertragsart

[Bild: 10. Vertragsart]

Wartungsverträge können bestimmten Vertragsarten zugeordnet werden, um z.B. darüber gezielt Auswertungen fahren zu können. So ist es z. B. denkbar, bestimmte Brennertypen, Anlagenelemente oder ähnliches über Vertragsarten zu gliedern. Da die Vertragsart als Selektionselement genommen werden kann, sind hiermit gezielte Auswertungen möglich.

>>> Empfehlung <<<

Label empfiehlt die Vertragsarten NICHT nach Anlagenart o.ä. einzuteilen, sondern nach dem Umfang des Vertrages. Sinnvoll sind Vertragarten wie z.B. „All inklusive“ oder "ohne Material".

Das hat den großen Vorteil, dass Sie beim Abrechnen von Wartungen in der Erledigt/Rechnung Maske des Kundendienstes eine wichtige Info sehen (nämlich die Bezeichnung der Vertragsart) nach der Sie gewisse für die Abrechnung wichtige Entscheidungen treffen können. Zum Beispiel, ob die Option „Fahrtkosten in Wartungs-Vertrag enthalten“ gesetzt werden sollte oder nicht.

[Bild]

Die Vertragsarten werden im Bereich EINSTELLUNGEN - Vertragsarten erfasst.

|
[Bild: 11]

Kommentar

[Bild: 11. Kommentar]

Tragen Sie in diesem Feld einen kurzen Kommentar zu dem Wartungsvertrag ein. Der Kommentar wird in der Wartungsliste (Nr. 3) gezeigt. Im Gegensatz zum Feld "Bemerkung " kann diese Eingabe zur Selektion genutzt werden.

|
[Bild: 12]

Bemerkung

[Bild: 12. Bemerkung]

Tragen Sie in dieses Feld beliebig viele Anmerkungen und Kommentare zu dem Wartungsvertrag ein. Der Inhalt dieses Feldes wird in der Regel nicht auf den Verträgen usw. ausgedruckt. Wenn Sie dies wünschen, ist es selbstverständlich möglich. Die Eintragungen in diesem Feld können nicht zur Selektion genutzt werden, sondern sind reine Anzeigen. Durch Betätigen des Knopfes ‚Datum/Zeit’ können Sie Ihre Anmerkung mit dem Eingabedatum versehen.

|
[Bild: 13]

Wartungszyklus

[Bild: 13. Wartungszyklus]

Die Eingabe eines Wartungszyklus dient lediglich der Druckausgabe auf der Wartungsrechnung.

Mittels der Schlüsselworte (@WVSWARTUNGVON@, @WVSWARTUNGBIS@ und @WVSWARTUNGSPERIODE@) kann in der Vorbemerkung der Wartungsrechnungsrechnung das Datum des Wartungsbeginns, das Ende und ggf. die Dauer in Monaten ausgegeben werden.

Das ist interessant und wichtig, wenn der Rechnungsmonat nicht der Beginn oder das Ende des Wartungszeitraumes ist.

Nach dem Druck der Rechnung wird das ‚Ab Datum‘ und das unsichtbare ‚Bis Datum‘ um die Anzahl der bei Periode angebenen Monate heraufgesetzt.

Die Periode wird in Monaten angegeben.

|

Hinweis: Eine Eingabe von 0 schaltet das Hochrechnen aus und bedeutet nicht, wie bei den Wartungsterminen, automatisch ein Jahr.

|
[Bild: 14]

Eigentümer

[Bild: 14. Eigentümer]

Tragen Sie hier die Anschrift desjenigen ein, mit dem der Wartungsvertrag geschlossen wurde. In der Regel ist das der Eigentümer der Anlage.

|
[Bild: 15]

Rechnungsanschrift

[Bild: 15. Rechnungsanschrift]

In der Regel wird die Rechnungsanschrift mit der Besitzeradresse identisch sein. Anderenfalls können Sie hier den Adresskurznamen der Rechnungsanschrift einsetzen.

|
[Bild: 16]

Projekt

[Bild: 16. Projekt]

Durch Betätigung des Knopfes ‚Projekt’ können Sie das gewünschte Projekt aus der Liste der angelegten Projekte auswählen. In dem Eingabefeld wird das Projekt gezeigt, zu dem der Wartungsvertrag zugeordnet wird. Die Zuordnung von Wartungsverträgen zu Projekten mag etwas merkwürdig erscheinen, aber nur so ist gewährleistet, dass sämtliche Kosten und Erträge projektbezogen ausgewertet werden können. Eine automatisch erzeugte Rechnung wird in diesem Projekt abgelegt.

|
[Bild: 17]

Erlöskonto

[Bild: 17. Erlöskonto]

Hier kann ein Erlöskonto für die Wartungsrechnung vorgegeben werden. Diese Option ist nur sichtbar, wenn mit Erlöskonten gearbeitet wird.

Hintergrund: Beim Schreiben der Wartungsrechnungen nach Vertrag (die meisten nutzen die Möglichkeit ‚nach Ausführung‘) wird standardmäßig das Erlöskonto für alle gleich aus dem Projekt genommen. Wenn Sie aber ein Konto im Vertrag selbst hinterlegen, hat dieses Vorrang.

|
[Bild: 18]

Rechnungsmonat

[Bild: 18. Rechnungsmonat]

Tragen Sie hier den Monat ein, in dem die Rechnungsstellung erfolgen soll. Bei der Rechnungsserie wird auf dieses Datenfeld zugegriffen, um die fälligen Rechnungen zu ermitteln.

|
[Bild: 19]

RG.-Betrag an Termin

[Bild: 19. RG.-Betrag an Termin]

Standardmäßig werden die Rechnungsbeträge dem Wartungsvertrag zugeordnet. Wenn Sie in diesem Datenfeld ein Kreuz setzen, werden die Rechnungsbeträge dem Wartungstermin zugeordnet. Dieses ist nur dann sinnvoll, wenn die Abrechnung aufgrund der Termine erfolgt. Wenn Sie in diesem Feld ein Kreuz setzen, so können Sie in den Feldern 17 und 18 keine Eintragungen vornehmen. Die Wartungssumme setzt sich in diesem Fall aus den bei den Terminen hinterlegten Einzelbeträgen zusammen. Wenn nun bei den Terminen ein weiterer Wartungstermin hinzukommt, erhöht sich automatisch die Wartungssumme um den beim neuen Termin eingetragenen Betrag.

|
[Bild: 20]

Rechnungssumme

[Bild: 20. Rechnungssumme]

Hier tragen Sie Ihren Preis für den Wartungsvertrag ein.

Sollten Sie Material beim Vertrag hinterlegt haben (Knopf Nr. 31), so wechselt die Beschriftung von "Rechnungssumme" auf "Pauschale (+ Material)" damit man direkt sieht, dass auch noch Wartungmaterial hinzukommt.

[Bild]

Pauschale (+Material): Wenn Sie dem Vertrag Wartungsmaterial hinterlegt haben, kann eine Wartungspauschale zusätzlich eingetragen werden.

Der Preis in der Rechnung setzt sich dann aus der Wartungspauschale und den hinterlegten Materialien zusammen. Wenn die Wartungspauschale auf 0 steht, wird nur das hinterlegte Material genommen. Die Wartungspauschale muss dann als Materialartikel hinterlegt werden. Dieser Betrag wird bei dem automatischen Rechnungsdruck verwendet. Die alte Rechnungssumme wird automatisch rechts daneben eingetragen, wenn Sie nach einer Preisänderung den Knopf ‚Speichern’ drücken.

Wenn Sie die Rechnungssumme ändern und den Knopf ‚Speichern’ drücken, erscheint eine Abfrage.

[Bild]

Hier haben Sie dann die Möglichkeit, das aktuelle Tagesdatum als Preisdatum einzutragen oder aber, wenn Sie zuvor bereits ein Datum eingetragen haben, dieses unverändert bestehen lassen.

|
[Bild: 21]

Sammelrechnung

[Bild: 21. Sammelrechnung]

Tragen Sie hier ein Kreuz ein, wenn die Rechnungsstellung über eine Sammelrechnung erfolgen soll. Das Programm sucht in diesem Falle alle fälligen Rechnungen dieser Rechnungsanschrift zusammen und trägt diese in eine Gesamtrechnung ein.

|
[Bild: 22]

Fahrtkosten enthalten

[Bild: 22. Fahrtkosten enthalten]

Wenn die Fahrtkosten mit der Wartungspauschale abgedeckt sind, setzen Sie in diesem Feld ein Kreuz.

|
[Bild: 23]

Material enthalten

[Bild: 23. Material enthalten]

Wenn alle Verbrauchsmaterialien mit der Wartungspauschale abgedeckt sind, so tragen Sie hier ein Kreuz ein. Anderenfalls können Sie in dem Feld daneben eine Materialsumme eintragen, bis zu deren Höhe keine separate Rechnung gestellt wird. In der Regel dürfte dieses Feld bei den meisten Kunden mit 0 belegt werden, da üblicherweise sämtliche Materialien separat in Rechnung gestellt werden.

bis: Hier kann eine Summe eingesetzt werden, bis zu der die Materialien über den Vertrag abgedeckt sind. Es handelt sich um ein reines Infofeld.

|
[Bild: 24]

Letzte Rechnung

[Bild: 24. Letzte Rechnung]

Wenn die Rechnungsstellung nach Vertrag erfolgt und Sie Rechnungen über einen automatischen Rechnungslauf ausdrucken, wird hier das Datum der letzten Rechnung eingetragen. Das geschieht auch, wenn Sie über den Menüpunkt <Bearbeiten> <Rechnung erstellen> die Rechnung einzeln ausdrucken.

|
[Bild: 25]

Störungen

[Bild: 25. Störungen]

Wenn Sie in diesem Feld ein Kreuz setzen, so werden alle Störungen über die Wartungspauschale abgewickelt. Wenn Sie hier kein Kreuz einsetzen, haben Sie die Möglichkeit, die Anzahl der inbegriffenen Störungen einzutragen. (Es erscheint rechts ein Eingabefeld)

Anzahl der Störungen: Falls eine bestimmte Anzahl über den Vertrag abgedeckt ist, wird diese hier eingetragen. Es handelt sich um ein reines Infofeld.

|
[Bild: 26]

Neu F2

[Bild: 26. Neu F2]

Durch Betätigen dieses Knopfes wird die Erfassungsmaske für Wartungsverträge geleert und Sie können einen neuen Vertrag anlegen.

|
[Bild: 27]

Speichern

[Bild: 27. Speichern]

Durch Betätigen dieses Knopfes werden die Eintragungen abgespeichert und in die Vertragsliste (Nr. 3) eingetragen. Sollte es sich um einen neuen Wartungsvertrag handeln, so wird er zusätzlich in die Liste eingetragen. Sollte es sich um eine Änderung handeln, so werden die bisherigen Daten überschrieben.

|
[Bild: 28]

Zugeordnete Dokumente

[Bild: 28. Zugeordnete Dokumente]

Durch Betätigen dieses Knopfes kommen Sie Liste der bereits hinterlegten Dokumente und haben dort die Möglichkeit, ein neues Dokument anzulegen. Wie gewohnt, kann man auch per Drag & Drop neue Dokumente an den Vertrag anhängen.

|
[Bild: 29]

Anlagen

[Bild: 29. Anlagen]

Wenn dem Wartungsvertrag Anlagen zugeordnet sind, so können Sie durch Betätigen dieses Knopfes die Anlagen einsehen. Die Anlagen werden einem Wartungsvertrag zugeordnet, indem bei der Anlagenadresse der Knopf ‚Anlagen’ gewählt wird. In der dann erscheinenden Maske wird über den Menüpunkt <Verträge> <Zuordnen> die Verknüpfung zwischen einer Anlage und dem Wartungsvertrag hergestellt. Lesen Sie dazu bitte in dem entsprechenden Kapitel Wartungstermine und Wartungsverträge nach.

|
[Bild: 30]

Zuordnen

[Bild: 30. Zuordnen]

Dieser Button ist nur sichtbar, wenn man aus der Anlagen Maske (siehe Punkt 4. Anlagen) heraus die Vertragszuordnung aufgerufen hat. Dann erscheint die Vertragsübersicht mit der Möglichkeit den Vertrag der Anlage zuzuordnen. Ein Vertrag kann übrigens mehreren Anlagen zugeordnet sein.

|
[Bild: 31]

Material

[Bild: 31. Material]

Sie haben die Möglichkeit, dem Wartungstermin Material zu hinterlegen. Wenn Sie unter Punkt 16 eine Wartungspauschale eingetragen haben, werden die Materialkosten zur Wartungspauschale hinzugerechnet. Dieser Knopf ist jedoch nur sichtbar, wenn Sie im Modul Einstellungen unter dem Menüpunkt <Programmbereiche> <Anlagen und Verträge> <Grundeinstellungen> die Materialhinterlegung aktiviert haben.

|
[Bild: 32]

Ende

[Bild: 32. Ende]

Durch Betätigen des Endeknopfes wird die Maske geschlossen. Sollten von Ihnen Änderungen vorgenommen worden sein ohne den Knopf ‚Speichern‘ (Nr. 17) betätigt zu haben, gehen diese Änderungen verloren.
