# 6.2 Daten exportieren

Pfad: Artikelstammdaten > Katalog [10] > 6. Sonderfunktionen > 6.2 Daten exportieren
Quelle: handbuch/6_2_daten_exportieren.htm

|

6.2 Daten exportieren

6.2.1 Lohnminuten auslagern

|

Mit Hilfe dieses Programmbereiches ist es möglich, die Lohnminuten eines Kataloges zu retten. Es kommt immer wieder vor, dass die Lieferanten dazu auffordern, die Artikeldaten zu löschen und neu einzuspielen. Obwohl nach der Datanorm Löschartikel übergeben werden können, können viele Großhändler und Hersteller nicht damit umgehen. Für Sie ist es häufig einfacher, den Katalog zu löschen und neu einspielen zu lassen. Bei diesem Schritt wären jedoch Ihre hinterlegten Lohnminuten verloren.

Die Lohnminuten können auf eine Diskette oder in einer Datei auf der Festplatte eingespeichert werden. Das Programm schreibt eine normale Datanormdatei in der Version 4.0. Diese Datei kann bei Label unter dem Menüpunkt <Einlesen> <Datanorm und Datpreis> eingespielt werden. Über diesen Weg ist es auch möglich, mit einem Kollegen die Minutensätze auszutauschen.

Da es zwei Ablagebereiche für Minutensätze gibt, müssen Sie ggf. das Programm zweimal laufen lassen. In der Regel werden Sie lediglich die Daten in dem Feld ´Eigene Minuten´ absichern. Wenn bei Label Minutensätze per Hand eingegeben werden, so landen diese in der Regel in diesem Feld.

|

[Bild]

Bild: Auslagerung Lohnminuten

6.2.2 Kalkgruppenzuordnungen auslagern

Es geht um die Funktion, bestimmte Artikelgruppen mit unterschiedlichen Kalkulationsfaktoren zu kalkulieren – also z.B. Isolierung mit Multi 1,5, Kessel mit 1,15 usw. Dazu müssen die Artikel mit einer Information der Kalkgruppe versehen sein. Diese ist unter anderem über eine Zuordnung der Rabatt- oder Warengruppen zu den Kalkgruppen möglich. Für den Fall, dass ein Händlerkatalog neu eingespielt werden muss, kann man die Zuordnungen hier in einer Datei speichern und dann später wieder importieren. Ein Import ist über das Menü in der Maske der Zuordnungen möglich.

6.2.3 Pendeldiskette

|

Bei der Pendeldiskette handelt es sich um ein Relikt aus alten Zeiten. Sie diente dazu, dem Großhändler mitzuteilen, welche Artikel seines Artikelstammes auf dem Kundenrechner vorhanden sind. Der Großhändler schrieb dann die entsprechenden Preise dahinter und gab die Pendeldiskette als DATPREIS-Datei zurück.

Unseres Wissens wird die Pendeldiskette nicht mehr verwendet – aber wer weiß.

Eine Beschreibung der einzelnen Punkte erübrigt sich sicherlich.

|

[Bild]

Bild: Pendeldiskette

6.2.4 Auslagerung Datanorm

In diesem Programmbereich können Sie einen Artikelkatalog als DATANORM oder DATPREIS-Datei ausgeben. Um Schwierigkeiten aus dem Weg zu gehen, sollten Sie solche Artikeldaten nicht über die ‚normale Erfassung’ in den Artikelstammdaten eingeben, sondern über den Programmbereich <Sonderfunktionen> <Datanorm erfassen>. Das große Problem ist, dass bei Label abweichend von der Datanorm Kurztexte bis zu 32000 Zeichen enthalten können. Bei der gerade angesprochenen Datanormerfassung ist gewährleistet, dass der Artikelkurztext max. 2 Zeilen a-40 Zeichen enthält. Nur solche Daten sind als Datanormdatei auszugeben.

Die erzeugten Datanorm- bzw. Datpreisdateien sind nach den Regeln der Datanorm 4.0 geschrieben.

Bei der Ausgabe als Datei besteht die Möglichkeit, die Zwischendateien mit den Namen Datanorm.001, Datanorm.002 usw. auf der Festplatte zu belassen. Hierüber können relativ einfach weitere Dateikopien erstellt werden.

Bitte gehen Sie die Maske Punkt für Punkt durch, um keine fehlerhaften Daten zu erzeugen. Wichtig ist die Kennzeichnung als Neuanlage oder Änderung. Falls beim Empfänger der Datanorm die Artikel noch nicht auf der Festplatte vorhanden sind, so dürfen Sie nicht als Änderungsartikel gekennzeichnet werden. Änderungsartikel dürfen nur übergeben werden wenn sichergestellt ist, dass die Artikel bereits vorhanden sind. Dabei ist es unerheblich, ob in dem Änderungssatz alle Datenfelder enthalten sind oder nicht. Im Zweifelsfalle sollten Sie die Datanorm also als Neuanlage übergeben. Die meisten Programme auf dem Markt werden sicherlich eine Prüfung durchführen um zu verhindern, dass ein Artikel doppelt auf der Festplatte abgelegt wird.

