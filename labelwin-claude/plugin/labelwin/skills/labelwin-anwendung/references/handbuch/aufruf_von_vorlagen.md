# Aufruf von Vorlagen

Pfad: Dokumentenbearbeitung > Dokumentenerstellung [3] > Aufruf von Vorlagen
Quelle: handbuch/aufruf_von_vorlagen.htm

|

Aufruf von Vorlagen

Vorlagen werden immer dann benötigt, wenn neue Dokumente auf der Basis von vorhandenen Dokumenten erstellt werden sollen. So wird z.B. für die Rechnung häufig die Auftragsbestätigung oder das Angebot kopiert, die Bestellungen aufgrund der Preisanfragen erstellt usw. Nicht zuletzt braucht man häufig Teilbereiche eines anderen Angebotes oder Musterdokumentes, in dem die benötigten Artikel enthalten sind. Vorlagen können an 2 Stellen aufgerufen werden.

· Beim Beginn eines neuen Dokuments kann ein vorhandenes Dokument (oder auch mehrere) als Vorlage gewählt werden. Der gleichzeitige Neuaufruf aus den Artikelstammdaten und die damit mögliche Neukalkulation können dort nicht erfolgen.

In der Maske ‚Dokumentenerstellung’ können unter dem Menüpunkt <Vorlagen> beliebige Dokumente eines x-beliebigen Projektes oder Musterdokumente aus der Vorlagedatenbank als Vorlage übertragen werden. Durch entsprechende ‚Schalter’ kann ein Neuaufruf aus den Stammdaten erreicht werden.

[Bild]

Bild: Vorlagenauswahl

Sie gelangen zu dieser Maske, wenn Sie in der Artikelaufruf-Maske den Menüpunkt <Vorlagen> <Standardvorlage aufrufen> oder <Vorlagen> <Dokument eines Projektes> anwählen. Bei dem Einstieg über die Standardvorlage ist der Knopf ‚Anderes Projekt’ (Nr. 5) nicht vorhanden. Je nach Einstieg greift das Programm auf die Standardvorlagen - Datenbank oder die normale Datenbank mit sämtlichen angelegten Dokumenten zu.

Die Dokumente gelangen in die Standardvorlagen - Datenbank, in dem bei der Dokumenten-erzeugung der Menüpunkt <Vorlagen> <Als Standardvorlagen speichern> angewählt wird oder sie im Modul EINSTELLUNGEN unter <Vorlagen> <Musterangebote> angelegt werden.

Bei der Wahl ‚Dokument eines Projektes’ können Sie auf sämtliche mit unserem System angelegten Dokumente zurückgreifen. Über den Knopf ‚Anderes Projekt’ (Nr. 5) kann das Projekt gewechselt werden. Beim Einstieg ist die Dokumentenliste des gerade aktiven Projektes sichtbar.

Wenn nur ein Dokument als Vorlage genommen wird, so wird dessen Kalkulationseinstellung mit kopiert. Es gilt also zunächst nicht die bei der Anlage des Dokumentes festzulegende Einstellung, sondern die im Vorlagendokument hinterlegte. Das gilt jedoch nicht, wenn gleichzeitig mehrere Dokumente als Vorlagen genommen werden. Hier greift dann die festgelegte Einstellung des neuen Dokuments.

Wenn ein oder mehrere Dokumente bei der Anlage eines neuen Dokumentes als Vorlage gewählt werden, können Textpositionen zwischen die einzelnen Dokumente eingefügt werden. Es geht in erster Linie darum, bei der Übernahme von Lieferscheinen eine Zwischenüberschrift mit der Nummer und dem Datum des Lieferscheines in die Rechnung zu bekommen.

Diese Zwischenartikel werden nur dann angelegt, wenn ein bestimmter Baustein existiert. Die Bausteine werden im Bereich der Vor- und Nachbemerkungen angelegt und der Art ‚Sonstiges’ zugeordnet, damit sie in der Vorschlagsliste der normalen Vor- und Nachmerkungen nicht erscheinen.

