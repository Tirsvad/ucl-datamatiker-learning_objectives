# Læringsmål – Dataanalyse og databehandling

*Del af et 30 ECTS-forløb, 26/8–6/12 2026, som køres sideløbende med et andet valgfrit læringsmål (min. 12, maks. 18 ECTS pr. valgfag). Dette læringsmål er på **12 ECTS**; det andet (AI til softwareløsninger) er på 18 ECTS. Se den fælles [Projektplan – Ugeplan.md](Projektplan%20-%20Ugeplan.md) for tidsplan og timefordeling.*

## 🎯 Mål

Jeg vil opnå praktisk kompetence i at indsamle, strukturere, rense, analysere og visualisere data med fokus på historiske hoteldata.

Jeg vil kunne anvende statistiske metoder og datavisualisering til at identificere trends, mønstre og sammenhænge i data og kunne forklare, hvad resultaterne betyder.

Jeg vil desuden kunne vurdere datakvalitet og begrænsninger og formidle analyseresultater på en måde, der kan understøtte beslutninger om eksempelvis kapacitet, priser, bemanding og planlægning.

Fokus er på dataenes kvalitet, behandling og fortolkning – ikke på at udvikle Machine Learning-modeller (det ligger i [Læringsmål 1](Læringsmål%20–%20AI%20til%20hotelbelægning%20og%20prisforudsigelse.md)).

### Viden, kunnen og kompetencer – med Bloom-niveau

**Viden** – jeg har viden om

| # | Jeg har viden om | Bloom-niveau |
|---|---|---|
| V1 | datakilder, datastruktur og typiske datakvalitetsproblemer (manglende værdier, dubletter, fejlformater) | Forstå |
| V2 | deskriptiv statistik: gennemsnit, median, kvartiler, standardafvigelse og variation | Forstå |
| V3 | visualiseringstyper (linje, søjle, histogram, boxplot, scatterplot) og hvad hver egner sig til | Forstå |
| V4 | datas begrænsninger og hvad data kan/ikke kan fortælle | Forstå |

**Kunnen** – jeg kan

| # | Jeg kan | Bloom-niveau |
|---|---|---|
| K1 | anvende Python-biblioteker til dataanalyse (Pandas og Matplotlib) | Anvende |
| K2 | dokumentere datakilde, struktur og begrænsninger for et historisk hoteldatasæt | Forstå |
| K3 | gennemføre en systematisk kontrol af datakvalitet (manglende værdier, dubletter, fejlformater m.m.) | Analysere |
| K4 | anvende statistiske mål (gennemsnit, median, kvartiler, standardafvigelse m.fl.) | Anvende |
| K5 | forklare, hvad statistiske resultater fortæller om datasættet | Forstå |
| K6 | identificere trends, mønstre og sammenhænge i data | Analysere |

**Kompetencer** – jeg kan selvstændigt

| # | Jeg kan selvstændigt | Bloom-niveau |
|---|---|---|
| C1 | vælge og designe relevante visualiseringer til en given problemstilling | Skabe |
| C2 | begrunde valg af visualiseringstype ud fra hvad den skal vise | Vurdere |
| C3 | vurdere datakvalitet, begrænsninger og hvad data kan/ikke kan fortælle | Vurdere |
| C4 | formidle analyseresultater som grundlag for beslutninger om kapacitet, pris, bemanding og planlægning | Skabe |
| C5 | overføre min dataforståelse til nye opgaver og domæner | Anvende |

Niveauet spænder fra forstå (viden) over anvende/analysere (kunnen) til vurdere/skabe (kompetencer) – passende for et 30 ECTS-forløb, hvor formidling og kritisk vurdering af data vejer tungere end ren beskrivelse.

## 📚 Kerneområder

**I større grad:**
Dataindsamling · Datastrukturering · Datakvalitet · Datarensning · Dataanalyse · Statistik · Deskriptiv statistik · Trends og mønstre · Sammenhænge mellem variable · Datavisualisering

**I mindre grad:**
Fortolkning af resultater (delt med Læringsmål 1) · Formidling af data

Dette læringsmål bærer hovedvægten af kerneområdet **Dataanalyse & databehandling**, med **Formidling/dokumentation** som understøttende (mindre) kerneområde.

