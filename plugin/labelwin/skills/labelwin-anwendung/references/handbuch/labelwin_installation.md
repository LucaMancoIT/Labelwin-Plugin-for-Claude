# Labelwin Installation

Pfad: Installation und Wartung > Labelwin Installation
Quelle: handbuch/labelwin_installation.htm

|

Labelwin Installation

Stand: 22.02.2019

(V5.89)

Die folgenden Beschreibungen und Erklärungen richten sich in erster Linie an Systembetreuer. Es wird erklärt wie Labelwin zu installieren ist, entweder als komplette Neu-Installation (1) oder nur ein weiterer Arbeitsplatz (2).

|

Hintergrund

Labelwin wird zentral auf einem Netzlaufwerk (Server) installiert. Zur Benutzung von Labelwin von einem Arbeitsplatz aus ist zudem eine Arbeitsplatzinstallation notwendig. Dabei werden Systemdateien, Treiber und Programme auf dem lokalen Rechner installiert und eingerichtet. Außerdem müssen ein paar benutzerspezifische Einstellungen vorgenommen werden. Hierfür ist es notwendig, sich auf dem Arbeitsplatzrechner (bzw. in der Terminalserversession) als Administrator und als Benutzer einzuloggen. Die entsprechenden Zugangsdaten (Benutzername und Passwort) müssen daher vorliegen.

Wichtiger Hinweis

Da es sich hier um systemrelevante Einstellungen und Anpassungen handelt, sollte die Einrichtung durch den bzw. mit dem Systembetreuer durchgeführt werden. Die Mitarbeiter von Label und deren Vertriebspartner haben dazu keine ausreichenden Systemrechte und keine ausreichenden Kenntnisse der lokalen Umgebung, um diese Aufgaben durchzuführen. Sie können lediglich beraten und unterstützen.

Allgemeines zur Verzeichnisfreigabe, Laufwerksbuchstabe und Rechte

Zugriff per Laufwerksbuchstabe und Verzeichnis

Da sich Labelwin auf einem zentralen Server-Netzlaufwerk befindet, muss jeder Benutzer von seinem Arbeitsplatzrechner oder Terminalserver-Session Zugriff auf diesen Labelwin-Pfad haben. Die Arbeitsplätze sprechen das Verzeichnis mit Laufwerksbuchstaben und Verzeichnisnamen an. Z.B. L:\labelwin\. Wichtig ist, dass ALLE Benutzer den GLEICHEN Laufwerksbuchstaben und Pfad benutzen.

Wichtig: Labelwin darf aus Sicht des Benutzers nicht im Root, sondern muss in einem Unterverzeichnis liegen.

-

In Ausnahmefällen kann auch ein UNC –Pfad („\\servername\freigabename\“) benutzt werden. Davon raten wir aber ab.

-

Wählen Sie besser einen Laufwerksbuchstaben aus der letzten Hälfte des Alphabetes, damit der Laufwerksbuchstabe nicht mit lokalen Laufwerken der Clientcomputer kollidiert. Bei einem Client mit vielen Laufwerken / Kartenslots bzw. Partitionen können schon mal 10 Laufwerksbuchstaben verbraucht sein.

-

Das Labelwin Verzeichnis sollte - muss aber nicht - Labelwin heißen.

Hinweis: Bei Installationen mit mehreren Instanzen von Labelwin (mehrere unabhängige Firmen), können diese Verzeichnisse auch nach dem Namen der Firma bekommen. Wichtig ist aber, dass die Verzeichnisnamen keine Leerstellen enthalten!

„Domänen Admin“ oder „Lokaler Admin“

In einem Domänen-Netzwerk haben Sie im Unterschied zum Workgroup-Netzwerk, zwei Admin-Konten. Im Normalfall genügt der „Lokale Admin“, da nur auf dem lokalen Arbeitsplatz Installationen vorgenommen werden. Da aber die Quelle für die Installationsdateien im Netz (das zentrale Labelwin Verzeichnis) liegen, benötigen Sie auch als lokaler Admin Zugriff auf das Labelwin Netz-Laufwerk (z.B. L:\). Das ist normalerweise für einen lokalen Admin nicht vorhanden, kann aber eingerichtet werden. Daher macht es Sinn, den Domänen-Admin zu benutzen.

