# 2.9.1 Grundeinstellungen

Pfad: Einrichtungsarbeiten > Einstellungen [14] > 2. Programmbereiche > 2.9 Buchhaltung > 2.9.1 Grundeinstellungen
Quelle: handbuch/2_9_1_grundeinstellungen.htm

|

2.9.1 Grundeinstellungen

In dieser Maske werden die Verteilungen und Vorgaben für die Eingangsrechnungen festgelegt.

Allgemeine Einstellungen

[Bild]

Bild: Grundeinstellung Ein- + Ausgangsrg

Erlöskonten verwenden: Bei der Verwendung von Erlöskonten muss jede Rechnung einem bestimmten Konto zugeordnet werden. Das Erlöskonto ist bereits im Datenblatt wählbar und wird dann an die Rechnungen vererbt. Bei der Rechnungserstellung kann das Erlöskonto dennoch umgesetzt werden.

Keine Überprüfung der MwSt. beim Druck: Beim Durchrechnen und Speichern erfolgt eine Warnung bei der Verwendung eines nicht ‚normalen’ MwSt.-Satzes. Wenn ein Kunde es nicht merkt und es auf dem Formular nicht ausgewiesen wird, können falsche Rechnungen gedruckt werden. Für den Druck unterschiedlicher MwSt.-Sätze ist das Formular rg3divMw.rpt erforderlich. Wenn Sie die Warnung jedoch stört, aktivieren Sie dieses Feld.

RG-Druck nur mit Debitorennr.: Wenn in der Finanzbuchhaltung mit Debitorennummern gearbeitet wird, so ist es sinnvoll den Rechnungsdruck ohne Debitorennummern zu verhindern.

Lieferschein-Druck nur mit Debitorennr.: Durch Aktivieren dieses Feldes legen Sie fest, dass auch ein Lieferschein-Druck nur mit einer Debitorennummer erfolgen kann.

Rechnungs-Kz verwenden (einstellig): Ein Rechnungskennzeichen ist ein Buchstabe oder Zahl, mit der jede Rechnung bei Beginn und auch der Druckausgabe versehen werden kann. Ursprünglich wurde es geschaffen, um Rechnungen zu kennzeichnen, die an ein Factoring-Unternehmen (Verkauf von Forderungen) übergeben werden sollten. Es kann aber auch anderweitig eingesetzt werden.

Im Rechnungsausgangsbuch kann aufgrund dieses Kennzeichens zusätzlich eingegrenzt werden. Auch die Summe von Rechnungen mit einem bestimmten Kennzeichen können gezeigt werden.

Nur Istversteuerte Abschläge zulassen: Hier geht darum, dass manche Firmen ausschließlich Ist-Versteuerte Abschläge zulassen wollen.

Das hat auch Auswirkungen auf die Dokumentenart ‚Teilrechnung'. Dort können bei aktiviertem Feld nur noch kumulierte Teil-Schlussrechnungen geschrieben werden.

Wenn es darum geht, dass bei einem Abschlag die einzelnen Positionen aufgelistet werden sollen, so kann das auch in einer Abschlagsrechnung erfolgen. Teilrechnungen ohne das Kennzeichen ‚abgeschlossene Teilleistung' (=Teilschlussrechnung) würden wie normale Rechnungen ausgewertet und sind deshalb nicht zulässig, wenn Sie generell mit IST-Versteuerung arbeiten möchten.

Mandantenhinweis: Das Feld muss ggf. bei jeder Firma aktivierte werden.

Mahntexte mandantenabhängig: Diese Frage ist nur für Betriebe mit einer Mandantenversion interessant. Damit können die Texte der Mahnungen für jeden Mandanten getrennt erfasst werden, während sonst für alle Mandanten die gleichen Texte verwendet würden.

Bestelldruck nur mit Kreditornummer: Durch Aktivieren dieses Feldes ist der Druck von Bestellungen nur möglich, wenn beim Lieferanten eine Kreditorennummer hinterlegt ist.

