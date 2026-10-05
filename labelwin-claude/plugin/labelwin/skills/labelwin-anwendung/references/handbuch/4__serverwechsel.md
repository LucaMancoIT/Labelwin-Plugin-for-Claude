# 4. Serverwechsel

Pfad: Installation und Wartung > Labelwin Installation > 4. Serverwechsel
Quelle: handbuch/4__serverwechsel.htm

|

4. Serverwechsel

Wird in Ihrem System ein neuer Server installiert, sollten Sie für den „Labelwin-Umzug“ auf keinen Fall die Installations- oder Update-CD nutzen.

Sie können das komplette Verzeichnis „Labelwin“ von dem alten Server auf den neuen Server kopieren. Wir „verstecken“ keine Dateien. Im Normalfall sind im Labelwin-Ordner alle Daten enthalten. Eine Ausnahme gilt eventuell für das Verzeichnis „Datanorm“. Dieses enthält die Händlerkataloge und ist bei einigen Kunden wegen der Datensicherung nicht im Labelwin-Ordner enthalten. Sie können dies einfach feststellen:

Starten Sie von einem Client aus das Modul EINSTELLUNGEN den Menüpunkt <Grundeinstellungen><Pfade>. Die Pfade 5, 7, 10 und UGS liegen standardmäßig auf dem lokalen Laufwerk. Sollte einer der anderen Pfad nicht im Labelwin-Ordner liegen, müssen Sie diese Ordner ggf. extra auf den neuen Server kopieren.

Auf Terminal-Servern befinden sich die User-Verzeichnisse im Labelwin-Ordner unter \Labelwin\Computer\Computername\Username.

[Bild]

Sofern die Clients den neuen Server und dem „alten“ Laufwerksbuchstaben sehen, ist die Installation abgeschlossen. Sollte dies nicht der Fall sein, führen Sie an den Clients die oben beschriebene Arbeitsplatzinstallation aus.
