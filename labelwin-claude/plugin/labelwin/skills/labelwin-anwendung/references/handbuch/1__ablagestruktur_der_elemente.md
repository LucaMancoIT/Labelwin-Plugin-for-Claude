# 1. Ablagestruktur der Elemente

Pfad: Kundendienst > TGM - Wartung und Instandhaltung [Modul] > 1. Ablagestruktur der Elemente
Quelle: handbuch/1__ablagestruktur_der_elemente.htm

|

1. Ablagestruktur der Elemente

Bei der Beschreibung der Einbaustandorte der Anlagenteile (eben jener erwähnten Ventilatoren, Brandschutzklappen usw.) erlaubt Labelwin eine fünfstufige Beschreibung. Diese Stufen sind so benannt:

[Bild]

Das Programm ist so konzipiert, dass bei einer einfacheren Ortsbeschreibung einige Stufen ausgelassen werden können. Zwingend erforderlich ist die Stufe 1 mit dem Vertrag und die Stufen ‚Anlage’ und ‚Anlagenteil’.

[Bild]

Zu der Benennung der Stufen muss gesagt werden, das diese im Grunde genommen willkürlich festgelegt wurden. Wir hätten auch die Bezeichnungen ‚Stufe 1’, ‚Stufe 2’ usw. nehmen können, aber wir halten die gewählten Beschreibungen für sprachlich einfacher anwendbar.

Auf jeder Stufe der Ortsbeschreibung können Daten wie Mieteradresse, Hausmeisteradresse, Rechnungsanschrift usw. hinterlegt werden.

Jede Stufe erlaubt bis zu 9999 Unterelemente. Ein Vertrag kann also bis zu 9999 Objekte beinhalten, ein Objekte bis zu 9999 Komplexe usw. Jede Stufe wird mit führenden Nullen aufgefüllt, so dass eine Ortbeschreibung mit 1.3.2.1.3den ersten Vertrag, dessen drittes Objekt, den zweiten Komplex usw. kennzeichnet.

Um die Gliederung der Ebenen abzuschließen wollen wir ein konkretes Beispiel bringen:

Vertrag: 1 Flughafen München

Objekt 1.2 Terminal B

Komplex 1.2.1 Parkhaus A

Wartungseinheit: 1.2.1.2 Parkreihe 1C

Anlage: 1.2.1.2.1 Abgasabsaugung

Anlagenteil: 1.2.1.2.1.1 Ventilator mit VDMA Nr. .................

Anlagenteil: 1.2.1.2.1.2 Filter mit VDMA Nr. .................

Anlagenteil: 1.2.1.2.1.3 Motor mit VDMA Nr. .................
