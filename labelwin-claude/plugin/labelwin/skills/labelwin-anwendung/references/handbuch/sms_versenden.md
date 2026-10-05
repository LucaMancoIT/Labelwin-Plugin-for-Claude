# SMS versenden

Pfad: Kundendienst > SMS Versand [Modul] > SMS versenden
Quelle: handbuch/sms_versenden.htm

|

SMS versenden

Bedienung im Adressmodul

Wählen Sie eine Adresse und starten Sie über den Menüpunkt <Bearbeiten> <SMS versenden> oder verwenden Sie die Tastenkombination Sie STRG + S. Das SMS Versand Modul wird gestartet. In der Auswahlliste der Telefonnummern stehen alle Telefonnummern der gewählten Adresse zur Verfügung.

[Bild]

Bild: SMS-Versand – Eingabe Text

1 Handy-Nr.: Sie können eine Telefonnummer auswählen oder eine eingeben. Ausländische Empfänger bitte wir folgt schreiben: 0044 780 1234567. Die Telefonnummer darf Leerstellen und Sonderzeichen wie / oder – enthalten.

2 Aktueller SMS Absender: Zeigt die hinterlegte Handy-Nr. und den Namen des SMS-Absenders an.

3 Laufbalken: Anhand des Laufbalkens können Sie erkennen, wie viel Platz sie noch pro SMS haben. Die blauen Quadrate über dem Laufbalken zeigen Ihnen an, aus wie vielen einzelnen SMS Ihre Mitteilung besteht.

4 SMS-Text: Hier geben Sie Ihre Mitteilung ein. Der Mitteilungstext kann bis zu 1600 Zeichen lang sein. Der Text wird automatisch in mehrere – max. 10 – SMS à 160 Zeichen aufgeteilt.

5 Guthaben/Kosten: Durch Betätigen dieses Knopfes können Sie Ihr Guthaben aufladen. Eine nähere Beschreibung dazu finden Sie im Kapitel Aufladen des SMS Guthabens und Kosten einer SMS.

6 Protokoll: Über diesen Knopf gelangen Sie zum SMS Versandprotokoll. Das Protokoll kann nach diversen Kriterien eingegrenzt werden, z.B. nach dem Loginnamen des Versenders, der internen Referenznummer (MsgID), der gewählten SMS Nummer und dem Mitteilungstext.

[Bild]

Einzelne markierte Einträge können per STRG-X (oder Menü <Datei> <Löschen Eintrag>) gelöscht werden. Über den Menüpunkt <Datei> <Löschen bis Datum> können alle alten Einträge bis zu einem bestimmten Datum gelöscht werden.

Bestimmte SMS Provider bieten manchmal die Möglichkeit, den Status einer verschickten SMS an Hand der Referenznummer (MsgID) abzufragen. Markieren Sie einen Eintrag und wählen Sie dazu den Menüpunkt <Datei> <Statusmeldung>. In den meisten Fällen wird es aber keine Statusmeldungen geben.

7 Senden: Zum Versenden der SMS drücken Sie den Knopf „Senden“ oder die Taste F9. Zum Versand ist eine funktionierende Internetverbindung notwendig.

[Bild] Eine erfolgreiche Übermittlung an den SMS Service Provider (z.B. T-Mobile oder Vodafone) wird bestätigt. Diese Bestätigung bedeutet aber nur, dass der Serviceprovider (z.B. T-Mobile) die SMS erhalten hat. Ein Zustellbestätigung, dass die SMS auf dem Handy angekommen ist, gibt es nicht.

Des Weiteren werden die Kosten der aktuellen SMS und das SMS Restguthaben angezeigt.

Wenn die SMS nicht erfolgreich versendet werden konnte, wird ein entsprechender Fehler ausgeben.

Folgende Fehler können auftreten:

· ERROR: Carrier Zustellung misslungen

Der SMS Provider hat die Zustellung der SMS abgelehnt. Die Telefonnummer des SMS Empfängers ist möglicherweise falsch. Ggf. ist auch Ihre in dem SMS Stammdaten (siehe Einrichtung) eingetragene Absender Nummer fehlerhaft.

Des Weiteren kann es auch an einer kurzfristigen Überlastung des Providers liegen.

· ERROR: Das SMS Internet Gateway steht derzeit nicht zur Verfügung

Das kann kurzfristig bei Überlastung oder Wartungsdiensten auftreten.

· ERROR: Interner Fehler

Es liegt ein interner Fehler vor, der umgehend behoben wird.

Nach dem erfolgreichen Versand kann ein Nachweis ausgedruckt werden. Er weist aber lediglich die erfolgreiche Übermittlung an den SMS Provider nach, nicht aber den erfolgreichen Versand oder Eintreffen der SMS.

8 Ende: Über diesen Knopf verlassen Sie den SMS Versand.

Bedienung im Kundendienstmodul

Wählen Sie einen Kundendienstauftrag aus und drücken Sie auf den Knopf ‚Drucken’. In der nachfolgenden Druckmaske erscheint der Knopf ‚SMS’. Beim Drücken dieses Knopfes wird das SMS Versand Modul gestartet, wobei das Telefonnummern- und das Textfeld schon gefüllt sind.

Als Telefonnummer wird die Handynummer des Monteurs, sofern im Personalstamm hinterlegt, eingetragen, der diesem Kundendienstauftrag zugeordnet ist. Sie kann natürlich vor dem Versand manuell abgeändert werden.

[Bild]

Im Mitteilungstext stehen die Daten des Kundendienstauftrages. Den Umfang und Inhalt können Sie selber festlegen, indem Sie einen Textbaustein (Modul EINSTELLUNGEN unter dem Menüpunkt <Vorlagen> <Vor- und Nachbemerkung>) mit der Bezeichnung SMS-KD anlegen. Damit er in der Auswahlliste der Vor- und Nachbemerkungen nicht stört, sollten Sie die Bausteinart auf ‚Sonstiges’ setzen.

Standardmäßig sieht der Textbaustein wie folgt aus:

KD: @KDauftrnr@ T:@KDtermin@ @KDUhrzeit@ @KDbauanrede@ @KDbauname@ @kdbauname1@ @kdbaustrasse@ @kdbauplz@ @kdbauort@ Tel: @kdbautel@ @kdauftragtext@ @kdkommentar@

Bedenken Sie bitte, dass es in einer SMS Mitteilung keine Zeilenschaltung gibt. Selbst wenn Sie am Bildschirm eine eingeben, so wird sie beim Versand in eine Leertaste umgewandelt. Wie der Text auf dem Display des Handys erscheint hängt ganz vom Handy ab.

Sie können vor dem Versand der SMS den zu versendenden Text vor dem Drücken der F9-Senden Taste korrigieren.
