# Adressen Karteikarte 4 ‚Bankdaten’

Pfad: Adressverwaltung > Adressen [5] > 1. Stammdaten > Adressen Karteikarte 4 ‚Bankdaten’
Quelle: handbuch/adressen_karteikarte_4__bankdaten__.htm

|

Adressen Karteikarte 4 ‚Bankdaten’

[Bild: Adressen Karteikarte 4 ‚Bankdaten’ ]

Punkt 1 – 4

Diese Daten werden benötigt, wenn die Eingangsrechnungen per Diskette, per Überweisungszettel oder per Online-Banking bezahlt werden sollen. Auch bei der Übergabe an ein Finanzbuchhaltungsprogramm werden diese Werte ggf. verwendet.

|
[Bild: 1]

BLZ / Konto

[Bild: 1. BLZ / Konto]

Tragen Sie hier die BLZ und die Konto-Nr. der Bank ein.

Hinweis: Wenn Sie den Banknamen nicht eintragen, sondern nur die BLZ und diese mit Enter bestätigen, wird das Feld Bankname automatisch gefüllt.

|
[Bild: 2]

Bankname

[Bild: 2. Bankname]

Tragen Sie hier den Namen der Bank ein, an die eine Zahlung überwiesen werden soll.

|
[Bild: 3]

IBAN

[Bild: 3. IBAN]

IBAN ist die neue internationale Kontonummer und steht für International Bank Account Number.

Die IBAN setzt sich zusammen aus:

- einem Landeskennzeichen,

- der Bankleitzahl,

- der Kontonummer und

- einer Prüfziffer

Sie kann daher aus Kontonummer und Bankleitzahl berechnet werden. Standardmäßig wird für das hinterlegte Landeskennzeichen des eigenen Landes benutzt (Modul Einstellungen unter dem Menüpunkt <Grundeinstellungen> <Firmendaten>).

Hinweis: Wenn die IBAN fehlerhaft ermittelt wird, setzen Sie bitte im Modul Einstellungen unter dem Menüpunkt <Grundeinstellungen> <Firmendaten> das eigene Land bei ‚Adressen ohne Länderkennzeichen sind aus - Deutschland -‘

|
[Bild: 4]

BIC

[Bild: 4. BIC]

Die BIC ist die Bankleitzahl für den internationalen Zahlungsverkehr.

BIC steht für Bank Identification Code. Statt BIC wird öfters auch fälschlicherweise das Wort SWIFT benutzt. Swift ist aber die Abkürzung für ein internationales Bankenabkommen, auf dem jedoch die BIC Nummern definiert wurden.

Leider kann die BIC nicht immer direkt aus der BLZ abgeleitet werden. So gibt es für identische BLZ diverse BIC (z.B. filialabhängig), oder mehrere BLZ bekommen eine BIC usw. Außerdem werden durch Bankenfusionen diese Nummern ständig geändert. Die im Programm hinterlegte Zuordnungstabelle stammt von der Bundesbank, muss aber nicht aktuell sein. Zum Aktualisieren wählen Sie bitte im Modul EINSTELLUNGEN den Menüpunkt <Programmbereiche> <Eingangsrechnungen> <Bankdaten>. Wählen Sie dort den Menüpunkt <Datei> <Import akt. BLZ Liste>.

Am besten vergleichen Sie aber immer die BIC mit den Informationen, die Sie von Ihrem Lieferanten / Ihrem Kunden / Ihrer Bank erhalten haben.

Hinweis: Beim Bezahlen der offenen Rechnungen im Rechnungseingangsbuch können Sie festlegen, ob Sie mit BLZ/Konto oder BIC/IBAN überweisen möchten.

|
[Bild: 5]

Zahlungsziele

[Bild: 5. Zahlungsziele]

Die Erfassung ist bei Nutzung des Rechnungseingangsbuches mit Zahlungsabwicklung erforderlich.

Erfassen Sie die Daten aufsteigend, also bei Zahlungsziel 1 die Anzahl der Tage bis zum größten Skontoabzug.

