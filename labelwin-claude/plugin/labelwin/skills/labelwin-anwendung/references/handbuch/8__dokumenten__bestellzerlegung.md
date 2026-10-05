# 8. Dokumenten-/Bestellzerlegung

Pfad: Projektverwaltung > Projektverwaltung [2] > 8. Dokumenten-/Bestellzerlegung
Quelle: handbuch/8__dokumenten__bestellzerlegung.htm

|

8. Dokumenten-/Bestellzerlegung

Ursprünglich diente diese Funktion lediglich dazu, ein Angebot oder eine Auftragsbestätigung so zu zerlegen, dass die Bestellungen für die einzelnen Lieferanten daraus automatisch erzeugt wurden. Mittlerweile kann mit diesem Modul ein beliebiges Dokument nach verschiedenen Merkmalen zerlegt werden. So dient z.B. die Zerlegung nach Bonusgruppen dazu, ein Angebot nach betriebsinternen Merkmalen zu zerlegen. Bei den Bonusgruppen handelt es sich um ein vom Anwender frei zu vergebendes Merkmal, welches in den Artikelstammdaten hinterlegt werden kann. Der erste Kunde, für den wir diese Funktionalität programmiert haben, hat dort Bonusgruppen für Vorfertigung, Fliesenleger, Elektroarbeiten und dergleichen definiert. Nach der Auftragserteilung zerlegt er nun die Auftragsbestätigung nach diesen Merkmalen und händigt jedem Bereichsleiter die entsprechende Liste aus.

Wenn die Artikel eines Dokumentes aus verschiedenen Großhändlerkatalogen stammen, kann das Programm hieraus beliebig viele Einzeldokumente erzeugen. Die einzelnen Bestelldokumente werden in dem aktiven Projekt abgelegt und können dort aktiviert und ausgedruckt werden.

Adresszuordnung der Kataloge:

Die Bestellzerlegung ist nur dann erfolgreich nutzbar, wenn Sie bei jedem Lieferantenkatalog die entsprechende Adresse hinterlegen. Dazu müssen im ersten Schritt alle Adressen erfasst werden, für die ein Katalog existiert. Anschließend müssen die Kataloge mit den Adressen verknüpft werden. Starten Sie dazu das Katalog-Modul und wählen den ersten Katalog aus. Wählen Sie dann im Menü <Katalog> <Katalog Grunddaten> an. Ordnen Sie hier dem Katalog die Händleradresse zu. Aktivieren Sie nun nacheinander alle Kataloge und ordnen Ihnen auf die gleiche Art die Adressen zu. Den eigenen Katalog sollten Sie nicht mit einer Adresse versehen, da Sie damit verhindern können, dass diese Artikel aus Versehen bestellt werden.

Über einen Schalter können Sie erreichen, dass stattdessen die Adressnummer des Lieferanten zugeordnet wird und die Zerlegung dann aufgrund der Adresse erfolgt. Hierzu gibt es eine ausführliche Beschreibung im LabelWiki. In allen Labelwin Modulen erreichen Sie das LabelWiki über den Menüpunkt <Info> <MyLabelwin Wiki>. Geben Sie dann links in der Suche „Bestellhändler“ ein.

Dokumenten-/Bestellzerlegung starten:

[Bild] [Bild]

Bild: Dokumenten-/Bestellzerlegung im ‚Dokumente’-Menü

Je nach Einstellung bei der Zerlegung kann das Originaldokument dabei verändert werden. Aus diesem Grund ist davon abzuraten, direkt ein Angebot oder ähnliches als Vorlage zu verwenden. Die Veränderung der Vorlage geschieht immer dann, wenn Sie die Option ‚Massen verringern’ anwählen. Wenn alle Artikel bestellt worden sind, enthält Ihre Vorlage dann überall die Menge 0. Wenn es sich um das Angebot gehandelt hat, kann dieses dann nicht mehr als Vorlage für die Rechnung verwendet werden.

