# 3. Datev-Schnittstelle Grundeinstellungen

Pfad: Buchhaltung > Fibu-Schnittstelle [24] > 3. Datev-Schnittstelle Grundeinstellungen
Quelle: handbuch/3__datev_schnittstelle_grundeinstellungen.htm

|

3. Datev-Schnittstelle Grundeinstellungen

Damit die im Labelwin erfassten Daten korrekt an die Datev übergeben werden können, müssen gewisse Grundeinstellungen für Sie und Ihren Steuerberater passend vorgenommen werden. Im Zweifelsfalle sprechen Sie die Informationen bitte mit Ihrem Steuerberater ab und stellen ihm dazu diese kurze Beschreibung zur Verfügung.

Bei der eigentlichen Übergabe muss zusätzlich jeweils die Abrechnungsnummer und das Abrechnungsjahr eingegeben werden. Dies geschieht jedoch an der Oberfläche, da die Daten evtl. bei jeder Übergabe angepasst werden müssen. Die hier beschriebenen Einstellungen müssen nur einmalig erfasst werden.

Anwahl: In diesem Bereich gelangen Sie nach dem Start des Moduls ‚Fibu-Schnittstelle‘ durch Betätigen des Knopfes ‚Einstellungen’

[Bild: 3. Datev-Schnittstelle Grundeinstellungen]

Bild: Einstellungen Datev

|
[Bild: 1]

Zielpfad

[Bild: 1. Zielpfad]

Geben Sie den Pfad an, in dem die Auslagerungsdateien erzeugt werden sollen. Standardmäßig vorgesehen haben wir den Pfad Fibu, der vom Labelwin Verzeichnis abzweigt. Dieser Pfad ist bei Ihnen bereits eingerichtet.

|
[Bild: 2]

Unterverzeichnis je Übertragungslauf

[Bild: 2. Unterverzeichnis je Übertragungslauf]

Der von jedem Betrieb selbst festzulegende Pfad unter [Nr.1] kann für jeden Lauf um einen Unterordner erweitert werden. Damit liegen alle Daten eines Laufes in einem eigenen Bereich und können so schneller gefunden werden.

Beispiel:

L:\labelwin\fibu\ - daraus wird beim Lauf 387 eine Ablage in

L:\labelwin\fibu\Lauf_387\

|
[Bild: 3]

neue Version ab 2017

[Bild: 3. neue Version ab 2017]

Die alte DATEV-Schnittstelle im Postversand-Format galt bis Ende 2017. Seit 2018 muss zwingend die neue Schnittstelle im sogenannten DATEV-Format verwendet werden.

|
[Bild: 4]

Berater-Nr.

[Bild: 4. Berater-Nr.]

Tragen Sie hier die Beraternummer ein.

|
[Bild: 5]

Berater Name

[Bild: 5. Berater Name]

Tragen Sie hier den Beraternamen ein.

|
[Bild: 6]

DFV-Kennzeichen

[Bild: 6. DFV-Kennzeichen]

Tragen Sie hier das DFV-Kennzeichen ein. Beispiel: Namenskürzel, nur 2 Buchstaben.

|
[Bild: 7]

Mandanten-Nr.

[Bild: 7. Mandanten-Nr.]

Tragen Sie hier die Mandantennummer ein.

|
[Bild: 8]

Eingangsrechnungen

[Bild: 8. Eingangsrechnungen]

„Eingangsrg.: Übergabe der Org.Nummer statt Labelwin-Belegzähler“: In Labelwin erhält jede Eingangsrechnung eine eindeutige interne Belegnummer. Diese wird standardmäßig übergeben, kann mit dieser Option aber durch die originale Rechnungsnummer ersetzt werden.

„Eing. Rg: Kostenstellen an Datev übergeben“: Mit diesem Schalter legen Sie fest ob Sie die Eingangsrechnungen mit Kostenstellen übergeben. Da eine Eingangsrechnungen auf beliebig viele Projekte und Kostenstellen aufgeteilt werden können, entstehen aus einer Eingangsrechnung ggf. mehrere Buchungssätze in der Fibu.

„komplette Adresse übertragen (sonst nur Konto +Kurzname/Suchwort)“: Hier kann festgelegt werden, ob Adressen in Kurzform und komplett mit Anschrift übertragen werden.

|
[Bild: 9]

Sonstige Optionen

[Bild: 9. Sonstige Optionen]

„Mahndatum übergeben“: Soll über die Datev gemahnt werden, ist es wichtig etwaige Mahndaten aus Label zu übergeben.

„Übergabe der Skontofrist Rgausgang (nur BMD-Fibu, Sonderversion)“: Bei der BMD-Fibu besteht die Möglichkeit die Skontofristen von Ausgangsrechnungen mit zu übergeben.

