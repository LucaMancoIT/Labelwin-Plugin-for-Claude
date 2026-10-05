# 1. ÖNorm einlesen

Pfad: Schnittstellen > ÖNorm > 1. ÖNorm einlesen
Quelle: handbuch/1__onorm_einlesen.htm

|

1. ÖNorm einlesen

Wählen Sie in der Positionserfassung den Menüpunkt <Vorlagen> <Ö-Norm Datei einlesen>.

[Bild]

Wählen Sie eine ÖNorm Datei über den Knopf „Durchsuchen“ aus oder ziehen Sie eine ÖNorm Datei auf das Drag&Drop Feld. Das Programm erkennt automatisch, ob es sich um eine gültige ÖNorm Datei handelt und wenn ja um welches Format. Es wird dann der entsprechende Karteireiter aktiv geschaltet und rechts oben im Dateiinfo Bereich sehen Sie ausgewählte Kopfinformationen.

[Bild]

[Bild]

Mit dem Knopf „Datei anzeigen“ können Sie sich die original ÖNorm Datei anzeigen lassen. Bei der A2063 erfolgt dies als XML Datei im Internet Browser.

Einleseoptionen A2063

Artikel-Schlusstext : Entscheiden Sie hier, ob und wenn ja welcher Artikelschlusstext hinter jeder Position angehängt werden soll

Mit dem Haken bei „ Alle Leistungspositonen als versteckte Sets anlegen “ erleichtern Sie sich die saubere Bepreisung mit Großhandelsartikel. Alle Anfragepositionen werden als versteckte Sets angelegt. Fügen Sie beim Bepreisen eine oder mehrere Positionen in den Set ein.

Tipp: Wenn Sie beim Einlesen den obigen Haken vergessen haben und sich später entscheiden, dass Sie doch gerne mit versteckten Sets arbeiten, so können Sie das in der Positionserfassung über die Blockbearbeitung <Bearbeiten>, <Blockbearbeitung> nachholen. Markieren Sie vorher die Positionen und wählen Sie in der Blockbearbeitungsmaske oben rechts die Option „Leistungspositionen in Sets verwandeln (verborgen multi)“.

Diese Option steht nur zur Verfügung, wenn Sie den Haken bei „Preise, wenn vorhanden, einlesen“ nicht setzen!

Preise, wenn vorhanden, einlesen : Damit werden ggf. vorhandene Preise in die Labelwin VK Preise eingelesen, ansonsten werden sie ignoriert. Ein Einlesen der Preise als EK Preis, so wie beim deutschen GAEB möglich, geht bei ÖNorm nicht.

Wenn Sie eine ÖNorm Datei in ein Dokument einlesen, welches bereits Positionen enthält und per ÖNorm entstanden ist, dann haben Sie die Option „ Nur Preise einlesen (bepreisen) “. Hierbei wird bis auf die Preisinformation alles ignoriert. Die Zuordnung der Positionen erfolgt über die Positionsnummer. Auch Positionen ohne Preis werden ignoriert und nicht auf 0 gesetzt.

[Bild]

Sollten Preisanteile in der ÖNorm Datei definiert sein, müssen Sie auswählen, in welches Labelwin Preisfeld diese übertragen werden sollen.

Mit einem Haken bei „ Preisanteileaufgliederung ignorieren “ können Sie alle Preisanteile in ein Feld (Material) übernehmen.

Bitte achten auf das Fehlerprotokoll, in der folgende, sich selbsterklärende, Fehler und Warnungen stehen können:

-

FEHLER: Position ’01.02.03‘ nicht gefunden!

-

FEHLER: Position ’01.02.03‘ mehrfach gefunden, mit Stichwort 'Heizungsrohr' aber nicht gefunden, keine Zuordnung möglich!

-

FEHLER: Position '01.02.03'/Heizung' mehrfach gefunden, keine Zuordnung möglich!

-

FEHLER: Unterschiedliche Mengen bei Position '01.02.03‘. DokMenge: 10 ÖNormMenge: 12. Es wird die ÖnormMenge genommen

-

FEHLER: Unterschiedliche Liefereinheiten bei Position '01.02.3‘. DokEinh: Stk ÖNormEinheit: Stck. Es wird die ÖnormEinheit genommen

-

"WARNUNG: Unterschiedliches Eventualkennzeichen bei Position '01.02.03‘. Dok: nicht eventual ÖNorm: eventual!

-

"WARNUNG: Unterschiedliches Eventualkennzeichen bei Position '01.02.03‘. Dok: eventual ÖNorm: nicht eventual

-

WARNUNG: Unterschiedliches Alternativkennzeichen bei Position '01.02.03‘. Dok: nicht alternativ ÖNorm: eventualalternativ

-

"WARNUNG: Unterschiedliches Alternativkennzeichen bei Position '01.02.03‘. Dok: alternativ ÖNorm: nicht alternativ

-

FEHLER: Rechenfehler Gesamtpreis und Einzelpreis

-

Fehler in Routine oe_xxxx: xxxxxx – Systemfehler, bitte auf den Text achten

Beim Einlesen einer ÖNorm in ein leeres Dokument (kein Bepreisen), können folgende Fehler und Warnungen auftreten:

-

FEHLER: Rechenfehler Gesamtpreis und Einzelpreis (10.00 * 2 <> 19.00)

-

Fehler in Routine oe_xxxx: xxxxxx – Systemfehler, bitte auf den Text achten
