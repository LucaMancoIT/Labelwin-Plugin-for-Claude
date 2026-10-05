# Schnelldurchlauf: GAEB im LV-Bereich

Pfad: Dokumentenbearbeitung > Dokumentenerstellung [3] > GAEB > Schnelldurchlauf: GAEB im LV-Bereich
Quelle: handbuch/schnelldurchlauf__gaeb_im_lv_bereich.htm

|

Schnelldurchlauf: GAEB im LV-Bereich

Bevor wir auf die Details und die Masken eingehen, möchten wir kurz den Ablauf einer LV Bearbeitung (80er Phasen) mittels GAEB Datenaustausch aufzeigen.

· Der Planer erstellt ein Leistungsverzeichnis und gibt es als Phase 83 (Aufforderung zur Angebots-abgabe) heraus.

· Der Handwerker liest diese „83er“ Datei in ein leeres Labelwin Dokument ein. Er hat jetzt ein in Bauteile, Bauabschnitten, Titel und Positionen aufgegliedertes Leistungsverzeichnis

· Jetzt muss dieses LV vom Handwerker bepreist werden. Hier gibt es generell 2 Methoden.

o Die VK Preise (Material und Lohn) werden per Änderungslauf eingetippt

Die Preise sind hierbei „vom Himmel gefallen“, d.h. sie wurden vorher auf einen Stück Papier ausgerechnet.

Diese Methode wird später unter dem Titel ‚Mit Änderungslauf bepreisen’ beschrieben

o Zu jeder Position wird der oder die Artikel aus den diversen Katalogen aufgerufen und zugeordnet. Dadurch lässt sich der Angebotspreis kalkulieren.

Diese Methode wird später unter dem Titel ‚Mit Artikeln bepreisen’ beschrieben

o Sie lassen sich, zumindest Teile, vom Großhändler mit Ihren projektspezifischen Einkaufspreisen bepreisen und schlagen nur noch Aufschlag und Lohnminuten drauf.

In diesem Fall erstellen Sie aus dem LV diverse Preisanfragen und geben diese als Phase 93 (Preisanfrage) für den Großhändler aus. Der schreibt Artikelnummern und Preise dazu, die sie als Phase 94 (Preisangebot) wieder zurückbekommen und in ihr LV einlesen können. Näheres dazu unter GAEB im Bestellwesen.

· Wenn das Angebot bepreist und kalkuliert ist, kann es abgegeben werden. Dazu schreibt man es als Phase 84 (Angebotsabgabe) raus. Diese Datei beinhaltet im Wesentlichen nur die Preise zu den einzelnen Positionen.

· Zusätzlich kann es Nebenangebote geben. Diese haben Phase 85 und können sowohl vom Planer als auch vom Handwerker kommen.

· Wenn man als Handwerker den Zuschlag bekommen hat, erhält man unter Umständen eine Auftragsbestätigung als Phase 86 Datei, die wie eine Phase 83 Datei aussieht, nur dass hier die vereinbarten Preise enthalten sind. Sie enthält aber nicht Ihre Kalkulation.

Wenn Sie mit einer Kalkulation, d.h. mit hinterlegten Artikeln Ihr Angebot bepreist haben, sollten Sie diese Datei nicht einlesen, sondern manuell Ihr abgegebenes Angebot an die Auftragbestätigung anpassen. Andernfalls können Sie Ihr ursprüngliches Angebot nicht als Basis verwenden.

· Die Phase 89, Rechnungsschreibung, hat sich in der Praxis nicht bewährt und nicht durchgesetzt. Sie ist daher gestrichen worden.
