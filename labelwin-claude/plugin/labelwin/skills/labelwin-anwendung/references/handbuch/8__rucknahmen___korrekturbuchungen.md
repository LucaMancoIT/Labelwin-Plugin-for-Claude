# 8. Rücknahmen / Korrekturbuchungen

Pfad: Materialwirtschaft > Scannerverarbeitung [Modul] > 8. Rücknahmen / Korrekturbuchungen
Quelle: handbuch/8__rucknahmen___korrekturbuchungen.htm

|

8. Rücknahmen / Korrekturbuchungen

Im einfachsten Fall scannen Sie den zurück zu buchenden Artikel und geben dann auf der Tastatur -1 (Enter) ein. Wichtig ist das Minuszeichen vor der Menge.

Wenn es sich um eine größere Rücknahme handelt, können Sie auch vor der Projekt- oder KD-Auftragsnummer ein Minus-Zeichen setzen. Damit werden alle folgenden Artikel automatisch negativ gebucht. Beispiel Projektnummer : -#96-5001 oder Minuszeichen tippen und ohne Enter sofort die Nummer vom Auftrag scannen.

Um das Scannen besonders im Bereich Rücknahmen zu erleichtern, haben wir die Umschaltung zwischen Positiv und Negativ als Strichcode eingeführt.

Wenn Sie den Code ‚NEGATIV’ scannen, werden alle nachfolgenden Artikel als negativ angesehen, sinngemäß also die eingebende Menge mit -1 multipliziert.

Dies bleibt solange aktiv, bis Sie:

- den Code ‚POSITIV' scannen.

- eine neue Projekt oder Auftragsnummer scannen oder eingeben

[Bild]

Erzeugung der Etiketten

Leider kann das ‚normale’ Lageretikett nicht zum Einsatz kommen, da dort die Artikelnummer mit einer vorangestellten Katalogkennung gedruckt wird.

Wir haben daher ein Formular ‚etkoepfe.rpt’ entwickelt, das sich bereits auf Ihrem Rechner befindet. Es muss allerdings noch in die Report.ini eingebunden werden, wobei Ihnen ggf. die Hotline hilft.

Beginnen Sie ein neues Dokument, am Besten mit der Dokumentenart ‚Frei’ und tragen als Bemerkung ‚Standardetiketten' ein.

Gehen Sie dann in den Artikelaufruf, stellen auf ‚Leistungsposition’ und geben Sie den Text, der als Etikett gedruckt werden soll in das Feld Positionsnummer ein. Um das Etikett NEGATIV zu erzeugen, geben Sie also nur das Wort ein. Den Artikeltext lassen Sie am Besten leer. Genauso erfassen Sie nun den Text POSITIV.

Übrigens können Sie so auch Etiketten für häufig benötigte Projekte wie z.B. AUTO1, Lager usw. ausdrucken. Allerdings sollten Sie dann auch ein Projekt mit diesem Namen anlegen.

Eine weitere Möglichkeit ist es, auf diesem Weg Etiketten für die Mengen zu erstellen. Wenn Sie sich Etiketten mit den gängigsten Mengen (2,3, - 9, 10, 20, 25, 50) erstellen, können Sie sich das Tippen ersparen. Ein Etikett mit der Menge 1 ist überflüssig, da dies die Standardmenge ist.

Drucken Sie das Dokument mit dem Formular ‚ETKOEPFE' aus.
