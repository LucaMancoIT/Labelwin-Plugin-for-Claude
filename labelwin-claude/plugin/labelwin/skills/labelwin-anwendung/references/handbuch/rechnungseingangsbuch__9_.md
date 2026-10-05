# Rechnungseingangsbuch [9]

Pfad: Buchhaltung > Rechnungseingangsbuch [9]
Quelle: handbuch/rechnungseingangsbuch__9_.htm

|

Rechnungseingangsbuch [9]

Stand: 05.10.2018

(V5.87)

|

[Bild]

|

Das Rechnungseingangsbuch wird aus dem Programmbaum heraus gestartet.

Die Verwaltung und Zahlungsabwicklung von Eingangsrechnungen gehört klassischerweise in eine Finanzbuchhaltung. Wir haben dieses Modul in erster Linie programmiert, um die Zuordnung der Rechnungen auf einzelne Baustellen/Projekte vornehmen zu können. Selbst wenn in einer FIBU eine Projektzuordnung möglich ist, kann dort dennoch keine Prüfung auf bei uns angelegte Projekte erfolgen. Ebenso taucht das Problem der Übergabe an unser Programmsystem auf. Die Nachkalkulation einer Baustelle kann nur dann sinnvoll vorgenommen werden, wenn auch die Eingangsrechnungen kostenmäßig berücksichtigt werden.

Hinweis: An dieser Stelle möchten wir noch auf die Möglichkeit von Lagerentnahmedokumenten hinweisen: Artikel, die nicht speziell eingekauft, sondern vom Lager entnommen werden, können unabhängig vom Vorhandensein der Lagerverwaltung in den Auswertungen berücksichtigt werden. Dazu muss in der Dokumentenverwaltung lediglich ein Dokument mit der Art ‚Lagerentnahme‘ erfasst werden. Alle dort hinterlegten Artikel werden kostenmäßig bei der Nachkalkulation genauso berücksichtigt wie die Eingangsrechnungen.

Wir haben diesen Programmbereich so entwickelt, dass Sie weitgehend alle Vorgänge Ihres Betriebes mit Eingangsrechnungen hierüber abwickeln können. Es ist jedoch nicht möglich, regelmäßig wiederkehrende Zahlungen einzutragen. Obwohl Rechnungen auf mehrere Baustellen verteilt werden können, empfehlen wir Ihnen, von Ihren Lieferanten die Rechnungen kommissionsweise zu verlangen. Dadurch ersparen Sie sich die Berechnung von Zwischensummen.

Bevor Sie Eingangsrechnungen erfassen können, müssen Sie unbedingt im Modul EINSTELLUNGEN unter <Programmbereiche> <Buchhaltung> <Grundeinstellung> die erforderlichen Einstellungen vornehmen. Für die Übergabe an eine Finanzbuchhaltung müssen dort auch die verwendbaren Warenkonten eingetragen werden.

Bevor auf einen Lieferanten eine Rechnung buchen können, muss die Lieferantenadresse erfasst sein. Zwingend erforderlich ist dort die Hinterlegung der Bankdaten und Zahlungsziele. Wenn Sie die Rechnungen an eine Fibu übergeben möchten, ist es ebenfalls zwingend erforderlich, dort die Kreditorennummer einzutragen.

Bei der Bezahlung der Eingangsrechnungen werden die ausgewählten Rechnungen immer zu einem Zahlungslauf zusammengefasst. Der Zahlungslauf ist also nur eine Liste, in der alle zu bezahlenden gewählten Rechnungen enthalten sind. Die Rechnungen eines Zahlungslaufes können per Überweisung, per Scheck oder per Diskette/Modem bezahlt werden. Die Zahlungsweise gilt stets für den kompletten Zahlungslauf. Wenn mehrere Rechnungen eines Lieferanten in einem Zahlungslauf enthalten sind, so werden diese zu einer Summe zusammengefasst. Dabei erstellt das Programm automatisch ein Begleitschreiben, in dem der Zahlungsempfänger darüber informiert wird, welche Rechnungen mit Skonto, ohne Skonto und dergleichen erledigt worden sind. Dieses Begleitschreiben kann per Brief oder Fax gesendet werden.

Die in einem Zahlungslauf gewählten Rechnungen stehen nicht automatisch auf bezahlt, sondern bekommen den Status ‚im Zahlungslauf’. Bei Nutzung des Zusatzmoduls Fibuerfassung werden die Rechnungen bei Buchen des Kontoauszugs auf ‚bezahlt‘ gesetzt. Ohne dieses Modul können Sie die Rechnungen durch Anwahl des Menüpunkts <Zahlungen> <Bezahlt setzen Zahlungslauf> umsetzen. Dabei wird die Buchung für den kompletten Zahlungslauf auf einmal durchgeführt.

Auf den ersten Blick mag es irritieren, dass wir immer von Bankdiskette sprechen. Für unser Programm handelt es sich hierbei um den gleichen Vorgang. Es wird eine Datei mit dem Namen SEPA.xml erzeugt, die auf die Diskette oder in einen beliebigen Bereich auf der Festplatte kopiert wird. Um nun die Zahlung online durchführen zu können, müssen Sie von der Bank ein entsprechendes Programm erwerben (z.B. S-Firm, VR-NetWorld). Diese Programme sind manchmal kostenlos, manchmal kosten sie auch 25,00 – 50,00 €. Mit derartigen Programmen können Sie Ihre Kontostände einsehen und auch Überweisungen per Hand durchführen. Bei der Durchführung von Überweisungen per Hand können Sie jedoch unser Rechnungseingangsbuch nicht nutzen. Derartige Bankprogramme bieten stets auch die Möglichkeit, eine vorbereitete Datei an die Bank zu übertragen. Über diesen Weg können Sie die von unserem Programm erzeugte Datei SEPA.xml an die Bank übermitteln. Über welchen Menüpunkt Sie dies in dem Bankprogramm erreichen, ist selbstverständlich vom Bankprogramm abhängig. An dieser Stelle können wir Ihnen keine Hilfestellung geben.
