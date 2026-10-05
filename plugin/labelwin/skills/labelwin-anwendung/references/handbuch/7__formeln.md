# 7. Formeln

Pfad: Auswertungen / Controlling > Controlling [Modul] > Controlling / Chefknopf > Abfragen erstellen > 7. Formeln
Quelle: handbuch/7__formeln.htm

|

7. Formeln

Was wir hier als Formel bezeichnen, liefert immer nur ein Ergebnis, im Gegensatz zu den Abfragen, die eine Liste oder eine Tabelle liefern.

Eine Formel kann in einem Ausdruck (=Report) ausgedruckt werden oder einen Eintrag in einer Exceltabelle vornehmen.

Formeln werden in der Regel zusätzlich zu der eigentlichen Abfrage in der Erfassmaske von Labelwin eingetragen, Es gibt aber auch eine Möglichkeit sogenannte Grundabfragen einfach in die Exceltabelle einzutragen. Sobald Labelwin ein Tabellenblatt ‚Grunddaten’ vorfindet, wird dieses automatisch nach den Namen von Grundabfragen durchsucht und ggf. gefüllt. So braucht die Nutzung der Abfrage nicht erst im Labelwin angemeldet zu werden. Näheres dazu im nächsten Kapitel.

Die Erstellung von Formeln erfolgt durch Betätigung des Knopfes ‚Formel’ in der Maske der Abfragenerstellung.

1) Formeln in Ausdrucken: Um einen einzelnen Wert in einen Report zu bekommen, kann im Formularprogramm Crystal-Report eine Formel eingesetzt werden. Als Beispiel nehmen wir mal eine Formel mit dem Namen ‚Umsatz’. Erstellen Sie nun eine Abfrage mit dem Namen ‚Umsatz’, die als Ergebnis nur die Umsatzsumme liefert, so wird der Wert von Labelwin ausgerechnet und quasi in den Report reingereicht.

2) Formeln in Exceldateien:

Hier gibt es 2 Möglichkeiten:

a) Um Formelergebnisse an Excel weiterzugeben müssen Sie den Namen der Formel nur in die erste Spalte eines Excelblattes eintragen. Bei der Ausführung ermittelt Labelwin das Ergebnis der Formel und durchsucht die erste Spalte des Blattes nach dem Formelnamen. Wenn er gefunden wird, so wird der Wert / das Ergebnis in die zweite Spalte der gleichen Zeile eingetragen. Um diesen Eintrag an anderer Stelle der Exceldatei nutzen zu können (in einer ‚schönen’ Zusammenstellung), muss lediglich ein Verweis auf dieses Feld gezogen werden.

b) Wie bereits oben erwähnt, gibt es die Möglichkeit Grundabfragen ohne besondere ‚Anmeldung’ in einer Exceltabelle namens ‚Grunddaten’ unterzubringen. Auch hier wird der Name der Abfrage in die erste Spalte geschrieben und der Wert / das Ergebnis wird in die zweite Spalte der gleichen Zeile eingetragen

Erstellung von Formeln:

Betätigen Sie in der Maske der Abfragenerstellung den Knopf ’Formel’

Es gibt 3 Arten von Formeln, wobei sicherlich die mit den Abfragen am interessantesten ist. Weil es schnell abgehandelt ist zunächst die Erklärung für den freien Text und die Fragen

1) Der freie Text dient nur dazu, Texte in Reports rein zu reichen, bei denen keine Nachfrage erfolgen soll. Wenn Sie z.B. in einem mehrfach verwendeten Report immer eine bestimmte Überschrift erscheinen soll, so wäre dies über eine Formel mit ‚freiem Text’ möglich.

2) Bei den Fragen ist die gleiche Beschreibung wie bei den Variablen in den Abfragen zutreffend. Werte werden unmittelbar vor der Ausgabe der Abfrage eingegeben und per Formel an Excel oder einen Report weitergereicht.

3) Formeln auf der Basis von Abfragen:

[Bild]