Die Bausteinnahme müssen in Großbuchstaben und exakt wie nachstehend beschrieben angelegt werden.

Der verwendete Zwischentext wird aufgrund der Dokumentenart des Vorlagedokumentes gefunden.

Beispiel: es gibt einen Baustein ZWISCHENARTIKEL-LIE mit dem Inhalt

Lieferschein Nr. @Txtextartnr@ vom @Txdatum@

Anlage einer Rechnung auf der Basis zweier Lieferscheine mit den Nummer 345 und 381

In der Rechnung steht dann:

Lieferschein 345 vom 15.02.2006

1 Stck ...................

3 Stck ...................

Lieferschein 381 vom 16.02.2006

2 Stck ...................

1 Stck ...................

Die Zwischenartikel müssen als Baustein mit folgenden Namen angelegt werden:

ZWISCHENARTIKEL-ANG Angebot

ZWISCHENARTIKEL-REC Rechnung Schluss-Rechnung, Abschlagsrechnung,

Teilrechnung, Sammelrechnung

ZWISCHENARTIKEL-ABG Auftragsbestätigung

ZWISCHENARTIKEL-BES Bestellung

ZWISCHENARTIKEL-LIE Lieferschein

ZWISCHENARTIKEL-OLV Ohne Preis LV

ZWISCHENARTIKEL-PLV Preis LV

ZWISCHENARTIKEL-AUF Aufmaß

ZWISCHENARTIKEL-BED Bedarfsanforderung

ZWISCHENARTIKEL-MAT Materialzettel

ZWISCHENARTIKEL-BAS Projektbasis

ZWISCHENARTIKEL-FRT Freier Text

ZWISCHENARTIKEL-LAG Lagerentnahme

ZWISCHENARTIKEL-PRA Preisanfrage

ZWISCHENARTIKEL-EIN Eingangslieferschein

Der Status der Quelldokumente kann automatisch umgesetzt werden. Hierzu ist es allerdings erforderlich, dass im Modul EINSTELLUNGEN unter dem Menüpunkt <Programmbereiche> <Dokumentenerstellung> <Dokumentenstatus umsetzen> die Logik der Umsetzung festgelegt wird.

[Bild]

1 Eingrenzung: In dieser Auswahlbox können Sie wählen, welche Dokumente in der Liste (Nr. 2) gezeigt werden sollen. Anfangs ist der Eintrag ‚Alle Dokumente’ gewählt, so dass Sie alle wählbaren Dokumente sehen. Durch Anwahl können Sie die Liste auf alle Rechnungen, alle Angebote, alle Bestellungen usw. begrenzen. Die Auswahl dient lediglich dazu, bei sehr großen Dokumentenlisten eine Einschränkung zu treffen. Kundendienstaufträge, Briefe und Notizen werden in der Liste nicht gezeigt.

[Bild]

2 Bemerkung: Wenn Sie hier etwas hinein schreiben, wird in den Bemerkungen der Dokumente gesucht und die entsprechenden Dokumente zur Auswahl angeboten. Sie können nur den Eintrag in der Bemerkung zur Eingrenzung nutzen oder aber als Ergänzung zur getroffenen Dokumentenauswahl (Nr. 1).

[Bild]

3 Dokumentenliste: In dieser Liste erscheinen alle zu dem aktiven Projekt oder der Vorlagendatenbank gehörenden Dokumente. Mit der linken Maus können Sie eines der Dokumente markieren, das dann als Vorlage verwendet werden soll. Über die Liste ‚Dokumentenart’ (Nr. 1) kann die Menge der gezeigten Dokumente eingeschränkt werden.

[Bild]

4 Dokument zeigen: Wenn Sie nicht sicher sind, ob das markierte Dokument der gesuchte ist, so können Sie durch Betätigen dieses Knopfes das Dokument sichtbar machen. In diesem Fenster erfolgt keine Übernahme, sondern lediglich die Anzeige, die mit dem OK-Knopf zu verlassen ist.

[Bild]

