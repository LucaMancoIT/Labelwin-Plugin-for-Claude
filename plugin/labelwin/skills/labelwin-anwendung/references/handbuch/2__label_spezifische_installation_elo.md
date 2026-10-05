# 2. Label-spezifische Installation ELO

Pfad: Archivierung > ELO Dokumentenarchivierung [Modul] > 2. Label-spezifische Installation ELO
Quelle: handbuch/2__label_spezifische_installation_elo.htm

|

2. Label-spezifische Installation ELO

Die Installation von Elo muss zunächst so erfolgen, wie dies im Elo-Handbuch beschrieben ist. Wenn Sie Elo im Netzwerk betreiben wollen, so muss der Archivpfad selbstverständlich auf ein Netzwerkverzeichnis zeigen, dass für alle Nutzer gleich sein muss. Falls Sie keine Komplettsicherung des Servers vornehmen, sollten Sie diesen Pfad unbedingt in Ihre Datensicherung einbeziehen.

Anlegen des neuen Archivs

Nachdem die Elo - Grundinstallation wie im Handbuch beschreiben, durchgeführt wurde, muss ein Archiv angelegt werden, das mit Label korrespondiert. Hierzu legen Sie bitte im Elo ein neues Archiv an.

[Bild]

Sollten Sie schon mit Elo arbeiten, so können Sie Ihr bisher verwendetes Archiv weiter benutzen.

Nachdem Sie die Maske mit OK bestätigt haben, müssen Sie dem Archiv einen Name geben.

[Bild]

Mit der Bestätigung legt Elo nun ein neues Archiv an.

Importieren der Masken

Um später Eintragungen im Elo von Labelwin aus automatisch verschlagworten zu können, müssen bestimmte Masken vorhanden sein. Diese Masken können entweder von Hand angelegt werden oder in das aktive Archive importiert werden. Wir empfehlen die Importmethode, da dort Schreibfehler ausgeschlossen sind.

Das importierte Archiv wird später wieder gelöscht und die Verschlagwortungsmasken bleiben erhalten.

Die entsprechenden Importdaten befinden sich auf der mitgelieferten Labelwin-CD im Verzeichnis ‚\inst32\eloinst\EloMuster’.

Wählen Sie nun den Menüpunkt <Eloe> <Datenaustausch> <Import>

Es erscheint folgende Maske:

[Bild]

Als Quelle geben Sie nun Ihr CD-Laufwerk und das Verzeichnis \inst32\Eloinst\ELOMuster an. In dem Feld ‚Gefunden’ muss dann ein Aktenschrank ‚test1’ zu sehen sein.

Danach können Sie bereits den Knopf ‚Fertigstellen’ anwählen. Elo wird nun den Aktenschrank ‚test1’ anlegen und 3 Dokumente importieren.

Danach müssen Sie die Frage beantworten, ob Sie den Volltextindex jetzt aufbauen wollen. Diese beantworten Sie mit (Falls Sie irrtümlich JA anwählen schadet es auch nicht)

[Bild]

Die Kontrollmaske des Importassistenten beenden Sie dann mit ‚Abbrechen’

Löschen des Test1-Aktenschrankes

Jetzt muss nur noch der Test1-Aktenschrank gelöscht werden. Markieren Sie den Aktenschrank, indem Sie ihn einmal anklicken. Danach wählen Sie im Menü <Start> <Löschen> und bestätigen die Sicherheitsabfrage mit ‚Ja’

[Bild]

Anlegen einer speziellen Suchmaske

Neben den importierten Verschlagwortungsmasken muss mindestens eine Suchmaske angelegt werden, damit eine einfache Verbindung zu dem Label-Adressprogramm erstellt werden kann. Diese Maske kann leider nicht automatisch mit importiert werden. Diese Suchmaske muss mit genau den unten aufgeführten Daten erstellt werden. Achten Sie unbedingt auf die Gross-Kleinschrift.

Wählen Sie den Menüpunkt <Elo> <Systemeinstellungen> <Verschlagwortungsmasken> an. In diesem Bild betätigen Sie den Knopf ‚Neue Maske’

Geben Sie den Namen Label-Suche ein. Achten Sie bitte unbedingt auf Groß-/Kleinschrift!

[Bild]

Im Folgenden müssen Sie die Maske exakt so ausfüllen, wie wir es beschreiben. Achten Sie unbedingt wieder auf die Groß / Kleinschrift. Um Ihnen die Eingaben zu erleichtern haben wir einen Kreis um die zu ändernden Felder gezogen.

