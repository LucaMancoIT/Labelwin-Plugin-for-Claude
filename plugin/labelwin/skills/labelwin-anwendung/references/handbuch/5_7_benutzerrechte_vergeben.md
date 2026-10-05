# 5.7 Benutzerrechte vergeben

Pfad: Einrichtungsarbeiten > Einstellungen [14] > 5. Optionen > 5.7 Benutzerrechte vergeben
Quelle: handbuch/5_7_benutzerrechte_vergeben.htm

|

5.7 Benutzerrechte vergeben

In größeren Betrieben ist es unumgänglich, manche Programmbereiche für einzelne Anwender oder Anwendergruppen zu sperren.

Der Schutz einzelner Programmbereiche über Zugangsberechtigungen ist nur dann aktiv, wenn dieses in der im Folgenden beschriebenen Maske angekreuzt worden ist. Anderenfalls sind sämtliche Programmbereiche für alle Benutzer frei verfügbar.

|

Hinweis für die ‚alten‘ Label-Anwender:

Früher waren die Rechte negativ formuliert, man musste also ankreuzen, was jemand nicht durfte. Diese Logik wurde gedreht. Nun wird das Kreuz entfernt, wenn jemand ein Recht nicht hat. Bisher vergebene Rechte bleiben aber unverändert.

Die Benutzergruppen wurden erst später programmiert, um die Vergabe zu vereinfachen. Ein neuer Nutzer kann nun einer oder mehreren Gruppen zugeordnet werden und hat damit sehr schnell die passenden Rechte.

Ein Problem bei der Konstruktion war, dass sich die Rechte von Gruppen überschneiden können. Wenn ein Mitarbeiter zur Gruppe A gehört, bei der z:B. das Recht für den Rechnungseingang fehlt und er auch zur Gruppe B gehört, die das Recht hat – welches sollte dann gelten? Die Lösung war, dass wir die Rechte quasi addieren. Sobald ein User ein bestimmtes Recht in irgendeiner Gruppe hat, gilt das Recht für ihn.

Zusätzlich kann jeder Mitarbeiter individuelle Rechte bekommen. Diese werden in die ‚Addition‘ ebenfalls einbezogen. Ein individuelles Recht kann aber nur vergeben werden, wenn der Mitarbeiter dieses nicht bereits über eine zugeordnete Gruppe besitzt. Ein Recht über eine Gruppe hat Vorrang und kann nicht individuell weggesetzt werden. Wenn ein Mitarbeiter keiner Gruppe angehört, sind alle seine Rechte individuell.

Bei aktivierter Rechtevergabe muss jeder Benutzer neben der für ihn erforderlichen Installation zusätzlich in der Personalerfassung angemeldet werden. Dort muss bei ‚Labeluser‘ der Windows-Anmeldename eingetragen werden.

Um es für Sie einfacher zu gestalten, wie die Benutzergruppen und Mitarbeiter mit Rechten versehen sind, ist die Ausgabe in eine Excel-Tabelle möglich.

Excel-Tabelle zur Prüfung

Da die Ausgabe der Rechte auch sehr gut zur Planung einzusetzen ist, hier die Beschreibung als Erstes. Sobald Sie einen Mitarbeiter oder eine Gruppe eingerichtet haben, ist die Ausgabe möglich.

Beispiel:

Mitarbeiter Willy gehört den Gruppen Bauleiter und Kalkulation an.

Bei dem Recht ‚Ändern Datum des Status‘ hat er ein individuelles Recht.

[Bild]

Ein vorhandenes Recht ist über den Buchstaben G oder X zu erkennen. Der Buchstabe G steht für Gruppenrecht.

Benutzergruppen

Wer mit Benutzergruppen arbeiten will, muss zwingend alle Mitarbeiter mit PC-Einsatz in den Personaldaten eintragen. Für die Benutzerrechte ist der Eintrag auf der 2. Karteiseite ‚Labeluser‘ wichtig. Dort muss der Windows-Anmeldename des Benutzers eingetragen werden.

