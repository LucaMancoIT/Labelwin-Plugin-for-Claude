# Version 5.87 (September 2018)

Pfad: Updatetexte (bisher) > Update 2018 > Version 5.87 (September 2018)
Quelle: handbuch/version_5_87__september_2018_.htm

|

Version 5.87 (September 2018)

Versionswechsel auf 5.87 - Änderungen September 2018

Löschen von Angeboten, Bestellungen usw. mit vergebener Nummer wieder möglich

Wie einige Anwender vielleicht gemerkt haben, hatten wir in der Version 5.86 das Löschen von Dokumenten mit vergebener Nummer generell blockiert. Diese Anforderung hatten wir aus der GoBD heraus interpretiert, weil alle geschäftsrelevanten Dokumente aufbewahrt werden müssen. Buchprüfer würden ggf. gerne auch Angebote sehen, die nicht zum Auftrag geworden sind, aber wie wir jetzt wissen, haben sie darauf keinen Anspruch.

Natürlich gibt es viele Gründe, solche Dokumente nicht zu löschen (z.B. wegen einer Angebots-Erfolgsauswertung), aber wir haben die Verantwortung jetzt in Ihre Hand gelegt. Im Einstellmodul unter den Menüpunkten <Programmbereiche>, <Dokumentenerstellung>, <Löschrecht GoDB> können Sie nun festlegen, welche Dokumententypen löschbar sind. Die Rechte, wer ein Dokument wirklich löschen darf oder es nur in den Papierkorb verschieben darf, gelten natürlich weiterhin.

|

Wareneingang auf KD-Aufträge

Beim Buchen des Wareneinganges auf einen Kundendienstauftrag kann nun ein Materialzettel angelegt oder ergänzt werden. Speziell für einen KD-Auftrag gekauftes Material steht damit dem Mitarbeiter auf der Baustelle beim mobilen Kundendienst oder bei Druck auf Papier zur Verfügung.

Diese Funktion kann Ihnen das Zusammenkopieren von Eingangslieferscheinen oder gar die manuelle Erfassung ersparen.

Da nun je nach bisheriger Verfahrensweise diese Funktion zu doppelten Einträgen führen kann, muss sie bewusst aktiviert werden. Dies geschieht im Einstellmodul unter: Programmbereiche – Lager

Bitte beachten Sie, das die Funktion keine bereits vorhanden Eingangslieferscheine automatisch in den Materialzettel kopiert.

|

[Bild]

|

Drucken von Rechnungen zu KD-Aufträgen auf den E-Doc-Drucker

Beim Drucken von Rechnungen zu KD-Aufträgen konnte bereits die PDF-Datei des Auftrages mit an die Rechnungs-Datei angehängt werden. Wenn allerdings auch Folgeaufträge existierten, waren diese Berichte nicht dabei. Nun werden automatisch auch alle PDF-Dateien von vorhandenen Folgeaufträgen mit angehängt. Dazu muss das Kreuz bei ‚KD-Scan anhängen‘ gesetzt werden

Hinweis: Wenn Sie direkt aus der Druckmaske heraus über die Hinterlegung ‚als Email senden‘ gearbeitet haben, hat wurden schon lange alle PDFs angehängt. Mit dieser Änderung ist das Verhalten also identisch.

Bei allen Funktionen wie ‚Speichern‘, Anzeigen‚ E-Mail. usw.‘ verhält sich das System ebenso.

|

[Bild]

Löschen und ändern von Zeitwirtschaftseinträgen

Alle Änderungen von Zeitwirtschaftseinträgen werden nun protokolliert. Diese wurde aufgrund von Anforderungen der Finanzprüfer benötigt. Gelöschte Zeitwirtschaftseinträge werden nicht mehr aus der Datenbank gelöscht, sondern über ein Kennzeichen markiert. Somit werden diese Einträge in den ‚normalen‘ Listen nicht mit ausgegeben. Im dem seltenen Fall, dass diese Datensätze benötigt werden, kann man die gelöschten Informationen mit ausgeben.

|

Ausgangsrechnungen prüfen, weitere Funktionen

