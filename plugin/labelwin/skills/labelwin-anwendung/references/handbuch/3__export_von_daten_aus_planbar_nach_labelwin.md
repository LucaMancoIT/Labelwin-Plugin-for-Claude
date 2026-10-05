# 3. Export von Daten aus planbar nach Labelwin

Pfad: Schnittstellen > planbar (Syntax) - Schnittstelle > 3. Export von Daten aus planbar nach Labelwin
Quelle: handbuch/3__export_von_daten_aus_planbar_nach_labelwin.htm

|

3. Export von Daten aus planbar nach Labelwin

3.1 Bereitstellung der Daten im plan bar

Die im plan bar berechnete Lohneinkaufswerte jedes einzelnen Mitarbeiters und der Durchschnittswert werden für die Kalkulation von Angeboten, Rechnungen usw. an das Labelwin-Programm als Selbstkostensatz übergeben, außerdem der aktuelle Grundlohn/Stundenlohn. Die Daten werden in den Personaldaten ergänzt bzw. ausgetauscht und in den allgemeinen Kalkulationseinstellungen übernommen (Selbstkosten).

Den Aufruf der Schnittstelle finden Sie auf der Karteikarte [Bild] des plan bar -Programms unter Import/Export.. Stellen Sie vor dem Import und Export bitte sicher, dass Sie sich im richtigen Jahr befinden.

Wenn der Export aufgerufen wird, wird ein Assistent aktiviert. Zunächst können Sie den Pfad für die Exportdatei bestimmen, der in den Einstellungen hinterlegte Pfad wird dabei vorgeschlagen.

Vollkostenbetrachtung:

Vollkosten umfassen alle Kosten, die im Rahmen der betrieblichen Leistungserstellung entstehen. Bei der Anwendung des sogenannten Vollkostensatzes ist gewährleistet, dass alle Kosten des Betriebes abgedeckt sind. Sie müssen sich nicht mehr fragen, ob ein ausgewiesener Deckungsbeitrag (Deckungsbeitragsrechnung) auch zur Erreichung des geplanten Betriebsergebnisses ausreicht. Vollkostenbetrachtung bedeutet hier, mit einer Null im Feld Deckungsbeitrag sind Sie sicher. Alle Kosten inkl. Gewinnanteil sind abgedeckt. Ein höherer positiver Wert bedeutet einen zusätzlichen Gewinn, negativer Wert einen verminderten Gewinn oder gar Verlust. Es ist auf diese Weise sehr einfach zu beurteilen, ob ein Projekt (oder auch z. B. ein einzelnes Angebot) vollkostendeckend kalkuliert ist.

Alternativ zu den reinen Lohnselbstkosten (Lohneinkauf) pro Mitarbeiter kann für eine Vollkostenbetrachtung Ihrer Projekte im Labelwin auch ein Vollkostensatz mit oder ohne Bewertung aus dem plan bar übergeben werden. Dafür muss Ihr Labelwin-Programm vorab auf Vollkostenbetrachtung umgestellt werden. Bitte besprechen Sie Einzelheiten dazu mit Ihrem Labelwin-Partner.

Keine Vollkostenübernahme

Klicken Sie hier, wenn Sie keine Vollkostenbetrachtung wünschen. Der Lohneinkauf Ihrer Mitarbeiter wird als Selbstkosten an Labelwin übergeben.

Vollkostenübernahme ohne Bewertung

Klicken Sie hier, wenn Sie den im planbar ermittelten Vollkostensatz pro Mitarbeiter als Kalkulationsgrundlage an Labelwin übergeben wollen.

Vollkostenübernahme mit Bewertung

Klicken Sie hier, wenn Sie das Seminar „Ermittlung der Lohnselbstkosten und Arbeiten mit Vollkosten“ besucht und sich im Labelwin für die Vollkostenbetrachtung mit Bewertung entschieden haben. Es wird eine Liste mit allen Mitarbeitern, die im plan bar Produktivstunden haben, mit folgenden Daten angezeigt.

[Bild]

Stundenlohn

Hier wird der durchschnittliche Stundenlohn des Mitarbeiters angegeben.

Produktivstunden

Hier werden die Produktivstunden des Mitarbeiters angezeigt.

Pers. Beurteilung

