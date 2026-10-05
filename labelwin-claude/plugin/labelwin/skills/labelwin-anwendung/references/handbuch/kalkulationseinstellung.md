# Kalkulationseinstellung

Pfad: Dokumentenbearbeitung > Dokumentenerstellung [3] > Kalkulationseinstellung
Quelle: handbuch/kalkulationseinstellung.htm

|

Kalkulationseinstellung

Unter dem Menüpunkt [Optionen - Kalkulationseinstellung] oder über die Funktionstaste F11 erreichen Sie im Artikelaufruf die Einstellungen für das derzeit aktive Dokument.

|

Tipp: Das Thema "Artikelkalkulation und Preisfindung" haben wir in einem Tutorial Video zusammengefasst. Sie können es im Unterkapitel Tutorial Artikelkalkulation betrachten.

Sie ändern eine Kalkulationseinstellung, indem Sie einfach an der entsprechenden Werte ändern und die Maske mit Okay verlassen. Statt der Änderung können Sie auch in der Liste "Einstellungen" [Nr.2] einfach eine andere hinterlegte Kalkulationseinstellung wählen.

Bei der Erstellung von Dokumenten mit Artikeln wie Angebote, Rechnungen, LV, Bestellungen usw. werden die aufgerufenen Artikel zwangsläufig kalkuliert, Um nicht bei jeder Neuanlage von solchen Dokumenten alle Kalkulationsfaktoren einzeln festzulegen, hat Label Kalkulationseinstellungen eingeführt. Dabei werden alle Einstellungen vorgenommen und unter einem Arbeitsnamen abgespeichert. Es werden üblicherweise solche Einstellungen wie “Brutto“, „Einkauf x 1,25“, „Thekenverkauf“ usw. eingerichtet. Bei der Neuanlage von Dokumenten wird nun einfach eine Einstellung über den Namen gewählt. Zusätzlich kann bei der Kundenadresse eine solche Einstellung hinterlegt werden, so dass bei der Dokumentenanlage nach der Adresswahl diese Einstellung vorgeschlagen wird. Kalkulationseinstellungen werden im Modul EINSTELLUNGEN im Bereich [Grundeinstellungen - Kalk.Einstellungen] verwaltet.

Hinweis: Eine Änderung in der Einstellung wirkt nur auf die anschließend aufgerufenen Artikel. Bereits erfasste Artikel können Sie über die Funktion Kalkulation ändern oder den Durchlauf "Preis-Update" an die geänderten Kalkulationseinstellungen anpassen.

[Bild: Kalkulationseinstellung]

Bild: Grundeinstellungen Kalkulationseinstellungen

Bevor wir die einzelnen Elemente einer Kalkulationseinstellung beschreiben, wollen wir auf die Logik der Preisermittlung eingehen. Die Ausführungen finden Sie im Unterkapitel Hierarchie bei der VK Ermittlung.

Noch einmal zur Erinnerung: Die Einstellung wirkt nur auf die anschließend aufgerufenen Artikel. Wenn Sie die bereits vorhandenen Artikel ändern wollen, geschieht dies über den Menüpunkt <Optionen> <Kalkulation ändern>.

|
[Bild: 1]

Menüleiste

[Bild: 1. Menüleiste]

Die Menüpunkte im Einzelnen:

Neu

Durch Anwahl dieses Menüpunktes wird eine neue Kalkulationsbasis angelegt. Häufig ist es sinnvoller, eine vorhandene Basis über ‚Speichern als’ zu kopieren und dann anzupassen.

Speichern

Durch Anwahl dieses Menüpunktes wird die aktuelle Kalkulationseinstellung gespeichert.

Speichern als neu (F3)

Durch Anwahl dieses Menüpunktes wird die aktuelle Kalkulationseinstellung unter einem anderen Namen gespeichert.

Löschen

Durch die Anwahl dieses Menüpunktes wird die aktuelle Kalkulationseinstellung gelöscht. Da eine Kalkulationseinstellung ggf. bei vielen Adressen hinterlegt ist, sollten Sie hier vorsichtig sein.

Del-Notiz eintragen

Hier können Sie die aktuell festgelegte Del-Notiz für ALLE Kalkulationseinstellungen eintragen lassen.

Lohnselbstkosten eintragen

Hier können Sie die aktuell festgelegten Lohnselbstkosten für ALLE Kalkulationseinstellungen eintragen lassen.