1) In der Maske gibt es nun ein Ankreuzfeld, mit dem sofort nach ‚Prüfen‘ oder ‚Fehlerhaft‘ die nächste Rechnung gezeigt wird, der Maskenwechsel kann damit entfallen

2) Sie haben bei der Prüfung von Ausgangsrechnungen zu KD-Aufträgen jetzt direkten Zugriff auf die Auswertungsmaske des einzelnen KD-Auftrages. Somit stehen Ihnen alle Daten des KD-Auftrages auf einen Klick zur Verfügung.

3) In der Übersichtsmaske ist die Anzahl der fehlerhaften Rechnungen sichtbar, so dass sie nicht mehr versehentlich liegen bleiben können.

|

[Bild]

|

Kalender / Balkendiagramm, eigenes Team möglich

Um die Kalenderfunktionen im Kundendienst noch effektiver benutzen zu können, haben Sie jetzt die Möglichkeit, ein temporäres, eigenes Team anzulegen. Wählen Sie hierzu bei den Eingrenzungen die Option ‚Bestimmtes Team‘ und in der Liste der Teams den neuen Eintrag ‚Eigenes Team‘.

Beim ersten Mal werden Sie nach einer Warnung zur Teamkonfiguration geleitet. Dort können Sie ein Team mit Mitarbeitern zusammenstelllen. Dieses Team wird dann gespeichert und steht nur Ihnen bis zur nächsten Änderung immer als eigenes Team zu Verfügung.

Um dieses Team schnell auswählen zu können steht Ihnen der Menüpunkt Ansicht – eigenes Team zur Verfügung. Dieser ist auch unter der Tastenkombination STRG + T erreichbar.

Ändern können Sie das Team unter dem Menüpunkt Datei – Eigenes Team ändern oder unter der Tastenkombination STRG + M.

|

[Bild]

Druck KD-Checklisten bei Verwendung von Geräten

Wenn beim Druck von Checklisten mit Anlage und Geräten konnte die Reihenfolge unsinnig sein. Ggf. kam die Anlagencheckliste als letztes. Diese Funktion wurde überarbeitet - es wird zunächst die Checkliste der Anlage gedruckt und dann alle Checklisten der Geräte.

Kundendienst-Bausteine

In den Bausteinen, die Sie z.B. zum Erstellen der Kundendienstrechnungen verwenden, können Sie nun auch Informationen aus dem gewählten Ansprechpartner verwenden. Bitte schauen Sie bei der Bausteinerstellung über den Knopf Schlüsselworte in den Programmbereich "Kundendienst" und dann in die Zeile "Ansprechpartner".

[Bild]

Löschen im Papierkorb

Beim Löschen von Dokumenten aus dem Papierkorb wird nur noch die Funktion ‚dauerhaft löschen‘ angeboten. Die Funktion ‚Löschen in Papierkorb‘ gibt dort keinen Sinn.

Im Papierkorb ist es nun auch möglich, mehrere Dokumente zu markieren und gleichzeitig zu löschen. Das funktioniert natürlich nur dann, wenn der Mitarbeiter das Löschrecht hat.

Neues Handbuch, aktuell und in Webansicht

Das Handbuch erscheint nun in neuem Gewand wie eine Webseite. Damit können nun alle Kapitel nach bestimmten Inhalten durchsucht und Querverweise zu anderen Bereichen sind möglich. Neben der Optik wurde es vor allen Dingen überarbeitet und ist nun endlich halbwegs aktuell. Die Einschränkung mit ‚halbwegs‘ schreiben wir deshalb, weil es bei so komplexen Programmen wie Labelwin nicht mehr möglich ist, alles passend zu dokumentieren. Aber die Änderungen der letzten Jahre, die bisher nur in den Updatetexten zu finden waren, sind alle an die passenden Stellen im Handbuch übertragen.

Filterzeile oberhalb der Tabellen mit Tastatur erreichbar

In nahezu allen Tabellen mit einer Filterzeile kann man diese nun mit der Tastenkombination Alt + Komma erreichen.

[Bild]

Damit brauchen Anwender, die viel mit der Tastatur arbeiten, nicht mehr zur Maus zu greifen. Um den Wunsch überall zu erfüllen, haben wir diese ungewöhnliche Kombination gewählt.