Bei der Preisausgabe ist es wichtig, auch das richtige Preiskennzeichen (brutto/netto) zu setzen.

Bei der Übergabe ist leider nur der Listen oder Nettopreis in einem Datensatz zu übergeben. Wenn Sie beide Preisfelder übergeben möchten, so müssen Sie nach der Datanorm mit dem Bruttokennzeichen eine Datpreis-Datei mit den Nettopreisen erzeugen. Diese beiden Dateien dürfen durchaus auf der gleichen Diskette abgelegt werden.

DATANORM 4 schreibt ein Währungskennzeichen vor. Das Währungskennezeichen wird automatisch auf EUR gesetzt. Sollten Sie Ihren Katalog in Landeswährung führen, haben Sie unter dem Menüpunkt <Sonderfunktionen> <Daten exportieren> <Euro Konvertierung> <Katalog in Landeswährung konvertieren> die Möglichkeit, den Katalog in die Landeswährung umzuwandeln.

[Bild]

Bild: Auslagerung Datanorm 4.0

[Bild]

1 Zielverzeichnis: Tragen Sie hier den Zielpfad ein.

[Bild]

2 Ausgabeart: In dieser Auswahlbox legen Sie fest, ob Sie eine Datanorm-Datei oder einen Preissatz (Datpreis) oder Setartikel (Dataset) übergeben möchten. Eine Übergabe als Datpreis kann nur dann erfolgen, wenn sichergestellt ist, dass der Artikel beim Anwender bereits angelegt ist. Die Datpreisdatei enthält lediglich die Artikelnummer und den dazugehörigen Preis.

[Bild]

3 Eingrenzung: Eine Übergabe als Änderung ist nur dann sinnvoll, wenn sichergestellt ist, dass der Artikel beim Endanwender bereits vorhanden ist. Durch eine Kennzeichnung als Änderungssatz kann niemals eine Neuanlage erfolgen. Da Sie in der Regel nicht wissen, welche Daten beim Anwender vorliegen, sollten Sie im Zweifelsfall die Artikel als Neuanlage übergeben. Nahezu alle vernünftigen Programme prüfen vor dem Einspielen ab, ob der Artikel bereits vorhanden ist. In diesem Falle haben die neuen Artikel in der Regel „gewonnen“ und überschreiben die Daten des alten.

[Bild]

4 Minuten übertragen: Wenn Sie bei Ihren Artikeln kalkulierte Lohnminuten hinterlegt haben, so können Sie diese ebenfalls mit übergeben. Bei LABEL gibt es zwei Datenfelder, in denen Minuten eingetragen werden können. Sie müssen hier festlegen, welches Datenfeld Sie übertragen möchten. Es werden nur jene Artikel übertragen, bei denen tatsächlich Minuten hinterlegt sind.

[Bild]

5 Preise ausgeben: Legen hier Sie fest, welcher Preis in die Datanorm oder Datpreis-Datei eingetragen werden soll. Über das Preiskennzeichen (Nr. 6) wird festgelegt, ob dieser Preis beim Endanwender als Brutto- oder Nettopreis erscheinen wird.

[Bild]

6 Preis Kennzeichnen als: Hier legen Sie fest, ob der unter Nr. 5 gewählte Preis beim End-Anwender als Brutto/Listenpreis oder Nettopreis übergeben werden soll.

[Bild]

7 gültig ab: Tragen Sie hier ein, ab wann die Datei gültig ist. Wenn Sie das Feld leer lassen, ist sie ab sofort gültig.

[Bild]

8 Datum: Setzen Sie hier dass Gültigkeitsdatum ein. Dieses Datum wird dem Endanwender beim Einspielen der Daten in der Regel auf dem Bildschirm angezeigt. Er kann also darüber feststellen, ob dies die aktuellste oder eine ältere Datanormdatei ist.

[Bild]

9 Hersteller: Hier können Sie Ihren Firmennamen eintragen. Der Name wird in der Regel bei der Einspielung gezeigt.

[Bild]

10/11 Kommentar 1/2: In diese beiden Zeilen können Sie Informationen eintragen, die dem Anwender beim Einspielen der Daten gezeigt sollen.

[Bild]

12 Ok: Durch Betätigen dieses Knopfes wird die Ausgabe gestartet.

[Bild]

13 Abbruch: Durch Betätigen dieses Knopfes wird die Ausgabe abgebrochen. Bereits gewählte Einstellungen werden ohne Nachnachfrage zurückgesetzt.
