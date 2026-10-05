# 3.3 Rabattgruppen

Pfad: Artikelstammdaten > Katalog [10] > 3. Stammdaten bearbeiten > 3.3 Rabattgruppen
Quelle: handbuch/3_3_rabattgruppen.htm

|

3.3 Rabattgruppen

EK / VK neu rechnen

Diese Funktion erreichen Sie über den Menüpunkt <Bearbeiten> <Rabattgruppen> <EK/VK neu rechnen>

Hier werden anhand der Rabattliste die Preise der Artikel neu berechnet, die Sie in der Liste angewählt haben. Wenn Sie diese Funktion ausführen, muss eine Rabattliste vorhanden sein.

Sie haben hier auch die Möglichkeit den Durchlauf für eine einzelne Rabattgruppe zu starten. Hintergrund ist, dass Lieferanten ggf. sowohl mit Nettopreisen (Datpreis-Datei) als auch mit Rabattgruppen arbeiten. Beim Einlesen von Datanorm/Datpreis-Dateien rechnet Labelwin dann zunächst den EK aufgrund der Rabattgruppe und liest erst zuletzt die Datpreis mit den speziellen Nettopreisen ein. Das System mit gleichzeitiger Nutzung von Nettopreisen und Rabattgruppen birgt große Probleme, wenn später bei einer Rabattgruppe der Prozentsatz wechselt. Der ‚normale“ Durchlauf Rabatt rechnet alles wieder mit der Rabattgruppe und vernichtet damit dann ggf. spezielle Nettopreise.

[Bild]

Bild: Preise neu rechnen

Rabattgruppen bearbeiten

Sie gelangen in diese Maske über den Menüpunkt <Bearbeiten> <Rabattgruppen> <Bearbeiten>.

Über die Rabattgruppen werden in der Regel die Einkaufspreise ermittelt. Einige Großhändler arbeiten jedoch mit Nettopreisdateien und benötigen daher keine Rabattgruppen. Um die ganze Sache noch komplizierter zu machen, gibt es auch Großhändler, bei denen die meisten Artikel über Rabattgruppen gerechnet werden und zusätzlich über Nettopreisdateien Sonderpreise übertragen werden. In diesem Fall empfehlen wir Ihnen die Nettopreisdateien besonders gut aufzubewahren, da Sie bei einem eventuellen Wechsel eines Rabattsatzes per Durchlauf sämtliche Einkaufspreise neu rechnen und dann die Nettosonderpreise nochmals als letztes hinterher einspielen müssen.

Falls Ihr Großhändler Ihnen die Rabatte per Datei zur Verfügung stellt, sollten Sie diese unter dem Menüpunkt <Einlesen> <Rabattgruppen Datanorm> eintragen. In der Regel sind damit auch Ihre firmenspezifischen Rabattsätze übertragen. Falls Ihnen Ihr Großhändler lediglich ein Blatt mit allen verwendeten Rabattsätzen übergibt, müssten Sie diese per Hand erfassen. Wir haben Ihnen diesen Weg etwas erleichtert, indem Sie über den Menüpunkt <Bearbeiten> <Rabattgruppen> <Generieren> per Durchlauf alle verwendeten Rabattgruppen in die Liste bekommen. In diesem Fall müssen Sie in der Maske lediglich noch Ihre firmenspezifischen Prozentsätze eintragen. Wenn Sie diese Maske verlassen, bietet Ihnen das Programm die Möglichkeit, alle Einkaufspreise per Durchlauf zu ermitteln.

Wenn Sie Rabattsätze neu eingetragen oder geändert haben, müssen Sie per Durchlauf die Einkaufspreise neu rechnen lassen. Unser Programm arbeitet beim späteren Artikelaufruf immer mit den fertig gerechneten Einkaufspreisen und ermittelt ihn nicht mit Hilfe der Rabattgruppe während der Kalkulation, sondern im Vorhinein.

|

[Bild] Bild: Rabattgruppen bearbeiten

|

1 Liste: Hier werden alle vorhandenen Rabattgruppen angezeigt. In dieser Liste kann nicht geschrieben werden, sie dient nur der Anzeige.

