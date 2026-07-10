# -*- coding: utf-8 -*-
"""Erzeugt alle PDFs: Themen-Dossiers (themen/<id>.pdf), DaZ/DaF-Arbeitsblätter
(arbeitsblaetter/...), Literatur (literatur/literatur-de-en.pdf).
Quelle: content.py (einzige Inhaltsquelle).
Sprachvergleich Deutsch–Englisch · Dr. Ergun Özsoy, LMU München."""
import os, datetime
from weasyprint import HTML
import content as C
try:
    import markdown as _md
except ImportError:
    _md = None

OUT=os.path.dirname(os.path.abspath(__file__))  # Skript-Ordner – funktioniert lokal & in CI
for d in ("themen","arbeitsblaetter","literatur"):
    os.makedirs(f"{OUT}/{d}", exist_ok=True)

GREEN="#00883A"; GOLD="#C8A45C"; INK="#222629"
DATE=datetime.date.today().strftime("%d.%m.%Y")

CSS=f"""
@page {{ size:A4; margin:20mm 18mm 22mm 18mm;
  @top-left {{ content:"Kontrastive Linguistik DE \\2194 EN"; font:8pt 'Georgia',serif; color:#888; }}
  @top-right {{ content:"Dr. Ergun \\00D6zsoy \\00B7 LMU M\\00FCnchen"; font:8pt 'Georgia',serif; color:#888; }}
  @bottom-left {{ content:"\\00A9 Dr. Ergun \\00D6zsoy \\2013 alle Rechte vorbehalten"; font:8pt sans-serif; color:#999; }}
  @bottom-right {{ content:"Seite " counter(page) " / " counter(pages); font:8pt sans-serif; color:#999; }} }}
*{{box-sizing:border-box}}
body{{font-family:'Calibri','Segoe UI',sans-serif;color:{INK};font-size:10.5pt;line-height:1.5}}
h1,h2,h3{{font-family:'Georgia','Times New Roman',serif;color:{GREEN};line-height:1.25}}
.brandbar{{height:6px;background:{GREEN};border-radius:3px;margin-bottom:4mm}} .brandbar.gold{{background:{GOLD}}}
.kicker{{font-size:8.5pt;letter-spacing:.12em;text-transform:uppercase;color:{GOLD};font-weight:700}}
h1{{font-size:21pt;margin:1mm 0 1mm}} .lead{{color:#555;font-size:10.5pt;margin:0 0 5mm}}
.block{{border:1px solid #e3e3e3;border-left:4px solid {GREEN};border-radius:6px;padding:4mm 5mm;margin:0 0 5mm;break-inside:avoid}}
.block .num{{display:inline-block;min-width:18px;color:{GOLD};font-weight:700;font-family:'Georgia',serif}}
.block h2{{font-size:13pt;margin:0 0 2mm}}
table{{width:100%;border-collapse:collapse;margin:2mm 0;font-size:9.6pt}}
th,td{{border:1px solid #dcdcdc;padding:2mm 3mm;text-align:left;vertical-align:top}}
th{{background:#f3f6f3;color:{GREEN};font-family:'Georgia',serif}}
td.de{{background:#fbfdfb}} td.en{{background:#fdfbf6}}
.ex{{font-family:'Consolas','Courier New',monospace}}
.eng{{font-family:'Consolas','Courier New',monospace;font-style:italic;color:#9a6a12;font-weight:600}}
td.de .ex{{color:#16407a}}
td.en .ex{{color:#9a6a12;font-style:italic}}
.err{{color:#b3261e;text-decoration:line-through}} .err::before{{content:"\\2717 ";text-decoration:none;font-weight:700}}
.ok{{color:{GREEN};font-weight:600}} .ok::before{{content:"\\2713 ";font-weight:700}}
.tag.typ.il{{background:#f6efe1;color:#8a6b22;border-color:#e6d4a6}} .tag.typ.al{{background:#eef1f6;color:#3a4a66;border-color:#cdd6e6}}
.tag{{display:inline-block;font-size:8pt;padding:1px 7px;border-radius:10px;background:#eef3ee;color:{GREEN};border:1px solid #cfe0cf}}
.tag.cat{{background:#f6efe1;color:#8a6b22;border-color:#e6d4a6}}
ul,ul.li{{margin:1mm 0 1mm 5mm;padding:0}} li{{margin:1mm 0}}
.note{{font-size:9pt;color:#666;font-style:italic}}
.foot{{margin-top:6mm;padding-top:3mm;border-top:1px solid #e3e3e3;font-size:8.5pt;color:#888}}
.task{{border:1px solid #e3e3e3;border-radius:6px;padding:3.5mm 4mm;margin:0 0 4mm;break-inside:avoid}}
.task h3{{font-size:11.5pt;margin:0 0 1.5mm;color:{INK}}}
.task .meta{{font-size:8.5pt;color:{GOLD};font-weight:700;text-transform:uppercase;letter-spacing:.08em}}
.line{{border-bottom:1px solid #bbb;min-height:6mm}}
.litcat{{font-family:'Georgia',serif;color:{GREEN};font-size:12pt;border-bottom:1px solid #e3e3e3;padding-bottom:1.5mm;margin:5mm 0 2mm;break-after:avoid}}
.lit{{font-size:9.6pt;padding:1.6mm 0;border-bottom:1px dashed #eee;break-inside:avoid}}
.lit .au{{font-weight:600}} .lit .ti{{font-style:italic}} .lit .q{{color:#666}}
.mk{{font-size:7.5pt;border-radius:8px;padding:0 5px;margin-left:4px}} .mk.proj{{background:#e2f0e6;color:#04632c}} .mk.cur{{background:#f6efe1;color:#8a6b22}}
"""

