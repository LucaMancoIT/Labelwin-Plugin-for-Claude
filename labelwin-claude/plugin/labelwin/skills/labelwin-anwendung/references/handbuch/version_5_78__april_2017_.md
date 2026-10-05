# Version 5.78 (April 2017)

Pfad: Updatetexte (bisher) > Update 2017 > Version 5.78 (April 2017)
Quelle: handbuch/version_5_78__april_2017_.htm

|

Version 5.78 (April 2017)

Versionswechsel auf 5.78 - Änderungen April 2017

Zahlungsbedingungen mit unkenntlicher Iban

Aus Datenschutzgründen ist es erforderlich, dass bei Rechnungsversand per E-Mail die IBAN nicht komplett sichtbar, sondern mindestens die letzten 4 Stellen mit xxxx ausgegeben werden. Beim Versand per Post ist dies nicht erforderlich.

Deshalb wurde ein neues Schlüsselwort für Zahlungsbedingungen geschaffen: @TxIbanX@ (die Groß / Kleinschrift ist egal)

Rechnungsversand per Email mit Arbeitsbericht

Bei dieser Option wurde zwar der gescannte Arbeitsbericht dazu gepackt, aber bei der Nutzung von Folgeaufträgen fehlten die Berichte der Folgeaufträge.

Update einspielen erleichtert

Solange ein Anwender im Labelwin angemeldet ist, kann kein Update eingespielt werden. Dies ist besonders ärgerlich, wenn der Mitarbeiter nicht mehr da ist und sich nur vergessen hat, sich abzumelden. Wir haben nun eine Möglichkeit gefunden, den Anwender automatisiert abzumelden. Er bekommt dann eine Meldung auf den Bildschirm und hat die Möglichkeit innerhalb von 60 Sekunden zu widersprechen. Wenn er wirklich gerade arbeitet, kann er also den Abmeldevorgang aufhalten. Wenn innerhalb der Zeit kein Widerspruch kommt, werden alle Anwender abgemeldet und das Update kann eingespielt werden.

Bestellüberwachung, geänderte Anzeige der offenen Artikel

Die Anzeige der noch nicht gelieferten (überfälligen) Artikel wurde so geändert, dass nun zunächst der Lieferant, die Objektadresse, die bestellte Menge und die Fehlmenge gezeigt wird. Bisher konnten die wichtigsten Informationen in der Anzeige nicht sofort erkannt werden. Die Bestellüberwachung gibt es als separates Modul und als Bestandteil der Lagerverwaltung.

Rechnungen ungültig kennzeichnen (statt Storno)

Mit der Berücksichtigung der GoBD in unserem Programm war es nicht mehr möglich, fehlerhafte Rechnungen erneut auszudrucken. Wir hatten diesen Weg gewählt, weil uns die Alternative, alle Änderungen für einen Prüfer zu dokumentieren, nicht möglich schien.

Wir haben nun noch mal viel Zeit investiert und einen Weg gefunden, Rechnungen ohne Stornobuchungen aber mit Dokumentation der Änderungen mit der gleichen Nummer zu drucken. Um das gleich klar zu stellen – Betrug ist damit auch verhindert.

Solange eine Rechnung das Haus nicht verlassen hat oder wenn das Original vorliegt, erlauben wir es, die Eintragung im Rechnungsausgangsbuch als UNGÜLTIG zu kennzeichnen. Die Aktion selbst passiert aber im Modul Projektverwaltung.

Die Rechnung bekommt neben dem Kommentar ‚ungültig‘ das ‚x‘ für stornierte Rechnungen. Ob das erste Original vorliegt, kann die EDV natürlich nicht wirklich prüfen. Dazu gibt es ein Ankreuzfeld, mit der der Anwender dies bestätigt. Erst dann kann der Vorgang stattfinden. Es wird protokolliert, wer wann welche Rechnung als ungültig erklärt hat.

Um eine Rechnung als ungültig zu kennzeichnen, muss in der Projektverwaltung die Rechnung markiert sein und der Menüpunkt zum Stornieren angewählt werden. In der dann erscheinenden Maske kann gewählt werden, ob die Rechnung ungültig werden soll, storniert oder eine Gutschrift erzeugt werden soll. Rechnungsausgangsbuch der ‚alten‘ Version 4.xx ist die Anwahl von ‚ungültig‘ nicht möglich.

Mit der Kennzeichnung als ‚ungültig‘ wird eine Kopie erstellt, die dann überarbeitet werden kann. Beim Drucken kann die neue Rechnung dann nur mit der bisherigen Nummer NEU im Rechnungsausgangsbuch eingetragen werden. Es kann dann also eine Rechnungsnummer mehrfach in der Liste vorkommen, wobei nur die letzte gilt und Vorversionen mit ‚x‘ (steht an sich für storniert) und ‚ungültig‘ gekennzeichnet sind.

Ungültige Rechnungen werden nicht in eine Finanzbuchhaltung übertragen.

Sobald eine Rechnung übertragen worden ist, kann sie nicht mehr auf ‚ungültig‘ gesetzt werden.

Intern sind die alten ungültigen Rechnungen miteinander verkettet. Im Protokoll einer einzelnen Rechnung im Rechnungsausgangsbuch (Menüpunkt <Bearbeiten>, <Protokoll>) sieht man deshalb nicht nur die Daten der markierten Rechnung, sondern auch die der vorigen Version. Sinngemäß zeigt das Protokoll also alles, was mit der Rechnungsnummer passiert ist.