Offene Posten aufgrund der Eigentümeradresse: Es geht um die Anzeige der offenen Posten im Kundendienstmodul. Wenn Rechnungen an eine Immobilienverwaltung gehen (als Rechnungsanschrift, nicht als Versandadresse), dann ist es sinnvoll zu sehen, ob der Eigentümer seine Rechnungen bezahlt hat.

Fibu-Erfassung nicht nutzen: Sollte trotz Vorhandensein des Moduls Fibu-Erfassung diese nicht eingesetzt werden, kann man sie hiermit deaktivieren.

Abbruch: Hiermit wird die Maske der Einstellungen geschlossen, ohne dass die Änderungen übernommen werden.

Ok: Hiermit werden die Änderungen übernommen und die Maske geschlossen.

Eingansgrechnungen - Grundeinstellungen

[Bild]

Verteilung der Buchung: Hier legen Sie fest, ob die Eingangsrechnungen auf Projekte und gegebenenfalls Warenkonten verteilt werden sollen. Um eine umfangreiche Nachkalkulation durchführen zu können, müssen Sie Eingangs-rechnungen bezogen auf ein Projekt einbuchen. Dabei ist die Verteilung einer Eingangsrechnung auf beliebig viele Projekte möglich. Es empfiehlt sich, die Rechnungen vom Großhändler kommissionsweise erstellen zu lassen, um an dieser Stelle keine detaillierte Verteilung vornehmen zu müssen. Mindestens sollte jedoch die Großhändlerrechnung projektweise/baustellenweise gegliedert sein. Die Verteilung auf Warenkonten ist immer dann notwendig, wenn Sie die Daten in eine Finanzbuchhaltung übernehmen wollen. In diesem Fall müssen Sie die Warenkonten ebenfalls erfasst haben.

Vorgabe Warenkonto: An dieser Stelle können Sie das Warenkonto als Vorgabe einsetzen. Bei jeder neuen Rechnungseintragung wird das Programm dieses Konto vorschlagen. Der Einsatz eines Kontos ist nur dann erforderlich, wenn die Daten an eine Finanzbuchhaltung übergeben werden sollen. Die Erfassung ist im Kapitel 14.4.9 beschrieben. Warenkonten können bei der Lieferantenadresse hinterlegt werden.

Standardprojekt: Wenn hier ein Projekt hinterlegt ist, gibt es in der Erfassmaske der Eingangsrechnungen einen Knopf mit der Beschriftung '...' neben der Projekteingabe. Mit diesem Knopf kann dann das hier hinterlegte Projekt gewählt werden. Sinnvoll ist es für diverse Rechnungen von Versicherungen, Miete Büromaterial usw.

Interne Belegnummer veränderbar: Das Programm zählt standardmäßig den internen Zähler automatisch hoch. Der Aufsatzpunkt des Zählers wird im Modul EINSTELLUNGEN unter dem Menüpunkt <Grundeinstellungen> <Nummernkreise> vorgegeben.

Betriebe, die alle Eingangsrechnungen über Stempel mit einer eigenen Nummer versehen, erfassen in unserem Programm ggf. nicht alle Eingangsrechnungen. Über diese Option kann der interne Zähler bei der Erfassung manuell verändert werden.

Erfassung auf Positionen: Wenn dieser Schalter gesetzt ist, kann bei solchen Projekten, bei denen eine Basis (Dokumentenart Projektbasis) vorhanden ist, die Zuordnung einer Rechnung auf einzelne Positionen oder Titel erfolgen. In der Regel ist dies nicht sinnvoll, weil es relativ aufwendig ist.

Preise vom Eingangslieferschein in Stammdaten EK2 eintragen: Wenn Sie dieses Feld aktivieren, werden die Preise beim Erfassen der Eingangslieferscheine im entsprechenden Katalog in die Stammdaten EK2 eingetragen.

Wie vor jedoch 'normalen' EK (überschreibt Datanprm-Preise): Wenn Sie dieses Feld aktivieren, werden die Preise beim Erfassen der Eingangslieferscheine im entsprechenden Katalog in die Stammdaten EK1 eingetragen. Sie sollten jedoch dabei bedenken, dass in diesem Fall die Preise der Datanorm überschrieben werden.

