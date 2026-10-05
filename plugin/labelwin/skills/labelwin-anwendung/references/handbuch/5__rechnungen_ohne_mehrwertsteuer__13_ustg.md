# 5. Rechnungen ohne Mehrwertsteuer §13 UstG

Pfad: Buchhaltung > Rechnungsausgangsbuch [7] > 5. Rechnungen ohne Mehrwertsteuer §13 UstG
Quelle: handbuch/5__rechnungen_ohne_mehrwertsteuer__13_ustg.htm

|

5. Rechnungen ohne Mehrwertsteuer §13 UstG

Mit einer Gesetzesänderung zum 01.04.2004 hat uns der Gesetzgeber den Umstand beschert, dass Rechnungen an Unternehmer, die selbst Bauleistungen verkaufen, ohne Mehrwertsteuer sein müssen. Ausgenommen sind davon reine Materiallieferungen, kleine Wartungen (wo immer hier die Grenze sein mag) und erst ab einer Rechnungshöhe von 500,00 €. Bei den 500,00 € handelt es sich in Deutschland entgegen anderen Gerüchten um eine Sollbestimmung. Das Programm prüft vor der Druckausgabe, ob Sie für die entsprechende Rechnungssumme ein passendes Erlöskonto gewählt haben.

Wenn Sie solche Rechnungen stellen müssen oder von Lieferanten solche Rechnungen bekommen, müssen Sie leider einige Einrichtungsarbeiten vornehmen.

1. Adressen

|

Bei jeder Adresse können Sie nun sowohl im Debitoren- als auch im Kreditorenbereich festlegen, ob diese in der Regel ohne Mehrwertsteuer benutzt wird. Die Festlegung erfolgt auf der Karteiseite ‚Bankdaten'. Bei der Anlage von neuen Dokumenten wird dann standardmäßig der passende Mehrwertsteuersatz vorgeschlagen.

Falls Sie bei der Dokumentenanlage die Mehrwertsteuer nicht aktivieren können, müssen Sie einmal im Modul EINSTELLUNGEN unter dem Menüpunkt <Grundeinstellungen> <MwSt.-Sätze> ankreuzen, dass diese jeweils veränderbar sein sollen.

|

[Bild]

2. Zahlungsbedingungen

|

In der Zahlungsbedingung sollten Sie dem Rechnungsempfänger unbedingt mitteilen, dass er für die Abführung der Mehrwertsteuer selber verantwortlich ist. Über entsprechende Schlüsselworte können Sie auch die von ihm zu zahlende Mehrwertsteuersumme automatisch errechnen lassen. Bei der Erfassung der Zahlungsbedingungen (Modul EINSTELLUNGEN unter dem Menüpunkt <Grundeinstellungen> <Zahlungsbedingungen>) finden Sie Muster-Zahlungsbedingungen, die Sie über die Zwischenablage kopieren können.

Es gibt sogar Schlüsselworte für den Mehrwertsteuerbetrag bei der Zahlung mit Skontoabzug.

|

[Bild]

3. Auswahl freischalten, ob mit MwSt

|

Damit Sie sehen, ob eine Rechnung oder ein Angebot mit oder ohne MwSt erstellt wird und Sie dies ggf. auch noch umschalten können, müssen Sie ggf. die Festlegung der MwSt frei schalten.

Wenn bei der gewählten Anschreibenanschrift das Kennzeichen für ‚ohne MwSt.' gesetzt ist, wird auch dieses Dokument standardmäßig ohne Mehrwertsteuer angelegt.

|

[Bild]

Wenn bei Ihnen das Ankreuzfeld für die Mehrwertsteuer nicht sichtbar ist, sollten Sie dies unbedingt im Modul EINSTELLUNGEN unter dem Menüpunkt <Grundeinstellungen> <MwSt.-Sätze> freigeben.

[Bild]

Die Belegung der MwSt erfolgt automatisch aufgrund der bei der Adresse hinterlegten Vorgabe. Wenn Sie die MwSt-Eingabe frei geschaltet haben, können Sie jedoch auch manuell auf 0% schalten.

