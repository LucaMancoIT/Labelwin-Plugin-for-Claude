# 1. Ausstattung

Pfad: Buchhaltung > Ladenkasse [23] > 1. Ausstattung
Quelle: handbuch/1__ausstattung.htm

|

1. Ausstattung

Eine Ladenkasse kann hardwareseitig unterschiedlich umfangreich ausgestattet sein. Labelwin kann ein Kassen-Display, eine Kassenschublade und ggf. ein Geldkartenterminal über die seriellen Ports ansteuern. Die Informationen über COM Port, Baudrate, Parity, Daten- und Stopbits und Handshake erhalten Sie aus dem Handbuch des Kassensystems.

· Österreich: Unabdingbar ist eine Signatureinheit zur Erstellung einer Signatur (USB-Stick). Diese Signatur wird mittels QR-Code auf jeden Beleg gedruckt und im Datenerfassungsprotoll protokolliert. Hinweise zur technischen Einrichtung der Signatureinheit finden Sie im Kapitel Installation der Signatureinheit. Die softwareseitige Einrichtung im Kapitel Ladenkasse Grundeinstellungen „Allgemeines“ (B). Zum Drucken des QR-Codes ist ggf. eine Formularanpassung notwendig.

· Kassenschublade: Nach Eintragung des Gegeben-Betrages springt die Kasse auf. Nach Schließen der Kassenschublade kann die nächste Belegerfassung stattfinden.

· Kassen-Display: Hier wird bei der Erfassung jeder Artikel, die dazugehörige Menge und der Verkaufspreis angezeigt. Nach Abschluss der Artikelerfassung wird der Gegeben- und Zurückbetrag angezeigt. Der Anschluss eines Displays ist nicht zwingend erforderlich.

· EC-Karten-Terminal: Der Einsatz eines solchen Gerätes ist nicht zwingend erforderlich.

· Bon Drucker: Soll der Kassenbeleg auf einen klassischen Bon-Drucker ausgegeben werden, muss ein solcher Drucker an dem Arbeitsplatz der Ladenkasse eingerichtet sein.

· Tastatur-Scanner: Um sich die zeitaufwendige und fehleranfällige manuelle Eingabe von Artikel-nummern zu sparen, kann mittels eines Tastatur-Scanners ein Barcode ausgelesen werden. Hierzu kann im Prinzip jeder handelsübliche Tastatur-Scanner verwendet werden. In der Ladenkasse ist keine gesonderte Einrichtung erforderlich.

· Transportabler Barcode-Scanner: Hier können die gleichen Barcode-Scanner zum Einsatz kommen, wie im Bereich Lagerverwaltung. Für die Ladenkasse ist es nur erforderlich in dem Scanner ein Projekt mit der Nummer K zu erfassen und dann die Artikel so zu scannen, wie sonst auch. Der Scanner wird wie gewohnt in dem Modul SCANNERVERARBEITUNG (scann.exe)* ausgelesen. Dabei wird dann automatisch die Datei K.UGS angelegt. Im Modul LADENKASSE wird mit der Taste F8 ohne Nachfrage diese K.UGS ausgelesen und für den Kassenbeleg übernommen.

|

Info: Die Scannerverarbeitung ist ein Zusatzmodul und muss ggf. noch angeschafft werden.

Die Einrichtung der Schnittstellen zu den einzelnen Komponenten des Kassensystems erfolgt in den Grundeinstellungen der Ladenkasse. Lesen Sie hierzu bitte das Kapitel Ladenkasse Grundeinstellungen „Schnittstellen“ (C).
