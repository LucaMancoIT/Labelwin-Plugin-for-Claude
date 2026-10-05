# Mobilzeit

Pfad: Schnittstellen > Mobilzeit
Quelle: handbuch/mobilzeit.htm

|

Mobilzeit

Um die Daten von Mobil-Zeit zu übernehmen, müssen gewisse Regeln eingehalten werden.

1) Es muss die aktuellste Version von Mobilzeit aktiv sein. Stand neuer als 20.11.2002

2) Die Version Labelwin muss neuer als 24.11.2002 sein. Wichtig ist das Datum des Modules Zeitwirt.exe

3) Die Schnittstelle muss von Labelwin frei geschaltet sein.

Um dem Monteur die Eingabe der Stundenart und eventueller Zulagen zu ermöglichen, muss er eine Liste mit den internen Nummern dieser Arten und Zulagen. Dazu müssen Sie im Einstellprogramm unter den Menüpunkten Programmbereiche, Zeitwirtschaft, Stundenarten die Druckausgabe anwählen. Der Druck muss auf dem Formular ESSD1 erfolgen.

[Bild]

Diese Nummer in Mobilzeit bei den Tätigkeitsschlüsseln als Lohnart hinterlegt werden. Wenn z.B. die Reklamationsstunde in Mobilzeit die Tätigkeitsnummer 123 hat, so muss in der Tabelle bei der Tätigkeit 123 die Lohnart 26 hinterlegt werden.

In dem Mobilzeitgerät wird dann wie gewohnt die Tätigkeitsnummer 123 eingetragen.

Da im Labelwin nur die vom Kunden unterschriebene Zeit wichtig ist, wird diese Zeit beim Abschluss des Auftrages manuell in das Gerät eingetragen.

Zulagen: Um auch in Mobilzeit zu einem Auftrag stunden- oder tageweise Zulagen erfassen zu können, hat Mobilzeit 4 weitere Eingabefelder geschaffen, die beim Abschluss des Auftrages manuell gefüllt werden können. Hier muss direkt die Label-interne Nummer der Zulagen erfasst werden. Dazu müssen Sie wieder eine Liste der Zulagen ausdrucken. Wählen Sie im Einstellprogramm unter den Menüpunkten Programmbereiche, Zeitwirtschaft, Stundenweise Zulagen die Druckausgabe anwählen. Der Druck muss auf dem Formular ESZA1 erfolgen.

[Bild]

Wenn Sie mit tageweisen Zulagen arbeiten, so müssen Sie diese ebenfalls ausdrucken.

Die Zulagen werden in Mobilzeit mit der Nummer und in dem Mengenfeld mit der Stückzahl (also meist 1 oder der Stundenzahl) eingetragen. Es können pro Auftrag 2 Zulagen erfasst werden.

|

Am besten schreiben Sie mit Word eine kleine Tabelle, in der Sie alle für den Monteur wichtigen Stundenarten und Zulagen eintragen.

Beispiel:

[Bild]

Übernahme der Zeiten in Labelwin

Wählen Sie im Modul Zeiterfassung die Menüpunkte Optionen, Zeiten aus Mobilzeit an. Beim ersten Mal müssen Sie den Pfad und Dateinamen der Schnittstellendatei eingeben. Das Programm merkt sich diese Informationen und schlägt sie beim nächsten Mal wieder vor.

Nach der Übergabe erhalten Sie ein übersichtliches Protokoll der übergebenen Daten und eventuell aufgetretener Fehler.

Die Übergabedatei wird nach der Übernahme automatisch gelöscht. Sollten Sie versehendlich Daten aus Mobilzeit übergeben, bevor Sie die letzten Daten verarbeitet haben, so entsteht kein Schaden. Mobilzeit hängt einfach an, wenn eine Datei vorhanden ist und somit können alle Daten in Labelwin eingelesen werden.

Datenstruktur :

Obwohl die Struktur der Daten für die Übernahme nicht interessant ist, kann die Kenntnis bei einer Fehlersuche interessant sein. Deshalb stellen wir hier den Aufbau der Übernahmedatei vor: Die einzelnen Informationen werden durch ein Semikolon getrennt. Jeder Datensatz wird mit Carriage Return abgeschlossen.

Beispieldatensatz:

20020920;9;A01-00821;8:15;11:30;26;3,25;3,25;BI-X12;20,5;8;1;0;0;0;0;text,1

20020920 Datum 2002, Monat 9, Tag 20

9 Personalnummer

A01-00821 Auftragsnummer 01-00821 (Projekt mit P am Anfang)

8:15 registrierte Anfangszeit (im Labelwin nicht verwendet)

11:30 registrierte Endzeit (im Labelwin nicht verwendet)

26 Stundenart (interne Nummer)

3,25 registrierte Arbeitszeit (im Labelwin schaltbar, ob verwendet, wird bei Mobilzeit ggf. nicht gefüllt)

3,25 vom Kunden unterschriebene Arbeitszeit

BI-X 12 Autonummer (im Labelwin nicht verwendet)

20,5 registrierte Fahrstrecke (im Labelwin nicht verwendet)

8 1.Zulagenart 8 (bei obigem Beispiel Schmutzzulage)

1 Menge der 1. Zulagenart

0 2.Zulagenart leer

0 Menge der 2. Zulagenart leer

0 Tageszulage 1 – wertmäßig

0 Tageszulage 2 – wertmäßig

Text Arbeitstex

1 Abrechnen Als Regie , wenn 1 dann wird das Kennzeichen gesetzt, in allen anderen Fällen nicht

(Neu seit dem 22.09.2017 ab V5:82t