4. Kontenplan

Wenn Sie Rechnungen ohne MwSt schreiben oder solche von Subunternehmern erhalten, müssen Sie weitere Konten anlegen, die als Gegenstück zu den bisherigen ohne MwSt arbeiten. In Labelwin ist es nicht möglich, ein Konto mal mit und mal ohne Steuer zu benutzen. Sie müssen dazu zwingend unterschiedliche Konten nutzen.

Alle neuen Kontonummern müssen Sie unbedingt mit Ihrem Steuerberater absprechen.

Situation 1, keine Datenübergabe an Fibu:

Wenn Sie keine Daten an eine Fibu übergeben, also der Steuerberater ohnehin alle Belege manuell erfasst, brauchen Sie sich um die folgen Erklärungen nicht kümmern.

Situation 2, Übergabe Ausgangsrechnungen an Fibu:

Da diese in der Finanzbuchhaltung in der Regel als Automatikkonten benutzt werden, müssen Sie im Labelwin getrennte Konten für Vorgänge mit und ohne Mehrwertsteuer haben. Zu allen Erlöskonten müssen Sie also ein weiteres ohne MwSt anlegen.

Situation 3, Übergabe Eingangsrechnungen an Fibu:

Für Ihre Warenkonten, die mal mit und mal ohne MwSt. angesprochen werden, müssen Sie weitere ohne MwSt. anlegen.

[Bild]

Situation 4, Nutzung des Moduls Fibuerfassung:

Neben den weiteren Erlös- und Warenkonten müssen Sie Konten zur Verbuchung von Skonto anlegen. Da Skontoabzug ggf. eine Korrekturbuchung der MwSt oder der Vorsteuer verursacht, müssen Sie sowohl für erhaltene, als auch für gewährte Skonti getrennte Konten je Steuersatz führen. Dazu sind im Kontenplan neue Kennzeichnungen für die Kontennutzung eingeführt worden.

Ausgangsrechnungen

Hier können Sie dem Erlöskonto das ggf. zu nutzende Skonto-Konto direkt zuordnen. Wenn Sie z.B. Erlöskonten je Abteilung verwenden, so können Sie damit auch ein Skontokonto je Abteilung festlegen.

[Bild]

Die in obigem Bild sichtbare Eintragung ‚Skontokonto Erlöse’ ist nur bei Konten mit dem Kennzeichen ‚Erlöskonto’ sichtbar. Damit kann man einem Erlöskonto direkt ein Skonto-Konto zuordnen (Anwendung in der Fibuerfassung)

5. Abschlags-, Teil- und Endrechnungen

In Bezug auf die Mehrwertsteuer gilt hier zunächst das Gleiche wie bei den normalen Ausgangsrechnungen. Hinzu gekommen ist jedoch die Forderung des Gesetzgebers, die eingegangenen Zahlungen und die berücksichtigte Mehrwertsteuer auf der Schlussrechnung zu vermerken. Darüber hinaus entstehen Übergangsprobleme, wenn erste Abschlags- und Teilrechnungen mit Mehrwertsteuer und alle weiteren ohne Mehrwertsteuer erstellt werden. Das bisher eingesetzte Druckformular kann mit dieser Situation nicht umgehen. Wenn bei Ihnen unser Standardformular im Einsatz ist, können Sie dieses relativ leicht auswechseln und über die Seitenränder an Ihr Briefpapier anpassen. Wenn es sich jedoch um ein speziell für Sie angepasstes Formular handelt, müssen wir unser Standardformular nehmen und erneut an Ihre Bedürfnisse anpassen. Für unsere Wartungskunden nehmen wir diese Anpassung zu einem Pauschalpreis von 25,00 € + MwSt. für das erste Formular und für 15 € für jedes weitere Formular vor. In der Regel hat jeder Kunde nur ein Formular für Schlussrechnungen im Einsatz. Bei Teilrechnungen mit Abzugsblock wird das gleiche Formular genutzt.

Eine Zusammenstellung in der Endrechnung kann jetzt so aussehen:

[Bild]