Beenden

Hiermit beenden Sie die Kalkulationseinstellung.

|
[Bild: 2]

Kalkulationsschema

[Bild: 2. Kalkulationsschema]

Hier wird die zu verändernde Einstellung gewählt.

|
[Bild: 3]

Posistionsnr. Schema

[Bild: 3. Posistionsnr. Schema]

Die haben die Möglichkeit die Positions-Nr. nach Ihren Wünschen zu gliedern. Dazu werden folgende Buchstaben verwendet:

B für Bauteile

A für Bauabschnitte (Lose)

T für Titel

P für Positionen

Wenn das Dokument dann später umnummeriert wird, so wird die Positions-Nr. entsprechend Ihrem Gliederungsschema gebildet.

Beispiel: Gliederungsschema ist TT.PPP, d.h. in Ihrem Dokument dürfen sich max. 99 Titel be-finden und in jedem Titel max. 999 Positionen. Die Positions-Nr. lauten dann 1.1 für die erste Position im ersten Titel, 2.1 für die erste Position im 2. Titel usw.

Solange Sie das Gliederungsschema mit Großbuchstaben bilden, entfallen führende Nullen. Wenn Sie statt Großbuchstaben Kleinbuchstaben verwenden, so werden führende Nullen in jeder Gliede-rungsebene aufgefüllt.

Beispiel: tt.ppp die erste Positions-Nr. im ersten Titel lautet dann 01.001. Damit ist gewährleistet, dass alle Positions-Nr. die identische Länge besitzen. Der Trenner zwischen den einzelnen Gliede-rungsebenen ist in der Regel der Punkt.

|
[Bild: 4]

Schrittweite

[Bild: 4. Schrittweite]

Mit dem Feld ‚Schrittweite’ steuern Sie, in welchen Schritten die Positions-Nr. gebildet wird. Die Schrittweite bezieht sich immer auf den Bereich P in der Gliederung. Somit ist es möglich Ihr Dokument auch in 5er bzw. 10er Schritten zu nummerieren.

|
[Bild: 5]

Artikelschlusstext

[Bild: 5. Artikelschlusstext]

Es ist möglich, jeden Artikel mit einem Artikelschlusstext wie z.B. ‚liefern und montieren’, oder ‚nur liefern’ usw. zu versehen. Da der exakte Text über eine Auswahl erst beim Drucken festgelegt wird, legen Sie an dieser Stelle eigentlich nur die Kategorie fest. Hierdurch ist es möglich, dass die gleiche Position beim Druck als Angebot mit ‚liefern und montieren’ und beim Druck als Rechnung mit ‚geliefert und montiert’ versehen werden kann.

An dieser Stelle wählen Sie die Standardvorgabe, die Ihnen bei jedem Artikel vorgeschlagen wird. Beim Artikelaufruf können Sie diese Vorgabe dann für jede Position verändern.

Die Artikelschlusstexte werden in dem Programm EINSTELLUNGEN unter dem Menüpunkt ‚Pro-grammbereiche’, ‚Texterstellung’, ‚Artikelschlusstexte’ erfasst und geändert.

|
[Bild: 6]

Vorgabe Langform

[Bild: 6. Vorgabe Langform]

Mit diesem Feld bestimmen Sie, ob Ihr Artikeltext in der eventuell vorhandenen Langform ausgegeben werden soll. Diese Schaltfläche dient als Vorgabe für den Artikelaufruf. Für jede einzelne Position können Sie diese Vorgabe später ändern. Die Vorgabe ‚Langtext’ trifft dann aber auch nur für die Artikel zu, die eine Langform beinhalten. Sollte keine Langform vorhanden sein, so wird automatisch der Kurztext übernommen.

|
[Bild: 7]

Artikeltext erhalten

[Bild: 7. Artikeltext erhalten]

Hier haben Sie die Möglichkeit, schon in der Kalkulationseinstellung festzulegen, dass bei Gaeb-Ausschreibungen der Originaltext erhalten bleibt, selbst wenn man Artikel aus den Stammdaten zur Kalkulation aufruft. Wenn die Option über den alten Menüpunkt geschaltet wird, so wird dieses ebenfalls dauerhaft für das aktuelle Dokument gespeichert. Sie können dieses auch im Einstellmodul für die Kalkulationsvorgabe dauerhaft einstellen.