[Bild]

Falls Sie versehentlich einmal die Entertaste betätigen, wird die Maske gespeichert und geschlossen. Gehen Sie dann einfach erneut über das Menü an diesen Punkt und betätigen den Knopf ‚Auswählen’. Wählen Sie dann die Suchmaske ‚Label-Suche’ und Sie können die weiteren Eingaben vornehmen.

Die obige Maske enthält viele Karteiseiten, von denen Sie insgesamt 7 ausfüllen müssen. Die erste Seite ist nach obiger Anleitung fertig. Wählen Sie nun nacheinander die weiteren 6 Karteiseiten an und füllen sie diese aus.

[Bild]

Falls Sie es so schneller ausfüllen können sind hier alle Eingabefelder in einer Tabelle dargestellt.

|

Nr

|

Index Feld

|

Gruppe

|

Min

|

Max

|

Typ

|

Zugriffsart

|

Verschl

|

Lasche

|

Stich- wort

|

vor

|

nach

|

1

|

Name

|

ADRRG

|

0

|

0

|

Txt

|

Normal

|

System

|

|

|

X

|

X

|

2

|

Adressnr alle

|

ADRNRALLE

|

0

|

0

|

Txt

|

Normal

|

System

|

|

|

X

|

X

|

3

|

Adressnr 1

|

ADRNR1

|

0

|

0

|

Txt

|

Normal

|

System

|

|

|

X

|

X

|

4

|

Adressnr 2

|

ADRNR2

|

0

|

0

|

Txt

|

Normal

|

System

|

|

|

X

|

X

|

5

|

Adressnr 3

|

ADRNR3

|

0

|

0

|

Txt

|

Normal

|

System

|

|

|

X

|

X

|

6

|

SCANKD

|

KDID

|

0

|

0

|

Txt

|

Normal

|

System

|

|

|

|

|

7

|

VDMA Ebene

|

VDMAEBENE

|

0

|

0

|

Txt

|

Normal

|

System

|

|

|

|

Die weiteren Masken:

[Bild]

[Bild]

[Bild]

[Bild]

[Bild]

[Bild]

Anlegen eines Scripts zur Verschlagwortung durch Labeldaten

Um die Eintragung und Verschlagwortung von Dateien mit Labeldaten nicht nur von Labelwin aus anstoßen zu können, haben wir ein kleines Programm entwickelt, dass von Elo aus gestartet werden kann. Die Einbindung von Programmen erfolgt im Elo über sogenannte Scripte.

Für die Ablage von Elo aus gibt es im Prinzip 5 Möglichkeiten:

1. Sie bauen sich eine eigene Verschlagwortungsmaske und legen einige Dokumente völlig unabhängig von Labelwin an. Verständlicherweise können Sie diese dann über Labelwin nicht finden, sondern nur im Elo.

2. Sie verwenden die Labelwin-Adressen und Verschlagwortungsmaske, legen aber in Labelwin keinen Dokumenteneintrag an. Solche Dokumente können Sie über Labelwin nur über die Adressverwaltung unter dem Menüpunkt <ELO Anzeige> <Alle Dokumente> finden.

3. Sie tragen das Dokument im Elo und im Labelwin ein. Dazu benutzen Sie die im Elo eingebundene Anlagemaske von Labelwin. Damit stehen im Labelwin alle Suchmöglichkeiten zur Verfügung – genauso als wenn Sie die Einbindung von Labelwin aus gestartet hätten. Diese Funktion wird benötigt, wenn an zentraler Stelle gescannt wird und der Benutzer ‚seine’ Dokumente selber einbinden möchte.

4. Anlegen eines Kundendienstauftrages

5. Ablegen von Eingangsrechnungen, die als PDF-Datei vorliegen

Für alle diese Möglichkeiten müssen Sie nun die Scripte einbinden.

Script 1

Im Elo muss unter dem Menüpunkt <Systemverwaltung> <Script> ein neues Script mit dem Namen ‚Labelablage‘ angelegt werden. Hier zu wird der Knopf ‚Neues Script’ an gewählt und der Name des Scripts erfasst.

[Bild]

Das Script könnte zwar auch von Hand angelegt werden, aber um es einfacher zu machen, ist es auf der CD abgelegt. Es befindet sich in der Datei \inst32\eloinst\sonstig\suchscript.txt .

Dort sind allerdings 5 Scripte abgelegt. Kopieren Sie zunächst den ersten Block in die Zwischenablage und fügen Sie ihn so wie im folgenden Bild ein.

