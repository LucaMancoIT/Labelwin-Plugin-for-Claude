# Einrichten des Telefonie-Moduls

Pfad: Einrichtungsarbeiten > Telefonie / Tapi [Modul] > Einrichten des Telefonie-Moduls
Quelle: handbuch/einrichten_des_telefonie_moduls.htm

|

Einrichten des Telefonie-Moduls

|

Telefonie aktivieren:

Wird die Labelwin TELEFONIE erstmalig eingesetzt, muss sie in den Telefonieeinstellungen - erreichbar im V5 Programmbaum unter [Optionen - Telefonieeinstellungen] - aktiviert werden. Dazu müssen die beiden Haken bei "Telefonie nicht aktivieren" und "Telefonie nicht initialisieren" weggesetzt werden. Anschließend muss Labelwin neu gestartet werden.

[Bild]

Oftmals ist die Einrichtung damit bereits abgeschlossen, da die Leitung automatisch erkannt und in die Labelwin Telefonieeinstellungen eingetragen wird.

Sollte die Telefon-Funktion nicht automatisch zur Verfügung stehen, sollte zuerst geprüft werden, ob eine Telefonleitung erkannt und eingetragen wurde. Die Leitung kann auf dem Karteikartenreiter "Erweitert" kontrolliert (und ggfs. geändert) werden.

[Bild]

Sollte bei der Leitungswahl die Leitung des Arbeitsplatzes nicht angeboten werden, ist die Einrichtung der Telefonanlage nicht korrekt erfolgt. In diesem Fall müssen Sie Ihren Systembetreuer kontaktieren.

|

Tipp: Prüfen Sie (bzw. Ihr Systembetreuer), ob die Windows Wählhilfe (dialer.exe) funktioniert. Sollte die nicht funktionieren, ist Ihre Telefonanlage nicht richtig konfiguriert und auch die Labelwin Telefonie kann nicht funktionieren.

Telefon und Modem:

Damit die Wahl in alle Länder funktioniert, müssen Einträge in der Systemsteuerung unter "Telefon und Modem" erfolgen. Falls hier keine oder falsche Einträge vorhanden sind, warnt Labelwin beim Aufruf der Telefonieeinstellungen und führt Sie automatisch in den Eingabebereich. Wichtig ist die Wahl des Landes und die Eingabe der eigenen Vorwahl, jedoch ohne führende Null.

[Bild] [Bild]

Telefonieeinstellungen:

Sollte die Telefonleitung korrekt erkannt worden sein und die Labelwin Telefonie somit grundsätzlich zur Verfügung stehen, kann es aber trotzdem sein, dass Rufnummern nicht bzw. nicht korrekt erkannt werden. In diesem Fall kann man Einstellungen in Labelwin vornehmen, die die Rufnummern Interpretation modifizieren und die Besonderheiten Ihrer Telefonanlage berücksichtigt.

Die Einrichtung der Telefonie kann an zwei Stellen im Programm erfolgen: Im Modul EINSTELLUNGEN unter dem Menüpunkt [Programmbereiche - Adressen - Telefonanbindung (Tapi)] oder im V5 Programmbaum unter [Optionen - Telefonieeinstellungen].

Die Einstellungen sind auf drei Karteiseiten verteilt. Sie sind zum Teil für die ganze Firma wirksam, zum Teil für den PC und zum Teil für den angemeldeten Benutzer.

Karteikarte "Ausgehende Telefonate"

|

[Bild] Bild: Telefonieeinstellungen "Ausgehende Telefonate"

|

Telefonnummern ausgehender Telefonate anpassen: Hier kann das Format, in dem die Telefonummern an Ihre Telefonanlage übermittelt werden, konfiguriert werden. In der Regel ist die kanonische Form die beste Wahl.

