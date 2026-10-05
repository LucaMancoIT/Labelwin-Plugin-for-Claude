# 7.9 Reservegerät einrichten und aktivieren

Pfad: Kundendienst > KD-Mobil Notebook [Modul] > 7. Installation und Einrichtungsarbeiten > 7.9 Reservegerät einrichten und aktivieren
Quelle: handbuch/7_9_reservegerat_einrichten_und_aktivieren.htm

|

7.9 Reservegerät einrichten und aktivieren

Wenn sich ein Betrieb völlig auf die Abwicklung mit mobilen Geräten eingerichtet hat, kann es sinnvoll sein, ein weiteres Gerät in Reserve zu halten, das zum Einsatz kommt, wenn ein Gerät ausfällt.

Das Reservegerät wird dabei genauso eingerichtet, wie alle anderen Laptops auch. Es wird lediglich auf einen der vorhandenen Monteure eingerichtet, da in den seltensten Fällen eine freie Laptop Lizenz vorhanden ist.

Nachfolgend sind die Schritte beschrieben, mit denen das Ersatzgerät aktiviert wird, wenn es zum Einsatz kommen soll.

Als Beispiel gehen wir davon aus, dass drei Geräte im Einsatz sind und das Ersatzgerät mit den Daten des Gerätes Nr. 3 bestückt worden ist. Was ist zu tun, wenn nun Gerät Nr. 2 ersetzt werden soll?

In der Zentrale / auf dem Bürorechner:

|

Hier erfolgt keine Änderung, es muss nur die letzte Übertragungslauf-Nummer festgestellt werden, weil diese beim neuen Laptop eingetragen werden muss.

Die letzte Übertragungsnummer kann im Einstellmodul im Bereich [Programmbereiche – Kundendienst – Laptop Grundeinstellungen] über den Button „Datei-Nr Laptops“ eingesehen werden.

Alternativ kann man auch in der Datei \labelwin\global.ini den entsprechenden Eintrag finden:

[KDMobil]

NB2=47 = bedeutet, dass vom Laptop 2 zuletzt die

Dateinummer 47 eingelesen wurde

Hintergrund: Um festzustellen, ob beim Einlesen der Dateien auf der Zentrale evtl. Dateien vergessen wurden, nummerieren wir diese Dateien fortlaufend je Laptop. Bei nicht fortlaufender Nummer wird eine Warnmeldung ausgegeben.

|

[Bild]

Auf dem Notebook:

|

-

Laptopnummer auf 2 ändern:

Modul Einstellungen: Menüpunkt <Programmbereiche> <Kundendienst> <Laptop Grundeinstellungen> <Laptop Nummer>.

-

Importpfad / Kopierpfad Export ggfs. anpassen:

Wird mit Cloud-Abgleich gearbeitet, müssen die monteurspezifischen Pfade angepasst werden. Ebenfalls unter <Programmbereiche> <Kundendienst> <Laptop Grundeinstellungen>.

-

Übertragungsnummer umsetzen

Die oben beschriebene Übertragungslauf-Nummer vom Bürorechner muss beim Laptop eingetragen werden. Schauen sie bitte in der Zentrale nach der letzten eingelesenen Dateinummer und tragen diese dann auf dem Notebook ein.

Hintergrund: Um festzustellen, ob beim Einlesen der Dateien auf der Zentrale evtl. Dateien vergessen wurden, nummerieren wir diese Dateien fortlaufend je Laptop. Bei nicht fortlaufender Nummer wird eine Warnung ausgegeben.

|

[Bild]

Bild: Laptop Grundeinstellungen

4. Mitarbeiter wechseln

In der Kundendienst Maske muss unter >Optionen> <Mitarbeiter wechseln> der neue Monteur ausgewählt werden.

5. Vorgabe-Monteur anpassen:

Modul Einstellungen: Menüpunkt <Programmbereiche> <Kundendienst> <Grundeinstellungen> <Benutzer Einstellungen> <Anzeige>. Hier muss der Vorgabe-Monteur für die neu anzulegenden Aufträge umgestellt werden.

6. Auftragsnummer und Rechnungsnummer passend setzen:

Modul Einstellungen: Menüpunkte <Grundeinstellungen>, <Nummernkreise>.

Dort muss mindestens die Auftragsnummer und Rechnungsnummer auf die zuletzt verwendete Nummer vom zu ersetzenden Notebook eingetragen werden. Diese Werte müssen in der Zentrale aus dem Kundendienst und dem Rechnungsausgang ausgelesen werden.

7. Benutzerrechte aktivieren, wenn mit Rechten gearbeitet wird.

Unter Einstellungen – Optionen – Benutzerrechte vergeben muss der Monteur vom Laptop 2 eingetragen werden, wenn sie mit der Benutzerrechteverwaltung arbeiten.

Update

Außerdem sollten sie auf dem Ersatzlaptop, das nun zum Einsatz kommt, ein Label Update aufspielen und in der Zentrale die Grunddaten neu erzeugen und auf dem Laptop einspielen ( > Kapitel Update auf mobilem Gerät).
