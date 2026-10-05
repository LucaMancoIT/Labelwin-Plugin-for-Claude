# 1. Einleitung

Pfad: Artikelstammdaten > Katalog [10] > 1. Einleitung
Quelle: handbuch/1__einleitung_2.htm

|

1. Einleitung

In diesem Programmteil findet das Einspielen von Artikelkatalogen, deren Namensvergabe, das Einspielen von Preisänderungen, Rabattgruppen usw. statt. Nach dem Start muss immer zunächst ein Artikelkatalog gewählt werden. Wenn Sie einen neuen Katalog einspielen wollen, können Sie irgendeinen Katalog wählen oder den Abbruch-Knopf anklicken.

[Bild]

Bild: Liste der bisherigen Kataloge

Die Artikelkataloge werden in jeweils einer eigenen Datenbank abgelegt. Dabei ist die Namensvergabe des Kataloges (in der Regel der Großhändlername) im Prinzip unabhängig von dem eigentlichen Katalog. Die Kataloge befinden sich auf der Festplatte in dem Unterverzeichnis Datanorm und haben den Namen KATA1, KATA2 .... Durch dieses Konzept ist es möglich, sehr schnell einzelne Kataloge wieder zu entfernen. Beim späteren Artikelaufruf sind die Kataloge miteinander verknüpfbar, so dass bei Eingabe einer Artikel-Nr./Suchbegriff über mehrere Kataloge nacheinander gesucht werden kann. In der Datenbank mit dem Namen KATA... befinden sich alle zu dem jeweiligen Großhändler vorhandenen Informationen; also neben den eigentlichen Artikeldaten auch die Rabattgruppe, Warengruppe usw.

Einspielen eines Großhändlerkataloges:

Wenn Sie einen neuen Großhändlerkatalog einspielen wollen, so ist es sinnvoll eine bestimmte Reihenfolge einzuhalten. Um einen neuen Katalog einzuspielen muss er zunächst angelegt werden. Dies geschieht unter dem Menüpunkt <Katalog> <Neuer Katalog>. Bei der Namensvergabe wird eine leere Datenbank angelegt. Zunächst ist zu klären, ob der Großhändler mit Rabattlisten arbeitet und ob die Einkaufspreise per Diskette übergeben werden. Falls mit Rabattlisten gearbeitet wird, so sollte diese unbedingt als erstes eingerichtet werden. Wenn die Rabattliste beim Einspielen der eigentlichen Artikeldaten vorhanden ist, so rechnet das Programm ‚nebenher’ Ihre Einkaufspreise aus. Sollte die Rabattliste nicht sofort vorhanden sein, so müssen mit einem späteren Durchlauf die Einkaufspreise ermittelt werden.

Exkurs: Die Datanorm-Versionen

Da es in der Vergangenheit immer mal wieder Probleme mit den Herstellern der Datanorm gab, haben wir hier einmal die wichtigsten Merkmale dargestellt.

Um eine Datanorm einzuspielen, brauchen Sie das nicht zu wissen – unser Programm erkenn beim Einspielen die Version automatisch.

Das Programm kann sowohl mit der Datanorm . Datanorm 4.0 und Datanorm 5.0 umgehen. Die Datanorm 3 und 4.0 unterscheiden sich nach außen hin durch unterschiedliche Dateibezeichnungen. Bei der älteren Version Datanorm 3 gibt es 3 verschiedene Arten von Dateien:

Datanorm Version 3

1. DATANORM:

Enthält in der Regel die eigentlichen Artikeldaten. Darüber hinaus werden auch Rabattgruppen oder Warengruppen in einer Datei mit dem Namen Datanorm abgelegt. Um sie dennoch eindeutig unterscheiden zu können, ist es zwingend erforderlich, dass bei der Datanorm 3 die Rabattgruppen und Warengruppen jeweils auf einer getrennten Diskette oder bei einer CD in einem sepraten Verzeichnis untergebracht werden. Der Datenlieferant hat diese in der Regel entsprechend beschriftet.

2. DATPREIS:

