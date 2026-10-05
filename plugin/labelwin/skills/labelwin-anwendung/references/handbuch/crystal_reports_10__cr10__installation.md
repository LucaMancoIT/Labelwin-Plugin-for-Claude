# Crystal Reports 10 (CR10) Installation

Pfad: Installation und Wartung > Crystal Reports 10 (CR10) Installation
Quelle: handbuch/crystal_reports_10__cr10__installation.htm

|

Crystal Reports 10 (CR10) Installation

(Drucken von formatierten RTF Texten und Bildern)

Systemvoraussetzungen

Betriebssystem/Computer

Die CR10 Treiberprogramme funktionieren nur auf Rechnern mit dem Betriebssystem Windows 2000, Windows XP oder höher. Rechner mit den Betriebssystemen Windows 95/98/Me und Windows NT können nicht umgestellt werden.

|

Hinweis: Nach der Umstellung des Labelwin Programmes kann auf Arbeitsplätzen mit den alten Betriebssystemen nicht mehr aus Labelwin heraus gedruckt werden!

Report Dateien

Um die formatierten Texte und Bilder in Dokumenten (Angebote, Rechnungen etc.) drucken zu können, benötigen Sie neue Standard Formulardateien bzw., wenn diese speziell angepasst wurden, neue angepasste Formulare. Speziell angepasste Formulare erkennen Sie daran, dass das Dateidatum der RPT-Datei nicht von 1980 ist.

Die neuen RTF-fähigen „Standardformulare“ finden Sie auf der Labelwin CD im Unterverzeichnis \inst32\RTF\. Die einzelnen Unterverzeichnisse haben folgende Bedeutung:

Endlos: Seite 1 und alle folgenden Seiten von Rechnungen und Angeboten sind identisch, d.h. es ist immer der komplette Briefkopf auf dem Papier.

Standard: Der Briefkopf ist nur auf Seite 1, alle Folgeseiten drucken auf weißes Papier.

UntenEB: Wie Standard, aber der Block mit den Nummern, Datum, Bearbeiter sind nicht rechts von der Adresse, sondern unter der Adresse. Für Briefköpfe, die rechts neben der Adresse schon bedruckt sind.

UntenEnd: Wie Endlos, aber der Block mit den Nummern, Datum, Bearbeiter sind nicht rechts von der Adresse, sondern unter der Adresse.

|

Hinweis: Die Umstellung der angepassten Formulare auf RTF wird vom Label Support durchgeführt, ist kostenpflichtig und wird nach Aufwand berechnet. Im Normalfall kann man mit Kosten zwischen 150,00 € und 250,00 € rechnen.

Die angepassten Reports müssen in das Labelwin Reportverzeichnis kopiert werden.

Crystal Report Designer

Um Report Dateien ggf. selber zu verändern, benötigen Sie das Programm Crystal Report Version 10.

Die Reports werden durch die Reportaktualisierung ins Version 10 Format gewandelt bzw. wenn man sie mit Crystal 10 öffnet und wieder speichert. Crystal Report Version 10 kann keine Reports in den älteren Versionen 9, 8.x oder 7 speichern. D.h. einmal in Version 10 gewandelte Report (.RPT) Dateien, können nicht mehr mit den älteren Versionen von Crystal Report geöffnet werden.

Die Crystal Report Designer der Versionen 7 bis 9 können nicht mehr benutzt werden!

Allgemeines zur Installation

Machen Sie vor der Installation eine komplette Datensicherung!

Starten Sie das Modul Update Aktualisierung. Wählen Sie ‚Diesen Arbeitsplatz einrichten/erweitern’ und aktivieren Sie ‚Crystal 10/11 für SQLServer/RTF’.

Bei der Installation wird ein Windows Installations-Programm gestartet.

Dieses meldet sich im nächsten Fenster, je nachdem, ob es zum ersten oder zum wiederholten Male läuft. Beim wiederholten Aufruf bietet es statt ‚Installieren’ die Optionen ‚Reparieren’ und ‚Entfernen’. Bitte wählen Sie ‚Reparieren’.

[Bild]

