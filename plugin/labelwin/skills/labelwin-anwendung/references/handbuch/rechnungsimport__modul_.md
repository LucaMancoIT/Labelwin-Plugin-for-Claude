# Rechnungsimport [Modul]

Pfad: Buchhaltung > Rechnungsimport [Modul]
Quelle: handbuch/rechnungsimport__modul_.htm

|

Rechnungsimport [Modul]

Stand: 01.10.2018

(V5.87)

Die Erfassung von Eingangsrechnungen und deren Prüfung ist relativ zeitaufwändig. Wenn die Rechnung dagegen importiert werden kann, so dass sich die Erfassarbeit auf minimale Eingaben beschränkt, kann dies dem Anwender die Arbeit in vielerlei Hinsicht erleichtern:

-

Rechnungsbuchung: Die Buchungsmaske ist schon beim Öffnen mit allen buchungsrelevanten Informationen ausgefüllt.

-

Archivierung: Der Computer archiviert die Rechnung automatisch und erstellt zu jedem einzelnen gekauften Artikel eine Einkaufshistorie.

-

Rechnungsprüfung (Preisvergleich mit Bestellung/Lieferschein): Wenn für die entsprechende Rechnung eine Bestellung oder ein Eingsangslieferschein im System ist, kann automatisch ein positionsbezogener Vergleich der

Mengen und Preise stattfinden. Dabei wird kontrolliert ob der Rechnungsbetrag mit dem der Bestellung und die Mengen mit dem Lieferschein übereinstimmen.

-

Positionsübernahme: Die Positionen aus der ZUGFeRD-Eingangsrechnung können direkt in die Ausgangsrechnung übernommen werden.

Derzeit gibt es für die Handwerksbranche zwei Verfahren eine Eingangsrechnung digital zu übertragen. Dabei reden wir davon, dass auch die Inhalte bis herunter zu den Positionen digital zur Verfügung stehen. Nach dieser Definition zählt eine reine PDF-Rechnung, wie man sie oft per Email erhält, nicht dazu. Denn das ist letztlich nur ein Bild einer Rechnung und maschinell nicht auswertbar.

-

Verfahren 1: UGL

Alte aber funktionierende Methode, um die Inhalte zu transportieren. Die Rechnung selbst muss dabei zusätzlich per Papier oder PDF versendet werden.

-

Verfahren 2: ZUGFeRD

Dieses Verfahren entwickelt sich sehr erfolgreich. Es handelt sich um eine spezielle PDF, die zusätzlich die Daten digital enthält. Damit ist sichergestellt, dass die EDV-Daten und das Bild der Rechnung immer zusammen bleiben. Die handwerksspezifischen Dinge sind nicht umgesetzt. Da dieses Format aber bereits von vielen SHK-und Elektro-Großhändlern geliefert wird, bietet es die größten Vorteile. Auch die Datev treibt den Einsatz voran. Zusätzlich kommt es auch in anderen Branchen zum Einsatz. Wer z.B. einen Mähdrescher kaufen will, bekommt bei Claas eine ZUGFeRD-Rechnung.

Wie die Datei zum Handwerker kommt, ist nicht festgelegt. Sicherlich meistens per Email-Anhang, aber die ersten Lieferanten bieten auch einen halbwegs automatisierbaren Weg über FTP (File Transport Protokoll) an.

>> ZUGFeRD ist das optimale Verfahren <<

Im Labelwin sind beide Verfahren realisiert. Auch die interne Verarbeitung ist weitgehend gleich. Wegen der festen Verbindung zwischen Daten und PDF ist ZUGFeRD das optimale Format.

|

ZUGFeRD (Zentrale User Guide des Forums elektronische Rechnung Deutschland) bezeichnet ein Format für elektronische Rechnungen. ZUGFeRD-Rechnungen zeichnen sich gegenüber anderen e-Rechnungsformaten als hybrides Rechnungsformat dadurch aus, dass sie Maschinenlesbarkeit und Menschenlesbarkeit in einem Dokument vereinen. Dafür wird in eine herkömmliche PDF-Datei eine XML-Datei eingebettet. Dieses Dokument verhält sich wie jede andere PDF-Datei und kann mit allen gängigen PDF-Readern geöffnet werden. Die eingebettet XML-Datei kann nur mit bestimmen Programmen wie z.B. Labelwin ausgewertet werden. Dadurch kann der Rechnungsempfäger mit entsprechender Software eine Reihe von erheblichen Vorteilen nutzen. Verfügt der Rechnungsempfänger jedoch nicht über eine solche Software, kann er die Rechnung, anders als bei anderen e-Rechnungsformaten, trotzdem lesen und verarbeiten wie eine normale Rechnung, die ihn per Mail erreicht hat. So hat der Rechnungssteller keinen Aufwand mit seinen Kunden abzusprechen, welche Rechnungsform diese verarbeiten können.

