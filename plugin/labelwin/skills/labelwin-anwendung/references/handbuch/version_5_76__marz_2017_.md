# Version 5.76 (März 2017)

Pfad: Updatetexte (bisher) > Update 2017 > Version 5.76 (März 2017)
Quelle: handbuch/version_5_76__marz_2017_.htm

|

Version 5.76 (März 2017)

Versionswechsel auf 5.76 - Änderungen März 2017

Benutzerrechte, Maske und Anzeige überarbeitet

Da die Rechte immer umfangreicher werden, wird es zunehmend schwieriger, zu verstehen, was mit welchem Recht gesichert ist. Wir haben deshalb die Maske mit einer Suchfunktion und vielen Erklärungstexten versehen.

Projektstand, Anzeige nur für ‚eigene Projekte‘

Über ein neues Recht ist es nun möglich, dass ein Bauleiter nur die Projekte auswerten kann, bei denen er als Verantwortlicher eingetragen ist.

Ausgangsrechnungen nach Status eingrenzen (V5)

Da es durchaus sinnvoll sein kann, für den Steuerberater eine Liste der stornierten Rechnungen zu drucken, wurde die Eingrenzung nach Status geschaffen.

Einstellmodul, Buchhaltungsthemen gebündelt

Alle Einstellungen, die die Buchhaltung betrifft, finden Sie nun unter den Menüpunkten <Programmbereiche>, <Buchhaltung>. Das betrifft einige Schalter von der Maske ‚Allgemein‘, den Kontenplan, den Kostenstellen usw.

Adressen, Kürzeltaste für Anrede

Weil wir uns überreden lassen hatten, das es nicht mehr üblich sei, als Anrede ‚Herrn‘ sondern nur noch ‚Herr‘ zu schreiben, gab es einige Beschwerden. Wir haben es nun flexibel gelöst und im Modul Einstellungen unter dem Bereich Adressen, Grundeinstellungen ein neues Ankreuzfeld eingeführt. Der Standard ist jetzt wie früher auf ‚Herrn‘ und wer das Kreuz wegnimmt, bekommt künftig bei der Eingabe von h den Text ‚Herr‘ vorgeschlagen. Der Vollständigkeit halber wollen wir noch erwähnen, dass alle diese Eingabekürzel bei der Adresserfassung anpassbar sind und auch erweitert werden können. So können die Kollegen aus Luxemburg z.B. mit ma den Text ‚Mademoiselle‘ erzeugen. Das geschieht mit dem Editor Notepad (nicht Word nehmen!) in der Datei \labelwin\global.ini unter der Gruppe [adresskuerzel]

Digitale Prüfung von Ausgangsrechnungen (V5)

Mit Einführung der GoBD-Regeln ist die einfache Möglichkeit entfallen, eine Rechnung erst nach dem Ausdruck zu prüfen und dann ggf. wieder zu ändern. Wir haben nun eine Möglichkeit geschaffen, die eine wesentlich bessere Prüfung als die Betrachtung des Papierausdrucks erlaubt. Es gibt eine Kontrolle der gebuchten Zeiten, die Ansicht des Arbeitsberichts, der Deckungsbeiträge usw. Die Rechnung kann auch aus dieser Maske heraus in Bearbeitung genommen oder direkt gedruckt werden.

[Bild]

Zunächst ist im Modul ‚Einstellungen‘ ein Schalter zu setzen. Unter <Programmbereiche>, <Buchhaltung>, <Grundeinstellung> gibt es unten links ein neues Ankreuzfeld.

Wenn es gesetzt wird, werden im Hintergrund 3 neue Stati für Rechnungen eingeführt. Es sind die Stati

· zu prüfen

· geprüft

· fehlerhaft‘.

Wenn der Schalter gesetzt ist, wird beim Verlassen der Positionserfassung gefragt, ob das Dokument auf ‚zu prüfen‘ gesetzt werden soll. Nur geprüfte Rechnungen können gedruckt werden. Deshalb erfolgt auch beim Drucken der Rechnung aus der Positionserfassung heraus die Frage, ob das Dokument auf geprüft gesetzt werden soll. Das dürfen aber nur die Anwender, die das Recht dazu haben.

Standardmäßig ist dieses Recht gesetzt, weil die Anwender ja zuvor Rechnungen auch einfach ausdrucken konnten. Wenn man jemandem dieses Recht nimmt, kann derjenige die Rechnungen nicht mehr mit Nummer ausdrucken.

Die Prüfung der Ausgangsrechnungen:

Man wählt in der Projektverwaltung den Menüpunkt Extern, Ausgangsrechnungen prüfen an und gelangt in eine Maske der zu prüfenden Rechnungen. Mit dem Knopf ‚Rechnung prüfen‘ gelangen Sie in die Prüfungsmaske.

