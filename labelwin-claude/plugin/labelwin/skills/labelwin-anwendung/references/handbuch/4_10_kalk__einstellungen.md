# 4.10 Kalk.-Einstellungen

Pfad: Einrichtungsarbeiten > Einstellungen [14] > 4. Grundeinstellungen > 4.10 Kalk.-Einstellungen
Quelle: handbuch/4_10_kalk__einstellungen.htm

|

4.10 Kalk.-Einstellungen

Bei der Erstellung von Dokumenten mit Artikeln wie Angebote, Rechnungen, LV, Bestellungen usw. werden die aufgerufenen Artikel zwangsläufig kalkuliert. Um nicht bei jeder Neuanlage von solchen Dokumenten alle Kalkulationsfaktoren einzeln festzulegen, hat Label Kalkulationseinstellungen eingeführt. Dabei werden alle Einstellungen vorgenommen und unter einem Arbeitsnamen abgespeichert. Es werden üblicherweise solche Einstellungen wie “Brutto“, „Einkauf x 1,25“, „Thekenverkauf“ usw. eingerichtet. Bei der Neuanlage von Dokumenten wird nun einfach eine Einstellung über den Namen gewählt. Zusätzlich kann bei der Kundenadresse eine solche Einstellung hinterlegt werden, so dass bei der Dokumentenanlage nach der Adresswahl diese Einstellung vorgeschlagen wird.

Bevor wir die einzelnen Elemente beschreiben, wollen wir auf die Logik der Preisermittlung eingehen.

Hierarchie bei Material-VK-Ermittlung

Je nach eingetragener Einstellung kann der VK (Verkauf) über unterschiedliche Wege ermittelt werden. In den folgenden Beispielen rechnen wir immer mit dem Einkaufspreis (EK) als Basis. Genau die gleiche Rechnung würde mit dem Listenpreis erfolgen, wenn dieses bei ‚Preisbildung’ (Nr. 7) angewählt wäre.

1. Priorität hat bei eingeschaltetem Vorrang ein fester Verkaufspreis, wenn bei den Artikelstammdaten einer hinterlegt ist.

[Bild]

2. Priorität hat ein gewählter Gruppenrahmen ‚Kleinteile’ oder ‚Handelspanne’(Nr.19). Je nach dort hinterlegten Stufen kann der Preis mit einem solchen Multi gerechnet werden.

Beispiel: EK = 7,00 €, Kleinteilefaktura Gruppenrahmen ‚Normal’.

[Bild]

Einstellungen: Mat.VK = 7,00 € * 1,80 = 12,60 €

Da diese Beispieltabelle bei 50,00 € endet, findet sie bei Preisen über 50,00 € Einkauf keine Anwendung.

|

Hinweis: Die Werte für den Gruppenrahmen werden im Modul EINSTELLUNGEN <Grundeinstellungen> <Kalkulationsgruppen> <bearbeiten Kleinteilefaktura> festgelegt.

Bei der Berechnung mit Handelspannen handelt es sich um eine Alternative zur Kleinteilefaktura. Während bei der Kleinteilefaktura der Zuschlagsfaktor von der Höhe des Einkaufpreises abhängt, wird ein Multi bei der Methode mit der Handelspanne, also der Differenz zwischen Listenpreis und Einkaufspreis gebildet. Je nach Wunsch, kann der Multi auf den Listenpreis oder den Einkaufspreis wirken.

Wenn Sie einen Multi auf den Listenpreis nutzen wollen, so wird er bei niedrigerem Rabatt oder keinem über 1 gehen, bei hohen Rabatten unter 1. Diese Methode bezieht den auf dem Markt bekannten Listenpreis mit ein und bestimmt den Multi über die Ihnen gewährte Handelsspanne.

Wenn Sie dagegen mit einem Multi auf den Einkaufspreis arbeiten, so muss er immer über 1 liegen.

[Bild]

Wenn Sie in der Kalkulationseinstellung Preisbildung über Listenkreis, Vorrang Festpreis Verkauf 1 und Handelsspanne Standard ausgewählt haben, ergibt sich folgendes Rechenbeispiel:

Der Listenpreis beträgt 3,82. Aufgrund des eigenen Rabatts von 79,06% greift der in der Zeile bis 80% hinterlegte Multi 0,5.

Listenpreis 3,82 € x Multi 0,5 = Material-VK 1,91 €

