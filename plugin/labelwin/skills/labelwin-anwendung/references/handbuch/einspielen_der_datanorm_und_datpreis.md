# Einspielen der Datanorm und Datpreis

Pfad: Schnittstellen > ZVEH und Meta-Daten > Einspielen der Datanorm und Datpreis
Quelle: handbuch/einspielen_der_datanorm_und_datpreis.htm

|

Einspielen der Datanorm und Datpreis

Der ZVEH liefert seine Daten auf der CD in unterschiedlichen Formaten. Für Labelwin sind die Datanormdateien zu verwenden. Diese werden zunächst auf der Festplatte abgelegt und können dann mit der ‚normalen’ Methode ins Labelwin eingespielt werden.

Beim Einlegen der e-CD 2 startet die Autostartfunktion oder sie starten von der CD mit der Datei CDStart.htm.

[Bild]

Wählen sie links den Punkt Kalkulationshilfe.

[Bild]

Wählen sie jetzt den Punkt Datanorm 4.x im Bereich Kalkulationshilfe (KfE) mit Stückliste.

[Bild]

Wählen Sie jetzt das Diskettensymbol hinter mit Einkaufspreisen A-Satz.

Gehen sie dann auf ‚Daten installieren’ und ,Ausführen’.

[Bild]

Die Datanorm Dateien werden dann in das Verzeichnis c:\zveh\2007\kfedat4_mstl_ek entpackt.

Einspielung des ZVEH Kataloges in Labelwin

Da bei der Einspielung einige Besonderheiten zu programmieren waren, benötigt Labelwin eine Information darüber, dass es sich um ZVEH-Daten handelt.

Der Name des Labelwin – Kataloges muss zwingend mit den Buchstaben ZVEH anfangen, danach können beliebige Beschreibungen folgen. Die Gross/Kleinschrift ist egal.

Die ZVEH-Daten werden genau so wie alle anderen Datanorm-Kataloge eingespielt.

Datanorm und Datpreis

Spielen Sie die Daten wie bei allen anderen Lieferanten ein.

Folgende Dateien werden entpackt.

DATANORM.001 Daten der Kalkulationshilfe (ohne Kapitel 28)

DATASETS.001 Stückliste der Kalkulationshilfe (ohne Kapitel 28)

DATANORM.002 Stücklistenartikel mit Nettopreis (Kennzeichen A)

DATANORM.003 Bauzeiten der Stücklistenartikel in Minuten

DATANORM.004 Bauzeiten der Stücklistenartikel in AW (100er Teilung)

DATANORM.028 Daten der Kalkulationshilfe Bereich IT-Servicearbeiten

DATANORM.029 Stücklistenartikel IT-Bereich

DATANORM.128 Bauzeiten der Stücklistenartikel in Minuten

DATANORM.228 Bauzeiten der Stücklistenartikel in AW (100er Teilung)

DATASETS.028 Stückliste Kapitel 28

Die folgende Maske ist nur informationshalber abgebildet – es sind keine besonderen Einstellungen zu treffen.

[Bild]

[Bild]

Hier dürfen Sie die Datei Datanorm.004 und Datanorm.228 nicht einspielen !

Diese Dateien enthalten Arbeitswerte und sie haben ja mit den Dateien Datanorm.003 und Datanorm.128 schon Minuten eingespielt.
