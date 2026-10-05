# 10.1 Einlesen der Auszüge

Pfad: Buchhaltung > Fibuerfassung [25] > 10. Kontoauszugsmanager [Modul] > 10.1 Einlesen der Auszüge
Quelle: handbuch/10_1_einlesen_der_auszuge.htm

|

10.1 Einlesen der Auszüge

Bevor Sie Auszüge einlesen können müssen diese erst mal erzeugt werden. Wie dies geschieht ist von dem verwendeten Bankprogramm abhängig.

Einstellen der Verarbeitungsart

Zusätzlich müssen Sie dafür sorgen, dass bei den Bankdaten im Modul EINSTELLUNGEN unter dem Menüpunkten <Programmbereiche> <Eingangsrechnungen> <Bankdaten> das richtige Bankprogramm eingestellt ist.

[Bild]

Mit den Bankprogrammen kann man die Datei in einem x-beliebigen Verzeichnis auf der Festplatte ablegen. Wir schlagen vor, dass Sie dazu ein Verzeichnis AUSZUG unter dem Verzeichnis \Labelwin anlegen und die Auszüge dort ablegen. Damit ist (hoffentlich) sichergestellt, dass sie mit gesichert werden.

Kontoführung im Internet:

Hier finden Sie in der Anzeigemaske der Kontoauszüge oft einen Knopf ‚Daten exportieren’, mit dem Sie die Auszüge irgendwo auf der Festplatte speichern können. In diesem Fall ist der Aufbau der Daten nicht zu beeinflussen.

Kontoführung mit Sfirm:

Bei Bankprogrammen wie Sfirm wird über eine Steuerdatei geregelt, in welcher Reihenfolge die Informationen in die Übergabedatei geschrieben werden. Hierzu benötigen Sie bei Sfirm die Steuerdatei ‚Label.scr’. Diese muss in dem Verzeichnis ‚\sfirm32\transfer’ liegen. Die Datei ist auf allen Auslieferungs-CD’s und Update-CD’s, seit dem 10.01.2003 im Verzeichnis ‚inst32\diverses’ zu finden.(Achtung ! nach dem Kopieren der Datei von der CD in den Ordner \sfirm32\transfer ist die Label.scr schreibgeschützt, Schreibschutz mit Explorer entfernen.

Bei ‚SFirm32’ handelt es um eine Sonderversion des Sparkassenprogramms, bei dem unsinnigerweise die Auszüge in falscher Reihenfolge ankommen.

Abgesehen von Sfirm und Windata können Sie (fast) alle Auszugsdaten über die Steuerdatei einlesen. Das ‚fast’ deshalb, weil es vielleicht auch Daten gibt, die so überhaupt nicht zu verarbeiten sind.

Wenn Sie mit einer Steuerdatei arbeiten (müssen), so sind zuvor einige Einrichtungsarbeiten erforderlich. Lesen Sie dazu bitte im Kapitel 25.10.4 nach.

Zum eigentlichen Abholen der Auszüge müssen Sie nun in Ihrem Bankprogramm die entsprechenden Menüpunkte anwählen. Für das Programm SFirm32 haben wir dies im Kapitel 25.10.5 ausführlich dokumentiert.

Wichtig ist beim Abholen, dass Sie eine Eingrenzung auf einen Buchungstag vornehmen. Am Besten holen Sie immer die Daten des Vortages ab und noch nicht die Daten des aktuellen Tages. Wenn Sie nämlich die Auszüge von heute schon mit abholen, so kann es passieren, dass bei weiteren Auszügen am heutigen Tage am nächsten Tag doppelt kommen oder einige fehlen (je nach Datumseingrenzung). Dadurch, dass man bei Sfirm nur auf den Tag eingrenzen kann und nicht auf Auszugsnummern, kämen die bereits abgeholten Auszüge erneut rüber. Das darf nicht sein.

Bevor Sie Daten einlesen und verarbeiten können, müssen Sie in Labelwin exakt den gleichen Kontostand des Bankkontos haben, wie in den Übergabedaten. Nur dann lassen wir das Einlesen der Auszüge zu.

Wählen Sie den Menüpunkt <Belege> <Auszugsdatei einlesen> an.

[Bild]

Bei Pfad und Dateiname müssen Sie selbstverständlich die Daten angeben, in denen das Bankprogramm die Auszüge abgelegt hat. Wenn Sie unserem Vorschlag gefolgt sind ist dies …labelwin\auszug.

Die Auszugs-Nr. ist nicht wirklich wichtig – sie wird lediglich bei den Daten im Labelwin hinterlegt, so dass Sie neben den eigentlichen Daten auch die Auszugsnummer sehen können. Unsere Empfehlung ist, das Tagesdatum einzusetzen, an dem Sie die Daten abholen. Noch einmal zur Wiederholung: Es empfiehlt sich nur die Daten bis einschließlich des Vortages zu holen.

Bei manchen Bankprogrammen kommen die Kontobewegungen in der falschen Reihenfolge, also die letzte Bewegung als erstes. Wenn Sie Tagesweise abholen ist das nicht schlimm, aber Sie können mit dem Ankreuzfeld die Reihenfolge beim Einlesen drehen.

Über das Menü gelangen Sie in den Bereich, eine Steuerdatei zum Einlesen der Auszüge zu erstellen. Lesen Sie dazu bitte im Kapitel 25.10.5 nach.

Nach Bestätigen des Okay-Knopfes werden die Daten in Labelwin in eine Zwischentabelle übertragen. Bei der späteren Buchung wird diese Zwischentabelle Buchung für Buchung abgearbeitet.

[Bild]

Kontenverwendung anpassen: Es kann passieren, dass beim Einlesen der Auszüge eine Verwendungsart gefunden wird, die bisher in unserem Programm nicht zugeordnet ist. Bei einer bisher dem Programm nicht bekannten Verwendungsart erscheint ein Hinweis darauf, und Sie müssen lediglich festlegen, ob es sich um eine Kundenzahlung oder eine x-beliebige andere Buchung handelt. Nur die Kundenzahlungen müssen über die Buchungsart erkannt werden. Das Programm speichert diese Festlegung und wird in Zukunft nicht mehr fragen.

Mögliche Fehlermeldung: Wenn möglich, wird der aktuelle Saldo in der Fibuerfassung mit dem Kontensaldo verglichen. Wenn der Auszug nicht zu den bisherigen Daten im Rechner passt, wird das Einlesen abgewiesen. Auf dem abgeholten Auszug ist der Konto-Anfangsbestand eingetragen, der exakt mit dem gebuchten Kontenstand bei Labelwin über einstimmen muss. Das heißt, bei dieser Meldung haben Sie entweder die Auszüge falsch abgeholt oder es haben schon Buchungen stattgefunden, die in den abgeholten Auszügen auch enthalten sind.

[Bild]

Falls Sie mit einer Steuerdatei arbeiten (müssen), so kann es sein, dass in Ihren Auszügen keine Anfangs- und Endbestand hinterlegt ist. In diesem Fall erfolgt lediglich der Hinweis, wie der aktuelle Kontenstand ist, und die Daten werden ohne Prüfung eingelesen.