Bei jedem Mitarbeiter können Sie einen Faktor einsetzen. Damit beeinflussen Sie die Aufteilung der Vollkosten unter den einzelnen Mitarbeitern. Wenn Sie den Faktor höher setzen, so bekommt dieser Mitarbeiter einen höheren Deckungsanteil zugeschoben, den er zu erwirtschaften hat. Im Gegenzug wird bei der Senkung des Faktors bei einem Mitarbeiter dessen Deckungsanteil gesenkt und - da die Kosten ja nun mal gedeckt werden müssen - die Deckungsanteile bei den anderen Mitarbeitern erhöht.

Die Werte für die persönlichen Beurteilungen stehen zunächst auf einen Wert von 1,0. Sie können aber individuell geändert werden. Über den Button [Bild] kann man die Beurteilungen wieder auf 1,0 setzen.

Gesamt

Das ist die Summe des Stundenlohns multipliziert mit den Produktivstunden und der Beurteilung. Aus dieser Gesamtsumme ergibt sich dann der persönliche Verteilungsschlüssel des Mitarbeiters.

Schlüssel

Dieser Schlüssel ist ein Prozentsatz, der berechnet wird. Zur Berechnung werden die unter Gesamt angezeigten Werte für alle Mitarbeiter addiert. Der Schlüssel des Mitarbeiters gibt dann an, wie viel Prozent der Gesamtsumme sein eigener Wert entspricht. Dieser prozentuale Anteil muss dann von diesem Mitarbeiter an Fixkosten erwirtschaftet werden. Dieser Schlüssel beinhaltet also eine Bewertung des Mitarbeiters. Grundlage dafür ist die Annahme, dass ein Mitarbeiter, der durch seinen Stundenlohn hohe Kosten verursacht, auch mehr DB erwirtschaften muss. Gleiches gilt für die Produktivstunden.

Fixkosten

Die gesamten Fixkosten aus planbar werden ermittelt. Diese Kosten werden nun anhand der Schlüssel auf die einzelnen Mitarbeiter verteilt. Die Kosten, die der Mitarbeiter erwirtschaften muss, werden hier angezeigt.

Über [Bild] werden aufgrund der neu berechneten Schlüssel die Fixkosten neu auf die Mitarbeiter verteilt und der benötigte Deckungsbeitrag berechnet

benötigter DB

Die Fixkosten des Mitarbeiters werden durch die Produktivstunden des Mitarbeiters geteilt. Daraus ergibt sich der benötigte DB pro Produktivstunde. Dieser Betrag muss pro Produktivstunde zusätzlich zu den Lohn- und Lohnnebenkosten erwirtschaftet werden.

Als Vollkostensatz wird übergeben: Lohneinkauf + benötigter DB

Export-Datei:

Zum Schluss wird die Exportdatei generiert und kann dann im Labelwin eingelesen werden.

3.2 Einspielung der Daten aus plan bar in Labelwin

Den Import der Daten finden Sie im Labelwin-Modul Einstellungen unter dem Menüpunkt Programmbereiche – Personal – Export / Import plan bar :

Es werden aus dem plan bar -Programm für alle Mitarbeiter der aktuelle Grundlohn, die Selbstkosten (Lohneinkauf) und ggf. auch die Vollkostensätze übergeben und in die Personaldaten übernommen. Außerdem wird der durchschnittliche Selbstkosten- bzw. Vollkostenpreis in die Kalkulationsgruppen übergeben.

[Bild]

Importdatei

Wenn sich beide Programme auf einem Rechner befinden lautet der Standardpfad zum Beispiel so:

C:\Benutzer\“Benutzername“\Eigene Dateien\planbar 2 Dateien\Labelwin Austausch\Import\

Dabei ist der „Benutzername“ der Anmeldename des Benutzers auf dem Rechner

Das plan bar benutzt diesen Pfad automatisch. Wenn sich beide Programme nicht auf dem gleichen Rechner befinden, kann man das Verzeichnis beliebig wählen. Die Datei heißt Kalkuel2imp.xml.

Die Übernahme der Selbstkosten an die Kalkulationsgruppen können Sie mit einer entsprechenden Abfrage verhindern. Dann müssen Sie den Wert per Hand in die Gruppen eintragen, die diesen Wert bekommen sollen.
