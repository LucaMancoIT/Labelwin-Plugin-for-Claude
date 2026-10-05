# 4. Rechnungen bezahlen

Pfad: Buchhaltung > Rechnungseingangsbuch [9] > 4. Rechnungen bezahlen
Quelle: handbuch/4__rechnungen_bezahlen.htm

|

4. Rechnungen bezahlen

Sie erreichen diese Maske durch Wahl des Moduls Rechnungseingang unter dem Menüpunkt [Zahlungen - Bezahlen offene Rechnungen].

Nach der Anwahl dieses Menüpunktes, erzeugt das Programm eine Liste der offenen Rechnungen. Dieser Vorgang kann bei großen Datenmengen einige Minuten dauern. Die Laufzeit wird durch einen roten Balken dargestellt. Aus dieser Liste der offenen Rechnungen können Sie über automatische Eingrenzungen oder durch Einzelauswahl die Rechnungen auswählen, die bezahlt werden sollen. Die gewählten Rechnungen werden zu einem Zahlungslauf zusammengefasst, dem das Programm automatisch eine laufende Nummer gibt. Über diese laufende Nummer können die gewählten Rechnungen später per Durchlauf auch auf bezahlt gesetzt werden. Bei der Zahlungsanweisung bleiben die Rechnungen auf offen stehen, um gegebenenfalls bei einem Druckerfehler oder einem Festplattenfehler den Vorgang wiederholen zu können.

Hinweis: Wenn das Programm mehrere Rechnungen für einen Lieferanten vorfindet, so fasst es diese zu einer Zahlung zusammen und es kann ein Begleitschreiben erstellt werden, mit dem Sie Ihrem Lieferanten die bezahlten Rechnungen mitteilen können.

[Bild: 4. Rechnungen bezahlen]

Bild: Eingangsrechnung bezahlen

|
[Bild: 1]

Zahlungsart

[Bild: 1. Zahlungsart]

Hier legen Sie fest, wie die gewählten Rechnungen bezahlt werden sollen. Sollten Sie einige Rechnungen per Scheck, andere per Überweisung und wieder andere per Datei bzw. Bankprogramm bezahlen wollen, so müssen Sie dies in getrennten Zahlungsläufen durchführen. Die Wahl an diesem Punkt gilt für alle ausgewählten Rechnungen.

|
[Bild: 2]

Bank

[Bild: 2. Bank]

Wählen Sie hier die Bank aus, mit der Sie bezahlen möchten. Achten Sie darauf, dass bei der Bank unter dem Menüpunkt <Optionen> <Eigene Bankdaten bearbeiten> die Bankdaten (IBAN) und die Methode SEPA eingetragen sind. Arbeiten Sie mit der Fibu-Erfassung wird hier auch der Kontostand der Bank angezeigt.

|
[Bild: 3]

Kontodaten

[Bild: 3. Kontodaten]

Diese Eingrenzung wird heutzutage nicht mehr benötigt, da Überweisungen nur noch per SEPA erfolgen können. Ihre Lieferanten müssen also zwingend eien IBAN hinterlegt haben.

|
[Bild: 4]

Engrenzungen

[Bild: 4. Engrenzungen]

-

nur fällige Rechnungen: Wenn Sie dieses Feld aktivieren, werden Ihnen nur die fälligen Rechnungen angezeigt. Ggf. erhalten Sie unterhalb der Liste eine Warnung, wenn es offenen Posten gibt, bei denen die BLZ bzw. die Bankdaten nicht vorhanden sind. Diese Rechnungen erscheinen NICHT in der Liste.

-

keine gesperrten Rechnungen: Wenn Sie dieses Feld aktivieren, werden gesperrten Rechnungen nicht zur Zahlung vorgeschlagen.

-

Geprüfte Rechnungen: Wenn Sie die Rechnungsprüfung aktiviert haben und dieses Feld anhaken, verhindern Sie damit, dass ungeprüfte Rechnungen zur Zahlung vorgeschlagen werden. Ob es noch ungeprüfte Rechnungen gibt, können Sie in der Hauptmaske unter dem Menüpunkt <Bearbeiten> <Rechnungsprüfung> nachschauen oder indem Sie die nachfolgende Option "Ungeprüfte Rechnungen" setzen.

