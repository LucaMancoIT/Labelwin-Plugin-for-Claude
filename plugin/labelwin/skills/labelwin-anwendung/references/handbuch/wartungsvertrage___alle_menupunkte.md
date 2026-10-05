# Wartungsverträge - Alle Menüpunkte

Pfad: Adressverwaltung > Adressen [5] > 7. Wartungsverträge > Wartungsverträge - Alle Menüpunkte
Quelle: handbuch/wartungsvertrage___alle_menupunkte.htm

|

Wartungsverträge - Alle Menüpunkte

Die Menüpunkte im Einzelnen:

|

Datei

Neuer Vertrag (F2)

Durch Anwahl dieses Punktes wird die Erfassungsmaske für Wartungsverträge geleert. Nachdem Sie die entsprechenden Daten eingetragen haben, müssen Sie den Knopf ‚Speichern’ anwählen, um die Daten dauerhaft abzuspeichern.

Speichern

Durch Anwahl dieses Punktes werden die in der Maske aktuell gezeigten Werte abgespeichert. Sollten Sie die Daten eines vorhandenen Wartungsvertrages aufgerufen haben, so werden die Änderungen abgespeichert. Sollten Sie zuvor den Menüpunkt ‚Neuer Vertrag’ gewählt haben, so werden die Werte als neuer Wartungsvertrag abgespeichert.

Speichern als Neu

Hierdurch erreichen Sie, dass die in der Maske aktuell gezeigten Daten als neuer Wartungsvertrag abgespeichert werde. Dies bedeutet, dass Sie den zuvor aufgerufenen Wartungsvertrag quasi verdoppeln. Die Funktion ist entwickelt worden, um bei ähnlichen Wartungsverträgen nicht immer alle Werte neu erfassen zu müssen.

Löschen

Hiermit wird der aktuell gezeigte Wartungsvertrag aus der Liste entfernt. Die Funktion greift nur dann, wenn für Sie die Rechte dazu eingerichtet sind.

Zugeordnete Dokumente

Durch die Anwahl dieses Menüpunktes kommen Sie Liste der bereits hinterlegten Dokumente und haben dort die Möglichkeit, ein neues Dokument anzulegen.

Dokument zuordnen

Mit diesem Menüpunkt können Sie ein Dokument zuordnen z.B. eine Bedienungsanleitung, eine Explosionszeichnung etc.

Beenden

Die Maske wird geschlossen. Falls Sie Änderungen vorgenommen haben, die noch nicht gespeichert sind, gehen diese Änderungen verloren.

|

Bearbeiten

Rechnung erstellen

Hiermit wird die Rechnung für einen einzelnen Vertrag erstellt. Wenn Sie Rechnungen für mehrere Verträge automatisch erstellen wollen, so müssen Sie dies im Modul KUNDENDIENST unter dem Menüpunkt <Optionen> <Wartungsrechnungen schreiben> erledigen.

Es wird automatisch eine Rechnung angelegt, in der die Position mit der Wartungspauschale eingetragen wird. Anschließend wird das Programm-Modul gestartet, mit dem sämtliche Rechnungen, Angebote usw. erstellt werden. Sie haben die Möglichkeit, weitere Positionen hinzuzufügen und die Rechnung dann wie jede andere Rechnung auch auszudrucken. Sollten Sie einen Artikel für die Wartung per Hand in eine Rechnung einsetzen, so müssen Sie unbedingt die Artikelart ‚Wartungspauschale’ verwenden, damit die Summe auf die Guthabenseite der Wartungsverträge gerechnet werden kann. Nur darüber ist eine exakte Nachkalkulation möglich.

Rechnung mit Vorlage

Unter diesem Menüpunkt können Sie für die Erstellung einer einzelnen Wartungsrechnung auf die Musterrechnungen zugreifen. Gleichzeitig ist damit die Möglichkeit geschaffen worden, mehrere Verträge in einer Rechnung aufzunehmen. Dieses hängt vom Kennzeichen ‚Sammelrechnung’ ab. Es greift nur, wenn mehrere Verträge mit dem gleichen Rechnungsmonat und dem Kennzeichen versehen werden. Die Möglichkeit der Sammelrechnung greift noch nicht beim Seriendruck der Vertragsrechnungen.