def render(path, inner, gold=False):
    HTML(string=f"<!doctype html><html lang='de'><head><meta charset='utf-8'><style>{CSS}</style></head>"
                f"<body><div class='brandbar {'gold' if gold else ''}'></div>{inner}</body></html>"
        ).write_pdf(path)
    print("  ->", path.split("/")[-1], os.path.getsize(path), "B")

# ---- Themen-Dossiers ------------------------------------------------------
def topic_pdf(tid, d):
    parts=[f'<div class="kicker">{d["modul"]} &middot; Sprachvergleich</div>'
           f'<h1>{d["titel"]}</h1><p class="lead">{d["lead"]}</p>']
    for i,b in enumerate(d["blocks"]):
        parts.append(f'<div class="block"><h2><span class="num">{i+1}</span>{C.BLOCKNAMES[i]}</h2>{b}</div>')
    parts.append(f'<div class="foot">Lernerformen nach Ursache: <i>intralingual</i> (systematisch) vs. '
                 f'<i>interlingual</i> (aus der L1 Englisch). Quellen: siehe Literatur-Seite. '
                 f'&middot; Stand: {DATE} &middot; Konzept &amp; Inhalt: Dr. Ergun &Ouml;zsoy, LMU M&uuml;nchen.</div>')
    render(f"{OUT}/themen/{tid}.pdf", "".join(parts))

print("Themen-Dossiers:")
for tid,d in C.DETAIL.items():
    topic_pdf(tid,d)

# ---- Arbeitsblätter -------------------------------------------------------
def worksheet(path, meta, intro, tasks, solutions):
    head=(f'<div class="kicker">DaZ/DaF-Arbeitsblatt &middot; {meta["modul"]}</div><h1>{meta["titel"]}</h1>'
          f'<p class="lead">{meta["niveau"]} &middot; {meta["ziel"]}</p><p>{intro}</p>')
    body="".join(f'<div class="task"><div class="meta">Aufgabe {i+1} &middot; {t["typ"]}</div>'
                 f'<h3>{t["titel"]}</h3>{t["html"]}</div>' for i,t in enumerate(tasks))
    sol=('<div style="break-before:page"></div><div class="brandbar gold"></div>'
         '<div class="kicker">L&ouml;sungsschl&uuml;ssel</div>'
         f'<h1 style="font-size:17pt">L&ouml;sungen &amp; Lehrerhinweise</h1>{solutions}')
    foot=(f'<div class="foot">DaZ/DaF-Material zum Sprachvergleich DE&ndash;EN &middot; '
          f'Konzept: Dr. Ergun &Ouml;zsoy, LMU M&uuml;nchen &middot; Stand: {DATE}</div>')
    render(path, head+body+foot+sol, gold=True)

