# Dataanalyse i NF Hotels markedsanalyse

**Dato:** 1/11 2026
**Læringsmål dækket:** [Dataanalyse og databehandling](https://tirsvad.studiesites.dk/laeringsmaal-dataanalyse-og-databehandling/) og [AI i softwareprojekter](https://tirsvad.studiesites.dk/laeringsmal-ai-til-softwarelosninger/)

Læringsmålet for dataanalyse kræver, at jeg beregner statistiske mål, finder trends og mønstre, vælger og begrunder visualiseringer og beskriver dataenes begrænsninger. Denne post er beviset for den del. Beviset er siden *Market analysis* i NF Hotels administration, som viser en kørsel af markedsanalysen over hotellets bookinger (kørt 29/10 2026). AI-opsummeringerne er endnu ikke koblet på (`AI_NOT_CONFIGURED`), så posten dokumenterer dataanalysen og ikke AI-delen.

## 🧭 Hvad analysen indeholder

Analysen blev kørt på **156.686 bookinger**. Nøgletal øverst viser, at 794 bookinger har prisen 0, og at der er 0 duplikerede booking-id'er.

Siden har ni analyser. Hver har sine egne diagrammer:

| Analyse | Diagramtyper | Eksempel på indhold |
|---|---|---|
| Lead time | Søjler, donut, sorterede søjler, måned × år | Fordeling på 0–7, 8–30, 31–90 og 91+ dage |
| Cambodian holidays | – | Ingen diagramdata i denne kørsel |
| Sæsonvariation og bookingtempo | Måned × år | Ankomster og bookinger pr. måned |
| Annulleringer | Søjler, sorterede søjler, måned × år | Annulleringsrate pr. depositumtype, lead time, kundetype, segment og antal særønsker |
| Værelsesværdi og opholdslængde | Donut, søjler | Estimeret værdi og opholdslængde |
| Gæste- og bookingmix | Donut, sorterede søjler, søjler | Gentagne gæster, måltid, parkering, værelsestype, land, antal gæster |
| Belægning | Måned × år | Belægningsprocent pr. måned |
| Belægning på helligdage | Søjler | Helligdage mod øvrige dage |
| Korrelationer | Varmekort | Spearman-korrelation mellem 12 bookingfelter |

### Valg af visualisering

Hvert diagram har tre faste tekster, som viser, hvordan jeg og systemet begrunder valget:

- **What it shows:** hvad diagrammet viser.
- **Why this chart:** hvorfor netop denne diagramtype. Eksempel: en donut bruges kun til 2–4 dele, der tilsammen er 100 %; selvstændige rater, der ikke summerer til 100 %, vises som søjler og aldrig som donut; mange kategorier vises som sorterede søjler; en lang række måneder vises som måned mod år, så en sæson ses som en mørk kolonne.
- **What it cannot say:** begrænsninger for det enkelte diagram.

De tre tekster er med i prototypen, fordi de gør begrundelsen synlig, mens jeg udvikler. De skal ikke med i produktionen, hvor en leder ikke har brug for at se, hvorfor en diagramtype er valgt.

## 📊 Trends og mønstre

Jeg fandt følgende mønstre i resultaterne. Hvert er understøttet af en beregning og et diagram:

1. **Annullering stiger med lead time.** Annulleringsraten er 6,5 % for 0–7 dage, 21,5 % for 8–30, 32,4 % for 31–90 og 39,2 % for 91+. Samlet er 27,5 % annulleret.
2. **Gruppebookinger og online-bureauer annullerer mest.** Segmentet Groups har 42,4 % og Online TA 34,9 %, mens Direct har 13,2 %.
3. **Depositumtype hænger tæt sammen med annullering.** No Deposit 24,4 %, Refundable 15 % og Non Refund 96 %. Den høje rate for Non Refund er påfaldende og bør undersøges i dataene, før den tolkes.
4. **Belægningen er sæsonbestemt.** Belægningen er højest i marts (65,6 % i 2025 og 65,9 % i 2026) og lavest i sommermånederne (25 % i juli 2025 og 36,2 % i juli 2026).
5. **Helligdage har lidt lavere belægning end øvrige dage.** 46,6 % mod 51,4 %. Forskellen er en sammenhæng og ikke en forklaring, da weekender og sæsoner også falder på helligdage.
6. **Korrelationer med annullering (Spearman):** lead time +0,28, tidligere annulleringer +0,22, krav til parkeringspladser −0,25, ændringer i booking −0,14 og antal særønsker −0,11. Lead time er også stærkt forbundet med antal hverdagsnætter (+0,54).

Fordelingerne giver også et billede af gæsterne: 4,5 % er gentagne gæster, 70,3 % rejser to personer, 75,1 % har morgenmad (BB), og 42,6 % har værelsestype A.

## ⚠️ Begrænsninger og datakvalitet

Siden viser selv, hvad analyserne ikke kan sige. Det jeg lagde mærke til:

- Landet er `Unknown` for 99,6 % af bookingerne, så en analyse af gæsternes oprindelse er ikke mulig.
- 794 bookinger har prisen 0. De er med i værdien og tælles i `zero_price_records`.
- Den estimerede værdi er et estimat og ikke omsætning. Annullerede bookinger værdisættes som de øvrige.
- Bookinger uden de nødvendige felter udelades og tælles i `records_left_out`, så fraværet er synligt.
- Bookingtal og belægning dækker fremtidige måneder. Januar 2027 viser 11,2 % belægning, fordi perioden kun er delvist dækket.
- Grupper med få bookinger er markeret med en stjerne. Eksempel: 16 ændringer i bookingen giver 100 %, men bygger på meget få bookinger.
- Korrelation er en sammenhæng og ikke en årsag. Spearman finder kun en jævn stigning eller et jævnt fald.
- Afsnittet om Cambodian holidays havde ingen diagramdata i denne kørsel.

## 🧩 Udfordringer undervejs

**Diagrammer fra Python til C#.** Analysen og diagrammerne laves i Python, men siden vises i C#-projektet. Jeg løser det ved at udvide JSON-skemaet, så det får et felt til SVG. Python tegner diagrammet som SVG og sender det med i svaret, og C# viser det uden selv at skulle tegne noget.

**Valg af LLM.** Jeg troede, at jeg havde valgt en god model, men den gik ikke i dybden med analysen. Derfor er jeg tilbage ved phi4. Den kræver en GPU, eller lang tid på CPU. Det er en pris, som skal med i vurderingen af, hvordan AI-opsummeringerne kan køre i produktion. Det stemmer med benchmarken, hvor phi4 kørte 10,8 tokens i sekundet mod 85,8 for gemma4:e2b.

**Systemer på forskellige arkitekturer.** At få flere systemer til at spille sammen og ikke bare arbejde sammen kræver mere arbejde, end jeg forventede. Det er ikke nok, at hver del virker. Formatet mellem dem skal aftales, og kontrakten skal holdes i begge ender.

## 🔄 Kolbs læringscirkel i praksis

**1. Konkret erfaring**

Jeg kørte markedsanalysen på hotellets bookinger og gennemgik de ni analyser med diagrammer og begrænsninger.

**2. Refleksion**

- Hvilke mønstre gav mest værdi?
  > Annullering efter lead time og segment, fordi de kan bruges til at vurdere risiko for tomme værelser, og belægning efter måned, fordi den viser, hvornår der er plads til flere bookinger.
- Hvad overraskede mig?
  > At Non Refund har 96 % annullering. Det er det modsatte af, hvad man forventer, og peger på noget i dataene, der skal undersøges.
- Hvad kan resultaterne ikke sige?
  > Årsager. Alt er sammenhænge, og landet er stort set ukendt, så oprindelse kan ikke analyseres.
- Hvad kan jeg gøre bedre?
  > Få AI-opsummeringerne koblet på med phi4, undersøge Non Refund-fundet og få data for helligdagene i Cambodia med. Jeg skal også teste kontrakten mellem Python og C# tidligere, så uoverensstemmelser opdages, før de bliver en blokering.

**3. Abstrakt begrebsliggørelse**

Jeg kobler erfaringen til teori om blandt andet:

- deskriptiv statistik: rater, andele og fordelinger
- korrelation (Spearman) versus kausalitet
- valg af diagramtype efter hvad data skal vise (del af helhed, rater, rækkefølge, kategorier, tid)
- datakvalitet: manglende værdier, nulpriser og ukendte kategorier
- stikprøvestørrelse og usikkerhed ved få observationer
- belægningsprocent og opholdslængde i hotelbranchen

**4. Aktiv eksperimenteren**

Jeg kører analysen på andre perioder (seneste år og seneste tre år), ser om mønstrene holder, og undersøger Non Refund-fundet i de rå data.

## 🎯 Hvilke kernemål i læringsmål dækkes

🟢 dækkes helt, 🟡 dækkes delvist, 🔴 dækkes kun lidt eller slet ikke endnu.

### Dataanalyse og databehandling

| Kerneområde | Vægt i læringsmål | Dækning | Begrundelse |
|---|---|:---:|---|
| Dataindsamling | Stor | 🟡 | Bookinger hentes fra markedsanalysens API; indsamlingen er ikke dokumenteret her |
| Datastrukturering | Stor | 🟡 | Bookinger grupperet i bånd, segmenter, måneder og år |
| Datakvalitet | Stor | 🟡 | Nulpriser, ukendt land og manglende felter er tællet og synlige |
| Datarensning | Stor | 🟡 | Poster uden de nødvendige felter udelades og tælles; ingen selvstændig rensning i denne post |
| Dataanalyse | Stor | 🟢 | Ni analyser af 156.686 bookinger |
| Statistik | Stor | 🟡 | Rater, andele og Spearman-korrelation |
| Deskriptiv statistik | Stor | 🟡 | Fordelinger og rater; median og standardafvigelse er ikke set på siden |
| Trends og mønstre | Stor | 🟢 | Seks mønstre understøttet af beregning og diagram |
| Sammenhænge mellem variable | Stor | 🟢 | Korrelationsmatrix over 12 felter |
| Datavisualisering | Stor | 🟢 | Donut, søjler, sorterede søjler, måned × år og varmekort, hver med begrundelse |
| Fortolkning af resultater | Mindre | 🟡 | Fortolket i denne post; en samlet fortolkning mangler |
| Formidling af data | Mindre | 🟡 | Rapportsiden viser, hvad hvert diagram viser og ikke kan sige |

### AI i softwareprojekter

| Kerneområde | Vægt i læringsmål | Dækning | Begrundelse |
|---|---|:---:|---|
| Python for AI | Stor | 🔴 | Ikke relevant for denne post |
| Machine Learning | Stor | 🔴 | Ikke relevant for denne post |
| AI til fortolkning af data | Stor | 🔴 | AI-opsummeringerne er ikke koblet på (`AI_NOT_CONFIGURED`) |
| Large Language Models (LLM) | Stor | 🔴 | Ikke relevant for denne post |
| Modelvalg og model comparison | Stor | 🟡 | Et tidligere modelvalg holdt ikke i den dybere analyse, så valget er tilbage ved phi4; begrundelsen er ikke dokumenteret endnu |
| Prompt engineering | Stor | 🔴 | Ikke relevant for denne post |
| Generativ AI | Stor | 🔴 | Ikke relevant for denne post |
| AI-baseret beslutningsstøtte | Stor | 🔴 | Siden er klargjort til AI-opsummeringer, men de er ikke aktive |
| OCR | Stor | 🔴 | Ikke relevant for denne post |
| Feature extraction | Stor | 🔴 | Ikke relevant for denne post |
| Fortolkning af hoteldata | Mindre | 🟡 | Hoteldata fortolket af mig; ikke af AI |
| Test og evaluering af AI-output | Mindre | 🔴 | Ikke relevant for denne post |
| Fejlhåndtering og usikkerhed | Mindre | 🟡 | Siden viser fejlkoden `AI_NOT_CONFIGURED` i stedet for at skjule, at AI mangler |
| Human-in-the-loop | Mindre | 🔴 | Ikke relevant for denne post |
| Privacy og ansvarlig AI | Mindre | 🔴 | Ikke relevant for denne post |

## 🏨 Hvilken værdi kan det give et hotel management-system?

- **Kapacitet og bemanding:** Belægningen pr. måned viser, hvornår hotellet er fyldt (marts) og tomt (sommer), så bemanding og vedligeholdelse kan planlægges efter det.
- **Pris og overbooking:** Annullering efter lead time og segment viser, hvor risikoen for tomme værelser er størst, og kan bruges til priser og depositumregler.
- **Beslutninger med forbehold:** Hver graf siger, hvad den ikke kan sige, så en leder ikke tager en sammenhæng for en årsag.
- **Driftsomkostning ved AI:** Valget af phi4 betyder, at hotellet skal have en GPU, eller leve med lang ventetid på CPU, hvis AI-opsummeringerne skal køre lokalt.
- **Datakvalitet som resultat:** At 99,6 % af landene er ukendte og 794 bookinger har prisen 0 er et konkret råd til dem, der registrerer bookinger.
