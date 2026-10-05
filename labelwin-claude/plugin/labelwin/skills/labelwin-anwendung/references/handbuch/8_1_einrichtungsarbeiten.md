# 8.1 Einrichtungsarbeiten

Pfad: Kundendienst > KD-Mobil Notebook [Modul] > 8. Zeiterfassung, flexible Maske V5 > 8.1 Einrichtungsarbeiten
Quelle: handbuch/8_1_einrichtungsarbeiten.htm

|

8.1 Einrichtungsarbeiten

Die Maske wurde so umgestaltet, dass die auszufüllenden Elemente in der Reihenfolge frei platzierbar sind. Alle Zeiterfassungs-Elemente wurden dazu mit Nummern versehen (siehe Kapitel Eingabe-Elemente).

Wo es vorher 3 Karteireiter für die Elemente gab, gibt es nun bis zu 3 Knöpfe. Wir gehen aber davon aus, dass in der Regel der zweite Button „Zusatz buchen“ nicht erforderlich sein wird.

[Bild]

Es gibt bisher keine Oberfläche im Einstellmodul um die Reihenfolge zu verändern. Dies muss mit Hilfe dieser Beschreibung direkt in der Global.ini erfolgen.

In der Datei global.ini werden bei der ersten Benutzung der neuen Maske die Werte so gesetzt, wie sie in der alten Maske platziert waren. Dazu müssen aber jene 3 Knöpfe ein Mal angeklickt werden.

[Zeitbuch1]

sichtbar1=1,2,17,3,23,4,5,6,7,9,10,8,11

sichtbar2=14,15,22,18,19,12,13,16,20

sichtbar3=21

Abstand=1

Erklärung:

Bei sichtbar1= sind die Felder festgelegt, die beim Start und bei Betätigung des Buttons „Buchen“ sichtbar sind

Bei sichtbar2= sind die Felder des Buttons „Zusatz buchen“ festgelegt.

Bei sichtbar2= 0 wird der Button „Zusatz buchen“ unsichtbar

Bei sichtbar3=21 werden unter „Anzeigen“ die bisher erfassten Zeitbuchungen aufgeführt

Abstand=1 regelt den Abstand zwischen den Eingabefeldern, Zahl zwischen 0 und jeweils x 60 Pixel,

max. 3 ist sinnvoll

Zusatzstd=1 ist eine Sonderentwicklung mit der Zusatzstunden automatisch mitgebucht werden können

Vorschau Einrichtung über das Einstellmodul (ab V5.86)

Anstelle die Zeiterfassungs-Elemente über die global.ini im Block [Zeitbuch1] wie oben beschrieben manuell zu konfigurieren, lässt sich das ganze jetzt über das Einstellmodul im Bereich [Programmbereiche – Zeitwirtschaft – Grundeinstellungen] realisieren.

[Bild]

Bei den drei Karteiseiten müssen die gewünschten Elemente mit Komma getrennt eingetragen werden. Die Vorgehensweise entspricht dem Prinzip in der global.ini.