|

Hinweis: Die Werte für den Gruppenrahmen werden im Modul EINSTELLUNGEN <Grundeinstellungen> <Kalkulationsgruppen> <bearbeiten Handelsspanne> festgelegt.

3. Priorität hat ein gewählter Gruppenrahmen ‚Material’ (Nr.18). Dort können Kalkulations-materialgruppen mit 4stelligen Bezeichnungen hinterlegt werden. Wenn der aufgerufene Artikel mit seiner Kalkulationsgruppe im Gruppenrahmen vorhanden ist, wird der dort hinterlegte Faktor verwendet. Falls der Faktor auf 0 steht, wird der allgemeine Materialmulti (Nr. 8) verwendet.

Beispiel: Der Artikel gehört zur Kalkulationsgruppe ‚Porz’

EK = 85,00 € - eingeschalteter Gruppenrahmen ‚FremdLV’

[Bild]

Der Einkaufpreis wird mit 1,30 multipliziert, also 85,00 € * 1,30 = 110,50 €

4. (und letzte) Priorität hat der normale Materialmulti.

Kalkulationseinstellung

Sie ändern eine Kalkulationseinstellung, indem Sie die entsprechende Einstellung aktivieren, dann die Einstellungen entsprechend verändern und unter dem Menüpunkt <Datei> <Speichern> diese wieder in die Stammdaten zurückführen. Das Speichern kann auch über den Knopf ‚Speichern’ erfolgen. Eine geänderte Kalkulationseinstellung kann als neue Einstellung abgespeichert werden, in dem Sie dieser unter dem Menüpunkt <Datei> <Speichern als neu> einen neuen Namen geben. Die Kalkulationseinstellungen gelten für alle Benutzer und können aber für das jeweilige Dokument abgeändert werden, ohne die dauerhaft gespeicherten Einstellungen zu verändern.

[Bild]

Bild: Grundeinstellungen: Kalkulationseinstellungen

[Bild]

1 Einstellungen: Hier wird die zu verändernde Einstellung gewählt.

[Bild]

2 Positions-Nummer Schema: Sie haben die Möglichkeit die Positions-Nr. nach Ihren Wünschen zu gliedern. Dazu werden folgende Buchstaben verwendet:

B für Bauteile

A für Bauabschnitte (Lose)

T für Titel

P für Positionen

Wenn das Dokument dann später umnummeriert wird, so wird die Positions-Nr. entsprechend Ihrem Gliederungsschema gebildet.

Beispiel: Gliederungsschema ist TT.PPP, d.h. in Ihrem Dokument dürfen sich max. 99 Titel be-finden und in jedem Titel max. 999 Positionen. Die Positions-Nr. lauten dann 1.1 für die erste Position im ersten Titel, 2.1 für die erste Position im 2. Titel usw.

Solange Sie das Gliederungsschema mit Großbuchstaben bilden, entfallen führende Nullen. Wenn Sie statt Großbuchstaben Kleinbuchstaben verwenden, so werden führende Nullen in jeder Gliede-rungsebene aufgefüllt.

Beispiel: tt.ppp die erste Positions-Nr. im ersten Titel lautet dann 01.001. Damit ist gewährleistet, dass alle Positions-Nr. die identische Länge besitzen. Der Trenner zwischen den einzelnen Gliede-rungsebenen ist in der Regel der Punkt.

[Bild]

3 Beispiel: Hier wird Ihnen eine Positionsnr. Gem. dem gewählten Positions-Nummer Schema als Beispiel angezeigt. Gerade bei Leistungsverzeichnissen ist es wichtig, dass die Positionsnummern gemäß den Vorgaben gewählt werden.

[Bild]

4 Schrittweite: Mit dem Feld ‚Schrittweite’ steuern Sie, in welchen Schritten die Positions-Nr. gebildet wird. Die Schrittweite bezieht sich immer auf den Bereich P in der Gliederung. Somit ist es möglich Ihr Dokument auch in 5er bzw. 10er Schritten zu nummerieren.

[Bild]

5 Anfangs-Nr.: Hier können Sie vorgeben, mit welcher Positionsnummer Sie die fortlaufende Nummerierung starten möchten.

[Bild]

