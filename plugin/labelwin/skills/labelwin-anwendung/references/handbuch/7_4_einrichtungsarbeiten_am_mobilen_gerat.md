# 7.4 Einrichtungsarbeiten am mobilen Gerät

Pfad: Kundendienst > KD-Mobil Notebook [Modul] > 7. Installation und Einrichtungsarbeiten > 7.4 Einrichtungsarbeiten am mobilen Gerät
Quelle: handbuch/7_4_einrichtungsarbeiten_am_mobilen_gerat.htm

|

7.4 Einrichtungsarbeiten am mobilen Gerät

Erstinstallation

[Bild]

Die Installation auf dem Laptop ist (fast) genauso wie eine „normale“ Labelwin-Neuinstallation.

Auf dem mobilen Gerät erfolgt die Installation mit dem Ausführen der Treiberdateien LabelwinSetup.exe und LabelwinSetupZ.exe und anschließend mit dem Start der LabelwinEinricht.exe aus dem Transferverzeichnis. Das Transportverzeichnis befindet sich z.B. auf einem USB-Stick (hier: K:\KD-Mobil Installation\)

Die Labelwineinricht.exe bietet nur die Option „Labelwin Neuinstallation“ an. Bei den Zusatzoptionen wird nur Crystal 10/11 benötigt, wenn im nächsten Schritt noch die V5 Oberfläche installiert wird.

Es wird dringend empfohlen auch die V5 Oberfläche zu installieren. Bitte gehen Sie entsprechend Kapitel KD-Mobil V5 Installation vor.

Nach der Einrichtung startet automatisiert das nächste Modul, mit dem die Datenbanken auf den aktuellen Stand gebracht werden und die Verknüpfung zwischen diesen erzeugt werden. Je nach Einstellung und Freigaben in der Zentrale können Meldungen kommen, die auf dem Laptop nicht relevant sind. Bestätigen Sie diese einfach mit dem Okay-Button.

[Bild]

Anschließend startet automatisch das Programm Grunddaten importieren (kdimnbgr.exe) durch. Es sei denn es sind Fehlermeldungen aufgetreten. Das Programm kann dann aber auch von Hand gestartet werden.

Dieses Programm überträgt die Grunddaten aus der Zentrale in die gerade installierte Version auf dem mobilen Gerät.

|

Info: Dieser Vorgang muss später immer mal wieder erfolgen, wenn sich Grunddaten in der Zentrale geändert haben. Bei der Erstinstallation können wir das Modul automatisch starten, später müssen Sie es ggf. manuell starten.

Tragen Sie zunächst den Pfad ein, in dem die Transportdaten liegen. Wenn möglich, wird dieser schon passend vorgeschlagen.

[Bild]

Bild: Grunddaten importieren

Nach dem Import der Grunddaten arbeiten Sie die nachstehenden Felder der Reihe nach ab.

Nummernkreise:

Hier legen Sie die Nummern für Projekte, Ausgangsrechnungen und Kundendienstaufträge fest. Bitte setzen Sie diese so weit auseinander, dass für jedes Notebook die Nummern keine Überschneidung ergeben. Bei vorangestellter Jahreszahl wird ein Abstand von jeweils 1000 wahrscheinlich und ein Abstand von 5000 garantiert ausreichen. Der getrennte Nummernkreis ist besonders für die Ausgangsrechnungen wichtig.

[Bild]

Da mit Ausnahme des Kundendienstauftrages keine Buchstaben in den Nummernkreisen zulässig sind, empfehlen wir ein Schema von z.B. „99“ + Laptopnummer + „0000“. Im Kundendienstauftrag ist dagegen das Schema „LP“ + Laptopnummer + „0000“ sinnvoll. So erkennt man im Büro direkt, wenn ein Auftrag oder Dokument auf einem mobilen Gerät erzeugt wurde und sogar auf welchem.

Mobile Grundeinstellungen:

Jedes Notebook muss eine andere Nummer erhalten. Im Bild sehen Sie die Einrichtung für Laptop Nummer 1.

Hier muss die gleiche Notebooknummer stehen, die Sie dem Techniker im Modul EINSTELLUNGEN unter dem Menüpunkt <Programmbereiche> <Personal> <Personal erfassen> auf der Zentrale zugeordnet haben.

Wichtig ist das Ankreuzfeld „Auftrag nicht per E-Mail, nur in Verzeichnis kopieren“. Damit legen Sie fest, wie der Transport der Aufträge stattfinden soll. Die Einrichtung der E-Mails für jeden Laptop ist relativ aufwändig, so dass Sie über die Möglichkeit des Cloud-Abgleichs (z.B. per Dropbox) nachdenken sollten. Die Beschreibung dazu finden Sie im nächsten Kapitel Datenaustausch per Cloud.

[Bild]

Falls Ihnen etwas unklar ist, nutzen Sie die kleinen Fragezeichen-Knöpfe hinter den Eingabefeldern.

Zeiten auf dem Laptop nicht löschen

Einige Male erreichte uns der Wunsch, dass die Mitarbeiter ihre auf dem mobilen Gerät gebuchten Zeiten im Nachhinein sehen und kontrollieren wollten.

