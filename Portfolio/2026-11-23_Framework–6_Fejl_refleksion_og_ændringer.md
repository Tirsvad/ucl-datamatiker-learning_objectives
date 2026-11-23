# Framework 6: Fejl, refleksion og ændringer

**Dato:** 23/11 2026
**Læringsmål dækket:** [AI i softwareprojekter](https://tirsvad.studiesites.dk/laeringsmal-ai-til-softwarelosninger/) og [Dataanalyse og databehandling](https://tirsvad.studiesites.dk/laeringsmaal-dataanalyse-og-databehandling/)

De første fem poster handler om, hvordan mit framework er bygget: [post 1](2026-11-23_Framework–1_Dokumentation_artefakter_og_krydsreferencer.md), [post 2](2026-11-23_Framework–2_AI_laver_artefakter_med_human-in-the-loop.md), [post 3](2026-11-23_Framework–3_Kvalitetssikring_af_artefakter.md), [post 4](2026-11-23_Framework–4_AI_laver_kode_ud_fra_artefakter.md) og [post 5](2026-11-23_Framework–5_Kvalitetssikring_af_koden.md). Denne post handler om det, der gik galt, hvad jeg lærte, og hvad jeg ændrede. Det er her, min udvikling som softwareudvikler kan ses. Hver af de andre poster har også et afsnit om fejl for sit eget emne.

Jeg har gennemgået ændringsloggene, review-rapporterne, README-filerne og commit-beskederne fra frameworket, de fælles workflows, webshoppen og NF Hotel-projektet. Posten viser de fejl, jeg nåede at skrive ned. Den er derfor ikke komplet.

<!-- UDKAST: Fakta er hentet fra changelogs og records. Refleksionerne er formuleret ud fra dem og skal rettes til mine egne ord. -->

## 🧭 Fem runder, hvor jeg tog fejl

Jeg viser fejlene som fem gennemløb af Kolbs læringscirkel, så man kan se, hvordan en fejl blev til en ændring.

### Runde 1: Det virkede i det små, men ikke i det store

**1. Konkret erfaring**
- Et script læste kun de nyeste 50 milepæle, så en ny kørsel lavede dubletter af ældre opgaver (5/10).
- En fil blev så stor, at et andet script stoppede midt i læsningen, og publiceringen af milepæle fejlede (10/11).
- Et script startede to programmer for hver review-rapport for hver milepæl. Det blev til omkring 4.700 programmer i én kørsel og fik serveren, der kørte det, til at gå ned (20/11).

**2. Refleksion:** Scripts virkede på mine små eksempler. Fejlene kom først, da der var mere data, eller da scriptet kørte på en anden maskine.

**3. Abstrakt begrebsliggørelse:** Størrelse og miljø er en del af koden. Man skal teste med flere data og der, hvor koden skal køre.

**4. Aktiv eksperimenteren:** Jeg skrev tests, der fejler uden rettelsen, fx med en milepælsfil på 300 KB. Scriptet søger nu én gang pr. milepæl i stedet for to gange pr. rapport.

### Runde 2: Delene var ikke enige

**1. Konkret erfaring**
- Alle skabeloner oprettede nye dokumenter som "godkendt". Derfor kunne en ny milepæl starte kodning, før den var gennemgået (5/10).
- Udgivelsen ledte efter en statuskontrol med det forkerte navn og fejlede på en commit, der var grøn (5/11).
- En workflow sendte et hemmeligt navn, som scriptet ikke genkendte (21/11).

**2. Refleksion:** Hver del var rigtig for sig. Fejlen lå i aftalen mellem dem.

**3. Abstrakt begrebsliggørelse:** Det, den ene del sender, og det, den anden forventer, skal testes.

**4. Aktiv eksperimenteren:** En test opretter nu alle dokumenttyper og tjekker, at de starter som "foreslået". Workflowen sender begge navne, indtil alle er skiftet.

### Runde 3: Mine egne værktøjer fulgte ikke mine regler

**1. Konkret erfaring**
- Den første gennemgang af mine scripts mod min egen tjekliste fandt et adgangsbevis (token), som andre brugere på maskinen kunne se, og et script der meldte "ok", selv når noget var fejlet (10/10).
- Min egen workflow-skabelon brød min egen tjekliste for workflows (11/10).

**2. Refleksion:** Jeg havde skrevet reglerne til koden, men ikke målt mine værktøjer på dem.

**3. Abstrakt begrebsliggørelse:** En regel er først noget værd, når den også gælder for mig selv.

**4. Aktiv eksperimenteren:** Mine scripts gennemgås nu mod samme tjekliste som anden kode. Fælles kode er samlet ét sted, og formateringen følger én fælles fil.

### Runde 4: En rettelse nåede ikke frem

**1. Konkret erfaring:** Jeg rettede fejlene fra runde 1 i frameworket. Alligevel fejlede workflowene igen, fordi de stadig brugte en gammel udgave af frameworket (10/11 og 20/11).

**2. Refleksion:** Jeg troede, en fejl var løst, når rettelsen var lavet. Men den, der bruger rettelsen, skal også skifte til den nye udgave.

**3. Abstrakt begrebsliggørelse:** Afhængigheder mellem projekter. En rettelse er først færdig, når hele kæden er flyttet.

**4. Aktiv eksperimenteren:** Ved hver rettelse tjekker jeg nu, hvilke andre dele der bruger den, og flytter dem også.

### Runde 5: Design kom efter koden i NF Hotel-projektet

**1. Konkret erfaring:** Planen sagde, at designet skulle være lavet før koden. Alligevel byggede jeg først kernen, analyserne og notebooken og skrev designet bagefter. Gennemgangen af designet fandt ni fejl og syv åbne spørgsmål, fx at koden havde flere lag end beslutningerne beskrev. Også da jeg senere designede først, var der forskelle mellem design og kode.

**2. Refleksion:** En regel i en tekst er ikke nok. Jeg bryder den, når jeg har travlt.

**3. Abstrakt begrebsliggørelse:** Design og kode skal holdes sammen. Derfor kræver frameworket nu, at designet er godkendt, før koden skrives, og et script nægter at oprette det næste dokument, før det foregående er godkendt.

**4. Aktiv eksperimenteren:** Næste use case i NF Hotel-projektet bygger jeg med designet først og tæller forskellene mellem design og kode.

## 🔁 Beslutninger, jeg ændrede

| Før | Efter | Hvorfor |
|---|---|---|
| 19 skills, én pr. dokumenttype | Én skill med en kort reference pr. type | De fyldte for meget i AI'ens hukommelse |
| En dansk og en engelsk udgave af hvert dokument | Én fil på produktejerens sprog | De gled fra hinanden |
| Test af GUI i fire miljøer | Kun Windows Sandbox og Docker | GUI-tests overtog min egen skærm |
| Use case-mapper direkte i `docs/` | Egen undermappe | De fyldte øverste niveau |
| Domænemodel med tekniske ord | Kun begreber fra produktejerens verden | Løsninger snigede sig ind i en model, der skulle være let at læse |
| Alle gamle review-rapporter gemt | Erstattede rapporter slettes | For mange at læse |
| Seks workflows | To: CI og CD | De hang sammen uden en fælles begivenhed |

## 🏨 Erfaringer for NF Hotel

NF Hotel-projektet bruger stadig den tidligste udgave af frameworket (`v0.1.0`). Det er derfor et godt før-billede: dokumenterne har den gamle status "Approved", en gammel sprogrække og en versionshistorik med fire kolonner. Næste gang vil jeg:

- designe og få designet godkendt, før jeg skriver koden
- føre prompt-log fra første dag. I dag findes kun planlægningsprompten
- få en person til at gennemgå AI-output, før det bruges. Reviewet af designet i projektet er lavet af en AI og endnu ikke bekræftet af en person
- flytte projektet til den nuværende udgave af frameworket og se, hvor meget af flytningen et script klarer
- teste med flere data end de 8.538 bookinger i eksemplet og holde følsomme oplysninger, fx pasoplysninger, ude af kommandolinjer og logfiler, hvis OCR-sporet bygges

## 📚 Kilder til viden

- ændringsloggene i frameworket og i de fælles workflows
- review-rapporter og milepæle i NF Hotel-projektet, webshoppen og `SQA-and-QC`
- webshoppens README (afsnittet Reflection) og [Omstillingsparathed](2026-10-09_Omstillingsparathed–ny_opgave_fra_anden_PO.md), hvor jeg også lærte, at planlægning gjorde en større forskel end prompting

## ➡️ Næste skridt

- Føre en logbog over fejl, mens de sker, så oversigten ikke kun bygger på ændringsloggen.
- Teste scripts med mange data, før jeg stoler på dem.
- Skrive en beslutning og dens begrundelse ned, før jeg ændrer en struktur.
- Bygge næste use case i NF Hotel-projektet med designet først og undersøge, om de samme fejltyper kommer igen.

## 🔄 Kolbs læringscirkel samlet

**1. Konkret erfaring**

Jeg byggede et framework og brugte det på egne projekter og kursusprojekter. Underveis fejlede scripts, workflows og mine egne beslutninger.

**2. Refleksion**

Fejlene viste sig ofte først, når data voksede, eller koden kørte et andet sted. Og mine egne værktøjer fulgte ikke altid mine egne regler.

**3. Abstrakt begrebsliggørelse**

Jeg kobler erfaringen til teori om blandt andet:

- regressionstest og test i stor skala
- kontrakter mellem komponenter
- afhængigheder mellem projekter og versionering
- arkitekturbeslutninger (ADR) og ændringspåvirkning
- Kolbs læringscirkel anvendt på mit eget arbejde

**4. Aktiv eksperimenteren**

I de næste projekter fører jeg en fejl-logbog, tester med flere data og skriver beslutninger ned, før jeg ændrer noget. Beviset på, at jeg har lært, er, at jeg arbejder anderledes næste gang, og at jeg kan måle forskellen.

## 🎯 Hvilke kernemål i læringsmål dækkes

🟢 dækkes helt, 🟡 dækkes delvist, 🔴 dækkes kun lidt eller slet ikke endnu. Posten handler om at lære af egne fejl, ikke om data.

### Dataanalyse og databehandling

| Kerneområde | Vægt i læringsmål | Dækning | Begrundelse |
|---|---|:---:|---|
| Dataindsamling | Stor | 🔴 | Ikke relevant for denne post |
| Datastrukturering | Stor | 🔴 | Ikke relevant for denne post |
| Datakvalitet | Stor | 🔴 | Fejlene gælder scripts og regler og ikke et datasæt |
| Datarensning | Stor | 🔴 | Ikke relevant for denne post |
| Dataanalyse | Stor | 🔴 | Ikke relevant for denne post |
| Statistik | Stor | 🔴 | Ikke relevant for denne post |
| Deskriptiv statistik | Stor | 🔴 | Tallene er optællinger og ikke en analyse |
| Trends og mønstre | Stor | 🟡 | Mønstre læst ud af listen over fejl; en kvalitativ gennemgang og ikke en beregning |
| Sammenhænge mellem variable | Stor | 🔴 | Ikke relevant for denne post |
| Datavisualisering | Stor | 🔴 | Ikke relevant for denne post |
| Fortolkning af resultater | Mindre | 🟡 | Mønstrene er fortolket, men ikke testet mod flere data |
| Formidling af data | Mindre | 🟡 | Fejl, rettelse og dato er vist i tabeller |

### AI i softwareprojekter

| Kerneområde | Vægt i læringsmål | Dækning | Begrundelse |
|---|---|:---:|---|
| Python for AI | Stor | 🔴 | Ikke relevant for denne post |
| Machine Learning | Stor | 🔴 | Ikke relevant for denne post |
| AI til fortolkning af data | Stor | 🔴 | Ikke relevant for denne post |
| Large Language Models (LLM) | Stor | 🔴 | Ikke relevant for denne post |
| Modelvalg og model comparison | Stor | 🔴 | Ikke relevant for denne post |
| Prompt engineering | Stor | 🔴 | Ikke relevant for denne post |
| Generativ AI | Stor | 🔴 | Ikke relevant for denne post |
| AI-baseret beslutningsstøtte | Stor | 🔴 | Ikke relevant for denne post |
| OCR | Stor | 🔴 | Ikke relevant for denne post |
| Feature extraction | Stor | 🔴 | Ikke relevant for denne post |
| Fortolkning af hoteldata | Mindre | 🔴 | Ikke relevant for denne post |
| Test og evaluering af AI-output | Mindre | 🟡 | Fejl i AI-assisteret kode og dokumenter er fundet og rettet med tests; en optælling af, hvem der lavede hver fejl, mangler |
| Fejlhåndtering og usikkerhed | Mindre | 🟡 | Fejl registreres, rettes med en test og beskrives i en ændringslog |
| Human-in-the-loop | Mindre | 🟡 | Mange fejl blev fundet ved gennemgang; ikke alle gennemgange er uafhængige |
| Privacy og ansvarlig AI | Mindre | 🟡 | Et adgangsbevis synligt for andre og en falsk nøgle i en test blev fundet og rettet |

## 🏨 Hvilken værdi kan det give et hotel management-system?

- **Fejl, der opdages før gæsterne:** Test med flere data og i det rigtige miljø er det, et hotelsystem med mange bookinger har brug for.
- **Rettelser, der når frem:** Hvis hotellet deler kode mellem flere dele, er en rettelse først færdig, når alle delene bruger den.
- **Sporbare beslutninger:** Når en beslutning står skrevet ned med en begrundelse, kan jeg forklare, hvorfor systemet er, som det er.
- **Ærlighed om fejl:** En log med fejl og rettelser er et bedre grundlag for tillid end en, der kun viser det, der virkede.