Vorgabe Status ‚gesperrt’ bei neuen Rechnungen: Wenn Sie dieses Feld aktivieren, werden alle neu erfassten Eingangsrechnungen mit dem Status ‚gesperrt’ versehen. Wenn Sie dann bei Vorgaben für den Zahlungslauf das Feld ‚ohne gesperrte Rechnungen’ aktivieren, können Sie verhindern, dass vor der Rechnungsprüfung evtl. eine Rechnung versehentlich bezahlt wird.

Offene KDA bei erster Buchung nach ‚in Arbeit’: Wenn Sie dieses Feld aktivieren und auf einen Kundendienstauftrag eine Eingangsrechnung erfassen, wird der Auftrag im Status von ‚offen’ auf ‚in Arbeit’ gesetzt.

Projekte bei erster Buchung auf "in Arbeit" setzen: Mit dieser Option wird erreicht, dass der Projektstatus automatisch auf "in Arbeit" gesetzt wird, wenn eine Eingangsrechnung auf dieses Projekt gebucht wird.

Schlossverwaltung aktiv: Um bei mehreren Filialen, die jedoch alle zu einer Firma gehören, die Eingangsrechnungen für die jeweils anderen Filialen unsichtbar zu machen, haben Sie die Möglichkeit der Schlossverwaltung. Auf diese Art können Rechnungen für einzelne Filialen weggefiltert werden. Das Schloss wirkt auf die ganze Rechnung. Es ist dann so, als würde die Rechnung nicht existieren, wenn der Anwender nicht den passenden Schlüssel hat. In der Projektverwaltung kann man die Verteilbuchungen der Eingangsrechnungen sehen, die das aktive Projekt betreffen. Dieses ist weiterhin möglich, unabhängig vom Schloss der Rechnung. Da auch gefilterte Rechnungen einem Projekt zugeordnet sind, muss das Projekt natürlich auch über ein entsprechendes Schloss abgesichert sein. Dieses geschieht im Modul EINSTELLUNGEN unter dem Menüpunkt <Optionen> <Berechtigungsschloss>.

projektspezifische Zahlungsbedingungen: Zahlungs-bedingungen werden manchmal für bestimmte Projekte speziell mit dem Lieferanten ausgehandelt. Gewissermaßen übernimmt der Lieferant damit die Zwischenfinanzierung, die sonst über eine Bank abgewickelt werden müsste. Wenn dieser Schalter gesetzt ist, so gibt es im Projekt Datenblatt einen neuen Knopf ‚Zahlungsbedingung'. Dort wird der Lieferantenname aufgerufen und als Vorschlag die in der Adresse hinterlegten Zahlungsbedingungen gezeigt. Nach der Anpassung werden die Daten speziell für dieses Projekt gespeichert.

Im Rechnungseingangsbuch kann man dann unmittelbar nach Wahl der Adresse des Lieferanten das Feld Projektnummer ausfüllen. In diesem Fall schaut das Programm nach, ob es spezielle Zahlungsbedingungen für dieses Projekt und diesen Lieferanten gibt. Wenn ja, werden diese verwendet, wenn nein, werden die ‚normalen' Zahlungsbedingungen aus der Adresse verwendet.

Die Projektnummer wird als Vorschlag in die Verteilmaske übernommen, damit keine doppelte Erfassung erforderlich ist.

Buchungen ohne Kreditornummer nicht zulassen: Aktivieren Sie dieses Feld, wenn Sie Buchungen auf ein spezielles Lieferantenkonto vornehmen möchten. Damit verhindern Sie, dass Eingangsrechnungen in der Finanzbuchhaltung auf einem Sammel-Kreditorenkonto gebucht werden.

Warnung, wenn Projekt <> "in Arbeit": Sie erhalten eine Warnung, wenn SIe auf ein PRojekt buchen, dass nicht den Status "in Arbeit" hat.

abweichender Zahlungsempfänger wählbar: Bei Einkaufsverbänden ist kommt die Rechnung manches Mal vom Lieferanten und muss beim Verband bezahlt werden. Dazu gibt es in der Adressmaske auf der Seite ‚Bankdaten' die Möglichkeit, eine Rechnungsadresse für Eingangsrechnungen zu erfassen.

