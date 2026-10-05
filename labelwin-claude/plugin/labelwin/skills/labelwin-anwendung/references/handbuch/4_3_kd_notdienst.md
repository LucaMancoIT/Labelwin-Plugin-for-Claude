# 4.3 KD-Notdienst

Pfad: Einrichtungsarbeiten > Einstellungen [14] > 4. Mobil > 4.3 KD-Notdienst
Quelle: handbuch/4_3_kd_notdienst.htm

|

4.3 KD-Notdienst

Dieser Menüpunkt ist nur sichtbar, wenn Sie das Modul KD-Mobil erworben haben.

Die Beschreibung der Notdienstabwicklung im mobilen Kundendienst finden Sie im Kapitel Notdienstabwicklung - Auftragsanlage per SMS oder E-Mail.

Einstellungen Auftragsanlage:

[Bild]

Bild: Einstellung für die Auftragsanlage

1 Zeitvorgaben: Mit der Labelwin KD-Notdienst Modul können KDMobil Monteure eine Email mit einer internen Anlagennumemr an den Notdienstserver senden.

Dieser Serverdienst (KDMail.exe) legt automatisch einen KD-Auftrag für diese Adresse und Anlage an und sendet diesen KD-Auftrag inkl. aller notwendigen Anlageinformationen ggf. an das mobile Gerät zurück.

Da wir davon ausgehen, dass während der Bürozeiten der automatische Versand nicht automatisch, sondern manuell durch einen Mitarbeiter erfolgen soll, können Sie hier Bürozeiten eingeben, in denen kein Notdienst erfolgen soll. Sinnigerweise setzen Sie die Büroendezeit auf ca. 15 Minuten vor Büroschluss.

Wichtig ist, dass Sie den Haken bei Notdienst setzen, damit der Notdienst Automatismus außerhalb der Bürozeiten auch aktiviert ist. Damit der Notdienst Automatismus immer aktiv ist, setzen Sie Bürozeiten auf 00:00 bis 00:00 und setzen Sie überall den Notdienst Haken.

[Bild]

