# 3. ZUGFeRD Einstellungen in Labelwin

Pfad: Einrichtungsarbeiten > ZUGFeRD mit PDF/A Druckertreiber (eDocPrintPro PDF/A) > 3. ZUGFeRD Einstellungen in Labelwin
Quelle: handbuch/3__zugferd_einstellungen_in_labelwin.htm

|

3. ZUGFeRD Einstellungen in Labelwin

Starten Sie pro Benutzer, wo der ZUGFeRD Druckertreiber installiert ist, in Labelwin das Modul „Einstellungen“ und dann den Menüpunkt <Programmbereiche>, <Druckausgabe>, <Grundeinstellungen>. Wählen Sie links unter Stations-Einstellungen die Option „Druckausgabe“.

[Bild]

Wählen Sie in der Gruppe ZUGFeRD-Drucker den entsprechenden Drucker aus und tragen Sie bei „Pfad für Dateien“ den Pfad ein, den Sie auch im Druckertreiber hinterlegt haben. Allerdings nur den Pfad, also ohne den Dateinamen.

Wechseln Sie jetzt links unter Firmeneinstellungen auf die Option „Druckoptionen“. Wählen Sie das Standard ZUGFeRD Ausgabeformat. Wir empfehlen „Extended“. Das ist die umfangreichste Option. Mit „Basic“ und „Comfort“ werden weniger Informationen in die Datei geschrieben, so dass der Nutzen beim Empfänger sinkt. Wählen Sie die beiden einfachen Formate nur aus, wenn ein Empfänger dies explizit fordert.

[Bild]

Mit der Option „Bei ZUGFeRD PDF’s auch EAN und Artnr ausgeben“ wird in die Datei pro Artikelposition auch die Artikelnummer und, wenn vorhanden, die EAN Nummer mit ausgegeben. Standardmäßig passiert das nicht, denn auf den meisten Druckformularen wird die Artikelnummer/EAN auch nicht ausgegeben.

Wenn die Software des empfangenen Systems zur automatischen Verbuchung eine Kommissionsnummer auslesen möchte, dann können Sie im "ZUGFeRD Kommissionstext" festlegen, wie sich diese zusammensetzt.

Wir empfehlen: @KDfremdnummer1@ @TXBemerkung@

D.h., bei Rechnungen aus dem Kundendienst kommt die Fremdnummer1 as dem Kundendienst. Dies ist häufig die Auftragsnummer der Wohnungsbaugesellschaft. Für Projektrechnungen kommt die Bemerkung aus dem Dokumentenkopf.

Hinweis: Es stehen alle Schlüsselworte aus dem Bereich TX und KD zur Verfügung.

Firmendaten

Die Firmendaten sind globale Einstellungen und brauchen daher nur einmal angepasst werden.

Wählen Sie nun im Modul „Einstellungen“ den Menüpunkt <Grundeinstellungen>, <Firmendaten>. Auf dem ersten Reiter müssen Sie unten Ihre „Eigene Adresse“ auswählen. Aus dieser Adresse werden Name und Anschrift, sowie ggf. USt-ID und Steuernummer für die ZUGFeRD-Datei gezogen.

[Bild]

Über den Reiter „Bankdaten“ müssen Sie die IBAN und BIC hinterlegen, die in der ZUGFeRD Datei als Bankverbindung erscheinen soll. Außerdem muss im feld REG-Info ein Text stehen, der alle rechtlich notwendigen Informationen wie Handelsregister, Geschäftsführer etc. enthält. Das Gesetz schreibt vor, dass die eingebettete XML Datei alle gesetzlich notwendigen Informationen enthalten muss, die auch eine auf Papier gedruckte Rechnung benötigt (auch wenn es für eine Verarbeitung nicht notwendig ist).

[Bild]
