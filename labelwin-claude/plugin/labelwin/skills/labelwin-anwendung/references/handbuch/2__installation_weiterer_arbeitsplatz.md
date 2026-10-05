# 2. Installation weiterer Arbeitsplatz

Pfad: Installation und Wartung > Labelwin Installation > 2. Installation weiterer Arbeitsplatz
Quelle: handbuch/2__installation_weiterer_arbeitsplatz.htm

|

2. Installation weiterer Arbeitsplatz

Diese Beschreibung ist zum Teil identisch mit der Neu-Installation des Labelwin-Systems, aber um Ihnen die Einrichtung eines weiteren Arbeitsplatzes zu erleichtern, haben wir hier alle erforderlichen Schritte zusammengefasst.

|

Da die Arbeitsplatzeinrichtung vielleicht von einem Systembetreuer durchgeführt werden soll und dieser keinen Zugriff auf das Handbuch hat, bieten wir hier zwei Dateien mit ausführlichen Beschreibungen und Hintergrundinformationen zum Download an.

|

Installationsanleitung weiterer Arbeitsplatz:

|


[Bild] 


|

Informationen zur Druckereinrichtung:

|


[Bild] 


Voraussetzungen

Der Rechner muss mit dem Betriebssystem komplett eingerichtet sein und das Labelwin-Verzeichnis muss über einen vorangestellten Plattenbuchstaben zur Verfügung stehen (z. B. L:\labelwin\).

Die grundlegenden Arbeitsschritte

Die Installation bzw. Einrichtung erfolgt in 6 Schritten:

-

Installation/Einrichtung von externen Treibern, Druckern, etc.

-

Installation/Einrichtung von Labelwin Routinen, für die Admin-Rechte benötigt werden

-

Einrichtung von Labelwin, bei denen man als Benutzer angemeldet sein muss

-

Maschinen-/stationsbezogene Einstellungen vornehmen

-

Den Benutzer im Personal eintragen und in der Rechteverwaltung freigeben

-

Weitere benutzerspezifische Einstellungen vornehmen

1. Installation/Einrichtung von externen Treibern, Druckern, etc.

Dieses sind vorbereitende Maßnahmen, die der Systembetreuer vorab und vollkommen unabhängig von der Labelwin Einrichtung durchführen kann.

Drucker

Logischerweise benötigt Labelwin installierte und eingerichtete Drucker. Da Labelwin keine Schachtansteuerung benutzt, muss für jeden Schacht ein eigener Drucker eingerichtet sein. Sollte das auf Grund von Netzwerkdruckern die per Gruppenrichtlinie freigegeben sind, Probleme bereiten, sollten diese Drucker statt dessen lokal installiert und über die IP-Adresse angesprochen werden.

Ein Drucker (bzw. Schacht), der als Folgeseitendrucker (Seite 1 Briefpapier, Seite 2ff auf weißes Papier) benutzt wird, muss heißen wie der Seite 1 Drucker, aber mit der Namensergänzung {Leertaste}S2.

Bsp.: „Brother Firmenpapier“ und „Brother Firmenpapier S2“. Hier muss der S2 Drucker, trotz des Namens, aber auf den Schacht mit weißen Papier verweisen. „Drucker weiß“ wäre dann identisch zu dem S2 Drucker.Die Zuweisung der Drucker erfolgt im Schritt 3

PDF-Drucker (eDoc)

Zum Erstellen von PDF-Dateien für den E-Mail Versand oder auch für die Ablage von Druckausgaben im Labelwin PDF-Archiv wird ein bestimmter PDF-Druckertreiber benötigt. Es darf nicht irgendein PDF Drucker sein, sondern muss der kostenlose eDocPrintpro Druckertreiber von www.pdfprinter.at sein. Sollten allerdings auch elektronsiche ZUGFeRD PDF Rechnungen erstellt werden, muss der kostenpflichtige eDocPrintpro PDF/A ZUGFeRD installiert werden. Bitte achten Sie auf die notwendigen userspezifische Einstellungen (siehe Kapitel PDF-Ablage und PDF Druckertreiber bzw. ZUGFeRD mit PDF/A Druckertreiber).

