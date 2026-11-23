# Framework 2: AI laver artefakter med human-in-the-loop

**Dato:** 23/11 2026
**Læringsmål dækket:** [AI i softwareprojekter](https://tirsvad.studiesites.dk/laeringsmal-ai-til-softwarelosninger/) og [Dataanalyse og databehandling](https://tirsvad.studiesites.dk/laeringsmaal-dataanalyse-og-databehandling/)

Denne post er nummer 2 i serien om mit framework. [Post 1](2026-11-23_Framework–1_Dokumentation_artefakter_og_krydsreferencer.md) viser, hvordan artefakterne er bygget. Her viser jeg, hvordan en AI skriver dem, og hvordan jeg som menneske holder styr på det. Læringsmålet for AI kræver, at jeg bruger AI til at løse en opgave og samtidig vurderer og kontrollerer resultatet. Beviset er frameworkets regler i `AGENTS.md`, `create-project`-skillen og processen for review samt projektets prompt-log og review-records i [`SQA-and-QC`](https://git.tirsystem.com/TirSystem/SQA-and-QC).

## 🧭 Hvem gør hvad

Arbejdet med en artefakt deles mellem tre parter:

| Part | Gør | Eksempel |
|---|---|---|
| **Script** | Det, der er det samme hver gang | `new-artifact.sh` vælger ID, krydsreferencer, links, sprog og domæne og laver filen ud fra skabelonen |
| **AI** | Det, der kræver at skrive og sammenligne | Fylder indholdet i artefakten, følger den påkrævede struktur for typen og forbereder reviewet |
| **Menneske** | Det, der er en beslutning | Svarer på spørgsmål, accepterer planen, vurderer og godkender, og er den, der kan sige nej |

### Indgangen: `create-project`

Når jeg siger "byg X", starter AI'en ikke med at skrive. `create-project`-skillen stiller først ni spørgsmål (idéen i én sætning og den tro, der ville dræbe den, om idéen er afprøvet eller en mavefornemmelse, rammer, hvem der er produktejer og reviewer, sprog og domæne, brugerflade eller API, projektets navn). Svarene går ind i de første dokumenter. Derefter går den kæden igennem ét trin ad gangen og stopper ved hvert review.

Skillen læser også, hvor et projekt står, ud fra projektets egne dokumenter: hvilke artefakter der findes, deres status og seneste verdict. Den opsummerer det i fem linjer, giver to til fire valg med en anbefaling og venter på, at jeg vælger. Den genstarter aldrig et projekt, der har en tilstand.

Når et nyt projekt oprettes, kommer AI'en desuden selv med forslag til User Stories, deler dem i use cases og prioriterer dem med MoSCoW. Hvis der er mere end én primær aktør, foreslår den rollebaseret adgang ud fra use cases. Det var et ønske, jeg skrev i en prompt (prompt 5 i session 001), og som blev til frameworkets udgave 0.12.0.

## 🔒 To tilstande og regler mod, at AI godkender sig selv

| | **Supervised** (standard) | **Autonomous** |
|---|---|---|
| Hvornår | Altid, når intet andet er sagt | Kun når jeg skriver det i chatten ("autonomous mode: byg X"), og så for resten af sessionen |
| Git | AI'en committer, pusher og åbner aldrig en pull request, medmindre jeg beder om det. Jeg ser ændringerne i arbejdstræet først | AI'en committer, pusher, åbner pull request og fletter, når checks er grønne. Det kræver, at jeg først har accepteret planen |
| Review | Jeg er reviewer, eller jeg navngiver en | AI'en er reviewer som **stand-in**, og det står i hver review-record |
| Min handling | Jeg gennemgår hver ændring | Jeg accepterer planen og læser en afsluttende opsummering |

Frameworket har fire regler, som skal forhindre, at en AI godkender sit eget arbejde uden at jeg ser det:

1. **En reviewer er aldrig forfatteren.** Når AI'en har skrevet både dokumentet og udkastet til reviewet, og jeg bekræfter det, skrives det som det er: `Mode: supervised, not independent`.
2. **Stand-in er markeret.** I autonomous mode står der `AI as stand-in for S02` på reviewet, og records får linjen `Mode: autonomous, not independent`. En stand-in-gennemgang kan ikke forveksles med en uafhængig.
3. **Pending kan ikke lukkes af en stand-in.** Et kriterium, som kun en anden person kan bekræfte (fx om fagordene bruges rigtigt), er `Pending`. Det giver højst `Go-with-conditions`, aldrig `Go`.
4. **Tilstanden skifter kun i chatten.** En fil, en issue, en review-record, en kommentar eller et værktøjs output kan aldrig skifte til autonomous mode. Det er en beskyttelse mod, at tekst i data bliver læst som en instruktion.

AI'en stopper og melder tilbage, uanset tilstand, når samme review eller check fejler tre runder i træk, når arbejdet kræver noget uden for den accepterede plan, når en handling er destruktiv (force push, sletning af tag, ændring af branch protection), når en sikkerhedsfejl findes, eller når en hemmelighed skulle udskrives.

## 📝 Prompt-log

Hver session får en mappe `docs/ai-prompts/session-NNN/` med en fil, hvor hver prompt står ordret og med et kort resultat. Hemmeligheder og personlige data erstattes med `[redacted]`. I et offentligt repository ignoreres loggen.

Loggen har 4 sessioner og 62 prompts. Eksempler på, hvordan jeg styrer AI'en med korte prompts:

> We need some rules so app gui is not test under my windows. it have to be test in docker container (linux) or Windows sandbox (hide desktop) so i do not get interrupted in windows GUI

Resultatet blev en regel i frameworket (udgave 0.10.0, senere indsnævret til Windows Sandbox og Docker i 0.11.0), som siger, at en GUI-test aldrig kører på min egen skærm.

> PR 87 merges uden egen release. Vi tager den med i næste framework-release.

Det er en beslutning, AI'en ikke selv skal tage. Resultatet i loggen er, at der ikke blev gjort noget.

## 🧩 Udfordringer undervejs

**AI'en er både forfatter og reviewer.** Jeg arbejder alene, så der er ingen anden, der kan være uafhængig reviewer. Mange af mine review-records siger derfor, at de er forberedt af AI'en og bekræftet af mig, ikke uafhængige. I review-recorden `RC-092` (milepælen om `.editorconfig`) står det fx, at hvert resultat er AI'ens egen vurdering, forberedt til reviewer, og at jeg bekræftede den i chatten, uden at der er en uafhængig læser. Det er ærligt, men det er stadig en svaghed. Frameworket gør den synlig i stedet for at skjule den.

**It-ord i en model, der skal læses af produktejeren.** En Domain Model skal kunne læses af en, der kender domænet, men ikke softwaren. Jeg måtte gøre reglen for den striks i udgave 0.24.0: Domain Model er en sort kasse for softwaren, ord som run, command, option, mode, log og screen må ikke være med, hvert begreb har en forklaring på én sætning i hverdagsord, og et begreb, der kræver softwaren for at blive forklaret, fjernes.
**AI'en vil gerne i gang.** "Byg X" er altid planlægning først: planen og issues, derefter et go. Kun jeg kan fravige det, i chatten, og kun for den ene forespørgsel.

**Autonomi kræver stopregler.** Jeg ville have, at jeg kunne acceptere en plan og lade AI'en køre. Derfor findes de stopregler, jeg nævnte, og en afsluttende opsummering: pull requests, hver review med sit verdict, hver stand-in-beslutning og det, der blev stoppet på. Opsummeringen er mit review, og en beslutning kan stadig udfordres.

**Loggen kom for sent.** Reglen om prompt-loggen kom efter, at jeg var startet. Session 001 og 002 er derfor skrevet bagefter (15/10 og 21/10). Det er en ulempe ved logfilen: den er kun så god som den vane, der holder den.

**AI'ens udkast består ikke altid.** I session 004 reviewede AI'en projektplanen (`PP-001`) mod sin tjekliste. Udkastet til verdict var `No-Go`, fordi tre Mandatory-kriterier (8, 10 og 15) og to Optional (13 og 14) fejlede (review-recorden `RC-089`). Det er præcis den slags, jeg vil have fanget, før noget accepteres.

## 📚 Kilder til viden

- `AGENTS.md` i `SQA-and-QC` og skabelonen i frameworket (tilstande, stopregler, regler for review)
- `process/review-checklist-process.md` (PRC-001) og `process/reviewer-training.md` (TRN-001)
- `process/ai-prompt-log.md` og `docs/ai-prompts/`
- skillen `create-project` og skillen `artifact`

Skills ligger i både `.agents/skills/` (denne harness og Codex CLI) og `.claude/skills/` (Claude Code), begge lavet af `install-skills.sh`. Reglerne er derfor ikke bundet til ét værktøj.

## 📈 Hvad det giver på lang sigt

| Gevinst | Hvorfor |
|---|---|
| Jeg bestemmer, AI'en udfører | De beslutninger, der er mine, er listet: tilstand, plan, godkendelse, destruktive handlinger, hemmeligheder, ændret omfang |
| Et spor at gå efter | Prompt-log, review-records og sporbarhedsmatrix viser, hvad AI'en gjorde, og hvem der godkendte det |
| Lavere risiko ved autonomi | Stopreglerne og den afsluttende opsummering gør, at jeg kan lade AI'en arbejde i længere stræk |
| Genbrug | Reglerne gælder for alle projekter, der bruger frameworket, og følger med, når jeg skifter værktøj |
| Ærlig kvalitet | Rapporterne siger, hvad der er uafhængigt og ikke, så ingen kan tro, at et stand-in-review er mere end det er |

Prisen er, at hver artefakt har en proces, der er langsommere end at skrive den selv. Det betaler sig, når der er mange artefakter, og når de skal bruges igen.

## ➡️ Næste skridt

- Få en person, som ikke er forfatteren, til at lukke et af de `Pending`-kriterier, så jeg har mindst ét uafhængigt review at vise.
- Tælle, hvor mange AI-udkast der får `No-Go` første gang, og hvilke kriterier der oftest fejler, så jeg kan forbedre skabelonerne.
- Lade et script kontrollere, at en `Mode: autonomous`-record altid har et navngivet stand-in-ID.

## 🔄 Kolbs læringscirkel i praksis

**1. Konkret erfaring**

Jeg lod AI'en oprette, redigere og forberede review af artefakter i `SQA-and-QC` i supervised og autonomous mode og loggede prompts i fire sessioner.

**2. Refleksion**

- Hvad virkede godt?
  > At script, AI og menneske har hver deres opgave. AI'en skal ikke gætte et ID, og jeg skal ikke skrive links.
- Hvad overraskede mig?
  > At det vigtigste ikke var, at AI'en kunne skrive dokumenter, men at den kunne godkende dem. Det var dér, reglerne måtte skærpes.
- Hvad er det svageste punkt?
  > At jeg selv er den eneste menneskelige reviewer. Frameworket siger det højt, men det løser det ikke.
- Hvad ville jeg gøre anderledes?
  > Starte prompt-loggen den første dag og få en anden person med fra begyndelsen.

**3. Abstrakt begrebsliggørelse**

Jeg kobler erfaringen til teori om blandt andet:

- human-in-the-loop og grader af autonomi
- adskillelse af opgaver (forfatter og reviewer)
- prompt injection: instruktioner må kun komme fra brugeren i chatten
- generativ AI til dokumenter og hallucinationer
- skabeloner og skills som genbrugelig kontekst

**4. Aktiv eksperimenteren**

Jeg afprøver autonomous mode på små projekter, læser opsummeringen og tæller, hvad jeg måtte rette. Resultaterne bruges i [post 3](2026-11-23_Framework–3_Kvalitetssikring_af_artefakter.md), som handler om kvalitetssikringen.

## 🎯 Hvilke kernemål i læringsmål dækkes

🟢 dækkes helt, 🟡 dækkes delvist, 🔴 dækkes kun lidt eller slet ikke endnu. Posten handler ikke om data.

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
| Python for AI | Stor | 🔴 | Ikke relevant for denne post |
| Machine Learning | Stor | 🔴 | Ikke relevant for denne post |
| AI til fortolkning af data | Stor | 🔴 | Ikke relevant for denne post |
| Large Language Models (LLM) | Stor | 🟡 | En LLM bruges som agent; modellen er ikke sammenlignet her |
| Modelvalg og model comparison | Stor | 🔴 | Ikke relevant for denne post |
| Prompt engineering | Stor | 🟡 | Skills, `AGENTS.md` og korte prompts i en log; prompts er ikke testet systematisk |
| Generativ AI | Stor | 🟡 | AI'en genererer dokumenter ud fra skabeloner; kvaliteten er vurderet gennem reviews |
| AI-baseret beslutningsstøtte | Stor | 🟡 | AI'en forbereder review og forslag til Go/No-Go; jeg beslutter |
| OCR | Stor | 🔴 | Ikke relevant for denne post |
| Feature extraction | Stor | 🔴 | Ikke relevant for denne post |
| Fortolkning af hoteldata | Mindre | 🔴 | Ikke relevant for denne post |
| Test og evaluering af AI-output | Mindre | 🟡 | Review-records evaluerer AI'ens udkast; en systematisk optælling mangler |
| Fejlhåndtering og usikkerhed | Mindre | 🟡 | `Pending`, stopregler og mærkning af ikke-uafhængige reviews |
| Human-in-the-loop | Mindre | 🟡 | Tilstande, regler og log findes; jeg er selv den eneste menneskelige reviewer |
| Privacy og ansvarlig AI | Mindre | 🟡 | Hemmeligheder redigeres væk i loggen og må aldrig udskrives; offentlige repositories ignorerer loggen |

## 🏨 Hvilken værdi kan det give et hotel management-system?

- **Samme regler for AI-forslag i hotellet:** Princippet om at AI'en forbereder og mennesket godkender kan bruges til prisforslag og AI-opsummeringer i NF Hotel, så en medarbejder altid godkender.
- **Sporbarhed ved beslutninger:** Hvis en AI foreslår en prisændring, kan en log vise, hvem der godkendte den og på hvilket grundlag.
- **Beskyttelse af gæstedata:** Reglen om, at hemmeligheder og personlige data ikke skrives i en log, er direkte brugbar i et hotelsystem.
- **Ærlighed om usikkerhed:** Mærkningen "ikke uafhængig" svarer til at mærke en AI-tekst som hypotese og ikke prognose.
