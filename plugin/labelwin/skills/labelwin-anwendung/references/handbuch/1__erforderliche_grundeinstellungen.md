# 1. Erforderliche Grundeinstellungen

Pfad: Buchhaltung > Fibuerfassung [25] > 1. Erforderliche Grundeinstellungen
Quelle: handbuch/1__erforderliche_grundeinstellungen.htm

|

1. Erforderliche Grundeinstellungen

|

Hinweis: Falls Sie mit der Mandantenversion arbeiten, müssen Sie alle im Folgenden beschriebenen Grunddaten für alle Mandanten erfassen, deren Kontoauszüge Sie buchen wollen.

Programmbaum erweitern

Das Modul FIBU-ERFASSUNG ist standardmäßig nicht im Programmbaum enthalten. Sie müssten es daher zunächst einbinden. Rufen Sie dazu im Programmbaum den Menüpunkt [Optionen - Programmbaum anpassen] auf und übernehmen das Modul Fibuerfassung.

[Bild]

1. Bankdaten

Starten Sie die Fibu-Erfassung. Erfassen Sie dann - soweit noch nicht geschehen - unter [Optionen - Bankdaten] die von Ihnen genutzten Banken. Tragen Sie unbedingt zusätzlich das in der Finanzbuchhaltung verwendete Konto dazu ein.

[Bild]

Die Bankdaten können auch im Modul EINSTELLUNGEN unter dem Menüpunkt [Programmbereiche - Buchhaltung - Bankdaten] aufgerufen werden.

Hinweis: Das Feld "Datentyp Kontoauszugsdatei’"muss nur belegt werden, wenn Sie für dieses Konto den Auszugsmanager benutzen wollen. Der Auszugsmanger ist ein separat zu erwerbendes Zusatzmodul.

2. Bank für Verrechnungen / Stornierungen (Dummy-Bank)

Um Verrechnungen zwischen Ausgangsrechnungen und Eingangsrechnungen vornehmen zu können, bei denen über das Konto kein Geld fließt, ist es sinnvoll ein weiteres Bankkonto zu simulieren. Wenn alles richtig gelaufen ist, steht der Kontostand immer auf Null. Dieser Bank müssen Sie in der Fibu ein Konto zuordnen (z.B. 1371 oder 1365, Unterkonto ‚Durchlaufender Posten’).

3. Kontenplan

Im Modul EINSTELLUNGEN unter dem Menüpunkt [Programmbereiche - Buchhaltung - Kontenplan] müssen sämtliche von Ihnen verwendeten Konten erfasst werden. Bei einer Neuauslieferung finden Sie dort bereits den Datev Kontenplan SKR 03 vor. Sollten Sie mit dem SKR 04 arbeiten wollen, so kann dieser ebenfalls eingespielt werden. Suchen Sie dann bitte die letzte CD von uns heraus und rufen bitte unsere Hotline an, die Sie dann führen wird. Kunden, die schon länger mit unserem Programmpaket arbeiten, müssen die dort eingetragenen Konten überprüfen und ggf. erweitern. Die in der Erfassung zu nutzenden Konten müssen unbedingt mit dem Merkmal „Fibuerfassung“ versehen sein. Neben den normalen Warenkonten benötigt die Fibu-Erfassung unbedingt mindestens ein Konto mit dem Merkmal „Skonti“ und ein Konto „Ausbuchung“. Diese Konten werden benötigt, wenn eine Ausgangsrechnung vom Kunden nicht komplett bezahlt wird. Je nach Verbuchung der Fehlsumme übergibt unser Modul die Skontosumme und ggf. auch die Ausbuchungssumme automatisch an die Finanzbuchhaltung.

Weitere Informationen lesen Sie bitte in der Beschreibung zur Erfassung des Kontenplanes.

Tipp: Sie können den Kontenplan auch über das Menü [Datei - Kontenplan] direkt in der Buchungsmaske erreichen.

4. Standard/Vorgabekonten für die Fibu-Erfassung

In dem Modul FIBU-ERFASSUNG finden Sie unter dem Menüpunkt <Optionen> die <Einstellungen>. Auch wenn Sie die hier abgefragten Konten bereits im Kontenplan hinterlegt haben, müssen Sie hier zusätzlich hinterlegt werden. Achten Sie unbedingt darauf, dass die Konten identisch mit dem Kontenplan sind. Obwohl die Konten überwiegend nur als Sicherheit gedacht sind, falls bei einer Buchung kein Skonto-Konto hinterlegt ist, sind diese Eintragungen zwingend. Bitte achten Sie darauf, dass die gleichen Konten auch im Kontenplan hinterlegt sind, da sonst keine Kontenmeldung an die Fibu erfolgen kann.