Bei diesem Schalter geht es darum, unter welcher Adresse die Rechnung nachher sichtbar ist.

Ohne gesetzten Schalter

Die Lieferantenadresse wird aufgerufen und die Adresse wird sofort auf die Zahlungsempfänger-Adresse umgeschaltet. Die Zahlungsbedingung wird von der Lieferantenadresse genommen.

Mit gesetztem Schalter

Bei Aufruf einer Adresse mit hinterlegter Zahlungsempfänger-Adresse erscheint ein Ankreuzfeld ‚Zahlung an:..'. Das Feld ist als Vorgabe aktiviert. Damit wird die Rechnung unter der Lieferantenadresse geführt und nur die Bezahlung erfolgt an den Zahlungsempfänger. Ohne Vorgabe wird speziell diese Rechnung direkt bezahlt.

Die hinterlegte Empfängeradresse dient also nur als Vorgabe für das Ankreuzfeld.

Bei der Bezahlung wird automatisch die richtige Adresse verwendet. Über eine weitere Eingrenzung kann man auf alle Rechnungen eines Zahlungsempfängers eingrenzen.

Eingangsrechnungen - Zahlungs-Einstellungen

[Bild]

Bezahlen per Zahlungslauf (Vorgaben):

Vorgabe auf ‚nur geprüfte Rechnungen’: Wenn Sie dieses Feld aktivieren, werden nur geprüfte Rechnungen im Zahlungslauf angezeigt.

Vorgabe auf ‚ohne gesperrte Rechnungen’: Wenn Sie dieses Feld aktivieren, werden gesperrte Rechnungen im Zahlungslauf nicht angezeigt.

Vorgabe auf ‚Eingrenzen nach Fälligkeit mit Skonto: Hier können Sie einen Vorgabetermin setzen. Wenn z. B. bei Ihnen alle 7 Tage ein Zahlungslauf erfolgt, können Sie festlegen, dass alle fälligen Rechnungen bis in 6 Tagen gezeigt werden.

Kontostand zeigen: Durch Aktivieren diese Feldes wird Ihnen in der Zahlungslaufmaske der aktuelle Kontostand der gewählten Bank angezeigt. Dieses ist jedoch nur bei der Nutzung der Fibuerfassung möglich.

Kommentarzeilen je Scheck: Bei der Verwendung von besonderen Scheckformularen wird hier festgelegt, wie viele Kommentarzeilen gedruckt werden können.

Eingangsrechnungen - Import ZUGFeRD/Gaeb/UGL

[Bild]

Standardprojekt: Die in der Datei enthaltenen Artikel werden in diesem Projekt als Dokument angelegt. Da die Dokumente keine Auswertungsrelevanz haben, werden sie als ‚Freier Text' angelegt. Richten Sie sich ein Projekt speziell dafür ein, das auch bei Auswertungen nicht berücksichtigt wird.

Kalk.einstellung: Die Rechnung wird als Dokument abgelegt, um ggf. Artikel daraus übernehmen zu können. Die Artikel werden zwangsläufig mit einer Kalkulations-Einstellung kalkuliert, die Sie hier festlegen können.

Nehmen Sie am besten eine Kalkulationseinstellung mit einer Preisbildung mit Einkauf * 1,0 und ohne Zeitübernahme (also ohne Minuten) oder rechnen Sie den Verkauf mit z.B. Einkauf * 1,3.

importierte Datei verschieben statt löschen: Nach Einlesen der UGL-Datei kann diese eigentlich gelöscht werden. Stattdessen können Sie diese aber in ein Sicherungsverzeichnis verschieben, um ggf. noch einmal nachschauen zu können.

Diff.-Projekt: Beim Import von Eingangsrechnungen wird eine Verbindung zu eventuell vorhandenen Eingangslieferscheinen hergestellt. Wenn zu einer Rechnung des Lieferanten mehrere Eingangslieferscheine vorhanden sind, wird immer ein zusätzlicher Verteilsatz angelegt, in dem die Differenz zwischen der Rechnungssumme und der Summe der Eingangslieferscheine abgelegt wird.

Die Differenzbuchung wird dem hier hinterlegten Projekt zugeordnet. Wenn Sie keine Vorgabe treffen, muss das Konto immer manuell gewählt werden.

