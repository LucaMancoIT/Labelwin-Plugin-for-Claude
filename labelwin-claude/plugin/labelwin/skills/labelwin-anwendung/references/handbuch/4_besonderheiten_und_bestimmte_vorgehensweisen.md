# 4.Besonderheiten und bestimmte Vorgehensweisen

Pfad: Schnittstellen > Mareon Schnittstelle [Modul] > 4.Besonderheiten und bestimmte Vorgehensweisen
Quelle: handbuch/4_besonderheiten_und_bestimmte_vorgehensweisen.htm

|

4.Besonderheiten und bestimmte Vorgehensweisen

Manuell angelegte Aufträge

Oft werden die Aufträge vorher schon telefonisch entgegengenommen und manuell angelegt. Beim Abholen der Aufträge aus dem Mareon Portal werden dann erneut ein Aufträge für diese Vorgänge angelegt.

Da die manuell angelegten Aufträge oft schon bearbeitet wurden (terminiert, Zeiten gebucht, Rechnung geschrieben) müssen Sie in diesem Fall die Mareondaten des abgeholten Auftrags in den bereits angelegten Auftrag kopieren und den automatisch abgeholten Auftrag stornieren.

Durch das Kopieren des Mareoneintrags ist sicher gestellt, dass die geschriebene und gedruckte Rechnung aus dem manuellen Auftrag in das Portal hochgeladen wird.

Um diese Daten zu kopieren, markieren Sie den manuell angelegten Auftrag und wählen dann den Menüpunkt <Bearbeiten> <Mareondaten aus anderem Auftrag> und wählen dann den zugehörigen Auftrag aus dem Portal, um von diesem die Daten zu kopieren.

Auftragstext und Materialzettel werden nicht kopiert, da diese in dem manuell angelegten Auftrag eventuell schon verändert wurden.

Eine weitere Möglichkeit ist die Zuordnung des manuellen Auftrages als Folgeauftrag zu dem heruntergeladenen Mareonauftrag. Nach Markieren des Mareonauftragss wählen Sie den Menüpunkt <Bearbeiten> <Wandeln Folgeauftrag/Hauptauftrag> und wählen dann den manuell angelegten Auftrag aus. Der Mareon Portalauftrag wird dann zum Folgeauftrag des manuell angelegten Auftrags. Dabei werden die notwendigen Mareondaten mit an den Hauptauftrag übertragen.

Bei der dann aus dem Hauptauftrag geschriebenen Rechnung müssen Sie den Textartikel des Folgeauftrags in die Vorbemerkung der Rechnung kopieren. Über die Schnittstelle kommen keine Textartikel, sondern nur Vorbemerkungen in das Mareon Portal zurück.

Einschränkungen

Auf Grund der Schnittstellendefinition von Mareon gibt es einige Einschränkungen:

· Max. 350 Zeichen der Vorbemerkung der Rechnung werden übertragen

· Textartikel im Dokument werden nicht übertragen

· Prozentpositionen und Geheimpositionen werden nicht übertragen

· Positionen mit negativer Menge / negativem Preis werden nicht übertragen

· Bei einem SET werden nur die Setbestandteile übertragen

· Leistungspositionen mit Menge 0 werden nicht übertragen

· Bei Artikeln aus einem EPA-Katalog werden nur die Artikelnummern und Mengen übertragen, da der Preis im Portal feststeht.

· Es gibt keine kumulierenden Abschlags-/Schlussrechnungen wie im Label. Abschlagsrechnung bedeutet lediglich, dass der Status des Auftrags im Portal nicht auf erledigt gesetzt wird, sondern es noch eine weitere Rechnung gibt

· Im Login und Passwort darf kein & enthalten sein

· max 99 Positionen pro Rechnung

Auftragstypen

Bei der Übernahme des Auftrages aus dem Mareon Portal wird das erste Zusatzfeld im Kundendienst mit der Auftragsnummer gefüllt.

z.B. 13009-MAREON+403

dabei bedeutet die Zahl hinter dem + ob und welcher EPA Katalog verwendet wird.

Keine Zahl hinter dem +:

der Auftrag ist vom Auftragstyp H, es können beliebige Artikel verwendet werden

HE hinter +:

der Auftrag ist vom Auftragstyp HE, es wird aber kein spez. EPA Katalog verwendet

andere Zahlen/Buchstaben:

es wird ein entsprechender EPA Katalog verwendet und nur Artikel aus diesem EPA Katalog können verwendet werden

Ein EPA Katalog ist ein vorgegebener Katalog vom Wohnungsbauunternehmen der eine bestimmte Gültigkeit hat.

Über die Mareon Schnittstelle kann dieser Katalog abgeholt werden, so dass er für die Erstellung der Rechnung zur Verfügung steht. Das Wohnungsbauunternehmen kann definieren, ob sie nur Artikel dieses Katalogs oder jedes beliebig anderen Katalogs anerkennen. Außerdem können Sie je nach Definition freie Artikel verwenden. In dem Fall gibt es eine spezielle Artikelnummer in diesem EPA Katalog.

Beim Hochladen der Rechnung bekommt Label von Mareon eine Information über den Gesamtpreis. Diese Information wird in der Nachbemerkung der Rechnung ausgegeben. Den abgerechneten Auftrag können Sie direkt aus Labelwin (Mareon Plus) oder im Mareon Portal weiterleiten, damit das Wohnungsunternehmen die Rechnung bekommt. Solange Sie diese Rechnung nicht weitergeleitet haben, können Sie jederzeit im Labelwin das Dokument erneut drucken und damit die Änderungen automatisch hochladen.

Auftragszettel

Wenn Sie mit dem Zusatzmodul ELO-Anbindung arbeiten, können Sie den vom Monteur ausgefüllten Auftragszettel einscannen. Damit ist er dem Label-Auftrag hinterlegt. Eine automatische Übergabe des eingescannten Auftragszettels an Mareon erfolgt bei der Übertragung der Rechnung zum Portal (Mareon plus).

Wird nicht mit der ELO-Anbindung gearbeitet, können Sie den Auftrag manuell als PDF-Datei in das Portal hochladen oder faxen. Dazu muss auf den Auftrag die interne Mareonnummer als Strichcode gedruckt werden. Die hierfür erforderliche Formularanpassung ist kostenpflichtig.
