# 10.4 Inventurwert ermitteln

Pfad: Materialwirtschaft > Lager [Modul] > 10. Inventur > 10.4 Inventurwert ermitteln
Quelle: handbuch/10_4_inventurwert_ermitteln.htm

|

10.4 Inventurwert ermitteln

Mit Hilfe des zugeordneten Einkaufswertes kann sehr schnell der aktuelle Lagerwert ermittelt werden. Jedem Artikel können zwei Einkaufswerte zugeordnet werden, die in der Regel identisch gehalten sind. Über ein Ankreuzfeld bei dem einzelnen Artikel können Sie jedoch festgelegen, dass ein bewerteter Einkaufspreis eingegeben werden kann. Hierbei geht es um die „Ladenhüter“, deren Lagerwert nicht dem aktuellen Einkaufswert beim Großhändler entspricht. Bei der Ausweisung des Inventurwertes wird ein Ergebnis für die normalen Preise und eines für die bewerteten Artikel ausgegeben.

[Bild]

In dem oberen Teil der Maske kann eine Preisübertragung aus den Stammdaten des Haupthändlers vorgenommen werden oder die aufgrund der Wareneingänge gebuchten Lieferscheine erfolgen. Bei der Preisübernahme aus den Wareneingängen besteht allerdings das Problem, dass bei Lieferscheinen häufig keine Einkaufpreise bekannt sind und daher im Protokoll sicherlich oft kein Einkaufspreis gespeichert worden ist. Das Programm sucht rückwärts so lange, bis es einen Preis größer als 0 vor findet. Wenn im Protokoll kein einziger Preis vorhanden ist, so wird automatisch der Einkaufswert aus den Stammdaten des Haupthändlers genommen. Über eine Option können Sie auch den Preis aus dem Feld ‚Einkauf 2’ entnehmen, wenn dieser gefüllt ist. Von dieser Methode raten wir allerdings ab, da der EK 2 in der Regel nicht richtig gepflegt wird.

Über den Knopf ‚Eintragen’ werden die ermittelten Preise bei den jeweiligen Artikeln hinterlegt. Wenn ein Artikel einen bewerteten Einkaufspreis besitzt, so wird dieses Feld nicht verändert. Wenn Sie also einen Artikel bewusst abgewertet haben, wird er durch diesen Lauf nicht wieder mit den aktuellen Preis versehen.

In dem unteren Teil der Maske können Sie über den Knopf ‚Berechnen’ den aktuellen Lagerwert ermitteln.

Bei der Druckausgabe gelangen Sie in den Bereich, in dem sonst auch Lagerlisten gedruckt werden können.
