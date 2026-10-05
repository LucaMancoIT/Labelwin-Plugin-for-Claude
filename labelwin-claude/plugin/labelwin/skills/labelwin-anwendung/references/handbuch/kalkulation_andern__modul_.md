# Kalkulation ändern [Modul]

Pfad: Dokumentenbearbeitung > Dokumentenerstellung [3] > Kalkulation ändern [Modul]
Quelle: handbuch/kalkulation_andern__modul_.htm

|

Kalkulation ändern [Modul]

Sie erreichen diesen Programmbereich, indem Sie bei der Erstellung eines Dokumentes unter dem Menüpunkt <Optionen> <Kalkulation ändern> anwählen. Die Bezeichnung ist an sich nicht völlig korrekt, es müsste heißen ‚Kalkulation analysieren und ggf. ändern’. Mit diesem Programm-Modul wird das aktive Dokument analysiert und kann ggf. auch verändert werden. Dabei beziehen sich die Veränderungen lediglich auf die preisliche Seite – Text und Mengenänderungen sind hier nicht möglich.

Für die Analyse und die Umkalkulation können Eingrenzungen über die Titel, Materialgruppen oder Lohngruppen getroffen werden. Bei einer Eingrenzung ist in der Tabelle (Nr. 6) lediglich dieser eingegrenzte Bereich sichtbar. Die angezeigten Gesamtpreise (Feld 7) beziehen sich ebenfalls auf diese eingegrenzte Artikelmenge. Um eine Änderung durchzuführen genügt es in dem entsprechenden Summenfeld eine andere Zahl einzutragen. Beim Verlassen des Summenfeldes werden automatisch alle anderen Summenfelder aktualisiert. Das eigentliche Dokument ist in diesem Moment jedoch noch nicht umkalkuliert. Aus Zeitgründen geschieht dies erst dann, wenn Sie den Knopf ‚Dokument umkalkulieren’ (Nr. 13) betätigen.

Für diejenigen die eine Kalkulationsänderung lieber über andere Multiplikatoren durchführen, haben wir eine separate Maske vorbereitet. Über den Knopf ‚Andere Multis’(Nr. 15) wird eine Form geöffnet, in der Sie die gewünschten Multiplikatoren eintragen können.

Beim Verlassen dieses Bereiches können Sie entscheiden, ob die ganzen Änderungen nur versuchsweise erfolgt sind oder tatsächlich wirksam werden sollen.

Beim Drucken greift das Programm wieder auf verschiedene Formulare zurück, so dass das Aussehen der Analysen auf Papier mit Hilfe des Reportgenerators frei gestaltbar ist.

An dieser Stelle möchten wir Sie auch noch auf die Blockbearbeitung hinweisen, mit der Sie ebenfalls eine ähnliche Preisänderung vornehmen können. Der entscheidende Unterschied ist, dass man bei der Blockbearbeitung einzelne Artikel herauspicken kann, während bei der Umkalkulation alle Artikel oder zumindest einzelne Titel geändert werden. Die Blockbearbeitung ist im Kapitel Blockbearbeitung beschrieben.

[Bild]

Bild: Kalkulationsauswertung

Über die Felder 1, 2, 3, 4 und 5 können Eingrenzungen der angezeigten Artikel getroffen werden. Dazu ist es allerdings erforderlich, dass bereits bei der Dokumenterstellung Einteilungen vorgenommen worden sind.

[Bild]

1 Titel: Wenn Sie in dem Dokument mit verschiedenen Titeln gearbeitet haben, so können Sie hier eine Eingrenzung darüber treffen. Das Programm erkennt Titel an der Artikelart Titel.

[Bild]

2 Materialgruppe: Wenn Sie bei der Dokumenterstellung verschiedene Material-gruppen verwendet haben, so kann hierüber eine Begrenzung erfolgen. Die Einträge gelangen in das Dokument, indem der aufgerufene Artikel bereits in den Stammdaten einer Materialgruppe zugeordnet worden oder beim Artikelaufruf jeweils eine Materialgruppe angewählt worden ist. Die Gruppenkalkulation wird wahrscheinlich von den wenigsten Kunden angewählt werden. Details lesen Sie in dem Kapitel Einstellungen - Kalkulationsgruppen nach.

