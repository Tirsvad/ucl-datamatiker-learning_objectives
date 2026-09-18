# Processen i at vælge – IDE til lokal AI

**Dato:** 18/9 2026
**Læringsmål dækket:** [AI i softwareprojekter](../Læringsmål–AI_til_softwareløsninger.md) og [Dataanalyse og databehandling](../Læringsmål–Dataanalyse_og_databehandling.md)

Jeg blev introduceret til Microsoft Visual Studio på uddannelsen, og det har dannet rammen om mit arbejde de første 3 semestre. Da jeg begyndte at arbejde med lokal AI, opstod der imidlertid et problem, som fik mig til at lede efter et alternativ. Denne post dokumenterer den valgproces.

## 🧭 Processen i at vælge

| Værktøj | Rolle | Valgt/beholdt fordi | Alternativ(er) overvejet |
|---|---|---|---|
| Visual Studio | IDE til C#-udvikling og debugging | Har en god debugger til C#, som Zed stadig mangler | – |
| Zed | Ny IDE til arbejde med lokal AI | Understøtter lokal AI som plugin, håndterer de fleste programmeringssprog, og er hurtigere og mindre ressourcekrævende end Visual Studio | Eclipse og andre IDE'er – kendt fra erfaring til at være langsomme og ressourcekrævende; blev ikke testet nærmere for lokal AI-understøttelse, da Zed allerede løste behovet |

Konklusionen blev ikke at skrotte Visual Studio til fordel for Zed, men at lade de to værktøjer supplere hinanden.

## 🔄 Kolbs læringscirkel i praksis

**1. Konkret erfaring**

Da jeg begyndte at arbejde med lokal AI, virkede det ikke som plugin i Visual Studio. Det betød, at jeg måtte lede efter et alternativ, der kunne det, Visual Studio ikke kunne.

**2. Refleksion**

- Hvad virkede ikke?
  > Lokal AI kunne ikke køre som plugin i Visual Studio.
- Hvilke alternativer overvejede jeg, og hvorfor testede jeg dem ikke nærmere?
  > Jeg kender Eclipse og andre IDE'er fra erfaring og ved, at de er langsomme og ressourcekrævende – derfor undersøgte jeg ikke, om de kunne køre lokal AI, og gik direkte videre til at søge efter et andet alternativ.
- Hvordan fandt jeg frem til Zed?
  > Ved at søge på nettet efter en IDE, der kunne understøtte lokal AI, faldt jeg over Zed, som håndterer de fleste programmeringssprog og understøtter lokal AI.
- Hvilke kriterier vægtede jeg højst?
  > Understøttelse af lokal AI, ressourceforbrug og hastighed – Zed bruger færre ressourcer og er hurtigere end Visual Studio.
- Var jeg klar til at skrotte Visual Studio helt?
  > Nej. Visual Studio har en god debugger til C#, som Zed stadig mangler, så de to værktøjer skal supplere hinanden i stedet for at erstatte hinanden.

**3. Abstrakt begrebsliggørelse**

Jeg kobler erfaringen til teori om blandt andet:

- IDE-arkitektur og plugin-økosystemer
- ressourceforbrug og performance i udviklingsværktøjer
- lokal AI versus cloud-baseret AI
- kriteriebaseret værktøjsvalg og trade-off-analyse
- privacy ved at køre AI lokalt frem for via eksterne tjenester

**4. Aktiv eksperimenteren**

Jeg bruger nu Zed til arbejde, hvor lokal AI er en fordel, og Visual Studio til C#-udvikling, hvor debuggeren er nødvendig. Næste skridt er at holde øje med, om Zed's værktøjsstøtte (fx debugging) udvikler sig, så fordelingen mellem de to værktøjer kan justeres. Det er den samme kriterie-baserede metode – kriterier, alternativer, begrundet valg – som jeg tidligere har brugt til at vælge infrastruktur til mit lab, og som jeg senere skal bruge til at vælge AI-modeller/LLM'er.

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
| Datavisualisering | Stor | 🔴 | Ikke relevant for denne post |
| Fortolkning af resultater | Mindre | 🔴 | Ikke relevant for denne post |
| Formidling af data | Mindre | 🔴 | Ikke relevant for denne post |

### AI i softwareprojekter

| Kerneområde | Vægt i læringsmål | Dækning | Begrundelse |
|---|---|:---:|---|
| Python for AI | Stor | 🔴 | Ikke relevant for denne post |
| Machine Learning | Stor | 🔴 | Ikke relevant for denne post |
| AI til fortolkning af data | Stor | 🔴 | Ikke relevant for denne post |
| Large Language Models (LLM) | Stor | 🔴 | Ikke relevant for denne post |
| Modelvalg og model comparison | Stor | 🟡 | Samme kriterie- og alternativ-baserede metode er øvet her på et udviklingsværktøj, klar til at genbruges på LLM-valg |
| Prompt engineering | Stor | 🔴 | Ikke relevant for denne post |
| Generativ AI | Stor | 🔴 | Ikke relevant for denne post |
| AI-baseret beslutningsstøtte | Stor | 🔴 | Ikke relevant for denne post |
| OCR | Stor | 🔴 | Ikke relevant for denne post |
| Feature extraction | Stor | 🔴 | Ikke relevant for denne post |
| Fortolkning af hoteldata | Mindre | 🔴 | Ikke relevant for denne post |
| Test og evaluering af AI-output | Mindre | 🔴 | Ikke relevant for denne post |
| Fejlhåndtering og usikkerhed | Mindre | 🟡 | At opdage at lokal AI ikke virkede som plugin i Visual Studio, og derefter systematisk lede efter et alternativ, er en mindre form for fejlhåndtering |
| Human-in-the-loop | Mindre | 🔴 | Ikke relevant for denne post |
| Privacy og ansvarlig AI | Mindre | 🟡 | At vælge lokal AI frem for en cloud-baseret løsning er et bevidst valg om at holde AI-arbejdet og data lokalt |

## 🏨 Hvilken værdi kan det give et hotel management-system?

Valget af udviklingsværktøjer er ikke kun et spørgsmål om personlig præference – det påvirker, hvor effektivt og sikkert et hotel management-system kan udvikles.

- **Lokal AI under udvikling:** Ved at kunne køre AI lokalt i udviklingsmiljøet kan jeg eksperimentere med AI-funktioner, uden at kode eller testdata (fx uddrag af hoteldata) nødvendigvis skal sendes til en ekstern tjeneste undervejs – det understøtter samme privacy-tankegang, som lå bag valget af selvhostet database og mailserver i labbet.
- **Effektivitet:** Et hurtigere og mindre ressourcekrævende værktøj som Zed betyder mere tid til faktisk udvikling og mindre tid brugt på at vente på værktøjet.
- **Pålidelighed i kernesystemet:** Ved at beholde Visual Studios stærke C#-debugger til den del af systemet, hvor det betyder mest (fx kernelogik i et hotel management-system), reduceres risikoen for udokumenterede fejl i produktionskoden.

Samlet set viser valget, at det rigtige værktøj afhænger af opgaven – og at det er en fordel at kunne skifte mellem eller kombinere flere værktøjer, i stedet for at insistere på ét værktøj til alt.
