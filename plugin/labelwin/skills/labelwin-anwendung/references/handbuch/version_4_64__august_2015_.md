# Version 4.64 (August 2015)

Pfad: Updatetexte (bisher) > Update 2015 > Version 4.64 (August 2015)
Quelle: handbuch/version_4_64__august_2015_.htm

|

Version 4.64 (August 2015)

Versionswechsel auf 4.64 - Änderungen August 2015

PDF Druckausgabe mit übergeblendeter Folie (KOPIE, Firmenkopf usw.)

Wer seine Rechnungen und Angebote auf Firmenpapier ausdruckt, hat in der Archiv-Pdf keinen Firmenkopf. Die Datei ist also nur dazu geeignet, sie auf Firmenpapier nachzudrucken und ungeeignet, um sie als Email-Anhang zu verschicken.

Nach entsprechender Einrichtung ist es nun möglich, eine andere Pdf wie eine Folie über unsere archivierte Pdf zu legen. Diese Folie kann eine Pdf mit Briefpapier oder auch eine mit dem Wort ‚Kopie‘ sein. An allen Stellen, wo auf der Folie nichts gedruckt ist, sind die Informationen unserer Archiv-Pdf zu sehen.

Das gleiche ist bei der allgemeinen Druckausgabe an den Edoc-Drucker. Nach der erfolgten Druckausgabe kann nun eine Folie darüber gelegt werden, bevor die Pdf-Datei gespeichert oder per Email-Anhang versandt wird.

[Bild]

Anwendung 1 (nur in V5-Version):

An allen Stellen mit dem Knopf ‚Archiv‘ können Sie diesen mit der rechten Maustaste anklicken. Wenn mehrere Folien existieren, wird eine Auswahl angeboten. Wählen Sie die gewünschte Folie, die dann über die archivierte Pdf gelegt wird. Die zusammenkopierte Pdf wird dann mit dem ‚normalen‘ Anzeigeprogramm gezeigt. Diese neue Pdf kann als Emailanhang genommen oder gedruckt werden. Die archivierte Pdf bleibt dabei unverändert.

Anwendung 2 (alle Versionen)

In der Maske der Pdf-Verarbeitung kann eine Folie ausgewählt werden, die vor der weiteren Verarbeitung auf das Dokument gelegt wird.

Hinweis zum Ankreuzfeld unten

Das Ankreuzfeld ‚Kd-Scan anhängen‘ erscheint immer dann, wenn es sich um eine Kundendienstrechnung handelt und der Arbeitsbericht mit unserem Modul ‚Scan-Archiv‘ hinterlegt wurde. Bei gesetztem Kreuz wird der Arbeitsbericht an die aktive Pdf angehängt.

Einrichtung:

- Das Programm pdftk.exe muss installiert sein. Informationen dazu im Einstellmodul unter <Programmbereiche>, <Archiveinstellungen>, <Scan-Archiv>. In dieser Maske wird unten rechts der Pfad der pdftk eingetragen. Mit dem

Fragezeichen-Knopf gelangen Sie in einen Hilfetext, in dem Sie zusätzlich ins LabelWiki-System gelangen.

- Die Folie(n) werden hergestellt, indem Sie mit Word die Datei erstellen und als Pdf ausdrucken. Diese Folie muss mit einem verständlichen Namen im Verzeichnis \labelwin\vorlage\layer abgelegt werden. Um Ihnen ein Beispiel zu geben, liefern wir eine Folie mit dem Wort ‚Kopie‘ aus.

Eintragen der Angebots- Rechnungsnummer in Vor- und Nachbemerkungen

Bisher konnte mit dem Schlüsselwort der Angebots- oder der Rechnungsnummer diese Nummer nicht in eine Vor- oder Nachbemerkung gesetzt werden. Dies hing damit zusammen, dass wir die Nummer erst im letzten Moment unmittelbar vor der Druckausgabe gezogen haben. Zu diesem Zeitpunkt war die Druckdatei aber schon komplett fertiggestellt. Nun ist es möglich, die Nummer auch in die Vor- oder Nachbemerkung einzutragen. Dazu wird das Schlüsselwort @TXTEXTARTNR@ verwendet.

Set erstellen, aufgerufene Artikel mit Preisanzeige und Minuten

Bei der Erstellung von Sets ist es seit vielen Jahren möglich, die Minuten des aufgerufenen Bestandteils zu sehen und ggf. auch ‚nebenher‘ zu erfassen. Um besser prüfen zu können, ob der richtige Artikel aufgerufen wurde, wird nun auch der Listen- und Einkaufspreis gezeigt. Änderbar sind die Preise an dieser Stelle aber nicht, da die Pflege ja in der Regel über den Lieferanten erfolgt.

Fibuerfassung, Knopf ‚Aufgabe‘ bei Erfassen eines Zahlungseingangs

