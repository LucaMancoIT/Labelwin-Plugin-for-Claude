# 2.10 Lager

Pfad: Einrichtungsarbeiten > Einstellungen [14] > 2. Programmbereiche > 2.10 Lager
Quelle: handbuch/2_10_lager.htm

|

2.10 Lager

Bevor Sie diesen Menüpunkt anwählen können, müssen Sie mindestens ein Projekt als Lager angemeldet haben. Die Lageranmeldung geschieht im Projekt-Datenblatt durch Setzen eines Kreuzes auf der Karteikarte Grunddaten im Eingabefeld ‚als Lager verwenden’. Es ist erforderlich, ein Projekt speziell als Hauptlager zu deklarieren. Das Hauptlager wird benötigt, damit das Programm Bestellungen, Inventurtexte und dergleichen in einem Projekt ablegen kann.

[Bild]

Bild: Lager-Einstellungen Wareneingang

[Bild]

1 Hauptlager: Wählen Sie hier zwischen den Projekten, die als Lager gekennzeichnet sind, eines als Hauptlager aus.

[Bild]

2 Fehlende Artikel anlegen: In diesem Bereich legen Sie fest, ob beim Einbuchen von Wareneingängen (über Bestellungen) nicht auf dem Lager vorhandene Artikel angelegt werden sollen. In der Regel ist es sinnvoll, diesen Bereich auf nie oder fragen zu stellen. Jeden Artikel, der eingeht, als Lagerartikel anzumelden, ist in der Regel nicht sinnvoll.

[Bild]

3 Fehlende Lagerorte anlegen: Wenn ein Artikel im Hauptlager vorhanden ist, ist er dennoch nicht automatisch dem Unterlager bekannt. Falls Sie beim Wareneingang die Eingänge auf ein Unterlager buchen, kann hier festgelegt werden, ob neue Artikel automatisch als Lagerort im Unterlager angelegt werden sollen.

[Bild]

4 Wareneingang für Projektbestellungen: Hier besteht die Möglichkeit Artikel, die standardmäßig auf dem Lager geführt werden, auch bei einem Wareneingang aufs Projekt dem Lager zuzubuchen.

Problem: Ein Handwerker bestellt z.B. für einen großen Auftrag neben diversen Sonderartikeln 100 Eckventile für die Baustelle, obwohl er genau diese Eckventile standardmäßig auf dem Lager führt. Mit dieser Möglichkeit können Sie jene 100 Eckventile bei der Einbuchung aufs Projekt gleichzeitig als Bestand im Lager zu buchen. Damit stimmt zwar der Lagerbestand im eigentlichen Lagerfach nicht, aber zusammen mit dem Bestand im Kommissionslager passt er. Sobald die Artikel aus dem Kommissionslager als Lieferschein gedruckt und gebucht werden, stimmt der Bestand auch im Lagerfach wieder.

[Bild]

5 Email an Projektverantwortlichen bei Wareneingang: Wenn im Projektdatenblatt der Verantwortliche (meist als Bauleiter bezeichnet) eingetragen ist, kann bei Wareneingang eine Email an ihn geschickt werden. Diese Email ist zusätzlich zu der bei der Bestellanlage gewählten Benachrichtigung.

Da die Email-Empfänger vor dem Versand gezeigt werden, sind jederzeit Korrekturen möglich.

[Bild]

6 mündliche Bestellungen mit EK2 statt EK1 einbuchen: Wenn der Lagerwert durch die Preise der eingekauften Artikel festgestellt werden soll, ist die Frage, woher der Preis schon beim Buchen des Wareneingangs herkommen soll. In der Regel ist es der ‚normale' Preis aus den Stammdaten. Dieser wird jedoch durch die Lieferanten-Datanorm ggf. geändert, so dass manche Anwender mit einem eingetragenem EK 2 arbeiten.

[Bild]

7 kein Druck mit Abbuchung bei negativem Bestand: Wenn bei einer Abbuchung per Rechnung oder Lieferschein ein negativer Bestand von einem (oder mehreren) Artikel(n) entsteht, kann eigentlich etwas nicht stimmen. Wenn Sie dieses Feld aktivieren, wird eine Druckausgabe verweigert, anderenfalls erfolgt nur ein Hinweis darauf.

