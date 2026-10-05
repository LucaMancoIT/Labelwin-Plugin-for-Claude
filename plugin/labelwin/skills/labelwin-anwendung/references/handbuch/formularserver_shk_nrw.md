# Formularserver SHK NRW

Pfad: Schnittstellen > Formularserver SHK NRW
Quelle: handbuch/formularserver_shk_nrw.htm

|

Formularserver SHK NRW

Verfügbar ab der Version 5.87 (Sept. 2018)

Hintergrund

Der Fachverband SHK NRW hat einen Formularserver erstellt, mit dem man Formulare online ausfüllen und als PDF abspeichern kann.

Derzeit gibt es dort folgenden Formulare, aber weitere kommen wohl noch dazu.

-

Bescheinigungen nach § 66 BauO NW für diverse Anlagetypen

-

Unternehmererklärungen zur EnEV

-

Bescheinigungen nach der Lüftungsanlagenrichtlinie NRW

-

Prüfbescheinigung nach TRGI (Gasinstallationen)

-

Dichtheitsprüfung von Grundleitungen

-

Einwilligungserklärung gemäß DSGVO

Für die Benutzung des Formularservers müssen Sie dort kostenpflichtig registriert sein. Weitere Infos finden Sie unter https://www.formulare-shk.de, per E-Mail an erben@shk-nrw.de oder telefonisch unter 0211 69065-90.

Zu besseren Bedienung wurde eine Schnittstelle zwischen Labelwin und dem Formularserver (oder Formular-Assistent) definiert und erstellt.

Der Formularserver benötigt jeweils zwei Adressen. Die des Bauherren und die des Objektes. Diese Adressen können per Schnittstelle reingereicht werden. Außerdem regelt die Schnittstelle das Abholen und Speichern der ausgefüllten PDFs in Labelwin.

Ohne Schnittstelle müsste man die Adressen jeweils manuell dort eingeben, sowie die PDFs downloaden, lokal abspeichern und anschließend per Drag und Drop in das Projekt ziehen.

Einrichten der Schnittstelle

Als erstes müssen Sie sich auf dem Formularserver als Benutzer registrieren. Siehe Infos oben. Danach rufen Sie die Webseite auf und melden sich an.

[Bild]

Wählen Sie den Menüpunkt <Benutzer>. Dort finden Sie für jeden Benutzer einen Schnittstellenschlüssel, der in etwa wie folgt aussieht: 6810xb55d161727585e8643a1c70341531f4375fe9c6b

[Bild]

Kopieren Sie den Schlüssel mit STRG-C. Starten Sie das Labelwin Modul „Einstellungen“, starten Sie den Menüpunkt <Programmbereiche>, <Dokumentenerstellung>, <Grundeinstellungen> und wählen Sie links unter „Benutzer-Einstellungen“ die Option „Allgemeines“. Auf der rechten Seite können Sie den Schlüssel bei „Authorisierungskey für den Formularserver SHK NRW“ mit STRG-V einfügen. Dieses müssen Sie pro Benutzer machen.

Nutzen der Schnittstelle

Legen Sie in der Projektverwaltung ein neues Dokument von Typ „Anderes Dokument“ und dem Untertyp „PDF“ an. Erfassen bzw. wählen Sie zuerst beide Adressen aus. Über den Menüpunkt <Datei>, <Formularserver SHK NRW starten>, der nur erscheint, wenn Sie den persönlichen Authorisierungskey hinterlegt haben, wird die Webseite gestartet.

[Bild]

Melden Sie sich mit dem persönlichen Benutzernamen und Passwort an. Diese Daten können wir leider nicht per Schnittstelle reinreichen. Sie können aber im Internet-Browser das Speichern der Zugangsdaten erlauben.

Die beiden Adressen aus Labelwin sind entsprechend reingereicht worden. Sie können sofort ein Formular bearbeiten und speichern. Gehen Sie zurück in die Labelwin Dokumentenanlage und wählen Sie den nächsten Menüpunkt <Datei>, <Formularserver SHK NRW PDF abrufen>. Damit wird die letzte von Ihnen gespeicherte PDF abgerufen und in Labelwin hinterlegt. Nach dem Schließen der Dokumentenanlage mit der Schaltfläche „OK“ wird das PDF Dokument angezeigt. Sie können es jetzt ausdrucken, versenden etc.
