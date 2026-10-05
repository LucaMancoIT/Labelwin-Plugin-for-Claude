# Labelwin Update [13]

Pfad: Installation und Wartung > Labelwin Update [13]
Quelle: handbuch/labelwin_update__13_.htm

|

Labelwin Update [13]

Das Einspielen einer neuen Programmversion ist so einfach, das es kaum einer Beschreibung bedarf.

Im Netzwerk darf keiner mit dem Programm arbeiten, während das Update eingespielt wird. Auch auf dem eigenen Arbeitsplatz darf außer dem Updatemodul keines unserer Programme aktiv sein.

In der Regel muss nach dem Update das Programm-Modul Datenbank aktualisieren ablaufen. Dieses Modul wird nach dem Einspielen des Updates automatisch nachgeladen und Sie müssen nur noch den Start-Knopf betätigen. Der Hintergrund ist, dass immer wenn wir neue Datenbankfelder eingeführt haben, diese auch in Ihrer aktuellen Datenbank eingefügt werden müssen. Dabei werden mitgelieferte leere Datenbanken mit Ihrer Datenbank verglichen und ggf. fehlende Felder werden eingefügt. Auch bei diesem Vorgang darf niemand mit dem Programm arbeiten. Wenn die Funktion nicht gelaufen ist (weil jemand vielleicht statt dem Startknopf den Abbruchknopf betätigt hat), so erscheint beim Arbeiten die typische Fehlermeldung 3265. Unsere Hotline wird Sie dann in das Modul Datenbank aktualisieren schicken.

Das Aktualisieren der Datenbanken wird am Anfang nur wenige Sekunden dauern und später bei großen Firmen vielleicht mehrere Minuten.

1. Update einspielen

|

[Bild]

|

Bevor wir auf den Transport des Updates eingehen, beschreiben wir hier erst, wie es eingespielt wird:

1. Starten Sie das Programm Update Aktualsierung.

2. Hier muss zunächst festgelegt werden, wo die Updatedateien liegen. Wahrscheinlich ist vom letzten Mal der Pfad schon passend vorbelegt, wenn nicht befindet er sich meist in der Auswahlliste. Wenn dies nicht der Fall ist, suchen Sie ihn mit dem Knopf ‚Durchsuchen’ heraus. Der Pfad lautet \Labelwin\update\.

3. Mit dem Knopf ‚Start’ wird die Einspielung gestartet, wobei ggf. die Meldung erscheint, dass noch jemand das Programm aktiv hat. Oft genug ist man es selber.

|

Anwender abmelden

Solange ein Anwender im Labelwin angemeldet ist, kann kein Update eingespielt werden. Dies ist besonders ärgerlich, wenn der Mitarbeiter nicht mehr da ist und sich nur vergessen hat, sich abzumelden. Wir haben eine Möglichkeit geschaffen, den Anwender automatisiert abzumelden. Er bekommt dann eine Meldung auf den Bildschirm und hat die Möglichkeit innerhalb von 60 Sekunden zu widersprechen. Wenn er wirklich gerade arbeitet, kann er also den Abmeldevorgang aufhalten. Wenn innerhalb der Zeit kein Widerspruch kommt, werden alle Anwender abgemeldet und das Update kann eingespielt werden.

2. Update per Internet

Alle Labelwin Kunden mit Wartungsvertrag können sich jederzeit ein Programmupdate über das Internet herunterladen.

|

Hinweis: Es muss eine Verbindung zum Internet existieren, da das Internetupdate Programm eine Verbindung ins Internet weder auf noch abbaut.

|

[Bild]

|

Das Update wird über ein eigenes Programmmodul durchgeführt. Starten Sie dazu aus dem Labelwin V5 Programmbaum das Modul "Internet Update". Sollte der Eintrag bei Ihnen fehlen, müssten Sie diesen erst noch über [Optionen - Programmbaum anpassen] einbinden.

|

Es öffnet sich folgendes Fenster:

[Bild]

|

