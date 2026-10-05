# 3.2 TGM, Vertrag und Ortsbeschreibung

Pfad: Kundendienst > TGM - Wartung und Instandhaltung [Modul] > 3. Erfassung > 3.2 TGM, Vertrag und Ortsbeschreibung
Quelle: handbuch/3_2_tgm__vertrag_und_ortsbeschreibung.htm

|

3.2 TGM, Vertrag und Ortsbeschreibung

Diese Maske dient der Erfassung der Vertragsdaten und der Ortsbeschreibung der Anlagen.. Wie bereits erwähnt kann die Beschreibung auf bis zu 4 Hierarchiestufen erfolgen, wobei man diese problemlos überspringen kann, also eine ganz flache, einfache Stufung erreichen kann.

Die Ansicht der Maske ist nahezu auf allen Ebenen gleich, nur auf der obersten Ebene – dem Vertrag – ist eine zusätzliche Suchfunktion sichtbar. Damit können Sie zum einen Verträge sehr schnell ansteuern - sobald sie mehr als 50 Verträge haben ist die Suche in der Tabelle ggf. etwas mühselig. Zum anderen können Sie nach jeder Ortsbeschreibung einer TGM-Ebene sehr schnell ansteuern.

[Bild]

Sobald Sie die Vertragsebene verlassen haben, wird an Stelle der Suchfunktionen die Hierarchiestufe angezeigt und Sie können durch Betätigung der Knöpfe sehr schnell auf eine höhere Stufe springen.

[Bild]

Erfassen Vertrag, Objekt, Komplex, Wartungseinheit

Wir haben die Erfassung all dieser Daten in der gleichen Maske programmiert, da überwiegend auf jeder Ebene die gleichen Informationen erfassbar sind und die gleichen Möglichkeiten bestehen.

Allerdings gibt es kleine Unterschiede. Die Vertragsnummer und das Datum ist nur auf der Vertragsebene zu erfassen, wird aber auf allen anderen Ebenen dennoch angezeigt.

Der zweite Unterschied ist ein Ankreuzfeld ‚Anlagen direkt bearbeiten’, das natürlich auf der Ebene der Anlagen nicht mehr wählbar ist.

Für die Beschreibung der einzelnen Elemente haben wir die Anlagenebene gewählt.

[Bild]

1 Anwahlknöpfe: Durch Betätigen eines dieser Knöpfe gelangen Sie sofort auf die entsprechende Ebene. Sobald Sie auf den Vertragsknopf drücken, gelangen Sie auf die oberste Ebene.

2 Tabelle: Je nach Strukturebene werden in dieser Tabelle alle Verträge, alle Objekte usw. gezeigt. Ein Doppelklick auf eine Zeile öffnet diese Bereich, genauso als wenn Sie den Bearbeiten-Knopf betätigt hätten.

3 Reihenfolge: Durch eine Eingabe in diesem Feld können Sie die Anzeigenreihenfolge in der Tabelle festlegen. Auch im Nachhinein kann man damit die Position verschieben.

4 Nummer: Geben Sie hier die Nummer ein, unter der Sie das Element künftig führen möchten. Es wird immer die Zahl vorgeschlagen, die als nächstes an der Reihe ist. Sie können sie zwar ändern, aber an sich gibt es keinen Grund dafür. Es sind nur Zahlen von 1 bis 9999 zulässig.

5 Bezeichnung: Geben Sie hier den Text ein, unter dem Sie dieses Element wiedererkennen können.

6 Original-Vertragsnummer: Falls der Wartungsvertrag bereits besteht und mit einer x-beliebigen Nummer abgeschlossen worden ist, so können Sie diese Nummer hier eintragen. Sie hat jedoch keinerlei Einfluss auf den Programmablauf. Die einzelnen Wartungselemente werden immer über die Vertragsnummer (Feld Nr. 1) definiert. Eine Eingabe ist nur dann möglich, wenn Sie sich auf der Vertragsebene befinden.

7 Vertragsbeginn: Hier können Sie einsetzen, wann Sie diesen Vertrag abgeschlossen haben. Eine Eingabe ist nur dann möglich, wenn Sie sich auf der Vertragsebene befinden.

8 Projekt: Alle Dokumente, die für diesen Vertrag entstehen, müssen in einem Labelwin-Projektordner hinterlegt werden. Hier können Sie die Nummer des Projektordner eingeben oder durch Betätigen des Knopfes Projekt aus der Liste auswählen. Ggf. müssen Sie über das Modul Projektverwaltung zuvor einen neuen Projektordner anlegen.

Alle automatisch erzeugten Dokumente wie Rechnungen, Materiallisten und Wartungsaufträge werden in diesem Projekt abgelegt.