Enthält lediglich Brutto- oder Nettopreise. Die Artikel müssen vor Einspielen einer DATPREIS-Diskette bereits angelegt sein.

3. DATASETS:

Mit dieser Dateiform können Sammelartikel wie z.B. Kesselanlage + Abgasrohr + Steuerung usw. übertragen werden. Sets-Dateien sind sehr wenig verwendet worden, weil kaum ein Großhändler/Lieferant sich die Mühe gemacht hat die Artikel entsprechend zusammenzustellen.

Datanorm Version 4.0 und 5.0

Bei diesem Format werden wesentlich weniger Disketten benötigt, da die einzelnen Informationen lediglich durch ein Semikolon ( ;) voneinander getrennt sind, während bei der Datanorm 3 die Daten immer mit Leerstellen aufgefüllt wurden. Die Namen der Datanormversion 4.0 sind eindeutig geworden, so dass es jetzt auch möglich ist Rabattgruppen, Warengruppen, Artikeldaten und Preisdateien auf einer Diskette/CD zu übertragen.

1. DATANORM.001 bis DATANORM.999:

In diesen Dateien sind die eigentlichen Artikelinformationen abgelegt. Sollten auf einer Diskette/CD mehrere dieser Dateien vorhanden sein, so hat der Lieferant in der Regel eine Trennung nach Artikelgruppen (z.B. Heizung/Sanitär/Ersatzteile o.ä.) vorgenommen. Lesen Sie hierzu unbedingt die entsprechenden Beschreibungen des Lieferanten. Leider haben viele Datanorm-Lieferanten Probleme beim Lesen des Datanorm-Handbuches - wir stoßen immer wieder auf Disketten, bei denen die Datei ‘DATANORM.´ statt ´DATANORM.001´usw heißt. Schauen Sie in die Datei hinein und wenn Sie viele Semikolons (;) vorfinden, benennen Sie sie in ´DATANORM.001´ um.

2. DATPREIS.001 bis DATPREIS.999:

Wie bei der Datanorm 3 sind hier die Brutto- oder Nettopreise hinterlegt. Vor dem Einspielen der DATPREIS-Diskette müssen die Artikel auf dem Rechner angelegt worden sein.

3. DATANORM.RAB:

Hierin ist die Rabattgruppenliste hinterlegt. Bei Vorhandensein dieser Datei sollte sie unbedingt als erstes eingespielt werden, da dann die Einkaufspreise beim Einspielen der Datanorm direkt ausgerechnet werden können.

4. DATANORM.WAR:

Diese Datei enthält die Warengruppen und braucht in unser System nur dann eingespielt zu werden, wenn Sie aufgrund der Warengruppen Zuordnungen wir z.B. Kalkulationsgruppen treffen wollen.

5. DATASETS.001 bis DATASETS.999:

Wie bei der Datanorm 3 sind hier Artikelsets zusammengestellt. Diese Dateiform findet bisher wenig Einsatz.

Datanorm Version 5.0

Der einzige relevante Unterschied ist, dass mit dieser Version auch Bilder transportiert werden können. Allerdings ist keine ausreichende Klassifizierung vorhanden, so dass man weder die Bildgröße noch die Qualität sehen kann.

Transportwege der Datanormdateien

Neben dem klassischen Weg per CD bekommt man die Dateien oft auch über das Internet. Hier sind im Wesentlichen 2 Wege zu unterscheiden.

Weg 1

In diesem Fall muss man die Dateien herunterladen und irgendwo auf der Festplatte speichern. Dabei ist das „irgendwo“ genau das Problem, denn beim Verarbeiten im Labelwin werden Sie aufgefordert, den Ablagepfad der Dateien zu benennen oder auszuwählen. Dabei kommt es immer wieder vor, dass alte Dateien eingespielt werden, weil der Download nicht geklappt hat und dort noch die Daten vom letzten Download gespeichert waren.

Achten Sie auf das Datum der Dateien.

Weg 2

Nach entsprechender Einrichtung von „Datanorm per Web“ kann Labelwin die Daten abholen, verarbeiten und danach automatisch löschen.
