# Kundeninfo per E-Mail /SMS

Pfad: Adressverwaltung > Kundeninfo per E-Mail /SMS
Quelle: handbuch/kundeninfo_per_e_mail__sms.htm

|

Kundeninfo per E-Mail /SMS

Stand: 21.10.2016

(V5.72)

Benachrichtigungen an den Endkunden über seinen Auftragsstand per E-Mail oder SMS.

Die Kommunikation mit dem Kunden wird zunehmend wichtiger. In Zeiten, wo man bei einer Internetbestellung von Amazon und anderen mit E-Mails zugeschüttet wird, erwarten manche Anwender so etwas auch von Ihnen. Außerdem sparen Sie sich vielleicht auch so manche Nachfrage vom Kunden, wenn Sie ihn rechtzeitig informieren.

Situationen, in denen Sie den Kunden über etwas informieren möchten, gibt es sicherlich viele. Als automatisierbar haben wir zunächst erkannt:

-

im Kundendienst die Anlage eines neuen Auftrags

-

eine Terminänderung,

-

die Erledigung eines Auftrags (dies sollte eigentlich überflüssig sein, wenn Sie sehr zeitnah die Rechnung schreiben, aber das klappt ja nicht immer)

-

der Wareneingang von für den Kunden speziell bestellten Waren.

Sie können am Ende einer bestimmten, von Labelwin vordefinierten Situation, automatisch oder manuell eine E-Mail oder eine SMS an den Endkunden versenden. Die derzeit definierten Situationen sind:

-

Beim Wareneingang (nur in V4 ab 4.74)

-

Beim Anlegen eines KD-Auftrages

-

Bei Terminverschiebung eines KD-Auftrages

-

Nach Abschluss des KD-Auftrages.

Diese Funktion ist nur in der V5 Programmversion verfügbar.

Voraussetzungen:

Da diese Funktion auch im Hintergrund und ohne ein Oberflächenfenster ablaufen kann, muss bei jeder betroffenen Adresse eine spezielle E-Mail Adresse oder SMS-Nummer hinterlegt werden.

Außerdem benötigen Sie Bausteine, die bei den entsprechenden Situationen benutzt werden.

Der SMS-Versand funktioniert natürlich nur, wenn Sie das SMS-Modul erworben haben, es auf Ihrem Arbeitsplatz freigeschaltet haben (Modul EINSTELLUNGEN, Menüpunkt <Programmbereiche><Adressen><SMS-Versand>) und Sie ein SMS Guthaben haben.

TUTORIAL VIDEO

Im folgenden Tutorial Video wird die Einrichtung und Handhabung der Kundeninfo beschrieben. In den folgenden Unterkapiteln können Sie alles nochmal nachlesen.

https://www.youtube.com/watch?v=vRIRj9K3Ln4

EINRICHTUNG

Die Einrichtung und Anwendung der Funktion "Kundeninfo" wird in dem obigen Tutorial Video anschaulich erklärt. Hier fassen wir das wichtigste einmal zusammen:

Hinterlegung der E-Mail und SMS Daten in der Adresse

|

Die erforderlichen Daten müssen bei der Rechnungsadresse hinterlegt werden. Also bei der Adresse, die sonst im Fensterumschlag sichtbar wäre. Sie gelangen in die entsprechende Maske über die Schaltfläche „Kundeninfo“ in der Adressmaske (im Rahmen „Kommunikation“).

|

[Bild]

Hier hinterlegen Sie eine oder mehrere E-Mail Adressen (ggf. mit Komma getrennt), sowie bei Bedarf eine (nur eine!) Handynummer für den SMS Versand. Wir greifen bewusst nicht auf eine E-Mail Adresse aus dem Hauptfenster oder dem Telefonreiter zurück, denn wir wissen nicht, welche die richtige ist. Außerdem können Sie für die Kundeninfo auch die E-Mail Adresse oder die SMS-Nummer des Hausmeisters hinterlegen.

[Bild: Kundeninfo per E-Mail /SMS]

|
[Bild: 1]

E-Mail Empfänger

[Bild: 1. E-Mail Empfänger]

Hier muss die E-Mail Adresse des Empfängers eingetragen werden. Die E-Mail Adresse kann über den Button " Aus weitere Telefon.." aus bereits hinterlegten Kontakten der Adressen übernommen werden.

