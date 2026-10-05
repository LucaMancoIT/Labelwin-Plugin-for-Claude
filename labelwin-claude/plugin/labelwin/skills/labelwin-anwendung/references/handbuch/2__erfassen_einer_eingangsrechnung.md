# 2. Erfassen einer Eingangsrechnung

Pfad: Buchhaltung > Rechnungseingangsbuch [9] > 2. Erfassen einer Eingangsrechnung
Quelle: handbuch/2__erfassen_einer_eingangsrechnung.htm

|

2. Erfassen einer Eingangsrechnung

Zahlungsziel und Bankdaten: Eingangsrechnungen können nur auf angelegte Adressen erfasst werden. Dabei ist es in der Regel sinnvoll, den Adressen von vornherein die Zahlungsziele und Bankverbindungen einzutragen. Dies geschieht in dem Adressprogramm auf der Karteiseite ‚Bankdaten’. Aufgrund der bei der Adresse hinterlegten Zahlungsziele ermittelt das Programm die konkreten Zahlungstermine und Skontobeträge. Die Vorschlagswerte können von Ihnen ggf. abgeändert werden. In der Regel wird der aus der Adresse übernommene Wert zutreffen.

Anmerkung zum Steuersatz: Das Programm verteilt die eingebuchte RG-Summe automatisch auf Felder, in denen der Nettobetrag und der MwSt-Betrag eingetragen werden. Sollten Sie einmal eine Rechnung haben, die nicht mit dem Standardmehrwertsteuersatz beaufschlagt wird, so müssen Sie in die entsprechenden Felder die Summen eintragen. Unser Programm lässt drei verschiedene Nettosummen zu:

· MwSt. normal

· MwSt. vermindert

· ohne MwSt.

|

Verteilung der Kosten: Wenn dies im Modul EINSTELLUNGEN unter <Programmbereiche> <Buchhaltung> <Grundeinstellung> <Eingangsrechnungen> <Grundeinstellungen> festgelegt ist, können die Rechnungen auf verschiedene Projekte verteilt werden.

Buchungen sind auch auf bestimmte Kundendienstaufträge möglich. Dazu muss die Vergabe ebenfalls an gleicher Stelle im Modul EINSTELLUNGEN freigegeben werden.

Falls die Daten an die Fibu übergeben werden sollen, müssen die Warenkonten unbedingt identisch mit der Fibu festgelegt werden.

|

[Bild]

Kostenstellen: Das Programm lässt die Buchung auf bestimmte Kostenstellen zu. Dazu ist es erforderlich, die möglichen Kostenstellen in dem Einstellungsprogramm zu erfassen.

|

Scannen: Wenn Sie einen Scanner benutzen, ist es möglich Eingangsrechnungen im Original zu hinterlegen. Die Rechnung kann dann bei jedem Projekt oder Auftrag eingesehen werden, dass Bestandteile dieser Rechnung enthält. Bei einer Verteilung auf verschiedene Projekte geht die gleiche Eingangsrechnung also unter allen Projekten bzw. Aufträgen einsehbar.

Damit das funktioniert, muss entweder das Modul Scan-Archiv oder die ELO Anbindung vorhanden sein. Auch ohne diese Module ist eine Hinterlegung von Scans möglich, allerdings ist das mit mehr Aufwand verbunden. Jeder Scan muss von Hand den von Label vorgegebene Dateinamen erhalten und im Lablewin-Scan Ordner abgelegt werden. Beim Eintragen einer Eingangsrechnung vergibt das Programm automatisch einen Dateinamen, unter dem die Rechnung anschließend einzuscannen ist. Außerdem muss im Modul EINSTELLUNGEN unter dem Menüpunkt <Programmbereiche> <Buchhaltung> <Grundeinstellung> <Eingangsrechnungen> <Scannen> die Extension der Scannerdateien und der Name des Betrachtungsprogramms hinterlegt werden.

|

[Bild]

Rechnungsimport: Beachten Sie bitte die Tipps im Kapitel Import von Eingangsrechnungen zur Beschleunigung der Datenerfassung

|

[Bild]

|

Sie erreichen die Erfassmaske im Modul RECHNUNGSEINGANGSBUCH durch Betätigen des Knopfes ‚Rechnung erfassen’.

[Bild: 2. Erfassen einer Eingangsrechnung]

Bild: Rechnung erfassen

Hinweis: Öffnet man eine bereits erfasste Rechnung, sieht die Maske fast identisch aus. Es gibt wenige Unterschiede, die am Ende dieser Seite aufgeführt werden.

|
[Bild: 1]

Lieferant

[Bild: 1. Lieferant]