2 Vorgabe Priorität: Alle per Notdienst angelegten Aufgaben können eine besondere Priorität bekommen, damit Sie im KD-Modul besser gesehen und ggf. farblich markiert werden können (siehe Menüpunkt <Programmbereiche> <Kundendienst> <Prioritäten>.

[Bild]

3 Temporärer Ablagepfad der Mails: Alle eingehenden Emails werden temporär, d.h. zeitweise, in diesem Pfad zwischengespeichert. Es kann ein beliebiger, aber vorhandener, Pfad sein.

[Bild]

4 Standardadresse: Die Adressen werden automatisch durch die ausgewählte Anlage festgelegt. Sollte es aber keine Adresse geben, so wird diese Notadresse genommen, da ein KD-Auftrag eine Adresse haben muss.

Vorgabe Bürozeiten

Hier wird definiert, was mit dem eingehenden Notdienst Auftrag während der Bürozeiten passieren soll.

[Bild]

5 Auftragsanlage Monteur: Der Notdienst Monteur kann in seiner Notdienst Email festlegen, für welchen Monteur der KD-Auftrag angelegt werden soll. Gibt er keinen oder einen fehlerhaften Monteur ein, dann wird der hier angegeben Monteur genommen.

[Bild]

6 Weiterleitung: Damit der KD-Leiter im Büro von einen eingehenden Notdienstauftrag sofort erfährt, kann hier eine Email Adresse hinterlegt werden, an die sofort eine Email gesendet wird. Sie können hier auch mehrere Email Adresse mit Komma oder Semikolon getrennt angeben.

Vorgaben Notdienst

Hier wird definiert, was mit dem eingehenden Notdienst Auftrag während der Notdienstzeiten passieren soll.

[Bild]

7 Auftragsanlage: Der Notdienst Monteur kann in seiner Notdienst Email festlegen, für welchen Monteur der KD-Auftrag angelegt werden soll. Gibt er keinen oder einen fehlerhaften Monteur ein, dann wird der hier angegeben Monteur genommen.

[Bild]

8 Rückversand an mobiles Gerät: Der Notdienst Monteur kann in seiner Notdienst Email festlegen, für welchen Monteur der KD-Auftrag angelegt werden soll. Gibt er keinen oder einen fehlerhaften Monteur ein, dann wird der hier angegeben Monteur bzw. das Gerät genommen.

[Bild]

9 Weiterleitung:

Mailadressen: Damit der KD-Leiter von eingehenden Notdienstaufträgen erfährt, kann hier eine Email Adresse hinterlegt werden, an die sofort eine Email gesendet wird. Sie können hier auch mehrere Email Adresse mit Komma oder Semikolon getrennt angeben.

SMS: Zusätzlich kann eine SMS versendet werden. Das ist z.B. dann sinnvoll, wenn die Notdienstaufträge (Notdienst-Emails) nicht vom auszuführenden Monteur, sondern von einem zu Hause sitzenden Mitarbeiter erstellt werden. Damit bekommt der KD-Monteur sofort eine SMS, damit er weiß, dass er sein KD-Mobil Gerät einschalten muss, um einen Notdienstauftrag in Empfang zu nehmen.

In der Notdienst Email kann eine abweichende SMS Nummer angegeben werden.

[Bild]

10 OK, speichern: Durch Betätigung dieses Knopfes werden die vorgenommen Einstellungen gespeichert.

[Bild]

11 Abbruch: Durch Betätigung dieses Knopfes wird die Maske geschlossen. Etwaige Änderungen werden nicht gespeichert.

Einstellungen Email-Server Vorgaben

[Bild]

Bild: Vorgaben für den Email Server

1 SMTP-Server (zum Versenden von Emails): Ein SMTP Server ist der Email Server Ihres Internet Providers für den Versand von Emails. Alle notwendigen Zugangsinformationen erhalten Sie von Ihrem Internet Provider. Es sind die gleichen Informationen, die Sie auch in Outlook etc. eintragen würden.

|

ACHTUNG

Sie müssen hier einen Email-Account wählen, der ausschließlich für diesen KD-Notdienst benutzt wird. Bitte benutzen Sie hier nicht Ihre info@firmenname.de Adresse!

Servername: Diesen erfahren Sie von Ihrem Email Provider.

Beispiele: Bei 1und1 smtp.1und1.de, bei Strato post.strato.de, bei GMX mail.gmx.de bzw. mail.gmx.net, bei T-Online mailto.t-online.de, bei Yahoo smtp.mail.yahoo.de

Bei Falscheingabe erhalten Sie z.B. den Fehler "Kein Connect! 1072"

Serverport: Diesen erfahren Sie von Ihrem Email Provider bzw. Ihremn Systemadministrator, sofern Sie eine Proxyserver habe, Der Standard ist Port 25, bei Einsatz von Proxyserver zumeist 587. Bei Falscheingabe erhalten Sie z.B. den Fehler "1078 Timeout: Verbindung zum Mailserver konnte aufgrund einer Zeitüberschreitung nicht aufgebaut werden."

Username: Dieses ist Ihr Anmeldename für den Email-Account. Das kann eine Nummer, ein Name, aber auch die Email Adresse sein. Bei Falscheingabe erhalten Sie z.B. den Fehler "1077 Fehler beim Senden der Authentifizierung. Entweder unterstützt der SMTP-Mailserver kein SMTP-AUTH oder es wurden ungültige Authentifizierungsdaten angegeben [535 Authentication failure]"

Passwort: Bei Falscheingabe erhalten Sie z.B. den Fehler "1077 Fehler beim Senden der Authentifizierung. Entweder unterstützt der SMTP-Mailserver kein SMTP-AUTH oder es wurden ungültige Authentifizierungsdaten angegeben [535 Authentication failure]"

Absender-Email: Das ist die Emailadresse, die der Empfänger einer Email als Absenderadresse enthält. Es ist aber auch gleichzeitig die Emailadresse, an die zum Testen der Verbindung eine Email gesendet wird und die Emailadresse, an die der Notdienst-Monteur seine Notdienst-Email sendet. D.h. diese Email-Adresse muss zu den obigen Daten passen.

Bei Falscheingabe erhalten Sie z.B. den Fehler "1068 Der Mailserver hat folgende Absenderadresse zurückgewiesen: [421 invalid sender domain]"

Absendername: Hier können Sie einen beliebigen Namen eingeben. Er wird in Outlook und anderen Programm als Absender bevorzugt angezeigt.

[Bild]

2 POP3-Server (zum Empfang von Emails): Ein POP3 Server ist der Email Server Ihres Internet Providers für den Empfang von Emails. Alle notwendigen Zugangsinformationen erhalten Sie von Ihrem Internet Provider. Es sind die gleichen Informationen, die Sie auch in Outlook etc. eintragen würden.

Servername: Diesen erfahren Sie von Ihrem Email Provider.

Beispiele: Bei 1und1 pop.1und1.de, bei Strato post.strato.de, bei GMX pop.gmx.de bzw. pop.gmx.net, bei T-Online pop.t-online.de, bei Yahoo pop.mail.yahoo.de

Bei Falscheingabe erhalten Sie z.B. den Fehler " Kein Connect! 1035 Entweder konnte keine Verbindung hergestellt werden oder die Verbindung wurde getrennt."

Serverport: Diesen erfahren Sie von Ihrem Email Provider bzw. Ihremn Systemadministrator, sofern Sie eine Proxyserver haben. Der Standard ist Port 110. Bei Falscheingabe erhalten Sie z.B. den Fehler "Kein Connect! 1048 Timeout: Verbindung zum Mailserver konnte aufgrund einer Zeitüberschreitung nicht aufgebaut werden."

Benötigt SMTP Authentifizierung: Aus historischen Gründen benötigt man zum Lesen eines Email-Accounts keine Zugangsdaten! Da das natürlich keiner will, werden zumeist die gleichen Daten wie beim Versenden benutzt. Setzen Sie dazu hier den Haken.

Bei Falscheingabe erhalten Sie z.B. den Fehler "Kein Connect! 1040 Der Server hat den Benutzernamen zurückgewiesen."

[Bild]

3 Testen: Über diesen Knopf können Sie Einstellungen testen.
