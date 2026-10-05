# Fibuerfassung [25]

Pfad: Buchhaltung > Fibuerfassung [25]
Quelle: handbuch/fibuerfassung__25_.htm

|

Fibuerfassung [25]

Stand: 06.05.2019

(V5.89)

THEMA

|

Das Programm-Modul FIBU-ERFASSUNG erhebt keinen Anspruch darauf, ein Fibu-Programm zu ersetzen. Es ist entwickelt worden, damit die Zahlungseingänge von Kunden nicht doppelt erfasst werden müssen. Zumindest die Zahlungseingänge der Kunden müssten sonst sowohl in der Fibu, als auch im Modul Rechnungsausgangsbuch eingetragen werden. Ohne die Eintragung im Labelwin-Bereich können die offenen Posten im Modul KUNDENDIENST nicht gezeigt werden und das MAHNWESEN nicht genutzt werden.

Eigentlich wäre es Sache der Fibu-Programme, die Daten der Zahlungseingänge an Labelwin zu liefern – da dies jedoch kaum eine Fibu kann, haben wir dieses Kontoauszug-Erfassmodul programmiert. Wir liefern die Informationen über Zahlungseingänge und Bezahlung von Eingangsrechnungen zum einen in ein Journal, das später an die Fibu übergeben wird und zum anderen an das Rechnungseingangs- und Ausgangsbuch von Labelwin.

Bei Nutzung dieses Programmmoduls reduziert sich die Tätigkeit des Steuerberaters auf die Kontrolle der Daten und Durchführung der Abschreibungen.

Obwohl es in erster Linie zum Buchen der Bank-Kontoauszüge entwickelt wurde, können Sie mit dem Programm auch freie Buchungen vornehmen. Beim Buchen der Kontoauszüge ist das erste Konto immer das Bankkonto und nur das zweite (Gegenkonto) wechselt. Bei einer freien Buchung können Sie beide Konten beliebig wählen.

Durch die Möglichkeit einer freien Buchungserfassung kann das Programm im Grunde genommen nur von jemandem genutzt werden, der mindestens zur Vorkontierung der Belege in der Lage ist. Da die Auszüge der Bank alle chronologisch erfasst werden müssen, muss jede Eintragung auch dem entsprechenden Konto zugeordnet werden können. Während dies bei Geldbewegungen wie Ausgangsrechnungen oder Eingangsrechnungen von Labelwin automatisch abläuft, müssen Buchungen wie Lohnzahlungen, Krankenkassen, Versicherungen und dergleichen dem entsprechenden Fibu-Konto zugeordnet werden. Im Zweifelsfall muss als Gegenkonto so etwas wie „Durchlaufende Posten“ gewählt werden, damit der Kontenstand für die Folgebuchungen richtig ausgewiesen wird. Der Eintrag auf dem „Durchlaufende Posten“-Konto muss dann in der Fibu oder über eine freie Buchung auf das richtige Konto umgebucht werden.

Bei Buchungsfehlern, die vor der Übergabe an die Fibu auffallen, kann eine Buchung gelöscht und neu erfasst werden. Beim Löschen der Buchung werden eventuell dahinter liegende Ausgangs- oder Eingangsrechnungen wieder in den vorigen Zustand gestellt. Konkret: Beim Löschen einer Buchung, die einen Zahlungslauf (= Summe von mehreren Eingangsrechnungen) betrifft, werden alle Rechnungen wieder auf offen bzw. „im Zahlungslauf“ gesetzt.

Wir möchten an dieser Stelle schon davor warnen, einer mit unserem Programm erzeugten Zahlungsliste (= Ausgabe als Bankdisk) im Bankprogramm noch weitere Überweisungen wie z.B. Löhne hinzuzufügen. In diesem Fall erscheint alles im Kontoauszug der TAN-Nummer in einer Summe und eine Zuweisung zu einem Zahlungslauf wird sehr schwer. Am besten ist es, wenn zu einer Summe auf dem Auszug nur eine Rechnung oder ein Zahlungslauf existiert. Wenn Kunden mehrere Rechnungen in einer Summe bezahlen, müssen hier mehrere Buchungen vorgenommen werden. Zu diesem Themenkomplex finden Sie weiter hinten in der Anleitung entsprechende Beispiele.

Mit Hilfe des Zusatzmoduls KONTOAUSZUGSMANGER können Sie die Kontoauszüge der Bank als Datei einlesen und halbautomatisch verarbeiten lassen. Dieses ermöglichen nahezu alle Banken, wobei die Struktur der Daten unterschiedlich ist. Über die Einstellung im Auszugsmanager lässt sich eine Anpassung an fast jedes Format vornehmen.

Wir möchten an dieser Stelle auch darauf hinweisen, dass Label keine Betreuung im Sinne von „welches Konto muss ich denn hier nehmen“ vornehmen wird. Unsere Betreuung bezieht sich ausschließlich auf die Handhabung des Programms.

VORAUSSETZUNGEN

|

Die Fibu-Erfassung ist ein kostenpflichtiges Zusatzmodul. Nach Erwerb und entsprechender Einrichtung, die nachfolgend erklärt wird, kann das Modul eingesetzt werden.

EINRICHTUNG

|

Bevor Sie mit dem Programm-Modul FIBU-ERFASSUNG arbeiten, sollten Sie alle Zahlungseingänge und Zahlungsausgänge auf erledigt setzen, die Kontoauszüge betreffen, die Sie nicht mehr erfassen möchten. Anders ausgedrückt, es sollten nur noch die Zahlungsläufe und Ausgangsrechnungen offen sein, die bei den künftig erfassten Kontoauszügen verbucht werden. Von dem Moment an, in dem Sie die Auszüge mit dem neuen Modul erfassen, dürfen Sie keine Zahlungen mehr manuell auf erledigt setzen. Anderenfalls können Sie die entsprechende Buchung auf dem Kontoauszug nicht mehr erfassen. Langfristig wird evtl. die Erfassung von Zahlungen im Modul Eingangs- und Ausgangsrechnungen blockiert. Bis dahin müssen Sie einfach entsprechend mit dem Programm umgehen und Rechnungen nur noch über dies Modul auf erledigt setzen.

Vor der erstmaligen Benutzung des Programms müssen unbedingt alle erforderlichen Grunddaten erfasst werden. Lesen Sie dazu bitte das nächste Kapitel Erforderliche Grundeinstellungen.