Seit etwa einem Jahr kann man im Rechnungsausgangsbuch zu einer Rechnung eine Aufgabe anlegen. Hintergrund der Entwicklung war, das z.B. bei der Buchhaltung die Info angekommen war, dass im Büro noch irgend etwas gemacht werden soll oder das z.B. der Chef informiert werden möchte, wenn die Rechnung bezahlt wurde. Diese Aufgabe kann nun auch in der Fibuerfassung bearbeitet werden. Es ist aber auch möglich, dort eine neue Aufgabe zu erfassen, um z.B. jemanden über etwas zu informieren (Kunde hat unberechtigt Skonto gezogen usw.)

[Bild]

Wartungsmaterial zu Anlagen mit zuordneten Geräten hinterlegen

Es ist leider ein sehr komplexes Thema, betrifft aber nur Firmen, die den Anlagen noch Geräte hinterlegt haben. Dies findet statt, damit einzelnen Bauteilen (den Geräten) eine eigene Karteikarte hinterlegt werden kann.

Wer dann Material für den Wartungstermin hinterlegt, musste dies bisher komplett bei der Anlage hinterlegen. Nun ist es möglich, die jeweiligen Artikel zum Termin der Anlage dennoch bei Geräten zu hinterlegen. Entwickelt wurde diese Funktion, um auch bei der Bestellung eine Information zu haben, für welches Gerät das Material benötigt wird. Sie hat den Vorteil, dass bei neu hinzukommenden Geräten oder entfallenden Geräten nur dort das

Material geändert werden muss, wo es zu gehört.

[Bild]

Die Tabelle zeigt ein Beispiel. Zum Termin am 06.2015 und der Anlage selbst gehören 2 Artikel. Zum Termin am 06.2015 und dem Gerät ‚Kessel 1‘ gehört ein Artikel und zum Gerät ‚Kessel 2‘ gehören 3 Artikel.

Zur Wartung am 06.2015 sind also 6 Artikel zu bestellen und mitzunehmen.

Zusätzlich gibt es einen für 01.2016 einen Termin mit nur dem Gerät Kessel 2. Dazu sind 4 Artikel hinterlegt.

Die Erfassung läuft so ab, dass beim Anlagentermin und der Materialerfassung über eine Auswahl zwischen der Anlage und den Geräten umgeschaltet werden kann. Zusätzlich kann das Anlagen-Termin-Material auch über die Geräte erfasst werden. In der Maske der Termine sind die Anlagentermine und eventuelle Gerätetermine sichtbar. Über die Markierung des Termins entscheiden Sie, ob beim Gerätetermin oder beim Anlagentermin Material hinterlegt wird.

Rechnungsprüfung mit Anzeige des Buchungshinweises

Da dort möglicherweise bereits bei der Erfassung der Eingangsrechnung wichtige Hinweise eingetragen werden, zeigen wir diesen Text auch bei der Prüfung der Rechnung an.

Ladenkasse, diverse Änderungen

-

Bereits aufgerufene Artikel mit anderer Kalkulationseinstellung kalkulieren Üblicherweise arbeitet man in der Ladenkasse mit der Adresse ‚Barverkauf‘ und der dort hinterlegten Kalkulationseinstellung. Wenn im Nachhinein eine Adresse gewählt wird, sind die ersten Artikel möglicherweise falsch kalkuliert, weil der Kunde spezielle Bedingungen hat. Über den Menüpunkt <Optionen> können nun die Artikel auf einen Rutsch mit der neuen Einstellung kalkuliert werden.

-

Für das Zählen des Kassenbestands gibt es nun ein Druckformular für die Ausgabe in Word. Eventuelle Anpassungen können in der Datei \labelwin\vorlage\ladenkas\kassenbestand.rtf vorgenommen werden.

Heizungslabel

Ab dem 26. September 2015 ist Vorschrift, dass bei einem Angebot über Heizungsanlagen eine Info über die Energieklasse der Anlage mit geliefert werden muss. An dieser Stelle wollen wir nicht alles wiederholen, was Ihnen sicherlich schon bekannt ist.

Das Label kann über die Seite Heizungslabel.de oder ggf. auch über eine Seite Ihres Lieferanten erfolgen. Wenn es über den Lieferanten geht, wird er Sie sicherlich schon informiert haben oder dies noch tun.

Einrichtung:

- Adresse Heizungslabel anlegen und speichern.

- Dann auf die Menüpunkte <Bearbeiten>, <Stammdaten UGL / Online> gehen (oder Strg O) und dort die Zugangsdaten eintragen.

- Die URL-Adresse von Heizungslabel.de können Sie über den Vorgabeknopf eintragen.

[Bild]

