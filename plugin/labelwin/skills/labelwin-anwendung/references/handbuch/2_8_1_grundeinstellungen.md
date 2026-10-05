# 2.8.1 Grundeinstellungen

Pfad: Einrichtungsarbeiten > Einstellungen [14] > 2. Programmbereiche > 2.8 Druckausgabe > 2.8.1 Grundeinstellungen
Quelle: handbuch/2_8_1_grundeinstellungen.htm

|

2.8.1 Grundeinstellungen

Die hier vorzunehmenden Eintragungen beziehen sich auf die Druckausgaben von Dokumenten auf der Basis von Artikeln (Angebote, Rechnungen usw.).

Firmen-Einstellungen

Druckoptionen

|

[Bild]

Bild: Druckoptionen

|

1. Makro je Benutzer: Die Makros in der Druckmaske sind global und gelten für alle Benutzer. Durch Aktivieren dieses Feldes haben Sie die Möglichkeit, dass für jeden Benutzer eigene Makros hinterlegt werden können.

2. Dokumenten-Bemerkung als Ausgangsrg.-Bemerkung vorschlagen: Wenn Sie dieses Feld aktivieren, wird die Dokumenten-Bemerkung in der Druckmaske als Ausgangsrechnung-Bemerkung vorgeschlagen.

3. Drucken und Beenden ohne Nachfrage: Wenn Sie dieses Feld aktivieren, wird Ihr Dokument nach dem Drucken ohne Nachfrage gespeichert und geschlossen.

4. Folgeexemplar auf anderen Drucker: Bei dieser Option wird lediglich das erste Exemplar einer Rechnung, Bestellungen Angebot usw. auf dem normalen Drucker ausgegeben. Der andere Drucker muss die gleichen Seiteneinstellungen haben, damit das Folgeexemplar mit dem ersten identisch ist. Wir haben diese Funktion für Kunden eingeführt, welche die Folgeexemplare z.B. auf gelbem Papier ausgedruckt haben wollen. Es ist auch möglich, dass der „2. Drucker“ in Wirklichkeit der 2. Schacht desselben Druckers ist. In diesem Fall muss ein weiterer Drucker im Windows angemeldet werden, dessen Papieinzug auf den 2. Schacht geschaltet ist

5. Folge-Formular (!) bei Bildschirmausdruck nicht ausgeben: Diese Funktion wird sicherlich nur für wenige Kunden interessant sein, aber wir wollen zumindest darauf hinweisen. Bei den Folgeexemplaren handelt es sich oft um interne Ausdrucke, in denen z.B. die Zuschlagsfaktoren ausgegeben werden. Wenn der Bildschirmdruck nur zum Testen der Optik genutzt wird, ist die Ausgabe bei Bildschirmansicht überflüssig oder stört sogar, weil ein weiteres Fenster geschlossen werden muss.

6. Sets mit Leerzeilen je Position: Früher war es bei Labelwin üblich, dass auch zwischen den Unterpositionen eines Sets eine Leerzeile ausgegeben wurde. Da dieses eigentlich sehr unschön war, wurde es geändert. Durch diesen Schalter kann man die Leerzeilen wieder einschalten.

7. Bei Bestellungen kein Lieferdatum vorschlagen: Durch Aktivieren dieses Feldes wird festgelegt, dass beim Druck kein Datum vorgeschlagen wird. Dieses soll verhindern, dass die Ware vielleicht zu früh oder zu spät kommt. Damit Sie das Datum besser wählen können, ist ein Kalenderknopf hinter dem Eingabefeld.

8. Summe letztes Aufmaß ermitteln: Wenn Sie dieses Feld aktivieren, kann die Summe des letzten Aufmaßes ermittelt werden und ausgedruckt werden. Dieses funktioniert allerdings nur mit Sonderformularen, die wir standardmäßig nicht mit ausliefern.

|

9. Artikelschlusstext auch bei Stück- und Zeitliste sowie Aufmaßvorbereitung drucken: Wenn Sie dieses Feld markieren, werden auch Stück- und Zeitlisten sowie die Aufmaßvorbereitung mit einem Artikelschlusstext ausgedruckt.

10. Bearbeiterfeld ersetzen durch Zusatz 1-8: Über diese Eingabe können Sie festlegen, dass eines der bei der Dokumentenanlage selbst zu definierenden Felder als Vorgabe für den Bearbeiternamen bei der Druckausgabe vorgeschlagen wird. Am besten hinterlegen Sie den Bearbeiternamen als Auswahl. Dazu wählen Sie im Modul EINSTELLUNGEN den Menüpunkt <Programmbereiche> <Dokumentenerstellung> <Zusatzfelder bei der Dokumentenerstellung> an und geben die Beschriftung ein. Erfassen Sie dann die Liste der Bearbeiternamen. Lesen Sie hierzu ggf. im Kapitel 14.2.6.6 nach.

