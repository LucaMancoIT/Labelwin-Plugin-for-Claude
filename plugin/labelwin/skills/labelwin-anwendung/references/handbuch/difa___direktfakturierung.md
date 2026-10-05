# DiFa - Direktfakturierung

Pfad: Kundendienst > DiFa - Direktfakturierung
Quelle: handbuch/difa___direktfakturierung.htm

|

DiFa - Direktfakturierung

Stand: 07.02.2019

V5.89)

ANWENDUNG

Diese Methode wurde für den Einsatz bei unseren mobilen Anwendungen KD-Mobil oder iDeXs entwickelt. Die Anzahl der mobil verfügbaren Artikel soll bewusst begrenzt werden, damit der Mitarbeiter nur die relevanten Artikel mitführt.

DiFa-Artikel können in unseren mobilen Anwendungen verwendet werden, um zum Beispiel verbrauchtes Material zu erfassen oder mobil Rechnungen zu stellen.

Theoretisch kann jeder Artikel zum DiFa-Artikel gemacht werden. Es ist jedoch sinnvoll, die Auswahl auf üblicherweise verwendete Artikel zu beschränken. Zu den historischen Hintergründen der DiFa Entwicklung finden Sie am Ende dieser Seite weiterführende Erläuterungen.

1. DiFa-Artikel bestimmen

Im Schnitt verkauft ein Betrieb nicht mehr als 8.000 verschiedene Artikel pro Jahr. Dennoch ist nicht zu erwarten, dass irgendjemand alle diese Artikel einzeln zu DiFa-Artikeln machen möchte. Deshalb können mit Labelwin bestimmte Gruppen von Artikeln automatisch zu DiFa-Artikeln gemacht werden. Öffnen Sie dafür das Modul EINSTELLUNGEN und wählen unter <Mobil> den Punkt <DiFa Kennzeichen>.

[Bild: DiFa - Direktfakturierung]

|
[Bild: 1]

Katalog

[Bild: 1. Katalog]

Die Liste der DiFa-Artikel [Nr.3] kann über diese Auswahl auf einen Katalog eingegrenzt werden

|
[Bild: 2]

Anzeige

[Bild: 2. Anzeige]

Die Liste der DiFa-Artikel [Nr.3] kann über diese Auswahl auf den Ursprung ihrer Festlegung eingegrenzt werden. Die verschiedenen Arten der Festlegung sind in Punkt [Nr.4] auswähhlbar.

|
[Bild: 3]

DiFa-Artikel

[Bild: 3. DiFa-Artikel]

Hier werden alle DiFa-Artikel aufgelistet. Die Auflistung kann durch die Einstellungen in [Nr.1] und [Nr.2] eingegrenzt sein.

|
[Bild: 4]

DiFa-Kennzeichen festlegen

[Bild: 4. DiFa-Kennzeichen festlegen]

Die Menge der Artikel, die zu DiFa-Artikeln gemacht werden sollen, lässt sich auf verschiedene Weisen eingrenzen:

-

aus verkauften Artikeln (VA)

Labelwin sammelt alle Artikel die in einem bestimmten Zeitraum, den Sie unten im Fenster festlegen können, auf Ihren Ausgangsrechnungen gedruckt wurden. Bei Bedarf können Sie den Prozess auf Kundendienstrechnungen einschränken.

-

aus Suchbaum (SB)

Sie können in einem Drop-Down-Menü einen Suchbaum Ihres Labelwin auswählen. Alle Artikel dieses Suchbaums werden zu DiFa-Artikeln gemacht. Diese Eingrenzung eignet sich besonders für Unternehmen, die bereits über einen KD-Mobil-Suchbaum verfügen.

-

aus Lager (LA)

Alle Artikel, die in Ihrem Lager gelistet sind, werden ausgewählt. Sie können bestimmen, ob dabei die Artikel aller oder nur bestimmter Lager berücksichtigt werden sollen.

-

aus CSV (CSV)

Vorab erstellte .csv-Dateien können auch als Vorlage dienen. Weiter unten im Abschnitt Ausgabe ist dieser Prozess näher beschrieben.

-

per Durchlauf aus Katalog (DK)

