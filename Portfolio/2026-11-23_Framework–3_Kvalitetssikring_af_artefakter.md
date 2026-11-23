# Framework 3: Kvalitetssikring af artefakter

**Dato:** 23/11 2026
**Læringsmål dækket:** [AI i softwareprojekter](https://tirsvad.studiesites.dk/laeringsmal-ai-til-softwarelosninger/) og [Dataanalyse og databehandling](https://tirsvad.studiesites.dk/laeringsmaal-dataanalyse-og-databehandling/)

Dette er post 3 i serien om mit framework. [Post 2](2026-11-23_Framework–2_AI_laver_artefakter_med_human-in-the-loop.md) viser, hvordan AI'en skriver dokumenter (artefakter). Her viser jeg, hvordan de kontrolleres, før noget bygges oven på dem. For hver dokumenttype har jeg en tjekliste, og hver gennemgang giver en review-rapport. Beviset er repositoriet [`sqa-qc-checklists`](https://git.tirsystem.com/TirSystem/sqa-qc-checklists) og de 87 review-rapporter i [`SQA-and-QC`](https://git.tirsystem.com/TirSystem/SQA-and-QC).

## 🧭 Sådan fungerer kvalitetssikringen

**Tjeklisterne.** Der er 33 tjeklister: 23 til dokumenter (fx Business Case, Use Case, Domain Model og ADR) og 10 til kode og automatisering ([post 5](2026-11-23_Framework–5_Kvalitetssikring_af_koden.md)). Tilsammen har de godt 400 kriterier. Hvert kriterium er enten *Mandatory* (skal altid opfyldes) eller *Optional*, og hvert har et kvalitetsområde fra standarden ISO/IEC 25010:2023, fx pålidelighed, sikkerhed og vedligeholdelighed. En tjekliste peger aldrig på et rigtigt dokument i et projekt, så den kan bruges overalt. Tjeklisterne ligger i et eget repository med en åben licens (CC BY-SA 4.0). En tværgående tjekliste, `QC-LANG-001`, tjekker desuden sprog og fagord i alle dokumenter på produktejerens sprog.

**En review-rapport pr. gennemgang.** Reviewer finder dokumentet og dets tjekliste og tjekker, at reviewer ikke er forfatteren. Hvert kriterium markeres som bestået, fejlet, ikke relevant eller afventende, med **evidens, en anden kan kontrollere**. Til sidst kommer en samlet afgørelse:

| Afgørelse | Betyder |
|---|---|
| **Go** | Dokumentet kan godkendes |
| **Go med betingelser** | Det kan godkendes, når opgaverne er lukket |
| **No-Go** | Det kan ikke godkendes |

Tre regler gør afgørelsen til mere end en mavefornemmelse:

- Et fejlet Mandatory-kriterium eller en åben, alvorlig sikkerhedsfejl giver altid No-Go.
- Et kriterium, som kun en anden person kan afgøre, er "afventende" og kan højst give Go med betingelser.
- Et blokerende fund kan kun accepteres i en begrænset tid med ejer, godkender og udløbsdato.

Et dokument skal gennemgås igen, når indholdet eller tjeklisten ændres. Et *delta-review* tager kun de kriterier, ændringen kan påvirke. En fuld gennemgang erstatter alle tidligere rapporter for dokumentet. Scripts kontrollerer det, der kan måles, fx at sproget er angivet, og at ingen kriterier har en ugyldig kvalitetstag. Om en tekst er forståelig, kræver en person.

## 📊 Hvad rapporterne viser

Et script tæller kriterier og resultater ud fra 52 rapporter, hvor kun én tjekliste er brugt:

| Kvalitetsområde | Kriterier | Mandatory | Bestået | Fejlet | Ikke relevant |
|---|---:|---:|---:|---:|---:|
| Functional Suitability | 89 | 80 | 143 | 5 | 8 |
| Performance Efficiency | 22 | 12 | 4 | 0 | 0 |
| Compatibility | 20 | 15 | 10 | 2 | 0 |
| Interaction Capability | 91 | 59 | 76 | 2 | 5 |
| Reliability | 131 | 105 | 143 | 2 | 6 |
| Security | 35 | 24 | 39 | 0 | 2 |
| Maintainability | 216 | 169 | 163 | 10 | 9 |
| Flexibility | 44 | 37 | 11 | 0 | 0 |
| Safety | 1 | 0 | 0 | 0 | 0 |

Et kriterium kan have flere kvalitetsområder, så rækkerne skal ikke lægges sammen. Det, jeg læser ud af tabellen:

- Fejlene samler sig om vedligeholdelighed (10 fejl), men det område har også flest kriterier (216).
- Flexibility og Performance Efficiency har få resultater i forhold til antallet af kriterier, så jeg ved mindre om dem.
- Tallene siger, hvad **tjeklisten** ser, ikke at dokumenterne er gode. De viser, at tjeklisterne er brugt, og hvor reglerne blev brudt. De er ikke et uafhængigt review.

## 🔄 Kolbs læringscirkel: tre runder

### Runde 1: Standarden blev omdøbt

**1. Konkret erfaring:** Tjeklisterne brugte de ældre navne fra ISO 25010, *Usability* og *Portability*. I 2023-udgaven hedder de *Interaction Capability* og *Flexibility* (25/10).

**2. Refleksion:** Jeg havde bygget på en standard og ikke tænkt på, at den kan ændre sig. Jeg ændrede 28 tjeklister på én gang. Jeg har endnu ikke kontrolleret navnene mod selve standarden, fordi den er ophavsretsbeskyttet.

**3. Abstrakt begrebsliggørelse:** Når et værktøj bygger på en ekstern standard, skal ændringer i standarden opdages automatisk.

**4. Aktiv eksperimenteren:** Et script fejler nu, hvis et kriterium har en tag uden for de ni navne i 2023-udgaven.

### Runde 2: En ny regel betød mange gennemgange

**1. Konkret erfaring:** Da alle dokumenter fik rækker for sprog og domæne (5/10), skulle hvert dokument gennemgås igen. Det blev til en lang række delta-rapporter. Af de 87 rapporter er 28 delta-gennemgange.

**2. Refleksion:** En ændring i en regel kan ramme mange dokumenter. Det er prisen for at have mange dokumenter, der følger samme regler.

**3. Abstrakt begrebsliggørelse:** Gør kontrollen så smal som muligt. Derfor valgte jeg én tværgående tjekliste for sprog og ikke et sprogkriterium i hver tjekliste, og derfor findes delta-review.

**4. Aktiv eksperimenteren:** Jeg ændrer en tjekliste samlet og tæller, hvor mange dokumenter den rammer, før jeg gør det.

### Runde 3: For mange rapporter at læse

**1. Konkret erfaring:** Jeg beholdt hver gennemgang, og de ældste beskrev ikke længere dokumentet. En person ville skulle læse mange rapporter for ét dokument.

**2. Refleksion:** Et revisionsspor, ingen kan læse, er ikke et spor. Git har allerede historikken.

**3. Abstrakt begrebsliggørelse:** Spor skal være til at bruge.

**4. Aktiv eksperimenteren:** Fra 19/11 slettes rapporter, som en fuld gennemgang har erstattet. Numrene bruges aldrig igen, så der er huller i rækken.

## 🧩 Udfordringer

- **Jeg er min egen reviewer.** Næsten alle rapporter er "ikke uafhængige". Afventende kriterier er lukket af mig og ikke af en, der kender domænet.
- **Tjeklisterne skal også kontrolleres.** Der er rapporter for selve tjeklisterne. En tjekliste, der ikke er gennemgået, er et skjult hul.
- **Tjeklisterne voksede af mine fejl.** Domain Model-tjeklisten fik fire nye kriterier, efter at modellerne fik tekniske ord og tomme begreber ([post 2](2026-11-23_Framework–2_AI_laver_artefakter_med_human-in-the-loop.md)). En tjekliste bliver bedre af at blive brugt.
- **Et review kan komme for sent.** I NF Hotel-projektet fandt reviewet af designet ni fejl, men designet var skrevet efter koden, så tjeklisten kunne ikke forhindre, at det kom for sent ([post 4](2026-11-23_Framework–4_AI_laver_kode_ud_fra_artefakter.md)). Projektet bruger den tidligste udgave, så mange af de nyere kriterier har dets dokumenter aldrig været målt på.

## 📈 Hvad det giver på lang sigt

- To reviewere bruger de samme kriterier, så afgørelser kan sammenlignes på tværs af dokumenter og projekter.
- Fejl kan fanges, før andre bygger oven på dem. Jeg har ikke målt, hvor meget omarbejde det sparer.
- Scriptet viser, hvor kriterierne oftest fejler, og det peger på, hvilke skabeloner jeg skal forbedre.
- Tjeklisterne er åbne og bruges af alle projekter, der bruger frameworket.

Prisen er tiden til at lave og vedligeholde 33 tjeklister og 87 rapporter.

## ➡️ Næste skridt

- Få en uafhængig reviewer til at gennemgå et dokument, så jeg kan sammenligne med mit eget review.
- Måle, hvor mange kriterier der fejler første gang, og se, om en ændring af en skabelon får tallet ned.
- Kontrollere kvalitetsområdernes navne mod selve standarden.

## 🔄 Kolbs læringscirkel samlet

**1. Konkret erfaring**

Jeg lavede tjeklister og brugte dem til at gennemgå mine dokumenter. Underveis ændrede standarden, mine regler og mine fejl tjeklisterne.

**2. Refleksion**

Kontrol koster tid, og en ændring i en regel rammer mange dokumenter. Jeg skal sige tydeligt, når et review ikke er uafhængigt.

**3. Abstrakt begrebsliggørelse**

Jeg kobler erfaringen til teori om blandt andet:

- softwarekvalitet og ISO/IEC 25010:2023
- review og inspektion, uafhængighed og evidens
- sporbarhed og versionsstyring af regler
- Kolbs læringscirkel anvendt på mit eget arbejde

**4. Aktiv eksperimenteren**

Jeg får en anden person til at gennemgå et dokument og tæller, hvor mange kriterier der fejler første gang.

<!-- UDKAST: Refleksionerne er formuleret ud fra changelog og records og skal rettes til mine egne ord. -->

## 📚 Kilder til viden

- ISO/IEC 25010:2023 (selve standarden er ophavsretsbeskyttet og ikke med i repositoriet)
- frameworkets proces for review og træning af reviewere
- tjeklisterne i `sqa-qc-checklists` og rapporterne i `docs/sqa/reviews/`

## 🎯 Hvilke kernemål i læringsmål dækkes

🟢 dækkes helt, 🟡 dækkes delvist, 🔴 dækkes kun lidt eller slet ikke endnu. Posten handler om dokumenters kvalitet og ikke om data.

### Dataanalyse og databehandling

| Kerneområde | Vægt i læringsmål | Dækning | Begrundelse |
|---|---|:---:|---|
| Dataindsamling | Stor | 🔴 | Ikke relevant for denne post |
| Datastrukturering | Stor | 🔴 | Ikke relevant for denne post |
| Datakvalitet | Stor | 🔴 | Posten gælder dokumenters kvalitet og ikke datasæt |
| Datarensning | Stor | 🔴 | Ikke relevant for denne post |
| Dataanalyse | Stor | 🔴 | Ikke relevant for denne post |
| Statistik | Stor | 🔴 | Ikke relevant for denne post |
| Deskriptiv statistik | Stor | 🔴 | Tællingen pr. kvalitetsområde er kun antal og ikke en analyse |
| Trends og mønstre | Stor | 🔴 | Ikke relevant for denne post |
| Sammenhænge mellem variable | Stor | 🔴 | Ikke relevant for denne post |
| Datavisualisering | Stor | 🔴 | Ikke relevant for denne post |
| Fortolkning af resultater | Mindre | 🔴 | Ikke relevant for denne post |
| Formidling af data | Mindre | 🟡 | Oversigten pr. kvalitetsområde viser kvaliteten på ét sted, men posten handler ikke om data |

### AI i softwareprojekter

| Kerneområde | Vægt i læringsmål | Dækning | Begrundelse |
|---|---|:---:|---|
| Python for AI | Stor | 🔴 | Scripts er skrevet i Bash |
| Machine Learning | Stor | 🔴 | Ikke relevant for denne post |
| AI til fortolkning af data | Stor | 🔴 | Ikke relevant for denne post |
| Large Language Models (LLM) | Stor | 🔴 | Ikke relevant for denne post |
| Modelvalg og model comparison | Stor | 🔴 | Ikke relevant for denne post |
| Prompt engineering | Stor | 🔴 | Ikke relevant for denne post |
| Generativ AI | Stor | 🔴 | Behandles i [post 2](2026-11-23_Framework–2_AI_laver_artefakter_med_human-in-the-loop.md) |
| AI-baseret beslutningsstøtte | Stor | 🔴 | Go/No-Go følger regler og er ikke AI-baseret |
| OCR | Stor | 🔴 | Ikke relevant for denne post |
| Feature extraction | Stor | 🔴 | Ikke relevant for denne post |
| Fortolkning af hoteldata | Mindre | 🔴 | Ikke relevant for denne post |
| Test og evaluering af AI-output | Mindre | 🟡 | AI-skrevne dokumenter vurderes kriterie for kriterie med evidens; en systematisk fejlrate mangler, og reviewet er ikke uafhængigt |
| Fejlhåndtering og usikkerhed | Mindre | 🟡 | Afventende kriterier, blokerende fund og risikoundtagelser gør usikkerhed synlig |
| Human-in-the-loop | Mindre | 🟡 | Afgørelse og godkendelse er menneskelige trin, men jeg er selv reviewer |
| Privacy og ansvarlig AI | Mindre | 🔴 | Ikke relevant for denne post |

## 🏨 Hvilken værdi kan det give et hotel management-system?

- **Samme kvalitetskrav til hotellets dokumenter:** Business Case, krav og design for NF Hotel kan vurderes med de samme kriterier, så to personer når samme afgørelse.
- **Fejl fanget før bygning:** En fejl i en domænemodel eller et kontraktdokument er billig at rette, før der er bygget en booking-løsning oven på den.
- **Et spor for revision:** Hver afgørelse har en rapport med evidens, så hotellet kan se, hvorfor noget blev godkendt.
- **Ærlighed om uafhængighed:** Rapporterne siger tydeligt, hvem der har bekræftet hvad.