Legen Sie hier fest, welches Zusatzfeld für den Bearbeiternamen verwendet werden soll. In der Regel sollten Sie das Feld 1 nehmen.

11. Zeitliste Korrekturfaktor: Wenn Sie hier einen Faktor eingeben und eine Zeitliste ausdrucken, wird dieser Faktor für die bei den Artikeln hinterlegten Zeiten zugrunde gelegt. Wenn Sie also z.B. 10 Minuten beim Artikel hinterlegt haben und hier den Faktor 0,9 eingeben, wird auf der Zeitliste für den Artikel 9 Minuten ausgedruckt

12. - 14. ZUGFeRD PDF Ausgabe Einstellungen

Details zur Ausgabe einer ZUGFeRD PDF Rechnung können Sie im Kapitel ZUGFeRD mit PDF/A Druckertreiber nachlesen.

12. ZUGFeRD Ausgabeformat: Definieren Sie hier, in welchen Ausgabeformat Sie normalerweise ZUGFeRD Rechnungen ausgeben möchten. In Normalfall ist Extended die beste Variante, da sie mehr Detailinformationen enthält. Nutzen Sie Basic oder Comfort nur dann, wenn ein Empfänger das ganz speziell anfordert.

13. Bei ZUGFeRD PDFs auch EAN und Artnr ausgeben: Entscheiden Sie hier, ob in der ZUGFeRD Datei pro Position auch die Artikelnummer und, wenn vorhanden, auch die EAN mit ausgegeben werden soll. Auf den Druckformularen werden sie normalerweise nicht ausgegeben.

14. ZUGFeRD Kommission: Wenn die Software des empfangenen Systems zur automatischen Verbuchung eine Kommissionsnummer auslesen möchte, dann können Sie hier festlegen, wie sich diese zusammensetzt.

Wir empfehlen: @KDfremdnummer1@ @TXBemerkung@

D.h., bei Rechnungen aus dem Kundendienst kommt die Fremdnummer1 as dem Kundendienst. Dies ist häufig die Auftragsnummer der Wohnungsbaugesellschaft. Für Projektrechnungen kommt die Bemerkung aus dem Dokumentenkopf.

Es stehen alle Schlüsselworte aus dem Bereich TX und KD zur Verfügung.

15. Nur eigene Drucker anzeigen: Für Kunden, die mit einem Terminal-Server arbeiten, ist es oft nervig, wenn sie nur lokal drucken und trotzdem alle Drucker angezeigt bekommen. Durch Aktivieren dieses Feldes werden nur die eigenen lokalen Drucker angezeigt.

16. Druckerliste alphabetisch sortieren: Aktivieren Sie dieses Feld, wenn die Druckerliste in der Druckerauswahl alphabetisch sortiert sein soll.

17. Ok: Durch Betätigen des OK-Knopfes werden die Änderungen übernommen und die Maske wird geschlossen.

18. Abbruch: Durch Betätigen des Abbruch-Knopfes wird die Maske geschlossen, ohne dass Änderungen übernommen werden.

Adressen-Ausgabeform

|

[Bild]

Bild: Adressen-Ausgabeform

|

1. keine Leerzeile zwischen Straße und Ort: Durch Aktivieren dieses Feldes verhindern Sie gemäß der neuen Postregel die Leerzeile zwischen Straße und Ort.

2. Zeile des Ansprechpartners zusätzlich drucken: Wenn Sie dieses Feld aktivieren, wird die Zeile des Ansprechpartners zusätzlich mit ausgedruckt.

3. Text vor Versandadresse: Geben Sie hier den Text ein, der vor einer Versandadresse stehen soll z.B. c/o

Titelzusammenstellung

|

[Bild]

Bild: Titelzusammenstellung

|

1. Titelüberschrift bei Summe wiederholen: Über diese Funktion können Sie festlegen, ob beim Drucken mit Titeln die Titelsumme die Wiederholung der Titelzeile enthalten soll.

Beispiel:

Titel Kesselanlage

Summe: Titel Kesselanlage

2. Ersatz für Summe: Bei Wiederholung der Titelüberschrift wird in der Regel das Wort ‚Summe‘ vorangestellt. Soll ein anderes Wort verwendet werden, müssen Sie es hier eingetragen.

UST-Identnummer

|

[Bild]

Bild: UST-Identnummer

|

1. Warnung USt-Identnummer: Wenn Sie Rechnungen ins Ausland verschicken, kann es je nach Land erforderlich sein, dass die Umsatzsteuer-Identnummer mit auf der Rechnung erscheint. Hier können Sie wählen, ob und wann eine Warnung erfolgen soll.

