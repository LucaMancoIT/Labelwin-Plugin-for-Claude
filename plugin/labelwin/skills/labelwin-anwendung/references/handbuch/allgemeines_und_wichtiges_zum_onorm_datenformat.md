# Allgemeines und Wichtiges zum ÖNorm Datenformat

Pfad: Schnittstellen > ÖNorm > Allgemeines und Wichtiges zum ÖNorm Datenformat
Quelle: handbuch/allgemeines_und_wichtiges_zum_onorm_datenformat.htm

|

Allgemeines und Wichtiges zum ÖNorm Datenformat

Das ÖNorm Datenformat ist für die Abbildung der teilweise sehr komplizierten Vertragswerke und Regeln gemäß der Verdingungsordnungen im Bauwesen konzipiert. Es ist nicht leicht, diese Strukturen in Labelwin abzubilden. Daher werden nicht alle Informationen in das Labelwin Dokument übernommen, sondern verbleiben in der Datei. Deswegen wird zum Bepreisen auch die Originaldatei wieder vorgeholt und mit den Prisen befüllt. Somit gehen die in Labelwin nicht abbildbaren Informationen nicht verloren.

Man muss daher die eingelesen Daten und die erzeugte Datei unbedingt kontrollieren. Labelwin erzeugt beim Lesen und Schreiben ein Fehlerprotokoll. Wir raten, sich dieses genau anzuschauen.

Das ÖNorm Fehlerprotokoll enthält ggf. WARNUNGEN und FEHLER, sofern welche aufgetreten sind. In diesem Fall erscheint ein roter Knopf mit Fehlerprotokoll. Bitte lesen Sie sich die Fehler durch und prüfen Sie, was zu machen ist.

Gruppierung

ÖNorm Dokumente teilen sich auf in Gruppen und Positionen.

-

Positionen: Positionen bestehen immer aus einem Grundtext, gefolgt von einer oder mehreren Positionen.

-

ULG: Die nächst höhere Ebene, in Labelwin „Titel“ genannt, heißt in der ÖNorm „Unterleistungsgruppe“ oder „ULG“

-

LG: Dadrüber kommt in Labelwin der „Bauabschnitt“ (auch „Los“ genannt). In der ÖNorm heißt das „Leistungsgruppe“ oder „LG“

-

OG: Danach folgt in Labelwin das „Bauteil“ (auch „Gewerk“ genannt). In der ÖNorm heißt das „Obergruppe“ oder „OG“

-

HG: In der ÖNorm gibt es noch eine höhere Ebene. Sie heißt „Hauptgruppe“ oder „HG“. Diese Ebene kann Labelwin nicht abbilden. Beim Einlesen wird die Gruppenüberschrift als Textartikel angelegt. Das ist für das weitere Bepreisen aber unerheblich. Lediglich das Neuerstellen eines Ausschreibungs-LV mit dieser Ebene ist in Labelwin nicht möglich.

Positionsnummern

HG, OG, LG, ULG, Grundtexte und Positionen werden mit einer eindeutigen Leistungsbeschreibung-Positionsnummer versehen. Sie setzt sich zusammen aus:

– zwei Stellen für die HG

– zwei Stellen für die OG

– zwei Stellen für die LG

– zwei Stellen für die ULG

– zwei Stellen für den Text oder Grundtext oder Position;

– allenfalls einer weiteren Stelle für den Folgepositionen. Die Sortierung erfolgt aufsteigend nach der eindeutigen Leistungsbereich-Positionsnummer.

ÖNorm LVs können mit der Gruppen HG, OG und LG beginnen. Der Start mit einer ULG (Titel) ist nicht möglich. Im Gegensatz zur deutschen GAEB Norm kann aber ein LV auch nur aus Positionen bestehen.

Beim Einlesen wird ein Dokument automatisch auf „Umnummerieren nie“ gesetzt. Ein Positionsschema wird nicht vergeben, da eine Umnummerierung nie erfolgt.

Beim Erstellen eines neuen ÖNorm Dokumentes, sollte das Positionsschema, je nach Struktur auf

-

„pp“ (Bsp.: 01),

-

„aa.tt.pp“ (Bsp.: 01.01.01) oder

-

„bb.aa.tt.pp“ (Bsp.: 01.01.01.01)

stehen.

Preisanteile

Bei der Ausgabe eine ÖNorm mit Preisen kann bei der Ausgabe entschieden werden, ob die Positionspreise und Summen nach Lohn und Material getrennt werden oder nicht. Was erlaubt bzw. vorgeschrieben ist, steht in der eingelesenen ÖNorm Datei.

Dieses können Sie in der Positionserfassung, Menüpunkt <Datei>, <ÖNorm Datei Kopfdaten> nachschlagen. Suchen Sie in der ÖNorm Datei nach dem Begriff „preisanteile“. Wenn es benannte Preisanteile gibt, dann müssen/sollen Sie entsprechend aufteilen, ansonsten nicht.

Rabatte/Nachlässe/Zuschläge

Dier ÖNorm kennt Zuschläge und Nachlässe auf Gruppenebenen und auf das komplette LV. Da die bei der ÖNorm angewandte Technik für Nachlässe und Zuschläge deutlich von der in Labelwin abweicht, können wir leider die korrekte Umsetzung nicht garantieren.

Beim Einlesen von LV’s mit Preisen und Nachlässen bzw. Zuschlägen müssen Sie das Ergebnis in Labelwin unbedingt mit dem ausgedruckten LV vergleichen Ggf. müssen Sie die Werte im Labelwin Dokument anpassen.

Beim Bepreisen von LV‘s empfehlen wir auf Nachlässe /Zuschläge im LV komplett zu verzichten und höchstens beim Schreiben der ÖNorm Datei über den Knopf „Kopfdaten“ einen manuellen Schlussrabatt bzw. Zuschlag zu erfassen.

Desweiteren weisen wir daraufhin, dass die eingelesene ÖNorm Datei vorgibt, an welchen Stellen Nachlässe und Zuschläge erfasst werden dürfen. Diese Informationen erhalten Sie ausschließlich aus der Original Ö-Norm Datei. Diese können Sie in der Positionserfassung, Menüpunkt <Datei>, <ÖNorm Datei Kopfdaten> ansehen.

Suchen Sie in der ÖNorm Datei nach dem Begriff „zugelassenenachlaesse“. Hier drunter finden Sie dann die Ebenen, wo es erlaubt ist, z.B. „auflvsumme“, „aufhgsummen“, „aufogsummen“, „auflgsummen“, „aufulgsummen“.

„Auflvsumme“ bedeutet, dass Sie einen Nachlass/Zuschlag für das gesamte Dokument über den Knopf „Kopfdaten“ bei der ÖNorm Ausgabe erfassen können.

Die anderen Arten entsprechen Labelwin Prozentpositionen am Ende eines Titels, Bauabschnitts oder Bauteils mit der Eingrenzung „Letzter Titel“. Von diesen möchten wir aber abraten, da die Ausgabe nicht hundertprozentig ÖNorm konform erfolgt!
