# LEC-Schnittstelle [Modul]

Pfad: Schnittstellen > LEC-Schnittstelle [Modul]
Quelle: handbuch/lec_schnittstelle__modul_.htm

|

LEC-Schnittstelle [Modul]

Stand: 15.01.2018

(Version 5.86)

Mit diesem Modul ist es möglich Bewegungsdaten aus der Labelwin-Software in die VDKF-LEC Software zu übergeben und die so erfassten Daten in Labelwin weiter zu benutzen.

|

Hintergrund: VDKF-LEC ist eine eingetragene Marke des VDKF e.V., Bonn. Die VDKF-LEC Software ist ein Werkzeug, das dem Anlagenbetreiber eine Gesamtlösung seiner Aufzeichnungs- und Meldepflichten bietet. Neben der Planung der Anlage, Installation, Wartung und Service bietet VDKF-LEC ein komplettes Dienstleistungspaket aus einer Hand.

VDKF = Verband deutscher Kälte-Klima Fachbetriebe e.V.

LEC = Leakage & Energy Control

Die europäischen Verordnungen und Normen - z.B. EU-VO 517/2014 (F-Gase-VO) und EU-VO 1005/2009 - sowie die nationale Gesetzgebung - z.B. Chemikalien-Ozonschichtverordnung (ChemOzonSchichtV) und Chemikalien-Klimaschutzverordnung (ChemKlimaschutzV) - stellen sowohl die Betreiber von Kälte- und Klimaanlagen als auch die Kälte-Klima-Fachbetriebe vor umfassende Aufgaben. Dazu zählen u.a. regelmäßige Leckagekontrollen, Emissionsreduzierung, Energieeffizienz, Wartungsaufgaben, Protokollpflichten und die Erfassung direkter und indirekter Emissionen.

Erfassung der Grunddaten:

Zunächst müssen Sie die von Ihnen verwendeten Materialien und Leistungen als Grunddaten erfassen. Hierzu wählen Sie im Einstellmodul den Menüpunkt :

[Programmbereiche – Kundendienst – LEC-Schnittstelle] an.

[Bild]

Wählen Sie zunächst die Stammdatenart ‚Kältemittel’ aus.

Die Bezeichnung muss der VDKF-LEC Normung entsprechen (Die Kältemittel müssen nach der R-Nomenklatur hinterlegt werden. Zwischen R und den Ziffern muss sich ein Leerzeichen befinden. Eventuelle nachfolgende Buchstaben sind direkt an die letzte Ziffer zu schreiben. Großschreibung bei der 400- und 500-Serie, sonst Kleinbuchstaben.) Sollten die Beschreibung nicht genau dieser Nomenklatur entsprechen, kann später keine Übergabe an die VDKF-LEC Software erfolgen.

In den Artikelstammdaten müssen für jedes Kältemittel je ein Artikel für die Entsorgung und ein Artikel für das eingefüllte Kältemittel angelegt werden. Diese Artikel werden nun aufgerufen und danach der Datensatz gespeichert.

Diesen Vorgang wiederholen Sie für jedes von Ihnen verwendete Kältemittel.

Wählen Sie jetzt den Stammdatentyp Öle aus.

[Bild]

Hier erfassen Sie wiederum für jedes von Ihnen verwendete Öl in den Stammdaten die Artikel für Entsorgung und für das aufgefüllte Öl. Zusätzlich müssen Sie unbedingt den Öltyp festlegen.

Nach dem Speichern des Datensatzes wiederholen Sie den Vorgang für alle von Ihnen verwendeten Öle.

Für die weiteren Stammdatenarten Dichtigkeitsprüfungen und ggf. für Reparaturen verfahren Sie entsprechend.

[Bild]

Damit sind die Stammdaten erfasst.

Zuordnen der LEC-Nummer zu den Labelwin-Anlagen :

Die Zuordnung der LEC-Nummern zu den Labelwin-Anlagen geschieht an zwei Stellen.

Zum einen in der Anlagenverwaltung. Hier existiert ein neues Feld LEC Nr. Hier muss die zugehörige VDKF-LEC-Nummer eingetragen werden.

[Bild]

Die zweite Stelle befindet sich im TGM-Modul. Hier wird ebenfalls bei der Anlage die VDKF-LEC-Nummer eingetragen.

[Bild]

Erfassen der Bewegungsdaten :

In einem geöffnetem KD-Auftrag finden Sie unter Bearbeiten den Menüpunkt ‚LEC-Daten erfassen’. Bei Anwahl dieses Menüpunktes öffnet sich folgende Maske:

[Bild]

Wählen Sie an dieser Stelle der Bewegungsart aus und erfassen Sie die entsprechenden Mengen. Die Auswahlboxen sind durch die Stammdaten und die VDKF-LEC-Schnittstelle vorgegeben. Sie können hier nicht verändert werden.

Nachdem Sie alle Bewegungsdaten zu diesem Auftrag erfasst haben, beenden Sie die Maske mit Ende.

Übernahme der Bewegungsdaten in die Rechnung:

Zur Übernahme der LEC-Bewegungsdaten in die Kundendienst-Rechnung gehen sie im KD Auftrag auf Erledigt/Rechnung und setzen den entsprechenden Haken in der folgenden Maske.

[Bild]

Die Artikel werden dann gemäß der Kalkulationseinstellung in die Rechnung übernommen.

Übergabe der Bewegungsdaten in die VDKF-LEC-Schnittstelle:

Zur Übergabe der Bewegungsdaten starten sie das Selektionsprogramm (select.exe).

Unter dem Menüpunkt ‚Kundendienst’ finden Sie die LEC-Schnittstelle.

[Bild]

Bitte beachten Sie, dass der Ausgabepfad der Datei existieren muss. Sollten sie das Übergabekennzeichen nicht setzen, so können Sie den Export wiederholen. Normalerweise werden nur die Datensätze exportiert, die noch nicht übergeben worden waren.

Die Exportdateien werden für jeden Export neu erzeugt.

Zum Einlesen in das VDKF-LEC-Programm folgen Sie bitte der Anweisung aus diesem Programm.
