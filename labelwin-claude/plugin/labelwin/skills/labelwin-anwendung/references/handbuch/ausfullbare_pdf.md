# Ausfüllbare PDF

Pfad: Schnittstellen > Ausfüllbare PDF
Quelle: handbuch/ausfullbare_pdf.htm

|

Ausfüllbare PDF

Stand: 28.03.2019

(V5.89)

Hintergrund: Unsere Kunden erhalten von Ihren Geschäftspartner (Lieferanten, Planungsbüros etc.) zunehmend PDF-Dateien, die ausfüllbare Felder enthalten Bei diesen Feldern handelt es sich oft um Namen und Adressen oder andere Informationen, die in Labelwin vorliegen und bisher immer manuell übertragen werden mussten. Darüber hinaus entstand das Bedürfnis aus einem Kundendienstauftrag eine ausfüllbare PDF-Datei zu generieren.

Es gibt nun eine neue Funktion mit der solche ausfüllbaren PDF-Dateien weitestgehend automatisiert ausgefüllt bzw. erzeugt werden können. Ausfüllbare PDF-Dateien können in drei Bereichen eingesetzt werden:

-

Druckausgabe

-

Dokumentenerstellung

-

Kundendienst-Auftragsdruck

EINRICHTUNG

1. „Ausfüllbare PDF“ aktivieren

Zur Aktivierung der Funktion muss zuerst ein Schalter in Global.ini gesetzt werden:

[Grundeinstellungen]

pdfausfuell=1

Vorsicht: Ist der Schalter schon vorhanden, dann muss er von =0 auf =1 umgesetzt werden.

2. PDF-Vorlage(n) anlegen

Es gibt einen neuen Menüpunkt im Einstellmodul unter [Vorlagen – PDF-Vorlagen].

[Bild]

Zuerst zieht man die ausfüllbare PDF-Datei per Drag & Drop auf die Maske der Vorlagenbearbeitung und vergibt einen Namen im Feld „Bemerkung“. Außerdem muss der Bereich der Verwendung gewählt werden. Möglich sind Kundendienst, Dokument und Druckausgabe.

Darüber hinaus ist auch die Zuordnung zu einer Gruppe möglich. Das macht aber nur Sinn, wenn man viele Vorlagen hat, die man zur besseren Übersicht in Gruppen einteilen möchte.

Im nächsten Schritt müssen die Verweise gefüllt werden.

3. Verweise in der Vorlage ausfüllen

Um automatisiert Daten aus Labelwin in eine ausfüllbare PDF zu bekommen, müssen die Eingabefelder der PDF mit den entsprechenden Schlüsselworten aus Labelwin versehen werden.

Labelwin liest alle ausfüllbaren Felder der PDF-Datei aus und listet diese in der linken Spalte „Bezeichnung in PDF“ auf. Sollte schon etwas in einem Feld stehen, wird das in der rechten Spalte „Inhalt in PDF“ angezeigt. Soll dieser Eintrag dauerhaft verwendet werden, kann dieser verbleiben und muss nicht durch ein Schlüsselwort ersetzt werden.

[Bild]

Wichtig ist nun die Zuordnung der Labelwin Schlüsselworte zu den ausfüllbaren Feldern.

Das Labelwin Schlüsselwort muss in das Feld „Inhalt bei Ausgabe“ eingetragen werden. Das Feld „Rückgabe Schlüsselwort“ ist nur wichtig, wenn so eine PDF später wieder zurückkommt und von Labelwin ausgelesen werden soll. Dieses Feld kann also vorerst leer bleiben.

|

Tipps Schlüsselwörter

-

Schlüsselworte der Artikeldaten (Art.Nr, Menge etc.) befinden sich im Bereich „Artikelschlusstexte [ART]“.

Sollen mehrere Artikel ausgegeben werden, müssen die Schlüsselworte um eine Ziffer erweitert werden, z.B. @ARTArtnr1@, @ARTArtnr2@, etc.

-

Schlüsselwort für einen zweiten Monteur im KD-Auftrag:

Soll auch ein weiterer Monteur, der im KD-Auftrag hinter dem Button "Monteur" erfasst wurde, ausgegeben werden, muss das Schlüsselwort @montname2@ verwendet werden. Der Hauptmonteur wäre @montname1@.