|
[Bild: 8]

Beispiel

[Bild: 8. Beispiel]

Nachdem Sie das Positions-Nummer Schema gewählt haben, wird Ihnen hier angezeigt, wie die Positions-Nummer im Dokument erscheint.

|
[Bild: 9]

Anfangs-Nr

[Bild: 9. Anfangs-Nr]

Hier können Sie vorgeben, mit welcher Positionsnummer Sie die fortlaufende Nummerierung starten möchten.

|
[Bild: 10]

Umnummerieren

[Bild: 10. Umnummerieren]

Mit dem Feld ‚Umnummerieren’ können Sie steuern, ob das Dokument später überhaupt umnummerierbar sein soll. Im Regelfall sollte ‚immer’ angekreuzt sein, weil es dann problemlos möglich ist, Positionen in Ihr Dokument einzufügen und später die Positions-Nr. neu zu bilden. Wenn das Feld ‚nie’ angekreuzt ist, so kann das Dokument nicht umnummeriert werden. Dies ist insbesondere dann wichtig, wenn Positions-Nr. von Hand erfasst werden (z.B. weil sie aus einem Fremd-LV übernommen werden) oder wenn später Referenzen auf diese Positions-Nr. gebildet werden (Mengenüberwachung). Bei Teilrechnungen sollte das Dokument auf nicht umnummerierbar gesetzt werden, damit die Bezüge auf die Positionen des Angebotes erhalten bleiben. Sie können jedoch auch ‚fragen’ ankreuzen. Wenn Sie dann ein Dokument verlassen, werden Sie gefragt, ob Sie umnummerieren möchten oder nicht. Bei ‚nur Setbestandteile’ wird nur innerhalb eines Sets umnummeriert.

|
[Bild: 11]

Preisbildung

[Bild: 11. Preisbildung]

Mit dieser Schaltfläche entscheiden Sie, welcher Preis aus den Artikelstammdaten zur Ermittlung Ihres Materialverkaufspreises herangezogen wird. Sie haben dazu die Wahl zwischen dem Listenpreis oder den Einkauf. Sollte kein Einkauf vorhanden sein, so wird in diesem Fall auch kein Materialverkauf ermittelt. Bei den Großhändlern, bei denen keine Einkaufspreise vorhanden sind, sollten Sie die Kalkulationseinstellung entsprechend auf Listenpreise, d.h. den Händlerbruttopreis schalten.

Die weitere Möglichkeit ist, automatisch den Artikel aus der Verknüpfung herauszusuchen, der den günstigsten Einkauf besitzt. Dabei muss darauf geachtet werden, dass die Einkaufspreise gepflegt sind. Alle Preise werden aus dem Artikel verwendet, der den günstigsten EK besitzt, zusätzlich kommen aus diesem Artikel die Artikelnummer sowie der Bestellhändler. Minuten und der Text kommen aus dem ursprünglich aufgerufenen Artikel. Wenn Sie mit EK2 kalkulieren, wird auch dieser bei der Berechnung berücksichtigt.

|
[Bild: 12]

Vorrang Festpreise

[Bild: 12. Vorrang Festpreise]

Sie haben in den Artikelstammdaten die Möglichkeit, außer dem Listenpreis und den beiden Einkaufspreisen weitere feste Verkaufspreise zu erfassen. Diesen Verkaufspreisen kann ein Vorrang gegenüber der normalen Zuschlagskalkulation eingeräumt werden. Über die Schaltfläche ‚Vorrang’ entscheiden Sie, welcher der Verkaufspreise einen eventuellen Vorrang genießt. Alle Artikel, bei denen dann kein entsprechender Verkaufspreis eingerichtet ist, werden mit den normalen Standardfaktoren kalkuliert. Dieses ist z. B. sinnvoll für Sicherheitsventile, die nicht mit Materialmulti 1,25 kalkuliert werden, sondern mit einen festen Preis von 19,20 erhalten.

|
[Bild: 13]

EK-Grundlage

[Bild: 13. EK-Grundlage]