Auch wenn Sie andere Dokumente später in einem anderen Projekt ablegen, so schadet das nicht. Über den Menüpunkt ‚Dokumentliste’ sehen Sie alle Dokumente aufgrund der zugeordneten Ebenennummer.

Eine Eingabe ist nur dann möglich, wenn Sie sich auf der Vertragsebene befinden.

Projekt-Knopf: Durch Betätigen dieses Knopfes gelangen Sie in die Projektsuche und können das gesuchte Projekt auswählen. Der Knopf nur auf der Vertragsebene sichtbar.

9 Status: Ein gespeicherter Wartungsvertrag kann drei Status einnehmen: 1. Wartung, 2. Angebot, 3. gekündigt. Natürlich könnte man bei dem Status ‚gekündigt’ gegebenenfalls auch den Vertrag löschen, aber sinnvoller ist es, ihn einfach weiter bestehen zu lassen, damit bei einer eventuellen Neuaufnahme alle Daten noch gespeichert sind. Bei dem Status ‚Angebot’ geht es darum, dass eine Wartung mit allen Details erfasst worden ist und sich im Moment in der Angebotsphase befindet.

10 Einbaudatum: Dieses Feld erscheint beim Vertrag etwas komisch, aber es wir aus den unteren Elementen hochgereicht und stellt hier eigentlich das Herstellungsdatum des Vertragsobjektes dar.

11 Bemerkung: In diesem Feld können Sie bis zu 32.000 Buchstaben als Bemerkung zu dem Wartungsvertrag hinterlegen. Beachten Sie jedoch, dass Sie nach den Eintragungen in diesem Bemerkungsfeld nicht gezielt suchen können – sie dienen wirklich nur der Information. Eine Ausgabe auf einem entsprechenden Formular ist selbstverständlich möglich.

12 Standort: Nur auf der Anlagenebene ist dieses Feld sichtbar. Sie können dort ggf. eine Ortsbeschreibung der Anlage eintragen.

[Bild]

12a Anlagen direkt bearbeiten: Wenn Sie sich nicht auf der Anlagenebene befinden, ist dieses Feld sichtbar. Durch einen Haken legen Sie fest, dass die folgenden Strukturebenen übersprungen werden und im nächsten Schritt sofort die Anlagen erfasst werden können. Das Feld ist ausgeblendet, wenn bereits Elemente unter der gerade aktiven Ebene erfasst worden sind

13 funktionales Hauptelement: Bitte lesen Sie hierzu im Kapitel Funktionale Verbindung nach. Es geht darum, ob der Vertrag für die unteren Ebenen als Zuordnungselement in einer Auswahlliste angeboten werden soll.

14 Zusatzfelder: Diese Felder können vom Anwender selber beschriftet und aktiviert werden. Dabei kann es sich sowohl um Eingabefelder, als auch um Auswahlboxen handeln. Die Einrichtung erfolgt im Modul Einstellungen unter den Menüpunkten ‚Programmbereiche, Anlagen,TGM, TGM-Zusatzfelder’. Es sind bis zu 10 solcher Felder selbst zu definieren. Der Inhalt wird auf die nächste Ebene vererbt, kann jedoch dort jeweils verändert werden.

15 Neu-Knopf: Durch Betätigen dieses Knopfes können Sie einen neuen Wartungsvertrag anlegen.

16 Speichern-Knopf: Durch Betätigen dieses Knopfes speichern Sie Ihre getroffenen Eingaben ab.

17 Bearbeiten-Knopf: Durch Betätigen dieses Knopfes gelangen Sie zur nächsten Eingabeebene. Sollten Sie jedoch auf der ersten Karteikarte das Häkchen bei ‚Anlagen direkt bearbeiten’ gesetzt haben, so gelangen Sie sofort zur Anlagenerfassung.

18 Ende-Knopf: Durch Betätigen dieses Knopfes wird das Modul geschlossen.

[Bild]

19 Toolbar: Durch Betätigen eines dieser kleinen Knöpfe können Sie Funktionen erreichen, die über das Menü ebenfalls anwählbar sind. Sobald Sie den Mauszeiger einen kleinen Moment auf einen dieser Knöpfe stellen, erhalten Sie einen Hinweis auf die Funktion des Knopfes.

1 Neues Element. Je nach aktiver Ebene ein neuer Vertrag, Objekt, Komplex ...

2 Speichern der aktuellen Eingaben

3 Druckausgabe der aktiven Ebene, ggf. mit allen untergeordneten Daten

4 Dokumentenliste, zeigt alle Dokumente dieser und ggf. auch der untergeordneten Ebene.

5 Nachkalkulation

