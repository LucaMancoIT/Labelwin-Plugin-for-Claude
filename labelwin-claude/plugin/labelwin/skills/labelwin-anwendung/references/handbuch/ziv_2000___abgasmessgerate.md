# ZIV 2000 - Abgasmessgeräte

Pfad: Schnittstellen > ZIV 2000 - Abgasmessgeräte
Quelle: handbuch/ziv_2000___abgasmessgerate.htm

|

ZIV 2000 / ZIV XML Schnittstelle zu Abgasmessgeräten

Stand 20.11.2018

(V5.87)

THEMA

|

Mit der ZIV2000 Schnittstelle können Messwerte aus Abgasmessgeräten in die Anlagen Karteikarten von Labelwin direkt übernommen werden. Es erspart das manuelle Erfassen oder Ausdrucken der Werte vor Ort und das manuelle Eintippen in die Karteikarten. Unsere ZIV2000 Schnittstelle kann Messwerte im Format ZIV 2000 und ZIV XML (2013) verarbeiten. Historisch bedingt belassen wir den Schnittstellenamen bei ZIV2000 Schnittstelle.

Gängige Hersteller von Abgasmessgeräten sind MRU und testo.

Info: ZIV steht für "Zentralinnungsverband des Bundesverbandes des Schornsteinfegerhandwerks"

VORAUSSETZUNGEN

|

-

ein Abgasmessgerät mit einer ZIV 2000 oder ZIV XML Schnittstelle

-

Übertragungssoftware des Messgeräte Herstellers

Hinweis: Sehr viele Abgasmessgeräte unterstützen die ZIV Schnittstelle. Bitte prüfen Sie das mit dem Hersteller des Messgerätes. Zusammen mit dem Übertragungskabel zum PC erhalten Sie vom Hersteller ein Programm zum Auslesen der Daten. Dieses Programm muss auf dem Labelwin Arbeitsplatz installiert sein, von dem aus Sie die Daten importieren wollen.

-

ZIV 2000 Messwerte Zuordnung in Labelwin

EINRICHTUNG

|

Installation Messgeräte Software

Installieren Sie die ZIV2000 Übertragungssoftware des Messgeräteherstellers auf dem Labelwin Arbeitsplatz, von dem aus Sie die Daten auslesen möchten. Bei der Einrichtung dieses Programms können wir Ihnen leider keine Hilfestellung geben. Ggf. müssen Sie sich an den Hersteller des Gerätes wenden.

Einrichtung Labelwin

Starten Sie das Labelwin Modul EINSTELLUNGEN und rufen Sie den Menüpunkt [Programmbereiche - Kundendienst - ZIV 2000 (Abgasmessgeräte)] auf.

|

[Bild]

|

Tragen Sie in der ersten Zeile unter Pfad und Dateinamen das ZIV 2000 Übertragungsprogramm des Messgeräte Herstellers ein.

Bei der Firma Testo liegt es wahrscheinlich unter „c:\programme\testo\“ und heißt „testo.exe“.

Bei der Firma MRU heißt es „Zivmodul.exe“ und liegt wahrscheinlich im Unterverzeichnis „\zivpack\“ des installierten Pfades.

Bei anderen Herstellern fragen Sie bitte dort nach.

Ordnen Sie dann den einzelnen ZIV Nummern und Beschreibungen den entsprechenden Karteikarten-Eintrag zu. Eine entsprechende Karteikarten Vorlage sollten Sie zuvor unter [Programmbereiche - Anlagen und Verträge - Karteikarte] erstellt haben.

Hinweis: Wenn für die Anlage noch keine Karteikarte existiert, werden die Messwerte nicht eingelesen, sondern in einer temporären Datei hinterlegt, die Sie dann im Anlagefenster unter [Bearbeiten - ZIV 2000 Abgaswerte einlesen] einlesen können. Karteikartenkürzel, die in der Karteikarte der Anlage noch nicht existieren, werden jedoch beim Einlesen der Messwerte automatisch angefügt.

Alle Messwerte für die eine Historie mit Messdatum geführt werden soll, müssen mit einem „#“ (Doppelkreuz) beginnen.

Einträge, die zwar übernommen, aber für die keine Historie geführt werden sollen, beginnen ohne „#“ (Doppelkreuz).

Einträge, die überhaupt nicht übernommen werden sollen, bekommen keinen Eintrag in der Spalte „Karteikartenfeld“ oder können komplett gelöscht werden.

Anlagenzuordnung der Messwerte im Messgerät

Damit im Messgerät gespeicherte Werte beim Einlesen den entsprechenden Anlagen zugeordnet werden können, muss eine Messung im Messgerät mit der Anlagennummer gespeichert werden (ohne Anlagennummer kann nur eine Messung direkt bei der Anlage eingelesen werden).

|

[Bild]

|

Diese Anlagenummer (ZIV2000 Nummer) sollte idealerweise auf dem KD-Auftragsformular mit aufgedruckt sein. Sie können diese Nummer auch im „Anlagen“ Fenster im Feld „ZIV2000 Nr“ sehen.

