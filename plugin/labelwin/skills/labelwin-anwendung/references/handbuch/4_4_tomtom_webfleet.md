# 4.4 TomTom Webfleet

Pfad: Einrichtungsarbeiten > Einstellungen [14] > 4. Mobil > 4.4 TomTom Webfleet
Quelle: handbuch/4_4_tomtom_webfleet.htm

|

4.4 TomTom Webfleet

Wenn Sie das Zusatzmodul "Fahrzeugortung / Navigation" erworben haben, müssen Sie hier den Zugang für TomTom Webfleet konfigurieren.

[Bild]

Bitte geben Sie hier Ihren Zugangsnamen ein, der Ihnen von TomTom mitgeteilt wurde ein.

Ebenso wird hier das Login und das Passwort des Benutzers benötigt, der das Recht ‚Zugriff auf Schnittstelle WEBFLEET.connect’ in der TomTom-Lösung besitzt. Bitte beachten Sie dabei die Groß- und Kleinschreibung der Begriffe.

Wichtig ist noch, dass Sie auf dem Webfleet einen Benutzer ‚connect’ anlegen - dieser bekommt die Berechtigung im Bereich System für den ‚Zugriff auf Schnittstelle WEBFLEET.connect’.

Außerdem aktivieren Sie hier die Zeitübernahme. Diese Daten können dann im Modul ZEITERFASSUNG unter dem Menüpunkt <Optionen> <Übernahme aus TomTom> übernommen werden.

Für die Erfassung der Stundenarten lesen Sie bitten das Kapitel 14.2.8.3

Der Text, der als Auftragstext an TomTom übergeben wird, ist frei steuerbar. Dazu müssen Sie nur einen passenden Baustein anlegen. Da es dabei leicht passieren kann, dass der zulässige Text von 500 Zeichen überschritten wird, kann der Rest als Nachricht verschickt werden.

Für den Text, der an TomTom übergeben werden soll, muss im Modul EINSTELLUNGEN unter dem Menüpunkt <Vorlagen> <Vor- und Nachbemerkungen> ein neuer Baustein angelegt werden. Dieser Baustein muss den Namen TomTom-KD1 haben. Dabei steht die 1 für den ersten Mandant. Bei der Nutzung mehrerer Mandanten müssen mehrere Bausteine angelegt werden.

Der Baustein muss ähnlich aufgebaut sein wie unser SMS-KD, mit dem die Struktur von einer Auftrags-SMS festgelegt wird. Es dürfen alle Schlüsselworte aus dem Bereich Kundendienst verwendet werden. Das Schlüsselwort @kdauftrnr@ muss unbedingt im Baustein enthalten sein, am besten gleich als erstes.

Die Schlüsselworte stehen bei der Erfassung des Textes mit dem Knopf ‚Schlüsselworte' zur Verfügung.

Eine Beschreibung zur Nutzung der Schlüsselworte finden Sie im Kapitel 17.4
