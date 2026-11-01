# Projektplan – uge for uge

**Periode:** onsdag 26. august 2026 – søndag 6. december 2026 (15 uger, milestone hver uge)
**Kerneområder i projektet (samlet over begge læringsmål):**

| Kerneområde | Vægt | Dækkes primært af |
|---|---|---|
| AI & Machine Learning | Stor | Læringsmål 1 |
| Dataanalyse & databehandling | Stor | Læringsmål 2 |
| Programmering / softwareudvikling | Mindre | Begge (Python, NF Hotel-integration, OCR-kode) |
| Formidling & dokumentation | Mindre | Begge (portfolio, rapportering, beslutningsstøtte) |

→ Opfylder kravet om mindst 3 kerneområder, heraf 2 i større grad og 1-2 i mindre grad.

## Fordeling af ECTS og timer

30 ECTS over 15 uger à 40 timer = 600 timer, dvs. 20 timer pr. ECTS.

| Læringsmål | ECTS | Andel | Timer i alt | Timer/uge (af 40) |
|---|---:|---:|---:|---:|
| 1 – AI til softwareløsninger | 18 | 60 % | 360 t | 24 t |
| 2 – Dataanalyse og databehandling | 12 | 40 % | 240 t | 16 t |
| **Samlet** | **30** | **100 %** | **600 t** | **40 t** |

Fordelingen gælder alle aktiviteter i tabellen nedenfor (kode, vejledning, teammøde, læring og portfolio), og fælles aktiviteter, der gavner begge spor (fx projektanalyse, lab, artefakt-framework, omstillingsparathed), fordeles efter samme 60/40.

## Ugentlig timefordeling (40 t/uge, gælder alle 15 uger)

| Aktivitet | Timer/uge | Formål |
|---|---|---|
| Programmering i projekter | 8 t | Kode: LLM-integration, prompt-eksperimenter, OCR/ML, databehandlingsscripts, NF Hotel-integration |
| Vejledning af lektorer | 2 t | Statusfremlæggelse og feedback på ugens milestone |
| Team møde | 4 t | Koordinering, deling af fund mellem AI-spor og data-spor |
| Læring (Kolb) og portfolio | 26 t | Kursus (100 Days of Code uge 1-3, Python-for-AI fra uge 4), refleksion, teori, dokumentation af portfolio |

Planen justeres løbende efter vejledning og efter hvilken ny viden/færdighed et givet milestone viser er nødvendig — datoerne herunder er derfor et styringsredskab, ikke en spændetrøje.

## Fælles 15-ugers milestone-plan

Begge læringsmål køres parallelt. Hver uge har ét primært fokus, men de 40 timer fordeles stadig efter tabellen ovenfor hver uge.

