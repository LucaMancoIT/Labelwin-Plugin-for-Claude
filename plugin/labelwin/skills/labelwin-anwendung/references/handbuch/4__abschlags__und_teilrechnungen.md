# 4. Abschlags- und Teilrechnungen

Pfad: Buchhaltung > Rechnungsausgangsbuch [7] > 4. Abschlags- und Teilrechnungen
Quelle: handbuch/4__abschlags__und_teilrechnungen.htm

|

4. Abschlags- und Teilrechnungen

Verfahrenshinweis für Abschlags- und Teilrechnungen

Um mit dem Programm bei der Erstellung von Endrechnungen automatisch gezahlte Abschläge oder Teilrechnungen berücksichtigen zu können, müssen bestimmte Regeln eingehalten werden.

-

Projekte:

Für den Bereich muss ein eigenes Projekt eingerichtet sein. Je Projekt kann nur eine Endrechnung erstellt werden, von der automatisch alle Abschläge oder Teilrechnungen abgezogen werden. Aus diesem Grunde sind Sammelprojekte ungeeignet, da in diesen verschiedene Kundenrechnungen auftreten können. Weitere "normale" Rechnungen wie z.B. Regierechnungen haben keinen Einfluss, da nur Abschlags- und Teilrechnungen abgezogen werden.

-

Kundendienst:

Obwohl es sicherlich nur selten vorkommt, kann auch bei einem Kundendienst-Auftrag mit Abschlägen und Endrechnungen gearbeitet werden. Allerdings müssen dann unbedingt alle Rechnungen über die Auftragsmaske geschrieben werden. Wenn Sie z.B. eine Endrechnung in einem Kunden-Projekt über die Projektverwaltung schreiben würden, würden alle im Projektordner liegenden Abschläge abgezogen. Um dort eine Sicherung zu aktivieren, sollten Sie bei den KD-Sammelprojekten im Datenblatt den Punkt ‚Kundendienstprojekt’ ankreuzen

-

Bereits bei der Erstellung der Abschlags- und Teilrechnungen muss die entsprechende Textart festgelegt werden. Die Textart ist im Nachhinein nicht mehr veränderbar.

-

Damit bei der Endrechnung die richtige Summe abgezogen wird, müssen Sie die Zahlungseingänge der Abschläge und Teilrechnungen entsprechend verbuchen.

Wir wollen im Folgenden einmal ein Projekt mit Abschlägen durchspielen. Die dabei auftretenden Randprobleme werden wir nebenher erklären. Richten Sie speziell für diesen Auftrag ein Projekt ein. Dies geschieht unter dem Menüpunkt ‚Projekt’, ‚Neues Projekt’. Falls Sie die Angebote zunächst in einem Sammelprojekt anlegen, so können Sie das Angebot bei Auftragserhalt auch in ein neues Projekt überführen. Legen Sie dazu zunächst das Projekt an und markieren dann im Sammelprojekt das entsprechende Angebot. Wählen Sie im Menü den Punkt ‚Start’, ‚Verschieben - in anderes Projekt’ an. Nun erscheint die Projektauswahlmaske und Sie können das neue Projekt anwählen. Nach der Bestätigung findet sich das Angebot in dem neuen Projekt und ist aus dem Sammelprojekt verschwunden. Dieses Verfahren ist übrigens mit allen Dokumenten möglich, wir empfehlen jedoch möglichst früh ein eigenes Projekt für den Vorgang anzulegen.

Mit dem neu erzeugten Projekt können Sie wie gewohnt arbeiten. Wenn Sie nun eine Abschlags- oder Teilrechnung erstellen möchten, so geschieht dies in dem Sie in dem Programmbereich Projekt einen neues Dokument beginnen. Wählen Sie als Art Abschlags- oder Teilrechnung an. Bei den nun erscheinenden Wahlfeldern mit ‚Kumulierend‘, ‚Versteuerung‘ und Teilleistung‘ ist es extrem wichtig, sie richtig einzustellen. In der Regel sind die Vorgaben passend. Die Vorgaben kommen aus dem Projektdatenblatt und das widerum erhält die Vorgaben aus dem Einstellmodul > EINSTELLUNGEN - Projektverwaltung - Grundeinstellungen / Zusatzfelder.

