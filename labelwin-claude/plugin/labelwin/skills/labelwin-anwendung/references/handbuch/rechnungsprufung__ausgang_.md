# Rechnungsprüfung (Ausgang)

Pfad: Buchhaltung > Rechnungsprüfung (Ausgang)
Quelle: handbuch/rechnungsprufung__ausgang_.htm

|

Rechnungsprüfung (Ausgang)

Stand: 03.02.2019

(V5.88)

THEMA

|

Mit Einführung der GoBD-Regeln ist die einfache Möglichkeit entfallen, eine Rechnung erst nach dem Ausdruck zu prüfen und dann ggf. wieder zu ändern. Wir haben daher eine Möglichkeit geschaffen, die eine wesentlich bessere Prüfung als die Betrachtung des Papierausdrucks erlaubt. Es gibt eine Kontrolle der gebuchten Zeiten, die Ansicht des Arbeitsberichts, der Deckungsbeiträge usw. Die Rechnung kann auch aus dieser Maske heraus in Bearbeitung genommen oder direkt gedruckt werden.

VORAUSSETZUNGEN

|

-

Die Rechnungsprüfung für Ausgangsrechnungen muss in den EINSTELLUNGEN aktiviert sein.

EINRICHTUNG

|

Zunächst ist im Modul EINSTELLUNGEN unter [Programmbereiche - Buchhaltung -Grundeinstellung] unter "Ausgangsrechnungen" die Option "Prüfen von Ausgangsrechnungen aktiv" zu setzen.

Prüferfestlegung

Wie beim Prüfen der Eingangsrechnungen können auch für Ausgangsrechnungen bis zu 2 Prüfer je Rechnung festgelegt werden. Nur die berechtigten Prüfer bekommen die Rechnungen im Arbeitsalltag als 'zu prüfen' angezeigt.

Wenn die Rechnungsprüfung aktiviert ist, ist bei 'Erfass-Vorgabe' zu entscheiden wer der 1. Prüfer sein soll:

-

Auswählen: Der Rechnungsersteller, der die Rechung zur Prüfung freigibt, wird aufgefordert einen Mitarbeiter auszuwählen.

-

Projektverantwortlicher: Es wird als Vorgabe jeweils der Projektverantwortliche vorgeschlagen. Der Rechnungsersteller, der die Rechung zur Prüfung freigibt, kann aber dennoch einen anderen Mitarbeiter wählen.

-

'Nutzer-Name': Der ausgewählte Nutzer ist als 1. Prüfer festgelegt.

|

[Bild]

|

Auch in dem Feld '2. Prüfer (Vorgabe)' gibt es mehrere Möglichkeiten:

-

Auswählen: Der Rechnungsersteller, der die Rechung zur Prüfung freigibt, wird aufgefordert einen Mitarbeiter auszuwählen.

-

Kein 2. Prüfer: Wählen Sie diese Option wenn eine Prüfung ausreicht. Gegebenenfalls kann der Rechnungsersteller, der die Rechung zur Prüfung freigibt, dann einen Mitarbeiter als 2. Prüfer bestimmen.

-

'Nutzer-Name': Der ausgewählte Nutzer ist als 2. Prüfer festgelegt.

Mit einem Haken bei 'Priorität' kann entschieden werden, dass der zweite Prüfer die Rechnung erst dann in seiner Liste sieht, wenn der erste Prüfer sie freigegeben hat. Der zweite Prüfer ist also dann erst nachrangig involviert. Wenn dieser Haken nicht gesetzt ist, müssen dennoch beide Prüfer die Rechnung freigeben.

'2. Prüfer fest, nicht änderbar' legt fest, dass der 2. Prüfer nicht von dem Rechnungsersteller bestimmt werden kann, sondern der im entsprechenden Feld ausgewählte Nutzer ist. Das ist sinnvoll, wenn immer die gleiche Person die zweite Freigabe vornehmen soll.

|

[Bild]

|

Der "Super-Prüfer"

In der Rechteverwaltung kann ein Prüfer mit diesem Sonderrecht (5-10) versehen werden. Das gibt allerdings nur Sinn, wenn Sie mit 2 Prüfern arbeiten. Der Super-Prüfer hat dann das Recht, auch alleine zu prüfen, kann also eine Rechnung ausdrucken, ohne dass eine 2. Person prüfen muss.

|

Auswertungscenter

Im Auswertungscenter kann die Anzahl der zu prüfenden Ausgangsrechnungen gezeigt werden. Dazu wurde eine eigene Standardauswertung gebaut: Aktiviert werden kann sie wie alle anderen Auswertungen im Modul EINSTELLUNGEN unter der Rechtevergabe.

[Bild]

|

[Bild]

ABLAUF

Wenn die Rechnungsprüfung aktiviert wird, werden im Hintergrund drei neue Status für Rechnungen eingeführt. Es sind die Status

-

zu prüfen

-

geprüft

-

fehlerhaft.

|

Nach der Erstellung einer Rechnung kommt eine Maske in der – je nach Voreinstellung – der oder die Prüfer gewählt werden können. Wenn die Maske mit Abbruch verlassen wird, ist die Rechnung noch nicht zur Prüfung zugelassen.

Nur geprüfte Rechnungen können gedruckt werden. Deshalb erfolgt auch beim Drucken der Rechnung aus der Positionserfassung heraus die Frage, ob das Dokument auf geprüft gesetzt werden soll. Das dürfen aber nur die Anwender, die das Recht dazu haben.

Standardmäßig ist dieses Recht gesetzt, weil die Anwender ja zuvor Rechnungen auch einfach ausdrucken konnten. Wenn man jemandem dieses Recht nimmt, kann derjenige die Rechnungen nicht mehr mit Nummer ausdrucken.

|

[Bild]

Die Mitarbeiter, die zur Rechnungsprüfung vorgesehen sind, müssen regelmäßig auf zu prüfende Rechnungen kontrollieren. Das geschieht entweder indem man die Prüfmaske öffnet oder sich wie oben beschrieben eine Auswertung in sein Auswertungscenter einrichtet.

Liegen zu prüfende Rechnungen vor, muss natürlich die Prüfung erfolgen. Gibt es keinerlei Beanstandungen kann die Rechnung entweder als geprüft markiert oder auch direkt gedruckt werden. Sollte die Rechnung nicht richtig zugeordnet worden sein, kann der Prüfer auch umgesetzt werden. Im negativen Prüfungsfall wird die Rechnung auf fehlerhaft gesetzt und im gleichen Zuge eine Aufgabe angelegt. Wenn ein Fehler in der Rechnung vorliegt, der nicht direkt vom Prüfer korrigiert werden kann, muss eine Kollegin oder Kollegin informiert und mit einer Prüfung oder Korrektur beauftragt werden,
