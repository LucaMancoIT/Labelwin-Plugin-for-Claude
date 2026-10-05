# 12. Kalkulation mit Excel

Pfad: Projektverwaltung > Projektverwaltung [2] > 12. Kalkulation mit Excel
Quelle: handbuch/12__kalkulation_mit_excel.htm

|

12. Kalkulation mit Excel

5.10.2014

Hinweis: Diese Funktion steht nur zur Verfügung, wenn das Modul CONTROLLING erworben wurde.

Obwohl Labelwin alle Änderungen der Kalkulation komfortabel über die Schnelländerung, die Blockbearbeitung und die ‚große‘ Umkalkulation ermöglicht, gibt es Situationen, in denen die Erfassung und Änderung mit Excel sinnvoll ist.

- Das Angebot kann als Exceltabelle zur Auftragsvergabe mitgenommen werden.

- Ein Mitarbeiter ist nicht in der Lage, Labelwin zu bedienen und kann aber gut kalkulieren

(ja, solche Leute gibt es)

- Man kann die Einkaufspreise von einer Hilfskraft eintragen lassen, die Labelwin nicht beherrschen muss.

- Die Eingabe der Preise und Minuten ist so sehr übersichtlich und schnell möglich

- Ein Subunternehmer soll seine Preise selber eingeben

- Man kann verschiedene Kalkulations-Vorgänge durchspielen, ohne sich um Sicherungen Gedanken zu machen

Ablauf Export

Ein markiertes Dokument kann per Menüpunkt (Projektverwaltung, Extern) in eine Exceltabelle geschaufelt werden. Dabei werden einige Vorlagen angeboten. Die gewählte Vorlage wird kopiert und mit den Daten gefüllt. Ggf. bekommen Sie eine Meldung, dass die Gesamtsummen in der Tabelle nicht stimmen. Das ist immer dann der Fall, wenn im Dokument Alternativ-Titel, vorkalkulierte Sets oder Prozentpositionen auf nur Lohn oder Material enthalten sind.

In den Tabellen sind die auszufüllenden Daten gelb markiert. Leider sind die anderen Felder aber nicht geschützt. Wenn wir die Tabelle vorher schützen, können wir selber keine Daten hinein bekommen. Den Blattschutz müssen Sie also ggf. selber vornehmen. Das geht aber sehr schnell:

Wählen Sie den Reiter ‚Überprüfen‘ und klicken auf das Bild ‚Blatt schützen‘

[Bild]

[Bild]

Entfernen Sie aus der dann erscheinenden Maske den Haken bei ‚gesperrte Zellen auswählen‘ und drücken den Okay-Knopf.

Auf die Eingabe eines Kennwortes sollten Sie verzichten.

Ablauf Import

Zum Importieren markieren Sie das Dokument, in das die Werte aus der Exceltabelle einfließen sollen. Dies kann durchaus auch eine Kopie des ursprünglichen Dokumentes sein. Besonders für die ersten Versuche empfehlen wir dies eindringlich.

Beim Übergang von Daten aus einer Exceltabelle kann viel schiefgehen, wenn in dieser Einträge unzulässig verändert wurden. Mit dem oben angesprochenen Blattschutz kann dies aber verhindert werden.

In einem ausführlichen Protokoll können Sie die Änderungen nachvollziehen.

Wählen Sie in der Projektverwaltung die Menüpunkte <Extern>, <Excel-Kalkulation importieren> an. Kreuzen Sie hier an, welche Felder Sie aus Excel in das Dokument übertragen wollen. Irritierend ist vielleicht, dass Sie den Multi und den Verkauf nicht gleichzeitig übernehmen können. Da Labelwin entweder den Verkauf über den Multi ermittelt oder den Multi über das Verhältnis Einkauf zu Verkauf berechnet, kann nicht beides übernommen werden. Es wird ggf. Abweichungen im Rundungsbereich geben, weil Labelwin Preise grundsätzlich auf 2 Nachkommastellen rundet, Excel dagegen mit allen Stellen rechnet, aber nur 2 anzeigt.

[Bild]

Mit dem Ankreuzfeld ‚Simulation‘ werden alle Änderungen protokolliert, aber nicht in das Dokument übertragen.