-

Ungeprüfte Rechnungen: Wenn Sie die Rechnungsprüfung aktiviert haben und dieses Feld anhaken, werden auch ungeprüfte Rechnungen zur Zahlung vorgeschlagen.

-

ohne Einkaufs-Verband: Mit diesem Ankreuzfeld werden nur noch normale Rechnungen gezeigt und die mit der Zahlung über einen Einkaufsverband weggefiltert.

Hintergrund: Wenn viele Lieferanten über einen Einkaufsverband abgerechnet werden, kann es sinnvoll sein, nur die "anderen" zur Bezahlung zu sehen.

-

Skontofristen nutzen: Durch ein Kreuz in diesem Feld erreichen Sie, dass das Programm nicht nur fällige Rechnungen zeigt sondern auch diejenigen, die aufgrund der Skontofrist innerhalb des gewählten Zeitraumes bezahlt werden müssen.

-

Immer Skontoabzug: Durch ein Kreuz in diesem Feld erreichen Sie, dass das Programm auch dann Skonto berücksichtigt, wenn der Termin überschritten ist.

-

markierte Rechnungen immer zeigen: Durch Aktivieren dieser Option bleiben die markierten Rechnungen immer sichtbar. Ohne Aktivierung kann es passieren, dass Rechnungen nicht sichtbar sind, aber trotzdem bei der Zahlung mit einbezogen werden.

|
[Bild: 5]

Nächster Zahlungslauf am

[Bild: 5. Nächster Zahlungslauf am]

Hier wird Ihnen das Datum des nächsten Zahlungslaufes angezeigt und bezieht sich nur auf die Eingrezung Fälligkeit mit Skontofristen. Die Vorgabe hierfür wird im Modul EINSTELLUNGEN unter dem Menüpunkt <Programmbereiche> <Eingangsrechnungen> <Grundeinstellungen> festgelegt.

|
[Bild: 6]

Lieferant

[Bild: 6. Lieferant]

Durch Aktivieren dieses Feldes können Sie die Eingangsrechnungen auf einen bestimmten Lieferanten eingrenzen.

|
[Bild: 7]

Zahlung an

[Bild: 7. Zahlung an]

Diese Eingrenzung ist nur sichtbar, wenn eine bestimmte Grundeinstellung gesetzt ist. Sie ist dazu gedacht Rechnungen an einen Einkaufsverbund zu bezahlen und nicht direkt an den Händler. Bei Eingabe einer Adresse an dieser Stelle werden alle Rechnungen gezeigt, die direkt an den Einkaufsverbund gehen oder bei denen die Bezahlung an den Einkaufsverband erfolgen soll.

Die genaue Funktionsweise wird im Kapitel Zahlung an andere Adresse erklärt.

|
[Bild: 8]

Filterzeile

[Bild: 8. Filterzeile]

Die Rechnungsliste [Nr.9] lässt sich mit den bekannten Funktionen der Filterzeile eingrenzen.

|
[Bild: 9]

Rechnungsliste

[Bild: 9. Rechnungsliste]

In der Liste werden alle Rechnungen aufgeführt, die den im oberen Bereich getroffenen Eingrenzungen entsprechen.

Sie haben die Möglichkeit die Liste der aufgeführten Rechnungen zu sortieren, indem Sie in die jeweilige Überschrift klicken.

|
[Bild: 10]

Markieren

[Bild: 10. Markieren]

Damit Rechnungen in den Zahlunsglauf geschrieben werden, müssen diese markiert werden. Das geschieht entweder per Doppelklick auf die gewünschten Zeilen oder über diese Buttons. Entweder man markiert alle Rechnungen in der Rechnungsliste und nur die markierten. Gleiches gilt für das Löschen von zur Zahlung markierten Einträgen.

|

[Bild]

|

Markierte Rechnungen werden durch ein "Z" in der OK-Spalte dargestellt.

Wenn die Spalte leer ist oder ein O enthält, ist die Rechnung offen und wird nicht zur Zahlung angewiesen. Das Z bedeutet, dass diese Zahlung jetzt durchgeführt werden soll.

|
[Bild: 11]

Summen

[Bild: 11. Summen]

