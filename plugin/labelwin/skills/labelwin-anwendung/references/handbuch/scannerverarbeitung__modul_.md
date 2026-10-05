# Scannerverarbeitung [Modul]

Pfad: Materialwirtschaft > Scannerverarbeitung [Modul]
Quelle: handbuch/scannerverarbeitung__modul_.htm

|

Scannerverarbeitung [Modul]

Stand 06.09.2018

(V4.86)

Grundsätzliches

Ein Strichcode- Scanner dient lediglich dazu, Daten im Speicher zu sammeln statt die Lagerentnahmen auf einen Zettel zu schreiben. Während der Zettel irgendwann abgeschrieben wird, muss der Scanner seine Daten zunächst im Rechner ablegen und die Artikel auf die jeweiligen Projekte oder Kundendienstaufträge zu verteilen. Dazu muss beim Scanner zunächst (als erstes!) die Projektnummer oder die KD-Auftragsnummer eingetragen oder gescannt werden. Erst danach werden die Artikeletiketten gescannt.

Auch beim Funkscanner, bei dem die Datenübertragung in den Rechner unmittelbar nach dem Scannen erfolgt, muß als erstes jeweils die Projekt oder Auftragsnummer eingetragen werden.

Erforderliche Einrichtungsarbeiten

Zunächst muss im Modul EINSTELLUNGEN unter den Menüpunkten ‚Programmbereiche‘, Strichcode-Scanner‘ die Scannerverarbeitung aktiviert werden. Dort wird auch festgelegt, ob die Daten unmittelbar nach dem Einlesen zur Prüfung angezeigt werden sollen oder nicht. Bei der Anzeige können auch Änderungen durchgeführt werden, so dass diese Funktion besonders am Anfang sehr sinnvoll ist. Man kann damit die eigenen Daten prüfen und versteht leichter, was man falsch gemacht hat. Die Übernahme läuft sonst im Hintergrund ab und wenn etwas nicht klappt, ist es schwierig, die Ursache zu finden.

|

Bitte beachten Sie, dass die Etiketten bei Label in einer bestimmten Art bedruckt werden sollten. Bereits auf den Waren befindliche Strichcodes bergen ggf. Probleme, da Labelwin dann nicht weiß, in welchem Großhändlerkatalog gesucht werden muss. In den von Label gedruckten Etiketten ist die interne Katalognummer enthalten.

Scannen allgemein

Obwohl der im folgenden beschriebene Vorgang bei den verschiedenen Scannern etwas unterschiedlich ist, geht es im Prinzip immer um die gleichen Vorgänge: Zunächst muss die Projekt- oder Auftragsnummer im Scanner eingetragen werden, danach wird die Artikelnummer gescannt und die Menge eingetragen. Bei einer Menge von 1 kann auf die Eingabe der Stückzahl verzichtet werden. Die Struktur der Scannerdatei sehen Sie weiter hinten.

UGS-Dateien

Im folgenden ist immer wieder von UGS-Dateien die Rede. Dies ist eine Datei, in der in einer bestimmten Art und Weise Artikel und Mengen abgelegt werden können. UGS-Dateien werden oft auch von Technischen Programmen erzeugt, um Daten in die Kaufmännischen Programme zu übernehmen.

Da Labelwin ohnehin schon seit langem solche UGS-Dateien einlesen kann, legt auch unsere Scannerlösung die Daten in dieser Form ab. In der Maske des Artikelaufrufes kann man dann über den Menüpunkt ‚UGS_Datei einlesen’ die Daten in eine Rechnung, Bestellung oder Lieferschein übernehmen.