Die Verwaltung über Benutzergruppen muss speziell aktiviert werden. Wählen Sie dazu den Menüpunkt <Datei> <Benutzergruppen aktivieren>.

Sollte die Aktivierung nicht möglich sein, weist das Programm auf die Fehlerquelle hin, und Sie müssen nach Korrektur den Menüpunkt erneut anwählen.

Erfassen / Ändern von Rechten

Wenn in der Maske die Anzeige eines einzelnen Anwenders sichtbar sind, werden die Rechte über die Gruppen abgeblendet angezeigt. Man kann ein Recht also nicht individuell wegsetzen, wenn es über eine Gruppe festgelegt wurde. Natürlich ist es in der eigentlichen Anwendung gleichgültig, ob das Recht über einen individuellen Eintrag oder eine Gruppe entstanden ist. Allerdings kann dies bei der Einrichtung der ganzen Rechte schon interessant sein, weil man dann die Gruppen ggf. etwas geringer mit Rechten ausstatten muss.

[Bild]

Bild: Rechteverwaltung Benutzergruppen

[Bild]

1 Rechtverwaltung aktiv: Nur wenn in diesen Feld aktiviert haben, werden individuelle Rechte berücksichtigt. Bei Nichtaktivierung dürfen grundsätzlich alle Anwender das Programm in allen Bereichen anwenden. Um die unzulässige Veränderung von Rechten zu verhindern, sollten Sie unbedingt ein Kennwort eingeben.

Wenn Sie das Passwort vergessen, kann Label mit einigem Aufwand eine Freischaltung vornehmen, die kostenpflichtig ist. Wenn Sie also mit Passwort arbeiten, sollten Sie es sich unbedingt merken!

[Bild]

2 Kennwort vergeben: Durch das Kennwort wird die komplette Rechtevergabe abgesichert. Es nutzt nichts, einem Anwender bestimmte Rechte nicht zu geben, wenn er diese selbst abändern kann. Eine Rechtevergabe ohne Kennwortschutz gibt also keinen Sinn. Bitte beachten Sie, dass Sie das Kennwort auf keinen Fall vergessen dürfen. Auch wir können das Passwort nur mit einigem Aufwand und Prüfungen deaktivieren. Dabei achten wir natürlich streng darauf, ob der Anrufer das überhaupt darf. Den Zeitaufwand von ca. einer Stunde würden wir Ihnen in diesem Fall in Rechnung stellen.

[Bild]

3 Benutzergruppen: Durch Aktivierung dieses Feldes können Sie mit Benutzergruppen arbeiten. Das bedeutet, dass Sie mehrere Mitarbeiter einer bestimmten Gruppe oder mehreren Gruppen zuordnen können. Das Zuordnen zu einer Gruppe erspart bei größeren Firmen, dass die Rechte für jeden Mitarbeiter einzeln festgelegt werden müssen.

Für Umsteller von Einzel auf Gruppenrechte: Nur nach Anwahl des Menüpunkts <Datei> <Benutzergruppen> und abarbeiten der dort hinterlegten Prüfungen kann mit Gruppenrechten gearbeitet werden.

[Bild]

4 Benutzerliste: Hier werden Ihnen je nach Auswahl die Benutzergruppen oder die Mitarbeiterliste gezeigt. Die Rechte werden für den geraden aktiven Eintrag eingestellt.

[Bild]

5 Bereich: Wählen Sie hier den Bereich aus, in dem Sie etwas ändern möchten. Je nach gewähltem Bereich, ändern sich die Auswahlfelder (Nr. 6).

[Bild]

6 Auswahlfelder: Wählen Sie hier aus, welche Rechte der Mitarbeiter oder die Gruppe haben soll. Wegen der Vielzahl von Möglichkeiten liegen die Felder auf Karteikarten 1- 6.

|

Die folgenden Erklärungen gelten immer für die aktive Benutzergruppe oder den Benutzer. Je nachdem, ob das Feld ‚Benutzergruppe‘ (Feld 3) angehakt ist oder nicht, wechselt die Beschriftung der Knöpfe

[Bild]