6 Artikelschlusstext: Es ist möglich, jeden Artikel mit einem Artikelschlusstext wie z.B. ‚liefern und montieren’, oder ‚nur liefern’ usw. zu versehen. Da der exakte Text über eine Auswahl erst beim Drucken festgelegt wird, legen Sie an dieser Stelle eigentlich nur die Kategorie fest. Hierdurch ist es möglich, dass die gleiche Position beim Druck als Angebot mit ‚liefern und montieren’ und beim Druck als Rechnung mit ‚geliefert und montiert’ versehen werden kann.

An dieser Stelle wählen Sie die Standardvorgabe, die Ihnen bei jedem Artikel vorgeschlagen wird. Beim Artikelaufruf können Sie diese Vorgabe dann für jede Position verändern.

Die Artikelschlusstexte werden in dem Modul EINSTELLUNGEN unter dem Menüpunkt <Pro-grammbereiche> <Dokumentenerstellung> <‚Artikelschlusstexte> erfasst und geändert.

[Bild]

7 Vorgabe Langform: Mit diesem Feld bestimmen Sie, ob Ihr Artikeltext in der eventuell vorhandenen Langform ausgegeben werden soll. Diese Schaltfläche dient als Vorgabe für den Artikelaufruf. Für jede einzelne Position können Sie diese Vorgabe später ändern. Die Vorgabe ‚Langtext’ trifft dann aber auch nur für die Artikel zu, die eine Langform beinhalten. Sollte keine Langform vorhanden sein, so wird automatisch der Kurztext übernommen.

[Bild]

8 Artikeltext erhalten: Hier haben Sie die Möglichkeit, schon in der Kalkulationseinstellung festzulegen, dass bei Gaeb-Ausschreibungen der Originaltext erhalten bleibt, selbst wenn man Artikel aus den Stammdaten zur Kalkulation aufruft. Wenn die Option über den alten Menüpunkt geschaltet wird, so wird dieses ebenfalls dauerhaft für das aktuelle Dokument gespeichert. Sie können dieses auch im Einstellmodul für die Kalkulationsvorgabe dauerhaft einstellen.

[Bild]

9 Umnummerieren: Mit dem Feld ‚Umnummerieren’ können Sie steuern, ob das Dokument später überhaupt umnummerierbar sein soll. Im Regelfall sollte ‚immer’ angekreuzt sein, weil es dann problemlos möglich ist, Positionen in Ihr Dokument einzufügen und später die Positions-Nr. neu zu bilden. Wenn das Feld ‚nie’ angekreuzt ist, so kann das Dokument nicht umnummeriert werden. Dies ist insbesondere dann wichtig, wenn Positions-Nr. von Hand erfasst werden (z.B. weil sie aus einem Fremd-LV übernommen werden) oder wenn später Referenzen auf diese Positions-Nr. gebildet werden (Mengenüberwachung). Bei Teilrechnungen sollte das Dokument auf nicht umnummerierbar gesetzt werden, damit die Bezüge auf die Positionen des Angebotes erhalten bleiben. Sie können jedoch auch ‚fragen’ ankreuzen. Wenn Sie dann ein Dokument verlassen, werden Sie gefragt, ob Sie umnummerieren möchten oder nicht. Bei ‚nur Setbestandteile’ wird nur innerhalb eines Sets umnummeriert.

[Bild]

10 Preisbildung über: Mit dieser Schaltfläche entscheiden Sie, welcher Preis aus den Artikelstammdaten zur Ermittlung Ihres Materialverkaufspreises herangezogen wird. Sie haben dazu die Wahl zwischen dem Listenpreis, Listenpreis 2 oder den Einkauf. Sollte kein Einkauf vorhanden sein, so wird in diesem Fall auch kein Materialverkauf ermittelt. Bei den Großhändlern, bei denen keine Einkaufspreise vorhanden sind, sollten Sie die Kalkulationseinstellung entsprechend auf Listenpreise, d.h. den Händlerbruttopreis schalten.

[Bild]

11 Vorrang Festpreise: Sie haben in den Artikelstammdaten die Möglichkeit, außer dem Listenpreis und den beiden Einkaufspreisen weitere feste Verkaufspreise zu erfassen. Diesen Verkaufspreisen kann ein Vorrang gegenüber der normalen Zuschlagskalkulation eingeräumt werden. Über die Schaltfläche ‚Vorrang’ entscheiden Sie, welcher der Verkaufspreise einen eventuellen Vorrang genießt. Alle Artikel, bei denen dann kein entsprechender Verkaufspreis eingerichtet ist, werden mit den normalen Standardfaktoren kalkuliert. Dieses ist z. B. sinnvoll für Sicherheitsventile, die nicht mit Materialmulti 1,25 kalkuliert werden, sondern mit einen festen Preis von 19,20 erhalten.