[Bild] Um auf der sicheren Seite zu sein, sollten Sie die Vorlage zuvor kopieren. Markieren Sie dazu die Vorlage und wählen im Menü <Dokumente> <Dokument kopieren> an. Als Dokumentenart wählen Sie am besten ‚Bedarfsanforderung’ an. Diese Dokumentenart wird vom Programm als neutral behandelt und hat keinen Einfluss auf Statistiken. Mit dem OK-Knopf wird der Kopiervorgang ausgelöst und in der Dokumentenliste steht ein weiterer Eintrag.

Manchmal ist es sinnvoll, das Dokument mit der Funktion ‚Gleiche Artikel zusammenfassen’ zu bearbeiten. Damit werden die Mengen von mehrfach vorhandenen Artikeln zu den ersten Positionen hinzu geschlagen.

Mit dem so erzeugten Dokument starten Sie dann in die Bestellzerlegung.

[Bild]

Bild: Dokumenten-/Bestellzerlegung

[Bild]

1 Zieldokument: Legen Sie hier fest, welche Dokumentenart bei der Zerlegung erzeugt werden soll, ob z.B. eine Bestellung oder ein Lieferschein.

[Bild]

2 Alle Kataloge/bestimmter: Mit dieser Option können die Artikel eines bestimmten Lieferanten aus der Vorlage herausgelöst werden. Ggf. wird hierdurch lediglich ein Bestelldokument für einen bestimmten Lieferanten erzeugt.

[Bild]

3 Haupthändler aus Verknüpfung eintragen: Wenn Sie dieses Feld aktivieren, werden alle verknüpften Artikel, bei denen ein Haupthändler eingetragen ist, beim Haupthändler bestellt.

Beispiel: Sie haben einen Artikel aus dem Großhändlerkatalog A in Ihrem Angebot. Dieser ist jedoch verknüpft und als Haupthändler ist Großhändler B eingetragen. Dieser Artikel wird dann nicht bei A sondern bei B bestellt.

[Bild]

4 Lagerartikel: Legen Sie hier fest, ob Sie für die Lagerartikel ein getrenntes Dokument erzeugen möchten, ob die Lagerkennzeichen nicht beachtet werden soll, ein Lagerauszug erstellt werden soll oder ob die Lagerartikel gar nicht verteilt werden sollen.

[Bild]

5 Menge nicht aufteilen auf Lager / Lieferant: Mit diesem Kennzeichen wird die komplette Menge immer dann beim Lieferanten bestellt, wenn der Mindestbestand im Lager unterschritten würde.

Ohne aktiviertes Feld wird eine Position ggf. aufgeteilt (abhängig vom Feld Nr. 6).

[Bild]

6 Lagermengen nur bis Mindestbestand reduzieren: Wenn Sie dieses Feld aktivieren, wird bei der Bestellzerlegung zunächst die entsprechende Menge vom Lager genommen, bis der Mindestbestand für den Artikel erreicht ist. Sollte die Bestellmenge höher sein, erscheint die Restmenge im Bestelldokument.

[Bild]

7 Lageradresse: Geben Sie hier die Lageradresse ein.

[Bild]

8 Lieferanschrift: Geben Sie hier Ihre Lieferanschrift ein. Sie haben die Möglichkeit, zwischen Lager, Objekt, sonstige Anschriften oder aus der hinterlegten Adresse im Datenblatt zu wählen.

[Bild]

9 Eventuell vorhandene Bestellungen ergänzen: Falls im aktiven Projekt ein noch nicht ausgedrucktes Bestelldokument vorhanden ist, können die Bestellartikel an dieses Dokument angehängt werden. In der Regel ist es sinnvoll, diese Möglichkeit nicht zu nutzen, damit Sie auch Rechnungen je Bauvorhaben erhalten.

[Bild]

10 Massen verringern: Bei dieser Option werden die Mengen im Vorlagedokument um die Bestellmenge reduziert. Bei Verwendung dieser Option sollten Sie sicher sein, dass die Werte der Gesamtmengen in der Lage nicht mehr benötigt werden.

[Bild]

11 Übernahme mit Einzelbestätigung: Bei dieser Option werden die Artikel nacheinander gezeigt und können ggf. auch mit anderer Stückzahl bestellt werden.

[Bild]

