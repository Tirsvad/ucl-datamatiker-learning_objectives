# Framework 4: AI laver kode ud fra artefakter

**Dato:** 23/11 2026
**Læringsmål dækket:** [AI i softwareprojekter](https://tirsvad.studiesites.dk/laeringsmal-ai-til-softwarelosninger/) og [Dataanalyse og databehandling](https://tirsvad.studiesites.dk/laeringsmaal-dataanalyse-og-databehandling/)

Denne post er nummer 4 i serien om mit framework. [Post 2](2026-11-23_Framework–2_AI_laver_artefakter_med_human-in-the-loop.md) viser, hvordan AI'en skriver dokumenter, og [post 3](2026-11-23_Framework–3_Kvalitetssikring_af_artefakter.md), hvordan de bliver kontrolleret. Her viser jeg næste led: AI'en skriver kode, men kun ud fra artefakter, der er godkendt. Det er en regel, jeg har sat: **AI'en må ikke lave kode uden et use case.** Frameworket har to undtagelser: en rent teknisk opgave, hvilket skal stå i planen, og at jeg selv fravælger planen i chatten for den ene forespørgsel. Beviset er frameworkets regel `plan-first-gate`, skillen `coding-conventions` og scriptet `check-plan.sh`, og et projekt bygget med dem: Udemy-kursets webshop `097-assignment-an-online-shop` ([Gennemførelse af Udemy-kursus](2026-11-23_Gennemførelse_af_Udemy-kursus.md)).

## 🧭 Reglen: ingen kode uden plan

Intet må ligge under `src/` eller `tests/`, medmindre alle disse fire betingelser er opfyldt (`plan-first-gate.md`):

| # | Betingelse |
|---|---|
| 1 | En milepæl (`MIL-*`) er `Accepted`, og dens seneste review-record har verdict `Go` |
| 2 | Opgaven er en række i milepælens `## Tasks`, helst allerede en issue |
| 3 | Opgaven nævner det use case eller den designartefakt, den implementerer, eller den er en ren teknisk opgave (kolonnen `Needs its own Use Case/User Story?` siger `No`) |
| 4 | For en opgave, der ikke er ren teknisk: use casets Domain Model, Operation Contract, Sequence Diagram og Design Class Diagram (og ERD, hvis data gemmes) er `Accepted` med `Go` |

Hvis betingelserne ikke er opfyldt, skriver AI'en ikke kode. Den planlægger det manglende med `project-planning`-skillen, viser tørkørslen af `sync-project.sh` og stopper for at få et go. Kun jeg kan fravige det, i chatten, for den ene forespørgsel.

### Hvad er et use case, og hvad er en teknisk opgave?

Skillen skiller mellem to slags opgaver: det, en bruger eller et andet system gør ("Gæsten betaler for sin booking"), og det, teamet gør for at bygge noget ("Tilføj et databaseindeks", "Opsæt CI"). Det første har et use case. Det andet er en ren teknisk opgave. Spørgsmålet er: *beskriver rækken et mål, en aktør har, eller et skridt, teamet tager?*

### Designet kommer før koden

Inden for et use case skrives og gennemgås artefakterne i en fast rækkefølge, og hver skal være `Accepted` med `Go`, før den næste oprettes:

```
DM → SSD → OC → SD → DCD → (ERD) → kode
```

| Artefakt | Hvad den afgør |
|---|---|
| Domain Model (DM) | Hvilke begreber domænet har, i produktejerens ord |
| System Sequence Diagram (SSD) | Hvad aktøren og systemet siger til hinanden |
| Operation Contract (OC) | Hvad hver systemoperation kræver og ændrer |
| Sequence Diagram (SD) | Hvordan objekterne samarbejder for at udføre operationen |
| Design Class Diagram (DCD) | Klasser, lag, afhængigheder og metodesignaturer |
| ERD | Hvilke data der gemmes |

`new-artifact.sh` nægter at oprette et led, før det foregående er `Accepted`. Projektets egne modeller (`docs/domain-model.md`, `docs/dcd.md`) ændres først, når use casets egen er godkendt.

### Koden følger designet

Kode laves ud fra det godkendte design, og ikke omvendt. Klasse- og pakkenavne, lag og signaturer følger use casets Sequence Diagram og projektets Design Class Diagram. Viser det sig under kodning, at designet er forkert eller mangelfuldt, er det en **designændring**: ret artefakten, få den gennemgået, og ret så koden. Koden må aldrig glide væk, mens diagrammet står. Reviewer sammenligner koden med DCD'et før pull requesten.

### Hvordan AI'en følger reglen

Skillen `coding-conventions` har en forudsætning, som AI'en skal følge, før den skriver eller redigerer kode: **nævn opgaverækken (`MIL-NNN`, opgave N) eller issuen og use casen eller designartefakten, eller sig, at det er en ren teknisk opgave.** Hvis den ikke kan, afviser den og planlægger i stedet. Hvis milepælen stadig er `Proposed`, eller seneste review er `Go-with-conditions` eller `No-Go`, stopper den og siger det.

Reglen kan også håndhæves, når man committer. `install-git-hooks.sh --enable-plan-gate` slår en kontrol til, som afviser en commit, der ændrer `src/` eller `tests/`, uden en `Task: MIL-NNN#N`-trailer, der peger på en eksisterende opgave i en `Accepted` milepæl med seneste review `Go`. Den er valgfri og slået fra, indtil et projekt vælger den. En bevidst undtagelse kræver `ALLOW_UNPLANNED=1` på den ene commit.

### Mappestrukturen, AI'en skriver i

Koden lægges i lag efter `clean-architecture`-skillen: `domain` (ingen afhængigheder), `application` (use cases og porte), `infrastructure` (databaser, eksterne tjenester) og `presentation` (UI, HTTP, CLI), og `tests/` har `unit`, `integration` og `e2e`. Afhængigheder peger indad. Præsentationsmønstret er MVVM for en brugerflade og MVC for et API, og en skitse af skærmbillederne (også en i den første prompt) er AI'ens første udgave. Mappenavne er engelske, uden mellemrum, og i sprogets casing.

## 🛒 Beviset: webshoppen

Webshoppen `097-assignment-an-online-shop` (Flask, SQLite, Stripe Checkout i testtilstand og en Kanban-tavle til ordrer) er bygget med AI efter frameworket:

| Hvad | Hvad projektet viser |
|---|---|
| Plan først | Business Case, Stakeholder Analysis, Project Plan og 7 milepæle blev skrevet og gennemgået, før der kom kode. Hver milepæl gik gennem én pull request med sin egen review-record |
| Opgaverækker | Milepæl 5 (Stripe) har syv opgaver, hver med en kort beskrivelse og et resultat, og kolonnen for use case siger `No` for dem alle |
| Task-trailere | Commit-historikken har 46 linjer med `Task:`-trailere |
| Lag og test | Fire lag under `src/`, og en enhedstest (`test_layering.py`) tjekker, at domæne og application ikke importerer Flask. Review-recorden for milepæl 5 nævner 289 tests og 99,8 % dækning; refleksionssiden nævner 340 tests til sidst |
| Beslutninger før kode | Skiftet fra standardbiblioteket til Flask blev skrevet i en ADR (`ADR-0002`) og i planen, og først derefter kodet |
| Review af koden | Milepælenes kode har hver en review-record mod Python-tjeklisten ([post 5](2026-11-23_Framework–5_Kvalitetssikring_af_koden.md)) |

Webshoppens egen refleksion siger det kort: *"A decision that changes in the middle of a project, here the switch from the standard library to Flask, is cheapest when it is written down first in an ADR and the plan, and only then coded."*

## 🧩 Udfordringer undervejs

**Webshoppen har ikke use cases.** Alle opgaver i milepæl 5 er rene tekniske opgaver. Der er ingen Domain Model, Operation Contract, Sequence Diagram eller Design Class Diagram, og review-recorden siger: *"no DCD exists in this plan"*. Reglen om, at kode kommer fra et use case og dets design, er defineret og testet i frameworket og kræves af `new-artifact.sh`, men jeg har endnu ikke vist hele kæden fra use case til kode i et projekt med AI-genereret kode. Webshoppen viser planen, milepælene og reviewet. Det er det vigtigste hul i beviset.

**Kontrollen ser kun milepælen.** Commit-kontrollen tjekker, at en opgave findes i en godkendt milepæl. Den tjekker ikke, at use casets DCD er godkendt, eller at koden matcher det. Det skal reviewer gøre.

**Rækkefølgen er langsom.** Fem artefakter skal skrives og godkendes, før et use case kan blive til kode. Det er meningen, men det koster. Derfor kan rent tekniske opgaver, der ikke er et brugermål, springe kæden over, og det er også derfor, at hele webshoppen er planlagt som tekniske opgaver.

**AI'en vil gerne skrive kode med det samme.** Derfor er "byg X" altid planlægning først. Kun en udtrykkelig fravigelse fra mig i chatten, for den ene forespørgsel, ændrer det. Den gælder ikke for næste forespørgsel.

**Design og kode kan glide fra hinanden.** Det er derfor reglen siger, at et behov for ændring er en designændring, og at DCD'et er sandheden. Jeg har ikke målt, hvor tit det sker.

**Ændringer midt i et projekt.** Webshoppen skiftede fra standardbibliotek til Flask undervejs (`ADR-0002`). Det krævede nye gennemgange af Business Case, Stakeholder Analysis og planen (review-recorderne `RC-014` til `RC-018`). Det er prisen for, at beslutningen er sporbar.

## 📚 Kilder til viden

- `process/plan-first-gate.md` og `scripts/check-plan.sh`
- skillerne `coding-conventions`, `project-planning` og `clean-architecture`
- Larmans rækkefølge fra use case over domænemodel og kontrakter til design
- webshoppens `docs/` (milepæle, ADR'er, review-records og wiki)

## 📈 Hvad det giver på lang sigt

| Gevinst | Hvorfor |
|---|---|
| Kode, der kan forklares | Hver opgave peger på en milepæl, og en milepæl peger på Business Casen, så jeg kan forklare, hvorfor en linje kode findes |
| Mindre drift mellem design og kode | Koden skal følge DCD'et, og en ændring går via designet |
| Mindre risiko ved AI | AI'en kan ikke gå i gang uden en accepteret plan, og dens kode skal igennem en gennemgang |
| Genbrug | Mappestruktur og lag er den samme i alle projekter, så en ny AI-session finder det samme sted til det samme |
| Hurtigere at starte næste projekt | Planen, skabelonerne og reglerne er klar; kursets 114 projektmapper bruger dem |

Prisen er, at AI'en bruger tid på planlægning og dokumenter, før den skriver kode. For et lille projekt fylder det meget; for et projekt, der skal bruges og vedligeholdes, er det tiden, der skal spares senere. Jeg har endnu ikke målt det.

## ➡️ Næste skridt

- Bygge ét use case helt igennem med AI: Domain Model, SSD, Operation Contract, Sequence Diagram og DCD, og så kode ud fra dem. Så kan jeg vise hele kæden.
- Lade kontrollen tjekke, at use casets artefakter er `Accepted`, og ikke kun milepælen.
- Måle tid og rettelser for et projekt med og uden kæden, så jeg kan svare på, om det betaler sig.

## 🔄 Kolbs læringscirkel i praksis

**1. Konkret erfaring**

Jeg lod AI'en bygge en webshop efter frameworket: først plan og milepæle, derefter kode i lag, med et review for hver milepæl.

**2. Refleksion**

- Hvad virkede godt?
  > At AI'en ikke kunne gå i gang uden en accepteret milepæl. Det tvang mig til at beslutte, før noget blev bygget.
- Hvad overraskede mig?
  > At en ændring af beslutning midt i projektet var billigst, når den først blev skrevet som en ADR.
- Hvad mangler i beviset?
  > Et projekt, hvor koden kommer ud af et use case og dets design. Webshoppen har kun tekniske opgaver.
- Hvad kan jeg gøre bedre?
  > Bygge et use case helt igennem og måle, hvor meget længere det tager, og hvad det sparer.

**3. Abstrakt begrebsliggørelse**

Jeg kobler erfaringen til teori om blandt andet:

- use case-drevet udvikling (Larman) og sporbarhed fra krav til kode
- clean architecture, porte og adaptere og afhængigheder, der peger indad
- Domain-Driven Design: domænemodel i fagets ord
- Architecture Decision Records
- generativ AI til kode og kontrol af AI-genereret kode

**4. Aktiv eksperimenteren**

Jeg bygger næste projekt med et use case og hele kæden og måler tiden. Resultatet bruger jeg til at beslutte, hvor mange led i kæden der er nødvendige for et projekt af en given størrelse.

## 🎯 Hvilke kernemål i læringsmål dækkes

🟢 dækkes helt, 🟡 dækkes delvist, 🔴 dækkes kun lidt eller slet ikke endnu. Posten handler om AI-genereret kode, ikke om data eller maskinlæring.

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
| Datavisualisering | Stor | 🔴 | Ikke relevant for denne post |
| Fortolkning af resultater | Mindre | 🔴 | Ikke relevant for denne post |
| Formidling af data | Mindre | 🔴 | Ikke relevant for denne post |

### AI i softwareprojekter

| Kerneområde | Vægt i læringsmål | Dækning | Begrundelse |
|---|---|:---:|---|
| Python for AI | Stor | 🔴 | Webshoppen er Python, men uden AI-funktioner; Python-grundlaget er dokumenteret i [Gennemførelse af Udemy-kursus](2026-11-23_Gennemførelse_af_Udemy-kursus.md) |
| Machine Learning | Stor | 🔴 | Ikke relevant for denne post |
| AI til fortolkning af data | Stor | 🔴 | Ikke relevant for denne post |
| Large Language Models (LLM) | Stor | 🟡 | En LLM skriver koden; modellen er ikke sammenlignet her |
| Modelvalg og model comparison | Stor | 🔴 | Ikke relevant for denne post |
| Prompt engineering | Stor | 🟡 | Reglen, planen og skillerne er prompten; prompts er ikke testet systematisk |
| Generativ AI | Stor | 🟡 | AI'en genererer kode ud fra en plan; hele kæden fra use case er ikke vist |
| AI-baseret beslutningsstøtte | Stor | 🔴 | Ikke relevant for denne post |
| OCR | Stor | 🔴 | Ikke relevant for denne post |
| Feature extraction | Stor | 🔴 | Ikke relevant for denne post |
| Fortolkning af hoteldata | Mindre | 🔴 | Ikke relevant for denne post |
| Test og evaluering af AI-output | Mindre | 🟡 | AI'ens kode har enheds-, integrations- og e2e-tests og et review pr. milepæl; behandles i [post 5](2026-11-23_Framework–5_Kvalitetssikring_af_koden.md) |
| Fejlhåndtering og usikkerhed | Mindre | 🟡 | Stopregler, når planen mangler eller et review ikke er `Go` |
| Human-in-the-loop | Mindre | 🟡 | Jeg accepterer planen og kan fravige reglen; reviewet af koden er ikke uafhængigt |
| Privacy og ansvarlig AI | Mindre | 🟡 | Stripe-nøgler læses kun fra en lokal fil uden for git, og en live-nøgle afvises |

## 🏨 Hvilken værdi kan det give et hotel management-system?

- **Bookingfunktioner, der kan spores til et krav:** Hver ny funktion i NF Hotel (fx en betaling eller en prisændring) kan starte som et use case med et design, der er gennemgået, før AI'en skriver kode.
- **Mindre risiko ved AI-kode i et system med gæstedata:** AI'en kan ikke ændre noget uden en accepteret plan, og dens kode gennemgås.
- **Webshop og Kanban som mulig model:** Webshoppen viser, hvordan betaling og en ordretavle kan bygges; i et hotel kunne tavlen følge en booking fra forespørgsel til afrejse. Det er en mulighed, ikke en del af opgaven.
- **Ændringer, der er til at forklare:** En ændring af en beslutning (fx en anden betalingsløsning) er en ADR og en ny gennemgang, så hotellet kan se, hvorfor det blev ændret.
