# Korrektur von Ausgangsrechnungen / GoBD

Pfad: Buchhaltung > Korrektur von Ausgangsrechnungen / GoBD
Quelle: handbuch/korrektur_von_ausgangsrechnungen___gobd.htm

|

Korrektur von Ausgangsrechnungen / GoBD

Stand: 28.08.2018

(V5.86)

Die Umsetzung der "Grundsätze zur ordnungsmäßigen Führung und Aufbewahrung von Büchern, Aufzeichnungen und Unterlagen in elektronischer Form sowie zum Datenzugriff" (kurz GoBD) hat zu einigen Änderungen im Programm geführt (Anfang 2017). Der GoBD entsprechend darf eine im Rechnungsausgangsbuch eingetragene Rechnung nicht mehr gelöscht oder geändert werden. Vom Finanzamt wird diese Vorschrift so ausgelegt, dass selbst die Möglichkeit mit der Buchhaltungssoftware eine Rechnung zu löschen nicht zulässig ist. Labelwin ist deshalb so eingerichtet, dass es nicht möglich ist eine im Rechnungsausgangsbuch eingetragene Rechnung zu ändern, zu überschreiben oder zu löschen. Dieser Umstand betrifft die Arbeitsabläufe für Probedrucke, das Gutschreiben, das ungültig Erklären, das Stornieren und die digitale Prüfung von Ausgangsrechnungen.

Die erforderlichen Sperren:

-

Eine Rechnung mit Nummer und Eintragung im Rechnungsausgangsbuch kann nicht mehr gelöscht oder geändert werden.

-

Bei einem Nachdruck muss immer das Wort "Kopie" drauf stehen.

Die eingeführten Neuerungen:

-

Der Probedruck

-

Das "ungültig erklären" einer Rechnung

-

Eine Funktion zum Stornieren, Gutschreiben und Ungültig erklären

Durch die GoBD sind Fehler in Ausgangsrechnungen noch kostspieliger geworden. Um Fehler in der Rechnung schon vor der Rechnungsnummernvergabe festzustellen, bieten sich folgende Verfahren an:

1. Die digitalen Prüfung (nur in V5) stellt den Rechnungsinhalt übersichtlich dar und bietet die Möglichkeit Veränderungen in der Maske vorzunehmen.

2. Die Probedruckfunktion erzeugt einen Ausdruck der Rechnung ohne, dass eine Rechnungsnummer vergeben wird, das Original bleibt also veränderbar.

TUTORIAL VIDEO

Die Hintergründe zur GoBD und die sich daraus ergebenen Veränderungen in Labelwin werden in dem folgenden Tutorial Video vorgestellt.

https://www.youtube.com/watch?v=giPZaeabVkQ

Probedruck / Bildschirmdruck

|

Um Fehler beim Rechnungsdruck zu vermeiden, empfiehlt es sich grundsätzlich vor dem echten Druck einen Bildschirmdruck oder Probedruck vorzunehmen. Bei diesen beiden Varianten wird noch keine Rechnungsnummer vergeben und somit kann das Dokument weiterhin bearbeitet werden.

Beim Probedruck handelt es sich sinngemäß um einen Bildschirmdruck, aber eben auf den vorgesehenen Drucker und mit Rechnungsnummer 0 und vor dem Text ‚Rechnung‘ steht ‚Entwurf‘, um die Probedrucke deutlich zu kennzeichnen.

In diesem Zusammenhang sei erwähnt, dass sich inhaltliche Fehler auch durch Einsatz der Rechnungsprüfung minimieren lassen.

|

[Bild]

Rechnung stornieren / gutschreiben / ungültig

|

Da man Fehler trotzdem nie ganz ausschließen kann, haben wir das Stornieren und Ändern der Rechnung besonders einfach gemacht. Mit Markieren des Rechnungsdokumentes und der rechten Maustaste erscheint ein Menüpunkt "Rechnung stornieren /ungültig".

Dieser Punkt erscheint in der Projektverwaltung und allen Masken mit ‚Zugeordnete Dokumente‘.

In der Projektverwaltung kann die gleiche Funktion auch über das Menü <Dokumente - Rechnungsstorno> aufgerufen werden.

