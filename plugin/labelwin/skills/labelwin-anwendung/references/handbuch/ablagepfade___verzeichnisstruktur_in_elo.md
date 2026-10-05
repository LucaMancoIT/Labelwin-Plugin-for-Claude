# Ablagepfade / Verzeichnisstruktur in Elo

Pfad: Archivierung > ELO Dokumentenarchivierung [Modul] > 3. Label-spezifische Grundeinstellungen > Ablagepfade / Verzeichnisstruktur in Elo
Quelle: handbuch/ablagepfade___verzeichnisstruktur_in_elo.htm

|

Ablagepfade / Verzeichnisstruktur in Elo

Elo legt die Dokumente in einer Verzeichnisstruktur an, die aufgrund unserer obigen Einstellung bis zu 8 Stufen umfassen kann. Um Ihnen alle Möglichkeiten offen zu lassen, ist die Struktur der Bereiche Eingangsrechnungen, KD-Aufträge und sonstiger Dokumente in einer Steuerdatei abgelegt. Es handelt sich um die Datei ELO.ini im Verzeichnis Labelwin. Die Einträge in dieser Datei sollten nur in Absprache mit Ihren Labelwin-Betreuer oder dem Hause Label selbst geändert werden.

Wichtig ist an dieser Stelle noch einmal der Hinweis, dass Sie die Dokumente unabhängig von dieser Struktur auf jeden Fall im Labelwin wiederfinden

Ein Ablagepfad für Labelwin-Dokumente kann z.B. so aussehen

[Bild]

Denkbar ist es auch die Projekte jahresweise abzulegen

[Bild]

Auch eine Ablage nach Anfangsbuchstaben des Projektsuchwortes kann Sinn geben. Standardmäßig ist diese Variante nach der Installation gesetzt

[Bild]

Bevor wir Ihnen die Details erklären hier ein Abdruck der Datei \labelwin\elo.ini, die Sie als Sicherung zusätzlich im Original auf der CD im Verzeichnis \inst32\eloinst\sonstig finden.

Da wir für eine Dauer von ca. 3 Wochen eine andere Variante als Standard auf unserem Internet-Update liegen hatten, prüfen Sie bitte Ihre Datei. Ggf. löschen Sie die Datei einfach weg und spielen das Update neu ein. (Eine vorhandene Elo.ini wird beim Update nicht überschrieben)

Hier ist die Variante 3 aktiv (Standardauslieferung)

[Mandant1]

1=Schriftverkehr

2=Lieferscheine

3=Zeichnungen

4=Fotos

5=Notizen

6=Sonstiges

[Ablage1]

'Variante 1: relativ wenig Projekte (ca. bis 200)

'KD=¿Projekte¿@KDprojektnr@ @KDprojektname@ @KDprojektort@

'DOC=¿Projekte¿@TXProjektnummer@ @TXprojektname@ @TXprojektort@

'RE=¿Projekte¿@PRProjektnummer@ @PRprojektname@ @PRprojektort@

‚Variante 2: Mit Jahreszahl der Projekte (Viele 'Baustellen'Projekte)

'DOC=¿Projekte¿$(1:2)@TXProjektnummer@$¿@TXProjektnummer@ @TXprojektname@ @TXprojektort@

'KD=¿Projekte¿$(1:2)@KDprojektnr@$¿@KDprojektnr@ @KDprojektname@ @KDprojektort@

'RE=¿Projekte¿$(1:2)@PRProjektnummer@$¿@PRProjektnummer@ @PRprojektname@ @PRprojektort@

'Variante 3: Ablage nach Buchstaben des Projektnamens (viele Pojekte nach Projektname sortiert)

DOC=¿Projekte¿$(1:1)@TXprojektname@$¿@TXProjektnummer@ @TXprojektname@ @TXprojektort@

KD=¿Projekte¿$(1:1)@KDprojektname@$¿@KDprojektnr@ @KDprojektname@ @KDprojektort@

RE=¿Projekte¿$(1:1)@PRprojektname@$¿@PRProjektnummer@ @PRprojektname@ @PRprojektort@

Wenn Sie einfach nur eine andere Variante wählen möchten, so müssen Sie nur die Häkchen vor den Zeilen 'KD= 'DOC= 'RE= entfernen und bei den bisher aktiven Zeilen davor setzen (oder die bisher aktiven Zeilen löschen)

Details:

Die Pfadstruktur ist weitgehend frei steuerbar. Man muss sie allerdings sehr früh festlegen. Eine nachträgliche Änderung würde nur auf die anschließend angelegten Dokumente greifen und damit wäre das Chaos sicher.

Eine Besonderheit sind die Eingangsrechnungen. Diese werden in der Regel mehrfach im Elo eingetragen, obwohl das eigentliche Dokument nur einmal gescannt wird. Da Elo mit Verweisen arbeiten kann, legen wir die Rechnung einmal unter dem Hauptzweig ’Eingangsrechnungen’ ab und zusätzlich wird ein Verweis bei jedem Projekt abgelegt, das mit dieser Rechnung zu tun hat. Der fest hinterlegte Pfad für die Rechnungen geht so:

