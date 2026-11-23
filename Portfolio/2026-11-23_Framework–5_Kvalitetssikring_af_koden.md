# Framework 5: Kvalitetssikring af koden

**Dato:** 23/11 2026
**Læringsmål dækket:** [AI i softwareprojekter](https://tirsvad.studiesites.dk/laeringsmal-ai-til-softwarelosninger/) og [Dataanalyse og databehandling](https://tirsvad.studiesites.dk/laeringsmaal-dataanalyse-og-databehandling/)

Denne post er nummer 5 og den sidste i serien om mit framework. [Post 4](2026-11-23_Framework–4_AI_laver_kode_ud_fra_artefakter.md) viser, hvordan AI'en skriver kode ud fra godkendte artefakter. Her viser jeg, hvordan koden kontrolleres, før den bliver flettet ind. Læringsmålet for AI kræver, at jeg tester og evaluerer AI-output, og kode fra en AI er output, der skal kontrolleres. Beviset er kode-tjeklisterne i [`sqa-qc-checklists`](https://git.tirsystem.com/TirSystem/sqa-qc-checklists), de delte workflows i [`git-workflows`](https://git.tirsystem.com/TirSystem/git-workflows) og webshoppen `097-assignment-an-online-shop`, som er bygget med dem.

## 🧭 Tre lag af kontrol

Koden kontrolleres tre steder. Jo tidligere en fejl findes, jo billigere er den.

| Lag | Hvad | Hvem eller hvad |
|---|---|---|
| **1. Lokalt, mens der kodes** | Formatering, linter, typetjek, tests og scripts | AI'en og jeg, før en commit |
| **2. Review mod en tjekliste** | Kriterier for sproget (`QC-PY-001` og de andre) og en review-record (`RC-*`) før pull requesten | Reviewer (i praksis AI som stand-in og mig) |
| **3. CI og CD på serveren** | Scanning efter hemmeligheder, kodescanning, delte kvalitetstjek, tests og tjek af changelog | Gitea Actions, i `git-workflows` |

### Lag 2: tjeklisterne til kode

Der er 10 tjeklister til kode og automatisering: Python, C, C++, C#, Rust, Flutter, React, shell, YAML-filer og CI-workflows. Python-tjeklisten (`QC-PY-001`) har 18 kriterier, fx:

- navne og casing følger PEP 8, og navne siger formål i domænets sprog
- koden er lavet af formatteren og består linteren uden uforklarede undertrykkelser
- hver signatur har typer, og typetjekket kører uden fejl
- ingen bar `except:` og ingen slugte undtagelser
- logging bruger `logging` og ikke `print`, og ingen hemmeligheder står i loggen
- **klasser og operationer kan spores til det Design Class Diagram, de implementerer; afvigelser er noteret**
- tests findes for ny adfærd, er navngivet efter adfærden og afhænger ikke af rækkefølge eller netværk
- hver viden er defineret ét sted (DRY), imports peger indad uden cirkler, og SOLID holder
- koden ligger i lagene `domain`, `application`, `infrastructure` og `presentation`, og `tests/` har `unit`, `integration` og `e2e`
- fil- og mappenavne er engelske, uden mellemrum

Hvert kriterium har en ISO/IEC 25010-karakteristik og et niveau, og tjeklisten har en liste over almindelige fejl, ligesom tjeklisterne til dokumenter i [post 3](2026-11-23_Framework–3_Kvalitetssikring_af_artefakter.md). Reviewet af koden skrives som en `RC`, nøjagtig som for et dokument.

### Hvad testene skal dække

`coding-conventions` har 14 slags test, og Test Plan skal sige, hvilke der ikke gælder, og hvorfor: positiv, negativ, grænseværdi, kanttilfælde, ækvivalensklasser, tilstandsovergang, samtidighed, kapløb, asynkron adfærd, timeout og genforsøg, fejlhåndtering, integration, regression og udforskende test. En enhedstest bruger et falsk ur og en falsk eller hukommelsesbaseret port og venter eller kalder aldrig netværket. En fejl, der rettes, får en regressionstest, som fejler uden rettelsen.

### Regler om, hvor tests kører

En GUI-test eller end-to-end-test kører aldrig på min egen skærm. Den kører i en Docker-container (Linux) eller i Windows Sandbox, så den ikke tager min mus og tastatur. Reglen er skrevet én gang (`process/gui-testing.md`), og webshoppen bruger Docker kun til skærmbilleder og browsertests.

### Fælles regler for alle kodeprojekter

Hvert kodeprojekt har en `.editorconfig` i roden, lavet af frameworkets skabelon (UTF-8, LF, to mellemrum, afsluttende linjeskift, undtagelser for Markdown, Python og C#). `check-editorconfig.sh` fejler, hvis et repository har kildefiler uden. Det samme gælder `.gitignore` fra GitHubs skabeloner, LF som linjeskift og engelske fil- og mappenavne.

### Lag 3: `git-workflows`

Delte workflows ligger i ét repository og bruges af alle repositories i organisationen. Der er otte workflows:

| Workflow | Hvad den kontrollerer |
|---|---|
| **CI** (scoped, kører i alle repositories) | `secret-scan` først (Gitleaks; et fund fejler kørslen og springer resten over og nævner regel, fil og linje, aldrig værdien), derefter `validate`, `opengrep` (statisk sikkerhedsscan) og `release-check` ved siden af hinanden |
| **CD** (scoped) | Venter på, at de fire CI-statusser for samme commit er grønne, og kører derefter `release`, udgivelse af godkendte milepæle, wiki og beskrivelsen af GitHub-spejlet for de stier, der er ændret |
| Quality checks | `ruff`, `mypy`, `shellcheck` og `shfmt` på de sporede filer; ændrer intet |
| Quality checks C++ og C# | `clang-format` og `clang-tidy` ved eksakte versioner; `dotnet format` og `dotnet build` med advarsler som fejl |
| Code metrics | Tæller kodefiler og linjer og publicerer dem og testdækningen som tre SVG-badges |
| English comments | Vurderer sproget i de kommentarer, en pull request tilføjer, og fejler, hvis en ikke er engelsk |
| Validate workflows | Repositoryets egne tests |

Værktøjerne er fastlåst til bestemte versioner. I CI har hvert job kun læserettigheder og en tidsfrist, og intet CI-job har en hemmelighed. Workflowene testes offline med `pytest`, og kørslen fejler, hvis dækningen af `tools/` falder under 95 %.

## 🛒 Beviset: webshoppen

Webshoppen er bygget af AI efter frameworket, og kontrollen kan ses i den:

| Hvad | Hvad projektet viser |
|---|---|
| Review af koden | Milepæl 1 til 6 har hver en review-record for koden mod `QC-PY-001`. `RC-022` (Stripe-milepælen) har alle 18 kriterier med evidens |
| Linter og typetjek | `ruff check` uden fejl, `mypy --strict src` uden fejl |
| Tests | 289 tests og 99,8 % dækning, da milepæl 5 blev gennemgået (grænsen er 90 %), og 340 tests til sidst ifølge refleksionssiden |
| Lag | `test_layering.py` fejler, hvis domæne eller application importerer Flask |
| Hemmeligheder | Stripe-nøglerne læses kun fra en lokal fil, som git ignorerer, en live-nøgle afvises, og en test viser, at en nøgle aldrig står i fejl eller i loggen |
| Test uden netværk | Betalingsporten testes mod en falsk gateway og en lokal falsk Stripe-server, så ingen test rammer netværket |

Webshoppens egen refleksion beskriver, hvad CI fangede, som mine lokale tjek ikke gjorde: *"a fake `sk_live_` key in a test tripped the secret scan, and SQL built from f-strings tripped the code scan."* Derfor er hver forespørgsel nu en almindelig streng med `?` som pladsholdere, og brugerinput bliver kun en bundet værdi og aldrig en del af SQL-teksten.

## 🧩 Udfordringer undervejs

**CI finder det, mit lokale tjek ikke gør.** Det var en uventet ting i webshoppen. Den falske nøgle i en test og SQL bygget af f-strings blev først fundet af CI. Min lære er at køre de samme scanninger lokalt før hver push, så en rød CI ikke er første gang, jeg ser fejlen.

**Scripts er også kode, og de skal testes i stor skala.** Et script, som læser milepæle og review-records, startede to processer for hver record for hver milepæl. For et projekt med 112 records og 21 milepæle gav det omkring 4.700 `fork`-kald i én kørsel. Det brugte processerne op på en CI-runner (`fork: retry: Resource temporarily unavailable`) og tog dens container-daemon ned. Det blev rettet i frameworkets udgave 0.24.4, så scriptet nu starter én proces pr. milepæl, og resultatet er det samme for alle milepæle i `git-workflows` (sammenlignet før og efter). Fejlen viste sig først, da der var mange records.

**Jeg er min egen reviewer.** Review-recorden for webshoppens kode siger `Mode: autonomous, not independent`, og reviewer er AI som stand-in for mig. Det er et ærligt mærke, men det betyder, at tjeklisten er anvendt, ikke at en anden har set koden. CI, linter og tests er det, der er uafhængigt af mig.

**Reglerne håndhæves ikke af frameworket.** Frameworket definerer konventionerne, men håndhæver dem ikke. Det er `git-workflows` der gør det. Det er en bevidst grænse, og den betyder, at et projekt, der ikke bruger workflowene, kun har tjeklisten at holde sig til.

**CI og CD hænger sammen uden en fælles begivenhed.** Instansen giver ikke en hændelse, der starter en workflow efter en anden. CD'en venter derfor ved at spørge efter de fire CI-statusser, op til 600 sekunder. Det er en løsning, der virker, men den er et kompromis.

**Meget arbejde i workflowene.** `git-workflows` har 558 commits og 28 tags frem til udgave 4.0.0. Seks scoped workflows blev i `ADR-0019` samlet i to, CI og CD. Det er vedligeholdelse, der kommer oven i selve projekterne.

**Dokumentationen halter efter.** README'en i `git-workflows` siger stadig "ikke kørt på instansen" for flere workflows (fx kodescanningen og valideringen), mens webshoppens refleksion viser, at secret-scan og kodescanning har fanget fejl der. Jeg skal tjekke og opdatere README'en, så den siger, hvad der faktisk er sket.

## 📚 Kilder til viden

- `qc/code/qc-programming-*.md`, `qc-yaml.md` og `qc-workflow.md`
- `coding-conventions`-skillen og dens regler for test, DRY, SOLID og `.editorconfig`
- `git-workflows`: README, guides og ADR'er (fx `ADR-0019` om CI og CD)
- webshoppens review-records, README og refleksion

## 📈 Hvad det giver på lang sigt

| Gevinst | Hvorfor |
|---|---|
| Fejl findes tidligt og af maskiner | Formatering, typer, hemmeligheder og kendte sikkerhedsfejl kontrolleres hver gang, og jeg skal ikke huske det |
| Kode fra en AI er ikke tillid, men kontrol | AI'ens kode skal bestå samme tests, tjek og review som min egen |
| Genbrug | De delte workflows bruges af alle repositories i organisationen. Kurset har 114 projektmapper med samme struktur |
| Et bevis ved siden af koden | Review-records viser, hvad der blev tjekket, og med hvilket resultat |
| Sikkerhed i bunden | Secret-scan kører først, og et fund stopper resten, så en hemmelighed ikke bliver liggende i historikken |

Prisen er, at jeg vedligeholder workflows, scripts og tjeklister ud over selve produktet. Det betaler sig, når der er mange projekter og kode skrevet af en AI, der ikke selv har ansvaret for at kontrollere den.

## ➡️ Næste skridt

- Køre CI-scanningerne lokalt før hver push i alle projekter.
- Få et uafhængigt review af koden, så jeg kan sammenligne med AI'ens.
- Opdatere README'en i `git-workflows` efter en kørsel på instansen og tjekke, at de enkelte status-linjer passer.
- Lave en test på store mængder records for alle scripts, der læser milepæle og review-records.

## 🔄 Kolbs læringscirkel i praksis

**1. Konkret erfaring**

Jeg lod AI'en skrive kode, kørte lokale tjek, lavede review mod `QC-PY-001` og lod CI og CD kontrollere resten. Jeg rettede det, CI fandt.

**2. Refleksion**

- Hvad virkede godt?
  > At maskinerne tager det, de er gode til: format, typer, hemmeligheder og SQL-mønstre. Reviewet kan bruge tiden på design og sporbarhed.
- Hvad overraskede mig?
  > At CI fandt noget, mine lokale tjek ikke gjorde, og at et script først fejlede, da der var mange records.
- Hvad er det svageste punkt?
  > At reviewet af koden ikke er uafhængigt.
- Hvad kan jeg gøre bedre?
  > Køre CI-tjekkene lokalt først og teste mine egne scripts i stor skala.

**3. Abstrakt begrebsliggørelse**

Jeg kobler erfaringen til teori om blandt andet:

- kontinuerlig integration og levering (CI/CD) og "shift left"
- statisk analyse, hemmelighedsscanning og sikre udviklingsmetoder (SSDF)
- testpyramiden og slags tests
- clean architecture og test af lagdeling
- kvalitetsmodellen ISO/IEC 25010
- skalering og ressourcegrænser i scripts

**4. Aktiv eksperimenteren**

Jeg bruger kontrollen på alle nye projekter og tæller, hvad CI finder, og hvad review finder. Tallene bruger jeg til at beslutte, hvilke tjek der skal flyttes til lokalt eller til CI.

## 🎯 Hvilke kernemål i læringsmål dækkes

🟢 dækkes helt, 🟡 dækkes delvist, 🔴 dækkes kun lidt eller slet ikke endnu. Posten handler om kontrol af kode og ikke om datasæt.

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
| Python for AI | Stor | 🔴 | Ikke relevant for denne post |
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
| Test og evaluering af AI-output | Mindre | 🟡 | Tests, linter, typetjek, review og CI vurderer AI'ens kode; en systematisk optælling af, hvad hvert lag finder, mangler |
| Fejlhåndtering og usikkerhed | Mindre | 🟡 | CI stopper ved fund, og stopreglerne gælder; en kørsel i stor skala fandt en fejl, jeg ikke havde set |
| Human-in-the-loop | Mindre | 🟡 | Pull request og review er menneskelige trin, men reviewet er ikke uafhængigt |
| Privacy og ansvarlig AI | Mindre | 🟡 | Hemmelighedsscanning, nøgler uden for git og regler om, at hemmeligheder aldrig udskrives |

## 🏨 Hvilken værdi kan det give et hotel management-system?

- **Sikker håndtering af gæstedata og betaling:** Hemmelighedsscanning, kodescanning og regler om nøgler og SQL med pladsholdere er direkte brugbare i et hotelsystem, der gemmer bookinger og kontaktoplysninger.
- **AI-kode, der kan stoles på:** Hvis AI'en skriver dele af NF Hotel, skal koden gennem de samme tests og tjek som koden, jeg selv skriver.
- **Fejl i drift findes før gæsterne:** Tests uden netværk og med falske porte gør, at betaling og booking kan testes uden rigtige penge og rigtige gæster.
- **Overskuelig vedligeholdelse:** Lag, `.editorconfig` og faste navne gør, at en ny udvikler hurtigt finder rundt.