PDFTK

Für das Zusammenmischen und Anhängen von PDF-Dateien bei Verwendung des Zusatzmoduls SCAN-ARCHIV benötigen Sie ein kostenloses Zusatzprogramm namens „PDFTK“. Im „\labelwin\vorlage\“ Verzeichnis finden Sie eine PDFTK_setup.exe. Starten Sie es mit „Ausführen als Administrator“. Merken (oder kopieren) Sie sich den Pfad, in dem es installiert wird. Z.B. „C:\Program Files (x86)\PDFtk“. Diesen Pfad, gefolgt vom Unterverzeichnis ‚bin‘, also „C:\Program Files (x86)\PDFtk\bin\“, müssen Sie später im Schritt 4 eintragen. Details zur Installation finden Sie auch unter PDFTK einrichten.

Sonstiges

Unter Umständen werden noch weitere Treiber benötigt, z.B. beim Einsatz von Dokumentenscannern (TWAIN Treiber) oder bei der Einbindung der Telefonanlage (TAPI).Außerdem werden ggf. weitere Fremdprogramme benötigt, wie z.B. MS-Office mit Word, Excel und Outlook.

nach oben

2. Installation/Einrichtung von Labelwin Routinen, für die Admin-Rechte benötigt werden

Dieses sind technische Maßnahmen, die auch der Systembetreuer, der sich mit Labelwin nicht auskennt, problemlos durchführen kann.

Siehe unbedingt die Hinweise unter Allgemeines zur Verzeichnisfreigabe, Laufwerksbuchstabe und Rechte zum Thema „lokaler Admin“ bzw. „Domänen-Admin“ und loggen Sie sich als Administrator ein.

Schritt 1: LabelwinSetup.exe und LabelwinSetupZ.exe

|

Starten Sie aus dem Labelwin Verzeichnis der Reihe nach die beiden Programme

„LabelwinSetup.exe“ und „LabelwinSetupZ.exe“

Diese typischen Windows Installationsprogramme laufen völlig ohne weitere Benutzereingaben durch.

Das LabelwinSetup Programm endet mit einem Info-Fenster, in dem das weitere Vorgehen kurz beschrieben wird. Sollte ein Computer Neustart verlangt werden, so sollte man ihn sinnigerweise jetzt durchführen.

Info: Sollte die gleiche Version der LabelwinSetup.exe oder LabelwinsetupZ.exe zum wiederholten Male auf einem Rechner laufen, dann erfolgt vorher die Frage, ob es ‚Repariert’ oder ‚Deinstalliert’ werden soll. Bitte in diesem Fall immer auf ‚Reparieren’ klicken.

|

[Bild] [Bild]

Hinweis für Terminalserver: Auf einem Terminalserver müssen Sie diese beiden Programme nur einmal starten und nicht für jeden Benutzer starten. Bei einem wiederholten Aufruf kommen die üblichen Nachfragen, ob Sie das Programm reparieren oder entfernen möchten.

Damit haben Sie die Grundroutinen installiert, damit das nächste Programm, die LabelwinEinricht.exe, gestartet werden kann.

Schritt 2: LabelwinEinricht.exe (als Admin)

Im zweiten Schritt starten Sie das Programm „LabelwinEinricht.exe“ aus dem Labelwin Verzeichnis. Wählen Sie die Option „Diesen Arbeitsplatz einrichten/ erweitern“ und setzen Sie auf der linken Seite im Rahmen „Nur als Administrator“ zwingend das Ankreuzfeld "Crystal 10/11 Druckerfunktionen". Die beiden anderen Ankreuzfelder sind optional.

Drücken Sie dann auf die Schaltfläche „Start“. Es werden jetzt der Reihe nach diverse Programme, Treiber und Bibliotheken installiert. Folgen Sie dabei den Anweisungen auf dem Bildschirm.

Hinweis für Terminalserver: Auch hier gilt, dass Sie diese Installationen auf einem Terminalserver nur einmal und nicht für alle Benutzer aufrufen müssen.

