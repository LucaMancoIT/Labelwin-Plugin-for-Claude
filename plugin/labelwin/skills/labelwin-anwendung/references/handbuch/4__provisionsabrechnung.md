# 4. Provisionsabrechnung

Pfad: Sondermodule > Provisionsabrechnung [Modul] > 4. Provisionsabrechnung
Quelle: handbuch/4__provisionsabrechnung.htm

|

4. Provisionsabrechnung

Über den Schalter vermittlerprov=2 (siehe erste Seite) kann bei den Vermittlerprovisionen erreicht werden, dass nach Drucken der Rechnung sofort die Gutschrift erstellt wird. Alle anderen beschriebenen Funktionen bleiben gleich. In diesem Fall wird sinngemäß die Vermittlerprovision nur für den einen Auftrag abgerechnet.

Um die eigentlichen Abrechnungen vorzunehmen, müssen Sie das Programm ‚select.exe’ starten. Am besten legen Sie sich dazu eine Verknüpfung auf die Oberfläche. Die Abrechnungen finden Sie in diesem Modul unter dem Menüpunkte ‚Provision’. Wählen Sie dort an, ob Sie eine Vermittlerabrechnung oder eine Monteurabrechnung durchführen wollen. Die eigentlichen Programmschritte sind weitgehend identisch.

In der Liste der zu verprovisionierenden Rechnungen für die Vermittler erscheinen nur jene, die berechnet oder mit Skontoabzug bezahlt worden sind (Status b oder s).

Bei der Monteurabrechnung erscheinen alle Rechnungen – unabhängig vom Zahlungseingang.

Sie können einzelne Rechnungen markieren – in der Regel werden Sie aber sicherlich den Knopf ‚Alle markieren’ benutzen, um alle gleichzeitig abzurechnen.

Bei der Ausgabe gibt es die Option, die Rechnung detailliert auszudrucken. In der Praxis wird dies sicherlich nicht angewendet werden, aber damit kann man die Provisionsabrechnung sehr schön nachvollziehen und prüfen. Bei der Prüfung sollten Sie die Druckausgabe ‚auf Bildschirm’ wählen, da dann die Provision im Rechnungsausgangsbuch nicht auf ‚berechnet’ gesetzt wird. Es ist allerdings nicht zu verhindern, dass auch bei diesem Test die Dokumente angelegt werden, da sonst der Ausdruck nicht möglich wäre. Wenn es Sie stört, müssen Sie diese manuell über die Projektverwaltung oder die Adresse heraussuchen und löschen.

Bei Betätigen des Abrechnen-Knopfs gelangen Sie in eine Maske, in der Sie den Drucker, die Zahlungsbedingungen und Ähnliches festlegen können. Die Einstellungen in dieser Maske ‚merkt’ sich das Programm und schlägt sie beim nächsten Mal wieder vor.

Zu den Vermittlerprovisionen werden automatisch Gutschriften erzeugt, im Rechnungsausgangs-buch eingetragen und automatisch auf dem gewählten Drucker ausgegeben. Bei den Monteurprovisionen dagegen werden sogenannte ‚freie Texte’ erzeugt, die gegebenenfalls automatisiert ausgegeben werden, jedoch nicht im Rechnungsausgangsbuch stehen.

Wenn viele Dokumente automatisch gedruckt werden, ist es sinnvoll die Druckausgabe zu einem sogenannten PDF-Drucker vorzunehmen mit anschließender Speicherung der Datei. Damit kann ein Papierstau keinen Schaden anrichten, da man aus der PDF-Datei ggf. auch einzelne Bereiche drucken kann.

4.1 Verteilungsarten bei der Monteurabrechnung

Wie am Anfang beschrieben, kann die Aufteilung der Provision auf die am Auftrag beteiligten Monteure auf 3 verschiedene Arten erfolgen. Gesteuert wird dies mit dem Schalter ‚Verteilart’.

1) Verteilart 1

Bei der Verteilart 1 erfolgt die Aufteilung auf Grund der gebuchten Zeiten.

Beispiel:

Monteur Anton hat 5 Stunden gearbeitet, Willy 10 Stunden Zusammen also 15 Stunden. Wenn ein Artikel nun einen Verkaufspreis von 300 € hat, so bekommt Anton seine Prämie auf den Betrag von 300 € / 15 * 5, also auf einen Betrag von 100 €.

Willy dagegen bekommt die Prämie auf 200 €

Allerdings kann man das Aufteilungsverhältnis noch durch Bewertungsfaktoren der Monteure beeinflussen. Diese Bewertungsfaktoren wurden zuvor bei der Personalerfassung schon erwähnt. Für unser Beispiel setzen wir Anton als fleißig und effektiv an und tragen einen Bewertungsfaktor von 120% ein, Willy lassen wir auf 100% stehen.

Nun wird gerechnet

Bei Anton 5 Stunden mit 120%, also 6 Stunden.

