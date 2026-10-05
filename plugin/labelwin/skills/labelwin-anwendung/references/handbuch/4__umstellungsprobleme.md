# 4. Umstellungsprobleme

Pfad: Zeitwirtschaft > Mandantenverrechnung [Modul] > 4. Umstellungsprobleme
Quelle: handbuch/4__umstellungsprobleme.htm

|

4. Umstellungsprobleme

Wenn die vorne beschriebene Möglichkeit genutzt wurde, die Monteure bei jedem Mandanten anzulegen, gibt es ein Übergangsproblem. Die ‚falschen‘ Buchungen müssen abgerechnet werden, was nur geht, wenn die Monteure nicht auf Entlassen stehen.

Mit einer kleinen Programmierung haben wir die Möglichkeit geschaffen, alle alten Buchungen auf die ‚richtigen‘ Monteure umzusetzen. Dazu muss das Programm aber wissen, welcher Personaleintrag zu welchem richtigen Monteur gehört.

Schreiben Sie sich dazu die internen Nummern der Monteure auf, die erhalten bleiben sollen. Diese Nummer sehen Sie in der Personalerfassung:

[Bild]

Aktivieren Sie dann den Mandant, bei dem die Monteure auf entlassen gesetzt werden sollen und setzen diese auf ‚Entlassen‘ (erste Karteiseite)

[Bild]

Gehen Sie dann auf die Karteiseite Zuordnung, tragen in das Feld ‚Abteilung‘ xx ein und in das Feld ‚Funktion‘ die interne Nummer der Mitarbeiters, der bei den ‚falschen‘ Buchungen eingesetzt werden sollen. Vergessen Sie nicht jedes Mal den Speichern-Knopf zu drücken.

Bei dieser Zuordnung dürfen Sie keinen Fehler machen, da die Buchungen unwiderruflich umgesetzt werden.

Umgesetzt werden also alle Monteure, die auf entlassen stehen, im Feld Abteilung die beiden xx stehen und im Feld Funktion eine Zahl steht.

Zum Umsetzen müssen Sie bei der Hotline ein Passwort abfragen. Starten Sie dann das Modul ‚Datenbank aktualisieren‘ und wählen die Menüpunkte <Datei>, <Korrekturen>, <Monteurtausch> an. Nach Eingabe des Passworts werden dann alle Buchungen umgesetzt.
