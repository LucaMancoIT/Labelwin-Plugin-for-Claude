# 2.9.2 Kontenplan

Pfad: Einrichtungsarbeiten > Einstellungen [14] > 2. Programmbereiche > 2.9 Buchhaltung > 2.9.2 Kontenplan
Quelle: handbuch/2_9_2_kontenplan.htm

|

2.9.2 Kontenplan

Bei der Nutzung des Moduls Fibuerfassung sind erheblich mehr Konten anzulegen, als unmittelbar im Programmpaket Labelwin benutzt werden. Da bei der Fibu-Erfassung auch freie Buchungen auf jedes beliebige Fibu-Konto möglich sind, sollte an dieser Stelle am besten der komplette Kontenplan hinterlegt werden.

Hinweis: Obwohl Sie die Konten unbedingt mit Ihrem Steuerberater absprechen sollten, haben wir am Ende dieses Kapitels den Datev SKR 03 abgebildet. Bei einer Auslieferung ist dieser Plan standardmäßig vorgegeben. Über das Menü können Sie auch den SKR 04 importieren.

[Bild]

Bild: Grundeinstellungen - Kontenplan

[Bild]

1 Eingrenzung: Durch Aktivieren dieses Feldes können Sie sich nur die Konten anzeigen lassen, die ein bestimmtes Kennzeichen haben wie z.B. alle Konten mit dem Kennzeichen Erlöskonto.

[Bild]

2 Liste: Zeigt Ihnen die Liste der bereits erfassten Konten an.

[Bild]

3 Kontonummer: Geben Sie hier die Kontonummer ein, wie Sie auch in der Finanzbuchhaltung verwendet wird. Unser Programm lässt hier eine zehnstellige Eingabe zu, weil z. B. in Österreich sechsstellige Kontonummern üblich sind. Erfassen Sie bitte die Kontonummer exakt so, wie sie auch in der Fibu verwendet wird. Wenn dort führende Nullen benutzt werden, müssen Sie auch hier führende Nullen davor setzen.

[Bild]

4 Bezeichnung: Geben Sie hier dem Konto eine Inhaltsangabe an.

[Bild]

5 Bilanzgruppe: Wenn Sie das Modul Controlling erworben haben und eine monatliche Betriebsauswertung erstellen möchten, ist es notwendig, dass Sie die Konten Bilanzgruppen zuordnen. Wählen Sie hier die entsprechende Bilanzgruppe für das Konto aus.

[Bild]

6 Steuerkonto: Hier ist nur dann ein Konto einzutragen, wenn in Ihrer Finanzbuchhaltung das gerade erfasste Konto kein so genanntes Automatikkonto ist. In der Datev und in anderen Finanzbuchhaltungen ist es üblich, bestimmte Konten automatisch mit der MwSt zu verbinden. In diesem Falle dürfen Sie hier kein Steuerkonto angeben. Bei der Angabe eines Steuerkontos ist unser Programm in der Lage, in der Fibu-Übergabe einen getrennten Buchungssatz für den MwSt-Anteil zu übergeben. Da Labelwin auf diese Werte erst bei der Datenübergabe an eine Fibu zugreift, können Sie die Daten auch im letzten Moment noch eintragen und auch ohne diese Werte in Labelwin arbeiten.

[Bild]

7 Steuersatz: Geben Sie hier unbedingt den zutreffenden Steuersatz an, damit das Programm bei Bruttosummen den Netto und Steueranteil ausrechnen kann. Diese Eingabe ist immer erforderlich, auch wenn es sich um ein Automatikkonto handelt.

[Bild]

8 Steuerschlüssel: Bei einigen Fibu’s wie z. B. der Datev können Kontonummern unterschiedlich genutzt werden. Über den Steuerschlüssel wird dann festgelegt, welcher MwSt bzw. Vorsteuersatz zum Einsatz kommt. Die Eintragung ist also nur dann erforderlich, wenn Ihre Finanzbuchhaltung eine entsprechende Möglichkeit hat. Sprechen Sie bitte diesen Bereich mit Ihrem Steuerberater ab, da wir Ihnen hier Ihnen keine Hilfestellung bieten können. Auch dieser Wert wird erst bei der Übergabe an die Fibu verwendet und kann nachgetragen werden.