|
[Bild: 2]

SMS Empfänger

[Bild: 2. SMS Empfänger]

Ist das SMS Modul vorhanden, kann hier eine mobile Telefonnummer eingegeben werden, die herangezogen wird, wenn SMS als Versandart eingestellt wird.

|
[Bild: 3]

Kundeninfo-Typ Vorlage

[Bild: 3. Kundeninfo-Typ Vorlage]

Wenn Sie bei vielen Adressen diese Daten hinterlegen möchten, können Sie sich Vorlagen erstellen, die für alle vier Situationen die Versandart, den Baustein und die beiden Haken ‚Nachfrage‘ und ‚Anhalten‘ bereits setzen.

|
[Bild: 4]

Aus weitere Telefon...

[Bild: 4. Aus weitere Telefon...]

Über diese Schaltfläche kommen Sie in die Kommunikationsmaske, die auch an anderen Stellen über die Tastenkombination STRG-W erreichbar ist. In dieser Maske können Sie per Doppelklick auf eine E-Mail Adresse oder eine Telefonnummer, diese in die Kundeninfo-Maske übernehmen (anhängen).

Pro Vorgang oder Situation, derzeit haben wir vier definiert, können Sie hinterlegen, ob und wenn ja wie (E-Mail oder SMS) eine Benachrichtigung an den Kunden gesendet werden soll.

|
[Bild: 5]

Versandart

|

[Bild: 5. Versandart]

|

Wählen Sie hier die gewünschte Versandart für die vier möglichen Vorgänge. Die Wahl erfolgt für jeden Vorgang gesondert.

|
[Bild: 6]

Baustein

|

[Bild: 6. Baustein]

|

Wählen Sie hier den Textbaustein für die jeweilige Situation.

Bausteine können Sie über den Button "Baustein", der sich auch auf dieser Maske befindet, anlegen bzw. editieren.

|
[Bild: 7]

Nachfrage

|

[Bild: 7. Nachfrage]

|

Damit kommt eine Abfrage, ob Sie die E-Mail oder die SMS senden möchten. Wenn Sie das bejahen, öffnet sich das entsprechende E-Mail oder SMS-Fenster mit dem ausgefüllten Bausteintext. Dieser Haken ist sinnvoll, wenn der Kunde nur in wichtigen Fällen informiert werden möchte.

|
[Bild: 8]

Anhalten

|

[Bild: 8. Anhalten]

|

Der Versand erfolgt dann nicht automatisch im Hintergrund, sondern es öffnet sich immer die entsprechende E-Mail oder SMS-Maske mit dem ausgefüllten Bausteintext. Dieser Haken ist auf jeden Fall am Anfang sinnvoll. Damit wissen Sie, dass eine E-Mail oder SMS rausgeht und Sie können den Text noch anpassen.

|
[Bild: 9]

Kunden-Info Vorlage

[Bild: 9. Kunden-Info Vorlage]

Hier können Sie Kunden-Info Vorlagen anlegen, die Sie dann bei "Kundeninfo-Typ Vorlage" ziehen können.

Im Unterkapitel Bausteine / Vorlage anlegen wird beschrieben wie eine Kundeninfo Vorlage angelegt wird.

|
[Bild: 10]

Baustein

[Bild: 10. Baustein]

Hier wählen Sie einen vorher definierten „Kundeinfo“-Baustein aus. Siehe Unterkapitel Bausteine / Vorlage anlegen. Zur Vereinfachung können Sie über die Schaltfläche „Baustein“ direkt in Bausteinverwaltung kommen. Der ‚normale‘ und weiterhin funktionierende Weg ist über das Modul „Einstellungen“, Menü <Vorlagen>, <Vor- und Nachbemerkung, Bausteine>.

Ohne den Haken bei ‚Nachfrage‘ bzw. ‚Anhalten‘ wird die E-Mail oder SMS sofort im Hintergrund gesendet.

|
[Bild: 11]

Abbruch

[Bild: 11. Abbruch]

Mit diesem Button verlassen Sie die Kundeninfo Maske ohne eventuelle Änderungen zu speichern.

|
[Bild: 12]

OK

[Bild: 12. OK]

Mit diesem Button verlassen Sie die Kundeninfo-Maske. Alle Eingaben werden gespeichert.
