# UGS und Megabild

Pfad: Dokumentenbearbeitung > Dokumentenerstellung [3] > UGS und Megabild
Quelle: handbuch/ugs_und_megabild.htm

|

UGS und Megabild

UGS-Schnittstelle

Eine UGS-Datei ist sinngemäß eine Liste, in der für jede Position nur die Menge, Artikelnummer und ein Verweis auf eine (Händler-)Katalognummer eine Zeile eingetragen ist. Bei der Übernahme werden alle Artikel der UGS-Datei aufgerufen und gemäß der aktuellen Kalkulationseinstellung kalkuliert. Die UGS-Datei ist ursprünglich zur Übernahme der Daten aus dem Katalogauswahlprogramm ‚Digis’ entstanden und wird mittlerweile auch von vielen anderen Programmen genutzt. Einige technische Programme wie CONSOFT, HT2000 nutzen auch diese Schnittstelle. Der Nachteil der Schnittstelle ist, dass sie keinen Artikeltext enthält und daher immer der Artikel aus einem Katalog aufgerufen werden muss.

Bei Labelwin werden vom Strichcode-Scanner UGS-Dateien erzeugt, die beim Projektbereich hier einzulesen sind. Im Programm KATALOGE können unter den Preislisten UGS-Dateien erzeugt werden, die hier zur Erzeugung eines Inventurtextes oder zur Vorbereitung der Lageraufnahme in ein Dokument eingetragen werden können. Üblicherweise werden die UGS-Dateien lokal auf der Festplatte C: im Verzeichnis UGS abgelegt.

Bei nicht gefundenen Artikeln erfolgt ein Hinweis, bei dem Sie am Besten nicht gefundene Artikel aufschreiben. Nach der Übernahme wird die UGS-Datei nämlich automatisch gelöscht.

Datenstruktur einer UGS-Datei: Eine UGS-Datei lässt sich sehr einfach mit dem Notepad kontrollieren. Sie muss die Dateiextension .ugs haben Sie hat eine Satzbreite von 32 Zeichen, gefolgt von einer Zeilenschaltung (Carriage Return). Die Dateilänge ist also durch 34 teilbar.

Der erste Satz beginnt manchmal mit V... und kann Informationen enthalten, die für uns unwichtig sind. Wenn er vorhanden ist, wird er von Labelwin ignoriert.

Die eigentlichen Informationen beginnen immer mit A, einer Leerstelle, 4 Stellen für die Katalognummer (manchmal mit Nullen aufgefüllt), 15 Stellen für die Artikelnummer, 8 Stellen für die Menge mit den letzten 3 Stellen für die Nachkommastellen.

Beispiel: c:\ugs\muster.ugs

A 3WTREN60 00001000

A 0082CUR15 00002450

Mit dem ersten Satz wird 1 Artikel WTREN60 aus dem Katalog 3 übergeben, mit dem zweiten Satz 2,45 Artikel CUR15 aus dem Katalog 82.

Megabild

Leider gibt es zwei verschiedene Bereiche, die allgemein beide als Megabild-Schnittstelle bezeichnet werden. An dieser Stelle geht es darum, bei eingelegter CD eines Großhändler und gestartetem Programm der CD Artikeldaten zu übernehmen, die aus dem Bild-Auswahlprogramm kommen.

Um Daten aus dem Megabildsystem übernehmen zu können, muss zunächst das Megabild-Programm entsprechend eingerichtet sein. In dem Programm muss unter dem Menüpunkt <Option> die DDE-Schnittstelle freigeschaltet sein. In dem Auswahlmenü werden diverse Programmschnittstellen angeboten, so z.B. Word, Excel usw. Sie müssen für die Übernahme in unser Programm die DDE-Schnittstelle anwählen.

Wenn Sie stattdessen die UGS-Schnittstelle benutzen möchten, lesen Sie bitte unter UGS-Schnittstelle nach.

Daten übernehmen:

Holen Sie sowohl das Megabild-Programm als auch unser Programm an die Oberfläche. Wählen Sie in unserem Programm in der Maske, in der Sie die Artikel aufrufen, den Menüpunkt <Schnittstellen> <Megabild mit Stop> an. ‚Mit Stop’ bedeutet, dass der aus Megabild übernommene Artikel in die Kalkulationsmaske übernommen wird und Sie Änderungen durchführen können. ‚Ohne Stop’ würde bedeuten, dass der Artikel sofort in das zu erstellende Dokument übernommen wird. Da leider die meisten Versionen von Megabild die Menge nicht richtig übergeben haben, empfehlen wir den Menüpunkt <Megabild mit Stop> zu verwenden. Außerdem haben Sie an dieser Stelle auch noch die Möglichkeit, die Preise, Mengeneinheiten und dergleichen zu verändern.

Wenn Sie im Megabild einen Artikel ausgewählt haben, markieren Sie diesen und betätigen die Tastenkombination CTRL + W. Dadurch wird der Artikel in unsere Kalkulationsmaske geschrieben und kann wie gewohnt mit dem OK-Knopf in das Dokument übernommen werden.
