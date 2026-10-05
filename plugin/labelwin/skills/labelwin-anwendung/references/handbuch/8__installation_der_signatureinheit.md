# 8. Installation der Signatureinheit

Pfad: Buchhaltung > Ladenkasse [23] > 8. Installation der Signatureinheit
Quelle: handbuch/8__installation_der_signatureinheit.htm

|

8. Installation der Signatureinheit

Diese Informationen sind nur für Österreich notwendig.

8.1 Erwerb der Signatureinheit (USB-Stick)

Nähere Informationen dazu erfahren Sie von unserem österreichischen Label Partner JT-Computer unter office@jt-computer.at.

8.2 Installation des USB-Stick Treibers

Den Treiber bekommen Sie zusammen mit dem USB-Stick. Führen Sie ihn auf dem Arbeitsplatz mit Administratorrechten aus.

[Bild]

8.3 Installation des A-Trust Clients

Um die Signatureinheit anzusteuern benötigen Sie den a.sign Client. Diesen finden Sie zum Download unter https://www.a-trust.at/downloads/.

Folgen Sie den Installationsanweisungen.

Hinweis: Die Installation von a.sign client sollte nur bei angeschlossenem Kartenlesegerät sowie einem korrekt installierten Karten-Treiber durchgeführt werden. Der hinterlegte PIN lautet standardmäßig 123456 und sollte nicht geändert werden. Wurde der a.sign client richtig installiert, erscheint in der Taskleiste ein rotes „a“-Logo. Jetzt können Sie Ihre Smartcard verwalten, aktualisieren, sämtliche Online-Dienste in Anspruch nehmen oder administrative Funktionen ändern.

[Bild]

[Bild]

8.4 Installation des Labelwin A-Trust Treibers

Dieser Treiber mit dem Namen „asignRKCom.dll“ muss derzeit manuell installiert und registriert werden.

· Nach dem Einspielen des Updates sollte die Datei „asignRKCom.dll“ im Labelwin Verzeichnis liegen

· Kopieren Sie die Datei „asignRKCom.dll“ in das lokale „\Windows\System32“ Verzeichnis

· Öffnen Sie eine Kommandooberfläche (cmd.exe) als Administrator

· Wechseln Sie in das lokale „\Windows\System32“ (z.B. „C: <enter>“ gefolgt von „cd \windows\system32 <enter>“)

· Geben Sie den Befehl „regsvr32 asignRKCom.dll“ ein. Es sollte die Meldung „DLL Register succeeded“ kommen. Bestätigen Sie die Meldung

· Schließen Sie die Kommandooberfläche.

8.5 Hinweise zur Formularanpassung

Zum Drucken des QR-Codes auf dem Ladenkassenbeleg muss das Feld textkopf.bildole1 auf das Formular gezogen werden. Außerdem muss im Formular das Formelfeld „qrcodedrucken“ existieren. Dazu muss an dem Arbeitsplatz die Bildverarbeitung aktiviert sein (Siehe Modul „LabelwinEinricht“, Option „Diesen Arbeitsplatz einrichten/erweitern“, Ankreuzfeld „Zusatz DLL’s registrieren, GraphicsProz.“). Ist das nicht der Fall, dass wird statt des QR-Codes der Inhalt als OCR-Text in der Nachbemerkung gedruckt. Bitte dafür das Feld textkopf.nachbemerkung auch auf das Formular ziehen.

Desweiteren sollte das Datumsfeld ausgetauscht werden gegen die Formel „DEPDatum“. Dieses enthält das Datum inkl. der sekundengenauen Uhrzeit, welches auch im DEP-Protokoll und auf dem QR-Code angegeben ist.

An geeigneter Stelle sollte die Kassen-ID mit der Formel „KassenID“ ausgedruckt werden. Außerdem sollte das Formelfeld „SigAusfall“ vorhanden sein, damit beim Ausfall der Signatureinheit ein entsprechender Hinweis „Signatureinheit ausgefallen“ auf dem Beleg erscheint.
