# Excel-Programmierung

Pfad: Auswertungen / Controlling > Controlling [Modul] > Controlling / Chefknopf > Excel-Programmierung
Quelle: handbuch/excel_programmierung.htm

|

Excel-Programmierung

Wenn Sie Daten in Excel-Tabellen reinreichen, mit denen in einer separaten Tabellenspalte gerechnet werden sollen, so müssen diese Rechenoperationen bereits in der Vorlage-Exceltabelle vorhanden sein. Wie solche Spalten bei der Ausgabe des SQL-Befehls per ’Dummy’ übersprungen werden können, steht im Kapitel 4.5.

Bei solchen Rechenzeilen gibt es jedoch das Problem, dass Sie nicht wissen, wie viel Zeilen später gefüllt werden, also nicht festlegen können, bis zu welcher Zeile Sie die Formel runterziehen müssen. Wenn Sie die Formel einfach bis 100 Zeilen runterziehen, gibt es ein Problem, sobald mehr als 100 Zeilen entstehen. Auf der anderen Seite erfolgt die Druckausgabe immer mit jenen 100 Zeilen, auch wenn nur wenige gefüllt sind.

Als Ausweg bietet es sich an, die Formeln per VBA-Programmierung auf die weiteren Felder auszuweiten. Die eigentliche Formel hinterlegen Sie einfach in der ersten Tabellenzeile.

[Bild]

Anschließend gehen Sie so vor:

- Vorlage der Exceldatei öffnen (liegt in Labelwin\excel\vorlage

- Makroprogrammierung starten mit ALT - F11 oder über das Menü ‚Extras, Makro, Visual-Basic

[Bild]

Wählen Sie nun ‚Diese Arbeitsmappe’ und drücken den kleinen Knopf ‚Code anzeigen’ (siehe Bild)

[Bild]

Anschließend können Sie in der großen freien Fläche das Programm schreiben, mit dem Ihre Excel-Tabelle beim Start verändert werden soll. Am besten kopieren Sie den Programmcode aus unserer mitgelieferten ‚Muster.xls’ heraus, fügen ihn ein und ändern ihn entsprechend ab.

Den Programmiermodus verlassen Sie mit ALT Q oder schließen ihn über das Kreuz oben rechts. Die Frage, ob Sie die Änderungen speichern wollen, müssen Sie dann natürlich mit JA beantworten.

Zum Lesen haben wir den Programmcode hier abgedruckt. Zeilen mit einem Häkchen am Anfang sind Kommentare / Erklärungen, die Sie nicht erfassen müssen.

|

Sub workbook_open()

Dim llng_last As Long

'Tabellenblatt ansteuern

Sheets("Halbfertige").Select

'Letzte Zeile feststellen,

' die 1 bei 'Cells(65536, 1)' ist Spalte A,

' Cells(65536, 2) würde Spalte B absuchen usw.

llng_last = Cells(65536, 1).End(xlUp).Row

'Nur wenn letzte Zeile größer als Zeile 10

If llng_last > 10 Then

'Bedingung 'nach unten' ziehen, bis zur letzten benutzten Zelle

Range("E10").Select

'Beginn bei Zelle E10 bis E...(letzte Zelle)

Selection.AutoFill Destination:=Range("E10:E" & CStr(llng_last)), Type:=xlFillDefault

'das Gleiche bei Zelle G10

Range("G10").Select

Selection.AutoFill Destination:=Range("G10:G" & CStr(llng_last)), Type:=xlFillDefault

End If

'Setzt Cursor auf Spalte A2 (nicht wichtig)

Range("A2").Select

'Aktiviert Tabellenblatt 'Ausgangsrg'

Sheets("Ausgangsrg").Select

'Setzt Cursor auf Spalte A2 (nicht wichtig)

Range("A2").Select

End Sub
