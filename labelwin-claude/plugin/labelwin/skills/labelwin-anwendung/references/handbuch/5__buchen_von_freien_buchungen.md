# 5. Buchen von freien Buchungen

Pfad: Buchhaltung > Fibuerfassung [25] > 5. Buchen von freien Buchungen
Quelle: handbuch/5__buchen_von_freien_buchungen.htm

|

5. Buchen von freien Buchungen

Statt die Buchungen auf ein Bankkonto zu beziehen, können Sie in der Hauptmaske das Buchen von freien Buchungen anwählen. In der Buchungsmaske werden dann nur noch die Belegarten „Bezahlen einer Eingangsrechnung ohne Zahlungslauf“ und sonstige Buchung angeboten. Im Grunde genommen handelt es sich hier um eine Buchung, die mit einer Kontoauszugerfassung nichts zu tun hat. Beide beteiligten Konten sind frei wählbar.

Die Ursache unserer Programmierung liegt darin, dass Sie hier Buchungen der Auszugserfassung, bei denen Sie das Fibukonto nicht wussten und daher einfach auf ein Konto „durchlaufender Posten“ gebucht haben, wieder in Ordnung bringen können. Unser Beispiel zeigt eine solche Buchung. Bei der Auszugserfassung war die Rechnung über die Internet-Gebühr nicht in Labelwin erfasst. Da bei der Erfassung die Zusammenhänge nicht klar waren, wurde die Summe von 78,50 € einfach auf das Konto 1370 gebucht. Nach der Klärung der Zusammenhänge wurde nun die gleiche Summe vom Konto 1370 auf das Konto 6810 gebucht. Das Konto 1370 ist dadurch wieder neutralisiert – es steht auf null. Allerdings darf auch jetzt die Rechnung nicht mehr im Labelwin Eingangsbuch eingetragen werden.

Wenn eine solche Rechnung im Nachhinein noch im Eingangsbuch eingetragen wird, so muss hier bei der freien Buchung die Belegart „Bezahlen einer Eingangsrechnung ohne Zahlungslauf“ angewählt werden. Um übrigens die Bezahlung einer solchen Rechnung über Labelwin zu verhindern, sollte man als Rechnungsstatus „Bankeinzug“ wählen. Anderenfalls könnte es passieren, dass bei einem Zahlungslauf diese Rechnung überwiesen wird, obwohl sie bereits abgebucht wurde. Gleiches gilt übrigens auch bei der Eintragung einer Eingangsrechnung, für die man dem Lieferanten bereits einen Scheck mitgegeben hat. Auch hier ist der Status auf ´Bankeinzug´ zu setzen.

Buchungsmakro: Auch hier kann man mit Buchungsmakros arbeiten. Eine Beschreibung finden Sie im folgenden Kapitel. Mit Buchungsmakros kann man wiederkehrende Buchungen sehr einfach vornehmen kann. Die Erstellung und Änderung von Buchungsmakros über den Knopf ‚Bearbeiten’ rechts neben der Auswahl.

Wichtig: Beachten Sie unbedingt, dass Sie bei einer freien Buchung kein Bankkonto ansprechen dürfen. Die Nutzung der Bankkonten muss immer über die Erfassung der Kontoauszüge stattfinden. Anderenfalls wird der Kontenstand der Bank falsch angezeigt. Arbeiten Sie einfach mit einem Geldtransit-Konto um Beträge zwischen den Banken zu verschieben.
