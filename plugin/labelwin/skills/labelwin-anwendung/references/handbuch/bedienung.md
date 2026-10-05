# Bedienung

Pfad: Einrichtungsarbeiten > E-Mails aus Outlook nach Labelwin > Bedienung
Quelle: handbuch/bedienung.htm

|

Bedienung

-

Öffnen Sie ein Email in Outlook.

-

Klicken Sie auf die neu angelegte Schaltfläche ‚Labelwin.KDAuftrag’. Das Fenster zum Anlegen eines Kundendienstauftrages wird automatisch geöffnet. Der Text der Email steht im Auftragstext.

-

Erfassen Sie jetzt die Adresse und alle weiteren Informationen. Leider liefert Outlook in der Schnittstelle die Original-Emailadresse nicht mit, so dass wir die Adresse nicht automatisch passend vorschlagen können.

-

Wenn die Email Dateianhänge hat öffnet sich nach dem Speichern des Auftrages eine Liste der Dateianhänge zum Auswählen. Die ausgewählten Dateianhänge werden hinter dem Auftrag als zugeordnetes Dokument abgelegt und können über den Knopf ‚Zugeordnete Dokumente’ wieder aufgerufen werden.

-

Statt einen KD-Auftrag anzulegen, können Sie in Punkt 2 auch ein Dokument in einem Projekt anlegen. Es öffnet sich dann das Fenster der Dokumentenneuanlage mit der Vorbelegung ‚Email’. Nach Betätigen des Okay-Knopfes kommt hier ebenfalls das Fenster mit den Dateianhängen. Hier besteht jedoch die Möglichkeit, nur die Anhänge abzulegen. In diesem Fall fehlt einfach die Email, der in der ursprünglichen Email vorhandene Text geht also verloren.

[Bild]

Ablage einer Email im Original

Sie haben die Möglichkeit eine Email im Original abzulegen. Eine so gespeicherte Email können Sie dann aus Labelwin heraus per Doppelklick mit der Outlook-Oberfläche im Original betrachten, auch wenn die Email im Outlook selbst nicht mehr zur Verfügung steht.

Wenn Sie die Outlookmakros bereits eingebunden haben, genügte es die Inhalte auszutauschen. Öffnen Sie dazu die Datei labelwin\vorlage\labelout.bas mit dem Editor (rechte Maustaste > Öffnen mit > Editor), markieren Sie mit Strg+A den gesamten Text und kopieren sie ihn mit Strg+C in die Zwischenablagen. Öffnen Sie dann im Outlook mit den Tasten Alt+F11 den makroeditor und tauschen Sie den kompletten Text aus. Ggf. bitten Sie Ihren Hardwarebetreuer um Hilfe.

Nach dem Austausch müssen Sie nur in der 10. Zeile (labelpfad = H:\labelwin\) den für Sie richtigen Plattenbuchstaben eintragen.

Damit ist die Einrichtung fast abgeschlossen. Nun muss nur noch der Domumententyp msg eingetragen werden. Öffnen Sie dazu im Modul EINSTELLUNGEN den Menüpunkt <Vorlagen> <Andere Dokumente> <Dokumenttypen erfassen>.

[Bild]

Der hier eingesetzte Pfad h:\labelwin\emails muss ggf. angelegt werden, da er standardmäßig nicht existiert.

Wenn der Outlookpfad vorgeschlagen wird, muss dieser noch um Leerstelle /f erweitert werden. Wenn die Option /f nicht eingesetzt ist, wird statt der Betrachtung eine neue Mail vorgeschlagen, bei der die abgelegte Email als Anhang eingetragen ist. Durch /f wird erreicht, dass die Email angezeigt wird.

Bei der Ablage von Emails sieht die Ablagemaske etwas anders aus:

[Bild]

Im obigen Bild wird nur die Email mitsamt ihren Anhängen abgelegt. Die Anhänge selbst sind nicht angekreuzt, weil diese ja zusammen mit der Original-Email abgelegt werden. Wenn Sie wollen, können Sie natürlich auf die Ablage der Original-Email verzichten und nur die Anhänge ablegen.
