# Installation

Pfad: Einrichtungsarbeiten > E-Mails aus Outlook nach Labelwin > Installation
Quelle: handbuch/installation_2.htm

|

Installation

1. Starten Sie Outlook

2. Zunächst muss in Outlook eingestellt werden, dass man die Visual-Basic-Umgebung erreichen kann. Dazu wählen Sie das Menü „Datei, Optionen“.

3. Im folgenden Fenster mit dem Titel „Outlook-Optionen“ wählen Sie links den Punkt „Menüband anpassen“. Im rechten Bereich setzen Sie die Checkbox bei „Entwicklertools“. Klicken Sie „OK“. Nun befindet sich im Outlook-Menü auch der Eintrag „Entwicklertools“. Wählen Sie diesen.

[Bild]

4. Öffnen Sie die Visual-Basic Umgebung, indem Sie links im Entwicklertools-Menü auf „Visual Basic“ klicken. (alternativ nutzen Sie die Tastenkombination: ALT + F11).

5. Ggf. im Folgefenster den Knopf ‘Makros aktivieren” betätigen.

6. Sie sehen folgendes Fenster

[Bild]

7. Importieren Sie das Labelwin Outlook Makro über den Menüpunkt ‚Datei, Datei importieren’

[Bild]

8. Die zu importierende Datei heißt labelout.bas. und liegt im Verzeichnis \labelwin\vorlage\

[Bild]

9. Sie haben danach im linken Fenster einen weiteren Eintrag ‚Module’

[Bild]

10. Klicken Sie dann auf das +-Zeichen vor dem Eintrag ‚Module’. Durch einen Doppelklick auf

das Wort ‚Modul1’ dann erscheint der Text des Makros.

Nun ändern Sie den Eintrag H:\labelwin auf das Verzeichnis, in dem bei Ihnen das Labelwin installiert ist.

[Bild]

11. Wählen Sie den Menüpunkt ‚Extras, Eigenschaften von Projekt’.

[Bild]

12. Ändern Sie den Namen ‚Projekt1’ auf ‚Labelwin’ ab und klicken Sie auf OK.

[Bild]

13. Wählen Sie den Menüpunkt ‚Extras, Verweise’.

Setzen Sie einen Haken bei folgenden zwei Einträgen:

- Microsoft Scripting Runtime

- Microsoft XML, Version 3.0

[Bild]

Sie finden die Einträge weit unten in der alphabetisch sortierten Liste.

Bestätigen Sie Auswahl mit OK.

Zur Kontrolle können Sie den Menüpunkt nochmals aufrufen. Dann müssen die beiden Einträge ausgewählt oben stehen (so ähnlich wie abgebildet)

14. Wählen Sie den Menüpunkt ‚Datei, Labelwin speichern aus. Danach: Wählen Sie den Menüpunkt ‚Datei, VBAProjekt.OTM speichern aus.

15. Beenden Sie den Outlook Visual Basic Editor UND das komplette Outlook

16. Starten Sie Outlook erneut .

17. Wählen Sie den Menüpunkt „Datei, Optionen, Sicherheitscnter“ aus.

Im rechten Fensterbereich sehen Sie dadurch die Schaltfläche „Einstellungen für das Sicherheitscenter…“ Klicken Sie diese. Sie gelangen in das Fenster:

[Bild]

Wählen Sie die Option „Benachrichtigung für alle Makros“ und klicken Sie OK.

18. Öffnen Sie eine beliebige Eingangs-Email

19. Klicken Sie auf den kleinen Pfeil in der Schnellzugriff-Symbolleiste und wählen den Menüpunk „Weitere Befehle“

[Bild]

20. Wählen Sie ‚Makros’ in der Combobox Befehle auswählen: aus und fügen die Makros „Labelwin.Ablage“, „Labelwin.Aufgabe“ und „Labelwin.KD-Auftrag“ der Symbolleiste für den Schnellzugriff hinzu.

[Bild]

21. Sie können das Aussehen des Eintrags und der Verknüpfung ändern, indem Sie den Eintrag markieren und auf den „Ändern“-Button klicken.

[Bild]

[Bild]

Schließen Sie das Fenster und das Makro ist eingerichtet.

22. In der geöffneten Email finden Sie nun in der Schnellzugriffs-Symbolleiste die Symbole für „Labelwin.Ablage“, „Labelwin.Aufgabe“ und „Labelwin.KD-Auftrag“. Ggf. dargestellt mit den von Ihnen eingestellten Symbolen.

[Bild]