[Bild]

3 Lohngruppe: Wenn Sie bei der Dokumenterstellung mit der Lohngruppenkalkulation gearbeitet haben, so können Sie hier aus der Liste eine Eingrenzung treffen. Diese Eingrenzung wird Sie höchstwahrscheinlich nicht betreffen, da die wenigsten Kunden eine gruppenweise Kalkulation durchführen werden. Die verschiedenen Lohngruppen müssen über das Modul EINSTELLUNGEN unter dem Menüpunkt <Grundeinstellung> <Gruppenkalkulation> <Lohngruppen> erfasst werden. Sie sind nur dann aktiv, wenn in der Kalkulationseinstellung des Dokumentes der Lohngruppenrahmen größer als 0 ist.

[Bild]

4 Arbeitsbereich: Wenn Sie bei der Dokumenterstellung mit Arbeitsbereichen gearbeitet haben, so können Sie hier aus der Liste eine Eingrenzung treffen. Die verschiedenen Arbeitsbereiche müssen über das Modul EINSTELLUNGEN unter dem Menüpunkt <Programmbereiche> <Zeitwirtschaft> <Arbeitsbereiche> erfasst werden.

[Bild]

5 Kostenstelle: Bei den Kostenstellen handelt es sich um ein Zusatzmodul. Wenn Sie diese aktiviert und damit gearbeitet haben, können Sie hier ebenfalls eine Eingrenzung treffen. Die Kostenstellen werden im Menü EINSTELLUNGEN unter dem Menüpunkt <Grundeinstellungen> <Kostenstellen> erfasst.

[Bild]

6 Ausgabe in Euro: Durch die Euroumstellung ist hier bei neuen Dokumenten generell das Häkchen gesetzt. Bei alten, noch in Landeswährung kalkulierten Dokumenten fehlt das Häkchen.

[Bild]

7 Tabelle: In dieser Tabelle werden die wichtigsten Artikelinformationen gezeigt. Da die Tabelle nicht breit genug ist, um sämtliche Daten auf dem Bildschirm zu zeigen, können Sie mit dem Laufbalken unten die Anzeige verändern. In dem unsichtbaren Bereich befinden sich Informationen über den Materialertrag und ähnliches.

Die Felder im Einzelnen:

Pos-Nr.:

Art: Wenn ein Artikel ein besonderes Merkmal hat, zeigen wir dieses hier an. Dabei bedeutet A = Alternativ , E = Eventual , N = Neutralposition , K = Nicht umkalkulierbar.

W: Erscheint hier der Hinweis ?M, wurde der Mindestmulti unterschritten. Erscheint hier ein Hinweis ?E, wurde der Einkaufspreis unterschritten. Die Preisänderung des Artikels ist jedoch an dieser Stelle nicht möglich. Sie müssen sich die Position merken oder ausdrucken und dann in der Artikelbeabeitungsmaske ändern.

Typ: Anzeige von Setanfängen, Setsummen, Titelanfängen, Titelsummen etc.

Kurztext: Kurztext aus dem Artikel

Menge: Menge des Artikels aus Dokument

Einzelpreis: Einzel – Verkaufspreis für 1 Stück

Gesamtpreis: Gesamt – Verkauf (= Menge x Einzelpreis)

Material: Material – Verkaufspreis je Stück

Einkauf: Material – Einkaufspreis je Stück

Lohnmin: Kalkulierte Lohnminuten je Stück

Lohn: Lohnkosten je Stück

Mat-Multi: Multiplikator zwischen Material Einkauf und Materialverkauf

Fremdl.VK: Verkaufpreis Fremdleistung je Stück

Fremdl.EK: Einkaufspreis Fremdleistung je Stück

Sonst.VK: Verkaufpreis Sonstige Kosten je Stück

Sonst.EK: Einkaufspreis Sonstige Kosten je Stück

Rohertrag: Differenz zwischen Gesamtverkauf und Gesamtkosten nicht je Stück

[Bild]