Ziffer(n) für Amtsholung (meistens 0): Bei den führenden Ziffern geht es darum, dass bei manchen Anlagen eine Null vorweggeschickt wird, wenn es ein Außenanruf ist. Durch die im Bild sichtbare Ziffer 0 wird eine führende Null abgeschnitten. Allerdings gab es auch schon einen Fall, dass die Telefonanlage eine eingehende Nummer um die erste Null gekürzt hat. Statt 0171 12345 kam nur 17112345 an. So etwas kann man in der Hauptmaske im Protokoll sehen. Wenn Sie diesen Fall haben sollten, setzen Sie hier die Zeichen +0 ein, dann hängen wir für die Adress-Suche wieder eine Null davor.

Rufaubau (alternative Methode): Beim Einsatz von anderer Telefonsoftware, kann hier der Rufaufbau über das Fremdprogramm eingerichtet werden. Im Normalfall sind hier allerdings keine Eintragungen erforderlich.

Karteikarte "Eingehende Telefonate"

|

[Bild] Bild: Telefonieeinstellungen "Eingehende Telefonate"

|

Beim Abheben LabelCRM starten: Wenn Sie diesen Haken setzen, wird beim Abheben der Leitung und einer eindeutig gefundenen Adresse sofort das Programm LabelCRM nachgestartet. In diesem sehen Sie dann alle Vorgänge der anrufenden Adresse.

Beim Klingeln LabelCRM starten: Wenn Sie diesen Haken setzen, wird bereits beim Klingeln und einer eindeutig gefundenen Adresse sofort das Programm LabelCRM nachgestartet. In diesem sehen Sie dann alle Vorgänge der anrufenden Adresse.

Telefon Fenster anzeigen/aktivieren bei

Hier legen Sie fest, ob das kleine Telefonie Fenster sofort an die Oberfläche kommen soll, wenn ein Anruf eingeht oder erst, wenn die Leitung abgehoben wird. Je nach Arbeitsplatz kann die sofortige Aktivierung ziemlich nervig sein. Man schreibt einen Text, das Telefon klingelt, wenn es nun sofort aktiviert ist, wird man beim Schreiben unterbrochen, getippte Zeichen gehen in Leere.

geführte Anrufe protokollieren: Bei eingeschalteten Protokoll werden die geführten Telefonate protokolliert und können von allen anderen Labelwin Anwendern adressbezogen eingesehen werden.

Die Vorteile dieser Protokollierung sind, dass Sie sehen können, wann Sie mit wem telefoniert haben und, dass andere Mitarbeiter sehen können, z.B. im Adressenmodul (Menüpunkt [Anzeigen - Anrufliste]), welcher Mitarbeiter zuletzt mit einer Adresse Kontakt hatte. Der zweite Punkt ist besonders interessant, wenn ein Kunde anruft und sagt "Ich habe bei mir einen verpassten Anruf aus Ihrer Firma, weiß aber nicht, wer mich sprechen wollte.". Dann können Sie sehen, wer als letztes versucht hat, den Kunden zu erreichen.

Hinweis: Besonders in der Einrichtungsphase sollten Sie die Protokolle mitlaufen lassen, da wir bei Problemen eventuell darüber die Ursache finden können.

verpasste Anrufe protokollieren: Hierbei handelt es sich um die gleiche Protokollfunktion wie bei geführten Anrufen, nur eben für die verpassten. Der Vorteil dieser Protokollierung ist, dass Sie sehen können, welche Anrufe Sie verpasst haben.

Verpasste Anrufe automatisch zeigen nach ..Minuten: Wenn Sie einen oder mehrere Anrufe verpasst haben, kommt automatisch das nach der hier eingesetzten Zeit die Liste mit den verpassten Anrufen an die Oberfläche. Wenn Sie die Zeit auf Null setzen, erscheint die Liste nicht automatisch, sondern muss ggf. manuell aktiviert werden.

Karteikarte "Erweitert"

Auf dieser Seite sollten Sie eigenständig keine Änderungen vornehmen. Hier befinden sich Spezialoptionen, die nur in Ausnahmefällen benötigt werden und nur vom Labelpartner oder der Hotline aktiviert werden.

|

[Bild]

Bild: Telefonieeinstellungen "Erweitert"

|