An dieser Stelle wird (wie bei allen anderen Adressaufrufen auch) der Adresskurzname eingegeben. Durch Drücken des Knopfes "Briefumschlag" kann auch das Adressprogramm gestartet werden, um ggf. eine neue Adresse zu erfassen.

|
[Bild: 2]

Kreditoren Nr.

[Bild: 2. Kreditoren Nr.]

Nach Aufruf der Adresse wird hier die in der Adresse hinterlegte Kreditorennummer angezeigt.

|
[Bild: 3]

Lieferant Name

[Bild: 3. Lieferant Name]

Hier wird der Kurzname der eingegebenen Lieferanten-Adresse gezeigt sowie der Name2 aus der Adresse, sofern dort etwas eingegeben wurde.

|
[Bild: 4]

Rg-Nummer

[Bild: 4. Rg-Nummer]

An dieser Stelle können Sie die Rechnungs-Nr. Ihres Lieferanten eingeben. Als Nr. sind sowohl Zahlen als auch Buchstaben zulässig. Die max. mögliche Rechnungs-Nr. enthält 20 Stellen. Zur Absicherung von doppelter Erfassung kann keine Nummer des gleichen Lieferanten doppelt eingegeben werden. Falls hier bei Ihnen ein Problem auftritt, weil jemand jedes Jahr mit der gleichen Nummer beginnt, schreiben Sie einfach das Jahr davor.

Da diese Nummer ggf. per Schnittstelle an eine Fibu übergeben wird, kann es zu Problemen mit der Länge der Nummer kommen. Die Datev lässt z.B. nur zwölfstellige Nummern zu. Hier schneidet die Schnittstelle einfach die ersten Stellen weg. In den Schnittstellen ist es auch möglich, die von Labelwin vergebene ‚Interne Nummer’ zu übergeben (Feld 9).

|
[Bild: 5]

hochzählen

[Bild: 5. hochzählen]

Setzen Sie hier bitte ein Häkchen, wenn Sie von Ihrem Lieferanten viele Rechnungen mit fortlaufender Rechnungsnummer erhalten. Sie brauchen dann nur einmal die Rechnungsnummer einzugeben. Beim Erfassen der nächsten Eingangsrechnung des Lieferanten erscheint automatisch die nächste Rechnungsnummer.

|
[Bild: 6]

Belegnummer

[Bild: 6. Belegnummer]

Sie dient zur Nummerierung der Eingangsrechnungen mit einer eigenen Nummer. In der Regel wird sie vom Programm vergeben und automatisch hoch gezählt. Auf Wunsch kann die Nummer auch selbst vergeben werden. Dazu muss im Modul EINSTELLUNGEN ein Schalter gesetzt werden Er findet sich unter <Programmbereiche> <Buchhaltung> <Grundeinstellung> <Eingangsrechnungen> bei ‚Interne Belegnummer veränderbar’.

Auch hier schlägt das Programm automatisch den nächsten Zähler vor. Wenn der hier erfasste Zähler höher als der automatisch vorgeschlagene ist, wird er für die nächste Buchung mit der entsprechend höheren Zahl abgespeichert.

Es empfiehlt sich, diese Nummer auf die jeweilige Rechnung zu schreiben und die Rechnungen in der Reihenfolge dieser Nummer abzuheften. Die Suche nach einer Rechnung kann dann über den Rechner erfolgen und über die ‚Belegnummer’ kann der Beleg schnell heraus gesucht werden.

|
[Bild: 7]

Interne Nr.

[Bild: 7. Interne Nr.]

Hier wird die interne lfd. Nr. des angelegten Datensatzes in der Datenbank angezeigt. Wir haben das Feld an die Oberfläche gelegt, weil einige Kunden, die mit dem Modul ELO arbeiten, ihre Elo-Nr. darauf abstimmen. Dazu ist es erforderlich; dass im Modul EINSTELLUNGEN <Programmbereiche> <Buchhaltung> <Grundeinstellung> <Eingangsrechnungen> das Feld ‚ELO Scan RV Nummer = interne Belegnummer’ aktiviert wird.

|
[Bild: 8]

Rg.-Datum

[Bild: 8. Rg.-Datum]

Das Rechnungsdatum wird in der Form TTMMJJ eingegeben. Das bedeutet beispielsweise für das Datum 28.09.2018 die Eingabe 280918. Die Trennpunkte für das Datum werden vom Programm automatisch eingesetzt.

|
[Bild: 9]

Valuta

[Bild: 9. Valuta]

Das Valutadatum wird vom Programm automatisch mit der Rechnungsdatum gesetzt und kann ggf. geändert werden. Ein Valutadatum ist das Datum, an dem die Rechnung wirksam wird. Auf diese Art können Rechnungen vorab gestellt werden, die in die Bilanz noch nicht eingehen. Die Zahlungsziele werden ausgehend vom Valutadatum ermittelt.

