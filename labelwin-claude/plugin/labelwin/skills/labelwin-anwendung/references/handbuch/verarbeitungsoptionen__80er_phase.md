# Verarbeitungsoptionen: 80er Phase

Pfad: Dokumentenbearbeitung > Dokumentenerstellung [3] > GAEB > Gaeb einlesen > Verarbeitungsoptionen: 80er Phase
Quelle: handbuch/verarbeitungsoptionen__80er_phase.htm

|

Verarbeitungsoptionen: 80er Phase

[Bild]

[Bild]

A1 Artikelschlusstext: Manchmal steht in GAEB Dokumenten schon der Text „liefern und montieren“ am Ende des Kurz- und/oder Langtextes. Feststellen können Sie es am Besten über die „formatierte Anzeige“. Wenn Sie einen Schlusstext auswählen, wird die entsprechende Auswahlbox im Artikelaufruf entsprechend für jede Position gesetzt.

[Bild]

A2 Katalaog: In der 80er-Phase ist die Angabe eines Kataloges meist nicht nötig. Es gibt aber durchaus GAEB Dateien die Produktinformationen, wie z.B. Artikelnummern, mit angeben. In diesem Fall schreiben wir die Artikelnummern und den Katalog in die Position im Labelwin Dokument.

[Bild]

A3 EK/VK Zuordnung: Wenn Sie eine GAEB Datei einlesen, die Preise enthält, müssen Sie eine Zuordnung treffen, wo diese hinkommen. Als Handwerker bekommen Sie Preise per GAEB entweder von Subunternehmern (als Phase 84) oder von Lieferanten (als Phase 84 oder Phase 94).

Aus Sicht des GAEB Erstellers sind es normalerweise Verkaufspreise. Aus Ihrer Sicht sind es meist Einkaufspreise.

[Bild]

A4 Verkaufspreise mit aktueller Kalkulation neu kalkulieren: Diese Option erscheint nur, wenn Sie vorher die Zuordnung „Einkauf“ gewählt haben. Bei gesetzten Haken werden die VK Preise an Hand der Kalkulationseinstellung neu kalkuliert. Z.B. EK * 1,3.

Wählen Sie diese Option nur dann, wenn Sie das Angebot noch nicht abgegeben haben und es kalkulieren möchten. Diese Neuberechnung kann nicht zurück genommen werden.

Lassen Sie den Haken weg, wenn Sie nach Abgabe des Angebots und Erhalt des Auftrags das Dokument lediglich mit aktuellen Einkaufspreisen für die Nachkalkulation versehen möchten.

[Bild]

A5 Kostenarten Zuordnung: Labelwin kennt 4 Kostenarten: Material, Lohn, Fremdleistung und Sonstige Kosten. Die GAEB kennt bis zu 6 Kostenarten oder „Einheitspreisaufgliederung“ wie es in der GAEB heißt. Diese ist aber nicht fest definiert, sondern kann pro GAEB Datei individuell festgelegt werden. Sollte es in der GAEB Datei eine Einheitspreisaufgliederung geben, so wird der Knopf rot und Sie müssen in der Folgemaske eine Zuordnung vornehmen.

[Bild]

Bild: GAEB Einheitspreisaufgliederung

Auf der linken Seite sehen Sie bis zu 6 Einheitspreis-Bezeichnungen aus der GAEB Datei. Diese müssen Sie nun den 4 Labelwin Kostenarten zuordnen. Es können durchaus mehrere GAEB Einheitspreisaufgliederungen derselben Labelwin Kostenart zugeordnet werden.

Wenn Sie eine GAEB Datei (Phase 84) von einem

Großhä ndler einlesen,

dann sollen wahrscheinlich alle genannten Preise in die Materialspalte kommen

Subunternehmer einlesen,

dann sollen wahrscheinlich alle genannten Preise in die Kostenart Fremdleistung kommen.

Die Einheitspreisaufgliederung kommt meist schon in der Phase 83 (Aufforderung zur Angebotsabgabe), wenn der Planer eine Splittung von Material und Lohn wünscht. In diesem Fall merkt sich Labelwin lediglich die Zuordnung und benutzt diese beim Schreiben der GAEB Datei.