print("Arbeitsblätter:")

# 1) Substantivgroßschreibung -------------------------------------------------
worksheet(f"{OUT}/arbeitsblaetter/ab_grossschreibung.pdf",
 {"modul":"Laut &amp; Schrift / Orthographie","titel":"Substantivgro&szlig;schreibung",
  "niveau":"A1&ndash;B1","ziel":"Alle Nomen gro&szlig; &ndash; Artikelprobe &amp; Nominalisierung"},
 "Im Deutschen schreibt man <b>alle</b> Nomen gro&szlig; (<span class='ex'>das Haus, die Liebe, das Lesen</span>), im Englischen nur Eigennamen. Achtung: Nationalit&auml;tsadjektive sind im Deutschen <b>klein</b> (<span class='ex'>die deutsche Sprache</span>).",
 [{"typ":"Nomen finden","titel":"Unterstreiche und schreibe gro&szlig;","html":"""
   <p>Markiere jedes Nomen und schreibe den Satz korrekt (englische Kleinschreibung korrigieren).</p>
   <table><tr><th>Lernersatz (zu klein)</th><th>richtig</th></tr>
   <tr><td class="ex">ich lese ein buch.</td><td class="line"></td></tr>
   <tr><td class="ex">der mann kauft einen apfel.</td><td class="line"></td></tr>
   <tr><td class="ex">meine schwester hat einen hund.</td><td class="line"></td></tr></table>"""},
  {"typ":"Artikelprobe","titel":"Nomen oder nicht? der/die/das davor?","html":"""
   <p>Wenn ein Artikel davor passt, ist es ein Nomen &rarr; gro&szlig;. Entscheide.</p>
   <table><tr><th>Wort im Satz</th><th>Nomen? (ja/nein)</th><th>gro&szlig;/klein</th></tr>
   <tr><td class="ex">Beim <u>schwimmen</u> ...</td><td class="line"></td><td class="line"></td></tr>
   <tr><td class="ex">Das <u>gute</u> gewinnt.</td><td class="line"></td><td class="line"></td></tr>
   <tr><td class="ex">Er kann gut <u>singen</u>.</td><td class="line"></td><td class="line"></td></tr></table>"""},
  {"typ":"Kontrastiv","titel":"Englische Regel vs. deutsche Regel","html":"""
   <p>Im Englischen gro&szlig;, im Deutschen klein (oder umgekehrt)? Korrigiere.</p>
   <table><tr><th>Lernersatz</th><th>richtig</th></tr>
   <tr><td class="ex">die Englische Grammatik</td><td class="line"></td></tr>
   <tr><td class="ex">ich lerne Deutsch am montag</td><td class="line"></td></tr></table>"""}],
 """<ul><li><b>A1:</b> Ich lese ein <b>Buch</b>. &middot; Der <b>Mann</b> kauft einen <b>Apfel</b>. &middot; Meine <b>Schwester</b> hat einen <b>Hund</b>.</li>
    <li><b>A2:</b> Beim <b>Schwimmen</b> (Nomen, gro&szlig;) &middot; Das <b>Gute</b> (nominalisiert, gro&szlig;) &middot; gut <b>singen</b> (Verb, klein).</li>
    <li><b>A3:</b> die <b>englische</b> Grammatik (Adjektiv klein!) &middot; Ich lerne <b>Deutsch</b> am <b>Montag</b> (Sprache &amp; Wochentag: Nomen, gro&szlig;).</li>
    <li class="note">Merksatz: <b>Nomen immer gro&szlig;</b>; Nationalit&auml;ts<i>adjektive</i> klein (englische Gewohnheit umlenken). Artikelprobe hilft bei Nominalisierungen.</li></ul>""")

