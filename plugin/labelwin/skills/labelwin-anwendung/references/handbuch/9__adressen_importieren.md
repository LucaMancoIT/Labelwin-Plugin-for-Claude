# 9. Adressen importieren

Pfad: Adressverwaltung > Adressen [5] > 9. Adressen importieren
Quelle: handbuch/9__adressen_importieren.htm

|

9. Adressen importieren

Das Importieren von Adressen findet in der Regel bei der Einführung des Programms statt und läuft nur ein Mal. Da dabei häufig auch Anlagedaten, Wartungsverträge und Wartungstermine übertragen werden sollen, ist es in der Regel sinnvoll eine speziell auf die Daten angepasste Import-Schnittstelle zu entwickeln.

Dennoch kommt es vor, dass Sie eine einfache Adressliste importieren wollen, die vielleicht von einer Wohnungsbaugesellschaft, einem übernommenen Mitbewerber, einem Adressenverlag oder woher auch immer kommen. Solche Adressen liegen meist im Excel-Format vor.

Es ist eine gefährliche Funktion, weil man damit sehr leicht tausende falsche Adressen importieren kann, die man nicht ohne weiteres wieder löschen kann. Sie finden die Funktion unter dem Menüpunkt <Optionen> <Daten importieren>.

Eine automatisierte Übernahme ist nur dann möglich, wenn die Daten in einer einheitlichen Struktur und mit einem einheitlichen Trennzeichen vorliegen. Wenn es sich um eine XLS-Datei handelt (Excel), so müssen Sie diese einmal in Excel in Bearbeitung nehmen und dann als CSV-Datei abspeichern.

Um die Daten an die jeweils richtige Stelle zu schreiben, treffen Sie eine Zuordnung in der Sie festlegen, wohin das erste Feld eingetragen wird, das 2. Feld usw. Diese Zuordnung ist extrem wichtig, es müssen alle Daten den ‚richtigen’ Feldern in Labelwin zugeordnet werden.

Bevor Sie die Daten übernehmen, sollten Sie unbedingt eine Datensicherung der Hauptdatenbank \labelwin\prodaten\projdat.mdb vorgenommen haben.

Nur mit einer Datensicherung haben Sie die Möglichkeit bei schweren Fehlern in den getroffenen Zuordnungen erneut die Daten zu übertragen. Ohne diese Sicherung hilft nur, die Adressen Stück für Stück zu löschen, was recht mühselig ist. Wenn Sie sorgfältig arbeiten, können Sie aber mit einer Einzelbestätigung ein paar Adressen übernehmen, um dann eine Prüfung vorzunehmen.

Die getroffenen Einstellungen und Zuordnungen werden im gleichen Verzeichnis abgelegt, in dem sich auch die Datendatei befindet. Damit haben Sie die Chance zu einem späteren Zeitpunkt eine Datei mit der gleichen Struktur einzulesen, ohne alle Einstellungen erneut zu treffen. Die Datei für die Einstellungen erhält die Extension ’.ord’ , also bei dem unten abgebildeten Beispiel mit der Ausland.txt entsteht eine Datei mit dem Namen Ausland.ord.

[Bild: 9. Adressen importieren]

|
[Bild: 1]

Importdatei

[Bild: 1. Importdatei]

Tragen Sie hier den Pfad und Dateinamen der Datei ein, in der Ihre zu importierenden Adressen abgelegt sind. Ggf. können Sie auch mit dem Knopf ‚Durchsuchen’ arbeiten. Wenn Sie den Pfad manuell tippen, bestätigen Sie ihn bitte mit der Enter-Taste.

|
[Bild: 2]

Anzeigetabelle

[Bild: 2. Anzeigetabelle]

Hier sehen Sie die Daten, wie das Programm sie im ersten Anlauf interpretiert. Nachdem Sie die Felder Trennzeichen und Textkennzeichen ausgefüllt haben, können Sie mit dem Einlesen-Knopf die Daten erneut in die Tabelle eintragen lassen.

|
[Bild: 3]

Trennzeichen

[Bild: 3. Trennzeichen]

Hier legen Sie fest, wie die einzelnen Adressinformationen untereinander getrennt sind. Meisten wird es sich um ein Semikolon handeln, aber auch Tab oder Komma getrennte Dateien sind möglich.

|
[Bild: 4]

Textkennzeichen

[Bild: 4. Textkennzeichen]

Manche Programme setzten jede einzelne Information in Anführungszeichen. Dass sieht dann zum Beispiel so aus: „Herrn“; „Willy Müller“; ....

Legen Sie hier fest, dass das Anführungszeichen ggf. entfernt werden muss.

|
[Bild: 5]

Import ab Zeile

[Bild: 5. Import ab Zeile]

Tragen Sie hier die erste Datenzeile ein. Häufig haben Excel Dateien einen ersten Datensatz, in dem die Feldbeschreibungen abgelegt werden. Für die Zuordnungen sind solche Informationen sehr sinnvoll, aber eine Adresse soll damit in der Regel nicht angelegt werden.

|
[Bild: 6]

Umlaute

[Bild: 6. Umlaute]

Achten Sie darauf, dass die Umlaute in den Daten lesbar sind. Sollten sie es nicht sein, schalten Sie auf den DOS-Standard um und prüfen Sie erneut.

|
[Bild: 7]

Einlesen

[Bild: 7. Einlesen]

Sobald Sie die Daten geändert haben (wie z.B. die Wahl des entsprechendes Trennzeichens oder des Textkennzeichens) müssen Sie die Daten der oberen Tabelle (Nr. 2) erneut einlesen. Wenn die Aufteilung erfolgreich war, so sehen Sie dies in der Tabelle Nr. 8.

