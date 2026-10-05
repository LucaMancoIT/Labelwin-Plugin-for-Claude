# 15. Brutto / Nettoabzüge unter Summenblock

Pfad: Projektverwaltung > Projektverwaltung [2] > 15. Brutto / Nettoabzüge unter Summenblock
Quelle: handbuch/15__brutto___nettoabzuge_unter_summenblock.htm

|

15. Brutto / Nettoabzüge unter Summenblock

Stand 10.09.2011

Es geht um Abzüge, die unter dem Summenblock der Rechnung geschrieben werden sollen. Bei den Nettoabzügen könnten sie im Grunde genommen auch in den Artikelbereich geschrieben werden, aber das ist halt eine Frage des Geschmacks. Einen Vorteil hat die Darstellung unter dem Summenblock allerdings: Wenn man mit Titeln oder Losen arbeitet, müssen alle Artikel innerhalb von Titeln und Losen stehen. Ggf. muss man also wegen. einem Nettoabzug extra einen neuen Titel und vielleicht sogar ein neues Los einführen.

Bis zur Freigabe gibt es den Schalter global.ini , GRUNDEINSTELLUNGEN, prnachlass=1

Nettoabzüge wirken so, als wenn sie im Artikelbereich stehen würden. Sie mindern die Rechnungssumme und auch den MwSt-Betrag.

Bruttoabzüge sind nur ein Angebot, die Zahlsumme zu mindern. Im Grunde genommen werden dabei nur Abzüge angeboten, die der Auftraggeber ohnehin abgezogen hätte. Das können bei Teil- und Abschlagsrechnungen Dinge wie anteilige Kosten für Baustrom, Versicherung und auch Sicherheitseinbehalt sein. Die im Rechnungsausgangsbuch eingetragenen Summen werden durch Bruttoabzüge nicht verändert. Für die Endrechnung kommt damit nur noch der Sicherheitseinbehalt als Bruttoabzug in Frage. Baustrom, Versicherung usw. müssen bei der Endrechnung entweder als Nettoabzug dargestellt werden oder man muss sie richtigerweise über eine Eingangsrechnung abrechnen.

Um mit den hier beschriebenen Abzügen arbeiten zu können, müssen speziell angepasste Druckformulare verwendet werden.

Die Abzüge können nicht bei jeder Rechnung individuell festgelegt werden, sondern müssen für das ganze Projekt erfasst werden. Sie greifen dann natürlich nur für nachfolgend erfasste Rechnungen.

Es kann mit Vorlagen gearbeitet werden. Diese finden Sie im Einstellmodul unter Programmbereiche, Projekt, Abzüge/Nachlass

Einrichten:

Bevor Sie bei einem Projekt die Daten für Abzüge eingeben, sollten Sie mindestens eine Vorlage erfassen. Gehen Sie dazu ins Modul Einstellungen und wählen die Menüpunkte <Programmbereiche>, <Projektverwaltung>, <Abzüge / Nachlass> an.

Dort erfassen Sie Daten für Brutto und Nettoabzüge.

, [Bild]

Oben links legen Sie fest, ob Sie Netto- oder Brutto-Abzüge erfassen wollen.

Die besondere Kennzeichnung vom Sicherheitseinbehalt ist erforderlich, weil dieser im Rechnungsausgangsbuch in einem speziellen Feld gespeichert wird. Nur so ist es möglich, diesen später bei der Zahlung zu zeigen.

Durch die Festlegung der Rechenbasis ist es möglich, einige Positionen hintereinander auf die gleiche Ursprungssumme zu beziehen.

Beispiel: Rechnungssumme 100.000 €

2% Baustrom 2.000 €

1% Versicherung (auf Rg.Summe) 1.000 €

Beispiel: Rechnungssumme 100.000 €

2% Baustrom 2.000 €

1% Versicherung (auf Restsumme) 980 €

Bei dem letzten Beispiel ist der Sinn einer Zwischensumme sichtbar. Weil die Rechenbasis wechselt, ist es leichter nachvollziehbar, wenn eine Zwischensumme gedruckt wird.

Bei dem Buchungskonto handelt es sich um den Vorschlag, auf welches Konto die Ausbuchung in der Fibu gebucht werden soll.

Gerechnet werden kann auf Basis der „gerechneten Restsumme“ oder der Rechnungssumme.

Erfassen der Abzüge:

Gehen Sie in Projektdatenblatt und wählen den Knopf ‚Abzüge/Nachlass‘ an.

Nach Wahl der vorher angelegten „Nachlassvereinbarung“ können ggf. noch Werte für das Projekt angepasst werden.

[Bild]

Eine Rechnung sieht dann sinngemäß so aus:

|

Pos 1

|

|

Pos 2

|

|

Pos ….

|

|

Summe der Positionen Netto

|

100.000,00 €

|

Nettoabzug 1 2%

|

- 2.000,00 €

|

Nettoabzug 2 1%

|

..- 1.000,00 €

|

Summe Netto

|

97.000,00 €

|

+ MwSt

|

18.430,00 €

|

Brutto incl. MwSt

|

115.430,00 €

Abzugsblock bei kumulierten Teil- und Abschlagsrechnungen

…..

|

Bruttoabzüge

|

|

Brutto incl. MwSt

|

115.430,00 €

|

Bruttoabzug 1 mit 2%

|

..- 2.308,60 €

|

Brutto Zahlsumme

|

113.121,40 €

Zahlungsblock mit bisherigen Zahlungseingängen

……

Rest zu Zahlen : …………,.. €

Hinweis: Beim Wechseln der Vorlagen im Modul Einstellungen werden die hinterlegten Einträge nicht angezeigt. Man muss erst auf die richtige Abzugsart wechseln. (Focus ist auf „Nettoabzug“ gesetzt)

Gilt auch für die Anzeige der Einträge in der Projektverwaltung.

Im Datenblatt des Projektes kann man keine andere Vorlage mehr wählen, wenn die 1. Vorlage bereits als Vorlage übernommen wurde.

Wenn im Datenblatt des Projektes die Vorlage nochmals ausgewählt wird, werden die Einträge dupliziert.
