# 4. Bezahlen

Pfad: Buchhaltung > Rechnungseingangsbuch [9] > 4. Bezahlen
Quelle: handbuch/4__bezahlen.htm

|

4. Bezahlen

Sie erreichen diese Maske durch Wahl des Moduls Rechnungseingang unter dem Menüpunkt <Bezahlen> <Bezahlen offene Rechnungen>.

Nach der Anwahl dieses Menüpunktes, erzeugt das Programm eine Liste der offenen Rechnungen. Dieser Vorgang kann bei großen Datenmengen einige Minuten dauern. Die Laufzeit wird durch einen roten Balken dargestellt. Aus dieser Liste der offenen Rechnungen können Sie über automatische Eingrenzungen oder durch Einzelauswahl die Rechnungen auswählen, die bezahlt werden sollen. Die gewählten Rechnungen werden zu einem Zahlungslauf zusammengefasst, dem das Programm automatisch eine laufende Nummer gibt. Über diese laufende Nummer können die gewählten Rechnungen später per Durchlauf auch auf bezahlt gesetzt werden. Bei der Zahlungsanweisung bleiben die Rechnungen auf offen stehen, um gegebenenfalls bei einem Druckerfehler oder einem Diskettenfehler den Vorgang wiederholen zu können.

[Bild]

Bild: Eingangsrechnung bezahlen

Neu ab V4.82: Ankreuzfeld 'ohne Einkaufs-Verband'

Mit dem neuen Ankreuzfeld 'ohne Einkaufs-Verband' werden nur noch normale Rechnungen gezeigt und die mit der Zahlung über einen Einkaufsverband weggefiltert.

Hintergrund: Wenn viele Lieferanten über einen Einkaufsverband abgerechnet werden, kann es sinnvoll sein, nur die ‚anderen‘ zur Bezahlung zu sehen.

Wenn das Programm mehrere Rechnungen für einen Lieferanten vorfindet, so fasst es diese zu einer Zahlung zusammen und es kann ein Begleitschreiben erstellt werden, mit dem Sie Ihrem Lieferanten die bezahlten Rechnungen mitteilen können.

Wenn Sie eine markierte Rechnung mit der rechten Maustaste anklicken, gelangen Sie in den Zahlungsplan oder über den Knopf ‚Zahlplan‘.

Sie haben die Möglichkeit die Liste der aufgeführten Rechnungen zu sortieren, indem Sie in die jeweilige Überschrift klicken.

Sollte es Eingangsrechnungen geben, bei denen die Bankdaten des Lieferanten unvollständig sind oder ganz fehlen, erhalten Sie einen Hinweis.

[Bild]

1 Zahlungsart: Hier legen Sie fest, wie die gewählten Rechnungen bezahlt werden sollen. Sollten Sie einige Rechnungen per Scheck, andere per Überweisung und wieder andere per Diskette bezahlen wollen, so müssen Sie dies in getrennten Zahlungsläufen durchführen. Die Wahl an diesem Punkt gilt für alle ausgewählten Rechnungen.

[Bild]

2 Immer Skontoabzug: Durch ein Kreuz in diesem Feld erreichen Sie, dass das Programm auch dann Skonto berücksichtigt, wenn der Termin überschritten ist.

[Bild]

3 Bank: Wählen Sie hier die Bank aus, mit der Sie bezahlen möchten. Hinterlegen Sie bei der Bank unter dem Menüpunkt <Optionen> <Eigene Bankdaten bearbeiten> welche Methoden (DTAUS, DTAZV, SEPA, VIR) die Bank verarbeiten kann. Kann sie nur DTAUS, muss bei allen Lieferanten BLZ und Konto hinterlegt sein. Bei den anderen Methoden muss bei allen Lieferanten BIC/Swift und IBAN hinterlegt sein.

[Bild]

4 nur fällige Rechnungen: Wenn Sie dieses Feld aktivieren, werden Ihnen nur die fälligen Rechnungen angezeigt. Ggf. erhalten Sie unterhalb der Liste eine Warnung, wenn es offenen Posten gibt, bei denen die BLZ bzw. die Bankdaten nicht vorhanden sind. Diese Rechnungen erscheinen NICHT in der Liste.

[Bild]

5 Skontofristen nutzen: Durch ein Kreuz in diesem Feld erreichen Sie, dass das Programm nicht nur fällige Rechnungen zeigt sondern auch diejenigen, die aufgrund der Skontofrist innerhalb des gewählten Zeitraumes bezahlt werden müssen.

[Bild]

