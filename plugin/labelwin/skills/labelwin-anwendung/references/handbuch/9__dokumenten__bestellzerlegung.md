# 9. Dokumenten-/Bestellzerlegung

Pfad: Projektverwaltung > Projektverwaltung [2] > 9. Dokumenten-/Bestellzerlegung
Quelle: handbuch/9__dokumenten__bestellzerlegung.htm

|

9. Dokumenten-/Bestellzerlegung

Stand: 04.02.2019

(V5.88)

Ursprünglich diente diese Funktion lediglich dazu, ein Angebot oder eine Auftragsbestätigung so zu zerlegen, dass die Bestellungen für die einzelnen Lieferanten daraus automatisch erzeugt wurden. Mittlerweile kann mit diesem Modul ein beliebiges Dokument nach verschiedenen Merkmalen zerlegt werden. So dient z.B. die Zerlegung nach Bonusgruppen dazu, ein Angebot nach betriebsinternen Merkmalen zu zerlegen. Bei den Bonusgruppen handelt es sich um ein vom Anwender frei zu vergebendes Merkmal, welches in den Artikelstammdaten hinterlegt werden kann. Der erste Kunde, für den wir diese Funktionalität programmiert haben, hat dort Bonusgruppen für Vorfertigung, Fliesenleger, Elektroarbeiten und dergleichen definiert. Nach der Auftragserteilung zerlegt er nun die Auftragsbestätigung nach diesen Merkmalen und händigt jedem Bereichsleiter die entsprechende Liste aus.

Wenn die Artikel eines Dokumentes aus verschiedenen Großhändlerkatalogen stammen, kann das Programm hieraus beliebig viele Einzeldokumente erzeugen. Die einzelnen Bestelldokumente werden in dem aktiven Projekt abgelegt und können dort aktiviert und ausgedruckt werden.

Adresszuordnung der Kataloge:

|

Die Bestellzerlegung ist nur dann erfolgreich nutzbar, wenn Sie bei jedem Lieferantenkatalog die entsprechende Adresse hinterlegen. Dazu müssen im ersten Schritt alle Adressen erfasst werden für die ein Katalog existiert. Anschließend müssen die Kataloge mit den Adressen verknüpft werden. Starten Sie dazu das Katalog-Modul und wählen den ersten Katalog aus. Wählen Sie dann im Menü <Katalog> <Katalog Grunddaten> an. Ordnen Sie hier dem Katalog die Händleradresse zu.

Aktivieren Sie nun nacheinander alle Kataloge und ordnen Ihnen auf die gleiche Art die Adressen zu. Den eigenen Katalog sollten Sie nicht mit einer Adresse versehen, da Sie damit verhindern können, dass diese Artikel aus Versehen bestellt werden.

|

Hinweis: Über einen Schalter können Sie erreichen, dass stattdessen die Adressnummer des Lieferanten zugeordnet wird und die Zerlegung dann aufgrund der Adresse erfolgt. Hierzu gibt es eine ausführliche Beschreibung im LabelWiki. In allen Labelwin Modulen erreichen Sie das LabelWiki über den Menüpunkt <Info> <MyLabelwin Wiki>. Geben Sie dann links in der Suche „Bestellhändler“ ein.

|

[Bild]

Dokumenten-/Bestellzerlegung aufrufen:

Je nach Einstellung bei der Zerlegung kann das Originaldokument dabei verändert werden. Aus diesem Grund ist davon abzuraten, direkt ein Angebot oder ähnliches als Vorlage zu verwenden. Die Veränderung der Vorlage geschieht immer dann, wenn Sie die Option "Massen verringern" anwählen. Wenn alle Artikel bestellt worden sind, enthält Ihre Vorlage dann überall die Menge 0. Wenn es sich um das Angebot gehandelt hat, kann dieses dann nicht mehr als Vorlage für die Rechnung verwendet werden.

|

Um auf der sicheren Seite zu sein, sollten Sie die Vorlage zuvor kopieren. Markieren Sie dazu die Vorlage und wählen im Menü <Start> <Dokument kopieren> an. Als Dokumentenart wählen Sie am besten ‚Bedarfsanforderung’ an. Diese Dokumentenart wird vom Programm als neutral behandelt und hat keinen Einfluss auf Statistiken. Mit dem OK-Knopf wird der Kopiervorgang ausgelöst und in der Dokumentenliste steht ein weiterer Eintrag.