Bei Willy bleibt es mit 10 Stunden zu 100%, also bei 10 Stunden.

Anton bekommt nun eine Prämie auf 300 € / 16 * 6 , also auf 112,50 €

Willy auf 300 € /16 * 10 , also 187,50 €.

2) Verteilart 2

Bei der Verteilart 2 erfolgt die Aufteilung auf Grund der beim Auftrag hinterlegten Monteure. Wenn bei ‚Weitere Monteure’ insgesamt 3 eingetragen sind, wird die Prämie auf Grund der Artikelpreise geteilt durch 3 ermittelt.

Mit den Bewertungsfaktoren gilt das Gleiche wie bei den Zeiten.

Für unser Beispiel setzen wir Anton wieder als fleißig und effektiv an und tragen einen Bewertungsfaktor von 120% ein, Willy lassen wir auf 100% stehen.

Nun wird gerechnet

Anton 300 € /220 Anteile * 120 Anteile = 163,64 €

Willy 300 € / 220 Anteile *100 Anteile = 136,36 €

3) Verteilart 3

Hier schaut das Programm in das Rechnungsdokument nach mindestens einer Geheimposition mit einem Kurztext ‚Prov_’ am Anfang. Wenn kein solcher Artikel vorhanden ist, kommt automatisch die Verteilart 2 zum Einsatz.

Die Steuerung der Provision erfolgt hier durch bestimmte Positionen in der Rechnung.

Es handelt sich um Artikel der Art ‚Geheimpos’, bei denen der Kurztext mit z.B. ‚Prov_75’ anfängt. Dabei ist die 75 die Personalnummer des Monteurs, der die Provision bekommen soll. Hinter dem Text Prov_75 kann ein beliebiger Text stehen. Es empfiehlt sich dort den Namen des Monteurs einzutragen. Die nachfolgenden Artikel werden für die Provisionsabrechnung verwendet, solange bis eine neue Geheimpos kommt.

[Bild]

Bei der abgebildeten Rechnung wird die Provision der Artikel 1,2,3 komplett der Personalnummer 777, die Positionen 4 bis 6 den Personalnummern 705 und 777 je zur Hälfte, die Positionen 7 bis 9 komplett der Nummer 705 zugerechnet.

Bei den Positionen 4 bis 6 wird aber ggf. nicht exakt geteilt, sondern es greift auch hier wieder der Bewertungsfaktor.

4.2 Monteurabrechnung mit vermindertem Betrag

1) Minderung auf Grund Rechnungsstellung statt bar zu kassieren

[Bild]

Es gibt eine Möglichkeit, bei der Monteurabrechnung einen prozentual verminderten Betrag zu ermitteln, wenn der Auftrag nicht in bar abgewickelt wurde. Es handelt sich quasi um einen Einbehalt, um mögliche Forderungsausfälle auch bei der Provisionsabrechnung zu berücksichtigen.

Einrichtung:

Im Einstellmodul die Nachkalkulation aktivieren.

Dort mindestens 2 Gruppen Barverkauf und Rechnung eintragen. Das Programm reagiert auf den Eintrag ‚Rechnung’.

Wenn im Kundendienst auf der Erledigtmaske die Nachkalkulation ‚Rechnung’ angewählt wird, so

wird bei der Monteurprovision für diesen Auftrag eine um x % niedrigere Summe ermittelt.

[Bild]

Die Zahl x wird in der Datei Global.ini eingetragen. Der Prozentsatz wird hinter dem Gleichzeichen eingetragen. Im Beispiel unten sind es 5,5%.

Global.ini, Gruppe [GRUNDEINSTELLUNGEN1], proveinbehalt=5,5

2) Minderung auf Grund abgerechneter Vermittlungsprovision

Wenn bei einem Auftrag eine Vermittlungsprovision gezahlt wird, soll die Ausschüttung an die Monteure ggf. auch entsprechend reduziert werden.

Dazu muss ein Schalter in der Datei Global.ini, unter der Gruppe [GRUNDEINSTELLUNGEN1] mit AbzugVermittlerProv =1

gesetzt werden.

In diesem Fall rechnet das Programm aus, um wie viel Prozent die Rechnungssumme auf Grund der Vermittlerprovision gesunken ist und mindert mit diesem Prozentsatz die Prämie der Monteure.

Diese Minderung wirkt mit einer Minderung auf Grund der Zahlart nicht multiplikativ, sondern additiv.

Beispiel:

Rechnung über 1000 €

Vermittlerprovision 90 € (z.B. 10%, die jedoch ggf. nicht auf alle Artikel wirkt)

Provisionseinbehalt 5% weil keine Barabrechnung, ergibt 50 € bei Bezug auf Rechnungssumme

Gerechnet wird 1000 €– 90 € – 50 € ergibt 860 €

Damit werden die Monteurprämien um 14% gemindert.