[Bild]

12 Einkaufspreis-Grundlage: Es besteht die Möglichkeit, in den Artikelstammdaten 2 Einkaufspreise zu verwalten. Der EK1 wird in der Regel vom Großhändler über die Datanorm belegt. Den EK2 können Sie verwenden, um Sondereinkaufspreise zu verwalten. Über die Schaltfläche ‚Einkaufspreis-Grundlage’ entscheiden Sie, welcher der beiden Einkaufspreise automatisch in die Artikelkalkulation eingefügt wird. Der Einkaufspreis wird auch dann eingefügt, wenn Sie über Listenpreise kalkulieren. Dadurch ist es möglich, auch bei einer Kalkulation über Listenpreis eine Kalkulationsauswertung und dementsprechend einen Materialertrag zu ermitteln.

Die weitere Möglichkeit ist, automatisch den Artikel aus der Verknüpfung herauszusuchen, der den günstigsten Einkauf besitzt. Dabei muss darauf geachtet werden, dass die Einkaufspreise gepflegt sind. Alle Preise werden aus dem Artikel verwendet, der den günstigsten EK besitzt, zusätzlich kommen aus diesem Artikel die Artikelnummer sowie der Bestellhändler. Minuten und der Text kommen aus dem ursprünglich aufgerufenen Artikel. Wenn Sie mit EK2 kalkulieren, wird auch dieser bei der Berechnung berücksichtigt.

[Bild]

13 Materialmulti: Über den Materialmulti bestimmen Sie, mit welchem Aufschlag Ihre Materialien berechnet werden sollen. Je nachdem, wie Sie die Preisbildung eingestellt haben, greift der Materialmulti auf den Einkaufspreis1, den Einkaufspreis2 oder den Listenpreis.

[Bild]

14 Mindestmulti: Über den Mindestaufschlag des Materials schalten Sie eine Warnung zu. Wenn der Mindestaufschlag unterschritten wird, d.h. wenn der Aufschlag auf den Materialeinkauf geringer ist als der Mindestmulti, so erhalten Sie ein großes Fenster als Warnung. Die Gefahr der Unterschreitung eines Mindestmultis ist häufig dann gegeben, wenn aufgrund von Listenpreisen kalkuliert wird. Dabei gibt es bei einzelnen Großhändlern immer wieder Artikel auf die Sie keinen oder einen sehr geringen Rabatt erhalten. Der Mindestzuschlag verhindert außerdem Tippfehler wie z.B. 300 statt 3000 €. Selbstverständlich können Sie Material zu jedem von Ihnen gewünschten Preis verkaufen. D.h. dieser Mindestzuschlag löst nur eine Warnung aus, verhindert dabei aber nicht, dass Sie mit einem zu geringen Multi kalkulieren können.

[Bild]

15 Datanormpreise ab: Wenn Sie eine Preisänderung einspielen, so kann Ihr Lieferant laut Datanorm ein Datum für ‚Preise gültig ab’ übergeben. Labelwin verwaltet diese Preise in einem separaten Feld und nimmt je nach Datum den richtigen Einkaufspreis. In diesem Feld können Sie festlegen, welches Datum zur Preisfindung genommen werden soll. Beispiel: Ein Artikel kostet EK 100,00 € und soll ab 01.10. 105,00 € kosten. Wenn Sie am 15.09. in einem Dokument in der Kalkulationseinstellung als Preisdatum den 01.10. (oder später) einsetzen, wird schon mit dem Preis von 105,00 € kalkuliert.

[Bild]

