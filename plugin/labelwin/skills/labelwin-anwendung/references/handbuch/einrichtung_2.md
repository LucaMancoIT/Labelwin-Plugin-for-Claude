# Einrichtung

Pfad: Label Mobile > Einrichtung
Quelle: handbuch/einrichtung_2.htm

|

Einrichtung

Die Einrichtungsarbeiten umfassen die Aktivierung des Label Mobile Web-Services, das Freigaben des Personals, die Rechteverwaltung und Sonstiges.

Label Mobile Service

|

Im Büro muss auf einem Gerät der Label Mobile Service laufen. Dieser nimmt die Anfragen der App-Benutzer entgegen und beantwortet sie. Dadurch sind die Daten immer aktuell, also in Echtzeit.

Label Mobile läuft ab der Labelwin Version 5.89.19.0412. Für die Benutzung benötigen Sie eine Label Mobile Lizenz und somit eine neue Freigabe-Datei („global.zip“) die Sie per E-Mail bekommen. Spielen Sie diese über das Modul „Einstellungen“ und dem Menüpunkt <Optionen>, <Freigabe entpacken> ein.

Starten Sie danach den Service über den

Menüpunkt <Optionen><Label Mobile Service automatisch starten> im Startcenter.

Dieser Service muss ständig auf einem beliebigen Arbeitsplatz oder auf dem Server laufen.

|

[Bild]

Es kommt eine Meldung, die entweder sagt, dass der Service bereits läuft (inkl. auf welchen Rechner und mit welchem Login) oder dass er jetzt gestartet werden kann. Beim Starten des Service wird gefragt, ob mit oder Lizenzverbrauch gestartet werden soll.

[Bild]

Auf dem Server kann es ohne Lizenzverbrauch sein, dann kann man mit Labelwin dort nicht arbeiten, sondern es bedient nur die App. Bei der Option ‚.. als normaler Arbeitsplatz‘ können Sie auf diesem Platz ganz normal arbeiten. Die Anfragen der App werden im Hintergrund abgearbeitet, ohne dass dies das Tempo beeinflusst.

Startet man den Service, obwohl er bereits woanders läuft, dann wird der andere abgeschaltet, so dass es immer nur EINEN aktiven Service geben kann.

Ob der Service läuft, können Sie jederzeit und von jedem Rechner aus über den Menüpunkt <Info><Info> erfahren.

Wenn Sie die mobilen Daten jederzeit zur Verfügung haben wollen, müssen Sie labelwin immer aktiv haben. Nur zum Update müssen Sie es schließen und dann wieder starten.

Personal

Jeder Mitarbeiter, der per App Label Mobile nutzen möchte, muss in der Personaltabelle angelegt und freigegeben sein. Starten Sie die Personalverwaltung im Modul „Einstellungen“ unter <Programmbereiche>, <Personal>, <Personal erfassen>.

[Bild]

-

Setzen Sie den Haken bei „Label Mobile nutzen“ (Reiter „Allgemein“)

-

Wählen Sie ein Paket aus. „Basis“ oder „Profi“. Bitte bedenken Sie, dass Sie ausreichend Basis bzw. Profi App-Lizenzen erworben haben müssen

-

Merken Sie sich die „Identnummer“. Diese benötigt der Mitarbeiter zum Einloggen

-

Hinterlegen Sie oben drüber ein Passwort

-

Achten Sie darauf, dass dem Mitarbeiter ein „Label-User“ zugeordnet ist. Darüber werden die Rechte gelesen. Sie müssen dem Mitarbeiter also auch in der Rechteverwaltung entsprechend anmelden.

-

Speichern Sie die Daten

Der Mitarbeiter kann ab sofort mit der App arbeiten.

Rechteverwaltung und Sicherheit

Bei der Nutzung von Label Mobile sollten Sie unbedingt die Rechteverwaltung aktivieren, wenn der Chef / die Chefin nicht der einzige Anwender ist. Bei allen Abfragen werden nur die Daten geliefert, für die der Anwender frei geschaltet ist.

Auf jeden Fall sollten Sie Ihr Handy mit einem Code versehen, da die App ja nur einmalig die Anmeldedaten abfragt.

Sonstiges

Zwangsabmelden bzw. Liste der aktiven Benutzer

Jeder Mitarbeiter kann gleichzeitig auf 2 Geräten (z.B. Handy und Tablet) angemeldet sein. Beim Versuch sich auf einem dritten Gerät anzumelden kommt die Meldung „Zu viele Benutzer gleichzeitig autorisiert.“ Der Mitarbeiter muss sich entweder auf einem eingeloggten Gerät abmelden oder Sie können ihn über das Labelwin Modul „Einstellungen“, Menüpunkt <Mobil>, <Label Mobile> zwangsabmelden. Wechseln Sie auf den Reiter „Benutzer“. Dort sehen Sie alle angemeldeten Label Mobile Benutzer mit Namen, Gerätename sowie Datum und Uhrzeit der letzten Aktivität. Nach dem Abmelden bekommt der Benutzer wieder die Login-Maske.

Protokoll, Suffix, Webserver

Über das Labelwin Modul „Einstellungen“, dem Menüpunkt <Mobil>, <Label Mobile> und dem Reiter „Einstellungen“ können Sie für Prüfzwecke ein „Technisches Protokoll“ aktivieren. Nach 2 Tagen wird es automatisch wieder abgeschaltet. Über den Knopf „Protokoll öffnen“ können Sie es einsehen.

Außerdem können Sie hier die 5-stellige Labelwin Lizenznummer um ein zweistelliges Suffix erweitern. Standardmäßig lautet das Suffix „01“. Das Suffix wird nur benötigt, wenn verschiedene Instanzen von Labelwin in verschiedenen Verzeichnissen oder auf verschiedenen Rechnern mit derselben Lizenznummer installiert ist. Das ist z.B. der Fall, wenn Sie für Schulungszwecke eine Testinstallation auf einem Laptop haben. Diese benötigt unbedingt ein anderes und eindeutiges Suffix. Das Suffix müssen Sie sich aber erst über den Label-Support freischalten lassen. Labelwin Anwender die eine Mandantenversion betreiben, benötigen KEIN weiteres Suffix. Die Mandantenzuordnung erfolgt über den Benutzer, der im Personalstamm einen Mandanten zugeordnet ist und ggf. auch die Berechtigungen für die anderen Mandanten hat.

Wenn Sie den Datentransfer nicht über unseren Label Mobile Webserver laufen lassen möchten, sondern einen eigenen Server betrieben möchten, dann können Sie hier die Adresse des eigenen Servers angeben. Diese muss dann auch im ersten Feld der Login-Maske eingetragen werden. Selbstverständlich müssen Sie auch auf dem Webserver ein PHP7-Programm installieren, welches Sie kostenpflichtig vom Label-Support bekommen können.

Mögliche Fehlermeldungen

Der Dienst konnte nicht erreicht werden! (996)

Das meldet die App, wenn der Label Mobile Service nicht gestartet wurde