|

Um ein Konto mit verschiedenen Steuerschlüsseln verwenden zu können, betätigen Sie den Hilfeknopf hinter dem Eingabefeld.

[Bild]

9 Fibukennz.: In diesem Feld können für die Fibuschnittstelle Informationen hinterlegt werden, die über unsere Fibuschnittstelle übertragen werden können. In der Regel wird dieses Feld leer bleiben, da die Reaktion in der Schnittstelle nur für bestimmte Buchhaltungsprogramme programmiert wird.

[Bild]

10 Erlöskonto MwSt. Satz 2: Bei der Dokumentenanlage kann nur ein Erlöskonto gewählt werden. Es kann jedoch innerhalb des Dokuments vorkommen, dass Sie einen Artikel mit einem verminderten Mehrwertsteuersatz haben. Tragen Sie hier das entsprechende Konto dafür ein. Es wird dann automatisch für diesen entsprechenden Artikel dieses Konto gewählt.

[Bild]

11 Erlöskonto ohne MwSt.: Genau wie beim verminderten Mehrwertsteuersatz, gibt es in Dokumenten auch Artikel, die nicht mehrwertsteuerpflichtig sind. Tragen Sie hier das entsprechende Konto ein.

[Bild]

12 Skontokonto Erlöse: Tragen Sie hier das Skontokonto für Erlöse ein.

[Bild]

13 Parallelkonto ohne MwSt.: Tragen Sie hier das Erlöskonto nach §13b UStG sein.

[Bild]

14 Verwendung bei: In diesem Bereich legen Sie fest, an welcher Stelle im Programmpaket das Konto eingesetzt werden kann. Wenn z.B. ein Konto das Merkmal ‚Fibuerfassung‘ nicht hat, wird es in diesem Modul nicht angeboten. Gehen Sie mit den Verwendungsbereichen sorgfältig um, da damit viele Fehlbuchungen ausgeschlossen werden können.

[Bild]

15 Kontoart: Hier legen Sie fest, ob im Bereich Kassenbuch und Fibu-Erfassung ein Konto üblicherweise positiv oder negativ belastet wird. Wir verändern damit das Vorzeichen der bei der Buchung einzugebenden Summe. Konkret erreichen Sie durch das Kennzeichen als Ausgang, dass eine positiv eingegebene Summe dennoch negativ verbucht wird. Wenn Sie auf diese Eingabehilfe verzichten wollen, können Sie alle Konten auf die Kontoart ‚Eingang’ setzen. In diesem Fall müssen Sie dann abgehende Summen mit einem Minuszeichen buchen.

[Bild]

16 Konto eingehende Mahngebühren/Zinsen: Wenn bei einer Ausgangsrechnung Mahngebühren oder Mahnzinsen entstanden sind, und diese vom Kunden tatsächlich bezahlt werden, so müssen diese im Prinzip auf ein separates Konto gebucht werden. Die Mahnerlöse werden als Ausbuchung im Zahlungseingang eingetragen.

Das Konto muss vom Typ ‚Ausbuchung‘ sein und wird mit negativen Beträgen bebucht

Mit dieser Vorgabe wird in der Zahlungsmaske das passende Konto in der Auswahlliste voreingestellt. Das Merkmal kann nur für ein Konto vergeben werden - das letzte gewinnt.

[Bild]

17 Bei Projektauswertung berücksichtigen: Dieses Feld ist nur sichtbar, wenn Sie bei ‚Verwendung bei’ das Merkmal ‚Fibuerfassung’ gesetzt haben. Damit haben Sie dann die Möglichkeit, dass das Konto in der Projektauswertung berücksichtigt wird.