[Bild]

A6 Alle Leistungspositionen als versteckte Sets anlegen: Um eine GAEB Datei sauber kalkulieren zu können, müssen Sie hinter jeder GAEB Position ein oder mehrere Artikel legen. Da Sie die Original GAEB Texte aber nicht verändern dürfen, müssen die GAEB Positionen als versteckte Sets angelegt werden, damit die dahinter liegenden Positionen nur für interne Kalkulationszwecke erscheinen.

Sie können diese Option hier wählen, aber wir empfehlen Ihnen, das Wandeln in versteckte Sets erst im Dokument vorzunehmen. Das ist in der Praxis schneller und einfacher. Bitte lesen Sie am Ende dieses Kapitels den Absatz „Mit Artikeln bepreisen“.

[Bild]

A7 Die in der GAEB Datei unter Umständen benutze Zeiteinheit entspricht: In einer GAEB Datei können auch Zeiten enthalten sein. Die GAEB hat aber keine Zeiteinheit definiert, sondern jeder Planer benutzt eine und gibt ihr irgendeinen Namen. Das werden meistens ‚Stunden’ oder ‚Minuten’ sein, können aber auch ‚Std’, ‚h’, ‚Tage’etc. sein.

Da Labelwin immer in Minuten rechnet, müssen Sie hier einen Umrechnungsfaktor eingeben. Bei der Eingabe von 0 werden alle Zeitwerte ignoriert.

[Bild]

A8 Hauptpositionen ohne Menge auf 1 setzen: Diese und alle weiteren Optionen dienen im Prinzip dazu, fehlerhafte GAEB Dateien zu korrigieren. Leider erlaubt die GAEB, Positionen ohne Mengenangabe anzugeben, wenn die Menge 1 aus dem Text doch „offensichtlich“ ist. Leider kann das ein Computer nicht erkennen.

Ob Sie den Haken setzen oder nicht, Sie werden auf jeden Fall im Protokoll gewarnt, wenn es Probleme mit der Mengenangabe gibt. Sie können die Menge dann auch später im Dokument verändern.

Teilweise fehlen auch Mengen, weil diese vom Bieter eingetragen werden müssen. Z.B. fehlt unter Umständen die Tonnenangabe bei der Position „Schutt abfahren“, weil der Planer möchte, dass das der Bieter selber errechnet. Ein entsprechender Hinweis erscheint dann im Protokoll.

[Bild]

A9 Mengen ungleich 1 bei ‚Psch‘ Positionen stehen lassen: In der GAEB ist definiert, dass pauschale Positionen, IMMER die Menge 1 haben müssen.

Pauschalposition werden daran erkannt, dass in der Liefermengeneinheit das Wort "PSCH" steht und nicht etwa "STCK", "MTR" oder "KG" etc.

- Pauschalpositionen, die Menge 0 haben, werden immer auf 1 gesetzt

engen größer als 1 ist dies nach Gaeb unzulässig, kommt aber in der Praxis leider vor.

Bei aktiviertem Feld

- werden Mengen so übernommen, wie sie in der Gaeb-Datei stehen und es erfolgt ein Eintrag in Aktionsprotokoll (Fehlerprotokoll)

Dieses entspricht nicht den Gaeb-Regeln.

3 x Montage von .... bedeutet dass der Einzelpreis der Montage 3 mal gerechnet wird

Bei nicht aktiviertem Feld

- werden Mengen immer auf 1 gesetzt, und es erfolgt ein Eintrag in Aktionsprotokoll (Fehlerprotokoll)

Dieses entspricht zwar den Gaeb-Regeln, aber nicht der menschlichen Logik.

[Bild]

A10 Kurztextverarbeitung: In einer GAEB Datei ist nur der Langtext verbindlich. Der Kurztext dient offiziell nur der besseren Übersicht.

Wenn ein GAEB Dokument aber im Kurztext immer wieder nur den sehr kurzen Kurztext „Rohr“ hat, lässt sich das Dokument in Labelwin sehr schwer überblicken, weil man immer wieder in den Langtext muss, um zu wissen, was für ein Rohr es ist. In diesem Fall macht es Sinn, den Kurztext zu ignorieren und den Langtext, sofern vorhanden, auch als Kurztext zu übernehmen.

