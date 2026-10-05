# 7.18 Oplock deaktivieren

Pfad: Einrichtungsarbeiten > Einstellungen [14] > 7. Serviceprogramme > 7.18 Oplock deaktivieren
Quelle: handbuch/7_18_oplock_deaktivieren.htm

|

7.18 Oplock deaktivieren

In Netzwerken werden zur Optimierung und Beschleunigung der Datenzugriffe verschiedene Caching (Zwischenspeicher Methoden) benutzt. Diese Caches puffern die Daten aus den eigentlichen Dateien auf dem Server und den lokalen Arbeitsstationen und schreiben nur die Informationen auf die Festplatte weg, die angeblich weg geschrieben werden müssen. Die Daten werden nach Möglichkeit nicht von der Festplatte, sondern aus dem schnelleren Cache (also RAM Speicher) gelesen. Damit das allerdings funktioniert, müssen die verschiedenen Caches auf den unterschiedlichen Arbeitsplätzen immer sauber und korrekt miteinander kommunizieren, denn sonst werden veraltete Informationen weg geschrieben und das führt unweigerlich zu einer Beschädigung der Integrität einer Datenbank.

Leider funktioniert das Caching nicht einwandfrei.

Die genaue Ursache könnte Ihnen Microsoft vielleicht verraten – wir vermuten Konstruktionsfehler, verschiedene Betriebssysteme, verschiedene Releasestände, ‚Macken’ der Rechner…..

Als Konsequenz aus diesen Problemen empfehlen wir dringend den Cache weg zu schalten. Wichtig

ist das Abschalten auf allen Rechnern (auch dem Server!).

Unter diesem Menüpunkt wird Oplock deaktiviert.
