# Einlesen eines neuen Angebotes

Pfad: Dokumentenbearbeitung > Dokumentenerstellung [3] > UGL-Schnittstelle > Einlesen eines neuen Angebotes
Quelle: handbuch/einlesen_eines_neuen_angebotes.htm

|

Einlesen eines neuen Angebotes

Im Folgenden geht es darum, Angebote oder Lieferscheine per UGL einzulesen, zu denen kein Dokument im Labelwin System gehört.

Legen Sie zunächst ein neues Dokument an. Als Dokumentenart wählen Sie am besten je nach Ziel ein Angebot oder bei Lieferscheinen per UGL den Eingangslieferschein an. Stellen Sie die Kalkulation so ein, wie Sie die übernommenen Artikel kalkulieren wollen. Bei Eingangslieferscheinen stellen Sie am Besten EK x 1 ein, obwohl es hier im Grunde genommen nur um die Einkaufspreise geht. Wenn auch an der Oberfläche in der Tabelle die Einkaufspreise sichtbar sind, können nicht so leicht Missverständnisse auftreten.

Wählen Sie dann in der Maske, in der die bisher aufgerufenen Artikel sichtbar sind; den Menüpunkt <Vorlagen> <UGL-Dateien übernehmen> <Datei an Dokument anhängen> an. Es erscheint die Maske mit der Liste der vorhandenen Eingangsdateien:

[Bild]

Markieren Sie hier die zu übernehmende Datei und betätigen den Knopf ‚An Dokument anhängen’.

Alle in der UGL-Datei abgelegten Artikel werden möglichst aus den Artikelstammdaten aufgerufen und nur der Preis aus der UGL-Datei genommen. Dieses findet statt, damit evtl. hinterlegte Lohnminuten und Sonderverkaufspreise in die Kalkulation einbezogen werden können. Statt des Einkaufspreises aus den Artikelstammdaten wird jedoch – falls vorhanden – der in der UGL-Datei hinterlegte Einkaufspreis verwendet. Je nach eingestellter Kalkulation wird dieser Preis zur Findung des Verkaufspreises oder auch nur zur Registrierung des Einkaufspreises eingesetzt werden. Wenn ein Artikel nicht in den Stammdaten vorhanden ist (Sonderbeschaffung oder Katalog ist nicht aktuell) werden alle Informationen aus den Stammdaten entnommen. In diesem Fall fehlen die Lohnminuten immer, da die UGL-Datei keine Werte dafür enthält.

Nach kurzer Zeit sind die Artikel übernommen und das Programm fragt nach, ob die Ursprungsdatei gelöscht werden soll. Wenn Sie nicht unnütz Dateileichen aufbauen wollen, sollten Sie sich von den übernommenen Daten trennen.

In den übernommenen Daten steht am Anfang ein ‚Geheimartikel’, in dem Informationen zur Datenquelle eingetragen sind. Da Geheimartikel nie an den Kunden ausgedruckt werden, stört diese Position nicht.

|

Viessmann-Konfigurator Import

Einige unserer Kunden setzen den Heizungskonfigurator von Viessmann ein. Dieser erzeugt eine UGL-Datei, die im Labelwin wie jede andere UGL eingelesen werden. Allerdings gibt es eine Besonderheit, um Minuten und Einkaufspreise zu übernehmen. Dazu wird die mobile offer-Erweiterung genutzt.

Allerdings werden bisher bei UGL-Dateien Sets als verborgen übernommen, weil die Bestandteile üblicherweise die zu bestellenden Materialien sind, die der Endkunde nicht sehen soll. Bei der UGL vom Viessmann-Konfigurator enthalten aber die Bestandteile die wichtigen Informationen. Deshalb müssen Sie bei dieser Übernahme den Haken bei "Sets auf offen statt verborgen setzen" (unten links) setzen.

|

[Bild]
