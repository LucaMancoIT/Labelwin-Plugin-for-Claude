# 4. Formulare mit Strichcode / QR-Code

Pfad: Materialwirtschaft > Scannerverarbeitung [Modul] > 4. Formulare mit Strichcode / QR-Code
Quelle: handbuch/4__formulare_mit_strichcode___qr_code.htm

|

4. Formulare mit Strichcode / QR-Code

Im Prinzip lässt sich bei jeder Druckausgabe mit einer Projektnummer, einer Kundendienstauftragsnummer oder einer Artikelnummer diese auch als Strichcode (bzw. QR-Code) drucken. Es müssen lediglich bestimmte Regeln eingehalten werden, da zum einen nicht alle Zeichen im Strichcode Code39 gedruckt werden können und zum anderen Label die Projektnummer und KD-Auftragsnummer durch bestimmte, der Nummer vorangestellte, Kennzeichen erkennen kann.

Formulare mit Strichcode

Für die eigentliche Druckausgabe muss auf dem Rechner die Schriftart CODE39 installiert sein, die leider nicht zum Windows-Auslieferungsstand gehört. Die Schriftart kann über uns bezogen werden. Manchmal finden sich auf Rechner auch Schriftarten mit Code39, die zum Teil jedoch nicht in der Lage sind, Buchstaben und Sonderzeichen zu drucken.

Wie gewohnt werden auch die Formulare mit Strichcode mit dem Programm Crystal-Report erstellt. Wir stellen eine Grundausstattung an Formularen mit Strichcode bereit, wenn die Schriftart Code39 über uns bezogen wurde. Formularanpassungen können nach Kundenwunsch kostenpflichtig vorgenommen werden.

|

PLETIBRU.RPT

SL1.RPT

DBTEXTE.RPT

GLSTRICH.RPT

KDSTRICH.RPT

ET97X42.RPT

ETKOEPFE.RPT

|

Ausgabe eines einzelnen Artikels aus den Stammdaten

Stückliste mit Projektnummer

Datenblatt mit Projektnummer

Etiketten mit Projektnummern, Globale Statistik

Kundendienstauftrag

Etiketten für Tintenstrahl oder Laserdrucker

Etiketten für Mengenerstellung

Artikeletiketten mit Strichcode

Wenn die Etiketten mit Labelwin erstellt werden, muss der Strichcode unbedingt die interne Katalognummer enthalten. Nach der 2-stelligen Katalognummer (also ggf. mit Null vorweg), muss an der dritten Stelle ein Punkt sein und dann die Artikelnummer folgen. Nur wenn diese Regel eingehalten wird, kann Labelwin diesen Artikel immer finden.

[Bild]

Wenn auf den Artikeln bereits Strichcodes vorhanden sind, kann man diese nur unter bestimmten Bedingungen nutzen. Der Strichcode muss der Artikelnummer entsprechen oder bei einem Artikel im Feld EAN-Code eingetragen sein. Um den entsprechenden Katalog zu finden, muss dieser in der Oberfläche der Scannerverarbeitung als Vorgabe gewählt werden.

Der abgebildete Strichcode hat in Wirklichkeit den Inhalt 05.EV, wobei 05 die interne Katalognummer ist.

Artikeletiketten mit QR-Code

Alle Etiketten Formulare mit Strichcode sind mit einem klassischen Barcode / Strichcode versehen, soweit die Code39 Schriftart vorhanden ist.

Über spezielle Formulare kann anstelle des Strichcodes auch ein QR-Code (und ein Artikelbild) ausgegeben werden. Details finde Sie im Kapitel Lager beschriften.
