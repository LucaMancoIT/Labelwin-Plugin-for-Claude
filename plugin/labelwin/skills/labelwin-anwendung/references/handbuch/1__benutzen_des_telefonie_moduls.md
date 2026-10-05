# 1. Benutzen des Telefonie-Moduls

Pfad: Einrichtungsarbeiten > Telefonie / Tapi [Modul] > 1. Benutzen des Telefonie-Moduls
Quelle: handbuch/1__benutzen_des_telefonie_moduls.htm

|

1. Benutzen des Telefonie-Moduls

Vor der Benutzung ist eine entsprechende Einrichtung auf jedem Arbeitsplatz erforderlich. Lesen Sie dazu im Kapitel 3

Das Wählen erfolgt aus der Adressverwaltung, dem Modul LabelCRM, dem Kundendienstmodul und einigen anderen Modulen, wo neben der angezeigten Telefonnummer ein kleiner Wählknopf ist. Damit wird das Telefon-Modul angesteuert und dieses übergibt dann die zu wählende Nummer an die Tapi-Schnittstelle.

Auch beim Rauswählen zeigt das Programm die gerade gewählte Adresse an.

Beim ersten Start erscheint die folgende Maske zunächst ohne Adresse und Telefonnummer, nach jeder Nutzung bleiben die letzten Daten stehen. Das Bild ist also nach einem Anruf ‚fotografiert’ worden.

[Bild]

1 Telefonnummer: Hier ist immer die Nummer des letzen Anrufers oder des zuletzt Angerufenen zu sehen. Sobald die letzten Ziffern der Nummer in Klammern stehen, wurde die Nummer nicht komplett gefunden. Wenn Sie beispielsweise von einem Anrufer die Zentrale mit 0521/1234-0 gespeichert haben und ein Anruf mit 0521123410 reinkommt, findet das Programm zwar die Adresse, schreibt aber die angezeigte Nummer so: 05211234(10). Dies Verhalten führt leider manchmal dazu, dass eine falsche Adresse gefunden wird, besonders dann, wenn man von einem Ort viele Adressen gespeichert hat.

2 Adressdaten: Wenn ein Anruf stattgefunden hat wird hier das Suchwort und die wichtigsten Informationen der Adresse gezeigt.

3 Knopf LabelCRM: Sobald Sie diesen Knopf drücken, wird das Modul LabelCRM gestartet. Wenn eine Adresse gefunden wurde, wird LabelCRM sofort mit den entsprechenden Informationen gefüllt. Über die Einstellungen kann man übrigens auch festlegen, dass LabelCRM immer sofort gestartet wird, wenn Sie das Gespräch annehmen. Ob Sie diese Funktion nutzen wollen, bleibt Ihnen überlassen, sie kann auch nervig sein. In der Auftragsannahme (oder bei uns in der Hotline) ist sie jedenfalls sinnvoll.

4 Knopf ‚Kurzwahl und Anrufliste’: Bei Betätigen dieses Knopfes öffnet sich das Fenster mit den Anruflisten. Die Beschreibung lesen Sie weiter hinten auf den nächsten Seiten.

5 Knopf ‚Menü einschalten’: Mit diesem Knopf wird das Menü des Telefonmoduls sichtbar, das aus Platzgründen zunächst ausgeschaltet ist. In der Anwendung ist es gut, wenn das Modul möglichst wenig Platz auf dem Bildschirm einnimmt, da es immer im Weg ist.

Menüpunkte:

|

|

Datei

|

|

Wählen (Strg W)

Nach der Anwahl dieses Menüpunktes erscheint ein kleines Eingabefenster, in das Sie die zu wählende Nummer eingeben können.

|

|

LabelCRM starten (F3)

Mit der F3-Taste können Sie das Modul LabelCRM nachstrten.

|

|

Menü Ein/Aus (F9)

Obwohl das Menü eventuell nicht sichtbar ist, können Sie es mit der Taste F9 ei- oder ausschalten.

|

|

Einstellungen

Mit diesem Menüpunkt gelangen Sie in die Einstellungen, die weiter unten beschrieben sind.

|

|

Tapi-Protokoll

Um bei Problemen die Ursachen zu finden, kann man hier in ein Ereignissprotokoll schauen. Diese Funktion ist im Wesentlichen für unsere Betreuung programmiert und wird daher hier nicht weiter erklärt.

|

|

Call by Call nutzen

Wenn in den Einstellungen Call by Call-Nummern hinterlegt sind, werden diese standardmäßig verwendet. Wenn diese Vorwahl mal wieder nicht klappt (was in der Anfangszeit dieser Systeme häufig vorkam), kann man die Funktion wegschalten. Da es immer mehr eine sogenannte ‚Flatrate’ verwendet wird, ist die Funktion oft nicht erforderlich. Das Ausschalten gilt für alle nachfolgenden Anrufe, schalten Sie sie also rechtzeitig wieder ein.

|

|

Reset Anruf-Informationen

Dieser Menüpunkt ist ein Rettungsanker bei der Einrichtung. Wenn wegen falscher Einrichtung oder einem fehlerhaften Tapi-Treiber die Verarbeitung blockiert ist, kann man hier alles zurücksetzen.

|

|

Simulation

In der Einrichtungsphase kann es sinnvoll sein einen Anruf zu simulieren, statt immer mit einem Handy zu wählen.

|

|

Ende

Das Modul wird nach einer Nachfrage geschlossen. Üblicherweise sollten Sie es den ganzen Tag geöffnet haben, da sonst die Aufzeichnung der verpassten Anrufe nicht stattfindet.

|

|

Telefonie

|

|

Leitung 1 annehmen (F5))

Statt zur Maus zu greifen, können Sie die Steuerung auch über Menüpunkte erreichen.

|

|

Info

Hier gelangen Sie in die Standard-Menüpunkte zum Handbuch und Informationen zur Programmversion.

Farbdarstellungen:

Die Farbe der Nummeranzeige wird über den Status der Leitung geschaltet:

Gelb = es klingelt, egal ob es sich um eingehenden oder ausgehenden Ruf handelt

Grün = aktives Gespräch, abgehobene Leitung

Rot = geparkte Leitung

Nicht erkannte Rufnummer eingehend

Wenn die Rufnummer unterdrückt ist, oder überhaupt nicht in Labelwin gefunden wird, so steht im Adressfeld der Text ‚*** Rufnummer unbekannt ***

Wenn die Rufnummer komplett in den Adressen nicht gefunden wird, sucht das Programm mit am Ende abgeschnittenen Ziffern. Oft handelt es sich um eine Telefonanlage und die letzten Ziffern des Anrufers sind nicht erfasst worden. Wenn mit abgeschnittenen Ziffern eine (vielleicht) passende Adresse gefunden wird, so wird diese in Rot mit ?-Zeichen gezeigt. In der Darstellung der Telefonnummer werden die nicht gefundenen Ziffern in Klammern gesetzt.

Auf dem Bild sehen Sie eine solche Adresse, in der eine Telefonnummer mit 0521 8810 am Anfang gefunden wurde. Die eingehende Nummer war 0521 881017

[Bild]

Doppelt vorhandene Telefonnummern

Wenn eine Telefonnummer bei unterschiedlichen Adressen eingetragen wurde, kann das System nicht entscheiden, welches die ‚richtige’ Adresse ist. In diesem Fall erscheint eine Auswahlcombo mit dem Text ‚Bitte wählen’. Wenn Sie die Liste ausklappen sehen Sie die in Frage kommenden Adressen.
