# Übertragung EK-Preise an Konfigurator

Pfad: Artikelstammdaten > mobile offer–Stücklisten [Modul] > Übertragung EK-Preise an Konfigurator
Quelle: handbuch/ubertragung_ek_preise_an_konfigurator.htm

|

Übertragung der EK-Preise für die mobile offer Stücklisten an den Konfigurator

Stand 12.05.2016

Im Labelwin haben Sie in der Maske „Import mobile offer Stückliste“ (Bild siehe unten) Ihre Lieferanten-Kataloge zugeordnet und darüber mit der Funktion „Verknüpfen“ Ihre tatsächlichen Einkaufspreise auf die mobile offer Stücklisten übertragen. Mit der hier beschriebenen Methode können Sie nun diese EK-Preise in den Konfigurator übertragen, sodass Sie dann auch dort mit Ihren tatsächlichen EK-Preisen kalkulieren.

Vorbereitung/Voraussetzung

Voraussetzung ist natürlich, dass Sie mithilfe der Anleitung „Installation und Update“ die EK-Preise eingestellt/verknüpft haben.

Schritt 1: Preise aus Labelwin rausschreiben

In der Maske „Import mobile offer Stückliste“ gibt es auf der rechten Seite die Funktion „Preise => mobile offer“. Bitte betätigen Sie diese.

[Bild]

Wenn diese Routine zu Ende gelaufen ist, liegt eine entsprechende Datei im Verzeichnis „…Labelwin/Datanorm/mo-Daten“ und ein Protokoll öffnet sich, dass Ihnen evtl. Hinweise anzeigt. Dabei handelt es sich um Artikel denen über das „verknüpfen“ nicht ausreichende Preisinformationen seitens Ihrer Lieferanten zugeordnet werden konnten. Für diese Artikel, soweit vorhanden, wird der voreingestellte „mobile offer Preis“ übertragen (den Sie wie im Kapitel Installation und Update beschrieben, über die Rabattgruppen im Katalogmodul auch einstellen können).

Schritt 2: Preise in den Konfigurator einlesen

Öffnen Sie über das StartCenter des Konfigurator den Programmteil Individualisierung. Dort wählen Sie das Register „Preise“.

[Bild]

Nun wählen Sie in der obersten Zeile („LAB/Datenübernahme LABEL“) den Button „einlesen“ und im sich dann öffnenden den Fenster den Pfad „…Labelwin/Datanorm/mo-Daten“ und dann OK.

Nun werden die Preise in den Konfigurator eingelesen. Sollte zwischenzeitlich „nichts“ passieren oder das Fenster „eine Rückmeldung“ anzeigen, haben Sie bitte einen Moment Geduld, Sie werden erkennen, wenn die Routine durchgelaufen ist.

Preis-Update / mobile offer Update

Sollten sich später die EK-Preise im Labelwin ändern oder im Falle eines mobile offer-Updates, wiederholen Sie die Schritte 1 und 2 (evtl. 3)

Schritt 3: Fehlende Artikelpreise und Kalkulationsfaktoren prüfen

Vereinzelt kann es dazu kommen, dass zu einem Artikel kein Preis aus dem Labelwin übertragen wird. Dies können Sie erkennen, wenn sie unter dem Register „Kalkulationsgruppen“ hinter einer Kalkulationsgruppe den Hinweis finden „enthält Artikel ohne GH-Preis/bestätigten Preis)“.

[Bild]

Öffnen Sie die entsprechende Kalkulationsgruppe über den Button in der Spalte „Artikel“ und sehen Sie sich die Artikel an. Alle Artikel mit dem Hinweis „LAB-Preis“ haben einen Preis aus Labelwin. Alle Artikel mit dem Hinweis „Eigener-Preis“ haben keinen Preis aus Labelwin (aber es sollten in der Regel nur eine „handvoll“ sein.

[Bild]

Sie haben nun hinsichtlich der Artikel mit „Eigener Preis“ zwei Möglichkeiten:

-

Sie bestätigen diesen Preis mit „K“. Somit ist der Artikel „konfigurierbar“ und hat einen Preis. Einstellen, bzw. verändern können Sie den Preis über die entsprechende Rabattgruppe und den dazu eingetragenen Rabatt unter dem Register „Rabattgruppen für Artikel mit Eigener Preis“ oder über die Lohnminuten.

-

Sie bestätigen diesen Preis nicht mit „K“. In diesem Fall wird in der Ergebnissicht des Konfigurators „ein Preis vorhanden“ angezeigt, falls der Artikel in der Konfiguration vorkommt. Sie könnten dann z.B. dem Kunden den Hinweis geben, dass Sie spontan keinen Preis nennen können und diesen erst einholen müssen.

Über die Funktion oben rechts „Seite vor/Seite zurück“ können Sie vor und zurückblättern, wenn es mehrere Seiten gibt (wie im Bild z.B. 9).

Hinweis: Zuschläge einstellen

Im Register „Kalkulationsgruppen“ können Sie über die Spalte „ Aufschlag auf Netto“ für die einzelnen Gruppen auch Ihre Zuschläge eintragen, bzw. die dort hinterlegten Zuschläge ändern.

Hinweis: Andere Großhändler/Hersteller unter „Preise“ (s. Schritt 2)

Unter dem Register „reise“ gibt es in der Zeile unter „LAB“ auch die diversen Großhändler und Hersteller. Dort müssen/sollten Sie allerdings nichts einlesen!!! Es würde unter Umständen einiges durcheinanderbringen und Sie benötigen diese Funktionen auch gar nicht, da Sie ja die Preise aus dem Labelwin übernehmen.

Hinweis: Register „Rabattgruppen für Artikel mit Eigener Preis“

Bis auf vereinzelte Artikel die womöglich auf „Eigener-Preis“ stehen bleiben (siehe Schritt 3), benötigen Sie das Register „Rabattgruppen für Artikel mit Eigener Preis“ nicht. Dort werden auch nicht die Rabatte angezeigt, die Sie aus Labelwin übernehmen. Wie der Name des Registers auch sagt, gelten die hier manuell eingetragenen und veränderbaren Rabattwerte nur für Artikel die keinen Preis aus dem Labelwin erhalten haben und auf „Eigener Preis“ stehen bleiben (siehe Schritt 3).

WICHTIGER HINWEIS: Übergabe des Konfigurationsergebnisses nach Labelwin!

Wenn Sie die EK-Preise in den Konfigurator übergeben haben, ist es wichtig bei Erzeugung der UGL-Datei, die Sie am Ende einer Konfiguration ins Labelwin übergeben wollen, die richtige Auswahl zu treffen!

Wählen Sie bitte unbedingt am Ende der Konfiguration unter „Ergebnis“ den Button „xport erweiterte mobile offer-UGL“! Den anderen Button „Export Standard-UGL“ benötigen Sie als Label-Kunde nicht!

In der dann folgenden Auswahl wählen Sie bitte: „Die mobile offer-Artikelnummer?“

[Bild]