Wenn Sie zunächst nur schauen wollen, was sich geändert hat, so können Sie das über den Knopf ‚Nur Update Info laden’ erreichen.

Klicken Sie auf den Knopf Start oder drücken Sie die F2-Taste. Das Update wird jetzt automatisch heruntergeladen.

Nach Abschluss des Downloads beenden Sie ggf. die Verbindung ins Internet.

Nachdem das Update komplett geladen wurde, erscheint die Frage, ob Sie das Update jetzt sofort einspielen wollen. Wenn Sie JA wählen, so gelangen Sie automatisch in das im vorherigen Abschnitt "Update einspielen" beschriebene Update-Programm. Wir lassen dies jedoch nur zu, wenn das Programm auf keinem Arbeitsplatz aktiv ist. Ggf. starten Sie das Einspielen des Updates zu einem späteren Zeitpunkt manuell.

Mögliche Fehlermeldungen beim Benutzen des Internet Update Programms

Der angemeldete Benutzer xyz ist dem System unbekannt

Das Programm iupd.exe muss im \labelwin\ Verzeichnis auf dem Server bzw. Hauptgerät liegen, dort wo auch alle anderen Labelwin Programm Dateien liegen

Fehler xxx beim Initialisieren des Updates oder

Fehler xxx beim Lesen der Zugangsberechtigung

Wahrscheinlich haben Sie keine korrekte Verbindung ins Internet. Das Internet Update Programm baut keine Verbindung auf oder ab, sondern erwartet eine existierende Verbindung.

Es ist auch möglich, dass der Label Software Internet Server derzeit nicht zur Verfügung steht oder überlastet ist. Probieren Sie es einfach noch einmal.

Download Fehler. Keine Download Berechtigung!

Sie haben keine Berechtigung zum Abholen eines Updates

Das Labelwin Internet Update steht nur Kunden mit einem gültigen Softwarepflegevertrag zur Verfügung.

Sollten Sie der Meinung sein, dass Sie einen gültigen Softwarepflegevertrag haben, so wenden Sie sich bitte an die Label Software Verwaltung unter Tel. 0521-5241960.

Keine neuen Dateien vorhanden!

Das Internet Update Programm prüft vor dem Download nach, wie aktuell Ihre Version ist. Wenn keine neuere Version vorhanden ist, wird auch nichts heruntergeladen.

Fehler xxx beim Download der Setup.lst oder

Die Datei xyz.xxx wurde nicht gefunden oder

Downloadfehler beim Download der Datei xyz.xxx oder

Fehler xxx - die Kontrolldatei xyz.xxx konnte nicht korrekt gelesen werden oder

Das Update Verzeichnis auf dem Labelwin Update Server wurde während des Download erneuert.

Vermutlich wird der Labelwin Update Server gerade mit einem neuen Update erneuert. Warten Sie bitte 15-30 Minuten und versuchen Sie es dann erneut.

Sollte der Fehler wieder auftreten, dann melden Sie es bitte dem Support unter Tel. 0521-5241940, per Fax unter 0521-137680 oder per Email unter service@label-software.de.

Prüfsummenfehler beim Download der Datei xyz.xxx

Vermutlich wird der Labelwin Update Server gerade mit einem neuen Update erneuert. Warten Sie bitte 15-30 Minuten und versuchen Sie es dann erneut.

Möglicherweise ist auch Ihre Internetverbindung zusammengebrochen oder es gab einen Übertragungsfehler. Brechen Sie die Übertragung ab, überprüfen Sie Ihre Internetverbindung und probieren Sie es erneut.

Unerwarteter Fehler beim Internet Download!

Dieser Fehler beruht auf einem Installationsfehler des Internet Update Programms oder das Programm selbst hat einen Fehler.

Bitte starten Sie Ihren Rechner dann neu und probieren Sie es noch einmal. Sollte der Fehler weiterhin auftreten, dann melden Sie es bitte dem Label Software Support unter Tel. 0521-5241940, per Fax unter 0521-137680 oder per Email unter service@label-software.de.
