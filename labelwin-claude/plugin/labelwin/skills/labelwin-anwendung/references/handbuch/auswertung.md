# Auswertung

Pfad: Auswertungen / Controlling > Liquidität [Modul] > Auswertung
Quelle: handbuch/auswertung.htm

|

Auswertung

Die Auswertung erfolgt nach entsprechender Einrichtung im Bereich der Controlling-Auswertungen.

Starten Sie also das Modul Selektieren, und wählen die Menüpunkte <Controlling>, <Auswertungen ausgeben>.

Gestartet wird die Auswertung mit dem Namen ‚Liquidität’. Es sind keine Datumseingrenzungen erforderlich.

Nach dem Start erscheint eine Maske, in der der Auswertungszeitraum, der bisherige Kontostand und der Kreditrahmen erfasst werden muss.

[Bild]

Der Kontostand wird aufgrund des Moduls ‚Fibuerfassung’ vorgeschlagen. Der Stand von allen Bankkonten wird addiert. Anwender ohne die Nutzung des Moduls können den Kontostand einfach eingeben.

Das Kreditlimit dient nur dazu, die Summen außerhalb dieses Rahmens in einer anderen Farbe darstellen zu können.

In der Exelauswertung werden für die wöchentliche Betrachtung aufaddiert:

- der aktuelle Kontenstand in der ersten Woche

- die Summen der offenen (=unbezahlten) Eingangsrechnungen in der jeweiligen Woche, in der sie fällig sind. Das Programm geht dabei vom Skontoziel aus. Die Zahlsummen werden mit Nutzung des Skontos berücksichtigt. Es werden nur die Rechnungen für Projekte genommen, die das Kennzeichen ‚Dauerprojekt’ nicht haben.

- Die Summen der offenen Ausgangsrechnungen aufgrund des angebotenen Skontoziels. Bei den Summen gehen wir davon aus, dass der Kunde angebotene Skonti nutzt. Es werden nur die Rechnungen für Projekte genommen, die das Kennzeichen ‚Dauerprojekt’ nicht haben.

- Die Einträge im Rechnungsplan mit den noch nicht geschriebenen Rechnungen. Bei den Summen und dem Zahlungseingang gehen wir wieder von Skontonutzung aus

- Die Einträge im Kostenplan, die noch nicht über eine Eingangsrechnung ‚neutralisiert’ worden sind

- Die Einträge in den Gemeinkosten / Erlösen

Nicht berücksichtigt werden überfällige Rechnungen, sowohl im Eingangs- als auch im Ausgangsbereich. Es gibt ja immer einen gewissen ‚überfällig Stand’, der bei einer halbwegs konstanten Höhe die Liquidität nicht beeinflusst. Letztlich ist ja nicht bekannt, ob sie überhaupt bezahlt werden.

Excel-Blatt ‚Korrektur’

Die Auswertung selbst, also die Exceltabelle wollen wir hier nicht darstellen. Einige Anmerkungen zum Blatt Korrektur halten wir aber für erforderlich:

Auf diesem Blatt können manuell Korrekturen vorgenommen werden, wenn es Werte gibt, die in den Grunddaten nicht erfasst werden können. Dies könnte z.B. eine große überfällige Rechnung sein, von der man weiß, dass die Zahlung eingeht. Wenn es sich bei der Korrektur um eine Verschiebung handelt, müssen Sie den Wert in der einen Woche positiv und in der anderen negativ eingeben.

Die Eingabe der Korrekturwerte erfolgt in den blauen Feldern. Für die ersten beiden Wochen haben wir eine detailierte Eingabe der Kosten / Erlöse eingerichtet, für die restlichen Wochen nur einen Gesamtwert. Spielen Sie einfach mit den Zahlen, es kann ja nicht kaputt gehen.

[Bild]
