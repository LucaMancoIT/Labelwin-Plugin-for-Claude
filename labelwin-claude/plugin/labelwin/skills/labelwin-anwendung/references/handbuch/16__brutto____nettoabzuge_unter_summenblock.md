# 16. Brutto- / Nettoabzüge unter Summenblock

Pfad: Projektverwaltung > Projektverwaltung [2] > 16. Brutto- / Nettoabzüge unter Summenblock
Quelle: handbuch/16__brutto____nettoabzuge_unter_summenblock.htm

|

16. Brutto- / Nettoabzüge unter Summenblock

Stand 08.11.2018

(V5.87)

THEMA

|

Es geht um Abzüge, die unter dem Summenblock der Rechnung geschrieben werden sollen. Diese Funktionalität wird insbesondere zum Ausweis eines Sicherheitseinbehaltes (SEB) verwendet.

Bei den Nettoabzügen könnten diese im Grunde genommen auch in den Artikelbereich geschrieben werden, aber das ist halt eine Frage des Geschmacks. Einen Vorteil hat die Darstellung unter dem Summenblock allerdings: Wenn man mit Titeln oder Losen arbeitet, müssen alle Artikel innerhalb von Titeln und Losen stehen. Ggf. muss man also wegen. einem Nettoabzug extra einen neuen Titel und vielleicht sogar ein neues Los einführen.

Nettoabzüge wirken so, als wenn sie im Artikelbereich stehen würden. Sie mindern die Rechnungssumme und auch den MwSt-Betrag.

Bruttoabzüge sind nur ein Angebot, die Zahlsumme zu mindern. Im Grunde genommen werden dabei nur Abzüge angeboten, die der Auftraggeber ohnehin abgezogen hätte. Das können bei Teil- und Abschlagsrechnungen Dinge wie anteilige Kosten für Baustrom, Versicherung und auch Sicherheitseinbehalt sein. Die im Rechnungsausgangsbuch eingetragenen Summen werden durch Bruttoabzüge nicht verändert. Für die Endrechnung kommt damit nur noch der Sicherheitseinbehalt als Bruttoabzug in Frage. Baustrom, Versicherung usw. müssen bei der Endrechnung entweder als Nettoabzug dargestellt werden oder man muss sie richtigerweise über eine Eingangsrechnung abrechnen.

Die Abzüge können nicht bei jeder Rechnung individuell festgelegt werden, sondern müssen für das ganze Projekt erfasst werden. Sie greifen dann natürlich nur für nachfolgend erfasste Rechnungen.

VORAUSSETZUNGEN

|

-

Der Schalter prnachlass=1 muss in der global.ini unter [GRUNDEINSTELLUNGEN] gesetzt werden

-

Es müssen speziell angepasste Druckformulare verwendet werden.

(Sollte Ihr Rechnungsformular nicht mit Brutto-/Nettoabzügen umgehen können, meldet das Programm dies beim Druckversuch. Wenden Sie sich in diesem Fall an Ihren Label-Partner oder die Hotline.)

EINRICHTUNG

Es ist möglich, im Einstellmodul unter [Programmbereiche - Projektverwaltung - Abzüge/Nachlass] Vorlagen für Abzüge zu erstellen. Dieses ist sinnvoll, wenn Sie häufig mit identischen Abzügen arbeiten.

Wenn Sie eine Vorlage erfasst haben, erscheint beim Aufruf der Abzüge im Datenblatt ein Auswahlmenü und Sie können die passende Vorlage auswählen Haben Sie keine Vorlage angelegt, landen Sie durch den Klick auf den Button "Abzüge / Nachlass" sofort in der Erfassmaske.

[Bild: 16. Brutto- / Nettoabzüge unter Summenblock]

Bild: Nachlassvereinbarungen erfassen

|

Hinweis: Beim Öffnen oder Wechseln der Vorlagen werden die hinterlegten Einträge nicht unbedingt direkt angezeigt. Man muss erst auf die richtige Abzugsart wechseln. Der Fokus ist standardmäßig auf „Nettoabzüge“ gesetzt, und somit wären bereits erfasste Brutto-Abzüge nicht direkt sichtbar. Dieser Umstand gilt auch für die Anzeige der Abzüge/Nachlässe im Projektdatenblatt.

|
[Bild: 1]

Neu (F2)

[Bild: 1. Neu (F2)]

Über den Button "Neu (F2)" legen Sie dann einen neuen Abzug / Nachlass an.

|
[Bild: 2]

Abzugsart

[Bild: 2. Abzugsart]

Zuerst müssen Sie festlegen, ob Sie Netto- oder Brutto-Abzüge erfassen wollen.

|
[Bild: 3]

Abzugstext

[Bild: 3. Abzugstext]

Tragen Sie den gewünschten Text des Abzuges ein (dieser Text erscheint dann auch auf der Rechnug) und füllen die weiteren Abzugsdaten aus.

