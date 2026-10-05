# 9. Statusmeldungen, Mitteilungen ans Büro

Pfad: Kundendienst > KD-Mobil Notebook [Modul] > 9. Statusmeldungen, Mitteilungen ans Büro
Quelle: handbuch/9__statusmeldungen__mitteilungen_ans_buro.htm

|

9. Statusmeldungen, Mitteilungen ans Büro

|

Hinweis: Die nachstehend beschriebenen Möglichkeiten sind nur bei der Datenübertragung per Cloud-Abgleich (z.B. Dropbox) möglich.

THEMA

|

Bei den Statusmeldungen geht es darum, dem Büro mehr Übersicht über die Mitarbeiter zu geben. Die mobilen Mitarbeiter können sehr einfach eine Meldung über ihren „Status“ abgeben und das Büro kann sehen, wer wo ist und was macht. Dabei geht es nicht um Überwachung, sondern darum, die Kommunikation zu verbessern Das Büro kann bei Verspätungen den nächsten Kunden informieren, sehen wo sich ggf. noch ein Noteinsatz einschieben lässt, bei Nachfragen sehen, dass der Mitarbeiter auf dem Weg zurück zum Büro ist (und man ihn deshalb nicht anrufen muss) und vieles mehr.

EINRICHTUNG

|

|

Die Statusmeldungen sind frei erfassbar. Es befindet sich ein Grundstandard auf Ihrem Rechner, den Sie beliebig verändern können. Die Meldungen können im Modul Einstellungen unter dem Menüpunkt [Mobil] - [Statusmeldungen] erfasst und verändert werden. Dort müssen Sie auch festlegen, dass Sie mit den Meldungen arbeiten wollen.

Bei der Wahl der Verwendung legen Sie fest, an welcher Stelle die Meldung angeboten wird. Das ist die die oberste Ebene, an der oft „neutrale“ Meldungen ohne Auftragsbezug abgesetzt werden und im geöffneten Auftrag in der Regel mit Auftragsbezug.

Bei den Meldungsvorlagen können Sie festlegen, bei welchen die Auftragsnummer mit gesendet wird und bei welchen nicht.

Ankreuzfeld „Mit Standortaufzeichnung“:

Mit gesetztem Haken versuchen die verwendeten Geräte den Standort zu bestimmen, an dem die Meldung abgesetzt wird. Dies funktioniert bei einem Smartphone und der App iDeXs fast immer, bei Einsatz des mobilen Kundendienstes per Tablett oder Notebook meist nur auf den neueren Geräten. Auf jeden Fall müssen Sie die Aufzeichnung mit Ihren Mitarbeitern absprechen, da davon die Persönlichkeitsrechte Ihrer Mitarbeiter betroffen sind.

Zusammen mit der neuen Kartenanzeige per Google (kostenpflichtiges Zusatzmodul) können nun die Standorte der letzten Statusmeldung aller Mitarbeiter angezeigt werden.

|

[Bild]

Abholen der Meldungen:

|

Zur Nutzung gehört, dass die Meldungen regelmäßig abgeholt werden. Dazu gibt es ein neues Modul, das auf einem Arbeitsplatz oder noch besser auf dem Server selbst gestartet werden muss. Es hat den Namen StatusImport.exe und liegt im Labelwin-Verzeichnis. Am besten erstellen Sie eine Verknüpfung auf die Datei oder binden sie im Startcenter ein. Das Programm sollte nur auf einem Rechner gleichzeitig laufen.

Mit der Zeitsteuerung schaut das Modul regelmäßig nach, ob neue Meldungen von iDeXs oder Mobilkd vorliegen und verarbeitet diese. Die zuletzt abgeholte Meldung wird nur zur Info gezeigt. In der Einführungsphase kann man damit gut testen.

|

[Bild]

|

Tipp: Wird die statusimport.exe auf dem Server ausgeführt, sollte eine Verknüpfung auf die statusimport.exe in den Autostart gelegt und in den Eigenschaften der Verknüpfung der Eintrag „L:\labelwin\statusimport.exe /auto“ erfolgen. Durch den Parameter /auto wird das Programm direkt in den Abholmodus versetzt. Die Zeitsteuerung muss nicht zusätzlich aktiviert werden.

ANWENDUNG

|

Anwendung im Mobilen Kundendienst

Es gibt 2 Stellen, an denen die Meldungen abgesetzt werden können.

-

Von der obersten Ebene im Menü <Datei>

-

Aus dem geöffneten Auftrag mit dem Button „Statusmeldungen“ für Meldungen mit Bezug zum geöffneten Auftrag.

Bei den Knöpfen in Gelb ist hinterlegt, dass sie sofort gesendet werden und sich die Maske schließt. Bei den anderen Knöpfen ist eine Texteingabe möglich, die erst mit dem „Senden“-Button raus geht.

[Bild]

Da für beide Situationen festgelegt wird, welcher Button sichtbar ist, kann die Maske je nach Startpunkt unterschiedlich aussehen.

Statusmeldung aus Büro-Auftragsmaske:

Es gibt einige Betriebe, bei denen auch im mobilen Kundendienst mit der Büromaske gearbeitet wird. Damit auch diese Statusmeldungen absetzen können, gibt es diese Möglichkeit auch über das Menü <Datei> im geöffneten Auftrag.

Der Überblick (nur in V5-Version):

Im Kundendienst finden Sie unter <Auswerten> den neuen Punkt <KD-Mobil Status>.

[Bild]

In der oberen Tabelle sehen Sie alle Mitarbeiter mit mobilem Gerät und deren letzte Statusmeldung. In der unteren Tabelle sehen Sie alle noch offenen Aufträge des oben markierten Mitarbeiters.

Diese Maske ist vom sonstigen Programm abgekoppelt, so dass sie dauerhaft geöffnet sein kann.

Anzeige sämtlicher Statusmeldungen

Die Statusmeldungen gibt es schon lange. Auch die Meldungen von TomTom werden im gleichen Bereich abgelegt. Sämtliche Statusmeldungen mit Eingrenzung auf einen Mitarbeiter oder auf einen bestimmten KD-Auftrag können im Kundendienst angezeigt werden. Die Menüpunkte finden Sie unter dem Menüpunkt <Export / Import>

Meldungen aus der Zentrale zum mobilen Gerät:

Auch in der Zentrale können Meldungen / Informationen zum Mitarbeiter geschickt werden. Dies geschieht von der obersten Ebene aus unter den Menüpunkten <Export / Import>, <KD-Meldungen>. Hier gibt der Rückgriff auf Bausteine aber keinen großen Nutzen. Stattdessen ist es möglich, einen Text an beliebig viele Mitarbeiter auf einen Rutsch zu senden.
