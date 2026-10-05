# Shop-Schnittstellen (IDS, UGL etc.)

Pfad: Schnittstellen > Shop-Schnittstellen (IDS, UGL etc.)
Quelle: handbuch/shop_schnittstellen__ids__ugl_etc__.htm

|

Shop-Schnittstellen (IDS, UGL etc.)

Artikel-Datenaustausch mit Lieferanten / Ansteuerung von Online-Shops mit Labelwin

Im Lauf der Jahre wurden diverse Schnittstellen zu den Daten und Systemen der Großhändler entwickelt.

Bei den Schnittstellen zu den Großhändlersystemen geht es im Wesentlichen um

-

das Erleichtern und elektronische Übermitteln von Bestellungen,

-

den elektronischen Austausch von Dokumenten zur Preisanfrage oder Angeboten,

-

den Erhalt von Detailinformationen zu einzelnen Artikeln per Knopfdruck (Deeplink) und um

-

den Onlinezugriff auf geschützte Seiten des Großhändlers.

Bei den derzeit vorhandenen Schnittstellen gibt es daher welche, die veraltet und überholt sind, aber auch welche, die nicht von allen Großhändlern unterstützt werden.

Des weiteren gibt es noch Formate und Schnittstellen zur Übermittlung von Stammdaten. Das älteste und bekannteste Format ist die „Datanorm“ zum Übertragen von Artikeldaten. Auch hier gibt es eine Übertragungsschnittstelle. Sie heißt SHK-Connect (bzw. je nach Teilnehmer auch Open-Connect). Informationen dazu finden Sie im Handbuch zum Modul Katalog.

Um den Wildwuchs der Schnittstellen zu begrenzen, hat sich in den letzten Jahren der Verband Bundesverband der Bausoftwarehäuser (BVBS), der Arbeitskreis der SHK-Großhändler (DG-Haustechnik), sowie das Paderborner Institut ITEK mit diesem Thema befasst und definiert einheitliche Schnittstellen (IDS, Heatinglabel, SHK-Connect etc.). Im BVBS ist Label nicht nur Mitglied, sondern mit Gerald Bax aktiv im Arbeitskreis dabei.

Schnittstellen, die eine gewisse adressenspezifische Einrichtung, wie Zugangsdaten und Ablagepfade, benötigen, werden im Modul Adressen über den Menüpunkt <Datei>, <Stammdaten UGL/Online> eingerichtet.

Die hier beschrieben Schnittstellen sind:

|

[Bild]

|

-

IDS-Shop – zur Kommunikation mit dem Online-Shop des Großhändlers

-

UGS – zur Übertragung von Artikel-Stücklisten

-

UGL dateibasierend – etwas umfangreichere Artikel-Stückliste

-

UGL per FTP – wie zuvor, jedoch per FTP Abruf

-

OCI – eine veraltete Version von IDS

-

Artikelinfo/DeepLink – Vorgänger von IDS zur Übertragung von Artikeldetailsinformationen

-

Heizungslabel – zum Erstellen von Energielabels für Heizungsverbundanlagen

-

ZUGFeRD-Rechnung – zum Erhalt von Eingangsrechnungen im elektronischen Format

|

Tipp: Vordruck zur Anfrage der Zugangsdaten beim Lieferanten

Sollten Ihnen Ihre Zugangsdaten nicht vorliegen, müssen Sie diese bei Ihrem Lieferanten anfragen. Zu diesem Zweck haben wir eine ausfüllbare PDF erstellt, die Sie hier herunterladen und an Ihren Lieferanten weiterreichen können:


[Bild] 


Einrichtung allgemein

Die Einrichtung der Schnittstellen erfolgt in der Adressverwaltung unter dem Namen des Lieferanten. Nach Speichern der Adresse sind die Menüpunkte [Datei - Stammdaten UGL / Online] anzuwählen.

Bei den Eingaben gibt es meist einen allgemeinen firmenbezogenen Zugang oder Ablagepfad der Daten. Darunter ist es möglich, personenbezogene Zugangsdaten oder Ablagepfade zu wählen. In der Anwendung verhält es sich so, dass die Personendaten vorrangig verwendet werden und nur bei Fehlen die Firmendaten zum Einsatz kommen.

[Bild]

In dieser Maske können Sie das System des Lieferanten ankreuzen.

Darunter müssen Sie festlegen, für welchen Artikelkatalog die Zugangsdaten gelten sollen. In der Regel wird es nur ein Katalog sein, aber manche Anwender haben für bestimmte Gewerke oder Ersatzteile einen separaten Katalog.

Bei dem Block ‚Shopvorgabe’ legen Sie fest, welcher Zugang bei der Anwendung vorgeschlagen werden soll. Die Vorgabe ‚Bestellung’ bezieht sich auf den Bereich der Druckausgabe, die Vorgabe ‚Suchen’ auf die Anwendung im Bereich der Artikelerfassung.

Je nach System müssen auf der rechten Seite die Karteiseiten ausgefüllt werden. Die Details finden Sie auf den nächsten Seiten.
