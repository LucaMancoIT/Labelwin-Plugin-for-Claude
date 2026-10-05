# 3.6 Kunden- und Technikerunterschrift

Pfad: Kundendienst > KD-Mobil Notebook [Modul] > 3. Auftragsabwicklung am mobilen Gerät > 3.6 Kunden- und Technikerunterschrift
Quelle: handbuch/3_6_kunden__und_technikerunterschrift.htm

|

3.6 Kunden- und Technikerunterschrift

Im mobilen Kundendienst kann man die Unterschrift des Kunden und ggf. auch des Technikers erfassen. Dazu ist es erforderlich den Auftrag zu drucken und in der Druckmaske den Button "Druck mit Unterschrift" zu verwenden.

[Bild]

Es empfiehlt sich den Ausdruck über den Drucker "Als PDF ablegen" auszugeben, da dann vorab eine PDF neben dem Unterschriftfeld angezeigt wird, So kann der Kunde und auch der Monteur vor der Unterschrift sehen und prüfen ob alles (Zeiten, Material, Abschlussdaten) korrekt erfasst wurden.

Neben der Unterschrift des Kunden kann auch eine Unterschrift vom Techniker erfasst werden. Dies wird in den Grundeinstellungen festgelegt.

[Bild]

|

Tipp: Bei der Unterschrift des Kunden muss man manchmal viel Phantasie haben, um daraus den Namen erkennen zu können. Deshalb gibt es schon lange ein Feld ‚Namen in Buchstaben‘. Dessen Eingabe kann man nun erzwingen. Dazu müssen Sie im Einstellmodul in den Laptopeinstellungen das Feld als Pflichtfeld festlegen.

Nun kann der Auftragszettel mit den Unterschriften gedruckt und ggf. auch per E-Mailanhang an den Kunden gesandt werden.

[Bild]

Das nebenstehende Formular wird kostenlos zur Verfügung gestellt, aber in der Regel werden unsere Kunden Anpassungen an ihre eigenen Wünsche haben wollen. Diese können gegen Abrechnung von uns oder unseren Vertriebspartnern vorgenommen werden.

Nach der Unterschrift erfolgt der Druck auf den eingestellten Drucker. Im Bild ist dies ein PDF-Drucker, es könnte aber jeder beliebige Drucker (z.B. ein mobiler Drucker) angesteuert werden.

Natürlich muss auf dem Formular das Unterschriftenfeld eingefügt werden.

Es gibt Standardformulare z.B. KD500sig oder KDLS1sig, die der Techniker auf dem Notebook drucken kann.

In diesen Formularen werden der Materialzettel, die Zeitbuchungen, Anfahrtspauschalen, Wartungs-terminpauschalen, Abschluss-arbeiten und die Unterschriften gedruckt.

|

Hinweis: Um die Unterschriftenfunktion unter Labelwin V4 nutzen zu können, installieren Sie zuerst ein OLE fähiges Grafikprogramm (z. B. Paint Shop Pro 5 aus dem psp5inst Ordner) und den eDoc Drucker. Richten Sie diesen lt. Handbuch ein (> PDF Ablage und PDF Druckertreiber). Um den Druck mit Unterschrift ausführen zu können, muss an dem Notebook außerdem die Bildverarbeitung aktiviert werden. Ggf. ist diese bereits bei der Installation aktiviert worden.

Sollte die Bildverarbeitung bei der Installation nicht aktiviert worden sein, gehen Sie bitte wie folgt vor: In der Kundendienstliste unter <Bearbeiten> müssen Sie einmal die <Bildverarbeitung aktivieren>.

Unter Labelwin V5 sind diese Schritte nicht erforderlich. Alle benötigten Komponenten werden bereits bei der Installation mit installiert.

Das Ausdrucken muss dann mit einem Formular erfolgen, auf dem die Unterschrift mitgedruckt wird, z.B. auf einem der eben erwähnten Standardformulare.

Sie können aber auch Ihre bisherigen Formulare weiter verwenden, wenn Sie auf die Ankreuzfelder der Abschlussarbeiten und die 2 Unterschriften verzichten können.

Unterschriften-Pad

Sollte mit Ihrem mobilen Gerät keine Unterschrift erfasst werden können, so besteht auch die Möglichkeit ein Unterschriften-Pad anzuschließen. Hierbei ist allerdings zu beachten, dass Labelwin nur Unterschriften-Pads von dem Hersteller signotec aus der Reihe SIGMA ansteuern kann.

Um die Ansteuerung eines solchen Pads zu ermöglichen, müssen zwei Dinge passieren:

1. Schalter setzen in global.ini

[Grundeinstellungen]

kdsignotec=1

2. Software von signotec installieren > signoPAD-API Windows V. 8.4.1040 32/64 Bit

ACHTUNG Treiber 32/64 und NICHT 64 only
