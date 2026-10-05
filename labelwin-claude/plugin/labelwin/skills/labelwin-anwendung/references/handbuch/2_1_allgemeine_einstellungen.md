# 2.1 Allgemeine Einstellungen

Pfad: Buchhaltung > Ladenkasse [23] > 2. Einrichtungsarbeiten > 2.1 Allgemeine Einstellungen
Quelle: handbuch/2_1_allgemeine_einstellungen.htm

|

2.1 Allgemeine Einstellungen

Bevor die Konten- und Grundeinstellungen in der Ladenkasse vorgenommen werden, sollten einige allgemeine Einstellungen im Modul EINSTELLUNGEN geprüft werden.

Personal:

In den Personalstammdaten kann bei jedem Mitarbeiter, der die Ladenkasse bedienen soll, eine Verkäufer-Nr. hinterlegt werden. Beim Start der Ladenkasse muss dann der Verkäufer ausgewählt werden. Vorteil der Vergabe von Verkäufer Nummern ist, dass so zum einen der Verkäufer je Beleg nachgehalten wird und zum anderen, dass man dann ein Passwort je Mitarbeiter hinterlegen kann, um den Zugriff auf die Kasse einzuschränken.

[Bild]

Die Verkäufer-Nummern werden im Modul EINSTELLUNGEN unter dem Menüpunkt <Programmbereiche> <Personal> <Personal erfassen> erfasst. Das Feld für die „Ladenkasse Verk.Nr.“ wird nur sichtbar, wenn der Haken bei Aufgaben gesetzt wird. Man kann zusätzlich ein Passwort vergeben, das in der Ladenkasse abgefragt wird, bevor der Mitarbeiter die Ladenkasse nutzen kann.

Benutzerrechte:

[Bild]

Bei Nutzung der Benutzerrechteverwaltung können zwei Berechtigungsstufen für die Verwendung der Ladenkasse vergeben werden. Bei dem ersten Recht muss sich jeder Nutzer beim Start des Kassenmoduls mit einem Passwort anmelden und kann von da an beliebig viele Belege erfassen. Bei der zweiten Stufe muss das Passwort zu jeder Kassenbuchung erneut eingetragen werden. Diese Einschränkung ist nur dann sinnvoll, wenn verschiedene Mitarbeiter das Programm abwechselnd nutzen, ohne zwischendurch das Kassenmodul erneut zu starten.

Kassenbuch:

Sollen die Umsätze der Ladenkasse in die Fibu übergeben werden, muss zwingend das Modul KASSENBUCH eingesetzt werden. Die Kassen-Umsätze müssen täglich an das Kassenbuch übergeben werden (vgl. Kapitel Abrechnung) und von dort an das Fibu-Journal. Damit die Übergabe reibungslos und vor allem nachvollziehbar funktioniert, empfehlen wir dringend ein separates Kassenbuch pro Ladenkasse anzulegen. Eine weitere Kasse wird direkt im Modul KASSENBUCH unter <Stammdaten> <Kassen> angelegt.

Kostenstellen:

[Bild]

Bei Verwendung von Kostenstellen müssen Erlöskonten für die Ladenkasse ( MwSt. normal, MwSt. vermindert, ohne MwSt.) hinterlegt werden, w enn die anfallenden Werte als getrenntes Konto an die Fibu übergeben sollen. Die gewünschten Erlöskonten werden im Modul EINSTELLUNGEN unter dem Menüpunkt <Grund-einstellungen> <Kostenstellen> erfasst.

|

Arbeiten mit mehr als einer Ladenkasse

Wird mit mehr als einer Ladenkasse gearbeitet, muss an den jeweiligen Arbeitsplätzen eine Kassen-zuordnung vorgenommen werden.

Diese Einrichtung ist bewusst nicht an der Oberfläche vorzunehmen. In der Datei labelusr.ini muss unter die Gruppe [LADEN] eine Eintragung KASSENNUMMER=2 usw. eingetragen werden. Diese Einstellung wird vom Label-Betreuer vorgenommen.
