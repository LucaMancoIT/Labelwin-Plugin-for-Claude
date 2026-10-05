# 1. Einrichtungsarbeiten

Pfad: Zeitwirtschaft > Zeitkonto [Modul] > 1. Einrichtungsarbeiten
Quelle: handbuch/1__einrichtungsarbeiten_2.htm

|

1. Einrichtungsarbeiten

Stundenart Zeitkonto

Zusätzlich zu den bei der Zeiterfassung erforderlichen Einstellungen muss eine weitere Stundenart mit der Bezeichnung ‚Zeitkonto’ angelegt werden. Weiter muss ein Projekt angelegt werden, das bei der Zeitbuchung angesprochen wird. Wir empfehlen Ihnen als Projektname ebenfalls ‚Zeitkonto‘ zu verwenden. Da dieses Projekt nie direkt gewählt wird, ist die Projektnummer gleichgültig. Wenn Sie dieses Projekt als Standardprojekt bei der Stundenart hinterlegen, sparen Sie bei der Eingabe Zeit.

Personalerfassung Sollzeiten

Um die Differenz zwischen den geleisteten Stunden und der Sollvorgabe automatisch ermitteln zu können, ist zwingend eine Stundenvorgabe für jeden Monteur erforderlich. Zur erleichterten Erfassung werden die Stundenvorgaben der Firma erfasst und als Vorgabe bei jedem Monteur verwendet.

Die Vorgaben sind im Modul EINSTELLUNGEN unter dem Menüpunkt <Programmbereiche> <Personal> <Arbeitszeiten> zu erfassen.

[Bild]

Anschließend ist für jeden Mitarbeiter in der Personalerfassung die tatsächliche Soll-Vorgabe festzulegen. Die Eingabe findet im Modul EINSTELLUNGEN unter dem Menüpunkt <Programmbereiche> <Personal> <Personal erfassen> 3. Karteikarte ‚Zeiten’ statt. Legen Sie hier fest, ob für den Mitarbeiter die Standardzeiten gelten oder individuelle Zeiten.

[Bild]

Nur bei den Mitarbeitern, bei denen ein Zeitkonto geführt werden soll, ist das Feld ‚mit Tages-/ Monatsvorgaben’ anzukreuzen und die Zeiten zu erfassen.

Mit Hilfe der Vorgaben je Tag ermittelt das Programm im jeweiligen Auswertungszeitraum die gesamten Sollzeiten. Die Summe wird gebildet über die Anzahl der Montage x Montag-Std. + Anzahl der Dienstage x Dienstag-Std. usw. Wenn als ein Mitarbeiter an einem Freitag mit einer vorgegebenen Stundenzahl von 5 Std. frei macht, so wird diese 5 Stunden vom Zeitkonto ausgeglichen. Das bedeutet, obwohl der Mitarbeiter die 5 Stunden nicht gearbeitet hat, bekommt er diese trotzdem bezahlt.

Erfassung des Kontostandes zu Beginn/Eröffnungsbuchung

Da bereits viele Firme vor dem Erfassen mit unserem Programm mit Zeitkonten arbeiten, stellt sich das Problem mit der Buchung des Anfangsbestandes. Wenn dieser auf den aktuellen Monat gebucht würde, würde eine Auswertung dieses Monats unsinnige Werte bringen.

Unsere Lösung sieht so aus, dass der Anfangsbestand über die normale Zeiterfassung auf das Datum 01.01.1980 gebucht wird.

Da über diesen Zeitraum keine Auswertung mehr stattfindet, tauchen hierbei keine Probleme auf. Wenn ein Mitarbeiter ein Guthaben von 20 Stunden hat, so muss die Zeitbuchung mit Minus 20 Stunden auf den 01.01.1980 erfolgen.

[Bild]

Das negative Vorzeichen ist richtig, weil genommene Freizeitstunden positiv eingetragen werden und damit den Bestand verringern. Nach dieser Logik müssen bereits angesparte Stunden mit negativem Vorzeichen erfasst werden.

Beispiel: Der Monteur arbeitet 4 Stunden und nimmt 4 Stunden Freizeit vom Zeitkonto. Beide Werte sind positiv zu buchen, damit der Monteur 8 Stunden bezahlt bekommt.

Am Besten vorzustellen ist es, dass die gebuchte Zeit die Auszahlungssumme erhöht oder senkt und daher das Vorzeichen in Bezug auf den Zeitkontostand gegenteilig ist.