Es besteht die Möglichkeit, in den Artikelstammdaten 2 Einkaufspreise zu verwalten. Der EK1 wird in der Regel vom Großhändler über die Datanorm belegt. Den EK2 können Sie verwenden, um Sondereinkaufspreise zu verwalten. Über die Schaltfläche ‚Einkaufspreis-Grundlage’ entscheiden Sie, welcher der beiden Einkaufspreise automatisch in die Artikelkalkulation eingefügt wird. Der Einkaufspreis wird auch dann eingefügt, wenn Sie über Listenpreise kalkulieren. Dadurch ist es möglich, auch bei einer Kalkulation über Listenpreis eine Kalkulationsauswertung und dementsprechend einen Materialertrag zu ermitteln.

Wenn Sie das Feld ‚günstigsten EK aus Verknüpfung‘ aktivieren, wird bei verknüpften Artikeln immer der günstigste EK eingesetzt.

Beispiel:

[Bild]

|
[Bild: 14]

Materialmulti

[Bild: 14. Materialmulti]

Über den Materialmulti bestimmen Sie, mit welchem Aufschlag Ihre Materialien berechnet werden sollen. Je nachdem, wie Sie die Preisbildung eingestellt haben, greift der Materialmulti auf den Einkaufspreis1, den Einkaufspreis2 oder den Listenpreis.

|
[Bild: 15]

Mindestmulti

[Bild: 15. Mindestmulti]

Über den Mindestaufschlag des Materials schalten Sie eine Warnung zu. Wenn der Mindestaufschlag unterschritten wird, d.h. wenn der Aufschlag auf den Materialeinkauf geringer ist als der Mindestmulti, so erhalten Sie ein großes Fenster als Warnung. Die Gefahr der Unterschreitung eines Mindestmultis ist häufig dann gegeben, wenn aufgrund von Listenpreisen kalkuliert wird. Dabei gibt es bei einzelnen Großhändlern immer wieder Artikel auf die Sie keinen oder einen sehr geringen Rabatt erhalten. Der Mindestzuschlag verhindert außerdem Tippfehler wie z.B. 300 statt 3000 €. Selbstverständlich können Sie Material zu jedem von Ihnen gewünschten Preis verkaufen. D.h. dieser Mindestzuschlag löst nur eine Warnung aus, verhindert dabei aber nicht, dass Sie mit einem zu geringen Multi kalkulieren können.

|
[Bild: 16]

mit Mindestmulti rechnen

[Bild: 16. mit Mindestmulti rechnen]

In der Kalkulationseinstellung kann nun festgelegt werden, dass mit dem Mindestmulti gerechnet wird, wenn er bei der eingestellten Kalkulation bei einem Artikel unterschritten wird. Es erfolgt dann also keine Warnung, dass der Mindestmulti unterschritten ist, sondern das Programm rechnet einfach mit Einkauf x Mindestmulti.

Falls ein Artikel einen Festpreis hat und dieser auf Vorrang steht, wird der Festpreis genommen.

Der Schalter kann in den abgespeicherten Einstellungen gesetzt werden oder individuell für das aktive Dokument.

Hintergrund: Ein Lieferant hatte ohne Vorankündigung die Listenpreise für einige Artikelgruppen radikal gesenkt und da unser Kunde (wie sicherlich noch viele) im Kundendienst mit Listenpreis arbeitet, waren diese Preise einfach zu niedrig. Mit der eventuellen Verwendung des Mindestmultis kann er die bisherige Methode beibehalten.

Exkurs: Viele Anwender arbeiten aus diesem Grund mit der Kleinteilefaktura. Dabei wird der Multi in Abhängigkeit vom Einkaufspreis festgelegt. Bei preiswerten viel Aufschlag und bei teuren Artikeln wenig Aufschlag. So arbeiten im Prinzip auch die Baumärkte.

|
[Bild: 17]

Datanormpreise ab

[Bild: 17. Datanormpreise ab]

Wenn Sie eine Preisänderung einspielen, so kann Ihr Lieferant laut Datanorm ein Datum für ‚Preise gültig ab’ übergeben. Labelwin verwaltet diese Preise in einem separaten Feld und nimmt je nach Datum den richtigen Einkaufspreis. In diesem Feld können Sie festlegen, welches Datum zur Preisfindung genommen werden soll. Beispiel: Ein Artikel kostet EK 100,00 € und soll ab 01.10. 105,00 € kosten. Wenn Sie am 15.09. in einem Dokument in der Kalkulationseinstellung als Preisdatum den 01.10. (oder später) einsetzen, wird schon mit dem Preis von 105,00 € kalkuliert.

|
[Bild: 18]

Gruppenrahmen Material

[Bild: 18. Gruppenrahmen Material]