[Bild]

18 Kommentar / Hinweise: In diesem Feld können Sie einen Kommentar oder Hinweis für das gewählte Konto hinterlegen.

[Bild]

19 Neu: Durch Betätigen dieses Knopfes wird die Maske geleert und Sie können ein neues Konto erfassen.

[Bild]

20 Speichern: Durch Betätigen dieses Knopfes werden die Eingaben gespeichert.

[Bild]

21 Speichern als neu: Durch Betätigen dieses Knopfes haben Sie die Möglichkeit, ein vorhandenes Konto abzuändern und dann als neuen Eintrag zu speichern.

[Bild]

22 Ende: Durch Betätigen dieses Knopfes wird die Erfassung des Kontenplanes beendet.

Die Menüpunkte im Einzelnen:

Datei

Neues Konto F2

Gleiche Bedeutung wie der Knopf ‚Neu’ (Nr. 18)

Speichern

Gleiche Bedeutung wie der Knopf ‚Speichern’ (Nr. 19)

Speichern als neu F3

Gleiche Bedeutung wie der Knopf ‚Speichern als neu’ (Nr. 20)

Löschen

Mit diesem Menüpunkt haben Sie die Möglichkeit, ein Konto zu löschen.

Kontenplan löschen

Mit diesem Menüpunkt können Sie den gesamten Kontenplan löschen.

Steuersatz ändern wg. MwSt. E

Hier haben Sie die Möglichkeit bei einer Mehrwertsteueränderung den Mehrwertsteuersatz zu ändern. Tragen Sie dann auch unbedingt ein, wie lange der alte Mehrwertsteuersatz Gültigkeit hat.

Zuordnung Bilanzgruppen prüfen

Mit diesem Menüpunkt wird geprüft, ob es Konten ohne Bilanzgruppe gibt.

Externen Kontenrahmen importieren

Mit diesem Menüpunkt können Sie von unserer Auslieferungs-CD den Kontenplan SKR03 oder SKR04 importieren. Standardmäßig ist der SKR03 installiert. Sie finden die Datei auf der CD im Verzeichnis inst32\diverses\skr. Bitte beachten Sie, dass durch den Import alle bisherigen Konteneinträge gelöscht werden. Der Import ist nur dann sinnvoll, wenn Sie mit dem Kontenplan noch nicht gearbeitet haben.

SKR03

Unter diesem Menüpunkt wählen Sie den Kontenplan SKR03 zum Import

SKR04

Unter diesem Menüpunkt wählen Sie den Kontenplan SKR04 zum Import

Aus CSV-Datei

Unter diesem Menüpunkt können Sie einen Kontenplan aus einer CSV-Datei importieren.

Bilanzgruppen aus Vorlage kopieren

SK03

Unter diesem Menüpunkt können Sie die Bilanzgruppen für den Kontenplan SKR03 einlesen.

SK04

Unter diesem Menüpunkt können Sie die Bilanzgruppen für den Kontenplan SKR04 einlesen

Drucken

Dient zum Ausdruck des Kontenplanes. Die Formularnamen beginnen mit KK.

Beenden

Schließt das Eingabefenster, gleiche Bedeutung wie der Knopf ‚Ende’ (Nr. 21)

Kontenliste SKR03 (als Muster betrachten!)

|

|

|

|

|

|

Steuer

|

Kto.-Nr.

|

Beschreibung

|

Verwendung

|

Gruppe

|

Art

|

Konto

|

Satz

|

Schlüssel

|

Klasse: 0

|

|

0200

|

Technische Anlagen und Maschinen

|

WKF

|

Diverses

|

Fragen

|

|

19,00

|

90

|

0320

|

PKW

|

WKF

|

Diverses

|

Fragen

|

|

19,00

|

90

|

0350

|

LKW

|

WKF

|

Diverses

|

Fragen

|

|

19,00

|

90

|

0400

|

Betriebsausstattung