Unterschied Abschlagsrechnung - Teilrechnung:

1. Abschlagsrechnung: Bei der Abschlagsrechnung bzw. Abschlagsanforderung handelt es sich entweder um eine Pauschalrechnung oder um eine detaillierte Rechnung mit Auslistung einzelner Positionen. Im Fall einer Pauschalrechnung werden die abzurechnenden Artikel nicht im Detail aufgelistet. In diesem Fall greift das Programm auf einen Mustertext zu, der über das Programm EINSTELLUNGEN unter [Vorlagen - Abschlagsrechnungen] an Ihre Bedürfnisse angepasst werden kann. Im anderen Fall kann die Rechnung wie eine normale Rechnung mit einzelnen Positionen erfasst werden.

2. Teilrechnung: Genau wie bei einer normalen Rechnung handelt es sich um eine Auflistung der einzelnen abzurechnenden Positionen. Eine Teilrechnung entsteht häufig auf der Basis eines Aufmaßes. Gegebenenfalls wird jedoch auch das Angebot oder die Auftragsbestätigung als Vorlage herangezogen. Bei der Erstellung einer zweiten Teilrechnung zieht das Programm automatisch die Summe der ersten Teilrechnung ab. Die zweite Teilrechnung enthält also alle Artikel der ersten Teilrechnung und die neu hinzugekommenen.

Besonderheiten der Abschlagsrechnung

|

[Bild]

|

Die nebenstehenden Entscheidungsfelder erscheinen, wenn nach der Wahl der Dokumentenart ‚Abschlagsrechnung‘ das Feld mit ENTER verlassen wird.

Das Feld ‚kumulierend‘ entscheidet darüber, ob die Summen vorher gestellter Abschlagsrechnungen abgezogen werden oder nicht.

In der Regel werden Abschlagsrechnungen nicht kumulierend gestellt, sondern jede enthält den zu zahlenden Betrag.

Bei der Versteuerung ist in der Regel die Soll-Versteuerung richtig. Die Gesetzgebung lässt eine ‚Ist-Versteuerung’ nur dann zu, wenn damit keine spezifizierte Leistung abgerechnet wird – was im Grunde genommen nur bei Vorauszahlungen der Fall ist. Bei einer Ist-Versteuerung eines Abschlages wird bei der folgenden Teil- oder Schlussrechnung nur der Betrag abgezogen, der als Zahlungseingang gebucht wurde.

Beispiel:

Ist-Versteuerter Abschlag 1000,00 €, Zahlungseingang 500,00 €, Schlussrechnung 5000,00 € --> unter der Schlussrechnung steht sinngemäß

„Abschlag vom ...... über 500,00 € , zu zahlen 4500,00€“

Die steuerpflichtige Summe für den Kunden beträgt bei dem Abschlag 500,00 € und bei der Schlussrechnung 4500,- €

Das gleiche Beispiel mit einer Soll-Versteuerung ergibt einen Schlusstext mit

„Abschlag vom .... 1000,00 €, gezahlt 500,00 €, zu zahlen 4500,00 €“

Die steuerpflichtige Summe für den Kunden beträgt jetzt bei dem Abschlag 1000,00 € und bei der Schlussrechnung 4000,00 €

Druckausgabe: die normalen, nicht kumulierenden Abschläge werden mit dem normalen Rechnungsformular Rg3 gedruckt.

Besonderheiten der Teilrechnung

|

[Bild]

|

Die nebenstehenden Entscheidungsfelder erscheinen, wenn nach der Wahl der Dokumentenart ‚Teilrechnung‘ das Feld mit ENTER verlassen wird.

Das Feld ‚kumulierend‘ entscheidet darüber, ob die Summen vorher gestellter Teilrechnungen abgezogen werden oder nicht.

In der Regel werden Teilrechnungen kumulierend gestellt, das heißt bei der 2. Teilrechnung werden alle Artikel (auch die von der 1. Teilrechnung) eingetragen und die Summe der 1. Teilrechnung abgezogen.

