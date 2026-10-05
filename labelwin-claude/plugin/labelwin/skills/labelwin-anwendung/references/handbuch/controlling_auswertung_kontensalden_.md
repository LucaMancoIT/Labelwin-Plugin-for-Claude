# Controlling-Auswertung Kontensalden

Pfad: Auswertungen / Controlling > Controlling [Modul] > Controlling-Auswertung Kontensalden
Quelle: handbuch/controlling_auswertung_kontensalden_.htm

|

Controlling-Auswertung Kontensalden

Stand 18.04.2009

Der hier beschriebene Programmbereich ist Bestandteil des Moduls ‚Controlling’ und steht nur dem Anwender zur Verfügung, der dies erworben hat.

Schon lange kann mit im Labelwin mit Konten arbeiten. Dabei ging es bisher ausschließlich darum, die Daten aus dem Rechnungsausgang, dem Rechnungseingang, der Fibuerfassung und des Kassenbuches mit der entsprechenden Gliederung nach Konten an die Finanzbuchhaltung zu übergeben. Zwar konnten die Daten auch im Labelwin in den jeweiligen Modulen nach Konten eingegrenzt oder mit der Kontenzuordnung gedruckt werden, aber ein Überblick über alle Konten, unabhängig von den Modulen, war bisher nicht möglich.

Mit der Schaffung einer Excel-Auswertung ‚BWA’ (siehe Handbuch Kapitel BWA mit Vorjahresvergleich) tauchte das Problem auf, dass dort die Summen von Konten gebündelt dargestellt werden, aber das Ergebnis nicht oder nur schwer nachprüfbar ist. In der Label-BWA werden die Summen von Konten als Bilanzgruppe dargestellt. Da zu einer Bilanzgruppe beliebig viele Konten gehören können, die Kontenänderungen aber in allen oben aufgezählten Modulen passieren können und dort mal negativ und mal positive erscheinen, ist eine Summe aller dieser Daten nicht nachvollziehbar. Was ist denn die Ursache, wenn in der Bilanzgruppe Kosten von einem Monat zum nächsten große Unterschiede auftauchen? Die Ursache ist mit den hier beschriebenen Funktionen relativ leicht zu finden!

|

Wichtig: Da in diesem Modul alle wichtigen Zahlen des Betriebes offen gelegt werden, sollten die Betriebe unbedingt über die Aktivierung der Rechteverwaltung nachdenken.

Erzeugung der Übersichtsdaten

Bevor die Kontensummen und deren Details betrachtet werden können, müssen die Daten in einem Durchlauf zusammengestellt werden.

Der Durchlauf wird im Moment im Modul ‚Selektieren’ unter den Menüpunkten <Controlling>, <Kontensalden erzeugen> gestartet. Später wird er mit in den Bereich geschoben, in dem alle anderen Auswertungen wie Projektübersicht, Kundendienstauswertung usw. stehen.

[Bild]

Die Übersichtsdaten werden für jeden Monat, jede Verwendungsart (Rg-ausgang, Rg-Eingang, Fibuerfassung usw.), ggf. jede Abteilung und Kostenstelle erzeugt. Wenn Sie einen Daten für einen Zeitraum erzeugen, der bereits einmal erzeugt wurde, werden diese Daten überschrieben. Die erzeugten Werte bleiben dauerhaft gespeichert.

Die Ankreuzfelder ‚je Abteilung’ und je Kostenstelle sind nur sichtbar, wenn bei Ihnen Abteilungen und Kostenstellen aktiv sind. Da es Kunden gibt, die zwar welche eingerichtet haben, aber nicht ernsthaft damit umgehen, kann man die Aufsplittung wegschalten.

Bedienung / Datenanzeige

Die Kontensalden werden angezeigt im Modul Selektieren unter den Menüpunkten <Controlling>, <Kontensalden>.

[Bild]

In dem linken Block können Sie Eingrenzungen treffen, um nicht alle Daten zu zeigen. Die wichtigste Eingrenzung ist sicherlich die Anzeige eines einzelnen Kontos oder einer Bilanzgruppe.

Summen von mehreren Zeilen anzeigen: Sobald Sie mit gedrückter STRG-Taste in das linke Feld der Tabelle klicken, können Sie beliebig viele Einträge markieren

[Bild]

Drucken : Statt eine Druckausgabe zu organisieren haben wir eine Ausgabe an Excel programmiert. Dort können Sie die Daten beliebig aufbereiten und dann drucken.

Detailansichten

Mit den Knöpfen am rechten Rand können Sie die der Kontensumme zugrunde liegenden Quelldaten betrachten. Die 4 Knöpfe stellen die möglichen Datenquellen dar. Der Knopf ‚Fibuerfassung’ ist erst anwählbar, wenn Sie die Aufsplittung nach Datenquelle aktiviert haben. Dies hängt damit zusammen, dass ein Konto in der Fibuerfassung an 4 verschiedenen Stellen verwendet werden kann: als Konto1, als Gegenkonto, als Skonto-Konto und als Ausbuchungskonto.

Wenn Sie eine Zeile in der Tabelle markiert haben (was fast immer der Fall ist), können Sie durch Druck auf einen der Knöpfe auf der rechten Seite die Details der Kontosumme sehen. Das klappt am Besten, wenn Sie die Ansicht auf die Anzeige der Datenquelle geschaltet haben, da man dann sehen kann, mit welchem Knopf Daten sichtbar werden.

[Bild]

Wenn die Dokumente in Elo gescannt worden sind, können Sie sich ggf. auch die Rechnung im Original betrachten.
