# 3.1 Fehlsummenbehandlung

Pfad: Buchhaltung > Rechnungsausgangsbuch [7] > 3. Zahlung erfassen > 3.1 Fehlsummenbehandlung
Quelle: handbuch/3_1_fehlsummenbehandlung.htm

|

3.1 Fehlsummenbehandlung

Ist die Zahlsumme nicht genau die Fehlsumme, erscheint der Block "Fehlsummenbehandlung". Hier müssen Sie entscheiden, wie die Fehlsumme berücksichtigt werden soll.

Entweder handelt es sich bei der Fehlsumme um Skonto, um einen Fehlbetrag - also ein Betrag, den Sie noch zur Zahlung erwarten, oder um eine Ausbuchung - also ein Betrag, den Sie nicht mehr einfordern, oder um eine Kombination aus diesen drei Varianten.

[Bild: 3.1 Fehlsummenbehandlung]

Bild: Ausgangsrechnung Zahlung erfassen mit Fehlsummenbehandlung

|
[Bild: 1]

Restsumme

[Bild: 1. Restsumme]

In diesem Anzeigefeld wird die nach der Buchung offenen Restsumme mit dem dazugehörigen Prozentsatz gezeigt.

|
[Bild: 2]

Fehlsummenbehandlung

[Bild: 2. Fehlsummenbehandlung]

Sie können festlegen, wie mit der offenen Restsumme verfahren werden soll.

Rest = Skonto: Wenn Sie dieses Feld markieren, wird die Restsumme als Skontobetrag ausgebucht. Bitte beachten Sie die Anzeige mit dem Prozentsatz des Skontoabzuges. Rechnungen die mit Abzug bezahlt worden sind, bekommen in der Anzeigeliste das Kennzeichen ‚s’.

Rest = Fehlbetrag: Durch diese Option können Sie erreichen, dass die fehlende Summe als Restbetrag stehen bleibt. Diese Fehlbeträge kommen ganz normal auch in den Mahnzyklus hin. In der Liste bekommen Sie das Kennzeichen ‘t’.

Rest = Ausbuchung: Über diese Möglichkeit können Sie erreichen, dass die Rechnung auf Erledigt gesetzt wird, obwohl sie nicht komplett beglichen wurde. Von der Wirkung her ist eine solche Ausbuchung ähnlich einem Skontoabzug. Da die Information jedoch in ein separates Feld geschrieben wird, ist der Verzicht auf einen Teilbetrag dokumentiert und kann auch später noch nachgesehen werden.

Verteilung eingeben: Durch dieses Feld können Sie erreichen, dass die eingezahlte Summe als Teilzahlung verbucht wird und dennoch Skonto abgezogen werden kann. Diese Option ist erforderlich, um auch bei Abschlags- und Teilrechungen die eingegangenen Summen skontieren zu können. Hiermit wollen wir folgendes Problem lösen: Abschlagsforderung über 10.000 € mit angebotenen Skontoabzug von 2 %. Der Kunde zahlt nur 7840 € (8.000 € abzüglich 2 % Skonto, weil seiner Meinung nach irgendwelche Teilleistungen noch nicht erbracht sind. Hier können Sie nun erfassen, dass bei der Endrechnung 8.000,00 € und nicht der tatsächliche Zahlungseingang berücksichtigt wird.

|
[Bild: 3]

Skonto in %

[Bild: 3. Skonto in %]

Dies Feld ist nur aktiv, wenn Teilbeträge mit Skontoabzug angewählt worden sind. Geben Sie hier den Prozentsatz ein, damit das Programm den Skontoabzug ausrechnen kann.

|
[Bild: 4]

Skontobetrag

[Bild: 4. Skontobetrag]

In diesem Feld trägt das Programm den Skontoabzug ein, wenn Sie in dem Feld Nr. 22 einen Prozentsatz eingetragen haben. Anderenfalls können Sie hier den Skontoabzug direkt eingeben.

|
[Bild: 5]

Skontokonto

[Bild: 5. Skontokonto]

Dieses Feld ist nur sichtbar, wenn im Modul EINSTELLUNGEN unter <Programmbereiche><Buchhaltung><Kontenplan> mindestens ein Konto mit dem Merkmal „Skonto“ eingetragen ist. Bei der Übergabe von Zahlungseingängen wird hier das zu benutzende Konto gewählt.

|
[Bild: 6]

Ausbuchung

[Bild: 6. Ausbuchung]

Bei Berücksichtigung von Teilbeträgen wird hier die rechnerische Ausbuchung eingetragen. So komisch es klingt: Überzahlungen aufgrund von gezahlten Gebühren oder Zinsen müssen ebenfalls hier eingetragen werden (mit negativem Vorzeichen).

|
[Bild: 7]

Ausbuchungskonto

[Bild: 7. Ausbuchungskonto]

Dieses Feld ist nur sichtbar, wenn im Modul EINSTELLUNGEN unter dem Menüpunkt <Programmbereiche><Buchhaltung><Kontenplan> mindestens ein Konto mit dem Merkmal „Ausbuchung“ eingetragen ist. Bei der Übergabe von Zahlungseingängen wird hier das zu benutzende Konto gewählt.

|
[Bild: 8]

Berück. Summe

[Bild: 8. Berück. Summe]

In diesem Feld ist die insgesamt berücksichtigte Summe sichtbar. Sie setzt sich zusammen aus Zahlsumme + Skontosumme + Ausbuchungssumme.

|
[Bild: 9]

Zahlungsziel

[Bild: 9. Zahlungsziel]

Tagen Sie hier das Zahlungsziel für die Restsumme z.B. Sicherheitseinbehalt ein.