|

WF

|

Diverses

|

Fragen

|

|

19,00

|

90

|

0410

|

Geschäftsausstattung

|

WF

|

Diverses

|

Fragen

|

|

19,00

|

90

|

0420

|

Büroeinrichtung

|

WF

|

Diverses

|

Fragen

|

|

19,00

|

90

|

0430

|

Ladeneinrichtung

|

F

|

Diverses

|

Fragen

|

|

19,00

|

90

|

0440

|

Werkzeuge

|

F

|

Diverses

|

Fragen

|

|

19,00

|

90

|

0480

|

geringw. Wirtschaftsgüter bis 410 EUR

|

WF

|

Diverses

|

Fragen

|

|

19,00

|

90

|

|

|

|

|

|

|

|

|

Klasse:1

|

|

1000

|

Kasse

|

|

Diverses

|

Fragen

|

|

|

|

1100

|

Postbank

|

|

Diverses

|

Fragen

|

|

|

|

1200

|

Bank

|

|

Diverses

|

Fragen

|

|

|

|

1330

|

Schecks

|

F

|

Diverses

|

Fragen

|

|

|

|

1360

|

Geldtransit

|

KF

|

Diverses

|

Fragen

|

|

|

|

1361

|

Verrechnung Eingangsrechnungen

|

|

|

Fragen

|

|

|

|

1362

|

Verrechnung Zahlungsläufe

|

|

|

Fragen

|

|

|

|

1363

|

Verrechnung / Stornierung

|

|

|

Fragen

|

|

|

|

1400

|

Forderung aus Lieferung und Leistung

|

|

|

Fragen

|

|

|

|

1590

|

Durchlaufender Posten

|

KF

|

Diverses

|

Fragen

|

|

|

|

1591

|

Verrechnungskonto Eingangsrechnungen

|

KF

|

Diverses

|

Fragen

|

|

|

|

1600

|

Verbindlichkeit aus Lieferung + Leistung

|

|

Diverses

|

Fragen

|

|

|

|

1660

|

Schuldwechsel

|

F

|

Diverses

|

Fragen

|

|

|

|

1700

|

sonstige Verbindlichkeiten

|

F

|

|

Ausgang

|

|

|

|

1710

|

Erhaltene Anzahlungen AU ohne UST

|

E

|

|

|

|

|

|

1717

|

16% erhalt. versteuerte Anzahlungen

|

E

|

|

|

|

16,00

|

|

1718

|

19% erhalt. versteuerte Anzahlungen

|

E

|

|

|

|

19,00

|

|

1740

|

Verb. Lohn und Gehalt

|

F

|

|

Ausgang

|

|

|

|

1741

|

Verb. Lohn und Kirchensteuer

|

F

|

|

Ausgang

|

|

|

|

1742

|

Verb. soziale Sicherheit

|

F

|

|

Ausgang

|

|

|

|

1750

|

Verb. VWL

|

F

|

|

Ausgang

|

|

|

|

1755

|

Lohn- und Gehaltsverrechnung

|

F

|

Diverses

|

Fragen

|

|

|

|

|

|

|

|

|

|

|

|

Klasse: 2

|

|

|

|

2100

|

Zinsen und ähnl. Aufwendungen

|

F

|

|

Fragen

|

|

|

|

|

|

|

|

|

|

|

|

Klasse: 3

|

|

|

|

3000

|

Roh-, Hilfs- und Betriebsstoffe

|

WKF

|

|

Fragen

|

|

19,00

|

90

|

3100

|

Fremdleistungen

|

WKF

|

|

Fragen

|

|

19,00

|

90

|

3120

|

Bauleistungen n. §13b 19% VST/UST

|

WKF

|

|

Ausgang

|

|

|

|

3122

|

Bauleistungen n. §13b 16% VST/UST

|

WKF

|

|

Ausgang

|

|

|

|

3151

|

§13b erhaltene Skonti

|

|

|

|

|