Bitte beachten Sie, dass es häufig nicht genügt, dass ein Benutzer Admin Rechte hat. Es muss schon der Lokale Admin oder der Domänen Admin sein.

Alternativ können Sie für den Installationsteil, der Admin Rechte benötigt, auch den lokalen Admin mit UNC-Pfaden benutzen. Achten Sie aber darauf, dass dieser dennoch Zugriffsrechte auf das Labelwin Netzlaufwerk haben muss.

Terminalserver

Achten Sie darauf, dass die Bereiche der Installation/Einrichtung die Administratorrechte benötigen, im Terminalserver-Installationsmodus durchgeführt werden. Laut Microsoft ist das ab Server 2012 nicht mehr zwingend notwendig, trotzdem empfehlen wir es.

Zugriffsrechte

Alle Benutzer benötigen mit ihrem Benutzerlogin folgende (NTFS-)Rechte auf dem Labelwin Verzeichnis: „Ändern“, „Lesen & Ausführen“, „Verzeichnisse lesen“ und „Schreiben“. Ein „Vollzugriff“ ist nicht notwendig. Die darüberliegende Freigabe (Share) muss mindestens diese Rechte besitzen. Da es hier aber nur „Ändern“ und „Lesen“, sowie „Vollzugriff“ gibt, sollten Sie „Vollzugriff“ freigeben. Jedoch, ganz wichtig, bei der NTFS-Berechtigung bitte ausschließlich „Verzeichnis lesen“. Damit sind Sie auf der sicheren Seite.

Szenario 1:

Auf der Serverfestplatte gibt es das Verzeichnis D:\label\labelwin\. „D:\label\“ wird als Share mit der Laufwerksbuchstabenzuordnung „L:“ freigegeben. Die Clients sehen das Labelwin-Verzeichnis als „L:\labelwin\“

Szenario 2:

Auf der Serverfestplatte gibt es das Verzeichnis D:\anwendungen\label\labelwin\. „D:\anwendungen\“ wird als Share freigegeben, der Share mit dem Unterverzeichnis „labelwin“ wir mit dem Laufwerksbuchstaben „L:“ verknüpft. Die Clients sehen das Labelwin-Verzeichnis als „L:\labelwin\“

Der Vorteil von Szenario 2 ist, dass Sie zusätzlich das Verzeichnis D:\anwendungen\lohn\lohnprog\ haben können, das komplett andere Berechtigungen bekommt.

Beispiel für Szenario 1:

-

Auf der Serverfestplatte gibt es das Verzeichnis D:\ label\labelwin\

-

Das Verzeichnis D:\label\ geben Sie als Share mit Vollzugriff frei. Bei der NTFS Berechtigung vergeben Sie alle Rechte bis auf „Vollzugriff“, also „Ändern“, „Lesen & Ausführen“, „Verzeichnisse lesen“ und „Schreiben“. Die Vererbung bleibt aktiv, denn alle untergeordneten Verzeichnisse benötigen die gleichen Rechte.

-

Mappen Sie auf den Clients das Verzeichnis „label“ des Shares mit dem Laufwerksbuchstaben „L:“, Dadurch sehen die Anwender das Labelwin-Verzeichnis als L:\Labelwin\.

Wichtig: Labelwin darf aus Sicht des Anwenders nicht auf Root-Ebene (L:\) liegen!

Beispiel für Szenario 2:

-

Auf der Serverfestplatte gibt es das Verzeichnis D:\Anwendungen\label\labelwin\ und z.B. das Verzeichnis D:\Anwendungen\lohn\lohnprog\

-