- Bei den Heizungslabeln über Lieferanten müssen Sie deren Zugangsdaten und ggf. auch einen Benutzernamen und Passwort eintragen. Dies können Sie nur vom Lieferanten erfahren

Hochgereichte Artikel kennzeichnen:

Wichtig: Sie können auch über unser Programm so in die Webseite einsteigen, dass Sie die Artikel dort zusammensuchen.

Das größte Problem bei der Nutzung ist, das die Webseite die von uns reingereichten Artikel findet.

1) Die Erkennung läuft im optimalen Fall über die EAN-Nummer (heißt heute GTIN, ist aber das Gleiche). Wenn Sie sich die Mühe machen, diese in den Stammdaten einzutragen, klappt alles. Es gibt bereits Großhändler, die diese in der Datanorm mit ausliefern.

2) Die Erkennung über die Artikelnummer funktioniert auch, wenn es sich um die Herstellernummer handelt und das Kennzeichen des Herstellers reingereicht wird. Dieses können Sie für den ganzen Katalog vergeben oder beim einzelnen Artikel.

Einzelner Artikel: Stammdaten, Feld Hersteller-Kürzel.

Ganzer Katalog: Katalogmodul, Menüpunkt <Katalog>, <Katalog-Grunddaten>, Feld Herstellerkürzel.

Welche Herstellerkürzel gibt es ?

Gehen Sie auf die Seite Heizungslabel.de und wählen die Lieferantensuche. Die dort hinterlegte LieferantenID ist unser Herstellekürzel.

[Bild]

3) Bei den Shops der Großhändler ist zu erwarten, das die Ihnen die Herstellerkennzeichen passend raussuchen und das es genügt, mit der Artikelnummer des Großhändlers da ran zu gehen. Das müssen Sie mit ihm klären.

Anwendung

Erstellen Sie Ihr Angebot wie gewohnt.

Um das Label zu erzeugen gibt es nun mehrere Wege:

- SHIFT-F8 drücken oder Menüpunkt <Datei>, <Heizungslabel>

- F8 oder <Datei>, <Online Shop> und einen Heizungslabel Lieferanten auswählen) und Artikel hochladen

In allen Fällen kommt die Frage, welche Artikel zur Berechnung des Labels hochgeladen werden sollen. Für die einfachere Bedienung der Webseite ist es sinnvoll, möglichst nur die Artikel zu nehmen, die für die Berechnung relevant sind. Diese können über eine Mehrfachmarkierung festgelegt werden oder auch über ein Kennzeichen am Artikel. Dieses Kennzeichen kann bereits mit der Datanorm mitgeliefert werden, wird es aber in Regel im

Moment noch nicht. In Labelwin können Sie das in den Stammdaten setzen oder für den gerade aufgerufenen Artikel in der Aufrufmaske (Bereich, indem man auch ‚Alternativ‘ usw. setzen kann)

Dann startet die hinterlegte Webseite Heizungslabel oder Ihres Lieferanten. Dort sind im optimalen Fall die reingereichten Artikel schon gefunden worden, was bei der derzeitigen Datenlage eher selten vorkommt. Sie können auf der Webseite die Artikel suchen oder ggf. auch die Daten des von Ihnen gewählten Objektes eintragen. Auf die Handhabung der Webseite haben wir keinen Einfluss. Zum Erlernen der Bedienung wenden Sie sich bitte an

Ihre Verbände oder Lieferanten.

Geben Sie auf der Webseite Ihren Firmennamen ein, damit dieser auf dem Label gedruckt wird. Obwohl 35 Zeichen möglich sind, sollten Sie nur 25 nutzen. Ansonsten wird es auf dem Label nicht ordentlich dargestellt (können wir nicht ändern)

Wenn das Label vom Shop erzeugt worden ist, wird es bei Labelwin in dem Projekt als Pdf abgelegt, in dem auch das aktive Angebot liegt. Dort können die Dateien gedruckt werden. Wenn Sie das Angebot ebenfalls als Pdf drucken und per Email versenden wollen, können Sie die Pdf als weitere Dokumente anhängen.

Umgang mit Alternativen:

Da Sie dann ggf. mehrere Labels mit ausliefern müssen und dies recht unübersichtlich wird, empfehlen wir, in diesem Fall 2 Angebote zu erstellen. Ansonsten müssen Sie irgendwie kennzeichnen, welches Label zu welchen Artikeln gehört.

|

Anmerkung Gerald Bax:

Aktuell (17.9.2015) würde ich die Einführung des Labels als misslungen ansehen. Die Webseite verhält sich an manchen Stellen falsch und ggf. fehlen immer noch manche Artikel. Daran wird zwar gearbeitet, aber ob es rechtzeitig geschafft wird, bezweifle ich. Leider haben wir auf die Berechnung und das Verhalten der Webseite keinen Einfluss.