Auch wenn es die Möglichkeit zum Deinstallieren/Entfernen gibt, so raten wir davon ab. Die Deinstallationsroutine funktioniert, wie fast alle Windows Deinstallationsprogramme, nicht richtig. Außerdem können einmal nach CR10 umgewandelte Reports nicht mehr in eine vorherige Version gewandelt werden.

Für alle Installationsprogramme benötigen Sie Administratorrechte!

Aktuelle Programmversion aus dem Internet

Zur Installation benötigen Sie eine aktuelle Programmversion. Auf unserem Internetupdate Server befindet sich aus organisatorischen Gründen nicht die notwendigen 24 MB und 48 MB großen Installationsdateien namens cr10inst.msi und cr11inst.msi. Diese Versionen haben Sie mit der letzten CD Update eingespielt.

Wenn die aktuelle Version nicht vorhanden ist, wird das Installationsprogramm versuchen, dieses aus dem Internet herunter zu laden. Sie benötigen dazu eine Internetverbindung und eine ggf. installierte Firewall muss dem Programm Zugang ins Internet erlauben.

Installation Einplatzanlage

Melden Sie sich unter Windows mit einem Benutzernamen an, der Administratorrechte hat. Es muss nicht der Anmeldename sein, mit dem Sie sich der Anwender normalerweise anmeldet.

Starten Sie das Modul Update Aktualisierung. Wählen Sie ‚Diesen Arbeitsplatz einrichten/erweitern’ und aktivieren Sie ‚Crystal 10/11 für SQLServer/RTF’.

Es startet ein Windows Installationsprogramm für die Labelwin Crystal 11 Treiber.

[Bild]

Klicken Sie auf „Installation“. Nach wenigen Minuten erscheint der Knopf „Fertig“, der das Windows Installationsprogramm beendet. Danach erfolgt analog die Installation der Crystal 10 Treiber.

Am Ende werden Sie gefragt, ob Sie die Reports jetzt oder später aktualisieren möchten. Wir empfehlen Ihnen, es sofort zu machen. Der Vorgang dauert je nach Rechner und Anzahl Reports zwischen 20 Minuten und 2 Stunden.

Achtung! Die Reports können nicht wieder auf die alte Version zurückgesetzt werden. Sie sollten Ihr Report-Verzeichnis vorher sichern!

Wenn Sie die Reports später aktualisieren möchten, so starten Sie das Labelwin Modul EINSTELLUNGEN und wählen den Menüpunkt <Programmbereiche> <Druckausgabe> <Reports aktualisieren> und dort dann ‚alle Reports’.

Installation im Netzwerk

Im Netzwerk muss die Installation auf allen Labelwin Arbeitsplätzen erfolgen. Eine Installation auf dem Server ist nur dann notwendig, wenn auf dem Server selbst auch mit Labelwin gearbeitet.

Eine Installation kann also auch erfolgen, wenn der Server unter dem Betriebssystem Linux läuft.

Folgender Vorgang muss auf allen Arbeitsplätzen durchgeführt werden:

Melden Sie sich unter Windows mit einem Benutzernamen an, der Administratorrechte hat und für Labelwin eingerichtet ist.

Starten Sie das Modul Update Aktualisierung. Wählen Sie ‚Diesen Arbeitsplatz einrichten/erweitern’ und aktivieren Sie ‚Crystal 10/11 für SQLServer/RTF’.

Es startet ein Windows Installationsprogramm für die Labelwin Crystal 11 Treiber. Klicken Sie auf „Installation“. Nach wenigen Minuten erscheint der Knopf „Fertig“, der das Windows Installationsprogramm beendet. Danach erfolgt analog die Installation der Crystal 10 Treiber.

Nur am Ende der Installation des ersten Rechners werden Sie gefragt, ob Sie die Reports jetzt oder später aktualisieren möchten. Wir empfehlen Ihnen, es sofort zu machen. Der Vorgang dauert je nach Rechner und Anzahl Reports zwischen 20 Minuten und 2 Stunden.

Achtung! Die Reports können nicht wieder auf die alte Version zurückgesetzt werden

