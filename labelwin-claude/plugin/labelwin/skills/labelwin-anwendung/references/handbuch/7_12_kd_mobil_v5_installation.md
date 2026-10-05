# 7.12 KD-Mobil V5 Installation

Pfad: Kundendienst > KD-Mobil Notebook [Modul] > 7. Installation und Einrichtungsarbeiten > 7.12 KD-Mobil V5 Installation
Quelle: handbuch/7_12_kd_mobil_v5_installation.htm

|

7.12 KD-Mobil V5 Installation

In Kapitel Einrichtungsarbeiten am mobilen Gerät wurde die KD-Mobil Installation auf dem mobilen Gerät beschrieben.

Soll auf dem mobilen Gerät mit der neuen V5 Oberfläche gearbeitet werden (was sehr zu empfehlen ist), muss noch eine gesonderte Installationsroutine aufgerufen werden. Ob die erforderlichen Installationsdaten vorliegen, hängt davon ab, ob das Gerät neu eingerichtet wurde oder schon länger im Einsatz ist. Prüfen Sie, ob im Labelwin Verzeichnis der Ordner „v5inst“ existiert (z.B. C:\labelkd\v5inst\).

1. „v5inst“ Ordner vorhanden

Im Idealfall liegen die V5 Installationsdaten schon vor. Ist das der Fall, starten Sie aus diesem Ordner bitte die V5 Grundinstallation in dem Sie Dateien vcredist_x86.exe und anschließend die setup.exe starten..

2. „v5inst“ Ordner nicht vorhanden

Liegen die V5 Installationsdaten nicht vor, müssen diese entweder heruntergeladen oder im Zuge eines Grunddaten-Updates übertragen werden. Alternativ kann man auch einfach den „v5inst“ Ordner aus der Zentrale kopieren.

2.1 Download:

· Starten Sie das Labelwin Modul „Update Aktualisierung“ bzw. die Datei „LabelwinEinricht.exe“ aus dem Labelwin-Verzeichnis.

· Wählen Sie den Menüpunkt <Datei>, <Labelwin V5 DVD Download>.

· Nach einer Rückfrage, ob die Installation aktuell ist, startet der V5 Download. Der Vorgang kann, je nach Internettempo wenige Minuten oder auch eine halbe Stunde dauern, denn es sind ca. 550 MB. Nach dem erfolgreichen Download wird die Grundinstallation sofort durchgestartet.

2.2 Grunddaten-Update:

Führen Sie einen Grunddaten-Export wie in Kapitel Erstinstallation und Aktualisierung beschrieben durch. Haken Sie „Transportieren“ und „V5-Grundinstallation“ an. Tragen Sie außerdem einen Transport-Pfad ein.

[Bild]

2.3 Kopieren

Kopieren Sie einfach den „v5inst“ Ordner aus der Zentrale auf das mobile Gerät.

Die Installation der V5 Oberfläche funktioniert auf den mobilen Geräten wie die Grundinstallation in der Zentrale. Entweder startet die Installation nach dem Download automatisch oder Sie rufen die Dateien vcredist_x86.exe und die setup.exe aus dem „v5inst“ Ordner auf.

[Bild]

Wichtig: Während der Installation wird ein Installationsordner abgefragt.

Tragen Sie hier bitte unbedingt den richtigen und passenden Installations-ordner auf dem mobilen Gerät ein

- z.B. C:\labelkd\.

Zum Abschluss der V5 Installation sollte der Programmbaum noch angepasst werden. Über <Optionen> <Programmbaum anpassen> können die gewünschten Module ausgewählt und sortiert werden. Ein Beispiel könnte wie nebenstehend aussehen.

[Bild]

Den in diesem Beispiel gezeigten Eintrag „KD-Mobil“ finden Sie in der Liste aller Module unter dem Begriff „Mobiler Kundendienst“.

Tipp: Man kann den mobilen Kundendienst beim Start von Labelwin automatisch starten lassen. Dazu muss nur der Haken bei „Autostart“ gesetzt werden.

[Bild]

Bei Problemen während der Installation:

Sollten mangelnde Windows-Rechte die Ausführung verhindern, so kann man die Installationsmodule auch manuell als Benutzer „Administrator“ starten.

· vcredist_x86.exe:

Starten Sie aus dem Labelwin Unterverzeichnis „v5inst“ das Programm „vcredist_x86.exe“.

Installieren Sie diese Komponente auch dann, wenn Sie das 64 Bit Windows verwenden.

· setup.exe :

Starten Sie aus dem Labelwin Unterverzeichnis „v5inst“ das Programm „setup.exe“.

· cr_net_2005_x86.msi :

Sollten während der Installation Fehlermeldungen mit dem Inhalt „common files\business objects\2.7\binexportmodeller.dll” oder ähnlich auftreten, brechen Sie die Installation nicht ab, sondern installieren anschließend die Datei „cr_net_2005_x86.msi“. Sie liegt ebenfalls im „v5inst“ Ordner.
