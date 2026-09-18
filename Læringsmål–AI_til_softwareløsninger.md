# Læringsmål – AI til softwareløsninger

*Del af 30 ECTS-projekt, 26/8–6/12 2026. Se den fælles [Projektplan – Ugeplan.md](Projektplan%20-%20Ugeplan.md) for tidsplan og timefordeling.*

## 🎯 Mål

Jeg vil opnå praktisk kompetence i at anvende AI til fortolkning af hoteldata og udvikle AI-baserede funktioner, som kan understøtte hotellets beslutninger.

Mit fokus er at forstå, hvordan forskellige AI-teknologier og LLM'er kan anvendes til at fortolke data, samt hvordan jeg vælger den AI-model eller teknologi, der passer bedst til en konkret problemstilling.

Som en del af projektet vil jeg desuden undersøge og anvende Machine Learning til OCR-behandling af pas, så relevante oplysninger som pasnummer, navn og nationalitet automatisk kan identificeres fra et pasbillede.

Jeg vil som grundlag for arbejdet gennemføre de relevante dele af et Python-for-AI-kursus med fokus på:

- Python
- LLM (rapportgenerering med visuelle modeller og konklusion for forbedringer)
- Machine Learning (lagring af pasinformationer)

Fokus er dermed på at forstå, vælge, anvende og evaluere AI-teknologier – ikke på at udvikle en komplet kommerciel AI-løsning.

### Jeg vil kunne – med Bloom-niveau

| # | Jeg vil kunne | Bloom-niveau |
|---|---|---|
| 1 | identificere hvor AI kan skabe værdi i hotelprojektet | Analysere |
| 2 | vælge og begrunde valg af relevante LLM'er og AI-modeller | Vurdere |
| 3 | sammenligne forskellige LLM'er ud fra kriterier som kvalitet, hastighed, pris, privacy og anvendelighed | Analysere |
| 4 | anvende LLM'er til fortolkning af strukturerede og ustrukturerede hoteldata | Anvende |
| 5 | formulere prompts, der giver brugbare og reproducerbare resultater | Skabe |
| 6 | anvende AI til at identificere mønstre, sammenhænge og mulige forklaringer i hoteldata | Analysere |
| 7 | vurdere AI's fortolkninger kritisk og sammenholde dem med de faktiske data | Vurdere |
| 8 | undersøge Machine Learning til OCR-behandling af pas | Forstå/Analysere |
| 9 | udvikle eller integrere en OCR-løsning, der kan identificere pasnummer, navn og nationalitet | Skabe |
| 10 | teste AI-løsningernes nøjagtighed og håndtere fejl og usikkerhed | Analysere/Vurdere |
| 11 | vurdere hvornår AI-output kræver menneskelig kontrol | Vurdere |
| 12 | dokumentere mine valg, eksperimenter, resultater og refleksioner | Forstå/Anvende |

Niveauet spænder bevidst fra analysere til skabe, så ambitionen matcher et 30 ECTS-forløb frem for et rent gengivelses- eller forståelsesniveau.

## 📚 Kerneområder

**I større grad:**
Python for AI · Machine Learning · AI til fortolkning af data · Large Language Models (LLM) · Modelvalg og model comparison · Prompt engineering · Generativ AI · AI-baseret beslutningsstøtte · OCR · Feature extraction

**I mindre grad:**
Fortolkning af hoteldata (delt med Læringsmål 2) · Test og evaluering af AI-output · Fejlhåndtering og usikkerhed · Human-in-the-loop · Privacy og ansvarlig AI

Dette læringsmål bærer hovedvægten af kerneområderne **AI & Machine Learning** i projektet, med **Programmering** som understøttende (mindre) kerneområde via kursus og implementering.

## 📊 Målbare succeskriterier

Jeg betragter læringsmålet som opnået, når jeg kan dokumentere:

**1. Python-for-AI-kursus**
Jeg gennemfører de relevante dele af et Python-for-AI-kursus med fokus på Python, Pandas, NumPy, Matplotlib og Machine Learning, og dokumenterer hvordan læringen anvendes i de efterfølgende AI-eksperimenter og i hotelprojektet.

**2. Valg af AI-model**
Jeg undersøger mindst 3 relevante LLM'er eller AI-modeller til projektets problemstillinger. For hver model dokumenterer jeg: hvad den kan anvendes til, styrker/begrænsninger, kvalitet af output, hastighed, ressourceforbrug, privacy/datahåndtering, og hvorfor den er/ikke er relevant. Jeg vælger mindst én model og begrunder valget ud fra konkrete testresultater.

**3. AI til fortolkning af hoteldata**
Jeg anvender en LLM eller anden AI-model til at fortolke hoteldata, fx til at identificere mønstre i belægningen, usædvanlige perioder, sammenhænge mellem faktorer, effekten af events/sæsoner, mulige forklaringer på ændringer i efterspørgslen og mulige forbedringer af hotellets marketing. Jeg sammenholder AI'ens fortolkning med de faktiske data og dokumenterer, hvor AI'en giver en korrekt, usikker eller forkert fortolkning.

**4. Prompting og AI-eksperimenter**
Jeg udvikler mindst 3 forskellige prompts eller promptstrategier til fortolkning af hoteldata og dokumenterer prompt, inputdata, AI-output, ændringer i prompten, forskelle i resultater og min vurdering af resultatets kvalitet.

**5. Machine Learning til OCR**
Jeg undersøger, hvordan Machine Learning og OCR kan anvendes til automatisk behandling af pasbilleder. Løsningen skal kunne identificere mindst pasnummer, navn og nationalitet. Jeg dokumenterer, hvordan data bevæger sig fra: Pasbillede → OCR/ML → tekst → strukturerede pasoplysninger.

**6. Test og evaluering**
Jeg gennemfører mindst 10 dokumenterede testcases fordelt på AI-funktionerne og registrerer input, forventet resultat, faktisk resultat, fejl/usikkerhed, hvordan fejlen håndteres, og om menneskelig kontrol er nødvendig.

## 🚀 Milestones (se ugeplan for datoer)

| Milestone | Uge | Indhold |
|---|---|---|
| M1 – Afprøvning af LLM-modeller | Uge 1–3 (26/8–9/9) | Identificér ≥3 LLM'er, afprøv på mindre datamængde, sammenlign kvalitet/hastighed/ressourceforbrug/anvendelighed, vælg model(ler) |
| M2 – Første LLM-eksperimenter | Uge 4–8 (16/9–14/10) | Systematiske eksperimenter med ≥3 promptstrategier, identificér mønstre/sammenhænge/årsager, udarbejd AI-baserede marketingkonklusioner |
| M3 – Implementering i NF Hotel | Uge 9–10 (21/10–28/10) | Integrér valgt AI-model med hoteldata i NF Hotel, præsentér AI-fortolkning som beslutningsstøtte |
| M4 – OCR/ML | Uge 11–13 (4/11–18/11) | Afprøv OCR/ML-teknologi på testbilleder, identificér pasnummer/navn/nationalitet, dokumentér nøjagtighed/fejl/begrænsninger, vurdér integration i NF Hotel |
| Aflevering | Uge 15 (2/12–6/12) | Samlet konklusion, SMART-tjek, portfolio |

## 🔄 Læring gennem Kolbs læringscirkel

**1. Konkret erfaring**
Jeg gennemfører Python-for-AI-kurset og eksperimenterer derefter med LLM'er, prompts og OCR/ML-teknologier på konkrete problemstillinger fra hotelprojektet.

**2. Refleksion**
Jeg dokumenterer: hvad der fungerede, hvad der ikke fungerede, forskelle mellem modeller, fejl i AI'ens fortolkninger, fejl i OCR-resultater, hvordan jeg vurderede kvaliteten.