Wenn Sie die Reports später aktualisieren möchten, so starten Sie das Labelwin Modul EINSTELLUNGEN und wählen den Menüpunkt <Programmbereiche> <Druckausgabe> <Reports aktualisieren> und dort dann ‚alle Reports’.

Installation Windows Terminal Server / Citrix

Melden Sie sich in einer Terminal Server Client Session oder direkt am Terminalserver als Administrator an oder als ein Benutzer mit Domänen-Administrator Rechten.

Starten Sie das Modul Update Aktualisierung. Wählen Sie ‚Diesen Arbeitsplatz einrichten/erweitern’ und aktivieren Sie ‚Crystal 10/11 für SQLServer/RTF’.

Es startet ein Windows Installationsprogramm für die Labelwin Crystal 11 Treiber. Klicken Sie auf „Installation“. Nach wenigen Minuten erscheint der Knopf „Fertig“, der das Windows Installationsprogramm beendet. Danach erfolgt analog die Installation der Crystal 10 Treiber.

Am Ende werden Sie gefragt, ob Sie die Reports jetzt oder später aktualisieren möchten. Wenn Sie mit einem Namen angemeldet sind, der für Labelwin eingerichtet ist, empfehlen wir Ihnen, es sofort zu machen. Der Vorgang dauert je nach Rechner und Anzahl Reports zwischen 20 Minuten und 2 Stunden.

Achtung! Die Reports können nicht wieder auf die alte Version zurückgesetzt werden.

Wenn Sie die Reports später aktualisieren möchten, so starten Sie das Labelwin Modul EINSTELLUNGEN und wählen den Menüpunkt <Programmbereiche> <Druckausgabe> <Reports aktualisieren> und dort dann ‚alle Reports’.

Auf den weiteren Arbeitsplätzen, die sich über eine Terminal Server Session anmelden, müssen Sie nichts weiter machen. Die Umstellung ist abgeschlossen.

Für weitere User müssen Sie im Labelwin folgenden Schalter setzen. Starten Sie im Modul EINSTELLUNGEN den Menüpunkt <Optionen> <ini-Dateien bearbeiten>. Drücken Sie die Funktionstaste F2. Es öffnet sich das Notepad. Tragen Sie unter [Grundeinstellungen] CR10=1 ein.

Wenn im Netzwerk noch Arbeitsplätze sind, die sich nicht über eine Terminal Server Session, sondern über eine Netzwerkverbindung anmelden, verfahren Sie bei diesen wie bei einer normalen Netzwerkinstallation.

Drucken von Bildern

Um Bilder in Dokumenten (Angebote, Rechnungen, etc.) drucken zu können benötigen Sie auf allen Rechnern ein ‚Ole-fähiges’ Bildbearbeitungsprogramm. Die mit Windows und Office mitgelieferten Bildbearbeitungsprogramme sind im Normalfall nicht OLE-fähig.

Auf der Labelwin CD befindet sich im Unterverzeichnis \inst32\psp5inst\ ein Setup Programm für das Shareware Programm Paint Shop Pro, welches Ole-fähig ist. Sie können es problemlos auf Ihren Rechnern installieren. Am Ende der Installation werden Sie gefragt, welche Bilddateien mit PSP verknüpft werden sollen, d.h. bei welchen Bilddateien öffnet sich per Doppelklick auf die Datei das Programm PSP.

Bitte wählen Sie entweder ‚Alle’ aus oder zumindest die Bildtypen, die Labelwin verarbeiten kann. Das sind: BMP, JPG, JPEG, GIF, TIF, TIFF, PNG und DIF

Beim Aktivieren der Bildbearbeitung wird geprüft, ob ein ‚Ole-fähiges’ Bildbearbeitungsprogramm für die einzelnen Bildtypen installiert ist und warnt gegebenenfalls (lesen Sie hierzu bitte Seite 5).

In der Druckenmaske ist standardmäßig ein Häkchen gesetzt bei ‚Ausdruck ohne Bilder’. Dieses müssen Sie entfernen, sonst werden Ihre Dokumente wie bisher ausgedruckt.

[Bild]
