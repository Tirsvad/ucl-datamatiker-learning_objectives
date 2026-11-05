# Perspektivering – ensartede artefakter efter besøg fra LEGO

**Dato:** 28/10 2026
**Læringsmål dækket:** [AI i softwareprojekter](https://tirsvad.studiesites.dk/laeringsmal-ai-til-softwarelosninger/) og [Dataanalyse og databehandling](https://tirsvad.studiesites.dk/laeringsmaal-dataanalyse-og-databehandling/)

Vi havde besøg af Trine, der har haft praktik hos LEGO-koncernen. Hun fortalte, at LEGO er i gang med at gøre deres artefakter ensartede. Det er netop det, jeg har arbejdet med det seneste semester, da jeg samlede mine artefakter i én artefakt-færdighed (se [Artefakt-færdighed – én samlet færdighed i stedet for 19](https://tirsvad.studiesites.dk/hvorfor-en-samlet-artefakt-faerdighed-til-en-gruppe-af-faerdigheder/)). Denne post perspektiverer mit valg og dokumenterer, hvad besøget bekræftede.

## 🧭 Perspektivering af valget om at ensarte artefakter

### Besøget bekræftede, at jeg ikke er alene

Da Trine fortalte fra sin praktik, at LEGO arbejder på at gøre deres artefakter ensartede, blev jeg bekræftet i, at synspunktet ikke kun er mit eget. Det styrker min tro på, at ensartede artefakter er en god vej at følge – også når det kræver en indsats at indføre.

### Hvordan ensartetheden er sikret

Det er lykkedes at sikre artefakternes ensartethed med tre elementer:

| Element | Hvad det sikrer |
|---|---|
| Templates | Alle dokumenter af samme type starter med den samme struktur, de samme afsnit og de samme pladsholdere (ID, krydsreferencer, links) |
| Scripts, der sammenligner dokumenterne | Afvigelser fra skabelonen og fra de øvrige dokumenter opdages automatisk, i stedet for at skulle findes ved manuel gennemlæsning |
| Tjekliste med kvalitetskriterier | Indholdet vurderes ud fra de samme kriterier hver gang, så kvaliteten ikke afhænger af, hvem der skriver eller gennemgår dokumentet |

De tre elementer supplerer hinanden: template sikrer **formen**, scripts sikrer **konsistensen** på tværs af dokumenter, og tjeklisten sikrer **kvaliteten** af indholdet.

### Hvorfor det betaler sig

- Ensartede dokumenter er lettere at læse, sammenligne og gennemgå, fordi man ved, hvor oplysningerne står.
- Fejl og afvigelser opdages tidligt, fordi deterministiske trin er overladt til scripts, og kun det, der kræver faglig vurdering, er overladt til AI og menneske.
- AI-agenten skal bruge færre tokens på at forstå dokumentets opbygning, da strukturen er den samme hver gang.
- Frameworket kan genbruges i andre projekter uden at dele projektdata.

### Afvejninger

- Ensartethed koster fleksibilitet: dokumenter, der ikke passer ind i skabelonen, kræver enten en ny type eller en bevidst undtagelse.
- Templates, scripts og tjekliste skal vedligeholdes, ellers forældes de, og så sikrer de ensartethed omkring noget forkert.
- Scripts kan kun sammenligne det, der kan måles formelt; indholdets kvalitet kræver stadig en tjekliste og en menneskelig vurdering.

## 🔄 Kolbs læringscirkel i praksis

**1. Konkret erfaring**

Jeg har det seneste semester arbejdet på at ensarte mine artefakter med template, sammenlignende scripts og en tjekliste med kvalitetskriterier. Så fik vi besøg af Trine, der havde været i praktik hos LEGO-koncernen og fortalte, at de er i gang med det samme.

**2. Refleksion**

- Hvad bekræftede besøget?
  > At jeg ikke er alene om synspunktet, og at ensartede artefakter er en god vej at følge.
- Hvad gjorde, at det lykkedes at sikre ensartetheden?
  > Kombinationen af template, scripts, der sammenligner dokumenterne, og en tjekliste med kvalitetskriterier.
- Hvad gør de tre elementer hver især?
  > Template sikrer formen, scripts sikrer konsistensen på tværs af dokumenter, og tjeklisten sikrer kvaliteten af indholdet.
- Hvad skal jeg være opmærksom på?
  > At templates, scripts og tjekliste vedligeholdes, og at ensartethed ikke bliver et mål i sig selv, hvis et dokument har brug for en anden form.

**3. Abstrakt begrebsliggørelse**

Jeg kobler erfaringen til teori om blandt andet:

- standardisering og dokumentationsstyring
- kvalitetssikring med kriterier og tjeklister
- deterministiske scripts versus AI-vurdering
- undgå gentagelse (DRY) og adskillelse af ansvar
- genbrug af kontekst i AI-skills og token-økonomi
- validering mod kriterier (human-in-the-loop)

**4. Aktiv eksperimenteren**

Jeg fortsætter med at køre scripts og tjekliste på nye dokumenter, og jeg overvejer at bruge den samme tilgang (template, automatisk sammenligning, kriterier) på de prompts og resultater, jeg dokumenterer i AI-eksperimenterne, så de også er sammenlignelige.

## 🎯 Hvilke kernemål i læringsmål dækkes

🟢 dækkes helt, 🟡 dækkes delvist, 🔴 dækkes kun lidt eller slet ikke endnu. Posten er en perspektivering af et tidligere valg og tilføjer ikke ny teknisk dækning ud over det, der allerede er beskrevet.

### Dataanalyse og databehandling

| Kerneområde | Vægt i læringsmål | Dækning | Begrundelse |
|---|---|:---:|---|
| Dataindsamling | Stor | 🔴 | Ikke relevant for denne post |
| Datastrukturering | Stor | 🔴 | Ikke relevant for denne post |
| Datakvalitet | Stor | 🔴 | Tjeklisten gælder dokumenters kvalitet, ikke datasæt |
| Datarensning | Stor | 🔴 | Ikke relevant for denne post |
| Dataanalyse | Stor | 🔴 | Ikke relevant for denne post |
| Statistik | Stor | 🔴 | Ikke relevant for denne post |
| Deskriptiv statistik | Stor | 🔴 | Ikke relevant for denne post |
| Trends og mønstre | Stor | 🔴 | Ikke relevant for denne post |
| Sammenhænge mellem variable | Stor | 🔴 | Ikke relevant for denne post |
| Datavisualisering | Stor | 🔴 | Ikke relevant for denne post |
| Fortolkning af resultater | Mindre | 🔴 | Ikke relevant for denne post |
| Formidling af data | Mindre | 🟡 | Ensartede dokumenter gør formidling af resultater mere konsistent, men posten handler ikke om data |

### AI i softwareprojekter

| Kerneområde | Vægt i læringsmål | Dækning | Begrundelse |
|---|---|:---:|---|
| Python for AI | Stor | 🔴 | Scripts er skrevet i Bash |
| Machine Learning | Stor | 🔴 | Ikke relevant for denne post |
| AI til fortolkning af data | Stor | 🔴 | Ikke relevant for denne post |
| Large Language Models (LLM) | Stor | 🟡 | Strukturen reducerer tokenforbruget, når agenten læser dokumenter |
| Modelvalg og model comparison | Stor | 🔴 | Ikke relevant for denne post |
| Prompt engineering | Stor | 🟡 | Templates og skills er genbrugelig kontekst, der gør prompts kortere og mere præcise |
| Generativ AI | Stor | 🔴 | Ikke relevant for denne post |
| AI-baseret beslutningsstøtte | Stor | 🔴 | Ikke relevant for denne post |
| OCR | Stor | 🔴 | Ikke relevant for denne post |
| Feature extraction | Stor | 🔴 | Ikke relevant for denne post |
| Fortolkning af hoteldata | Mindre | 🔴 | Ikke relevant for denne post |
| Test og evaluering af AI-output | Mindre | 🟡 | Tjekliste med kvalitetskriterier og sammenlignende scripts bruges til at vurdere AI-genererede dokumenter |
| Fejlhåndtering og usikkerhed | Mindre | 🟡 | Afvigelser fanges af scripts; vedligeholdelsesrisikoen er identificeret |
| Human-in-the-loop | Mindre | 🟡 | Scripts tager det rutineprægede, mens faglig vurdering og tjekliste ligger hos mennesket |
| Privacy og ansvarlig AI | Mindre | 🟡 | Framework og projektdata holdes adskilt |

## 🏨 Hvilken værdi kan det give et hotel management-system?

Værdien er indirekte, men konkret:

- **Sporbar og ensartet dokumentation:** Business case, milepæle, domænemodel og ADR'er for NF Hotel følger samme form, så de er lette at gennemgå og sammenligne.
- **Kvalitetssikring af AI-output:** Samme kombination af template, automatisk sammenligning og kriterier kan bruges til at tjekke AI-genererede rapporter og konklusioner om hoteldata, så de har samme struktur og opfylder de samme krav.
- **Bekræftet retning:** At en stor organisation som LEGO går samme vej, understøtter, at ensartethed er et valg, der også kan skalere til et større hotel- eller systemmiljø.
