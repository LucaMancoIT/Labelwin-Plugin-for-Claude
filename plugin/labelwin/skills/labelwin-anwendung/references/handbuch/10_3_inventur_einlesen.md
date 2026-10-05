# 10.3 Inventur einlesen

Pfad: Materialwirtschaft > Lager [Modul] > 10. Inventur > 10.3 Inventur einlesen
Quelle: handbuch/10_3_inventur_einlesen.htm

|

10.3 Inventur einlesen

Um den Lagerbestand mit Hilfe des Aufmaßtextes zu aktualisieren, wählen Sie in der Lagerhauptmaske den Menüpunkt <Inventur> <Inventurtext einlesen>. Es werden die Stückzahlen des Dokumentes als Bestand eingetragen. Bei Abweichungen zum vorherigen Bestand wird die Differenz als Inventur-Korrektur eingetragen.

Über diesen Weg lassen sich auch noch nicht vorhandene Artikel automatisch auf dem Lager anmelden.

[Bild]

Bild: Inventur einlesen

[Bild]

1 Lager: Wählen Sie hier das Lager, dessen Bestände mit dem Dokument aktualisiert werden sollen.

[Bild]

2 Verkaufspreis als EK bewertet übernehmen: Hier kann ein bewerteter EK im Lager eingetragen werden.

Beispiel: Ein Artikel hat einmal 3,00 € gekostet. Er wurde jedoch nicht verkauft und liegt nun als „Ladenhüter“ am Lager. Sie bewerten diesen Artikel nun mit 1,50 €. Tragen Sie diesen Wert im Inventurtext als VK ein. Wenn Sie dieses Feld aktiviert haben, wird dieser Wert als bewerteter EK im Lager eingetragen.

[Bild]

3 Positionsnummer als Lagerfach verwenden: Bei einem Dokument kann in das Feld der Positionsnummer die Beschreibung des Lagerfaches eingesetzt werden. Bei aktiviertem Feld wird das Fach automatisch eingetragen, wenn es sich um einen neuen Artikel handelt oder bei bereits im Lager angelegten Artikeln, wenn das Feld bisher leer war.

[Bild]

4 Menge zu vorhandenem Bestand addieren: Wenn Sie dieses Feld aktivieren, wird die Menge Ihres Inventurtextes zum vorhandenen Bestand addiert. Das macht nur dann Sinn, wenn Sie mehrere Inventurdokumente haben, in denen gleiche Artikel vorkommen. Ohne diese Option würde das 2.Dokument die Mengen des ersten vernichten. Bei dieser Methode müssen aber vor dem ersten Einlesen alle Bestände auf Null gesetzt werden. Das geschieht unter dem Menüpunkt <Inventur> <Bestände auf 0>

[Bild]

5 Gruppenzuordnung für automatisch angelegte Artikel: Wählen Sie hier die Gruppe aus, zu der automatisch angelegte Artikel zugeordnet werden sollen.

[Bild]

6 Fehlende Artikel anlegen: Falls in Ihrem Inventurdokument Artikel enthalten sind, die bisher noch nicht im Lager angemeldet sind, so legen Sie hier fest, ob diese angelegt werden sollen. Unsere Empfehlung lautet, diese automatisch anlegen zu lassen.

[Bild] 7 Ggf. im Lager anmelden: Jeder Lagerartikel bekommt eine eigene Lagerartikelnummer. Im Normalfall wird als Lagerartikelnummer die Katalog-Artikelnummer des Großhändlers benutzt.

Existiert im Lager keine Verknüpfung für diese Katalog-Artikelnummer, dann wird automatisch ein neuer Lagerartikel angelegt. Dabei ist die Lagerartikelnummer die gleiche wie die Katalog Artikelnummer.

Existiert bereits ein Lagerartikel mit dieser Lagerartikelnummer gibt, dann wird ein neuer Lagerartikel angemeldet. Die Lagerartikelnummer ist die Katalog-Artikelnummer gefolgt von einem Bindestrich und einem fortlaufenden Zähler. Meist 1, aber wenn es die Nummer schon gibt, dann 2 oder 3 etc. Ist die Katalog-Artikelnummer länger als 11 Zeichen, dann lautet die Lagerartikelnummer ‚AUTO-' gefolgt von der nächsten verfügbaren fortlaufenden Nummer.

Wenn Sie dieses Feld aktivieren, wird davon ausgegangen, dass dieser Lagerartikel der passende Artikel ist. Allerdings wurde er mit einem anderen Katalog, der das gleiche Nummernsystem benutzt, verknüpft. In diesem Fall wird einfach eine neue Verknüpfung mit diesem Katalog erzeugt.

Diese zweite Methode ist eigentlich nur dann sinnvoll, wenn Sie für den gleichen Großhändler mehrere Labelwin Kataloge definiert haben.

Beispiel: Sie haben die Kataloge ‚Cordes&Gräfe alt’ und ‚Cordes&Gräfe neu’. Im Lager existiert Artikel ‚EV’, der mit dem Artikel ‚EV’ aus dem alten Katalog verknüpft ist. Jetzt lesen Sie ein Inventurdokument ein, das Sie mit dem neuen Katalog erstellt haben. Dann wird lediglich eine weitere Verknüpfung erstellt.

Gehen Sie daher mit dieser Option vorsichtig um.

[Bild]

8 Tabelle: Markieren Sie hier das Dokument, der die Inventurbestände enthält.

[Bild]

9 Löschen: Das in der Tabelle markierte Dokument wird nach einer Sicherheitsabfrage gelöscht.

[Bild]

10 Bearbeiten: Das in der Tabelle markierte Dokument wird in Bearbeitung genommen.

[Bild]

11 Einlesen: Mit diesem Knopf wird die Übertragung der Inventurbestände in die Lagerverwaltung gestartet. in der Tabelle markierte Text wird in Bearbeitung genommen.

[Bild]

12 Ende: Mit diesem Knopf wird die Maske geschlossen.