Neben der oben beschriebenen einfachen Zuschlagskalkulation können unterschiedliche Artikelgruppen mit verschiedenen Zuschlagssätzen kalkuliert werden. Dazu müssen Kalkulationsgruppen wie z.B. KESS für Kessel, HK für Heizkörper oder auch 001 für eine bestimmte Materialgruppe definiert werden. Die Anlage der Gruppen findet im Programm EINSTELLUNGEN statt. Jeder Artikel, der über die Gruppenkalkulation kalkuliert werden soll, muss einer solchen Gruppe zugeordnet werden (geschieht im Programm KATALOG). Außerdem müssen die Kalkulationsmultis für die Gruppen festgelegt werden. Um beim obigen Beispiel zu bleiben, wird der Gruppe KESS (stellvertretend für Kessel) ein Multiplikator 1.2 zugeordnet. Dieser Faktor wird im Gruppenrahmen 1 eingetragen. Im Gruppenrahmen 2 wird als Multi 1.3 eingetragen usw. Bis zu 99 Gruppenrahmen sind möglich.

An dieser Stelle in der Kalkulationseinstellung legen Sie fest, mit welchem Gruppenrahmen Sie arbeiten möchten.

Bei der Eingabe von 0 ist die Gruppenkalkulation ausgeschaltet, bei 1 wird bei Artikeln der Gruppe KESS mit 1.2, bei 2 mit 1.3 usw. gerechnet.

Lesen Sie hierzu im Kapitel Kalkulationsgruppen - Material nach.

Sie haben außerdem die Möglichkeit, für jede Materialgruppe festzulegen, ob sich der Faktor auf den Listen- oder Nettopreis auswirken soll. Im Modul EINSTELLUNGEN <Grundeinstellungen> <Kalkulationsgruppen> <bearbeiten Material> können Sie für jede einzelne Materialgruppe festlegen, ob der Preis

- wie bisher aufgrund der Kalkulationseinstellung oder

- aufgrund des Listenpreises oder

- aufgrund des Nettopreises

gebildet werden soll.

|
[Bild: 19]

Kleinteile / Handelsspanne

[Bild: 19. Kleinteile / Handelsspanne]

Bei eingeschalteter Kleinteilefakturierung oder Handelsspanne kann der Multiplikator in Abhängigkeit vom Preis oder der Handelsspanne festgelegt werden. Zu Details lesen Sie am Anfang dieses Kapitels über die Kalkulation und im Kapitel Kalkulationsgruppen - Kleinteilefaktura über die Einrichtung nach.

|
[Bild: 20]

Lohnkalkulation

[Bild: 20. Lohnkalkulation]

Wenn Sie beim Artikel hinterlegte Kalkulations-zeiten für die Lohnermittlung nehmen möchten, so müssen Sie hier das Feld der Minuten festlegen. Je Artikel sind 2 verschiedene Minutensätze zuzuordnen. Die als Fremdminuten bezeichneten Werte gelangen in der Regel über eine Diskette vom Großhändler in Ihren Rechner, die anderen vergeben Sie selbst. Wenn die Einstellung auf ‚Eigene’ steht und dort kein Wert hinterlegt ist, nimmt das Programm automatisch die ‚Fremdminuten’. Sollten Sie jedoch ‚Eigene Min (immer)’ gewählt haben, wird kein Wert übernommen, auch wenn bei ‚Fremdminuten’ etwas hinterlegt ist.

|
[Bild: 21]

Zeitmulti

[Bild: 21. Zeitmulti]

Sie können jeden Artikel in den Artikelstammdaten mit einer Zeit versehen.

Beispiel: Einen Heizkörper komplett montieren, demontieren für Malerzwecke und wieder montieren dauert 180 Minuten. Diese Zeit gilt für eine ‚normale Baustelle’. Weil jede Baustelle einen unterschiedlichen Erschwernisgrad besitzt, muss diese Zeit nicht für jede Baustelle identisch sein. Sie haben über den Zeitmulti die Möglichkeit die hinterlegten Zeiten zu verlängern (Multi größer als 1) oder zu verkürzen (Multi kleiner als 1). Dadurch brauchen Sie sich nicht bei jeder einzelnen Position Gedanken über die Zeit machen. Wenn Sie den Zeitmulti auf 0 setzen, so rechnen Sie ohne die hinterlegten Zeiten (z.B. bei einer Kundendienstrechnung, in der die Zeit als Montagestunde berechnet wird).

