# 1. Export von Daten aus Labelwin

Pfad: Schnittstellen > planbar (Syntax) - Schnittstelle > 1. Export von Daten aus Labelwin
Quelle: handbuch/1__export_von_daten_aus_labelwin.htm

|

1. Export von Daten aus Labelwin

1. Export von Daten aus dem Labelwin-Programm zur Einspielung in das plan bar-Programm

1.1 Bereitstellung der Personaldaten

Im Labelwin-Programm werden in dem Modul Einstellungen unter dem Menüpunkt Programmbereiche – Personal – Personal erfassen die Mitarbeiter angelegt

[Bild]

Folgende Werte werden aus den Personaldaten an das plan bar -Programm übergeben:

Personalnummer Über die Personalnummer können die Programme Labelwin und plan bar einen Mitarbeiter identifizieren. Diese Nummer muss also für jeden Mitarbeiter eindeutig sein und darf nicht nachträglich geändert werden.

Name Hier steht zur visuellen Identifizierung der Name des Mitarbeiters.

Lohngruppe Die Labelwin-Lohngruppen werden den plan bar -Gruppen zugeordnet.

Eingestellt am Über das Eintrittsdatum erkennt das plan bar -Programm, ob

(Karteikarte Zusatzdaten) der Mitarbeiter ganzjährig beschäftigt oder erst im aktuellen Jahr eingestellt wurde. Dieses Feld muss gefüllt sein.

Jahresurlaub Diese Urlaubsangabe wird in das plan bar -Programm (Karteikarte Zeiten) individuell übernommen.

Grundlohn Hier sollte der aktuelle Stundenlohn des Mitarbeiters

(Karteikarte Zusatzdaten) stehen. Wenn das Feld leer ist, können Sie den Stunden-lohn bzw. das Gehalt auch im plan bar nachtragen.

Produktivitätsprozentsatz Dieser für den Mitarbeiter individuelle Anteil der Produktivstunden an den Anwesenheitsstunden wird an das plan bar -Programm übergeben. Die dafür benötigten Stunden bezieht die Schnittstelle aus den erfassten Stunden in der Zeitwirtschaft. Um die Stunden korrekt abgrenzen zu können, muss jeder Labelwin-Stundenart eine plan bar -Gruppe zugeordnet werden (siehe Punkt 1.2).

1.2 Bereitstellung der Stunden für die Abweichungsanalyse

In der Abweichungsanalyse des plan bar -Programms können für einen Soll/Ist-Vergleich des Jahresumsatzes die tatsächlichen Stunden der Mitarbeiter eingegeben werden. Über die Export-Schnittstelle im Labelwin können Sie diese Daten automatisch ermitteln lassen und an die Abweichungsanalyse übergeben. Es handelt sich dabei um die Produktivstunden, Urlaubsstunden, Krankstunden und Fortbildungs/Schulstunden.

Damit diese Stunden für die Übergabe unterschieden werden können, müssen allen Stundenarten im Labelwin-Programm eine plan bar -Gruppe zugeordnet werden. Dafür gehen Sie in das Modul Einstellungen unter den Menüpunkt Programmbereiche – Zeitwirtschaft – Stundenarten.

[Bild]

Es gibt sechs plan bar -Gruppen zur Auswahl:

Produktiv Dieses Kennzeichen müssen alle Lohnarten bekommen, mit denen Sie Stunden eingeben, die weiter berechnet werden können z.B. Normalstunden, Kundendienst, Zeitkonto usw.

Urlaub Dieses Kennzeichen bekommen alle Urlaubsstundenarten z.B. Urlaub, Sonderurlaub, Urlaub Azubis usw.

Krank Dieses Kennzeichen bekommen alle Stundenarten, die mit Krankstunden zu tun haben z.B. krank. Krank > 6 Wochen, Kur usw.

Fortbildung Dieses Kennzeichen bekommen alle Stundenarten, die mit Fortbildungsstunden zu tun haben z.B. Schule Azubis, Schulungen, Seminare usw.

Anwesend Hier geht es um alle Stunden, an denen die Mitarbeiter zwar

Unproduktiv anwesend waren, also gearbeitet haben, aber unproduktiv (nicht an Kunden berechenbar) z.B. Garantiearbeiten, Werkstatt, Büro

Feiertag Hier geht es um die Stundenarten für bezahlte Feiertage, an denen nicht gearbeitet wurde.

Bitte achten Sie darauf, dass auch das Produktivitätskennzeichen korrekt gesetzt sein muss.

1.3 Programmaufruf des Exports aus Labelwin

Den Export der Daten finden Sie im Modul Einstellungen unter dem Menüpunkt Programmbereiche – Personal – Export / Import plan bar :

[Bild]

Wenn Sie den Export plan bar aufrufen, werden beide Exportdateien (Personaldaten und Abweichungsanalyse) angelegt. Zunächst erscheint ein Menü, in dem Sie ein paar generelle Einstellungen vornehmen müssen. Diese Einstellungen merkt sich das Programm dann für den nächsten Export:

[Bild]

Zielpfad

Wenn sich die beiden Programme auf einem Rechner befinden lautet der Standard-Zielpfad:

C:\Benutzer\“Benutzername“\Eigene Dateien\planbar Dateien\Labelwin Austausch\Import\

Dabei ist der „Benutzername“ der Anmeldename des Benutzers auf dem Rechner

Das plan bar benutzt diesen Pfad automatisch. Wenn sich beide Programme nicht auf dem gleichen Rechner befinden, können Sie das Verzeichnis beliebig wählen. Die Dateien heißen LabelwinImp.xml (Personaldaten) und LabelwinImpA.xml (Abweichungsanalyse).

Zeitraum für Produktivitätsberechnung

Hier kann ein beliebiger Zeitraum für die Berechnung des Produktivitätsprozentsatzes vorgegeben werden. Dabei sollten Sie beachten, dass nur Monate verwendet werden, die in der Stundenerfassung abgeschlossen sind und der Zeitraum nicht zu groß wird (max. 2 Jahre).

Zeitraum für Stundenübergabe

Hier wird ein Zeitraum angegeben, über den die Stunden für die Abweichungsanalyse zusammengestellt werden. Dieser Zeitraum sollte dem der Abweichungsanalyse im plan bar entsprechen. Er kann aber auch kleiner sein, ist dann aber für die Analyse ungenauer. Dabei sollten Sie beachten, dass nur Monate verwendet werden, die in der Stundenerfassung abgeschlossen sind und dass der Zeitraum nicht ein Jahr übertreffen darf.
