# Werte aus Labelwin zur Ermittlung der Monteurkosten

Pfad: Auswertungen / Controlling > Vollkosten > Werte aus Labelwin zur Ermittlung der Monteurkosten
Quelle: handbuch/werte_aus_labelwin_zur_ermittlung_der_monteurkosten.htm

|

Werte aus Labelwin zur Ermittlung der Monteurkosten

Direkt aus Labelwin werden in der gesamten Excel-Tabelle nur die Anzahl der Stunden für Unproduktiv, Krank Urlaub, usw. übernommen. Dabei kann man sich darüber streiten, ob man für eine vorausplanende Kalkulation wirklich die Krankstunden der einzelnen Mitarbeiter einsetzen soll oder besser einen Durchschnittswert. Schließlich ist es ja extrem unwahrscheinlich, dass der einzelne Mitarbeiter in der Zukunft genau so viel krank ist wie in der Vergangenheit. Andererseits stellt sich die Frage, wie denn der Durchschnitt festgestellt wird ? Letzten Endes ermittelt man ihn, indem man die Anzahl der gesamten Krankstunden der Vergangenheit durch die Anzahl der Mitarbeiter teilt. Dann kann man sich unserer Meinung nach die Durchschnittsberechnung sparen und gleich die konkreten Zahlen der einzelne Mitarbeiter eintragen. Allerdings entsteht ein Problem, wenn die Krankzeit länger als 6 Wochen dauert und die weiteren Kosten von der Krankenkasse übernommen wird.

Krank, Urlaubsstunden in Labelwin

Zunächst ist es natürlich erforderlich, dass die Stunden entsprechend gebucht werden. Als Stundenarten halten wir diese für die Mindestvoraussetzung:

· Normal Produktiv

· Reklamation / Nachbesserung Unproduktiv gearbeitet

· Krank Unproduktiv Ausfall

· Feiertag Unproduktiv Ausfall

· Urlaub Unproduktiv Ausfall

· Schule / Weiterbildung Unproduktiv Ausfall

· Lagerarbeiten, Inventur, Sonstiges Unproduktiv gearbeitet

· Büroarbeit Büro

Es ist sehr wichtig, dass Sie die Produktivkennzeichen bei den Stundenarten passen hinterlegt haben.

Eine Ausgabe der gebuchten Stunden erhalten Sie in der Zeitwirtschaft über die Menüpunkte ‚Auswerten’, ‚Produktivitätsauswertung’. In der Maske müssen Sie Stundenarten Label angekreuzt haben und am besten als Zeitraum ein ganzes Jahr einsetzen. Falls Sie die Zeiterfassung noch nicht so lange mit Labelwin vornehmen, so müssen Sie die Zeiten entsprechend auf ein Jahr hochrechnen.

[Bild]

Wählen Sie bei der Druckausgabe das Formular LC-stdq an.

[Bild]

Diese Werte müssen Sie nun in der Excel-Tabelle eintragen. Da die Zeiten dort in Tagen eingetragen werden, müssen die im Labelwin ermittelten Stundensummen durch die Anzahl der üblichen Stunden je Tag geteilt werden. Dies muss übrigens der gleiche Wert sein, wie in der Tabelle.

Die ermittelten Tage müssen sich unbedingt auf ein Jahr beziehen, auch wenn der Mitarbeiter ggf. nur einige Monate gearbeitet hat.

Die Ausgabe im Labelwin erfolgt genauso wie oben beschrieben, nur dass Sie als Formular LC-PROD wählen müssen.

Problematisch bei dieser Eintragung der konkreten unproduktiven Stunden bei jedem Mitarbeiter ist, dass dadurch seine Selbstkosten erhöht werden, obwohl er vielleicht nicht der Verursacher der unproduktiven Stunden ist. Wenn z.B. der beste (und vielleicht auch teuerste) Mitarbeitet oft die Sachen in Ordnung bringt, die andere verpfuscht haben, so sieht er besonders unproduktiv aus. Seine Selbstkosten sind also wesentlich höher, als die eines gleich bezahlten Mitarbeiters. In so einem Fall gibt es Sinn, die unproduktiven Stunden bei den Mitarbeitern anzusetzen, die sie verursacht haben. Da dies nur sehr aufwändig erfasst werden kann, ist eventuell eine Durchschnittsbildung der Unproduktivstunden sinnvoll. Allerdings sollte man den Durchschnitt nur bei etwa gleich teuren Mitarbeitern bilden, da die Stunden des Lehrling wesentlich billiger sind als des Monteurs.

Exkurs: Wer hat unproduktive Stunden verursacht?

Wenn Sie in der Zukunft eine Aussage darüber haben möchte, welche Pfuschstunden von den einzelnen Mitarbeitern zu verantworten sind, so können wir folgenden Weg anbieten: Richten Sie sich 2 weitere Stundenarten mit ‚unproduktiv verursacht’ und ‚unproduktiv Ausgleich’ ein. Buchen sie nun wie bisher die unproduktiven Stunden bei dem, der sie geleistet hat. Bei dem Verursacher buchen Sie nun z.B. 3 Stunden auf die Art ‚unproduktiv verursacht’ und - 3 Std. (also negativ) auf die Art ‚unproduktiv Ausgleich’. Damit bekommt auch der Verursacher das gleiche Geld wie bisher und über die Auswertung der Stundenarten können Sie dennoch die verursachten Stunden einsehen. Wenn Sie den Mitarbeitern allerdings eine monatliche Stundenausgabe zur Kontrolle geben, so könnte dies harte Diskussionen geben. Eventuell buchen Sie die Stunden erst mit Verspätung, nämlich nach dem Ausdruck für die Mitarbeiter.