|
[Bild: 22]

Selbstkosten

[Bild: 22. Selbstkosten]

Mit den Selbstkosten je Stunde geben Sie an, wie hoch Ihre Kosten pro Monteurstunde sind. In den Selbstkosten sollten enthalten sein der Monteurlohn, die Sozialbeiträge, ein Zuschlag für Unproduktivität sowie die Kosten für Urlaub und Krankheit. Durch Eingabe dieses Wertes ist es Ihnen später möglich, einen Ertrag auch für die Lohnseite zu ermitteln.

|
[Bild: 23]

Verrechnungssatz

[Bild: 23. Verrechnungssatz]

Als Verrechnungssatz geben Sie bitte Ihren Stundenverrechnungssatz ein. Die Differenz zwischen den Selbstkosten und dem Verrechnungssatz wird Ihnen dann später als Lohnertrag in der Kalkulationsauswertung ausgewiesen. Beide Kostensätze können allerdings nur dann greifen, wenn Sie mit Leistungen arbeiten, d.h. dass Sie jeden Artikel mit Lohnminuten versehen.

|
[Bild: 24]

Gruppenrahmen Lohn

[Bild: 24. Gruppenrahmen Lohn]

Ähnlich wie beim Gruppenrahmen Material können auch beim Lohn verschiedene Kalkulationsgruppen benutzt werden. Dies dient dazu, um verschiedene Monteur-gruppen mit unterschiedlichen Preisen kalkulieren zu können. Lesen Sie hierzu im Kapitel Kalkulationsgruppen - Lohn nach.

|
[Bild: 25]

Fremdleistungen

[Bild: 25. Fremdleistungen]

Wenn Sie Fremdleistungen mit einem Multi beaufschlagen, müssen Sie hier den Wert eingeben. In den Stammdaten kann man festlegen, dass der Fremdleistungs-VK als fester Preis genommen und nicht kalkuliert wird. Wenn das der Fall ist, wird hier das Kreuz bei ‚VK hat Vorrang’ gesetzt.

|
[Bild: 26]

Sonstige Kosten

[Bild: 26. Sonstige Kosten]

Wenn Sie sonstige Kosten mit einem Multi beaufschlagen, müssen Sie hier den Wert eingeben. In den Stammdaten kann man festlegen, dass der VK für Sonstige Kosten als fester Preis genommen und nicht kalkuliert wird. Wenn das der Fall ist, wird hier das Kreuz bei ‚VK hat Vorrang’ gesetzt.

|
[Bild: 27]

Preis runden

[Bild: 27. Preis runden]

Wenn das Feld ‚Gesamtpreis runden’ angekreuzt wird, so wird der Einzelpreis der Position (gebildet aus Material und eventuellem Lohnanteil) aufgrund einer Rundungstabelle nach oben aufgerundet. Die Rundungstabelle wird im Modul EINSTELLUNGEN unter dem Menüpunkt <Grundeinstellungen> <Rundungstabelle> eingegeben. Der Preis wird immer bei Einschaltung dieses Feldes gerundet, Sie können es nicht individuell verhindern.

|
[Bild: 28]

DEL-Notiz

[Bild: 28. DEL-Notiz]

Geben Sie hier den Tageskupferpreis pro 100 kg ein.

|
[Bild: 29]

Multi auf CU-Anteil

[Bild: 29. Multi auf CU-Anteil]

Dieser Multi ist nur in der Elektrokalkulation interessant. Wenn mit dem Listenpreis kalkuliert wird, errechnet sich der Kupferwert dennoch aus der DEL-Notiz und dem Gewicht. Dadurch würde sich der Verkauf ermitteln aus Listenpreis + Kupferwert, wobei es sich bei dem Kupferwert um den Einkaufspreis handelt. Mit der CU-Bruttomulti rechnet das Programm Listenpreis +( Kupferwert * CU-Bruttomulti)

|
[Bild: 30]

Speichern

[Bild: 30. Speichern]

Durch Betätigen dieses Knopfes werden die von Ihnen vorgenommen Änderungen gespeichert.

|
[Bild: 31]

Ende

[Bild: 31. Ende]

Mit dem Knopf ‚Ende’ werden die Änderungen Verworfen und die Kalkulationseinstellung verlassen.
