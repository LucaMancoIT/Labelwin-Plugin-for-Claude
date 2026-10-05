# Verarbeitungsoptionen: 90er Phase

Pfad: Dokumentenbearbeitung > Dokumentenerstellung [3] > GAEB > Gaeb einlesen > Verarbeitungsoptionen: 90er Phase
Quelle: handbuch/verarbeitungsoptionen__90er_phase.htm

|

Verarbeitungsoptionen: 90er Phase

[Bild]

[Bild]

B1 Katalog: In der 90er-Phase ist die Angabe eines Kataloges eigentlich immer notwendig. Mit der Phase 94 bekommen Sie von den Großhändlern bepreiste Artikel mit Artikelnummern zurück. In diesem Fall wird die Artikelnummer und der Katalog in der Position gespeichert.

Zusätzlich wird dieser Katalog gefüllt, wenn die Option ‚Artikel in Katalogstammdaten anlegen/ändern’ gewählt wird.

[Bild]

B2 Kostenarbeiten Zuordnung: Bitte ordnen Sie ggf. enthaltene Preise in der GAEB Datei den Label Kostenarten zu.

[Bild]

B3 Verkaufspreise mit aktueller Kalkulation neu kalkulieren: Wenn Sie per GAEB Preise als Einkaufpreis einlesen, z.B. weil Sie per GAEB Preise von einem Lieferanten oder Subunternehmer erhalten haben, dann möchten Sie auf dieser Basis Ihren Verkaufspreis unter Umständen errechnen. Setzen Sie in diesem Fall hier einen Haken.

Wenn Sie aber bereits ein Angebot mit Preise abgegeben haben und nun lediglich per GAEB Ihre Einkaufspreise aktualisieren, dann möchten und dürfen Sie natürlich Ihre VK Preise nicht verändern. Aktivieren Sie dann das Feld also nicht.

[Bild]

B4 Lohnminuten ggf. aus Stammdaten holen : Hier haben die Möglichkeit, die hinterlegten Lohnminuten aus den Stammdaten (Kalkulationseinstellung) zu holen.

[Bild]

B5 Artikeltext ggf. durch GAEB Texte überschreiben: Wenn bei Phase 94 (Preisangebot) Artikel in das Dokument übernommen werden, findet die Zuordnung über die Positionsnummer statt. Dabei gibt es zwei Verhaltensmuster

Die Position ist eine ‚normale LV Position’ (also ein Text vom Planer) Dann wird die Position in einen versteckten Set gewandelt und der GAEB Artikel wird als Setbestandteil angelegt.

Die Position ist bereits ein ‚normaler Artikel’, wurde also aus einem Katalog aufgerufen Dann wird bei diesem Artikel der Preis eingesetzt, sowie Artikelnummer und Katalog überschrieben. Wenn allerdings diese Option gesetzt ist, wird auch der Artikeltext überschrieben.

[Bild]

B6 Artikel autom. in Katalogstammdaten anlegen/ändern: Hiermit wird der Artikel, mit allen zur Verfügung stehenden Informationen im angegeben Katalog angelegt bzw. geändert. Der Preis wird nur übertragen, wenn die folgende Option „auch Artikelpreise“ gesetzt ist.

Hinweis: In der 90er Phase kennt die GAEB pro Position zwei Preise. Einen Listenpreis und einen Nettopreis. Die Preise werden in den entsprechenden Feldern gespeichert. Sind jedoch beide Preise identisch, gehen wir davon aus, dass es sich um Ihren Einkaufspreis handelt. Dann wird der Listenpreis ignoriert, damit nicht aus Versehen Ihr Einkaufspreis im Listenpreis steht.

[Bild]

B7 Bei AKTIONsmeldungen im Protokoll ‚Merker‘ setzen: Beim Einlesen einer GAEB Datei wird ein Protokoll mitgeführt. Bei wichtigen Meldungen (Typ: Aktion) wird bei der Position automatisch der ‚Merker‘ gesetzt, um diese Positionen schneller zu finden. (STRG-F im Dokument).

In diesem Protokoll gibt es rein informative Einträge und sehr wichtige Einträge. Die wichtigen Einträge werden mit AKTION gekennzeichnet, weil Sie sich diese Positionen näher anschauen müssen/sollten. Z.B. kann es sein, dass wir beim Einlesen

- eine Mengenangabe von 0 auf 1 korrigiert haben (da Pauschalposition),

- einen Multiplikationsfehler bei Menge * Preis festgestellt haben,

- eine Position oder Artikel als "entfällt" gekennzeichnet ist

usw.

Diese wichtigen AKTIONsmeldungen werden nicht nur ins Protokoll, sondern auch in die Positionsanmerkung (erkennbar am roten Knopf ‚Anmerkungen‘ im Artikelaufruf) geschrieben. Damit Sie diese Positionen schneller auffinden können, wird bei aktiviertem Feld zusätzlich auch der ‚Merker‘ in der Position gesetzt. Da das manchmal störend sein kann, können Sie das Setzen des Merkers ausschalten.

[Bild]

B8 Positionsnummer von links her auflösen (Sonepar): Die Fa. Sonepar hat in den Positionsnummern Leerzeichen. Um diese zu unterdrücken, müssen Sie dieses Feld aktivieren, wenn Sie eine Datei dieses Großhändlers einlesen.

[Bild]

7 Datei anzeigen (unformatiert): Bei der Suche nach Problemlösungen hilft es manchmal, die Datei mit einem Editor direkt anzuschauen. Als Laie wird Ihnen diese Anzeige jedoch nicht viel bringen. Fü r unsere Support Mitarbeiter kann es aber oft sehr hilfreich sein.

Hinweis: GAEB90 und GAEB2000 Dateien werden im Windows-Editor gezeigt. GAEBXML Dateien im Internet Explorer.

[Bild]

8 Datei Anzeigen (formatiert): Hier wird die GAEB Datei mit einer speziellen Toolbox in ein optisch besser lesbares Format gebracht und im Internet Explorer angezeigt. Die Aufbereitung kann bei großen GAEB Dateien eine Weile dauern. Dafür bekommt man aber einen schönen Überblick über den Inhalt.

[Bild]

[Bild]

9 Einlese-Protokoll: Hier können Sie immer das aktuelle GAEB Verarbeitungsprotokoll im Windows Editor lesen. Sie sollten es nach dem Einlesen immer öffnen und anschauen bzw. zumindest kurz überfliegen, da das Programm den Schweregrad eines möglichen Problems nicht erkennen kann. Unter Umständen sollten Sie es sogar abspeichern oder ausdrucken.

[Bild]

10 Aktions-Protokoll: Sollte die GAEB-Datei fehlerhaft sein, wird ein Aktions-Protokoll erstellt, dass Sie hier nachlesen können.

[Bild]

11 Einlesen: Hiermit lesen Sie das GAEB Dokument ein.

Wenn Sie ein bestehendes Labelwin Dokument dabei aktualisieren, empfehlen wir Ihnen dringend, das Dokument vorher zu kopieren. Sie können einen Fehler beim Einlesen, z.B. bei defekter GAEB Datei oder falsch gesetzter Option, nicht rückgängig machen.

Bitte lesen Sie am Ende des Einlesens unbedingt das Protokoll.

[Bild]

12 Abbruch: Durch Betätigen diesen Knopfes beenden Sie das GAEB einlesen.