Manchmal ist es sinnvoll, das Dokument mit der Funktion ‚Gleiche Artikel zusammenfassen’ zu bearbeiten. Damit werden die Mengen von mehrfach vorhandenen Artikeln zu den ersten Positionen hinzu geschlagen.

|

[Bild]

|

Mit dem so erzeugten Dokument starten Sie dann in die Dokumenten-/ Bestellzerlegung. Wählen Sie dazu den entsprechenden Menüpunkt entweder aus dem Kontextmenü oder über das Hauptmenü <Dokumente> <Dokuemntenzerlegung>.

|

Hinweis zu Sets:

In früheren Versionen wurden im Quelldokument alle Sets aufgelöst, um die Zerlegung durchführen zu können. Das ist inzwischen nicht mehr erforderlich. Im Quelldokument bleiben alle Sets unverändert. In den erzeugten Dokumenten sind dann aber alle Sets aufgelöst, da die Setbestandteile natürlich bei verschiedenen Lieferanten bestellt werden können sollen.

|

[Bild]

Bild: Dokumenten-/Bestellzerlegung im Kontextmenü

Dokumenten-/Bestellzerlegung ausführen:

[Bild: 9. Dokumenten-/Bestellzerlegung]

Bild: Dokumenten-/Bestellzerlegung

|
[Bild: 1]

Zerlegung gemäß

[Bild: 1. Zerlegung gemäß]

Hier müssen Sie zuerst festlegen nach welchem Kriterium das Dokument zerlegt werden soll. Am meisten genutzt werden dürfte die Zerlegung nach Bestellhändler, aber auch eine Aufteilung nach Bonusgruppe oder Materialgruppe ist möglich.

|
[Bild: 2]

Dokumente je Arbeitsbereich

[Bild: 2. Dokumente je Arbeitsbereich]

Diese Option macht nur Sinn, wenn Sie Arbeitsbereiche ja nach Baufortschritt definieren und die Baustelle eine gewisse Laufzeit hat. Nach der Zerlegung kann dann das Material für die einzelnen Bauabschnitte zeitlich passend bestellt werden.

|
[Bild: 3]

Zieldokument

[Bild: 3. Zieldokument]

Legen Sie hier fest, welche Dokumentenart bei der Zerlegung erzeugt werden soll, ob z.B. eine Bestellung oder ein Lieferschein.

|
[Bild: 4]

Dokument erzeugen für

[Bild: 4. Dokument erzeugen für]

Mit dieser Option können die Artikel eines bestimmten Lieferanten aus der Vorlage herausgelöst werden. Ggf. wird hierdurch lediglich ein Bestelldokument für einen bestimmten Lieferanten erzeugt.

|
[Bild: 5]

Umgang mit Lagerartikeln

[Bild: 5. Umgang mit Lagerartikeln]

Dieser Bereich ist nur anwählbar, wenn Lagerartikel im Dokument enthalten sind. Legen Sie hier fest, ob Sie für die Lagerartikel ein getrenntes Dokument erzeugen möchten, ob die Lagerkennzeichen nicht beachtet werden soll, ein Lagerauszug erstellt werden soll oder ob die Lagerartikel gar nicht verteilt werden sollen.

Hinweis: Wird als Dokument die Lagerentnahme gewählt, führt das dazu, dass das Projekt sofort belastet wird und man spart sich den Aufwand, den Wareneingang für die Zieldokumente (meistens Bestellungen) zu buchen. Allerdings führt dies auch zu möglichen Fehlern, wenn die Artikel auf dem Lager doch nicht alle vorhanden sind. Welche Methode für die Betriebe die bessere ist, muss jeder selbst entscheiden.

|
[Bild: 6]

Wenn Bestand nicht ausreicht

[Bild: 6. Wenn Bestand nicht ausreicht]

Wenn Artikel auf dem Lager geführt werden, aber für den konkreten Auftrag mehr benötigt werden, als momentan vorhanden sind, können Sie hier das Verhalten festlegen.

1. Bei "komplett bestellen" wird die Position komplett beim Lieferanten bestellt (bzw. in das Bestelldokument eingetragen).

Es kann aber auch sinnvoll sein, die Position komplett in die Packliste einzutragen. Dann muss der Lagerist dafür sorgen, dass er die Bestände passend aufstockt. Sinnvoll kann diese Vorgehensweise sein, wenn für die Lagerartikel Sonderpreise vereinbart sind und es sonst teurer wird.

