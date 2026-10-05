# Aufruf von Sets

Pfad: Dokumentenbearbeitung > Dokumentenerstellung [3] > Arbeiten mit Sets > Aufruf von Sets
Quelle: handbuch/aufruf_von_sets.htm

|

Aufruf von Sets

Abgespeicherte Sets werden genauso wie alle anderen Artikel aufgerufen. Sollten bei dem Set feste Bestandteile hinterlegt sein, so werden diese automatisch übernommen. Sie können im Nachhinein in dem Set ohne weiteres Positionen austauschen, löschen, einfügen. Die Setsumme wird automatisch beim Verlassen der Dokumentenerstellungsmaske neu gerechnet. Wenn Sie die Setsumme vorher bereits sehen wollen, so können Sie dies über den Menüpunkt <Bearbeiten> <Summen neu rechnen> oder durch Betätigen des kleinen Taschenrechner-Knopfes. Bei der Positionsnummervergabe bekommen Sets grundsätzlich eine Unternummer die zwischen Klammern gesetzt wird. Die Unternummer wird in der Regel nicht mit ausgedruckt, so dass sie im Angebot oder der Rechnung für den Endkunden nicht sichtbar ist. Ohnehin können ja je nach gewählter Setart die Unterartikel gänzlich auf dem Papier fehlen.

Man kann beim Anlegen eines Sets im Katalog auch eine Zeitantragung vornehmen. Sobald in einem Set Zeiten hinterlegt sind, werden beim Aufruf die Bestandteile ohne Zeit übernommen und als letzte Pos. automatisch ein Artikel mit der Nummer ‚zzmontagezeit’ aufgerufen. Wenn Sie Sets per Datanorm einspielen, wird dieser Artikel im Katalog automatische angelegt, beim eigenen Katalog müssen Sie ihn manuell anlegen, wenn Sie diese Möglichkeit nutzen wollen. Der Artikel muss die Art ‚Leistungsposition’ erhalten und bei der Zeit muss 1 Minute hinterlegt sein. Der Text bleibt Ihnen überlassen, aber wir empfehlen ‚Montage’ . Als Liefereinheit empfehlen wir ein kleines x, damit Texte wie ‚1 x Montage 198,00 €’ entstehen. Solange Sie mit verborgenen Sets arbeiten, sieht den Text allerdings ohnehin niemand auf dem Papier.

Wenn Sie im Setkopf ‚mit Stop’ ankreuzen, bietet das Programm eine Auswahlliste aller Bestandteile an und Sie können über die Eingabe der Menge steuern, wie die Bestandteile übernommen werden sollen

[Bild]

[Bild]

Selbst die Mengen von Unter-Sets und Prozentartikeln lassen sich ändern.

Vorkalkulierte Sets:

In der Regel wird der Setpreis über die Preise seiner Bestandteile ermittelt. Darüber hinaus bietet das Programm die Möglichkeit das Set als vorkalkuliert zu kennzeichnen. In diesem Fall können Sie dem Set einen festen Preis geben. Auf diese Weise ist es z.B. möglich, einer Anschlussgarnitur sämtliche Bestandteile zuzuordnen und den Preis dennoch auf einen von Ihnen zu wählenden Festpreis festzusetzen. Wenn ein Set das Vorkalkulationskennzeichen hat, so werden auch bei einem Wechsel der Bestandteile die Preise nicht verändert.

Die Vorkalkulation lässt sich auch in den Artikelstammdaten festlegen.

Bei diesen Sets ist es interessant, den aktuellen Einkaufswert zu sehen. Wenn Sie in der Maske der Stammdaten auf den Knopf ‚Setsumme’ drücken, dann werden die aktuellen Einkaufswerte, Listenpreis und die den Artikeln hinterlegten Lohnminuten angezeigt. Die gleiche Anzeige erscheint automatisch, wenn Sie Setbestandteile aufgerufen oder verändert haben.

[Bild]

EK-Berechnung bei vorkalkulierten Sets

Nach vielen Diskussionen haben wir hier 2 neue Möglichkeiten geschaffen, wie sich in Ihrem Betrieb die Einkaufswerte von ‚Vorkalkulierten Sets‘ verhalten sollen.

Die Änderung kann im Modul Einstellungen unter den Menüpunkten <Programmbereiche>, <Dokumentenerstellung>, <Grundeinstellung> erfolgen. Die Auswahl ist dann unter dem Punkt ‚Allgemeine Einstellungen‘ zu finden.

[Bild]

