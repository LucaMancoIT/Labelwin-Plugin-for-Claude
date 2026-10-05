# 1.1 Maske Scannerverarbeitung (alt)

Pfad: Materialwirtschaft > Scannerverarbeitung [Modul] > 1. Maske Scannerverarbeitung > 1.1 Maske Scannerverarbeitung (alt)
Quelle: handbuch/1_1_maske_scannerverarbeitung__alt_.htm

|

1.1 Maske Scannerverarbeitung (alt)

Hinweis: Die auf dieser Seite beschriebene Maske ist nur noch bei Kunden im Einsatz, die ein älteres Scannermodell einsetzen. Bei aktuellen Geräten (ab ca. 2014) wird in der Regel die aktuelle Oberfläche eingesetzt.

Das Aussehen der im Folgenden beschrieben Maske ändert sich je nach gewähltem Scannertyp.

[Bild]

1 Ändern-Knopf: Betätigen Sie den Knopf ‚Ändern’, damit Sie den bei Ihnen eingesetzten Scannertyp einstellen können. Erst dann sind Eingaben im Bereich 2,3 und 4 möglich.

2 Einstellung Dieser Knopf ist nur beim Formula-Scanner sichtbar. Die Einrichtung lesen Sie am Ende dieses Handbuches.

3 Scannertyp: Stellen Sie hier bitte den von Ihnen verwendeten Scanner ein. Bevor Sie sich einen Scanner anschaffen beachten Sie bitte, dass Label nicht alle unterstützt.

4 Pfad und Datei: Je nach Scannertyp müssen Sie hier ggf. einen Datenpfad oder auch den Comm-Port wählen.

5 Prüfunterbrechung und Fehlermeldungen: Die Prüfunterbrechung ist nur dann sinnvoll, wenn Sie sich unsicher sind, ob Sie alles richtig gescannt und die richtigen Mengen eingegeben haben. Nach dem Auslesen des Scanners bzw. der Erzeugung der von Labelwin zu verarbeitenden Datei hält das Programm an und Sie können die Daten betrachten und ggf. auch ändern.

Wenn Sie die Optionen ‚Anhalten wenn ...’ angewählt haben, wirkt dies wie die Prüfunterbrechung, aber halt nur bei Fehlern. Ansonsten läuft das Programm einfach durch.

Eine Datei mit Fehlern kann z.B. so aussehen:

[Bild]

Die Fehlerstellen sind mit einem Stern gekennzeichnet. Bei einer manuellen Korrektur brauchen Sie nicht darauf zu achten, dass die senkrechten Striche wieder untereinander stehen, aber Sie dürfen die Striche nicht weglöschen.

6 Lagerdokumente:

Keine Dokumente anlegen: Alle Daten werden je Projekt oder Kundendienstauftrag in einer UGS-Datei angelegt.

an offene Lagerentnahmen anhängen: Bei dieser Option geht es darum, dass die gescannten Artikel automatisch dem Projekt zugeordnet werden können. Die Automatik funktioniert nur dann, wenn in dem entsprechenden Projekt ein Dokument der Art ‚Lagerentnahme’ mit dem Dokumentenstatus ‚Offen’ vorhanden ist. In diesem Fall werden die Artikel ohne den Umweg über eine UGS-Datei sofort in dem Dokument angehängt. Wenn bei gesetztem Kreuz ein Projekt nicht existiert oder kein Dokument ‚Lagerentnahme’ vorhanden ist, schadet dies nicht. In diesem Fall wird einfach eine UGS-Datei mit dem entsprechenden Namen angelegt, die später manuell übernommen werden kann.

Jeweils neue Lagerentnahmen anlegen: Wenn dieser Punkt aktiv ist, wird für jedes gescannte Projekt oder Kundendienstauftrag eine neue Lagerentnahme angelegt. Sollte das Projekt oder die Auftragsnummer nicht existieren (Schreibfehler) so wird auch hier eine UGS-Datei angelegt.

7 Lagerabbuchung: Dieses Ankreuzfeld ist nur sichtbar, wenn Sie das Lagermodul im Einsatz haben. Wenn Sie es setzen müssen Sie festlegen, von welchem Lager Sie die Artikel abbuchen möchten. Das kann natürlich nur das Lager sein, in dem Sie auch gescannt haben.

8 Lieferscheine sofort ausdrucken: Dieses Ankreuzfeld ist nur sichtbar, wenn Sie im Einstellprogramm entsprechende Einrichtungsarbeiten vorgenommen haben. Diese lesen Sie im nächsten Kapitel Lagerentnahme als Lieferschein drucken.

9 Katalog, falls Artikelnummer ohne Katalog-Kennzeichen: Wenn der Strichcode der Artikel mit Labelwin gedruckt wird, setzen wir vor die eigentliche Nummer die interne Katalognummer in 2 Stellen, gefolgt von einem Punkt. Beispiel: Artikel HTB10045 aus Katalog mit interner Nummer 8 wird mit 08.HTB10045 als Strichcode gedruckt. Diese Logik ist bereits in den Labelwin-Formularen fest eingebaut. Wenn Artikelnummer ohne dieses Katalogkennzeichen gedruckt werden oder auf den Artikeln Original-EAN-Codes gedruckt sind, kann dieser in den Labelwin-Stammdaten nicht eindeutig zugeordnet werden. Durch diese Eingabe verhält sich Labelwin so, dass jeder Artikel ohne Katalog-Kennzeichen automatisch das hier eingestellte bekommt.