Sie haben hier folgende Auswahlmöglichkeiten:

- Leeren Kurztext durch Langtext ersetzen (verschieben)

- Leeren Kurztext gleich Langtext setzen (kopieren)

- Kurztext immer durch Langtext ersetzen (verschieben)

- Kurztext immer gleich Langtext setzen (kopieren)

[Bild]

A11 Kurztext vor den Langtext setzen (bei fehlerhafter GAEB): In einer GAEB Datei ist nur der Langtext verbindlich. Der Kurztext dient offiziell nur der besseren Übersicht.

Wenn ein GAEB Dokument aber im Kurztext immer wieder nur den sehr kurzen Kurztext „Rohr“ hat, lässt sich das Dokument in Labelwin sehr schwer überblicken, weil man immer wieder in den Langtext muss, um zu wissen, was für ein Rohres ist. In diesem Fall macht es Sinn, den Kurztext zu ignorieren und den Langtext, sofern vorhanden, auch als Kurztext zu übernehmen.

[Bild]

A12 Bei AKTIONsmeldungen im Protokoll Merker setzen: Beim Einlesen einer GAEB Datei wird ein Aktions-Protokoll mitgeführt. Bei wichtigen Meldungen (Typ: Aktion) wird bei der Position automatisch der "Merker" gesetzt, um diese Positionen schneller zu finden. (STRG-F im Dokument).

Diese wichtigen AKTIONsmeldungen werden nicht nur ins Aktions-Protokoll, sondern auch in die Positionsanmerkung (erkennbar am roten Knopf "Anmerkungen" im Artikelaufruf) geschrieben. Damit Sie diese Positionen schneller auffinden können, wird bei hier gesetztem Haken zusätzlich auch der "Merker" in der Position gesetzt. Da das manchmal störend sein kann, können Sie das Setzen des Merkers ausschalten.

[Bild]

A12 Dateilieferant für Kat.Zuord.: Hier wird ein Katalog für GAEB-Dateien von Herstellern bzw. für GAEB-Dateien, die durch technische Auslegungsprogramme erstellt wurden (z.B. Badplanungs-programme) zugeordnet.

GAEB-Dateien von Auslegungsprogrammen enthalten manches Mal Artikelinformationen, wie Artikel-nummer, Hersteller und Texte. Die Übernahme der Artikelnummer und des Textes sind unproblematisch. Der Hersteller steht in der GAEB Datei aber als Text, wie. z.B. „Villeroy&Boch", „Viessmann" etc. Damit beim Einlesen eine Zuordnung dieser Begriffe in eine Labelwin Datanorm Katalognummer erfolgen kann, muss hier der Name der Katalog Zuordnungstabelle hinterlegt werden.

Gehen Sie wie folgt vor:

- Tippen Sie vor dem Einlesen der GAEB Datei in dieses Auswahlliste den Namen des Badplanungsprogrammes, z.B. Visoft

- Lesen Sie die GAEB Datei ein

- Starten Sie im Modul EINSTELLUNGEN den Menüpunkt <Programmbereiche> <Dokumentenerstellung> <Katalogzuordnung>.

- Wählen Sie die eben erfasste Schnittstelle, z.B. Visoft, aus

- Hier finden Sie eine Liste aller in der GAEB Datei benutzten Hersteller. Ordnen Sie jedem eine Labelwin Katalognummer zu, sofern Ihnen Datanorm Daten vorliegen.

- Löschen Sie das eben per GAEB erstellte Dokument und lesen Sie die GAEB Datei in ein neues Dokument ein. Wählen Sie den entsprechenden Datenlieferanten, z.B. Visoft.

Jetzt wird im Labelwin Dokument automatisch nicht nur die Artikelnummer, sondern auch der richtige Katalog hinterlegt.

Wählen Sie in Zukunft immer diesen Datenlieferanten aus, wenn Sie GAEB-Dateien dieser Software einlesen. Wenn keine neuen Katalognamen dazugekommen sind, brauchen Sie nichts neu zuzuordnen.