2 Rabattgruppe: Schreiben Sie hier die verwendete Artikelgruppe hinein. Die Gruppen-bezeichnung kann maximal vier Zeichen haben und auch aus Buchstaben bestehen. In der Regel werden jedoch Zahlen verwendet.

3 Kalk.-Gruppe: Tragen Sie hier die Kalkulationsgruppe ein, zu der die Rabattgruppe gehört. Die Kalkulationsgruppen werden im Modul EINSTELLUNGEN unter dem Menüpunkt <Grundeinstellungen> <Kalkulationsgruppen> eingetragen.

4 Kostenstelle: Wenn Sie mit Kostenstellen arbeiten, können Sie bei der Rabattgruppe eine Kostenstelle hinterlegen. Dazu müssen im Modul EINSTELLUNGEN unter dem Menüpunkt <Grundeinstellungen> <Kostenstellen> die Kostenstellen eingetragen und aktiviert werden.

5 Bezeichnung: Auf die Eingabe der Beschreibung können Sie verzichten, da der Text nur zu Ihrer eigenen Information dient. Beim Generieren der Rabattgruppe wird hier der Text vom ersten gefundenen Artikel dieser Gruppe eingetragen.

6 Faktor: Tragen Sie hier den Multipultiplikar für die einzelnen Preise ein. Beim EK1 haben Sie die Wahl zwischen einem Rabattsatz und einem Multiplikator.

7 Artikel zeigen: Bei Anwahl werden alle Artikel mit der gerade markierten Rabattgruppe angezeigt. Geschaffen wurde diese Funktion, um bei den Rabattsätzen für die mobile offer-Stücklisten die betroffenen Artikel zu sehen, aber vielleicht ist die Funktion allgemein interessant

8 Neu: Mit Betätigen dieses Knopfes werden die Eingaben geleert und Sie können eine neue Rabattgruppe eintragen.

9 Löschen: Mit Betätigen dieses Knopfes können Sie eine in der Liste (Nr.1) markierte Rabattgruppe löschen.

10 Speichern: Mit Betätigen dieses Knopfes speichern Sie die vorgenommenen Änderungen oder eine neue Rabattgruppe ab.

|

11 Erfassung: Entscheiden Sie hier, wie Sie bei der Erfassung der Rabattgruppen die Einträge für den Faktor vornehmen möchten.

-

alle Werte: Sie können bei allen Werten einen Multi eintragen. Bei Einkauf 1 müssen Sie zwischen Rabattsatz oder Multi wählen.

-

nur Einkauf 1: Hier können Sie dann nur bei Einkauf 1 einen Rabattsatz oder Multiplikator einsetzen. Alle anderen Felder sind nicht anwählbar.

-

nur Multis: Hier können Sie bei allen Feldern einen Multi eintragen mit Ausnahme vom Einkauf 1. Dieses Feld ist nicht anwählbar.

12 Drucken: Durch Betätigen dieses Knopfes können Sie eine Liste der Rabattgruppen des aktuell gewählten Katalogs ausdrucken.

13 Ende: Durch Betätigen dieses Knopfes wird die Maske geschlossen und es erscheint folgendes Fenster:

[Bild]

Rabattliste generieren

Sie gelangen in diese Maske über den Menüpunkt <Bearbeiten> <Rabattgruppen> <Generieren>.

[Bild]

Bild: Rabattliste generieren

Wenn Ihnen Ihr Großhändler keine Rabattliste per Datei übergibt, können Sie hiermit eine Rabattliste erzeugen. In diese Liste müssen Sie dann anschließend Ihre individuellen Rabattsätze eintragen. Wir ersparen Ihnen durch diese Funktion die Mühe, alle Rabattgruppen per Hand einzugeben.

Bevor Sie die Rabattliste aus den Artikel-Stammdaten generieren können, müssen Sie selbstverständlich die Datanorm-Dateien eingespielt haben. Das Programm guckt bei jedem Artikel nach, ob dessen Rabattgruppe bereits in der Liste vorhanden ist. Bei nicht vorhandenen Rabattgruppen werden diese automatisch eingetragen. Als Beschreibungstext setzt das Programm die Artikelnummer des ersten gefundenen Artikels und den Anfang des Kurztextes ein.
