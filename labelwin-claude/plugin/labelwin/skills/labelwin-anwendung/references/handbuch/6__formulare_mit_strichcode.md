# 6. Formulare mit Strichcode

Pfad: Materialwirtschaft > Scannerverarbeitung [Modul] > 6. Formulare mit Strichcode
Quelle: handbuch/6__formulare_mit_strichcode.htm

|

6. Formulare mit Strichcode

Im Prinzip lässt sich bei jeder Druckausgabe mit einer Projektnummer, einer Kundendienstauftragsnummer oder einer Artikelnummer diese auch als Strichcode drucken. Es müssen lediglich bestimmte Regeln eingehalten werden, da zum einen nicht alle Zeichen im Strichcode Code39 gedruckt werden können und zum anderen Label die Projektnummer und KD-Auftragsnummer durch bestimmte, der Nummer vorangestellte, Kennzeichen erkennen kann.

Für die eigentliche Druckausgabe muss auf dem Rechner die Schriftart CODE39 installiert sein , die leider nicht zum Windows-Auslieferungsstand gehört. Die Schriftart kann über uns bezogen werden. Manchmal finden sich auf Rechner auch Schriftarten mit Code39, die zum Teil jedoch nicht in der Lage sind, Buchstaben und Sonderzeichen zu drucken.

Wie gewohnt werden die Strichcodes mit dem Programm Crystal-Report erstellt. Es gibt Standardformulare auf unserem ISDN-Server im Bereich L:\Kunden\service\32v6\formulare Code39 , die bitte nur als Beispiel zu betrachten sind.

Im Bedarfsfall sollte man von einem solchen über STRG-C und Strg-V den Strichcode auf das eigene (angepasste) Formular übertragen.

PLETIBRU.RPT Ausgabe eines einzelnen Artikels aus den Stammdaten

SL1.RPT Stückliste mit Projektnummer

DBTEXTE.RPT Datenblatt mit Projektnummer

GLSTRICH.RPT Etiketten mit Projektnummern, Globale Statistik

KDSTRICH.RPT Kundendienstauftrag

ET97X42.RPT Etiketten für Tintenstrahl oder Laserdrucker

ETKOEPFE.RPT Etiketten für Mengenerstellung

Artikeletiketten

Wenn die Etiketten mit Labelwin erstellt werden, muss der Strichcode unbedingt die interne Katalognummer enthalten. Nach der 2-stelligen Katalognummer (also ggf. mit Null vorweg), muss an der dritten Stelle ein Punkt sein und dann die Artikelnummer folgen. Nur wenn diese Regel eingehalten wird, kann Labelwin diesen Artikel immer finden.

[Bild]

Wenn auf den Artikeln bereits Strichcodes vorhanden sind, kann man diese nur unter bestimmten Bedingungen nutzen. Der Strichcode muss der Artikelnummer entsprechen oder bei einem Artikel im Feld EAN-Code eingetragen sein. Um den entsprechenden Katalog zu finden, muss dieser in der Oberfläche des Scannmoduls als Vorgabe gewählt werden.

Der abgebildete Strichcode hat in Wirklichkeit den Inhalt 05.EV, wobei 05 die interne Katalognummer ist.
