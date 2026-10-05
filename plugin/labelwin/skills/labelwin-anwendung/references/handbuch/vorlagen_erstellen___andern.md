# Vorlagen erstellen / ändern

Pfad: Projektverwaltung > Checklisten [Modul] > 1. Vorlagen anlegen, duplizieren, Import / Export > Vorlagen erstellen / ändern
Quelle: handbuch/vorlagen_erstellen___andern.htm

|

Vorlagen erstellen / ändern

Bei einem Eintrag in einer Vorlage muss zunächst ein Zeilentyp festgelegt werden. Den Zeilentyp könnte man auch als Eintragsart bezeichnen.

Es gibt 4 Arten:

· Standard besteht nur aus der Beschreibung einer Tätigkeit

· Mit Texteingabe wie Standard, zusätzliche Zeile, in die bei der Erledigtsetzung eine Anmerkung eingetragen werden kann werden kann

· Überschriftzeile reine Beschreibungszeile, ohne Funktion, sie wird nur als Trenner verwendet

Je nach Wahl der Zeilenart werden weitere Eingabefelder ein und ausgeblendet.

Im Wesentlichen gibt es die Bereiche:

· Tätigkeit , diese kann durch eine Texteingabe oder Auswahlliste erweitert werden

· Termin , kann auf festes Datum, in Abhängigkeit vom Projektbeginn oder in Abhängigkeit einer anderen Zeile festgelegt werden

· Dauer , kann als festes Datum oder in Tagen festgelegt werden

Als letztes Feld ist das Feld Bemerkung zu nennen. Es ist in allen Situationen sichtbar und dient dazu, Anmerkungen zur Tätigkeit oder dessen Erledigtsetzung einzutragen. Man kann dieses Feld auch als Protokoll zur jeweiligen Tätigkeit verwenden.

[Bild]

|

Neu seid V4.72 (2016):

Um die Checklisten für die grafische Projektplanung effektiver einsetzen zu können, wurden 2 neue Merkmale eingeführt.

Mindestabstand:

Dabei geht es um die Situation, das Einträge zeitlich verkettet sind. Wenn ein Arbeitsschritt z.B. 10 Tage nach Abschluss eines anderen Schrittes erfolgen soll, was soll dann passieren, wenn einer verschoben werden soll? Bleiben dann alle nachfolgenden Termin im gleichen Abstand, werden also mit verschoben? Bisher war dies so und nun kann man über die Eingabe eines Mindestabstandes festlegen, dass die Verschiebung der Folgetermine nur stattfindet, wenn der Mindestabstand unterschritten wird. Ein Mindestabstand von 0 Tagen wird übrigens so behandelt, wie der frühere Zustand, ein Termin wird also aufgrund seines Abstandes mit verschoben.

Ankreuzfeld ‚Fixtermin‘.

Damit kann man nur mit einem konkreten Datum versehene Zeilen kennzeichnen. Eine Verschiebung im Kalender ist dann nicht mehr möglich, weil dieser Termin meist mit jemand anderem (z.B. dem Kunden) fest vereinbart ist.

Ein konkretes Beispiel: Im Laufe der Projektbearbeitung wird ein Termin fest vereinbart. Diese ist z.B. der Baubeginn. Der Baubeginn ist abhängig von der Bestellung der Ware . Die Ware soll 10 Tage vor Baubeginn bestellt werden, der Mindestabstand beträgt 7 Tage. Nun wird die Bestellung um 14 Tage verschoben, weil ein Mitarbeiter erkrankt ist.

Somit würde sich zur Zeit entweder der Baubeginn verschieben, dieser ist jedoch mit dem Kunden fest vereinbart, oder die Bestellung würde 7 Tage nach Baubeginn erfolgen - dann ist kein Material auf der Baustelle vorhanden.

Beide Möglichkeiten sind also keine Lösung. Um nun eine solche Situation vermeiden zu können, gibt es in der Checkliste das Ankreuzfeld ‚Fixtermin‘. Ein solcher Termin wird nicht mehr über die Verkettung mit anderen Terminen verschoben. Wenn der Mindestabstand unterschritten wird, erfolgt eine Warnung. Die anderen Termine werden trotzdem verschoben und es muss manuell nachgearbeitet werden.

1 Vorlage: Hier wird der Name und der Verwendungsbereich der aktiven Vorlage angezeigt. Beides kann in der vorigen Maske geändert werden.

[Bild]

2 Zeilentyp: Durch diese Auswahl wird festegelegt, ob eine Tätigkeit mit einer zusätzlichen Textzeile oder einer Auswahlliste versehen werden soll. Bei der Wahl als Überschrift wird gewissermaßen eine Kapitelüberschrift gewählt. Diese Überschrift hat für die eigentliche Checkliste keine Bedeutung und dient nur der optischen Trennung.

3 Reihenfolge: Die einzelnen Zeilen der Checkliste werden automatisch durchnummeriert. Wenn Sie in dem Reihenfolgefeld eine Änderung vornehmen, so wird nach dem Speichern der Zeile, diese Zeile an die entsprechende Stelle gerückt. Das Eingabefeld dient also lediglich dazu, Tätigkeiten in der Reihenfolge zu verschieben.