## 📊 Målbare succeskriterier

Jeg betragter læringsmålet som opnået, når jeg kan dokumentere:

**1. Datasæt**
Jeg anvender mindst ét historisk datasæt med hotelrelaterede data, som indeholder relevante variable såsom dato, ugedag, måned/sæson, antal bookede værelser, kapacitet, belægningsprocent, værelsestype og pris. Jeg dokumenterer datakilde, struktur og eventuelle begrænsninger.

**2. Datakvalitet og databehandling**
Jeg gennemfører en systematisk kontrol af datasættet og identificerer manglende værdier, ugyldige værdier, dubletter, fejlformater og irrelevante data. Jeg dokumenterer mindst 3 konkrete datakvalitetsproblemer og beskriver, hvordan de håndteres.

**3. Statistisk analyse**
Jeg anvender mindst 4 statistiske mål eller beregninger (fx gennemsnit, median, minimum/maksimum, kvartiler, standardafvigelse, variation) og kan forklare, hvad resultaterne fortæller om datasættet.

**4. Trends og mønstre**
Jeg identificerer mindst 5 konkrete trends, mønstre eller sammenhænge (fx forskel mellem hverdage/weekender, sæsonvariation, perioder med høj/lav belægning, forskelle mellem værelsestyper, sammenhæng mellem pris og belægning). Hver observation understøttes af en relevant beregning eller visualisering.

**5. Visualisering**
Jeg udvikler mindst 4 forskellige relevante visualiseringer (fx linjediagram, søjlediagram, histogram, boxplot, scatterplot) og kan forklare, hvorfor hver er valgt, og hvad den viser.

**6. Fortolkning**
Jeg udarbejder en samlet analyse, hvor jeg forklarer hvilke mønstre der findes, hvilke variable der ser ud til at hænge sammen, hvad data kan/ikke kan fortælle, og hvilke begrænsninger der er ved analysen.

## 🚀 Milestones (se ugeplan for datoer)

| Milestone | Uge | Indhold |
|---|---|---|
| M1 – Domæneforståelse | Uge 1–2 (26/8–2/9) | Domæneforståelse af det sideløbende projekt (NF Hotel), som datasættet og analysen tager udgangspunkt i |
| M2 – Python-opstart | Uge 1–3 (26/8–9/9) | Python-kursus (*100 Days of Code*): opstart på Python-sproget samt Pandas- og Matplotlib-bibliotekerne – kurset er kun påbegyndt i denne periode, ikke gennemført |
| M3 – Datasæt og datakvalitet | Uge 4–5 (16/9–23/9) | Find/opret datasæt, dokumentér variable/kilde, identificér ≥3 datakvalitetsproblemer, første Kolb-refleksion |
| M4 – Første databehandling | Uge 6–7 (30/9–7/10) | Rens data, beregn gennemsnit/median/min/maks, ≥2 indledende visualiseringer |
| M5 – Uddybet statistik | Uge 8 (14/10) | Udvid til ≥4 statistiske mål (kvartiler, standardafvigelse) |
| M6 – Trends og mønstre | Uge 9–12 (21/10–11/11) | Identificér ≥5 trends/mønstre understøttet af beregning/visualisering, ≥4. visualisering |
| M7 – Samlet fortolkning | Uge 13 (18/11) | Beskriv hvad data kan/ikke kan fortælle, og analysens begrænsninger |
| M8 – Konklusion | Uge 14 (25/11) | Samlet konklusion på analysen, portfolio klargøres |
| Aflevering | Uge 15 (2/12–6/12) | SMART-tjek, samlet konklusion, portfolio |

## 🔄 Læring gennem Kolbs læringscirkel

**1. Konkret erfaring**
Jeg arbejder praktisk med et hoteldata-sæt og gennemfører dataindsamling, datarensning og analyse.

**2. Refleksion**
Jeg dokumenterer: hvilke problemer jeg fandt i data, hvilke valg jeg foretog, hvilke visualiseringer der fungerede, hvilke resultater der overraskede mig.

**3. Abstrakt begrebsliggørelse**
Jeg kobler mine erfaringer til teori om: statistik, datakvalitet, databehandling, visualisering, korrelation og sammenhænge.