2. USt-Indentnummer bei Gutschriften erforderlich: Wenn Sie dieses Feld aktivieren, können Sie Gutschriften nur noch drucken, wenn eine USt-Identnummer eingetragen wurde.

3. USt-ID-Nr erforderlich, wenn Gesamtsumme größer ist als: Hier können Sie festlegen, dass eine USt-Identnummer erst ab einem bestimmten Betrag erforderlich ist. In Österreich ist die Erfordernis vom Betrag abhängig. Wenn Sie hier nichts einsetzen gilt keine Grenze nach oben.

Währung

|

[Bild]

Bild: Währung

|

1. Vorgabe: Ausgabe mit 2. Währung: Dieser wurde im Zuge der Euroumstellung eingeführt. Durch Aktivieren des Feldes hat man die Möglichkeit, eine 2. Währung mit auszugeben. In der Textvorgabe können Sie einen entsprechenden Text einsetzen, der dann mit ausgedruckt wird.

Texte Kopie-Folgeexemplar

|

[Bild]

Bild: Texte Kopie Folgeformular

|

1. Kopie-Texte Rechungen: Alle Rechnungskopien und Rechnungsnachdrucke müssen als solche gekennzeichnet sein (Vorschrift der GOBD). Sie können hier festlegen, mit welchem Text Sie diese Exemplare kennzeichen wollen. Sollten Sie keinen Text eingeben, werden diese Formulare automatisch mit dem Wort "Kopie" versehen.

2. Kopietext Rechnungen Folgeformulare: Alle Rechnungskopien und Rechnungsnachdrucke müssen als solche gekennzeichnet sein (Vorschrift der GOBD). Sie können hier festlegen, mit welchem Text Sie diese Exemplare kennzeichen wollen. Folgeexemplare können bei Bedarf mit einem anderen Text gekennzeichnet werden als Folgeformulare.

3. Kopietext Angebote: Angebotskopien können als solche gekennzeichnet werden. Sie können hier festlegen, mit welchem Text Sie diese Exemplare kennzeichen wollen.

4. Kopietext Auftragsbestätigungen: Kopien von Auftragsbestätigungen können als solche gekennzeichnet werden. Sie können hier festlegen, mit welchem Text Sie diese Exemplare kennzeichen wollen.

Stations-Einstellungen

Druckausgabe

|

[Bild]

Bild: Druckausgabe

|

1. Drucker für Folgeexemplare: Wenn Sie das 2. und 3. Exemplar eines Ausdruckes auf einen anderen Drucker ausgeben möchten, so können Sie hier den entsprechenden auswählen.

2. Drucker für Folgeformulare: Bei manchen Druckausgaben kann hinter der normalen Ausgabe ein anderes Formular ausgegeben werden. Die Einrichtung solcher Folgeformulare erfolgt im Modul EINSTELLUNGEN unter dem Menüpunkt <Programmbereiche> <Druckausgabe> <Report.ini bearbeiten>. Lesen Sie hierzu im Kapitel 14.2.8.2 nach.

3. Drucker für Überweisungen: Sie beim Rechnungsdruck Überweisungsträger für den Kunden beilegen möchten, so können Sie hier den Drucker dafür auswählen.

4. Formular für Überweisungen: Wählen Sie hier den Formularnamen für den Überweisungsträger aus.

5.+6. Elo und Edoc-Drucker: Diese Festlegung ist nur dann erforderlich, wenn im Netz mehrere Drucker mit dieser Bezeichnung existieren. Ohne diese Festlegung wird der erstbeste Drucker mit Elo bzw. Edoc am Anfang genommen.

Besonders bei den Edoc-Treibern kann kein x-beliebiger genommen werden, da in dessen Grundeinstellungen arbeitsplatzbezogene Einstellungen hinterlegt sind.

7. Pfad der pdftk.exe: Hier wird der Pfad zur pdftk.exe hinterlegt. Die komplette Einrichtung finden Sie unter PDFTK einrichten.

8. ZUGFeRD-Drucker: Hier muss der Drucker gewählt werden, der bei der Erzeugung von ZUGFeRD Rechnungen verwendet werden soll.

9. Pfad für Dateien: Hier muss der Pfad zur ZUGFeRD XML Datei eingetragen werden.

10. keine Anzeige VK-Preis und Zeit: In der Maske der Druckausgabe wird die Gesamtsumme und die Arbeitszeit des aktiven Dokuments angezeigt. Dieses kann störend sein, z.B. beim der Lieferscheinschreibung an einem Platz mit Kundensicht. Durch Aktivieren dieses Feldes können Sie die Anzeige wegschalten.

11. keine Anzeige EK: Bei der Rechnungsschreibung mit Kundensicht ist es natürlich unerwünscht, dass Ihr Kunde den EK sieht. Durch Betätigen dieses Feldes wird der EK in der Druckmaske weggesetzt.
