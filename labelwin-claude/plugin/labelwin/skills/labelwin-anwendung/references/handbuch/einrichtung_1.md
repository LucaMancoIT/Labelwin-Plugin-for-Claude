# Einrichtung

Pfad: Zeitwirtschaft > Zeiterfassung [11] > 5. Automatische Stundenzulagen > Einrichtung
Quelle: handbuch/einrichtung_1.htm

|

Einrichtung

Damit Zulagen automatisch erzeugt werden können, müssen diese überhaupt erst einmal exisitieren. Legen Sie daher - soweit nicht schon in der Vergangenheit geschehen - im Modul EINSTELLUNGEN unter [Programmbereiche - Zeitwirtschaft - Zulagen Stunden] die benötigten Zulagen an. Sinnvoll sind Zulagen wie "Zulage 25 %", "Zulage 50 %" etc. Details zur Anlage von Zulagen erfahren Sie im Kapitel EINSTELLUNGEN - Zeitwirtschaft - Zulagen Stunden.

Wie in der Einleitung erwähnt, können automatische Zulagen aufgrund der Uhrzeit und/oder aufgrund der Dauer erzeugt werden. Es ergeben sich daraus insgesamt sechs Varianten der Zulagenermittlung:

1. Zulage nur nach Uhzeit

2. Zulagen nach Uhrzeit und Dauer mit Vorrang Uhrzeit

3. Zulage nur nach Dauer

4. Zulage nach Uhrzeit und Dauer mit Vorrang Dauer

5. Zulage nach Uhrzeit oder Dauer (mit Optimum für Monteur)

6. Zulagen nach Uhrzeit und Dauer

Die Einrichtung wird im folgenden erläutert:

1. Zulagen nach UHRZEIT

Wählen Sie im Modul EINSTELLUNGEN den Menüpunkt [Programmbereiche - Zeitwirtschaft - Automatische Zulagen - Zulagen nach Uhrzeit] an. Es öffnet sich die Maske zur Festlegung der automatischen Zulagen aufgrund der Uhrzeit der Arbeit.

[Bild: Einrichtung]

In dieser Maske definieren Sie bei welcher Tagesart zu welchen Zeiten welche Zulage angesetzt wird. Wichtig hierbei ist, dass Sie ALLE Zeiten eines Tages mit der Tabelle abdecken müssen. Zeiten, in denen keine Zulagen gezahlt werden, müssen trotzdem registriert werden (mit 'Keine Zulage').

Beispiel:

|

Donnerstag

Donnerstag

Donnerstag

Donnerstag

Donnerstag

|

00 bis 06 Uhr

06 bis 16 Uhr

16 bis 18 Uhr

18 bis 21 Uhr

21 bis 24 Uhr

|

Zulage 100 %

keine Zulage

Zulage 25 %

Zulage 50 %

Zulage 100 %

|

(= Zulage Nachtarbeit)

(= reguläre Arbeitszeit)

(= Zulage Nachmittag)

(= Zulage Abend)

(= Zulage Nachtarbeit)

Hinweis: Mitternacht (24:00) kann nicht erfasst werden. Tragen Sie bitte 23:59 Uhr ein.

|
[Bild: 1]

Neue Tagesart

[Bild: 1. Neue Tagesart]

Über die Tagesart wird festgelegt, welche Regeln an welchen Tagen genutzt werden. Die Tagesarten können Sie selber definieren, nur die normalen Wochentage sind schon angelegt. Weitere Tagesarten sind z.B. Normale Feiertage, Heiligabend (wenn dort andere Zulagen oder andere Zeiten gelten), Hohe Feiertage, Karneval oder was auch immer bei Ihnen für unterschiedliche Tagesarten mit unterschiedlichen Zulagen versehen werden.

[Bild]

|
[Bild: 2]

Vorlage nehmen

[Bild: 2. Vorlage nehmen]

Wenn Sie für einen Tag, z.B. den Montag, die gewünschten Einstellungen vorgenommen haben, können Sie diese als Vorlage für einen anderen Tag übernehmen. Stellen Sie dazu die Tagesart auf den gewünschten Zielwert ein, also z.B. Dienstag, und wählen dann über diesen Button die Tagesart, aus der Sie die Daten übernehmen möchten, also in diesem Fall Montag.

[Bild]

Feiertage

|

Damit ein Feiertag auch als Feiertag (oder als Hoher Feiertag, Karneval etc.) bei der automatischen Zulagenermittlung erkannt wird, muss in der Feiertagstabelle die Tagesart zugewiesen werden.

Die Feiertage werden im Modul EINSTELLUNGEN unter [Programmbereiche - Kundendienst - Feiertage] verwaltet. Hier muss den Feiertagen die passende Tagesart zugewiesen werden. Wenn Sie nur mit einer Tagesart "Feiertag" arbeiten, müssen alle Feiertage diese Tagesart erhalten. Differenzieren Sie aber (normaler Feiertag, Hoher Feiertag, Heiligabend etc.) muss die Zuweisung entsprechend stattfinden.

In der nebenstehenden Maske sehen Sie wie das ganze aussehen könnte.

|

[Bild]

1. Zulagen nur nach UHRZEIT

