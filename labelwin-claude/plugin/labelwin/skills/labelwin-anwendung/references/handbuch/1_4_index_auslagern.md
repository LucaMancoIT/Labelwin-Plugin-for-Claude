# 1.4 Index auslagern

Pfad: Artikelstammdaten > Katalog [10] > 1. Einleitung > 1.4 Index auslagern
Quelle: handbuch/1_4_index_auslagern.htm

|

1.4 Index auslagern

Ein Katalog besteht immer zum einen aus den reinen Artikeldaten (Artikelnummer, Kurztext, Langtext, Preis etc.) und zum anderen aus dem sogenannten Volltextindex. Dieser ist wichtig, um Artikel bei der Suche auch dann zu finden, wenn die Artikelnummer nicht oder nicht komplett bekannt ist. Der Index kann bei großen Katalogen mehrere hundert Megabyte in Anspruch nehmen und sollte daher ausgelagert werden. Ansonsten wird die Maximalgröße einer Katalogdatenbank von 2 Gigabyte schnell erreicht.

Wird ein Katalog komplett neu angelegt, erfolgt die Auslagerung des Indexes automatisch. Bei Katalogen aus dem Bestand kann es aber erforderlich sein diese Auslagerung manuell anzustossen.

[Bild]

Die Katalogdatenbanken werden im Ordner \labelwin\datanorm\ verwaltet. Zu jedem Katalog gibt es nach der Splittung eine KATAX.mdb und eine KATAXidx.mdb. Sollten Sie einmal manuell einen Katalog sichern, kopieren oder zurücksichern wollen, müssen Sie immer beide Datenbanken berücksichtigen.
