# 16. Rekonstruktion eines gelöschten Projekts

Pfad: Projektverwaltung > Projektverwaltung [2] > 16. Rekonstruktion eines gelöschten Projekts
Quelle: handbuch/16__rekonstruktion_eines_geloschten_projekts.htm

|

16. Rekonstruktion eines gelöschten Projekts

Hintergrund

Trotz vielfältiger Warnungen schaffen es Kunden immer mal wieder, ein Projekt zu löschen. Eigentlich kann es nicht passieren, da Sie beim Löschen eines Projekts nach der Anzahl der Dokumente des Projekts gefragt werden. Diese müssen Sie eintragen, bevor man überhaupt ein Projekt löschen kann. Die Löschung eines Projekts findet also ganz bewusst statt.

[Bild]

Labelwin verwendet ein Projekt als Ordner, in dem sich verschiedene Blätter (Angebote, Rechnungen, Bestellungen) befinden.

Ein Projekt zu löschen bedeutet also, einen kompletten Aktenordner zu vernichten!

Es gibt im Programm keine Möglichkeit, ein gelöschtes Projekt per Mausklick wieder herzustellen. Sie müssen in diesem Fall entweder die Datensicherung vom Vortag zurück holen, was u.U. bedeuten kann, dass die gesamte Arbeit des Tages verloren ist oder sich die Mühe machen, jedes einzelne Dokument in einen neuen Ordner zu packen.

Vorgehensweise

Dazu gehen Sie wie folgt vor:

Kopieren Sie sich von der Datensicherung (vor dem Löschdatum des Projekts) die Projdat.mdb auf Ihre lokale Festplatte. Auf keinen Fall in den Verzeichnispfad kopieren, in dem die aktuelle Datenbank abgelegt ist.

Gehen Sie ins Modul EINSTELLUNGEN und wählen den Menüpunkt <Grundeinstellungen> <Pfade>. Bitte ändern Sie in dem sich öffnenden Fenster den 21.Pfad (Projekte) auf „c:\“ (falls Sie die Projdat.mdb direkt unter c: liegen haben), merken sich aber bitte den zuvor eingetragenen Pfad zur Sicherheit.

Legen Sie sich mit dem Explorer einen Ordner an, der als „Sammelbehälter“ für Ihre Dokumente dient (in unserem Beispiel „Export“).

Wenn Sie nun die Projektverwaltung öffnen, werden Sie Ihr gelöschtes Projekt wiederfinden. Die eigentliche Arbeit geht an dieser Stelle erst richtig los, da Sie jedes Dokument per Hand exportieren müssen.

Achtung! Legen Sie während des gesamten Vorgangs keine neuen Dokumente an, Sie arbeiten mit einer alten Datenbank! Sie können also nicht am aktuellen Tagesgeschehen teilnehmen!

Markieren Sie im Projekt das erste Dokument, wählen Sie den Menüpunkt <Extern> <Dokument exportieren> an. Es öffnet sich folgendes Fenster:

[Bild]

Bei Pfad + Dateiname geben Sie den Ordner an, der den Sammelbehälter darstellt und den Namen, unter dem Sie das Dokument anschließend wiederfinden. In unserem Beispiel: c:\export\1470.mdb. Dies tun Sie mit jedem Dokument, das sich im betreffenden Projekt befindet.

Setzen Sie nun im Modul EINSTELLUNGEN unter dem Menüpunkt <Grundeinstellungen> <Pfade> den Pfad wieder auf die Server-Festplatte zurück.

Legen Sie jetzt eine neue Verknüpfung im Ordner ‚Label für Windows‘ an, indem Sie den Ordner öffnen und den Menüpunkt <Datei> <Neu> <Verknüpfung> anwählen.

[Bild]

Beim folgenden Fenster geben Sie bitte „x:\labelwin\import.exe“ als Pfad an (x steht in diesem Fall für den Laufwerksbuchstaben, auf dem sich das Labelwin befindet.

Mit Doppelklick auf die neue Verknüpfung öffnet sich folgendes Fenster, in dem Sie den Pfad und das Projekt wählen müssen. Sie sollten sicherstellen, dass es sich um ein leeres, evtl. neues Projekt handelt.

[Bild]

Wenn Sie alle Dokumente in das Projekt importiert haben, sollten Sie die Kopie der Projdat.mdb von Ihrer lokalen Festplatte löschen.