Bei einer abgeschlossenen Teilleistung werden die Summen dieser Rechnung erst bei der Endrechnung wieder abgezogen. Eine nachfolgende Teilrechnung beginnt mit Summe Null (also ohne Abzug) und darf auch nicht die Artikel der Rechnung mit „Teilleistung JA“ enthalten. Durch diesen Schalter wird das System mit den Abzügen der vorherigen Rechnung ausgesetzt. Eine solche Rechnung wird auch als Teilschlussrechnung bezeichnet, (also die Schlussrechnung eines in sich abgeschlossenen Bereiches). Über diesen Weg kann z.B. erreicht werden, dass bei einem Auftrag mit der Sanierung von vielen einzelnen Wohnungen jeweils nach der Fertigstellung einer Wohnung die Gewährleistung beginnt. Bitte denken Sie aber daran, dies durch die Wahl der Überschrift (Teilschlussrechnung) oder in der Vorbemerkung für den Kunden deutlich zu machen. Wir haben die Möglichkeit mit der abgeschlossenen Teilleistung auch geschaffen, um bei einem Wechsel der Mehrwertsteuer die fertig gestellten Bereiche mit dem alten Satz abrechnen zu können. Der Gesetzgeber lässt dies nur für abgeschlossene Bereiche zu.

In der Regel ist die Vorgabe mit Teilleistung NEIN die richtige Wahl.

Druckausgabe: die erste Teilrechnung, bei der es noch keine Abzüge gibt, sollte mit dem normalen Rechnungsformular Rg3 oder bei der Verwendung von Titeln mit dem Formular Rg4 gedruckt werden. Alle nachfolgenden Rechnungen müssen den Abzugsblock der vorherigen Rechnungen enthalten und daher genau wie die Schlussrechnung mit dem Formular Rg6 gedruckt werden.

Bearbeiten Sie nun die Abschlagsrechnung oder Teilrechnung wie gewohnt und drucken Sie sie als Rechnung aus. Es ist wichtig, dass die Rechnung in das Rechnungsausgangsbuch eingetragen wird. Nur dann kann sie bei der Endrechnung berücksichtigt werden.

Abschlags- und Teilrechnungen sind im Rechnungsausgangsbuch über die Rechnungsart erkennbar.

Schreiben Sie die Endrechnung, indem Sie bei der Dokumentenanlage die Dokumentenart Endrechnung wählen. Falls Sie in dem Projekt ein dazugehöriges Angebot oder Aufmaß haben, so können Sie bereits bei der Dokumentenanlage die entsprechende Vorlage wählen. Anderenfalls können Sie in der Dokumentenerstellungsmaske über den Menüpunkt ‚Vorlage’ jeden Text eines x-beliebigen Projektes als Vorlage verwenden. Sollten Sie also irrtümlich das Angebot in einem Sammelprojekt abgelegt haben, so können Sie auch darauf wieder zugreifen. Bearbeiten Sie nun wie gewohnt die Endrechnung und drucken Sie sie aus. Das Programm greift bei dem Ausdruck automatisch auf ein Formular zu, bei dem am Ende eine Tabelle mit den bisher eingegangenen Zahlungen ausgedruckt wird (Anmerkung für Insider: Das Formular ist in der report.ini festgelegt und heißt bei der Auslieferung rg6.rpt).

Endrechnung ohne Abschlagsrechnung

Wenn Sie Abschläge erhalten haben, die nicht in unserem Rechnungsausgangsbuch eingetragen sind (z.B. weil sie mit dem vorher eingesetzten Programm geschrieben wurden) und dennoch bei der Endrechnung abgezogen werden sollen, haben Sie 2 Möglichkeiten:

Zum einen die sicherlich sauberste Lösung ist, die Rechnung per Hand in das Rechnungsausgangsbuch einzubuchen. Dies geschieht im Rechnungsausgangsbuch durch Betätigen des Knopfes "Rechnung eintragen". Wählen Sie in dieser Maske das entsprechende Projekt an und die Rechnungsart Teil-Rg. oder Abschlag. Sie können die Rechnung an dieser Stelle auch sofort auf bezahlt setzen. Die Abschlagszahlung wird dann genauso berücksichtigt, als wenn ein Ausdruck erfolgt wäre.