**4. Aktiv eksperimenteren**
Jeg bruger min nye forståelse til at ændre analysen, afprøve andre metoder eller visualiseringer og sammenligne resultaterne.

Analyse → refleksion → teori → ny analyse

## 🗂️ Bevis / portfolio

- [x] Python ([bevis](Portfolio/2026-10-28_Python_og_Pandas_fra_Udemy-kurset.md))
  - [x] Pandas
  - [ ] Mathplotlib
- [x] Datasæt og datakilde
- [ ] Beskrivelse af variable
- [x] Analyse af datakvalitet
- [ ] Dokumentation af mindst 3 datakvalitetsproblemer
  - [x] Felter uden værdi
  - [ ] Kolonne der ikke har værdi for data analysen
  - [x] Fjernelse af rækker hvor der mangler værdi til at analysere
  - [ ] Fjernelse af duplikater
- [x] Mindst 4 statistiske beregninger ([bevis](Portfolio/2026-11-01_dataanalyse_i_NF_Hotels_markedsanalyse.md))
  - [x] Cancellation rate
  - [x] Belægning procent af værelser
  - [x] Belægning af værelser på helligdage
  - [x] Omsætning på værelser
- [ ] Forklaring af hvad hver statistisk beregning fortæller om datasættet
- [x] Mindst 4 visualiseringer ([bevis](Portfolio/2026-11-01_dataanalyse_i_NF_Hotels_markedsanalyse.md))
  - [x] Cancellation rate
  - [x] Belægning procent af værelser
  - [x] Belægning af værelser på helligdage
  - [x] Omsætning på værelser
- [x] Begrundelse for valg af visualiseringstype pr. visualisering
- [x] Mindst 5 identificerede trends/mønstre
- [ ] Fortolkning af resultater
- [x] Beskrivelse af dataenes begrænsninger
- [ ] Refleksioner efter Kolbs læringscirkel
- [ ] Samlet konklusion på analysen som beslutningsstøtte (kapacitet, pris, bemanding, planlægning)

## ✅ SMART-tjek

### 🎯 S – Specifikt
🎯 **Måltavle:** Jeg vil analysere historiske hoteldata med fokus på datakvalitet, statistik, trends, mønstre og visualisering.

📍 **Placeringsnål:** Målet er placeret ved databehandling og -fortolkning, afgrænset fra ML-modelbygning, som hører til Læringsmål 1.

### 📊 M – Målbart
📊 **Søjlediagram:** ≥3 dokumenterede datakvalitetsproblemer med håndtering.
📈 **Stigende kurve:** ≥4 statistiske beregninger og ≥5 identificerede trends/mønstre, hver understøttet af beregning eller visualisering.
📏 **Lineal:** ≥1 datasæt, ≥4 visualiseringer, samlet fortolkning med eksplicitte begrænsninger.

### 🤝 A – Attraktivt/Opnåeligt
🤝 **Håndtryk:** Projektet afgrænses til dataanalyse og databehandling uden krav om at udvikle Machine Learning-modeller.

💪 **Spændt biceps:** De 26 ugentlige lærings-/portfolio-timer giver plads til grundig databehandling og dokumentation gennem hele perioden.

✅ **Flueben:** Hvert milestone har konkrete, afkrydsbare leverancer (se milestone-tabel og portfolio-liste).

### ⚖️ R – Relevant
⚖️ **Vægt:** Læringsmålet balancerer teknisk databehandling med formidling, der kan bruges til reelle beslutninger.

🔑 **Nøgle:** Det giver et praktisk grundlag for at arbejde med datadrevne softwareløsninger og understøtter projektets dataanalyse-kerneområde.

### ⏱️ T – Tidsbestemt
⏱️ **Stopur:** 26/8–6/12 2026, milestone hver uge (se ugeplan).

📅 **Kalender:** M1 uge 1–2, M2 uge 1–3, M3 uge 4–5, M4 uge 6–7, M5 uge 8, M6 uge 9–12, M7 uge 13, M8 uge 14, aflevering uge 15.

⏳ **Timeglas:** Ved eksamen afgøres det, om læringsmålet er opnået, ud fra om jeg kan indsamle, behandle, analysere, visualisere og fortolke et datasæt samt forklare mine metodiske valg og analysens begrænsninger.
