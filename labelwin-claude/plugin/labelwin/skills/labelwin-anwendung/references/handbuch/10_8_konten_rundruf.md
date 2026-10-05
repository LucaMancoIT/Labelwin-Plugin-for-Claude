# 10.8 Konten-Rundruf

Pfad: Buchhaltung > Fibuerfassung [25] > 10. Kontoauszugsmanager [Modul] > 10.8 Konten-Rundruf
Quelle: handbuch/10_8_konten_rundruf.htm

|

10.8 Konten-Rundruf

Mit aktuellen Bankprogrammen lässt sich ein sogenannter Kontenrundruf durchführen. Damit werden die Daten von allen dort angemeldeten Konten auf einen Rutsch abgeholt. Anschließend kann man zwar für jedes Konto eine separate Datei erzeugen, aber dies ist zusätzlicher Aufwand und man macht leicht Fehler.

Mit einer neuen Funktion in Labelwin können die Auszüge nun ebenfalls für alle Konten auf einmal eingelesen werden.

Erforderliche Einstellungen:

- Die Bankdaten müssen auf den Einzugstyp ‚Steuerdatei‘ gesetzt werden

- In der Steuerdatei muss festgelegt werden, in welchem Feld eine Kontenkennung eingetragen ist, also woran das Konto erkannt werden kann. Diese Kennung ist in der Regel die Kontonummer selbst.

- Bei den Bankdaten muss zu jedem Konto das entsprechende Kennzeichen eingetragen werden.

- Bei Konten, deren Auszüge über einen Rundruf eingelesen werden, muss das Kennzeichen ‚Kontenrundruf‘ gesetzt werden.

- Bei gemeinsam abgeholten Konten wird zwangsläufig die gleiche Steuerdatei zur Zerlegung der Daten eingesetzt - schließlich sind ja alle in der gleichen Datei, haben also zwangsläufig die gleiche Struktur. Um Fehler zu verhindern verlangt Labelwin, dass bei Konten, die gemeinsam abgeholt auch der gleiche Name im Feld ‚Steuerdatei‘ steht. Bei gesetztem Schalter ‚Rundruf‘ kann der Name der Steuerdatei eingegeben werden und muss dann identisch eingesetzt werden.

- Konten, die in der Rundrufdatei enthalten sind, werden unter diesen Bedingungen nicht verarbeitet:

o das Kennzeichen Kontenrundruf ist nicht gesetzt

o die Kontenkennung ist in den Bankdaten nicht oder falsch eingetragen

o in den Bankdaten ist eine andere Steuerdatei eingetragen, als bei der Bank, bei der das Einlesen der Auszüge gestartet wird.
