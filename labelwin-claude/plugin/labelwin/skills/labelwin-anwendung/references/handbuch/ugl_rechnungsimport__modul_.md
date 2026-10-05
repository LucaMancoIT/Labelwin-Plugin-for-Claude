# UGL Rechnungsimport [Modul]

Pfad: Buchhaltung > UGL Rechnungsimport [Modul]
Quelle: handbuch/ugl_rechnungsimport__modul_.htm

|

UGL Rechnungsimport [Modul]

Die Erfassung von Eingangsrechnungen und deren Prüfung ist relativ zeitaufwändig. Wenn die Rechnung dagegen importiert werden kann, so dass sich die Erfassarbeit auf minimale Eingaben beschränkt, kann dies viel Arbeit ersparen.

Ein komplett automatischer Import wird sicherlich nie möglich sein, weil es mindestens bei telefonischen Bestellungen immer wieder Übertragungsfehler geben wird. Auch das Kostenkonto und ggf. eine Kostenstelle können vom Lieferanten nicht mitgeliefert werden, so dass immer wieder Eingriffe / Eingaben erforderlich sind.

Die Hinterlegung des ‚üblicherweise‘ verwendeten Kostenkontos bei der Adresse des Lieferanten spart Arbeit und vermindert Fehler.

Auch die Zahlungsbedingungen sollten bei der Adresse hinterlegt werden, damit diese mit den Daten der Importdatei verglichen werden können. Bei Unterschieden erscheint ein Fenster in dem die Werte und die Unterschiede dargestellt werden. In diesem Fall kann gewählt werden, welche Zahlungsbedingung genommen werden soll.

Die Eingangsrechnung kann über das UGL-Verfahren oder per Gaeb XML Verfahren 99 übermittelt werden. Beim Gaeb-Verfahren ist definiert, dass die Rechnung zusätzlich per PDF als Bild mitgeliefert wird. Erst dieses Verfahren macht die Papierrechnung wirklich überflüssig. Beim UGL muss die Rechnung per Papier mitgeliefert werden, so dass die Datei letztlich nur Tipparbeit spart und eine Hinterlegung der einzelnen Artikel mit ihren echten Einkaufspreisen ermöglicht.

Transport der UGL-Dateien:

Wie die UGL-Rechnungen zu Ihnen gelangen, ist letztlich mit jedem Lieferanten zu vereinbaren. Wünschenswert ist es, diese Dateien ohne vorherige Markierung und Bereitstellung direkt vom Lieferanten zu erhalten. Dabei kann der Transport genau wie bei Angeboten im UGL-Format per FTP-Protokoll ‚auf einen Rutsch‘ stattfinden.

Die Transportwege müssen Sie mit Ihrem Lieferanten abstimmen.

Rechnungen per PDF

Wenn Sie die Rechnungen zusätzlich per PDF bekommen, sollten Sie diese im gleichen Verzeichnis wie die UGL-Dateien ablegen. Damit kann die PDF zur Ablage verwendet werden und der Scann-Vorgang kann entfallen.

Umgang mit Kommissionen

Der nachfolgend beschriebene Umgang mit Bestell- und Auftrags- und Projektnummern bei Bestellungen und Einkäufen ist erforderlich, um einen reibungslosen Import zu bekommen.

- wenn möglich per UGL bestellen

- bei schriftlicher Bestellung muss die Bestellnummer vom Lieferanten in das Feld ‚Vorgangsnummer des Handwerkers' eingetragen werden

- bei Online-Bestellungen muss die Bestellnummer (wenn vorhanden) vom Anwender in das Feld Vorgangsnummer geschrieben werden.

- wenn keine Bestellnummer vorhanden ist, sollte die Projektnummer oder die Kundendienst-Auftragsnummer mit einem vorangestellten k (=Kundendienst) oder p (=Projektnummer) geschrieben werden.

Beispiel:

Projekt 13-1234 => p13-1234

Kundendienstauftrag 13-5678 => k13-5678

Hinter dem p und k kann auch eine Leerstelle sein, Labelwin erkennt es mit und ohne Leerstelle.

- bei Erfassung des Wareneingangs sollte die komplette Lieferscheinnummer des Lieferanten erfasst werden. Da diese in der UGL-Rechnung geführt wird, ist damit ein eindeutiger Vergleich zwischen den Preisen der bestellten Ware und den berechneten Artikeln möglich.