[Bild]

Hier noch einmal der Text des Scripts:

Set Elo=CreateObject("ELO.office")

elo.doExecuteEx "c:\labelwin\eloablag.exe","1","c:\labelwin\","",-1

Der Pfad ‘C:\labelwin’ muss durch den auf dem entsprechenden System gültigen Labelwin-Pfad ersetzt werden. Dies kann im Peer to Peer-Netz ggf. problematisch sein, da der Pfad für alle Nutzer identisch sein muss. In diesem Fall tragen Sie bitte den sogenannten UNC-Pfad ein (//Computername/... )

Dieses Script wird durch den Knopf ‚Speichern’ auf der rechten Seite gespeichert. Eventuell kommt die Frage, ob es auch lokal gespeichert werden soll. Die Entscheidung ist im Prinzip egal – wählen Sie einfach NEIN.

Script 2

Nun muss ein weiteres Scipt mit dem Namen ‚Label neues Dokument’ angelegt werden. Der Inhalt dieses Scriptes ist:

Set Elo=CreateObject("ELO.office")

elo.doExecuteEx "c:\labelwin\eloablag.exe ","2","c:\labelwin\","",-1

Achtung: Der einzige Unterschied zum ersten Script ist die Stelle mit ‚1‘ und ‚2‘.

Script 3

Das dritte Scipt wird mit dem Namen ‚Label Dokumentzuordnung’ angelegt. Der Inhalt dieses Scriptes ist:

Set Elo=CreateObject("ELO.office")

elo.doExecuteEx "c:\labelwin\eloablag.exe ","3","c:\labelwin\","",-1

Achtung: Der einzige Unterschied zum ersten Script ist die Stelle mit ‚1‘ und ‚3‘.

Script 4

Das vierte Scipt wird mit dem Namen ‚Label KD-Auftrag’ angelegt. Der Inhalt dieses Scriptes ist:

Set Elo=CreateObject("ELO.office")

elo.doExecuteEx "c:\labelwin\kdeinzel.exe ","ELOKD=1","c:\labelwin\","",-1

Script 5

Das fünfte Scipt wird mit dem Namen ‚Label Eingangsrg’ angelegt. Der Inhalt dieses Scriptes ist:

Set Elo=CreateObject("ELO.office")

elo.doExecuteEx "c:\labelwin\reeinzel.exe","ELORE","c:\labelwin\","",-1

Zuordnen der Scripte zur Oberfläche:

Als nächstes müssen 5 weitere Buttons im Elo erzeugt werden. Wählen Sie hierzu den Button ‚Postbox‘ und dann die Karteikarte Scannen/Ablegen mit einem Rechtsklick.

Es erscheint ein Auswahlmenü. Halten Sie die Strg-Taste gedrückt und wählen Sie mit einem Linksklick ‚Labelablage‘ aus. Wiederholen Sie diesen Schritt mit ‚Label Neues Dokument‘, ‚Label Dokumentenzuordnung‘, ‚Label KD-Auftrag‘ und ‚Label Eingangsrechnung‘.

[Bild]

Aktivieren Sie nun den Button ‚Postbox‘. Sie finden auf der Karteikarte ‚Scannen / Ablagen‘ in der Werkzeugleiste unter ‚Ablage‘ die neu angelegten Buttons.

[Bild]

Um diese Knöpfe jeweils mit einem Script zu belegen sind einige Verrenkungen nötig, die Sie exakt befolgen müssen. Sie drücken die Taste STRG und halten sie die ganze Zeit unten. Nun muss auf dem 1. Button die rechte Maustaste betätigt werden. Aus dem erscheinenden Menü wählen Sie mit der linken Maustaste den Eintrag mit dem Text ‚Labelablage‘. Nun lassen Sie die Taste STRG wieder los.

Es folgt die identische Prozedur mit dem 2. Button und dem Text ‚Label Neues Dokument’, der 3. Button und dem Text ‚Label Dokumentzuordnung’ sowie der 4. Button und dem Text ‚Label KD-Auftrag’

Zuletzt folgt nun der Button 5 mit dem Text ‚Label Eingangsrechnung’.

Es gibt auch irgendeinen Trick, wie man den Knopf mit einen Bild versehen kann, aber den kennen wir noch nicht.

Prüfen der Einbindung:

Um sicher zu stellen dass Sie die oben beschriebenen Verrenkungen richtig vorgenommen haben, müssen Sie nur die Knöpfe mit den Beschriftungen 1bis 5 einfach drücken.
