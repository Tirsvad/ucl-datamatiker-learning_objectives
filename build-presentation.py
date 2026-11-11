from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.chart.data import CategoryChartData
from pptx.enum.chart import XL_CHART_TYPE, XL_LABEL_POSITION
from PIL import Image
import os

A = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "NF-Hotel-mit-bidrag.pptx")

NAVY = RGBColor(0x0F, 0x17, 0x2A)
TEAL = RGBColor(0x1F, 0x9E, 0xB0)
TEAL_D = RGBColor(0x14, 0x6F, 0x7C)
AMBER = RGBColor(0xE5, 0xA8, 0x2E)
INK = RGBColor(0x1E, 0x29, 0x3B)
MUTED = RGBColor(0x5B, 0x67, 0x7A)
LIGHT = RGBColor(0xF3, 0xF6, 0xF9)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
RED = RGBColor(0xC2, 0x41, 0x3B)
GREEN = RGBColor(0x2E, 0x8B, 0x57)
HEAD = "Cambria"
BODY = "Calibri"

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
BLANK = prs.slide_layouts[6]
SW, SH = 13.333, 7.5
count = [0]


def bg(slide, color):
    f = slide.background.fill
    f.solid()
    f.fore_color.rgb = color


def text(slide, x, y, w, h, content, size=16, color=INK, bold=False, font=BODY,
         align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP, italic=False, name=None):
    tb = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    if name:
        tb.name = name
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    tf.vertical_anchor = anchor
    paras = content if isinstance(content, list) else [content]
    for i, p in enumerate(paras):
        para = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        para.alignment = align
        runs = p if isinstance(p, list) else [(p, {})]
        for r in runs:
            if isinstance(r, str):
                r = (r, {})
            t, o = r
            run = para.add_run()
            run.text = t
            run.font.name = o.get("font", font)
            run.font.size = Pt(o.get("size", size))
            run.font.bold = o.get("bold", bold)
            run.font.italic = o.get("italic", italic)
            run.font.color.rgb = o.get("color", color)
        para.space_after = Pt(6)
    return tb


def bullets(slide, x, y, w, h, items, size=16, color=INK, gap=8):
    tb = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    for i, it in enumerate(items):
        para = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        para.space_after = Pt(gap)
        pPr = para._p.get_or_add_pPr()
        pPr.set("marL", str(int(Inches(0.28))))
        pPr.set("indent", str(-int(Inches(0.28))))
        from lxml import etree
        ns = "http://schemas.openxmlformats.org/drawingml/2006/main"
        bc = etree.SubElement(pPr, "{%s}buClr" % ns)
        clr = etree.SubElement(bc, "{%s}srgbClr" % ns)
        clr.set("val", "1F9EB0")
        bu = etree.SubElement(pPr, "{%s}buChar" % ns)
        bu.set("char", "•")
        runs = it if isinstance(it, list) else [(it, {})]
        for r in runs:
            if isinstance(r, str):
                r = (r, {})
            t, o = r
            run = para.add_run()
            run.text = t
            run.font.name = BODY
            run.font.size = Pt(o.get("size", size))
            run.font.bold = o.get("bold", False)
            run.font.color.rgb = o.get("color", color)
    return tb


def box(slide, x, y, w, h, fill=WHITE, line=None, shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.06, name=None):
    s = slide.shapes.add_shape(shape, Inches(x), Inches(y), Inches(w), Inches(h))
    if name:
        s.name = name
    if shape == MSO_SHAPE.ROUNDED_RECTANGLE:
        s.adjustments[0] = radius
    s.fill.solid()
    s.fill.fore_color.rgb = fill
    if line is None:
        s.line.fill.background()
    else:
        s.line.color.rgb = line
        s.line.width = Pt(0.75)
    s.shadow.inherit = False
    return s


def picture(slide, path, x, y, w, h, frame=True, name=None):
    """Fit image inside the box keeping aspect ratio, centred."""
    iw, ih = Image.open(path).size
    r = min(w / iw, h / ih)
    pw, ph = iw * r, ih * r
    px, py = x + (w - pw) / 2, y + (h - ph) / 2
    if frame:
        box(slide, px - 0.06, py - 0.06, pw + 0.12, ph + 0.12, fill=WHITE, line=RGBColor(0xD5, 0xDC, 0xE4), radius=0.02)
    pic = slide.shapes.add_picture(path, Inches(px), Inches(py), Inches(pw), Inches(ph))
    if name:
        pic.name = name
    return pic


def title(slide, t, sub=None, dark=False):
    text(slide, 0.6, 0.45, 12.1, 0.8, t, size=34, color=WHITE if dark else NAVY, bold=True, font=HEAD, name="Titel")
    if sub:
        text(slide, 0.6, 1.2, 12.1, 0.5, sub, size=16, color=RGBColor(0xB8, 0xC4, 0xD6) if dark else MUTED)


def footer(slide, dark=False):
    count[0] += 1
    c = RGBColor(0x8A, 0x97, 0xAB)
    text(slide, 0.6, 7.05, 9, 0.3, "NF Hotel · Jens Tirsvad Nielsen · UCL Datamatiker 2026", size=10, color=c)
    text(slide, 12.0, 7.05, 0.75, 0.3, str(count[0]), size=10, color=c, align=PP_ALIGN.RIGHT)


def new(dark=False, light=False):
    s = prs.slides.add_slide(BLANK)
    bg(s, NAVY if dark else (LIGHT if light else WHITE))
    return s


def notes(slide, t):
    slide.notes_slide.notes_text_frame.text = t