Die weiteren Zahlungsziele in Tagen müssen größer als als das vorige sein. Eine Ausnahme ist die Anzahl 0. Wenn alle weiteren Zahlungsziele auf 0 gesetzt werden, wird dies akzeptiert.

|

Besondere Zahlungsbedingungen:

Um auch mit Zahlungszielen wie "immer am 15. des Folgemonats" arbeiten zu können, hat Label zu einem kleinen Trick gegriffen. Da davon auszugehen ist, dass keine Zahlungsziele von über 700 Tage vorkommen, wird mit Zahlen ab 700 die Zahlungsweise an bestimmten Tagen geregelt. Wenn die Zahl der Tage über 700 liegt, ist der aktuelle Monat, bei über 800 der Folgemonat und bei über 900 der übernächste Monat festgelegt. Die nächste Zahl dient der Festlegung des Tages.

[Bild]

Beispiele:

715 bedeutet den 15. Tag des aktuellen Monats

810 den 10. des Folgemonats

912 den 12. des übernächsten Monats

Sollte bei einem Wert mit dem aktuellen Monat der Tag bereits vorüber sein, wird automatisch auf den nächsten Monat umgeschaltet.

Beispiel:

Am 16.10.2018 eine Rechnung für einen Lieferanten mit Zahlungsziel 714 zu erfassen bewirkt die Vorgabe des 14.11.2018 als Zahlungsziel.

Hinweis: Wenn bei einer Eingabe von 731 oder 831 oder 931 der entsprechende Monat keinen 31. hat, wird automatisch auf das zuvor gültige Datum zurückgestellt.

Weitere (selten benötigte) Variante:

Mit einem Eintrag von 3015 wird erreicht, dass alle Rechnungen mit Datum vor dem 15ten am 30ten bezahlt werden müssen. Alles nach dem 15ten bis einschließlich 30ten wird am 15ten des Folgemonats gezahlt. Nach dieser Logik kommen also Zahlungsfristen zwischen 15 und 30 Tagen zum Einsatz. Falls das jemand braucht – auch mit 2814 würde das funktionieren.

Da man sich so etwas kaum merken kann, bekommen Sie diese Info auch über den kleinen Hilfeknopf hinter dem 1. Zahlungsziel.

|
[Bild: 6]

Rg. ohne MwSt

[Bild: 6. Rg. ohne MwSt]

Wenn Sie von einem Lieferanten (z.B. Post) generell Rechnungen ohne MwSt. erhalten, setzen Sie bitte hier ein Kreuz. Beim Einbuchen der Eingangsrechnung wird Ihnen dann keine Mehrwertsteuer vorgeschlagen.

|
[Bild: 7]

Bankeinzug

[Bild: 7. Bankeinzug]

Bei Lieferanten, denen Bankeinzug gewährt wird, werden über diesen Schalter die Überweisungen mit dem Rechnungseingangsbuch verhindert.

|
[Bild: 8]

Rg-Adresse

[Bild: 8. Rg-Adresse]

Es gibt mindestens einen Einkaufsverband, der die Rechnungsstellung mit seinen Mitgliedern abwickelt, obwohl die Ware direkt beim Hersteller bestellt wird. Deshalb kann man in der Maske der Verteilung auf die Projekte eine Herstelleradresse eingeben. Die Hersteller haben ggf. unterschiedliche Zahlungsziele und Skontobedingungen. Die Zahlungsbedingung aus der Rechnungsadresse (also dem Einkaufsverband) ist dann oft falsch.

Die Zahlungsbedingungen des Herstellers können nun verwendet werden, wenn Sie bei der Adresse des Herstellers im Feld Rg.-Adresse die Rechnungsanschrift des Einkaufsverbandes hinterlegen. Betätigen Sie den Knopf ‚Suchen’ und ordnen die Adresse der Rechnungsanschrift zu.

|
[Bild: 9]

Eigene Kunden-Nr.

[Bild: 9. Eigene Kunden-Nr.]

