# 2b. Die LabelCRM-Maske im Detail (alt)

Pfad: Adressverwaltung > LabelCRM [28] > 2b. Die LabelCRM-Maske im Detail (alt)
Quelle: handbuch/2b__die_labelcrm_maske_im_detail__alt_.htm

|

2b. Die LabelCRM-Maske im Detail (alt)

Der Vollständigkeit halber folgt hier noch die Beschreibung der alten LabelCRM Maske der V4 Version. Wir empfehlen aber jedem Anwender die neue V5 Oberfläche zu verwenden - nicht zuletzt, weil die neue LabelCRM Maske deutlich mehr Möglichkeiten bietet.

[Bild]

[Bild]

1 Suchwort: Geben Sie hier das Suchwort der Adresse ein. Wenn Sie mit der Telefonanbindung arbeiten und diese entsprechend eingestellt ist, startet das Modul automatisch und die entsprechende Adresse ist bereits vorgegeben. Mit Enter oder dem Suchen-Knopf wird die Adresse gesucht.

[Bild]

2 komplette Anschrift: Hier sehen Sie die komplette Anschrift. Es handelt sich hierbei um ein reines Anzeigefeld und dient nur zur Information. Änderungen können hier nicht vorgenommen werden.

[Bild]

3 Suchen: Nach Eingabe eines Suchbegriffs kann die Suche mit Enter oder diesem Knopf ausgelöst werden.

[Bild]

4 Adresse: Wenn Sie diesen Knopf aktivieren, wird das Modul Adressen gestartet. Hier können dann ggf. Änderungen oder Ergänzungen vorgenommen werden.

[Bild]

5 weitere Adressen: Wenn Sie diesen Knopf aktivieren, gelangen Sie in die Maske der weiteren Adressen und können hier ggf. etwas ergänzen. Wurden hier schon weitere Adressen hinterlegt, ist der Knopf rot.

[Bild]

6 Internet: Wenn in der aktivieren Adresse eine Internetadresse eingetragen wurde, kann diese über den Knopf direkt aufgerufen werden.

[Bild]

7 Telefonprotokoll: Hier erhalten Sie eine Liste der protokollierten Anrufe, die der ausgewählten Adresse eindeutig zugeordnet wurden. Diese Funktion steht Ihnen nur zur Verfügung, wenn Sie das Modul Telefonanbindung erworben haben.

[Bild]

8 Wählhilfe: Wenn die Windows-Wählhilfe bei Ihnen funktioniert, können Sie über diesen Knopf die angezeigte Nummer anwählen.

[Bild]

9 zusätzliche Adressen: Wenn Sie zur aktiven Adresse weitere Adressen wie Rg.-Adresse, Eigentümer, Versand an oder Hausmeister hinterlegt haben, dann werden Ihnen diese hier mit dem Kurznamen angezeigt. Wenn die aktive Adresse einer Liegenschaft zugeordnet ist, wird diese ebenfalls angezeigt.

Wenn die Rechnungsanschrift offene Posten hat, wird dieses durch einen auffälligen Hinweis angezeigt. Um die Höhe des OP’s zu sehen, müssen Sie nur die Adresse aktivieren.

Bei entsprechender Festlegung im Modul EINSTELLUNGEN kann mit dem Knopf ‚Aktivieren‘ auch ein neues, weiteres Label CRM-Fenster geöffnet werden. Das hat den Vorteil, dass das Fenster des Anrufenden geöffnet bleibt und man dennoch bei den weiteren Adressen etwas nachschauen kann. Es hat den einzigen Nachteil, dass damit noch mehr geöffnete Fenster sichtbar sind, und der Anwender ggf. den Überblick verliert.

Das entsprechende Feld zum Aktivieren dieser Funktion finden Sie im Modul EINSTELLUNGEN unter dem Menüpunkt <Programmbereiche> <Adressen> <Grundeinstellungen>.

[Bild]

[Bild]

10 Forderungen: Falls es zu der gewählten Adresse offene Forderungen gibt, werden Ihnen diese hier angezeigt. Über den Knopf ‚Anzeigen‘ gelangen Sie in die Rechnungsausgangsliste.

[Bild]

Dort haben Sie über den Knopf ‚Druck‘ die Möglichkeit, dem Kunden schnell per Email eine Liste der offenen Posten zu senden. Voraussetzung hierfür ist jedoch, dass Sie einen pdf-Drucker installiert haben. Eine Beschreibung dazu gibt es in unserem Handbuch unter PDF Ablage und PDF Druckertreiber.

[Bild]

11 Überfällig: Wenn eine Forderung überfällig ist, wird diese in rot angezeigt.

[Bild]

12 Verbindlichkeiten: Wenn es zu der gewählten Adresse Verbindlichkeiten gibt, werden Ihnen diese hier angezeigt. Über den Knopf ‚Anzeigen‘ gelangen Sie in die Eingangsrechnungsliste.

[Bild]

13 Bewertung: In der Adressmaske auf der Karteiseite ‚Bankdaten', im Kundendienst und im Label CRM werden Zahlen über einen Mahnfaktor und die Zahlungsmoral angezeigt.

Diese Werte werden per Durchlauf im Rechnungsausgangsbuch in die Adressen eingetragen.

Genauere Information über die Grundlage der Zahlen findet sich in der OP-Anzeige im Kundendienst und in der Adresse. Dort kann der Wert auch aktualisiert werden.

