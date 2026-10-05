# 2.3 Stammdaten Datanorm und Datpreis

Pfad: Artikelstammdaten > Katalog [10] > 2. Einlesen Datanorm > 2.3 Stammdaten Datanorm und Datpreis
Quelle: handbuch/2_3_stammdaten_datanorm_und_datpreis.htm

|

2.3 Stammdaten Datanorm und Datpreis

Sie gelangen in diese Maske durch Anwahl des Menüpunkts [Einlesen - Stammdaten Datanorm und Datpreis].

In diesem Bereich können Datanorm Dateien mit Artikeldaten und Preisen, die Sie online abgeholt oder per CD erhalten haben, eingespielt werden. Das Programm erkennt automatisch, um welche Datanorm-Version es sich handelt und verhält sich dementsprechend.

Falls Sie gleichzeitig DATANORM- und DATPREIS einspielen, achten Sie unbedingt auf die richtige Reihenfolge. In der Regel müssen zunächst die Datanorm- und dann die Datpreis-Datei eingespielt werden. Oberste Priorität hat selbstverständlich immer das Datum der Datei. Wenn Datensätze mit Löschartikeln vorhanden sind (sogenannte X-Datensätze), so empfiehlt es sich, diese als erstes einzuspielen. Leider ist die vom Großhändler vorgegebene Einspielreihenfolge manchmal verkehrt. Auf der sicheren Seite sind Sie, wenn Sie vor Einspielen der Daten eine Datensicherung vornehmen. In diesem Falle können Sie bei einem Fehler relativ einfach den vorherigen Stand wieder herstellen.

|

Hinweis: In manchen Netzwerken gibt es Probleme, wenn die Datanormdateien direkt auf die Netzwerkplatte einfließen. Darüber hinaus lässt sich das Tempo wesentlich beschleunigen, wenn die Einspielung auf der lokalen Festplatte (also C:) erfolgt. Je nach Netzwerkgeschwindigkeit kann die Temposteigerung bis zu 3-fach sein. Der Katalog kann daher menügesteuert auf die lokale Festplatte eingespielt werden.

Dieser Vorgang hat den zusätzlichen Vorteil, dass die anderen Nutzer im Netzwerk während der Einspielung noch mit dem alten Katalog arbeiten können. Allerdings dürfen sie keine Änderungen vornehmen, da diese nach Zurückkopieren des Kataloges verloren wären. Bitte lesen Sie unbedingt das Kapitel Katalog - Auslagern / Einlagern.

Wenn der Katalog auf die lokale Festplatte kopiert worden ist, lassen sich dort nicht nur Datanorm und Datpreis-Dateien einspielen, sondern ebenfalls Preisänderungsläufe und dergleichen durchführen. Alle diese Vorgänge laufen ggf. lokal wesentlich schneller ab, als dies im Netzwerk möglich ist. Einige Menüpunkte sind bei ausgelagertem Katalog blockiert, weil Sie das Vorhandensein aller Kataloge im gleichen Verzeichnis bedingen. So ist z.B. der Menüpunkt ´Stammdaten Eintragen ändern´ nicht erreichbar, da bei der Set-Erstellung auf Artikel anderer Kataloge zurückgegriffen werden müsste.

Nach Einspielung der Datanorm/Datpreis-Dateien muss der Katalog wieder auf das Netzwerk zurückkopiert werden. Der Kopiervorgang ist nicht möglich, wenn ein anderer Benutzer den Katalog zurzeit geöffnet hat. In diesem Fall erfolgt eine entsprechende Meldung und Sie müssen den Katalog später per Hand zurückkopieren. Dies geschieht durch Anwahl des Menüpunkts <Katalog> <Einlagern>.

