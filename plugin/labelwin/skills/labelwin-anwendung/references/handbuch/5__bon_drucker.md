# 5. Bon-Drucker

Pfad: Buchhaltung > Ladenkasse [23] > 5. Bon-Drucker
Quelle: handbuch/5__bon_drucker.htm

|

5. Bon-Drucker

Ein Bon-Drucker wird heutzutage in der Regel - wie ein normaler Drucker - per USB angeschlossen und kann somit in den „Drucker/Formular“ Einstellungen der Ladenkasse als Standard-Drucker ausgewählt werden. Vereinzelt soll es aber Kunden geben, die einen Bon-Drucker nutzen, der noch DOS-seitig angesteuert wird. Der Einsatz eines solchen Bon-Druckers hat den großen Vorteil, dass die Druckausgabe sehr schnell erfolgt. Um die Ladenkasse mit einem DOS Bon-Drucker nutzen zu können, sind in Labelwin bestimmte Einstellungen erforderlich.

Sonderfall DOS Bon-Drucker

Die Ladenkasse lässt sich, wie eben erwähnt, auch in Verbindung mit einem DOS-seitig angesteuerten Bon-Drucker nutzen. Der Bon-Drucker muss in diesem Fall an dem LPT1-Port angeschlossen sein. Außerdem muss in den „Drucker/Formular“ Einstellungen der DOS Bon-Druck aktiviert werden.

Wählen Sie dazu den Menüpunkt <Optionen> <Grundeinstellungen>. Aktivieren Sie dort auf der ersten Seite „Drucker/Formulare“ die Option „Druckausgabe auf DOS-Bondrucker“.

[Bild]

Die alten DOS-Drucker haben leider keinen automatischen Vorschub bis an die Abrisskante und keinen Rückzug für den nächsten Druck. Deshalb ist unser System so programmiert, dass der Firmenkopf jeweils nach dem eigentlichen Ausdruck des Bons ausgedruckt wird.

Über die Einstellung „Vorschubzeilen vor Schneiden (platzabhängig)“ können Sie den Vorschub anpassen.

Wenn Sie es passend positioniert haben, enthält der abgerissene Bon genau die letzte Zeile, aber noch nicht den Firmenkopf des nächsten Bons. Nach dem Einlegen einer neuen Rolle müssen Sie allerdings zunächst einen Firmenkopf ausdrucken. Dazu wählen Sie den Menüpunkt <Bearbeiten> <Kopfdruck neue Rolle> an.

Die Firmendaten, die auf dem Bon gedruckt werden sollen, müssen im Modul EINSTELLUNGEN unter dem Menüpunkt <Grundeinstellungen> <Firmendaten> eingegeben werden. Geben Sie auf der Karteikarte ‚Firmen Zusatz 2‘ ab dem Feld ‚Zusatz 15’ Ihre Firmendaten ein. Das Programm druckt diese Daten solange, bis es auf eine Leerzeile stößt. Wenn Sie eine Leerzeile bewusst einfügen wollen, so müssen Sie in das Zusatzfeld einen Punkt am Anfang eintragen. Bei der Druckausgabe wird der Punkt dann durch eine Leerstelle ersetzt, so dass der Ausdruck einwandfrei ist. Über diese Logik ist es möglich, dass Sie den Firmenkopf so lang gestalten können, wie Sie es möchten.

Sobald Sie die Druckausgabe anwählen, erfolgt sofort die Ausgabe der Artikel, während sich noch die Maske für die Abrechnung aufbaut. Diese sofortige Druckausgabe erfolgt aus Zeitgründen - gerade an der Ladenkasse muss es sehr schnell gehen. Wenn Sie dann den ‚gegeben' Betrag eingegeben haben und die OK-Taste betätigen, wird der Rest des Bons gedruckt. Zum Ende hin - wie bereits erwähnt - erscheint automatisch der Firmenkopf für den nächsten Bon.

Sollten Sie versehentlich einen Bon-Druck begonnen haben und befinden sich bereits in der Zahlen-Maske, so können Sie auch dort ein Häkchen bei Bon-Drucker entfernen. In diesem Fall wird der Druck verworfen und Sie können einen DINA4 Drucker auswählen.

Das Programm erlaubt weiterhin die Ausgabe eines Kassenzettels auf einem anderen Drucker z. B. auf DINA4. Auf der Druckmaske, die Sie über die Funktion ‚F12 Druckausgabe' erreichen, werden Ihnen immer zwei Druck-Buttons angeboten. Einmal der Standard-Druck, der den Bon-Druck ausführt und einmal die A4 Druckausgabe.