[Bild]

PDF-Dateien über eigenes Modul öffnen

Alle PDF-Dateien die im Labelwin angezeigt werden, öffnen sich jetzt standardmäßig in einem Label-Fenster und nicht in dem im Windows hinterlegten Viewer. Dieses hat unter anderem den Vorteil, dass sich das Fenster seine Position auf dem Bildschirm merken kann und dass Informationen zu der Datei angezeigt werden können. Zusätzlich können z.B. ein KD-Auftrag und alle Folgeaufträge in der richtigen Reihenfolge angezeigt werden.

[Bild]

Label-CRM

Auch im CRM-Modul gibt es jetzt bei der Dokumentenliste die Möglichkeit, sich die Artikel eines Dokumentes als Tabelle anzeigen zu lassen, ohne das Dokument in Bearbeitung zu nehmen. Sie können diese Funktion entweder über die Toolbar oder das Kontextmenü aufrufen.

[Bild]

Neugestaltung der Projektoberfläche

[Bild]

Nach dem Label-CRM und dem Kundendienst wurde nun auch die Projektmaske mit der sogenannten Ribbon-Bar gestaltet. Alle bisherigen Menüpunkte sind nun in der neugestalteten Oberfläche untergebracht.

Auch alle bisher als Knopf wählbaren Funktionen sind nun in der Ribbon-Bar unter dem Punkt Start enthalten. Damit sind alle bisherigen Punkte weiterhin schnell erreichbar. Alle gewohnten Tastaturbefehle sind unverändert weiter nutzbar.

In der vorherigen Maske gab es zwei Menüpunkte, die angehakt werden konnten. Diese finden Sie nun als Ankreuzfelder unten links in der Maske.

Der Dokumentenbaum an der linken Seite ist nun immer sichtbar. Dieses ist ohne Verlust an Übersicht möglich, weil wir den Platz auf der rechten Seite durch den Wegfall der Knöpfe gewonnen haben.

Wichtiger Hinweis: Um die Ribbon-Bar optimal zu nutzen, empfehlen wir Ihnen das Video im LabelWiki. Dort lernen Sie u.a. wie Sie sich eine Toolbar selber anpassen können.

|

Digitale Bauakte und iDeXs zeitgleich importieren

Sowohl im Projekt als auch im Kundendienst ist in der Import / Export Ribbon eine weitere Schaltfläche hinzugekommen. Mit dem Punkt ‚Alles Importieren‘ werden sowohl die iDeXs als auch die Elemente der digitalen Bauakte ohne erneutes Nachfragen abgeholt

Für den mobilen Kundendienst ist dies leider noch nicht mögllich, weil beim Import oft Entscheidungen getroffen werden müssen, die einen Eingriff des Mitarbeiters erfordern.

|

[Bild]

Zeitwirtschaft, runden von Arbeitswerten

Der Schalter ‚Zeiten runden auf Basis der Arbeitswerte‘ rundete bisher nur das Ergebnis der Stunden. Nun werden auch die Arbeitswerte selber gerundet. Erforderlich ist dies, wenn die Zeiten über eine Uhrzeiterfassung reinkommen und dennoch mit Arbeitswerten gearbeitet werden soll..

Aufgaben mit Termin, ggf. Warnung wenn schon vergeben

Wenn Aufgaben mit einem Termin versehen werden, prüft Labelwin nun, ob der Mitarbeiter an jenem Tag ggf. bereits anderweitig beschäftigt ist. Das kann durchaus auch Urlaub sein, bei dem bisher keine Warnung kam.

Digitale Bauakte, diverse Erweiterungen

1) Bei jeder Person und bei jedem Projekt kann festgelegt werden, ob der User nur Leserechte im Projekt hat, oder ob auch Dokumente hochgeladen werden dürfen.

Hintergrund: Eine Firma will in einem speziell dafür eingerichtetem Projekt für alle Mitarbeiter alle Informationen, Formulare, Vorschriften usw. hinterlegen. Wenn ein neues Dokument hochgeladen wird, können alle Mitarbeiter darüber mit einer E-Mail informiert werden. Verständlicherweise soll außer der Zentrale dort niemand was hinzufügen können.

