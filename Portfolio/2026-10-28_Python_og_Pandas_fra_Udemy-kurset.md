# Python og Pandas fra Udemy-kurset

**Dato:** 28/10 2026
**Læringsmål dækket:** [Dataanalyse og databehandling](https://tirsvad.studiesites.dk/laeringsmaal-dataanalyse-og-databehandling/) og [AI i softwareprojekter](https://tirsvad.studiesites.dk/laeringsmal-ai-til-softwarelosninger/)

Begge læringsmål bygger på Python. Denne post er beviset for, at jeg har arbejdet med Python og Pandas gennem Udemy-kurset *100 Days of Code™: The Complete Python Pro Bootcamp*. Beviset er repositoryet `Tirsvad-Udemy-100-days-of-code`. Kurset er ikke færdigt: jeg er nået til dag 41, og Matplotlib er endnu ikke brugt, så den del af læringsmålet er ikke afkrydset.

## 🧭 Hvad repositoryet indeholder

Hver dag i kurset er et selvstændigt projekt i en mappe, nummereret fra `001` til `041`. De dækker blandt andet:

| Emne | Eksempler på projekter |
|---|---|
| Grundlæggende Python: variabler, funktioner, løkker, betingelser | `001-band-name-generator`, `002-tip-calculator`, `005-py-password-generator`, `012-guess-the-number` |
| Spil og logik | `003-treasure-island`, `007-hangman`, `011-black-jack`, `014-higher-lower` |
| Objektorienteret programmering | `015-coffee-machine`, `016-oop-coffee-machine`, `020-snake-game`, `022-pong-game` |
| Filer og data | `024-mail-merge`, `029-password-manager`, `031-flash-card` |
| **Pandas og CSV-data** | `025-squirrel`, `025-us-states-game`, `025-weather` |
| API'er og webdata | `033-iss-location`, `035-rain-alert`, `036-stocknews`, `038-nutritionix` |

## 📊 Pandas i praksis

Pandas blev brugt i tre projekter fra dag 25:

- **`025-weather`:** CSV-filen med vejrdata blev læst ind i en `DataFrame` med `pandas.read_csv`, konverteret til en dictionary og en liste, og jeg beregnede gennemsnits- og maksimumstemperatur samt udvalgte rækker. Pandas-delen ligger i ét modul (`analysis.py`) og er en valgfri afhængighed.
- **`025-squirrel`:** Pandas er afhængighed i projektet, som arbejder med en CSV-fil med egernoptællinger (`squirrel_count.csv`).
- **`025-us-states-game`:** Pandas bruges til at gemme og læse data i spillets lager.

## 🔄 Kolbs læringscirkel i praksis

**1. Konkret erfaring**

Jeg løste kursets opgaver dag for dag og lagde hver i sit eget projekt, med struktur, dokumentation og afhængigheder.

**2. Refleksion**

- Hvad lærte jeg af at læse en CSV-fil med Pandas?
  > At en hel tabel kan indlæses i én linje, og at beregninger som gennemsnit og maksimum er korte, når data ligger i en `DataFrame`.
- Hvad mangler?
  > Matplotlib og de senere dage i kurset, hvor Pandas bruges til egentlig analyse og visualisering. Det er først dér, jeg kan dokumentere visualiseringer af data.
- Hvad kan jeg bruge det til?
  > Til at indlæse, undersøge og rense bookingsdata, før de analyseres og vises.

**3. Abstrakt begrebsliggørelse**

Jeg kobler erfaringen til teori om blandt andet:

- tabelbaserede data (`DataFrame`) og kolonner
- læsning af CSV-filer
- gennemsnit, maksimum og udvælgelse af rækker
- adskillelse af ansvar: Pandas ligger i ét modul, resten af programmet er uafhængigt

**4. Aktiv eksperimenteren**

Jeg fortsætter kurset til Matplotlib og bruger Pandas på hotelbookingsdata.

## 🎯 Hvilke kernemål i læringsmål dækkes

🟢 dækkes helt, 🟡 dækkes delvist, 🔴 dækkes kun lidt eller slet ikke endnu.

### Dataanalyse og databehandling

| Kerneområde | Vægt i læringsmål | Dækning | Begrundelse |
|---|---|:---:|---|
| Dataindsamling | Stor | 🟡 | CSV-filer blev indlæst med Pandas |
| Datastrukturering | Stor | 🟡 | Data blev lagt i en `DataFrame` og konverteret til dictionary og liste |
| Datakvalitet | Stor | 🔴 | Ikke relevant for denne post |
| Datarensning | Stor | 🔴 | Ikke relevant for denne post |
| Dataanalyse | Stor | 🟡 | Enkle beregninger og udvælgelse af rækker |
| Statistik | Stor | 🔴 | Kun gennemsnit og maksimum |
| Deskriptiv statistik | Stor | 🟡 | Gennemsnit og maksimum for temperatur |
| Trends og mønstre | Stor | 🔴 | Ikke relevant for denne post |
| Sammenhænge mellem variable | Stor | 🔴 | Ikke relevant for denne post |
| Datavisualisering | Stor | 🔴 | Matplotlib er ikke brugt endnu |
| Fortolkning af resultater | Mindre | 🔴 | Ikke relevant for denne post |
| Formidling af data | Mindre | 🔴 | Ikke relevant for denne post |

### AI i softwareprojekter

| Kerneområde | Vægt i læringsmål | Dækning | Begrundelse |
|---|---|:---:|---|
| Python for AI | Stor | 🟡 | Python-grundlaget er på plads, men selve Python-for-AI-kurset er ikke påbegyndt |
| Machine Learning | Stor | 🔴 | Ikke relevant for denne post |
| AI til fortolkning af data | Stor | 🔴 | Ikke relevant for denne post |
| Large Language Models (LLM) | Stor | 🔴 | Ikke relevant for denne post |
| Modelvalg og model comparison | Stor | 🔴 | Ikke relevant for denne post |
| Prompt engineering | Stor | 🔴 | Ikke relevant for denne post |
| Generativ AI | Stor | 🔴 | Ikke relevant for denne post |
| AI-baseret beslutningsstøtte | Stor | 🔴 | Ikke relevant for denne post |
| OCR | Stor | 🔴 | Ikke relevant for denne post |
| Feature extraction | Stor | 🔴 | Ikke relevant for denne post |
| Fortolkning af hoteldata | Mindre | 🔴 | Ikke relevant for denne post |
| Test og evaluering af AI-output | Mindre | 🔴 | Ikke relevant for denne post |
| Fejlhåndtering og usikkerhed | Mindre | 🔴 | Ikke relevant for denne post |
| Human-in-the-loop | Mindre | 🔴 | Ikke relevant for denne post |
| Privacy og ansvarlig AI | Mindre | 🔴 | Ikke relevant for denne post |

## 🏨 Hvilken værdi kan det give et hotel management-system?

- **Grundlag for dataanalysen:** Indlæsning af CSV-filer, udvælgelse af rækker og enkle beregninger er byggestenene i analysen af hotelbookingsdata.
- **Overskuelig kode:** At holde Pandas i ét modul gør det lettere at udskifte eller teste databehandlingen i NF Hotels analyseservice.
- **Fundament for AI-arbejdet:** Python-færdighederne bruges til benchmark, dataopsummering og senere integration af AI-funktioner i hotelsystemet.
