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
| 1 | 26/8 | **Projektanalyse:** analysér projektet, find værdiskabende opgaver fra PO og prioritér dem. Genopfrisk Python med *100 Days of Code™: The Complete Python Pro Bootcamp* (dækker også Pandas og Matplotlib) | Identificér mindst 3 kandidat-LLM'er (ud fra prioriterede PO-opgaver) | Find/opret historisk hoteldatasæt, dokumentér variable og kilde | 🟡 Delvist – datasæt fundet (40.060 bookinger, 25 variable, `data/nf_hotel_bookings.csv`). 2 af 3 kandidat-LLM'er nu afprøvet (qwen3.8-27b lokalt, claude-sonnet-5 i sky), en 3. mangler. Mangler desuden: kilde til datasæt dokumenteret, 100 Days of Code, portfolio-post |
| 2 | 2/9 | Fortsæt projektanalyse og prioritering af PO-opgaver. Fortsæt 100 Days of Code | Afprøv de 3 LLM'er på en mindre mængde hoteldata | **M1 (Data):** identificér mindst 3 datakvalitetsproblemer | 🟡 Delvist – 3 datakvalitetsproblemer findes i data (7.220 dubletter, urealistiske værdier som 55 voksne, 13 bookinger uden gæster) og håndteres i `DataCleaningService`. LLM-test gennemført: 4 kørsler (`docs/python-ai/ai-test-svar/descriptive-analysis-001..004.md`) af qwen3.8-27b (lokalt) og claude-sonnet-5 (sky, manuel – endnu ikke koblet på appens `LLM_BASE_URL`) på den deskriptive statistik. Fundet undervejs: qwen3's "tænke"-tekst bruger et andet markørformat (`__LM_STUDIO_INTERNAL_LSEP_..._END_...__`) end det `<think>...</think>`-mønster, som `LLMReportService._strip_thinking` leder efter – rå ræsonnement ville derfor lække urenset ud i 3 af de 4 svar. Mangler: 3. LLM-kandidat, portfolio-post |
| 3 | 9/9 | Afslut/konsolidér 100 Days of Code | **M1 (AI):** sammenlign kvalitet/hastighed/pris/privacy, vælg model(ler) | Fortsæt datarensning baseret på uge 2's fund | 🟡 Delvist – datarensning implementeret og testet. Model­sammenligning delvist i gang på baggrund af de 4 testsvar: **hastighed** – qwen 220–378 s, faldt markant da prompten fik en eksplicit "svar uden at stille spørgsmål, i markdown"-instruks (før det: 1+ time); claude ikke tidsmålt endnu (kørt manuelt, ikke gennem pipelinen). **Kvalitet** – claude's svar er struktureret og flagger selv datakvalitetsproblemer (fx `adults`=0, outliers, `agent` som ID); qwens svar er indholdsrige, men 3 af 4 har urenset ræsonnement-tekst i outputtet (se uge 2). **Privacy** – qwen kører selvhostet/lokalt, claude er cloud. **Pris** – ikke sammenlignet endnu. Mangler: endeligt modelvalg, pris-sammenligning, portfolio-post |
| 4 | 16/9 | **Opstart Python-for-AI-kursus** (Udemy) | Design 3 forskellige promptstrategier | **M2 (Data):** beregn gennemsnit, median, min/maks; 2 første visualiseringer | 🟡 Delvist – gennemsnit, median, min/maks beregnes via `describe()`. Mangler: 2 visualiseringer, 3 promptstrategier (kun 1 prompt), portfolio-post |
| 5 | 23/9 | | **M2 (AI) start:** kør første systematiske prompt-eksperimenter på hoteldata | Uddyb statistik: kvartiler, standardafvigelse (mod 4 mål i alt) | 🟡 Delvist – kvartiler og standardafvigelse er allerede med i `describe()`. Mangler: systematiske prompt-eksperimenter |
| 6 | 30/9 | | Sammenlign prompt-resultater, identificér mønstre/sammenhænge | **M3 (Data):** identificér mindst 3 foreløbige trends/mønstre | ⬜ Ikke startet |
| 7 | 7/10 | | Identificér mulige årsager til ændringer i efterspørgsel | Understøt trends med beregninger/visualisering nr. 3 | ⬜ Ikke startet |
| 8 | 14/10 | | **M2 (AI) afslut:** AI-baserede konklusioner om marketingforbedringer | Midtvejsrefleksion (Kolb) på tværs af begge spor | ⬜ Ikke startet |
| 9 | 21/10 | | Forbered integration: definér snitflade til NF Hotel | **M4 (Data):** udvid til 5 identificerede trends/mønstre, visualisering nr. 4 | 🟡 Delvist – REST-snitflade er de facto defineret (`/report/from-file`, `/report/from-json`, API-nøgle). Mangler: afstemning med NF Hotel, visualisering nr. 4, trends |
| 10 | 28/10 | | **M3 (AI):** implementér AI-fortolkning i NF Hotel | Kvalitetssikring af visualiseringer og beregninger | 🟡 Delvist – AI-fortolkning findes som selvstændig API-tjeneste. Ikke verificeret integreret i NF Hotel |
| 11 | 4/11 | | **M4 (AI) start:** afprøv OCR/ML-teknologi på pasbilleder | **M5 (Data):** samlet fortolkning – hvad data kan/ikke kan fortælle | ⬜ Ikke startet |
| 12 | 11/11 | | Test OCR/ML-nøjagtighed på flere testbilleder | Beskriv analysens begrænsninger | ⬜ Ikke startet |
| 13 | 18/11 | | **M4 (AI) afslut:** min. 10 dokumenterede testcases på tværs af AI-funktioner | Sidste kvalitetstjek af portfolio-materiale | ⬜ Ikke startet |
| 14 | 25/11 | | Færdiggør dokumentation og tekniske valg | **M6 (Data):** samlet konklusion på analysen | ⬜ Ikke startet |
| 15 | 2/12–6/12 | | **Aflevering:** SMART-tjek, samlet konklusion, portfolio | **Aflevering:** SMART-tjek, samlet konklusion, portfolio | ⬜ Ikke startet |

**Færdig-kolonnen** (status pr. 22/9 2026, vurderet ud fra portfolioen og Python-projektet `Other.NFHotelDataanalysis`): 🟢 færdig og dokumenteret · 🟡 delvist – ofte udført i kode, men endnu ikke dokumenteret i portfolioen · 🔴 forfalden, men hverken i kode eller portfolio · ⬜ endnu ikke startet. Portfolioposterne om lab, teknologivalg, IDE og artefakt-færdighed hører ikke til et bestemt milestone i planen og er derfor ikke talt med.

Se de to læringsmåls egne dokumenter for detaljerede succeskriterier bag hvert milestone:
- [Læringsmål – AI til hotelbelægning og prisforudsigelse.md](Læringsmål%20–%20AI%20til%20hotelbelægning%20og%20prisforudsigelse.md)
- [Læringsmål – Dataanalyse og databehandling.md](Læringsmål%20–%20Dataanalyse%20og%20databehandling.md)