Import-Protokoll erzeugen: Dieses Feld ist standardmäßig aktiviert. Im Hintergrund öffnet sich der Editor. Hier werden dann Lieferschein-Nr,, Bestell-Nr., wenn eine Bestellung usw. protokolliert.

[Bild]

PDF sofort anzeigen, wenn vorhanden: Sowohl mit UGL, als auch mit Gaeb kann die Rechnung als Pdf mitgeliefert werden.

Wenn Sie dieses Feld aktivieren, wird neben der Erfassmaske der Rechnung sofort die Pdf angezeigt. Ggf. sollte man das Fenster auf den 2. Monitor schieben. Sobald die Rechnung gespeichert oder die Erfassung abgebrochen wird, wird das Anzeigefenster automatisch geschlossen.

Hinweis: Die Pdf-Datei muss im gleichen Verzeichnis wie die UGL-Datei liegen. Bei GC heißen diese Dateien RG...Nr..._1.pdf, wenn die UGL-Datei die Extension (Dateiendung) .001 hat.

immer ‚eigene‘ Zahlungsbedingungen nehmen: Beim Import von Eingangsrechnungen per Datei ist oft ein Unterschied zwischen den Daten der Datei und denen, die bei der Lieferantenadresse hinterlegt sind. Sobald Unterschiede bestehen, wird eine Maske mit den Differezen gezeigt, in der man sich entscheiden muss, welche Daten verwendet werden sollen.

Diese Anzeige stört natürlich im Arbeitsablauf. Daher kann es sinnvoll sein, immer die eigenen, bei der Adresse hinterlegten Bedingungen zu verwenden.

Online-Rabatt als separaten Verteilsatz: Wenn ein Lieferant einen Rabatt aufgrund einer Online-Bestellung gewährt, führt dieses zu Unterschieden zwischen dem Wert der Bestellung bzw. dem Eingangslieferschein sowie dem Rechnungsblock. Wenn immer Unterschiede da sind, kann man die ‚echten' Probleme (falsche Artikel, Mengen, Preise) nicht mehr erkennen.

Vorteil: Mit dieser Option werden die Positionen mit dem Online-Rabatt ‚neutralisiert' und als letzter Verteilsatz in einer Summe gebucht.

Damit sind ausgewiesene Unterschiede echte Unterschiede.

Nachteil: Der Online-Rabatt wird nicht auf das jeweilige Projekt gebucht, sondern auf das in dieser Maske vorgegebene Standard-Projekt.

Problem: Der Online-Rabatt ist nicht eindeutig erkennbar. Bei der GC-Gruppe identifizieren wir ihn am Text ‚Online - Vergütung'. Bei anderen Lieferanten sind vielleicht Anpassungen erforderlich - sprechen Sie uns ggf. an.

Eingangsrechnungen - Rechnungsprüfung Eingang

[Bild]

Rechnungsprüfung aktiv: Durch Markieren dieses Feldes aktivieren Sie die Rechnungprüfung.

Bei aktivierter Rechnungsprüfung kann mit dem Feld ‚Vorgabe auf nicht prüfen’ festgelegt werden, ob die Vorgabe beim Erfassen von neuen Rechnungen auf Prüfen steht oder nicht.

Bereits bei der Erfassung kann festgelegt werden, wer die Prüfung vornehmen soll. Über eine ‚Prüfenmaske’ kann dann jeder Mitarbeiter seine Rechnungen auf ‚geprüft’ oder ‚fehlerhaft’ setzen. Bei der Bezahlung kann man eingrenzen, dass nur die komplett geprüften Rechnungen angezeigt werden. Da eine Rechnung auf mehrere Projekte oder KD-Aufträge aufgeteilt werden kann, wird der Prüfer je Verteilung festgelegt. Die Rechnung bekommt erst dann den Status ‚geprüft’, wenn alle Verteilungen geprüft worden sind.

