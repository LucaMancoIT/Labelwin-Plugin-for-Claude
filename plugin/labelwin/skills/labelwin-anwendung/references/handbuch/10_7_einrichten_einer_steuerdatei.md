# 10.7 Einrichten einer Steuerdatei

Pfad: Buchhaltung > Fibuerfassung [25] > 10. Kontoauszugsmanager [Modul] > 10.7 Einrichten einer Steuerdatei
Quelle: handbuch/10_7_einrichten_einer_steuerdatei.htm

|

10.7 Einrichten einer Steuerdatei

Nur bei den Daten des Programms Sfirm und Windata sind die Strukturen der Auszugsdatei fest im Programm hinterlegt. Sobald Sie Daten von einem anderen Programm bekommen, so müssen Sie im Einstellprogramm unter den Menüpunkten ‚Programmbereiche, Eingangsrechnung, Bankdaten’ die Übernahme der Kontoauszüge gemäß ‚Steuerdatei’ anwählen.

Im Folgenden ist beschrieben, wie diese Steuerdatei eingerichtet wird. Sinngemäß handelt es sich um Informationen darüber, in welcher Spalte der Auszugsdatei der Betrag, in welcher Spalte die Adresse, der Buchungstext usw. eingetragen ist. Um Ihnen diese Zuordnung etwas zu erleichtern, haben wir eine Einstellmaske speziell dafür erstellt.

Eine Steuerdatei muss für jede Bank separat erstellt werden, auch dann, wenn die Daten mit dem gleichen Bankprogramm von verschiedenen Banken abgeholt werden. Selbst dabei kommt es nämlich vor, dass die Datenstruktur unterschiedlich ist.

Wählen Sie im Modul Fibuerfassung die richtige Bank an. Wählen Sie dann den Menüpunkt <Belege> <Auszugsdatei einlesen>. In dieser Maske legen Sie zunächst fest, wo sich der von Ihren Bankprogrammen erzeugte Kontoauszug befindet. Nutzen Sie gegebenenfalls den Durchsuchen-Knopf. Wählen Sie anschließend im Menü dieser Maske den Menüpunkt <Datei> <Steuerdatei bearbeiten> an.

[Bild]

In der Tabelle werden sämtliche in der Auszugsdatei vorhandenen Daten angezeigt. Sie müssen nun festlegen, in welcher Spalte z.B. die Information für den Betrag, das Datum und dergleichen hinterlegt ist. Die im Kopf der Maske zu treffenden Einstellungen werden wahrscheinlich weitgehend automatisch richtig vorbelegt sein. Lediglich die Eintragung, ab welcher Zeile die eigentlichen Daten beginnen, müssen Sie festlegen. Bei manchen Auszugsdateien sind als Vorspann zwischen 1 und 8 Zeilen Kopftext angelegt, die für unsere Übernahme keine Bedeutung haben.

Bei der Eingabe ‚Format’ handelt es sich im Grunde genommen nur um die Darstellung von Umlauten. Da die meisten Daten ohnehin in reinen Großbuchstaben und die Umlaute mit ue, oe usw. geschrieben sind, ist dieses in der Regel nicht relevant.

Bei dem Trenner handelt es sich um das Kennzeichen, mit dem die Informationen einer Zeile untereinander getrennt sind. In der Regel handelt es sich um ein Tabulator- oder Semikolon-Zeichen.

Sobald Sie Ihre Einstellungen getroffen haben, können Sie mit dem Schalter ‚Testmodus’ die Tabelle auf die Informationen eingrenzen, die später von unserem Programm verwendet werden sollen.

Sobald Sie in der Tabelle hoch- und runterfahren, werden die jeweils zu nutzenden Felder angezeigt.

Wenn Sie die Maske mit dem OK-Knopf verlassen, werden die von Ihnen getroffenen Einstellungen in die Steuerdatei übertragen. Von nun an werden die Auszugsdaten gemäß dieser hinterlegten Steuerdatei eingelesen. Sollten Sie in der Anfangsphase einen Fehler gemacht haben, können Sie die Buchungsdaten einfach wieder herauslöschen und über den eben beschriebenen Weg die Steuerdatei erneut anpassen.

Sollten Sie Probleme mit der Einrichtung haben, so müssen Sie uns neben der eigentlichen Auszugsdatei auch diese Steuerdatei zukommen lassen. Sie liegt im Verzeichnis Labelwin\Prodaten und trägt den Namen FB1200.txt, wenn es sich um Ihr Bankkonto 1200 handelt. Bei anderen Kontonummern ist natürlich entsprechend eine andere Nummer im Dateinamen hinterlegt.
