# Mit lab – fra simpel opsætning til fejlfinding

**Dato:** 01/9 2026
**Læringsmål dækket:** [AI i softwareprojekter](../Læringsmål–AI_til_softwareløsninger.md) og [Dataanalyse og databehandling](../Læringsmål–Dataanalyse_og_databehandling.md)

Som en del af mine to valgfag AI i softwareprojekter og Dataanalyse og databehandling har jeg arbejdet med at opbygge mit eget lab-miljø.

Formålet har ikke kun været at få nogle Docker-containere til at køre. Labbet er blevet en praktisk platform, hvor jeg kan eksperimentere, fejlsøge og koble teori til konkrete problemstillinger fra mit hotelprojekt.

Mit lab består blandt andet af:

- PostgreSQL som database
- Gitea som Git-server
- Nginx som reverse proxy
- Mailserver til håndtering af e-mail
- Docker som grundlag for containerisering

På papiret ser opsætningen forholdsvis simpel ud. I praksis viste det sig hurtigt, at det er noget helt andet at få flere services til at fungere sammen.

*Selve begrundelsen for valget af hver komponent (og de fravalgte alternativer) er dokumenteret i sin egen post: [Processen i at vælge – teknologivalg til labbet](2026-09-17_Processen_i_at_vælge–teknologivalg_til_labbet.md).*

## 🧩 Udfordringer, løsninger og reflektion

### 🔧 Da mailserveren ikke virkede

Jeg undersøgte systemet trin for trin. Jeg brugte blandt andet:

```
ss -tlpn
```

Kommandoen viste, hvilke TCP-porte der lyttede på serveren. Her opdagede jeg, at port 993, som bruges til IMAPS, ikke var åben.

Derefter undersøgte jeg konfigurationen inde i Docker-containeren:

```
docker exec mailserver doveconf -n | grep -A2 -E "^service imap-login|^ssl "
```

Det gav et vigtigt spor: problemet var relateret til SSL-certifikatet, hvilket betød, at IMAPS ikke blev startet korrekt.

### 💡 Løsningen

Jeg endte med at generere et certifikat til mailserveren ved hjælp af Certbot.

Efter certifikatet var på plads, kunne mailserveren starte IMAPS korrekt, og port 993 blev igen synlig på serveren.

Det interessante var derfor ikke kun selve løsningen. Det var processen:

**Problem → undersøgelse → hypotese → test → ny viden → løsning**

Det er netop denne proces, jeg gerne vil kunne dokumentere i min læring.

### 🔐 En anden vigtig læring – passwords og data

Jeg stødte også på problemer med passwords i mine Bash-scripts.

Passwords med specialtegn gav uventede resultater, når de blev sendt som parametre til funktioner. Det fik mig til at undersøge, hvordan Bash håndterer værdier, og hvordan jeg kunne ændre min tilgang.

Det gav mig en vigtig erfaring:

**Data skal ikke bare kunne flyttes fra A til B – det skal ske på en måde, der er robust og sikker.**

Det er særligt relevant i et hotel management-system, hvor systemet potentielt håndterer bookingdata og andre oplysninger, som kræver korrekt behandling og kontrol.

## 🔄 Kolbs læringscirkel i praksis

Arbejdet med labbet kan kobles direkte til Kolbs læringscirkel, som jeg bruger i begge mine læringsmål.

**1. Konkret erfaring**

En af de største udfordringer i labbet var mailserveren. Jeg fulgte først vejledningen fra mailserverens egen dokumentation, men løsningen fungerede ikke i mit miljø, og jeg fandt heller ikke en løsning ved at søge efter andre løsninger online. Det betød, at jeg selv måtte undersøge systemet trin for trin for at finde ud af, hvorfor IMAPS-tjenesten (port 993) ikke startede – se de tekniske detaljer under "Da mailserveren ikke virkede" ovenfor.

**2. Refleksion**

Jeg undersøger, med udgangspunkt i mailserver-problemet:

- Hvad virkede ikke?
  > IMAPS-tjenesten startede ikke – port 993 var lukket, selvom jeg fulgte mailserverens officielle opsætningsvejledning.
- Hvor opstod fejlen?
  > Inde i selve containeren, i SSL/TLS-konfigurationen: uden et gyldigt certifikat kunne imap-login-servicen ikke starte.
- Hvilke antagelser havde jeg?
  > Jeg antog, at en installation efter dokumentationen ville virke uden videre, og ledte derfor først efter en netværks-/portfejl frem for at mistænke certifikatet.
- Hvilke værktøjer kunne hjælpe mig?
  > `ss -tlpn` til at se hvilke porte der reelt lyttede, og `docker exec ... doveconf -n` til at læse den faktiske konfiguration inde i containeren i stedet for kun at læse dokumentation udefra.
- Hvad kunne jeg gøre anderledes?
  > Undersøge konfigurationen inde i containeren fra starten i stedet for at bruge tid på at søge efter færdige løsninger, og lade certifikat-generering med Certbot være en fast del af opsætningen fra begyndelsen.

  > Meget af tiden gik med trial-and-error. Jeg kunne have sparet tid ved bare at finde en løsning på nettet, men så havde jeg ikke lært at debugge fejlen selv. Ved i stedet at bruge terminalkommandoerne til at spore årsagen har jeg nu en metode, jeg kan bruge igen – næste gang jeg ser problemet, ved jeg, hvor jeg skal lede.

**3. Abstrakt begrebsliggørelse**

Jeg kobler mine erfaringer til teori om blandt andet:

- Docker og containerisering
- netværk og porte
- SSL/TLS
- systemintegration
- databehandling
- fejlhåndtering
- sikkerhed og privacy

