# 10. Opticon OPL-8728

Pfad: Materialwirtschaft > Scannerverarbeitung [Modul] > 10. Opticon OPL-8728
Quelle: handbuch/10__opticon_opl_8728.htm

|

10. Opticon OPL-8728

|

Der Opticon-Scanner kann mit der Scann.exe ab der Version 3.71.69 genutzt werden. Diese kommt erst ca. Sept. 2009 in die allgemeine Auslieferung. Fragen Sie ggf. nach, damit wir Ihnen das Modul vorab zur Verfügung stellen.

Bei der Nutzung des Opticon-Scanners müssen einige Dinge beachtet werden, damit die Anwendung auch im Labelwin ohne Aufwand funktioniert.

Handhabung:

Nach Einschalten des Scanners erscheint in der Maske die Frage nach dem Kunden. Sinngemäß müsste hier unsere Projektnummer eingegeben werden. Das Eingabefeld lässt jedoch keine Sonderzeichen zu, sodass wir die Kennzeichnung der Projekt- und Kundendienstauftragsnummer auf besondere Art geregelt haben. Wenn Sie die Projekt- oder Auftragsnummer von einem Papier scannen können, so geben Sie in dem Feld Kunde lediglich eine 1 ein. Wenn Sie die Projekt- oder Auftragsnummer manuell tippen wollen, so müssen Sie bei der Projektnummer ein vorangestelltes p und bei der Kundendienstnummer ein vorangestelltes k eintippen (Gross/Kleinschrift ist egal). Den Bindestrich innerhalb der Nummer müssen Sie mit einem m (steht für Minus) ersetzen.

Beispiel Projektnummer 96-50002 müssen Sie erfassen als p96n50002.

Sollte es sich um eine Gutschrift handeln, muss zusätzlich das Minuszeichen vor die Projektnummer gestellt werden. Das Minus muss wiederum durch ein m geschrieben werden, da die Minustaste ja nicht angenommen wird. Bei vorigem Beispiel würde also mp96n50002 getippt.

Wenn die Projekt- oder Kundendienstnummer als Strichcode vorliegt (z.B. auf dem Kundendienstauftrag mitgedruckt), so können wir ein besseres Verfahren vorschlagen. Geben Sie nach Start des Scannerprogramms im Feld Kunde einfach nur eine 1 ein. Scannen Sie anschließend die Projekt- oder Kundendienstnummer an der Stelle, an der vom Programm eigentlich eine Artikelnummer erwartet wird. Diese Nummer kann Labelwin nachher richtig interpretieren, weil in unserem Strichcode entsprechende Kennzeichen mit enthalten sind.

Das Programm auf dem Scanner verlangt anschließend zwingend wieder eine Eingabe der Menge, die bei einer Projekt- oder Kundendienstauftragsnummer natürlich unsinnig ist. Geben Sie hier wieder einfach nur eine 1 ein und bestätigen mit der Enter-Taste.

Der Ablauf mit Auftragsnummern als Strichcode sieht also so aus:

Scanner aktivieren

Bei Name 1 eingeben + Enter

Auftragsnummer scannen

Menge 1 eingeben + Enter

Artikelnummer scannen

Menge eingeben + Enter

Artikelnummer usw.

Wenn im gleichen Scannvorgang ein weiterer Kundendienstauftrag gescannt werden soll, so wird dieser jetzt einfach gescannt ohne zuvor auf das Start-Menü mit dem Kundennamen zurück zu gehen.

Einrichtungsarbeiten:

Da die Datei zum Auslesen des Scanners an einer x-beliebigen Stelle in Ihrem Programmsystem liegen kann, benötigt unser Programm den Pfad und Namen dieses Programms. Dazu muss eine Datei OPTICON.BAT im Verzeichnis Labelwin angelegt werden.

Inhalt der Datei:

c:\Programme\NOS GmbH\BC Scan\ID_NOS.exe

Bei diesem Inhalt lägen die Programme auf der Platte C: :

Hinweis für Spezialisten: Wenn man sich in das Verzeichnis stellt und dann die Datei startet, schließt sich das Programm nicht wieder. Das klappt nur, wenn man aus einem anderen Verzeichnis heraus startet.

Weiter muss ein Pfad eingerichtet werden, in dem das Scannerprogramm seine Daten ablegt (als xxx.DAT) und unser Programm dann die Daten ausliest und löscht. Der Pfad ist völlig frei, aber da nach dem Auslesen alle UGL und UGS-Dateien gelöscht werden, die vom Scannerprogramm erzeugt aber im Labelwin nicht benötigt werden, muss es ein sonst ungenutztes Verzeichnis sein. Unser Vorschlag ist \labelwin\opticon . Der Pfad muss manuell angelegt werden.

Der Eintrag im Scannerprogramm erfolgt nach Aufruf der Datei C:\Programme\NOS GmbH\BC Scan.exe mit dem Explorer. Es erscheint dieses Bild, in dem Sie den gleichen Pfad eintragen müssen, wie im Labelwin.

[Bild]

….

[Bild]

Der Eintrag im Labelwin erfolgt im Modul Scanner. Drücken Sie dort den Knopf Ändern und nehmen die Einstellungen vor.