Die Funktion steht außerdem im Rechnungsausgangsbuch unter <Bearbeiten> <Stornorechnung / Gutschrift / ungültig> zur Verfügung.

|

[Bild]

Zunächst erscheint die folgende Maske, in der Sie entscheiden müssen, ob die Rechnung storniert werden soll oder eine Stornorechnung (Gutschrift) erzeugt oder die Rechnung für ungültig erklärt werden soll.

[Bild: Korrektur von Ausgangsrechnungen / GoBD]

|

Hinweis: In der Rechteverwaltung kann eingestellt werden, dass einzelne Mitarbeiter Rechnungen weder stornieren, noch das Kennzeichen ‚zu stornieren‘ und auch nicht für ungültig erklären können. Ausführliches weiter hinten!

|
[Bild: 1]

Rechnung liegt vor

[Bild: 1. Rechnung liegt vor]

Die ersten beiden Optionen stehen nur zur Verfügung, wenn Sie den Haken bei "die Rechnung hat das Haus nicht verlassen oder das Original liegt vor" gesetzt haben. Dieser Haken wird protokolliert.

Hintergrund dieser Protokollierung ist, dass immer nur ein Original einer Rechnungsnummer im Umlauf sein darf.

|
[Bild: 2]

Ungültig erklären

[Bild: 2. Ungültig erklären]

Die Funktion 'Rechnung für ungültig erklären' ist im Zuge der Umsetzung der GoBD eingeführt geworden. Mit ihr können fehlerhafte Rechnungen, die das Haus noch nicht verlassen haben schnell korrigiert werden ohne, dass es dabei zu einer Lücke in der Rechnungsnummersabfolge kommt. Das Ungültigmachen erzeugt direkt eine Kopie des Originals, das ausgebessert werden kann. Das Original bleibt unveränderbar mit dem Vermerk "ungültig" bestehen. Dabei wird, anders als bei Gutschreiben und Stornieren keine neue Rechnungsnummer vergeben.

Im Rechnungsausgangsbuch bekommt die Rechnung neben dem Kommentar ‚ungültig‘ den Status ‚x‘ für stornierte Rechnungen. Beim Drucken kann die neue Rechnung dann nur mit der bisherigen Nummer NEU im Rechnungsausgangsbuch eingetragen werden. Es kann dann also eine Rechnungsnummer mehrfach in der Liste vorkommen, wobei nur die letzte gilt und Vorversionen mit ‚x‘ (steht an sich für storniert) und ‚ungültig‘ gekennzeichnet sind.

Solange eine Rechnung das Haus nicht verlassen hat oder wenn das Original vorliegt, erlauben wir es, eine Rechnung als ungültig zu kennzeichnen. Ob das erste Original vorliegt, kann die EDV natürlich nicht wirklich prüfen. Dazu gibt es das Ankreuzfeld "die Rechnung hat das Haus nicht verlassen oder das Original liegt vor", mit der der Anwender dies bestätigt. Erst dann wird die Ungültig Methode freigegeben. Es wird protokolliert, wer wann welche Rechnung als ungültig erklärt hat.

Hinweis: Standardmäßig ist die Möglichkeit Rechnungen für ungültig zu erklären aktiviert. Sollten Sie sich in Ihrem Unternehmen dazu entscheiden, diese Methode zu meiden und konsequent nur Gutschriften oder Stornierungen verwenden möchten, können Sie die 'Ungültig-Methode' im Einstellmodul unter [Programmbereiche - Buchhaltung - Grundeinstellung - Ausgangsrechungen 'Optionen'] deaktivieren.

|
[Bild: 3]

Stornieren

[Bild: 3. Stornieren]

Die Rechnung wird storniert einschließlich der erforderlichen Buchungssätze. Es wird eine Kopie der Rechnung erstellt, die überarbeitet werden kann. Die Bearbeitung der neuen Rechnung erfolgt dann wie gewohnt.

Beim Druck der Kopie wird eine neue Rechnungsnummer vergeben.

|

Der Storniervorgang:

Ob die Stornierung abgeschlossen ist, hängt von den Rechten des Anwenders ab und ob im Betrieb das Modul ‚Fibuerfassung‘ eingesetzt wird.

