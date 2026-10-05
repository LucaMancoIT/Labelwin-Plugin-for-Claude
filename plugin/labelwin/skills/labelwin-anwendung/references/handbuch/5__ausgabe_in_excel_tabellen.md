# 5. Ausgabe in Excel-Tabellen

Pfad: Auswertungen / Controlling > Controlling [Modul] > Controlling / Chefknopf > Abfragen erstellen > 5. Ausgabe in Excel-Tabellen
Quelle: handbuch/5__ausgabe_in_excel_tabellen.htm

|

5. Ausgabe in Excel-Tabellen

Bevor Sie eine Abfrage mit Ausgabe in eine Excel-Datei erstellen können, muss diese angelegt sein. Das Programm erwartet die Tabelle zwingend im Verzeichnis labelwin\excel\vorlage.

Bei der Ausgabe einer Abfrage wird diese Exceldatei in das Verzeichnis ‚labelwin\excel\ausgabe’ kopiert und mit Werten gefüllt. Die Originaldatei bleibt dabei unverändert.

Eine Exceldatei hat eine oder mehrere Blätter, die mit Namen versehen sind. Standardmäßig heißen sie Tabelle1, Tabelle2 usw., können aber umbenannt werden (mit rechter Maustaste auf die Beschriftung). Auch die Benennung sollten Sie durchführen, bevor Sie die Tabelle in einer Abfrage eintragen.

Bei einer Excel-Abfrage können Sie beliebig viele Einzelabfragen mit der Ausgabe auf verschiedene Blätter erstellen. Über die Verwendung von ‚Formeln’ können Sie auch einzelne Summe wie z.B. Summe Eingangsrechnungen, Ausgangsrechnungen, Lohnkosten usw. in Ihre Exceldatei bekommen, um diese dort weiterverarbeiten zu können. Details dazu lesen Sie weiter hinten.

Bevor wir zu den Abfragen im Labelwin kommen, müssen wir die Regeln beschreiben, mit denen die Excel-Vorlagedatei erstellt wird. Dabei können wir natürlich nicht auf die generelle Bedienung von Excel eingehen, sondern nur auf die uns hier betreffenden Bereiche.

Der Ablauf könnte so aussehen:

- beginnen einer neuen Exceldatei

- sofort speichern im Verzeichnis Labelwin\excel\vorlage mit z.B. dem Namen Auswert1.xls

- die erste Tabelle soll uns eine ‚schöne’ Darstellung unseres Ergebnisses. Benennen wir sie mit ‚Ergebnis’.

- Auf der zweiten Tabelle möchten wir die Ausgangsrechnungen des letzten Monats sehen. Benennen wir sie ‚Ausgangsrg’

- die dritte Seite nennen wir ‚Eingangsrg’

- auf der vierten Seite bringen wir die Werte der ‚Personal’-Liste

- auf der fünften und letzten Seite bringen wir Zwischenergebnisse unter und nennen sie ‚Grunddaten’. Dieser Name hat eine besondere Bedeutung, da wir dort ohne großen Aufwand sehr einfach einzelne Abfrageergebnisse platzieren können.

[Bild]

Schauen wir zunächst nach der Seite der Ausgangsrechnungen: Bis auf eine Überschrift ist sie leer.

Als Abfrage setzen wir eine Liste mit Rechnungsnummer, Datum, Brutto, Netto ein.

Die Abfrage ist relativ einfach:

SELECT rgausgang.rgnummer, rgausgang.rgdatum, rgausgang.Brutto, rgausgang.netto

Allerdings fehlt eine Eingrenzung nach Datum und ggf. nach dem Mandant (falls Sie mit mehreren Firmen in einer Datenbank arbeiten). Um so etwas in die Abfrage zu bekommen gibt es Schlüsselworte, die später automatisch ersetzt werden. Eine Liste aller Schlüsselworte finden Sie am Ende dieses Kapitels.

SELECT rgausgang.rgnummer, rgausgang.rgdatum, rgausgang.Brutto, rgausgang.netto

WHERE rgausgang.mandant= ##mandant##

AND rgausgang.rgdatum >= ##vondatum##

AND rgausgang.rgdatum <= ##bisdatum##