Es werden als Prüfer alle Mitarbeiter angeboten, die in den Personalstammdaten erfasst und mit dem Kennzeichen ‚Verwaltung’ versehen sind. Im Modul EINSTELLUNGEN können Sie festlegen, dass die ‚Verwaltungsmitarbeiter’ im Projektdatenblatt als ‚Verantwortlich’ angeboten werden. Wenn ein Projekt einen eingetragenen Verantwortlichen hat, so wird dieser als Rechnungsprüfer vorgeschlagen. Wenn Sie diese Einstellung nicht treffen, so müssen Sie bei jeder Rechnung festlegen, wer sie prüfen soll.

Prüfstatus bei Erfassung anwählbar

Wenn dieses Feld aktiviert ist, kann der Prüfstatus schon während der Erfassung auf ‚geprüft' oder ‚fehlerhaft' gesetzt werden. Wie sinnvoll dies ist, muss jeder Betrieb für sich entscheiden.

Prüfer dürfen Projektzuordnung ändern

Wenn dieses Feld aktiviert ist, erscheint in der Maske der Rechnungsprüfung vor dem Feld der Projektnummer ein Knopf, mit dem das Projekt gewechselt werden kann.

Dies bedeutet zwar eine gewisse Flexibilität bei falsch zugeordneten Projekten, birgt aber auch eine Gefahr, dass Rechnungen auf ‚Diverses' geschoben werden, um das eigene Projekt nicht zu belasten.

Priorität (2. Prüfer erst nach 1. Prüfung aktivieren):

Wenn Sie dieses Feld aktivieren, erreichen Sie, dass der 2. Prüfer erst ins Spiel kommt, wenn der erste Prüfer die Rechnung als ‚geprüft' kennzeichnet hat. Die Logik dahinter ist, dass ein Chef als 2. Prüfer die Rechnungen erst in seiner ‚zu prüfen-Liste' sehen möchte, wenn der Bauleiter sie für richtig befunden hat.

Die folgende Vorgabe muss für jeden Prüfer speziell festgelegt werden. Damit können je nach erstem Prüfer unterschiedliche Mitarbeiter als Folgeprüfer vorbelegt werden. Ohne die Vorgabe wird die Liste aller möglichen Prüfer zur Auswahl angeboten.

2. Prüfer (Vorgabe): Wenn Sie bei der Rechnungsprüfung mit 2 Prüfern arbeiten, kann hier der 2. Prüfer festgelegt werden. Diese Einstellung ist dann sinnvoll, wenn es sich bei dem 2. Prüfer immer um die gleiche Person z.B. aus der Buchhaltung handelt.

Eingangsrechnungen - Scannen

[Bild]

Extension für Scannerdateien: Es besteht die Möglichkeit, die Rechnungen in ihrer Originalerscheinung im System zu hinterlegen. Dazu müssen diese eingescannt werden. Die Scanner erzeugen automatisch eine Datei mit einem bestimmten Namensanhängsel. Dieses Anhängsel wird als Extension bezeichnet. Wenn Sie keine Eingangsrechnungen einscannen wollen, so ist hier keine Eingabe erforderlich. Üblicherweise werden die Rechnungen heute mit ELO gescannt. Dann ist hier kein Eintrag erforderlich. Die meisten Scanner erzeugen Dateien mit Extension tif, da hier mehrere Seiten einer Rechnung in einem Dokument abgelegt werden können. Tragen Sie hier ggf. den richtigen Wert ein. Im Kapitel Eingangsrechnungen finden Sie eine ausführliche Beschreibung des Scannens.

ELO Scan RV-Nummer = interne Nummer: Wenn Sie mit dem Zusatzmodul ELO-Anbindung arbeiten und hier ein Häkchen setzen, wird Ihnen beim Speichern der Rechnung eine interne RV Nummer angezeigt.

Eingangsrechnung vor Erfassung scannen: Wenn Sie dieses Feld aktivieren, müssen Sie Ihre Eingangsrechnungen mit Aufklebern mit einer eindeutigen RV-Nummer versehen und eingescannt werden. Bei der späteren Erfassung der Eingangsrechnung muss dann diese RV-Nummer eingegeben werden. Eine nähere Beschreibung finden Sie im Handbuch unter ELO Dokumentenarchivierung.