På samme måde skal jeg i dataanalyse koble mine praktiske erfaringer til teori om datakvalitet, statistik, visualisering og sammenhænge. I AI-sporet kobles erfaringerne til blandt andet LLM'er, modelvalg, AI-evaluering og human-in-the-loop.

**4. Aktiv eksperimenteren**

Når jeg har fundet en mulig forklaring, ændrer jeg konfigurationen eller metoden og tester igen. Det giver en løbende proces:

**Eksperiment → refleksion → teori → forbedring → nyt eksperiment**

Det er den samme tilgang, jeg senere vil bruge, når jeg arbejder med hoteldata, AI-modeller og AI-baseret beslutningsstøtte.

## 🎯 Hvilke kernemål i læringsmål dækkes

Arbejdet med labbet opfylder ikke hele mine læringsmål alene. Tabellerne herunder viser, hvor meget hvert kerneområde er dækket lige nu: 🟢 dækkes helt, 🟡 dækkes delvist, 🔴 dækkes kun lidt eller slet ikke endnu.

### Dataanalyse og databehandling

| Kerneområde | Vægt i læringsmål | Dækning | Begrundelse |
|---|---|:---:|---|
| Dataindsamling | Stor | 🟡 | PostgreSQL er sat op, men der indsamles endnu ikke reelle hoteldata |
| Datastrukturering | Stor | 🟡 | Databasen giver et sted at strukturere data, men skemaet til hoteldata er ikke designet endnu |
| Datakvalitet | Stor | 🔴 | Ikke arbejdet med endnu – kræver et faktisk datasæt |
| Datarensning | Stor | 🔴 | Ikke relevant før der er data at rense |
| Dataanalyse | Stor | 🔴 | Ikke påbegyndt |
| Statistik | Stor | 🔴 | Ikke påbegyndt |
| Deskriptiv statistik | Stor | 🔴 | Ikke påbegyndt |
| Trends og mønstre | Stor | 🔴 | Ikke påbegyndt |
| Sammenhænge mellem variable | Stor | 🔴 | Ikke påbegyndt |
| Datavisualisering | Stor | 🔴 | Ikke påbegyndt |
| Fortolkning af resultater | Mindre | 🔴 | Ikke relevant endnu |
| Formidling af data | Mindre | 🔴 | Denne post formidler proces, ikke data |

Labbet bliver derfor ikke selve dataanalysen, men den platform hvor data senere kan opbevares og gøres tilgængelige for analyse.

### AI i softwareprojekter

| Kerneområde | Vægt i læringsmål | Dækning | Begrundelse |
|---|---|:---:|---|
| Python for AI | Stor | 🔴 | Kurset er ikke startet endnu i denne del af forløbet |
| Machine Learning | Stor | 🔴 | Ikke påbegyndt |
| AI til fortolkning af data | Stor | 🔴 | Ikke påbegyndt |
| Large Language Models (LLM) | Stor | 🔴 | Ikke påbegyndt |
| Modelvalg og model comparison | Stor | 🔴 | Ikke påbegyndt |
| Prompt engineering | Stor | 🔴 | Ikke påbegyndt |
| Generativ AI | Stor | 🔴 | Ikke påbegyndt |
| AI-baseret beslutningsstøtte | Stor | 🟡 | Labbet lægger den tekniske forbindelse (data → software → AI), men selve beslutningsstøtten er ikke bygget |
| OCR | Stor | 🔴 | Ikke påbegyndt |
| Feature extraction | Stor | 🔴 | Ikke påbegyndt |
| Fortolkning af hoteldata | Mindre | 🔴 | Ikke påbegyndt |
| Test og evaluering af AI-output | Mindre | 🔴 | Ikke relevant endnu – ingen AI-output at teste |
| Fejlhåndtering og usikkerhed | Mindre | 🟢 | Fejlsøgningen af mailserveren (port, SSL-certifikat) er direkte, dokumenteret træning i systematisk fejlhåndtering |
| Human-in-the-loop | Mindre | 🔴 | Ikke relevant endnu |
| Privacy og ansvarlig AI | Mindre | 🟡 | SSL-certifikater og robust password-håndtering i Bash er et skridt mod ansvarlig datahåndtering, men dækker endnu ikke AI-specifikke privacy-spørgsmål |

Labbet dækker altså ikke de store, tunge AI-kerneområder som LLM'er eller modelvalg endnu – de kommer i senere poster, når Python-for-AI-kurset og LLM-eksperimenterne er i gang. Her lægges i stedet fundamentet: et miljø hvor AI senere kan integreres med hoteldata, og en solid træning i systematisk fejlhåndtering.

Det betyder, at labbet kan blive forbindelsen mellem:

**Hoteldata → database → software → AI → beslutningsstøtte**

## 🏨 Hvilken værdi kan det give et hotel management-system?

Når jeg ser på labbet i forhold til et hotel management-system som NF Hotel, handler værdien ikke kun om teknologien i sig selv.

En samlet teknisk platform kan eksempelvis understøtte:

- sikker og struktureret håndtering af hoteldata
- integration mellem forskellige services
- automatiseret kommunikation via e-mail (ej efterspurgt af PO men kan være vigtigt for beslutningsstøtte)
- adgang til data til analyse
- integration af AI-funktioner
- bedre grundlag for beslutningsstøtte

På længere sigt kan data fra systemet analyseres for eksempelvis at finde trends i belægning, sæsonvariationer, forskelle mellem hverdage og weekender eller sammenhænge mellem pris og belægning. Det er netop nogle af de analyseområder, der indgår i mit dataanalyse-læringsmål.

AI kan derefter bruges som et ekstra lag til at fortolke data og undersøge mulige forklaringer eller forbedringer.
