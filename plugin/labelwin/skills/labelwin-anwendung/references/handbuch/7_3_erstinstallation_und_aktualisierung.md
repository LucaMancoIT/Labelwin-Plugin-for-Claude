# 7.3 Erstinstallation und Aktualisierung

Pfad: Kundendienst > KD-Mobil Notebook [Modul] > 7. Installation und Einrichtungsarbeiten > 7.3 Erstinstallation und Aktualisierung
Quelle: handbuch/7_3_erstinstallation_und_aktualisierung.htm

|

7.3 Erstinstallation und Aktualisierung

In diesem Kapitel lesen Sie, wie die Erstinstallation des mobilen Gerätes und die Übertragung der Grunddaten wie Zahlungsbedingungen, Lohngruppen, Kalkulationseinstellungen usw. erfolgt.

Da die Grunddaten auf dem mobilen Gerät die gleichen wie in der Zentrale sein müssen, werden diese bei einem Grunddaten-Export ausgelagert und auf dem Notebook wieder eingelesen.

|

Info: Die Übertragung der Grunddaten muss immer wiederholt werden, wenn neue Mitarbeiter, andere Preislisten usw. in der Zentrale eingetragen wurden.

Lediglich die Fahrtkosten je Km können einfach geändert werden. Für die Softwarebetreuer hier der Hinweis, dass nur Werte, die in der global.ini eingetragen sind, einfach nachgetragen werden können. Alle Grundwerte, die in der Datenbank eingetragen sind, müssen über den Grunddatenexport und Import übertragen werden.

Bei den Grunddaten können auch Adressen und Anlagen übertragen werden. Die Adressen für die Übertragung können vorher über die normale Adress-Selektion als Word Steuerdatei selektiert werden.

Als Vorlage für die Steuerdatei muss die Datei kdmobil.txt verwendet werden. In der Regel werden dort die Adressen der Großhändler und Hersteller-Hotlines übertragen.

Von der Übertragung aller Anlagen raten wir ab, weil der Stand der übertragenen Anlagen nicht mit dem Stand der Zentrale abgeglichen werden kann und es so passiert, dass „alte“ Anlagen vom Laptop zurückkommen – Anlagen, die in der Zentrale schon längst gelöscht wurden.

Um bei Notdienst-Einsätzen trotzdem die Anlagedaten zur Verfügung zu haben, empfehlen wir den Einsatz der KD Notdienst Lösung. Dort kann sich der Techniker die Daten aus der Zentrale automatisiert schicken lassen, auch wenn die Zentrale nicht besetzt ist (siehe Kapitel Notdienstabwicklung, neue Aufträge mobil anlegen).

|

Wichtig: Vor dem Export sollten Sie die in Kapitel Einstellungen Zentrale beschriebenen Einstellungen vorgenommen haben. Wenn nicht, werden Sie den Grunddatenexport garantiert wiederholen müssen.

Grunddaten und Installationsdaten erzeugen:

Alle Daten werden in einem Transportverzeichnis abgelegt. Dieses Verzeichnis ist im einfachsten Fall ein USB-Stick, eine transportable Festplatte oder eine Speicherkarte. Mit dieser erfolgt auf dem mobilen Gerät dann die Installation, das Update oder die Aktualisierung der Grunddaten.

Es muss das Programm KdexpZen.exe gestartet werden. Dieses Programm liegt im Verzeichnis Labelwin. Da Sie es bei einer späteren Aktualisierung der Grunddaten immer mal wieder brauchen, legen Sie am besten eine Verknüpfung zum Programm an.

Start ohne Verknüpfung:

Das Programm kann auch ohne Verknüpfung direkt gestartet werden. Starten Sie dazu in der Labelwin-Version der Zentrale das Modul EINSTELLUNGEN und wählen dort die Menüpunkte <Optionen> <DOS-Befehl ohne Stop> an. Starten Sie dann das Programm mit dem Namen KdexpZen.exe, indem Sie diesen Namen eingeben.

Zusammenstellen der Daten:

Bei der Erstinstallation kreuzen Sie oben links das Feld "Erstinstallation" an. Damit sind die wichtigsten Punkte passend vorbelegt.

|

[Bild]

Bild: Grunddaten exportieren

|

Adressen und Anlagen:

Bei den Grunddaten können Sie festlegen, dass zusätzlich Adressen und ggf. auch Anlagen übertragen werden sollen. Bei der Übertragung von Kundendienst-Aufträgen werden die dazu gehörigen Adressen ohnehin immer mit übertragen, werden aber nach Rückübertragung des Auftrages auch wieder gelöscht.

Hier geht es also darum, bestimmte Adressen dauerhaft auf dem mobilen Gerät zu haben.

Wenn Sie Adressen übertragen wollen, haben Sie die Möglichkeit Adressen aus einer Selektion zu übertragen. Diese Adressen verbleiben dann immer auf dem Notebook (z.B. Wohnungsgesellschaften, Lieferantenadressen u. ä.)

Unsere Empfehlung ist, möglichst keine oder wirklich nur ausgesuchte Adressen zu übertragen.

Kataloge:

Wenn auf dem mobilen Gerät die verbauten Materialien erfasst oder gar Rechnungen geschrieben werden sollen, müssen Sie die entsprechenden Artikelkataloge übertragen. Wenn Sie die internen Nummern wissen, können Sie diese direkt mit Kommas getrennt eintragen. Sicherer ist es aber, wenn Sie diese mit dem kleinen Button neben der Eingabe auswählen.

Bei manchen Firmen sollen die Mitarbeiter absolut keine Einkaufspreise sehen. Mit dem Ankreuzfeld „Katalogpreise auf 0 setzen“ können Sie diese auf einen Rutsch nach dem Kopieren im Transportverzeichnis löschen. Man kann allerdings auch über die Rechteverwaltung auf dem Notebook realisieren, dass keine Preise eingesehen werden können.

|

Tipp: Um die Masse an Artikeln für den Monteur deutlich zu reduzieren, empfehlen wir das Arbeiten mit einem DiFa-Katalog. Details erfahren Sie im Kapitel DiFa - Direktfakturierung.

Programmupdate und erneuern der Grunddaten

In der Zentrale und auf den mobilen Geräten sollte möglichst die gleiche Programmversion laufen. Dazu kann auch auf dem mobilen Gerät das Update über das Internet geholt werden und eingespielt werden, oder die Update-Dateien in den Transportpfad kopiert und damit das Update eingespielt werden.

Die Grunddaten müssen immer dann übertragen werden, wenn sich folgende Daten verändert haben: Preislisten der Zeitwirtschaft, Personaldaten, Kalkulationseinstellungen, Zahlungsbedingungen, Auftragsarten, Anlagenarten, Karteikarten-Vorlagen usw.

Im gleichen Zuge sollten Sie die Vorlagedatenbank erneut übertragen, da sich einige der Informationen dort befinden.

Auch die Kataloge müssen Sie ggf. von Zeit zu Zeit erneut übertragen, damit alle Artikel auch mobil zur Verfügung stehen.

|

V5 Oberfläche:

Damit auch auf dem mobilen Gerät die neue V5 Oberfläche genutzt werden kann, muss die V5 Grundinstallation übertragen werden. Setzen Sie daher den Haken bei „V5-Grundinstallation“.

Es wird ein Ordner mit dem Namen „v5inst“ übertragen. Die Installation der V5 Oberfläche wird in Kapitel KD-Mobil V5 Installation erklärt.