[Bild: 2. Installation weiterer Arbeitsplatz]

Hinweise:

-

Der linke Block im Bereich Zusatz-Optionen [Nr.2] bis [Nr.4] ist nur mit Adminstrator Rechten anwählbar. Für eine vollständige Arbeitsplatz-Installation sind also Admin Rechte - zumindest temporär - erforderlich.

-

Den Eintrag [Nr.3] können, müssen Sie aber nicht zwingend ankreuzen. Wenn Sie später bei Angeboten und Rechnungen mit formatierten Texten und / oder Bildern arbeiten möchten, müssen Sie diese Option installieren. Wenn Sie schon lange mit Labelwin arbeiten, beachten Sie bitte, dass Ihre Druckformulare ggf. überarbeitet werden müssen.

-

Eintrag [Nr.7] müssen Sie nicht ankreuzen. Hierüber wird das Startmenü für Labelwin V4 erzeugt. Sie sollten aber nur noch mit der neuen V5 Version arbeiten, die über Eintrag [Nr.5] installiert wird.

-

Den Punkt [Nr.8] müssen Sie nur dann ankreuzen, wenn Sie nicht mit dem gleichen Namen eingeloggt sind, mit dem später im Labelwin gearbeitet werden soll. Sie müssen dann exakt den Namen eingeben, mit dem der spätere Benutzer angemeldet wird. Sollten Sie hier einen Fehler machen, so müssen Sie die Einrichtung später wiederholen, weil der Anwender im Labelwin nicht gefunden werden kann.

|

Labelwin V5:

Eintrag [Nr.5] V5 Client installieren ist erst anwählbar, wenn die Labelwineinricht.exe bereits einmal gelaufen ist. Man muss also, um den V5 Client installieren zu können, erst einmal die Einrichtung ohne diese Option laufen lassen. Beim zweiten Durchgang lässt man dann alle Haken weg außer bei Punkt [Nr.5].

Sollte die V5 Client Installation mit Fehlermeldungen abbrechen, kann es an fehlenden Rechten am Arbeitsplatz liegen oder an einer defekten .Net Framework Installation. In zweiten Fall empfehlen wir das Microsoft .NET Framework Repair Tool auszuführen. Sie erhalten es auf der offiziellen Seite von Microsoft.

Beschreibung der einzelnen Punkte in der Labelwineinricht.exe:

|
[Bild: 1]

Arbeitsplatz einrichten

[Bild: 1. Arbeitsplatz einrichten]

Dieses Modul kann drei Funktionen ausführen. Wählen Sie hier die Funktion "Diesen Arbeitsplatz einrichten/erweitern".

Hinweis: Die folgenden Punkte 2 bis 4 sind nur anwählbar, wenn Administratorrechte vorliegen. Sollten Sie diese Punkte nicht anklicken können, müssen Sie sich zuerst mit einem Benutzerkonto mit Adminstratorrechten anmelden. Fragen Sie im Zweifel Ihren Systembetreuer.

|
[Bild: 2]

Crystal 10/11 Druckerfunktionen

[Bild: 2. Crystal 10/11 Druckerfunktionen]

Wenn Sie später bei Angeboten und Rechnungen mit formatierten Texten und / oder Bildern arbeiten möchten, müssen Sie diese Option installieren. Wenn Sie schon lange mit Labelwin arbeiten beachten Sie bitte, dass Ihre Druckformulare ggf. überarbeitet werden müssen. Bei einer Neuinstallation werden standardmäßig Formulare mit Formatierungs-möglichkeit eingerichtet.

Diese Option startet die Installationsroutinen CR11inst.msi und CR10inst.msi. Ggf. müssen Sie zwischendurch die Fragen gemäß der Vorgabe bestätigen.

|
[Bild: 3]

OLE fähiges PSP5 installieren

[Bild: 3. OLE fähiges PSP5 installieren]

Dahinter verbirgt sich die Installation eines Programms mit dem Namen PSP5, dass kostenlos verwendet werden darf. Wenn Sie mit Bildern in Angeboten arbeiten möchten, so muss dieses oder ein anderes OLE-fähiges Bildbearbeitungsprogramm installiert sein.

