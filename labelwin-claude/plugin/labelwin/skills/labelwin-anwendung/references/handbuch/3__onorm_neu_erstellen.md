# 3. ÖNorm neu erstellen

Pfad: Schnittstellen > ÖNorm > 3. ÖNorm neu erstellen
Quelle: handbuch/3__onorm_neu_erstellen.htm

|

3. ÖNorm neu erstellen

Mit der ÖNorm-Ausgabe können Sie eine auch ÖNorm-Datei erstellen, ohne vorher eine ÖNorm-Datei eingelesen zu haben. Die ÖNorm Ausgabe von selbst erstellten ÖNorm Dateien erfolgt ausschließlich im Format A2063 XML.

Starten Sie dazu einfach ein neues Dokument. Setzen Sie das Positionsschema wie oben unter „Positionsnummern“ beschrieben, z.B.

-

„pp“ (Bsp.: 01),

-

„aa.tt.pp“ (Bsp.: 01.01.01) oder

-

„bb.aa.tt.pp“ (Bsp.: 01.01.01.01)

Eine ÖNorm-Datei besteht entweder aus ‚nur Positionen“, aus „Los/Titel/Positionen“ oder aus „Bauteil/Los/Titel/Positionen“. Nur „Titel/Positionen“ ist nicht erlaubt.

Grundtexte, ungeteilte Positionen und Folgepositionen

Die ÖNorm Struktur arbeitet auf Positionsebene mit Grundtexten gefolgt von einer oder mehreren ungeteilten Positionen bzw. Folgepositionen.

Bsp.: Im Grundtext steht eine sehr ausführliche Beschreibung des Kupferrohrs. Danach kommen Folgepositionen, die dann nur noch ein Stichwort enthalten, z.B. „DN 15“ und dann eine Menge, Mengeneinheit und einen Preis haben bzw. bekommen sollen.

Labelwin kennt diese Technik nur bedingt. Jede Position ist für sich abgeschlossen. Bei der Ausgabe wird jede einzelne Labelwin Position in einen „Grundtext“ und eine „ungeteilte Position“ unterteilt.

-

Im Grundtext steht der Langtext, sofern gefüllt und der Haken bei „Langform“ gesetzt ist, ansonsten der Kurztext

-

In der ungeteilten Position stehen als Stichwort die ersten 60 Zeichen des Kurztextes, sowie Menge, Mengeneinheit, ggf. Preis, sowie bei Bedarf die Eigenschaften Alternativ bzw. Eventual

Bei Sets wird anders vorgegangen

Ein verborgener Set wird wie ein normaler Artikel behandelt. Alle Setbestandteile werden komplett ignoriert.

Beim Listenset wird der Setkopf als „Grundtext“ übernommen, also nur mit Text und ohne Mengen etc. Alle Setbestandteile werden vorher intern ausmultipliziert und als „Folgeposition“ mit Stichwort, Menge, Mengeneinheit etc. ausgegeben. Bedenken Sie also, dass bei den Setbestandteilen nur die ersten 60 Zeichen des Kurztextes als „Stichwort“ ausgegeben wird. Beim Setkopf dagegen kommt der gesamte Text, dafür entfällt aber Menge, Mengeneinheit etc.

Sets im Set werden wie eine Leistungspositionen behandelt.

Liefermengeneinheiten

Die ÖNorm erlaubt nur eine kleine Auswahl von Liefermengeneinheiten. Bitte beachten Sie das bei der Erfassung bzw. nutzen Sie die Option <Durchläufe>, <Liefereinheiten anpassen>. Folgende Einheiten sind erlaubt (bitte auch auf Groß-/Kleinschreibung und Sonderzeichen achten!):

cm m km cm² m² cm³ m³ l g kg t Stk PA h d Wo Mo VE

Textformatierungen

Die ÖNorm kann mit formatierten Texten umgehen. Allerdings benutzt die ÖNorm eine sehr eigene und eingeschränkte Syntax, so dass Labelwin diese Formatierungsbefehle nicht unterstützt. Die Ausgabe erfolgt immer unformatiert, auch wenn es Formatierungen gibt.
