# Processen i at vælge – benchmark af lokal AI

**Dato:** 27/9 2026
**Læringsmål dækket:** [AI i softwareprojekter](https://tirsvad.studiesites.dk/laeringsmal-ai-til-softwarelosninger/) og [Dataanalyse og databehandling](https://tirsvad.studiesites.dk/laeringsmaal-dataanalyse-og-databehandling/)

Jeg har brug for at vælge en lokal AI-model/LLM, som passer til den prototype, der skal udvikles og køre på den valgte PO-hardware. I stedet for blot at vælge en model ud fra specifikationer eller andres benchmarks vil jeg gerne have et beslutningsgrundlag, der tager udgangspunkt i den hardware og de krav, som prototypen faktisk skal køre med. Derfor har jeg valgt at lave min egen benchmark af relevante lokale AI-modeller.

Formålet er ikke at finde den bedste AI-model generelt, men at undersøge: *"hvilken lokal AI-model/LLM passer bedst til prototypen på den hardware, som prototypen skal køre på?"* For at kunne svare på det har jeg brug for data om både performance, ressourceforbrug og kvaliteten af modellens svar.

## 🧭 Processen i at vælge et benchmark-grundlag

### Valg af kriterier

Jeg har valgt at måle på flere forskellige områder:

| Kriterium | Hvad måles? |
|---|---|
| TTFT | Hvor lang tid der går, før modellen begynder at svare |
| Total execution time | Hvor lang tid hele prompten tager at gennemføre |
| Completion tokens | Hvor mange tokens modellen genererer |
| Tokens/sec | Hvor hurtigt modellen genererer tokens |
| Ressourceforbrug | CPU, RAM, GPU og VRAM, hvor det er relevant |
| Svar fra modellen | Kvaliteten og anvendeligheden af modellens svar |
| Task pass/fail | Om modellen løser den konkrete opgave korrekt, hvor dette kan vurderes objektivt |

Det er vigtigt, at benchmarken ikke kun ser på hastighed. En model kan være hurtig, men hvis svarene ikke er anvendelige til prototypens formål, er hastigheden ikke alene et tilstrækkeligt grundlag for valget.

### Benchmark på den hardware, prototypen skal bruge

Et vigtigt valg i processen er, at benchmarken skal køres på den PO-hardware, som prototypen skal køre på. Hvis jeg benchmarker modellerne på min egen udviklingscomputer, kan resultaterne være svære at bruge som beslutningsgrundlag – den samme model kan have meget forskellige egenskaber afhængigt af hardware. Derfor er princippet:

**Samme hardware → samme test → sammenlignelige resultater**

På den måde får jeg data, der er relevante for den faktiske prototype. De lokale modeller køres via Ollama, med mulighed for også at teste modeller gennem LM Studio.

### Marimo som benchmark-værktøj

Jeg har valgt at bruge Marimo Notebook til benchmarken. Fordelen er, at jeg kan kombinere Python-kode, beregninger, resultater og visualisering i samme notebook. Benchmarken kan derfor både:

1. køre testene
2. indsamle resultater
3. beregne relevante metrics
4. visualisere resultaterne
5. sammenligne modellerne

Det gør det lettere at gå fra rå benchmarkdata til et beslutningsgrundlag.

### Human-in-the-loop

Performance kan måles med tal, men kvaliteten af et AI-svar kan ikke nødvendigvis reduceres til én måling. Derfor bruger jeg human-in-the-loop. Modellerne får de samme prompts, og deres svar vurderes efterfølgende. Jeg ser blandt andet på:

- om svaret løser opgaven
- om svaret er relevant
- om svaret kan anvendes
- om modellen følger promptens krav
- om der er fejl eller mangler

På den måde kombinerer jeg de målbare data med en menneskelig vurdering af outputtet. Det giver en mere nuanceret vurdering af modellerne end kun at kigge på eksempelvis tokens/sec.

### Jeg brugte AI til at lave benchmarken

En interessant del af processen er, at jeg også brugte AI til at udvikle selve benchmark-notebooken. Gennem mit arbejde med AI prompting og AI skills har jeg arbejdet med at formulere prompts, der beskriver kravene til den løsning, jeg ønsker. Jeg lod derfor AI hjælpe med at generere projektet og notebook-koden. AI kunne generere en stor del af projektet væsentligt hurtigere, end jeg selv ville kunne skrive det fra bunden. Det sparede både tid og ressourcer.

Men jeg accepterede ikke bare den genererede kode. Jeg gennemgik koden, vurderede strukturen og kontrollerede, om den gjorde det, som jeg havde bedt om. Det blev dermed også en praktisk øvelse i human-in-the-loop – ikke kun i selve benchmarken, men også i udviklingen af værktøjet. AI producerer outputtet, men det er stadig mig, der skal forstå, kontrollere og validere resultatet.

### Fra benchmark til beslutningsgrundlag

Benchmarken skal ikke blot ende med en tabel med tal. Målet er at kunne bruge resultaterne til at træffe et teknisk valg.

![Diagram 1](https://tirsvad.studiesites.dk/wp-content/uploads/sites/82065/2026/09/image-5.png)

Det betyder, at valget af model bliver baseret på data fra den konkrete situation, hvor modellen skal anvendes.

## 🔄 Kolbs læringscirkel i praksis

**1. Konkret erfaring**

Jeg havde behov for at vælge en lokal AI-model til prototypen og begyndte derfor at undersøge, hvordan modellerne kunne sammenlignes.

**2. Refleksion**

- Hvorfor var det ikke nok blot at vælge en model ud fra specifikationer eller andres benchmarks?
  > Fordi den samme model kan have meget forskellige egenskaber afhængigt af hardware – jeg havde brug for et beslutningsgrundlag baseret på den hardware og de krav, som prototypen faktisk skal køre med.
- Hvad viste det sig, at jeg havde brug for, ud over hastighed?
  > Data om både performance, ressourceforbrug og kvaliteten af modellens svar. En hurtig model er ikke tilstrækkelig, hvis svarene ikke er anvendelige til prototypens formål.

**3. Abstrakt begrebsliggørelse**

Jeg definerede derfor konkrete benchmark-kriterier som TTFT, execution time, tokens/sec, tokenforbrug, ressourceforbrug og kvaliteten af svarene.

**4. Aktiv eksperimenteren**

Jeg byggede benchmarken som en Marimo Notebook og kørte modellerne på PO-hardware. Resultaterne kan derefter bruges til at sammenligne modellerne og kvalificere valget.

Min vigtigste læring er, at valg af AI-model ikke nødvendigvis bør starte med spørgsmålet *"hvilken model er bedst?"*, men med det mere relevante spørgsmål: *"hvilken model passer bedst til vores konkrete behov, vores hardware og de opgaver, modellen skal løse?"* Ved at benchmarke modellerne på den hardware, som prototypen skal køre på, får jeg et mere relevant beslutningsgrundlag. Samtidig har arbejdet vist mig, hvordan AI, prompting, dataanalyse og softwareudvikling kan kombineres i én praktisk proces.

## 🎯 Hvilke kernemål i læringsmål dækkes

🟢 dækkes helt, 🟡 dækkes delvist, 🔴 dækkes kun lidt eller slet ikke endnu.

### Dataanalyse og databehandling

| Kerneområde | Vægt i læringsmål | Dækning | Begrundelse |
|---|---|:---:|---|
| Dataindsamling | Stor | 🟡 | Benchmark-kriterierne (TTFT, execution time, tokens/sec, ressourceforbrug) definerer, hvilke data der skal indsamles, men selve målingerne er endnu ikke kørt |
| Datastrukturering | Stor | 🟡 | Marimo Notebook er valgt netop for at kunne strukturere benchmark-resultater, men strukturen er endnu ikke udfyldt med data |
| Datakvalitet | Stor | 🔴 | Ikke relevant for denne post |
| Datarensning | Stor | 🔴 | Ikke relevant for denne post |
| Dataanalyse | Stor | 🟡 | Notebooken er designet til at beregne og sammenligne metrics, men analysen er endnu ikke gennemført |
| Statistik | Stor | 🔴 | Ikke udført endnu |
| Deskriptiv statistik | Stor | 🔴 | Ikke udført endnu |
| Trends og mønstre | Stor | 🔴 | Ikke udført endnu |
| Sammenhænge mellem variable | Stor | 🟡 | Formålet er netop at undersøge sammenhængen mellem hardware, model og performance, men dette er endnu ikke gjort |
| Datavisualisering | Stor | 🟡 | Visualisering af resultater indgår i planen for notebooken, men er ikke produceret endnu |
| Fortolkning af resultater | Mindre | 🔴 | Ikke muligt før benchmarken er kørt |
| Formidling af data | Mindre | 🔴 | Ikke relevant for denne post |

### AI i softwareprojekter

| Kerneområde | Vægt i læringsmål | Dækning | Begrundelse |
|---|---|:---:|---|
| Python for AI | Stor | 🟡 | Benchmarken bygges som Python-kode i en Marimo Notebook |
| Machine Learning | Stor | 🔴 | Ikke relevant for denne post |
| AI til fortolkning af data | Stor | 🔴 | Ikke udført endnu |
| Large Language Models (LLM) | Stor | 🟢 | Selve formålet er at benchmarke og vælge mellem lokale LLM'er |
| Modelvalg og model comparison | Stor | 🟡 | En konkret, kriteriebaseret metode til modelvalg er defineret (hardware-specifik benchmark), men selve sammenligningen er ikke gennemført endnu |
| Prompt engineering | Stor | 🟡 | Modellerne får de samme prompts som del af benchmarken, og AI blev også promptet til at bygge selve værktøjet |
| Generativ AI | Stor | 🟡 | AI bruges til at generere benchmark-notebooken |
| AI-baseret beslutningsstøtte | Stor | 🟡 | Hele formålet er at skabe et databaseret beslutningsgrundlag for modelvalg |
| OCR | Stor | 🔴 | Ikke relevant for denne post |
| Feature extraction | Stor | 🔴 | Ikke relevant for denne post |
| Fortolkning af hoteldata | Mindre | 🔴 | Ikke relevant for denne post |
| Test og evaluering af AI-output | Mindre | 🟡 | Human-in-the-loop-kriterierne (løser opgaven, relevans, anvendelighed, fejl/mangler) definerer, hvordan AI-output skal evalueres |
| Fejlhåndtering og usikkerhed | Mindre | 🔴 | Ikke udført endnu – benchmarken er endnu ikke kørt |
| Human-in-the-loop | Mindre | 🟢 | Eksplicit gennemgående tema, både i selve benchmarken og i kontrollen af den AI-genererede benchmark-kode |
| Privacy og ansvarlig AI | Mindre | 🟡 | Fokus på lokale modeller (via Ollama/LM Studio) understøtter samme privacy-tankegang som tidligere værktøjsvalg |

## 🏨 Hvilken værdi kan det give et hotel management-system?

Benchmarken skal give et mere dokumenteret grundlag for valget af lokal AI-model/LLM til prototypen. I stedet for *"denne model virker som den bedste"* kan jeg arbejde ud fra *"denne model har disse målte egenskaber på den hardware, som prototypen skal køre på, og dens svar er vurderet i forhold til de konkrete opgaver."*

Det giver mulighed for at tage højde for flere faktorer samtidig:

- performance
- ressourceforbrug
- svartid
- kvalitet
- anvendelighed
- hardwarebegrænsninger
- lokal databehandling og privacy

Det passer med projektets overordnede fokus, hvor dataanalyse skal skabe et grundlag for at kunne anvende AI og efterfølgende validere resultaterne med menneskelig kontrol. Samtidig har arbejdet vist, hvordan AI, prompting, dataanalyse og softwareudvikling kan kombineres i én praktisk proces: AI har hjulpet med at udvikle benchmark-værktøjet hurtigere, mens jeg selv har haft ansvaret for krav, kontrol, vurdering og den endelige tekniske beslutning – en tilgang, der direkte kan genbruges, når hotellets egne AI-funktioner skal vælges, bygges og valideres.