· Tragen Sie die Nettosumme (also ohne Mwst.) als normale Leistungsposition in die Endrechnung ein. Geben Sie bei der Stückzahl oder beim Preis ein Minuszeichen vor, damit die Summe abgezogen wird. Dieses Verfahren hat den Nachteil, dass der Kunde die geleistete Summe inklusiv Mehrwertsteuer nicht automatisch sehen kann. Gegebenenfalls müssen Sie diese in dem Artikeltext erfassen.

· Tragen Sie die Abschlagszahlung in die Nachbemerkung ein. Gegebenenfalls stellen Sie zuvor den Gesamtwert der Endrechnung unter dem Menüpunkt ‚Option’, Kurzauswertung’ fest. Tragen Sie dann Ihre ‚Abrechnung’ in die Nachbemerkung ein und rechnen mit dem Taschenrechner den zu zahlenden Betrag aus. Nach dem Ausdruck der Rechnung sollten Sie dann sofort in das Rechnungsausgangsbuch gehen und die eingegangene Abschlagssumme einbuchen.

Teilrechnung mit Skontoabzug

Wenn Sie Ihren Kunden bei Teil- oder Abschlagszahlungen bereits Skonto anbieten wollen, so müssen Sie dies neben der textuellen Ausweisung im Rechnungsausgangsbuch entsprechend eintragen. Wählen Sie dort bei der Einbuchung den Bereich Teilzahlung mit Skt.- Abzug an. Tragen Sie dort neben der gezahlten Summe den zu berücksichtigenden Skontobetrag ein. Beispiele zu diesem Bereich finden Sie in der Beschreibung des Rechnungsausgangsbuches.

Abschlagsrechnung / Teilrechnung / Endrechnung drucken

Da es hier immer wieder Fehler gab, deren Beseitigung durch die GoBD zusätzlich erschwert wird, haben wir weitere Sicherungen gegen Bedienungsfehler eingebaut.

-

Bei allen diesen Rechnungsarten wird unmittelbar vor der Druckausgabe eine Maske mit allen Abschlags- und Teilrechnungen gezeigt, die abgezogen werden. Das passiert auch bei der ersten Abschlagsrechnung, damit man merkt, dass nichts abgezogen wird. In dieser Maske können Sie sich auch die Artikel und ggf. die Druck-Pdf ansehen. Sie können also alles ordentlich prüfen, bevor ein Fehler viel Aufwand verursacht. In dieser Maske kann man den Druck auch noch abbrechen.

[Bild]

-

Es passierte immer mal wieder, dass jemand eine Abschlagsrechnung im normalen Baustellen-Projekt zu einem dort angelegten Kundendienstauftrag angelegt hat und diese dann bei der Schlussrechnung fehlte.

Eine Kundendienst-Abschlagsrechnung wird daher auch bei nachfolgenden Projektabschlags- oder Schlussrechnung abgezogen.

Beispiel 1:

Abschlag zu KDA 18-1234 im Projekt XYZ

Schlussrechnung zu Projekt XYZ berücksichtigt den Abschlag (und zeigt ihn zuvor an, damit man ggf. Fehler merkt)

Beispiel 2:

Abschlag zu Projekt XYZ

Schlussrechnung zu KDA 18-1234 zieht den Abschlag nicht ab.

Zusammengefasst: Kontrollieren Sie mit der neuen Maske noch einmal die Abzüge und ggf. auch den Zahlstatus – das spart Ihnen Zeit und Nerven.

Abschlags- und Teilrechnungen hochzählen

Über einen Schalter kann festgelegt werden, das Überschriften wie 1.Abschlag, 2. Teilrechnung usw. entstehen. Die Zahl wird je Projekt hochgezählt. Die Nummer wird nirgends gespeichert, sondern unmittelbar vor der Druckausgabe wird die Anzahl der Abschläge mit Rechnungsnummer gezählt. Die Einstellung erfolgt im Modul Einstellungen unter den Menüpunkten <Programmbereiche>, <Druckausgabe>, <Druck-Überschriften>.
