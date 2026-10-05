# 3. Einrichten des Telefonie-Moduls

Pfad: Einrichtungsarbeiten > Telefonie / Tapi [Modul] > 3. Einrichten des Telefonie-Moduls
Quelle: handbuch/3__einrichten_des_telefonie_moduls.htm

|

3. Einrichten des Telefonie-Moduls

Zunächst müssen Sie das Programm-Icon ‚Telefon’ an die Oberfläche holen, das wahrscheinlich bei Ihnen noch nicht sichtbar ist. Standardmäßig wird es jedenfalls nicht installiert. Am einfachsten geschieht dies im Programmmodul ‚Einstellungen’ unter den Menüpunkten ‚Serviceprogramme, Verknüpfungen auf Desktop erstellen’. Kreuzen Sie in dieser Liste das Programm ‚TELEFON.EXE’ an und betätigen den Start-Knopf. Danach befindet sich ein neues Icon an der Oberfläche, dass Sie in die Gruppe ‚Label für Windows’ hineinziehen oder aber vom Desktop aus benutzen können.

Es gibt übrigens durchaus Sinn, nach den erfolgreichen Tests das Programm in die Autostart-Liste aufzunehmen, so dass es beim Rechnerstart gleich mit gestartet wird.

Beim ersten Start des Moduls müssen Eintragungen in der Windows-Umgebung erfolgen, so dass Sie am besten als Administrator angemeldet sein sollten. Wenn das Labelwin-System für den Administrator nicht eingerichtet sein sollte, können Sie die Einträge auch durch jeweils einen Doppelklick auf die Dateien \labelwin\tapiActv.exe und \labelwin\tapiServ.exe vornehmen. Dabei starten die Programme nicht, es erfolgt nur die sogenannte Registrierung.

Damit die Wahl in allen Ländern funktioniert, müssen Einträge in der Systemsteuerung erfolgen. Falls hier keine oder falsche Einträge vorhanden sind, warnt das Telefon-Programm beim Start und führt Sie automatisch in den Eingabebereich. Wichtig ist die Wahl des Landes und die Eingabe der eigenen Vorwahl, jedoch ohne führende Null.

[Bild]

Die Einrichtung des Telefonmoduls kann an 2 Stellen im Programm erfolgen, im Modul Einstellungen unter den Menüpunkten ‚Programmbereiche, Adressen, Tapi / Telefonie’ und im Telefonmodul selber, wenn Sie mit F9 das Menü sichtbar schalten und dann die Punkte ‚Datei, Einstellungen’ anwählen.

Die Einträge müssen auf mehreren Karteiseiten erfolgen. Sie sind zum Teil für die ganze Firma wirksam, zum Teil für den PC und zum Teil für den angemeldeten Benutzer.

[Bild]

Auf dieser Seite sind wahrscheinlich nur wenige Erklärungen erforderlich. Die Protokolle können Sie mitlaufen lassen da sie ohnehin automatisch jeden Tag gelöscht werden. Besonders in der Einrichtungsphase sollten Sie die Protokolle mitlaufen lassen, da wir bei Problemen eventuell darüber die Ursache finden können.

LabelCRM starten: Wenn Sie diesen Haken setzen, wird beim Abheben der Leitung und einer eindeutig gefundenen Adresse sofort das Programm LabelCRM nachgestartet. In diesem sehen Sie dann alle Vorgänge der anrufenden Adresse.

Telefonfenster aktivieren bei...

Hier legen Sie fest, ob unser Programm sofort an die Oberfläche und aktiv werden soll, wenn ein Anruf eingeht oder erst wenn die Leitung abgehoben wird. Je nach Arbeitsplatz kann die sofortige Aktivierung ziemlich nervig sein. Man schreibt einen Text, das Telefon klingelt, wenn es nun sofort aktiviert ist, wird man beim Schreiben unterbrochen, getippte Zeichen gehen in Leere.

Verpasste Anrufe protokollieren für Nummern: Auch wenn auf Ihrem Telefon diverse eingehende Leitungen klingeln, können Sie hier eine Protokolleingrenzung treffen.

Verpasste Anrufe zeigen nach ..Minuten: Wenn Sie einen oder mehrere Anrufe verpasst haben, kommt automatisch das nach der hier eingesetzten Zeit die Liste mit den verpassten Anrufen an die Oberfläche. Wenn Sie die Zeit auf Null setzen, erscheint die Liste nicht automatisch, sondern muss ggf. manuell aktiviert werden.

[Bild]

Tapi-System: Hier ist es wichtig den Eintrag ‚Labelwin Active Tapi’ zu aktivieren und die richtige Tapi-Leitung zu wählen. Meist erkennen Sie die Tapi-Leitung am Namen der Telefonanlage. In der Liste sind oft auch Einträge wie ‚Drucker’ usw, so etwas ist garantiert die falsche Einstellung. Wenn Sie die Tapi-Leitung nicht finden, so liegt der Fehler im System bzw. in den Verbindungen zwischen dem Rechner und der Telefonanlage. Wenden Sie sich dann an den Telefonbetreuer.

Führende Ziffer: Bei den führenden Ziffern geht es darum, dass bei manchen Anlagen eine Null vorweggeschickt wird, wenn es ein Außenanruf ist. Durch die im Bild sichtbare Ziffer 0 wird eine führende Null abgeschnitten. Allerdings gab es auch schon einen Fall, dass die Telefonanlage eine eingehende Nummer um die erste Null gekürzt hat. Statt 0171 12345 kam nur 17112345 an. So etwas kann man in der Hauptmaske im Protokoll sehen. Wenn Sie diesen Fall haben sollten, setzen Sie hier die Zeichen +0 ein, dann hängen wir für die Adress-Suche wieder eine Null davor.

Call by Call: In dieser Datei werden ggf. auf der Karteiseite entsprechende Vorwahlnummern hinterlegt. Wenn Sie das nicht möchten, lassen Sie diesen Namen einfach stehen und schreiben auf der Karteiseite nichts rein. Wenn Sie einen anderen Namen eintragen, so können Sie für den eigenen Arbeitsplatz andere Nummern eintragen, als für die anderen Arbeitsplätze im Netz.

Aus Systemeinstellungen: Wir zeigen hier nur die Werte aus der Systemeinstellung an. Änderungen können Sie nur über den Knopf vornehmen. Die erforderlichen Einstellungen sehen Sie im Bild weiter oben.

[Bild]

Wenn Sie vor der Wahl automatisch eine andere Nummer vorweg wählen wollen, so müssen Sie diese hier erfassen. Wir haben z.B. eine Flatrate, die jedoch Handynummern ausschließt. Deshalb haben wir hier eine Call by Call-Nummer hinterlegt.

[Bild]

In dieser Übersetzungstabelle können Sie die eingehenden Nummern mit den dazu gehörenden Namen versehen. Wenn Sie z.B. mehrere eingehende Leitungen haben und feststellen wollen, auf welcher Leitung der Kunde gewählt hat, können Sie hier die Nummer umsetzen lassen.

Wenn Sie wie im obigen Beispiel die internen Nummern eintragen, so können Sie halt nicht mehr sehen, dass ein Anruf von Nummer 31 erfolgt, sondern dass Willy Sie erreichen will.