Berechnung:

Mahnfaktor =

Anzahl der Mahnungen Stufe 1 (= Zahlungserinnerung)

+ Anzahl der Mahnungen Stufe 2 * 4 (= 1. Mahnung)

+ Anzahl der Mahnungen Stufe 3 * 9 (= 2. Mahnung)

+ Anzahl der Mahnungen Stufe 4 * 16 (= 3. Mahnung)

geteilt durch die Anzahl der berücksichtigten Rechnungen * 100

Ein Faktor von 100 bedeutet also, dass durchschnittlich jede Rechnung die Mahnstufe 1 erreicht hat. Ein Faktor von 0 bedeutet, dass alle Rechnungen ohne Mahnung bezahlt wurden.

Je höher die Zahl desto schlechter der Wert. Durch die Multiplikatoren mit 4, 9, 16 wird erreicht, dass die höhere Mahnstufe verstärkt in den Mahnfaktor greift. Je höher die Mahnstufe desto stärker der Einfluss auf den Mahnfaktor.

Zahlungsmoral in Tagen =

( Addition aller (Tage zwischen Druckdatum und Zahlungsdatum) * gezahlte Summe ) / (Addition aller Rechnungssummen)

Beispiel: Rechnung 1000 €

Zahlung 1 nach 10 Tagen mit 600 € = 6000 Punkte

Zahlung 2 nach 20 Tagen mit 400 € = 8000 Punkte

Summe 14000 Punkte geteilt durch 1000 € ergibt 14 Tage Zahlungsmoral

[Bild]

14 aktive Projekte: Hier erhalten Sie je nach Wahl des Knopfes eine Projektliste. Da die Projektverwaltung nur einmal zu starten ist, kann das Projekt hier nicht aktiviert werden.

Anschreibenadresse: Hier erhalten Sie eine Liste aller Projekte, bei denen die gewählte Adresse im Datenblatt als Auftraggeber hinterlegt ist. Der Knopf wird dann rot.

Baustellenadresse: Hier erhalten Sie eine Liste aller Projekte, bei denen die gewählte Adresse im Datenblatt als Objektadresse hinterlegt ist.

[Bild]

15 Dokumentenliste: Hier erhalten Sie je nach Wahl des Knopfes eine Dokumentenliste, in der die gewählte Adresse entweder als Anschreibenadresse, als Baustellenadresse oder als Versandadresse verwendet wird.

[Bild]

16 Rechnungsartikel: Hier erhalten Sie je nach Wahl des Knopfes die Rechnungsartikel, in der die aktive Adresse entweder die Anschreibenadresse (Rechnungsempfänger), die Baustellenadresse oder die Versandadresse ist

[Bild]

17 KD-Logbuch: Durch Aktivieren dieses Knopfes gelangen Sie ins Kundendienst-Logbuch. Wenn es noch offene Aufträge gibt, ist der Knopf rot.

[Bild]

18 Anlagen: Durch Aktivieren dieses Knopfes gelangen Sie in die Anlagenmaske. Hier können Sie eine neue Anlage erfassen. Ist der Adresse bereits eine Anlage zugeordnet, ist dieser Knopf rot. Wenn es zu der Anlage einen Vertrag gibt, ändert sich die Beschriftung auf ‚Anlagen + Vertrag‘.

[Bild]

19 Verträge: Durch Betätigen des Knopfes gelangen Sie in die Maske Wartungsverträge. Hier können Sie einen neuen Vertrag anlegen oder zu einem bestehenden Vertrag Änderungen vornehmen. Gibt es zu der gewählten Adresse bereits einen Vertrag, ist der Knopf rot.

[Bild]

20 SMS: Durch Aktivieren dieses Knopfes gelangen Sie in die Maske zur Erfassung einer SMS. Es werden Ihnen hier die Telefon-Nr. vorgeschlagen, die bei der aktivieren Adresse hinterlegt sind.

[Bild]

21 Aufgaben: Durch Aktivieren dieses Knopfes gelangen Sie in die Aufgabenliste. Hier haben Sie dann die Möglichkeit, eine neue Aufgabe zu erfassen oder eine bereits vorhandene zu ändern. Wenn es zu der gewählten Adresse offene Aufgaben gibt, erscheint der Knopf in rot.

[Bild]

22 F2 Neues Dokument: Durch Aktivieren dieses Knopfes haben Sie die Möglichkeit, ein neues Dokument zu erfassen. Sollten Sie mit mehreren Mandanten arbeiten, können Sie in dem aufsteigenden Fenster den Mandanten wechseln.

[Bild]

23 F3 Neuer KD-Auftrag: Durch Aktivieren dieses Knopfes haben Sie die Möglichkeit, einen neuen Kundendienstauftrag zu erfassen. Sollten Sie mit mehreren Mandanten arbeiten, können Sie in dem aufsteigenden Fenster den Mandanten wechseln.

[Bild]

24 Anzeige Mandant: Wenn Sie mit der Mandantenversion arbeiten, wird Ihnen hier der Mandant angezeigt, in dem Sie gerade arbeiten.

[Bild]

25 Ende: Durch Betätigen dieses Knopfes wird das Label CRM-Fenster geschlossen.

[Bild]

26 Label News: Wenn es Neuigkeiten zu Labelwin gibt, werden diese anzeigt. Mit einem Klick auf das Kästchen startet das LabelWiki und Sie gelangen zu den News.