Mit dieser Option werden bei dem Export von Zeiten diese auf dem Laptop nicht gelöscht. Damit kann der Techniker seine Zeiten auf dem Laptop nachträglich anschauen und ggf. seine Abrechnung kontrollieren.

Dazu steht die bereits aus der Zeitwirtschafft bekannte Anzeige ‚Monatsauswertung Monteur‘ im Hauptmenü zur Verfügung.

Da der Auftrag aber weiterhin gelöscht wird, schreiben wir die wichtigsten Information in den Arbeitstext der Zeitbuchung. Letzteres natürlich nur auf dem Laptop und nicht in den Daten der Zentrale.

Unterschrift Eingabe des Namens erzwingen

Bei der Unterschrift des Kunden mit einem Tablett-Pc oder einem Unterschriftenpad muss man manchmal viel Phantasie haben, um daraus den Namen erkennen zu können. Deshalb gibt es schon lange ein Feld ‚Namen in Buchstaben‘. Dessen Eingabe kann man nun erzwingen.

Druck mit Unterschrift nur bei erledigtem Auftrag

Der Druck eines KD-Auftrages in der mobilen Version kann jetzt so eingerichtet werden, dass er nur möglich ist, wenn der Auftrag zuvor auf den Status 'Erledigt' gesetzt wurde.

Damit wird sichergestellt, dass der Kunde nur einen vollständigen Auftrag unterschreiben kann.

Standardprojekt anlegen:

[Bild]

Nun muss ein Projekt zur Ablage der Kundendienstaufträge und Rechnungen angelegt werden. Mit dem Button starten Sie in die Projektverwaltung. Legen Sie dort ein Projekt mit z.B. dem Namen „Aufträge“ oder „Mobil“ an. Ordnen Sie diesem Projekt unter Vorgaben bitte das „normale“ Erlöskonto zu.

Aktivieren Sie außerdem die Zeitwirtschaft mit der Option „Preisliste aus Adresse“.

KD-Grundeinstellungen:

Tragen Sie danach dieses Projekt als Standardprojekt für den Kundendienst ein. Dies geschieht über den Button „Standardprojekt“ oder in der nachfolgend beschriebenen Maske. In diese Maske müssen Sie ggf. spezielle Eintragungen wie Drucker, Druckformulare usw. einstellen. Die ausführliche Beschreibung dieser Maske finden Sie im hinterlegten Handbuch im Kapitel Einstellungen - Kundendienst.

[Bild]

Wenn der Mitarbeitername in der Rechnung und der Dokumenteninfo passend vorgeschlagen werden soll, so müssen Sie diesen Vorschlag im Modul EINSTELLUNGEN unter dem Menüpunkt <Programmbereiche> <Dokumentenerstellung> <Vorgabe Dokumentenart und Zusatzfelder>. Diese Werte werden nicht aus der Zentrale übertragen.

Rechteverwaltung:

Wenn Sie die Rechteverwaltung auf dem mobilen Gerät aktiveren wollen, um gewisse Funktionen für den Monteur zu sperren, so geschieht dies im Modul EINSTELLUGNEN unter [Optionen - Benutzerrechte vergeben]. Sobald die Rechteverwaltung scharf geschaltet ist, kann der Anwender in der Grunddaten-Import Maske nur noch die Grunddaten erneuern. Über einen Button rechts oben kann allerdings in dieser Maske die Rechteverwaltung kurzfristig deaktiviert werden, um erforderliche Einstellungen vorzunehmen. Dazu ist die Eingabe des Kennwortes erforderlich. Mit Verlassen der EINSTELLUNGEN ist die Rechteverwaltung automatisch wieder aktiv.

Tipp: Die Rechte der Monteure können auch zentral im Büro gepflegt werden, denn die Benutzerrechte Einstellungen werden beim Grunddaten Export mit übertragen. Hierbei ist nur zu beachten, dass im Personalstamm der labelusr Eintrag bei jedem Monteur passend gefüllt ist und dieser labelusr Eintrag in den Benutzerrechte Einstellungen vorhanden ist. Die labelusr Datei wird normalerweise beim Einrichten des Arbeitsplatzes vom Programm generiert. Das geschieht für die KD-Mobil Monteure im Büro natürlich nicht, daher müssen diese Dateien manuell im Labelwin Hauptverzeichnis angelegt werden.

Menüpunkte ausblenden:

Die Kundendienst-Maske lässt sich auf Wunsch weiter einschränken. So lassen sich sogar ganze Menüpunkte ausblenden. Da diese Einschränkungen in der Regel nicht benötigt werden, erfolgt die erforderliche Einrichtung nicht an der Oberfläche, sondern nur über Ini-Schalter. Fragen Sie bei Interesse bei der Labelwin-Hotline oder Ihrem Label-Partner nach.

|

V5 Oberfläche:

Die wichtigsten Einrichtungsarbeiten für KD-Mobil sind nun erfolgt. Es fehlt jetzt nur noch die V5 Oberfläche, die mit einer gesonderter Installationsroutine aufgerufen wird. Gehen Sie dazu einfach in den „v5inst“-Ordner des Installationsverzeichnisses (in unserem Beispiel D:\KDMOBIL Transfer\v5inst\) und starten die Dateien vcredist_x86.exe und anschließend die setup.exe. Details finden Sie in Kapitel KD-Mobil V5 Installation.
