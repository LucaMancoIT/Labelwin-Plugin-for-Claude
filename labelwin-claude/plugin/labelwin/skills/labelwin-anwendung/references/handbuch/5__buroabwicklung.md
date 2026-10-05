# 5. Büroabwicklung

Pfad: Kundendienst > KD-Mobil Notebook [Modul] > 5. Büroabwicklung
Quelle: handbuch/5__buroabwicklung.htm

|

5. Büroabwicklung

Erledigte Aufträge in Zentrale importieren

1. Stehen die Aufträge per Cloud-Abgleich zur Verfügung könnte man diese wie beim E-Mail Import (siehe Punkt 2) per Doppelklick importieren. Dazu müsste man aber alle Importpfade prüfen, was beim Einsatz mehrerer Monteure etwas umständlich ist. Wir empfehlen daher entweder das Import-Modul kdimport.exe in den Programmbaum einzubinden und dann über den „Rundruf“ alle Pfade gleichzeitig abzufragen oder noch einfacher den gelben Button „NEUE AUFTRÄGE“ zu verwenden.

Dieser muss in den Laptop Grundeinstellungen aktiviert werden (unter Mobil - Laptop Grundeinstellungen - "Knopf für Auftrag holen sichtbar") und erscheint danach immer automatisch in der Statusleiste der Kundendienst-Maske, wenn ein Auftrag in einem der Cloud Pfade liegt.

[Bild]

Dieser Button ist identisch zu dem auf dem Laptop (siehe Kapitel KD-Mobil: Import der Daten vom Büro).

2. Wenn Sie die Daten als E-Mail bekommen, müssen Sie beim ersten Mal auch die Doppelklick-Funktion einrichten. Gehen Sie dazu vor wie im Kapitel Import / Doppelklick-Funktion bei der Notebookeinrichtung beschrieben. Es handelt sich hier aber um eine Datei mit der Endung .labelze.

[Bild]

Neue Adresse

Wenn auf dem mobilen Gerät ein (Notdienst-)Auftrag angelegt worden ist, ist dabei möglicherweise eine neue Adresse erfasst worden. In diesem Fall wird die neue Adresse gezeigt und es besteht die Möglichkeit, die Daten stattdessen einer bereits vorhandenen Adresse zuzuordnen.

[Bild]

Die gleiche Möglichkeit besteht bei einer Anlage, die vom Techniker vor Ort angelegt wurde. Wenn die Adresse in der Zentrale noch keine Anlage hat, so wird die neue Anlage mit allen dazu gehörenden Informationen (Karteikarte, Messwerte) ohne Nachfrage übernommen. Wenn die Adresse bereits mindestens eine Anlage hat, so werden diese in einer Tabelle gezeigt. Es besteht dann die Auswahl, die neue Anlage neu anzulegen oder die neue Anlage auf eine bereits bestehende Anlage zu zuordnen. Im letzten Fall wird aber wieder nur die Karteikarte übertragen – die Anlageinformationen selber werden nicht geändert.

Die importierte Datei wird umbenannt (.sic), so dass Sie die gleiche Datei nicht noch mal importieren. In den Einstellungen kann man auch einen Sicherungspfad hinterlegen in den die eingelesenen Dateien verschoben werden.

Die Import-Dateien haben als Kennung im Datennamen die Notebook-Nr. und eine fortlaufende Zahl, z.B. NB1-12.labelze. Beim Importieren achten wir auf die Nummerierung und bringen Ihnen einen Hinweis, wenn von diesem Notebook nicht die fortlaufenden Dateien eingelesen wurden.

Büroarbeiten

Bevor wir die erforderlichen Arbeiten schildern, möchten wir die Frage klären, woran man im Büro erkennt, dass ein Auftrag zurückgekommen ist.

Sinnvoll ist es, die Auftragsliste so zu gestalten, dass ein Exportkennzeichen sichtbar ist. Also eine Spalte "N" in der z.B. ein X steht, wenn der Auftrag exportiert worden ist. Damit erkennt man aber nicht, wenn ein Auftrag zurückgekommen ist. Ggf. steht der Status auf „erledigt“, aber auch das ist nicht immer der Fall. Deshalb gibt es ein Rückübertragungs-Datum. Gefüllt wird es in dem Moment, wenn ein Auftrag im Büro importiert wird. Deshalb sollte auch dieses Feld sichtbar gesetzt werden. Außerdem empfiehlt es sich die Büro-Informationen einzublenden. Hier erscheint der Text, den der Monteur speziell für das Büro in dem Auftrag hinterlassen hat.

[Bild]

Die Anzeige der sichtbaren Spalten wird über eine TAB-Datei gesteuert. Sie können TAB-Dateien im Modul EINSTELLUNGEN unter <Optionen><TAB-Dateien bearbeiten> selbst anlegen und modifizieren. Sprechen Sie alternativ Ihren Labelwin-Betreuer an.

|

Info: In MyLabelwin Wiki gibt es im Bereich „Lernvideos und Tutorials“ eine detaillierte Anleitung zur Erstellung von TAB-Dateien mit dem Namen „ TAB Dateien selber anpassen “.

Des Weiteren besteht die Möglichkeit Aufträge, die vom Laptop zurückkommen, mit einer gesonderten Priorität zu versehen (und somit auch farblich kenntlich zu machen). Ist das der Fall können Laptop Aufträge auch über die Priorität gefiltert bzw. erkannt werden. Details zur Einrichtung finden Sie in Kapitel Einstellungen Zentrale.

Was mit einem Auftrag noch geschehen muss, hängt davon ab, wie weit er vom Techniker vor Ort zu Ende gebracht worden ist. Wenn er die Rechnung gestellt und möglicherweise auch schon abgerechnet hat, ist damit alles erledigt. Oft wird es aber noch Arbeiten im Büro geben, bevor die Abrechnung erfolgen kann.

Wir empfehlen Ihnen hierzu mit der Prüfmöglichkeit zu arbeiten. Dieses Kennzeichen ist im Grunde genommen immer sinnvoll, auch wenn kein mobiler Kundendienst genutzt wird. Wenn alles in Ordnung ist, setzen Sie den Haken „geprüft“ (unten rechts).

[Bild]

Die Prüfmöglichkeit muss einmalig im Einstellmodul aktiviert werden (Programmbereiche, Kundendienst, Grundeinstellungen, Allgemein).

[Bild]

In der Maske der Auftragsliste kann nun auf Aufträge eingegrenzt werden, die noch nicht geprüft sind. Diese Aufträge öffnen Sie und prüfen, ob noch Folgearbeiten erforderlich sind (Button Büro-Info ist ggf. rot), ob das eingetragene Material passt oder etwas fehlt, ob die Ankreuzfelder und Eingaben der Abschlussarbeiten richtig gesetzt wurden usw.

Um die Rechnungen nur für die geprüften Aufträge zu schreiben, grenzen Sie die Auftragsliste auf die erledigten und geprüften Aufträge ein.