Bei dem Recht geht es um den Bereich ‚Rechnungen‘, ‚gebuchte Rechnungen erneut ausdrucken‘. Wer dieses Recht in der Vergangenheit hatte, durfte im Rechnungsausgang eingetragene Rechnungen ändern und neu drucken / eintragen lassen. Wer dieses Recht hat, darf nun komplett stornieren, allerdings ohne deshalb ins Rechnungsausgangsbuch zu gehen.

Wichtig: Bei Nutzung der Fibuerfassung muss dort eine Verrechnungsbank eingetragen werden. Dies geschieht direkt in der Fibuerfassung unter dem Menüpunkt <Optionen>, <Einstellungen>.

Storniervorgang ohne Nutzung der Fibuerfassung

-

Rechte ‚Darf alles‘:

Die Rechnung wird storniert – im Rechnungsausgang fertig, Die Stornierung muss in der Fibu beim Steuerberater zusätzlich erfolgen.

-

Recht ‚Darf nicht stornieren (Recht fehlt)

Nur Eintragung im RA-Buch im Feld ‚Bemerkung „Zu stornieren‘ mit Name und Datum/Uhrzeit. Die Stornierung im Rechnungsausgangsbuch muss später von jemand berechtigtem vorgenommen werden. Zur Suche wird der Filter mit dem Text ‚Storno‘ eingesetzt.

Storniervorgang mit Nutzung der Fibuerfassung

-

Rechte ‚Darf alles‘:

Die Rechnung wird im Rechnungsausgang storniert und in den Datensätzen der Fibuerfasssung die Umkehrbuchungen erzeugt – damit ist wirklich alles fertig, der Steuerberater braucht nichts mehr machen.

-

Recht ‚Darf nicht stornieren (Recht fehlt)

Nur Eintragung im RA-Buch im Feld ‚Bemerkung „Zu stornieren‘ mit Name und Datum/Uhrzeit. Der Stornovorgang erfolgt in der Fibuerfassung wie bisher: Anwahl von ‚ Rechnung bezahlen‘, Summe 0, Rest ausbuchen und damit stornieren.

Hinweis: Wenn die Stornierung komplett automatisiert stattfindet, erfolgt eine Generalumkehr - die Ausbuchung erfolgt negativ auf dem Erlöskonto. Wenn jemand diese auf einem speziellen Konto haben möchte, kann er dieses bei den Erlöskonten hinterlegen. In der Regel ist aber die Generalumkehr der richtige Weg und Sie brauchen nichts zu machen.

|
[Bild: 4]

Stornorechnung (Gutschrift)

[Bild: 4. Stornorechnung (Gutschrift)]

Eine Stornorechnung oder Gutschrift muss immer dann erzeugt werden, wenn die Rechnung das Haus schon verlassen hat. Das hat also letztlich mit GoBD nichts zu tun, sondern war schon immer erforderlich. Bisher musste man aber in einem neuen Dokument die alte Rechnung als Vorlage wählen und den Mengenmulti auf -1 setzen. Mit der neuen Funktion haben wir es also viel einfacher gemacht, da automatisch eine Kopie mit negierten Mengen erzeugt wird.

Egal ob Sie eine neue Rechnung oder eine Stornorechnung anlegen wollen, erscheint die Maske zur Anlage von neuen Dokumenten, in der alle Werte der ‚alten‘ Rechnung vorbelegt sind. Ggf. können Sie hier Änderungen vornehmen.

Bei der Stornierung erscheint dann danach ein Fenster, in dem Sie den Grund der Stornierung eingeben können. Dieser Text kommt ins Rechnungsausgangsbuch als Anmerkung. Zusätzlich wird in die Bemerkung der Rechnung das Wort ‚Storno‘ vorangestellt.

Die Bearbeitung der neuen Rechnung erfolgt dann wie gewohnt.

|
[Bild: 5]

Dokumententyp der Kopie

[Bild: 5. Dokumententyp der Kopie]

Bisher wurde die Kopie der Rechnung immer mit der gleichen Art, also Abschlag zu Abschlag, Schlussrechnung zu Schlussrechnung kopiert. Das ist unglücklich, wenn der Fehler darin bestand, dass die falsche Art gewählt wurde. Nun kann in der Ungültig / Stornieren-Maske unten in einer Auswahlliste gewählt werden, von welcher Art die Kopie sein soll.