|

[Bild]

Damit Labelwin die Eingangsrechnung dem richtigen Projekt oder Kundendienstauftrag zuordnen kann, muss die Rechnung eindeutig gekennzeichnet sein. Dafür kann die Bestellnummer, die Projektnummer oder die Kundendienst-Auftragsnummer verwendet werden. Anders als das Format UGL ist ZUGFeRD nicht Branchenbezogen und wird von immer mehr Betrieben verwendet. Es ist also davon auszugehen, dass bald fast alle Eingangsrechnungen den Betrieb im ZUGFeRD-Format erreichen, von Großhändler über Fahrzeugmechaniker und Internetprovider.

Mögliche Probleme:

Um eine automatische Zuordnung zum Projekt oder Kundendienstauftrag oder der Bestellung zu bekommen, müssen Sie die Kommission entsprechend angeben und vom Lieferanten passend eintragen lassen. Lesen Sie dazu bitte das Kapitel Einrichtungsarbeiten. Nur mit dieser Zuordnung werden die Vorteile einer elektronischen Rechnung voll ausgeschöpft.

Ein komplett automatischer Import wird sicherlich nie möglich sein, weil es mindestens bei telefonischen Bestellungen immer wieder Übertragungsfehler bei der Kommission geben wird. Auch das Kostenkonto und ggf. eine Kostenstelle können vom Lieferanten nicht mitgeliefert werden, so dass immer wieder Eingriffe / Eingaben erforderlich sind.

Die Hinterlegung des ‚üblicherweise‘ verwendeten Kostenkontos bei der Adresse des Lieferanten spart Arbeit und vermindert Fehler.

Auch die Zahlungsbedingungen sollten bei der Adresse hinterlegt werden, damit diese mit den Daten der Importdatei verglichen werden können. Bei Unterschieden erscheint ein Fenster in dem die Werte und die Unterschiede dargestellt werden. In diesem Fall kann gewählt werden, welche Zahlungsbedingung genommen werden soll.

Transport

Wie die digitalen Rechnungen Ihr Unternehmen erreichen ist letztendlich egal. Das kann zum Beispiel per E-Mail oder FTP-Download passieren. Es ist wünschenswert, die Dateien ohne vorherige Markierung und Bereitstellung vom Lieferanten zu erhalten. Dabei kann der Transfer per FTP-Protokoll 'auf einen Rutsch' stattfinden. Welchen Transportweg Sie wählen, müssen Sie mit Ihrem Lieferanten absprechen.

Umgang mit Kommissionen

Der nachfolgend beschriebene Umgang mit Bestell- und Auftrags- und Projektnummern bei Bestellungen und Einkäufen ist erforderlich, um einen reibungslosen Import zu bekommen.

- wenn möglich per IDS oder UGL bestellen

- bei schriftlicher Bestellung muss die Bestellnummer vom Lieferanten in das Feld ‚Vorgangsnummer des Handwerkers' eingetragen werden

- bei Online-Bestellungen muss die Bestellnummer (wenn vorhanden) vom Anwender in das Feld Vorgangsnummer geschrieben werden.

- wenn keine Bestellnummer vorhanden ist, sollte die Projektnummer oder die Kundendienst-Auftragsnummer mit einem vorangestellten k (=Kundendienst) oder p (=Projektnummer) geschrieben werden.

[Bild]

Hinter dem p und k kann auch eine Leerstelle sein, Labelwin erkennt es mit und ohne Leerstelle.

- bei Erfassung des Wareneingangs sollte die komplette Lieferscheinnummer des Lieferanten erfasst werden. Da diese in der UGL-Rechnung geführt wird, ist damit ein eindeutiger Vergleich zwischen den Preisen der bestellten Ware und den berechneten Artikeln möglich.

|

Tipp: Artikel des Lieferanten aus den Eingangsrechnungen anzeigen

Da mit den Verfahren UGL und ZUGFeRD die Rechnungspositionen übertragen werden und diese in ein Labelwin-Dokument übertragen werden (als ‚Freier Text‘ in einem festgelegten Projekt) bietet sich eine Anzeige und Suchfunktion an.

Im Modul Adressen unter dem Menüpunkt <Anzeigen> können Sie die gekauften Artikel sehen und in der Liste auch suchen.

Hinweis: Die Eingangsrechnungen müssen mit dem Modul Rechnungsimport eingelesen worden sein.
