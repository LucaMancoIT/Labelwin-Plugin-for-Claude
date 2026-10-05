# 7.8 Update auf mobilem Gerät

Pfad: Kundendienst > KD-Mobil Notebook [Modul] > 7. Installation und Einrichtungsarbeiten > 7.8 Update auf mobilem Gerät
Quelle: handbuch/7_8_update_auf_mobilem_gerat.htm

|

7.8 Update auf mobilem Gerät

Hier müssen wir zwei verschiedene Updates unterscheiden:

A) Update des Programmes KD-Mobil

B) Erneuerung der Grunddaten aus der Zentrale

Beide Updatearten können in einem Rutsch direkt hintereinander ablaufen.

A) Update des Programmes KD-Mobil

Wenn in der Zentrale eine neue Labelwin-Version eingespielt wurde, ist es in der Regel erforderlich, auch auf dem mobilen Gerät die Programme zu erneuern. Hier gibt es mehrere Möglichkeiten:

1. Starten Sie nach Einspielen des Updates in der Zentrale wie im Kapitel Erstinstallation und Aktualisierung beschrieben das Programm KD Daten Export (KdexpZen.exe). Wählen Sie dort unter „Transportieren“ die Updatedateien aus und übertragen diese in einen frei wählbaren Transport-Pfad.

[Bild]

Starten Sie danach auf dem Notebook das Programm „Update einspielen“ (labelwineinricht.exe). Geben Sie hier als Quellpfad das Transportverzeichnis an.

Info: Über diesen Weg können Sie auch neue Grunddaten aus der Zentrale an das Notebook übertragen. Über eine Nachfrage kommen Sie zuletzt in den Bereich, in dem neue Grunddaten importiert werden können.

2. Sie holen auf dem Notebook das Update auch aus dem Internet (iupd.exe).

Das ist aber eigentlich nur sinnvoll, wenn das Gerät in einem WLAN ist oder eine unbegrenzte Flatrate hat. Über diesen Weg können Sie keine neuen Grunddaten aus der Zentrale an das Notebook übertragen.

Weitere Möglichkeiten, die aber an sich zu aufwändig sind und leicht schief gehen:

3. Kopieren Sie alle Dateien aus dem Verzeichnis \labelwin\update aus der Zentrale in das Verzeichnis \labelwin\update auf dem Notebook und starten sie dann die Verknüpfung „Update einspielen“ (labelwineinricht.exe) auf dem Notebook. Geben sie dann als Quellpfad für das Update das Verzeichnis \labelwin\update des Notebooks an

4. Kopieren Sie alle Dateien aus dem Verzeichnis \labelwin\update der Zentrale in ein Verzeichnis auf einen USB Stick und starten sie dann die Verknüpfung „Update einspielen“ (labelwineinricht.exe) auf dem Notebook. Geben sie als Quellpfad für das Update das Verzeichnis auf dem Stick an

5. Wenn Sie das Notebook im Netzwerk anmelden können, brauchen sie nichts kopieren. Starten Sie dann die Verknüpfung „Update einspielen“ (labelwineinricht.exe) auf dem Notebook und geben als Quellpfad für das Update das Verzeichnis \labelwin\update vom Server an

B) Erneuerung der Grunddaten aus der Zentrale

1. Starten Sie in der Zentrale wie im Kapitel Erstinstallation und Aktualisierung beschrieben das Programm KdexpZen.exe. Wählen Sie dort die Grunddaten aus und übertragen diese in den Transportpfad.

[Bild]

2. Starten Sie anschließend auf dem Notebook das Programm Grunddaten importieren (oder die kdimnbgr.exe - das steht für "KD Import Notebook Grunddaten"). Dort wird das letzte Transportverzeichnis vorgeschlagen. Falls es sich geändert hat, können Sie es aber auch neu wählen. Alles Weitere ist wie bei der weiter oben beschriebenen Neuinstallation.