Tipp: Der Text kann das Schlüsselwort @summe@ enthalten. Dieses wird beim Rechnungsdruck automatisch durch den Rechnungsbetrag ersetzt.

|
[Bild: 4]

Verwendung bei

[Bild: 4. Verwendung bei]

Hier legen Sie fest, ob der Abzug bei Abschlägen/Teilrechnungen oder bei Schlussrechnungen greifen soll. Es ist auch möglich beide Rechnungsarten anzuhaken.

|
[Bild: 5]

Sicherheitseinbehalt

[Bild: 5. Sicherheitseinbehalt]

Die besondere Kennzeichnung als Sicherheitseinbehalt ist erforderlich, weil dieser im Rechnungsausgangsbuch in einem speziellen Feld gespeichert wird, der später bei der Eingabe der Zahlung angezeigt wird.

|
[Bild: 6]

Zwischensumme

[Bild: 6. Zwischensumme]

Wenn Sie hier den Haken setzen, werden alle Abzugsdatenfelder weggeblendet und es wird ein Eintrag "Zwischensumme" erzeugt. Die Wirkung einer Zwischensumme auf einer Rechnung kann man auf dem nachfolgenden Beispiel gut erkennen. Wichtig ist die richtige Reihenfolge der Abzüge/Nachlässe in der Vorlage.

Die Abzüge des obigen Vorlagenbeispiels ergeben den folgenden Ausdruck auf einer Abschlagsrechnung:

[Bild]

|
[Bild: 7]

Reihenfolge

[Bild: 7. Reihenfolge]

Über dieses Feld können Sie festlegen in welcher Reihenfolge die Abzüge erzeugt werden sollen. Hierüber lässt sich auch nachträglich die Reihenfolge der bereits erfassten Abzüge ändern.

|
[Bild: 8]

Prozentsatz

[Bild: 8. Prozentsatz]

Tragen Sie hier den gewünschten Prozentsatz des Nachlasses/Abzuges ein. Durch Erfassung eines positiven Wertes kann auch ein Aufschlag erzeugt werden.

|
[Bild: 9]

Buchungskonto

[Bild: 9. Buchungskonto]

Bei dem Buchungskonto handelt es sich um den Vorschlag, auf welches Konto die Ausbuchung in der Fibu gebucht werden soll.

|
[Bild: 10]

Rechnet auf Basis

[Bild: 10. Rechnet auf Basis]

Gerechnet werden kann auf Basis der „gerechneten Restsumme“ oder der Rechnungssumme. Durch die Festlegung der Rechenbasis ist es möglich, einige Positionen hintereinander auf die gleiche Ursprungssumme zu beziehen. Der Unterschied wird an einem Beispiel deutlich:

Beispiel: Rechnungssumme 100.000 €

2% Baustrom 2.000 €

1% Versicherung (auf Rg.Summe) 1.000 €

Beispiel: Rechnungssumme 100.000 €

2% Baustrom 2.000 €

1% Versicherung (auf Restsumme) 980 €

Hinweis: Bei dem letzten Beispiel ist der Sinn einer Zwischensumme sichtbar. Weil die Rechenbasis wechselt, wäre es leichter nachvollziehbar, wenn eine Zwischensumme gedruckt würde.

ANWENDUNG

1. Erfassen der Abzüge:

Damit ein oder mehrere Butto- /Nettoabzüge bei der Rechnungsschreibung berücksichtigt werden, müssen diese im Datenblatt des Projektes der Rechnung hinterlegt werden.

Gehen Sie in das Projektdatenblatt und wählen den Knopf ‚Abzüge/Nachlass‘ an. Sie werden gefragt, ob eine Vorlage übernommen werden soll. In der Regel sollte das gemacht werden, da ansonsten bei jedem Projekt die Nachlässe neu erfasst werden müssten. Nach der Übernahme einer Vorlage können ggf. noch Werte für das Projekt angepasst werden.

Hinweis: Im Datenblatt des Projektes kann man keine andere Vorlage mehr wählen, wenn die 1. Vorlage bereits als Vorlage übernommen wurde. Wenn im Datenblatt des Projektes die Vorlage nochmals ausgewählt wird, werden die Einträge dupliziert.

2. Rechnung drucken:

Eine Rechnung mit Brutto- /Nettoabzügen sieht beim Druck sinngemäß wie folgt aus:

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

|

Rest zu Zahlen :

|

…………,.. €

3. Erfassen der Zahlung

Wurde eine Rechnung mit einem Sicherheitseinbehalt erzeugt, wird dieser beim Einbuchen der Zahlung angezeigt und bei der vorgeschlagenen Zahlsumme automatisch abgezogen.

a.) Buchung der Zahlung im Rechnungsausgangsbuch:

[Bild]

Bild: Zahlung erfassen im RG-Ausgang

b.) Buchung der Zahlung in der FIBU-ERFASSUNG:

[Bild]

Bild: Zahlung erfassen in der Fibu-Erfassung
