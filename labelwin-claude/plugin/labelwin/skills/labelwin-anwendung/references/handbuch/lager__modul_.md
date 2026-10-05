# Lager [Modul]

Pfad: Materialwirtschaft > Lager [Modul]
Quelle: handbuch/lager__modul_.htm

|

Lager [Modul]

Das Programmmodul Lager ist nur als Zusatzmodul zum Programmpaket Labelwin zu nutzen. Zur Bearbeitung von Bestellungen, Lieferscheinen, Inventurlisten und dergleichen benutzt es den gleichen Editor wie die Angebots- und Rechnungsstellung. Es ist daher nicht allein lauffähig.

Um das Grundprinzip unserer Lagerorganisation zu verstehen, betrachten Sie bitte die Skizze.

[Bild]

Die Lagerliste baut immer auf einem Artikel auf, der in einem Katalog hinterlegt ist. Bei der Lageranmeldung (=Neuanlage) wird von dem Eckventil mit der Nummer 123 der Text und die Artikelnummer kopiert. Nun kann in der Lagerliste zwar auch die vorgeschlagene Nummer geändert werden, aber in der Regel ist dies nicht sinnvoll. Die Bestände werden immer bei dem einzelnen Lager verwaltet – die im Bild ‚Lagerliste’ sichtbare Menge setzt sich immer aus den Einzelmengen der verschiedenen Lager zusammen. Die oben sichtbare Verbindung zum Artikel xyz im Katalog 2 wird nachträglich über die Artikelzuordnung hergestellt. Von da an werden bei einer Rechnungsstellung oder Lieferscheindruck von beiden zugeordneten Artikeln die Bestände verändert.

Alle Auswertungen bauen darauf auf, dass jede Lagerbewegung in einem Protokoll registriert wird. Aus diesem Protokoll heraus werden jegliche Auswertungen erzeugt.

[Bild]

Das Modul ist darauf ausgelegt, mit beliebig vielen Lagern zu arbeiten. Dabei wird eines der Lager als Hauptlager eingerichtet und alle anderen als Unter- oder Baustellenlager. Ein Unterlager kann durchaus auch ein Monteurfahrzeug sein, in dem diverse Reparaturmaterialien aufbewahrt werden. Bei der Bestandsanzeige wird immer der Gesamtbestand über alle Lager hinweg angezeigt - jedoch auch die einzelnen Bestände der Unterlager sind sichtbar zu machen.

Es ist möglich, eine Baustelle als Lager anzumelden, um die dort lagernden Materialien ebenfalls mit zu verwalten.

|

Zur den Vor- und Nachteilen von mehreren Lagern lesen Sie vor der Einrichtung von weiteren Lagern das Kapitel Lager beschriften

Ein Lager wird eingerichtet, indem ein neues Projekt angelegt wird und im Datenblatt ein Kreuz bei ‚Als Lager verwenden’ gesetzt wird.

Alle Projekte mit diesem Kennzeichen werden als mögliche Lagerorte angeboten. Im Modul EINSTELLUNGEN unter dem Menüpunkt <Programmbereiche> <Lager> muss eines der Projekte als Hauptlager deklariert werden.

Über die Festlegung von Mindestbeständen und Mindestbestellmengen kann das Programm selbsttätig Bestellvorschläge erstellen. Diese Bestellvorschläge sind jedoch vor dem Ausdruck beliebig veränderbar. Nur die tatsächlich bei der Bestellung ausgedruckten Mengen werden im Lager als Bestellbestand geführt. Bei einer Druckausgabe auf den Bildschirm erfolgt keine Lagerbuchung, sondern nur bei einer tatsächlichen Ausgabe auf Papier oder Fax.

Über eine Bestellverwaltung ist es möglich, jederzeit eine Bestellung zu verfolgen. Dabei ist es auch möglich, Teilmengen einzelner Positionen einzubuchen. In diesem Fall werden lediglich die noch fehlenden Mengen als Rückstand geführt. In dieser Rückstandsverwaltung ist es auch möglich neue Liefertermine für einzelne Artikel einzutragen. Zu jeder Position kann auch über eine Bemerkung der Grund der Lieferverzögerung und dergleichen eingetragen werden. Näheres zur Bestellüberwachung lesen Sie im Kapitel Bestellung bearbeiten und in unserem Handbuch unter Bestellüberwachung.

Die Lagerbestände können automatisch beim Druck einer Rechnung oder eines Lieferscheines aktualisiert werden, wenn das entsprechende Feld dafür aktiviert ist.

Einem Lagerartikel können beliebig viele Großhändlerartikel zugeordnet werden. Darüber ist es möglich, bei der Abbuchung oder Bestellung die Lagerartikel von verschiedenen Händlern zu bestellen.

Um nicht nur Einzelartikel sondern auch bestimmte Artikelgruppen umsatzmäßig analysieren zu können, muss jeder Artikel einer Gruppe zugeordnet werden. Die Anzahl dieser Gruppen ist unbegrenzt und die Bezeichnung ist frei wählbar. Die Gruppen werden unter dem Menüpunkt <Optionen> angemeldet.

Die Statistiken werden je nach gewähltem Formular auf verschiedene Arten ausgegeben. Die Formulare lassen sich wie alle anderen Formulare auch, lediglich mit dem Crystal Report bearbeiten.

Wie Sie Ihr Lager beschriften können, lesen Sie bitte im Kapitel Lager beschriften nach.
