# 7.4 Datenerfassungsprotokoll (DEP) – eine Erklärung

Pfad: Buchhaltung > Ladenkasse [23] > 7. Auswertungen > 7.4 Datenerfassungsprotokoll (DEP) – eine Erklärung
Quelle: handbuch/7_4_datenerfassungsprotokoll__dep____eine_erklarung.htm

|

7.4 Datenerfassungsprotokoll (DEP) – eine Erklärung

Nur für Österreich.

Was steht eigentlich in den „wilden“ Zeichen im Protokoll bzw. in der JSON Datei?

Im Prinzip das gleiche, was auch auf dem QR-Code, der zwingend auf dem Kassenbeleg mit ausgedruckt werden muss. Hier eine kleine „technische“ Erklärung.

_R1-AT0_89F01D01_1234_2017-02-21T14:06:12_15,78_0,00_0,00_0,00_0,00_

deaZfI04m8RFyEUSg== _B3B24A_Eot4U1keepU= _Ey6Q+B0a0DlmVeCXngoodOhy5oL6N9snJBNLcvDj9cA2XzgyK5CEmc9LFX9vKPlxOUmzn15hF8m5MnW4XHk3xg==

Die Buchstabenkolonne ist in 10 Felder aufgeteilt, die durch Unterstrichen ( _ ) getrennt sind.

R1-AT0 Eine Kennung für den Datensatztyp nach österreichischen Muster

89F01D01 Die Kassen-ID

1234 Die Belegnummer

2017-02-21T14:06:12 Das Belegdatum mit Uhrzeit

15,78 Der Umsatz brutto mit Standard Mehrwertsteuersatz

0,00 Der Umsatz brutto mit dem ermäßigten Mehrwertsteuersatz

0,00 Der Umsatz brutto mit dem zweiten ermäßigten Mehrwertsteuersatz

0,00 Der Umsatz brutto mit Null Mehrwertsteuersatz

0,00 Der Umsatz brutto mit besonderem Mehrwertsteuersatz

deaZfI04m8RFyEUSg== Der kumulierte Umsatz der Kasse seit Einrichtung und Anmeldung der Kasse

bei FinanzOnline. Der Wert ist mit einem AES-256Bit-Schlüssel verschlüsselt

und anschließend Base64 kodiert. Ein Entschlüsselung funktioniert nur mit

dem AES-Schlüssel

B3B24A_Eot4U1keepU= Ein Hash-Code (eine Art Prüfsumme) auf die vorherige DEP-Protokollzeile.

Damit wird verhindert, dass man unbemerkt eine Zeile aus dem Protokoll

Entfernen kann.

Ey6Q+B … k3xg== Eine Signatur (auch eine Art Prüfsumme) auf die bisherigen Informationen in

der Zeile. Diese Signatur wird mittels des USB-Signatur-Sticks ermittelt. Zur

Rückrechnung benötigt man die öffentlichen Signaturzertifikate, die am Anfang

Der JSON-Datei stehen.

Damit wird verhindert, dass die Werte der Zeile im Nachhinein unbemerkt

Verändert werden können.

[Bild]

Der QR-Code (Muster siehe links) kann mit jedem modernen Smartphone ausgelesen werden. „Geheime“ Informationen, die nicht auch im Klartext auf dem Beleg stehen, sind nicht lesbar. Der Umsatz ist 256-Bit verschlüsselt.
