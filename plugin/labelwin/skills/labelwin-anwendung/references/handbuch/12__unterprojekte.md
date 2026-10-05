# 12. Unterprojekte

Pfad: Projektverwaltung > Projektverwaltung [2] > 12. Unterprojekte
Quelle: handbuch/12__unterprojekte.htm

|

12. Unterprojekte

In der Vergangenheit gab es häufiger den Wunsch, die Vorgänge eines Großauftrages in einem Projekt zusammenzuhalten. Das war aber nicht möglich, da man wegen mehrerer Schlussrechnungen getrennte Projekte anlegen musste. Problematisch war dann auch, dass man nicht aufteilbare Kosten wie z.B. Einrichtungsarbeiten, diverse Materialbestellungen usw. aufteilen musste. Diese Kosten können nun einfach auf das ‚Hauptprojekt’ gebucht werden und alle eindeutig zuzuordnenden Kosten auf die Unterprojekte. Die Auswertung kann nun gemeinsam oder auch getrennt für jedes Unterprojekt erfolgen.

Bei der Darstellung im Labelwin stehen die Haupt- und Unterprojekte auf der gleichen Ebene. Ein Unterprojekt kann also exakt genauso benutzt werden, wie ein Hauptprojekt. Der Unterschied ist nur, dass bei dem Unterprojekt ein Hinweis auf das Hauptprojekt hinterlegt ist und das Hauptprojekt feststellen kann, welche Unterprojekte zu ihm gehört. Die Bündelung, oder vielleicht sollte man von der Zusammenfassung der Daten sprechen, findet nur in der Auswertung und ggf. einer gemeinsamen Endrechnung statt. Im Folgenden bezeichnen wir die Zusammenfassung aller Daten als ‚Gesamtprojekt’, obwohl es dieses in den abgespeicherten Daten nicht gibt, sondern die Werte jeweils aktuell addiert werden.

Um die Möglichkeiten deutlicher zu machen, wollen wir bei den folgenden zwei Beispielen davon ausgehen, dass Sie getrennte Aufträge für Heizung und Sanitär einer Baustelle erhalten haben. Es werden also zwei Endrechnungen geschrieben, die nach der Labelwin-Logik in getrennten Projekten liegen müssen.

Beispiel 1

|

02-123 = Hauptprojekt: Hier werden nur solche Kosten gebucht, die nicht auf die Bereiche Heizung und Sanitär auszuteilen sind oder bei denen Sie sich die Arbeit der Aufteilung nicht machen wollen.

02-123/1 = Unterprojekt Heizung: Bestellungen, Kosten, Abschläge, Zeitbuchungen usw. für den Heizungsbereich. Die Endrechnung Heizung wird hier geschrieben.

02/123/2 = Unterprojekt Sanitär: Alle Kosten und Buchungen für den Sanitärbereich. Die Endrechnung Sanitär wird hier geschrieben.

Die Auswertung kann einzeln und für ein simuliertes ‚Gesamtprojekt’ durchgeführt werden.

Bei dem Gesamtprojekt werden die Kosten und Erlöse aller drei Projekte zusammen gezählt.

Beispiel 2

|

02-123 = Projekt Heizung wird als Hauptprojekt betrachtet. Hier werden auch solche Kosten gebucht, die nicht auf die Bereiche Heizung und Sanitär aufzuteilen sind oder bei denen Sie sich die Arbeit der Aufteilung nicht machen wollen.

Bei der Endrechnung erfolgt die Frage, ob die Abschläge aller Unterprojekte einbezogen werden sollen. Die Frage muss mit NEIN beantwortet werden.

02-123/1 = Unterprojekt Sanitär: Bestellungen, Kosten, Abschläge, Zeitbuchungen usw. für den Sanitärbereich. Die Endrechnung Sanitär muss hier geschrieben werden.

Die Auswertung kann wieder einzeln und für das simulierte ‚Gesamtprojekt’ erfolgen. Sollten auf das Hauptprojekt Heizung allgemeine Kosten gebucht sein, verfälscht das die Auswertung des Heizungs-bereiches. Die Auswertung des fiktiven ‚Gesamtprojektes’ liefert die gleichen Ergebnisse wie im Beispiel 1.

Beispiel 3

|

02-123 = Hauptprojekt Bauträger: Alle Kosten, die über den Pauschalauftrag entstehen, werden hier erfasst. Bei der Endrechnung erfolgt die Frage, ob die Abschläge aller Unterprojekte einbezogen werden sollen. Die Frage muss mit NEIN beantwortet werden.

