# Processen i at lære – AI-prompts, der rammer kriterierne

**Dato:** 27/9 2026
**Læringsmål dækket:** [AI i softwareprojekter](https://tirsvad.studiesites.dk/laeringsmal-ai-til-softwarelosninger/) og [Dataanalyse og databehandling](https://tirsvad.studiesites.dk/laeringsmaal-dataanalyse-og-databehandling/)

I artiklen [Processen i at vælge – benchmark af lokal AI](https://tirsvad.studiesites.dk/processen-i-at-vaelge-benchmark-af-lokal-ai/) havde jeg en udfordring: at prompte AI, så den lavede et resultat efter mine kriterier. Denne post dokumenterer, hvordan jeg løste den udfordring, og hvad jeg lærte af det.

## 🧭 Processen i at lære at prompte AI

### Udfordringen: at få AI til at ramme mine kriterier

Da jeg selv forsøgte at prompte mit foretrukne AI-værktøj direkte til at bygge benchmark-notebooken, fik jeg ikke et resultat, der ramte de kriterier, jeg havde sat op. Kriterierne handlede ikke kun om benchmark-målinger (TTFT, execution time, tokens/sec, ressourceforbrug m.fl.) – de drejede sig også om, at koden skulle overholde DRY og clean architecture.

### Prompten voksede fra 15 til 1150 linjer

For at ramme alle kriterierne voksede min prompt undervejs fra 15 linjer til omkring 1150 linjers forklaring af hvad, hvorfor og hvordan projektet skulle være – herunder krav til struktur (DRY, clean architecture) og til selve benchmarkens målinger.

### En AI-skill kan gøre fremtidige prompts kortere

En del af det, prompten på 1150 linjer forklarede, er faste krav, der gælder på tværs af projekter – fx DRY og clean architecture. Den slags gentagne krav kan i stedet lægges i en AI-skill (som beskrevet i [Artefakt-færdighed – én samlet færdighed i stedet for 19](https://tirsvad.studiesites.dk/hvorfor-en-samlet-artefakt-faerdighed-til-en-gruppe-af-faerdigheder/)), så prompten fremover kan nøjes med at beskrive selve opgaven, mens skillen dækker de faste krav.

Hvis der opstår uoverensstemmelse mellem det, prompten beder om, og det, en skill foreskriver, bliver jeg spurgt om det valg, der skal træffes, i stedet for at AI'en bare vælger ét af dem stiltiende.

### Hjælp fra en kollega

En kollega vejledte mig i en to-trins tilgang:

1. Brug ChatGPT til at formulere selve prompten.
2. Brug derefter den færdige prompt i mit foretrukne AI-værktøj til programmering, til at generere koden.

![Diagram 1](https://tirsvad.studiesites.dk/wp-content/uploads/sites/82065/2026/09/image-6.png)

### Fra try-and-fail til nul eksperimentering

At række ud til en kollega forkortede min egen eksperimentering (try and fail) til nul. Jeg lavede min prompt, og projektet gik fra scratch til prototype på godt 1,5 time.

### Resultatet: bedre end forventet, med ét punkt at rette

Det visuelle koncept, AI'en kom med, var bedre end jeg havde forestillet mig. Min gennemgang af data for VRAM- og systemRAM-forbrug viste, at det var det eneste, jeg skulle rette op på.

## 🔄 Kolbs læringscirkel i praksis

**1. Konkret erfaring**

Jeg forsøgte selv at prompte AI til at bygge benchmark-notebooken, men fik ikke et resultat, der ramte mine kriterier. Jeg bad derfor en kollega om hjælp.

**2. Refleksion**

- Hvorfor ramte mine egne forsøg ikke mine kriterier?
  > Mine egne prompts producerede ikke et resultat, der stemte med de kriterier, jeg havde defineret i benchmark-processen – både benchmark-målingerne og krav som DRY og clean architecture.
- Hvad ændrede kollegaens råd?
  > At bruge ChatGPT specifikt til at formulere selve prompten, og først derefter bruge den færdige prompt i mit foretrukne AI-værktøj til programmering.
- Hvor stor blev prompten, for at den skulle ramme alle kriterierne?
  > Den voksede fra 15 linjer til omkring 1150 linjers forklaring af hvad, hvorfor og hvordan projektet skulle være.
- Kunne prompten være blevet kortere?
  > Ja – faste krav som DRY og clean architecture kan i stedet lægges i en AI-skill, så fremtidige prompts kan nøjes med at beskrive selve opgaven. Hvis prompt og skill kommer i konflikt, bliver jeg spurgt om det valg, der skal træffes, i stedet for at AI'en vælger stiltiende.
- Hvad gjorde det ved min eksperimenteringstid?
  > Det forkortede try-and-fail til nul – jeg gik fra scratch til prototype på ca. 1,5 time.
- Hvad viste min gennemgang af resultatet?
  > At det visuelle koncept var bedre end forventet, og at det eneste, der skulle rettes, var data for VRAM- og systemRAM-forbrug.

**3. Abstrakt begrebsliggørelse**

Jeg kobler erfaringen til teori om blandt andet:

- prompt engineering som en selvstændig disciplin, adskilt fra selve kodegenereringen
- et to-trins workflow: ét værktøj til at designe prompten, et andet til at udføre den
- sparring/hjælp fra andre som alternativ til ren trial-and-error
- iterativ prompt-udvikling: en prompt kan vokse betydeligt (her fra 15 til ca. 1150 linjer), når flere kriterier skal dækkes eksplicit
- softwarearkitekturprincipper som eksplicitte AI-krav (DRY, clean architecture)
- AI-skills som genanvendelig kontekst, der kan afkorte fremtidige prompts, og hvordan konflikter mellem prompt og skill håndteres ved at spørge frem for at vælge stiltiende
- validering af AI-genereret output mod målbare kriterier (human-in-the-loop)

**4. Aktiv eksperimenteren**

Fremover bruger jeg samme to-trins tilgang – ChatGPT til selve prompten, mit foretrukne værktøj til koden – til andre AI-opgaver. Jeg vil også fortsat granske ressourcemålinger som en fast del af gennemgangen, siden det var den eneste fejlkilde i dette forsøg. Næste skridt er at flytte de faste krav (DRY, clean architecture) ind i en AI-skill, så fremtidige prompts kan blive markant kortere end 1150 linjer.

## 🎯 Hvilke kernemål i læringsmål dækkes

🟢 dækkes helt, 🟡 dækkes delvist, 🔴 dækkes kun lidt eller slet ikke endnu.

### Dataanalyse og databehandling

| Kerneområde | Vægt i læringsmål | Dækning | Begrundelse |
|---|---|:---:|---|
| Dataindsamling | Stor | 🔴 | Ikke relevant for denne post |
| Datastrukturering | Stor | 🔴 | Ikke relevant for denne post |
| Datakvalitet | Stor | 🔴 | Ikke relevant for denne post |
| Datarensning | Stor | 🔴 | Ikke relevant for denne post |
| Dataanalyse | Stor | 🔴 | Ikke relevant for denne post |
| Statistik | Stor | 🔴 | Ikke relevant for denne post |
| Deskriptiv statistik | Stor | 🔴 | Ikke relevant for denne post |
| Trends og mønstre | Stor | 🔴 | Ikke relevant for denne post |
| Sammenhænge mellem variable | Stor | 🔴 | Ikke relevant for denne post |
| Datavisualisering | Stor | 🟡 | Det AI-genererede visuelle koncept er en visualisering af benchmark-data, men er ikke selv designet af mig |
| Fortolkning af resultater | Mindre | 🟡 | Min gennemgang af VRAM-/systemRAM-data er en fortolkning af, om resultatet er pålideligt |
| Formidling af data | Mindre | 🔴 | Ikke relevant for denne post |

### AI i softwareprojekter

| Kerneområde | Vægt i læringsmål | Dækning | Begrundelse |
|---|---|:---:|---|
| Python for AI | Stor | 🔴 | Ikke relevant for denne post |
| Machine Learning | Stor | 🔴 | Ikke relevant for denne post |
| AI til fortolkning af data | Stor | 🔴 | Ikke relevant for denne post |
| Large Language Models (LLM) | Stor | 🟡 | ChatGPT og mit foretrukne AI-værktøj bruges begge som LLM'er i to forskellige roller (prompt-design og kodegenerering) |
| Modelvalg og model comparison | Stor | 🔴 | Ikke relevant for denne post – dette handler om prompt-processen, ikke om at vælge mellem modeller |
| Prompt engineering | Stor | 🟢 | Kernen i posten: at lære at formulere en prompt, der rammer konkrete kriterier |
| Generativ AI | Stor | 🟢 | AI genererer både selve prompten (via ChatGPT) og projektet/koden (via mit foretrukne værktøj) |
| AI-baseret beslutningsstøtte | Stor | 🔴 | Ikke relevant for denne post |
| OCR | Stor | 🔴 | Ikke relevant for denne post |
| Feature extraction | Stor | 🔴 | Ikke relevant for denne post |
| Fortolkning af hoteldata | Mindre | 🔴 | Ikke relevant for denne post |
| Test og evaluering af AI-output | Mindre | 🟡 | Gennemgangen af VRAM-/systemRAM-data er en konkret evaluering af AI-outputtets pålidelighed |
| Fejlhåndtering og usikkerhed | Mindre | 🟡 | Et konkret fund (fejl i VRAM-/systemRAM-måling) blev identificeret og skal rettes |
| Human-in-the-loop | Mindre | 🟡 | Jeg gennemgår og vurderer det AI-genererede resultat, i stedet for at acceptere det ukritisk |
| Privacy og ansvarlig AI | Mindre | 🔴 | Ikke behandlet i denne post |

## 🏨 Hvilken værdi kan det give et hotel management-system?

At kunne prompte AI effektivt, så resultatet rammer konkrete kriterier, er direkte genanvendeligt, når hotellets egne AI-funktioner skal bygges:

- **Hurtigere fra idé til prototype:** Samme to-trins tilgang (prompt designet i ét værktøj, udført i et andet) kan bruges til hurtigt at bygge prototyper på AI-funktioner til NF Hotel, ligesom det tog benchmark-notebooken fra scratch til prototype på ca. 1,5 time.
- **Sparring frem for spildtid:** At hente hjælp fra en kollega i stedet for at blive i en trial-and-error-løkke er en genanvendelig arbejdsmetode, når nye AI-opgaver i hotelprojektet støder på lignende udfordringer.
- **Kritisk gennemgang forbliver nødvendig:** Selvom resultatet var bedre end forventet, var der stadig ét konkret punkt (VRAM-/systemRAM-data), der skulle rettes – en påmindelse om, at AI-genererede løsninger til hotellet altid skal gennemgås, før de bruges som beslutningsgrundlag.