7 Neue Gruppe / Neuer Benutzer: Durch Betätigen dieses Knopfes können Sie eine neue Benutzergruppe anlegen.

[Bild]

[Bild]

8 Gruppe / Benutzer kopieren: Durch Betätigen dieses Knopfes können Sie die Rechte der aktiven Eintragung auf eine neue Gruppe / Benutzer kopieren. Das Programm fragt dann nach dem neuen Namen.

[Bild]

9 Gruppe ändern: Durch Betätigen dieses Knopfes können Sie den Namen einer Benutzergruppe ändern.

[Bild]

10 Gruppe löschen: Hier haben Sie die Möglichkeit, eine Benutzergruppe zu löschen. Bedenken Sie dabei bitte, dass beim Löschen einer Benutzergruppe die Rechte dieser Gruppe bei ALLEN Mitarbeitern weggesetzt werden, die dieser Gruppe zugeordnet waren.

[Bild]

11 Gruppen zuordnen: Durch Betätigen dieses Knopfes werden die Mitarbeiter einer Gruppe geordnet. Wählen Sie dazu im Auswahlmenü die gewünschte Gruppe aus und ordnen Sie die entsprechenden Mitarbeiter zu. Mit dem Pfeil nach rechts werden die Mitarbeiter der Benutzergruppe zugeordnet, mit dem Pfeil nach links wieder aus der Gruppe heraus genommen.

[Bild]

[Bild]

12 Excel: Um es für Sie einfacher und übersichtlicher zu gestalten, wie die Benutzergruppen und Mitarbeiter mit Rechten versehen sind, ist die Ausgabe in eine Excel-Tabelle möglich.

[Bild]

13 Speichern: Falls Sie Veränderungen bei den Rechten vorgenommen haben, so müssen Sie diese durch den Knopf ‚Speichern’ absichern.

[Bild] 14 Ende: Durch Betätigen dieses Knopfes wird die Maske geschlossen.

Die Menüpunkte im Einzelnen:

[Bild]

Datei

Benutzergruppe aktivieren

Dieser Menüpunkt muss nur einmalig betätigt werden, wenn die Gruppen aktiviert werden sollen. Falls schon Rechte für einige Mitarbeiter eingetragen sind, führt das Programm einige Prüfungen durch und weist die Umstellung ggf. ab. In der Regel wird es sich um fehlende Einträge in der Personalverwaltung handeln.

Alle Rechte aktivieren

Alle Rechte deaktivieren Manchmal spart es eine Menge anklicken, wenn die Rechte auf einmal gesetzt oder weggesetzt werden können.

Anzuzeigende Auswertungen im Startcenter (Karteiseite 7)

Hier haben Sie die Möglichkeit, die anzuzeigenden Auswertungen entweder individuell für jeden Mitarbeiter oder für eine Benutzergruppe festzulegen.

[Bild]

Auch hier gilt die Regel, dass eine Auswertung von der Benutzergruppe vererbt wird. Diese sind durch das voran gestellt (G) zu erkennen. Sie können beim Benutzer nicht entfernt werden. Lediglich die Reihenfolge der Auswertung ist über die Knöpfe Pfeil-hoch und Pfeil-runter individuell einzustellen.

Wenn eine Auswertung bei einer Benutzergruppe nachträglich entfernt wird, verschwindet sie automatisch bei allen Benutzern.

Berechtigungsschlüssel (Bereich Schlüssel)

Dieser Bereich steht nur zur Verfügung, wenn die Schlossverwaltung in Labelwin aktiv ist, also wenn Schlösser angelegt sind. Die Beschreibung dazu finden Sie im nächsten Kapitel Berechtigungsschloss.

Mit einem Schloss können Projekte, Dokumente, Bankkonten usw. für Mitarbeiter gesperrt werden, die keinen Schlüssel für das jeweilige Schloss haben.

An dieser Stelle wird dem Mitarbeiter sinngemäß ein Schlüsselbund gegeben.

Auch hier gilt die Regel, dass eine Auswertung von der Benutzergruppe vererbt wird.
