# 1. Labelwin Neu-Installation

Pfad: Installation und Wartung > Labelwin Installation > 1. Labelwin Neu-Installation
Quelle: handbuch/1__labelwin_neu_installation.htm

|

1. Labelwin Neu-Installation

(erfolgt im Normalfall durch den Vertriebspartner)

Installationen sollten grundsätzlich als Administrator, bzw. als Benutzer mit Admin-Rechten erfolgen, da Dateien ansonsten nicht registriert werden können.

Bevor die Einrichtung des Labelwin-Systems erfolgen kann, müssen einige Grundroutinen installiert sein. Auf der Installations-CD gibt es im Hauptverzeichnis folgende Dateien:

-

Grundinst – startet im Verzeichnis \inst32 die LabelwinSetup.exe

-

Einrichtung – startet im Verzeichnis \inst32 die LabelEinricht.exe

-

Handbuch startet diese Beschreibung

-

Readme startet eine Kurzbeschreibung der Installation

Schritt 1: LabelwinSetup.exe und LabelwinSetupZ.exe starten

|

Man startet von der CD per Explorer-Doppelklick zuerst die Datei Grundinst (alternativ aus dem Unterverzeichnis \inst32 die LabelwinSetup.exe). Dieses typische Windows Installationsprogramm läuft völlig ohne weitere Benutzereingaben durch.

Das LabelwinSetup Programm endet mit einem Info-Fenster, in dem das weitere Vorgehen kurz beschrieben wird. Sollte ein Computer Neustart verlangt werden, so sollte man ihn sinnigerweise jetzt durchführen.

Den gleichen Vorgang wiederholt man mit der Datei LabelwinsetupZ.exe.

Hinweis: Sollte die gleiche Version der LabelwinSetup.exe oder LabelwinsetupZ.exe zum wiederholten Male auf einem Rechner laufen, dann erfolgt vorher die Frage, ob es ‚Repariert’ oder ‚Deinstalliert’ werden soll. Bitte in diesem Fall immer auf ‚Reparieren’ klicken.

|

[Bild] [Bild]

Anmerkungen zu Rechten:

|

Startet man das LabelwinSetup.exe Programm als normaler User auf einem Rechner ab Betriebssystem Windows Vista, kommt sofort der Login Bildschirm, an dem man sich erst mit Administratoren-Rechten anmelden muss. Ohne tatsächliche Admin Rechte gibt es also definitiv keine Installation auf einem Rechner mit aktuellem Betriebssystem. Als Admin wird man bei eingeschalteter Benutzerkontenkontrolle auf die notwendigen Admin Rechte hingewiesen.

Hat man auf einem Rechner keine Admin Rechte, so wird es im Laufe der Installation zu diversen Fehlermeldungen kommen (kann Datei xyz.dll nicht installieren oder registrieren).

Die LabelwinEinricht.exe braucht zwar keine Administratoren-Rechte, aber für die Einrichtung von Hilfsprogrammen wie PSP5 (Grafikprogramm um Bilder in Angeboten drucken zu können) und E-Doc (Druckausgabe als PDF-Datei) benötigt man zum Installieren ggf. Admin Rechte und auch für das Anlegen vom Startmenü braucht man gewisse Rechte.

Ggf. startet man, genau wie die LabelwinSetup.exe, auch die LabelwinEinricht.exe als Admin und gibt dann an, dass man eigentlich für einen anderen Benutzer installiert.

Schritt 2: LabelwinEinricht.exe starten

Im zweiten Schritt startet man von der CD per Explorer-Doppelklick die Datei Einrichtung (alternativ aus dem Unterverzeichnis \inst32 die LabelwinEinricht.exe).

[Bild: 1. Labelwin Neu-Installation]

Die Neuinstallation erfolgt in der Regel auf dem Server. Da dort normalerweise nicht als Anwender gearbeitet wird, können die Zusatzoptionen allesamt abgehakt werden. Bei der Arbeitsplatz Einrichtung werden sie dagegen benötigt.

|
[Bild: 1]

Neuinstallation

[Bild: 1. Neuinstallation]

Die LabelwinEinricht.exe erkennt automatisch, dass sie aus einem Verzeichnis heraus gestartet wurde, in dem kein Labelwin installiert ist. Man kann daher bei einer Neuinstallation nichts auswählen, sondern die erste Einstellung steht automatisch auf dem Punkt Labelwin Neuinstallation (von CD).

Eine Auswahl besteht nur nach der erfolgten Erstinstallation. Das gleiche Modul wird zur Einrichtung weiteren Arbeitsplätzen und zum Update einspielen verwendet.

|
[Bild: 2]

Zielpfad

[Bild: 2. Zielpfad]

Als erste Eingabe muss man den Labelwin Zielpfad angeben. In der Regel sollten Sie höchstens den Plattenbuchstaben ändern und das Verzeichnis bei ‚Labelwin’ belassen. Unsere Hotliner werden bei Problemen zunächst davon ausgehen, dass es so heißt. Wenn Sie einen anderen Namen auswählen, erschweren Sie nur die Betreuung.

Über den Durchsuchen-Knopf kann man ein bestehendes Verzeichnis auswählen. Ein neues Verzeichnis muss per Hand eingetippt werden. Es wird mit Nachfrage automatisch angelegt. Daten in einer bestehenden Labelwin Installation werden nicht überschrieben.

