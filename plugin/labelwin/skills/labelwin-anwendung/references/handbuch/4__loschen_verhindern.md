# 4. Löschen verhindern

Pfad: Archivierung > Scan-Archiv [Modul] > 4. Löschen verhindern
Quelle: handbuch/4__loschen_verhindern.htm

|

4. Löschen verhindern

(ab V5.90)

Unberechtigte Lese- und Löschzugriffe per Explorer verhindern

Bisher war es so, dass die Rechte im Labelwin nicht verhindern konnten, dass man von der Windows Explorer Seite aus darauf zugreifen konnte. Mit der seit etwa Anfang 2018 verfügbaren Verschlüsselung kann zwar niemand mehr in die gescannten Pdf’s reinschauen, aber das Löschen wäre immer noch möglich. So etwas muss man natürlich als Sabotage verbuchen, aber sicherer ist es, auch das zu verhindern.

Dies ist mit einer Methode möglich, bei dem der Systembetreuer leider auch zum Einsatz kommen muss. Hier nur die grobe Beschreibung:

-

Man muss ein zweites Verzeichnis einrichten, bei dem die Anwender nur Leserechte haben.

Beim Scannen wird wie bisher in das ‚normale‘ Verzeichnis geschrieben. Ein Programm wie Robocopy kopiert regelmäßig die Daten in das neue Lese-Verzeichnis und löscht sie im bisherigen Pfad. Das einzurichten ist der Part Ihres Systembetreuers, der von uns dazu eine Anleitung bekommen kann. Die Anzeige im Labelwin, bei der dann wie bisher alle Rechte und Schlösser greifen, holt die anzuzeigende Pdf dann aus dem Lesebereich und zeigt sie. Manipulationen sind damit ausgeschlossen, was im Sinne der DSGVO sicherlich auch wichtig ist.

Hinweis: Um damit eine Revisionssicherheit zu erreichen, müssen Sie dennoch mit dem Finanzamt reden und vor allem eine revisionssichere Datensicherung aufbauen.

Nun haben wir im Einstellbereich vom Scanarchiv die Beschreibung und den Pfad hinterlegt, damit der Einsatz unabhängig von uns eingerichtet werden kann.
