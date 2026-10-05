# 2.7.11 Grundeinstellungen

Pfad: Einrichtungsarbeiten > Einstellungen [14] > 2. Programmbereiche > 2.7 Zeitwirtschaft > 2.7.11 Grundeinstellungen
Quelle: handbuch/2_7_11_grundeinstellungen.htm

|

2.7.11 Grundeinstellungen

Bevor Sie mit der Zeitwirtschaft Zeiten erfassen, sollten Sie unbedingt die Maske an Ihre eigenen Bedürfnisse anpassen. Von dieser Möglichkeit sollten Sie Gebrauch machen, um die voll gestopfte Maske übersichtlicher zu gestalten.

Sichtbare Elemente

|

[Bild] Bild: Sichtbare Elemente

|

In dieser Maske kreuzen Sie an, welche Eingabefelder Sie in der Zeitwirtschaft nutzen wollen. Die Bedeutung der einzelnen Felder werden im Folgenden erklärt.

Sichtbare Elemente: An dieser Stelle möchten wir lediglich noch auf das Feld Anzahl/Stck. eingehen. Es handelt sich um eine Sonderentwicklung für einen Fertigungsbetrieb, der neben der Zeit auch die hergestellte Menge erfassen und auswerten wollte. Da dieser Bereich kaum für einen Kunden interessant sein dürfte, haben wir ihn bei der Beschreibung der Zeiterfassungsmaske weggelassen.

Ok: Durch Betätigen dieses Knopfes werden die Änderungen übernommen und die Maske wird geschlossen.

Abbruch: Durch Betätigen dieses Knopfes wird die Maske geschlossen, vorgenommene Änderungen werden nicht übernommen.

Diverse Einstellungen

|

[Bild]

Bild: Diverse Einstellungen

|

Lohn-Selbstkosten

- aus Personalstammdaten: In der Regel sollten Sie hier ankreuzen, dass die Selbstkosten jeweils beim Monteur hinterlegt werden. Da die Projekte mit diesen Selbstkosten belastet werden, sollten sie möglichst exakt stimmen. Diese Einstellung entspricht dem Standard bei den meisten unserer Kunden.

- aus Grundlohn errechnen: Zur Belastung der Projekte und Kundendienstaufträge arbeitet Labelwin mit Monteur-Selbstkosten. Dieses ist der Stundelohn zzgl. aller lohngebundenen Nebenkosten wie Sozialversicherungen, Urlaubs- und Krankheitskosten, Weihnachtsgeld usw. Dieser Zuschlag wird in der Regel mit Hilfe des Steuerberaters oder Programmen wie planbar (Firma Syntax, Oldenburg) ermittelt und als Multi auf den Grundlohn verwendet.

In Labelwin können Sie statt die Lohnkosten einzutragen auch die Stundenlöhne mit diesem Faktor berechnen. Das spart bei einer Änderung des Faktors den Aufwand, bei allen Mitarbeitern den Selbstkostensatz neu zu berechnen.

In den Personalstammdaten ist das Eingabefeld für die Selbstkosten dann ausgeblendet – dort kann nur noch die Eingabe des Stundenlohns erfolgen.

[Bild]

Statusänderungen Auftrag / Projekt

- bei Kundendienstaufträge mit Status "offen": Wenn Sie diesen Schalter gesetzt haben, wird ein Kundendienstauftrag nach einer Zeitbuchung sofort auf den Status ‚In Arbeit’ gesetzt, wenn er zuvor den Status ‚Offen’ hatte.

- bei Projekten mit Status kleiner als "in Arbeit": Wenn Sie diesen Schalter gesetzt haben, wird ein Projekt nach einer Zeitbuchung sofort auf den Status ‚In Arbeit’ gesetzt, wenn er zuvor einen "kleineren" Status hatte (also Anfrage, Angebot oder Auftrag).

Warnungen /Prüfungen

- erledigte Aufträge: Wenn Sie diese Option setzen, werden Sie bei der Zeitbuchung gewarnt, wenn der bebuchte Auftrag bereits den Status "erledigt" hat.

- bereits berechnet: Wenn diese Option gesetzt wird, werden Sie bei der Zeitbuchung gewarnt, wenn der bebuchte Auftrag bereits den Status "berechnet" hat.

- Hinweis, wenn Buchung je Tag mehr als: Geben Sie hier die max. Stunden ein, die pro Tag gebucht werden können. Sollten dann mehr Stunden gebucht werden, erfolgt eine Warnung.

Bedienung / Handhabung

Maske für Laptop / Tablet-PC verwenden: Aktivieren Sie dieses Feld, wenn Sie mit einem Laptop oder Tablet-PC arbeiten. Die Maske enthält die gleichen Elemente, ist jedoch für die Erfassung auf einem Laptop/Tablet-PC optimiert.

Monteurauswahl bei Personalnr. Eingabe überspringen: Aktivieren Sie dieses Feld, wenn Sie bei der Zeitenbuchung die Personalnr. eingeben möchten. Es wird dann automatisch der richtige Monteur eingetragen.

schneller Mandantenwechsel: Wenn in der Zeiterfassung ein Projekt oder ein Kundendienstauftrag eines anderen Mandanten eingegeben wird, kann das Programm den Mandanten umschalten. Damit dabei keine Fehler entstehen, dürfen sich die Nummern der Aufträge nicht überschneiden. Bei den Projekten besteht diese Gefahr nicht, weil die Nummer immer eindeutig ist.

