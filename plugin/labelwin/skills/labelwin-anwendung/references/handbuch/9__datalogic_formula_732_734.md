# 9. Datalogic Formula 732/734

Pfad: Materialwirtschaft > Scannerverarbeitung [Modul] > 9. Datalogic Formula 732/734
Quelle: handbuch/9__datalogic_formula_732_734.htm

|

9. Datalogic Formula 732/734

Benötigte Dateien:

Es werden folgende Dateien benötigt, die Sie von Label per Diskette oder Emailanhang erhalten:

Formscan.exe (muss ins Verzeichnis Labelwin)

Easysend.exe (muss ins Verzeichnis Labelwin)

Formula.dll (muss ins Verzeichnis Labelwin)

Formula.ocx (muss ins Verzeichnis Labelwin)

Formula3.cfg (muss ins Verzeichnis Labelwin\vorlage)

Labelfor.exs (muss ins Verzeichnis Labelwin\vorlage)

Bitte registrieren Sie als erstes die Datei Formula.ocx, indem Sie unter ‚Start’, Ausführen’ den Befehl eintippen :

regsvr32 c:\labelwin\formula.ocx (Enter)

Den Pfad C: müssen Sie natürlich durch Ihren Labelwin-Pfad ersetzen.

Programm auf Scanner installieren

Die Schritte in diesem Abschnitt müssen Sie nur dann vornehmen, wenn der Scanner nach dem Einschalten keinen Hinweis auf ‚Label Software’ zeigt.

Starten Sie das Programm Easysend.exe im Verzeichnis Labelwin.

[Bild]

- Gehen Sie auf die Menüpunkte ‚Settings’, ‚Options’ und wählen den Port aus, an dem der Scanner angeschlossen ist. Alles andere lassen Sie unverändert.

- Anschließend wählen Sie die Datei Labelfor.exs aus (ggf. über den Knopf mit den 3 Punkten)

- Spätestens jetzt muss der Scanner angeschlossen sein

- Betätigen den Knopf ‚Send’ . Wenn der Scanner am richtigen Com-Port angeschlossen ist und der Com-Port funktioniert, läuft eine Installation durch. Diese endet mit ‚Data Transfer is succefully terminated’ : Damit ist der Scanner mit unserem Programm bestückt und einsatzbereit.

- Wenn Sie den Scanner aus der Station nehmen, wird an der Oberfläche nach ‚’Art.Nr. oder Menge’ gefragt.

Datenübernahme einrichten

Starten Sie nun das Programm Scann.exe im Verzeichnis Labelwin. Wenn dies nicht schon geschehen ist, sollten Sie eine Verknüpfung auf der Oberfläche erstellen.

[Bild]

Wählen Sie den Scanner aus, nachdem Sie den Knopf ‚Ändern’ betätigt haben. Geben Sie als Pfad und Dateiname ein Ver- zeichnis ein, dass nur von Ihnen benutzt wird. Dies kann z.B. Ihre Platte C: sein oder c:\labeltmp\ oder ...

Als Datei tragen Sie bitte term001.dat ein. Bei der Ablage auf C schreiben Sie also C:\term001.dat

Betätigen Sie dann den Knopf ‚Einstellung’ und tragen in erster Linie den passenden Com-Port ein. Falls Sie einen anderen Pfad als C: gewählt haben, so müssen Sie auf der 2. Karteiseite ebenfalls Änderungen vornehmen. Von allen anderen Einstellmöglichkeiten lassen Sie bitte die Finger weg – es ist alles passend !

[Bild] [Bild]

Das war’s.
