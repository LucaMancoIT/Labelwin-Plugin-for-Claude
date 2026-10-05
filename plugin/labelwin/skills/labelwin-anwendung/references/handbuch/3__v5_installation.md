# 3. V5 Installation

Pfad: Installation und Wartung > Labelwin Installation > 3. V5 Installation
Quelle: handbuch/3__v5_installation.htm

|

3. V5 Installation

Stand: 17.11.2015

V5 ist die neue Labelwin Programmgeneration. Mit neuer verbesserter Oberfläche, neuer Technik und vielen neuen Features. Sie wird langfristig die bestehende V4-Version ablösen.

Derzeit läuft Sie aber parallel zur V4-Version, da noch nicht alle Module umgestellt sind. D.h., manche Module sind in V5, andere noch in V4.

Die beiden Versionen sind absolut Daten-kompatibel. D.h. man kann gleichzeitig oder abwechselnd mit der V4 und der V5 arbeiten. Allerdings gibt es viele neue Funktionen NUR in der V5-Version.

Daher wird ein Umstieg auf die V5-Version dringend empfohlen.

Sollte es während der Installation Probleme geben, so können Sie diese jederzeit abbrechen. Die „alte“ Labelwin V4-Version wird weiterhin wie gewohnt funktionieren.

Starten Sie das Labelwiki über den Menüpunkt <Info>, <MyLabelwin Wiki> und suchen Sie nach dem Begriff „V5“. Hier erhalten Sie weitergehende Infos zur Einrichtung und zu den neuen Features.

Voraussetzungen:

-

Labelwin V5 wird als Erweiterung zu einem bestehenden Labelwin installiert. Eine V5-Installation setzt eine bestehende V4-Installation (mind. Version 4.42) voraus

-

Für V5 Arbeitsplätze wird als Betriebssystem Windows 7, Windows 8 oder Windows 10 empfohlen. Es läuft aber auch unter Windows Vista. Aber nicht auf XP!

-

Labelwin V4 muss vorher auf die Crystal 10 Druckroutinen (CR10) umgestellt sein

[Bild]

Über den Menüpunkt <Info>, <Info> in jedem Labelwin Modul erfahren Sie, welche Versionsnummer und welchen CR10-Status Labelwin hat. Der CR10-Status muss „1/1“ sein

Ablauf der Installation:

Die Installation läuft prinzipiell in 3 Schritten ab und kann von jedem System-Betreuer selbstständig

an Hand dieser Anleitung durchgeführt werden.

-

V5 Download: Herunterladen der Installationsdateien aus dem Internet (ca. 550 MB)

-

Grundinstallation: Durchführen der Grundinstallation auf dem Server

-

Arbeitsplatz(Client)-Installation: Durchführen der Arbeitsplatz(Client)-Installation auf allen weiteren Arbeitsplätzen

Windows-Rechte:

Da man zur Installation von Software gewisse Windows-Rechte benötigt, sollten Sie (der angemeldete Benutzer) ausreichend Rechte zur Installation von Programmen besitzen (Admin). Allerdings muss dieser Benutzer auch ein Labelwin-Anwender sein! Ggf. muss vorher für den Admin eine normale V4-ArbeitsplatzInstallation durchgeführt werden.

Datenschutzhinweis:

Um ggf. auftretende Programmfehler besser lokalisieren und beheben zu können, legt das Programm im Fehlerfall automatisch ein Protokoll mit Daten zum Programmablauf und zur Konfiguration an. Die Dateien befinden sich im Labelwin-Unterverzeichnis 'Systemberichte'. Auf Nachfrage des Programms können diese automatisch an den Label Support gesendet. Das können Sie aber bei Bedarf verneinen.

3.1 V5 Download

-

Starten Sie das Labelwin Modul „Update Aktualisierung“ bzw. die Datei „LabelwinEinricht.exe“ aus dem Labelwin-Verzeichnis

-

Wählen Sie den Menüpunkt <Datei>, <Labelwin V5 DVD Download>

-

