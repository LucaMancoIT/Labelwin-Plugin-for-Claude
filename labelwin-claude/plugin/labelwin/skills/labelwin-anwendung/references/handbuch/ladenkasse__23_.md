# Ladenkasse [23]

Pfad: Buchhaltung > Ladenkasse [23]
Quelle: handbuch/ladenkasse__23_.htm

|

Ladenkasse [23]

Stand: 29.01.2018

Das Modul LADENKASSE ist so konzipiert, dass es komplett in das normale LABELWIN-Programmpaket eingebunden ist. Im Netzwerk kann es auf einem normalen Arbeitsplatz genutzt werden. Dieser Arbeitsplatz kann ohne Probleme parallel auch zur Angebots- und Auftragsbearbeitung genutzt werden. Das Modul LADENKASSE wird über ein separates Icon gestartet und kann bei Nichtbenutzung in der Taskleiste abgelegt werden.

Der Rechner unterliegt also den gleichen Hardwareanforderungen wie jeder andere Arbeitsplatz auch. Zusätzlich müssen an diesem Rechner - je nach gewünschter Kassenausstattung - bis zu vier serielle Schnittstellen vorhanden sein. Diese werden mit der Ansteuerung für die Kassenschublade, Kundendisplay und das Scheckkarten-Terminal belegt. Ein stationärer Scanner kann zwischen den Tastaturanschluss gesetzt werden.

Jeder Kassenbeleg erzeugt genau wie alle anderen Dokumente einen Eintrag in einem Projekt. Über die Einstellmaske des Kassenmoduls kann hier ein Projekt vorgewählt werden. Bei der eigentlichen Kassenbuchung kann dieses Projekt jedoch umgeschaltet werden. Es ist sinnvoll, sich ein Projekt mit dem Namen ‚Ladenkasse‘ hierfür anzulegen. Die Anlage erfolgt wie sonst auch über das Modul PROJEKTE.

Bei jedem Kassenbeleg ist zwingend auch eine Adresse beteiligt. Es ist sinnvoll, hierzu eine Adresse mit dem Namen „Barverkauf“ anzulegen. Diese Adresse kann in den Grundeinstellungen der Ladenkasse vorbelegt werden. Bei der Kassenbuchung kann jedoch wieder auf jede beliebige Adresse umgeschaltet werden. Immer wenn ein bereits vorhandener Kunde über die Kasse einkauft, sollte auch dessen Adresse angewählt werden. Dies hat den Vorteil, dass auch die so gekauften Artikel über die Adress-Statistik eingesehen werden können.

Bei aktiver Lagerverwaltung werden sämtliche Kassenbewegungen automatisch im Lager abgebucht. Die Abbuchung erfolgt im Augenblick des Belegdruckes. Rücknahmen/Gutschriften werden mit negativer Menge eingebucht und wirken genauso auf die Lagerverwaltung.

Die Preisbildung erfolgt genau wie bei der normalen Angebots- und Rechnungsstellung über Kalkulationseinstellungen. Dabei ist die Standardkalkulationseinstellung in der Einstellmaske vorzugeben.

Es ist möglich normale Rechnungen im Rechnungsausgangsbuch über die Kasse zu begleichen. Als Zahlungsart kann neben der Barzahlung auch die Bezahlung per Scheck, Kreditkarte oder Gutschein erfolgen. Auch der Verkauf von Gutscheinen ist möglich. Das Kassenjournal kann die Werte für jede Zahlungsart getrennt auswerten.

Die Ausgabe des Kassenzettels kann auf jedem beliebigen Windowsdrucker erfolgen. Dies beinhaltet sowohl den Druck auf einem normalen Laserdrucker, als auch einem speziellen Etikettendrucker. Je nach Papiergröße muss das Formular mit Hilfe des Programmes „Crystal Report“ an die Wünsche des Kunden angepasst werden. Unsere Standard-Reports sind auf A4-Papier Laserdrucker ausgerichtet.

Innerhalb der Ladenkasse erfolgt eine fortlaufende Bestandzählung. Um diese zu ermöglichen gibt es auch einen Menüpunkt zur Entnahme sowie eine Eintragungsmöglichkeit für den Wechselgeld-Bestand. Bei einem Kassensturz ist somit der Vergleich des Soll Bestandes mit dem kompletten Inhalt möglich. Der Barbestand kann Beleg genau über Protokolle ausgegeben werden.

|

Info: In Österreich muss ab 2017 jeder Betrieb mit Barumsätzen über 15.000 € im Jahr eine Registrierkasse führen. Dazu zählt auch, wenn ein Kunde eine Rechnung in bar bezahlt. Die Protokolle müssen regelmäßig dem Finanzamt zugestellt werden. In Deutschland gibt es ähnliche Entwicklungen.

Wenn Sie mehr als eine Ladenkasse einsetzen wollen, muss eine spezielle Eintragung vorgenommen werden. Für jede Kasse wird ein separater Nummernkreis geführt.

Alle Einrichtungsarbeiten werden in Kapitel Einrichtungsarbeiten im Detail erläutert.

Kassenbuch (Bar-Kasse)

In Deutschland ist es im Gegensatz zu Österreich im Moment nicht zwingend erforderlich, parallel zur Ladenkasse unser Modul KASSENBUCH einzusetzen. Es wird aber auch hier dringend empfohlen.

Die Zusammenfassung zu Erlöskonten, Gutscheinkonten, Barumsätzen und dergleichen findet im Kassenbuch statt. Die Übertragung aller Vorgänge der Ladenkasse an die Bar- Kasse muss täglich stattfinden. Vom Kassenbuch aus kann über die Fibu-Schnittstelle eine Weitergabe an ein Fibu-Programm (wie Datev) bzw. an den Steuerberater erfolgen.

|

Wichtig. Bei Einsatz des Kassenbuches empfehlen wir ein separates Kassenbuch anzulegen, das nur für die Ladenkasse verwendet wird.

Hintergrund: Sowohl die Bestände der Ladenkasse, als auch des Kassenbuchs müssen jederzeit prüfbar sein. Bei einer Bargeldentnahme aus der Ladenkasse zu Sicherungszwecken wird der Betrag im Kassenbuch sofort verbucht. Da im Kassenbuch nur vorwärts gebucht werden kann, also keine Beleg rückdatiert, sondern nur auf das aktuelle Entnahmedatum gebucht werden kann, ist ein separates Kassenbuch nur für die Ladenkasse der bessere Weg.