| Uge | Dato | Fælles / kursus | Læringsmål 1 – AI/OCR | Læringsmål 2 – Dataanalyse | Færdig |
|---|---|---|---|---|---|
| 1 | 26/8 | **Projektanalyse:** analysér projektet, find værdiskabende opgaver fra PO og prioritér dem. Genopfrisk Python med *100 Days of Code™: The Complete Python Pro Bootcamp* (dækker også Pandas og Matplotlib) | Identificér mindst 3 kandidat-LLM'er (ud fra prioriterede PO-opgaver) | **M1+M2 (Data):** domæneforståelse af projektet (indgår i fælles projektanalyse); opstart på Python (100 Days of Code – dækker også Pandas og Matplotlib) | 🟡 Delvist – datasæt fundet (40.060 bookinger, 25 variable, `data/nf_hotel_bookings.csv`). Kandidat-LLM'er identificeret og afprøvet: senere benchmark af 5 lokale modeller (se uge 2). 100 Days of Code er nået til dag 41 af 100 (bevispost 28/10). Mangler: kilde til datasæt dokumenteret, 100 Days of Code færdiggjort |
| 2 | 2/9 | Fortsæt projektanalyse og prioritering af PO-opgaver. Fortsæt 100 Days of Code | Afprøv de 3 LLM'er på en mindre mængde hoteldata | **M1 (Data) afslut:** domæneforståelse af projektet | 🟡 Delvist – 3 datakvalitetsproblemer findes i data (7.220 dubletter, urealistiske værdier som 55 voksne, 13 bookinger uden gæster) og håndteres i `DataCleaningService`. LLM-test gennemført: 4 kørsler (`docs/python-ai/ai-test-svar/descriptive-analysis-001..004.md`) af qwen3.8-27b (lokalt) og claude-sonnet-5 (sky, manuel – endnu ikke koblet på appens `LLM_BASE_URL`) på den deskriptive statistik. Fundet undervejs: qwen3's "tænke"-tekst bruger et andet markørformat (`__LM_STUDIO_INTERNAL_LSEP_..._END_...__`) end det `<think>...</think>`-mønster, som `LLMReportService._strip_thinking` leder efter – rå ræsonnement ville derfor lække urenset ud i 3 af de 4 svar. Senere (pr. 28/10): benchmark af 5 lokale modeller (`phi4`, `phi4-reasoning:plus`, `gemma4:e2b`, Whittle-Qwen3.8-MoE-27B, `qwen3-coder-next`), 135 kørsler på et syntetisk datasæt med 3.000 rækker, dokumenteret i portfolio (27/9 og bevispost 28/10). 3. LLM-kandidat er dermed dækket. Mangler: tests på rigtige NF Hotel-data |
| 3 | 9/9 | Afslut/konsolidér 100 Days of Code | **M1 (AI):** sammenlign kvalitet/hastighed/pris/privacy, vælg model(ler) | **M2 (Data) afslut:** opstart på Python, Pandas og Matplotlib (100 Days of Code fortsat – ikke færdiggjort) | 🟡 Delvist – datarensning implementeret og testet. Model­sammenligning delvist i gang på baggrund af de 4 testsvar: **hastighed** – qwen 220–378 s, faldt markant da prompten fik en eksplicit "svar uden at stille spørgsmål, i markdown"-instruks (før det: 1+ time); claude ikke tidsmålt endnu (kørt manuelt, ikke gennem pipelinen). **Kvalitet** – claude's svar er struktureret og flagger selv datakvalitetsproblemer (fx `adults`=0, outliers, `agent` som ID); qwens svar er indholdsrige, men 3 af 4 har urenset ræsonnement-tekst i outputtet (se uge 2). **Privacy** – qwen kører selvhostet/lokalt, claude er cloud. **Pris** – ikke sammenlignet endnu. Pr. 28/10 er sammenligningen af 5 modeller dokumenteret med hastighed (median tokens/s fra 3,8 til 85,8), RAM/VRAM, gyldig JSON og fejl; alle modeller kører lokalt (privacy). Modelvalg truffet 28/10: **phi4**. Mangler: bevispost med begrundelse for valget, pris-sammenligning og kontrol af valget på rigtige NF Hotel-data og sammenligning af opsummeringer (MIL-007) |
| 4 | 16/9 | **Opstart Python-for-AI-kursus** (Udemy) | Design 3 forskellige promptstrategier | **M3 (Data) start:** find/opret historisk hoteldatasæt, dokumentér variable og kilde | 🟡 Delvist – gennemsnit, median, min/maks beregnes via `describe()`. Mangler: 2 visualiseringer, 3 promptstrategier (benchmarken bruger kun én prompt, `hotel-cancellation-v1`), Python-for-AI-kurset (ingen spor i projekterne endnu) |
| 5 | 23/9 | **Værktøjsvalg og prompt-læring:** Jupyter til lokal visualisering, benchmark af lokal AI og AI-prompts, der rammer kriterierne (portfolio 22/9 og 27/9) | **M2 (AI) start:** kør første systematiske prompt-eksperimenter på hoteldata | **M3 (Data) afslut:** identificér mindst 3 datakvalitetsproblemer | 🟡 Delvist – kvartiler og standardafvigelse er allerede med i `describe()`. Mangler: systematiske prompt-eksperimenter |
| 6 | 30/9 | | Sammenlign prompt-resultater, identificér mønstre/sammenhænge | **M4 (Data) start:** rens data baseret på uge 5's fund | ⬜ Ikke startet |
| 7 | 7/10 | **Omstillingsparathed:** ny opgave fra anden PO (Excel-bog → VBA, 56 ark) løst med AI og projektplanlægning (portfolio 9/10) | Identificér mulige årsager til ændringer i efterspørgsel | **M4 (Data) afslut:** beregn gennemsnit/median/min/maks; 2 indledende visualiseringer | 🟡 Delvist – fælles opgave udført (omstillingsparathed, portfolio 9/10). Milepælens eget indhold er ikke dokumenteret |
| 8 | 14/10 | | **M2 (AI) afslut:** AI-baserede konklusioner om marketingforbedringer | **M5 (Data):** udvid til mindst 4 statistiske mål (kvartiler, standardafvigelse); midtvejsrefleksion (Kolb) på tværs af begge spor | ⬜ Ikke startet |
| 9 | 21/10 | | Forbered integration: definér snitflade til NF Hotel | **M6 (Data) start:** identificér mindst 3 foreløbige trends/mønstre | 🟡 Delvist – REST-snitflade er de facto defineret (`/report/from-file`, `/report/from-json`, API-nøgle). Mangler: afstemning med NF Hotel, visualisering nr. 4, trends |
| 10 | 28/10 | **Perspektivering:** ensartede artefakter (template, scripts, kvalitetstjekliste) set i lyset af erfaringer fra LEGO-koncernen via Trines praktik (portfolio 28/10). Læringsmålene omskrevet til viden, kunnen og kompetencer | **M3 (AI):** implementér AI-fortolkning i NF Hotel | **M6 (Data) fortsat:** understøt trends med beregning/visualisering nr. 3 | 🟡 Delvist – AI-fortolkning findes som selvstændig API-tjeneste. Ikke verificeret integreret i NF Hotel |
| 11 | 4/11 | | **M4 (AI) start:** afprøv OCR/ML-teknologi på pasbilleder | **M6 (Data) fortsat:** udvid til 5 identificerede trends/mønstre, visualisering nr. 4 | ⬜ Ikke startet |
| 12 | 11/11 | | Test OCR/ML-nøjagtighed på flere testbilleder | **M6 (Data) afslut:** kvalitetssikring af visualiseringer og beregninger | ⬜ Ikke startet |
| 13 | 18/11 | | **M4 (AI) afslut:** min. 10 dokumenterede testcases på tværs af AI-funktioner | **M7 (Data):** samlet fortolkning – hvad data kan/ikke kan fortælle, og analysens begrænsninger | ⬜ Ikke startet |
| 14 | 25/11 | | Færdiggør dokumentation og tekniske valg | **M8 (Data):** samlet konklusion på analysen; sidste kvalitetstjek af portfolio-materiale | ⬜ Ikke startet |
| 15 | 2/12–6/12 | | **Aflevering:** SMART-tjek, samlet konklusion, portfolio | **Aflevering:** SMART-tjek, samlet konklusion, portfolio | ⬜ Ikke startet |