2. Mit der Option "aufteilen" wird die komplette Menge immer dann beim Lieferanten bestellt, wenn der Mindestbestand im Lager unterschritten würde.

Ohne diesen Haken wird eine Position ggf. aufgeteilt (abhängig vom nächsten Ankreuzfeld [Nr.7]).

|
[Bild: 7]

Nur bis MIndestbestand reduzieren

[Bild: 7. Nur bis MIndestbestand reduzieren]

Wenn Sie dieses Feld aktivieren, wird bei der Bestellzerlegung zunächst die entsprechende Menge vom Lager genommen, bis der Mindestbestand für den Artikel erreicht ist. Sollte die Bestellmenge höher sein, erscheint die Restmenge im Bestelldokument.

|
[Bild: 8]

Lageradresse

[Bild: 8. Lageradresse]

Geben Sie hier die Lageradresse ein.

|
[Bild: 9]

Status Quelldokument

[Bild: 9. Status Quelldokument]

Mit dieser Einstellung kann festgelegt werden, ob bzw. wie der Status des Quelldokumentes nach der Zerlegung umgesetzt werden soll. Die Umsetzungstabelle wird im Modul EINSTELLUNGEN im Bereich Dokumentenstatus umsetzen verwaltet.

|
[Bild: 10]

Massen des Quelldokumentes verringern

[Bild: 10. Massen des Quelldokumentes verringern]

Bei dieser Option werden die Mengen im Vorlagedokument um die Bestellmenge reduziert. Bei Verwendung dieser Option sollten Sie sicher sein, dass die Werte der Gesamtmengen nicht mehr benötigt werden (oder zuvor eine Kopie vom Quelldokument erstellen).

|
[Bild: 11]

gleiche Artikel zusammenfassen

[Bild: 11. gleiche Artikel zusammenfassen]

Mit dieser Option werden in den Zieldokumenten möglicherweise vorhandene gleiche Artikel zusammengefasst.

|
[Bild: 12]

nur Lagerdokument erstellen

[Bild: 12. nur Lagerdokument erstellen]

Dieser Button ist nur vorhanden, wenn Lagerartikel im Dokument enthalten sind und im Bereich [Nr.5] "Lagerdokument erzeugen" angehakt ist. Auf diese Weise lässt sich nur das Lagerdokument erzeugen ohne die sonst zusätzlich erzeugten Zerlegungsdokumente.

|
[Bild: 13]

Haupthändler aus Verknüpfung

[Bild: 13. Haupthändler aus Verknüpfung]

Wenn Sie dieses Feld aktivieren, werden alle verknüpften Artikel, bei denen ein Haupthändler eingetragen ist, beim Haupthändler bestellt.

Beispiel: Sie haben einen Artikel aus dem Großhändlerkatalog A in Ihrem Angebot. Dieser ist jedoch verknüpft und als Haupthändler ist Großhändler B eingetragen. Dieser Artikel wird dann nicht bei A sondern bei B bestellt.

|
[Bild: 14]

Text und Artikelnummer des Bestellhändlers

[Bild: 14. Text und Artikelnummer des Bestellhändlers]

Mit diesem Schalter können Sie erreichen, dass in den neuen Dokumenten die Artikelnummer und der Artikeltext des Bestellhändlers verwendet werden. Dies erfolgt aber nur dann, wenn Sie die Artikel miteinander verknüpft haben.

Beispiel: Sie rufen einen Artikel mit der Nummer 1234 des Händler XYZ auf, den Sie wegen der 'schönen' Texte im Angebot verwenden möchten. Wenn Sie es schon wissen, dass Sie diesen Artikel bei dem Händler abc kaufen wollen, schalten Sie in der Artikelmaske die Auswahl 'Bestellhändler' auf den Händler abc um.

Der Artikel 1234 des Händlers xyz ist verknüpft mit einem entsprechenden Artikel des Händler abc. Nun schaut das Programm nach, ob es zu dem Artikel 1234 einen verknüpften Artikel des Händlers abc gibt. Wenn ja, wird dieser aufgerufen und dessen Text und Artikelnummer in das neue Dokument (die Bestellung) eingetragen.

|
[Bild: 15]

Auch Artikel mit Menge 0 übernehmen