4 Referenz-Kennzeichen: Das bis zu 5-stellige Referenz-Kennzeichen jedes Eintrags dient zu 2 Zwecken:

1) Damit kann festgelegt werden, den Termin einer Tätigkeit auf der Basis einer anderen, vorigen Tätigkeit festzulegen.

2) Es dient es dazu,. dass eine bestimmte Eintragung / Tätigkeit in einem Formular ausgedruckt werden kann. Das Drucken der kompletten Checkliste geht auch ohne Kennzeichen.

Wenn Sie das Feld leer lassen, fügt das Programm automatisch ein Kennzeichen mit dem Text k1, k2 usw. ein. Damit kann man später einfach auf diesen Eintrag Bezug nehmen, auch wenn man zuvor nicht daran gedacht hat.

Kennzeichen können im Nachhinein einfach geändert werden, wobei der Eintrag in Zeilen, die einen Bezug darauf haben, automatisch geändert werden.

5 Tätigkeit: In diesem Feld geben Sie eine Kurzbeschreibung der auszuführenden Tätigkeit ein. Wenn der Platz nicht ausreicht, so können Sie weitere Anweisungen in das Bemerkungsfeld eintragen.

6 Tätigkeit mit Eingabezeile:

Diese zusätzliche Eingabezeile kann dazu verwendet werden, bei der Erledigtsetzung bestimmte Kommentare oder Hinweise einzugeben.

[Bild]

7 Terminart: Wenn Sie eine Tätigkeit mit einem Feld Termin versehen wollen, so bestehen mehrere Möglichkeiten. Bei der Option ‚festes Datum’ wird in der späteren Anwendung die Eingabe eines Datums ermöglicht.

Bei der Terminart Projektbeginn (hier abgebildet) erscheint keine Datumseingabe, sondern stattdessen können Tage definiert werden, mit denen ab dem Projektbeginn der Termin ermittelt werden kann. Bitte beachten Sie, dass an dieser Stelle auch negative Zahlen möglich sind. Der Projektbeginn wird im Projektdatenblatt festgelegt. Sollte er bei der Anlage einer Checkliste noch nicht eingetragen sein, so erfolgt die Rechnung bei der späteren Eingabe dennoch automatisch.

Bei einer Eingabe der Tagesanzahl kann in der folgenden Auswahlliste festgelegt werden, ob das Datum aufgrund von Arbeitstagen, Werktagen (Montag bis Samstag) oder Kalendertage ermittelt werden soll

Beginn Referenz-Zeile:

In diesem Fall können Sie auf eine vorherige Tätigkeit verweisen. Der Beginn der Tätigkeit wird dann aufgrund der Tagesanzahl nach dem Beginn der Referenz-Zeile ermittelt.

Ende Referenz-Zeile:

Das vorher gesagte gilt entsprechend für das Ende-Datum der Referenz-Zeile und das Erledigt-Datum der Referenz-Zeile. Beim Erledigt-Datum kann das Datum einer der aktiven Zeile nur dann ermittelt werden, wenn die Referenz-Zeile bereits auf erledigt gesetzt worden ist.

[Bild]

8 Dauer: Hier gibt es die Möglichkeit Tätigkeiten ohne Dauer festzulegen, ein festes Ende-Datum der Tätigkeit oder das Ende der Tätigkeit über die Eingabe von Tagen festzulegen. Bei einer Eingabe der Tagesanzahl kann in der folgenden Auswahlliste festgelegt werden, ob das Datum aufgrund von Arbeitstagen, Werktagen (Montag bis Samstag) oder Kalendertage ermittelt werden soll.

9 Bemerkung: In diesem Feld können unbegrenzt viele Informationen ´zu der Tätigkeit abgelegt werden. Man kann es sowohl für eine erweiterte Tätigkeitsbeschreibung verwenden, als auch als Logbuch. Über den Knopf Datum/Zeit kann das eigene Kürzel mit dem Datum automatisiert eingefügt werden.

[Bild]

10 Qualifikation: Wenn Sie für die Verwaltungsmitarbeiter Qualifikationen erfasst haben, können Sie hier eine für die jeweilige Tätigkeit festlegen. In der Anwendung der Vorlage können dann die verantwortlichen Mitarbeiter für die Tätigkeiten aufgrund der Qualifikationen festgelegt werden.

Die Erfassung der Qualifikationen erfolgt im Modul Einstellungen unter den Menüpunkten <Programmbereiche>, <Personal>, <Qualifikationen erfassen> .

Wichtig ist der Haken bei Verwaltungsqualifikation. Nur diese werden bei den Checklisten angeboten.

11 im Kalender anzeigen: Wenn Sie hier ein Kreuz setzen, wird der Termin der Tätigkeit in der Kalenderanzeige sichtbar.

Menüpunkte:

|

Datei

Drucken

Über diesen Punkt können Sie die Daten der gerade aktivern Vorlage zu Papier bringen.

Beenden

Hiermit schließen Sie die Maske genauso, als wenn Sie den Ende Knopf betätigen würden.

|

Zeile

Hier sind die gleichen Funktionen verfügbar, wie über die Knöpfe