Eingangsrechnungen mit Aufklebern nachträglich scannen: Wenn Sie dieses Feld aktivieren, müssen Sie Ihre Eingangsrechnungen mit Aufklebern mit einer eindeutigen RV-Nummer versehen und können nachträglich eingescannt werden. Eine nähere Beschreibung finden Sie im Handbuch unter ELO Dokumentenarchivierung.

Scannerbetrachter: Diese Einstellung gilt nur für Kunden, die Ihre Eingangsrechnung ohne Elo einscannen möchten.

Wenn Sie Eingangsrechnungen im Original hinterlegen möchten, so müssen Sie diese einscannen. Bei der Eintragung der Eingangsrechnung nennt Ihnen das Programm einen Dateinamen, unter dem ggf. die Rechnung eingescannt werden kann. Wenn die Datei in dem entsprechenden Scanner-Verzeichnis (Menüpunkt <Grundeinstellung> <Pfade> Pfad12 (Scannerdatei Rg-Eingang)) abgelegt wird, so kann sie über das Rechnungseingangsbuch und die Projektverwaltung betrachtet werden. In dieser Maske wird das Programm eingetragen, mit dem die Betrachtung erfolgen kann. Hier bieten sich mehrere Programme an. Es kann jedes beliebige Programm eingesetzt werden, mit dem die gescannten Bilder zu betrachten sind. Wenn Sie keines finden – der Internet-Explorer ist auf jeder Maschine

Gehen Sie ggf. über den Durchsuchen-Knopf, um die entsprechende Datei herauszusuchen.

[Bild]

Bild: Scanner-Betrachter

Ausgangsrechnungen - Optionen

[Bild]

Ungültig-Methode zulassen: Wenn dieser Haken gesetzt ist, können Rechnungen als ungültig erklärt und eine Kopie mit gleicher Nummer erneut ausgedruckt werden. Sobald eine Rechnung an einen Finanzbuchhaltung übergeben wurde, ist dies aber nicht mehr möglich.

Hintergrund dieses Schalters: Einige große Firmen wollen diese Variante der Rechnungskorrektur nicht zulassen, sondern wollen immer mit Storno und Gutschriften arbeiten.

Prüfen von Ausgangsrechnungen aktiv: Mit Setzen dieses Hakens werden 3 neue Dokumentenstatus eingeführt, die nur bei Rechnungen aktiv sind. Dies sind die Status 'zu prüfen', 'fehlerhaft' und 'geprüft'

Wenn der Schalter gesetzt ist, wird bei Rechnungen beim Verlassen der Artikelerfassung gefragt, ob diese geprüft werden sollen. Bei ja bekommen sie den Status 'zu prüfen'.

In der Projektverwaltung kann dann über die Menüpunkte <Extern>, <Ausgangsrechnungen prüfen> die Prüfung vorgenommen werden.

Bitte beachten Sie auch das Recht zum Umsetzen des Dokumenten-Status.

Erfass-Vorgabe

Legen Sie hier fest, wer die Rechnung als erstes prüfen soll. Bei der Einstellung 'Projektverantwortlicher' wird als Vorgabe jeweils der Verantwortliche vorgeschlagen. Der Rechnungsersteller, der die Rechnung zur Prüfung freigibt, kann aber dennoch einen anderen Mitarbeiter wählen.

2. Prüfer (Vorgabe)

Legen Sie hier fest, wer die Rechnung als zweites prüfen soll. Wenn ein Prüfer ausreicht oder es keinen festen zweiten Prüfer gibt, wählen Sie "Keinen 2. Prüfer". Der Rechnungsersteller, der die Rechnung zur Prüfung freigibt, kann dann ggf. individuell einen Mitarbeiter als 2. Prüfer bestimmen.

Priorität (2. Prüfer erst nach 1.Prüfung aktivieren)

Wenn mit 2 Prüfern gearbeitet wird, kann man hier festlegen, dass der zweite Prüfer die Rechnung erst dann in seiner Liste sieht, wenn der erste Prüfer sie freigegeben hat. Der zweite Prüfer ist also dann erst nachrangig involviert.

Wenn dieser Haken nicht gesetzt ist, müssen dennoch beide Prüfer die Rechnung freigeben.