8 Summenfeld Gesamt: Hier werden die Felder der Gesamtsummen angezeigt. In allen weiß hinterlegten Feldern können Sie einfach andere Werte hineinschreiben und beim Verlassen des Feldes werden automatisch alle anderen Werte aktualisiert. Dabei findet die Änderung jedoch nicht sofort in den eigentlichen Artikeln statt, sondern lediglich in dieser Zusammenstellung. Die tatsächliche Änderung der Artikel wird erreicht, wenn Sie den Knopf ‚Dokument umkalkulieren’ (Nr. 13) betätigen. Da dieser Vorgang bei langen Dokumenten ggf. einige Zeit dauert, wird er nicht automatisch gestartet.

Die meisten Datenfelder in diesem Bereich bedürfen sicherlich keiner Erläuterung - lediglich auf den Deckungsbeitrag je Stunde möchten wir an dieser Stelle noch eingehen. Der Deckungsbeitrag ist der Erlös je eingesetzter Arbeitsstunde. Der Deckungsbeitrag aufgrund des Lohnes ist daher die Differenz zwischen Lohnselbstkosten und Lohnverkaufspreis. Der Materialdeckungsbeitrag ermittelt sich aus der Differenz zwischen Materialverkauf und Materialeinkauf geteilt durch die Anzahl der eingesetzten Arbeitsstunden. Der Gesamtdeckungsbeitrag ist dann die Summe dieser beiden Beträge. Für die Beurteilung eines Auftrages ist der Deckungsbeitrag ein wesentlich wichtigerer Wert als der Ertrag. Für die Bewertung ist entscheidend, in welcher Zeit dieser Ertrag erwirtschaftet wird.

[Bild]

9 Neutralpositionen: Ähnlich dem Kennzeichen als Eventual- oder Alternativposition können bei der Artikelerfassung einzelne mit dem Kennzeichen ‚Neutralposition’ versehen werden. Die Kennzeichnung hat den Zweck, dass solche Positionen bei der Umkalkulation ausgelassen werden können. Damit soll verhindert werden, dass so genannte Angstpositionen von Planern wie ‚200 Stunden diverse Arbeiten, Abrechnung nach Aufwand’ in die Kalkulation nicht einfließen. Durch solche Angstpositionen, die nachher nicht wirklich zum Einsatz kommen, wird jegliche Deckungsbeitragsrechnung unsinnig. Da solche Positionen dennoch in die Angebotsabgabe einfließen müssen, können wir sie hier bei der Umkalkulation neutralisieren.

10 Summenfeld Details: Die hier aufgeführten Summen unterteilen sich in Material, Lohn, Fremdleistungen und sonstige Kosten. Auch hier haben Sie die Möglichkeit, in allen weiß hinterlegten Feldern Änderungen vorzunehmen. Die Werte werden beim Verlassen des Feldes automatisch aktualisiert. Die Änderung findet nur in dieser Zusammenstellung statt. Die tatsächliche Änderung erfolgt über den Knopf ‚Dokument umkalkulieren’ (Nr. 14)

Über die Eingabe in dem Feld ‚Folgerabatt’ können Sie die Einkaufspreise für den aktiven Dokumentbereich verändern. Der Dokumentbereich kann ggf. über den Titel oder Gruppen begrenzt sein.

[Bild]

[Bild]

11 Umkalkulation:

Einzelpreise runden: Durch ein Kreuz in diesem Feld erreichen Sie, dass bei der Umkalkulation die Artikelpreise aufgerundet werden. Die Rundung erfolgt aufgrund der im Modul EINSTELLUNGEN unter dem Menüpunkt <Grundeinstellungen> <Rundungstabelle> getroffenen Vorgaben. Wenn Sie dieses Feld aktiv geschaltet haben, kann das Programm selbstverständlich einen ganz bestimmten Verkaufspreis nicht mehr erreichen, da die Summen durch das Aufrunden beeinflusst werden.

Alternativen und Eventuale / Neutralpositionen mit umkalkulieren: Alternativ- und Eventualpositionen werden in den gezeigten Gesamtsummen nicht berücksichtigt.