|

|

3300

|

7% Wareneingang

|

WKF

|

|

Ausgang

|

|

7,00

|

|

3340

|

16% Wareneingang ab 2007

|

WKF

|

|

Ausgang

|

|

16,00

|

|

3340

|

19% Wareneingang

|

WKF

|

|

Ausgang

|

|

19,00

|

|

3410

|

19% Wareneingang mit Steuerschlüssel

|

WKF

|

|

Ausgang

|

|

19,00

|

90

|

3720

|

Nachlässe 19% Vorsteuer

|

WKF

|

|

Fragen

|

|

19,00

|

|

3730

|

Erhaltene Skonti ohne VSt

|

|

|

Fragen

|

|

|

|

3731

|

7% erhaltene Skonti

|

|

|

|

|

7,00

|

|

3735

|

16% erhaltene Skonti

|

|

|

|

|

16,00

|

|

3736

|

19% erhaltene Skonti

|

|

|

|

|

19,00

|

|

|

|

|

|

|

|

|

|

Klasse: 4

|

|

|

|

4100

|

Löhne und Gehälter

|

WKF

|

|

Ausgang

|

|

|

|

4110

|

Löhne

|

WKF

|

|

Ausgang

|

|

|

|

4120

|

Gehälter

|

WKF

|

|

Ausgang

|

|

|

|

4130

|

gesetzliche soziale Aufwendungen

|

WKF

|

|

Ausgang

|

|

|

|

4138

|

Beiträge zur Berufsgenossenschaft

|

WKF

|

|

Ausgang

|

|

|

|

4140

|

freiw. sozi. Aufwendung, lohnsteuerfrei

|

WKF

|

|

Ausgang

|

|

|

|

4141

|

19% VSt freiw. sozi. Aufwendungen

|

WKF

|

|

Ausgang

|

|

19,00

|

90

W=Warenkonto E=Erlöskonto K=Kassenbuch S=Skonto A=Ausbuchung F=FIBU-Erfassung

|

|

|

|

|

|

Steuer

|

Kto.-Nr.

|

Beschreibung

|

Verwendung

|

Gruppe

|

Art

|

Konto

|

Satz

|

Schlüssel

|

4170

|

vermögenswirksame Leistungen

|

WKF

|

|

Ausgang

|

|

|

|

4175

|

Fahrtkostenerst. Wohnung/Arbeitsstätte

|

WKF

|

|

Ausgang

|

|

|

|

4190

|

Aushilfslöhne

|

WKF

|

|

Ausgang

|

|

|

|

4199

|

Lohnsteuer für Aushilfen

|

WKF

|

|

Ausgang

|

|

|

|

4210

|

Miete

|

WKF

|

|

Ausgang

|

|

|

|

4220

|

Pacht

|

WKF

|

|

Ausgang

|

|

|

|

4230

|

Heizung

|

WKF

|

|

Ausgang

|

|

19,00

|

90

|

4240

|

