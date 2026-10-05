# Telefonie / Tapi [Modul]

Pfad: Einrichtungsarbeiten > Telefonie / Tapi [Modul]
Quelle: handbuch/telefonie___tapi__modul_.htm

|

Telefonie / Tapi [Modul]

Stand: 07.12.2018

(V5.87)

THEMA

|

Immer mehr Telefonanlagen werden mit den Rechnern verbunden, um aus der Anwendung heraus wählen zu können und im optimalen Fall auch bei eingehenden Anrufen den Namen / Adresse des Anrufers zu sehen.

Mit Hilfe des Moduls TELEFONIE können Sie nicht nur die Adresse sehen, sondern sehr schnell alle wichtigen Informationen über den Anrufer. Dazu wird das Modul LabelCRM nachgestartet, das speziell dafür entwickelt worden ist.

|

Auszug Wikipedia zum Thema CRM: Kundenbeziehungsmanagement oder Kundenpflege (engl. Customer Relationship Management, CRM) bezeichnet die Dokumentation und Verwaltung von Kundenbeziehungen.

Beim Nachladen von LabelCRM ist die Maske sofort mit den Daten des Anrufers gefüllt (wenn er denn über die Telefonnummer eindeutig erkannt worden ist).

Über einzuschaltende Protokolle können alle verpassten, geführten und auch gewählten, aber nicht zustande gekommenen Telefonate registriert werden. In der Anzeigeliste kann auch der Eintrag markiert und ein erneuter Wählvorgang gestartet werden.

Über eine für jeden Benutzer anzulegende Kurzwahlliste können oft benötigte Telefonnummern sehr schnell gewählt werden.

Es ist uns klar, dass einige dieser Funktionen auch in Ihrer Telefonanlage vorhanden sind, aber dort fehlt halt die Verbindung zur im Labelwin gespeicherten Adresse.

Wenn es Ihnen nur um das raustelefonieren aus Labelwin heraus geht, benötigen Sie dieses Zusatzmodul nicht, sondern können es bei entsprechender Einrichtung mit der Windows-Wählhilfe erreichen.

VORAUSSETZUNGEN

|

-

Es muss eine TAPI fähige Telefonanlage im Betrieb vorhanden und eingerichtet sein.

-

Jedem Arbeitsplatz muss eine Telefonleitung zugewiesen sein, ggfs. muss ein TAPI Treiber der Telefonanlage installiert sein.

-

Das Zusatzmodul TELEFONIE muss erworben worden sein.

EINRICHTUNG

|

Wird die Labelwin TELEFONIE erstmalig eingesetzt, muss sie in den Telefonieeinstellungen aktiviert werden. Dazu müssen die beiden Haken bei "Telefonie nicht aktivieren" und "Telefonie nicht initialisieren" weggesetzt werden. Anschließend muss Labelwin neu gestartet werden.

[Bild]

Oftmals ist die Einrichtung damit bereits abgeschlossen, da die Leitung automatisch erkannt und in die Labelwin Telefonieeinstellungen eingetragen wird. Ausführliche Erklärungen zur Einrichtung lesen Sie bitte im Unterkapitel Einrichten des Telefonie-Moduls nach.

ANWENDUNG

|

Raus telefonieren

|

Das Wählen kann auf verschiedenen Wege erfolgen.

1. Telefonhörer: In der Adressverwaltung, dem LabelCRM, dem Kundendienstmodul und einigen anderen Modulen wird neben der angezeigten Telefonnummer ein kleiner Telefonhörer angezeigt. Bei Klick auf dieses Icon wird das Telefonie-Modul angesteuert und dieses wiederum übergibt dann die zu wählende Nummer an die TAPI-Schnittstelle.

|

[Bild]

|

2. Kontektmenü: Per Rechtsklick auf eine Adresse - ganz egal wo im Programm - wird ein Kontektmenü aufgerufen. Hier finden Sie den Eintrag "Anrufen.." mit dem Sie auf alle Telefoneinträge dieser Adresse zugreifen können.