Labelwin kann die Kataloge, für die Sie die DiFa-Funktion aktiviert haben nach verschiedenen Kriterien durchsuchen. Zur Auswahl stehen die Kriterien "Alle Artikel", „Beginn Artikelnummer“, „Suchwort Anfang“, „Einzelne Rabattgruppen“ und „Einzelne Warengruppen“. Wenn Sie einen Haken bei „Eintragen mit Einzelbestätigung“ setzen, wird Labelwin Ihnen die Artikel dieser Eingrenzung einzeln zeigen, damit sie entscheiden können, ob der jeweilige Artikel zu einem DiFa-Artikel gemacht werden soll oder nicht. Mit der Auswahl "Alle Artikel" können sogar alle Artikel eines Kataloge zu DiFa-Artikeln gemacht werden. Davon ist in der Regel jedoch abzuraten, da die Anzahl an DiFa-Artikeln auf diese Weise schnell unnötig groß und schwer zu händeln wird.

-

Manuell (MA)

Hier können die Artikel einzeln aufgerufen werden, die zu DiFa Artikeln gemacht werden sollen.

|
[Bild: 5]

Optionen

[Bild: 5. Optionen]

Dieser Bereich variiert abhängig von der bei Punkt [Nr.4] getroffenen Auswahl.

|
[Bild: 6]

Eintragen

[Bild: 6. Eintragen]

Hiermit können Sie bei den von Ihnen in Punkt [Nr.4] und [Nr.5] eingegrenzten Artikeln das Difa-Kennzeichen direkt im Katalog setzen.

|
[Bild: 7]

DiFa-Katalog für KD-Mobil füllen

[Bild: 7. DiFa-Katalog für KD-Mobil füllen]

Mit dieser Funktion werden alle Artikel mit DiFa-Kennzeichen in einen Katalog eingetragen, der dann zum mobilen Gerät (KD-Mobil) transportiert werden kann.

Der Katalog muss bereits angelegt sein (z.B. mit dem Namen 'Mobilartikel').

Je nach Anzahl der Artikel kann der Durchlauf sehr lange dauern und kann nicht abgebrochen werden.

Hinweis: Sollen die DiFa-Artikel an iDeXs übergeben werden, muss die Übertragung anders erfolgen. Im nachfolgenden Abschnitt "3. DiFa-Artikel an mobilen Anwendung übertragen" finden Sie die Beschreibung dazu.

|
[Bild: 8]

Ausgabe als CSV-Datei

[Bild: 8. Ausgabe als CSV-Datei]

Die Liste der DiFa-Artikel kann auch als .csv-Datei ausgegeben werden. Die CSV können Sie dann in Excel öffnen, um die Eingrenzung zu überprüfen und gegebenenfalls Änderungen vorzunehmen. Um den gesamten Prozess besser nachvollziehen zu können, ist es daher besonders am Anfang zu empfehlen, zunächst eine CSV ausgeben zu lassen, mit Excel zu kontrollieren und dann per Eingrenzung auf „aus CSV“ die Artikel zu DiFa-Artikeln zu machen.

|
[Bild: 9]

Alle gezeigten löschen

[Bild: 9. Alle gezeigten löschen]

Mit dieser Funktion können Sie die DiFA-Kennzeichen bei allen angezeigten Artikeln wieder löschen. Es wird bei allen Artikel mit dem Kennzeichen DiFa der Status weggesetzt. Sie werden wieder zu normalen Artikeln. Diese Option eignet sich dazu mit den Difa-Artikeln von Null zu starten..

|
[Bild: 10]

Löschen markierte Artikel

[Bild: 10. Löschen markierte Artikel]

Mit dieser Funktion können Sie die DiFA-Kennzeichen bei den markierten Artikeln wieder löschen. Es wird bei allen markierten Artikel mit dem Kennzeichen DiFa der Status weggesetzt. Sie werden wieder zu normalen Artikeln.

2. DiFa-Artikel an mobile Anwendung übertragen

1. Übergabe an iDeXs

Nachdem der Prozess in Labelwin abgeschlossen ist, können Sie die Artikel mit den DiFA-Kennzeichen an das iDeXs-Web übergeben. Von dort holt sich dann jedes Endgerät den Katalog ab.

Öffnen Sie dafür das Einstellungsmodul und klicken unter <Mobil> auf <iDeXs Stammdaten>. In der Maske klicken Sie auf die Schaltfläche <DiFa-Artikel übertragen>. Bedenken Sie, dass die Übertragung, je nachdem wie viele Artikel Sie übertragen möchten, viel Zeit in Anspruch nehmen kann.

[Bild]