Eingangsrechnungen – Lieferant - Jahr (02) – Datum + Rechnungsnummer

Bei obigem Beispiel sind hinter der Projektnummer der Suchbegriff und der Ort sichtbar. Auch hier ist es frei steuerbar, wie die Strukturebene beschriftet werden soll. Bei sehr lokal arbeitenden Firmen würde man die Ortsbezeichnung sicherlich weglassen.

Es existieren drei in der Elo.ini festgelegten Pfade:

KD für Ablage der KD-Aufträge

RE für Ablage der Eingangsrechnungen zusätzlich zu deren Standardablage

DOC für Ablage gescannter und im Label hinterlegter Dokumente.

Elo setzt als Trennung zwischen den einzelnen Pfaden statt eines \ - Zeichens wie der Explorer ein umgedrehtes Fragezeichen. Dieses Zeichen wird dargestellt mit ‚¿’ . Man kopiert es bei Bedarf am Besten mit der Windows-Zwischenablage oder schreibt es mit Alt-Taste168 .

Der Eintrag für Eingangsrechnungen sieht z.B. so aus:

RE=¿Projekte¿@PRProjektnummer@ @PRprojektname@ @PRprojektort@

Dies entspricht einer Gliederung, wie sie oben im ersten Beispiel dargestellt ist. Um die Gliederung jedem Kunden beliebig zu ermöglichen arbeiten wir mit Schlüsselworten. Es handelt sich fast um die gleichen Worte, wie sie bei der Textverarbeitung mit Word und den Vor- und Nachbemerkungen verwendet werden. Diese sind im Handbuch im Kapitel Textverarbeitung nach zu lesen.

Die Schlüsselworte sind nur fast identisch, weil sich die ersten beiden Buchstaben je nach Ablage unterscheiden müssen.

Im Regelfall sollten alle 3 Pfade identisch sein.( mit Ausnahme der ersten beiden Buchstaben). Somit können dann aber nicht alle Schlüsselworte verwendet werden, sondern nur die, die in allen 3 Bereichen existieren.

Um etwas wie im zweiten obigen Beispiel zu ermöglichen wurde eine Methode benötigt, die aus einem Wort nur bestimmte Teile herauslöst. Die Jahreszahl wurde oben aus den ersten beiden Stellen der Projektnummer heraus genommen. Das Herauslösen geschieht durch eine Festlegung des ersten und letzten Zeichens aus dem Begriff. Damit der Rechner erkennt, dass nun nicht der ganze Begriff genommen werden soll, sondern nur ein Teil, wird das ganze in $_Zeichen eingeschlossen. Die Darstellung erfolgt dann mit $(Anfang : Ende ) Pfadteil $

Konkretes Beispiel mit einem Projekt der Nummer 02-01234 und dem Namen Müller der Objektadresse.

DOC = ¿Projekte¿$(1:2)@TXprojektnr@$¿@TXprojektnr@ @TXpadr2name@

Wir betrachten zunächst nur den Bereich $(1:2)@TXprojektnr@$

Zunächst wird das Schlüsselwort @TXprojektnr@ durch die jeweilige Projektnummer ersetzt. Damit entsteht $(1:2)02-01234$. Aufgrund der Werte (1:2) nimmt das Programm nur die Zeichen 1 bis 2, also in diesem Fall die ‚02’ . Da das Schlüsselwort für die Projektnummer noch mal vorkommt entsteht ein Pfad mit ¿Projekte¿02¿02-01234 Müller (das Schlüsselwort @TXpadr2name@ verweist auf den Namen der 2. Adresse im Projektdatenblatt) Da zwischen der Projektnummer und dem Namen kein ¿ - Zeichen steht, wird der Pfad mit der Projektnummer und dem Namen beschriftet.

Als zweites Beispiel wollen wir aus der Projektnummer nur die Werte ab der 4. Stelle haben. Man muss dann angeben $(4:99) )@TXprojektnr@$ - damit wird ab der 4.Stelle alles (nämlich bis zur 99ten Stelle) genommen.

Bei mehreren Mandanten muss ebenfalls die ELO.ini angepasst werden, da die Einträge jeweils nur für einen Mandanten gelten.

Der Eintrag in die Elo.ini im 3. Beispiel kann nun als Intelligenztest genutzt werden (oder als Kontrolle, ob Sie oben dafür oben alles verstanden haben).

Der Eintrag lautet

DOC = ¿Projekte¿$(1:1)@TXprojektname@$¿@TXprojektnr@ @TXprojektname@ TXprojektort

|

Achtung: Wenn Sie den Projektnamen für den Datenpfad verwenden wollen, so müssen Sie selbst dafür sorgen, dass jedes Projekt bei Ihnen einen Namen erhält. Dies wird im Labelwin bisher nicht erzwungen. Bei Projekten ohne Namen bleiben die Scans einfach in der Postbox liegen und werden nicht weiter verarbeitet.
