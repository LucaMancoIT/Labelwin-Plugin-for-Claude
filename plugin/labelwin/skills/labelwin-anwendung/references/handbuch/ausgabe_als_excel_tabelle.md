# Ausgabe als Excel-Tabelle

Pfad: Dokumentenbearbeitung > Aufmaß per Excel-Tabelle > Ausgabe als Excel-Tabelle
Quelle: handbuch/ausgabe_als_excel_tabelle.htm

|

Ausgabe als Excel-Tabelle

Tipp: Die Handhabung der Aufmaßerfassung per Excel wird in einem Tutorial Video im vorherigen Kapitel Aufmaß per Excel-Tabelle anschaulich erklärt.

Erstellen Sie wie gewohnt das Aufmaßdokument, indem Sie die Basis, die Auftragsbestätigung oder das Angebot kopieren. Starten Sie in die Bearbeitung und wählen die Menüpunkte <Durchläufe>, <bei allen/markierten Positionen Menge auf 0 setzen> an. Danach speichern das Dokument wieder ab, indem Sie die Bearbeitung mit OKAY verlassen

|

In der Maske der Projektverwaltung markieren Sie das zu exportierende Aufmaß und wählen den Menüpunkt [Import / Export] - [Export] an.

Es öffnet sich eine Maske zur Aufmaßvorberitung an Excel.

|

[Bild]

In dieser Maske legen Sie fest, welche Excel-Tabelle als Vorlage gewählt werden soll, welche Raumnamen eingesetzt werden und welche Positionen / Artikel in der Tabelle erscheinen sollen.

[Bild: Ausgabe als Excel-Tabelle]

Bild: Aufmaß Export an Excel

|
[Bild: 1]

Vorlage

[Bild: 1. Vorlage]

Legen Sie zunächst die Vorlage fest. In der Auslieferung sind zunächst nur 3 Tabellen verfügbar. Diese können Sie aber kopieren und unter Einhaltung von bestimmten Bedingungen selbst verändern. Die Beschreibung zur Erstellung eigener Vorlagen finden Sie unter Eigene Tabellen.

|

Folgende Spalten können exportiert werden:

Position, Text, Bereich, Typ, Alt / Ev, PosArt, Planmenge, SetMenge, Menge_Ges., Menge_bisher, Einheit, Artikelnr, Langtext, EP

Hinweis: In der Standardvorlage "_aufmass.xls" werden nur die Spalten "Position" bis "Menge_bisher" exportiert. Soll auch eine der Spalten Einheit, Artikelnr, Langtext oder EP exportiert werden, müssen Sie diese in Ihre eigene Vorlage aufnehmen. Gleiches gilt übrigens auch für die Spalte Bemerkung, wenn Sie im Aufmaß eine Bemerkung erfassen möchten, die importiert werden soll.

Alle verwendbaren Schlüsselworte - also Spaltenüberschriften - finden Sie auch mit dem Knopf ‚Hilfe zur Vorlage‘.

|

[Bild]

|
[Bild: 2]

Räume

[Bild: 2. Räume]

|

Damit im Excel die Spalten gleich mit den richtigen Raumnamen / Nummern beschriftet sind, können die Räume erfasst werden. Das ist übrigens auch im Projektdatenblatt über den Button "Räume (Aufmass)" möglich.

|

[Bild]

[Bild]

Wichtig ist das Feld ‚Raum‘, weil dieses nach dem Import in der Aufmaßzeile gespeichert wird. Die Beschreibung dient nur der möglicherweise einfacheren Identifikation auf der Baustelle.

|
[Bild: 3]

Arbeitsbereiche

[Bild: 3. Arbeitsbereiche]

Wenn Sie im Dokument mit Arbeitsbereichen gearbeitet haben, können Sie die Ausgabe der Positionen auf einen oder mehrere Arbeitsbereiche begrenzen. Positionen, die anderen Arbeitsbereichen zugeordnet sind, werden dann nicht an Excel übergeben.

|
[Bild: 4]

Aufmaßnummer

[Bild: 4. Aufmaßnummer]

Die Aufmaßnummer wird zur Bildung des Dateinamens verwendet (den Sie jedoch ändern dürfen) und zusätzlich in die Excel-Tabelle eingetragen. Wichtig ist diese Nummer beim späteren Import, weil sie in die Aufmaßzeilen eingetragen wird. Die Nummer kann aber auch später beim Import noch geändert werden. Dort wird auch das Aufmaßdatum aus der Excel-Tabelle ausgelesen, was zwingend manuell im Excel eingetragen werden muss. Mit der Kombination Aufmaßnummer und Datum kann kaum noch was schief gehen.

|
[Bild: 5]

Ausgabepfad

[Bild: 5. Ausgabepfad]

Hier wird die erzeugte Excel-Tabelle abgelegt. Mit dem Knopf können Sie einen vorhandenen Pfad wählen. Am besten Sie richten sich selbst mit dem Explorer einen Pfad ein, den Sie dann hier eintragen. Das Programm merkt sich den zuletzt von Ihnen gewählten Pfad und schlägt diesen bei künftigen Exporten, aber auch beim Import wieder vor. Wenn Sie ein Cloud-Verzeichnis z.B. mit Dropbox oder ähnlichem eingerichtet haben, können Sie die Date auch direkt dort ablegen.

|
[Bild: 6]

Optionen

[Bild: 6. Optionen]

Die Möglichkeiten sind sicherlich weitgehend selbst erklärend. Beim Thema Set dagegen gibt es unterschiedliche Standpunkte. Wir sind der Meinung, dass man nur ganze Sets aufmessen kann, weil dem Kunden die Bestandteile ja in der Regel nicht bekannt sind. Die Mitarbeiter dagegen wissen oft nicht, was in dem Set enthalten ist und sehen auf der Baustelle nur die Bestandteile. Der Kompromiss ist vielleicht, dass Sie die Bestandteile zwar ausgeben, jedoch dort keine Mengen erfasst werden dürfen. In den Mengenfelder ist bei Set-Bestandteilen ein Strich vorgegeben, damit es hoffentlich auffällt, das hier keine Menge eingegeben werden soll.

Beim Import werden alle Mengen aufgrund der Positionsnummer in das Aufmaß übernommen. Wenn Sie also die Bestandteile ausgeben und hier Mengen eingegeben werden, ist das Chaos vorprogrammiert.
