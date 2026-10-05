# 6. Rechnungen ohne Mehrwertsteuer §13 UstG

Pfad: Buchhaltung > Rechnungseingangsbuch [9] > 6. Rechnungen ohne Mehrwertsteuer §13 UstG
Quelle: handbuch/6__rechnungen_ohne_mehrwertsteuer__13_ustg.htm

|

6. Rechnungen ohne Mehrwertsteuer §13 UstG

Mit der Gesetzesänderung zum 01.04.2004 hat uns der Gesetzgeber den Umstand beschert, dass Rechnungen an Unternehmer, die selbst Bauleistungen verkaufen, ohne Mehrwertsteuer sein müssen. Ausgenommen sind davon reine Materiallieferungen, kleine Wartungen (wo immer hier die Grenze sein mag) und erst ab einer Rechnungshöhe von 500,00 €. Bei den 500,00 € handelt es in Deutschland entgegen anderen Gerüchten um eine Sollbestimmung. Das Programm prüft vor der Druckausgabe, ob Sie für die entsprechende Rechnungssumme ein passendes Erlöskonto gewählt haben.

Wenn Sie solche Rechnungen stellen müssen oder von Lieferanten solche Rechnungen bekommen, müssen Sie leider einige Einrichtungsarbeiten vornehmen.

1. Adressen

Bei jeder Adresse können Sie nun sowohl im Debitoren- als auch im Kreditorenbereich festlegen, ob diese in der Regel ohne Mehrwertsteuer benutzt wird. Die Festlegung erfolgt auf der Karteiseite ‚Bankdaten'. Bei der Anlage von neuen Dokumenten wird dann standardmäßig der passende Mehrwertsteuersatz vorgeschlagen.

Falls bei Ihnen bei der Dokumentenanlage die Mehrwertsteuer nicht ankreuzbar ist, müssen Sie einmal im Modul EINSTELLUNGEN unter dem Menüpunkt <Grundeinstellungen> <MwSt.-Sätze> ankreuzen, dass diese jeweils veränderbar sein sollen.

[Bild]

2. Zahlungsbedingungen

In der Zahlungsbedingung sollten Sie dem Rechnungsempfänger unbedingt mitteilen, dass er für die Abführung der Mehrwertsteuer selber verantwortlich ist. Über entsprechende Schlüsselworte können Sie auch die von ihm zu zahlende Mehrwertsteuersumme automatisch errechnen lassen. Bei der Erfassung der Zahlungsbedingungen im Modul EINSTELLUNGEN unter dem Menüpunkt <Grundeinstellungen> <Zahlungsbedingungen> finden Sie Muster-Zahlungsbedingungen, die Sie über die Zwischenablage kopieren können.

Es gibt sogar Schlüsselworte für den Mehrwertsteuerbetrag bei der Zahlung mit Skontoabzug.

[Bild]

3. Auswahl freischalten, ob mit MwSt

Damit Sie sehen, ob eine Rechnung oder ein Angebot mit oder ohne MwSt erstellt wird und Sie dies ggf. auch noch umschalten können, müssen Sie ggf. die Festlegung der MwSt frei schalten.

Wenn bei der gewählten Anschreibenanschrift das Kennzeichen für 'ohne MwSt.' gesetzt ist, wird auch dieses Dokument standardmäßig ohne Mehrwertsteuer angelegt.

Wenn bei Ihnen das Ankreuzfeld für die Mehrwertsteuer nicht sichtbar ist, sollten Sie dies unbedingt im Modul EINSTELLUNGEN unter dem Menüpunkt <Grundeinstellungen> <MwSt.-Sätze> freigeben.

[Bild]

Die Belegung der MwSt erfolgt automatisch aufgrund der bei der Adresse hinterlegten Vorgabe. Wenn Sie die MwSt-Eingabe frei geschaltet haben, können Sie in der Druckmaske jedoch auch manuell auf 0% schalten.

