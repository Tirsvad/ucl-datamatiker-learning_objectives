# Framework 2: AI laver artefakter med human-in-the-loop

**Dato:** 23/11 2026
**Læringsmål dækket:** [AI i softwareprojekter](https://tirsvad.studiesites.dk/laeringsmal-ai-til-softwarelosninger/) og [Dataanalyse og databehandling](https://tirsvad.studiesites.dk/laeringsmaal-dataanalyse-og-databehandling/)

Dette er post 2 i serien om mit framework. [Post 1](2026-11-23_Framework–1_Dokumentation_artefakter_og_krydsreferencer.md) viser, hvordan dokumenterne (artefakterne) er bygget. Her viser jeg, hvordan en AI skriver dem, og hvordan jeg som menneske holder styr på det. Human-in-the-loop betyder, at en person altid godkender, før noget regnes for færdigt.

## 🧭 Hvem gør hvad

| Part | Gør | Eksempel |
|---|---|---|
| **Script** | Det, der er ens hver gang | Laver filen ud fra skabelonen med ID, links, sprog og domæne |
| **AI** | Det, der kræver at skrive og sammenligne | Skriver indholdet og forbereder et udkast til review |
| **Menneske (mig)** | Det, der er en beslutning | Svarer på spørgsmål, godkender planen og kan sige nej |

Når jeg siger "byg X", skriver AI'en ikke med det samme. Den stiller først ni spørgsmål, fx hvad idéen er, hvem produktejeren er, og om der skal være en brugerflade. Derefter går den et trin ad gangen og stopper ved hvert review. Den foreslår også selv brugerhistorier og prioriterer dem.

## 🔒 Regler mod, at AI godkender sig selv

AI'en arbejder i en af to tilstande:

| | **Overvåget** (standard) | **Autonom** |
|---|---|---|
| Hvornår | Altid, når intet andet er sagt | Kun når jeg skriver det i chatten, og kun for den session |
| Git | AI'en gemmer og deler ikke ændringer uden at blive bedt om det | AI'en gemmer, deler og fletter, når kontrollerne er grønne, efter jeg har godkendt planen |
| Review | Jeg er reviewer | AI'en står i for en person, og det står i rapporten |

Reglerne er:

1. En reviewer er aldrig forfatteren. Hvis AI'en har skrevet både dokument og review, og jeg bekræfter, står der "ikke uafhængigt".
2. Når AI'en står i for en person, står det på rapporten.
3. Et punkt, som kun en person kan afgøre, kan ikke lukkes af AI'en. Så kan resultatet højst blive "go med betingelser".
4. Tilstanden skifter kun i chatten. Tekst i en fil eller et værktøjs output kan aldrig skifte den.

AI'en stopper og melder tilbage, når et tjek fejler tre gange i træk, når arbejdet kræver noget uden for planen, når en handling er destruktiv, eller når en hemmelighed skulle udskrives.

**Prompt-log:** Hver session har en fil, hvor hver prompt står ordret med et kort resultat. Hemmeligheder erstattes med `[redacted]`. Loggen i `SQA-and-QC` har 4 sessioner og 62 prompts. Et eksempel på, hvordan en kort prompt blev en regel: *"…it have to be test in docker container (linux) or Windows sandbox … so i do not get interrupted in windows GUI"* blev til reglen om, at en GUI-test aldrig kører på min egen skærm.

## 🔄 Kolbs læringscirkel: tre runder

### Runde 1: Systemet godkendte sig selv

**1. Konkret erfaring:** Alle skabeloner oprettede nye dokumenter som "godkendt". Derfor kunne en ny milepæl starte kodning, før nogen havde gennemgået den (5/10). En anden fejl i samme kontrol var, at en milepæl, der blev foreslået igen efter sin godkendelse, stadig bestod.

**2. Refleksion:** Det var samme fejl, som jeg ville forhindre hos AI'en, bare i en skabelon. Noget kunne godkende sig selv, uden at jeg så det.

**3. Abstrakt begrebsliggørelse:** Godkendelse skal være en handling, ikke en standardværdi. Og reglen skal ligge i en test og ikke kun i en tekst.

**4. Aktiv eksperimenteren:** Alle dokumenttyper starter som "foreslået", og en test opretter hver type og tjekker det. Kontrollen læser kun den seneste status.

### Runde 2: AI'en lagde tekniske ord i en model for produktejeren

**1. Konkret erfaring:** En Domain Model skal kunne læses af en, der kender hotellet, men ikke softwaren. Alligevel kom der tekniske løsninger og ord som "kommando", "log" og "skærm" ind i modellen. Jeg måtte stramme reglen to gange (12/11 og 19/11).

**2. Refleksion:** AI'en lægger gerne en løsning ind, så snart den ser en. Jeg gjorde det også selv.

**3. Abstrakt begrebsliggørelse:** Modellen skal være en sort kasse for softwaren. Hvert begreb har en forklaring på én sætning i hverdagsord, og et begreb, der kræver softwaren for at blive forklaret, fjernes.

**4. Aktiv eksperimenteren:** Tjeklisten for Domain Model fik nye kriterier, så et review kan fange det.

### Runde 3: Loggen kom for sent

**1. Konkret erfaring:** Reglen om prompt-log kom, efter jeg var startet. Session 1 og 2 er skrevet bagefter (15/10 og 21/10). I NF Hotel-projektet findes kun planlægningsprompten, så prompts til design og kode er ikke logget.

**2. Refleksion:** En log, der skrives bagefter, er en erindring og ikke et spor.

**3. Abstrakt begrebsliggørelse:** Sporbarhed kræver en vane fra dag ét.

**4. Aktiv eksperimenteren:** Loggen startes i første session i det næste arbejde.

## 🧩 Udfordringer

- **Jeg er min egen reviewer.** Jeg arbejder alene, så mange rapporter siger "forberedt af AI'en og bekræftet af mig". Det er ærligt, men det er ikke et uafhængigt review. I NF Hotel-projektet er reviewet af designet lavet af en AI-reviewer, der ikke skrev dokumentet, men reviewer S04 har ikke bekræftet det, så resultatet er betinget.
- **Planen kan accepteres af en, der også har skrevet den.** Det strider mod reglen om, at reviewer aldrig er forfatter. Det står som et kendt hul, og jeg har ikke lukket det.
- **AI'ens udkast består ikke altid.** AI'ens første review af projektplanen blev et udkast til "no-go", fordi fem punkter fejlede. Det er netop det, jeg vil have fanget, før noget godkendes.

## 📈 Hvad det giver på lang sigt

- Jeg bestemmer, og AI'en udfører. De beslutninger, der er mine, er skrevet ned.
- Der er et spor: prompt-log, review-rapporter og sporbarhedsmatrix viser, hvad AI'en gjorde, og hvem der godkendte det.
- Reglerne gælder for alle projekter og følger med, når jeg skifter AI-værktøj.
- Rapporterne siger, hvad der er uafhængigt og ikke, så ingen tror, at en AI-gennemgang er mere end den er.

Prisen er, at hvert dokument har en proces, der er langsommere end at skrive det selv.

## ➡️ Næste skridt

- Få en anden person til at gennemgå et dokument, så jeg har mindst ét uafhængigt review.
- Tælle, hvor mange AI-udkast der får "no-go" første gang, og hvilke punkter der oftest fejler.
- Lade et script kontrollere, at en rapport fra autonom tilstand altid siger, hvem AI'en stod i for.

## 🔄 Kolbs læringscirkel samlet

**1. Konkret erfaring**

Jeg lod AI'en skrive dokumenter efter frameworket, med et review ved hvert trin og en log over prompts.

**2. Refleksion**

Det er ikke kun AI'en, der kan godkende sig selv. En skabelon, et script og jeg selv kan også. Jeg stoler ikke på en kontrol, jeg ikke selv har set fejle.

**3. Abstrakt begrebsliggørelse**

Jeg kobler erfaringen til teori om blandt andet:

- human-in-the-loop og uafhængighed i review
- prompt engineering og kontekst til AI-agenter
- sporbarhed og ansvarlig AI
- Kolbs læringscirkel anvendt på mit eget arbejde

**4. Aktiv eksperimenteren**

Jeg starter prompt-loggen første dag og får en anden person til at gennemgå mindst ét dokument.

<!-- UDKAST: Refleksionerne er formuleret ud fra changelog og records og skal rettes til mine egne ord. -->

## 📚 Kilder til viden

- `AGENTS.md` og skillen `create-project` (tilstande, stopregler, regler for review)
- frameworkets proces for review og træning af reviewere
- prompt-loggen i `docs/ai-prompts/` og review-rapporterne i `SQA-and-QC`

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
| AI-baseret beslutningsstøtte | Stor | 🟡 | AI'en forbereder review og forslag til go/no-go; jeg beslutter |
| OCR | Stor | 🔴 | Ikke relevant for denne post |
| Feature extraction | Stor | 🔴 | Ikke relevant for denne post |
| Fortolkning af hoteldata | Mindre | 🔴 | Ikke relevant for denne post |
| Test og evaluering af AI-output | Mindre | 🟡 | Review-rapporter evaluerer AI'ens udkast; en systematisk optælling mangler |
| Fejlhåndtering og usikkerhed | Mindre | 🟡 | Stopregler, punkter der afventer en person, og mærkning af ikke-uafhængige reviews |
| Human-in-the-loop | Mindre | 🟡 | Tilstande, regler og log findes; jeg er selv den eneste menneskelige reviewer |
| Privacy og ansvarlig AI | Mindre | 🟡 | Hemmeligheder redigeres væk i loggen og må aldrig udskrives; offentlige repositories ignorerer loggen |

## 🏨 Hvilken værdi kan det give et hotel management-system?

- **Samme regler for AI-forslag i hotellet:** AI'en forbereder, og mennesket godkender. Det kan bruges til prisforslag og AI-opsummeringer i NF Hotel, så en medarbejder altid godkender.
- **Sporbarhed ved beslutninger:** Hvis en AI foreslår en prisændring, kan en log vise, hvem der godkendte den og på hvilket grundlag.
- **Beskyttelse af gæstedata:** Reglen om, at hemmeligheder og personlige data ikke skrives i en log, kan bruges direkte i et hotelsystem.
- **Ærlighed om usikkerhed:** Mærkningen "ikke uafhængig" svarer til at mærke en AI-tekst som hypotese og ikke som prognose.