Sollte eine Dateieinspielung aus irgendeinem Grund einmal komplett schief gegangen sein, so ist es möglich den vorherigen Katalogstand zu behalten und nur das Kennzeichen der Auslagerung wegzusetzen. Dies geschieht unter dem Menüpunkt <Katalog> <Auslagerung löschen>. Das Programm löscht dabei auch den ausgelagerten Katalog auf der Platte C. Sollte dieses nicht möglich sein, weil er auf einem anderen Rechner ausgelagert wurde, so bleibt dort eine „Dateileiche“ zurück.

TUTORIAL VIDEO: Artikelkatalog einspielen

https://www.youtube.com/watch?v=EMahQSev9F4

Datanorm einspielen

Die entscheidenden Einstellungen zum Einlesen von Datanorm Dateien befinden sich auf der Seite "Datanorm einspielen". Aus diesem Grund öffnet sich auch immer diese Seite beim Aufruf des Menüpunktes <Einlesen> <Stammdaten Datanorm und Datpreis>. Alle weiteren Einlese-Parameter sind auf den anderen Seiten untergebracht (die Beschreibung folgt weiter unten) und müssen im Regelfall nicht angefasst werden.

|

[Bild]

Bild: Datanorm einspielen

5 Katalog lokal einspielen: Im Netzwerk ist es immer sinnvoll, den Katalog lokal einzuspielen. Zum einen geht die Einspielung auf der lokalen Festplatte wesentlich schneller, zum anderen können alle anderen Benutzer im Netzwerk mit den bisherigen Katalogdaten weiterarbeiten. Nach dem Einspielen muss der Katalog unbedingt ins Netzwerk zurück kopiert werden. Dies geschieht unter dem Menüpunkt <Katalog> <Einlagern -> Netz>.

|

1 Quell-Quellverzeichnis: Tragen Sie hier den Pfad der Datanormdateien ein.

2 Durchsuchen: Wenn die Händler ihre Kataloge per CD übergeben, so sind die Daten manchmal in irgendwelchen Unterverzeichnissen verborgen. Durch diesen Knopf können Sie einen den Windows-Regeln entsprechenden Pfad anwählen. Die Daten werden zwar auch gezeigt, können jedoch nicht angewählt werden. Es geht nur darum, den richtigen Pfad zu finden.

3 Ansehen: Durch Betätigen dieses Knopfes wird der in der Liste der vorhandenen Dateien markierte Eintrag mit dem Texteditor geöffnet.

4 Online-Daten holen: Über diesen Knopf haben Sie die Möglichkeit, sich die aktuellen Datanorm-Daten online abzuholen, sofern Ihr Großhändler diese online zur Verfügung stellt und in unserer Großhändler-/Herstellerauswahlliste zu finden ist. Wenn Sie Ihre Daten im Bereich <Katalog> <Katalog Grunddaten> korrekt eingetragen haben und den Knopf betätigen, erscheint folgendes Bild:

[Bild]

|

Solange ein Katalog ausgelagert ist, wird er auf dem lokalen Rechner einen grünen Hintergrund des Menübildes erzeugen. Die anderen Benutzter im Netzwerk bekommen einen roten Hintergrund als Zeichen dafür, dass der Katalog zurzeit nicht zur Verfügung steht, da er auf einem anderen Rechner in Bearbeitung ist.

6 Logbuch Kommentar: Hier haben Sie die Möglichkeit, sich das Logbuch anzuschauen und ggf. durch einen Kommentar zu ergänzen.

7 Ok: Durch Betätigen dieses Knopfes wird die Datanorm-Übergabe mit den getroffenen Einstellungen gestartet.

8 Abbruch: Durch Betätigen dieses Knopfes wird die Datanorm-Übergabe abgebrochen und Sie gelangen wieder in die Katalog-Hauptmaske.

Diverse Parameter

Legen Sie hier fest, wie die Texte übernommen werden sollen.

|

[Bild]

Bild: Diverse Parameter

|

1 nur Kurzform übernehmen: Durch ein Kreuz in diesem Feld können Sie erreichen, dass die Langform von Artikeln nicht übernommen werden. Hier handelt es sich um ein Relikt aus der Zeit teurer Festplatten. In der Regel ist es sinnvoll, die Artikel in Kurz- und Langform zu übernehmen.

