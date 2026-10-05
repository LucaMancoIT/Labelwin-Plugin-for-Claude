# E-Mails aus David nach Labelwin

Pfad: Einrichtungsarbeiten > E-Mails aus David nach Labelwin
Quelle: handbuch/e_mails_aus_david_nach_labelwin.htm

|

E-Mails aus David nach Labelwin

Mit dem Labelwin David-Infocenter Script, das in das David-Infocenter eingebunden wird, können Sie E-Mails mit und ohne Dateianhang in die Labelwin Projektverwaltung, die Aufgabenverwaltung oder in das Kundendienstmodul übernehmen.

Der Textteil der E-Mail wird als Dokument E-Mail bzw. als Kundendienstauftrag übernommen. Die ggf. vorhandenen Dateianhänge der E-Mail können bei Bedarf als ‚Zugeordnete Dokumente’ hinter der Notiz oder dem Auftrag abgelegt werden.

Die E-Mail inkl. Anhang steht dann jedem Labelwin-Anwender zur Verfügung. Das Tobit David-Infocenter ist zum Lesen der hinterlegten E-Mails nicht mehr notwendig.

|

Hinweis: HTML-formatiere E-Mails werden beim Speichern in Labelwin auf den reinen Textteil reduziert.

Zum Anschauen der Dateianhänge müssen auf dem Arbeitsplatz die entsprechenden Programme je nach Datei-Extension hinterlegt sein. Dieses geschieht im Modul EINSTELLUNGEN unter dem Menüpunkt <Vorlagen> <Andere Dokumente> <Dokumententypen erfassen>.

Einbinden eines Labelwin DAVID Scripts

Dieses Script bietet die Möglichkeit, eine geöffnet E-Mail inkl. Anhang im David-Infocenter mit den Funktionen Aufgaben, Ablage und Kundendienstauftrag aus Labelwin zu verbinden.

[Bild]

Mit den folgenden Schritten wird die einfache Installation durchgeführt.

1. Labelwin Verzeichnisstruktur erweitern:

Sie müssen zunächst unterhalb von Labelwin ein Verzeichnis für die Zwischenablage der E-Mails anlegen, z.B. labelwin\tobitout

Dieses Verzeichnis wird mit der erfolgreichen Übergabe der E-Mail an Labelwin wieder geleert.

2. Labelwin Schnittstelle einfügen:

Die Datei mailin.exe muss in das Stammverzeichnis von Labelwin kopiert werden. Wenn Sie sich ein aktuelles Update über das Internet holen und einspielen, geschieht das automatisch.

3. Kopieren Sie dann das David-Script „Labelout.vbs“ in die David Verzeichnisstruktur und passen Sie diese auf Labelwin an. Sie finden das Script im Verzeichnis labelwin\vorlage.

Die Datei Labelout.vbs muss dann im Verzeichnis David\Code\Scripts auf dem Server gespeichert werden.

[Bild]

[Bild]

Editieren der Script-Datei Labelout.vbs

Öffnen Sie die Datei „Labelout.vbs“ mit einem Editor, z.B. Notepad.

Die Einträge ‚Einstellungen(0)’ und ‚Einstellungen (1)’ müssen dem Verzeichnis Ihrer Labelwin-Installation angepasst werden. Bitte beachten Sie, dass dieser Eintrag für alle Label Benutzer und David Anwender gleich ist.

[Bild]

David Benutzer administrieren

[Bild]

Öffnen Sie (oder der Administrator) den David Administrator auf dem Server. Gehen Sie dort in die Benutzerverwaltung und öffnen den David Benutzer.

Im Register Benutzerdaten muss ein Häkchen für individuelles Script gesetzt und das Script „Labelout.vbs“ eingetragen werden.

Diesen Vorgang müssen Sie für jeden Benutzer durchführen, der die Labelwin David-Schnittstelle nutzen soll.

David Infocenter neu starten

Jetzt muss das David-Infocenter auf den Arbeitsplätzen beendet und neu gestartet werden. Bitte beachten Sie, dass das Infocenter nicht nur geschlossen wird. Wenn es als Sys Try-Symbol (als kleines Symbol sichtbar in der Windows-Taskleiste) weiter aktiv ist, müssen Sie das Icon mit der rechten Maustaste anklicken und im Kontextmenü den Punkt ‚Beenden’ anwählen.