|
[Bild: 10]

mit Auslagerung der Archiv-PDF's

[Bild: 10. mit Auslagerung der Archiv-PDF's]

Diese Möglichkeit betrifft nur die DATEV mit der ‚neuen‘ Schnittstelle ab 2017. Dazu gehört natürlich auch, dass Sie das Modul Scan-Archiv nutzen.

Wird diese Option aktiviert, wird automatisch auch der Haken bei [Nr.2] gesetzt und somit immer Unterverzeichnisse im Zielpfad erzeugt.

1) Steuerberater: Beachten Sie, dass die Daten aufgrund ihrer Größe nicht mehr als Email-Anhang an den Steuerberater versendet werden können. Ihr Steuerberater muss Ihnen also einen FTP-Transfer einrichten oder Sie müssen mit einem USB-Stick arbeiten.

Hinweis: Wenn Ihr Steuerberater das DATEV-Modul "Beleg to Buchung" einsetzt, kann er Ihre Belege in der DATEV-Cloud dauerhaft archivieren. Über die revisionssichere Ablage brauchen Sie sich dann keine Gedanken mehr machen.

2) Datev-Inhouse-Lösung: Ist die Datev bei Ihnen im Haus, sollten Sie die Daten immer in das gleiche Verzeichnis packen, weil die Pfadumstellung in Datev jedesmal aufwändig wäre. Bei der Übernahme löscht Datev dann die Dateien weg, so dass das Verzeichnis für den nächsten Übertragungslauf wieder leer ist.

|
[Bild: 11]

Umbuchung geparkte Erlöse

[Bild: 11. Umbuchung geparkte Erlöse]

Wird mit IST-versteuerten Abschlägen gearbeitet, erfolgt die Umbuchung der Erlöse standardmäßig über das Verrechnungskonto. Mit dieser Option kann die Umbuchung über das Debitorenkonto aktiviert werden.

|
[Bild: 12]

Kontonummern

[Bild: 12. Kontonummern]

„Länge der Sachkonten“: Legen Sie hier fest, wie lang ein Sachkonto ist. Datev lässt bis zu siebenstellige Konten zu, aber hier muss die tatsächlich verwendete Länge stehen. Üblicherweise werden 4-stellige Nummern verwendet.

„Verwendung 6 stelligen Belegzähler bis Datum“: Hier kann ein Datum eingetragen werden, bis wann 6-stellige Belegzähler verwendet werden sollen.

|
[Bild: 13]

Umgang mit Kost1 und Kost2

[Bild: 13. Umgang mit Kost1 und Kost2]

„Projektnr. Als Kost1, Kostenstelle als Kost2 übergeben“: Es gibt Firmen, die jedes Projekt als Kostenstelle definieren. Mit dieser Option wird die Projektnummer als Kost1 übergeben und die Kostenstelle als Kost2.

„gedreht, Projektnr. als Kost2, Kostenstelle als Kost1 übergeben“: Die obige Option lässt sich auch drehen.

„Sonderzeichen aus Projektnummer entfernen“: Sonderzeichen werden hiermit aus Projektnummern entfernt. Das kann sinnvoll sein, da einigen Fibu's Probleme bekommen können.

„Abteilung als Kostenstelle übergeben“: Manche Firmen möchten die Erlöse und Kosten je Abteilung getrennt haben. Um dennoch nicht mit Kostenstellen innerhalb von Labelwin zu arbeiten und auch keine Konten je Abteilung zu führen, wurde diese Möglichkeit geschaffen. Da jedes Projekt zwingend zu einer Abteilung gehören kann, sind auch die Ausgangs- und Eingangsrechnungen sinngemäß einer Abteilung zugeordnet.

Mit diesem Schalter wird festgelegt OB die 'Kostenstelle' übergeben wird, mit weiteren Schaltern wird festgelegt, ob die Übergabe im Feld Kost1 oder in Kost2 erfolgt.

|
[Bild: 14]

Wiederherstellen

[Bild: 14. Wiederherstellen]

Falls Sie versehentlich eine falsche Änderung in der Maske gemacht haben, können Sie durch Betätigung dieses Knopfes die Änderungen, die Sie seit dem letzten ‚Übernehmen‘ gemacht haben, rückgängig machen.

|
[Bild: 15]

Übernehmen

[Bild: 15. Übernehmen]

Durch Betätigung dieses Knopfes werden die Einstellungen gespeichert.

|
[Bild: 16]

Abbruch

[Bild: 16. Abbruch]

Durch Betätigung dieses Knopfes wird die Einstell-Maske ohne Übernahme von evtl. Änderungen geschlossen.