12 Text und Artikelnummer des Bestellhändlers: Mit diesem Schalter können Sie erreichen, dass in den neuen Dokumenten die Artikelnummer und der Artikeltext des Bestellhändlers verwendet werden. Dies erfolgt aber nur dann, wenn Sie die Artikel miteinander verknüpft haben.

Beispiel: Sie rufen einen Artikel mit der Nummer 1234 des Händler XYZ auf, den Sie wegen der 'schönen' Texte im Angebot verwenden möchten. Wenn Sie es schon wissen, dass Sie diesen Artikel bei dem Händler abc kaufen wollen, schalten Sie in der Artikelmaske die Auswahl 'Bestellhändler' auf den Händler abc um.

Der Artikel 1234 des Händlers xyz ist verknüpft mit einem entsprechenden Artikel des Händler abc. Nun schaut das Programm nach, ob es zu dem Artikel 1234 einen verknüpften Artikel des Händlers abc gibt. Wenn ja, wird dieser aufgerufen und dessen Text und Artikelnummer in das neue Dokument (die fBestellung) eingetragen.

[Bild]

13 Auch Artikel mit Menge 0 übernehmen: Wählen Sie diesen Punkt nur in Verbindung mit dem Punkt Übernahme mit Einzelbestätigung. Hier haben Sie dann die Möglichkeit, in der Einzelbestätigung die Menge 0 zu korrigieren und können die korrekte Stückzahl eingeben.

[Bild]

14 Alternativen / Eventualen übernehmen: Manchmal ist es notwendig, dass die Alternativen / Eventualen mit bestellt werden. Durch Aktivieren dieses Feldes werden solche Artikel bei den Bestellungen berücksichtigt.

[Bild]

15 Vorbem. andern: Hier haben Sie die Möglichkeit, die Vorbemerkung ihres Dokuments zu ändern bzw. zu ergänzen.

[Bild]

16 Nachbem. Ändern: Durch Betätigung dieses Knopfes gelangen Sie in die Nachbemerkung Ihres Dokuments und können Änderungen oder Ergänzungen vornehmen.

[Bild]

17 OK-Knopf: Hiermit wird die Bestellzerlegung gestartet. Bei der Wahl mit Einzelbestätigung erscheint die nächste Maske, anderenfalls erfolgt die komplette Zerlegung automatisch.

[Bild]

18 Abbruch-Knopf: Die Maske wird geschlossen ohne die Bestellzerlegung zu starten.

Zerlegung mit Einzelbestätigung:

[Bild]

Bild: Zerlegung mit Einzelbestätigung

In diesem Fenster werden die Positionen nacheinander angezeigt. Die vorgeschlagene Bestellmenge ist immer die im Vorlagedokument enthaltene Menge und kann verändert werden. Wenn Sie in der vorherigen Maske ‚Massen verringern’ angekreuzt haben, werden die Mengen in der Vorlage entsprechend reduziert.

[Bild]

1 Bestellhändler: Hier legen Sie den Großhändler fest, bei dem Sie diesen Artikel bestellen möchten. Standardmäßig wird der Händler vorgeschlagen, den Sie beim Artikelaufruf festgelegt haben.

[Bild]

2 Artikel vom Lager nehmen: Setzen Sie hier ein Kreuz, wenn Sie den vorgeschlagenen Artikel von Ihrem Lager nehmen möchten.

[Bild]

3 Auszugsmenge: Die hier eingesetzte Menge wird in das Bestelldokument übertragen.

[Bild]

4 OK Übernehmen: Der Artikel wird in das Bestelldokument des entsprechenden Großhändlers eingetragen. Der Vorgang ist nicht rückgängig zu machen. Es erfolgt automatisch die Anzeige der nächsten Position.

[Bild]

5 Nicht übernehmen: Das Programm springt zur nächsten Position.

[Bild]

6 Übernahme abbrechen: Durch Betätigen dieses Knopfes wird die Zerlegung abgebrochen. Bereits zugeordnete Positionen bleiben in den Bestelldokumenten erhalten. Es handelt sich nicht um einen Abbruch mit Rücknahme der Verteilung, sondern es werden lediglich keine weiteren Positionen verteilt.