Gas, Strom, Wasser (Verwaltung-Vertrieb

|

WKF

|

|

Ausgang

|

|

19,00

|

90

|

4250

|

Reinigung

|

WKF

|

|

Ausgang

|

|

19,00

|

90

|

4260

|

Instandhaltung betrieblicher Räume

|

WKF

|

|

Ausgang

|

|

19,00

|

90

|

4320

|

Gewerbesteuer

|

WF

|

|

Ausgang

|

|

|

|

4360

|

Versicherungen

|

WF

|

|

Ausgang

|

|

|

|

4510

|

Kfz-Steuer

|

WKF

|

|

Ausgang

|

|

|

|

4520

|

Kfz-Versicherung

|

WKF

|

|

Ausgang

|

|

|

|

4530

|

laufende Kfz-Betriebskosten

|

WKF

|

|

Ausgang

|

|

19,00

|

90

|

4540

|

Kfz-Reparaturen

|

WKF

|

|

Ausgang

|

|

19,00

|

90

|

4570

|

Fremdfahrzeuge

|

WKF

|

|

Ausgang

|

|

19,00

|

90

|

4600

|

Werbe- und Reisekosten

|

WKF

|

|

Ausgang

|

|

19,00

|

90

|

4610

|

Werbekosten

|

WKF

|

|

Ausgang

|

|

19,00

|

90

|

4630

|

Geschenke bis 35 € 19% abzugsfähig

|

WKF

|

|

Ausgang

|

|

19,00

|

90

|

4635

|

Geschenke ü.35 € 19%nicht abzugsfähig

|

WKF

|

|

Ausgang

|

|

19,00

|

90

|

4650

|

Bewirtungskosten

|

WKF

|

|

Ausgang

|

|

19,00

|

90

|

4660

|

Reisekosten Arbeitnehmer

|

WKF

|

|

Ausgang

|

|

19,00

|

90

|

4760

|

Verkaufsprovision

|

WKF

|

|

Ausgang

|

|

19,00

|

90

|

4780

|

Fremdarbeiten

|

WKF

|

|

Ausgang

|

|

19,00

|

90

|

4790

|

Aufwand für Gewährleistungen

|

WKF

|

|

Ausgang

|

|

19,00

|

90

|

4910

|

Porto

|

WKF

|

|

Ausgang

|

|

|

|

4920

|

Telefon

|

WKF

|

|

Ausgang

|

|

19,00

|

90

|

4930

|

Bürobedarf

|

WKF

|

|

Ausgang

|

|

19,00

|

90

|

4940

|

Zeitschriften, Bücher 7%

|

WKF

|

|

Ausgang

|

|

7,00

|

90

|

4950

|

Rechts- und Beratungskosten

|

WKF

|

|

Ausgang

|

|

19,00

|

90

|

4955

|

Buchführungskosten

|

WKF

|

|

Ausgang

|

|

19,00

|

90

|

4980

|

Betriebsbedarf 19% mit Steuerschlüssel

|

WKF

|

|

Ausgang

|

|

19,00

|

90

|

4981

|

Kosten 2007 16% mit Steuerschlüssel

|

WKF

|

|

Ausgang

|

|

16,00

|

70

|

|

|

|

|

|

|

|

|

Klasse: 8

|

|

|

|

8000

|

Erlöse ohne Steuer

|

|

|

Eingang

|

|

|

|

8300

|

7% Erlöse Sonstige

|

K

|

|

Eingang

|

|

7,00

|

|

8337

|

Erlöse nach §13b UStG

|

E

|

|

Eingang

|

|

|

|

8340

|

16% Erlöse ab 2007

|

E

|

|

Eingang

|

|

16,00

|

|

8400

|

Erlöse 19%

|

E

|

|

Eingang

|

|

19,00

|

|

8410

|

Erlöse Kundendienst 19%

|

E

|

|

Eingang

|

|

19,00

|

30

|

8420

|

Erlöse Sonstige 19%

|

EF

|

|

Eingang

|

|

19,00

|

30

|

8650

|

Erlöse Zinsen u. Mahngebühren

|

A

|

|

Eingang

|

|

|

|

8720

|

Erlösschmälerung 19% USt

|

A

|

|

|

|

19,00

|

|

8723

|

Erlösschmälerung 16% USt

|

A

|

|

|

|

16,00

|

|

8730

|

gewährte Skonti o. USt

|

S

|

|

Ausgang

|

|

|

|

8735

|

16% gewährte Skonti

|

S

|

|

|

|

16,00

|

|

8736

|

19% gewährte Skonti

|

S

|

|

|

|

19,00

|

|

|

|

|

|

|

|

|

|

Klasse: 9

|

|

|

|

9000

|

Saldenvorträge

|

KF

|

Diverses

|

Eingang

|

|

|

W=Warenkonto E=Erlöskonto K=Kassenbuch S=Skonto A=Ausbuchung F=FIBU-Erfassung