Wartungsvertrag drucken

Hiermit werden alle zu dem Wartungsvertrag erfassten Daten ausgedruckt. Bei der Ausgabe greift das Programm auf ein Formular zurück, welches ggf. auch nach Ihren Wünschen angepasst werden kann. Bei allen im Programm verwendeten Formularen kann die Anpassung nur über uns erfolgen, es sei denn, Sie kaufen ein Programm namens Crystal Report. Um einen Wartungsvertrag optisch ansprechend zu gestalten, gehen viele unserer Kunden über die Textverarbeitung Word. Dazu legen sie im Projekt einfach einen Brief unter Verwendung einer entsprechenden Vorlage an, bekommen die Adresse automatisch hinein und müssen lediglich die Vertragsdaten per Hand eintragen.

Selektieren Wartungsverträge

Hiermit können Sie in den Wartungsverträgen nach beliebigen Werten selektieren und diese gefundenen Verträge auf verschiedene Arten ausdrucken. Da die Vorgänge die gleichen sind wie beim Selektieren von Adressen, lesen Sie die Methode bitte im Kapitel Adressen selektieren nach.

|

Nachkalkulation

Aktueller Vertrag

In einer Tabelle werden alle auf den aktuell markierten Vertrag aufgelaufenen Kosten und Erträge gezeigt. Ausgewertet werden Kundendienstaufträge, die zu einer Anlage gehören, die wiederum zu einem Wartungsvertrag gehört.

[Bild]

Die Auswertung wird in 3 Gruppen (Spalten) unterteilt:

· Aufträge mit zugeordnetem Wartungstermin

· Aufträge mit ‚Störung‘. Sie sind ohne Wartungstermin, aber bei ihnen ist das Kennzeichen ‚Abrechnung über Wart.-Vertrag‘ gesetzt. Das Kennzeichen befindet sich in der Auftrags-erfassung im Bereich des Statusfelds

[Bild]

· Alle restlichen Aufträge ohne Termin oder Wartungskennzeichen

|

Erklärung zu Feldern, die eventuell unklar sind:

Erlös Wartungspauschale:

Hier werden Artikel aus den Rechnungen dargestellt, die als Artikelart ‚Wartungspauschale' haben. Bei den automatisch generierten Artikeln ist dies der Fall, kann aber auch manuell bei anderen Artikeln gesetzt werden.

Fahrtkosten aus Kd-Auftrag:

Diese werden über die Erledigtmaske des Auftrages aufgrund der Kilometereingabe ermittelt. Wenn die Fahrtkosten nicht im Vertrag enthalten sind (Ankreuzfeld in der Vertragsmaske) werden sie hier nicht berücksichtigt, sondern sind in den Materialkosten und Erlösen enthalten. Es werden die Kilometer-Selbstkosten verwendet.

Materialkosten aus Kd :

In der Erledigt-Maske kann eine Auswahl auf ‚Wartung' gesetzt werden. Dann können Kosten erfasst werden, obwohl keine Rechnung geschrieben wird. Dies ist bei Störungen interessant, Sie können aber auch eine Null-Rechnung schreiben, damit die einzelnen Artikel dokumentiert sind. Dann erscheinen die Kosten im Feld ‚Materialkosten aus Rg.'

Knopf Logbuch mit Termin:

Über diesen Knopf werden Ihnen alle Kundendienstaufträge angezeigt, die mit dem Wartungstermin verknüpft sind.

Knopf Logbuch mit Störung:

Über diesen Knopf werden Ihnen alle Kundendienstaufträge angezeigt, die keinen Wartungstermin aber das Kennzeichen ‚Abrechnung über Wart.-Vertrag‘ haben.

Knopf Logbuch Rest:

Über diesen Knopf werden Ihnen alle Kundendienstaufträge angezeigt, die weder einen Termin noch ein Wartungskennzeichen haben.

Alle Verträge

Nach Wahl dieses Menüpunktes erscheint eine Maske, in der über einen Zeitraum von bis alle Wartungsverträge in einer übersichtlichen Liste dargestellt werden.

In der übergreifenden Auswertung ist es möglich, eine Eingrenzung auf eine bestimmte Vertragsart oder Eigentümeradresse zu treffen.

[Bild]
