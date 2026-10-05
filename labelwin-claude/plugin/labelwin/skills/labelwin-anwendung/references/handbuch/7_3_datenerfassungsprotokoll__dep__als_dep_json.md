# 7.3 Datenerfassungsprotokoll (DEP) als DEP.JSON

Pfad: Buchhaltung > Ladenkasse [23] > 7. Auswertungen > 7.3 Datenerfassungsprotokoll (DEP) als DEP.JSON
Quelle: handbuch/7_3_datenerfassungsprotokoll__dep__als_dep_json.htm

|

7.3 Datenerfassungsprotokoll (DEP) als DEP.JSON

|

Nur für Österreich. Die Schaltfläche „Export DEP.JSON“ ist nur sichtbar, wenn in den Grundeinstellungen, Reiter „Allgemein“, die Option „Datenerfassungsprotokoll anzeigbar“ aktiviert ist.

Das Datenerfassungsprotokoll - kurz DEP - ist in Österreich zu Prüfzwecken zwingend vorgeschrieben. Es muss, zusammen mit der DEP.CSV Datei auf Verlagen des Finanzamtes jederzeit und sofort für einen gewissen Zeitraum ausgegeben und übergeben werden können.

Diese JSON Datei enthält verschlüsselte und kodierte Informationen, die ausschließlich für die österreichischen Steuerprüfer nutzbar sind. Sie enthält neben den öffentlichen Signaturschlüsseln, jede Belegsignatur für den gewünschten Zeitraum. Diese finden Sie auch in der DEP.CSV Datei.

Die JSON Datei werden im Labelwin Unterverzeichnis „DEPProt“ abgelegt. Der Dateiname lautet DEP_{interne Ladenkassennummer}_{Kassen-ID}_{von Datum im Format YYYYMMDD}_{bis Datum im Format YYYYMMDD}.JSON

[Bild]

Über den Menüpunkt <Auswerten> <Auswerten Ladenkasse> erreichen Sie die Schaltfläche „Export DEP.JSON“, der bei Betätigung eine Datei im JSON Format erzeugt.
