# 3. Anwendung

Pfad: Schnittstellen > Shop-Schnittstellen (IDS, UGL, OCI etc.) > 3. Anwendung
Quelle: handbuch/3__anwendung_2.htm

|

3. Anwendung

3.1 Allgemein

Die Shop-Einbindung kommt in der Artikelerfassung zum Einsatz. In der Maske, in der Sie die bisherigen Artikel eines Dokumentes aufgelistet bekommen, kommen Sie mit der Taste F8 in das Shop-System. Dabei verhält sich das Programm etwas unterschiedlich, je nachdem ob Sie bereits Artikel in dem Dokument haben oder noch ein leeres Dokument vorhanden ist.

Bei vorhandenen Artikeln stellen Sie sich am besten auf eine Position des Großhändlerkataloges, in dessen Shop Sie gehen wollen. Die Shop-Maske positioniert sich dann sofort auf diesen Großhändlerkatalog und findet ggf. auch die richtige Lieferantenadresse aus den Adressstammdaten. Der bei der Adresse als bevorzugter Shop-Typ hinterlegte Shop wird automatisch aktiviert. Je nach Shop-Typ stehen jetzt unterschiedliche Funktionen zur Verfügung

[Bild]

1) Mit diesem Knopf startet nur der Shop, ohne jegliche Datenübergabe. Es ist also so, als wenn der Shop direkt per Internet-Browser gestartet würde.

2) Shopsuche:

Der Shop wird ohne Übergabe von Daten gestartet. Wenn im Shop ein Warenkorb gefüllt wird und dort die Rückgae entsprechend ausgelöst wird, werden die Artikel ins Labelwin übernommen. Übernommen werden sie wie üblich vor der markierten Zeile im Dokument. Der Verkauf wird entsprechend der aktuellen Kalkulationseinstellung ermittelt.

3) Bestellung senden:

An den Shop werden die Artikel entsprechend der Einstellung (7) übergeben. Bevor der Shop startet, gelangen Sie in eine Bestellmaske, in der Sie diverse Eingaben für die Bestellung festlegen können. Es wird bereits an dieser Stelle eine Bestellnummer vergeben. Falls Sie die Bestellung abbrechen, fehlt im Labelwin eine Nummer, was jedoch keine Auswirkungen hat. Das Fehler einer Bestellnummer spielt keine Rolle.

Wenn die Bestellung im Shop wirklich ausgelöst wurde, legt Labelwin nach der Rückgabe ein neues Dokument vom Typ Bestellung an.

4) Artikel -> Shop:

An den Shop werden die Artikel entsprechend der Einstellung (7) übergeben. Innerhalb des Shops können nun diverse Änderungen vorgenommen werden, Artikel hinzugefügt werden usw. Wenn im Shop die Rückübergabe an das Handwerkerprogramm (Labelwin) eingestellt wird, wird der Warenkorb mit dem aktiven Labelwin-Dokument abgeglichen. Der Abgleich erfolgt aufgrund der Labelwin-Positionsnummer, die laut Schnittstellenvereinbarung im Shop nicht verändert werden darf.

Zum Test empfehlen wir die Rückgabe mit Einzelbestätigung zu aktivieren (Feld 8).

5) Artikelinfo:

Für den gerade anzeigten, im Dokument markierten Artikel wird die Artikelinfo des Lieferanten gestartet. Je nach Shop können Sie dort aktuelle Preise, Verfügbarkeiten, Bilder, Explosionszeichnungen usw. sehen.

6) Übergabe an Shop:

Hier legen Sie fest, welche Artikel an den Shop übergeben werden. Die Übergabe erfolgt aber nur bei den Knöpfen 3 + 4

7) Rückgabewerte:

Legen Sie hier fest, was mit den Rückgaben aus dem Shop passieren soll. Neue Artikel werden automatisch am Ende des Dokuments neu angelegt.

Je nach Dokumententyp müssen Sie die zu übernehmenden Werte festlegen. Bei einem LV werden geänderte Mengen und Verkaufspreise sicherlich nicht übernommen, bei einem Angebot kann dies durchaus sein.

Aktivieren Sie zum Testen zunächst einfach die ‚Einzelbestätigung’, damit Sie sehen können, was passiert.