2 Textänderung verhindern(gilt nur für Kurztext): Wenn Sie Artikeltexte selbst verändert haben, können Sie über ein Kreuz an dieser Stelle verhindern, dass sie verändert werden. Neue Artikel werden dennoch übertragen.

3 Löschartikel entfernen: Durch ein Kreuz in diesem Feld erreichen Sie, dass zu löschende Artikel tatsächlich entfernt werden. Wenn Sie einen Artikel als Lagerartikel angemeldet haben, so wird er dennoch nicht gelöscht.

4 Suchworte erhalten: Jeder Artikel kann neben der Artikelnummer und einem Textbestandteil über Suchworte aufgerufen werden. Die Suchworte können Sie selbst vergeben. Durch ein Kreuz in diesem Feld verhindern Sie, dass die solchermaßen vergebenen Suchbegriffe überschrieben werden.

5 Zahlen im Text mit auf den Suchindex übernehmen: Bei vielen Händlern sind Typennummern oder Original-Herstellernummern im Artikeltext vorhanden. Durch diesen Schalter können auch diese in die Stichwortliste aufgenommen werden.

6 Umlaute sind ANSI kodiert: Wenn im Text statt der Umlaute unleserliche Zeichen stehen, so kann es an einer fehlerhaften Erfassung liegen. Die Datanorm ist relativ alt und verlangt die Verschlüsselung der Umlaute nach den DOS-Regeln, statt nach der Windows-Verschlüsselung.

Mit gesetztem Schalter werden die Umlaute dann (hoffentlich) richtig dargestellt. Wenn es nichts nützt, müssen Sie sich mit dem Datenlieferanten in Verbindung setzen.

7 Dim/Langtexte ohne Umbruch: Wenn der Lieferant unsinnige Umbrüche in der Datanorm hat, z.B. immer nach 30 Zeichen eine neue Zeile beginnt, kann der Umbruch weg gefiltert werden. Damit steht der komplette Text einfach hintereinander und wird beim Drucken an der Stelle umgebrochen, wo es gerade passt. Die Langtexte müssen ab ggf. trotzdem manuell überarbeitet werden, weil auch Aufzählungen (Farbe ..., Abmessung:....) einfach hintereinander stehen.

|

8 VPEs ungleich 1 nach Anmerkung: Bei einigen Artikeln und Großhändlern ist es wichtig, dass bei einer Bestellung die Menge ein Vielfaches der Verpackungseinheit (VPE) beträgt.

Da diese bei einigen Großhändlern zwar per Datanorm ausgeliefert wird, Labelwin sie aber nirgendwo anzeigt, können Sie durch Setzen dieses Schalters dafür sorgen, dass bei einer VPE ungleich 1 diese als Text (z.B. VPE 50) in die Artikelanmerkung geschrieben wird.

Das hat den Effekt, dass bei jedem Artikelaufruf diese Info in einem Meldefenster angezeigt wird.

Diese Funktion mag zwar sinnvoll sein, kann in vielen Fällen aber auch sehr störend sein. Daher können Sie hier entscheiden, ob Sie das möchten oder nicht.

9 VPEs als VKEinheit übernehmen: Mit diesem Schalter wird die Verpackungseinheit (VPE), sofern sie in der Datanorm Datei angegeben ist, in die Verkaufseinheit (VKE) kopiert, sofern die Preiseinheit (PE) größer 1 ist. Ist der Haken nicht gesetzt, dann bleibt die VKEinheit wie gehabt.