# 2) Genus, Artikel & Kasus ---------------------------------------------------
worksheet(f"{OUT}/arbeitsblaetter/ab_genus-kasus.pdf",
 {"modul":"Nomen","titel":"Genus, Artikel &amp; Kasus","niveau":"A2&ndash;B1","ziel":"der/die/das sichern; Nominativ vs. Akkusativ; Pronomen-Kongruenz"},
 "Das Englische hat kein Genus (<span class='eng'>the</span>) und Kasus nur am Pronomen (<span class='eng'>he/him</span>). Diese &Uuml;bungen sichern <b>der/die/das</b> und die Formen <b>der/den/dem</b>.",
 [{"typ":"Genus-Heuristik","titel":"der, die oder das?","html":"""
   <p>Nutze die Endungen-Regeln (<span class="ex">-ung/-heit/-keit &rarr; die</span>; <span class="ex">-chen/-ment &rarr; das</span>; <span class="ex">-er (Person)/Tage &rarr; der</span>).</p>
   <table><tr><th>Nomen</th><th>Artikel</th><th>Nomen</th><th>Artikel</th></tr>
   <tr><td class="ex">Zeitung</td><td class="line"></td><td class="ex">M&auml;dchen</td><td class="line"></td></tr>
   <tr><td class="ex">Freiheit</td><td class="line"></td><td class="ex">Lehrer</td><td class="line"></td></tr>
   <tr><td class="ex">Nation</td><td class="line"></td><td class="ex">Montag</td><td class="line"></td></tr></table>"""},
  {"typ":"Nom / Akk","titel":"der oder den? (Subjekt vs. Objekt)","html":"""
   <p>Subjekt &rarr; Nominativ (der), direktes Objekt &rarr; Akkusativ (den, nur maskulin sichtbar).</p>
   <table><tr><th>Satz</th><th>der/den?</th></tr>
   <tr><td class="ex">___ Mann liest. (Subjekt)</td><td class="line"></td></tr>
   <tr><td class="ex">Ich sehe ___ Mann. (Objekt)</td><td class="line"></td></tr>
   <tr><td class="ex">Ich helfe ___ Mann. (helfen + Dativ)</td><td class="line"></td></tr></table>"""},
  {"typ":"Kontrastiv / Pronomen","titel":"it oder er/sie/es?","html":"""
   <p>Im Deutschen richtet sich das Pronomen nach dem <b>grammatischen</b> Genus. Erg&auml;nze er/sie/es.</p>
   <table><tr><th>Satz</th><th>Pronomen</th></tr>
   <tr><td class="ex">Der Tisch ist neu. ___ ist aus Holz.</td><td class="line"></td></tr>
   <tr><td class="ex">Das M&auml;dchen lacht. ___ ist froh.</td><td class="line"></td></tr>
   <tr><td class="ex">Die Lampe ist an. ___ ist hell.</td><td class="line"></td></tr></table>"""}],
 """<ul><li><b>A1:</b> die Zeitung &middot; das M&auml;dchen &middot; die Freiheit &middot; der Lehrer &middot; die Nation &middot; der Montag.</li>
    <li><b>A2:</b> <b>Der</b> Mann liest. &middot; Ich sehe <b>den</b> Mann. &middot; Ich helfe <b>dem</b> Mann (Dativ).</li>
    <li><b>A3:</b> Der Tisch &rarr; <b>Er</b> (nicht &bdquo;it&ldquo;) &middot; Das M&auml;dchen &rarr; <b>Es</b> (grammatisch neutrum) &middot; Die Lampe &rarr; <b>Sie</b>.</li>
    <li class="note">Br&uuml;cke zum Englischen: <span class="eng">him = ihm</span>, <span class="eng">who/whom = der/den</span> &ndash; Kasus ist aus dem Pronomen bekannt.</li></ul>""")