6 Neuen Historieneintrag vornehmen

7 Historie zeigen

8 Scannerhistorie zeigen (Siehe separates Kapitel Historie)

9 Neuen Kundendienstauftrag anlegen

Karteiseite Adressen:

[Bild]

1 Suchwort: Geben Sie hier den Suchenamen der gewünschten Adresse ein. Selbstverständlich können Sie hier wieder mit dem vorangestellten @-Zeichen über beliebige Adressbestandteile suchen. Mit der Enter-Taste können Sie die Suche auslösen.

2 Suchen-Knopf: Statt beim Suchwort mit Enter zu bestätigen, können Sie auch diesen Knopf betätigen, um die Adresssuche auszulösen.

3 Adressknopf: Mit diesem Knopf gelangen Sie in das Adressprogramm. Falls Sie diese Maske aus dem Adressprogramm angesteuert haben, ist der Knopf nicht sichtbar (man kann aus dem Adressmodul halt nicht das Adressmodul starten)

4 Zugeordnete Adressen: Mit diesem Knopf werden Ihnen alle mit der Adresse verknüpften Adressen gezeigt. Die Beschreibung lesen Sie bitte bei dem Adressmodul nach.

5 Adresse: Hier wird die gefundene Adresse angezeigt.

6 Telefonliste: Sämtlich in der Adresse hinterlegten Telefonnummern werden in dieser Auswahl zum Wählen angeboten.

7 Wählknopf: Wenn bei Ihnen die Wählhilfe installiert ist und Ihr Telefon mit dem Rechner verbunden ist, können Sie mit diesem Knopf die in der Auswahlliste (Nr. 6) sichtbare Telefonnummer wählen.

Karteiseite Zeiten und Intervalle:

[Bild]

Bei der Anlage des Vertrages legen Sie hier lediglich die Wartungsperiode und den Termin der nächsten Wartung oder Inspektion fest. Die eingebbaren Zeiten werden später von den eigentlichen Anlageteilen her gefüllt, so dass hier eine Vorabeingabe keinen Sinn ergibt.

Karteiseite Funktionale Verbeindung:

Da es sich hier um ein wichtiges Element des Programmes handelt, dass sich auf jeder Ebene wiederholt, finden Sie die Beschreibung im separaten Kapitel Funktionale Verbindung

|

|

Bearbeiten

|

|

Neu

Genau wie bei der Betätigung des Neu-Knopfes können Sie über diesen Menüpunkt einen neuen Vertrag anlegen.

|

|

Speichern

Genau wie beim Speichern-Knopf können Sie hiermit Ihre getroffenen Eingaben abspeichern.

|

|

Löschen

Mit diesem Menüpunkt werden nach einer entsprechenden Warnung die angezeigten Daten und alle Unterelemente bis hin zu den Anlagen und dort hinterlegten Materiallisten gelöscht. Im Modul ‚Einstellungen’ können Sie unter den Menüpunkten ‚Option, Benutzerrechte’ die Löschmöglichkeit für einzelne Mitarbeiter verhindern.

|

|

Vorlage kopieren

Mit diesem Menüpunkt können Sie unmittelbar nach der Anlage eines neuen Elementes die Daten eines anderen Elementes als Vorlage aufrufen. Dabei werden sämtliche Unterelemente mit kopiert. Bitte beachten Sie, dass nur Kopien von der gleichen Strukturebene möglich sind. Mit dieser Funktion können gleiche Bereiche eines Gebäudes sehr schnell angelegt werden.

|

|

Drucken

Mit diesem Menüpunkt werden die Daten der aktiven Ebene gedruckt. Je nach Formular werden gegebenenfalls alle Unterelemente mit den auszuführenden Tätigkeiten ausgedruckt werden. Was tatsächlich auf dem Papier zu sehen ist, hängt letztlich nur von dem erstellten Druckformular ab.

|

|

Dokumentenliste

Hier werden alle mit dem aktiven Element in Verbindung stehenden Dokumente in einer Liste angezeigt. Standardmäßig werden auch jene Dokumente angezeigt, die zu einer der Unterebenen erfasst worden sind. Über ein Ankreuzfeld können Sie aber die Liste auf jene der aktiven Ebene eingrenzen. Über eine weitere Eingrenzung kann die Liste auch auf Fotos, Rechnungen, usw. beschränkt werden.

|

|

Neues Dokument

Mit diesem Menüpunkt können Sie ein neues Dokument anlegen, dass damit automatisch dem aktiven Element zugeordnet ist.

|

|

Neuer KD-Auftrag

Mit diesem Menüpunkt können Sie einen neuen Auftrag anlegen, der damit automatisch dem aktiven Element zugeordnet ist.

|