Für welche Dateiendungen bereits ein OLE-fähiges Programm installiert ist, erfährt man im Tooltip, wenn man mit der Maus über das Checkfeld fährt. Wenn dort alle standardmäßigen Formate dabei sind, können Sie auf die Installation verzichten. Wichtig sind meist nur die Formate BMP, TIF und JPG. Mit letzterem arbeiten die meisten Kameras.

|
[Bild: 4]

Zusatz DLL's registrieren

[Bild: 4. Zusatz DLL's registrieren]

Für einige Zusatzmodule bzw. Zusatzfunktionen werden weitere Programmbibliotheken benötigt. Sollte die Bildverarbeitung, die Gaeb Datei Bearbeitung, das Telefonie Modul oder die Blockanzeige im Kalender genutzt werden, müssen hier die entsprechenden Haken gesetzt werden. Im Zweifel setzt man einfach alle Haken.

Mangels Windows Benutzerrechte kann es aber passieren, dass die Registrierung ganz oder teilweise fehlschlägt. In diesem Fall sollte die LabelwinEinricht.exe anschließend einmal als Admin gestartet werden, um die Zusatz DLL’s zu registrieren.

Tipp: Ggf. hilft es auch die „Administrator.ini“ umzubenennen, in (Administrator_org.ini) und dann über den „Netzwerkpfad“ zu gehen und die „labelwineinricht.exe“ als „Administrator“ zu starten. Ein Registrieren der Dateien sollte dann erfolgreich sein.

|
[Bild: 5]

Labelwin V5 Client installieren

[Bild: 5. Labelwin V5 Client installieren]

Durch die Wahl dieser Option wird die neue V5 Oberfläche installiert. Wichtig hierbei ist, dass bereits eine Grundinstallation (im Idealfall auf dem Server) erfolgt sein muss. Details zur V5 Installation können dem entsprechenden Kapitel entnommen werden.

|
[Bild: 6]

Startmenü anlegen

[Bild: 6. Startmenü anlegen]

Hiermit wird das V4 Startmenü für den gerade aktiven Nutzer angelegt. In der Regel wird das V4 Startmenü nicht mehr benötigt, da nur noch die neuere V5 Oberfläche verwendet werden sollte.

Per Option im Modul EINSTELLUNGEN kann man dieses V4 Startmenü auch noch nachträglich als ‚gelben’ Ordner auf den Desktop legen.

Hinweis: Es ist dann ein eigenständiger Ordner und keine Verknüpfung mit dem Startmenü!

|
[Bild: 7]

Vorlage für user.ini nehmen

[Bild: 7. Vorlage für user.ini nehmen]

Durch die Wahl dieser Option ist es möglich, die Pfadeinstellungen eines Benutzers zu ändern und die sonstigen Benutzereinstellungen unverändert zu lassen. Bei dem Abgleich mit der Auswahl ‚Standard Pfade’ werden alle Labelwin-Pfade so belegt, wie dies bei einer Neuinstallation gemacht wird. Sie können jedoch auch einen Abgleich mit einer ‚User.ini’ vornehmen, so dass die dort eingetragenen Pfade übertragen werden.

Diese Möglichkeit wird immer dann gebraucht, wenn sich der Verzeichnispfad des Labelwin-Systems geändert hat, was z.B. bei Server-Neueinrichtungen manchmal der Fall ist.

Standardmäßig werden die Pfade in der User.ini nach Standardregeln erstellt. Also alle einstellbaren, durchnummerierten Pfade liegen unter Labelwin und heißen wie standardmäßig vorgesehen.

Wenn bei einer Labelwin Installation aber einige Pfade außerhalb des Labelwin Verzeichnissystem verlegt wurden, dann kann man die einstellbaren Pfade für einen Anwender aus einer Vorlage user.ini kopieren.

In der Vorlage User.ini kann dabei mit 2 Schlüsselworten für den Benutzernamen und den Computernamen gearbeitet werden.

z.B.: 10=f:\labelwin\user\$(labeluser)\labeltmp

z.B.: 10=f:\labelwin\computer\$(computer)\labeltmp

Umsetzen von Verzeichnispfaden

Um im Netzwerk mehr Tempo in die Anwendung zu bringen, könnte der Wunsch auftauchen, die Programme auf der lokalen Festplatte zu verwalten. Bei unserem momentanen Programmstand müssen wir davon abraten, weil auch Einstellungen (INI-Dateien) in diesem Bereich abgelegt werden. Bei nachträglichen Änderungen sind diese Einstellungen dann auf den Plätzen unterschiedlich und es gibt Probleme. Auch kann beim Update nicht gewährleistet werden kann, dass die Programmänderungen überall auf die lokalen Platten kopiert werden. In diesem Falle könnte also das Einspielen eines Updates auf einem Platz die Arbeitsfähigkeit der anderen Benutzer blockieren. Langfristig ist geplant, diese Möglichkeit über entsprechende Batch-Dateien einzurichten.

Da die Betreuung und Aktualisierung der Programme wesentlich erschwert wird, raten wir davon ab, die einzelnen Teile unseres Paketes auf der lokalen Festplatte zu führen.

|
[Bild: 8]

Aktueller Pfad

[Bild: 8. Aktueller Pfad]

Hier wird der Pfad angezeigt aus dem das Programm aufgerufen wurde.

|
[Bild: 9]

Protokoll

[Bild: 9. Protokoll]

Hierüber kann das Protokoll der zuvor ausgeführten Aktion (Installation, Einrichtung, Update) eingesehen werden.

|
[Bild: 10]

Handbuch

[Bild: 10. Handbuch]

Über diesen Button kann das Handbuch aufgerufen werden. Es öffnet sich diese Seite.

|
[Bild: 11]

Details einblenden

[Bild: 11. Details einblenden]

Dieser Button erweitert das Fenster. In diesem werden weitere Details zum Rechner und zum Installaionsverlauf angezeigt.

|
[Bild: 12]

Start

[Bild: 12. Start]

Dieser Button startet die gewählte Aktion.

|
[Bild: 13]

Ende

[Bild: 13. Ende]

Bei Betätigung dieses Buttons wird das Programm geschlossen.

Die Menüpunkte im Einzelnen:

|

Datei

|

Start (F5)

|

Gleiche Bedeutung wie der Startknopf [Nr.12]

|

Labelwin V5 DVD Download

|

Lädt die aktuelle Version (V5) herunter. Hierfür muss die bestehende Version aktuell sein. Es handelt sich um einen einmaligen Vorgang, da bestehende V5-Versionen über die normalen Update-Routinen aktualisiert werden.

|

V5 Mehrfach-Installation

|

Wird nur verwendet, wenn Sie innerhalb des Systems mit mehreren unabhängig voneinander installierten Labelwin-Versionen arbeiten.

|

AufmaßMobil Installation

|

Dieser Menüpunkt wird nur benötigt für die Installation des Zusatzmoduls AufmaßMobil

|

Protokoll lesen (F9)

|

Gleiche Bedeutung wie der Kopf [Nr.9]

|

Grundroutinen (DLL) erneuern

|

Wählt man diesen Menüpunkt aus, wird die LabelwinSetup.exe durchgestartet. Diese Möglichkeit ist weitgehend überflüssig, weil das gerade aktive Programm nur läuft, wenn die Grundroutinen installiert sind. Es kann allerdings in seltenen Fällen erforderlich sein, die Grundroutinen noch einmal zu installieren, weil diese z.B. durch die Installation eines anderen Programms vernichtet bzw. mit einer zu alten Version überschrieben worden sind.

|

Grundroutinen Zusatz installieren

|

Bei einer Programmerweiterung ist es möglicherweise erforderlich, weitere ‚Grundroutinen’ zu installieren. Um diese im Internet-Update transportieren zu können, werden sie in einer kleinen separaten Datei ausgeliefert. Wenn die Installation erforderlich ist, werden wir Sie in der Update-Beschreibung darauf hinweisen.

|

Register/Deregister

|

Bitte starten Sie diesen Menüpunkt nur, wenn Sie vom Label Support dazu aufgefordert werden!

|

Laufwerksbuchstaben/Pfad umstellen

|

Durch die Wahl dieses Menüpunktes können Sie nach dem Verschieben von Labelwin in ein anderes Verzeichnis bzw. bei Änderung des Laufwerkbuchstabens automatisch alle Pfadeinträge in den INI-Dateien und in den Datenbanken anpassen.

Die Pfadangaben in der user.ini für den aktuellen Benutzer (administrator.ini) müssen bereits korrekt sein!

|

KD-Ordner anlegen

|

Bei Interesse wenden Sie sich bitte an den Labelwin Support.

|

Ende (F4)

|

Gleiche Bedeutung wie der Endeknopf [Nr.13].

nach oben

3. Einrichtung von Labelwin, bei denen man als Benutzer angemeldet sein muss

Diese eigentliche Einrichtung sollte der Labelwin-Betreuer durchführen.

Stellen Sie sicher, dass Sie als der neue Benutzer eingeloggt sind.

Schritt 1. Labelwineinricht.exe (als Benutzer)

Starten Sie die Labelwineinricht.exe aus dem Labelwin Verzeichnis per Doppelklick. Wählen Sie die Option „Diesen Arbeitsplatz einrichten/erweitern“ und gehen Sie auf der rechten Seite zum Rahmen „Für den aktiven Benutzer“.

Dieser Durchlauf richtet den Benutzer ein.

Sie können mit dem Haken bei „V4 Startmenü anlegen“ ein Startmenü-Eintrag mit den wichtigsten Modulen als Untermenü-Eintrag erzeugen. Allerdings ist das im Prinzip nicht mehr notwendig, da die nachfolgende Labelwin V5 Client Installation eine lila Startflagge auf den Desktop legt.

Mit einem Haken bei „Vorlage für User.ini nehmen“ können Sie viele benutzerspezifische Einstellungen eines anderen Users (Benutzers) übernehmen. Etliche Einstellungen (Name, E-Mail Adresse etc.) müssen jedoch immer individuell angepasst werden. Drücken Sie auf die Schaltfläche „Start“.

Schritt 2. Labelwineinricht.exe (als Benutzer) mit V5 Client

Starten Sie die Labelwineinricht.exe ein weiteres Mal. Wählen Sie erneut die Option „Diesen Arbeitsplatz einrichten/erweitern“ und setzen den Haken bei „Labelwin V5 Client installieren“.

[Bild]

Nachdem man den Start Knopf betätigt hat, wird das Installationspaket (client.zip) entpackt und die Arbeitsplatzinstallation vorbereitet. Sollte die client.zip nicht vorhanden sein, wird das Programm diese vom Labelwin Server runterladen.

Ist das Installationspaket entpackt, startet die Installation mit zwei vorbereitenden Windows Treiber Installationen (VCRedist). Es müssen einige Meldungen bestätigt werden.

[Bild]

Anschließend kann die eigentliche Labelwin V5 Arbeitsplatzinstallation beginnen.

[Bild]

Während der Installation wird ein Zielordner abgefragt. Hier ist es ganz wichtig den Zielordner über den Ändern Button auf das Labelwin Verzeichnis, z. B. L:\labelwin\ einzustellen.

[Bild]

Die V5 Arbeitsplatzinstallation endet mit einer entsprechenden Meldung.

|

[Bild]

|

Nach erfolgreicher Installation finden Sie eine Verknüpfung ‘Labelwin starten‘ auf Ihrem Desktop. Damit starten Sie das Labelwin V5 Startcenter“.

Sollte die Verknüpfung einmal fehlen, kann sie auch manuell angelegt werden. Sie verweist auf die Datei labelwin.exe

nach oben

4. Maschinen-/stationsbezogene Einstellungen vornehmen

Diese stationsbezogenen Einstellungen sollte der Labelwin-Betreuer, ggf. mit Unterstützung des Systembetreuers, durchführen.

Stellen Sie sicher, dass Sie als der neue Benutzer eingeloggt sind.

Nach dem erfolgreichen Einrichten des Benutzers (Schritt 3) taucht auf der Maske eine neue Schaltfläche „Stationseinstellungen“ auf.

Hierüber können Sie Vorgaben für die Druckerauswahl erfassen. Denn diese Einstellungen müssen Sie von diesem Arbeitsplatz ausführen.

[Bild]

|
[Bild: 14]

Stationseinstellungen

[Bild: 14. Stationseinstellungen]

Hinter diesem Knopf verbergen sich alle wichtigen Stationseinstellungen. In erste Linie handelt es sich dabei um Drucker- und Scannereinstellungen. Alle Einstellungen auf dieser Maske können auch einzeln im Einstellmodul vorgenommen werden. Da diese dort aber in verschiedenen Bereichen wiederzufinden sind, haben Sie hier eine einfachere Möglichkeit alle wichtigen Einstellungen vorzunehmen.

[Bild]

Außerdem können Sie in dieser Maske den Pfad zu PDFTK hinterlegen (siehe oben unter „Installation Treiber“). Der Pfad ist der Installationspfad plus das Unterverzeichnis „bin“. In Normalfall also „C:\Program Files (x86)\PDFtk\bin\“.

5. Den Benutzer im Personal eintragen und in der Rechteverwaltung freigeben

Diese eigentliche Einrichtung muss der Labelwin-Betreuer bzw. der „Chef“, der über ausreichende Rechte im Einstellmodul verfügt, durchführen.

Die Erst-Einrichtung des Arbeitsplatzes ist somit abgeschlossen. Jetzt muss der Benutzer noch im Labelwin Personalstamm und ggf. in der Rechteverwaltung eingetragen werden.

|

Verlassen Sie diesen Arbeitsplatz und wechseln Sie zu einem „Chef“-Arbeitsplatz. Starten Sie das Modul „Einstellungen“ und wählen Sie den Menüpunkt <Programmbereiche>, <Personal>, <Personal erfassen>. Legen Sie den Benutzer als neuen Mitarbeiter an, sofern es noch nicht geschehen ist. Wichtig ist hier erstmal nur eine eindeutige Personalnummer, ein Name und ein Name komplett, sowie den Label-User. In der Auswahlliste von Label-User müsste der soeben eingerichtete User (=Loginname) jetzt vorhanden sein. Klicken Sie auf die Schaltfläche „Speichern“, gefolgt von „Ende“.

|

[Bild]

|

Wenn Sie mit den Labelwin Benutzerrechten arbeiten, und das sollten Sie auf jeden Fall, wählen Sie nun den Menüpunkt <Optionen>, <Benutzerrechte vergeben>. Drücken Sie die Schaltfläche „Neuer Benutzer“ und tippen Sie den soeben eingerichteten Usernamen (=Loginname) ein. Der neue Benutzer hat jetzt erstmal alle Standardrechte. Beenden Sie die Maske mit „Speichern“ und „Ende“.

|

[Bild]

nach oben

6. Weitere benutzerspezifische Einstellungen vornehmen

Auch diese eigentliche Einrichtung muss der Labelwin-Betreuer bzw. der „Chef“, der über ausreichende Rechte im Einstellmodul verfügt, durchführen.

Alle weiteren benutzerspezifischen Einstellungen können Sie von diesem „Chef“-Arbeitsplatz aus machen. Rufen sie den Menüpunkt <Serviceprogramme>, <Usereinstellung> auf. Wählen Sie die Option „Einstellungen für anderen User aktivieren“ und wählen Sie den Namen (Login) des Users und bestätigen Sie mit „OK“. Jetzt können Sie der Reihe nach alle notwendigen Menüpunkte aufrufen. Alle benutzerspezifischen Einstellungen werden für den gewählten Benutzer gespeichert.

Dieser Weg ist zwingend erforderlich, wenn der neue Benutzer keine oder keine ausreichenden Rechte im Modul Einstellungen hat.

nach oben