# 3) Wortstellung: V2 & Satzklammer ------------------------------------------
worksheet(f"{OUT}/arbeitsblaetter/ab_wortstellung.pdf",
 {"modul":"Syntax","titel":"Wortstellung: Verbzweit &amp; Satzklammer","niveau":"A2&ndash;B1","ziel":"V2 &amp; Inversion sichern, Klammer schlie&szlig;en, Nebensatz verbfinal"},
 "Im Englischen gilt festes <b>SVO</b>. Im Deutschen steht das finite Verb im Hauptsatz an <b>2. Stelle</b> (auch nach einem vorangestellten Glied &rarr; Inversion) &ndash; im Nebensatz aber am <b>Ende</b>.",
 [{"typ":"V2 &amp; Inversion","titel":"Bring das Verb an die 2. Stelle","html":"""
   <p>Beginne mit dem <u>fett</u> markierten Glied. Achtung: nicht die englische Folge &bdquo;Heute ich gehe&ldquo;!</p>
   <table><tr><th>durcheinander</th><th>richtig</th></tr>
   <tr><td class="ex"><b>Morgen</b> / ich / fahre / nach Berlin</td><td class="line"></td></tr>
   <tr><td class="ex"><b>Heute</b> / wir / lernen / Deutsch</td><td class="line"></td></tr></table>"""},
  {"typ":"Klammer schlie&szlig;en","titel":"Zweites Verbteil ans Ende","html":"""
   <table><tr><th>Lernersatz (englische Folge)</th><th>richtig</th></tr>
   <tr><td class="ex">Ich habe gekauft ein Buch.</td><td class="line"></td></tr>
   <tr><td class="ex">Ich will lernen Deutsch.</td><td class="line"></td></tr>
   <tr><td class="ex">Ich aufstehe um sieben.</td><td class="line"></td></tr></table>"""},
  {"typ":"Nebensatz","titel":"Verb ans Ende (weil/dass)","html":"""
   <table><tr><th>Hauptsatz + &hellip;</th><th>Nebensatz</th></tr>
   <tr><td>Er kommt nicht, weil &hellip; (er / ist / krank)</td><td class="line"></td></tr>
   <tr><td>Ich wei&szlig;, dass &hellip; (du / Deutsch / lernst)</td><td class="line"></td></tr></table>"""}],
 """<ul><li><b>A1:</b> Morgen <b>fahre</b> ich nach Berlin. &middot; Heute <b>lernen</b> wir Deutsch. (finites Verb an 2. Stelle, Inversion)</li>
    <li><b>A2:</b> Ich habe ein Buch <b>gekauft</b>. &middot; Ich will Deutsch <b>lernen</b>. &middot; Ich <b>stehe</b> um sieben <b>auf</b>.</li>
    <li><b>A3:</b> &hellip;, weil er krank <b>ist</b>. &middot; &hellip;, dass du Deutsch <b>lernst</b>. (Verb am Ende)</li>
    <li class="note">Kontrast: Englisch ist immer SVO; Deutsch wechselt zwischen V2 (Hauptsatz) und verbfinal (Nebensatz). Vgl. engl. V2-Reste: <span class="eng">Never have I seen &hellip;</span></li></ul>""")

# 4) Präpositionen & Kasus ----------------------------------------------------
worksheet(f"{OUT}/arbeitsblaetter/ab_praepositionen.pdf",
 {"modul":"Pr&auml;positionen","titel":"Pr&auml;positionen &amp; Kasus","niveau":"A2&ndash;B1","ziel":"Wechselpr&auml;positionen (wohin?/wo?), feste Rektion"},
 "Englische Pr&auml;positionen regieren keinen Kasus. Deutsche schon: <b>wohin?</b> &rarr; Akkusativ, <b>wo?</b> &rarr; Dativ. Englisch trennt Richtung/Ort lexikalisch (<span class='eng'>into/in, onto/on</span>).",
 [{"typ":"wohin? / wo?","titel":"Akkusativ oder Dativ?","html":"""
   <table><tr><th>Satz</th><th>Akk / Dat?</th></tr>
   <tr><td class="ex">Ich gehe in ___ Schule. (wohin?)</td><td class="line"></td></tr>
   <tr><td class="ex">Ich bin in ___ Schule. (wo?)</td><td class="line"></td></tr>
   <tr><td class="ex">Das Bild h&auml;ngt an ___ Wand. (wo?)</td><td class="line"></td></tr>
   <tr><td class="ex">Ich h&auml;nge das Bild an ___ Wand. (wohin?)</td><td class="line"></td></tr></table>"""},
  {"typ":"into/in &harr; Akk/Dat","titel":"&Uuml;bersetze die Relation","html":"""
   <table><tr><th>Englisch</th><th>Deutsch (Kasus!)</th></tr>
   <tr><td class="eng">into the house (wohin?)</td><td>in ___ Haus</td></tr>
   <tr><td class="eng">in the house (wo?)</td><td>in ___ Haus</td></tr>
   <tr><td class="eng">onto the table (wohin?)</td><td>auf ___ Tisch</td></tr></table>"""},
  {"typ":"Rektion / Wahl","titel":"Fester Kasus &amp; richtige Pr&auml;position","html":"""
   <table><tr><th>Lernersatz</th><th>richtig</th></tr>
   <tr><td class="ex">mit der Auto</td><td class="line"></td></tr>
   <tr><td class="ex">Ich warte f&uuml;r dich. (engl. wait for)</td><td class="line"></td></tr></table>"""}],
 """<ul><li><b>A1:</b> in <b>die</b> Schule (Akk) &middot; in <b>der</b> Schule (Dat) &middot; an <b>der</b> Wand (Dat) &middot; an <b>die</b> Wand (Akk).</li>
    <li><b>A2:</b> in <b>das/ins</b> Haus (Akk) &middot; in <b>dem/im</b> Haus (Dat) &middot; auf <b>den</b> Tisch (Akk). (into/onto &rarr; Akk; in/on &rarr; Dat)</li>
    <li><b>A3:</b> mit <b>dem</b> Auto (mit + Dativ) &middot; Ich warte <b>auf</b> dich (nicht &bdquo;f&uuml;r&ldquo; &ndash; feste Verb-Pr&auml;position).</li>
    <li class="note">Englisch kodiert Richtung/Ort schon lexikalisch (into/in) &ndash; im Deutschen wandert die Unterscheidung auf den Kasus.</li></ul>""")