Wenn Sie hier Ihre Kunden-Nr. eintragen, die Sie von Ihrem Lieferanten erhalten haben, wird diese beim Ausdruck einer Zahlungsankündigung mit ausgedruckt.

|
[Bild: 10]

Scan-Profil

[Bild: 10. Scan-Profil]

Wenn Sie über das Zusatzmodul Scan-Archiv oder ELO verfügen, können Sie hier ein Scan-Profil eintragen – Beispiel: Ihr Lieferant hat besonders dünnes Papier für die Rechnungen und Sie haben dafür ein spezielles Scan-Profil erstellt. Beim Einscannen der Eingangsrechnung wird dann das entsprechende Scan-Profil angesprochen und die Rechnung wird problemlos gescannt.

|
[Bild: 11]

Vorgabe Warenkonto

[Bild: 11. Vorgabe Warenkonto]

Geben Sie hier das Warenkonto ein, dass beim Einbuchen der Eingangsrechnung vorgeschlagen werden soll. Des Weiteren können Sie zum Warenkonto die entsprechende Kostenart auswählen. Wenn Sie hier nichts eintragen, wird wie bisher ‚Material’ vorgeschlagen.

|
[Bild: 12]

Projektvorgabe

[Bild: 12. Projektvorgabe]

Es gibt Eingangsrechnungen von bestimmten Lieferanten, die immer auf das gleiche Projekt gebucht werden müssen. Als Beispiel könnte man Berufsbekleidung, Versicherungen usw. nennen. Deshalb kann man hier ein Projekt vorgeben. Bei der Erfassung der Verteilung / Zuordnung der Eingangsrechnung wird dann das Projekt passend vorgeschlagen.

|
[Bild: 13]

Offene Posten gesamt

[Bild: 13. Offene Posten gesamt]

In diesem Feld wird die Summe aller offenen Beträge im Rechnungsausgangsbuch angezeigt.

|
[Bild: 14]

Offene Posten überfällig

[Bild: 14. Offene Posten überfällig]

In diesem Feld werden die offenen Rechnungsbeiträge angezeigt, bei denen das Zahlungsziel überschritten wurde.

|
[Bild: 15]

Mahnfaktor und Zahlungsmoral

[Bild: 15. Mahnfaktor und Zahlungsmoral]

In der Adressmaske und im Kundendienst werden Zahlen über einen Mahnfaktor und die Zahlungsmoral angezeigt. Diese Werte werden per Durchlauf im Rechnungsausgangsbuch in die Adressen eingetragen. Wählen Sie dort den Menüpunkt <Bearbeiten> <Zahlungsmoral ermitteln>. Mit der Datumsangabe legen Sie fest, ab wann die Bewertungsfaktoren gebildet werden sollen.

Es gibt Rechnungen, die man in die Bewertung nicht einbeziehen sollte, weil sie das Bild verfälschen. Dies ist immer dann der Fall, wenn mit Sicherheitseinbehalten oder Ratenzahlungen gearbeitet wird. Es gibt deshalb in der Maske der Rechnungsanzeige im Rechnungsausgangsbuch eine Auswahlcombo, in der Sie festlegen, ob es sich um eine ‚normale Rechnung’, um ‚Sicherheitseinbehalt’ oder ‚Ratenzahlung’ handelt. Nur die ‚normalen’ Rechnungen werden in die Statistik einbezogen.

Ähnliches gilt für die Zahlungsmoral. Wenn Sie eine einzelne Zahlung nicht in die Bewertung einfließen lassen wollen, so können Sie in der Zahlungsmaske einen Haken bei ‚für Zahlungsmoral nicht nutzen’ setzen. Dies ist z.B. sinnvoll, wenn Sie selbst die späte Zahlung verursacht haben, weil Sie zwar die Rechnung gestellt, aber Reklamationen nicht rechtzeitig geregelt haben.

Genauere Information über die Grundlage der Zahl findet sich in der OP-Anzeige im Kundendienst und in der Adresse. Dort kann der Wert auch aktualisiert werden.