Wie schon erwähnt liefert eine Formel nur ein Ergebnis, wie z.B. einen Umsatz, eine Kostensumme, Lohnkosten oder was auch immer. Die Abfrage, die einer solchen Berechnung zugrunde liegt, können Sie selbst erfassen oder auf eine von uns mitgelieferte ‚Grundabfrage’ zugreifen. Die Liste der mitgelieferten Grundabfragen wird im Laufe der Zeit immer umfangreicher werden und beim Update automatisch in Ihr System übertragen. Die von uns mitgelieferten Grundabfragen können von Ihnen nicht verändert werden, aber Sie können eigene Grundabfragen hinzufügen.

Ob Sie auf eine selbst erstellte Abfrage oder eine Grundabfrage zugreifen entscheiden Sie mit dem Ankreuzfeld ‚Grundabfragen(siehe Bild).

1 Tabelle: Sobald Sie mehr als eine Formel hinterlegen, werden dies in der Tabelle angezeigt. Mit einem Klick auf einen Eintrag kann dieser geändert werden.

2 Art: Legen Sie hier fest, wie die Formel entstehen soll.

Bei ‚Abfrage’ können Sie auf eine Grundabfrage oder eine beliebige von Ihnen erfasste Bildschirmabfrage zugreifen. Achten Sie bei selbsterfassten Abfragen darauf, das sie nur ein Ergebnis liefern und dieses dem Namen ‚Ausgabe’ zugeordnet ist (.... as Ausgabe FROM ....)

Bei ‚Freier Text’ geht es nur darum, bestimmte Texte flexibel in einen Report zu bekommen.

Bei ‚Frage’ können Sie eine Eingabe definieren, die unmittelbar vor der Anwendung abgefragt wird.

3 Name: Mit dem Namen erfolgt der Zugriff über den Report oder in der Exceldatei. Er muss hier exakt so geschrieben werden, wie in der Anwendung.

4 Grundabfragen: Einige Grundabfragen werden von uns mitgeliefert, Sie können jedoch auch eigene erfassen. Wenn Sie dieses Kreuz wegschalten, können Sie auf alle Bildschirmabfragen zugreifen.

5 Abfragenname-Knopf: Mit diesem Knopf wird der Name der Abfrage als Name für die Formel verwendet. Wenn der Abfragenname aussagekräftig ist, sparen Sie sich dadurch etwas Tipparbeit. Noch einmal der Hinweis, dass Sie solche Grundabfragen nicht im Labelwin zuordnen müssen, sondern sie direkt im Excelblatt ‚Grunddaten’ verwenden können.

6 Abfragenauswahl-Liste: Wählen Sie hier die zu verwendende Abfrage.

7 Kommentar: Wenn bei einer Abfrage ein Kommentar / Eine Bemerkung eingetragen ist, wird sie hier angezeigt.

8 Neu-Knopf: Um eine neue Formel festzulegen, müssen Sie diesen Knopf betätigen. Bei der ersten Formel ist dies nicht notwendig, da wir es so vorgegeben haben.

9 Speichern-Knopf: Eine Formel muss immer über diesen Knopf gespeichert werden.

10 Löschen-Knopf: Die in der Tabelle markierte Formel wird gelöscht.

11 Okay-Knopf: Mit diesem Knopf wird die Maske geschlossen

12 Abbruch-Knopf: Mit diesem Knopf wird die Maske ohne Änderung geschlossen

Um die oben gezeigte Abfrage anzuwenden müssen Sie in der Exceldatei oder im Report exakt den Namen ‚Erlöse Kundendienst’ verwenden. Die mitgelieferte Grundabfrage ‚Erloes_kd’ liefert die Nettosumme aller Rechnungen, die sich auf einen Kundendienstauftrag beziehen und hat diesen ‚Text’:

SELECT SUM(rgausgang.netto) AS Ausgabe FROM rgausgang INNER JOIN textkopf ON rgausgang.textnr = textkopf.Textzaehler WHERE textkopf.kdauftrgnr > 0 and rgausgang.mandant=##mandant## AND ( rgausgang.rgdatum BETWEEN ##vondatum## AND ##bisdatum##)

Hinweisen möchten wir auf den Bereich ‚AS Ausgabe’. Dieser Text ist immer erforderlich, damit das Ergebnis der Abfrage auf den Formelnamen zugewiesen werden kann

Über die Anwendung wurde bereits bei der Beschreibung der Excelausgabe berichtet. Trotzdem hier noch mal die Bilder der Anwendung in Excel:
