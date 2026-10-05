# Lesen/Verarbeiten

Pfad: Dokumentenbearbeitung > Dokumentenerstellung [3] > UGL-Schnittstelle > Lesen/Verarbeiten
Quelle: handbuch/lesen_verarbeiten.htm

|

Lesen/Verarbeiten

Hier müssen wir unterscheiden zwischen Daten, die wir selbst zum Großhändler geschickt haben und nun als Antwort zurückerhalten und solchen, die vom Großhändler ohne vorherige Übergabe aus dem Labelwin System bereitgestellt werden. Bei den zuletzt genannten Daten handelt es sich in der Regel um Lieferscheine des Großhändlers (die übrigens mit Preisen versehen sind) und Angebote, die vom Großhändler zusammengestellt worden sind. Solche UGL-Dateien werden übernommen, in dem ein neues Dokument mit der gewünschten Dokumentenart angelegt wird und dort über den Menüpunkt <Vorlagen> <UGL-Datei übernehmen> <Daten an Dokument anhängen> die entsprechende Vorlage gewählt wird.

Hauptmaske

Nach dem Start muss zunächst die Liste der UGL-Dateien aufgebaut werden. Treffen Sie dazu zunächst die gewünschte Eingrenzung (Punkte 2 und 10) und betätigen Sie dann den Knopf ‚Liste aufbauen’ (Nr. 9). Je nach Wahl werden dann ggf. nur die Ausgangs- oder Eingangsdateien aufgelistet. Die Eingangsdaten (also die vom Großhändler gekommenen) erkennt man am Kennzeichen E in der ersten Spalte der Tabelle, die Ausgangsdateien am Kennzeichen A. In der Regel werden die übergebenen Ausgangsdateien und die verarbeiteten Eingangsdateien gelöscht, so dass hier nur die aktuellen Vorgänge sichtbar sind. Die Formulierung ‚in der Regel’ bezieht sich darauf, dass Sie bei die Eingangsdateien nach dem Einlesen gefragt werden, ob sie gelöscht werden sollen.

[Bild: Lesen/Verarbeiten]

|
[Bild: 1]

Lieferant

[Bild: 1. Lieferant]

Falls Sie bei mehreren Großhändler den UGL-Datenaustausch eingerichtet haben, müssen Sie hier eine Auswahl treffen.

|
[Bild: 2]

Suche

[Bild: 2. Suche]

Wenn Sie im Feld 2 einen Lieferantennamen eingetragen haben oder nur die Anfangsbuchstaben des Namens, erhalten Sie durch Betätigen des Knopfes eine Auswahlliste mit dem eingegebenen Namen, sofern es diesen mehrfach gibt.

|
[Bild: 3]

Ablagepfad

[Bild: 3. Ablagepfad]

Hier wird Ihnen der Ablagepfad der UGL-Datei angezeigt. Wenn Sie ihn in der Großhändleradresse unter UGL-Stammdaten hinterlegt haben, wird er hier automatisch durchgereicht.

|
[Bild: 4]

Katalog

[Bild: 4. Katalog]

Hier wird Ihnen der Kurzname des Kataloges angezeigt, dessen Namen Sie im Feld 2 eingegeben haben.

|
[Bild: 5]

Durchsuchen

[Bild: 5. Durchsuchen]

Durch Betätigen dieses Knopfes öffnet sich der Explorer und Sie können so den Ablagepfad der UGL-Dateien manuell suchen.

|
[Bild: 6]

Einleseoptionen

[Bild: 6. Einleseoptionen]

Signifikante GH Stellen manuell:

Die aktuelle UGL kann standardmäßig mit Sets umgehen. Die früheren Versionen jedoch nicht. Aus diesem Grund benutzten und benutzen viele Großhändler einen kleinen Trick. Sie arbeiten mit signifikanten Stellen. Dieses Verfahren ist nirgendwo beschrieben oder geregelt. Es ist aber üblich, also ein ungeschriebenes Gesetz. Labelwin versucht diese Anzahl signfikanter Stellen automatisch zu ermitteln. Das klappt meistens, aber nicht immer. Wenn es einmal nicht klappt, können Sie es hier manuell anpassen.

Erklärung: Die Großhändler nummerieren ihre Positionen intern durch. Häufig in 1000er Schritten (=3 signifikante Stellen). 100er Schritte entsprechen 2 signifikante Stellen, 10er Schritte eine signifikante Stelle und bei 1er Schritten sind es null signifikante Stellen.

Bsp. für 3 signifikante Stellen:

00001000 Produkt A

00002000 Produkt B

00002010 Zubehör zu Produkt B

00002020 Zubehör zu Produkt B

00003000 Produkt C

Labelwin erkennt, dass es sich bei Produkt B um einen Setartikel handelt. Setzt man die signifikanten Stellen auf 1 oder 0, dann wird für Produkt B kein Set angelegt, sondern sie werden alle wie einzelne, vollwertige, Positionen angesehen.

Wie erkenne man nun, dass man die Anzahl der signifikanten Stellen manuell ändern muss?

Leider nicht so einfach. Sie erkennen es am ehesten daran, dass Labelwin Sets anlegt, wo keine Sets sein sollten, bzw. Einzelartikel anlegt, obwohl es Sets hätten werden sollten.

Wenn Sie aber bei einer UGL-Datei die signifikanten Stellen manuell ändern müssen, dann müssen Sie es höchstwahrscheinlich bei diesem Großhändler immer machen. Speichern Sie daher die Anzahl der signifikanten Stellen bei der Großhändleradresse ab (Modul Adressen unter dem Menüpunkt <Datei> <Bearbeiten> <Stammdaten UGL / Online>) und dort beim Reiter ‚UGL‘ unter ‚Signifikante GH Stellen manuell‘.

Merker setzen, wenn Artnr nicht vorhanden:

Wenn Sie ein UGL-Angebot vom Großhändler einspielen, wollen Sie manchmal Daten aus den Stammdaten dazu mischen, wie z.B. die kalkulierten Minuten. Nun kann das Programm bei den Positionen, bei denen ein Artikel nicht in den Stammdaten ist, einen Merker setzen. Mit der Suchfunktion können Sie dann die Positionen mit gesetztem Merker anspringen, um diese manuell zu bearbeiten.

Preis aus Stammdaten nehmen

Bei gesetztem Haken wird geprüft, ob der per UGL gekommene Artikel auch in den Katalog-Stammdaten vorhanden ist. Wenn das der Fall ist, wird der Einkaufspreis und der Listenpreis nicht aus der UGL-Datei, sondern aus den Stammdaten verwendet. Diese Option ist nur dann sinnvoll, wenn Daten aus einer Schnittstelle z.B. einem Auslegungsprogramm per UGL übertragen werden. Bei Lieferantendateien dagegen sollen ja gerade die Preise aus der UGL-Datei verwendet werden.

Sets auf offen statt verborgen setzen:

Dieses Ankreuzfeld kommt nur, wenn die UGL-Datei vom Typ MO (mobile offer) ist UND der ausgewählte Katalog KEIN mobile offer Katalog ist.

Standardmäßig werden Sets bei mobile offer auf verbogen gesetzt, da der beschreibende Text aus dem Setartikel und icht aus den Bestandteilen kommt.

Wenn aber ein UGL-Datei Ersteller wegen der Minuten das MO-Format benutzt, können die beschreibenden Texte aus den Bestandteilen kommen. Setzen Sie in diesem Fall den Haken.

Hinweis: Das Programm merkt sich den Haken benutzerbezogen.

|
[Bild: 7]

UGL-Typ Eingrenzung

[Bild: 7. UGL-Typ Eingrenzung]

Hier können Sie den UGL Typ eingrenzen. Es werden Ihnen dann nur UGL Dateien von den gewünschten Typen angezeigt. Die Eingrenzung soll helfen die Übersicht bei der Vielzahl an Dateien zu behalten.

Hinweis: Je mehr UGL-Dateien genutzt werden, desto wilder werden die Fehler. Neben den verschiedenen Eingrenzungen haben wir deshalb auch ein Ankreuzfeld "keine Typeingrenzung" eingeführt. Das hat zwar den Nachteil, dass man auch je nach Situation mal eine falsche Datei wählen kann, aber wir kommen sonst gegen das Chaos nicht an. Von manchen Lieferanten werden Varianten genutzt, die in der UGL-Definition einfach nicht vorgesehen sind. Ein Beispiel ist

