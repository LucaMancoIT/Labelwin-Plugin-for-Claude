# 9. Einrichten ZEBEX-Scanner

Pfad: Materialwirtschaft > Scannerverarbeitung [Modul] > 9. Einrichten ZEBEX-Scanner
Quelle: handbuch/9__einrichten_zebex_scanner.htm

|

9. Einrichten ZEBEX-Scanner

Vor der erstmaligen Benutzung des Zebex-Scanners muss einmal die Batterie für ca. 12 Std. entfernt werden, da er nur dann in den Grundzustand geht. Im Auslieferungstand sind schon irgendwelche Programme gestartet, die auch unser Lieferant nicht erklären kann. 12 Std. ohne Knopfzelle setzen alles zurück.

In dem Programm ‚Einstellungen’, ‚Grundeinstellungen’, ‚Allgemein’ , Kreuzen Sie bitte den Punkt ‚Scannerverarbeitung aktiv’ an.

Der Scanner wird standardmäßig an die COM2 – Schnittstelle angeschlossen.

Für das Auslesen des Scanners müssen folgende Dateien im Verzeichnis Labelwin vorhanden sein:

scann.exe (Label-Modul)

UPL.exe (startet den Auslesevorgang (DOS-Programm)

Upload.set unbedingt unverändert lassen

Comm.set ggf. mit Notepad com2 gegen comx auswechseln

Ablauf beim Benutzen des ZEBEX-Scanners:

- Scanner einschalten und nach der umfangreichen englischen Meldung einfach die Enter-Taste (oben links) drücken.

- nun kann gescannt oder über die Tastatur eingegeben werden.

- geben Sie nun je nachdem, ob es sich um ein Baustellenprojekt oder um einen Kundendienstauftrag handelt die entsprechende Nummer ein. Wenn die Nummer von einem Auftragszettel oder einer Stückliste gescannt wird, sollte alles passend eingerichtet sein.

- Bei der Handeingabe müssen Sie bestimmte Regeln einhalten:

-bei Projekten muss vor die Projektnummer ein # - Zeichen, ein $-Zeichen oder ein ;-Zeichen (Semikolon) gesetzt werden. Sie dürfen bei Projekten auch Bezeichnungen eingeben, die nicht als Projekt in Label angelegt sind. Wenn Sie beispielsweise #bestell eingeben, obwohl es dieses Projekt nicht gibt, wird lediglich eine UGS-Datei mit dem Namen BESTELL.UGS angelegt.

-bei Kundendienstaufträgen muss vor die Nummer ein * - Zeichen gesetzt werden.

Um auf der Zebex-Tastatur die passenden Zeichen zu erreichen müssen Sie ggf. mit den Tasten F1, F2,F3,Num umschalten. Einige Tasten sind mit 4 Symbolen belegt, die über diese Umschaltung erreichbar sind. Betätigen Sie nach der Eingabe die Enter-Taste. Falls Sie sich dabei vertippen, so ist dies nicht schlimm. Lediglich die automatische Zuordnung ist nicht möglich und muss manuell erfolgen.

- Scannen Sie nun den Artikel. Wenn Sie den Artikel nur einmal benötigen, können Sie sofort den nächsten scannen. Anderenfalls geben Sie nach dem Scannen die Menge auf der Tastatur ein (ggf. vorher auf ‚num’ umschalten) und Betätigen die Enter-Taste.

- wenn die Erfassung für ein Projekt abgeschlossen ist, erfassen Sie einfach die nächste Projekt oder Auftragsnummer.

Auslesen der Daten beim ZEBEX

- legen Sie den Scanner in die Ladeschale und schalten ihn ein. Falls der Scanner schon an ist, schalten Sie ihn aus und erneut ein.

- lassen Sie den Scanner in dem Bild mit dem englischen Starttext stehen.

- starten Sie das Labelwin Modul Scanner und stellen Sie beim ersten Mal alle Werte gemäß der unten stehenden Beschreibung ein.

- betätigen Sie die Knopf ‚Übernahme starten’. Wenn die Übertragung einwandfrei gelaufen ist, können Sie das Modul wieder schließen - anderenfalls bekommen Sie entsprechende Fehlerhinweise und es werden Reparaturmöglichkeiten angeboten.