2) Die eigenen Mitarbeiter können nun in der Personalerfassung einzeln oder auch auf einen Rutsch (Mehrfachmarkierung und Menüpunkt) für die Digitale Bauakte mit einem Webuser-Namen versehen werden.

3) Wenn die Mitarbeiter einen Zugang haben (voriger Punkt), können sie sehr schnell für ein Projekt frei geschaltet werden. In der Freigabemaske gibt es dazu einen neuen Knopf ‚Personal‘, mit dem ein ganzes Team oder auch frei anklickbar die Mitarbeiter gewählt werden können.

4) Sie können nun ein eigenes Logo hochladen, damit der Bezug zu Ihrer Firma besonders für Außenstehende (am Bau beteiligte Personen) besser sichtbar ist.

5) Zum Thema Datenschutz werden jetzt bei der ersten Anmeldung Hinweise gegeben, die bestätigt werden müssen. Diesen Text können Sie selbst festlegen, sonst erscheint die von uns entwickelte Vorlage.

6) Dokumente können nun auch per neuem Knopf aus der Dokumenteninfo heraus frei gegeben werden. Dabei ist übrigens auch sichtbar, wer bisher Zugriff auf das aktive Dokument hat und man kann auch dort die Berechtigung entziehen.

7) Über ein neues Recht kann nun festgelegt werden, wer Dokumente für die Digitale Bauakte freigeben darf.

Emailversand mit mehreren Anhängen und aus verschiedenen Projekten

Die Anhänge einer E- Mail aus Labelwin heraus können nun auch aus verschiedenen Projekten zusammen gesucht werden. Möglich wurde dies durch den Knopf in der Dokumentenauswahl ‚Anderes Projekt‘, mit dem in beliebigen anderen Projekten gesucht werden kann.

Interessant ist sicherlich auch, dass mit der Mehrfachmarkierung gleich mehrere Dokumente gewählt und versendet werden können.

Aufgaben anlegen beim Druck von Rechnungen, Angeboten usw.

Seit einiger Zeit können beim Druck von Angeboten, Bestellungen und Preisanfragen automatisch Aufgaben angelegt werden. Dies wurde um den Punkt Rechnungen erweitert.

Hintergrund: Eine Firma will bei manchen Rechnungen nachfragen, ob der Kunde den in der Nachbemerkung angebotenen Wartungsvertag abschließen möchte.

Um die Aufgabe wahlweise erstellen zu können, haben wir nun eine Fragemöglichkeit eingebaut. Sie erscheint, wenn der Drucken-Knopf ausgelöst wird.

[Bild]

Details lesen Sie im Handbuch unter Aufgabenverwaltung.

Module Rechnungseingangsbuch, Kassenmodul und Postbox-Verteiler auf V5 Oberflächen umgestellt

Hier gibt es eigentlich nicht viel zu schreiben. Die Funktionen sind weitgehend gleich geblieben, aber das Ganze sieht zeitgemäßer aus. Auch die von allen Anwendern geliebte Filterzeile steht damit in diesen Bereichen zur Verfügung.

Eingangsrechnungen prüfen, Prüfer auch bei bezahlten Rechnungen umsetzbar

Um Fehler zu verhindern konnte bisher bei bezahlten Eingangsrechnungen der Prüfer nicht gewechselt werden. Es gibt jedoch Firmen, bei denen wg. der Skontofrist auch ungeprüfte Rechnungen bezahlt werden und sie sich bei Fehler trotzdem mit dem Lieferanten einigen können. Da wir uns dieser Argumentation nicht verschließen können, ist es nun auch möglich bereits bezahlte Rechnungen zu prüfen und ggf. auch den Prüfer umzusetzen..

ZUGFeRD Rechnungen, Fehler bei Schalter ‚immer eigene Zahlungsbedingungen‘

Bei der Umsetzung von Gaeb-Rechnungen (sind tot) auf ZUGFeRD wurde der Schalter ‚immer eigene Zahlungsbedingungen nehmen‘ nicht berücksichtigt. Wen also heute die Maske mit unterschiedlichen Zahlungsbedingungen aus den Stammdaten und der jeweiligen ZUGFeRD-Rechnung stört, kann festlegen, dass immer sein in der Adresse hinterlegten Werte gelten.