Das Verzeichnis D:\Anwendungen\ geben Sie als Share mit Vollzugriff frei. Bei der NTFS Berechtigung vergeben Sie aber ausschließlich das Recht „Verzeichnisse lesen“. Sinnigerweise „Ohne Vererbung“. Nur so sind Sie auf der sicheren Seite.

-

Das Verzeichnis „label“ ist kein Share und hat somit keine Share-Berechtigungen. Wohl aber NTFS-Berechtigungen. Vergeben Sie alle Rechte bis auf „Vollzugriff“, also „Ändern“, „Lesen & Ausführen“, „Verzeichnisse lesen“ und „Schreiben“. Die Vererbung bleibt aktiv, denn alle untergeordneten Verzeichnisse benötigen die gleichen Rechte.

-

Machen Sie das gleiche mit Lohn und den dort entsprechend notwendigen Rechten

-

Mappen Sie auf den Clients das Verzeichnis „label“ des Shares mit dem Laufwerksbuchstaben „L:“, Dadurch sehen die Anwender das Labelwin-Verzeichnis als L:\Labelwin\.

Wichtig: Labelwin darf aus Sicht des Anwenders nicht auf Root-Ebene (L:\) liegen!

-

Das Verzeichnis „lohn“ des Shares mappen Sie, falls notwendig, mit einem anderen Buchstaben

Die Freigabe bzw. das gemappte Laufwerk, z.B. „L:“, sollte nur das Verzeichnis Labelwin kennen und keine weiteren Verzeichnisse auf gleicher Ebene, es sei denn, sie haben direkt etwas mit Labelwin zu tun und werden von den Labelwin Anwendern benötigt.

Sonstige Hinweise

Die Arbeitsplätze müssen mit dem Betriebssystem komplett eingerichtet sein und das Labelwin-Verzeichnis muss über einen vorangestellten Plattenbuchstaben zur Verfügung stehen (z. B. L:\labelwin\).

Microsoft Office und andere Standard-Fremdprogramme

Labelwin nutzt im Bereich der Textverarbeitung MS-Word, für die Controlling-Ausgaben MS-Excel und für E-Mails MS-Outlook. Für eine umfängliche Nutzung von Labelwin sollten daher diese Programme installiert und eingerichtet sein. Statt Outlook geht auch David. Aber statt MS-Word und MS-Excel funktionieren Open Office Produkte nur sehr eingeschränkt.

Die Installation von Adobe Acrobat Reader ist empfehlenswert. Es geht aber auch jeder andere PDF Viewer. Z.B. MS-Edge.

Drucker

Alle Drucker, die der Benutzer benutzen möchte, müssen selbstverständlich eingerichtet sein. Drucker mit mehreren Einzugsschächten sollten mehrfach installiert sein. D.h., pro Einzugsschacht ein Drucker. Nähere Details siehe weiter unten.

Zur Ausgabe von PDF Dateien und für die Nutzung des Labelwin PDF-Archives ist ein spezieller PDF-Drucker nötig. Dieser heißt eDocPrintpro, kommt von www.pdfprinter.at und ist kostenlos. Die Installation wird im Kapitel PDF Ablage und PDF Drucketreiber beschrieben. Für die Ausgabe von ZUGFeRD PDF Dateien ist eine Erweiterung auf die kostenpflichtige Version eDocPrintpro PDF/A ZUGFeRD nötig. Die Einrichtung wird im Kapitel ZUGFeRD mit PDF/A Druckertreiber erklärt.

Telefonie

Zur Nutzung der Telefonie muss die Telefonanlage TAPI 2.0-fähig und eingerichtet sein. Grundsätzlich kann man davon ausgehen, dass, wenn die Windows Wählhilfe funktioniert, die entsprechenden Voraussetzungen höchstwahrscheinlich gegeben sind.

Dokumentenscanner

Bei Einsatz des Labelwin Scan-Archives ist die Ansteuerung von Dokumentenscannern sinnvoll. Damit das möglich ist, müssen diese TWAIN kompatibel sein. In Terminalserver Umgebungen empfehlen wir die kostenpflichtige Zusatzsoftware TSScan von Terminalworks.
