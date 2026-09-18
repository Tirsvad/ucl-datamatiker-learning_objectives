# Processen i at vælge – teknologivalg til labbet

**Dato:** 02/9 2026
**Læringsmål dækket:** [AI i softwareprojekter](../Læringsmål–AI_til_softwareløsninger.md) og [Dataanalyse og databehandling](../Læringsmål–Dataanalyse_og_databehandling.md)

Da jeg satte mit lab op (se [Mit lab – fra simpel opsætning til fejlfinding](2026-09-01_Mit_lab–fra_opsætning_til_fejlfinding.md)), var hver komponent et valg, jeg kan begrunde – og som havde alternativer, jeg bevidst fravalgte. Denne post dokumenterer selve valgprocessen: hvilke kriterier jeg vægtede, og hvilke alternativer jeg overvejede og fravalgte for hver komponent.

Mit udgangspunkt for at finde løsninger var, at de ikke måtte være ressourcekrævende, og at de gerne skulle være open source og self-hosted, så jeg holder mig til privacy by design. Jeg fandt kandidatløsninger via Google AI og tjekkede efterfølgende nogle af de kilder, som Google AI's svar byggede på, for at bekræfte ægtheden af informationen, før jeg lagde den til grund for et valg.

## 🧭 Processen i at vælge

| Komponent | Valgt fordi | Alternativ(er) overvejet |
|---|---|---|
| PostgreSQL som database | Understøtter avanceret data-integritet, JSONB til semistrukturerede data og har ekstremt høj ydeevne ved komplekse forespørgsler (queries) | MySQL/MariaDB – lettere at gå til, men mangler PostgreSQL's avancerede indeksering og stærke håndtering af komplekse datatyper. SQLite – god til helt små setups, men mangler concurrency (samtidige brugere) og skalering |
| Gitea som Git-server | Letvægtsløsning og privat by design | GitLab – enterprise-orienteret og mere ressourcekrævende |
| Nginx som reverse proxy | Ekstremt hurtig til statisk indhold, lavt hukommelsesaftryk, og simpel konfiguration af SSL (fx via Certbot), load balancing og URL-rewriting | Apache – traditionel og modulær, men bruger markant flere ressourcer (proces-per-forbindelse) under høj belastning |
| Mailserver til håndtering af e-mail | Samlet løsning i én container (fx docker-mailserver). Giver fuld kontrol over data, ingen eksterne licensomkostninger og nem opsætning af SMTP/IMAP i et lukket miljø | Eksterne API'er (SendGrid/Mailgun) – nemme at integrere, men medfører faste udgifter, vendor lock-in og potentielle GDPR-udfordringer med tredjepartsdata |
| Docker som grundlag for containerisering | Sikrer ensartede miljøer på tværs af udvikling og produktion ("virker på min maskine"-problemet løses). Gør udrulning, skalering og isolation af services lynhurtig | Bare-metal/direkte installation – minimalt overhead, men store problemer med afhængigheder, versionskonflikter og svær migrering |

## 🔄 Kolbs læringscirkel i praksis

**1. Konkret erfaring**

Inden jeg satte labbet op, stod jeg over for fem konkrete valg: database, Git-server, reverse proxy, mailløsning og containerisering. For hvert valg fandtes der mindst ét realistisk alternativ, og jeg måtte tage stilling til, hvilket der passede bedst til et lille, selvstændigt lab-miljø. Jeg brugte Google AI til at finde kandidatløsninger og fravalgte ikke bare at stole på svaret – jeg tjekkede nogle af de underliggende kilder for at bekræfte, at informationen var korrekt.

**2. Refleksion**

- Hvilke kriterier vægtede jeg højst?
  > At løsningen ikke var ressourcekrævende, at den var open source og self-hosted (privacy by design), samt kontrol over egne data og hvor godt løsningen skalerer til fremtidige behov (fx JSONB til semistrukturerede hoteldata i PostgreSQL).
- Hvordan sikrede jeg mig, at informationen fra Google AI var pålidelig?
  > Ved at tjekke nogle af de referencer, Google AI's svar var bygget på, i stedet for at stole blindt på et AI-genereret svar.