Ungültige Rechnungen werden nicht in eine Finanzbuchhaltung übertragen.

Sobald eine Rechnung übertragen worden ist, kann sie nicht mehr auf ‚ungültig‘ gesetzt werden.

Intern sind die alten ungültigen Rechnungen miteinander verkettet. Im Protokoll einer einzelnen Rechnung im Rechnungsausgangsbuch (Menüpunkt <Bearbeiten>, <Protokoll>) sieht man deshalb nicht nur die Daten der markierten Rechnung, sondern auch die der vorigen Version. Sinngemäß zeigt das Protokoll also alles, was mit der Rechnungsnummer passiert ist.

Im Dokumentenprotokoll ist sichtbar, was gegenüber der Vorversion geändert wurde. Keine der Rechnungen kann gelöscht oder verändert werden. Das erste Original sollte bei der Papierablage dazu geheftet werden (damit der Prüfer was zu prüfen hat) und steht bei Nutzung des PDF-Archivs auch dort zur Verfügung.

Sonstiges

Nur das erste Exemplar sieht so aus wie bisher, beim zweiten muss schon das Wort KOPIE drauf stehen. Dazu sind ggf. Formularänderungen erforderlich, die bei vielen Anwendern aber schon stattgefunden haben. Wer ein Formular ohne diese Möglichkeit verwendet, wird jedesmal darauf hingewiesen, dass dies nach GoBD nicht zulässig ist.

Wer bisher die Rechnungen einfach ausgedruckt hat, danach geprüft und ggf. dann geändert und neu gedruckt hat, sollte dies unserer Meinung nach mindestens bei den Kundendienstrechnungen weiter so machen, wenn die Fehlerquote klein ist. Mit dem Unterschied allerdings, dass der oben beschriebene Ungültig /Kopiervorgang ausgelöst werden müsste zur Korrektur. Je nach Fehlerquote gibt es dann halt ein paar stornierte Rechnungen. Diese sollten Sie auch in den Rechnungsordner heften und als ‚Storniert‘ kennzeichnen. Der Grund steht ja im Rechnungsausgangsbuch, das sollte bei einer Buchprüfung reichen. Damit findet ein Buchprüfer einige Stornierungen und kann seine Zeit damit verbringen, diese zu prüfen

Weitere Berechtigungen

1) Wenn eine Firma nie mit der ‚Ungültig‘-Methode arbeiten möchte, kann sie die komplett verhindern. Zu finden ist die Einstellung Im Modul Einstellungen, <Programmbereiche>, <Buchhaltung> auf der Karteiseite ‚Ausgangsrechnungen‘

2) Der Stornovorgang selbst kann über 2 Rechte abgesichert werden:

[Bild]

Das erste Recht gibt es schon länger, nur der Beschreibungstext wurde verbessert. Wer dieses Recht hat, darf alles was im Rahmen der GoBD möglich ist.

Wenn jemand dieses Recht nicht hat, greift das zweite, jetzt neu eingerichtete Recht. Der Anwender darf Rechnungen mit dem Kennzeichen ‚Zu stornieren‘ versehen und darf auch Rechnungen für ungültig erklären.

Wenn der Anwender keines der beiden Rechte hat, darf er weder stornieren noch eine Rechnung für ungültig erklären. Bei einem Fehler muss er sich also an einen Mitarbeiter wenden, der über diese Rechte verfügt.

Rechnungsnachdruck

Die Adresse der Rechnung steht nun in der Rechnung selbst. Bei einem Nachdruck wird darauf zugegriffen und nicht auf eine ggf. geänderte Adresse in den Stammdaten.

Das gleiche gilt für die Zahlungsbedingungen.

bei Verwendung des PDF- Druckarchives

Wenn das PDF-Druckarchiv verwendet wird, besteht zusätzlich zum Nachdruck die Möglichkeit auf den Archiv Eintrag zurückzugreifen.

[Bild]

In der Regel sollte die Archiv PDF für den Nachdruck genutzt werden, da man dann in jedem Fall eine genaue Kopie erhält.

Beim Nachdruck hingegen könnte ein anderes Druckformular gewählt werden. Dadurch entsteht eine Kopie, die jedoch völlig anders aussieht, als das Original.
