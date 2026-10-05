# IDS-Shop Anwendung

Pfad: Schnittstellen > Shop-Schnittstellen (IDS, UGL etc.) > IDS-Shop > IDS-Shop Anwendung
Quelle: handbuch/ids_shop_anwendung.htm

|

IDS-Shop Anwendung

Die Shop-Einbindung kommt in der Artikelerfassung zum Einsatz. In der Maske, in der Sie die bisherigen Artikel eines Dokumentes aufgelistet bekommen, kommen Sie mit der Taste F8 in das Shop-System. Dabei verhält sich das Programm etwas unterschiedlich, je nachdem ob Sie bereits Artikel in dem Dokument haben oder noch ein leeres Dokument vorhanden ist.

Bei vorhandenen Artikeln stellen Sie sich am besten auf eine Position des Großhändlerkataloges, in dessen Shop Sie gehen wollen. Die Shop-Maske positioniert sich dann sofort auf diesen Großhändlerkatalog und findet ggf. auch die richtige Lieferantenadresse aus den Adressstammdaten. Der bei der Adresse als bevorzugter Shop-Typ hinterlegte Shop wird automatisch aktiviert. Je nach Shop-Typ stehen jetzt unterschiedliche Funktionen zur Verfügung

[Bild: IDS-Shop Anwendung]

Bild: Online-Shop

|
[Bild: 1]

Shop Auswahl

[Bild: 1. Shop Auswahl]

Wählen Sie hier den Händler mit dem Sie IDS-Daten austauschen möchten. Sollten mehrere Shop-Schnittstellen beim Händler eingerichtet sein, so achten Sie darauf, dass hier der "IDS Webshop" ausgewählt wird.

|
[Bild: 2]

Übergabe

[Bild: 2. Übergabe]

Hier legen Sie fest, welche Artikel an den Shop übergeben werden. Die Übergabe erfolgt aber nur bei den Knöpfen 3 + 4

|
[Bild: 3]

verknüpfte Artikel

[Bild: 3. verknüpfte Artikel]

Diese Option ist für Anwender, die Artikelverknüpfungen für diesen Großhändler definiert haben.

Mit IDS können Sie nur Artikelnummern senden, die der Großhändler auch kennt, d.h. nur die echten Artikelnummern des Großhändlers. Wenn Sie in Ihrem Dokument Artikel eines anderen Großhändlers oder aus dem eigenen Katalog haben, wird der Versand scheitern. Haben Sie aber diese Artikel mit den entsprechenden Artikeln dieses Großhändlers verknüpft, dann wird die Artikelnummer des Großhändlers gesendet.

ACHTUNG: Bei der Rückübertragung des Artikels wird im Dokument Artikelnummer und Katalog ausgetauscht.

Dies ist sinnvoll, wenn Sie im Dokument die Artikel von Großhändler A haben, jetzt aber bei Großhändler B bestellen.

Wenn Sie aber im Dokument die Artikel aus dem 'eigenen' Katalog gewählt haben, weil Sie hier z.B. die schöneren Texte haben, dann sollten Sie über die Option "ggf. verkn. Artikel lesen" im Bereich "Rückgabewerte" dafür sorgen, dass im Dokument der eigene Artikel mit Artikelnummer, Katalognummer, Text und Liefermengeneinheit stehen bleibt.

|
[Bild: 4]

Referenz- / Bezugsnummer

[Bild: 4. Referenz- / Bezugsnummer]

Damit der Großhändler beim Abruf von Artikeln auf Preise reagieren kann, die in einem vorherigen Angebot oder Auftragsbestätigung vereinbart wurden, können/müssen Sie hier die Referenz- oder Bezugsnummer angeben. Das ist normalerweise die Vorgangsnummer, bzw. die Angebots- oder Auftragsbestätigungsnummer.

Leider benötigen die meisten Großhändler nicht nur diese Nummer, sondern auch noch eine spezielle Referenznummer pro Artikelzeile. Diese bekommen Sie nur, wenn Sie das Angebot bzw. die Auftragsbestätigung vorher per UGL/GAEB oder IDS importiert haben. In diesem Fall finden Sie auch die entsprechende Vorgangsnummer in der Auswahlliste.