Sie haben keine Auswirkung auf den Gesamtpreis eines Angebotes. Bei einer Umkalkulation ist es in der Regel sinnvoll, diese Positionen ebenfalls mit umzukalkulieren. Zur Umkalkulation der Neutralpositionen lesen Sie bitte im vorherigen Absatz.

Festpreisartikel mit umkalkulieren: Beim Aufrufen von Artikeln besteht die Möglichkeit, diesen als Festpreis zu deklarieren. Wenn beim Artikelaufruf der hinterlegte Verkaufspreis 1 oder 2 genommen wird, so wird dieser automatisch als Festpreis festgelegt. Bei der Umkalkulation gehen wir davon aus, dass diese Festpreise in der Regel erhalten bleiben sollen. Dadurch ist es z. B. möglich, die solchermaßen festgelegten Artikel unverändert zu lassen und die Preisänderung auf alle anderen Artikel zu verteilen. Durch ein Kreuz an dieser Stelle werden die Festpreise freigegeben und die Änderung an sämtlichen Artikeln durchgeführt.

[Bild]

12 Anzeige: Standardmäßig werden in den Deckungsbeitrag die Neutralpositionen nicht berücksichtigt. In der Kurauswertung (F9) in der Artikelerfassung werden dagegen alle Positionen einbezogen. Damit unterscheidet sich der ausgewiesene Deckungsbeitrag in beiden Fenstern. Wenn Sie hier ein Kreuz setzen, werden alle Positionen mit in den Deckungsbeitrag einbezogen. Des Weiteren erhalten Sie hier Hinweise, wenn sich in Ihrem Dokument Artikel mit Festpreis befinden oder es Artikel gibt, in denen der Mindestmulti unterschritten wurde oder der EK=0 ist.

[Bild]

13 Drucken: Durch Betätigen dieses Knopfes gelangen Sie in die Druckausgabe der Kalkulationsanalyse. Das Programm greift auf Formulare zurück, die über den Crystal Report frei gestaltbar sind. Wir haben standardmäßig folgende Formulare mitgeliefert:

|

KAEU1

|

Kalkulation gesamt ,EP, Einkauf, Zeit, Lohn, Rohertrag, Zusammenfassung

|

KAEU2

|

Kalkulation, nur Zusammenfassung

|

KAEU3

|

Kalkulation gesamt, mit Gesamtpreis ohne Rohertrag, EP, GP, Einkauf, Zeit, Lohn, Zusammenfassung

|

KAEU4

|

Kalkulation, gesamt, mit Gesamtpreis und Material

|

KAEU5

|

Kalkulation gesamt mit Brutto, Rabatt, Aufschlag

|

KAEU6

|

Kalkulation gesamt mit Fremdleistung und sonstigen Kosten

|

KAEUARB

|

Kalkulation gesamt mit Fremdleistung und sonstigen Kosten nach Arbeitsbereichen

Tabelle: Formulare für Kalkulationen

[Bild]

14 Dokument umkalkulieren: Durch Betätigen dieses Knopfes werden alle Artikel aufgrund der in den Summenfeldern vorgenommenen Änderungen durchkalkuliert. Aus Zeitgründen erfolgt die Umkalkulation nicht automatisch bei der Änderung eines Summenfeldes.

[Bild]

15 Originaldokument: Durch Betätigen dieses Knopfes wird das Originaldokument aktiviert und alle von Ihnen vorgenommenen Änderungen verworfen. Wenn Sie also ein Dokument total ‚kaputt kalkuliert’ haben, so können Sie mit diesem Knopf wieder neu anfangen.

[Bild]

16 Andere Multis: Durch Betätigen dieses Knopfes gelangen Sie in eine Maske, in der Sie mit anderen Multiplikatoren kalkulieren können. Da diese Maske recht umfangreich ist, haben wir diesen Bereich im Anschluss an dieses Kapitel beschrieben.

[Bild]

17 OK/Ende: Durch Betätigen dieses Knopfes wird das Programm-Modul verlassen. Eventuell vorgenommenen Kalkulationsänderungen werden in das Dokument übernommen.

[Bild]

18 Abbruch: Durch Betätigen dieses Knopfes wird das Programm-Modul verlassen. Alle ggf. vorgenommenen Änderungen werden verworfen.
