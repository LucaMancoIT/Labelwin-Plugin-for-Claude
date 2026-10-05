# 2. ÖNorm bearbeiten (bepreisen)

Pfad: Schnittstellen > ÖNorm > 2. ÖNorm bearbeiten (bepreisen)
Quelle: handbuch/2__onorm_bearbeiten__bepreisen_.htm

|

2. ÖNorm bearbeiten (bepreisen)

Weitere Artikelinfo

Da systembedingt nicht alle ÖNorm Informationen in Labelwin verarbeitet werden können, wird pro Position der XML Originalausschnitt hinterm Artikel gespeichert. Klicken Sie in der Artikelaufruf Maske auf den Knopf „ÖNorm-Info“.

[Bild]

Bieterlücken

In manchen LVs sind im Langtext Bieterlücken markiert, in denen der Bieter den Text ergänzen muss, z.B. durch den Namen des gleichwertigen Fabrikats. Diese Bieterlücken sind gekennzeichnet durch [bl]$[/bl]. Das $-Zeichen bewirkt, dass Sie beim Verlassen der Position in ein Ersetzungsfenster kommen.

Hier müssen Sie nun jedes $-Zeichen entfernen oder durch einen Text ersetzen. Bitte lassen Sie unbedingt das [bl] und [/bl] stehen und ändern, löschen oder ergänzen Sie keine anderen Textstellen!

Ein Muster für eine Bieterergänzung sehen Sie hier (Die wichtigen Stellen sind fett markiert).

Kälteleistung:

min. 1,9 kW bei -30°C Verdampfungstemperatur

Fabrikat: LU-VE

Type: BHA 28 E 80

Druckprüfung: mind. 28 bar

Fabrikate: Küba, Güntner, LU-VE

oder gleichwertig

Fabrikat: [bl]$[/bl]

Kälteleistung: bei -30°C VT [bl]$[/bl] kw

Luftleistung: [bl]$[/bl] m3/h

Abmessungen-Gerät HxBxT: [bl]$[/bl] mm

Gewicht:[bl]$[/bl] kg

Beim Rausschreiben werden diese (ausgefüllten) Bieterlücken rausgesucht und entsprechend mit ausgegeben.

[Bild]

Bitte beachten Sie, dass es auch Bieterlücken in den Textartikeln am Anfang des LV’S geben kann. Damit Sie die Positionen besser finden, bekommen sie beim Einlesen einen Merker gesetzt.

Mit <Bearbeiten>, <Suchen> oder STRG-F können Sie das ganze Dokument nach Positionen mit gesetzten Merken suchen.

Vergessen Sie nicht, nach dem Füllen der Bieterlücken diesen Haken bei Merker zu entfernen.

Tipp: Damit Sie beim ersten Bepreisen und Lesen nicht ständig über das Textersetzungsfenster kommen, welches Sie erst zu einem späteren Zeitpunkt ausfüllen möchten, können Sie über den Menüpunkt <Optionen>, <$-Textersetzungen ignorieren> das Fenster ausblenden.

Textformatierungen

Doe ÖNorm unterstützt formatierte Texte. Allerdings benutzt die ÖNorm eine sehr eigene und eingeschränkte Syntax, so dass Labelwin diese Formatierungsbefehle nicht unterstützt. Alle Formatierungsbefehle (z.B. fett, unterstrichen etc.) werden ignoriert. Aufzählungszeichen (Bullets) werden durch einen führenden Bindestrich ersetzt. Nicht interpretierbare Formatierungsbefehle, z.B. Tabellendefinitionen, bleiben als Formatierungskennzeichen stehen, z.B. „<table>“, „<td>“, „<tr>“ etc.

Rabatte/Nachlässe/Zuschläge

Bitte bepreisen Sie die Positionen mit den Endpreisen. Zwar erlaubt die ÖNorm die Definition von Nachlässen und Zuschlägen auf Bauteile, Lose, Titel und das gesamte LV, allerdings kann diese Technik nicht ganz sauber in Labelwin abgebildet werden. Sie auch die Anmerkungen weiter oben dazu.

Sollten Sie es dennoch machen wollen bzw. müssen, dann können Sie einen Nachlass/Zuschlag für das gesamte LV in der ÖNorm-Ausgabe Maske hinterlegen (siehe weiter unten) oder am Ende eines Titels, Los oder Bauteils. Bei der letzteren Methode müssen Sie als letzte Position vor der Titelsumme (bzw. Lossumme/Bauteilsumme) eine Prozentposition mit der Eingrenzung auf „auf letzten Titel“ erfassen. Alle anderen Eingrenzungsarten (z.B. von Position bis Position) sind nicht erlaubt.

Ob und an welchen Stellen Sie Rabatte bzw. Zuschläge geben können, steht in den Kopfdaten der ÖNorm Datei. Näheres dazu siehe oben.

Preisanteil Aufgliederung

Bei der ÖNorm Ausgabe entscheiden Sie, ob Sie eine Preisaufgliederung, also Lohn und Material getrennt, ausgeben möchten. Beachten Sie, dass die Trennung nur erlaubt ist (bzw. sogar verpflichtend ist), wenn es in der eingelesenen ÖNorm definiert wurde. Auch diese Information finden Sie in den Kopfdaten (siehe oben). Näheres dazu auch unter Kapitel „3.x.4 Önorm ausgeben“.