Im Dokumentenprotokoll ist sichtbar, was gegenüber der Vorversion geändert wurde. Keine der Rechnungen kann gelöscht oder verändert werden. Das erste Original sollte bei der Papierablage dazu geheftet werden (damit der Prüfer was zu prüfen hat) und steht bei Nutzung des PDF-Archivs auch dort zur Verfügung.

|

Nachtrag 11.5.2017

In der Rechteverwaltung kann eingestellt werden, dass einzelne Mitarbeiter Rechnungen weder stornieren, noch das Kennzeichen ‚zu stornieren‘ und auch nicht für ungültig erklären können. Ausführliches weiter hinten!

Kassenbuch, Scannen der Belege

Im Kassenbuch können nun auch die Belege eingescannt werden. Das funktioniert aber nur mit dem Scan-Archiv und nicht mit Elo. Zur Aktivierung müssen Sie im Einstellmodul unter den Menüpunkten <Programmbereiche>, <Archiveinstellungen> den nebenstehend abgebildeten Schalter setzen.

[Bild]

Kassenbuch, Zuordnung zu KD-Auftrag

Im Kassenbuch können Belege einem Kundendienstauftrag zugeordnet werden. Damit die möglicherweise speziell für Sie angepassten Druckformulare nicht geändert werden müssen, werden diese Einträge in der KD-Auswertung unter der Rubrik ‚Eingangsrechnung berücksichtigt. Sinngemäß sind sie das ja auch.

Fibuschnittstelle Datev neue Version

Die alte Datev-Schnittstelle gilt nur noch bis Ende 2017. Sie können aber schon jetzt auf die neue Schnittstelle umstellen.

Dazu müssen Sie in der Startmaske den Knopf Einstellungen anwählen.

[Bild]

[Bild]

Geben Sie danach in der Maske das Datev-Wirtschaftsjahr ein. Alles andere läuft wie gewohnt. Im Ablagepfad finden Sie dann die neuen Dateien im Format EXTF_Buchungsstapel_lfdnr.

Diese übergeben Sie dem Steuerberater oder importieren sie selbst, wenn Sie die Datev im Haus haben.

Anrufliste im Kontextmenü (rechte Maustaste)

Wenn von einer Adresse die Informationen gezeigt werden, kann man mit der Menü diverse Funktionen wie ‚Anrufen‘ uvm. anwählen. Nun kann dort auch die Anrufliste gezeigt werden. Hintergrund: Wenn jemand mit den Worten anruft „… jemand aus Ihrer Firma hat versucht mich zu erreichen …“ kann man nun sehen, wer das wohl war. Natürlich funktioniert dies nur bei aktivem Tapimodul.

iDeXs-Stammdaten überarbeitet

Die Veröffentlichung der iDeXs V2 – Version steht unmittelbar bevor (geschrieben am 4.5.2017), so dass die Maske an die neuen Möglichkeiten angepasst werden musste. Wir haben dies zu einer kompletten Überarbeitung genutzt und auch die sonst beim Personal zu hinterlegenden Daten in diesen Bereich gezogen. Da nahezu alle Ankreuzfelder und Eingaben einen Hilfeknopf haben, verzichten wir hier auf die weiteren Beschreibungen.

In Kürze wird auch das neue Handbuch für diesen Bereich veröffentlicht, so dass alles nachzulesen ist.

[Bild]

Viessmann-Konfigurator

Einige unserer Kunden setzen den Heizungskonfigurator von Viessmann ein. Dieser erzeugt eine UGL-Datei, die im Labelwin wie jede andere UGL eingelesen werden. Allerdings gibt es eine Besonderheit, um Minuten und Einkaufspreise zu übernehmen. Dazu wird die mobile offer-Erweiterung genutzt.

Allerdings werden bisher bei UGL-Dateien Sets als verborgen übernommen, weil die Bestandteile üblicherweise die zu bestellenden Materialien sind, die der Endkunde nicht sehen soll. Bei der UGL vom Viessmann-Konfigurator enthalten aber die Bestandteile die wichtigen Informationen. Deshalb müssen Sie bei dieser Übernahme den Haken unten links setzen.

[Bild]

Rechnungen stornieren / für ungültig erklären – weitere Berechtigungen

Das Thema ist bereits einige Seiten vorher beschrieben, aber wurde im Nachhinein noch um neue Funktionen erweitert.

1) Wenn eine Firma nie mit der ‚Ungültig‘-Methode arbeiten möchte, kann sie die komplett verhindern. Zu finden ist die Einstellung Im Modul Einstellungen, <Programmbereiche>, <Buchhaltung> auf der Karteiseite ‚Ausgangsrechnungen‘

2) Der Stornovorgang selbst kann über 2 Rechte abgesichert werden:

[Bild]

Das erste Recht gibt es schon länger, nur der Beschreibungstext wurde verbessert. Wer dieses Recht hat, darf alles was im Rahmen der GoBD möglich ist.

Wenn jemand dieses Recht nicht hat, greift das zweite, jetzt neu eingerichtete Recht. Der Anwender darf Rechnungen mit dem Kennzeichen ‚Zu stornieren‘ versehen und darf auch Rechnungen für ungültig erklären.

Wenn der Anwender keines der beiden Rechte hat, darf er weder stornieren noch eine Rechnung für ungültig erklären. Bei einem Fehler muss er sich also an einen Mitarbeiter wenden, der über diese Rechte verfügt.