|

Wichtig: Diese Einstellung hat große Auswirkungen auf den gerechneten Deckungsbeitrag. Bitte sprechen Sie eine Änderung unbedingt mit den Verantwortlichen Ihrer Firma und möglichst auch mit allen (Büro-)Mitarbeitern ab.

Es geht um die Frage, welche Einkaufswerte ein vorkalkuliertes Set hat. Bei einem solchen Set können Sie in der Erfassung und den Stammdaten zunächst alle Werte erfassen. Je nach Einstellung werden die Einkaufswerte aber später automatisch neu gerechnet.

1. Material-Einkauf aus Bestandteilen

Diese Methode ist (historisch gewachsen) der Standard. Der Material-Einkauf, der Fremdleistungseinkauf und 'Sonstige Kosten' der Set-Bestandteile werden aufaddiert und gelten für den Einkaufswert des ganzen Sets. Eine Deckungsbeitragsrechnung greift auf diese Werte. Die Lohnkosten und die Minuten bleiben dagegen so, wie sie bei der Anlage des Sets festgelegt wurden.

2. NICHTS aus den Bestandteilen

Alle Einkaufswerte bleiben so, wie sie bei der Anlage des Sets festgelegt wurden. Die Bestandteile dienen also sinngemäß nur als Stückliste für die Bestellung, für einen Materialauszug usw. Eine Änderung von Mengen oder Preise der Setbestandteile hat keine Auswirkungen auf den Set-Einkauswert.

3. Alle Kosten aus den Bestandteilen

Hier werden alle Einkaufswerte aus den Set-Bestandteilen gezogen. Jede Änderung bei einem Set-Bestandteil hat Auswirkungen auf die Set-Kosten. Im Prinzip können Sie sich also bei der Setanlage die Erfassung der Kosten sparen, denn sie werden auf jeden Fall immer wieder neu berechnet.

Ausgabe der Setbestandteile auf Papier:

Auch bei den Sets, bei denen der Kunde die Bestandteile nicht sehen soll, besteht Bedarf an einer Auflistung. Diese Auflistung wird z.B. für die Stückliste, für die Händlerpreisanfrage oder die Bestellung benötigt. Da die Menge der Setbestandteile ggf. mit der Menge der Sets multipliziert werden muss, ist es mit einer einfachen Druckausgabe nicht getan. Sie müssen in unserem Programm ein neues Dokument anlegen und das gewünschte Vorlagedokument wählen. In der Maske ‚Dokumentenerstellung’ können Sie unter dem Menüpunkt <Optionen> <Alle Set-Artikel auflösen> die ganzen Setbestandteile ausmultiplizieren lassen. Das Programm fragt nach, ob die Setüberschriften als Textartikel erscheinen sollen oder einfach entfallen. Nach der Setauflösung haben Sie ein Dokument, in dem sämtliche Setbestandteile in Ihrer tatsächlich benötigten Stückzahl aufgelöst sind. Drucken Sie dieses Dokument auf die gewünschte Art (Bestellung, Lieferschein, Preisanfrage ...) aus.

Für interne Unterlagen können Bestandteile von verborgenen Sets ausgedruckt werden. Dazu gibt es in der Druckmasken unten links ein Ankreuzfeld. Dieses kann zum Beispiel sinnvoll sein, wenn der Chef sich das Angebot anschauen möchte, bevor der endgültige Druck an den Kunden geht.

[Bild]

Des Weiteren ist es ebenso möglich, dass man in der Druckausgabe wählen kann, dass die Setbestandteile mit Einzelpreisen gedruckt werden. Die Ausgabe erfolgt auf dem normalen Rechnungs- oder Angebotsformular. Hierbei werden die Setbestandteile nicht wie sonst eingerückt, sondern stehen in dem gleichen Bereich wie ‚normale’ Artikel. Ausgedruckt wird nur der Einzelpreis. Damit soll verhindert werden, dass beim Summieren der rechten Spalte die Preise der Set-Bestandteile mitgezählt werden, da die Gesamtpreise im Setkopf stehen.

Schachtelung von Sets:

Sets können in bis zu 5 Ebenen miteinander verschachtelt werden. Ein Set kann also einen Set als Bestandteil enthalten, der wiederum Sets enthält. Dabei können die verschiedenen Setarten beliebig verwendet werden. Die Druckausgabe auf dem Papier endet an der Stelle, an der in der Hierarchie das erste Mal ein Set mit Verborgen-Bestandteilen gewählt worden ist.