10 fehlende Artikel löschen: Üblicherweise wird ein Katalog durch regelmäßige Aktualisierungen aktuell gehalten. Hat man diese Aktualisierungen aber nicht durchgängig gemacht oder der Händler bietet nur einen Komplettsatz an, hat man entweder die Möglichkeit (1) den Katalog komplett zu löschen und neu einzuspielen oder (2) den Artikelstamm auf den bestehenden Katalog einzulesen. Mit Hilfe dieser Option wird vermieden, dass hierbei "Artikelleichen" entstehen. Die genaue Vorgehensweise wird im Unterkapitel Fehlende Artikel löschen beschrieben.

11 Indexaufbau erst am Ende: Wenn Sie hier ein Häkchen setzen, wird der Index erst am Ende des Einlesevorgangs aufgebaut. Das führt ggf. zu einem schnelleren Einlesen der Dateien.

12 Suchwortmindestlänge: Das Programm baut für die spätere Artikelsuche eine so genannte Indexdatei auf. Dabei werden die Artikelnummer, das Suchwort und jedes Wort aus dem Artikelkurztext in eine Liste eingetragen. Bei dem späteren Artikelaufruf muss der erste Suchbegriff mit einem dieser Worte (Anfänge) identisch sein. Um die Indexdatei in Ihrer Länge ein wenig zu begrenzen, ist es sinnvoll eine Suchwortmindestlänge vorzugeben. Die Erfahrung hat gezeigt, dass eine Suchwortmindestlänge von 3 Zeichen sinnvoll ist. Auf diese Art wird verhindert, dass Worte wie in, f., DN usw. nicht in den Index hineinkommen. Um Ihnen eine Größenordnung zu geben: Eine Händlerdatei mit ca. 100.000 Artikeln baut in der Regel einen Index mit 800.000 Indexeinträgen auf. Wenn wir die Suchwortmindestlänge auf 2 heruntersetzen, so sind es häufig gleich 1.2 Millionen Indexeinträge.

Minuteneinstellungen

|

[Bild]

Bild: Minuteneinstellungen

|

1 Minuten übernehmen: Wenn mit der Datanorm-Datei Minutensätze übergeben werden, können Sie hier festlegen, wie diese übernommen werden sollen.

Minuten lassen sich ab der Datanorm-Version 4 übertragen. Im Moment werden die meisten Minutendateien im System Bürgerle übertragen. Diese werden unter dem Menüpunkt <Einlesen> <Minuten (Bürgele)> eingelesen.

Weitere Informationen zur Minutenübernahme finden Sie im Kapitel Katalog - Minuten (Bürgerle).

2 Übernahme als Fremdminuten/ eigene Minuten: Legen Sie hier das Feld fest, in das die Minuten übertragen werden sollen. In der Regel ist es das Feld ‚Fremdminuten’.

3 Faktor: Man kann beim Einspielen von Minuten an dieser Stelle einen Multiplikator auf die eingelesenen Minuten eingeben. Damit werden diese Zeiten verlängert oder - bei Werten kleiner als 1 - verkürzt.

Protokoll-Einstellung

Die Datanorm schreibt vor, dass Übertragungsfehler protokolliert werden müssen. In diesem Protokoll stehen dann alle gelöschten Artikel und auch neue Artikel, die auf bereits vorhandene Artikel überspielt worden sind.

|

[Bild]

Bild: Protokoll-Einstellung

|

1 Einspiel-Protokoll löschen: Durch ein Kreuz in diesem Feld erreichen Sie, dass ein gegebenenfalls vorhandenes Logbuch vor der Übertragung gelöscht wird. Ansonsten wird das Logbuch immer länger und Sie sehen sämtliche aufgetretenen Probleme bei Datanorm-Einspielungen.

2 Einspiel-Protokoll führen: Da diese Informationen meist unwichtig sind, können Sie hier das Führen des Logbuches verhindern. Das Logbuch wird ohnehin nicht sofort ausgedruckt, sondern in einer Datei abgelegt. Diese Datei kann nach der erfolgten Datanorm-Einspielung eingesehen und gegebenenfalls auch gedruckt werden. Echte Fehler in der Datanorm werden auf jeden Fall protokolliert, unabhängig von der hier getroffenen Wahl.