Sollten die Bezeichnungen der ausfüllbaren Felder in der PDF-Datei nicht eindeutig sein, kann man sich mit dem Knopf „PDF mit Inhalt zeigen“ behelfen. Hier wird die PDF-Datei geöffnet und alle ausfüllbaren Felder werden mit ihrer Bezeichnung bzw. dem bereits vorgenommen Eintrag bei „Inhalt bei Ausgabe“ angezeigt werden. Beispiel:

[Bild]

Die erzeugte Vorlagen PDF wird automatisch in den Labelwin Pfad \labelwin\Pdfvorlagen\ gespeichert. Die Original PDF bleibt unverändert.

Nachdem alle Zuordnungen vorgenommen wurden, kann man die Vorlagenbearbeitung verlassen.

ANWENDUNG

Bereich „Druckausgabe“

|

Um auf die ausfüllbare PDF-Vorlage des Bereiches Druckausgabe zugreifen zu können, muss das Label Dokument über die V5 Druckmaske aufgerufen werden. Es kann übrigens bei jedem Label Dokumententyp verwendet werden.

In der Druckmaske gibt es im Menü unter [Datei] den Eintrag [Ausfüllbare PDF].

|

[Bild]

Es öffnet sich eine Maske mit allen Vorlagen. Die gewünschte PDF-Vorlage wird mit der Pfeiltaste in der Mitte ausgewählt. Theoretisch kann man auch mehrere Vorlagen auf einmal ausfüllen lassen.

[Bild]

Im Ablagepfad muss der Ort gewählt werden an dem die erzeugte PDF-Datei gespeichert werden soll. Es wird immer der zuletzt genutzte Pfad vorgeschlagen.

Alternativ kann man die PDF auch als Dokument in Labelwin anlegen lassen. Im gleichen Projekt des Dokumentes wird dann ein Eintrag des Typs „afPDF“ angelegt. Diese Option wird über die Option „als Dokument anlegen“ aktviert.

Über das Ankreuzfeld „sofort öffnen“ lässt sich erreichen, dass die Datei direkt angezeigt wird.

|

Hinweis zu Bestellungen:

Wird eine Bestellung als ausfüllbare PDF gedruckt, so wird die Bestellung wie bei einem echten Druck in die Bestellüberwachung eingetragen. Es ist also kein weiterer Druck erforderlich.

Bereich „Kundendienst“

Ausfüllbare PDF des Bereiches Kundendienst werden in der Druckmaske des Kundendienstauftrages angeboten.

[Bild]

Über das Dropdown Menü „Vorlage“ kann die gewünschte PDF-Vorlage gewählt werden, falls es mehr als eine Vorlage gibt. Die Wahl der Vorlage kann auch über den Auswahl Button rechts daneben erfolgen. Hier erhält man die Liste alle PDF-Vorlagen für den Bereich „Kundendienst“. Es handelt sich um die gleiche Auswahl wie im Bereich „Druckausgabe“, jedoch eingegrenzt auf die Kundendienst Vorlagen.

Soll die PDF-Datei einem Mitarbeiter über eine Cloud zur Verfügung gestellt werden, kann die Option „An Monteur exportieren“ gesetzt werden. Die Datei wird dann in einem im Personalstamm definierten Ablagepfad gespeichert.

Nach Betätigung des Drucken Buttons öffnet sich das Fenster zur PDF Formularausgabe. Es stehen mehrere Möglichkeiten zur Weiterverarbeitung der eben erzeugten PDF zur Auswahl:

|

[Bild]

|

An Monteur:

Die PDF wird in dem im Personalstamm hinterlegten Export-Pfad abgelegt.

Als E-Mail:

Es wird eine E-Mail angelegt, die im Anhang die PDF enthält.

Speichern als:

Die PDF wird an einem frei wählbaren Ort gespeichert.

Anzeigen:

Die PDF wird zur Anzeige geöffnet.

Bereich „Dokument“

|

Wurde mindestens eine PDF-Vorlage für den Bereich „Dokument“ angelegt, erweitert sich die Liste der Dokumententypen um den Eintrag „Ausfüllbare PDF“.

Nach Auswahl dieses Eintrages öffnet sich wie üblich die Dokumentenanlagemaske. Hier wechselt man auf den zweiten Karteireiter „PDF Vorlagen“ und kann die gewünschte Vorlage über die Pfeiltaste in der Mitte auswählen.

|

[Bild]

[Bild]

Unten auf dieser Seite kann wiederum ein Ablagepfad eingestellt und die Option „sofort öffnen“ gewählt werden.