Hinweis: Aufgrund von MwSt-Umstellungen (zuletzt 2007 von 16% auf 19 %) müssen einige Konten ggf. doppelt eingetragen werden. Es sollten zumindest für eine gewisse Übergangszeit einige Konten mit dem bisherigen Steuersatz erfasst werden.

[Bild: 1. Erforderliche Grundeinstellungen]

|
[Bild: 1]

Skonto auf Eingangsrg.

[Bild: 1. Skonto auf Eingangsrg.]

Dieses Konto wird automatisch verwendet, wenn eine Eingangsrechnung nicht komplett bezahlt wird.

|
[Bild: 2]

Skonto auf EIngangsrg. anderer MwSt.

[Bild: 2. Skonto auf EIngangsrg. anderer MwSt.]

Dieses Konto wird automatisch verwendet, wenn eine Eingangsrechnung nicht komplett bezahlt wird.

|
[Bild: 3]

Verrechnungskonto Eingangsrg.

[Bild: 3. Verrechnungskonto Eingangsrg.]

Da mit einer Summe auf einem Kontoauszug mehrere Eingangsrechnungen bezahlt werden können (Zahlungslauf) benötigen wir zum Aufbau der Buchungssätze ein Zwischenkonto. Dieses Konto ist nach Ablauf der Buchungssätze immer ausgeglichen. In der verwendeten Finanzbuchhaltung muss das Verrechnungskonto unbedingt angelegt sein.

|
[Bild: 4]

Skonto auf Ausgangsrg.

[Bild: 4. Skonto auf Ausgangsrg.]

Bei ordnungsgemäßer Einrichtung des Programms wird dieses Skonto nie benutzt werden. Es kommt nur dann zum Einsatz, wenn beim Kontenplan kein Konto mit dem Merkmal "Skonto“ vorhanden ist. Um auf der sicheren Seite zu sein, erzwingen wir hier eine Standardvorgabe.

|
[Bild: 5]

Skonto auf Ausgangsrg. anderer MwSt.

[Bild: 5. Skonto auf Ausgangsrg. anderer MwSt.]

Bei ordnungsgemäßer Einrichtung des Programms wird dieses Skonto nie benutzt werden. Es kommt nur dann zum Einsatz, wenn beim Kontenplan kein Konto mit dem Merkmal "Skonto“ vorhanden ist. Um auf der sicheren Seite zu sein, erzwingen wir hier eine Standardvorgabe.

|
[Bild: 6]

Verrechnungskonto Ausgangsrg.

[Bild: 6. Verrechnungskonto Ausgangsrg.]

Wenn Sie Ausgangsrechnungen per Lastschrift (Bankeinzug) abrechnen, benötigen Sie ein Zwischenkonto, da in einer Summe auf dem Auszug ggf. mehrere Rechnungen eingezogen werden. Dieses Konto ist nach Ablauf der Buchungssätze immer ausgeglichen. In der verwendeten Finanzbuchhaltung muss das Verrechnungskonto unbedingt angelegt sein.

|
[Bild: 7]

Ausbuchung Ausgangsrg.

[Bild: 7. Ausbuchung Ausgangsrg.]

Auch dieses Konto wird bei ordnungsgemäßer Einrichtung nie zum Einsatz kommen. Es ist nur für den Fall vorgesehen, dass Sie im Kontenplan kein Konto mit dem Merkmal „Ausbuchung“ eingerichtet haben.

|
[Bild: 8]

Standarddebitor

[Bild: 8. Standarddebitor]

Wenn eine Ausgangsrechnung an einen Kunden ohne Debitoren-Nummer geschrieben wurde, wird bei der Zahlung dieses Standardkonto verwendet. Im Programmodul Einstellungen können Sie unter den Menüpunkten Grundeinstellungen, Allgemein erzwingen, dass Ausgangsrechnungen nur an Adressen mit Debitor-Nummer geschrieben werden können. In diesem Falle würde das hier hinterlegte Konto nie zum Einsatz kommen.

|
[Bild: 9]

Standardkreditor

[Bild: 9. Standardkreditor]

Wie beim Debitor kommt dieses Konto nur dann zum Einsatz, wenn eine Lieferantenadresse ohne Kreditor Nummer verwendet wurde.

|
[Bild: 10]

Verrechnungsbank

[Bild: 10. Verrechnungsbank]

<TODO>: Hier Beschreibung einfügen...

|
[Bild: 11]

OK

[Bild: 11. OK]

Durch Betätigen dieses Knopfes werden die Einträge übernommen.

|
[Bild: 12]

Abbruch

[Bild: 12. Abbruch]

Durch Betätigen dieses Knopfes wird die Maske ohne Speicherung verlassen.