5 Anderes Projekt: Dieser Knopf ist nicht sichtbar, wenn Sie mit der Vorlagendatenbank arbeiten. Bei der Wahl ‚Dokument eines Projektes’ können Sie hier das Projekt umschalten. Die Projektauswahl erfolgt wie in allen anderen Bereichen, bei denen Projekte gewählt werden können. Die Beschreibung dieses Bereiches lesen Sie im Kapitel Projektsuche.

Übernahme

[Bild]

6 Vorbemerkung: Durch Aktivieren dieses Feldes wird die Vorbemerkung in das aktive Dokument übernommen. Falls das aktive Dokument bereits eine Vorbemerkung hat, erfolgt eine Abfrage, ob diese überschrieben oder um die andere Vorbemerkung erweitert werden soll.

[Bild]

7 Artikel einzeln: Wenn Sie dieses Feld aktivieren, haben Sie die Möglichkeit, aus dem ausgewählten Dokument einzelne Artikel zu übernehmen und ggf. die Menge entsprechend anzupassen.

[Bild]

8 alle Artikel ohne Stop: Wenn Sie dieses Feld aktivieren, werden alle Artikel des Vorlagedokumentes übernommen. Andernfalls erscheint ein Fenster mit den Artikeln der Vorlage und Sie können einzelne Artikel zur Übernahme anwählen.

[Bild]

9 Nachbemerkung: Durch die Aktivierung dieses Feldes erreichen Sie, dass die Nachbemerkung der Vorlage in das aktive Dokument übernommen wird. Falls das aktive Dokument bereits eine Nachbemerkung hat, kann diese überschrieben oder die neue dahinter gehängt werden.

[Bild]

10 Mengenmulti: Mit einem hier zu erfassenden Multiplikator können die übernommenen Mengen erhöhen oder vermindern. Interessant ist die Eingabe von –1, weil sich damit Gutschriften aus Rechnungen entwickeln lassen.

[Bild]

11 Setbestandteile multiplizieren: Die Entscheidung ist nur bei einem von 1 abweichendem Multi interessant. Es geht darum, ob die Set-Hauptmengen oder die Bestandteilmengen verändert werden sollen.

Daten

[Bild]

12 Artikel neu aufrufen: Standardmäßig werden die Artikel mit sämtlichen dazugehörigen Daten wie Preis, Lohnminuten, Einkaufspreis usw. aus dem Vorlagedokument kopiert. Wenn Sie ein Kreuz an dieser Stelle setzen, so versucht das Programm die Artikel aus den Stammdaten neu aufzurufen. In diesem Falle greift Ihre aktuelle Kalkulationseinstellung und verändert ggf.. auch die Verkaufspreise, Lohnminuten usw. Falls es sich um einen frei erfassten Artikel handelt, der in den Stammdaten nicht abgelegt ist, so wird dieser Artikel unverändert übernommen.

[Bild]

13 Text erhalten: Dieses Feld ist nur dann aktiv, wenn Sie in dem Feld 12 (Artikel neu aufrufen) ein Kreuz gesetzt haben. Beim Neuaufruf der Artikel können hiermit die bisher vorhandenen Artikeltexte erhalten werden. Der Sinn liegt darin, ggf. verbesserte Artikeltexte nicht aus den Stammdaten zu übernehmen, sondern aus dem Vorlagedokument.

[Bild]

14 Verkaufspreis erhalten: Bei einer Aktivierung an dieser Stelle werden die Artikel zwar neu aufgerufen mit den aktuellen Einkaufspreisen, Lohnminuten usw., jedoch der Verkaufspreis wird aus der Vorlage übernommen. Die Anwahl ist nur möglich, wenn die Artikel neu aufgerufen werden (Nr. 12)

[Bild]

15 Einkaufspreis erhalten: Durch Aktivieren dieses Feldes können Sie erreichen, dass beim Neuaufruf der Artikel nicht die aktuellen Einkaufspreise sondern die Einkaufspreise aus der Vorlage erhalten bleiben. Die Anwahl ist nur möglich, wenn die Artikel neu aufgerufen werden (Nr. 12).