6 Datum des nächsten Zahlungslaufes: Hier wird Ihnen das Datum des nächsten Zahlungslaufes angezeigt und bezieht sich nur auf die Eingrezung Fälligkeit mit Skontofristen. Die Vorgabe hierfür wird im Modul EINSTELLUNGEN unter dem Menüpunkt <Programmbereiche> <Eingangsrechnungen> <Grundeinstellungen> festgelegt.

[Bild]

7 bestimmter Lieferant: Durch Aktivieren dieses Feldes können Sie die Eingangsrechnungen auf einen bestimmten Lieferanten eingrenzen.

[Bild]

8 keine gesperrten Rechnungen: Wenn Sie dieses Feld aktivieren, werden gesperrten Rechnungen nicht zur Zahlung vorgeschlagen.

[Bild]

9 nur geprüfte Rechnungen: Wenn Sie die Rechnungsprüfung aktiviert haben und dieses Feld anhaken, verhindern Sie damit, dass ungeprüfte Rechnungen zur Zahlung vorgeschlagen werden. Ob es noch ungeprüfte Rechnungen gibt, können Sie in der Hauptmaske unter dem Menüpunkt <Bearbeiten> <Rechnungsprüfung> nachschauen

[Bild]

10 markierte Rechnungen immer zeigen: Durch Aktivieren dieser Option bleiben die markierten Rechnungen immer sichtbar. Ohne Aktivierung kann es passieren, dass Rechnungen nicht sichtbar sind, aber trotzdem bei der Zahlung mit einbezogen werden.

[Bild]

11 Liste aufbauen: Betätigen Sie diesen Knopf, damit die getroffenen Eingrenzungen sichtbar werden.

[Bild]

12 Hilfe: Durch Betätigen dieses Knopfes wird Ihnen ein Hilfetext angezeigt. Ggf. erhalten Sie hier einen weiteren Hinweis auf das LabelWiki.

[Bild]

13 OK-Spalte in Rechnungstabelle: In dieser Spalte können Sie sehen, wenn eine Rechnung zum Zahlen angewiesen ist. Wenn die Spalte leer ist oder ein O enthält, ist die Rechnung offen und wird nicht zur Zahlung angewiesen. Wenn Sie die Zeile mit einem Doppelklick markieren, so wird ein Z in die OK-Spalte eingetragen. Das Z bedeutet, dass diese Zahlung jetzt durchgeführt werden soll.

[Bild]

14 Anzeigefeld der gewählten Rechnungen: In diesen Feldern zeigt das Programm, die Anzahl und Summe der offenen Rechnungen, der aktuell gezeigten Liste markierten Rechnungen sowie alle gewählten Rechnungen. Hier bedarf es einer weiteren Erläuterung zwischen den aktuell markierten und allen gewählten Rechnungen. Die im oberen Bildschirmdrittel möglichen Begrenzungen können beliebig hin und her geschaltet werden, um bestimmte Rechnungen zu wählen. Wenn diese mit dem Z markiert sind, werden Sie in der Spalte alle gewählten eingetragen. Wenn Sie danach über eine Begrenzung z. B. mit einem bestimmten Lieferant die Liste umstellen, so kann es sein, dass Sie bereits gewählte Rechnungen nicht mehr in der Liste sehen, die dennoch zur Zahlung anstehen.

[Bild]

15 Anmerkung: Wenn zu einer Eingangsrechnung eine Anmerkung hinterlegt wurde, ist dieser Knopf rot. Sie können hier die Möglichkeit, sich die Anmerkung anzusehen und ggf. zu ergänzen.

[Bild]

16 Rechnung zeigen: Wenn Sie die Eingangsrechnungen einscannen, können Sie sich über diesen Knopf die markierte Rechnung ansehen.

[Bild]

17 Zahlplan bearbeiten: Wenn Sie diesen Knopf betätigen, gelangen Sie in den Zahlplan der in der Rechnungsliste markierten Rechnungen.

[Bild]

18 Kontodaten bearbeiten: Durch Betätigen dieses Knopfes können Sie die Bankdaten des Lieferanten der in der Rechnungsliste markierten Rechnung ansehen und ggf. ändern.

[Bild]

19 ZL-Bemerkung: Hier wird Ihnen die Bemerkung des Zahlungslaufes angezeigt.

[Bild]

20 OK/Zahlen: Wenn Sie diesen Knopf betätigen, versucht das Programm alle gewählten Rechnungen zu bezahlen. Je nach gewählter Zahlungsart erscheinen noch weitere Fragen, die von Ihnen beantwortet werden müssen. Dies betrifft insbesondere bei Diskette/Modem den Banknamen und die von Ihnen gewählte Kontonummer.

[Bild]

21 Ende: Durch Betätigung dieses Knopfes werden alle vorher getroffenen Auswahlen ungültig und die Zahlungsmaske wird verlassen.
