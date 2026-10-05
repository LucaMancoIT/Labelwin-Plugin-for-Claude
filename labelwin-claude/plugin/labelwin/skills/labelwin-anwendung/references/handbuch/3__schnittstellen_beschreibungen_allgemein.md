# 3. Schnittstellen-Beschreibungen allgemein

Pfad: Buchhaltung > Fibu-Schnittstelle [24] > 3. Schnittstellen-Beschreibungen allgemein
Quelle: handbuch/3__schnittstellen_beschreibungen_allgemein.htm

|

3. Schnittstellen-Beschreibungen allgemein

In diesem Abschnitt soll eine Beschreibung der spezifischen Einstellungen der Fibu-Schnittstellen erfolgen. Da der untere Teil der Einstell-Maske jedoch für jede Schnittstelle gleich ist, folgt zunächst eine Beschreibung dafür.

|

Hinweis: Da die erforderlichen Einstellungen für die unterschiedlichen Fibu-Schnittstellen z. Teil sehr unterschiedlich sind, stellen wir Ihnen diese Seiten jeweils nach Bedarf zur Verfügung. Es wäre unsinnig hier im Handbuch alle Schnittstellen zu beschreiben. Weil diese am häufigsten eingesetzt wird, haben wir nur die Datev abgebildet.

[Bild]

[Bild]

1 Verrechnungskonto: Im Label-Programm ist es möglich, die Summe einer Eingangsrechnung nicht komplett auf ein einziges Konto zu buchen, sondern man kann eine Aufsplittung auf mehrere Konten vornehmen. Bei der Auslagerung einer solchen Rechnung wird zunächst die gesamte Summe auf das hier einzutragende Verrechnungskonto gebucht. Dann folgen weitere Buchungssätze, mit denen die Einzelbeträge von dem Verrechnungskonto auf die jeweiligen Zielkonten gebucht werden. Nach Abschluss aller Buchungen ist das Verrechnungskonto also immer auf Null.

[Bild]

2 Standard-Erlöskonto: Geben Sie hier eine „Ersatz“-Kontonummer an, für den Fall dass in einer Ausgangsrechnung kein Erlöskonto eingetragen ist.

[Bild]

3 Standard Warenkonto: Geben Sie hier eine „Ersatz“-Kontonummer an, falls für eine Eingangsrechnung kein Warenkonto eingetragen ist.

[Bild]

4 Vorgabe von Datum: Die Eingabe des Von-Datums ist auf der Hauptmaske aus Gründen der Fehler-Vermeidung nicht veränderbar. Hier können Sie das Datum vorgeben.

[Bild]

5 Standard Debitor: Geben Sie hier eine „Ersatz“-Kontonummer an, für den Fall dass in einer zur Rechnung gehörenden Kunden-Adresse keine Debitor-Nummer angegeben ist.

[Bild]

6 Standard Kreditor: Geben Sie hier eine „Ersatz“-Kontonummer an, für den Fall dass in einer zur Rechnung gehörenden Lieferanten-Adresse keine Kreditor-Nummer angegeben ist.

Karteikarte Ausgangsrechnungen:

[Bild]

7 Ankreuzfelder:

Ankreuz-Feld „Übertragung nur der noch nicht gekennzeichneten Rechnungen“:

Jede Rechnung, die übertragen wird, erhält vom Programm eine Kennzeichnung. Durch ein Kreuz in diesem Feld werden alle Rechnungen, die dieses Kennzeichen besitzen, nicht mit ausgelagert. Dadurch wird erreicht, dass im Normalfall eine Rechnung nur einmal übertragen wird.

Ankreuz-Feld „stornierte Rechnungen übertragen“:

Durch ein Kreuz in diesem Feld werden auch stornierte Rechnungen ausgelagert. Die Wahl dieser Option ist nur sinnvoll, wenn die Schnittstelle zu Ihrer Fibu-Software auch den Rechnungs-Status überträgt.

Ankreuz-Feld „Rechnungen mit Null-Summe übertragen“:

Durch ein Kreuz in diesem Feld werden auch Rechnungen ausgelagert, deren Summe im Label-Programm auf „0“ steht.

Ankreuz-Feld „Standard-Erlöskonto immer nehmen“:

Bei einem Kreuz in diesem Feld wird das in Feld Nr. 2 eingetragene Standard-Erlöskonto immer genommen, auch wenn in der Ausgangsrechnung ein Konto eingetragen ist.

Ankreuz-Feld „Verteilung nach Kostenstellen“:

Wenn Sie im Bereich der Ausgangsrechnungen mit unterschiedlichen Kostenstellen arbeiten, so können Sie die Buchungssätze auch nach diesen Kostenstellen getrennt an die Datev übergeben.

Ankreuz-Feld „bei Kostenstellen hinterlegte Erlöskonten nutzen“:

Diese Möglichkeit ist für die meisten Anwender sicherlich nicht sinnvoll. Sie kann nur angewendet werden, wenn in dem Bereich Ausgangsrechnungen mit unterschiedlichen Kostenstellen gearbeitet wird. Es geht darum, dann eine einzelne Ausgangsrechnung nicht auf ein einzelnes Erlöskonto sondern auf verschiedene Erlöskonten zu buchen. In diesem Falle wird nicht das bei der Dokumentenanlage vorgegebene Erlöskonto genutzt, sondern je nach Kostenstellen, zu der ein Artikel gehört, wird das in der Tabelle Kostenstellen hinterlegte Erlöskonto verwendet. Zu diesem Thema gibt es bei Label-Software ein zweiseitiges Dokument, in dem diese Vorgehensweise beschrieben ist. Bitte fordern Sie es bei Bedarf an.

Ankreuz-Feld „absolut keine Kostenstellen einsetzen (BMD-Fibu)“:

Die weiteren Ankreuzfelder werden in Absprache bei der Einrichtung erklärt.

Die hier gemachten Einstellungen dienen auch als Vorgabe für die Kreuze in der Eingrenzungs-Maske.

[Bild]

8 Buchungstext: Hier haben Sie die Möglichkeit, einen individuellen Buchungstext zu übergeben unter Benutzung von Schlüsselworten.

[Bild]

9 Wiederherstellen: Falls Sie versehentlich eine falsche Änderung in der Maske gemacht haben, können Sie durch Betätigung dieses Knopfes die Änderungen, die Sie seit dem letzten ‚Übernehmen‘ gemacht haben, rückgängig machen.

[Bild]

10 Ok speichern: Durch Betätigung dieses Knopfes werden die Einstellungen gespeichert und die Einstell-Maske wird geschlossen.

[Bild]

11 Abbruch: Durch Betätigung dieses Knopfes wird die Einstell-Maske ohne Übernahme von evtl. Änderungen geschlossen.

Karteikarte Eingangsrechnungen.

[Bild]

12 Ankreuzfelder:

[Bild]

Ankreuz-Feld „Übertragung nur der noch nicht gekennzeichneten Rechnungen“:

Jede Rechnung, die übertragen wird, erhält vom Programm eine Kennzeichnung. Durch ein Kreuz in diesem Feld werden alle Rechnungen, die dieses Kennzeichen besitzen, nicht mit ausgelagert. Dadurch wird erreicht, dass im Normalfall eine Rechnung nur einmal übertragen wird.

Ankreuz-Feld „stornierte Rechnungen übertragen“:

Durch ein Kreuz in diesem Feld werden auch stornierte Rechnungen ausgelagert. Die Wahl dieser Option ist nur sinnvoll, wenn die Schnittstelle zu Ihrer Fibu-Software auch den Rechnungs-Status überträgt.

Ankreuz-Feld „gesperrte Rechnungen nicht übergeben“:

Bei der Erfassung der Eingangsrechnung besteht die Möglichkeit eine solche auf gesperrt zu setzen. Dadurch wird verhindert, dass diese Rechnung bereits bezahlt wird, bevor die Unklarheiten beseitigt worden sind. Hier bieten wir Ihnen die Möglichkeit selbst festzulegen, ob diese bereits an die Fibu übergeben werden soll oder noch nicht. Da Sie bei eventuellen Korrekturen am besten mit Gutschriften arbeiten, empfehlen wir auch gesperrte Rechnungen an die Buchhaltung zu übergeben.

Ankreuz-Feld „Eigenen Zähler statt Rechnungsnummer im Logbuch eintragen“:

Da die Datev bei den Rechnungsnummern nur bis zu 6 Stellen zulässt, übergeben wir bei den Eingangsrechnungen grundsätzlich den eigenen Zähler und nicht die Rechnungsnummer des Lieferanten. In unserem Logbuch können Sie bei nicht gesetztem Schalter die Original-Rechnungsnummer einsehen. Wir empfehlen Ihnen allerdings auch dort auf den Belegzähler zu verweisen, da Sie dann bei Unstimmigkeiten das Problem wesentlich schneller eingrenzen können.

Ankreuz-Feld „Verteilung je Projekt“:

Wenn Sie hier ein Kreuz setzen, werden auch bei gleichen Warenkonten und wechselnden Projekten mehrere Datensätze an die Fibu übergeben.

Ankreuz-Feld „nur geprüfte Rechnungen übertragen“:

Durch ein Kreuz in diesem Feld erreichen Sie, dass nur geprüfte Rechnungen übertragen werden. Somit kann verhindert werden, dass eine Rechnung, bei der z.B. die Lieferung noch nicht vollständig erfolgt ist, schon an die Fibu übertragen wird.

Ankreuz-Feld „nicht je Konto + Kostenstellen zusammenfassen“:

Üblicherweise werden die Daten einer Eingangsrechnung zu einer Summe zusammengefasst, wenn das gleiche Konto, Kostenstelle und Projekt verwendet wurde.

Wenn Sie dieses Kreuz setzen, findet keine Zusammenfassung statt, es werden also in der Fibu genau so viele Datensätze angelegt, wie Verteilbuchungen vorhanden sind. Sinnvoll ist dies z.B. wenn Sie im Anlagevermögen der Fibu jedes Werkzeug einzeln gebucht haben wollen und Sie z.B. 3 Bohrmaschinen in einer Rechnung kaufen.

[Bild]

13 Buchungstext: Hier haben Sie die Möglichkeit, einen individuellen Buchungstext zu übergeben unter Benutzung von Schlüsselworten.