Kostenstellen aus Personalstamm: Legen Sie hier fest, ob die Kostenstelle aus den Personalstammdaten verwendet werden soll. Dieser Eintrag wird nur benötigt, wenn Sie mit Kostenstellen arbeiten.

Datumsvorgabe aus Termin des KD-Auftrages: Die Zeitbuchung erhält automatisch das Datum des Auftrages.

Zeiteinheiten

|

[Bild]

Bild: Zeiteinheiten

|

Zeiteinheiten:

Es ist möglich, in der Zeiterfassung wahlweise Stunden oder Arbeitseinheiten zu erfassen. Mit einem Schalter kann man festlegen, dass bei Aufträgen das Eingabefeld für AW’s verfügbar ist und bei Projektbuchungen nur Stundeneingaben möglich sind.

Sowohl die Preise als auch die Artikeltexte können für die Übernahme in eine Rechnung unterschiedlich gehalten werden. Schließlich geht es bei der Verwendung von Arbeitseinheiten darum, einen höheren Stundenverrechnungssatz anzusetzen. Dies in der Hoffnung, dass der Kunde den Preis der Aw nicht auf eine Stunde umrechnet.

Bei der Übernahme in eine Rechnung verhält sich das Programm so, dass es den Text und Vk-Preis der AW nimmt, wenn sie erfasst wurden, sind dagegen nur die Stunden erfasst, wird der Text und Vk-Preis der Stunde verwendet. Die Selbstkosten werden bei beiden Erfassmethoden immer aus den Monteurdaten genommen und sind identisch.

Um die Dauer einer AW festzulegen, müssen Sie den Knopf ‚Ändern’ drücken und dann die gewünschte Dauer eingeben. Auch hier führt Sie das Programm, so dass wir auf weitere Erklärungen verzichten. Legen Sie danach fest, ob Sie alles in AW’s, nur die KD-Aufträge in AW’s erfassen möchten

Wichtig: Prozentuale Zulagen

Der Umgang mit prozentualen Zulagen für Überstunden unterscheidet sich jetzt beim Arbeiten mit AW’s und Stunden. Sobald Sie im AW-Feld eine Menge eingetragen haben, wirken die Prozentsätze auf die Preise der AW, sonst wie bisher auf die Stunden.

Das heißt, dass Sie z.B. bei 8 AW’s mit 15 Minuten vielleicht auch 8 Zulagen einbuchen müssen, bei einer Eingabe von 2 Stunden (was ja das gleiche ist) dagegen auch nur 2 Zulagen. Um dieses Problem besonders deutlich zu machen, wird der Beschriftungstext der Zulage auf Gelb geschaltet, damit man darauf aufmerksam wird.

Übergabe / Schnittstellen

|

[Bild]

Bild: Übergabe / Schnittstellen

|

Liefereinheiten bei Übernahme in Rechnung: Tragen Sie hier die Einheit der Liefermenge ein, die bei der Übernahme der Zeiten auf der Kundendienstrechnung erscheinen soll. Haben Sie bereits im Artikeltext das Wort ‚Stunden’ oder ‚Arbeitseinheit’ erfasst, sollten Sie diese Felder leer lassen.

Lohn-Schnittstelle: Hier findet eine Zuordnung einer Lohnart zu den Fahrtkosten und allgemeinen Kosten statt. Diese werden nur für die Übergabe an Lohnprogramme benötigt.

Kostenstellen: Legen Sie hier fest, ob die Kostenstelle aus dem Auftrag oder Projekt verwendet werden soll. Dieser Eintrag wird nur benötigt, wenn Sie mit Kostenstellen arbeiten.

Prüfung / Freigabe

|

[Bild]

Bild: Prüfung / Freigabe

|

Prüfung / Freigabe: In der Zeiterfassung besteht die Möglichkeit mit einem 'Geprüft'-Merkmal zu arbeiten. Damit können einzelne Buchungen so gekennzeichnet werden, dass sie zwar erfasst werden können, aber noch nicht freigegeben sind. Die Prüfung der Zeitbuchungen kann auf zwei Arten erfolgen. Die einfache Variante arbeitet mit einem einfachem Anhakfeld in der Zeiterfassmaske.Es kann aber auch in einer speziell entwickelten großen Maske geprüft werden, in der alle relevanten Daten sichtbar sind. Hier ist z.B. auch die Anzeige des gescannten oder im mobilen Kundendienst entstandenen Auftragsberichtes und der hinterlegten Fotos möglich. Details erfahren Sie unter Zeitbuchungen prüfen.

Vorgabe auf "geprüft" bei der Erfassung: Bei aktivierter Prüfung, kann das "Geprüft"-Merkmal mit "geprüft" vorbelegt werden. So wäre standardmäßig jede Buchung geprüft, abhängig davon in welcher Zeiterfassmaske sie erfasst wurde.

Auf "geprüft" setzen bei der Übernahme aus: Bei aktivierter Prüfung, kann das "Geprüft"-Merkmal bei der Übernahme aus einem anderen Programmteil mit "geprüft" gesetzt werden. Hier sind alle möglichen Schnittstellen aufgeführt, die einzeln ausgewählt werden können.

Aktive Elemete für mobilen Kundendienst

|

[Bild]

Bild: Aktive Elemente für mobilen KD

|

Diese Einstellungen werden nur benötigt, wenn mit der "kleinen" Erfassmaske für den mobilen Kundendienst gearbeitet wird. Alle Details erfahren Sie hinter dem Fragezeichen Knopf.
