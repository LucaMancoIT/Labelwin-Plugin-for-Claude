# 3.1 Funktionale Verbindung

Pfad: Kundendienst > TGM - Wartung und Instandhaltung [Modul] > 3. Erfassung > 3.1 Funktionale Verbindung
Quelle: handbuch/3_1_funktionale_verbindung.htm

|

3.1 Funktionale Verbindung

Obwohl die Erfassung der ‚Funktionalen Verbindungen’ in der Praxis erst relativ spät erfolgen wird, haben wir dies Kapitel vor die eigentliche Erfassung der Daten gezogen. Für Ihr Verständnis scheint uns dies wichtig zu sein, da Sie diese Möglichkeit in jeder Stufe der Ortsbeschreibung finden.

|

Bei der ‚Funktionalen Verbindung’ geht es darum, Geräte oder Anlagen miteinander in Beziehung zu setzen, die von der Ortsbeschreibung her nichts miteinander zu tun haben. Bei Störungen kann über diese Verbindungen einfacher die Ursache gefunden werden.

Die Ablagestruktur des Wartungsmoduls geht ja im Prinzip immer von einer Ortsbeschreibung aus, die sich baumartig bis zu den Anlageteilen herunter aufbaut. Diese geographische Beschreibung hat oft nichts mit der Verbindung der Anlagenteile untereinander zu tun.

So können z.B. mehrere Gebäudekomplexe von einem gemeinsamen Kälteerzeuger versorgt werden. Dann sind die Kondensatoren in den einzelnen Gebäuden untergebracht und von der Klassifizierung her (abgesehen von der gemeinsamen Vertragsnummer) völlig anders gekennzeichnet, als die Klassifizierung des Kälteerzeugers.

Über die funktionale Verbindung besteht nun die Möglichkeit, die einzelnen Kondensatoren jeweils mit dem Kälteerzeuger zu verbinden. Diese Verbindung ist besonders bei einer Störung interessant. Wenn nun in einem Gebäude die Kühlung nicht mehr funktioniert, muss man sich im Rechner bis an jenes Kühlelement heranklicken und kann dann über die funktionale Verbindung sofort feststellen, wo der dazugehörige Kälteerzeuger steht. Da sich die funktionale Verbindung auf beliebig viele Elemente beziehen kann, ist es selbstverständlich auch möglich dazwischen geschaltete Verteiler, Pumpen, Regelorgane und dergleichen zu lokalisieren.

Ein Ausdruck aller mit dem Kühlelement verbundenen Elemente ermöglicht es dem Techniker den Fehler schneller einzugrenzen. Dies ist besonders dann wichtig, wenn der Techniker die Anlage nicht kennt und die Rohrführungen in abgehängten Decken geführt werden. Sollte nun der Fehler bei einem übergeordneten Teil zu finden sein, so kann bei diesem wiederum festgestellt werden, welche Teile alle mit ihm verbunden sind. Dabei ist es auch möglich, gegebenenfalls die davon betroffenen Mieter in einer Liste auszugeben, um diese gegebenenfalls über die Störung zu informieren.

Aufbau einer funktionalen Verbindung:

Jedes Element jeder Stufe lässt mit jedem anderen Element verbinden. Selbst eine vertragsübergreifende Zuordnung könnte aufgebaut werden.

[Bild]

Um Ihnen beim Aufbau der logischen Zuordnungen die Arbeit zu erleichtern, besteht die Möglichkeit, einem Element einer beliebigen Stufe ein Kennzeichen ‚funktionales Hauptelement’ mitzugeben.

Beim Aufbau der Verbindung werden nun in einer Auswahlliste sämtliche mit dem entsprechenden Kennzeichen vergebenen Hauptelemente angeboten. Wenn Sie also beispielsweise jenen Kälteerzeuger mit dem Kennzeichen ‚Hauptelement’ versehen, können Sie sehr schnell bei der Erfassung der einzelnen Kondensatoren den Kälteerzeuger mit den einzelnen Kondensatoren verbinden. Darüber hinaus besteht die Möglichkeit auch andere, nicht mit diesem Kennzeichen versehene Elemente über eine Suchmaske zuzuordnen.

Die folgende Maske finden Sie auf jeder Stufe der Datenerfassung, also sowohl beim Vertrag, dem Objekt, dem Komplex usw.

[Bild]

1 Anzeigetabelle: Hier sind alle mit dem aktiven Element verbundenen Elemente aufgelistet.

2 neue Verbindung (Auswahlliste): In dieser Liste werden alle Elemente angeboten, die das Kennzeichen ‚logisches Hauptelement’ bekommen haben. Wenn Sie ein Element verknüpfen wollen, das nicht in dieser Auswahlliste vorhanden ist, betätigen Sie den Knopf ‚Zuordnung suchen’ (Nr. 3).

3 Verbindung suchen-Knopf: Bei Betätigen dieses Knopfes erscheint eine Auswahlliste, mit deren Hilfe Sie ein zu verknüpfendes Element finden können. Wenn Sie die Suchmaske mit dem Okay-Knopf verlassen, wird der Eintrag automatisch gespeichert.

4 Verbindung speichern-Knopf: Durch Betätigen dieses Knopfes wird die gewählte Zuordnung in die Tabelle Nr. 1 übernommen.

5 Verbindung drucken-Knopf: Bei Betätigung dieses Knopfes können Sie alle mit dem aktiven Element verbundenen Elemente ausdrucken.

6 Verbindung löschen-Knopf: Mit diesem Knopf können Sie den in der Tabelle Nr. 1 markierten Eintrag löschen. Selbstverständlich wird nicht das Element selber gelöscht, sondern lediglich die aufgebaute Beziehung zu diesem Element entfernt.