16 Gruppenrahmen Material: Neben der oben beschriebenen einfachen Zuschlags-kalkulation können unterschiedliche Artikelgruppen mit verschiedenen Zuschlagssätzen kalkuliert werden. Dazu müssen Kalkulationsgruppen wie z.B. KESS für Kessel, HK für Heizkörper oder auch 001 für eine bestimmte Materialgruppe definiert werden. Die Anlage der Gruppen findet im Programm EINSTELLUNGEN statt. Jeder Artikel, der über die Gruppenkalkulation kalkuliert werden soll, muss einer solchen Gruppe zugeordnet werden (geschieht im Programm KATALOG). Außerdem müssen die Kalkulationsmultis für die Gruppen festgelegt werden. Um beim obigen Beispiel zu bleiben, wird der Gruppe KESS (stellvertretend für Kessel) ein Multiplikator 1.2 zugeordnet. Dieser Faktor wird im Gruppenrahmen 1 eingetragen. Im Gruppenrahmen 2 wird als Multi 1.3 eingetragen usw. Bis zu 99 Gruppenrahmen sind möglich.

An dieser Stelle in der Kalkulationseinstellung legen Sie fest, mit welchem Gruppenrahmen Sie arbeiten möchten.

Bei der Eingabe von 0 ist die Gruppenkalkulation ausgeschaltet, bei 1 wird bei Artikeln der Gruppe KESS mit 1.2, bei 2 mit 1.3 usw. gerechnet.

Lesen Sie hierzu im Kapitel 14.4.12.1 nach.

Sie haben außerdem die Möglichkeit, für jede Materialgruppe festzulegen, ob sich der Faktor auf den Listen- oder Nettopreis auswirken soll. Im Modul EINSTELLUNGEN <Grundeinstellungen> <Kalkulationsgruppen> <bearbeiten Material> können Sie für jede einzelne Materialgruppe festlegen, ob der Preis

- wie bisher aufgrund der Kalkulationseinstellung oder

- aufgrund des Listenpreises oder

- aufgrund des Nettopreises

gebildet werden soll.

[Bild]

17 Gruppenrahmen Kleinteile/Handels-spanne: Bei eingeschalteter Kleinteile-fakturierung oder Handelsspanne kann der Multiplikator in Abhängigkeit vom Preis oder der Handelsspanne festgelegt werden. Zu Details lesen Sie am Anfang dieses Kapitels über die Kalkulation und im Kapitel 14.4.12.3 über die Einrichtung nach.

[Bild]

18 Lohn-Kalkulation: Wenn Sie beim Artikel hinterlegte Kalkulations-zeiten für die Lohnermittlung nehmen möchten, so müssen Sie hier das Feld der Minuten festlegen. Je Artikel sind 2 verschiedene Minutensätze zuzuordnen. Die als Fremdminuten bezeichneten Werte gelangen in der Regel über eine Diskette vom Großhändler in Ihren Rechner, die anderen vergeben Sie selbst. Wenn die Einstellung auf ‚Eigene’ steht und dort kein Wert hinterlegt ist, nimmt das Programm automatisch die ‚Fremdminuten’. Sollten Sie jedoch ‚Eigene Min (immer)’ gewählt haben, wird kein Wert übernommen, auch wenn bei ‚Fremdminuten’ etwas hinterlegt ist.

[Bild]

19 Zeitmulti: Sie können jeden Artikel in den Artikelstammdaten mit einer Zeit versehen. Zum Beispiel: Einen Heizkörper komplett montieren, demontieren für Malerzwecke und wieder montieren dauert 180 Minuten. Diese Zeit gilt für eine ‚normale Baustelle’. Weil jede Baustelle einen unterschiedlichen Erschwernisgrad besitzt, muss diese Zeit nicht für jede Baustelle identisch sein. Sie haben über den Zeitmulti die Möglichkeit die hinterlegten Zeiten zu verlängern (Multi größer als 1) oder zu verkürzen (Multi kleiner als 1). Dadurch brauchen Sie sich nicht bei jeder einzelnen Positionen Gedanken über die Zeit machen. Wenn Sie den Zeitmulti auf 0 setzen, so rechnen Sie ohne die hinterlegten Zeiten (z.B. bei einer Kundendienstrechnung, in der die Zeit als Montagestunde berechnet wird).

[Bild]

20 Selbstkosten / Std.: Mit den Selbstkosten je Stunde geben Sie an, wie hoch Ihre Kosten pro Monteurstunde sind. In den Selbstkosten sollten enthalten sein der Monteurlohn, die Sozialbeiträge, ein Zuschlag für Unproduktivität sowie die Kosten für Urlaub und Krankheit. Durch Eingabe dieses Wertes ist es Ihnen später möglich, einen Ertrag auch für die Lohnseite zu ermitteln.

