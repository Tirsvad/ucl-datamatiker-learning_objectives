# Processen i at vælge – fra Jupyter til Marimo med AI

**Dato:** 27/9 2026
**Læringsmål dækket:** [AI i softwareprojekter](https://tirsvad.studiesites.dk/laeringsmal-ai-til-softwarelosninger/) og [Dataanalyse og databehandling](https://tirsvad.studiesites.dk/laeringsmaal-dataanalyse-og-databehandling/)

I min tidligere post beskrev jeg processen med at vælge et værktøj til at visualisere Python-output. Mit første valg var Jupyter, som jeg kendte fra mit Python-kursus. Jeg undersøgte efterfølgende alternativer og så blandt andet på Marimo. Jeg endte med at fastholde Jupyter, blandt andet fordi REPL var vigtigt for mig, når jeg arbejdede med lokale AI-modeller, og fordi Jupyter har et stort og modent økosystem.

Siden har jeg arbejdet videre med mit eksperiment med [benchmark af lokale AI-modeller/LLM'er](https://tirsvad.studiesites.dk/processen-i-at-vaelge-benchmark-af-lokal-ai/). Det har fået mig til at ændre holdning: jeg er nu kommet frem til, at Marimo er blevet mit foretrukne notebook-værktøj til denne type arbejde. Grunden er ikke, at Jupyter pludselig er blevet et dårligere værktøj. Grunden er, at min måde at udvikle software på har ændret sig.

## 🧭 Fra Jupyter til Marimo – et fornyet valg

### AI ændrer måden, vi programmerer på

Jeg oplever i mit arbejde med AI, at kode kan genereres langt hurtigere med AI, end jeg selv kan skrive den manuelt. Det betyder ikke, at mennesket bliver overflødigt. Tværtimod ændrer vores rolle sig. Jeg forventer, at AI fremover vil overtage en stadig større del af det tunge og manuelle arbejde med kodning. Det betyder, at vores opgave i højere grad bliver at:

- beskrive problemet
- formulere gode prompts
- definere krav og rammer
- skabe skills, som AI kan arbejde efter
- kontrollere den genererede kode
- teste resultatet
- validere output
- rette fejl og afvigelser
- træffe de endelige tekniske beslutninger

### Marimo passer godt til AI-genereret kode

Det er her, mit syn på Marimo har ændret sig. En Marimo Notebook er i praksis Python-kode. Det gør den meget velegnet til at få AI til at hjælpe med at designe og udvikle notebooken. Hvor jeg tidligere så manglende REPL som en ulempe, ser jeg nu også en fordel i, at notebooken i høj grad består af almindelig programmeringskode.

Jeg kan beskrive, hvad jeg ønsker:

> Lav en benchmark-notebook, der kan køre lokale LLM'er, måle performance og systemressourcer, gemme resultaterne og visualisere dem.

AI kan derefter hjælpe med at omsætte denne beskrivelse til Python- og Marimo-kode. Det betyder, at jeg ikke nødvendigvis behøver at skrive notebooken celle for celle selv.

### 1,5 time i stedet for en hel dag

Det mest interessante kom, da jeg brugte AI til at lave min benchmark-notebook. På cirka 1,5 time fik jeg:

- lavet prompten
- beskrevet kravene
- genereret notebook-projektet
- fået en fungerende prototype
- testet løsningen
- fundet enkelte afvigelser i målingen af systemressourcer

Hvis jeg skulle have lavet det hele manuelt, vurderer jeg, at jeg kunne have brugt en hel dag. Det er for mig et konkret eksempel på den produktivitetsforskel, AI kan give i softwareudvikling. Processen var:

**Jeg definerer behovet → jeg skriver prompten → AI genererer løsningen → jeg gennemgår og tester koden → jeg finder afvigelser → jeg forbedrer løsningen.**

### AI lavede ikke det perfekte resultat

Benchmark-prototypen var ikke perfekt. Der var enkelte afvigelser i målingen af systemressourcer. Det er faktisk en vigtig del af læringen: hvis jeg bare havde taget den AI-genererede kode og accepteret resultatet, kunne jeg have fået et benchmark med målinger, som ikke var tilstrækkeligt pålidelige. Derfor er det stadig nødvendigt at kunne læse og forstå den kode, AI genererer. AI gør udviklingen hurtigere, men ansvaret for resultatet forsvinder ikke.

### Fra programmering til AI-styret programmering

Tidligere: **Problem → menneskelig programmering → test → resultat**

Nu: **Problem → prompt → AI-genereret kode → menneskelig kontrol → test → resultat**

Det betyder ikke, at jeg skal kunne mindre programmering. Tværtimod. Jeg skal kunne forstå programmeringen godt nok til at kunne:

- stille de rigtige spørgsmål til AI
- opdage fejl i AI-genereret kode
- vurdere arkitekturen
- kontrollere implementationen
- teste løsningen
- vurdere om resultatet faktisk opfylder kravene

Det ændrer derfor mere hvordan jeg bruger mine programmeringskompetencer, end det ændrer behovet for dem.

### Hvorfor Marimo nu?

Mit oprindelige valg var Jupyter. Jeg undersøgte Marimo som et alternativ, blandt andet fordi det er nemt at git-versionere og distribuere som almindelig kode. På det tidspunkt vurderede jeg dog, at Jupyters REPL og store økosystem gjorde Jupyter mere passende til mit arbejde. Mit benchmark-eksperiment har ændret denne vurdering.

Når AI står for en stor del af selve programmeringsarbejdet, bliver det en fordel, at notebooken er ren Python-kode. Marimo passer derfor godt til den arbejdsform, jeg nu er ved at opbygge:

- Python-baseret
- git-versionerbar
- egnet til visualisering
- egnet til benchmark
- reproducerbar
- velegnet til AI-assisteret udvikling

Jeg har altså ikke fundet et universelt bedre notebook-værktøj. Jeg har fundet et værktøj, der passer bedre til min nuværende måde at arbejde på.

### Human-in-the-loop

Hvis AI overtager mere af det manuelle kodearbejde, bliver menneskets rolle i udviklingsprocessen endnu vigtigere. Mennesket skal ikke nødvendigvis skrive hver linje kode, men mennesket skal kunne:

- definere problemet
- formulere kravene
- prompte AI
- vurdere den genererede kode
- teste resultatet
- identificere fejl
- træffe de tekniske beslutninger

I benchmark-eksperimentet blev det meget konkret: AI kunne hurtigt generere en fungerende prototype, men jeg skulle stadig kontrollere resultatet og opdage afvigelserne.

### Hvad har ændret sig?

Min tidligere konklusion var: *"Jupyter passer bedst til mit behov, fordi REPL og det modne økosystem er vigtigt."*

Min nye konklusion er: *"Marimo passer bedre til min nuværende arbejdsform, fordi notebooken er ren Python-kode og derfor kan udvikles effektivt med AI."*

Jeg har ikke ændret mening, fordi jeg har fundet en ny feature. Jeg har ændret mening, fordi selve udviklingsprocessen har ændret sig.

## 🔄 Kolbs læringscirkel i praksis

Det interessante ved denne proces er, at jeg ikke bare har valgt et værktøj én gang – jeg har gennemgået processen igen.

**1. Konkret erfaring**

Mit første valg var Jupyter. Jeg kendte det fra Python-kurset og valgte at undersøge alternativer, før jeg fastholdt Jupyter.

**2. Refleksion**

- Hvad ændrede sig, efter jeg havde valgt Jupyter?
  > Jeg begyndte efterfølgende at bruge AI mere aktivt til programmering, og det ændrede min vurdering af, hvad der er vigtigt i en notebook.
- Hvorfor blev manglende REPL i Marimo pludselig mindre afgørende?
  > Fordi fordelen ved, at notebooken i høj grad består af almindelig Python-kode, nu vejer tungere end REPL, når AI skal hjælpe med at skrive selve notebooken.
- Hvad viste 1,5-timers-eksperimentet om at stole på AI-genereret kode?
  > At AI ikke lavede et perfekt resultat – der var afvigelser i målingen af systemressourcer – så det var stadig nødvendigt selv at læse, forstå og validere koden.

**3. Abstrakt begrebsliggørelse**

Jeg kunne se, at en notebook, der i høj grad består af almindelig Python-kode, er velegnet til AI-assisteret udvikling. Det gør prompten og min evne til at kontrollere AI-output vigtigere end tidligere.

**4. Aktiv eksperimenteren**

Jeg brugte AI til at udvikle benchmark-notebooken. Resultatet var, at jeg på cirka 1,5 time havde en fungerende prototype med kun enkelte afvigelser, blandt andet omkring måling af systemressourcer. Det gav mig ny praktisk erfaring, og erfaringen førte til et nyt valg: Marimo.

Mit største udbytte af eksperimentet er ikke kun benchmark-resultaterne. Det er også en ny forståelse af, hvordan jeg selv skal arbejde som softwareudvikler i en verden med AI. Jeg skal fortsat kunne programmere, men jeg skal samtidig blive bedre til at formulere krav til AI, skrive gode prompts, udvikle skills, strukturere AI-opgaver, evaluere AI-genereret kode, teste output, identificere fejl og bruge AI som udviklingsværktøj uden at overlade ansvaret til AI.

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
| Datavisualisering | Stor | 🟡 | Marimo vælges bl.a. fordi det er egnet til visualisering af benchmark-resultater, men ingen visualisering er lavet i denne post |
| Fortolkning af resultater | Mindre | 🔴 | Ikke relevant for denne post |
| Formidling af data | Mindre | 🔴 | Ikke relevant for denne post |

### AI i softwareprojekter

| Kerneområde | Vægt i læringsmål | Dækning | Begrundelse |
|---|---|:---:|---|
| Python for AI | Stor | 🟡 | Marimo vælges netop fordi notebooken er ren Python-kode, hvilket understøtter arbejdet med Python for AI |
| Machine Learning | Stor | 🔴 | Ikke relevant for denne post |
| AI til fortolkning af data | Stor | 🔴 | Ikke relevant for denne post |
| Large Language Models (LLM) | Stor | 🔴 | Ikke relevant for denne post |
| Modelvalg og model comparison | Stor | 🟡 | Samme kriterie- og alternativ-baserede metode (krav, alternativer, begrundet valg) genbruges her på et notebook-værktøj i stedet for en AI-model |
| Prompt engineering | Stor | 🟢 | Kernen i posten: en konkret prompt bruges til at få AI til at generere hele benchmark-notebooken |
| Generativ AI | Stor | 🟢 | AI genererer selve notebook-projektet og koden ud fra prompten |
| AI-baseret beslutningsstøtte | Stor | 🔴 | Ikke relevant for denne post |
| OCR | Stor | 🔴 | Ikke relevant for denne post |
| Feature extraction | Stor | 🔴 | Ikke relevant for denne post |
| Fortolkning af hoteldata | Mindre | 🔴 | Ikke relevant for denne post |
| Test og evaluering af AI-output | Mindre | 🟡 | Den AI-genererede kode testes og gennemgås, og afvigelser i ressourcemålingen identificeres, men uden en formel testcase-dokumentation |
| Fejlhåndtering og usikkerhed | Mindre | 🟡 | Afvigelserne i den AI-genererede kodes måling af systemressourcer er et konkret, dokumenteret eksempel på usikkerhed i AI-output |
| Human-in-the-loop | Mindre | 🟢 | Eksplicit gennemgående tema: AI genererer koden, men mennesket kontrollerer, tester og træffer de tekniske beslutninger |
| Privacy og ansvarlig AI | Mindre | 🔴 | Ikke behandlet i denne post |

## 🏨 Hvilken værdi kan det give et hotel management-system?

Skiftet fra Jupyter til Marimo handler ikke kun om notebook-præferencer – det er et eksempel på, hvordan AI-assisteret udvikling kan ændre, hvordan værktøjer til hotelprojektet bør vælges og bygges:

- **Hurtigere udvikling af analyseværktøjer:** Hvis AI kan generere en fungerende prototype på 1,5 time i stedet for en hel dag, kan de samme metoder bruges til hurtigere at bygge og justere analyse- og AI-værktøjer til NF Hotels data.
- **Kode frem for celler:** Fordi en Marimo Notebook er almindelig, git-versionerbar Python-kode, passer den bedre ind i et projekt, hvor analyser og AI-eksperimenter skal kunne deles, gennemgås og genbruges som resten af kodebasen.
- **Menneskelig kontrol forbliver nødvendig:** At AI-genereret kode indeholdt afvigelser i ressourcemålingen er en påmindelse om, at AI-genererede analyser af hoteldata eller AI-forslag til hotellet altid skal kontrolleres, før de bruges som beslutningsgrundlag.

Det viser også noget vigtigt ved en god valgproces: et teknologivalg er ikke nødvendigvis permanent. Når erfaringerne og kravene ændrer sig – her fordi min egen arbejdsform ændrede sig med mere AI-assisteret udvikling – skal man være villig til at revurdere sit valg. Det samme princip vil gælde, når værktøjer og metoder til hotelprojektet skal vælges og justeres undervejs.
