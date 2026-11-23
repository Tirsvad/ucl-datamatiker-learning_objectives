# Framework 4: AI laver kode ud fra artefakter

**Dato:** 23/11 2026
**Læringsmål dækket:** [AI i softwareprojekter](https://tirsvad.studiesites.dk/laeringsmal-ai-til-softwarelosninger/) og [Dataanalyse og databehandling](https://tirsvad.studiesites.dk/laeringsmaal-dataanalyse-og-databehandling/)

Dette er post 4 i serien om mit framework. [Post 2](2026-11-23_Framework–2_AI_laver_artefakter_med_human-in-the-loop.md) viser, hvordan AI'en skriver dokumenter (artefakter), og [post 3](2026-11-23_Framework–3_Kvalitetssikring_af_artefakter.md), hvordan de kontrolleres. Her viser jeg næste skridt: AI'en skriver kode, men kun ud fra dokumenter, der er godkendt.

Min regel er: **AI'en må ikke skrive kode uden en godkendt plan.** For en funktion betyder det et use case (en beskrivelse af, hvad en bruger vil opnå) og et godkendt design. Rene tekniske opgaver, som at sætte CI op, kan undtages, hvis planen siger det. Jeg kan selv fravælge planen i chatten, men kun for den ene forespørgsel.

## 🧭 Sådan foregår det

Først godkendes planen og opgaven. Derefter laves designet i en fast rækkefølge, og hvert led skal være godkendt, før det næste laves:

```
Use case → Domain Model → SSD → Operation Contract → Sequence Diagram → Design Class Diagram → kode → test og review
```

| Led | Hvad det afgør |
|---|---|
| Domain Model | Hvilke begreber domænet har, i produktejerens ord |
| System Sequence Diagram (SSD) | Hvad brugeren og systemet siger til hinanden |
| Operation Contract | Hvad hver handling kræver, og hvad den ændrer |
| Sequence Diagram | Hvordan delene i koden samarbejder om handlingen |
| Design Class Diagram | Klasser, lag og hvem der må bruge hvem |

Koden følger designet og ikke omvendt. Viser designet sig at være forkert, ændrer jeg designet først, får det gennemgået og retter så koden. Reviewer sammenligner koden med designet, før den lægges sammen med resten.

Frameworket kontrollerer det på tre måder:

- AI'en skal nævne opgaven og use casen, før den skriver kode. Ellers planlægger den i stedet og stopper for at få mit go.
- Et script (`new-artifact.sh`) nægter at lave det næste dokument, før det foregående er godkendt.
- Man kan slå en kontrol til, der afviser en commit med kode, som ikke peger på en godkendt opgave.

## 📚 To projekter som bevis

| Projekt | Hvad det viser |
|---|---|
| **NF Hotel** (`Notebook_Market_Analysis`): et program, der analyserer hotelbookinger fra en JSON-fil | Hele kæden findes: 12 milepæle, 5 use cases, design, 13 beslutninger (ADR) og 30 review-rapporter. Koden har fem lag, 73 testfiler og en kontrol af, at lagene kun bruger hinanden i den rigtige retning |
| **Webshoppen** fra Udemy-kurset | Planen og 7 milepæle blev godkendt før koden. 289 tests og 99,8 % dækning ved milepæl 5. Her er alle opgaver rent tekniske, så kæden fra use case til design vises ikke |

NF Hotel-projektet bruger stadig den tidligste udgave af frameworket (`v0.1.0`).

## 🔄 Kolbs læringscirkel: tre runder

### Runde 1: Design kom efter koden

**1. Konkret erfaring:** I NF Hotel-projektet sagde planen, at designet skulle være lavet før koden. Alligevel byggede jeg først kernen, analyserne og notebooken. Designet skrev jeg bagefter ("som bygget").

**2. Refleksion:** Gennemgangen af designet fandt ni fejl og syv åbne spørgsmål. Fx havde koden fem lag og ti porte, hvor beslutningen beskrev færre, og domænemodellen passede ikke til koden. Det meste løste jeg ved at ændre beslutningen og ikke koden. Det viste mig, at det ikke er nok at skrive "design før kode" i en plan. Jeg bryder den, når jeg har travlt.

**3. Abstrakt begrebsliggørelse:** En regel skal håndhæves af en kontrol og ikke kun stå i en tekst. Frameworket krævede først kun, at milepælen var godkendt. Fra 19/11 kræver det også, at designet er godkendt, før koden skrives, og et script tjekker rækkefølgen. Jeg har ikke en record, der siger, at NF Hotel-forløbet førte til ændringen, så det må jeg selv bekræfte.

**4. Aktiv eksperimenteren:** Næste use case i NF Hotel-projektet laver jeg med designet først.

### Runde 2: Design og kode gled fra hinanden alligevel

**1. Konkret erfaring:** De nye use cases (nr. 3 til 5) blev designet før koden. Alligevel var der samme dag seks forskelle mellem design og kode.

**2. Refleksion:** Selv med designet først ændrer man ting, mens man koder.

**3. Abstrakt begrebsliggørelse:** Design og kode skal holdes sammen hele vejen. Derfor siger reglen, at et behov for ændring er en designændring: ret designet, og ret så koden.

**4. Aktiv eksperimenteren:** Jeg registrerer forskellene mellem design og kode og tæller dem. Antallet kan vise, om processen virker.

### Runde 3: En beslutning ændrede sig midt i projektet

**1. Konkret erfaring:** I webshoppen skiftede jeg fra Pythons standardbibliotek til Flask, mens projektet var i gang.

**2. Refleksion:** Skiftet var billigt, fordi jeg skrev det ned som en beslutning (ADR) først og så ændrede planen og koden. Det krævede nye gennemgange af forretningsgrundlaget, interessenterne og planen, men det var til at følge.

**3. Abstrakt begrebsliggørelse:** En beslutning, der ændres, er billigst, når den er skrevet ned med en begrundelse, før koden ændres.

**4. Aktiv eksperimenteren:** Jeg skriver en beslutning ned, før jeg ændrer strukturen i et projekt. I webshoppens egen konklusion står også, at jeg skulle have gjort frameworket færdigt, før første milepæl.

## 🧩 Udfordringer

- **Jeg har endnu ikke brugt hele processen, som den er nu, i et projekt fra start til slut.** NF Hotel har kæden, men designet kom efter koden. Webshoppen har den nye regel, men ingen use cases. Det er det vigtigste hul i beviset.
- **Det går langsommere.** Fem dokumenter skal skrives og godkendes, før et use case kan blive til kode. Rene tekniske opgaver kan springe kæden over, og derfor er hele webshoppen planlagt som tekniske opgaver.
- **Kontrollen er ikke fuld.** Den tjekker, at milepælen er godkendt, men ikke, at use casets design er det. Det skal en reviewer gøre.
- **Det koster at holde frameworket opdateret.** NF Hotel-projektet står stadig på den tidlige udgave, så hver ændring i frameworket er en flytning, jeg selv skal lave.

## 📈 Hvad det giver på lang sigt

- Jeg kan forklare, hvorfor en linje kode findes, fordi hver opgave peger på en plan, og planen peger på forretningsgrundlaget.
- AI'en kan ikke gå i gang uden en godkendt plan, og dens kode gennemgås.
- Mapper og lag er ens i alle projekter, så en ny AI-session finder det samme sted til det samme.
- Næste projekt starter med færdige skabeloner og regler.

Jeg har endnu ikke målt, hvor meget tid eller hvor mange fejl det sparer.

## ➡️ Næste skridt

- Flytte NF Hotel-projektet til den nuværende udgave af frameworket med `update-framework.sh`.
- Bygge næste use case dér med designet først, måle tiden og tælle forskellene mellem design og kode.
- Lade kontrollen tjekke, at use casets design er godkendt, og ikke kun milepælen.

## 🔄 Kolbs læringscirkel samlet

**1. Konkret erfaring**

Jeg brugte AI til at bygge kode ud fra planer og milepæle, i NF Hotel-projektet og i webshoppen.

**2. Refleksion**

Det er ikke nok at skrive "design før kode". Design og kode kan stadig afvige fra hinanden, og ændringer midt i arbejdet skal skrives ned.

**3. Abstrakt begrebsliggørelse**

AI-kode skal bygge på godkendte krav og design. Regler skal følges af kontroller, og en person skal gennemgå resultatet. Jeg kobler det til teori om blandt andet:

- use case-drevet udvikling (Larman) og sporbarhed fra krav til kode
- clean architecture og afhængigheder, der peger indad
- Domain-Driven Design: domænemodel i fagets ord
- arkitekturbeslutninger (ADR)
- generativ AI til kode og kontrol af AI-genereret kode

**4. Aktiv eksperimenteren**

I næste use case i NF Hotel-projektet godkender jeg designet, før AI'en skriver kode. Jeg måler tiden og registrerer forskellene mellem design og kode.

<!-- UDKAST: Refleksionerne er formuleret ud fra projekternes dokumenter og skal rettes til mine egne ord. -->

## 📚 Kilder til viden

- frameworkets regel `process/plan-first-gate.md` og skillerne `coding-conventions`, `project-planning` og `clean-architecture`
- Larmans rækkefølge fra use case over domænemodel og kontrakter til design
- NF Hotel-projektets og webshoppens dokumenter (milepæle, beslutninger, review-rapporter)

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
| Generativ AI | Stor | 🟡 | AI'en genererer kode ud fra en plan, og i NF Hotel-projektet findes hele kæden; designet blev dog skrevet efter koden for de første to use cases |
| AI-baseret beslutningsstøtte | Stor | 🔴 | Ikke relevant for denne post |
| OCR | Stor | 🔴 | Ikke relevant for denne post |
| Feature extraction | Stor | 🔴 | Ikke relevant for denne post |
| Fortolkning af hoteldata | Mindre | 🔴 | Ikke relevant for denne post |
| Test og evaluering af AI-output | Mindre | 🟡 | AI'ens kode har tests og et review pr. milepæl; behandles i [post 5](2026-11-23_Framework–5_Kvalitetssikring_af_koden.md) |
| Fejlhåndtering og usikkerhed | Mindre | 🟡 | AI'en stopper, når planen mangler, eller et review ikke er godkendt |
| Human-in-the-loop | Mindre | 🟡 | Jeg godkender planen og kan fravige reglen; reviewet af koden er ikke uafhængigt |
| Privacy og ansvarlig AI | Mindre | 🟡 | Betalingsnøgler i webshoppen læses kun fra en lokal fil uden for git, og en live-nøgle afvises |

## 🏨 Hvilken værdi kan det give et hotel management-system?

- **Funktioner, der kan spores til et krav:** Hver ny funktion i NF Hotel kan starte som et use case med et gennemgået design, før AI'en skriver kode, så en ændring kan forklares.
- **Mindre risiko ved AI-kode i et system med gæstedata:** AI'en kan ikke ændre noget uden en godkendt plan, og dens kode gennemgås.
- **Ændringer, der er til at forklare:** En ny beslutning, fx en anden betalingsløsning, skrives ned og gennemgås, så hotellet kan se, hvorfor den blev ændret.
- **Kun en mulighed endnu:** Jeg har endnu ikke målt, hvor meget tid eller hvor mange fejl metoden sparer, så det skal jeg afprøve i et helt use case.