Bei den Testo Messgeräten wird die ZIV2000 Nummer als Speichername erfasst. Achten Sie auf den Schrägstrich. Der darf nicht vergessen werden.

Im Messgerät können beliebig viele Messungen von verschiedenen Anlagen gespeichert werden.

Anpassung des Kundendienstreports (optional)

Damit im Messgerät gespeicherte Werte beim Auslesen den entsprechenden Anlagen zugeordnet werden können, muss eine Messung im Messgerät mit der Anlagennummer gespeichert werden.

Damit der KD-Monteur diese Nummer weiß, sollte sie auf dem KD-Auftragszettel mit ausgedruckt werden.

Wenn Sie den Crystal Reportgenerator haben, können Sie diese Nummer mit der Formel „@ZIV2000“ in den entsprechenden KD Reports eintragen.

Wenn Sie keinen Crystal Reports haben, können wir diese Reportänderungen für Sie durchführen (gegen eine geringe Kostenpauschale).

Anpassung des SMS Textbausteins (optional)

Wenn Sie das SMS Modul benutzen, um KD-Aufträge an den Monteur zu übermitteln, sollten Sie bei Aufträgen, die eine Messung beinhalten, die ZIV2000 Nummer mit in die SMS schreiben.

Das Schlüsselwort für die ZIV2000 Nummer lautet:

@KDanlagennr@/@KDdifapruefziffer@

Der Baustein wird im Modul EINSTELLUNGEN Menüpunkt [Vorlagen - Vor- und Nachbemerkung] angelegt und heißt „SMS-KD“.

ANWENDUNG

Auslesen des Messgerätes

|

[Bild]

|

Das Messgerät kann im Programm an zwei Stellen ausgelesen werden. Entweder in der Kundendienst Hauptmaske unter [Import/Export - Messdaten einlesen (ZIV 2000)] oder in der Anlagenmaske unter [Bearbeiten - ZIV2000 Abgasdaten einlesen]. Beide Wege öffnet die gleiche Einlesemaske, die nachfolgend dargestellt wird. Es gibt aber einen entscheidenden Unterschied. Wird das Messdaten einlesen im Kundendienst aufgerufen, können mehrere Messungen für verschiedene Anlagen in einem Rutsch eingelesen werden; in der Anlage wird nur eine Messung für die gewählte Anlage eingelesen. Damit mehrere Messung automatisch richtig zugeordnet werden können, muss bei jeder Messung die ZIV2000 Nr. eingetragen worden sein. Ohne diese Nummer kann die Einspielung nur einzeln direkt in der Anlage selbst erfolgen.

|

[Bild]

|

Zum Auslesen des Messgerätes gibt es mehrere Methoden:

-

direkt über den COM-Port mit einem Übertragungskabel

-

über eine Datendatei

-

per Bluetooth

-

IrDa

-

USB

-

Manuelle POrtangabe

-

ZIV XML Datei

-

MRU

-

Direkt über den COM-port

Schließen Sie das Messgerät mit dem PC Übertragungskabel über einen seriellen COM-Port an den PC an.

Wählen Sie unter "Serielle Schnittstelle" den entsprechenden COM-Port aus und klicken Sie auf OK. Wenn alles richtig angeschlossen ist, werden die Daten automatisch aus dem Messgerät gelesen und in die entsprechenden Karteikarten eingetragen. Am Ende der Übertragung wird ein Übertragungsprotokoll angezeigt.

Die Messwerte müssen danach im Messgerät gelöscht werden, denn sonst würden sie ggf. ein zweites Mal übertragen. Wie die Daten aus dem Messgerät gelöscht werden, lesen Sie bitte im Handbuch des Messgerätes nach.

-

Über eine Datendatei

Schließen Sie das Messgerät mit dem PC Übertragungskabel an einen seriellen COM-Port an den PC an. Benutzen Sie die beim Messgerät mitgelieferte Software, um die Messwerte auszulesen und in eine Datei zu schreiben. Pfad und Dateiname sind egal, solange Sie sich den Dateinamen merken. Näheres zum Auslesen entnehmen Sie bitte der Bedienungsanleitung des Messgeräteherstellers.

Klicken Sie auf „Datendatei“ und geben Sie Pfad und Dateinamen der soeben erzeugten Datendatei ein. Sie können ihn auch über den "Durchsuchen" Knopf auswählen.

Zur Kontrolle, ob es die richtige Datei ist, können Sie sich die Datei über den Knopf „Datendatei zeigen“ anzeigen lassen.

[Bild]

Klicken Sie dann auf OK. Wenn die Datei eine korrekte ZIV2000 Datei ist, werden die Messwerte in die entsprechenden Karteikarten eingetragen. Am Ende der Übertragung wird ein Übertragungsprotokoll angezeigt.