Soll nur mit Zulagen aufgrund der Uhrzeit gearbeitet werden, darf die Zulagenermittlung aufgrund der Dauer nicht aktiviert werden. Der Haken bei "Zulagenbuchung aufgrund der gearbeiteten Tagesstunden" darf also im Bereich [Programmbereiche - Zeitwirtschaft - Automatische Zulagen - Überstunden] nicht gesetzt werden.

Die Wahl der Methode im Modul EINSTELLUNGEN unter [Programmbereiche - Zeitwirtschaft - Automatische Zulagen - Methode] ist dann egal.

2. Zulagen mit Vorrang UHRZEIT

Soll dagegen mit Zulagen aufgrund der Uhrzeit und Dauer gearbeitet werden, wobei die Zulagen nach Uhrzeit vorrangig ermittelt werden, müssen beide Methoden eingerichtet sein und zusätzlich die entsprechende Methode im Modul EINSTELLUNGEN unter [Programmbereiche - Zeitwirtschaft - Automatische Zulagen - Methode] gewählt werden:

[Bild]

Um es einmal klarzustellen, bei dieser Methode wird zuerst geschaut, ob eine Zulage aufgrund der Uhrzeit anfällt. Ist das der Fall, wird diese eingetragen. Gibt es allerdings keine, wird weitergeschaut, ob eine Zulage nach Dauer anfällt. Ist dem so, wird diese eingetragen. Trifft keins von beiden zu, wird natürlich keine Zulage erzeugt.

3. Zulagen nach DAUER

Neben den Zuschlägen nach Uhrzeit kann man auch automatische Zulagen aufgrund von Überstunden erzeugen lassen. Um diese Form des automatischen Zuschlags zu aktivieren, muss im Modul EINSTELLUNGEN unter [Programmbereiche - Zeitwirtschaft - Automatische Zulagen - Überstunden] der Haken bei "Zulagenbuchung aufgrund der gearbeiteten Tagesstunden" gesetzt werden.

[Bild]

Desweiteren ist hier festzulegen (1) wohin die zusätzlichen Kosten gebucht werden sollen, (2) wie das Tages-Soll festgelegt wird und (3) welche Zulagen verwendet werden sollen.

(1) Buchungsprojekt: Möglich ist die Angabe eines gesonderten Sammelprojektes (das zuvor angelegt werden muss) oder die Einstellung, dass die Zulagen immer auf das gearbeitete Projekt gebucht werden sollen.

Da die Kosten für gewährte Überstunden-Zuschläge eigentlich nicht dem Projekt zu Lasten gelegt werden können, empfehlen wir die Zuordnung zu einem gesonderten Sammelprojekt für Zuschläge.

(2) Tagessoll: Die Vorgabe kann entweder aus den Standard-Arbeitszeiten kommen oder aus der indivduellen Arbeitszeittabelle des Monteurs oder fest vorgegeben werden.

(3) Zulagen: Es können zwei verschiedene Zulagen hinterlegt werden. Die erste Zulage gilt bis zu einer gewissen Anzahl Stunden über Soll. Die zweite Zulage gilt darüberhinaus.

3. Zulagen nur nach DAUER

Soll nur mit Zulagen aufgrund der Dauer gearbeitet werden, darf unter [Programmbereiche - Zeitwirtschaft - Automatische Zulagen - Zulagen nach Uhrzeit] kein Eintrag gemacht worden sein. Die Wahl der Methode im Modul EINSTELLUNGEN unter [Programmbereiche - Zeitwirtschaft - Automatische Zulagen - Methode] ist egal.

4. Zulagen mit Vorrang DAUER

Soll dagegen mit Zulagen aufgrund der Dauer und Uhrzeit gearbeitet werden, wobei die Zulagen nach Dauer vorrangig ermittelt werden, müssen beide Methoden eingerichtet sein und zusätzlich die entsprechende Methode im Modul EINSTELLUNGEN unter [Programmbereiche - Zeitwirtschaft - Automatische Zulagen - Methode] gewählt werden:

[Bild]

Um es einmal klarzustellen, bei dieser Methode wird zuerst geschaut, ob eine Zulage aufgrund der Dauer anfällt. Ist das der Fall, wird diese eingetragen. Gibt es allerdings keine, wird weitergeschaut, ob eine Zulage nach Uhrzeit anfällt. Ist dem so, wird diese eingetragen. Trifft keins von beiden zu, wird natürlich keine Zulage erzeugt.

5. Optimale Zulage für Mitarbeiter

Die Einrichtung der Zulagen Methoden nach Dauer und nach Uhrzeit muss wie oben beschrieben erfolgen. Im Modul EINSTELLUNGEN muss dann nur noch unter [Programmbereiche - Zeitwirtschaft - Automatische Zulagen - Methode] die Methode "Optimale Zulage für Mitarbeiter" gewählt werden. Es werden dann immer die Zulagen nach beiden Methoden berechnet, aber nur die für den Mitarbeiter bessere gewählt.

[Bild]

6. Zulagen aufgrund der Dauer und Uhrzeit

Wird unter [Programmbereiche - Zeitwirtschaft - Automatische Zulagen - Methode] im Modul EINSTELLUNGEN die Option "Nur eine Zulage vergeben" nicht angewählt, werden beide Methoden berücksichtigt. Der Mitarbeiter kann somit gleichzeitig eine Zulage für Überstunden als auch für die Uhrzeit erhalten.

[Bild]