- Hvorfor fravalgte jeg de "nemmere" alternativer (MySQL/SQLite, eksterne mail-API'er)?
  > Fordi de enten manglede funktionalitet, jeg forventer at få brug for (concurrency, avanceret indeksering), eller fordi de flyttede kontrollen over data ud af mit eget miljø (vendor lock-in, GDPR-risiko ved tredjepartsdata) og dermed væk fra mit udgangspunkt om privacy by design.
- Hvad var trade-off'et ved mine valg?
  > Valget af Nginx og Gitea frem for tungere enterprise-løsninger som Apache og GitLab er baseret på en bevidst arkitektonisk afvejning (trade-off). I et mindre lab-miljø har prioriteringen ligget på ressourceoptimering, lav driftskompleksitet (Low Operational Overhead) og høj ydeevne.
- Hvad ville få mig til at vælge anderledes?
  > Hvis labbet skulle skalere til mange samtidige brugere eller et team, ville GitLab og Apache blive mere attraktive – kriterierne ændrer sig med kravene.

**3. Abstrakt begrebsliggørelse**

Jeg kobler mine erfaringer til teori om blandt andet:

- databasearkitektur og ACID/indeksering
- reverse proxy-arkitektur og ressourceforbrug
- containerisering versus bare-metal
- vendor lock-in og GDPR ved tredjepartsdata
- kriteriebaseret teknologivalg og trade-off-analyse

Det er præcis den samme metode – kriterier, alternativer, begrundet valg – som mit AI-læringsmål kræver, når jeg senere skal sammenligne mindst 3 LLM'er/AI-modeller og begrunde mit valg. Her har jeg øvet metoden på infrastruktur, før jeg skal bruge den på AI-modeller.

**4. Aktiv eksperimenteren**

Næste gang jeg skal vælge en teknologi – uanset om det er en AI-model, et bibliotek eller en service – vil jeg bruge samme fremgangsmåde: opstille kriterier først, identificere realistiske alternativer, og eksplicit dokumentere, hvorfor de blev fravalgt.

## 🎯 Hvilke kernemål i læringsmål dækkes

🟢 dækkes helt, 🟡 dækkes delvist, 🔴 dækkes kun lidt eller slet ikke endnu.

### Dataanalyse og databehandling

| Kerneområde | Vægt i læringsmål | Dækning | Begrundelse |
|---|---|:---:|---|
| Dataindsamling | Stor | 🔴 | Ikke relevant for denne post |
| Datastrukturering | Stor | 🟡 | PostgreSQL blev valgt bl.a. pga. JSONB til semistrukturerede data – en direkte overvejelse om datastrukturering |
| Datakvalitet | Stor | 🔴 | Ikke relevant for denne post |
| Datarensning | Stor | 🔴 | Ikke relevant for denne post |
| Dataanalyse | Stor | 🔴 | Ikke relevant for denne post |
| Statistik | Stor | 🔴 | Ikke relevant for denne post |
| Deskriptiv statistik | Stor | 🔴 | Ikke relevant for denne post |
| Trends og mønstre | Stor | 🔴 | Ikke relevant for denne post |
| Sammenhænge mellem variable | Stor | 🔴 | Ikke relevant for denne post |
| Datavisualisering | Stor | 🔴 | Ikke relevant for denne post |
| Fortolkning af resultater | Mindre | 🔴 | Ikke relevant for denne post |
| Formidling af data | Mindre | 🔴 | Denne post formidler en valgproces, ikke data |

### AI i softwareprojekter

| Kerneområde | Vægt i læringsmål | Dækning | Begrundelse |
|---|---|:---:|---|
| Python for AI | Stor | 🔴 | Ikke relevant for denne post |
| Machine Learning | Stor | 🔴 | Ikke relevant for denne post |
| AI til fortolkning af data | Stor | 🔴 | Ikke relevant for denne post |
| Large Language Models (LLM) | Stor | 🔴 | Ikke relevant for denne post |
| Modelvalg og model comparison | Stor | 🟡 | Samme kriterie- og alternativ-baserede metode er øvet her på infrastruktur, klar til at genbruges på LLM-valg |
| Prompt engineering | Stor | 🔴 | Ikke relevant for denne post |
| Generativ AI | Stor | 🔴 | Ikke relevant for denne post |
| AI-baseret beslutningsstøtte | Stor | 🔴 | Ikke relevant for denne post |
| OCR | Stor | 🔴 | Ikke relevant for denne post |
| Feature extraction | Stor | 🔴 | Ikke relevant for denne post |
| Fortolkning af hoteldata | Mindre | 🔴 | Ikke relevant for denne post |
| Test og evaluering af AI-output | Mindre | 🟡 | Jeg brugte Google AI til research, men tjekkede efterfølgende nogle af dens kildehenvisninger for at bekræfte ægtheden – en tidlig øvelse i kritisk evaluering af AI-output |
| Fejlhåndtering og usikkerhed | Mindre | 🔴 | Dækket i den forrige post, ikke denne |
| Human-in-the-loop | Mindre | 🟡 | Jeg lod ikke Google AI's svar stå uimodsagt, men verificerede det selv, før jeg brugte det til et valg |
| Privacy og ansvarlig AI | Mindre | 🟡 | "Privacy by design" (open source, self-hosted) var et eksplicit kriterie fra start, og GDPR-risikoen ved eksterne mail-API'er blev vurderet ud fra det |

## 🏨 Hvilken værdi kan det give et hotel management-system?

Bevidste teknologivalg er ikke kun en teknisk detalje – de sætter rammerne for, hvad et hotel management-system kan holde til senere.

- **Data-integritet og performance:** 
  > PostgreSQL's håndtering af semistrukturerede data og komplekse forespørgsler betyder, at systemet kan holde til mere avancerede analyser af booking- og belægningsdata, efterhånden som de vokser.
- **Kontrol over følsomme data:** 
  > At vælge en selvhostet mailserver og database frem for eksterne API'er giver fuld kontrol over gæstedata og bookingoplysninger – relevant for GDPR, og direkte relevant for OCR-projektet, hvor pasoplysninger (pasnummer, navn, nationalitet) er særligt følsomme data, der bør blive i eget miljø.
- **Skalerbarhed:**
  > Docker og en let reverse proxy som Nginx gør det muligt at skalere systemet op i højsæson uden at skifte hele arkitekturen ud.
- **Undgå vendor lock-in:**
  > Ved at fravælge tredjepartsservices til kernefunktioner (mail, database) undgår systemet at blive afhængigt af en enkelt leverandørs priser og vilkår.

Samlet set betyder det, at de valg, jeg har truffet i labbet, ikke kun handler om at få tingene til at virke – de er også en del af at bygge et fundament, der kan bære et rigtigt hotel management-system.
