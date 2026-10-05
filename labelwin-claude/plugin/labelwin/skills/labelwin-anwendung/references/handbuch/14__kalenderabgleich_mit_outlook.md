# 14. Kalenderabgleich mit Outlook

Pfad: Kundendienst > Kundendienst [6] > 14. Kalenderabgleich mit Outlook
Quelle: handbuch/14__kalenderabgleich_mit_outlook.htm

|

14. Kalenderabgleich mit Outlook

Mit diesem Modul wird es Ihnen ermöglicht, die im Kundendienst und im Kalender geplanten Termine entweder vollautomatisch an Outlook zu übergeben oder bei Bedarf durch einen manuellen Start alle bis dahin durchgeführten Terminänderungen zu übertragen. Voraussetzung hierfür ist eine installierte Outlookversion auf den entsprechenden Rechnern.

Wenn Sie einen Exchangeserver einsetzen, kann der Abgleich automatisch bei jeder Änderung im Kundendienstmodul erfolgen.

Der Abgleich ist eine Einbahnstrasse, es werden nur die Termine von Labelwin an Outlook übergeben. Bei einer Verschiebung im Outlook bleibt der Termin im Label unverändert. Wenn der Auftrag in Label neu gespeichert wird, wird eine ggf. stattgefundene Verschiebung wieder vernichtet.

Eine Verschiebung im Labelwin bewirkt auch eine Verschiebung im Outlook.

Einrichtungsarbeiten im Labelwin:

Zunächst muss im Einstellmodul unter <Grundeinstellungen> <Allgemein> die Art des Outlookabgleichs konfiguriert werden.

[Bild]

Beim Exchangeserver kann der Abgleich zu jeder Zeit stattfinden, wenn alle Anwender ihre Kalender im Outlook freigegeben haben. Das hört sich zunächst positiv an, aber bei manchen Exchange-Servern kommt immer die folgende Meldung bei jeder Termineintragung. Das ist so störend, dass man besser die 3. Möglichkeit anwählt, mit der der Abgleich manuell ausgelöst wird. Dann kommt die Meldung nur einmal.

[Bild]

Da nicht automatisch festgestellt werden kann, ob Outlook vorhanden ist und ob ein Exchange-Server existiert, müssen Sie die Option richtig einstellen. Bitte nehmen Sie ggf. Kontakt mit Ihrem Hardware-Betreuer auf.

Zusätzlich müssen Sie in der Personalverwaltung für alle Mitarbeiter, deren Kalender abgeglichen werden sollen, zwingend drei Eintragungen vornehmen. Das Programm zunächst feststellen, wer gerade seinen Kalender abgleichen will. Das geschieht über den Eintrag ‚Labeluser’. Danach muss das Programm den Kalender finden, was über die Emailadresse möglich ist.

1. Labeluser Zuordnung

Tragen Sie hier den Windows-Anmeldenamen ein.

[Bild]

2.+3. Kontoname und Ablgeich aktivieren

Auf der Karteikarte ‚Zuordnung’ muss der Kontoname gefüllt sein und der Schalter für den Abgleich aktiviert werden.

[Bild]

Über diese E-Mail-Adresse kann man im Exchange-Server den Kalender des entsprechenden Mitarbeiters finden.

Einrichtungsarbeiten im Outlook (bei Exchange-Server):

Alle Kalender müssen im Outlook für alle Mitarbeiter freigegeben sein. Es müssen die Rechte für ändern, neu eintragen und löschen gesetzt worden sein.

Leider sind diese Einstellungen in jeder Outlookversion etwas anders. Fragen Sie bitte ggf. Ihren Hardwarebetreuer.

Arbeiten im Kalender mit Exchange-Server

Sie brauchen nichts weiter zu beachten, da alle Termine, die ab jetzt eingetragen oder verändert werden, automatisch im Outlook eingetragen werden.

Arbeiten im Kalender mit manuellem Start

[Bild]

Im Modul Kalender/Balkendiagramm erhalten Sie einen neuen Menüpunkt mit der Beschriftung ‚Outlook’.

Wenn Sie hier den Punkt Abgleich anwählen, werden alle Terminänderungen, die für den angemeldeten Windows-User vorgenommen wurden, an das aktive Outlook übergeben. Diesen Outlook-Abgleich kann man nur für seinen eigenen Kalender durchführen.

Beim Komplettabgleich werden die Label Kalender Einträge an Outlook übergeben und im gleichen Zuge die Outlook Einträge nach Labelwin übernommen.

Der Menüpunkt Kalender einlesen bewirkt, dass die Outlook Einträge nach Labelwin übernommen werden.
