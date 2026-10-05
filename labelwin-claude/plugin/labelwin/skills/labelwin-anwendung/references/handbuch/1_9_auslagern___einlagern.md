# 1.9 Auslagern / Einlagern

Pfad: Artikelstammdaten > Katalog [10] > 1. Einleitung > 1.9 Auslagern / Einlagern
Quelle: handbuch/1_9_auslagern___einlagern.htm

|

1.9 Auslagern / Einlagern

Auslagern -> lokal

Beim Einspielen von großen Mengen Artikeldaten kann es sinnvoll sein, diese nicht auf dem Hauptrechner einzuspielen, sondern zunächst auf der lokalen Festplatte. Damit wird das Netzwerk während der Umsetzung nicht belastet.

Das Programm kopiert den Katalog zusätzlich auf die lokale Festplatte und nimmt die Änderungen zunächst nur dort vor.

|

Verständlicherweise muss auf der lokalen Festplatte ein ausreichend großer Speicherplatz vorhanden sein. Bitte nehmen Sie als Faustregel je 1000 Großhändlerartikel 1 MB an. Ein großer Händlerkatalog mit 100 000 Artikeln benötigt also ca. einen freien Festplattenspeicher von 100 MB. Da im Vorhinein die Größe des Kataloges noch nicht feststeht, kann unser Programm den erforderlichen Bedarf vorab nicht prüfen. Sollte es sich jedoch bei dem Katalog um einen bereits vorhandenen Katalog und eine Artikeländerung handeln, so wird automatisch geprüft ob der Katalog auf die lokale Festplatte kopiert werden kann. Ggf. erfolgt eine entsprechende Warnmeldung.

Nach Anwahl des Menüpunktes zur Auslagerung kommt die nebenstehende Meldung, aus der hervorgeht wohin die Auslagerung gelegt wird. Hier sollte kontrolliert werden, dass auch wirklich ein lokales Laufwerk (in der Regel C: oder D:) verwendet wird.

Ist das Zielverzeichnis kein lokales Laufwerk sollte der Vorgang abgebrochen werden und zuerst über die EINSTELLUNGEN ein lokaler Auslagerpfad eingestellt werden.

|

[Bild]

Den Auslagerpfad legt man im Modul EINSTELLUNGEN unter <Grundeinstellungen><Pfade> fest.

[Bild]

Nach erfolgter Einspielung muss der Katalog unter dem Menüpunkt <Katalog> <Einlagern -> Netz> wieder eingelagert - also zurück kopiert werden.

Tipp: Die Auslagerung auf die lokale Platte kann auch in der Maske der Datanormeinspielung gesetzt werden und hat exakt die gleiche Wirkung.

[Bild]

Auf dem Rechner, auf dem sich die Kopie befindet wird der Hintergrund der Maske Grün dargestellt, auf allen anderen Rechnern wird ein ausgelagerter Katalog durch einen roten Hintergrund angezeigt.

[Bild]

Hinweis: Da es insbesondere bei großen Katalogen zu Problemen während der Einspielung gibt, sollten Sie dort die Datanorm-Dateien immer lokal einspielen.

Wenn bei der Einspielung Probleme auftreten, können Sie die Auslagerung unter dem Menüpunkt <Katalog> <Auslagerung löschen> einfach löschen. Die Datei auf der lokalen Platte wird damit gelöscht und in der Hauptdatenbank wird die Information über die lokale Kopie entfernt. Der Vorgang dauert nur Sekunden.

Einlagern -> Netz

Beim Einspielen von großen Mengen Artikeldaten kann es sinnvoll sein, diese nicht auf dem Hauptrechner einzuspielen, sondern zunächst auf der lokalen Festplatte. Damit wird das Netzwerk während der Umsetzung nicht belastet.

Wenn keine Fehler aufgetreten sind, muss der Katalog nach der Einspielung auf der lokalen Platte ins Netz zurückkopiert werden.

Hinweis: Wenn bei der Einspielung Fehler aufgetreten sind, sollten Sie den Katalog nicht wieder einlagern, sondern unter dem Menüpunkt <Katalog> <Auslagerung löschen> den vorherigen Zustand wieder herstellen.

Die Einlagerung kann bei großen Katalogen und langsamen Netzwerken durchaus 5-10 Minuten dauern.

Die Einlagerung ist nur möglich, wenn niemand den Katalog geöffnet hat. Es darf also auch keine Artikelsuche oder Preisinfo genutzt werden.

Auf dem Rechner, auf dem sich die Kopie befindet wird der Hintergrund der Maske Grün dargestellt, auf allen anderen Rechnern wird ein ausgelagerter Katalog durch einen roten Hintergrund angezeigt.
