# Processen i at vælge – Jupyter til at visualisere Python-output

**Dato:** 22/9 2026
**Læringsmål dækket:** [AI i softwareprojekter](https://tirsvad.studiesites.dk/laeringsmal-ai-til-softwarelosninger/) og [Dataanalyse og databehandling](https://tirsvad.studiesites.dk/laeringsmaal-dataanalyse-og-databehandling/)

Jeg manglede et værktøj til at visualisere output fra Python-kode. Kravet var, at det skulle kunne køre lokalt, så lokal AI kan benyttes. Jeg stødte oprindeligt på Jupyter gennem Python-kurset, men søgte alligevel på nettet efter alternativer. Jeg havde foreløbigt valgt Marimo, men endte tilbage ved Jupyter på grund af REPL. Denne post dokumenterer den valgproces.

## 🧭 Processen i at vælge

Fordi kravet om lokal kørsel var afgørende, blev Google Colab og andre skybaserede løsninger slet ikke overvejet nærmere.

| Værktøj | Rolle | Valgt/fravalgt fordi | Alternativ(er) overvejet |
|---|---|---|---|
| Google Colab og andre skybaserede løsninger | Notebook til at visualisere Python-output | Fravalgt uden videre overvejelse – gratis og skybaseret, men opfylder ikke kravet om lokal kørsel til lokal AI | – |
| Marimo | Notebook der kan git-versioneres og distribueres som kode | Fravalgt: kan ikke køre REPL, hvor tunge opgaver (fx AI-prompts) kan springes over, når de allerede er kørt én gang – det besværliggør debugging | Jupyter |
| Jupyter | Notebook til at visualisere Python-output, kører lokalt | Massivt økosystem med årevis af udvidelser, tutorials og native rendering-understøttelse på platforme som GitHub, samt understøttelse af REPL | Marimo, Google Colab |

## 🔄 Kolbs læringscirkel i praksis

**1. Konkret erfaring**

Jeg manglede et værktøj til at visualisere output fra Python-kode og skulle finde et, der kunne køre lokalt, så jeg kunne bruge lokal AI. Jeg stødte oprindeligt på Jupyter gennem Python-kurset, men søgte alligevel på nettet efter alternativer og endte med foreløbigt at vælge Marimo i stedet.

**2. Refleksion**

- Jeg kendte allerede Jupyter fra Python-kurset – hvorfor ledte jeg alligevel efter alternativer?
  > For at undersøge, om der fandtes et værktøj, der var bedre egnet til formålet, i stedet for bare at bruge det første værktøj, jeg var stødt på.
- Hvorfor blev cloud-baserede løsninger som Google Colab fravalgt uden videre overvejelse?
  > Fordi kravet om lokal kørsel (for at kunne bruge lokal AI) i sig selv udelukkede dem – der var ingen grund til at undersøge dem nærmere.
- Hvad talte for Marimo?
  > At det er nemmere at git-versionere og kan distribueres som almindelig kode.
- Hvorfor blev Marimo fravalgt alligevel?
  > Fordi det ikke kan køre REPL, hvor tunge opgaver (fx AI-prompts) kan springes over, når de allerede er kørt én gang – det gør debugging besværligt, når man arbejder med AI-kald.
- Hvorfor endte valget tilbage på Jupyter?
  > Fordi Marimos manglende REPL besværliggjorde debugging af tunge AI-kald. Det, kombineret med Jupyters massive økosystem (udvidelser, tutorials, native rendering på fx GitHub) opbygget over mange år, gjorde at jeg endte tilbage ved det værktøj, jeg allerede kendte fra Python-kurset.

**3. Abstrakt begrebsliggørelse**

Jeg kobler erfaringen til teori om blandt andet:

- notebook-arkitektur og cell-baseret eksekvering
- REPL versus reproducerbar/deterministisk kode-eksekvering
- git-versionering af notebooks
- økosystem-modenhed som valgkriterium
- lokal versus cloud-baseret AI

**4. Aktiv eksperimenteren**

Jeg bruger nu Jupyter til at visualisere output fra Python-kode og til at eksperimentere med lokal AI. Jeg holder øje med, om Marimo på sigt løser REPL-/caching-begrænsningen, og genbruger samme kriteriebaserede metode – krav først, alternativer, begrundet valg – når jeg senere skal vælge AI-modeller/LLM'er.

## 🎯 Hvilke kernemål i læringsmål dækkes

🟢 dækkes helt, 🟡 dækkes delvist, 🔴 dækkes kun lidt eller slet ikke endnu.

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
| Datavisualisering | Stor | 🟡 | Jupyter er valgt netop som værktøj til at visualisere output, men selve visualiseringerne er ikke lavet i denne post |
| Fortolkning af resultater | Mindre | 🔴 | Ikke relevant for denne post |
| Formidling af data | Mindre | 🔴 | Ikke relevant for denne post |

### AI i softwareprojekter

| Kerneområde | Vægt i læringsmål | Dækning | Begrundelse |
|---|---|:---:|---|
| Python for AI | Stor | 🟡 | Jupyter vælges som det værktøj, Python-for-AI-arbejdet skal foregå i |
| Machine Learning | Stor | 🔴 | Ikke relevant for denne post |
| AI til fortolkning af data | Stor | 🔴 | Ikke relevant for denne post |
| Large Language Models (LLM) | Stor | 🔴 | Ikke relevant for denne post |
| Modelvalg og model comparison | Stor | 🟡 | Samme kriterie- og alternativ-baserede metode (krav, alternativer, begrundet valg) er øvet her, klar til at genbruges på LLM-valg |
| Prompt engineering | Stor | 🔴 | Ikke relevant for denne post |
| Generativ AI | Stor | 🔴 | Ikke relevant for denne post |
| AI-baseret beslutningsstøtte | Stor | 🔴 | Ikke relevant for denne post |
| OCR | Stor | 🔴 | Ikke relevant for denne post |
| Feature extraction | Stor | 🔴 | Ikke relevant for denne post |
| Fortolkning af hoteldata | Mindre | 🔴 | Ikke relevant for denne post |
| Test og evaluering af AI-output | Mindre | 🔴 | Ikke relevant for denne post |
| Fejlhåndtering og usikkerhed | Mindre | 🟡 | REPL-understøttelse blev vurderet netop ud fra, hvor let det gør debugging af AI-kald |
| Human-in-the-loop | Mindre | 🔴 | Ikke relevant for denne post |
| Privacy og ansvarlig AI | Mindre | 🟡 | Kravet om lokal kørsel er et bevidst valg om at holde AI-arbejdet lokalt frem for i skyen |

## 🏨 Hvilken værdi kan det give et hotel management-system?

At kunne visualisere Python-output lokalt, sammen med lokal AI, understøtter arbejdet med hotelprojektet på flere måder:

- **Data forbliver lokalt:** Når AI og visualisering kører lokalt i stedet for i skyen, skal hoteldata og testdata ikke sendes til en ekstern tjeneste for at kunne udforskes – samme privacy-tankegang, som lå bag valget af selvhostet database og mailserver i labbet.
- **Lettere debugging af AI-kald:** Jupyters REPL gør det muligt at teste og fejlsøge tunge AI-kald (fx prompts mod en lokal model) trin for trin, uden at genkøre hele analysen fra bunden.
- **Modent økosystem:** Jupyters udvidelser og native rendering (fx på GitHub) gør det lettere at dele og genbruge analyser af hoteldata som en del af portfolioen.

Samlet set er valget af Jupyter endnu et eksempel på, at kravet om lokal, privacy-bevidst AI-arbejde går igen som et gennemgående kriterie i mine værktøjsvalg.
