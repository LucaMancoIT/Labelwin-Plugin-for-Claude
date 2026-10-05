# Mandantenverrechnung [Modul]

Pfad: Zeitwirtschaft > Mandantenverrechnung [Modul]
Quelle: handbuch/mandantenverrechnung__modul_.htm

|

Mandantenverrechnung [Modul]

06.09.2011

Zeitbuchungen und KD-Aufträge über Mandanten hinweg

Wenn jemand mehrere Firmen besitzt, die in Labelwin als Mandanten verwaltet werden, besteht oft das Bedürfnis, die Mitarbeiter eines Mandanten zeitweise auch beim anderen Mandanten einzusetzen. Das ist allemal besser als Leiharbeiter zu beschäftigen, während bei anderen Mandanten nichts zu tun ist. Im Prinzip leihen sich die Mandanten untereinander Mitarbeiter aus.

Da die Firmen buchhalterisch getrennt sein müssen, müssen jeweils Rechnungen untereinander gestellt werden müssen. Sowohl die Zeitbuchungen als auch die Rechnungsstellung sind relativ aufwändig. In der Zeiterfassung gibt es ohne das hier beschriebene Modul 3 Möglichkeiten:

1) die geliehenen Mitarbeiter werden bei den Einsätzen gar nicht gebucht, sondern die Zeit wird nur beim ‚Besitzer‘ auf ein Projekt ‚Ausleihen‘ gebucht. Die Kosten fallen dann beim anderen Mandat als Eingangsrechnungen an. Beim Einbuchen der Eingangsrechnung werden dann neben der Summe auch die Stunden gebucht.

2) Die Leiharbeiter werden zusätzlich als Personal angemeldet und so gebucht, als wenn es eigene Mitarbeiter wären. In diesem Fall muss darf die Eingangsrechnung nicht auf das Baustellen-Projekt gebucht werden, da dann die Kosten doppelt drin wären.

3) Die Stunden werden neutral als ‚Leiharbeiter‘ ohne Kostensatz gebucht. Die Kosten kommen über die Eingangsrechnung, bei der der dann aber keine Stunden eingetragen werden dürfen. Der Ausleiher muss dann die Zeiten ebenfalls buchen, am besten auf ein Projekt ‚Ausleihen‘, damit darüber die Rechnung erstellt werden können.

Alle diese Verfahren sind aufwändig und haben den Nachteil, dass entweder die Kosten der Leiharbeiter nicht zeitnah auf den Projekten stehen oder (beim Weg 2) die Mitarbeiterabrechnung bei allen Mandanten erfolgen muss und dann die Werte ggf. addiert werden müssen.

Bei dem neuen Verfahren lassen wir es zu, dass ein Mitarbeiter eines anderen Mandanten einfach gebucht werden kann. Damit sind die Kostenbelastungen der Projekte sofort sichtbar und in der monatlichen Monteurabrechnung sind alle Werte auf einem Ausdruck.

Über einen Menüpunkt im Modul ‚Selektieren‘ können automatisch alle Rechnungen an den jeweils anderen Mandanten erzeugt werden.

Wenn ein Mitarbeiter eines anderen Mandanten eingesetzt wird, darf dieser an sich nicht mit dem normalen Selbstkostensatz berücksichtigt werden. Richtig wäre es, die Selbstkosten um einen Anteil der Gemeinkosten des Verleihers zu erhöhen. Wir haben dies ermöglicht, indem man bei jedem Mitarbeiter neben den Selbstkosten in einem neuen Feld den ‚Internen Verrechnungssatz‘ erfassen kann. Mit diesem Satz werden dann die Kosten des Leiharbeiters angesetzt. Das hat aber den Nachteil, dass der Kostenblock beim jeweiligen Projekt steigt, der Deckungsbeitrag also sinkt. Wenn sich der Mitarbeitertausch etwa ausgleicht, sollten Sie dort den normalen Satz eintragen. Wenn aber ein Mandant regelmäßig Mitarbeiter leiht, ohne das ein Ausgleich stattfindet, sollte ein erhöhter Satz angewendet werden. Das ist auf jeden Fall gegeben, wenn z.B. ein Mandant keine eigenen Monteure hat.

An dieser Stelle wollen wir auf ein mögliches Problem hinweisen und die Lösung schildern. Wenn die Monteure mit den Kosten eingebucht werden und später die Eingangsrechnung auf das gleiche Projekt gebucht wird, stehen die Kosten doppelt auf dem Projekt. Man kann die Eingangsrechnung einfach auf ein ‚diverses‘-Projekt buchen, aber spätestens bei Nutzung unseres Controlling-Moduls mit der BWA-Tabelle tauchen die Kosten als allgemeine Kosten wieder auf.

Wir haben deshalb eine Möglichkeit geschaffen, die Lohnkosten aus der Zeiterfassung zunächst zu berücksichtigen und sie bei Einbuchen der Eingangsrechnung zu neutralisieren. Danach werden aus der Zeiterfassung nur noch die Stunden genommen und die Kosten aus der Eingangsrechnung. Unser erster Ansatz war hier, die Beträge in der Zeiterfassunfg einfach auf Null zu setzen, aber das hat Nachteile bei der Übernahme der Zeiten in eine Rechnung. In dieser würde dann der DB (Deckungsbeitrag) zu hoch dargestellt. Deshalb lassen wir die Kosten in den Zeitbuchungen drin und sorgen über ein Kennzeichen dafür, das diese beim Projektstand und der übergreifenden Projektauswertung nicht berücksichtigt werden.
