# Framework 5: Kvalitetssikring af koden

**Dato:** 23/11 2026
**Læringsmål dækket:** [AI i softwareprojekter](https://tirsvad.studiesites.dk/laeringsmal-ai-til-softwarelosninger/) og [Dataanalyse og databehandling](https://tirsvad.studiesites.dk/laeringsmaal-dataanalyse-og-databehandling/)

Dette er post 5 i serien om mit framework. [Post 4](2026-11-23_Framework–4_AI_laver_kode_ud_fra_artefakter.md) viser, hvordan AI'en skriver kode ud fra godkendte dokumenter. Her viser jeg, hvordan koden kontrolleres, før den lægges sammen med resten. Kode fra en AI er output, der skal kontrolleres, ligesom andet AI-output. Beviset er kode-tjeklisterne i [`sqa-qc-checklists`](https://git.tirsystem.com/TirSystem/sqa-qc-checklists), de delte workflows i [`git-workflows`](https://git.tirsystem.com/TirSystem/git-workflows) og webshoppen fra Udemy-kurset, som er bygget med dem.

## 🧭 Tre lag af kontrol

Jo tidligere en fejl findes, jo billigere er den.

| Lag | Hvad | Hvem eller hvad |
|---|---|---|
| **1. Lokalt, mens der kodes** | Formatering, tjek af kodestil, typer og tests | AI'en og jeg, før en commit |
| **2. Review mod en tjekliste** | Kriterier for sproget, fx `QC-PY-001` til Python, og en review-rapport før koden lægges sammen | Reviewer (i praksis AI som stand-in og mig) |
| **3. Automatisk på serveren (CI og CD)** | Scanning efter hemmeligheder og sikkerhedsfejl, kvalitetstjek, tests og tjek af ændringsloggen | Delte workflows i `git-workflows` |

**Tjeklisterne til kode.** Der er 10: Python, C, C++, C#, Rust, Flutter, React, shell, YAML-filer og workflows. Python-tjeklisten har 18 kriterier, fx at koden følger formatteren og stilreglerne, at hver funktion har typer, at fejl ikke bliver slugt, at ingen hemmeligheder står i loggen, at hver klasse kan spores til designet, at tests findes for ny adfærd, og at koden ligger i de aftalte lag.

**Tests.** Frameworket har 14 slags test, fx positive, negative, grænseværdier og fejlhåndtering. En fejl, der rettes, får en test, som fejler uden rettelsen. En GUI-test kører aldrig på min egen skærm, men i Docker eller Windows Sandbox.

**Fælles regler.** Hvert kodeprojekt har en `.editorconfig` med faste indstillinger for tegnsæt, linjeskift og mellemrum, og et script fejler, hvis den mangler.

**Workflows på serveren.** De ligger i ét repository og bruges af alle repositories i organisationen:

- **CI** scanner først efter hemmeligheder (et fund stopper resten og nævner fil og linje, aldrig værdien), derefter validering og sikkerhedsscanning.
- **CD** venter på, at CI er grøn, og udgiver derefter godkendte milepæle og wiki.
- Kvalitetstjek for Python, shell, C++ og C#, tællere for kodelinjer og testdækning og et tjek af, at kommentarer er på engelsk.

Værktøjerne er fastlåst til bestemte versioner. I CI har hvert job kun læserettigheder og en tidsfrist, og intet CI-job har en hemmelighed.

## 🛒 Beviset: webshoppen og NF Hotel

| Projekt | Hvad det viser |
|---|---|
| **Webshoppen** | Milepæl 1 til 6 har hver en review-rapport for koden mod Python-tjeklisten. Kodestil og typetjek består uden fejl. 289 tests og 99,8 % dækning ved milepæl 5. En test fejler, hvis domænet importerer Flask. Betalingsnøgler læses kun fra en lokal fil uden for git, og betalingen testes uden netværk |
| **NF Hotel** | 73 testfiler og en kontrol af, at lagene kun bruger hinanden i den rigtige retning. En review-rapport tjekker med et script, at alle 166 tegnede operationer findes i koden |

## 🔄 Kolbs læringscirkel: tre runder

### Runde 1: Mine egne værktøjer brød mine egne regler

**1. Konkret erfaring:** Den første gennemgang af mine scripts mod min egen tjekliste fandt et adgangsbevis (token) på kommandolinjen, hvor andre brugere kan se det, og et script, der meldte "ok", selv når noget var fejlet (10/10). Dagen efter brød min egen workflow-skabelon min tjekliste for workflows: ingen tidsfrist, ingen begrænsning af rettigheder og lange scripts inde i filen. Valideringen af workflows fandt senere flere fund i mine scripts (4/11).

**2. Refleksion:** Jeg havde skrevet reglerne til koden, men ikke målt mit eget værktøj på dem. Det, jeg selv havde skrevet, havde en sikkerhedsfejl.

**3. Abstrakt begrebsliggørelse:** Scripts er også kode. En regel er først noget værd, når den også gælder for mig selv.

**4. Aktiv eksperimenteren:** Mine scripts gennemgås mod samme tjekliste som anden kode, og kontrollerne kører automatisk.

### Runde 2: Det virkede lokalt, men ikke i CI

**1. Konkret erfaring:** I webshoppen fandt CI en falsk betalingsnøgle i en test og SQL bygget af tekststumper. Mine lokale tjek fandt dem ikke. Scripts fejlede også i CI: et stoppede midt i læsningen, da en fil blev stor (10/11), og et startede omkring 4.700 programmer i én kørsel og fik serveren til at gå ned (20/11).

**2. Refleksion:** Mine lokale tjek og CI kørte ikke det samme, og scripts blev kun prøvet på små eksempler.

**3. Abstrakt begrebsliggørelse:** Størrelse og miljø er en del af koden. Test i det miljø, koden skal køre i, og med flere data.

**4. Aktiv eksperimenteren:** Jeg kører CI's scanninger lokalt før hver push. Alle forespørgsler i webshoppen er nu faste tekster med pladsholdere. Scripts har tests med store filer.

### Runde 3: En rettelse nåede ikke frem

**1. Konkret erfaring:** Jeg rettede fejlene i frameworket, men de delte workflows brugte stadig en gammel udgave af det og fejlede igen (10/11 og 20/11).

**2. Refleksion:** Jeg troede, en fejl var løst, når rettelsen var lavet. Men den, der bruger rettelsen, skal også skifte version.

**3. Abstrakt begrebsliggørelse:** Afhængigheder mellem projekter og versionering.

**4. Aktiv eksperimenteren:** Ved hver rettelse flytter jeg også de dele, der bruger den. Da jeg i 4.0.0 samlede seks workflows i to, ændrede navnene på statuskontrollerne sig, så jeg lavede et værktøj til at flytte kravene i to trin.

## 🧩 Udfordringer

- **Jeg er min egen reviewer.** Review-rapporten for webshoppens kode siger, at AI'en er stand-in for mig. CI, kodekontrol og tests er det, der er uafhængigt af mig.
- **Frameworket håndhæver ikke reglerne.** Det gør workflowene i `git-workflows`. Et projekt uden dem har kun tjeklisten.
- **Meget arbejde i workflowene.** `git-workflows` har 561 commits og 28 udgivelser. Det er vedligeholdelse oven i selve projekterne.
- **Dokumentationen halter.** README'en i `git-workflows` siger stadig "ikke kørt på serveren" for flere workflows, selvom de har fanget fejl i webshoppen. Den skal opdateres.
- **NF Hotel har ingen automatiske kontroller.** Projektet har ingen workflow-mappe i min lokale kopi, og det ligger på GitHub og ikke på min Gitea. Tjekscriptet i en review-rapport er ikke committet, så kontrollen kan kun gentages med et tilsvarende script.

## 📈 Hvad det giver på lang sigt

- Fejl findes tidligt og af maskiner. Jeg skal ikke selv huske formatering, typer og hemmeligheder.
- AI'ens kode skal bestå samme tests, tjek og review som min egen. Det er kontrol og ikke tillid.
- De delte workflows bruges af alle repositories. Kurset har 114 projektmapper med samme struktur.
- Review-rapporter viser, hvad der blev tjekket, og med hvilket resultat.

Prisen er, at jeg vedligeholder workflows, scripts og tjeklister ud over selve produktet.

## ➡️ Næste skridt

- Køre CI's scanninger lokalt før hver push.
- Få et uafhængigt review af koden.
- Opdatere README'en i `git-workflows` efter en kørsel på serveren.
- Lave en test med mange data for alle scripts, der læser milepæle og review-rapporter.
- Flytte NF Hotel-projektet til de delte workflows og committe tjekscriptet.

## 🔄 Kolbs læringscirkel samlet

**1. Konkret erfaring**

Jeg lod AI'en bygge kode og kontrollerede den med tjeklister, tests og workflows. Underveis fejlede mine egne scripts og workflows.

**2. Refleksion**

Mine egne værktøjer fulgte ikke altid mine regler, og fejl viste sig først i CI eller med mere data.

**3. Abstrakt begrebsliggørelse**

Jeg kobler erfaringen til teori om blandt andet:

- CI/CD og statisk analyse
- test i stor skala og regressionstest
- sikker udvikling og styring af hemmeligheder
- afhængigheder og versionering mellem repositories
- Kolbs læringscirkel anvendt på mit eget arbejde

**4. Aktiv eksperimenteren**

Jeg kører de samme scanninger lokalt som i CI, tester med store datamængder og tæller, om de samme fejltyper kommer igen.

<!-- UDKAST: Refleksionerne er formuleret ud fra changelog, records og webshoppens README og skal rettes til mine egne ord. -->

## 📚 Kilder til viden

- kode-tjeklisterne i `sqa-qc-checklists` og frameworkets regler for kode
- `git-workflows`: README, guides og beslutningen om at samle workflowene i CI og CD
- webshoppens og NF Hotel-projektets review-rapporter, README og refleksion

## 🎯 Hvilke kernemål i læringsmål dækkes

🟢 dækkes helt, 🟡 dækkes delvist, 🔴 dækkes kun lidt eller slet ikke endnu. Posten handler om kontrol af kode og ikke om data eller maskinlæring.

### Dataanalyse og databehandling

| Kerneområde | Vægt i læringsmål | Dækning | Begrundelse |
|---|---|:---:|---|
| Dataindsamling | Stor | 🔴 | Ikke relevant for denne post |
| Datastrukturering | Stor | 🔴 | Ikke relevant for denne post |
| Datakvalitet | Stor | 🔴 | Posten gælder kodekvalitet og ikke datasæt |
| Datarensning | Stor | 🔴 | Ikke relevant for denne post |
| Dataanalyse | Stor | 🔴 | Ikke relevant for denne post |
| Statistik | Stor | 🔴 | Ikke relevant for denne post |
| Deskriptiv statistik | Stor | 🔴 | Ikke relevant for denne post |
| Trends og mønstre | Stor | 🔴 | Ikke relevant for denne post |
| Sammenhænge mellem variable | Stor | 🔴 | Ikke relevant for denne post |
| Datavisualisering | Stor | 🔴 | Ikke relevant for denne post |
| Fortolkning af resultater | Mindre | 🔴 | Ikke relevant for denne post |
| Formidling af data | Mindre | 🔴 | Ikke relevant for denne post |

### AI i softwareprojekter

| Kerneområde | Vægt i læringsmål | Dækning | Begrundelse |
|---|---|:---:|---|
| Python for AI | Stor | 🔴 | Webshoppen er Python, men uden AI-funktioner |
| Machine Learning | Stor | 🔴 | Ikke relevant for denne post |
| AI til fortolkning af data | Stor | 🔴 | Ikke relevant for denne post |
| Large Language Models (LLM) | Stor | 🟡 | En LLM skriver koden; modellen er ikke sammenlignet her |
| Modelvalg og model comparison | Stor | 🔴 | Ikke relevant for denne post |
| Prompt engineering | Stor | 🔴 | Ikke relevant for denne post |
| Generativ AI | Stor | 🟡 | AI-genereret kode kontrolleres; behandles også i [post 4](2026-11-23_Framework–4_AI_laver_kode_ud_fra_artefakter.md) |
| AI-baseret beslutningsstøtte | Stor | 🔴 | Ikke relevant for denne post |
| OCR | Stor | 🔴 | Ikke relevant for denne post |
| Feature extraction | Stor | 🔴 | Ikke relevant for denne post |
| Fortolkning af hoteldata | Mindre | 🔴 | Ikke relevant for denne post |
| Test og evaluering af AI-output | Mindre | 🟡 | Tests, kodekontrol, review og CI vurderer AI'ens kode; en systematisk optælling af, hvad hvert lag finder, mangler |
| Fejlhåndtering og usikkerhed | Mindre | 🟡 | CI stopper ved fund, og stopreglerne gælder; en kørsel i stor skala fandt en fejl, jeg ikke havde set |
| Human-in-the-loop | Mindre | 🟡 | Pull request og review er menneskelige trin, men reviewet er ikke uafhængigt |
| Privacy og ansvarlig AI | Mindre | 🟡 | Hemmelighedsscanning, nøgler uden for git og regler om, at hemmeligheder aldrig udskrives |

## 🏨 Hvilken værdi kan det give et hotel management-system?

- **Sikkerhed for gæstedata:** Scanning efter hemmeligheder og regler mod hemmeligheder i logfiler passer til et system, der håndterer gæster. Skal pasoplysninger udlæses med OCR, skal de behandles som hemmeligheder: aldrig på en kommandolinje og aldrig i en log.
- **Kode, der kan stoles på:** En betaling eller booking, som AI'en har skrevet, skal bestå de samme tests og tjek, før hotellet bruger den.
- **Fejl i god tid:** Tests i det rigtige miljø og med mange data er det, et hotelsystem med mange bookinger har brug for.
- **Genbrug:** De delte workflows kan bruges på hotellets repositories uden at starte forfra.
