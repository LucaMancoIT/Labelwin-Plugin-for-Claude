# Meta-Daten einspielen

Pfad: Schnittstellen > ZVEH und Meta-Daten > Meta-Daten einspielen
Quelle: handbuch/meta_daten_einspielen.htm

|

Meta-Daten einspielen

Über dieses System können Sie statt der ‚neutralen’ ZVEH-Stücklistenartikel Artikel Ihrer Großhändler einspielen. Dabei sind aber leider einige Dinge zu beachten, weil es nicht so einfach ist, wie man es erwarten würde. Mit der Meta werden alle Bestandteile der Sets ausgetauscht, da diese ggf. nicht eins zu eins umsetzbar sind. So kann es passieren, dass ein Set beim ZVEH aus 3 Artikeln besteht, während es beim Großhändler nur einer ist, der alle Komponenten enthält.

Da der uns vorliegende Meta-Katalog nicht alle Artikel des ZVEHs enthält, sondern es etwa 250 Sets weniger sind, sollten Sie den Katalog separat einspielen. Ebenfalls für die separate Einspielung spricht, dass die Listenpreise und Eks der Kataloge sich sehr unterscheiden, so dass man auch bei einer Vermischung nicht weiß woran man ist.

1) Legen Sie einen neuen Katalog mit dem Namen META am Anfang an und spielen von der META-CD alle Daten mit Datanorm und Datasets im Format 4.0 ein. Bitte beachten Sie, dass damit nicht die Meta-Daten von der ZVEH-Cd gemeint sind, sondern es eine separate CD von der Meta oder ggf. auch von Ihrem Grosshändler gibt. Das was auf der ZVEH_CD unter Meta abgelegt ist, wird von unserem Programm nicht verarbeitet.

[Bild]

[Bild]

DATANORM.001 Stücklistenartikel mit Listenpreis und Kennzeichen N=Neuanlage

DATANORM.002 Stücklistenartikel mit Listenpreis und Kennzeichen A=Pflegemerkmal

DATANORM.003 Stücklistenartikel mit Nettopreis und Kennzeichen N=Neuanlage

DATANORM.004 Stücklistenartikel mit Nettopreis und Kennzeichen A=Pflegemerkmal

DATANORM.005 Bauzeiten der Stücklistenartikel in AW (100er Teilung)

DATANORM.006 Bauzeiten der Stücklistenartikel in Minuten

DATASETS.001 Stückliste der Kalkulationshilfe

Auch hier dürfen sie die Datanorm.005 nicht einspielen, da diese wieder die Arbeitswerte enthält !

2) Wählen Sie bei aktivem Meta-Katalog die Menüpunkte ‚Bearbeiten, Sets bearbeiten, Set-Beschriftung kopieren’ an. Stellen Sie als Quellkatalog den ZVEH ein und starten die Übertragung. Damit werden die Langtexte der ZVEH-Sets und die hinterlegten Lohnminuten kopiert. Abgesehen von den schon erwähnten 250 Sets, die bei uns im ZVEH, nicht aber im vorliegenden Meta-Katalog waren, ist der ZVEH-Katalog nun überflüssig und sollte bei der späteren Artikelsuche nicht aktiviert werden.

[Bild]

3) Wenn dies nicht bereits geschehen ist, sollten Sie nun spätestens den Elektrokatalog Ihres Großhändlers einspielen, dessen Artikel Sie für die Kalkulation verwenden wollen.

4) Auch der Meta-Katalog ist in sich geschlossen organisiert. Eine Prüfung auf ggf. nicht vorhandene Set-Bestandteile ergibt, dass alle im aktiven Katalog, also Meta, vorhanden sind. Nun geht es darum, dass bei einem Set-Aufruf nicht die Bestandteile / Stücklistenartikel aus dem Meta-Katalog genommen werden, sondern möglichst aus dem Katalog Ihres Großhändlers und damit dessen Preise verwendet werden.

Wir haben deshalb eine Funktion programmiert, die den Verweis vom eigenen (Meta-)Katalog auf einen anderen Katalog umsetzt. Dies passiert nur dann, wenn der Artikel mit der gleichen Nummer auch im anderen Katalog vorhanden ist. Bei den uns zum Test vorliegenden Daten gab es etwa 3000 Artikel, deren Verweis auf Meta verblieb, also beim Großhändler nicht vorhanden waren.

Unserer Meinung nach sollten Sie solche Artikel, die nun von Meta auf den Großhändler verweisen, bei Meta löschen. Sonst kann es nicht passieren, dass Sie bei der übergreifenden Suche im Metakatalog und beim Großhändler jeweils einen Artikel mit der gleichen Nummer finden. Dabei ist der Meta-Artikel dann nicht preisgepflegt und eigentlich eine ‚Leiche’. Die Löschung veranlassen Sie durch ein Kreuz bei ‚umgesetzte Artikel im aktuellen Katalog löschen

[Bild]