|
[Bild: 3]

Durchsuchen

[Bild: 3. Durchsuchen]

Falls das Labelwin-Verzeichnis bereits angelegt wurde, kann man es mit diesem Knopf auswählen.

|
[Bild: 4]

Startmenü anlegen

[Bild: 4. Startmenü anlegen]

Hiermit wird das V4 Startmenü für den gerade aktiven Nutzer angelegt. In der Regel wird das V4 Startmenü nicht benötigt, da nur noch die neuere V5 Oberfläche verwendet werden sollte.

Per Option im Modul EINSTELLUNGEN kann man dieses V4 Startmenü auch als ‚gelben’ Ordner auf den Desktop legen.

Hinweis: Es ist dann ein eigenständiger Ordner und keine Verknüpfung mit dem Startmenü!

|
[Bild: 5]

Crystal 10/11 Druckerfunktionen

[Bild: 5. Crystal 10/11 Druckerfunktionen]

Wenn Sie später bei Angeboten und Rechnungen mit formatierten Texten und / oder Bildern arbeiten möchten, müssen Sie diese Option installieren. Wenn Sie schon lange mit Labelwin arbeiten, beachten Sie bitte, dass Ihre Druckformulare ggf. überarbeitet werden müssen. Bei einer Neuinstallation werden standardmäßig Formulare mit Formatierungsmöglichkeit eingerichtet.

Diese Option startet die Installationsroutinen CR11inst.msi und CR10inst.msi. Ggf. müssen Sie zwischendurch die Fragen gemäß der Vorgabe bestätigen.

|
[Bild: 6]

PSP5 installieren

[Bild: 6. PSP5 installieren]

Dahinter verbirgt sich die Installation eines Programmes mit dem Namen PSP5, welches kostenlos verwendet werden darf. Wenn Sie mit Bildern in Angeboten arbeiten möchten, so muss dieses oder ein anderes OLE-fähiges Bildbearbeitungsprogramm installiert sein.

Für welche Dateiendungen bereits ein OLE-fähiges Programm installiert ist, erfährt man im Tooltip, wenn man mit der Maus über das Checkfeld fährt. Wenn dort alle standardmäßigen Formate dabei sind, können Sie auf die Installation verzichten. Wichtig sind meist nur die Formate BMP, TIF und JPG. Mit letzterem arbeiten die meisten Kameras.

|
[Bild: 7]

Zusatz DLL's registrieren

[Bild: 7. Zusatz DLL's registrieren]

Für einige Zusatzmodule bzw. Zusatzfunktionen werden weitere Programmbibliotheken benötigt. Sollte die Bildverarbeitung, die Gaeb Datei Bearbeitung, das Telefonie Modul oder die Blockanzeige im Kalender genutzt werden, müssen hier die entsprechenden Haken gesetzt werden. Im Zweifel setzt man einfach alle Haken.

Mangels Windows Benutzerrechte kann es aber passieren, dass die Registrierung ganz oder teilweise fehlschlägt. In diesem Fall sollte die LabelwinEinricht.exe anschließend einmal als Admin gestartet werden, um die Zusatz DLL’s zu registrieren.

Tipp: Ggf. hilft es auch die „Administrator.ini“ umzubenennen, in (Administrator_org.ini) und dann über den „Netzwerkpfad“ zu gehen und die „labelwineinricht.exe“ als „Administrator“ zu starten. Ein Registrieren der Dateien sollte dann erfolgreich sein.

|
[Bild: 8]

Aktueller Pfad

[Bild: 8. Aktueller Pfad]

Hier wird der Pfad angezeigt aus dem das Programm aufgerufen wurde.

|
[Bild: 9]

Protokoll

[Bild: 9. Protokoll]

Während ein Update eingespielt wird, eine Neuinstallation vorgenommen wird oder was auch immer hier passiert, es wird protokolliert. Mit diesem Knopf kann man das Protokoll von den vorherigen Vorgängen einsehen.

|
[Bild: 10]

Handbuch

[Bild: 10. Handbuch]

Durch Betätigen dieses Knopfes haben Sie die Möglichkeit, während eines Updates im Handbuch zu lesen. Bei einer Neuinstallation ist diese Funktion nicht anwählbar.

|
[Bild: 11]

Details einblenden

[Bild: 11. Details einblenden]

Wenn Sie diesen Knopf drücken, wird rechts neben der Maske ein Bereich eingeblendet, in dem das Protokoll direkt mitläuft und einige Statusinformationen sichtbar sind. In dieser Maske kann auch der Schalter ‚Installation Terminalserver / Vistarechner’ gesetzt werden. Allerdings wird diese Information automatisch erkannt und entsprechend belegt.

|
[Bild: 12]

Start

[Bild: 12. Start]

Hiermit starten Sie den gewählten Vorgang.

|
[Bild: 13]

Ende

[Bild: 13. Ende]

Durch Betätigen dieses Knopfes wird das Fenster geschlossen.

|

Wichtig: Die Installation der V4 Version ist nun abgeschlossen. Es muss anschließend zwingend noch die V5 Version installiert werden. Die entsprechende Installationsanleitung befindet sich im Kapitel V5 Installation.
