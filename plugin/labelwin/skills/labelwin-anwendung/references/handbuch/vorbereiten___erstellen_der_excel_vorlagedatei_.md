# Vorbereiten / Erstellen der Excel-Vorlagedatei

Pfad: Auswertungen / Controlling > Controlling [Modul] > BWA mit Vorjahresvergleich > Vorbereiten / Erstellen der Excel-Vorlagedatei
Quelle: handbuch/vorbereiten___erstellen_der_excel_vorlagedatei_.htm

|

Vorbereiten / Erstellen der Excel-Vorlagedatei

Kopieren Sie per Explorer die Datei \labelwin\excel\vorlage\bwaVJleer.xls in das gleiche Verzeichnis unter dem Namen BwaVj.xls. Damit wird unsere Vorlage auf die später von Ihnen verwendete, noch anzupassende Auswertung kopiert.

Importieren Sie dann die Abfrage ‚BWA_mit_Vorjahresvergleich.sql’ in Ihr System. Starten Sie hierzu das Modul Selektieren und rufen den Menüpunkt >Controlling> – >Auswertung erfassen> auf. Wählen Sie eine Abfragegruppe aus und importieren Sie die Datei bwa_mit_vorjahresvergleich_server.sql (für SQL-Server-Datenbanken) bzw. bwa_mit_vorjahresvergleich (für Access-Datenbanken) über den Menüpunkt <Optionen>, <Abfrage importieren>.

Nehmen Sie dann diese Abfrage (‚Bwa mit Vorjahresvergleich’) in Bearbeitung. Markieren Sie die erste Auswertung mit dem Namen ‚Beschriftung’ mit dem Excelblatt ‚Bilanzgruppen’. Mit dem Knopf ‚Schnelltest’ lassen Sie nur diese Auswertung ablaufen (wählen Sie also bei der Frage ‚Einzeln/Gesamt’ den Knopf ‚Einzeln’).

Dabei werden die vorhandenen Bilanzgruppen in jene Excel-Vorlage namens BwaVJ.xls eingetragen. Wenn Excel gestartet ist, gehen Sie auf die Seite ‚Bilanzgruppen’

Hier wurden alle Bilanzgruppen eingetragen (alle, auch die ggf. nicht verwendeten) und Sie müssen einige Kennzeichen eintragen. Für jede Bilanzgruppe muss das passende Kennzeichen ‚Erlös’, ‚Material’, ‚Kosten’ oder ‚Bilanz’ eingetragen werden. Diese Worte werden als Schlüsselworte verwendet und müssen deshalb exakt so geschrieben werden. Am Besten kopieren Sie die Worte an die richtige Stelle.

[Bild]

In der nächsten Spalte müssen Sie einen Wert mit 1 oder –1 eintragen. Labelwin geht mit den Kontensalden rein mathematisch um, so dass Erlöse positiv und Kosten negativ dargestellt werden. Der Anwender ist jedoch leicht irritiert, wenn dies auch in der Tabelle so dargestellt wird, besonders wenn dann Erlöse und Kosten addiert werden, um den Rohertrag darzustellen. Deshalb werden alle Werte für die Darstellung je nach Bilanzgruppe mit dem Faktor 1 oder –1 multipliziert.

|

Erst nachdem diese Eingaben vorgenommen worden sind, betätigen Sie den Knopf ‚Anpassen’.

Damit werden die Bilanzgruppen auf alle Blätter übertragen, die Berechnungsformeln angepasst, die Farben auf alle Eingabe und Ausgabefelder passend gezogen usw.

Wenn Sie sicher sind, dass Sie alle Daten richtig erfasst haben, speichern Sie die Tabelle im

Verzeichnis \labelwin\excel\vorlage\ mit dem Namen bwaVJ.xls ab. Beachten Sie, dass die aktive Datei im Verzeichnis ‚Ausgabe’ steht - Sie müssen also in das Verzeichnis ‚Vorlage’ wechseln.

Wenn Sie einen Soll-Istvergleich durchführen wollen, so müssen Sie die Planzahlen in die Vorlage eintragen. Um das Ganze aber erst mal zu testen, können Sie diese auch später eintragen. Die Beschreibung finden Sie im Kapitel 4, Budgetplanung.