das Kennzeichen LS für Lieferschein. Bei der Definition der UGL war das Kennzeichen nicht eingeplant (obwohl durchaus sinnvoll). Wir haben es jetzt zwar auch an der Oberfläche, aber sobald jemand eine Datei mit XYZ übergibt, müssten wir wieder ändern. Wenn Ihnen eine vorhandene Datei nicht angeboten wird, setzen Sie den Haken. Ob die Datei dann innen drin ggf. andere Fehler hat, ist ein anderes Thema.

|
[Bild: 8]

Liste neu aufbauen

[Bild: 8. Liste neu aufbauen]

Die Liste wird nach Änderungen nicht automatisch neu aufgebaut, sondern nur nach Betätigen dieses Knopfes. Wenn das Programm eine Änderung registriert hat, wird der Knopf in Rot dargestellt.

|
[Bild: 9]

Liste

[Bild: 9. Liste]

Wenn Sie von einer UGL-Datei die Werte übernehmen möchten, müssen Sie diese vorher markieren.

|
[Bild: 10]

Datei anzeigen

[Bild: 10. Datei anzeigen]

Das UGL-Format ist so verdichtet, dass man die Daten nicht lesen kann. Labelwin zieht sie in lesbarer Form auseinander.

|

Hinweis: Wegen des verwendeten Editors können Sie zwar in der Datei schreiben, die Änderungen werden jedoch nicht übernommen.

[Bild]

|
[Bild: 11]

FTP Versand

[Bild: 11. FTP Versand]

Wenn Sie von dieser Stelle aus den Transfer starten, werden nur die markierten Ausgabedateien übertragen. Die Mehrfachmarkierung erfolgt wie unter Windows üblich mit der Maus in dem ersten Feld der Tabelle und der gedrückten Shift- oder Strg-Taste.

|
[Bild: 12]

FTP Abholung

[Bild: 12. FTP Abholung]

Durch die Betätigung dieses Knopfes holen Sie die für Sie bereitsgestellten Dateien vom Großhändler ab.

|
[Bild: 13]

An Dokument anhängen

[Bild: 13. An Dokument anhängen]

Hier können die Preise einer als UGL eingegangenen Preisauskunft in das aktuelle Dokument übertragen werden. Dabei erfolgt die Zuordnung aufgrund der Positionsnummer – das aktive Dokument muss also entweder die ursprüngliche Preisanfrage sein oder die gleiche Struktur aufweisen. Im Zweifelsfalle erzeugen Sie erst eine Kopie von Ihrem Angebot, bevor Sie die Übertragung vornehmen.

|
[Bild: 14]

Ende

[Bild: 14. Ende]

Die Maske wird geschlossen.

Die Menüpunkte im Einzelnen:

|

Datei

Datei anzeigen (F3)

Mit dieser Funktion können Sie sich die markierte Datei anzeigen lassen. Es ist die gleiche Funktion wie der Knopf ‚Datei anzeigen’.

Dateien versenden per FTP (F7)

Durch die Wahl dieses Menüpunktes können Sie die in der Tabelle markierten Dateien versenden. Der Knopf ‚FTP-Versand’ hat die gleiche Funktion oder Sie benutzen die Funktionstaste F7.

Dateien abholen per FTP (F8)

Durch die Wahl dieses Menüpunktes können Sie die für Sie beim Großhändler bereit liegenden Dateien abholen. Der Knopf ‚FTP-Abholung’ hat die gleiche Funktion oder Sie benutzen die Funktionstaste F8.

Dateien anhängen an Dokument

Mit dieser Funktion können Sie die vom Großhändler abgeholte Datei in ein vorhandenes Dokument einlesen. Eine nähere Beschreibung hierzu finden Sie im Kapitel UGL-Schnittstelle.

Liste neu aufbauen

Nach dem Abholen oder Löschen von Dateien muss die Liste neu aufgebaut werden, damit Sie eine aktuelle Tabelle der vorhandenen Dateien erhalten. Es ist die gleiche Funktion wie der Knopf ‚Liste neu aufbauen’.

UGL-Vorgabe

Wenn Sie im Feld 2 einen Großhändler eingetragen haben und diesen Menüpunkt wählen, wird diese Adresse als feste Vorgabe gespeichert und Sie müssen nicht bei jedem Öffnen dieser Maske den Großhändler erneut eingeben.

UGL Datei löschen

Mit dieser Funktion können Sie eine in der Tabelle markierte Datei löschen.

Ende

Die Maske wird geschlossen.