**3. Abstrakt begrebsliggørelse**
Jeg kobler erfaringerne til teori om: Python for AI, LLM'er, Machine Learning, OCR, Computer Vision, prompting, model selection, AI-evaluering, hallucinationer og usikkerhed, human-in-the-loop.

**4. Aktiv eksperimenteren**
Jeg bruger mine erfaringer til at ændre model, prompt eller metode og gennemfører nye eksperimenter.

Eksperiment → refleksion → teori → forbedring → nyt eksperiment

## 🗂️ Bevis / portfolio

- Dokumentation fra relevante dele af Python-for-AI-kurset
- Sammenligning af mindst 3 AI-modeller/LLM'er
- Begrundelse for valg af model
- AI-fortolkning af hoteldata
- Mindst 3 promptstrategier
- AI-baserede konklusioner om mulige marketingforbedringer
- Integration af AI-fortolkning i NF Hotel
- ML/OCR-prototype til pasinformation
- Mindst 10 dokumenterede testcases
- Eksempler på fejl og usikkerhed
- Mine egne vurderinger af AI-output
- Refleksioner gennem Kolbs læringscirkel
- Konklusion på AI-teknologiernes anvendelighed

## ✅ SMART-tjek

### 🎯 S – Specifikt
🎯 **Måltavle:** Jeg vil udvikle mine kompetencer inden for AI ved at anvende LLM'er og Machine Learning på konkrete problemstillinger i NF Hotel, med fokus på AI-baseret fortolkning af hoteldata, rapportgenerering og OCR-behandling af pasinformation.
📍 **Placeringsnål:** Målet er placeret præcist ved skæringspunktet mellem modelvalg, prompt engineering og OCR/ML til pasdata – ikke bred AI-udvikling generelt.

### 📊 M – Målbart
📊 **Søjlediagram:** Sammenligning af ≥3 AI-modeller/LLM'er på tværs af kvalitet, hastighed, ressourceforbrug og privacy.  
📈 **Stigende kurve:** ≥3 promptstrategier med dokumenterede forbedringer mellem iterationer.  
📏 **Lineal:** ≥1 AI-baseret analyse/rapport af hoteldata, ≥1 OCR/ML-prototype til pasnummer/navn/nationalitet, ≥10 dokumenterede testcases med fejl/usikkerhed og behov for menneskelig kontrol.  

### 🤝 A – Attraktivt/Opnåeligt
🤝 **Håndtryk:** Læringsmålet tager udgangspunkt i eksisterende teknologi og data fra NF Hotel – jeg afgrænser arbejdet til at undersøge, udvikle og evaluere AI-baserede funktioner frem for at bygge en komplet kommerciel AI-platform.  
💪 **Spændt biceps:** De 8 ugentlige programmeringstimer og 26 ugentlige lærings-/portfolio-timer giver realistisk tid til kursus, eksperimenter og dokumentation inden for de 15 uger.  
✅ **Flueben:** Hvert milestone har konkrete, afkrydsbare leverancer (se milestone-tabel og portfolio-liste).  

### ⚖️ R – Relevant
⚖️ **Vægt:** Læringsmålet balancerer teoretisk forståelse af AI-teknologier med praktisk anvendelse på reelle hoteldata.  
🔑 **Nøgle:** Det låser op for kompetencer inden for AI i softwareudvikling – valg, anvendelse og evaluering af AI-teknologier på reelle data – som er centrale for projektets AI-kerneområde.  

### ⏱️ T – Tidsbestemt
⏱️ **Stopur:** 26/8–6/12 2026, milestone hver uge (se ugeplan).  
📅 **Kalender:** M1 uge 1–3, M2 uge 4–8, M3 uge 9–10, M4 uge 11–13, aflevering uge 15.  
⏳ **Timeglas:** Ved eksamen afgøres det, om læringsmålet er opnået, ud fra om jeg kan dokumentere mine AI-eksperimenter, begrunde mine teknologivalg, evaluere resultaterne kritisk og anvende mindst én AI-baseret funktion i NF Hotel.
