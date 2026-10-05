# 6.4 Auftragsanlage per SMS oder E-Mail

Pfad: Kundendienst > KD-Mobil Notebook [Modul] > 6. Notdienstabwicklung, neue Aufträge mobil anlegen > 6.4 Auftragsanlage per SMS oder E-Mail
Quelle: handbuch/6_4_auftragsanlage_per_sms_oder_e_mail.htm

|

6.4 Auftragsanlage per SMS oder E-Mail

1. Hier muss durch Ihren EDV-Betreuer ein Programm auf dem Server eingerichtet werden, dass eingehende E-Mails empfangen und automatisch verarbeiten kann (Einrichtung Notdienstlösung Server). Das Programm hat den Namen Kdmail.exe. Die E-Mailadresse darf nur zu diesem Zweck verwendet werden, weil der Server ja alle E-Mails auf diese Adresse abfangen muss.

Bei der SMS muss eine bestimmte Nummer angewählt werden, die daraus eine E-Mail macht und weiterleitet. In der SMS muss die E-Mail-Adresse am Textanfang stehen und an eine bestimmte Nummer (z.B. 8000 bei T-Mobile) gesendet werden. Der Text kommt dann als E-Mail in der Zentrale an.

2. In der E-Mail oder der SMS muss eine Information über die Anlage oder Adresse enthalten sein, für die ein Auftrag angelegt werden soll. Optimal ist es also, wenn der Endkunde seine Anlagennummer bereits am Telefon nennen kann. Die Anlagennummer kann frei vergeben werden und muss im Labelwin in der Anlagenmaske in dem Feld „Eigene Anlagen-Nr.“ eingetragen sein.

Der Inhalt der E-Mail kann auf zwei Arten gefüllt werden.

(den folgenden Text finden Sie auch im Labelwiki unter dem Stichwort „Kdmail“)

|

Vorteile:

|

- alle Adressinformation und Anlagedaten vorhanden

- Kundendienst-Logbuch einsehbar

|

Nachteile:

|

- Einrichtung erforderlich

- E-Mail / SMS Handling etwas umständlich

- nur möglich, wenn eine Info (z.B. Anlagennummer) bekannt ist

Methode1: Nur ein Eintrag in der „Betreff“-Zeile

Folgende Einträge in der Betreffzeile sind möglich. Zwischen dem Schlüsselwort und der Nummer dürfen keine Leerstellen sein und die Betreffzeile darf keine weiteren Informationen enthalten!

- ANL12345

Es wird ein KD-Auftrag für die Anlage mit der „internen“ Anlagennummer bzw. „DiFa-Nummer“, hier 12345, erstellt und gemäß den Einstellungen ggf. an das mobile Gerät gesendet

- DIDxxxx

Es wird ein KD-Auftrag für die Anlage mit der „Device-ID/Eigenen Anlagennummer“, hier xxxx, erstellt und gemäß den Einstellungen ggf. an das mobile Gerät gesendet

- EANxxxx

Es wird ein KD-Auftrag für die Anlage mit der „eigenen Anlagennummer (EAN)“, hier xxxx, erstellt und gemäß den Einstellungen ggf. an das mobile Gerät gesendet

- TGM0001000200030004

Es wird ein KD-Auftrag für das TGM-Element mit der „TFM-Nummer“, hier 0001000200030004, erstellt und gemäß den Einstellungen ggf. an das mobile Gerät gesendet. Wichtig. Die TGM Nummer bitte ohne die Punkte erfassen

- ADR12345

Es wird ein KD-Auftrag für die Adresse mit der „internen/laufenden“ Adressenummer (Reiter „Zusatzdaten“), hier 12345, erstellt und gemäß den Einstellungen ggf. an das mobile Gerät gesendet

Der eigentliche E-Mail Text wird als Auftragstext (auszuführende Arbeiten) übernommen und kann unter Umständen weitere Schlüsselworte enthalten.

Methode 2: Einträge im E-Mail-Text

In diesem Fall können die Einträge im Betreff entfallen, sofern Sie im E-Mail-Text definiert sind. Andernfalls sind es zusätzliche Informationen.

- ANL12345

Es wird ein KD-Auftrag für die Anlage mit der "internen" Anlagennummer bzw. "DiFa-Nummer", hier 12345, erstellt und gemäß den Einstellungen ggf. an das mobile Gerät gesendet. Das Schlüsselwort muss ganz links beginnen

