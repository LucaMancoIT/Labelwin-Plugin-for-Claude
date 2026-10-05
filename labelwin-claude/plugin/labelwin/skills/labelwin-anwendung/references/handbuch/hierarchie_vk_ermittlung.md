# Hierarchie VK-Ermittlung

Pfad: Dokumentenbearbeitung > Dokumentenerstellung [3] > Kalkulationseinstellung > Hierarchie VK-Ermittlung
Quelle: handbuch/hierarchie_vk_ermittlung.htm

|

Hierarchie VK-Ermittlung

Je nach eingetragener Einstellung kann der VK (Verkauf) über unterschiedliche Wege ermittelt werden. In den folgenden Beispielen rechnen wir immer mit dem Einkaufspreis (EK) als Basis. Genau die gleiche Rechnung würde mit dem Listenpreis erfolgen, wenn dieses bei "Preisbildung über" [Nr.10] angewählt wäre.

1. Priorität hat bei eingeschaltetem Vorrang ein fester Verkaufspreis, wenn bei den Artikelstammdaten einer hinterlegt ist.

[Bild]

2. Priorität hat ein gewählter Gruppenrahmen ‚Kleinteile’ oder ‚Handelspanne’(Nr.19). Je nach dort hinterlegten Stufen kann der Preis mit einem solchen Multi gerechnet werden.

Beispiel: EK = 7,00 €, Kleinteilefaktura Gruppenrahmen ‚Normal’.

[Bild]

Einstellungen: Mat.VK = 7,00 € * 1,80 = 12,60 €

Da diese Beispieltabelle bei 50,00 € endet, findet sie bei Preisen über 50,00 € Einkauf keine Anwendung.

|

Hinweis: Die Werte für den Gruppenrahmen werden im Modul EINSTELLUNGEN <Grundeinstellungen> <Kalkulationsgruppen> <bearbeiten Kleinteilefaktura> festgelegt.

Bei der Berechnung mit Handelspannen handelt es sich um eine Alternative zur Kleinteilefaktura. Während bei der Kleinteilefaktura der Zuschlagsfaktor von der Höhe des Einkaufpreises abhängt, wird ein Multi bei der Methode mit der Handelspanne, also der Differenz zwischen Listenpreis und Einkaufspreis gebildet. Je nach Wunsch, kann der Multi auf den Listenpreis oder den Einkaufspreis wirken.

Wenn Sie einen Multi auf den Listenpreis nutzen wollen, so wird er bei niedrigerem Rabatt oder keinem über 1 gehen, bei hohen Rabatten unter 1. Diese Methode bezieht den auf dem Markt bekannten Listenpreis mit ein und bestimmt den Multi über die Ihnen gewährte Handelsspanne.

Wenn Sie dagegen mit einem Multi auf den Einkaufspreis arbeiten, so muss er immer über 1 liegen.

[Bild]

Wenn Sie in der Kalkulationseinstellung Preisbildung über Listenkreis, Vorrang Festpreis Verkauf 1 und Handelsspanne Standard ausgewählt haben, ergibt sich folgendes Rechenbeispiel:

Der Listenpreis beträgt 3,82. Aufgrund des eigenen Rabatts von 79,06% greift der in der Zeile bis 80% hinterlegte Multi 0,5.

Listenpreis 3,82 € x Multi 0,5 = Material-VK 1,91 €

|

Hinweis: Die Werte für den Gruppenrahmen werden im Modul EINSTELLUNGEN <Grundeinstellungen> <Kalkulationsgruppen> <bearbeiten Handelsspanne> festgelegt.

3. Priorität hat ein gewählter Gruppenrahmen ‚Material’ (Nr.18). Dort können Kalkulations-materialgruppen mit 4stelligen Bezeichnungen hinterlegt werden. Wenn der aufgerufene Artikel mit seiner Kalkulationsgruppe im Gruppenrahmen vorhanden ist, wird der dort hinterlegte Faktor verwendet. Falls der Faktor auf 0 steht, wird der allgemeine Materialmulti (Nr. 8) verwendet.

Beispiel: Der Artikel gehört zur Kalkulationsgruppe ‚Porz’

EK = 85,00 € - eingeschalteter Gruppenrahmen ‚FremdLV’

[Bild]

Der Einkaufpreis wird mit 1,30 multipliziert, also 85,00 € * 1,30 = 110,50 €

4. (und letzte) Priorität hat der normale Materialmulti.