Jetzt wird es komplizierter, wenn wir auch die Adresse des Kunden und die Objektadresse zeigen wollen. Da im Rechnungsausgangsbuch nur die Nummer der Adresse gespeichert ist, muss eine Verbindung zur Adresstabelle erstellt werden. Dies geschieht durch Befehle wie LEFT JOIN, INNER JOIN. Spätestens hier wird verständlich, warum die Erstellung solcher Abfragen etwas für Spezialisten ist, die mit Access-Abfragen umgehen können.

SELECT rgausgang.rgnummer, rgausgang.rgdatum, rgausgang.Brutto, rgausgang.netto, adstamm.Suchwort1, adstamm.Ort, Objektadresse.Suchwort1, Objektadresse.Ort

FROM (rgausgang

LEFT JOIN adstamm AS Objektadresse ON rgausgang.objektadr = Objektadresse.adnr)

INNER JOIN adstamm ON rgausgang.adresse = adstamm.adn

WHERE rgausgang.mandant= ##mandant## AND rgausgang.rgdatum >= ##vondatum## AND rgausgang.rgdatum <= ##bisdatum##

Im Ergebnis werden im Excelblattes die Daten mit der Überschrift der Feldnamen eingetragen. Das sieht nicht wirklich schön aus.

[Bild]

Deshalb schreiben wir die Überschriften nun in die Exceltabelle selber.

Das Programm verhält sich so, dass die Überschriften nicht automatisch gefüllt werden, wenn in der Spalte, deren Nummer in der Abfrage eingetragen ist, bereits etwas steht.

[Bild]

Als letztes setzen wir noch einen Autofilter auf die Überschriften. Dies geschieht nach Markierung der 4. Zeile mit den Menüpunkten ‚Daten, Filter, Autofilter’.

Das Endergebnis kann so aussehen:

[Bild]

Über die Pfeile bei den Überschriften, die durch die Funktion ‚Autofilter’ entstehen, können nun sehr einfach Eingrenzungen getroffen werden.

Tricks:

Dummy-Spalte

Wenn auf einem Excelblatt Zwischensummen oder Ergebnisse in einer Tabellenspalte ausgegeben werden sollen, taucht das Problem auf, dass diese entweder am Ende der vom SQL-Befehl gefüllten Spalten stehen muss, damit das Zwischenergebnis nicht überschrieben wird. Um dieses Problem zu umgehen haben wir ein Feld ’Dummy’ eingeführt. Bei dem Häkchen vor und hinter dem Wort handelt es sich um das Zeichen, was zusammen mit dem #-Zeichen auf der Taste ist. Es wird so in den SQL-Befehl geschrieben, als wenn es sich um ein Datenbankfeld handeln würde.

Beispiel: SELECT rgausgang.brutto, ’Dummy’, rgausgang.netto

In der Exceltabelle würde dann in der ersten Spalte die Bruttosumme stehen, die zweite Spalte würde nicht verändert, in der dritten Spalte steht die Nettosumme. Die zweite Spalte wird also nicht geleert, sondern bleibt so wie sie ist. Wenn Sie also in der zweiten Spalte des Excelblattes eine Rechenformel eingetragen haben, bleibt diese erhalten.

Spalte +

Eine ähnliche Funktion gibt es mit ’Spalte + 1’ , wobei statt der 1 eine beliebige Zahl eingetragen werden kann. Bei ’Spalte + 2’ bleiben 2 Spalten unverändert, bei ’Spalte + 3’ sind es 3 Spalten usw. Auf den ersten Blick sieht es so aus, als wenn man genauso gut 3 mal ’Dummy’ hätte schreiben können. Die Besonderheit ist jedoch, dass man die Zahl auch im SQL-Befehl berechnen lassen kann. In unserem ausgelieferten Muster finden Sie so etwas bei der Ausgabe der Monatssummen. Darin gibt es eine Stelle mit

'spalte+' + Format$([rgausgang].[rgdatum],'mm') AS [rgdatum nach Monaten]

wo dies genutzt wird. Je nach Monat der Rechnung wird Spalte + 1 bei Januar bis Spalte +12 bei Dezember gesetzt.
