# 1. Einrichtungsarbeiten

Pfad: Buchhaltung > Rechnungsimport [Modul] > 1. Einrichtungsarbeiten
Quelle: handbuch/1__einrichtungsarbeiten_1.htm

|

1. Einrichtungsarbeiten

Die Einrichtung des Rechnungsimportes besteht aus zwei Bereichen. Zum einen muss die Schnittstelle zum Großhändler in der Adresse gepflegt werden (Teil 1.1) und zum anderen müssen allgemeine Import-Einstellungen gemacht werden (Teil 1.2).

1. 1 Schnittstellen Einrichtung

Wie die Rechnungen zu Ihnen gelangen, ist letztlich mit jedem Lieferanten zu vereinbaren. Wünschenswert ist es, diese Dateien ohne vorherige Markierung und Bereitstellung direkt vom Lieferanten zu erhalten. Dabei kann der Transport genau wie bei Angeboten, Preisanfragen etc. per FTP-Protokoll "auf einen Rutsch" oder einzeln per E-Mail stattfinden.

Rufen Sie im Adressprogramm die Adresse des Lieferanten auf und wählen den Menüpunkt <Bearbeiten> <Stammdaten UGL / Online>.

Je nach angebotenem Verfahren des Lieferanten (UGL oder ZUGFeRD) müssen Sie die entsprechende Karteikarte anwählen und die im folgenden beschriebenen Einstellungen vornehmen.

|

Tipp: Vordruck zur Anfrage der Zugangsdaten beim Lieferanten

Sollten Ihnen Ihre ZUGFeRD Zugangsdaten nicht vorliegen, müssen Sie diese bei Ihrem Lieferanten anfragen. Zu diesem Zweck haben wir eine ausfüllbare PDF erstellt, die Sie hier herunterladen und an Ihren Lieferanten weiterreichen können:


[Bild] 


ZUGFeRD

Hier setzen Sie links einen Haken bei "ZUGFeRD-Rechnung" und tragen im Reiter <ZUGFeRD> (rechte Seite) folgende Daten ein:

-

die FTP-Server-URL des Lieferanten (wird vom Lieferanten bei Absprache mitgeteilt)

-

Ihre Zugangsdaten (Username & Passwort) für den FTP-Server

-

den Pfad für die ZUGFeRD-Dateien auf dem FTP-Server (wird vom Lieferanten bei Absprache mitgeteilt)

-

Wählen Sie links den Katalog des Händlers aus und übertragen ihn in das Feld "Selektierte Kataloge".

[Bild]

Wenn der Datenaustausch nicht per FTP (sondern z.B. per E-Mail) erfolgt, müssen Sie "UGL dateibasierend" wählen und tragen im Reiter <UGL-Datei> (rechte Seite) folgende Daten ein:

-

Wählen Sie links den Katalog des Händlers aus und übertragen ihn in das Feld "Selektierte Kataloge".

-

einen Ablagepfad für die erhaltenen Dateien auf Ihrem Computer. Dieser Ordner dient später als "Umschlagebahnhof" für die eingehenden Rechnungen. Den Pfad müssen Sie zuvor per Windows Explorer anlegen. (Labelwin läd dann beim Importieren alle Rechnungen aus diesem Verzeichnis. Alternativ können Sie die einzelnen Rechnungen später auch einzeln per 'Drag&Drop' in das Programm laden.)

[Bild]

UGL

Die Einstellungen für UGL-Rechnungen sind fast identisch mit denen von ZUGFeRD Rechnungen. Es muss nur kein ZUGFeRD-Pfad ausgefüllt werden und die EInstellungen erfolgen auf der Karteikarte "UGL-FTP".

[Bild]

Wenn der Datenaustausch nicht per FTP erfolgt, müssen Sie den Ablagepfad unter "UGL dateibasierend" eintragen:

[Bild]

Rechnungen per PDF

Wenn Sie die Rechnungen zusätzlich per PDF bekommen, sollten Sie diese im gleichen Verzeichnis wie die UGL-Dateien ablegen. Damit kann die PDF zur Ablage verwendet werden und der Scan-Vorgang kann entfallen.

1.2 Import Einstellungen

Im nächsten Schritt müssen Sie Einträge im Modul EINSTELLUNGEN vornehmen. Wählen Sie dort den Menüpunkt <Programmbereiche> <Buchhaltung> <Grundeinstellungen>.

|

[Bild]

|

Standardprojekt:

Das Standardprojekt brauchen Sie für die Ablage der Rechnung als Labelwin-Dokument. Beim Import wird in dem Projekt ein ‚Freier Text‘ angelegt, der alle Artikel der Rechnung enthält. Bei Schreiben einer Rechnung können übrigens Artikel aus diesem Dokument kopiert werden. So können auch die Artikel von mündlichen Bestellungen in eine Ausgangs-Rechnung übernommen werden. Richten Sie am besten speziell hierfür ein Projekt ein, dem Sie das Kennzeichen ‚Für Auswertungen nicht nutzen‘ geben.