[Bild: 15. Auch Artikel mit Menge 0 übernehmen]

Wählen Sie diesen Punkt nur in Verbindung mit dem Punkt Übernahme mit Einzelbestätigung. Hier haben Sie dann die Möglichkeit, in der Einzelbestätigung die Menge 0 zu korrigieren und können die korrekte Stückzahl eingeben.

|
[Bild: 16]

Alternativen/Eventuale übernehmen

[Bild: 16. Alternativen/Eventuale übernehmen]

Manchmal ist es notwendig, dass die Alternativen / Eventualen mit bestellt werden. Durch Aktivieren dieses Feldes werden solche Artikel bei den Bestellungen berücksichtigt.

|
[Bild: 17]

evtl. vorhandene Bestellungen übernehmen

[Bild: 17. evtl. vorhandene Bestellungen übernehmen]

Falls im aktiven Projekt ein noch nicht ausgedrucktes Bestelldokument vorhanden ist, können die Bestellartikel an dieses Dokument angehängt werden. In der Regel ist es sinnvoll, diese Möglichkeit nicht zu nutzen, damit Sie auch Rechnungen je Bauvorhaben erhalten.

|
[Bild: 18]

Bestellungen sofort drucken

[Bild: 18. Bestellungen sofort drucken]

Die durch die Zerlegung erzeugten Bestelldokumente können mit dieser Option direkt gedruckt werden.

|
[Bild: 19]

Vorbemerkung erfassen

[Bild: 19. Vorbemerkung erfassen]

Hier haben Sie die Möglichkeit, die Vorbemerkung ihres Dokuments zu ändern bzw. zu ergänzen.

|
[Bild: 20]

Nachbemerkung erfassen

[Bild: 20. Nachbemerkung erfassen]

Durch Betätigung dieses Knopfes gelangen Sie in die Nachbemerkung Ihres Dokuments und können Änderungen oder Ergänzungen vornehmen.

|
[Bild: 21]

Übernahme mit Einzelbestätigung

[Bild: 21. Übernahme mit Einzelbestätigung]

In diesem Fenster werden die Positionen nacheinander angezeigt. Die vorgeschlagene Bestellmenge ist immer die im Vorlagedokument enthaltene Menge und kann verändert werden. Wenn Sie in der vorherigen Maske ‚Massen verringern’ angekreuzt haben, werden die Mengen in der Vorlage entsprechend reduziert.

|

[Bild] Bild: Zerlegung mit Einzelbestätigung

|

1 Bestellhändler: Hier legen Sie den Großhändler fest, bei dem Sie diesen Artikel bestellen möchten. Standardmäßig wird der Händler vorgeschlagen, den Sie beim Artikelaufruf festgelegt haben.

2 Artikel vom Lager nehmen: Setzen Sie hier ein Kreuz, wenn Sie den vorgeschlagenen Artikel von Ihrem Lager nehmen möchten.

3 Auszugsmenge: Die hier eingesetzte Menge wird in das Bestelldokument übertragen.

4 Übernahme abbrechen: Durch Betätigen dieses Knopfes wird die Zerlegung abgebrochen. Bereits zugeordnete Positionen bleiben in den Bestelldokumenten erhalten. Es handelt sich nicht um einen Abbruch mit Rücknahme der Verteilung, sondern es werden lediglich keine weiteren Positionen verteilt.

5 Nicht übernehmen: Das Programm springt zur nächsten Position.

6 OK Übernehmen: Der Artikel wird in das Bestelldokument des entsprechenden Großhändlers eingetragen. Der Vorgang ist nicht rückgängig zu machen. Es erfolgt automatisch die Anzeige der nächsten Position.

|
[Bild: 22]

Lieferanschrift

[Bild: 22. Lieferanschrift]

Geben Sie hier Ihre Lieferanschrift ein. Sie haben die Möglichkeit, zwischen Lager, Objekt, sonstige Anschriften oder aus der hinterlegten Adresse im Datenblatt zu wählen.

|
[Bild: 23]

Ende

[Bild: 23. Ende]

Die Maske wird geschlossen ohne die Bestellzerlegung zu starten.

|
[Bild: 24]

OK

[Bild: 24. OK]

Hiermit wird die Bestellzerlegung gestartet. Bei der Wahl mit Einzelbestätigung erscheint die nächste Maske, anderenfalls erfolgt die komplette Zerlegung automatisch.