[Bild]

16 Lohn erhalten: Durch die Aktivierung an dieser Stelle erreichen Sie, dass beim Neuaufruf der Artikel die Lohnsumme dennoch aus der Vorlagedatenbank genommen wird. Die Anwahl ist nur möglich, wenn die Artikel neu aufgerufen werden (Nr. 12).

[Bild]

17 Schlusstext: Wenn ein Artikel der Vorlage mit einem Schlusstext (‚Liefern und Montieren‘) versehen ist, muss hier entschieden werden, ob dieser übernommen oder der in der aktiven Kalkulationseinstellung hinterlegte Schlusstext gilt.

[Bild]

18 Alternative / Eventuale-Kennzeichen beibehalten: Hier legen Sie fest, ob Alternativen und Eventualen in ein neues Dokument übernommen werden oder nicht.

[Bild]

19 Aufmaßzeilen mit kopieren: Je nach Situation ist es interessant, die Aufmasszeilen mit zu kopieren oder nicht.

20, 21, 22 Status Quelldokumente: Der Status der Vorlage-Dokumente kann bei einer Übernahme in ein neues Dokument automatisch umgesetzt werden. Dazu muss der neue Status allerdings in Abhängigkeit von dem Ziel (Rechnung, Bestellung usw.) und der Quelle (Lieferscheine, Bedarfsanforderung) festgelegt werden. Durch die vielen Dokumentenarten im Labelwin sind natürlich sehr viele Kombinationen möglich. In der Praxis wird man die Umsetzung jedoch nur bei bestimmten Arten wie z.B. eine Rechnung mit der Vorlage von Lieferscheinen verwenden.

Hierzu werden im Modul EINSTELLUNGENl unter dem Menüpunkt <Programmbereiche> <Dokumentenerstellung> <Dokumentenstatus umsetzen> die neuen Status für die Quelldokumente festgelegt. Bei Kombinationen, für die kein neuer Status festgelegt wurde, wird der Status bei der Vorlagenübernahme nicht verändert.

Bei der Vorlagenübernahme gibt es jetzt 3 Möglichkeiten der Statusveränderung:

[Bild] beibehalten: der Status der Quelldokumente wird nicht verändert.

[Bild] umsetzen nach Tabelle: Es wird laut der Tabelle im Modul EINSTELLUNGEN der Status verändert.

[Bild] mit Auswahl: Mit diesem Status kann jetzt ausgewählt werden.

[Bild]

23 Kostenstellen: Dieses Feld ist nur dann sichtbar, wenn Sie mit Kostenstellen arbeiten (festzulegen im Programm EINSTELLUNGEN unter dem Menüpunkt <Grundeinstellungen> <Allgemein>. Die Kostenstellenauswahl ist nur dann sichtbar, wenn Sie mit Kostenstellen arbeiten und im Feld 22 den Punkt ‚auswählen‘ eingestellt haben.

[Bild]

24 OK Dokument nehmen: Durch Betätigen dieses Knopfes wird das markierte Dokument aufgrund der von Ihnen getroffenen Optionen übernommen. Wenn Sie ‚alle Artikel ohne Stop’ (Nr. 11) angewählt haben, so werden sofort automatisch alle Artikel übernommen. Wenn dies nicht der Fall ist, so erscheint auf Ihrem Schirm ein zweites Dokumentenfenster mit den Artikeln des gewählten Vorlagedokumentes. In dieser Liste können Sie die gewünschten Artikel markieren und mit dem OK-Knopf übernehmen (markieren und Doppelklick hat die gleiche Wirkung). Bei der Einzelübernahme können Sie in dem zu erstellenden Dokument die Position ändern, in dem Sie auf das Fenster mit dem bereits erstellten Dokument klicken und einen anderen Artikel anfahren. Die Übernahmeartikel werden stets vor dem markierten Artikel übernommen.

[Bild]

25 Abbruch: Durch Betätigen dieses Knopfes brechen Sie die Übernahme einer Vorlage ab.-