|
[Bild: 8]

Anzeigetabellle

[Bild: 8. Anzeigetabellle]

Hier sehen Sie die Struktur der zu importierenden Daten. Um die Daten besser lesen zu können, können Sie evtl. die Trennstriche zwischen der Überschrift mit der Maus nach rechts ziehen.

|
[Bild: 9]

Zuordnungstabelle

[Bild: 9. Zuordnungstabelle]

In dieser Tabelle legen Sie fest, welche Informationen der importierten Daten welchem Labelfeld zugeordnet werden soll. Die Eingabe erfolgt jedoch nicht direkt in der Tabelle, sondern durch die Erfassung in den Feldern elf und zwölf.

|
[Bild: 10]

Datei-Feld

[Bild: 10. Datei-Feld]

Hier sehen Sie die Information der einzelnen Felder. Ordnen Sie allen Feldern die Sie in Labelwin übernehmen wollen, ein entsprechendes Label-Feld (Nr. 11) zu.

|
[Bild: 11]

Label-Feld

[Bild: 11. Label-Feld]

Hier finden Sie eine Auswahl aller in den Labelwin Adressen vorhandenen Informationen.

|
[Bild: 12]

Muster-Adresse

[Bild: 12. Muster-Adresse]

Hier können Sie ggf. eine bereits vorhandene Adresse als Musteradresse auswählen.

|
[Bild: 13]

Kriterium

[Bild: 13. Kriterium]

Wenn Sie hier ein Häkchen setzen, erscheint eine Auswahlliste der von Ihnen festgelegten Kriterien. Wenn Sie hier eine Auswahl treffen, wird dieses in allen importierten Adressen eingetragen.

|
[Bild: 14]

Optionen

[Bild: 14. Optionen]

Neue Adressen anlegen

Diese Option ist standardmäßig gesetzt, da man in der Regel Adressen gerade deshalb importiert, um diese neu in den Adressstamm einzupflegen. Möchte man aber nur die bestehenden Adressen aktualisieren, kann es sinnvoll sein diese Option weg zusetzen damit keine neuen Adressen hinzugefügt werden.

Vorhandene Adressen überschreiben: Mit diesem Häkchen legen Sie fest, ob ggf. gefundene Adressen überschrieben werden sollen (also die zu Importierenden Daten gelten) oder die bisher vorhanden Adressen unverändert bleiben sollen.

Anzeige vor Überschreiben: Mit Aktivieren dieses Feldes wird Ihnen die zu überschreibende Adresse vorher angezeigt.

Einzelbestätigung: Wenn Sie diesen Schalter setzen, wird vor jeder Adresse gefragt, ob Sie diese abspeichern wollen. Damit können Sie Adressen auslassen. In erster Linie ist diese Option dazu da, dass Sie ein paar Adressen testweise übernehmen und dann die weitere Übernahme abbrechen können. Sie können dann die übernommenen Adressen prüfen und ggf. löschen falls etwas falsch eingestellt wurde.

|
[Bild: 15]

Reihenfolge

[Bild: 15. Reihenfolge]

Dieses Feld ist nur dann interessant, wenn Sie getrennte Felder in den Daten auf ein gemeinsamen Label-Feld zuordnen wollen. Zum Beispiel ist im Labelwin keine Trennung zwischen Vorname und Nachname vorhanden. Wenn die Daten jedoch in getrennter Form vorliegen, so geben Sie bei der Zuordnung des Vornamens die Reihenfolge eins ein und bei der Zuordnung des Nachnamens die Reihenfolge zwei ein. Das Programm setzt die Felder dann in der entsprechenden Reihenfolge zusammen. Im Regelfall muss hier für alle Dateifelder eine 1 stehen.

|
[Bild: 16]

Wiedererkennungsmerkmal

[Bild: 16. Wiedererkennungsmerkmal]

Hier geht es darum, wie eine bereits vorhandene Adresse wiedererkannt werden kann. Bei allen Datenfeldern, die zu einem Vergleich genommen werden sollen, setzten Sie hier das Kreuz. Sinnvoll ist es zum Beispiel den Namen, den Namen zwei, die Strasse, PLZ, Kundennummer, Kreditorennummern usw. zu vergeben. Beim eigentlichen Import sucht das Programm, ob bereits eine Adresse mit diesen Daten vorhanden ist und überschreibt ggf. die Vorhandene (Das Überschreiben können Sie durch das Ankreuzfeld Nr. 8 verhindern).

|
[Bild: 17]

Zuordnung löschen

[Bild: 17. Zuordnung löschen]

Damit können Sie eine in der Tabelle 10 betroffene Zuordnung wieder löschen.

|
[Bild: 18]

Speichern

[Bild: 18. Speichern]

Nach jeder getroffenen Zuordnung müssen Sie den Speichern-Knopf betätigen, damit die Information in die Tabelle (Nr. 9) eingetragen wird.

|
[Bild: 19]

Starten

[Bild: 19. Starten]

Durch Betätigung dieses Knopfes wird der Adressimport gestartet. Bitte denken Sie unbedingt an die oben bereits erwähnte Datensicherung.

|
[Bild: 20]

Abbruch

[Bild: 20. Abbruch]

Durch Betätigen dieses Knopfes schließen Sie die Maske, ohne Adressen übernommen zu haben. Falls Sie schon Zuordnungen getroffen haben, werden Sie gefragt, ob Sie diese sichern wollen.