|
[Bild: 10]

Rg.-Summe

[Bild: 10. Rg.-Summe]

Als Rechnungssumme geben Sie bitte die gesamte Bruttosumme der Rechnung ein. Selbst wenn die Rechnung skontiert werden soll, sollten Sie hier die komplette Rechnungssumme einsetzen.

|
[Bild: 11]

Betrag ist netto

[Bild: 11. Betrag ist netto]

Um die Erfassung von Rechnungen ohne Mehrwertsteueranteil zu erleichtern, finden Sie neben der Rechnungssumme ein Ankreuzfeld ‚Betrag ist Netto'. Dieses Feld wird auf Grund der in der Adresse hinterlegten Information passend vorgeschlagen.

|
[Bild: 12]

Status

[Bild: 12. Status]

Jede Rechnung, die in das System eingetragen wird, bekommt zwangsläufig einen Status. Durch Drücken auf den Pfeil erhalten Sie eine Liste der möglichen Stadien. Nachdem Sie die Erfassung einer Rechnung gespeichert haben, können Sie den Status nur noch über den Zahlungsplan ändern.

Die Möglichkeiten im Einzelnen:

-

Offen: Dies wird der Normalfall sein. Die Rechnung wird eingetragen und ist noch nicht bezahlt.

-

Bezahlt:Die Rechnung ist bereits erledigt und nur für die Übersichten (ggf. nur für den Steuerberater) erfasst worden. Rechnungen mit diesem Status werden bei Zahlungsläufen nicht berücksichtigt.

-

Teilzahlung: Wenn Sie von der Rechnung nur einen Teilbetrag bezahlt haben, so bekommt sie diesen Status. Teilzahlung bedeutet, dass noch ein Restbetrag gezahlt werden muss.

-

Skontozahlung:Die Rechnung ist bereits mit Skontoabzug bezahlt worden.

-

Storniert: Statt eine falsche Eingangsrechnung zu löschen, kann diese auch storniert werden. Die Entscheidung ist immer dann richtig, wenn alle Vorgänge mit dem Lieferanten nachvollziehbar sein sollen.

-

Gesperrt: Bedeutet, dass die Rechnung zwar offen ist, jedoch noch nicht bezahlt werden soll. Dies kann z.B. dafür genutzt werden, um Rechnungen zu erfassen, bei denen bei der Lieferung wichtige Teile gefehlt haben. Hierdurch können Sie erreichen, dass die Rechnung zwar in der OP-Liste berücksichtigt, jedoch noch nicht beglichen wird. Bei der Durchführung von Zahlungen können diese gesperrten Rechnungen ‚nebenher’ freigegeben werden.

Bankeinzug: Wenn Rechnungen nicht mit einem Zahlungslauf überwiesen werden sollen, muss man diese auf den Status "Bankeinzug" setzen. Diesen Status sollten Sie auch dann vergeben, wenn die Rechnung sofort per Scheck bezahlt wurde, ohne dieses über einen Zahlungslauf abzuwickeln (beim Postboten per Scheck).

-

Im Zahlungslauf: Das bedeutet, dass die Rechnung bereits per Überweisung, Scheck oder Bankdiskette angewiesen ist, aber noch nicht auf ‚Bezahlt’ gesetzt worden ist. Dieser Zwischenstatus ist erforderlich, damit die Zahlung ggf. noch einmal wiederholt werden kann.

-

Offen/gesperrt: Dieser Status wird nur für den Zahlungsplan verwendet. Wenn Sie hier einen Teilbetrag mit dem Status offen eingeben und den anderen Teilbetrag sperren, weil z.B. die Lieferung noch nicht erfolgt ist, bekommt die Rechnung den Status offen/gesperrt.

-

Teilz./gesperrt: Dieser Status wird nur für den Zahlungsplan verwendet. Wenn hier ein Teilbetrag bereits bezahlt wurde und der anderen Teilbetrag noch offen aber gesperrt ist, weil z.B. die Lieferung noch nicht erfolgt ist, bekommt die Rechnung den Status Teilz./gesperrt.

|
[Bild: 13]

Skontokonto

[Bild: 13. Skontokonto]

Dieses Konto dient dazu, gewährte Lieferantenskonti zu verbuchen. Je nachdem, ob die Rechnung mit oder ohne Mehrwertsteuer ist, wird das Konto für Skontobuchungen mit oder ohne Mehrwertsteuer vorgeschlagen. Wichtig ist das Skonto-Konto nur für diejenigen, die ihre Eingangsrechnungen per Zahlungslauf bezahlen und diesen in dem Programm-Modul FIBUERFASSUNG buchen.

|
[Bild: 14]

Buchungshinweis

[Bild: 14. Buchungshinweis]