Kalkulations-Einstellung

Die Rechnung wird als Dokument abgelegt, um ggf. Artikel daraus übernehmen zu können. Die Artikel werden zwangsläufig mit einer Kalkulations-Einstellung kalkuliert, die Sie hier festlegen können.

Nehmen Sie am besten eine Kalkulationseinstellung mit einer Preisbildung wie im Kundendienst, da Sie wahrscheinlich öfter mal die Artikel des Thekenverkaufs in eine Rechnung übernehmen werden. Allerdings können Sie die Artikel bei der Verwendung auch jeweils neu kalkulieren, so dass die hier getroffene Einstellung nicht wichtig ist.

Importierte Datei verschieben statt löschen

Legen Sie fest, ob die UGL-Datei nach dem Import gelöscht oder in ein anderes Verzeichnis verschoben werden soll. Mindestens für die erste Zeit empfehlen wir das Verschieben, damit man bei Problemen die Ursache herausfinden und eine Rechnung ggf. erneut einlesen kann. Langfristig sollten Sie die Datei aber nach der Verarbeitung löschen, denn sie wird nicht mehr benötigt. Die Ablage im Scan-Archiv findet unabhängig von dieser Einstellung statt.

Bei UGL: Falls Sie die Rechnung zusätzlich als PDF bekommen, muss diese zur automatischen Ablage im gleichen Verzeichnis liegen. Eine vorhandene PDF wird ebenfalls in dieses Verzeichnis verschoben.

Wenn Sie die Verschiebe-Option nutzen, sollten Sie von Zeit zu Zeit in diesem Verzeichnis ‚aufräumen‘ / löschen.

|

Differenzprojekt

Beim Import von Eingangsrechnungen wird eine Verbindung zu eventuell vorhandenen Eingangslieferscheinen hergestellt. Wenn zu einer Rechnung des Lieferanten mehrere Eingangslieferscheine vorhanden sind, wird immer ein zusätzlicher Verteilsatz angelegt, in dem die Differenz zwischen der Rechnungssumme und der Summe der Eingangslieferscheine abgelegt wird.

Die Differenzbuchung wird dem hier hinterlegten Projekt zugeordnet. Wenn Sie keine Vorgabe treffen, muss das Projekt immer manuell gewählt werden. Wenn Sie bei dem Projekt das Warenkonto für 'Differenzen' hinterlegen, wird dieses passend vorgeschlagen.

Import-Protokoll erzeugen:

Dieses Feld ist für die Einführungsphase interessant. Beim Import werden die Vorgänge protokolliert und können im Fehlerfall zur Ursachensuche verwendet werden. Bei Öffnen der Buchungsmaske wird das Protokoll im Hintergrund geöffnet und schließt sich automatisch nach Abschluss der Buchung.

[Bild]

Bei Bedarf können Sie diese Datei speichern, um ggf. später noch einmal etwas nachzuschauen.

PDF sofort anzeigen, wenn vorhanden

Bei gesetztem Schalter wird eine vorhandene PDF sofort zur Ansicht geöffnet. Sinnvoll ist dies, wenn Sie einen sehr großen Bildschirm haben, 2 Bildschirme haben oder die Rechnung nur als Pdf bekommen haben.(kein Papierausdruck)

Das Programm sucht beim UGL-Import die PDF im gleichen Verzeichnis wie die UGL-Dateien. Die PDF-Datei heißt im optimalen Fall Rg 12345.pdf. Es genügt aber auch, wenn die Rechnungsnummer im Datei-Namen vorkommt. Da es hier keine Norm gibt, haben wir unser Programm möglichst tolerant programmiert. Von der Logik her müsste die Rechnungsnummer genau so sein, wie sie in der UGL eingetragen ist. Allerdings wird sie auch gefunden, wenn sie dort führenden Nullen (z.B. 0001245) aufgeführt ist, und im PDF-Namen die Nullen weggelassen worden sind.

Beim ZUGfERD-Import besteht dieses Problem nicht, da die PDF mit den EDV-Daten zusammen in einer Datei ist.

Die PDF-Anzeige schließt sich automatisch nach Abschluss der Buchung.

Immer eigene Zahlungsbedingung nehmen

Beim Import von Eingangsrechnungen per Datei ist oft ein Unterschied zwischen den Daten der Datei und denen, die bei der Lieferantenadresse hinterlegt sind. Sobald Unterschiede bestehen, wird eine Maske mit den Differenzen gezeigt, in der man sich entscheiden muss, welche Daten verwendet werden sollen.

Diese Anzeige stört natürlich im Arbeitsablauf und es kann sinnvoll sein, 'ohne Rücksicht auf Verluste' immer die eigenen, bei der Adresse oder dem Projekt hinterlegten Zahlungsbedingungen zu verwenden.
