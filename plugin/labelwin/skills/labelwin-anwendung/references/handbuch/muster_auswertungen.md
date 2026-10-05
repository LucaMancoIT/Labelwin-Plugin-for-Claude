# Muster Auswertungen

Pfad: Einrichtungsarbeiten > Auswertungscenter (V5) / Startcenter (V4) [27] > Weitere Auswertungen anlegen > Muster Auswertungen
Quelle: handbuch/muster_auswertungen.htm

|

Muster Auswertungen

Wenn Sie das Modul CONTROLLING gekauft haben, haben Sie auch die Möglichkeit eigene Auswertungen für das Startcenter zu erfassen.

Im Modul EINSTELLUNGEN unter [Optionen - Benutzerrechte vergeben] müssen Sie den User markieren für den Sie die Auswertungen ändern wollen. Die Einstellungen für das Startcenter finden Sie dann im Bereich "Startcenter"'. Dort gibt es einen Knopf um eigene Auswertungen zu erfassen. Unter dem Menüpunkt 'Auswertungen' können Sie unter <Optionen> erstellte Auswertungen im Label Format importieren.

Anzahl KD Aufträge/Dokumente

Wenn Sie die Datei EigeneAuswertungen.scaw auf Ihren Rechner speichern und dann importieren, haben Sie im Startcenter folgende zusätzliche Auswertungen:

-

Anzahl der KD-Aufträge mit Status 'Offen'

-

Anzahl der KD-Aufträge mit Status 'In Arbeit'

-

Anzahl der KD-Aufträge mit Status 'Ware bestellt'

-

Anzahl der KD-Aufträge mit Status 'erledigt'

-

Lohnsumme aus den Zeitbuchungen auf noch nicht berechnete KD-Aufträge. Das ist also die Lohnsumme, für die Ihr Betrieb im Kundendienst bereits gearbeitet hat und noch nicht in Rechnung gestellt wurde.

-

Anzahl der Angebote mit Status 'offen'


[Bild] 

Termine mit Fälligkeit

Wenn sie die Datei AufgabenmitFälligkeit.scaw auf Ihren Rechner speichern und dann importieren, haben sie im Startcenter folgende zusätzliche Auswertungen:

-

Anzahl offener Termine mit Fälligkeit bis heute

-

Anzahl offener Termine mit Fälligkeit in den nächsten 07 Tagen

-

Anzahl offener Termine mit Fälligkeit in den nächsten 14 Tagen

-

Anzahl offener Termine mit Fälligkeit in den nächsten 30 Tagen

In dem Befehl wird das Schlüsselwort ##aufgabenuser## mit dem User ersetzt, dessen Termine auf diesem Rechner geprüft werden.

Hinweis vom 11.09.2009: Im Datenbank SQL Befehl wird für die Auswertung der Befehl format verwendet. Dieser funktioniert beim SQL Server nicht.


[Bild] 

Kontostand anzeigen

Der aktuelle Kontostand des Bankkontos kann im Startcenter angezeigt werden, wenn man mit dem nachfolgenden SQL-Befehl eine Auswertung erstellt.

SELECT FORMAT(LAST(auszugdaten.endbestand),"#,###,##0.00 \€") AS ausgabe FROM auszugdaten WHERE konto1 = 'XXX'

XXX ersetzen Sie bitte durch die Kontonummer der Bank, deren Kontostand Sie ausgeben möchten. Wenn Sie die Kontostände mehrerer Banken ausgeben möchten, müssen Sie pro Bank einen separaten SELECT-Befehl erstellen.