Der Vorgang kann, je nach Internettempo wenige Minuten oder auch eine halbe Stunde dauern, denn es sind ca. 550 MB,

[Bild]

Nach dem erfolgreichen Download kann die Grundinstallation sofort durchgestartet werden

3.2 Grundinstallation

Diese Grundinstallation sollte nach Möglichkeit auf dem Server durchgeführt werden. Dazu sollte auf dem Server die V4 Version ausführbar sein.

Technischer Hinweis: Diese Grundinstallation geht prinzipiell auf einem beliebigen Arbeitsplatz. Sollte aber diese Installation mal deinstalliert werden, wird die V5-Version für ALLE Arbeitsplätze deinstalliert. Für eine sicheren Ablauf ist die

Installation auf dem Server als Admin dringend zu empfehlen.

> Installationsmodule: Es werden automatisch zwei Windows Installationsmodule gestartet. Bitte folgen Sie den Anweisungen am Bildschirm.

WICHTIG: Tragen Sie bei Aufforderung unbedingt den richtigen und passenden Labelwin Pfad der bestehenden Installation ein, z.B. L:\labelwin

> Bei Problemen: Sollten mangelnde Windows-Rechte die Ausführung verhindern, so kann man die beiden Installationsmodule auch manuell als Benutzer „Administrator“ starten

-

VCRedist_x86.exe:

Starten Sie aus dem Labelwin Unterverzeichnis ‘v5inst‘ das Programm ‘vcredist_x86.exe‘.

Installieren Sie diese Komponente auch dann, wenn Sie das 64 Bit Windows verwenden

-

Setup.exe:

Starten Sie aus dem Labelwin Unterverzeichnis ‘v5inst‘ das Programm ‘setup.exe‘

> Labelwin Flagge:

Nach erfolgreicher Installation finden Sie eine Verknüpfung ‘Labelwin starten‘ auf Ihrem Desktop. Damit starten Sie das Labelwin V5 Startcenter, der Ersatz für den gelben Ordner „Label für Windows“ Von jetzt an können Sie auf diesem Server-Arbeitsplatz mit der V5 Version arbeiten

[Bild]

> Update herunterladen und einspielen:

Im Anschluss sollten Sie Programmmodul „Internet-Update“, die neuste Programmversion abholen und installieren, da der vorherige Download nicht immer ganz aktuell ist

3.3 Arbeitsplatzinstallation

Dieser Schritt muss auf JEDEM WEITEREN Arbeitsplatz durchgeführt werden. Sie sollten als normaler Labelwin Benutzer eingeloggt sein.

Sollte die Installation auf Grund mangelnder Rechte scheitern, so führen Sie es erneut als Administrator durch. In dem Fall müssen Sie die Verknüpfung zu Labelwin-Flagge (L:\labelwin\labelwin.exe) manuell auf

den Desktop des Anwenders anlegen bzw. vom öffentlichen Profil in das lokale Profil übertragen.

[Bild]

> Update/Aktualisierung:

Starten Sie auf dem Arbeitsplatz das Labelwin Modul „Update/Aktualisierung“ bzw. das Programm „LabelwinEinricht.exe“

> Diesen Arbeitsplatz einrichten/erweitern:

Wählen Sie die Option ‘Diesen Arbeitsplatz einrichten/erweitern‘ und setzen Sie lediglich den Haken bei

„Labelwin V5 Client installieren“.

Klicken Sie den Start Knopf und folgen Sie den Anweisungen auf dem Bildschirm.

> Labelwin-Flagge:

Nach erfolgreicher Installation finden Sie eine Verknüpfung ‘Labelwin starten‘ auf Ihrem Desktop. Damit starten Sie das Labelwin V5 Startcenter, der Ersatz für den „gelben Ordner“

Von jetzt an können Sie auf diesem Arbeitsplatz mit der V5 Version arbeiten

Sonstige Infos:

> Die Aktualisierung (Update) der Labelwin V5-Version erfolgt zusammen mit der normalen V4-Version

Wir wünschen viel Spaß und viel Erfolg mit der V5-Version