Nachträgliches Einfügen von Sets:

Wenn Sie nachträglich bereits im Dokument vorhandene Artikel in einen Set überführen möchten, gehen Sie folgendermaßen vor:

- Fügen Sie zunächst einen leeren Set ein. Es erscheinen ein Set-Anfang-Artikel und direkt dahinter ein Set-Ende-Artikel.

- Markieren Sie nun die Artikel, die Sie in den Set überführen möchten.

- Schneiden Sie die Artikel aus.

Markieren Sie den Set-Ende-Artikel und fügen sie die Artikel wieder ein.

|

Hinweise zur Benutzung der Tabelle (nach Windows-Regeln):

Markieren von Artikeln in der Tabelle:

Um einen einzelnen Artikel zu markieren, klicken Sie mit der Maus auf das graue Kästchen am Anfang der Tabellenzeile. Wenn Sie zusätzlich weitere Artikel markieren möchten, halten Sie die STRG-Taste gedrückt und markieren Sie weitere Artikel. Mit der SHIFT-Taste können Sie Artikel blockweise markieren. Markierte Artikel sind blau hinterlegt.

Ausschneiden von markierten Artikeln:

Wenn Sie die markierten Artikel ausschneiden möchten, können Sie entweder in dem Popup-Menü (rechte Maustaste) ‚Ausschneiden‘ wählen oder den Menüpunkt <Bearbeiten> <Ausschneiden> benutzen oder einfach die Tastenkombination STRG+X benutzen. Dadurch werden die Artikel in die Zwischenablage verschoben.

Einfügen von Artikel aus der Zwischenablage:

Wenn Sie Artikel aus der Zwischenablage einfügen möchten, können Sie entweder in dem Popup-Menü (rechte Maustaste) ‚Einfügen‘ wählen oder den Menüpunkt <Bearbeiten> <Einfügen> benutzen oder einfach die Tastenkombination STRG+V benutzen.

Auf ähnliche Weise können Sie auch ein Set in den Stammdaten anlegen. Dazu müssen Sie die Artikel markieren und kopieren. (Strg + C). Legen Sie dann wie gewohnt das Set in den Stammdaten an und betätigen Sie dann den Knopf ‚Set-Bestandteile. Damit gelangen Sie in die Maske, in der Sie die Artikel für den Set-Inhalt aufrufen. Gehen Sie jetzt auf den Menüpunkt <Bearbeiten> <Übernahme aus Zwischenablage>. Die zuvor kopierten Artikel werden übernommen. Die einzige Einschränkung ist, dass Sie über diesen Weg kein Set im Set aufrufen können. Titelüberschriften, %-Zuschläge usw. sind möglich. Theoretisch könnten Sie also ein ganzes Angebot als Set hinterlegen.

Die Methode mit den Sets hat gegenüber einer Speicherung als Vorlage den Vorteil, dass bei der Verwendung die Artikel immer neu aufgerufen und mit den aktuellen Preisen kalkuliert werden.

Prüfung von Sets

Nach der Anlage oder nach der Einspielung von Händlerdaten empfiehlt sich die Prüfung von allen Sets und Serienartikel, ob ihre Bestandteil-Artikel (noch) existieren

Um das zu prüfen wählen Sie im Programm KATALOGE nach der Aktivierung des Kataloges, der die Serienartikel enthält, die Menüpunkte <Bearbeiten> <Set bearbeiten/prüfen> <Set, Bestandteile prüfen> an. Dabei werden alle Bestandteile aller Sets daraufhin geprüft, ob sie in dem entsprechenden Katalog existieren. Bei der Anwahl können Sie entscheiden, ob Sie in der Fehlerliste den Setnamen ausgewiesen haben wollen oder nicht. Bei der Ausweisung der Set-Namen kann ein Artikel mehrfach aufgelistet werden, wenn er in mehreren Sets enthalten ist.

[Bild]

Sollte ein Artikel vom Großhändler gelöscht worden sein, können Sie unter den Menüpunkten <Bearbeiten> <Set bearbeiten/prüfen> <Set, Bestandteile tauschen> diese Artikel gegen einen anderen austauschen. Der betreffende Artikel wird in allen Sets automatisch getauscht.

[Bild]

Bei ‚Neue Nr.’ muss natürlich eine Artikelnummer eingetragen worden. Mit der Eingabe oben im Bild möchten wir nur zeigen, dass Sie die Nummer auch über die üblichen Suchmethoden heraus gesucht werden.