In diesen Feldern zeigt das Programm, die Anzahl und Summe der offenen Rechnungen, der aktuell gezeigten Liste markierten Rechnungen sowie alle gewählten Rechnungen. Hier bedarf es einer weiteren Erläuterung zwischen den aktuell markierten und allen gewählten Rechnungen. Die im oberen Bildschirmdrittel möglichen Begrenzungen können beliebig hin und her geschaltet werden, um bestimmte Rechnungen zu wählen. Wenn diese mit dem Z markiert sind, werden Sie in der Spalte alle gewählten eingetragen. Wenn Sie danach über eine Begrenzung z. B. mit einem bestimmten Lieferant die Liste umstellen, so kann es sein, dass Sie bereits gewählte Rechnungen nicht mehr in der Liste sehen, die dennoch zur Zahlung anstehen.

|
[Bild: 12]

ZL-Bemerkung

[Bild: 12. ZL-Bemerkung]

Hier wird Ihnen die Bemerkung des Zahlungslaufes angezeigt.

|
[Bild: 13]

Anmerkung

[Bild: 13. Anmerkung]

Wenn zu einer Eingangsrechnung eine Anmerkung hinterlegt wurde, ist dieser Knopf rot. Sie können hier die Möglichkeit, sich die Anmerkung anzusehen und ggf. zu ergänzen.

|
[Bild: 14]

Rechnung zeigen

[Bild: 14. Rechnung zeigen]

Wenn Sie die Eingangsrechnungen einscannen, können Sie sich über diesen Knopf die markierte Rechnung ansehen.

|
[Bild: 15]

Offener Posten Details

[Bild: 15. Offener Posten Details]

Hier werden die Details zu der in der Rechnungsliste markierten Rechnung angezeigt.

|
[Bild: 16]

Zahlplan bearbeiten

[Bild: 16. Zahlplan bearbeiten]

Wenn Sie diesen Knopf betätigen, gelangen Sie in den Zahlplan der in der Rechnungsliste markierten Rechnungen. Die gleiche Funktion erreichen Sie übrigens auch über einen Rechtsklick auf die markierte Rechnung

|
[Bild: 17]

Konto bearbeiten

[Bild: 17. Konto bearbeiten]

Durch Betätigen dieses Knopfes können Sie die Bankdaten des Lieferanten der in der Rechnungsliste markierten Rechnung ansehen und ggf. ändern.

|
[Bild: 18]

Liste aufbauen (F5)

[Bild: 18. Liste aufbauen (F5)]

Betätigen Sie diesen Knopf, damit die getroffenen Eingrenzungen sichtbar werden.

|
[Bild: 19]

Markierte Adresse (F8)

[Bild: 19. Markierte Adresse (F8)]

Bei Betätigung dieses Knopfes wird die Eingrenzung derart verändert, dass die Lieferantenadresse der markierten Rechnung als Eingrenzungskriterium verwendet wird und somit nur noch Rechnungen dieses Liefeanten angezeigt werden.

|
[Bild: 20]

Hilfe

[Bild: 20. Hilfe]

Durch Betätigen dieses Knopfes wird Ihnen ein Hilfetext angezeigt. Ggf. erhalten Sie hier einen weiteren Hinweis auf das LabelWiki.

|
[Bild: 21]

Fehlende Bankdaten

[Bild: 21. Fehlende Bankdaten]

Sollte es Eingangsrechnungen geben, bei denen die Bankdaten des Lieferanten unvollständig sind oder ganz fehlen, erhalten Sie einen Hinweis.

|
[Bild: 22]

OK Zahlen

[Bild: 22. OK Zahlen]

Wenn Sie diesen Knopf betätigen, versucht das Programm alle gewählten Rechnungen zu bezahlen. Je nach gewählter Zahlungsart erscheinen noch weitere Fragen, die von Ihnen beantwortet werden müssen. Dies betrifft insbesondere bei Diskette/Modem den Banknamen und die von Ihnen gewählte Kontonummer.

|
[Bild: 23]

Ende

[Bild: 23. Ende]

Durch Betätigung dieses Knopfes werden alle vorher getroffenen Auswahlen ungültig und die Zahlungsmaske wird verlassen.