Verrechnungssatz / Std.: Als Verrechnungssatz geben Sie bitte Ihren Stundenverrechnungssatz ein. Die Differenz zwischen den Selbstkosten und dem Verrechnungssatz wird Ihnen dann später als Lohnertrag in der Kalkulationsauswertung ausgewiesen. Beide Kostensätze können allerdings nur dann greifen, wenn Sie mit Leistungen arbeiten, d.h. dass Sie jeden Artikel mit Lohnminuten versehen.

[Bild]

21 Gruppenrahmen Lohn: Ähnlich wie beim Gruppenrahmen Material können auch beim Lohn verschiedene Kalkulationsgruppen benutzt werden. Dies dient dazu, um verschiedene Monteur-gruppen mit unterschiedlichen Preisen kalkulieren zu können. Lesen Sie hierzu im Kapitel 14.4.11.2 nach.

[Bild]

22 Fremdleistungen: Wenn Sie Fremdleistungen mit einem Multi beaufschlagen, müssen Sie hier den Wert eingeben. In den Stammdaten kann man festlegen, dass der Fremdleistungs-VK als fester Preis genommen und nicht kalkuliert wird. Wenn das der Fall ist, wird hier das Kreuz bei ‚VK hat Vorrang’ gesetzt.

[Bild]

23 Sonstige Kosten: Wenn Sie sonstige Kosten mit einem Multi beaufschlagen, müssen Sie hier den Wert eingeben. In den Stammdaten kann man festlegen, dass der VK für Sonstige Kosten als fester Preis genommen und nicht kalkuliert wird. Wenn das der Fall ist, wird hier das Kreuz bei ‚VK hat Vorrang’ gesetzt.

[Bild]

24 Preis runden: Wenn das Feld ‚Gesamtpreis runden’ angekreuzt wird, so wird der Einzelpreis der Position (gebildet aus Material und eventuellem Lohnanteil) aufgrund einer Rundungstabelle nach oben aufgerundet. Die Rundungstabelle wird im Modul EINSTELLUNGEN unter dem Menüpunkt <Grundeinstellungen> <Rundungstabelle> eingegeben. Der Preis wird immer bei Einschaltung dieses Feldes gerundet, Sie können es nicht individuell verhindern.

[Bild]

25 DEL-Notiz: Geben Sie hier den Tageskupferpreis pro 100 kg ein.

[Bild]

26 CU-Multi bei Listenpreis: Dieser Multi ist nur in der Elektrokalkulation interessant. Wenn mit dem Listenpreis kalkuliert wird, errechnet sich der Kupferwert dennoch aus der DEL-Notiz und dem Gewicht. Dadurch würde sich der Verkauf ermitteln aus Listenpreis + Kupferwert, wobei es sich bei dem Kupferwert um den Einkaufspreis handelt. Mit der CU-Bruttomulti rechnet das Programm Listenpreis +( Kupferwert * CU-Bruttomulti)

[Bild]

27 Speichern: Durch Betätigen dieses Knopfes speichern Sie die Eingaben für eine vorhandene oder neue Kalkulationseinstellung.

[Bild]

28 Ende: Durch Betätigen dieses Knopfes wird die Maske geschlossen.

Die Menupunkte im Einzelnen:

Datei

Neu

Durch Anwahl dieses Menüpunktes wird eine neue Kalkulationsbasis angelegt. Häufig ist es sinnvoller, eine vorhandene Basis über ‚Speichern als’ zu kopieren und dann anzupassen.

Speichern

Durch Anwahl dieses Menüpunktes wird die aktuelle Kalkulationseinstellung gespeichert.

Speichern als neu F3

Durch Anwahl dieses Menüpunktes wird die aktuelle Kalkulationseinstellung unter einem anderen Namen gespeichert.

Löschen

Durch die Anwahl dieses Menüpunktes wird die aktuelle Kalkulationseinstellung gelöscht. Da eine Kalkulationseinstellung ggf. bei vielen Adressen hinterlegt ist, sollten Sie hier vorsichtig sein.

Del-Notiz eintragen

Hier können Sie die aktuell festgelegte Del-Notiz für ALLE Kalkulationseinstellungen eintragen lassen.

Lohnselbstkosten eintragen

Hier können Sie die aktuell festgelegten Lohnselbstkosten für ALLE Kalkulationseinstellungen eintragen lassen.

Beenden

Hiermit beenden Sie die Kalkulationseinstellung.