Hinweis: Wenn Sie mehr als eine Vorgangsnummer in der Liste haben, dann haben Sie mehrere Vorgänge in ein Dokument gemischt. In diesem Fall wird der Großhändler nur teilweise oder gar keine individuellen Preise zuordnen können, weil die Referenzen in einigen Zeilen nicht zur Vorgangsnummer passen.

Wichtiger Hinweis: Die UGL/GAEB und IDS Schnittstellen sehen diese Technik vor. Es ist aber nicht garantiert, dass die EDV des Großhändlers darauf reagiert. Bitte fragen Sie ggf. bei Ihrem Großhändler nach.

|
[Bild: 5]

Rückgabewerte

[Bild: 5. Rückgabewerte]

Legen Sie hier fest, was mit den Rückgaben aus dem Shop passieren soll. Neue Artikel werden automatisch am Ende des Dokuments neu angelegt.

Je nach Dokumententyp müssen Sie die zu übernehmenden Werte festlegen. Bei einem LV werden geänderte Mengen und Verkaufspreise sicherlich nicht übernommen, bei einem Angebot kann dies durchaus sein.

Aktivieren Sie zum Testen zunächst einfach die ‚Einzelbestätigung’, damit Sie sehen können, was passiert.

|
[Bild: 6]

Zum Shop Portal

[Bild: 6. Zum Shop Portal]

Mit diesem Knopf startet nur der Shop, ohne jegliche Datenübergabe. Es ist also so, als wenn der Shop direkt per Internet-Browser gestartet würde.

|
[Bild: 7]

Shopsuche (WKE)

[Bild: 7. Shopsuche (WKE)]

Der Shop wird ohne Übergabe von Daten gestartet. Wenn im Shop ein Warenkorb gefüllt wird und dort die Rückgae entsprechend ausgelöst wird, werden die Artikel ins Labelwin übernommen. Übernommen werden sie wie üblich vor der markierten Zeile im Dokument. Der Verkauf wird entsprechend der aktuellen Kalkulationseinstellung ermittelt.

|
[Bild: 8]

Bestellung senden (WKS)

[Bild: 8. Bestellung senden (WKS)]

An den Shop werden die Artikel entsprechend der Einstellung (7) übergeben. Bevor der Shop startet, gelangen Sie in eine Bestellmaske, in der Sie diverse Eingaben für die Bestellung festlegen können. Es wird bereits an dieser Stelle eine Bestellnummer vergeben. Falls Sie die Bestellung abbrechen, fehlt im Labelwin eine Nummer, was jedoch keine Auswirkungen hat. Das Fehler einer Bestellnummer spielt keine Rolle.

Wenn die Bestellung im Shop wirklich ausgelöst wurde, legt Labelwin nach der Rückgabe ein neues Dokument vom Typ Bestellung an.

|
[Bild: 9]

Artikel senden (WKS)

[Bild: 9. Artikel senden (WKS)]

An den Shop werden die Artikel entsprechend der Einstellung (7) übergeben. Innerhalb des Shops können nun diverse Änderungen vorgenommen werden, Artikel hinzugefügt werden usw. Wenn im Shop die Rückübergabe an das Handwerkerprogramm (Labelwin) eingestellt wird, wird der Warenkorb mit dem aktiven Labelwin-Dokument abgeglichen. Der Abgleich erfolgt aufgrund der Labelwin-Positionsnummer, die laut Schnittstellenvereinbarung im Shop nicht verändert werden darf.

Zum Test empfehlen wir die Rückgabe mit Einzelbestätigung zu aktivieren (Feld 8).

|
[Bild: 10]

Umlaute kodieren

[Bild: 10. Umlaute kodieren]

Es kann vorkommen, dass ein Händlershop mit Umlauten nicht zurecht kommt. In diesem Fall kann mit dieser Option erreicht werden, dass keine übliche Kodierung erfolgt

|
[Bild: 11]

Artikelinfo

[Bild: 11. Artikelinfo]

Für den gerade anzeigten, im Dokument markierten Artikel wird die Artikelinfo des Lieferanten gestartet. Je nach Shop können Sie dort aktuelle Preise, Verfügbarkeiten, Bilder, Explosionszeichnungen usw. sehen.
