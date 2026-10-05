# Allgemeines und Wichtiges zum GAEB Datenformat

Pfad: Dokumentenbearbeitung > Dokumentenerstellung [3] > GAEB > Allgemeines und Wichtiges zum GAEB Datenformat
Quelle: handbuch/allgemeines_und_wichtiges_zum_gaeb_datenformat.htm

|

Allgemeines und Wichtiges zum GAEB Datenformat

Da das GAEB Format ursprünglich nicht für den Einsatz beim Handwerker gedacht war, ist es teilweise sehr schwierig, die GAEB Informationen in Labelwin abzubilden und umgekehrt die Datenstruktur von Labelwin im GAEB Format abzubilden. Dies war zu Zeiten der GAEB 90 noch schwieriger als heute, vor allem weil die Regelungen sehr schwammig sind bzw. waren und häufig mehrere Interpretationsmöglichkeiten bieten. Des Weiteren sind die Regelungen in „Beamtendeutsch“ verfasst, so dass sie nicht jeder ohne weiteres versteht und daher viele Softwarehäuser, defekte bzw. falsche GAEB Dateien erstellen.

Man muss daher die eingelesen Daten unbedingt kontrollieren. Labelwin erzeugt beim Lesen und Schreiben ein sehr ausführliches Protokoll. Wir raten, sich dieses genau anzuschauen.

Das Protokoll

Das GAEB Verarbeitungsprotokoll enthält Kopfinformationen, die das Dokument im Allgemeinen betreffen und Informationen zu jeder Position.

· Allgemeine Informationen und Hinweise zur Verarbeitung beginnen mit dem Wort „GAEB:“

· Wichtige Informationen, bei denen unter Umständen nach dem Einlesen manuell eingegriffen bzw. korrigiert werden muss, beginnen mit dem Wort „AKTION:“

Zusätzlich werden diese Informationen beim Artikel in der Anmerkung (roter Knopf in der Artikelaufrufmaske) hinterlegt und ein Merker beim Artikel gesetzt, damit man diese Positionen schnell finden kann (Menü ‚Bearbeiten, Suchen’, Auswahl ‚Merker’ in der Positionsbearbeitung)

Positionsnummern

Alle GAEB Positionen haben eine eindeutige Positionsnummer (Ausnahmen gibt es in der 90er Phase). Diese Positionsnummern sind hierarchisch mit Position, Titel, Los etc. definiert. Sie dürfen, wenn sie einmal vergeben wurden, unter keinen Umständen geändert werden. Die gesamte Zuordnung beim Einlesen einer Preisdatei (Phase 84) und beim Austausch mit dem Planer/Architekten/Großhändler, funktioniert ausschließlich über diese Positionsnummern.

Die Positionsnummern unterliegen einem Schema (in der GAEB90 Version hieß das noch OZ Ordnungszahl- oder OZ-Schema). Es entspricht in etwa dem Positionsnummernschema in der Labelwin Kalkulationsmaske, z.B. aa.tt.ppp.

Wichtig dabei ist, dass es immer eine feste Länge hat. Also z.B. 01.02.0003 und keinesfalls 1.2.3. Als „Füller“ können es statt der führenden Nullen aber auch Leerstellen sein. Da man diese schlecht erkennen kann, übersetzt Labelwin diese in Unterstriche. Bsp.: _1._2.___3. Beim Abgleich bzw. der Zuordnung berücksichtigt Labelwin diese Varianten so gut es geht. Wenn diese Positionsnummern irgendwann mal leicht abgeändert wurden, kann es zu Zuordnungsproblemen kommen.

Lücken in der Hierarchiestufe („Dummy-Titel“)

Eine Besonderheit bei GAEB Dokumenten ist, dass sie Lücken in der Hierarchie haben dürfen.

Beispiel:

1 Erstes Los

1._1 Erster Titel im ersten Los

1._1._1 Position

1._2. Zweiter Titel

1._2._1 Position

2 Zweites Los

2.__._1 Position im Los aber ohne Titel

3 Drittes Los

3._1. Wieder mit Titel

3._1._1 Position

Die problematische Stelle ist fett markiert. Da Labelwin keine „Lücken“ erlaubt, fügen wir automatisch einen so genannten „Dummy Titel“ ein. Beim Drucken und Ausgeben werden diese „Dummy Titel“ wieder ignoriert.