|

[Bild]

|

3. Telefonie:

Es kann auch direkt über das Telefonie-Modul gewählt werden. Entweder ruft man eine Adresse über das obere Suchfeld auf oder man gibt die gewünschte Rufnummern direkt in das Eingabefeld ein.

Darüber hinaus kann man sich auch die Nummernliste bzw. Kurzwahlliste anzeigen lassen, um von dort aus eine Nummer anzuwählen.

|

[Bild]

[Bild]

Wird eine Nummer gewählt - egal auf welchem Weg der Anruf ausgeführt wird - zeigt das Telefoniefenster die gerade gewählte Adresse an.

Eingehende Anrufe

Beim Start von Labelwin V5 öffnet sich bei aktiver Telefonie die folgende Maske zunächst ohne Adresse und Telefonnummer. Stattdessen werden eine Suchzeile und die Nummernliste / Kurzwahl angeboten.

[Bild]

Kommt ein Anruf rein und kann die Telefonnummer eindeutig einer Adresse zugeordnet werden, wird diese angezeigt. Die Telefonie ändert sich wie folgt:

|

[Bild]

|

1. Telefonnummer: Oben (gelber Hintergrund) wird die Nummer des Anrufers angezeigt. Sobald die letzten Ziffern der Nummer in Klammern stehen, wurde die Nummer nicht komplett gefunden. Wenn Sie beispielsweise von einem Anrufer die Zentrale mit 0521/1234-0 gespeichert haben und ein Anruf mit 0521123410 reinkommt, findet das Programm zwar die Adresse, schreibt aber die angezeigte Nummer so: 05211234(10). Dies Verhalten führt leider manchmal dazu, dass eine falsche Adresse gefunden wird, besonders dann, wenn man von einem Ort viele Adressen gespeichert hat.

2. Adressdaten: Im mittleren Bereich, wird die Adresse des Anrufers gezeigt, wenn sie eindeutig zugeordnet werden kann.

3. LabelCRM: Oben rechts (im Bereich mit gelben Hintergrund) wird über einen Button das Modul LabelCRM angeboten. Wenn eine Adresse gefunden wird, kann in den Telefonieeinstellungen festgelegt werden, dass automatisch das LabelCRM mit den entsprechenden Informationen durchgestartet wird. Hat man diese Automatik nicht aktiv, kann über diesen Button bedarfsweise das LabelCRM gestartet werden. Ob Sie die Automatik nutzen wollen, bleibt Ihnen überlassen. Sie kann auch nervig sein. In der Auftragsannahme (oder bei uns in der Hotline) ist sie jedenfalls sinnvoll.

Nicht erkannte Rufnummer eingehend

Wenn die Rufnummer nicht in Labelwin gefunden wird, so steht im Telefonie Fenster der Text "Anruf von NUMMER (nicht gefunden)":

[Bild]

Wenn die Rufnummer komplett in den Adressen nicht gefunden wird, sucht das Programm mit am Ende abgeschnittenen Ziffern. Oft handelt es sich um eine Telefonanlage mit Durchwahlen und die letzten Ziffern des Anrufers sind nicht erfasst worden. Wenn mit abgeschnittenen Ziffern eine (vielleicht) passende Adresse gefunden wird, so wird diese Adresse mit rotem Hintergrund und einem kleinen Stopzeichen in der rechten unteren Ecke angezeigt.

Auf dem folgenden Bild sehen Sie eine solche Adresse, in der eine Telefonnummer nicht komplett übereinstimmt.

[Bild]

Doppelt vorhandene Telefonnummern

Wenn eine Telefonnummer bei unterschiedlichen Adressen eingetragen wurde, kann das System nicht entscheiden, welches die ‚richtige’ Adresse ist. In diesem Fall erscheinen beide Adressen mit dem Text "Nicht eindeutig - Bitte wählen!".

[Bild]
