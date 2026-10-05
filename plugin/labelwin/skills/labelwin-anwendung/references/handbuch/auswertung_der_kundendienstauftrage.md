# Auswertung der Kundendienstaufträge

Pfad: Auswertungen / Controlling > Auswertungen [21] > Auswertung der Kundendienstaufträge
Quelle: handbuch/auswertung_der_kundendienstauftrage.htm

|

Auswertung der Kundendienstaufträge

|

Bei dieser Beschreibung geht es um eine übergreifende Kundendienstauswertung über alle Aufträge hinweg. Die Auswertung eines einzelnen Auftrages geschieht im Modul KUNDENDIENST unter dem Menüpunkt <Auswerten> <Einzelner Auftrag>.

Um die Kundendienstaufträge nach verschiedenen Kriterien auswerten zu können, muss zunächst eine Auswertungsdatei erzeugt werden. Dies geschieht im Modul PROJEKTE unter dem Menüpunk [Projekt - Statistik - Daten erzeugen] oder im KUNDENDIENST unter [Auswerten - Alle Aufträge]. Wählen Sie in dieser Maske den Auswertungsbereich „Kundendienst” an.

Je nach Anzahl der Aufträge kann der Aufbau der Auswertungsdatei einige Zeit in Anspruch nehmen. In Netzwerken empfehlen wir Ihnen, die Erzeugung der Daten zu einer Zeit vorzunehmen, in der nicht viel Bewegung im Netz ist.

|

Wichtig: Die Datumseingrenzung greift nur auf das Datum des Auftrages und nicht auf die zugeordneten Kosten. Es werden immer alle Kosten eines Auftrages in die Auswertungsdaten geschrieben, auch wenn die Kosten selbst nicht in dem angegebenen Zeitrraum entstanden oder gebucht wurden.

Bei den Auswertungen greifen wir immer wieder auf diese Zwischendatei zu, so dass später keine großen Zeitverzögerungen entstehen. Dieses Verfahren hat allerdings den Nachteil, dass die Auswertungen immer den Stand zur Zeit der Erzeugung der Zwischendatei haben. Bei vorgenommenen Änderungen muss also die Auswertungsdatei neu erzeugt werden, damit diese in den Auswertungen sichtbar werden.

|

[Bild]

Ausgabe

Die Ausgabe der Auswertung kann wie bei allen anderen Auswertungen auch über beliebige Formulare erfolgen. Die Formulare sind mit Hilfe des Programms Crystal Report innerhalb gewisser Grenzen frei gestaltbar.

Standardmäßig werden folgende Formulare mitgeliefert:

|

KY1

KY2

KY3

KY4

KY5

KY6

KY-Komp

|

Liste mit Rg.-Summe, Zeit ,DB und DB/std

Liste nach Monteur mit Rg.-Summe, Zeit ,DB und DB/std

Liste mit Stundenarten mit Rg.-Summe, Zeit ,DB und DB/std

Liste nach Anlagearten mit Rg.-Summe, Zeit ,DB und DB/std

Liste nach Auftragsart mit Rg.-Summe, Zeit ,DB und DB/std

Garantiearbeiten

Liste mit allen Daten

Bei den mitgelieferten Formularen wird der Deckungsbeitrag jeweils aus den Summen der Rechnung und der Zeitwirtschaft ermittelt (wie bei der Eingrenzung ‚DB aus RG’)

Ausgabefelder

Der Reportgenerator Crystal Report erlaubt Ausgaben aus den Tabellen der beiden am Auftrag beteiligten Adressen, alle Feldern des Kundendienstauftrages und der Zwischendatenbank.

Die für diese Auswertungen zusammengetragenen Werte liegen in der Zwischendatenbank projausn.mdb. Sollten Ihnen auf den standardmäßig ausgelieferten Formularen Angaben fehlen, sprechen Sie uns an. Wir können dann für Sie ein individuell erstelltes Formular gestalten. Bitte haben Sie Verständnis dafür, dass für Sie individuell angepassten Formulare nicht in der Softwarepflege enthalten sind und separat bezahlt werden müssen.