# ---- Literatur-PDF --------------------------------------------------------
print("Literatur:")
lit=[f'<div class="kicker">Bibliografie &middot; Sprachvergleich DE&ndash;EN / DaZ-DaF</div>',
     '<h1>Literatur</h1>', f'<p class="lead">{C.LIT_INTRO}</p>']
for cat,items in C.LIT.items():
    lit.append(f'<div class="litcat">{cat}</div>')
    for e in items:
        marks=(('<span class="mk proj">&#9679; im Projekt</span>' if e.get("proj") else '')
              +('<span class="mk cur">&#10022; aktuell</span>' if e.get("cur") else ''))
        lit.append(f'<div class="lit"><span class="au">{e["a"]}</span> ({e["y"]}): '
                   f'<span class="ti">{e["t"]}</span>. <span class="q">{e["q"]}.</span>{marks}</div>')
lit.append(f'<div class="foot">Auswahl als Referenzmaterial &middot; Stand: {DATE} &middot; '
           f'Konzept &amp; alle Rechte: Dr. Ergun &Ouml;zsoy, LMU M&uuml;nchen.</div>')
render(f"{OUT}/literatur/literatur-de-en.pdf", "".join(lit))

# ---- Werkstattbericht-PDF (aus YAMA_WERKSTATT.md) -------------------------
print("Werkstatt:")
wpath=f"{OUT}/YAMA_WERKSTATT.md"
if _md and os.path.exists(wpath):
    src=open(wpath, encoding="utf-8").read()
    # den ersten H1-Titel als Kicker/H1 herausl&ouml;sen, Rest als Body
    body_html=_md.markdown(src, extensions=["tables","sane_lists"])
    inner=(f'<div class="kicker">Werkstattbericht &middot; Digital-Humanities-Projekt</div>{body_html}')
    render(f"{OUT}/werkstatt.pdf", inner, gold=True)
else:
    print("  (uebersprungen: markdown fehlt oder Datei nicht gefunden)")

# ---- Fazit-PDF ------------------------------------------------------------
print("Fazit:")
fz=C.FAZIT
fparts=[f'<div class="kicker">{fz["untertitel"]} &middot; Sprachvergleich</div>'
        f'<h1>{fz["titel"]}</h1><p class="lead">{fz["lead"]}</p>']
for i,(h,b) in enumerate(fz["blocks"]):
    fparts.append(f'<div class="block"><h2><span class="num">{i+1}</span>{h}</h2>{b}</div>')
fparts.append(f'<div class="foot">Stand: {DATE} &middot; Konzept &amp; Inhalt: Dr. Ergun &Ouml;zsoy, LMU M&uuml;nchen.</div>')
render(f"{OUT}/fazit.pdf", "".join(fparts))

print("\nFERTIG.")
