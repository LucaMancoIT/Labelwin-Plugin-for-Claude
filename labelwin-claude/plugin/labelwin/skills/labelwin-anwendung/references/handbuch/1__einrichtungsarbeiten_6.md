# 1. Einrichtungsarbeiten

Pfad: Sondermodule > Verkaufsprovision [Modul] > 1. Einrichtungsarbeiten
Quelle: handbuch/1__einrichtungsarbeiten_6.htm

|

1. Einrichtungsarbeiten

Damit ein Abrechnungsdokument erzeugt werden kann, müssen die Adressen aller Mitarbeiter, die ggf. Provision bekommen, erfasst werden. Im zweiten Schritt muss in der Personalerfassung bei allen Mitarbeitern diese Adresse zugeordnet werden.

[Bild]

[Bild]

Weiter muss bei jedem Mitarbeiter ein Prozentsatz hinterlegt werden, mit dem im Falle einer Provisionszahlung die Höhe berechnet wird.

Grundeinstellung:

Im Modul Einstellungen müssen Regeln für die Provisionsberechnung hinterlegt werden. Wählen Sie dazu die Menüpunkte <Programmbereiche>, <Personal>, <Provision> an.

[Bild]

Für die Verkaufsprovision gilt nur der obere Block.

- Nur bezahlte Rg.:Hier legen Sie fest, ob die Abrechnung erst nach Zahlungseingang erfolgen soll.

- Detailiert: In diesem Fall wird in der Abrechnung jede Position aufgeführt, für die Prov. ausgezahlt wird. Anderenfalls gibt es pro Rechnung nur eine Position mit der Gesamtsumme.

- Wenn die Prämie einer Position auf mehrere Mitarbeiter aufgeteilt wird, kann dieser Anteilfaktor ausgewiesen werden.

Mit dem Knopf ‚Vorlagedokument‘ legen Sie ein Musterdokument an, aus dem später die Artikeltexte sowie die Vor- und Nachbemerkungen übernommen werden.

[Bild]

Formular für Druckausgabe

Das Ergebnis einer Provisionsberechnung ist ein Ausdruck für jeden Mitarbeiter. Dieses Formular ist frei gestaltbar. Wir haben Standardformulare erstellt, die sich am Druck einer Rechnung orientierten. Diese Formulare werden durch das Update auf Ihrem Rechner hinterlegt, aber nicht automatisch eingebunden.

Tragen Sie diese bitte über das Modul Einstellungen mit den Menüpunkten <Programmbereiche>, <Druckausgabe>, <Report.ini bearbeiten> ein. Der Eintrag muss in die Gruppe ‚Rechnungen‘ erfolgen. Es handelt sich um das Formular rgprov oder für Kunden mit formatierten Texten um das Formular rgprovR.

Bei einem späteren Nachdruck wird dies unter dem Bereich Stücklisten gedruckt (..als Rechnung ist nicht anwählbar), deshalb muss es ebenfalls unter den Stücklisten eingetragen werden.

Vorlage-Dokument

Legen Sie eine neue Vorlage an. Der Name ist im Prinzip egal, unser Vorschlag ist ‚Verkaufsprovision‘. Sie gelangen dann in die Maske der Artikelerfassung. Hier legen Sie auf Wunsch eine Vor-und Nachbemerkung an und einen Artikel, der als Rechnungskopf verwendet wird.

In den Vor- und Nachbemerkungen können diese Schlüsselworte verwendet werden:

@datumvon@

@datumbis@

Beispiel:

[Bild]

In dem Vorlageartikel können über Schlüsselworte alle Informationen aus dem Rechnungsdokument übernommen werden. Übernehmen Sie diese am besten mit dem Modul ‚Schlüsselworte‘ (..\labelwin\schluesselwort.exe)

[Bild]

Zusätzlich können mit diesen Schlüsselworten die Daten aus dem Rechnungsausgangsbuch übertragen werden:

@provrgnr@ Rechnungsnummer

@provrgdatum@ Rechnungsdatum

@provrgsumme@ Gesamtsumme der Rechnung

Artikelstammdaten

Um zu kennzeichnen welche Artikel mit Provision abgerechnet werden, müssen bestimmte ‚Geheimpositionen‘ mit der Personalnummer in die Rechnung eingetragen werden. Es ist sinnvoll, die häufig verwendeten Geheimpositionen in den Stammdaten zu hinterlegen. Die Artikelnummer ist im Prinzip frei wählbar. Wir empfehlen aber Nummern wie z.B. provWilly oder prov123 (wobei 123 die Personalnummer ist).

Als Artikeltext muss prov_123 eingetragen werden, wobei 123 wieder die Personalnummer ist. Dahinter können Sie zu Ihrer Information wieder den Namen des Mitarbeiters eintragen. Texte wie

prov_123 Willy Müller

sind also möglich.

Es ist auch möglich, einen Artikeltext mit prov_$ anzulegen. Das Dollarzeichen bewirkt einen Stopp beim Artikelaufruf, damit man dann die Personalnummer eintragen kann.

Die Provision gilt immer für die nachfolgenden Artikel. Um dies zu beenden muss ein Geheim-Artikel mit dem Text prov_ende im Dokument stehen. Diesen sollten Sie am besten ebenfalls in den Stammdaten hinterlegen.