**Færdig-kolonnen** (status pr. 28/10 2026, vurderet ud fra portfolioen og Python-projekterne `Other.NFHotelDataanalysis`, `notebook-ai-benchmark`, `notebook-market-analysis` og `Tirsvad-Udemy-100-days-of-code`): 🟢 færdig og dokumenteret · 🟡 delvist – ofte udført i kode, men endnu ikke dokumenteret i portfolioen · 🔴 forfalden, men hverken i kode eller portfolio · ⬜ endnu ikke startet. Portfolioposterne om lab, teknologivalg, IDE og artefakt-færdighed hører ikke til et bestemt milestone i planen og er derfor ikke talt med. Uge 1–5 og 7 er opdateret efter gennemgangen af projekterne 28/10; uge 6 og 8–15 er ikke vurderet på ny. I `notebook-market-analysis` er kun `/health` og helligdagskalenderen bygget; de ni analyser og AI-opsummeringerne er planlagt (MIL-001), og uge 9–10 er derfor ikke opgraderet. Ingen milepæle er 🟢, fordi flere mangler (modelvalg, 3 promptstrategier, visualiseringer, Python-for-AI-kurset).

Se de to læringsmåls egne dokumenter for detaljerede succeskriterier bag hvert milestone:
- [Læringsmål – AI til softwareløsninger.md](Læringsmål–AI_til_softwareløsninger.md) (18 ECTS)
- [Læringsmål – Dataanalyse og databehandling.md](Læringsmål–Dataanalyse_og_databehandling.md) (12 ECTS)