In dieser Zeile können Sie eigene Informationen hinterlegen, die Ihnen zu dieser Rechnung wichtig erscheinen. Der Buchungsvermerk kann sowohl bei der Erfassung als auch bei der Zahlung erfasst/geändert werden. Der Buchungsvermerk findet keine Berücksichtigung, außer dass er bei entsprechenden Listen mit ausgedruckt werden kann. Er dient also lediglich Ihrer eigenen Information.

|
[Bild: 15]

Zahlungsziele

[Bild: 15. Zahlungsziele]

In diesen Datenfeldern schlägt das Programm die Zahlungssummen und Ziele vor. Die Werte werden aufgrund der in der Adresse hinterlegten Daten (Karteiseite ‚Bankdaten‘ oder über speziell im Projekt hinterlegte Werte (Datenblatt, Knopf Zahlungsbedingungen) ermittelt. Wenn Sie abweichende Zahlungsziele erfassen wollen, so können Sie diese hier eintragen.

|

Besondere Zahlungsbedingungen:

[Bild]

Um auch mit Zahlungszielen wie „immer am 15. des Folgemonats“ arbeiten zu können, hat Label zu einem kleinen Trick gegriffen. Hierbei müssen die Eingaben bei der entsprechenden Lieferantenadresse erfolgen.

Da davon auszugehen ist, dass keine Zahlungsziele von über 700 Tage vorkommen, wird mit Zahlen ab 700 die Zahlungsweise an bestimmten Tagen geregelt. Wenn die Zahl der Tage über 700 liegt, ist der aktuelle Monat, bei über 800 der Folgemonat und bei über 900 der übernächste Monat festgelegt. Die nächste Zahl dient der Festlegung des Tages.

Beispiele: 701 bedeutet den 1. Tag des aktuellen Monats

815 den 15. des Folgemonats

912 den 12. des übernächsten Monats

Sollte bei einem Wert mit dem aktuellen Monat der Tag bereits vorüber sein, wird automatisch auf den nächsten Monat umgeschaltet.

Beispiel: Am 16.01.2013 eine Rechnung für einen Lieferanten mit Zahlungsziel 714 zu erfassen, bewirkt die Vorgabe des 14.02.2013 als Zahlungsziel. Wenn bei einer Eingabe von 731 oder 831 oder 931 der entsprechende Monat keinen 31. Tag hat, wird automatisch auf das zuvor gültige Datum zurückgestellt.

[Bild]

Wenn Sie mit Ihrem Großhändler für ein bestimmtes Projekt eine gesonderte Zahlungsbedingung ausgehandelt haben und dieses im Projekt hinterlegt wurde (lesen Sie hierzu das Kapitel 2.4), dann haben diese Zahlungsbedingungen für dieses Projekt Vorrang vor der Zahlungsbedingung, die in der Adresse des Lieferanten hinterlegt ist.

Nach dem Speichern, ist dieses Feld nicht mehr sichtbar und es wird die Tabelle des Zahlungsplans angezeigt (Nr. 21).

|
[Bild: 16]

MwSt. Verteilung

[Bild: 16. MwSt. Verteilung]

In diesen Feldern stehen die Nettosummen und dazugehörigen MwSt-Beträge. Standardmäßig geht das Programm davon aus, dass die komplette Summe mit 19% belastet ist. Wenn jedoch Beträge mit dem verminderten Steuersatz oder ohne Steuer dabei sind, müssen Sie nur die Summe im Nettofeld mit 19% ändern. Das Programm schiebt damit die passende Summe automatisch auf die verminderte Nettosumme. Wenn Sie auch hier eine Änderung vornehmen, wird der Rest automatisch auf die Nettosumme ohne MwSt geschoben.

Der Prozentsatz ist an dieser Stelle nicht änderbar, sondern wird über das Modul EINSTELLUNGEN unter dem Menüpunkt <Grundeinstellungen> <MwSt.-Sätze> festgelegt.

Wenn im Modul EINSTELLUNGEN die entsprechende Eintragung vorgenommen worden ist, können Eingangsrechnungen auf verschiedene Warenkonten und Kostenstellen verteilt werden.

Verteilung auf Positionen: Wenn diese Eingabe frei geschaltet ist, können bei vorhandener Projektbasis (siehe Beschreibung Dokumentenarten) die Kosten auf eine einzelne Position oder auch einen Titel gebucht werden. Unter Anzahl können Sie die Stückzahl eintragen, die für diese Position eingekauft wurde.

|
[Bild: 17]

Lieferschein

[Bild: 17. Lieferschein]

Wenn Sie das Modul BESTELLÜBERWACHUNG oder LAGERVERWALTUNG erworben haben, so werden bei der Einbuchung der Bestellartikel Eingangslieferscheine erzeugt. Auf diese kann dann bei der Erfassung der Eingangsrechnungen zurückgegriffen werden. Lesen Sie dazu die Beschreibung im Kapitel Verteilung mit Hilfe von Lieferscheinen oder Bestellungen.

|
[Bild: 18]

KD-Auftrag

[Bild: 18. KD-Auftrag]

Falls die Zuordnung auf einen Kundendienstauftrag erfolgen soll, so ist dieser mit seiner Nummer oder über den Knopf Aufträge einzutragen. Bei einer reinen Projektzuordnung kann dieses Feld einfach leer bleiben.

|
[Bild: 19]

Status KD-Auftrag

[Bild: 19. Status KD-Auftrag]

Hier wird der Status des in Feld [Nr.18] eingetragenen KD-Auftrages angezeigt.

|
[Bild: 20]

Details KD-Auftrag

[Bild: 20. Details KD-Auftrag]

Wenn Sie für die Verteilung einen KD-Auftrag angewählt haben, erscheinen in diesem Feld Informationen zu dem KD-Auftrag wie Auftrags-Nr., Auftragsdatum und Objektadresse.

|
[Bild: 21]

Bearbeiten KD-Auftrag

[Bild: 21. Bearbeiten KD-Auftrag]

Über diesen Knopf gelangen Sie in den KD-Auftrag, den Sie im Feld [Nr.18] eingetragen haben und können ihn in Bearbeitung nehmen.

|
[Bild: 22]

Projekt

[Bild: 22. Projekt]

Hier müssen Sie die Projekt-Nr. eingeben. Die Projekt-Nr. kann aus der Projektliste heraus ausgewählt werden, indem Sie den Knopf Projektauswahl betätigen.

Die Projektzuordnung ist nur auf ein eingerichtetes Projekt möglich. Das bedeutet, dass Sie auch solche Sammelprojekte wie Lager und ähnliches einrichten müssen, damit wirklich alle Summen auf irgendeinem Projekt verbucht werden können. Es ist nicht möglich, Teilbeträge keinem Projekt zuzuordnen.

|
[Bild: 23]

Objekt

[Bild: 23. Objekt]

Die Objektadresse wird aus dem KD-Auftrag oder dem Projektdatenblatt übernommen. Hier geht es nur darum, dass Sie unter der Objektadresse alle Eingangsbuchungen sehen können.

|
[Bild: 24]

Hersteller

[Bild: 24. Hersteller]

Bei der Herstelleradresse geht es in erste Linie um Einkaufsgenossenschaften wie z.B. der SHK die die Zahlungsabwicklung für ihre Mitglieder vornimmt. Die Rechnungen kommen IMMER von der SHK, auch wenn die Artikel direkt beim Hersteller bestellt wurden. Durch die Zuordnungsmöglichkeit einer Herstelladresse ist es möglich, den Umsatz mit diesem Hersteller festzustellen. Lesen Sie hierzu das Kapitel Zahlung an andere Adresse.

|
[Bild: 25]

Warenkonto

[Bild: 25. Warenkonto]

Die Wahl des Kontos ist nur dann erforderlich, wenn Sie die Daten an eine Finanzbuchhaltung übergeben möchten. Das Programm lässt nur Konten zu, die über das Programm EINSTELLUNGEN eingetragen sind.

Dieses dient dazu, bei der Übergabe an Fibu-Programme als Gegenkonto genutzt zu werden. Wenn Sie die Buchungen auf Projekte verteilen, so werden die Konten für jedes Projekt einzeln eingegeben.

Wenn Sie mit keinem Fibu-Programm arbeiten, so können Sie es vernachlässigen.

Die Warenkonten werden im Modul EINSTELLUNGEN unter dem Menüpunkt <Grundeinstellungen> <Buchhaltung> <Kontenplan> erfasst. Hier werden nur die Konten angeboten, die das Merkmal ‚Warenkonto‘ haben.

|
[Bild: 26]

Kostenstelle

[Bild: 26. Kostenstelle]

Das Eingabefeld ‚Kostenstelle’ ist nur dann vorhanden, wenn im Modul EINSTELLUNGEN das Arbeiten mit Kostenstellen aktiviert und Kostenstellen erfasst worden sind.

Dann wird Ihnen je nach Einstellung die Kostenstelle hier angezeigt. Sie haben die Möglichkeit, bei der Erfassung der Eingangsrechnung die entsprechende Kostenstelle zu wählen. Die Kostenstellen müssen im Modul EINSTELLUNGEN unter dem Menüpunkt <Grundeinstellungen> <Kostenstellen> eingetragen sein.

|
[Bild: 27]

Verteilung

[Bild: 27. Verteilung]

Material, Fremdleistung, Sonstige Kosten, Lohnbetrag, Lohnzeit: Bei den Nettosummen können Sie zwischen den Kostenarten Material, Fremd-leistungen, Sonstige Kosten und Lohnbetrag unterscheiden. In der Regel werden die Beträge sicherlich nur beim Material eingetragen. Bei der Nutzung der weiteren Kostenarten ist die Auswertung nur über Sonderformulare möglich.

Die gleichen Kostenarten können auch bei der Angebotserstellung bzw. Rechnungsstellung verwendet werden. Mit Hilfe der Kostenarten ist ein Soll/Ist-Vergleich wesentlich effizienter möglich.

Beim Lohnbetrag haben Sie die Möglichkeit eine Eingangsrechnung auf den Bereich Lohn zu buchen (z.B. wenn Sie für sich selbst kalkulierte Zeiten als Fremdleistung vergeben haben). Im Feld [Nr.31] "Lohn in Std." können Sie auch die Stunden erfassen.

|
[Bild: 28]

Lohn in Std.

[Bild: 28. Lohn in Std.]

Hier können Sie für den Stundenvergleich auch Stunden hinterlegen. Diese Stunden können bei entsprechender Formulargestaltung (=Ausdruck) in den Vergleich mit einfließen.

Leider entsteht hier ein Problem mit speziell angepassten Formularen. Wenn diese nicht nachträglich an das neue System angepasst werden, werden die Zeiten und Lohnkosten aus dem Rechnungseingang ggf. nicht berücksichtigt. Natürlich müssen Sie sich entscheiden, ob Sie die Leiharbeiter-Stunden über die Eingangsrechnungen ODER über die Zeiterfassung buchen, da ansonsten die Stunden und Kosten doppelt gerechnet werden. Dazu gibt es im Label-Wiki einen Text über die Vor- und Nachteile der Methoden (Stichwort Leiharbeiter).

|
[Bild: 29]

Bemerkung

[Bild: 29. Bemerkung]

In diesem Feld können Sie ein kurzes Stichwort zu der Eintragung vornehmen. Denkbar wäre z.B. die Art des Materials o.ä. einzugeben. Selbstverständlich können Sie das Bemerkungsfeld auch leer lassen.

|
[Bild: 30]

Werkzeug

[Bild: 30. Werkzeug]

Wenn Sie das Zusatzmodul Werkzeugverwaltung erworben haben, wird dieser Knopf sichtbar. Durch Betätigen des Knopfes erscheint eine Maske, in der Sie

eine bestimmte Werkzeug-Nr. eines Werkzeugs eintragen können, für das Sie z.B. ein Ersatzteil bestellt haben.

[Bild]

|
[Bild: 31]

TGM

[Bild: 31. TGM]

Dieser Knopf ist nur dann sichtbar, wenn Sie das Modul TGM erworben haben. Durch Betätigen dieses Knopfes wird ein weiteres Feld sichtbar, in der Sie die TGM Ebene eintragen können

|
[Bild: 32]

Rechnungsprüfung

[Bild: 32. Rechnungsprüfung]

Wenn Sie hier kein Häkchen setzen, bedeutet dieses, dass der Erfasser der Buchung die Rechnung bereits geprüft und als OK bezeichnet hat.

Für die Prüfung von Rechnungen können 2 Prüfer festgelegt werden – sinngemäß einer für die technische und einer für die kaufmännische Prüfung. Die Auswahlbox für den 2. Prüfer erscheint automatisch, wenn die Verwendung von Prüfern aktiviert ist. Wenn keine 2. Prüfer benötigt wird, lässt man die Auswahl einfach auf ‚nicht gewählt‘ stehen.

Wenn eine Rechnung bzw. eine Verteilbuchung 2 Prüfer hat, so erscheint sie bei beiden in der Prüfliste, egal ob der Name als 1. oder 2. Prüfer eingetragen ist. Freigegeben wird die Rechnung zur Zahlung erst, wenn beide Prüfer die Freigabe erteilt haben.

Es werden alle Mitarbeiten als Prüfer angeboten, die in den Personalstammdaten erfasst und mit dem Kennzeichen ‚Verwaltung’ versehen sind. Zum Prüfen einer Rechnung braucht der Prüfer nicht im Modul Rechnungseingangsbuch arbeiten. Die Prüfung kann auch im Modul Projekte unter dem Menüpunkt <Extern> <Rechnungsprüfung> und im Modul Selektieren unter <Projekt>, <Rechnungsprüfung> erfolgen. Die Anzahl der zu prüfenden Rechnungen kann auch im Startcenter gezeigt werden und von dort die Prüfung aktiviert werden.

|
[Bild: 33]

Verteilung Summe

[Bild: 33. Verteilung Summe]

Hier sehen Sie die Rg.-Summe und die Summe der bisher verteilten Kosten sowie den restlichen Anteil. Dieser Übersicht ermöglicht eine schnelle Kontrolle der Eingaben. Verstärkt wird dieser Kontrollmechanismus durch die Ampel [Nr.34], die den Status der Verteilung farblich anzeigt.

|
[Bild: 34]

Verteilung Status

[Bild: 34. Verteilung Status]

Die Ampel reagiert bei jeder Eingabe und zeigt Gelb, wenn nach Abschluss der Verteilbuchung alles erledigt ist und Rot, wenn weitere Verteilbuchungen erforderlich sind. Das ist z.B. sehr hilfreich, wenn ein falsches MwSt.-Konto gewählt wurde.

|
[Bild: 35]

Verteilung speichern

[Bild: 35. Verteilung speichern]

Mit dem Betätigen dieses Knopfes werden die Verteilungengespeichert. Sind alle Summen korrekt verteilt, wird der Punkt neben diesem Knopf grün. Wenn Sie nur eine Summe eintragen, können Sie gleich den Knopf ‚Speichern‘ [Nr.43] betätigen.

|
[Bild: 36]

Archiv Rechnung

[Bild: 36. Archiv Rechnung]

<TODO>: Hier Beschreibung einfügen...

|
[Bild: 37]

Rechnungsartikel

[Bild: 37. Rechnungsartikel]

<TODO>: Hier Beschreibung einfügen...

|
[Bild: 38]

Zahlungsplan

[Bild: 38. Zahlungsplan]

Um das Bezahlen von Eingangsrechnungen in Teilsummen zu ermöglichen, kann einer Eingangsrechnung ein Zahlungsplan hinterlegt werden. Dieses kann bei der Erfassung der Rechnung, durch späteres Ändern des Zahlungsplanes oder bei der Bezahlung, also beim Erstellen eines Zahlungslaufes geschehen.

|

Der Zahlungsplan muss nur bei Teilzahlungen oder Abzügen von der Rechnungssumme (Ausbuchung) angewählt werden. Wenn Sie die volle Summe bezahlen oder nur Skontoabzüge zum Tragen kommen, brauchen Sie die Maske ‚Zahlungsplan’ nicht zu öffnen.

Wenn Sie den Knopf ‚Zahlungsplan’‚ bei einer bereits gespeicherten Rechnung betätigen, so finden Sie im Zahlungsplan einen automatisch erzeugten Eintrag mit der vollen Summe. Diesen können Sie durch einen Doppelklick auf den Eintrag ändern.

Obwohl es beim Zahlungsplan natürlich in erster Linie darum geht, die Zahlung zu splitten, können hier auch Ausbuchungen / Abzüge erfasst werden. Zusätzlich kann ein Teilbetrag auf ‚gesperrt’ gesetzt werden, wenn der Lieferant seine Verpflichtungen noch nicht vollständig erfüllt hat oder ein Sicherungseinbehalt erfolgen soll.

Sobald Sie einen Eintrag mit einer Teilzahlung erfasst haben, müssen Sie der Restsumme ebenfalls ein Zahlungsziel geben. Sie können die Maske erst verlassen, wenn Sie die komplette Rechnungssumme im Zahlungsplan verteilt haben.

Als erstes muss zunächst der mit der ersten Zahlung berücksichtigte Teilbetrag eingegeben werden. Die Zahlungsziele werden aus der vorigen Maske übernommen, so dass Sie in der Regel gleich den Speichern-Knopf betätigen können. Wenn Sie mit der Restsumme oder ggf. mit beliebig vielen weiteren Einträgen genauso verfahren haben, können Sie die Maske mit dem Ok-Knopf verlassen.

Ausbuchung: Wenn Sie einen Teilbetrag ausbuchen wollen, so müssen Sie nach der Eintragung der Summe im Feld ‚Ausbuchungsumme’ das Fibu-Konto eingeben, von dem diese Summe abgehen soll. In die Finanzbuchhaltung gelangt dieser Eintrag aber nur, wenn Sie das Modul FIBUERFASSUNG nutzen. Ohne dieses Modul können keine Zahlungen und auch keine Ausbuchungen übergeben werden. In diesem Falle müssen Sie also die tatsächlich gezahlte Summe und die Ausbuchung zusätzlich in der Fibu erfassen.

Um die Maske verlassen zu können, muss die Summe aller Einträge ‚Teilbetrag Brutto’ und die Ausbuchungssumme genau der Gesamtrechnungssumme entsprechen.

Bei der Erfassung der zweiten und weiteren Teilsumme geht das Programm davon aus, dass keine weiteren Skonti gezogen werden sollen und blendet die weiteren Zahlungsziele aus. Wenn Sie das automatisch gesetzte Kreuz bei ‚Erfassung ohne Skonto’ herausnehmen, können Sie auch hier Skontoziele festlegen.

Änderung des Zahlungsplans

- beim Zahlungslauf:

Beim Bezahlen von Eingangsrechnungen können Sie einen Eintrag markieren und mit dem Menüpunkt <Bezahlen> <Zahlungsplan bearbeiten> die zu zahlende Summe ändern. Dieser Menüpunkt ist auch über das Popup-Menü mit der rechten Maustaste erreichbar.

- von der Gesamtliste aus:

Nach Markieren der Rechnung über den Menüpunkt <Bearbeiten> <Zahlungsplan> oder durch Betätigen der rechten Maustaste.

Zahlung eintragen:

Wenn Sie das Modul FIBUERFASSUNG nicht nutzen, können Sie eine Rechnung (oder eine Teilsumme) über den Zahlungsplan auf bezahlt setzen. Markieren Sie dann den Tabelleneintrag, schalten den Status auf ‚Bezahlt’. Erst dann erscheinen die Zahlungsfelder, in denen Sie das Datum und die Summen eintragen können.

|
[Bild: 39]

Anmerkung

[Bild: 39. Anmerkung]

Sie können zu jeder Eingangsrechnung eine beliebig lange Anmerkung hinterlegen, z.B. wegen Lieferverzögerungen, Sicherheitseinbehalten usw. Diese Anmerkung ist auch im Zahlungslauf verfügbar, so dass Sie hier ggf. noch einmal nachschauen können.

|
[Bild: 40]

Verteilung ändern

[Bild: 40. Verteilung ändern]

Durch Betätigen dieses Knopfes können Sie die Verteilbuchungen ändern.

|
[Bild: 41]

Eintrag löschen

[Bild: 41. Eintrag löschen]

Durch Betätigen dieses Knopfes können Sie einen markierten Eintrag in der Liste der Verteilbuchungen löschen.

|
[Bild: 42]

Editieren

[Bild: 42. Editieren]

Dieses Feld kann nur beim Import von Rechnungen (siehe Kapitel Rechnungsimport) verwendet werden. Wenn in der Verteilmaske mehrere Einträge sind (Sammelrechnung), wird nach Änderung des ersten Eintrags sofort der nächste Eintrag im Änderungsmodus aktiviert. Sonst müsste man erst einen Doppelklick auf den nächsten Eintrag machen.

|
[Bild: 43]

Speichern

[Bild: 43. Speichern]

Durch Betätigen des Speichern-Knopfes wird die Eintragung in das Rechnungseingangsbuch übernommen. Die Maske wird geleert um die nächste Eintragung vornehmen zu können.

|
[Bild: 44]

Ende

[Bild: 44. Ende]

Um die Datenerfassung zu beenden, müssen Sie den Ende-Knopf betätigen. Falls die letzte Eintragung noch nicht übernommen worden ist, geht dieser Wert verloren. Wenn Sie also Buchungen vornehmen, müssen Sie unbedingt vor Verlassen der Maske den Speichern-Knopf betätigt haben.

Anzeige erfasste Rechnung

Wenn Sie sich eine erfasste Rechnung öffnen, ändert sich die Maske im oberen Bereich ein wenig:

.

[Bild]

Bild: Erfassen / ändern

1 Angelegt: Hier wird der Erfasser und das Erfassdatum der Eingangsrechnung angezeigt. Es gilt nur zur Information.

2 Prüfungskennzeichen: Hier wird angezeigt, ob eine Rechnung geprüft wurde oder nicht. Voraussetzung hierfür ist, dass Sie im Modul EINSTELLUNGEN unter dem Menüpunkt <Programmbereiche> <Eingangsrechnungen> <Grundeinstellungen> die Rechnungsprüfung freigegeben haben.

3 Zahldatum, Zahlsumme, Fehlbetrag: Hier wird der Zahlungsstand der Rechnung angezeigt. Die Werte entstehen aus der Zahlung per Zahlungslauf, also der tatsächlichen Bezahlung.

4 Liste Verteilbuchungen: Hier werden die verteilten Summen angezeigt. Sie haben die Möglichkeit, die Summe auf mehrere Projekte oder Kundendienstaufträge zu verteilen.

5 Tabelle Zahlungsplan: Wenn Sie für Eingangsrechnungen Teilsummen buchen, werden hier die Teilsummen sichtbar. In der Tabelle kann nicht geschrieben werden – sie wird über den Knopf ‚Zahlungsplan’ (Nr. 17) gefüllt.

6 Neuer Eintrag: Durch Betätigen dieses Knopfes können Sie eine weitere Verteilbuchung hinzufügen.