Berechnung:

Mahnfaktor = Summe Mahnungen Stufe 1

+ Summe Mahnungen Stufe 2 * 2

+ Summe Mahnungen Stufe 3 * 3

+ Summe Mahnungen Stufe 4 * 4

geteilt durch die Anzahl der berücksichtigten Rechnungen * 100

Ein Faktor von 100 bedeutet also, dass durchschnittlich jede Rechnung die Mahnstufe 1erreicht hat. Durch die Sache mit Stufe 2 * 2 wird erreicht, dass die höhere Mahnstufe verstärkt in den Mahnfaktor greift. Je höher die Mahnstufe desto stärker der Einfluss auf den Mahnfaktor.

Zahlungsmoral in Tagen:

( Addition aller (Tage zwischen Druckdatum und Zahlungsdatum) * gezahlte Summe ) / (Addition aller Rechnungssummen)

Beispiel: Rechnung 1000 €

Zahlung 1 nach 10 Tagen mit 600 € 6000

Zahlung 2 nach 20 Tagen mit 400 € 8000

= 14000 geteilt durch 1000 € ergibt 14 Tage Zahlungsmoral

|
[Bild: 16]

Kredit-Limit

[Bild: 16. Kredit-Limit]

Bei eingetragenen Werten kommt bei der Anlage eines neuen Dokumentes und der Anlage eines neuen Kundendienstauftrages eventuell ein Hinweis auf Überschreitung. Der Vergleich wird mit den offenen Posten des Rechnungsausgangsbuches vorgenommen.

|
[Bild: 17]

USt-Ident-Nr.

[Bild: 17. USt-Ident-Nr.]

Hier kann für Auslandsadressen und für Adressen, für die Sie eine Gutschrift erstellen, die Umsatzsteuer-Ident-Nr. eingesetzt werden. Zur automatischen Übertragung muss das Schlüsselwort @TXustidentnr@ in der Vorbemerkung oder in der Zahlungsbedingung eingesetzt werden.

|
[Bild: 18]

Steuernummer

[Bild: 18. Steuernummer]

In diesem Feld können Sie Ihre Steuernr. hinterlegen.

|
[Bild: 19]

OP nicht zeigen

[Bild: 19. OP nicht zeigen]

Wenn bei einer Adresse dieses Feld angekreuzt ist, wird die offene Postensumme im Kundendienst und LabelCRM nicht angezeigt. Dies ist für Großkunden vorgesehen, damit die Mitarbeiter nicht über die Summen nachdenken müssen. Ein gesetztes Kreditlimit greift unabhängig von diesem Schalter.

|
[Bild: 20]

Abrechnung ohne MwSt

[Bild: 20. Abrechnung ohne MwSt]

Mit einer Gesetzesänderung zum 01.04.2004 hat uns der Gesetzgeber den Umstand beschert, dass Rechnungen an Unternehmer, die selbst Bauleistungen verkaufen, ohne Mehrwertsteuer sein müssen. Ausgenommen sind davon reine Materiallieferungen, kleine Wartungen (wo immer hier die Grenze sein mag) und Rechnungen bis 500,00 €. Leider tritt das Problem auf, dass Sie bei Rechnungen unter 500,00 € ein Erlöskonto mit MwSt. wählen müssen und bei Rechnungen über 500,00 € eines ohne MwSt. Zwar haben wir deshalb in die Druckmaske auch die Auswahl der Erlöskonten vorgenommen, dennoch muss man noch manuell umschalten. Deshalb können Sie im Kontenplan (Modul EINSTELLUNGEN unter dem Menüpunkt <Grundeinstellungen> <Kontenplan>) ein ‚Parallelkonto’ festlegen. Wenn Sie beim Drucken ein Erlöskonto mit MwSt. gewählt haben und nach dem Gesetz eines ohne MwSt. zum Tragen kommen würde, schaltet das Programm auf das Parallelkonto um. Die Zuordnung von Parallelkonten ist also nicht zwingend erforderlich, aber es vereinfacht das Leben.

