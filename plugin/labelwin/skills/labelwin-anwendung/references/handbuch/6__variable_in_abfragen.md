# 6. Variable in Abfragen

Pfad: Auswertungen / Controlling > Controlling [Modul] > Controlling / Chefknopf > Abfragen erstellen > 6. Variable in Abfragen
Quelle: handbuch/6__variable_in_abfragen.htm

|

6. Variable in Abfragen

Um in einer Abfrage eine Eingrenzung einzutragen, die erst bei der späteren Ausführung der Abfrage wirksam wird, kann man in dem SQL-Befehl Variable eintragen. Wenn Sie z.B. eine Abfrage mit der Eingrenzung auf ein einzelnes Erlöskonto erstellen, ist es gegebenenfalls interessant, dieses Erlöskonto jeweils bei der Ausführung wählbar zu machen. In dem SQL-Befehl müssen Sie dann exakt das Erlöskonto markieren und dann den Knopf ‚Frage erfassen’ betätigen. Die bisherige Kontonummer steht aufgrund der vorherigen Markierung dann schon im Feld ‚Vorgabe’ und Sie können als Frage den Text ‚Nur Kontonummer’ eingeben. Verlassen Sie die Maske mit ‚Speichern’. In dem Abfragetext steht nun ein Text mit jeweils zwei @-Zeichen am Anfang und am Ende. Wenn Sie Änderungen vornehmen wollen, markieren Sie den kompletten Text einschließlich der @-Zeichen und betätigen wieder den Knopf ‚Frage erfassen’. Zwar könnten Sie Änderungen auch direkt vornehmen, aber dabei besteht die Gefahr, dass Sie die Logik zerstören.

Beispiel: Abfrage aus dem Rechnungsausgangsbuch, um einen Ausdruck für das Erlöskonto 8400 zu erzeugen. Um den Abfragetext verständlicher zu halten, wurde auf eine zeitliche Eingrenzung verzichtet.

Nach dem Erstellen der Abfrage steht im Feld ‚Abfrage’ :

{rgausgang.mandant}=##mandant## AND {rgausgang.erloeskonto}='8400'

Wenn Sie die Frage so erfasst haben, wie dies beschrieben wurde, steht dann im Abfragetext:

{rgausgang.mandant}=##mandant## AND {rgausgang.erloeskonto}='@@A Nur Kontonummer_|_8400@@'

Wenn Sie nun den Knopf ‚Testen’ betätigen oder von der obersten Ebene aus die Ausführung dieser Abfrage anwählen, gibt es ein Eingabefeld in der Maske

[Bild]

Den Vorgabewert 8400 können Sie nun unmittelbar vor der Ausgabe ändern

Sie können innerhalb einer Abfrage beliebig viele Variable/Fragen in der beschriebenen Form ablegen.

Standardmäßig sind Variablen für die Mandantennummer und das von und bis Datum vorgesehen. Die Schlüsselworte für das Datum werden Sie in allen Abfragen vorfinden, die auf Grund einer zeitlichen Eingrenzung entstanden sind.

Die folgende Auflistung finden Sie auch in der Maske der Abfragenerstellung mit dem Knopf ‚Hilfe’.

##vondatum## setzt das allgemeine Von-Datum ein

##bisdatum## setzt das allgemeine Bis-Datum ein

##vonjahr## setzt auf den 1.1. 0:01 Uhr der Jahreseingabe

##bisjahr## setzt auf den 31.12. 23:59 Uhr der Jahreseingabe)

##mandant## setzt aktiven Mandant ein

##auswertnr## nimmt die letzte Datenerzeugung der Projektauswertung,

Kundendienstauswertung oder Artikelauswertung