10 Knopf Übernahme starten: Wenn Sie die erforderlichen Einstellungen getroffen haben, lösen Sie hiermit die Datenübernahme aus. Je nach Art der Daten und getroffener Einstellung werden nun die Artikel direkt in ein Lagerdokument eingesetzt oder je Projekt / Auftrag wird eine UGS-Datei erzeugt. Sollte von einem vorherigen Scanvorgang bereits eine UGS-Datei vorhanden sein, wird an diese angehängt. Die UGS-Dateien werden erst bei der Übernahme in ein Dokument gelöscht.

|

|

Übernahmen

|

|

Übernahme der Daten in ein Lagerentnahme-Dokument

Hintergrund dieser Funktion ist, dass manche Kunden relativ viele Materialien vom Lager entnehmen und nicht speziell einkaufen. Die Belastung der Baustelle mit den Kosten erfolgt also über die Lagerentnahmen. Dabei ist es übrigens egal, ob unsere Lagerwirtschaft genutzt wird oder nicht. Auch ein Ausdruck der Lagerentnahmen ist nicht erforderlich. Schon das Vorhandensein eines Dokumentes mit dieser Art führt dazu, dass die Einkaufswerte (!) der Artikel in diesem Dokument die Baustelle belasten. In der Projektübersicht werden die Kosten der Lagerentnahme separat angezeigt.

Bei einer Übernahme der Artikel in ein Lagerentnahme- Dokument erfolgt die Eintragung schon beim Auslesen der Daten und es wird keine UGS-Datei erzeugt. Bei dieser Option geht es darum, dass die gescannten Artikel automatisch dem Projekt zugeordnet werden können. Je nach Einstellung funktioniert die Automatik funktioniert ggf. nur dann, wenn in dem entsprechenden Projekt ein Dokument der Art „Lagerentnahme“ mit dem Dokumentenstatus ‚Offen’ vorhanden ist. Bei dieser Option werden die Artikel immer dann in eine UGS_Datei geschrieben, wenn kein Lagerentnahmedokument existiert.

Wenn Sie die jeweilige Neuanlage von Lagerentnahmedokumenten angewählt haben, erfolgt nie die Übergabe in UGS-Dateien, sondern immer in jeweils neue Dokumente.

Man muss also dabei keine weiteren Tätigkeiten vornehmen. Falls es sich nicht um einen pauschal abzurechnenden Auftrag handelt, muss man allerdings daran denken, aus dem Lagerentnahme-Dokument irgendwann eine Rechnung zu entwickeln.

|

|

Übernahme der Daten in eine UGS-Datei

In allen anderen Fällen wird eine sogenannte UGS-Datei erzeugt, die in dem Bereich des Artikelaufrufes übernommen werden kann. Eine UGS-Datei enthält im Wesentlichen nur eine Menge, ein Katalogkennzeichen und eine Artikelnummer. Die Zugehörigkeit zu einem Projekt oder einem Kundendienstauftrag ist nur über den Namen der UGS-Datei festzulegen. Die UGS-Dateien liegen bei Labelwin üblicherweise auf der lokalen Festplatte C: im Verzeichnis UGS . Nach der Übernahme der Daten in ein Dokument wird die jeweilige Datei automatisch gelöscht.

|

|

Übernahme Kundendienst-Rechnung

Wenn es sich um eine Rechnung für einen Kundendienstauftrag handelt, kann die UGS-Datei an der Stelle, an der die Artikel aufgerufen werden, mit der Tastenkombination STRG F11 oder über das Menü mit ‚Schnittstellen’, ‚KD-Auftrag’, ‚Scannerdaten’ übernommen werden. In diesem Fall ist keine manuelle Auswahl mehr erforderlich, weil Labelwin die Auftragsnummer mit dem Namen der UGS-Datei vergleicht und die passenden Daten automatisch findet.

|

|

Übernahme Projekt / Bestellung, Lieferschein

Beginnen Sie ein neues Dokument oder aktivieren Sie ein schon vorhandenes, in das Sie die UGS-Daten einfügen möchten. Sorgen Sie dafür, dass die richtige Kalkulationseinstellung aktiv ist, da die Übernahme ohne Halt auf einen Rutsch erfolgt.

Die Übernahme kann historisch bedingt an 2 Stellen im Programm erfolgen. Nutzen Sie die schnellere Methode in der Maske, in der Sie die bereits übernommenen Artikel sehen, unter dem Menüpunkt ‚Vorlagen’, ‚UGS-Datei übernehmen’ . Der gleiche Punkt ist unter der Maske Artikelaufruf zu finden, läuft aber wesentlich langsamer ab.

Wählen Sie aus der Liste der angebotenen UGS-Datei die richtige Datei aus. Wenn Sie einmal aus Versehen die falsche Datei gewählt haben, übertragen Sie die übernommenen Daten in ein anderes Dokument, bevor Sie sie löschen. Da die UGS-Datei direkt nach der Übernahme gelöscht wird, wären die Daten sonst verloren.

Bei der Übernahme von Artikeln, die nicht im Artikelstamm des Labelwin-Programms vorhanden sind, wird hierzu ein Artikel übernommen mit dem Hinweis ‚Artikelnummer Renova fehlt in Händlerkatalog Kata2.mdb’ mit der entsprechenden Stückzahl. Diese ‚fehlenden Artikel’ erscheinen jedoch nur, wenn die Übernahme unter dem Punkt ‚Vorlagen’, ‚UGS-Dateien übernehmen’ erfolgt.