- ANL:12345

Es wird ein KD-Auftrag für die Anlage mit der "internen" Anlagennummer bzw. "DiFa-Nummer", hier 12345, erstellt und gemäß den Einstellungen ggf. an das mobile Gerät gesendet

- ANL 12 34 5

Es wird ein KD-Auftrag für die Anlage mit der "internen" Anlagennummer bzw. "DiFa-Nummer", hier 12345, erstellt und gemäß den Einstellungen ggf. an das mobile Gerät gesendet. Hierbei darf die Zahl Leerstellen, aber keine sonstigen Zeichen enthalten

- DIDxxxx

Es wird ein KD-Auftrag für die Anlage mit der "Device-ID/eigenen Anlagennummer", hier xxxx, erstellt und gemäß den Einstellungen ggf. an das mobile Gerät gesendet. Das Schlüsselwort muss ganz links beginnen

- DID:xxxx

Es wird ein KD-Auftrag für die Anlage mit der "Device-ID/eigenen Anlagennummer", hier xxxx, erstellt und gemäß den Einstellungen ggf. an das mobile Gerät gesendet

- EANxxxx

Es wird ein KD-Auftrag für die Anlage mit der "Eigenen Anlagennummer (EAN)", hier xxxx, erstellt und gemäß den Einstellungen ggf. an das mobile Gerät gesendet. Das Schlüsselwort muss ganz links beginnen

- EAN:xxxx

Es wird ein KD-Auftrag für die Anlage mit der "Eigenen Anlagennummer (EAN)", hier xxxx, erstellt und gemäß den Einstellungen ggf. an das mobile Gerät gesendet

- TGM:0001000200030004

Es wird ein KD-Auftrag für das TGM-Element mit der "TFM-Nummer", hier 0001000200030004, erstellt und gemäß den Einstellungen ggf. an das mobile Gerät gesendet. Wichtig. Die TGM Nummer bitte ohne die Punkte erfassen

- ADR:12345

Es wird ein KD-Auftrag für die Adresse mit der "internen/laufenden" Adressenummer (Reiter "Zusatzdaten"), hier 12345, erstellt und gemäß den Einstellungen ggf. an das mobile Gerät gesendet

- MONT:30

Der KD-Auftrag wird nicht an den Standard-Notdienst-Monteur lt. KD-Notdienst Einstellungen gesendet, sondern an den Monteuer mit der angegebenen "Personalnummer", hier 30, sofern bei diesem auch eine externe E-Mail-Adresse und eine Notebook-Nummer hinterlegt sind.

- SMS:017112345678

Zusätzlich zum KD-Auftrag wird an die angegebene Telefonnummer eine SMS gesendet, so dass der Monteur mitbekommt, dass er einen Auftrag per E-Mail erhalten hat. Die in den KD-Notdienst Einstellungen hinterlegte SMS wird in dem Fall ignoriert.

- NOT:1

In den KD-Notdienst Einstellungen ist hinterlegt, an welchen Wochentagen und Uhrzeiten die Notdienst Abwicklung läuft, d.h. der automatische Versand des KDA-Auftrages an den Notdienstmonteur. Mit diesem Eintrag kann für diese E-Mail die Notdienst Einstellung erzwungen werden.

- SUCHE:wiese 40

Zum Anlegen eines Notdienst KD-Auftrages benötigt der Monteur entweder die interne Anlagennummer, die Device-ID, die TGM-Nummer oder die Adressnummer. Diese sollte als Aufkleber an der Anlage des Kunden hinterlegt sein.

Wenn dies nicht der Fall ist, kann sich hierüber der Monteur eine kurze Adressen- und Anlagenliste per E-Mail senden lassen. Dazu gibt er hinter dem Wort SUCHE: Suchbegriffe ein, wie Sie es aus der normalen Labelwin Adressensuche gewohnt sind. Allerdings OHNE den führenden Klammeraffen, der wird hier intern immer gesetzt.

Damit das klappt, MUSS zusätzlich die Zeile MONT:xx mit der entsprechenden Monteur Personalnummer existieren, damit die Antwort E-Mail an den Monteur gehen kann, da in diesem Fall kein KD-Auftrag angelegt wird und auch die anderen Optionen nicht greifen
