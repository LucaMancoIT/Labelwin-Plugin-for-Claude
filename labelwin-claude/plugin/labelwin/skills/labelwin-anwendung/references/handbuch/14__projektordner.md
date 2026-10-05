# 14. Projektordner

Pfad: Projektverwaltung > Projektverwaltung [2] > 14. Projektordner
Quelle: handbuch/14__projektordner.htm

|

14. Projektordner

THEMA

In der Projektverwaltung arbeitet man mit Projekten. Jedes Projekt kann dabei als Ordner betrachtet werden in dem alle Dokumente zu einer Baustelle gesammelt werden. Bei diesen Dokumenten handelt es sich vorwiegend um Label-eigene Dokumente, also Angebote, Bestellungen, Rechnungen, Stücklisten etc. In einem Projekt lassen sich aber auch Label-fremde Dokumentenarten, wie Word, Excel, PDF oder Bilder ablegen. Da für jedes Dokument ein eigener Eintrag in der Dokumentenliste erfolgt, kann die Liste der Dokumente mit der Zeit sehr lang und somit auch etwas unübersichtlich werden. Außerdem sind die Dokumente nur aus Labelwin heraus erreichbar.

[Bild]

Bild: Projekt BROTFABRIK

Der Labelwin Projektordner kann die beiden geschilderten Probleme umgehen. Der Projektordner ist im Grunde ein normaler Windows Ordner, der in Labelwin eingebunden wird. Der Vorteil hierbei ist, dass man auf die Inhalte auch außerhalb von Labelwin zugreifen kann. Hinzu kommt, dass man die gewohnte Windows Dateiverwaltung nutzen kann und nicht jedes Dokument einzeln im Labelwin Projekt ablegen muss.

Ein Projektordner kann aus mehreren Unterordnern bestehen. Es lassen sich beliebig viele neue Unterordner anlegen und/oder Dateien ablegen.

[Bild]

Da man vermutlich immer eine ähnliche Ordnerstruktur in den Projektordnern verwendet, lässt sich über das Einstellmodul auch ein oder mehrere Musterordner anlegen, die bei der Anlage eines Projektordners zur Auswahl stehen.

[Bild]

Es ist sogar möglich Vorlagedateien in die Ordnerstruktur hineinzukopieren. Die Einrichtung der Musterordner wird im nächsten Abschnitt erklärt.

Hinweis: Es kann nur einen Projektordner je Projekt geben.

EINRICHTUNG

Die Einrichtung des Projektordners erfolgt im Modul EINSTELLUNGEN unter [Programmbereiche - Projektverwaltung - Grundeinstellungen] im Bereich "Diverse Einstellungen".

[Bild]

Pfad: Tragen Sie hier in Pfad für den Projekt-Standardordner ein. In diesem Ordner werden dann alle weiteren Projektordner abgelegt. Jeder Projektordner erhält als Namen die Projektnummer.

Ordner automatisch anlegen: Wenn Sie dieses Feld aktivieren, werden Sie beim Anlegen eines neues Projektes gefragt, ob ein Projektordner angelegt werden soll.

Musterordner: Es ist möglich für verschiedene Projekte ggf. unterschiedliche Ordnerstrukturen anzulegen. Dazu werden in der Mustervorlage mehrere Blöcke angelegt.

Wenn mehrere Blöcke vorhanden sind, werden diese zur Auswahl angeboten. Wenn nur ein Block vorhanden ist, erfolgt nur die Frage, ob die Ordner-Struktur angelegt werden soll.

Die Einträge in eckigen Klammern werden im Projekt zur Auswahl angeboten. z.B. [Bäder]

Mit einem vorangestellten #-Zeichen können bei Bedarf bestimmte Vorlagedateien sofort in die Ordnerstruktur kopiert werden. Hintergrund dieser Funktion ist, dass ein Kunde immer eine bestimmte Excel-Tabelle je Projekt haben wollte. Die Kopie erfolgt in den in der vorigen Zeile angelegten Ordner.

Nachfolgend Beispiele, die Sie markieren und über die Zwischenablage in die Mustervorlage kopieren können.

|

1. Einfach nur einen Ordner

[Dokumente]

2. Auswahl der Blöcke Lüftung und Klima

[Lüftung]

[Klima]

3. Komplexe Blöcke zur Auswahl mit Unterordnern und Musterdatei kopieren

[Bäder]

Bestand

Planung;Zeichnungen

planung;CAD

Installation;Demontage

Installation;Keramik;Gäste-WC

Installation;Keramik;Bad

[Heizung]

Bestand

Planung;Zeichnungen

Planung;Wärmebedarf

Installation

#D:\Muster\bauplan.xls

Installation;Demontage

Installation;Montage;Rohrnetz

Installation;Montage;Kessel

|

[Bild]

ANWENDUNG

Ein Projektordner kann automatisiert bei Projektneuanlage angelegt werden (vgl. Abschnitt "Einrichtung") oder nach Bedarf individuell über das Datenblatt des Projektes.

[Bild]

Wenn der Projektordner einmal angelegt ist, kann er entweder über einen Doppelklick auf den Eintrag in der Dokumentenliste (PrOrd) oder über das Menü geöffnet werden. Da man bei größeren Projekten mit vielen Dokumenten den Eintrag für den Projektordner nicht immer auf Anhieb findet, ist die Variante über des Menü oftmals einfacher.

[Bild]

Wichtig: Da es sich bei dem Projektorder um einen Windows Ordner handelt, der mit dem Label Projekt verknüpft ist, kann dieser wie gewohnt verwendet werden. Sie können Ordner anlegen, löschen oder umbenennen und beliebige Dateien einfügen, kopieren oder löschen. Zu berücksichtigen ist hier lediglich, dass diese Dateien und Ordner auch außerhalb von Label (über den Windows Explorer) erreichbar sind. Sollten Sie auch auf Dateiebene auf den Projektordner zugreifen, wirken sich alle Änderungen auch auf Label aus.