[Bild]

8 Ausdruck Lagerentnahmen: Wenn Sie dieses Feld aktivieren, haben Sie die Möglichkeit, dass Lagerentnahmen ohne Ausdruck beim Verlassen des Artikelaufrufs gebucht werden. Es erfolgt eine Sicherheitsabfrage. Des Weiteren müssen Sie hier ein Lager für die Materialzettel vorgeben.

[Bild]

9 Kalkulation: Wenn man beim Wareneingang den Druck von Preisetiketten ausgewählt hat, wird im Ablageprojekt ein freier Text angelegt. Die Preise der Positionen in diesem Dokument werden aufgrund der hier hinterlegten Kalkulationseinstellung errechnet.

[Bild]

10 Ablageprojekt: Tragen Sie hier das Ablageprojekt für die Dokumente ein, die beim Wareneingang erzeugt werden.

[Bild]

11 Bei Wareneingang Lieferscheine anlegen: Wenn Sie dies aktivieren, wird neben dem Eingangslieferschein zusätzlich ein Lieferschein mit den eingegangenen Materialien angelegt.

Bei der Option ‚Sammellieferschein' wird ggf. ein noch nicht gedruckter, offener Lieferschein vom Projekt oder dem KD-Auftrag gesucht und die neuen Artikel angehängt. Wenn keiner existiert, wird er angelegt.

Kommissionsfach nicht prüfen: Dieses Feld ist nur sichtbar, wenn Sie die Option ‚Sammellieferschein‘ gewählt haben. Bei der Anlage von Lieferscheinen wird beim Buchungsvorgang eine Kommission abgefragt. Ohne diese Option wird auf eine fehlende Eingabe hingewiesen

[Bild]

12 Kommissionsfach nicht prüfen: Bei der Anlage von Lieferscheinen wird beim Buchungsvorgang eine Kommission abgefragt. Ohne diese Option wird auf eine fehlende Eingabe hingewiesen

[Bild]

13 Lageradresse: Die Lageradresse wird an zwei Stellen im Programm eingesetzt:

Bei der Bestellzerlegung: Hier kann dem Dokument, in dem die vom Lager zu entnehmenden Artikel hinterlegt werden, diese Adresse zugeordnet werden.

Beim Wareneingang: Die beim Lager ‚bestellten’ Artikel können genauso eingebucht werden, wie die Lieferungen vom Großhandel. Dazu wird als Lieferantenadresse genau jene Lageradresse gewählt. In diesem Fall wird dann beim Buchen der Materialien kein Eingangslieferschein, sondern eine Lagerentnahme erzeugt.

[Bild]

14 kein Hinweis auf offene Bestellung (Recnungen): Beim Schreiben einer Rechnung erfolgt eine Warnung, wenn im Projekt noch offene Bestellungen vorhanden sind.

Wenn der Wareneingang nicht vorgenommen wird, stört diese Meldung, weil ja dann fast immer offene Bestellungen im Projekt liegen.

Hier kann diese Warnung deaktiviert werden.

Sobald Sie den Wareneingang nutzen oder die Bestellungen beim Einbuchen der Eingangsrechnung erfasst werden, sollten Sie die Warnung wieder aktivieren

[Bild]

15 Maschinenabhängige Einstellungen: Hier haben Sie die Möglichkeit, dass Lieferscheine (Wareneingang) und Bestellvorschläge sofort ausgedruckt werden können. Wenn die diese Optionen akvitieren, müssen Sie über den Knopf ‚Einstellung‘ die Vorgaben für den automatischen Druck erfassen.

[Bild]

16 Ok: Durch Betätigen dieses Knopfes werden die vorgenommenen Einstellungen abgespeichert.

[Bild]

17 Abbruch: Durch Betätigen dieses Knopfes werden alle ggf. vorgenommenen Änderungen verworfen und die bisherigen Einstellungen bleiben erhalten.
