# einrgzahlplan

PK: lfdnr

| Spalte | Typ | Null | Beschreibung |
|---|---|---|---|
| lfdnr | int | NO |  |
| eingangsrglfdnr | int | YES |  |
| brutto | money | YES |  |
| zahlziel1 | datetime | YES |  |
| zahlziel2 | datetime | YES |  |
| zahlziel3 | datetime | YES |  |
| skonto1 | float | YES |  |
| skonto2 | float | YES |  |
| zahlbetrag1 | money | YES |  |
| zahlbetrag2 | money | YES |  |
| zahlbetrag3 | money | YES |  |
| bezahltdatum | datetime | YES |  |
| zahlsumme | money | YES |  |
| fehlsumme | money | YES |  |
| statusname | nvarchar(15) | YES |  |
| status | int | YES |  |
| bemerkung | nvarchar(30) | YES |  |
| vorgzahlsumme | money | YES |  |
| zahlungslauf | int | YES |  |
| zukstatus | int | YES |  |
| waekzerfass | int | YES |  |
| waekzzahlist | int | YES |  |
| zahlbetragakt | float | YES |  |
| schecknr | int | YES |  |
| laststatus | int | YES |  |
| lastvorgzahlsumme | money | YES |  |
| banklfdnr | int | YES |  |
| ausbuchungskonto | nvarchar(10) | YES |  |
| ausbuchungssumme | float | YES |  |
| zahlsummeskonto | float | YES |  |
| zahlsummeausbuch | datetime | YES |  |
| mandant | int | YES |  |
| wahl | nvarchar(1) | YES |  |
| zahlsummeausbuchneu | float | YES |  |
| zahlzielkw1 | nvarchar(7) | YES |  |
| zahlzielkw2 | nvarchar(7) | YES |  |
| zahlzielkw3 | nvarchar(7) | YES |  |
| zeitstempel | timestamp | NO |  |
| freigabeperson | int | YES |  |
| freigabedatum | datetime | YES |  |