Die Messwerte müssen danach im Messgerät gelöscht werden, denn sonst würden sie ggf. ein zweites Mal übertragen. Wie die Daten aus dem Messgerät gelöscht werden, lesen Sie bitte Im Handbuch des Messgerätes nach.

-

Per Bluetooth

Aktuelle Messgeräte beherrschen die Kommunikation über Bluetooth. Sollte Ihr PC oder Laptop ebenfalls über Bluetooth verfügen, können Sie die Messdaten auch kabellos übertragen. Aktivieren Sie dazu das Bluetooth auf dem Messgerät und Ihrem PC/Laptop. Koppeln Sie die Geräte. Da die Kopplung eine reine Windows Funktion ist, können wir Ihnen bei der Einrichtung der Bluettoth Verbindung nicht helfen.

Am Ende der Übertragung wird ein Übertragungsprotokoll angezeigt. Die Messwerte müssen danach im Messgerät gelöscht werden, denn sonst würden sie ggf. ein zweites Mal übertragen. Wie die Daten aus dem Messgerät gelöscht werden, lesen Sie bitte im Handbuch des Messgerätes nach.

-

Über eine ZIV XML

Aktuelle Messgeräte können die Messungen an ein Smartphone senden. Wenn dort eine spezielle App des Messgeräte Herstellers installiert ist, kann die Messung im ZIV XML Format an eine E-Mail Adresse gesendet werden.

Liegt Ihnen so eine ZIV XML Datei vor, kann diese über die Option "ZIV XML (Verzeichnis)" eingelesen werden. Im Unterschied zu den Methoden "Serielle Schnittstelle" und "Bluetooth" kann keine direkte Kommunikation zwischen dem Messgerät und Labelwin stattfinden. Sie müssen zuerst außerhalb von Labelwin eine ZIV XML Datei erzeugen.

Beim erstmaligen Einlesen einer ZIV XML werden alle neuen ZIV Felder, die anders lauten als bei ZIV2000, in die ZIV Messwerte Zuordnungliste eingetragen. Hier müssen Sie wiederum die Zuordnung zu Ihren Karteikartenfeldern vornehmen. ZIV XML Daten haben im Unterschied zu ZIV200 keine 6 bis 7-stellige Nummern, sondern Zeichenketten wie "Date", P_Draft". Lambda" etc.

[Bild]

Wenn alles richtig eingerichtet wurde, werden die Daten aus der ZIV XML gelesen und in die entsprechenden Karteikarten eingetragen. Am Ende der Übertragung wird ein Übertragungsprotokoll angezeigt.

Hinweis: Eine ZIV XML kann zusätzlich zum Kundendienst und Anlage auch direkt in der Karteikarte unter [Bearbeiten - ZIV XML einlesen] eingelesen werden.

-

Über MRU (Remotedata.exe)

Der Hersteller MRU verwendet eine remotedata.exe zum Auslesen seiner Messgeräte. Verwenden Sie also ein Gerät von MRU wählen Sie diese Option. Natürlich muss die Software von MRU zuvor installiert worden sein.

Wenn alles richtig eingerichtet wurde, werden die Daten automatisch aus dem Messgerät gelesen und in die entsprechenden Karteikarten eingetragen. Am Ende der Übertragung wird ein Übertragungsprotokoll angezeigt.

Fehlende Karteikarten

Sollte es zu einer Anlage noch keine Karteikarte geben, werden die Messwerte nicht eingetragen, sondern in eine temporäre Datei geschrieben. Nachdem Sie für die Anlage eine Karteikarte erstellt

haben, können Sie im Anlagenfenster über den Menüpunkt „Bearbeiten, ZIV2000 Abgaswerte einlesen“, aus der temporären Datei einlesen. Pfad und Dateiname der temporären Datei wird bereits vorgeschlagen.

[Bild]

Fehlerhafte Zuordnungen

Sollte eine Messung nicht einer Anlage zugeordnet werden können, da entweder die ZIV2000 Nummer fehlt oder fehlerhaft erfasst wurde, dann gibt es eine entsprechende Meldung. Die Daten der Messungen werden in einzelnen Dateien mit dem Namen „ZIVn.TXT“ im Labelwin Temp-Verzeichnis (meist „c:\labeltmp\“ oder „c:\labelwin\temp\“) abgelegt. Den genauen Dateinamen entnehmen Sie dem Meldefenster.

[Bild]

Wechseln Sie dann über das Programm ADRESSEN oder über die Kundendienstauftragsmaske im Modul KUNDENDIENST zur Anlage. Über den Menüpunkt [Bearbeiten - ZIV2000 Abgasdaten] können Sie dann eine solche einzelne Datei einlesen und in der Karteikarte eintragen lassen.

Wenn Sie allerdings mehrere ZIVn.TXT Dateien erstellt wurden, kann es recht schwierig werden die Datei, die aus lauter Zahlen besteht, der richtigen Anlage zuzuordnen. Der beste Weg ist daher, von vornherein die ZIV2000 Nummer im Abgasgerät korrekt zu erfassen.