[Bild]

4. Kontenplan

Wenn Sie Rechnungen ohne MwSt schreiben oder solche von Subunternehmern erhalten, müssen Sie weitere Konten anlegen, die als Gegenstück zu den bisherigen mit MwSt arbeiten. In Labelwin ist es nicht möglich, ein Konto mal mit und mal ohne Steuer zu benutzen. Sie müssen dazu zwingend unterschiedliche Konten nutzen.

[Bild]

Bild: Kontenplan anlegen

Alle neuen Kontonummern müssen Sie unbedingt mit Ihrem Steuerberater absprechen.

Situation 1, keine Datenübergabe an Fibu:

Wenn Sie keine Daten an eine Fibu übergeben, also der Steuerberater ohnehin alle Belege manuell erfasst, brauchen Sie sich um die folgen Erklärungen nicht kümmern.

Situation 2, Übergabe Ausgangsrechnungen an Fibu:

Da diese in der Finanzbuchhaltung in der Regel als Automatikkonten benutzt werden, müssen Sie im Labelwin getrennte Konten für Vorgänge mit und ohne Mehrwertsteuer haben. Zu allen Erlöskonten müssen Sie also ein weiteres ohne MwSt anlegen.

Situation 3, Übergabe Eingangsrechnungen an Fibu:

Für Ihre Warenkonten, die mal mit und mal ohne MwSt. angesprochen werden, müssen Sie weitere ohne MwSt. anlegen.

Situation 4, Nutzung des Moduls FIBUER-FASSUNG:

Neben den weiteren Erlös- und Warenkonten müssen Sie Konten zur Verbuchung von Skonto anlegen. Da Skontoabzug ggf. eine Korrekturbuchung der MwSt oder der Vorsteuer verursacht, müssen Sie sowohl für erhaltene, als auch für gewährte Skonti getrennte Konten je Steuersatz führen. Dazu sind im Kontenplan neue Kennzeichnungen für die Kontennutzung eingeführt worden.

[Bild]

4a. Eingangsrechnungen - Skontokonto

Da bei der Bezahlung per Zahlungslauf Rechnungen mit unterschiedlichen Steuersätzen beglichen werden und die Abbuchung in der FIBUERFASSUNG auf einen Rutsch passiert, müssen ggf. in einem Zahlungslauf verschiedene Skontokonten angesprochen werden. Dies würde natürlich einen erheblichen Aufwand verursachen, so dass wir die Festlegung des zu nutzenden Skonto-Kontos einfach bei der Erfassung der Eingangsrechnung ermöglichen. Wenn Sie keines festlegen (alte Rechnungen), so wird weiterhin das bisherige Standardkonto für Skonti verwendet (dies ist in den Grundeinstellungen der FIBUERFASSUNG festgelegt).

5. Eingangsrechnungen - Betrag ist Netto

Um die Erfassung von Rechnungen ohne Mehrwertsteueranteil zu erleichtern, finden Sie nun neben der Rechnungsnummer ein Ankreuzfeld ‚Betrag ist Netto'. Dieses Feld wird aufgrund der in der Adresse hinterlegten Information passend vorgeschlagen.

Weiter finden Sie in der Maske eine Auswahlliste der Skonto-Konten. Je nachdem, ob die Rechnung mit oder ohne Mehrwertsteuer ist, wird das Konto für Skontobuchungen mit oder ohne Mehrwertsteuer vorgeschlagen.

|

Wichtig ist das Skonto-Konto nur für diejenigen, die ihre Eingangsrechnungen per Zahlungslauf bezahlen und diesen in dem Programmmodul FIBUERFASSUNG buchen.

Da innerhalb eines Zahlungslaufs nun Konten mit unterschiedlichen Mehrwertsteuersätzen angesprochen werden können, müssen die Skontobeträge entsprechend auf unterschiedliche Konten gebucht werden.

[Bild]

Bild: Eingangsrechnung erfassen