|

Rechnungsbeträge

Bei der Anwahl dieses Menüpunktes erscheint eine neue Maske, in der Sie die Rechnungsintervalle und Rechnungssummen festlegen können. Lesen Sie hierzu bitte im separaten Kapitel Rechnungen selektieren.

|

|

Liste Wartungsmaterialien erzeugen

[Bild]

Mit diesem Punkt können die Wartungsmaterialien aller zur aktiven Ebene gehörenden Anlagenteile ausgegeben werden. Statt sofort in die Druckausgabe zu starten, gelangen Sie in die Maske der Dokumentbearbeitung und können von dort aus drucken. Bei jedem Wechsel der Anlage und des Anlagenteiles können sogenannte Textartikel eingefügt werden, die den Einbauort beschreiben. An dieser Stelle ist aber das Problem, dass bei den Mengen nicht die Wartungsintervalle berücksichtigt werden, sondern einfach die hinterlegten Artikel der Anlagenteile genommen werden. Wenn Sie die Listen unter dem Menüpunkt ‚Selektieren, Wartungsaufträge’ erzeugen, wird die Eingrenzung der Termine berücksichtigt.

|

|

Ersatzteilliste erzeugen

Mit dem Unterschied, dass hier die hinterlegten Ersatzteile ausgegeben werden, gilt hier exakt die gleiche Beschreibung wie bei dem vorigen Punkt ‚Liste Wartungsmaterialien erzeugen’.

|

|

Nachkalkulation

Bitte lesen Sie im Kapitel Nachkalkulation

|

|

Historie

Hier handelt es sich um die Erfassung und Ausgabe von Beschreibungen zu einzelnen Elementen. Da sich diese Historie auf allen Masken zur Erfassung von Objekten, Komplexen, Wartungseinheiten usw. findet, haben wir die Beschreibung im Kapitel Historie abgelegt.

|

|

Neuer Eintrag F8

.Siehe Kapitel Historie.

|

|

Anzeigen F9

. Siehe Kapitel Historie.

|

|

ELO-Dokumente zu dieser Ebene

Unter der Voraussetzung, das Sie die Archivierung mit ELO installiert haben, können Sie hier alle zu der aktivenen Ebene vorhandenen Dokumente anzeigen.

|

|

ELO-Dokumente zu allen Unterebenen

Wie vor, jedoch werden zusätzlich die ELO-Dokumente der Unterelemente gezeigt.

|

|

Scanner-Historie

. Wenn Sie die Anlagenteile mit einem RFID-Chip oder einem Strichcode versehen, können Sie jeweils bei der Wartung diesen Code einscannen lassen. Damit wird der Beweis geführt, dass der Techniker zumindestens bei der Anlage war. Wenn der Teile der Anlage zur Wartung demontiert werden müssen, ist es sinnvoll den Chip oder Strichcode innen unterzubringen.

|

|

Selektieren

|

|

Wartungsaufträge und Materiallisten

Durch Anwahl dieses Menüpunktes werden die eigentlichen Wartungsaufträge erzeugt oder Materiallisten zur Bestellung ermittelt. Die ausführliche Beschreibung lesen Sie im Kapitel Wartungsaufträge / Inspektionsaufträge erzeugen

|

|

Inspektionsaufträge

Durch Anwahl dieses Menüpunktes können Sie für alle fälligen Inspektionen Kundendienstaufträge generieren. Die ausführliche Beschreibung lesen Sie im Kapitel Wartungsaufträge / Inspektionsaufträge erzeugen

|

|

Selektieren, Rechnungen

Durch Anwahl dieses Menüpunktes können Sie alle fälligen Rechnungen generieren lassen. Die ausführliche Beschreibung lesen Sie im Kapitel Rechnungen selektieren

|

|

Optionen

|

|

Qualifikation umsetzen

[Bild]

Jede einzelne Leistung / Tätigkeit kann mit einer Qualifikation gekennzeichnet werden. Bei der Erzeugung der Kundendienstaufträge ist es dann möglich, nur die Arbeiten einer bestimmten Qualifikation in den Auftrag aufzunehmen.

Um eventuelle Erfassungsfehler einfach korrigieren zu können, kann mit diesem Menüpunkt die Qualifikation aller Unterelemente umgesetzt werden.

|

|

Index neu aufbauen

Dieser Punkt wird nur dann benötigt, wenn durch Erweiterungen der Suchfunktion neue Felder in die Suche aufgenommen werden sollen. Da dies in der Vergangenheit bereits 2 Mal der Fall war, gibt es diesen Punkt an der Oberfläche. Eine überflüssige Anwahl schadet nicht, aber der Vorgang darf nicht abgebrochen werden.