def icon_circle(slide, x, y, d, label, fill=TEAL, color=WHITE, size=16):
    c = box(slide, x, y, d, d, fill=fill, shape=MSO_SHAPE.OVAL)
    tf = c.text_frame
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    r = p.add_run()
    r.text = label
    r.font.size = Pt(size)
    r.font.bold = True
    r.font.name = BODY
    r.font.color.rgb = color
    return c


def style_chart(chart, size=12):
    chart.font.size = Pt(size)
    chart.font.name = BODY
    chart.font.color.rgb = INK


# ---------------------------------------------------------------- 1 Titel
s = new(dark=True)
count[0] += 1
box(s, 0.6, 2.0, 1.1, 1.1, fill=TEAL, shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.18)
text(s, 0.6, 2.0, 1.1, 1.1, "NF", size=40, color=WHITE, bold=True, font=HEAD, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
text(s, 2.0, 1.95, 10.5, 1.0, "NF Hotel – mit bidrag", size=48, color=WHITE, bold=True, font=HEAD)
text(s, 2.0, 2.95, 10.5, 0.6, "Dataanalyse og AI i et hotel management-system", size=24, color=RGBColor(0xB8, 0xC4, 0xD6))
text(s, 0.6, 5.3, 12, 0.4, "Jens Tirsvad Nielsen · Data Analysis & AI", size=18, color=WHITE, bold=True)
text(s, 0.6, 5.75, 12, 0.4, "UCL Datamatiker · 30 ECTS-projekt · 26. august – 6. december 2026", size=16, color=RGBColor(0xB8, 0xC4, 0xD6))
notes(s, "Kort intro: jeg præsenterer NF Hotel-projektet, men fokus er på det, jeg selv har bidraget med inden for de to læringsmål: AI til softwareløsninger og Dataanalyse og databehandling.")

# ---------------------------------------------------------------- 2 Projektet
s = new()
title(s, "NF Hotel: et webbaseret hotelsystem", "Hotel og bar i Phnom Penh · bygget af et team på fem")
bullets(s, 0.6, 1.95, 5.6, 3.2, [
    "Bookinger, gæster, værelser og priser samlet ét sted",
    "Blazor-web, .NET API og PostgreSQL; kun API'et åbner databasen",
    "Mobilapp til personale (Flutter)",
    "To Python-services: markedsanalyse og LLM-benchmark, med lokale modeller i Ollama",
    "Docker, nginx og CI/CD med sikkerhedstjek",
], size=16)
picture(s, os.path.join(A, "dash.jpg"), 6.6, 1.85, 6.15, 3.3, name="Skærmbillede: dashboard")
text(s, 6.6, 5.3, 6.15, 0.3, "Administrationen: dashboard for hotellets forreception", size=11, color=MUTED, italic=True)
team = [("Michael Kragh", "Cyber Security & DevOps", False), ("William B. Christensen", "Software Development", False),
        ("Jakob K. Jensen", "Mobile Development", False), ("Valdemar L. V. Carlsson", "Frontend & AI", False),
        ("Jens Tirsvad Nielsen", "Data Analysis & AI", True)]
for i, (n, r, me) in enumerate(team):
    x = 0.6 + i * 2.45
    box(s, x, 5.85, 2.3, 1.0, fill=TEAL if me else LIGHT)
    text(s, x + 0.15, 5.97, 2.0, 0.4, n, size=13, bold=True, color=WHITE if me else NAVY)
    text(s, x + 0.15, 6.35, 2.0, 0.4, r, size=12, color=WHITE if me else MUTED)
footer(s)
notes(s, "Teamet har fem medlemmer med hvert deres område. Mit område er Data Analysis & AI. Systemet er bredere end mit bidrag; resten af præsentationen handler om de dele, jeg har bygget og dokumenteret.")

# ---------------------------------------------------------------- 3 Læringsmål
s = new(light=True)
title(s, "To læringsmål, ét samlet flow", "De er designet til at supplere hinanden")
for i, (hd, ects, pts) in enumerate([
    ("AI til softwareløsninger", "18 ECTS", ["Vælge og evaluere LLM'er", "Prompt engineering og fortolkning af hoteldata", "OCR/ML til pasoplysninger", "Test, usikkerhed og human-in-the-loop"]),
    ("Dataanalyse og databehandling", "12 ECTS", ["Datakvalitet og rensning", "Statistik, trends og sammenhænge", "Visualisering med begrundelse", "Formidling som beslutningsstøtte"]),
]):
    x = 0.6 + i * 6.2
    box(s, x, 1.9, 5.95, 3.2, fill=WHITE, line=RGBColor(0xD5, 0xDC, 0xE4))
    text(s, x + 0.3, 2.1, 4.2, 0.5, hd, size=21, bold=True, color=NAVY, font=HEAD)
    box(s, x + 4.65, 2.12, 1.05, 0.42, fill=TEAL, radius=0.4)
    text(s, x + 4.65, 2.12, 1.05, 0.42, ects, size=13, bold=True, color=WHITE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    bullets(s, x + 0.3, 2.85, 5.4, 2.2, pts, size=15, gap=6)
steps = ["Problem", "Data", "Datakvalitet", "Analyse", "Trends", "AI-eksperiment", "Validering", "Beslutningsstøtte"]
w = 1.37
for i, st in enumerate(steps):
    x = 0.6 + i * (w + 0.17)
    fill = AMBER if i == len(steps) - 1 else (TEAL if i < 5 else TEAL_D)
    box(s, x, 5.6, w, 0.85, fill=fill)
    text(s, x, 5.6, w, 0.85, st, size=12, bold=True, color=NAVY if i == len(steps) - 1 else WHITE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
text(s, 0.6, 6.55, 12, 0.3, "Dataanalysen giver grundlaget for at forstå og kontrollere data; AI-sporet fortolker de samme data, og et menneske validerer.", size=12, color=MUTED, italic=True)
footer(s)
notes(s, "Mine to læringsmål følger samme flow: fra problem og data via datakvalitet og analyse til AI-eksperiment, validering og beslutningsstøtte. Det er også den rækkefølge, jeg har bygget markedsanalysen og prisforslagene i.")

# ---------------------------------------------------------------- F1 Framework: hvorfor
s = new()
title(s, "Frameworket: struktur, der understøtter AI i processen", "AI er hurtig, men uden rammer varierer resultatet fra gang til gang")
els = [
    ("Skabeloner", "Alle dokumenter af samme type får samme form, samme afsnit og samme pladsholdere."),
    ("Skills", "Én samlet artefakt-skill i stedet for 19. Type-specifikke filer læses kun, når de skal bruges."),
    ("Scripts", "Rutinearbejde er deterministisk: næste ID, krydsreferencer og links. AI laver kun den faglige del."),
    ("QC-tjeklister", "Over 30 tjeklister tagget efter ISO/IEC 25010. Hvert dokument gennemgås efter samme kriterier."),
]
for i, (hd, body) in enumerate(els):
    x = 0.6 + (i % 2) * 3.55
    y = 1.95 + (i // 2) * 2.45
    box(s, x, y, 3.35, 2.25, fill=LIGHT)
    icon_circle(s, x + 0.25, y + 0.25, 0.55, str(i + 1), fill=TEAL, size=18)
    text(s, x + 1.0, y + 0.33, 2.2, 0.4, hd, size=17, bold=True, color=NAVY, font=HEAD)
    text(s, x + 0.25, y + 0.95, 2.9, 1.3, body, size=13)
box(s, 7.9, 1.95, 4.85, 2.05, fill=NAVY)
text(s, 8.15, 2.1, 4.4, 0.4, "framework/", size=18, bold=True, color=AMBER, font=HEAD)
text(s, 8.15, 2.6, 4.4, 1.3, "Genbruges af andre projekter. Indeholder skabeloner, skills, scripts og tjeklister, men ingen projektdata.", size=14, color=WHITE)
text(s, 7.9, 4.05, 4.85, 0.4, "↓  AI læser skill og bruger skabelon  ↓", size=13, bold=True, color=TEAL_D, align=PP_ALIGN.CENTER)
box(s, 7.9, 4.5, 4.85, 2.4, fill=TEAL)
text(s, 8.15, 4.65, 4.4, 0.4, "docs/ og src/", size=18, bold=True, color=WHITE, font=HEAD)
text(s, 8.15, 5.15, 4.4, 1.7, "Projektets egne dokumenter, kode og review-records. Frameworket er et git-submodul, så NF Hotels data aldrig lander i det.", size=14, color=WHITE)
footer(s)
notes(s, "Frameworket er det, der gør AI brugbar i et projekt. Uden rammer skriver AI et dokument forskelligt hver gang. Med skabeloner, én samlet skill, scripts til rutinearbejde og tjeklister er det kun den faglige vurdering, der overlades til AI og menneske. Frameworket ligger adskilt i et submodul og indeholder ingen projektdata.")

# ---------------------------------------------------------------- F2 Framework: rækkefølge og gate
s = new(light=True)
title(s, "Frameworket styrer rækkefølgen", "Hvert trin ender i en review, og ingen kode skrives før planen er godkendt")
chain = ["Business Case", "Stakeholder-analyse", "Projektplan", "Milestones", "Tasks som issues", "Kode"]
w = 1.85
for i, c in enumerate(chain):
    x = 0.6 + i * (w + 0.2)
    fill = AMBER if i == 5 else NAVY
    box(s, x, 1.95, w, 1.1, fill=fill)
    text(s, x + 0.08, 1.95, w - 0.16, 1.1, c, size=15, bold=True, color=NAVY if i == 5 else WHITE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    box(s, x + 0.25, 3.15, w - 0.5, 0.42, fill=GREEN, radius=0.4)
    text(s, x + 0.25, 3.15, w - 0.5, 0.42, "Review: Go", size=12, bold=True, color=WHITE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    if i < 5:
        text(s, x + w - 0.02, 2.25, 0.24, 0.4, "›", size=22, bold=True, color=MUTED, align=PP_ALIGN.CENTER)
cards = [
    ("Plan-first gate", "Intet i src/ eller tests/ før milestonen er Accepted og har en review med Go, og opgaven står som række i den. Håndhæves af script og git-hook.", TEAL_D),
    ("To arbejdsmåder", "Supervised er standard: AI redigerer, og jeg gennemgår, før noget committes. Autonomous kun når jeg beder om det i chatten og har godkendt planen.", TEAL_D),
    ("Stop-regler", "AI stopper og melder tilbage ved destruktive handlinger, ændret scope, sikkerhedsfejl, hemmeligheder eller tre mislykkede reviews i træk.", TEAL_D),
]
for i, (hd, body, col) in enumerate(cards):
    x = 0.6 + i * 4.1
    box(s, x, 4.0, 3.9, 2.4, fill=WHITE, line=RGBColor(0xD5, 0xDC, 0xE4))
    text(s, x + 0.25, 4.2, 3.4, 0.4, hd, size=18, bold=True, color=col, font=HEAD)
    text(s, x + 0.25, 4.75, 3.4, 2.0, body, size=13)
footer(s)
notes(s, "Frameworket gør AI-arbejdet styrbart. Rækkefølgen er fast, og hvert trin skal have en review-record med Go, før næste trin starter. Plan-first gate betyder, at AI ikke kan begynde at skrive kode uden en godkendt plan. Supervised er standard, så det er mig, der gennemgår ændringerne. Autonomous bruges kun efter min udtrykkelige anmodning, og AI optræder så som stand-in og skriver det i review-recorden.")

# ---------------------------------------------------------------- F3 Framework: effekt
s = new()
title(s, "Hvad frameworket gav i NF Hotel", "Færre tokens for AI, og et spor, der kan kontrolleres")
cd = CategoryChartData()
cd.categories = ["Skill-beskrivelser (altid indlæst)", "AGENTS.md (altid indlæst)", "Redigere en business case"]
cd.add_series("Før: 19 skills", (1550, 830, 4000))
cd.add_series("Efter: én samlet skill", (115, 340, 1400))
gf = s.shapes.add_chart(XL_CHART_TYPE.COLUMN_CLUSTERED, Inches(0.6), Inches(1.95), Inches(7.2), Inches(4.5), cd)
ch = gf.chart
style_chart(ch, 12)
ch.has_title = True
ch.chart_title.text_frame.text = "Tokens AI'en skal læse (groft estimat)"
ch.chart_title.text_frame.paragraphs[0].runs[0].font.size = Pt(14)
ch.chart_title.text_frame.paragraphs[0].runs[0].font.bold = True
ch.has_legend = True
ch.legend.include_in_layout = False
from pptx.enum.chart import XL_LEGEND_POSITION
ch.legend.position = XL_LEGEND_POSITION.BOTTOM
ch.legend.font.size = Pt(12)
ch.value_axis.visible = False
ch.value_axis.has_major_gridlines = False
ch.value_axis.maximum_scale = 4800
pl = ch.plots[0]
pl.gap_width = 60
pl.overlap = -5
pl.has_data_labels = True
pl.data_labels.number_format = "#,##0"
pl.data_labels.number_format_is_linked = False
pl.data_labels.font.size = Pt(12)
pl.data_labels.font.bold = True
pl.data_labels.position = XL_LABEL_POSITION.OUTSIDE_END
pl.series[0].format.fill.solid()
pl.series[0].format.fill.fore_color.rgb = RGBColor(0xB5, 0xBF, 0xCC)
pl.series[1].format.fill.solid()
pl.series[1].format.fill.fore_color.rgb = TEAL
text(s, 0.6, 6.5, 7.2, 0.3, "Estimat: tegn divideret med fire. Kilde: min portfolio-post om artefakt-færdigheden.", size=11, color=MUTED, italic=True)
tiles = [("v0.19.0", "frameworkversion i NF Hotel"), ("ca. 70", "milestones med tasks"),
         ("40+", "ADR'er (arkitekturbeslutninger)"), ("300+", "review-records (RC) med Go eller No-Go")]
for i, (n, l) in enumerate(tiles):
    x = 8.2 + (i % 2) * 2.35
    y = 1.95 + (i // 2) * 1.85
    box(s, x, y, 2.2, 1.7, fill=NAVY)
    text(s, x + 0.2, y + 0.2, 1.9, 0.7, n, size=28, bold=True, color=AMBER, font=HEAD)
    text(s, x + 0.2, y + 0.95, 1.85, 0.7, l, size=12, color=WHITE)
box(s, 8.2, 5.7, 4.55, 1.15, fill=LIGHT)
text(s, 8.4, 5.78, 4.2, 1.0, "Pris: skabeloner, scripts og tjeklister skal vedligeholdes, og ensartethed koster fleksibilitet.", size=13, color=INK, anchor=MSO_ANCHOR.MIDDLE)
footer(s)
notes(s, "Her ser man effekten af at samle 19 skills til én: AI'en skal læse langt færre tokens, før den kan arbejde. Tallene er et groft estimat. Besøget af en praktikant fra LEGO bekræftede, at ensartede artefakter er en retning, flere arbejder i. Afvejningen er, at frameworket skal vedligeholdes, ellers forældes det.")

# ---------------------------------------------------------------- 4 Tal
s = new(dark=True)
title(s, "Mit bidrag i tal", dark=True)
stats = [("327", "commits i NF Hotel-repositoriet"), ("156.686", "bookinger i markedsanalysen"),
         ("9 + 3", "analyser plus forecast for omsætning, ankomster og belægning"),
         ("5", "lokale LLM'er målt i 135 forespørgsler"), ("2", "milestones: MIL-026 markedsanalyse, MIL-055 prisforslag")]
pos = [(0.6, 1.9), (4.6, 1.9), (8.6, 1.9), (0.6, 4.4), (4.6, 4.4)]
for (n, l), (x, y) in zip(stats, pos):
    box(s, x, y, 3.7, 2.2, fill=RGBColor(0x1A, 0x25, 0x3F))
    text(s, x + 0.3, y + 0.25, 3.2, 1.0, n, size=54, bold=True, color=AMBER, font=HEAD)
    text(s, x + 0.3, y + 1.4, 3.2, 0.7, l, size=15, color=WHITE)
box(s, 8.6, 4.4, 3.7, 2.2, fill=TEAL)
text(s, 8.9, 4.65, 3.2, 1.6, "Alt med forbehold: hvert tal er sporbart til portfolio og til repositoriet", size=16, color=WHITE, bold=True)
footer(s, dark=True)
notes(s, "327 commits er mine commits på alle grene, inklusive merges. 156.686 er antal bookinger i den kørsel, som portfolio-posten bygger på. De fem modeller og 135 forespørgsler kommer fra benchmarken.")

# ---------------------------------------------------------------- 5 Pipeline
s = new()
title(s, "Fra data til beslutning: det jeg byggede", "Tallene regnes af kode; AI'en forklarer; et menneske beslutter")
nodes = [("Bookinger", "PostgreSQL"), ("Markedsanalyse", "Python-service"), ("API", ".NET"),
         ("Administration", "Blazor"), ("Prisforslag", "fast regel"), ("Manager", "godkender")]
w = 1.85
for i, (a, b) in enumerate(nodes):
    x = 0.6 + i * (w + 0.2)
    fill = AMBER if i == 5 else (TEAL if i in (1, 4) else NAVY)
    box(s, x, 2.2, w, 1.5, fill=fill)
    text(s, x + 0.1, 2.5, w - 0.2, 0.5, a, size=16, bold=True, color=NAVY if i == 5 else WHITE, align=PP_ALIGN.CENTER)
    text(s, x + 0.1, 3.05, w - 0.2, 0.4, b, size=13, color=NAVY if i == 5 else RGBColor(0xD8, 0xE2, 0xEE), align=PP_ALIGN.CENTER)
    if i < 5:
        text(s, x + w - 0.02, 2.75, 0.24, 0.4, "›", size=22, bold=True, color=MUTED, align=PP_ALIGN.CENTER)
for i, (hd, body) in enumerate([
    ("Deterministisk", "Python regner rater, belægning, omsætning, korrelationer og forecast. Det kan kontrolleres."),
    ("AI til forklaring", "Lokale modeller (Ollama) skriver opsummeringer. De er mærket som hypotese, ikke prognose."),
    ("Human-in-the-loop", "Prisen ændres først, når en Manager har godkendt forslaget. Hver godkendelse logges."),
]):
    x = 0.6 + i * 4.1
    box(s, x, 4.4, 3.9, 2.3, fill=LIGHT)
    text(s, x + 0.25, 4.6, 3.4, 0.4, hd, size=18, bold=True, color=NAVY, font=HEAD)
    text(s, x + 0.25, 5.15, 3.4, 1.5, body, size=14, color=INK)
footer(s)
notes(s, "Det vigtigste designvalg: tallene kommer fra kode, ikke fra AI. AI'en forklarer bagefter. Og prisen er en forretningsbeslutning, så den skal kunne spores og godkendes af et menneske.")

# ---------------------------------------------------------------- 6 Modelvalg chart
s = new()
title(s, "Modelvalg: jeg målte i stedet for at gætte", "Benchmark af fem lokale modeller, samme prompt og samme data")
cd = CategoryChartData()
cd.categories = ["gemma4:e2b", "phi4", "phi4-reasoning:plus", "Whittle MoE 27B"]
cd.add_series("Median tokens/s", (85.8, 10.8, 6.4, 3.8))
gf = s.shapes.add_chart(XL_CHART_TYPE.BAR_CLUSTERED, Inches(0.6), Inches(1.95), Inches(6.6), Inches(4.2), cd)
ch = gf.chart
style_chart(ch)
ch.has_legend = False
ch.has_title = True
ch.chart_title.text_frame.text = "Hastighed: median tokens pr. sekund"
ch.chart_title.text_frame.paragraphs[0].runs[0].font.size = Pt(14)
ch.chart_title.text_frame.paragraphs[0].runs[0].font.bold = True
ch.category_axis.reverse_order = True
ch.category_axis.format.line.fill.background()
ch.value_axis.visible = False
ch.value_axis.has_major_gridlines = False
pl = ch.plots[0]
pl.gap_width = 60
pl.has_data_labels = True
pl.data_labels.font.size = Pt(13)
pl.data_labels.font.bold = True
pl.data_labels.number_format = "0.0"
pl.data_labels.number_format_is_linked = False
pl.data_labels.position = XL_LABEL_POSITION.OUTSIDE_END
ser = pl.series[0]
ser.format.fill.solid()
ser.format.fill.fore_color.rgb = TEAL
pt = ser.points[1]
pt.format.fill.solid()
pt.format.fill.fore_color.rgb = AMBER
text(s, 0.6, 6.3, 6.6, 0.5, "qwen3-coder-next gav ingen gyldige svar (0 af 20) og er derfor ikke med i søjlerne.", size=11, color=MUTED, italic=True)
text(s, 7.7, 1.95, 5.0, 0.4, "Det jeg læste ud af tallene", size=20, bold=True, color=NAVY, font=HEAD)
bullets(s, 7.7, 2.6, 5.0, 4.2, [
    [("Hurtig er ikke nok. ", {"bold": True}), "phi4-reasoning:plus og qwen3-coder gav timeouts eller ugyldig JSON"],
    [("Pålidelighed før kvalitet. ", {"bold": True}), "Kun gemma4:e2b og phi4 bestod 20 af 25 opgaver"],
    [("Privacy. ", {"bold": True}), "Alle modeller kørte lokalt; CSV-filen blev aldrig sendt til modellen"],
    [("Valgt: phi4. ", {"bold": True}), "Den gik dybere i analysen end gemma, men koster tid (næste slide)"],
], size=15, gap=10)
footer(s)
notes(s, "Dette dækker succeskriteriet om at undersøge mindst tre modeller. Der er fem modeller i benchmarken. gemma4:e2b er en mindre variant end den, læringsmålet nævner, og qwen3.8-27b er endnu ikke testet som selvstændig model. Det siger jeg ærligt.")

# ---------------------------------------------------------------- 7 Benchmark admin
s = new(light=True)
title(s, "Valget kan skiftes i administrationen", "Benchmark-siden i NF Hotel")
picture(s, os.path.join(A, "benchmark.jpg"), 0.6, 1.9, 7.9, 4.9, name="Skærmbillede: Benchmark")
bullets(s, 8.9, 2.0, 3.9, 4.8, [
    "Standardmodel for websitet og markedsanalysen vælges her; nu phi4:latest",
    "Færdige kørsler gemmes med maskinen, de kørte på",
    "Modeller kan hentes og slettes fra siden",
    [("Prisen for phi4: ", {"bold": True}), "analysen med AI-tekster over alle bookinger tog ca. 20 minutter uden GPU"],
], size=15, gap=12)
footer(s)
notes(s, "Her ses Benchmark-siden i den kørende administration. Benchmarken kører i en separat Python-service og sender resultater til API'et. Et tidligere modelvalg holdt ikke i den dybere analyse, så jeg er tilbage ved phi4.")

# ---------------------------------------------------------------- 8 Markedsanalyse
s = new()
title(s, "Markedsanalysen i administrationen", "Ni analyser med diagrammer, der selv siger, hvad de ikke kan")
picture(s, os.path.join(A, "market.jpg"), 0.6, 1.9, 6.0, 3.1, name="Skærmbillede: Market analysis")
picture(s, os.path.join(A, "market2.jpg"), 6.75, 1.9, 6.0, 3.1, name="Skærmbillede: diagrammer")
text(s, 0.6, 5.15, 12.1, 0.3, "Skærmbillederne er fra den kørende installation; portfolioens tal bruger kørslen over alle 156.686 bookinger.", size=11, color=MUTED, italic=True)
for i, (hd, body) in enumerate([
    ("What it shows", "Hvad diagrammet viser"),
    ("Why this chart", "Hvorfor netop denne diagramtype: donut kun til 2–4 dele, der giver 100 %"),
    ("What it cannot say", "Begrænsninger, fx at korrelation ikke er årsag"),
]):
    x = 0.6 + i * 4.1
    box(s, x, 5.65, 3.9, 1.25, fill=LIGHT)
    text(s, x + 0.2, 5.78, 3.5, 0.35, hd, size=15, bold=True, color=TEAL_D)
    text(s, x + 0.2, 6.15, 3.5, 0.7, body, size=13, color=INK)
footer(s)
notes(s, "Hver graf har tre faste tekster. De gør begrundelsen for diagramvalget synlig, mens jeg udvikler. I produktion skal en leder ikke se dem. Den live-kørsel, jeg viser, har ingen AI-tekster (AI_NOT_CONFIGURED); portfolioens kørsel havde dem fra phi4.")

# ---------------------------------------------------------------- 9 Fund annullering
s = new()
title(s, "Fund: jo tidligere man booker, jo oftere annullerer man", "Annulleringsrate efter lead time, alle 156.686 bookinger")
cd = CategoryChartData()
cd.categories = ["0–7 dage", "8–30 dage", "31–90 dage", "91+ dage"]
cd.add_series("Annullering %", (6.5, 21.5, 32.4, 39.2))
gf = s.shapes.add_chart(XL_CHART_TYPE.COLUMN_CLUSTERED, Inches(0.6), Inches(1.95), Inches(6.4), Inches(4.7), cd)
ch = gf.chart
style_chart(ch)
ch.has_legend = False
ch.value_axis.visible = False
ch.value_axis.has_major_gridlines = False
ch.value_axis.maximum_scale = 48
ch.category_axis.format.line.color.rgb = RGBColor(0xC5, 0xCD, 0xD8)
pl = ch.plots[0]
pl.gap_width = 55
pl.has_data_labels = True
pl.data_labels.number_format = '0.0"%"'
pl.data_labels.number_format_is_linked = False
pl.data_labels.font.size = Pt(14)
pl.data_labels.font.bold = True
pl.data_labels.position = XL_LABEL_POSITION.OUTSIDE_END
ser = pl.series[0]
ser.format.fill.solid()
ser.format.fill.fore_color.rgb = TEAL
text(s, 7.5, 1.95, 5.2, 0.4, "Flere mønstre i samme kørsel", size=19, bold=True, color=NAVY, font=HEAD)
bullets(s, 7.5, 2.65, 5.25, 4.2, [
    [("Segment: ", {"bold": True}), "Groups 42,4 % og Online TA 34,9 % mod Direct 13,2 %"],
    [("Depositum: ", {"bold": True}), "Non Refund 96 %. Påfaldende, og skal undersøges før tolkning"],
    [("Sæson: ", {"bold": True}), "belægning højest i marts (ca. 66 %), lavest om sommeren (25 % i juli 2025)"],
    [("Helligdage: ", {"bold": True}), "46,6 % belægning mod 51,4 % på øvrige dage"],
    [("Korrelation med annullering: ", {"bold": True}), "lead time +0,28, parkering −0,25 (Spearman)"],
], size=14, gap=9)
footer(s)
notes(s, "Samlet er 27,5 procent annulleret. Non Refund med 96 procent annullering er det modsatte af, hvad man forventer, så jeg tolker det ikke, før jeg har set på de rå data. Helligdagsforskellen er en sammenhæng, ikke en forklaring, fordi weekender og sæsoner også falder på helligdage.")

# ---------------------------------------------------------------- 10 Forecast
s = new(light=True)
title(s, "Sæsonen i tallene og forecast for næste halve år", "Belægning pr. måned og forecast af ankomster")
text(s, 0.6, 1.85, 6, 0.35, "Belægning pr. måned × år", size=14, bold=True, color=TEAL_D)
picture(s, os.path.join(A, "occ.png"), 0.6, 2.25, 6.0, 2.6, name="Diagram: belægning")
text(s, 6.9, 1.85, 6, 0.35, "Forecast: ankomster, 6 måneder frem", size=14, bold=True, color=TEAL_D)
picture(s, os.path.join(A, "forecast.png"), 6.9, 2.25, 5.85, 2.6, name="Diagram: forecast")
box(s, 0.6, 5.2, 6.0, 1.7, fill=WHITE, line=RGBColor(0xD5, 0xDC, 0xE4))
text(s, 0.8, 5.3, 5.6, 0.35, "Hvad forecastet gør", size=15, bold=True, color=NAVY)
text(s, 0.8, 5.7, 5.6, 1.2, "Gentager sæsonmønsteret fra 102 måneders historik. Jan–jun 2027: ankomster 999–1.179 pr. måned, belægning 45–48 %. Båndet er spændet i historikken.", size=13)
box(s, 6.9, 5.2, 5.85, 1.7, fill=WHITE, line=RGBColor(0xD5, 0xDC, 0xE4))
text(s, 7.1, 5.3, 5.45, 0.35, "Hvad det ikke kan", size=15, bold=True, color=RED)
text(s, 7.1, 5.7, 5.45, 1.2, "Det kender ikke trend, prisændringer, nye begivenheder eller ændret antal værelser. Det er ikke en sandsynlighed og ikke et løfte.", size=13)
footer(s)
notes(s, "Omsætningen på værelser er 50,8 millioner US dollars i alt, i gennemsnit 447 dollars pr. booking, før skatter og gebyrer. Forecastet er regnet af servicen, ikke af en AI.")

# ---------------------------------------------------------------- 11 Prisforslag
s = new()
title(s, "Prisforslag med ét klik", "Næste skridt efter analysen, bygget i MIL-055")
picture(s, os.path.join(A, "suggest.jpg"), 0.6, 1.9, 7.4, 4.9, name="Skærmbillede: prisforslag")
text(s, 8.4, 1.95, 4.4, 0.4, "Sådan virker det", size=20, bold=True, color=NAVY, font=HEAD)
bullets(s, 8.4, 2.6, 4.4, 4.3, [
    [("Fast regel, ikke AI. ", {"bold": True}), "Belægning fra markedsanalysen udløser tillæg i højsæson og rabat i lavsæson"],
    [("Forklarligt. ", {"bold": True}), "Eksempel: Single, lavsæson, −15 %, 15,00 → 12,75, fordi belægning er 37,0 % (grænse 40 %)"],
    [("Manager godkender. ", {"bold": True}), "Ingen prisændring før klik; AI-teksten forklarer kun"],
    [("Sporbart. ", {"bold": True}), "Godkendelser logges; ændringen gælder nye bookinger"],
], size=14, gap=10)
footer(s)
notes(s, "Her er human-in-the-loop i praksis. Jeg valgte at regne forslagene ud fra tal og kun lade AI forklare dem, fordi prisen er en forretningsbeslutning, der skal kunne spores. Det er den del af læringsmålet om AI-baseret beslutningsstøtte.")

# ---------------------------------------------------------------- 12 Begrænsninger
s = new(light=True)
title(s, "Kritisk blik: hvad data og AI ikke kan sige", "En del af læringsmålet er at vide, hvornår man ikke skal stole på resultatet")
cards = [
    ("Datakvalitet", "Land er Unknown for 99,6 % af bookingerne. 794 bookinger har prisen 0. Poster uden nødvendige felter udelades og tælles."),
    ("Korrelation er ikke årsag", "Spearman finder kun jævne sammenhænge. Små grupper er markeret med stjerne, fx 16 ændringer = 100 %."),
    ("AI-tekster kontrolleret", "Flere AI-forslag til omsætning havde evidensen “0 bookings”. Derfor er teksterne mærket hypotese, og jeg tjekker dem mod tallene."),
    ("Forecast og estimater", "Forecastet kender ikke trend. Omsætning er før skatter og gebyrer og er ikke regnskab."),
]
for i, (hd, body) in enumerate(cards):
    x = 0.6 + (i % 2) * 6.2
    y = 1.95 + (i // 2) * 2.5
    box(s, x, y, 5.95, 2.3, fill=WHITE, line=RGBColor(0xD5, 0xDC, 0xE4))
    icon_circle(s, x + 0.25, y + 0.25, 0.55, "!" if i != 3 else "?", fill=AMBER if i != 2 else RED, color=NAVY if i != 2 else WHITE, size=20)
    text(s, x + 1.0, y + 0.3, 4.7, 0.4, hd, size=18, bold=True, color=NAVY, font=HEAD)
    text(s, x + 1.0, y + 0.85, 4.7, 1.4, body, size=14)
footer(s)
notes(s, "Det her dækker kompetencen om at vurdere AI's fortolkninger kritisk. Min ærlige vurdering: markedsanalyse er ikke mit domænesprog, så jeg har brugt AI til at forstå analyserne. Det gør det ekstra vigtigt at kontrollere svarene mod tallene og få en med hotelfaglig viden til at vurdere dem.")

# ---------------------------------------------------------------- 13 Udfordringer
s = new()
title(s, "Udfordringer og det jeg lærte", "Kolbs læringscirkel i praksis")
chal = [
    ("Python → C#", "Diagrammer laves i Python, men siden vises i C#. Løsning: JSON-skemaet fik et SVG-felt, så C# kun viser."),
    ("Systemer skal aftale kontrakten", "Det er ikke nok, at hver del virker. Formatet skal aftales og holdes i begge ender, og testes tidligt."),
    ("Domænet var nyt", "Jeg kendte ikke fagets begreber og brugte AI som støtte, men kontrollerede mod tallene."),
    ("AI koster tid", "phi4 uden GPU: næsten 20 minutter for hele analysen. Det skal med i vurderingen af produktion."),
]
for i, (hd, body) in enumerate(chal):
    y = 1.95 + i * 1.2
    icon_circle(s, 0.6, y + 0.1, 0.6, str(i + 1), fill=TEAL, size=18)
    text(s, 1.45, y, 5.4, 0.4, hd, size=17, bold=True, color=NAVY, font=HEAD)
    text(s, 1.45, y + 0.42, 5.4, 0.8, body, size=13, color=INK)
box(s, 7.3, 1.95, 5.45, 4.7, fill=NAVY)
text(s, 7.6, 2.15, 4.9, 0.4, "Kolb: cyklussen i markedsanalysen", size=17, bold=True, color=WHITE, font=HEAD)
for i, (k, v) in enumerate([("Erfaring", "Kørte analysen på 156.686 bookinger"),
                            ("Refleksion", "Non Refund 96 %? AI-tekster med 0 bookings?"),
                            ("Teori", "Spearman vs. kausalitet, valg af diagramtype"),
                            ("Eksperiment", "Nye perioder, forecast mod faktiske tal, prisforslag")]):
    y = 2.85 + i * 0.95
    box(s, 7.6, y, 1.5, 0.7, fill=TEAL, radius=0.15)
    text(s, 7.6, y, 1.5, 0.7, k, size=13, bold=True, color=WHITE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    text(s, 9.25, y, 3.3, 0.7, v, size=13, color=WHITE, anchor=MSO_ANCHOR.MIDDLE)
footer(s)
notes(s, "Kolbs cirkel: erfaring, refleksion, teori, eksperiment. Den vigtigste læring er, at flere systemer skal spille sammen, ikke bare arbejde sammen, og at AI-output altid skal kontrolleres.")

# ---------------------------------------------------------------- 14 Status
s = new(light=True)
title(s, "Status mod læringsmålene", "Det er dokumenteret, og det mangler stadig")
box(s, 0.6, 1.9, 6.0, 4.95, fill=WHITE, line=RGBColor(0xD5, 0xDC, 0xE4))
text(s, 0.9, 2.05, 5.4, 0.4, "Dokumenteret", size=20, bold=True, color=GREEN, font=HEAD)
bullets(s, 0.9, 2.65, 5.4, 4.1, [
    "Sammenligning af 5 LLM'er (kræver ≥3)",
    "4 statistiske beregninger: annulleringsrate, belægning, helligdagsbelægning, omsætning",
    "Mere end 4 visualiseringer med begrundelse pr. diagramtype",
    "6 trends og mønstre med beregning",
    "Dataenes begrænsninger beskrevet",
    "Ensartede artefakter: skabelon, scripts og tjekliste",
    "Fejl og usikkerhed dokumenteret",
], size=14, gap=7)
box(s, 6.75, 1.9, 6.0, 4.95, fill=WHITE, line=RGBColor(0xD5, 0xDC, 0xE4))
text(s, 7.05, 2.05, 5.4, 0.4, "Mangler endnu", size=20, bold=True, color=RED, font=HEAD)
bullets(s, 7.05, 2.65, 5.4, 4.1, [
    "OCR/ML-prototype til pasnummer, navn og nationalitet",
    "Mindst 3 promptstrategier, dokumenteret",
    "Mindst 10 dokumenterede testcases",
    "Systematisk evaluering af AI-opsummeringerne",
    "Kurset: Matplotlib og dokumentation af Python-for-AI",
    "Samlet fortolkning og konklusion som beslutningsstøtte",
], size=14, gap=7)
footer(s)
notes(s, "Her er det vigtigt at være ærlig over for censor: Checklisten i læringsmålene viser, hvad der er afkrydset, og hvad der mangler. OCR/ML-delen er planlagt som milestone 4 i november.")

# ---------------------------------------------------------------- 15 Afslutning
s = new(dark=True)
count[0] += 1
text(s, 0.6, 0.6, 12, 0.8, "Næste skridt", size=38, bold=True, color=WHITE, font=HEAD)
for i, (hd, body) in enumerate([
    ("OCR/ML til pas", "Pasbillede → OCR → tekst → strukturerede oplysninger, med nøjagtighed og fejl dokumenteret."),
    ("Systematisk AI-evaluering", "Mindst 3 promptstrategier og 10 testcases; sammenlign AI-tekster mod tallene."),
    ("Undersøg Non Refund", "Find ud af, hvorfor 96 % annullerer, før resultatet bruges i prisregler."),
]):
    x = 0.6 + i * 4.1
    box(s, x, 1.9, 3.9, 3.2, fill=RGBColor(0x1A, 0x25, 0x3F))
    icon_circle(s, x + 0.3, 2.15, 0.6, str(i + 1), fill=AMBER, color=NAVY, size=20)
    text(s, x + 0.3, 2.95, 3.4, 0.5, hd, size=19, bold=True, color=WHITE, font=HEAD)
    text(s, x + 0.3, 3.55, 3.4, 1.5, body, size=14, color=RGBColor(0xD8, 0xE2, 0xEE))
text(s, 0.6, 5.7, 12, 0.6, "Tak. Spørgsmål?", size=30, bold=True, color=AMBER, font=HEAD)
text(s, 0.6, 6.4, 12, 0.4, "nfhotel.devmatiker.com · github.com/NF-Hotel/NFHotel", size=14, color=RGBColor(0xB8, 0xC4, 0xD6))
notes(s, "Afslut med de tre næste skridt og åbn for spørgsmål.")

prs.save(OUT)
print("saved", OUT)
