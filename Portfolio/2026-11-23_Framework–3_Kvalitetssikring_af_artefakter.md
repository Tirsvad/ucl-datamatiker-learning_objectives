# Framework 3: Kvalitetssikring af artefakter

**Dato:** 23/11 2026
**Læringsmål dækket:** [AI i softwareprojekter](https://tirsvad.studiesites.dk/laeringsmal-ai-til-softwarelosninger/) og [Dataanalyse og databehandling](https://tirsvad.studiesites.dk/laeringsmaal-dataanalyse-og-databehandling/)

Denne post er nummer 3 i serien om mit framework. [Post 2](2026-11-23_Framework–2_AI_laver_artefakter_med_human-in-the-loop.md) viser, hvordan AI'en skriver artefakter. Her viser jeg, hvordan de bliver kontrolleret, før noget bygges oven på dem. Læringsmålet for AI kræver, at jeg tester og evaluerer AI-output. For dokumenter gør jeg det med kvalitetskriterier (QC), en tjekliste pr. artefakttype og en review-record pr. gennemgang. Beviset er repositoriet [`sqa-qc-checklists`](https://git.tirsystem.com/TirSystem/sqa-qc-checklists) og de 87 review-records i [`SQA-and-QC`](https://git.tirsystem.com/TirSystem/SQA-and-QC).

## 🧭 Hvad kvalitetssikringen består af

### Tjeklisterne

Der er 33 tjeklister: 23 til dokumenter (fx Business Case, Use Case, Domain Model, Sequence Diagram, ADR og Wiki) og 10 til kode og automatisering (se [post 5](2026-11-23_Framework–5_Kvalitetssikring_af_koden.md)). Tilsammen har de godt 400 kriterier. Hver tjekliste har:

- et ID, der er uafhængigt af projektet (`QC-BC-001`), og en versionshistorik
- kriterier med et niveau, **Mandatory** (grundlaget, som alle skal opfylde) eller **Optional**
- en **ISO/IEC 25010:2023-karakteristik** på hvert kriterium (Maintainability, Reliability, Interaction Capability og så videre)
- en liste over **almindelige fejl**, som en reviewer afviser med det samme
- en `CrossReference` til de tjeklister, den hænger sammen med

En tjekliste må aldrig pege på en rigtig artefakt i et projekt. Den er et værktøj og ikke et eksempel, og den kan derfor bruges i alle projekter. Tjeklisterne ligger i et selvstændigt repository med licensen CC BY-SA 4.0, så andre må dele og tilpasse dem, hvis de angiver kilden og bruger samme licens.

En tværgående tjekliste, `QC-LANG-001` med 10 kriterier, gælder desuden for alle typer, der er skrevet på produktejerens sprog: sproget og domænet er angivet, teksten er på det sprog, ordene er fagets ord fra ordbogen, og en, der kender sproget og domænet, har bekræftet det.

### En review-record pr. gennemgang

Reviewet følger en fast procedure (`PRC-001`), og resultatet er en review-record (`RC-NNN`):

| Trin | Hvad der sker |
|---|---|
| 1–2 | Find artefakten og dens tjekliste. Kontrollér, at reviewer ikke er forfatteren og kan læse sproget |
| 3–4 | Tag næste `RC`-nummer og opret recorden ud fra skabelonen |
| 5 | Skriv hvert kriterium af i samme rækkefølge og marker `Pass`, `Fail`, `N-A` eller `Pending` med **evidens, en anden kan kontrollere** |
| 6 | Sæt verdict: `Go`, `Go-with-conditions` eller `No-Go` med begrundelse |
| 7 | Hver `Fail` får en handling med ejer (et interessent-ID) og en dato |
| 8–9 | Få en godkendelse efter governance-dokumentet. Opdatér sporbarhedsmatrixen og artefaktens versionshistorik (`Accepted`, og rækken før bliver `Deprecated`) |

Regler, der gør verdictet til noget andet end en mavefornemmelse:

- **Blokerende fund:** en `Fail` på et Mandatory-kriterium, eller en åben sikkerhedsfejl med høj eller kritisk alvor, giver altid `No-Go`. Ingen handling kan gøre det til `Go-with-conditions`.
- **Pending:** et kriterium, som kun en anden person kan bekræfte, er `Pending` og kan højst give `Go-with-conditions`.
- **Risikoundtagelse:** et blokerende fund kan accepteres i en begrænset tid, men kun med ejer, en godkender, der hverken er forfatter eller ejer, en udløbsdato og kompenserende kontroller. Der findes ingen åben undtagelse.
- **Evidens:** et kriterium, der er "i orden", er ikke nok. Reviewer skriver, hvad der blev set, fx "Auditor har ingen use case i tabellen".

### Når noget skal gennemgås igen

Et dokument skal gennemgås igen, når indholdet ændres, når tjeklisten ændres, når sprog eller domæne skifter, og når en risikoundtagelse udløber. Et **delta-review** tager kun de kriterier, ændringen kan påvirke, og må ikke bruges til et første review eller til en indholdsmæssig ændring. En **fuld** gennemgang erstatter alle tidligere records for artefakten, og de gamle slettes i en særskilt commit, efter at links er flyttet. Git har historikken, så sporet går ikke tabt.

### Træning og kontrol af reviewere

`TRN-001` er et træningsmateriale til en reviewer: en øvelse med et diagram, hvor fejl er lagt ind, og seks krav, som alle skal være opfyldt for at bestå. Hvem der har bestået og kan læse hvilket sprog og domæne står i `TRR-001`.

### Scripts, der kontrollerer kontrollen

| Script | Hvad det gør |
|---|---|
| `check-qc-tags.sh` | Fejler, når et kriterium har en tag uden for de ni ISO/IEC 25010:2023-karakteristikker |
| `quality-overview.sh` | Tæller kriterier og resultater pr. karakteristik ud fra alle records |
| `check-languages.sh` | Fejler, når et dokument mangler et gyldigt sprog og domæne |
| `check-readme.sh` | Fejler, når en README eller frameworkets README ikke svarer til skabelonen |

## 📊 Hvad review-recordsene viser

`quality-overview.sh` over projektets review-records giver dette billede (52 records har kun én tjekliste og er talt med; delta-records og records om tjeklisterne selv er sprunget over):

| Karakteristik | Kriterier | Mandatory | Pass | Fail | N-A | Pending |
|---|---:|---:|---:|---:|---:|---:|
| Functional Suitability | 89 | 80 | 143 | 5 | 8 | 0 |
| Performance Efficiency | 22 | 12 | 4 | 0 | 0 | 0 |
| Compatibility | 20 | 15 | 10 | 2 | 0 | 0 |
| Interaction Capability | 91 | 59 | 76 | 2 | 5 | 0 |
| Reliability | 131 | 105 | 143 | 2 | 6 | 0 |
| Security | 35 | 24 | 39 | 0 | 2 | 0 |
| Maintainability | 216 | 169 | 163 | 10 | 9 | 0 |
| Flexibility | 44 | 37 | 11 | 0 | 0 | 0 |
| Safety | 1 | 0 | 0 | 0 | 0 | 0 |

Et kriterium kan have flere tags, så rækkerne skal ikke lægges sammen. Det, jeg læser ud af tabellen:

- **Fejlene samler sig om Maintainability** (10 `Fail`; næstflest har Functional Suitability med 5). Maintainability er også den karakteristik, der har flest kriterier (216), så det siger ikke alene, at den er sværest.
- **Der er ingen `Pending`** i de talte records. Det betyder, at ingen kriterier venter på en anden person; det betyder ikke, at en anden person har set dem. Det kommer jeg tilbage til under udfordringer.
- **Flexibility og Performance Efficiency har få resultater** i forhold til antallet af kriterier (11 mod 44 og 4 mod 22), så jeg ved mindre om dem. Jeg har ikke undersøgt hvorfor.
- Tallet siger noget om, hvad **tjeklisten** ser, og ikke, at dokumenterne er gode. En tjekliste kan overse noget.

## 🧩 Udfordringer undervejs

**Vedligeholdelse af tjek koster mere end tjekket.** Da jeg indførte rækkerne `Language` og `Domain` i alle dokumenter, skulle hvert dokument gennemgås igen. Det blev til en lang række delta-records (`RC-055` til `RC-074` og flere). Af de 87 records, der findes nu, er 28 delta-gennemgange. Hver ændring i en tjekliste kan ramme mange dokumenter. Det er prisen for at have mange dokumenter, der skal følge de samme regler.

**ISO-standarden blev omdøbt.** Tjeklisterne brugte de ældre navne Usability og Portability. ISO/IEC 25010:2023 hedder Interaction Capability og Flexibility, og jeg ændrede alle tjeklister (review-recorden `RC-083`). `check-qc-tags.sh` fanger nu en tag uden for de ni navne, så en ændring af standarden bliver opdaget.

**Jeg er min egen reviewer.** Næsten alle records er "ikke uafhængige". Pending-kriterierne er lukket af mig som stand-in, ikke af en person, der kender domænet. Tabellen ovenfor viser derfor ikke et uafhængigt review, og jeg skal ikke bruge den som bevis for, at dokumenterne er i orden. Den viser, at tjeklisterne er anvendt, og hvor reglerne er blevet brudt.

**For mange records at læse.** Hvis jeg beholdt hver gennemgang, ville en person skulle læse mange records for én artefakt, og de ældste beskriver ikke længere artefakten. Derfor sletter jeg records, som en fuld gennemgang har erstattet. Numrene bruges aldrig igen, så der er huller i rækken (`RC-093` er det højeste nummer, men der er 87 filer).

**Tjeklister skal også kontrolleres.** Der er records for selve tjeklisterne (fx `RC-084` for arkitekturbeskrivelsen, `RC-088` for projektplanen og `RC-091` for kriterierne 9 og 10 i domænemodellen). En tjekliste, der ikke er gennemgået, er et skjult hul.

**Kun det målbare kan scriptes.** Scripts finder manglende rækker og ugyldige tags. Om en tekst er forståelig, eller om et fagord er brugt rigtigt, kræver en person.

## 📚 Kilder til viden

- ISO/IEC 25010:2023 (karakteristikkerne). Selve standarden er ophavsretsbeskyttet og ikke med i repositoriet
- `process/review-checklist-process.md` (`PRC-001`) og `process/reviewer-training.md` (`TRN-001`)
- tjeklisterne i `sqa-qc-checklists` og records i `docs/sqa/reviews/`

## 📈 Hvad det giver på lang sigt

| Gevinst | Hvorfor |
|---|---|
| Sammenlignelige resultater | To reviewere bruger de samme kriterier, så verdicts kan sammenlignes på tværs af artefakter og projekter |
| Fejl fanges, før de bygges ind | Hvert trin slutter med et review, og næste trin kræver `Go`. Jeg har ikke målt, hvor meget omarbejde det sparer, men gaten er bygget til det |
| Et overblik over, hvor fejlene er | `quality-overview.sh` viser, hvor kriterierne oftest fejler, og det peger på, hvilke skabeloner jeg skal forbedre |
| Genbrug | Tjeklisterne er et åbent repository og bruges af alle projekter, der bruger frameworket |
| Et revisionsspor | Hver artefakt har en `RC` med evidens, og matrixen viser, hvornår den sidst blev gennemgået |

Prisen er tiden til at lave og vedligeholde 33 tjeklister og 87 records. Gevinsten kommer, når den samme tjekliste bruges på mange dokumenter og projekter.

## ➡️ Næste skridt

- Få en uafhængig reviewer til at gennemgå et dokument, så jeg kan sammenligne med mit eget review.
- Måle, hvor mange kriterier der fejler første gang, og se, om en ændring af en skabelon får tallet ned.
- Lade `quality-overview.sh` tælle delta-records med, så vedligeholdelsen af kontrollen også er synlig.

## 🔄 Kolbs læringscirkel i praksis

**1. Konkret erfaring**

Jeg lavede tjeklister til artefakter, en procedure for review og en træning, og jeg gennemgik mine egne dokumenter med dem. Jeg talte resultaterne med `quality-overview.sh`.

**2. Refleksion**

- Hvad virkede godt?
  > At verdictet har regler: et blokerende fund kan ikke forhandles om, og et kriterium, der kræver en person, kan ikke afkrydses af mig selv.
- Hvad overraskede mig?
  > At vedligeholdelsen af kontrollen fylder mere end selve kontrollen. 28 af 87 records er delta-gennemgange.
- Hvad kan tallene ikke sige?
  > At dokumenterne er gode. De siger, at kriterierne er anvendt af mig, og hvor jeg selv fandt fejl.
- Hvad kan jeg gøre bedre?
  > Få en uafhængig reviewer og lave tællingen på delta-records.

**3. Abstrakt begrebsliggørelse**

Jeg kobler erfaringen til teori om blandt andet:

- kvalitetsmodeller (ISO/IEC 25010) og kvalitetskriterier
- verifikation og validering, reviews og inspektioner
- uafhængighed i review og interessekonflikter
- ændringspåvirkning (hvad skal tjekkes igen, når en regel ændres)
- sporbarhed og revisionsspor

**4. Aktiv eksperimenteren**

Jeg bruger tjeklisterne på nye dokumenter og på [koden](2026-11-23_Framework–5_Kvalitetssikring_af_koden.md), og jeg prøver at få en anden person til at tage et review.

## 🎯 Hvilke kernemål i læringsmål dækkes

🟢 dækkes helt, 🟡 dækkes delvist, 🔴 dækkes kun lidt eller slet ikke endnu. Posten handler om kvalitet af dokumenter og ikke af datasæt.

### Dataanalyse og databehandling

| Kerneområde | Vægt i læringsmål | Dækning | Begrundelse |
|---|---|:---:|---|
| Dataindsamling | Stor | 🔴 | Ikke relevant for denne post |
| Datastrukturering | Stor | 🔴 | Ikke relevant for denne post |
| Datakvalitet | Stor | 🔴 | Tjeklisterne gælder dokumenters kvalitet og ikke datasæt |
| Datarensning | Stor | 🔴 | Ikke relevant for denne post |
| Dataanalyse | Stor | 🔴 | Ikke relevant for denne post |
| Statistik | Stor | 🔴 | Ikke relevant for denne post |
| Deskriptiv statistik | Stor | 🔴 | Tællingen pr. karakteristik er kun antal, ikke en analyse |
| Trends og mønstre | Stor | 🔴 | Ikke relevant for denne post |
| Sammenhænge mellem variable | Stor | 🔴 | Ikke relevant for denne post |
| Datavisualisering | Stor | 🔴 | Ikke relevant for denne post |
| Fortolkning af resultater | Mindre | 🔴 | Ikke relevant for denne post |
| Formidling af data | Mindre | 🟡 | Oversigten pr. karakteristik viser kvaliteten på ét sted, men posten handler ikke om data |

### AI i softwareprojekter

| Kerneområde | Vægt i læringsmål | Dækning | Begrundelse |
|---|---|:---:|---|
| Python for AI | Stor | 🔴 | Ikke relevant for denne post |
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
| Fejlhåndtering og usikkerhed | Mindre | 🟡 | `Pending`, blokerende fund og risikoundtagelser gør usikkerhed synlig |
| Human-in-the-loop | Mindre | 🟡 | Verdict og godkendelse er menneskelige trin, men jeg er selv reviewer |
| Privacy og ansvarlig AI | Mindre | 🔴 | Ikke relevant for denne post |

## 🏨 Hvilken værdi kan det give et hotel management-system?

- **Kvalitetssikring af AI-output om hotellet:** Den samme måde at gennemgå på (kriterier, evidens, verdict) kan bruges til AI-opsummeringer og prisforslag i NF Hotel, så hvert forslag er vurderet mod de samme krav.
- **Krav, der kan kontrolleres:** Hotellets krav (fx om booking og betaling) kan skrives som User Stories og use cases, som en reviewer kan afkrydse.
- **Sikkerhed ved ændringer:** En ændring i et krav udløser et nyt review af dokumenter, der afhænger af det, så en ændring ikke snigende ødelægger noget andet.
- **Kvalitet, der kan forklares for en leder:** Oversigten pr. karakteristik viser kvaliteten uden at man skal læse hver record.
