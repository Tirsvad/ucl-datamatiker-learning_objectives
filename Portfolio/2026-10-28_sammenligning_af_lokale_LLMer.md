# Sammenligning af mindst 3 lokale LLM'er

**Dato:** 28/10 2026
**Læringsmål dækket:** [AI i softwareprojekter](https://tirsvad.studiesites.dk/laeringsmal-ai-til-softwarelosninger/) og [Dataanalyse og databehandling](https://tirsvad.studiesites.dk/laeringsmaal-dataanalyse-og-databehandling/)

Læringsmålet for AI kræver, at jeg undersøger mindst 3 relevante LLM'er eller AI-modeller og dokumenterer kvalitet, hastighed, ressourceforbrug og privacy. Denne post er beviset for den del: en benchmark af fem lokale modeller, kørt i projektet `notebook-ai-benchmark`. Valget af den endelige model er ikke truffet endnu og er derfor ikke en del af dette bevis. Den proces er beskrevet i [Processen i at vælge – benchmark af lokal AI](https://tirsvad.studiesites.dk/processen-i-at-vaelge-benchmark-af-lokal-ai/).

## 🧭 Hvad blev målt

Benchmarken er en Marimo-notebook, der kører mod Ollama og LM Studio. Python beregner faktaene, og modellen fortolker dem. Der blev kørt to typer opgaver:

1. **Hotelanalyse:** modellen modtog en deterministisk opsummering af annulleringsstatistik (samlet, direkte kunder mod agentbookinger, opdelt på hotel, markedssegment, depositum og leveringstid) og skulle svare i en fast JSON-struktur. CSV-filen blev aldrig sendt til modellen. Datasættet var det syntetiske eksempeldatasæt med 3.000 rækker.
2. **Deterministiske opgaver:** fem korte prompts med automatisk bestået/ikke bestået (`math-1`, `logic-1`, `code-1`, `extract-1`, `summ-1`).

For hver forespørgsel blev der registreret TTFT, samlet tid, tokens pr. sekund, systemhukommelse og GPU-VRAM, cold/warm, gyldig JSON, afslutningsårsag og fejl. I alt blev der gemt 135 forespørgsler i `output/results.jsonl` (schema version 2).

## 📊 Resultater

| Model | Deterministiske opgaver bestået | Median tokens/s | Hotelanalyse med gyldig JSON | Fejl |
|---|:---:|---:|:---:|:---:|
| `phi4:latest` | 20 af 25 | 10,8 | 3 af 3 | 0 |
| `phi4-reasoning:plus` | 15 af 25 | 6,4 | 0 af 3 | 1 |
| `gemma4:e2b` | 20 af 25 | 85,8 | 3 af 3 | 0 |
| `Whittle/Qwen3.8-Whittle-MoE-27B` | 16 af 25 | 3,8 | 3 af 3 | 5 |
| `qwen3-coder-next:latest` | 0 af 20 | – | 0 af 3 | 23 |

I alt blev 71 af 120 deterministiske kørsler bestået.

Det, jeg læste ud af tallene:

- **Hastighed:** `gemma4:e2b` var klart hurtigst (median ca. 86 tokens/s) og svarede på hotelanalysen på 17–185 sekunder. Whittle-modellen brugte omkring 670–820 sekunder pr. hotelanalyse.
- **Kvalitet og pålidelighed:** `phi4-reasoning:plus` blev afbrudt af tokengrænsen (`finish_reason: length`) eller af timeouten på 600 sekunder og gav ingen gyldig JSON. `qwen3-coder-next` nåede aldrig et gyldigt svar i denne konfiguration. Fejl og timeouts er ikke fjernet fra resultaterne.
- **Ressourcer:** Systemhukommelsen og VRAM'en er målt for hele maskinen, ikke kun for modellen (psutil og `nvidia-smi`), så tallene er en øvre grænse. Spidsværdierne lå på op til ca. 64 GB systemhukommelse og ca. 7,8 GB VRAM.
- **Privacy:** Alle modeller kørte lokalt via Ollama, så hoteldata blev ikke sendt til en ekstern tjeneste.

Modellerne i checklisten i læringsmålet var `microsoft/phi-4`, `google/gemma-4-31b-qat`, `whittle-moe-27b-a18b` og `qwen3.8-27b`. Af dem er `phi4` og Whittle-modellen testet direkte. Gemma-modellen var en mindre variant (`gemma4:e2b`), og `qwen3.8-27b` er endnu ikke testet som selvstændig model. Derfor har jeg kun afkrydset de to første under evidens.

## 🔄 Kolbs læringscirkel i praksis

**1. Konkret erfaring**

Jeg byggede en benchmark, der kørte fem lokale modeller på samme prompt og samme data og gemte hver forespørgsel med målinger og svar.

**2. Refleksion**

- Hvad viste benchmarken, som jeg ikke havde forventet?
  > At en lille model (`gemma4:e2b`) både var hurtigst og leverede gyldigt svar hver gang, mens modeller, der virker stærke på papiret, gav timeouts eller ugyldig JSON.
- Hvad gik galt?
  > `phi4-reasoning:plus` og `qwen3-coder-next` gav ikke et brugbart svar på hotelanalysen. Det viser, at et svar, der er hurtigt, men ugyldigt, ikke kan bruges, og at en model skal måles på det faktiske formål.
- Hvad kan tallene ikke sige?
  > De måler hastighed, ressourcer og om svaret er gyldigt, ikke hvor god opsummeringen er. Derfor er næste skridt en sammenligning af selve opsummeringerne side om side.
- Hvad kan jeg gøre bedre?
  > Teste de to manglende modeller, køre flere gentagelser pr. model og bruge det rigtige NF Hotel-datasæt frem for det syntetiske.

**3. Abstrakt begrebsliggørelse**

Jeg kobler erfaringen til teori om blandt andet:

- benchmarking af LLM'er: TTFT, throughput, cold versus warm start
- deterministiske fakta fra Python versus fortolkning fra modellen
- strukturerede svar (JSON) og validering af output
- ressourcemåling (RAM og VRAM) og dens begrænsninger
- lokal versus cloudbaseret AI og privacy

**4. Aktiv eksperimenteren**

Jeg sammenligner opsummeringerne fra modellerne side om side (MIL-007), tester de to manglende modeller og kører benchmarken på NF Hotels rigtige data, før jeg vælger standardmodel.

## 🎯 Hvilke kernemål i læringsmål dækkes

🟢 dækkes helt, 🟡 dækkes delvist, 🔴 dækkes kun lidt eller slet ikke endnu.

### Dataanalyse og databehandling

| Kerneområde | Vægt i læringsmål | Dækning | Begrundelse |
|---|---|:---:|---|
| Dataindsamling | Stor | 🔴 | Datasættet var et færdigt syntetisk eksempel |
| Datastrukturering | Stor | 🟡 | Rækkerne blev grupperet pr. hotel, segment, depositum og leveringstid |
| Datakvalitet | Stor | 🟡 | Datasættet valideres ved indlæsning (manglende kolonner, ugyldige værdier) |
| Datarensning | Stor | 🔴 | Ikke relevant for denne post |
| Dataanalyse | Stor | 🟡 | Annulleringsstatistik blev beregnet deterministisk med Python |
| Statistik | Stor | 🔴 | Kun annulleringsrater, ikke et bredt udvalg af mål |
| Deskriptiv statistik | Stor | 🟡 | Annulleringsrater for direkte kunder og agentbookinger |
| Trends og mønstre | Stor | 🔴 | Mønstrene blev fundet af modellerne, ikke af min egen analyse |
| Sammenhænge mellem variable | Stor | 🔴 | Ikke undersøgt selvstændigt |
| Datavisualisering | Stor | 🟡 | Resultaterne blev vist med Altair i notebooken |
| Fortolkning af resultater | Mindre | 🟡 | Modellernes fortolkning blev stillet op mod de beregnede værdier |
| Formidling af data | Mindre | 🔴 | Ikke relevant for denne post |

### AI i softwareprojekter

| Kerneområde | Vægt i læringsmål | Dækning | Begrundelse |
|---|---|:---:|---|
| Python for AI | Stor | 🟡 | Python bruges til benchmark, målinger og dataopsummering |
| Machine Learning | Stor | 🔴 | Ikke relevant for denne post |
| AI til fortolkning af data | Stor | 🟡 | Modellerne fortolkede annulleringsstatistik |
| Large Language Models (LLM) | Stor | 🟢 | Fem LLM'er blev kørt og målt på samme opgave |
| Modelvalg og model comparison | Stor | 🟡 | Sammenligningen er gennemført, men endeligt modelvalg mangler |
| Prompt engineering | Stor | 🟡 | Én prompt (`hotel-cancellation-v1`) med fast JSON-format; endnu ikke 3 strategier |
| Generativ AI | Stor | 🔴 | Ikke relevant for denne post |
| AI-baseret beslutningsstøtte | Stor | 🔴 | Valg af standardmodel mangler |
| OCR | Stor | 🔴 | Ikke relevant for denne post |
| Feature extraction | Stor | 🔴 | Ikke relevant for denne post |
| Fortolkning af hoteldata | Mindre | 🟡 | Kun syntetiske data indtil videre |
| Test og evaluering af AI-output | Mindre | 🟡 | 120 deterministiske kørsler med automatisk kontrol og validering af JSON |
| Fejlhåndtering og usikkerhed | Mindre | 🟡 | Timeouts, afbrudte svar og ugyldig JSON er registreret og ikke skjult |
| Human-in-the-loop | Mindre | 🔴 | Ikke dokumenteret endnu |
| Privacy og ansvarlig AI | Mindre | 🟡 | Alle modeller kørte lokalt; CSV-filen blev ikke sendt til modellen |

## 🏨 Hvilken værdi kan det give et hotel management-system?

- **Evidensbaseret modelvalg:** NF Hotels markedsanalyse skal bruge en lokal model til at skrive indsigter. Benchmarken viser, hvilke modeller der faktisk leverer gyldige svar i en acceptabel tid, og hvilke der ikke gør.
- **Pålidelighed før kvalitet:** At to af fem modeller ikke gav brugbart svar viser, at en AI-funktion i hotelsystemet skal have timeouts, validering af output og en fejlmelding, der ikke skjules.
- **Data forbliver lokalt:** Kørsel via Ollama betyder, at hoteldata ikke forlader serveren, i tråd med de øvrige privacy-valg i projektet.