Für unsere ausländischen Kunden, die diese unsinnige 500,00 Euro-Regel nicht trifft, gibt es einen Schalter im Modul EINSTELLUNGEN unter dem Menüpunkt <Grundeinstellungen> <Allgemein>, mit dem die Prüfung weggeschaltet werden kann.

Wenn Sie nun hier ein Kreuz setzen, wird standardmäßig bei der Neuanlage eines Dokumentes keine Mehrwertsteuer ausgewiesen.

In der Zahlungsbedingung sollten Sie dem Rechnungsempfänger unbedingt mitteilen, dass er für die Abführung der Mehrwertsteuer selbst verantwortlich ist. Über entsprechende Schlüsselworte können Sie die von ihm zu zahlende Mehrwertsteuersumme automatisch errechnen lassen. Bei der Erfassung der Zahlungsbedingungen (Modul EINSTELLUNGEN unter dem Menüpunkt <Grundeinstellungen> <Zahlungsbedingungen>) finden Sie Muster-Zahlungsbedingungen, die Sie über die Zwischenablage kopieren können.

|
[Bild: 21]

Bankeinzug (Lastschrift)

[Bild: 21. Bankeinzug (Lastschrift)]

Setzen Sie hier ein Häkchen, wenn Sie mit Ihrem Kunden Bankeinzug vereinbart haben. Tragen Sie in diesem Fall auch die SEPA Mandatsnummer und das SEPA Mandatsdatum ein.

Hintergrund: Für das Bankeinzugsverfahren nach SEPA Richtlinien (in Deutschland zwingend vorgeschrieben ab Februar 2014) müssen Sie jedem Kunden eine eindeutige Mandatsnummer geben und das Datum hinterlegen, an dem der Kunde die Einzugsberechtigung unterschrieben hat. Dieses Datum darf weder in der Zukunft noch vor dem 09.07.2012 liegen.

Zusammen mit dem Bankeinzug wird dem Zahlungspflichtigen Ihre Gläubiger ID und die in Ihrem Betrieb einmalig vergebene Mandatsnummer, sowie das Mandatsdatum (Datum der Kunden-Unterschrift auf der Einzugsberechtigung) übermittelt. So kann er feststellen, ob Sie dazu berechtigt waren.

Mehr Informationen zum Ablauf finden im LabelWiki unter "SEPA-Lastschriften".

|
[Bild: 22]

Vorgabe Mahnart

[Bild: 22. Vorgabe Mahnart]

Hier kann festgelegt werden, ob die aktive Adresse normal gemahnt werden soll oder nicht. Wir wollen damit erreichen, dass Sie die vorgeschlagenen Mahnungen einfach ausdrucken können, ohne über jede Rechnung nachdenken zu müssen. Bei Großkunden, die nicht gemahnt werden sollen, setzt man einfach auf ‚Nicht mahnen‘ und bei lieben Kunden, die man dezent erinnern möchte auf ‚Anrufen‘. Im Mahnwesen können aufgrund der überfälligen Rechnungen Listen der anzurufenden Kunden und nicht zu mahnenden Kunden erzeugt werden. Die hier getroffene Festlegung wird beim Druck einer Rechnung vorgeschlagen und kann dort ggf. auch nur für eine Rechnung umgesetzt werden. Diese Einstellung hat nichts mit der Anzeige der offenen und überfälligen Rechnungen zu tun – es geht nur um das Mahnwesen.

|
[Bild: 23]

Zinssatz Mahnen

[Bild: 23. Zinssatz Mahnen]

Hier können Sie festlegen, ob die bei einer Mahnung anfallenden Mahngebühren mit dem Zinssatz für Privat-Kunden (Zinssatz 1) oder für Geschäftskunden (Zinssatz 2) ermittelt werden sollen. Die beiden Zinssätze werden direkt im Mahnprogramm hinterlegt. Details finden Sie im Kapitel Mahnen.