Automatische Artikelverknüpfung, neue Prüfungen, neue Möglichkeiten

Im Katalogmodul können Verknüpfungen zwischen 2 Katalogen automatisch aufgebaut werden, wenn es gemeinsame Merkmale bei den Artikeln gibt. Im optimalen Fall ist dies die EAN-Nummer (heute heißt sie offiziell GTIN), manchmal die gleiche Artikelnummer, Suchwort, Herstellernummer oder was auch immer.

Da es vor einigen Monaten große Probleme gab, als ein Lieferant die gleiche EAN-Nummer bei einer kompletten Warengruppe verwendet hat, gibt es nun Prüfungen. Das gewählte Merkmal darf weder in der Zieldatei, noch in der Quelle mehrfach verwendet sein. Wenn es doppelte gibt, wird der Durchlauf abgewiesen. Sie können nun aber die Artikel mit identischen Merkmalen anzeigen lassen, um das Problem ggf. selbst zu beseitigen oder dem Lieferanten zu informieren.

Ebenfalls ist es möglich, einen Probelauf mit Protokoll zu starten, um zu schauen, ob die Verknüpfung korrekt läuft.

Hintergrund: Warum Verknüpfungen ?

Wenn Artikel von verschiedenen Lieferanten miteinander verknüpft sind, können sie bei einer Bestellung leicht gegen die Artikelnummer des anderen ausgetauscht werden. Zusätzlich kann man erkennen, wer ein Bauteil zum niedrigsten Preis liefert und ggf. sogar beim Aufruf immer den Artikel vom billigsten nehmen.

|

Schnittstelle zum Formularprogramm des Fachverbandes NRW

Innungsmitglieder können diverse Formulare des Fachverbandes im Web ausfüllen und sich dann eine PDF erzeugen lassen. Bei Labelwin können nun die Adressen an den Formularserver übertragen werden und das fertige PDF automatisch im Labelwin-Projekt abgelegt werden. Die Funktion steht allen Nutzern kostenlos zur Verfügung, ledigtlich mit dem Verband muss ein Vertag abgeschlossen werden.

So geht’s: Sie legen in Labelwin ein neues Dokument der Art ‚Anderes Dokument an. Nachdem Sie alles ausgefüllt und die Adressen gewählt haben, schließen Sie die Maske nicht mit ‚Okay‘, sondern wählen die Menüpunkte <Datei>, <Formularserver starten> an.

Wählen Sie dann das Formular in Programm des Verbandes, füllen alles aus und beenden das Programm. Wählen Sie danach erneut den Menüpunkt <Datei> an und übernehmen die Pdf in die Labelwin-Dokumentenverwaltung.

Details lesen Sie im Handbuch unter Formularserver SHK NRW.

|

[Bild]

ZUGFeRD-Rechnungen schreiben

Mit einer speziellen Version des Edoc-Druckertreibers können Sie nun auch selber Rechnungen in diesem Format erzeugen. Der Treiber kostet etwa 100 € pro Arbeitsplatz, wobei bei den meisten Betrieben sicherlich erst mal eine Lizenz ausreichend ist. Alles weitere lesen Sie im Handbuch unter ZUGFeRD-Rechnungen mit PDF/A Druckertreiber.

Aufmasserfassung, Schulungsvideo

Das Video finden Sie im Label-Wiki und im Kapitel Aufmaßerfassung und ist auch für Mitarbeiter interessant, die schon lange mit diesem Bereich arbeiten. Es sind einige Tricks beschrieben, mit denen die Arbeit vielleicht schneller erledigt werden kann.

Postbox Stapelablage per OCR

Mithilfe der Postbox, die Teil des Zusatzmoduls SCAN-ARCHIV ist, besteht die Möglichkeit einer automatischen Stapelablage von gescannten KD-Aufträgen. Voraussetzung hierfür sind durchsuchbare PDF-Dateien und eine eindeutige Kennung auf dem KD-Formular (die sogenannte SCANID). Details erfahren Sie im Kapitel KD-Aufträge automatisch ablegen.