[Bild]

Viele der Knöpfe dort sind sicherlich selbsterklärend, aber auf die wichtigsten Bereiche möchten wir hier eingehen:

[Bild]

In dieser Maske sehen Sie viel mehr, als auf einer gedruckten Rechnung. Sie sehen die Einkaufspreise, die Deckungsbeiträge, die Quelle der Daten (Eingangsrechnungen, Zeitbuchungen), und können bei Kundendiensteinsätzen den Auftrag und ggf. den Arbeitsbericht sehen.

Wenn das Dokument fehlerfrei ist, können Sie von hier sofort drucken.

Bei Fehlern im Bereich der Adressen, Zahlungsbedingung, Vor- und Nachbemerkung können Sie dies über den Knopf ‚Dokumenteninfo‘ ändern.

Bei Fehlern im Bereich der Positionen können Sie das Dokument in Bearbeitung nehmen,

Sie können es aber auch auf ‚Fehlerhaft‘ setzen und in die Anmerkung den Grund eintragen.

Drucken von geprüften und Ändern von fehlerhaften Rechnungen

Um den nachträglichen Druck der geprüften Rechnungen und die Änderung der fehlerhaften zu erleichtern, können Sie in der in der Liste der zu prüfenden Rechnungen umschalten.

Bausteine mit Email-Betreffzeile

Bei der Verwendung von Bausteinen im Emailbereich war es störend, das es keine Vorgaben für die Betreffzeile gab. Nun kann diese in den Bausteinen hinterlegt werden und genau so mit Schlüsselworten versehen werden, wie der Emailtext selber.

Aufmassmaske überarbeitet

Diese Maske wurde grundlegend überarbeitet, wobei es in erster Linie um aufräumen und Übersichtlichkeit ging. Die Einstellmöglichkeiten waren vorher wild über die Maske verteilt und der Blick musste bei der Erfassung in der Maske immer hin und her gehen. Jetzt die wichtigsten Daten zusammen und in der Erfassreihenfolge besser angeordnet. Den Sinn von einigen nicht sofort verständlichen Optionen können Sie nun in Hilfetexten nachlesen. Neu ist nur die einfache Einfügemöglichkeit, wenn Sie die Maske auf die Anzeige der Erfassreihenfolge schalten.

[Bild]

Suchfeld ins Startcenter eingebaut (V5)

Im Startcenter wurde nun auch eine Filterzeile geschaffen, um ein Modul ggf. schneller zu finden und zu starten. Die Funktion ist sicherlich nicht sehr wichtig, aber vielleicht hilft es ja, die Suche zu beschleunigen.

[Bild]

In dem Bild wurde nur das k in das Suchfeld eingegeben und sofort auf jene Befehle eingegrenzt, die ein k enthalten.

Projektschnellsuche in Projekt-Maske eingebaut

Um schneller auf ein anderes Projekt umzuschalten kann man in der Projektverwaltung nun oben rechts einfach etwas aus dem Projektnamen, der Nummer oder dem Ort eintippen.

[Bild]

Optimal ist es allerdings nach wie vor, wenn Sie die Favoritenliste nutzen.

Weitere Telefonnummer umgestaltet (ohne Karteireiter) (V5)

Damit mögliche Zusatzfelder / Selektionsmerkmale der Ansprechpartner besser wahrgenommen werden, wurde die Maske umgestaltet. Neu hinzugekommen ist das Feld Funktion, in dem man den Arbeitsbereich der Person hinterlegen kann.

Aufgaben mit Kundenemail, neuer Knopf (V5)

Neben dem schon länger vorhandenen Knopf SMS können Sie nun aus einer Aufgabe heraus auch eine E-Mail an den Kunden schicken. In der Email-Vorlage können Sie Schlüsselworte verwenden, um Daten aus der Aufgabe selbst, aus den Adressen und aus dem Projekt automatisch einzutragen.

Kundendienst, Mehrfachdruck von Aufträgen möglich (V5)

Wenn Sie in der Kundendienst-Hauptmaske mehrere Aufträge markieren, können diese auf einen Rutsch gedruckt werden. Dann sind natürlich die Formulare, die Anzahl usw. für alle Aufträge identisch.

Ladenkasse

Hier haben sehr umfangreiche Änderungen stattgefunden, die für unsere österreichischen Anwender erforderlich waren, aber nach den Änderungen der Ladenkassenverordnung zum 1. Januar 2017 zum großen Teil auch in Deutschland erforderlich sind.

Die ausführliche Beschreibung der Änderungen lesen Sie im Handbuchbereich der Ladenkasse.