Im ersten Schritt untersucht das Programm alle Kataloge ! mit der DiFa-Freigabe. Über diese Freigabe können Sie auch Kataloge aktivieren oder wegschalten. Das Programm zeigt Ihnen dann, welche Kataloge mit wieviel Artikeln hochgeladen werden. Diese Anzeige dient der Kontrolle, damit Sie noch mal sehen können, welche Kataloge und wie viele Artikel dabei sind. Sollte Ihnen dabei ein Fehler auffallen, können Sie noch abbrechen.

Anschließend werden die Daten Katalog für Katalog übertragen. Dieser Vorgang kann durchaus auch 30 Minuten dauern. Dabei kommt oft wieder die unsinnige (weil falsche) Meldung ‚dass das System nicht mehr reagiert.

Abholung durch das mobile Gerät

Im iDeXs selbst wählen Sie die Materialerfassung an und finden in der Maske des Artikelaufrufs einen Knopf zum aktualisieren (Kreis mit Pfeil). Das Abholen der Artikel geht sehr schnell – es dauert sicher nnur 1-2 Minuten. Dennoch ist es empfehlenswert den Vorgang in einem WLan zu starten.

2. Übergabe an KD-Mobil

Die Übergabe an KD-Mobil erfolgt anders als bei iDeXs. Die mit dem DiFa-Kennzeichen versehenen Artikel werden nicht einzeln übertragen, sondern es muss ein eigener DiFa-Katalog erzeugt werden. Dazu steht die Funktion DiFa-Katalog für KD-Mobil füllen zur Verfügung. Mit dieser Funktion werden alle Artikel mit DiFa-Kennzeichen in einen Katalog eingetragen. Der Katalog muss bereits angelegt sein (z.B. mit dem Namen 'Mobilartikel').

Der auf diese Weise gefüllte Katalog kann dann über den Grunddaten Export auf die KD-Mobil Geräte exportiert werden.

HINTERGRUND

|

Diese Methode wurde entwickelt, weil am Anfang der mobilen Anwendung kaum Speicher auf den ersten Geräten vorhanden war. Die Anzahl der Artikel für eine Abrechnung war also sehr begrenzt.

Aber auch heute gibt es noch Sinn, mit einer begrenzten Anzahl von Artikeln zu arbeiten. DiFa-Artikel können in mobilen Anwendungen, wie KD-Mobil und iDeXs, verwendet werden, um zum Beispiel mobil Rechnungen zu stellen.

Theoretisch kann jeder Artikel zum DiFa-Artikel gemacht werden. Es ist jedoch sinnvoll, die Auswahl auf üblicherweise verwendete Artikel zu beschränken.

Im Bereich des mobilen Kundendienstes können Sie beliebig viele Kataloge verwalten, also auch einfach alle in Frage kommenden Großhändlerkataloge zum mobilen Gerät transportieren. Allerdings besteht die Gefahr, dass der Mitarbeiter vor lauter Wald den Baum nicht sieht. Also er einen Artikel nicht finden kann, weil er in der Menge untergeht. Dieses Problem kann mit einem DiFa-Katalog umgangen werden.

|

Hinweis: Möglicherweise ist die Funktion auch für Anwender interessant, die nicht im mobilen Kundendienst unterwegs sind. Man kann nämlich nun einen eigenen (DiFa-)Katalog mit den Daten füllen, die man die letzten Jahre verkauft hat.

Wer diesen Weg geht, sucht die Artikel zwar im eigenen Katalog, aber sie bekommen das Händlerkennzeichen von dem Lieferanten, aus dessen Katalog der Artikel wirklich stammt.

|

|

Besonders anschaulich wird die Menge der benötigten Artikel, wenn Sie schauen, welche Artikel im Kundendienst in einem Jahr fakturiert worden sind.

Bei den meisten Betrieben sind es zwischen 2.000 und 8.000 verschiedene Artikel beim Hauptlieferanten.

Das können Sie für sich selber nachschauen, wenn Sie im Katalog-Modul auf den Menüpunkt [Katalog - Einzelübersicht] gehen. Dort wird Ihnen oben die gesamte Anzahl der im Katalog geführten Artikel angezeigt.

Unten befindet sich im Bereich "Benutze Artikel" der Knopf "Anzahl". Wenn Sie diese Knopf drucken, wird ermittelt wieviele Artikel aus diesem Katalog ab dem eingestellten Datum verwendet wurden.

[Bild]

|

[Bild]