Das Schreiben des Logbuches nimmt eventuell sehr viel Zeit in Anspruch, so dass wir empfehlen, in der Regel darauf zu verzichten.

3 Preishistorie führen: Durch ein Kreuz in diesem Feld können Sie erreichen, dass alle Preisänderungen registriert werden. In diesem Fall können Sie in den Stammdaten die Preisänderungen jedes einzelnen Artikels nachvollziehen.

Artikeleingrenzung bei Übernahme

|

[Bild]

Bild: Artikeleingrenzung bei Übernahme

|

1 Zu übernehmende Artikel: Hier müssen Sie die Auswahl treffen, welche Artikel übernommen werden sollen.

-

Alle Artikel übernehmen: Übernimmt alle Artikel aus der Datanorm-Datei.

-

Nur bestimmte Artikel: Diese Eingabe ist nur dann möglich, wenn neue Artikel nicht automatisch übernommen werden sollen. In diesem Falle kann hier der Artikelnummernbereich eingegeben werden.

2 Artikelübernahme gemäß Warengruppenauswahl: Wenn eine Warengruppendatei vorhanden ist, haben Sie hier die Möglichkeit festzulegen, ob die Artikel gemäß dieser Warengruppenauswahl übernommen werden sollen.

3 Einzelbestätigung: Wenn Sie in dieses Feld ankreuzen, werden Sie bei jedem Artikel gefragt, ob Sie ihn übernehmen wollen, oder nicht.

Preis-Einstellungen

|

[Bild]

Bild: Preis-Einstellungen

|

1 Rabattgruppe vorhanden: Wenn Rabattgrupen vorhanden sind, wird der EK aufgrund dieser Rabattgruppen ermittelt.

Wenn die Rabattdatei fehlt, müssen Sie entscheiden, wie sich das Programm verhalten soll.

[Bild]

Die Entscheidung ist nur wichtig, wenn es sich um vorhandene Artikeldaten handelt, die bereits mit einem Einkaufspreis versehen sind. Falls per Datei nun ein neuer Bruttopreis übertragen wird, so könnte es passieren, dass der alte Einkaufspreis trotz Preiserhöhung erhalten bleibt, weil kein Rabattsatz vorhanden ist. Um dies zu verhindern, muss angewählt werden EK1 = 0 setzen. In der Praxis kommt es leider manchmal vor, dass diese Entscheidung nicht richtig ist. Wir hatten es einmal, dass ein Händler per Datei zunächst den Einkaufspreis und anschließend den Listenpreis übergeben hat. Ohne die Entscheidung EK1 erhalten, würde der zuvor eingespielte Einkaufspreis immer gelöscht. Leider trifft die Datanorm keine Aussage über die Reihenfolge, mit der die Preise eingespielt werden müssen. Zusammengefasst kann man sagen, in der Regel ist es richtig den EK1 ggf. auf 0 zu setzen. Im Zweifel sollten Sie dieses anwählen. An dieser Stelle noch einmal der Hinweis auf eine Datensicherung.

2 Preise gültig ab: Falls Ihre Datanorm-Datei ohne Datum ist, haben Sie hier die Möglichkeit, das Datum einzusetzen. Standardmäßig wird dann hier das Tagesdatum vorgegeben, das Sie jedoch entsprechend ändern können.

Hinweis zu Staffelpreisen: Mit der Datanorm können Staffelpreise übertragen werden. Dabei wechselt der Einkaufspreis in Abhängigkeit von der eingekauften Menge. Da unser Programm über eine solche Datenstruktur nicht verfügt, lesen wir in diesem Falle den ersten Staffelpreis als Einkaufspreis ein und hinterlegen die weiteren Stufungen in der Artikelanmerkung. Wenn Sie einen Artikel aufrufen, der eine Artikelanmerkung hinterlegt hat, so können Sie dies am roten Knopf ‚Anmerkung’ erkennen.