02-123/1 = Unterprojekt Wohnung 1: Bestellungen, Kosten, Abschläge, Zeitbuchungen usw. für die Wohnungsbesitzer werden hier geschrieben. Die Abwicklung mit Abschlägen und Endrechnung ist möglich.

02-123/2 = Unterprojekt Wohnung 2

02-123/3 = Unterprojekt Wohnung 3

....

Die Auswertung kann wieder einzeln und für das simulierte ‚Gesamtprojekt’ erfolgen.

Wenn der Bauträger die Bereiche Heizung und Sanitär getrennt abgerechnet haben will, muss man das Hauptprojekt leer lassen und die Unterprojekte Heizung-Bauträger und Sanitär-Bauträger anlegen.

|

Eine Auswertung nur für den Bauträger ist dann nur über die globale Projektstatistik mit Eingrenzung auf die Bauträgeradresse und dem Projektnummernanfang 02-123* möglich.

Anlegen eines Unterprojektes

Bei der Anlage eines Unterprojektes wird das Datenblatt des gerade aktiven Projektes kopiert und bei der Projektnummer ein „/1“ oder beim zweiten Projekt ein „/2“. angehängt. Es handelt sich hier nur um Vorschläge der neuen Projektnummer, die Sie ggf. ändern können. Wenn Sie zum Beispiel häufig nur im Bereich Heizung und Sanitär unterscheiden, so können Sie auch einfach ein H oder S anhängen. Damit Sie das Unterprojekt auch an der Oberfläche sofort als solches erkennen, sollten Sie unbedingt die Projektbezeichnung anpassen. Auch die Hinterlegten Rechnungsadressen sollten Sie ggf. ändern.

[Bild]

Sobald Sie das erste Unterprojekt ange-legt haben, können Sie in der Hauptmaske über eine Combobox sehr schnell zwischen dem Haupt- und Unterprojekt wechseln.

Kosten buchen Unterprojekt / Hauptprojekt

Behandeln Sie die Unterprojekte wie ein normales Projekt und buchen Sie die Kosten, Arbeitszeiten usw. auf das richtige Projekt.

Endrechnung

Schreiben Sie die Endrechnung wie gewohnt in dem Projekt, in dem sie abgelegt werden soll. Wenn diese in dem Hauptprojekt liegt, erfolgt unmittelbar vor der Druckausgabe die Frage, ob die Abschläge und Teilrechnungen der Unterprojekte einbezogen werden sollen. Hier müssen Sie je nach Situation entscheiden.

Auswerten 1 , lokale Projektauswertung

Wenn Sie die Auswertung in einem aktiven Unterprojekt anwählen, so erfolgt die Analyse nur für dieses Projekt.

Wenn Sie ein Hauptprojekt aktiv haben, so wird standardmäßig das ‚Gesamtprojekt’ ausgewertet und an der Oberfläche gezeigt. Es werden also die Werte des Hauptprojektes und aller Unterprojekte zusammengezählt. Über einen Schalter können Sie erreichen, dass Sie nur die Werte des Hauptprojektes anzeigen.

[Bild]

Wenn der Schalter gesetzt ist, so werden Sie nach Betätigen des Drucken-Knopfes gefragt, ob Sie nur das Gesamtprojekt drucken möchten oder die detaillierte Ausgabe des Hauptprojektes und der Unterprojekte wünschen. Mit den ‚alten’ Formularen wird wie bisher nur die Analyse eines Projektes gezeigt, das je nach Wahl nur die Werte des Hauptprojektes oder des Gesamtprojektes enthält.

Mit neuen Formularen wie z.B. sygesamt.rpt oder sygesamtQ.rpt (für Querdruck) werden die Werte aller Unterprojekte und des Hauptprojektes aufgelistet. Da die Zusammenfassung, die ja quasi die Werte des Gesamtprojektes darstellen, nun vom Formularprogramm Crystal-Report gerechnet wird, können geringe Rundungsdifferenzen gegenüber dem Gesamtprojekt in der Oberfläche auftreten.

Auswerten 2 , globale Projektauswertung

Wie schon immer muss hier zunächst die Auswertungstabelle erstellt werden. Wählen Sie dazu den Menüpunkt <Projekt> <Globale Auswertung> <Projektauswertung> an.

Ähnlich wie in der lokalen Projektstatistik kann hier beim Drucken über ein zu aktivierendes Feld festgelegt werden, ob bei der Ausgabe von Projekten mit Unterprojekten nur das Gesamtprojekt oder alle Details, also das Hauptprojekt und die Unterprojekte, ausgegeben werden sollen.

[Bild]

Ansonsten läuft die Auswertung unverändert.
