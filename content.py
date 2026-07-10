# -*- coding: utf-8 -*-
"""
Einzige Inhaltsquelle für Plattform + PDFs.
Sprachvergleich Deutsch–Englisch · DaZ/DaF · Dr. Ergun Özsoy, LMU München.

Perspektive: Deutsch als Ziel-/Zweitsprache aus englischer L1-Perspektive
(englische Muttersprachler, die Deutsch lernen).

Konvention: englische Tokens stehen in <span class="eng"> (kursiv, eigene Farbe),
deutsche/neutrale Beispiele in <span class="ex">. Quellen ausschließlich auf der
Literatur-Seite – im Inhalt keine Zitate/Quellenkürzel.
"""

BLOCKNAMES = ["Kontrastiver Befund","Didaktik & DaZ-Relevanz","Interferenzanalyse",
              "Korrektur & Förderung","Interkulturalität & Mehrsprachigkeit als Ressource"]

# Strukturbaum (Reihenfolge = Navigation). status: "ready" | "draft"
MODULES = [
 {"id":"m1","name":"Modul I · Laut & Schrift","topics":[
   {"id":"alphabet","t":"Alphabet & Buchstaben-Lautwerte","s":"ready","desc":"Gleiches Alphabet – aber w/v/j/z und ei/ie/eu klingen anders.","prio":{"h":"mittel","f":"gering","l":"hoch"}},
   {"id":"konsonanten","t":"ch- und r-Laut & Konsonanten","s":"ready","desc":"ach-/ich-Laut und das uvulare r existieren im Englischen nicht.","prio":{"h":"hoch","f":"hoch","l":"mittel"}},
   {"id":"auslaut","t":"Auslautverhärtung","s":"ready","desc":"Deutsch entstimmt am Wortende – Englisch nicht.","prio":{"h":"mittel","f":"mittel","l":"gering"}},
   {"id":"vokale","t":"Vokale: Länge & Umlaute (ä ö ü)","s":"ready","desc":"Vokallänge phonemisch; ö/ü ohne englische Entsprechung.","prio":{"h":"hoch","f":"hoch","l":"mittel"}},
   {"id":"grossschreibung","t":"Substantivgroßschreibung & ß","s":"ready","desc":"Deutsch schreibt alle Nomen groß; Englisch nur Eigennamen.","prio":{"h":"hoch","f":"mittel","l":"hoch"}},
 ]},
 {"id":"m2","name":"Modul II · Morphologie","topics":[
   {"id":"genus","t":"Genus & Artikel","s":"ready","desc":"der/die/das – Englisch kennt kein grammatisches Genus.","prio":{"h":"hoch","f":"hoch","l":"hoch"}},
   {"id":"kasus","t":"Kasus (Nom · Akk · Dat · Gen)","s":"ready","desc":"Vier Fälle am Artikel; Englisch nur an Pronomen (he/him).","prio":{"h":"hoch","f":"hoch","l":"hoch"}},
   {"id":"plural","t":"Plural","s":"ready","desc":"Fünf Pluraltypen + Umlaut vs. englisches -s.","prio":{"h":"hoch","f":"mittel","l":"hoch"}},
   {"id":"adjektiv","t":"Adjektivdeklination","s":"ready","desc":"Stark/schwach/gemischt – Englisch flektiert Adjektive gar nicht.","prio":{"h":"hoch","f":"hoch","l":"hoch"}},
   {"id":"pronomen","t":"Pronomen & Anrede (du/Sie)","s":"ready","desc":"Kasus am Pronomen; du/Sie – Englisch hat nur „you“.","prio":{"h":"mittel","f":"mittel","l":"mittel"}},
   {"id":"verben","t":"Verben & trennbare Verben","s":"ready","desc":"Trennbare Vorsilben & Verbklammer; Ablaut als gemeinsames Erbe.","prio":{"h":"hoch","f":"mittel","l":"hoch"}},
   {"id":"zeit","t":"Zeitformen & Aspekt","s":"ready","desc":"Kein Progressiv (I am reading); Perfekt als mündliche Vergangenheit.","prio":{"h":"hoch","f":"hoch","l":"hoch"}},
   {"id":"konjunktiv","t":"Konjunktiv II & I","s":"ready","desc":"Irrealis/Höflichkeit (would) vs. K I der indirekten Rede.","prio":{"h":"mittel","f":"mittel","l":"mittel"}},
   {"id":"passiv","t":"Passiv","s":"ready","desc":"werden- vs. sein-Passiv; Englisch verdeckt das mit „to be“.","prio":{"h":"mittel","f":"gering","l":"mittel"}},
   {"id":"praep","t":"Präpositionen & Wechselpräpositionen","s":"ready","desc":"Kasusrektion; wohin?→Akk / wo?→Dat – Englisch ohne Kasus.","prio":{"h":"hoch","f":"hoch","l":"hoch"}},
 ]},
 {"id":"m3","name":"Modul III · Syntax","topics":[
   {"id":"satzart","t":"Satzarten & Fragebildung","s":"ready","desc":"Inversion (Kommst du?) vs. englisches do-support (Do you…?).","prio":{"h":"hoch","f":"mittel","l":"mittel"}},
   {"id":"wortstell","t":"Wortstellung (V2 & Satzklammer)","s":"ready","desc":"Verbzweit + Klammer vs. festes englisches SVO.","prio":{"h":"hoch","f":"hoch","l":"hoch"}},
   {"id":"nebensatz","t":"Nebensatz & Verbendstellung","s":"ready","desc":"Verb ans Ende (…, weil er kommt); Englisch bleibt SVO.","prio":{"h":"hoch","f":"hoch","l":"hoch"}},
   {"id":"negation","t":"Negation (nicht & kein)","s":"ready","desc":"nicht/kein & Stellung – ohne „do“-Hilfsverb.","prio":{"h":"mittel","f":"mittel","l":"mittel"}},
   {"id":"modalpart","t":"Modalpartikeln (doch, ja, mal …)","s":"ready","desc":"Abtönung ohne direktes englisches Äquivalent.","prio":{"h":"mittel","f":"gering","l":"gering"}},
 ]},
]

# Hilfsfunktionen -----------------------------------------------------------
def e(s):  # englisches Token (kursiv, eigene Farbe) – die L1
    return f'<span class="eng">{s}</span>'
def d(s):  # deutsches/neutrales Beispiel-Token
    return f'<span class="ex">{s}</span>'

def T(rows, head=("Merkmal","Deutsch","Englisch")):
    h="".join(f"<th>{x}</th>" for x in head)
    body=""
    for r in rows:
        body+=f'<tr><td>{r[0]}</td><td class="de">{r[1]}</td><td class="en">{r[2]}</td></tr>'
    return f"<table><tr>{h}</tr>{body}</table>"

def ITAB(rows):  # (lernerform, zielform, ursache, typ) ; typ: 'interlingual'|'intralingual'
    body=""
    for f,z,u,typ in rows:
        cls="il" if typ=="interlingual" else "al"
        body+=(f'<tr><td><span class="err">{f}</span></td>'
               f'<td><span class="ok">{z}</span></td><td>{u}</td>'
               f'<td><span class="tag typ {cls}">{typ}</span></td></tr>')
    return ('<table><tr><th>Lernerform</th><th>Zielform</th><th>Ursache</th>'
            f'<th>Typ</th></tr>{body}</table>')

def NOTE(s): return f'<p class="note">{s}</p>'
def P(s): return f"<p>{s}</p>"

# === DETAIL: 5 Blöcke je Thema ============================================
DETAIL = {}

# ---------------------------------------------------------------- Modul I --
DETAIL["alphabet"]=dict(
 modul="Modul I · Laut & Schrift", titel="Alphabet & Buchstaben-Lautwerte",
 lead="Deutsch und Englisch teilen das lateinische Alphabet – doch viele Buchstaben tragen andere Lautwerte. Gerade weil sie vertraut aussehen, werden die falschen Werte unbemerkt übertragen (die Buchstaben sind „falsche Freunde“).",
 blocks=[
  T([("⟨w⟩",f"[v] – {d('Wein, Wasser')}",f"[w] – {e('wine, water')}"),
    ("⟨v⟩",f"[f] – {d('Vater, viel')}",f"[v] – {e('very, van')}"),
    ("⟨j⟩",f"[j] – {d('ja, Jahr')}",f"[dʒ] – {e('jam, June')}"),
    ("⟨z⟩",f"[ts] – {d('Zeit, Zoo')}",f"[z] – {e('zoo, zebra')}"),
    ("⟨s⟩ vor Vokal",f"[z] – {d('Sonne, Sie')}",f"[s] – {e('sun, see')}"),
    ("Digraphe",f"{d('ei')}=[aɪ], {d('ie')}=[iː], {d('eu/äu')}=[ɔɪ]",f"{e('ei')} oft [iː]; {e('ie')} variabel"),],
    head=("Graphem","Deutsch","Englisch"))
  +NOTE("Kernpunkt: Ein Buchstabe hat keinen universellen Lautwert. Die englischen Werte sind nicht falsch – sie gelten nur in der L1."),
  P("Betroffen sind Aussprache <i>und</i> Lesetechnik: Wer ⟨w v j z⟩ englisch liest, verliest sich systematisch. Besonders zäh ist ⟨w⟩=[v] und die Verwechslung von ⟨ei⟩ und ⟨ie⟩ (<i>Wein</i> vs. <i>wie</i>). Früh im Lernprozess zu sichern."),
  ITAB([("[w]ein für Wein","[v]ein",f"englisches ⟨w⟩ = [w]","interlingual"),
        ("[v]ater für Vater","[f]ater",f"englisches ⟨v⟩ = [v]","interlingual"),
        ("[dʒ]a für ja","[j]a",f"englisches ⟨j⟩ = [dʒ]","interlingual"),
        ("[z]eit für Zeit","[ts]eit",f"englisches ⟨z⟩ = [z]","interlingual")]),
  P("Graphem-Phonem-Kontrasttabelle; <b>farbige Markierung</b> der „falschen Freunde“ ⟨w v j z s⟩; Minimalpaare (<i>vier/wir</i>, <i>Wein/fein</i>); ei/ie-Merksatz (⟨ei⟩ spricht man wie den zweiten Buchstaben, ⟨ie⟩ wie ein langes i); Diktat mit Fokus auf ⟨w v j z⟩."),
  P("Das gemeinsame lateinische Alphabet ist ein <b>Lesevorsprung</b> – die Buchstabenformen sind bereits vertraut. Aufgabe ist nicht, das Lesen neu zu lernen, sondern nur die abweichenden Lautwerte zu ergänzen. Viele Kognaten (<i>Wasser/water, Sonne/sun</i>) stützen zusätzlich das Verständnis."),
 ])

DETAIL["konsonanten"]=dict(
 modul="Modul I · Laut & Schrift", titel="ch- und r-Laut & Konsonanten",
 lead="Das Deutsche besitzt Konsonanten, die es im Englischen nicht gibt – den ach-Laut und den ich-Laut ⟨ch⟩ sowie das uvulare bzw. vokalisierte ⟨r⟩. Sie werden durch den nächstliegenden englischen Laut ersetzt und erzeugen einen hartnäckigen Akzent.",
 blocks=[
  T([("ach-Laut [x]",f"{d('nach, Bach, doch')}","kein Äquivalent (nur schott. <i>loch</i>)"),
    ("ich-Laut [ç]",f"{d('ich, Milch, nicht')}",f"nur ähnlich in {e('huge, hue')} [hj]"),
    ("⟨r⟩",f"uvular [ʁ] / vokalisiert [ɐ] – {d('rot, Vater')}",f"retroflex/rhotisch [ɹ] – {e('red')}"),
    ("⟨l⟩",f"stets „hell“ [l] – {d('voll, alt')}",f"„dark l“ [ɫ] – {e('full, all')}"),
    ("Affrikaten",f"{d('pf')} (Pferd), {d('z')} [ts] (Zeit)","ungewohnte Anlautcluster"),],
    head=("Laut / Graphem","Deutsch","Englisch"))
  +NOTE("Diese Laute existieren im Englischen nicht – sie müssen neu gebildet, nicht nur „richtig getroffen“ werden."),
  P("Betroffen sind Aussprache und Hörverstehen. ich-/ach-Laut sind die deutlichsten Akzentmarker; die Vokalisierung von ⟨-er⟩ am Wortende ("+d("Vater")+" [ˈfaːtɐ]) wird oft als volles [r] realisiert."),
  ITAB([("[k] für ⟨ch⟩ (Bach → „Bak“)","[x]",f"englisch fehlt [x] → Ersatz durch [k]","interlingual"),
        ("[ʃ] für ich-Laut (ich → „isch“)","[ç]","Ersatz durch nächstliegenden L1-Laut","interlingual"),
        ("retroflexes [ɹ] für ⟨r⟩","[ʁ] / [ɐ]","englische Rhotizität übertragen","interlingual"),
        ("„dark l“ in voll","helles [l]","englisches [ɫ] übertragen","interlingual")]),
  P("ich-Laut über <i>huge/hue</i> anbahnen; ach-Laut aus dem hinteren [k]-Bereich mit Reibung entwickeln; vokalisiertes ⟨-er⟩ als [ɐ] üben; helles [l] isolieren; Minimalpaare (<i>Kirche/Kirsche</i>, <i>Loch/Koch</i>)."),
  P("Der englische h-Anlaut in <i>huge</i> liegt nahe am ich-Laut – eine nutzbare <b>Brücke</b>. Auch das vokalisierte deutsche ⟨-er⟩ ähnelt dem englischen Schwa. Vorhandene Laute dienen als Anker für die neuen."),
 ])

DETAIL["auslaut"]=dict(
 modul="Modul I · Laut & Schrift", titel="Auslautverhärtung",
 lead="Das Deutsche entstimmt Plosive am Wortende (Tag [taːk]) und behält dennoch die Schreibung bei. Das Englische entstimmt <i>nicht</i> (dog [dɒg]). Für Englischsprachige liegt die Hürde also im Sprechen, kaum in der Schreibung.",
 blocks=[
  T([("Prozess",f"Entstimmung {d('/b d g/ → [p t k]')} am Wortende","keine finale Entstimmung"),
    ("gesprochen",f"{d('Tag')} [taːk], {d('Hund')} [hʊnt], {d('lieb')} [liːp]",f"{e('dog')} [dɒg], {e('bad')} [bæd] – stimmhaft"),
    ("Verschriftung",f"morphophonemisch: Graphem bleibt ({d('Tag – Tage')})",f"stimmhaft gesprochen <i>und</i> geschrieben"),])
  +NOTE("Kernpunkt: Die Schreibung fällt Englischsprachigen leicht (sie schreiben ⟨d/g/b⟩ ohnehin); neu ist nur die Aussprache­regel „am Ende entstimmen“."),
  P("Relevant für die <b>Aussprache</b> (Akzent) und das <b>Leseverstehen</b> von Wortfamilien ("+d("Tag – täglich – Tage")+"). Anders als bei vielen anderen L1 ist hier die Orthographie kein Problem, sondern das lautliche Ziel."),
  ITAB([("[taːg] für Tag","[taːk]","keine finale Entstimmung im Englischen","interlingual"),
        ("[hʊnd] für Hund","[hʊnt]","stimmhafter Auslaut aus der L1","interlingual"),
        ("[liːb] für lieb","[liːp]","englische Stimmhaftigkeit übertragen","interlingual")]),
  P("Gezieltes Entstimmungs-Training am Wortende; <b>Minimalpaare</b>, die im Deutschen zusammenfallen (<i>Rad/Rat</i> beide [raːt], <i>seit/seid</i>); Verlängerungsprobe zur Schreibung ("+d("Rad → Räder")+" → ⟨d⟩ bleibt)."),
  P("Das Englische <i>besitzt</i> stimmhafte Auslaute – ein Vorsprung für die <b>Rechtschreibung</b> (das ⟨d⟩ in <i>Hund</i> wird intuitiv geschrieben). Reframing: nicht „ein neuer Laut“, sondern „eine Aussprache­regel für denselben Buchstaben“."),
 ])

DETAIL["vokale"]=dict(
 modul="Modul I · Laut & Schrift", titel="Vokale: Länge & Umlaute (ä ö ü)",
 lead="Das Deutsche unterscheidet Vokallänge bedeutungsunterscheidend und besitzt die vorderen Rundvokale ö/ü, die dem Englischen fehlen. Zudem werden deutsche Langvokale gern englisch diphthongiert.",
 blocks=[
  T([("Vokallänge",f"phonemisch: {d('Miete/Mitte')} [iː]/[ɪ]","weniger kontrastiv"),
    ("ö [øː]/[œ]",f"{d('schön, können, hören')}","kein Äquivalent"),
    ("ü [yː]/[ʏ]",f"{d('über, müssen, Tür')}","kein Äquivalent"),
    ("Monophthonge",f"rein: {d('See')} [zeː], {d('Boot')} [boːt]",f"diphthongiert: {e('say')} [eɪ], {e('boat')} [oʊ]"),])
  +NOTE("Neu sind die Laute ö/ü <i>und</i> die Tendenz, deutsche Langvokale (ee, oo) englisch gleiten zu lassen."),
  P("Kernbereich der Aussprache. ö/ü sind die auffälligsten Vokalhürden; dazu die englische Diphthongierung von [eː] und [oː] ("+d("See")+" → „say“, "+d("Boot")+" → „boat“) und die feine Längenopposition."),
  ITAB([("[uː] für ü (über → „uber“)","[yː]","ö/ü im Englischen nicht vorhanden","interlingual"),
        ("[ɜ]/[ɛ] für ö (schön → „shern“)","[øː]","Ersatzlaut aus der L1","interlingual"),
        ("[oʊ] für [oː] (Boot → „boat“)","[oː]","englische Diphthongierung übertragen","interlingual"),
        ("[eɪ] für [eː] (See → „say“)","[eː]","Gleitlaut aus der L1","interlingual")]),
  P("ü = Lippen zu [iː] runden („ee“ sagen, dann Lippen spitzen); ö = [eː] mit Rundung; Langvokale „rein, ohne Gleiten“ halten; Längen-Minimalpaare (<i>Ofen/offen</i>, <i>Miete/Mitte</i>, <i>Höhle/Hölle</i>)."),
  P("Das Englische hat vordere Vokale und Lippenrundung – nur nie <i>gleichzeitig</i>. Das Kombinieren (gespreiztes [iː] + Rundung → ü) ist die Brücke. Und die Opposition <i>sheep/ship</i> [iː]/[ɪ] entspricht der deutschen Vokallänge – vorhandenes Wissen, das direkt trägt."),
 ])

DETAIL["grossschreibung"]=dict(
 modul="Modul I · Laut & Schrift (Orthographie)", titel="Substantivgroßschreibung & ß",
 lead="Das Deutsche schreibt <i>alle</i> Substantive groß (der Tisch, die Freiheit, das Lesen), das Englische nur Eigennamen. Dazu kommen ß und die ss/ß-Regel. Eine unscheinbare, aber allgegenwärtige orthographische Hürde.",
 blocks=[
  T([("Nomen",f"alle groß: {d('das Haus, die Liebe')}",f"nur Eigennamen: {e('the house, love')}"),
    ("Nominalisierung",f"{d('das Gute, beim Schwimmen')}",f"klein: {e('the good, while swimming')}"),
    ("Nationalität",f"Adjektiv klein: {d('die deutsche Sprache')}",f"groß: {e('the German language')}"),
    ("ß / ss",f"{d('Straße')} (langer Vokal), {d('Fluss')} (kurzer)","kein ß"),])
  +NOTE("Die Regel ist einfach formuliert („alle Nomen groß“), aber pervasiv – jeder Satz ist betroffen."),
  P("Betrifft die <b>Rechtschreibung</b> durchgehend und hilft zugleich dem <b>Lesen</b> (Nomen sind sichtbar). Typisch: Englischsprachige schreiben deutsche Nomen zu <i>klein</i> und Nationalitätsadjektive fälschlich <i>groß</i> (nach der englischen Regel für <i>English, German</i>)."),
  ITAB([("„ich lese ein buch“","… ein Buch","Nomen nicht großgeschrieben (englische Regel)","interlingual"),
        ("„die Deutsche Grammatik“","die deutsche Grammatik","Nationalitätsadjektiv fälschlich groß","interlingual"),
        ("„beim schwimmen“","beim Schwimmen","nominalisiertes Verb nicht erkannt","intralingual")]),
  P("Regel „alle Nomen groß“; <b>Artikelprobe</b> (steht/passt ein Artikel davor → Nomen → groß); Nominalisierungs­signale ("+d("das, beim, zum, im")+" + Verb/Adjektiv); Nationalitätsadjektive klein; ß/ss über die Vokallänge (langer Vokal/Diphthong → ß)."),
  P("Das Englische schreibt Wochentage, Monate, Sprachen und Nationalitäten groß – eine <i>teilweise</i> Großschreibung, die sich umlenken lässt. Das Prinzip „Großschreibung trägt grammatische Information“ ist bekannt; das Deutsche wendet es nur konsequent auf alle Nomen an."),
 ])

# --------------------------------------------------------------- Modul II --
DETAIL["genus"]=dict(
 modul="Modul II · Morphologie (Nomen)", titel="Genus & Artikel",
 lead="Das Deutsche markiert grammatisches Genus (der/die/das) am Nomen; das englische „the“ ist genuslos. Da die L1 die Kategorie nicht besitzt, an die sich das Genus heften ließe, bleiben Genus-/Artikelfehler eine der hartnäckigsten Fehlerquellen.",
 blocks=[
  T([("Genus",f"3 Genera, lexikalisch fest: {d('der Tisch, die Lampe, das Buch')}",f"kein Genus: {e('the')}"),
    ("best. Artikel",f"{d('der/die/das')} (+ Flexion)",f"invariabel: {e('the')}"),
    ("unbest. Artikel",f"{d('ein/eine/ein')}",f"{e('a / an')}"),
    ("Kongruenz","Artikel, Adjektiv, Pronomen richten sich nach dem Genus","keine Genuskongruenz"),])
  +NOTE("Genus ist meist nicht aus der Bedeutung ableitbar ("+d("das Mädchen")+", "+d("die Sonne")+", "+d("der Mond")+") und muss mit dem Nomen gelernt werden."),
  P("Der Artikel muss <b>mit jedem Nomen mitgelernt</b> werden (Nomen + Artikel als Einheit). Da die L1 kein Genus besitzt, bleiben Fehler oft lange bestehen – ein <b>diagnostischer Dauerbrenner</b>. Auch die Pronominalisierung folgt dem Genus ("+d("das Mädchen → es")+", nicht „sie“)."),
  ITAB([("das Tisch","der Tisch","kein Genus in der L1 → Zuweisung geraten","interlingual"),
        ("das Mädchen … sie/it","das Mädchen … es","natürliches statt grammatisches Genus (engl. „she/it“)","interlingual"),
        ("der Sonne","die Sonne","falsche Genuszuweisung","intralingual")]),
  P("<b>1. Nomen-Artikel-Kopplung</b> – Vokabeln nie ohne Artikel; Farbcode <span style='color:#1565c0'>der</span>/<span style='color:#c62828'>die</span>/<span style='color:#2e7d32'>das</span>.")
  +"<p><b>2. Genus-Heuristiken:</b></p><ul class='li'><li>"+d("-ung, -heit, -keit, -schaft, -tion, -e")+" → <span class='ok'>die</span></li><li>"+d("-chen, -lein, -ment, -um")+" → <span class='ok'>das</span></li><li>Agens auf "+d("-er")+", Tage/Monate/Jahreszeiten → <span class='ok'>der</span></li></ul>"
  +P("<b>3. Pronomenkongruenz</b> – "+d("der → er, die → sie, das → es")+" auch für Dinge (der Tisch → er)."),
  P("Das Englische <i>hatte</i> im Altenglischen drei Genera – es ist historisch germanisch wie das Deutsche. Heute löst es die Bezugnahme über das natürliche Genus; den Kontrast „grammatisches vs. natürliches Genus“ ("+d("das Mädchen")+" ist grammatisch neutrum) explizit zu machen, entzaubert das System. Das Konzept „bestimmt/unbestimmt“ ist über <i>the/a</i> ohnehin vertraut."),
 ])

DETAIL["kasus"]=dict(
 modul="Modul II · Morphologie", titel="Kasus (Nom · Akk · Dat · Gen)",
 lead="Das Deutsche markiert vier Kasus an Artikel, Adjektiv und Pronomen; das Englische hat Kasus nur noch am Pronomen (he/him, who/whom). Die Fälle und die Kasusrektion sind eine der größten morphologischen Hürden.",
 blocks=[
  T([("System",f"4 Kasus: {d('Nom · Akk · Dat · Gen')}",f"nur am Pronomen: {e('I/me, he/him, who/whom')}"),
    ("Markierung",f"am Artikel/Adjektiv: {d('der/den/dem/des')}","Wortstellung + Präpositionen"),
    ("Rollen",f"Subjekt=Nom, dir. Obj.=Akk, indir. Obj.=Dat","über Position / „to“ ausgedrückt"),
    ("Genitiv",f"{d('das Buch des Mannes')}",f"{e('the man’s book / of the man')}"),])
  +NOTE("Dieselben Rollen kodiert das Englische über die Stellung ("+e("the man sees the dog")+" ≠ "+e("the dog sees the man")+") – die Funktion ist bekannt, nur die Markierung ist neu."),
  P("Die Endungen an Artikel und Adjektiv sind der Kern; die Opposition Nom/Akk ("+d("der/den")+") ist subtil, der Dativ nach bestimmten Verben und Präpositionen zusätzlich. Die englischen Pronomenformen (<i>me, him, her</i>) sind der beste Anker."),
  ITAB([("Ich sehe der Mann.","Ich sehe den Mann.","Akkusativ am Artikel nicht markiert (engl. kein Kasus)","interlingual"),
        ("Ich helfe die Frau.","Ich helfe der Frau.","Dativ-Verb nicht erkannt","intralingual"),
        ("mit mein Bruder","mit meinem Bruder","Dativrektion der Präposition nicht realisiert","interlingual")]),
  P("Kasustabelle ("+d("der/den/dem/des")+"); Analogie zu englischen Pronomen ("+e("I / me / to me")+" → "+d("er / ihn / ihm")+"); Wechsel- und feste Präpositionen; Dativ-Verben-Liste (helfen, danken, folgen, gehören); Akk/Dat über <i>wen?/wem?</i>."),
  P("Das Englische bewahrt Kasus im Pronomen ("+e("I–me–my, he–him–his, who–whom")+") – ein lebendiger Rest. Auf „<i>him</i> = ihm“ aufzubauen lässt das deutsche System als <b>Erweiterung</b> erscheinen, nicht als Neuland. Und die Einsicht „Stellung kodiert Rolle“ erklärt umgekehrt, warum das Deutsche freier umstellen darf."),
 ])

DETAIL["plural"]=dict(
 modul="Modul II · Morphologie (Nomen)", titel="Plural",
 lead="Der deutsche Plural ist unvorhersehbar (fünf Grundtypen + Umlaut), der englische nahezu regelmäßig (-s). Englischsprachige übergeneralisieren -s und bilden Umlautplurale nicht.",
 blocks=[
  T([("Typen",f"{d('-e, -er, -(e)n, -s, ∅')} (+ Umlaut), unvorhersehbar",f"fast nur {e('-s')}"),
    ("Umlaut",f"{d('Mann → Männer, Buch → Bücher')}","keiner"),
    ("-s-Plural",f"nur Fremd-/Kurzwörter: {d('Autos, Parks')}",f"Standardplural: {e('cars, books')}"),
    ("Nullplural",f"{d('der Lehrer → die Lehrer')}",f"{e('teacher → teachers')}"),])
  +NOTE("Auch das Englische hat Umlaut-Reste ("+e("man/men, foot/feet")+") – die Brücke zum deutschen Umlautplural."),
  P("Plural nicht ableitbar → mit Artikel mitlernen. Typische Fehler: das englische -s wird übergeneralisiert, und der Umlaut als Pluralsignal wird übersehen."),
  ITAB([("die Mans / Manns","die Männer","englisches -s übergeneralisiert, Umlaut fehlt","interlingual"),
        ("die Buchs","die Bücher","-s statt -er + Umlaut","interlingual"),
        ("die Fraus","die Frauen","falscher Pluraltyp gewählt","intralingual")]),
  P("Pluraltypen in Gruppen mit Artikel üben; Regel „nach Fremd-/Kurzwörtern steht -s, sonst nicht“; Umlaut als Pluralsignal markieren; Kognaten-Brücke <i>man/men → Mann/Männer</i>."),
  P("Englisch <i>man/men, foot/feet, tooth/teeth, mouse/mice, goose/geese</i> sind genau der i-Umlaut – historisch identisch mit "+d("Mann/Männer, Fuß/Füße, Zahn/Zähne, Maus/Mäuse")+". Diese lebenden Kognaten sind der Beweis, dass der Mechanismus im Englischen existiert – der deutsche Umlautplural fühlt sich dann vertraut an."),
 ])

DETAIL["adjektiv"]=dict(
 modul="Modul II · Morphologie", titel="Adjektivdeklination",
 lead="Das Deutsche flektiert attributive Adjektive (stark/schwach/gemischt – je nach Artikelwort); das englische Adjektiv ist unveränderlich. Dies ist der wohl schwierigste Formbereich für englische Lernende.",
 blocks=[
  T([("Attributiv",f"{d('ein guter Mann, der gute Mann, guten Wein')}",f"invariabel: {e('a good man, the good man')}"),
    ("Deklinationstyp",f"stark/schwach/gemischt je nach Artikelwort","kein Typ – keine Endung"),
    ("Prädikativ",f"unflektiert: {d('der Mann ist gut')}",f"ebenfalls invariabel: {e('the man is good')}"),])
  +NOTE("Prädikativ ist identisch ("+d("ist gut")+" / "+e("is good")+") – nur die <i>attributive</i> Flexion ist neu."),
  P("Das Endungssystem (stark/schwach/gemischt) hängt von Genus, Kasus und Artikelwort ab; prädikativ gibt es keine Endung (Entlastung). Hohe Fossilisierungs­gefahr, weil die L1 die Kategorie gar nicht kennt."),
  ITAB([("ein gut Mann","ein guter Mann","attributive Endung fehlt (englisch invariabel)","interlingual"),
        ("der guter Mann","der gute Mann","starke statt schwache Endung nach best. Artikel","intralingual"),
        ("mit guter Wein","mit gutem Wein","Kasusendung des Adjektivs falsch","intralingual")]),
  P("Prädikativ zuerst (keine Endung), dann attributiv aufbauen; Tabelle nach Artikeltyp; Faustregel „steht "+d("der/die/das")+" davor → schwache Endung (-e/-en)“; Genus + Kasus → Endung systematisch üben."),
  P("Englische Reste wie <i>golden, wooden</i> (-en) und die Reihenfolge attributiver Adjektive zeigen: Adjektive <i>können</i> Form tragen. Vor allem existiert die Unterscheidung prädikativ/attributiv konzeptuell bereits ("+e("the man is good / the good man")+"). Auf der prädikativen Gleichheit aufbauen und die Endungen schrittweise ergänzen."),
 ])

DETAIL["pronomen"]=dict(
 modul="Modul II · Morphologie", titel="Pronomen & Anrede (du/Sie)",
 lead="Beide Sprachen haben Personalpronomen – doch deutsche Pronomen tragen Kasus, ihre Genuskongruenz folgt dem grammatischen Genus, und das Deutsche unterscheidet Anredeformen (du/Sie), die das Englische mit „thou“ verloren hat.",
 blocks=[
  T([("Personal",f"{d('ich/mich/mir, er/ihn/ihm')}",f"{e('I/me, he/him')} (zwei Formen)"),
    ("Anrede",f"{d('du')} (vertraut) / {d('Sie')} (formell)",f"nur {e('you')}"),
    ("3. Person (Dinge)",f"nach grammatischem Genus: {d('der Tisch → er')}",f"nach natürlichem Genus: {e('it')}"),])
  +NOTE("„you“ deckt alles ab – die Wahl du/Sie ist neu und sozial heikel."),
  P("Zwei Lernpunkte mit hoher Last: die <b>du/Sie</b>-Wahl (Register) und die Pronominalisierung nach grammatischem Genus ("+d("der Tisch → er")+", nicht „es/it“); dazu die Kasusformen der Pronomen."),
  ITAB([("Wie alt bist du? (zum Vorgesetzten)","Wie alt sind Sie?","fehlende du/Sie-Distinktion (engl. nur „you“)","interlingual"),
        ("Der Tisch … es/it ist alt.","Der Tisch … er ist alt.","Genuskongruenz des Pronomens","interlingual"),
        ("mit du","mit dir","Kasus nach Präposition nicht realisiert","intralingual")]),
  P("du/Sie-Register (wann welche Form) an Situationen üben; Pronomen-Kongruenz "+d("der → er, die → sie, das → es")+"; Kasusformen ("+d("mich/mir, dich/dir")+"); Possessiva ("+d("mein/dein/sein/ihr")+")."),
  P("Das Englische <i>hatte</i> mit <i>thou/thee/thy</i> genau die du-Reihe (heute noch in Gebet und bei Shakespeare) – inklusive Kasus (<i>thou–thee</i>). Dieses Bewusstsein macht "+d("du/dich/dir")+" nicht fremd, sondern <b>wiederentdeckbar</b>."),
 ])

DETAIL["verben"]=dict(
 modul="Modul II · Morphologie", titel="Verben & trennbare Verben",
 lead="Deutsche Verben konjugieren nach Person, gliedern sich in stark/schwach und – als Besonderheit – trennen bei trennbaren Vorsilben ihren Präfix ab (aufstehen → ich stehe … auf) und bilden so eine Klammer. Die englischen phrasal verbs sind das nächste Analogon.",
 blocks=[
  T([("Konjugation",f"reiche Endungen {d('-e, -st, -t, -en')}",f"fast nur 3. Sg. {e('-s')}"),
    ("stark/schwach",f"{d('singen – sang – gesungen')}",f"{e('sing – sang – sung')} (parallel!)"),
    ("Trennbar",f"{d('aufstehen → ich stehe … auf')}",f"phrasal: {e('get up')} (bleibt beim Verb)"),
    ("Position","Präfix ans Satzende (Klammer)","Partikel folgt dem Verb"),])
  +NOTE("Englische starke Verben ("+e("sing/sang/sung")+") sind Kognaten – der Ablaut ist gemeinsames germanisches Erbe."),
  P("Große Baustellen: trennbare Verben mit der <b>Verbklammer</b> und die Hilfsverbwahl (haben/sein). Die Personalendungen sind reicher als im Englischen (nur -s in der 3. Sg.)."),
  ITAB([("Ich aufstehe um 7.","Ich stehe um 7 auf.","Präfix nicht abgetrennt (engl. phrasal bleibt zusammen)","interlingual"),
        ("Ich habe gegangen.","Ich bin gegangen.","Hilfsverbwahl (Bewegung → sein); engl. „have gone“","interlingual"),
        ("er gehen / er geht-s","er geht","Personalendung -t nicht realisiert","intralingual")]),
  P("Trennbare Verben mit der <b>Satzklammer</b> visualisieren ("+d("steht … auf")+"); haben/sein-Regeln (Bewegung/Zustandswechsel → sein); starke Reihen über Kognaten sichern ("+d("trinken/drink, beginnen/begin")+"); Personalendungen automatisieren."),
  P("Das Englische bewahrt rund 150 starke Verben mit demselben Ablaut ("+e("drink/drank/drunk")+" = "+d("trinken/trank/getrunken")+", "+e("begin/began/begun")+" = "+d("beginnen/begann/begonnen")+"). Und phrasal verbs ("+e("give up, look after")+") funktionieren semantisch wie trennbare Präfixe – das Konzept überträgt sich; neu ist nur die Klammer­stellung."),
 ])

DETAIL["zeit"]=dict(
 modul="Modul II · Morphologie", titel="Zeitformen & Aspekt",
 lead="Der große Kontrast ist nicht das Tempus, sondern der Aspekt: Das Englische grammatikalisiert den Verlauf (I am reading), das Deutsche hat keine Verlaufsform und nutzt das Präsens. Zudem ist das deutsche Perfekt die mündliche Vergangenheit.",
 blocks=[
  T([("Progressiv",f"keiner: {d('ich lese')} = I read / I am reading",f"obligatorisch: {e('be + -ing')}"),
    ("Vergangenheit",f"Perfekt (mündl.) / Präteritum (schriftl.)",f"simple past / present perfect (andere Verteilung)"),
    ("Zukunft",f"{d('Präsens + Adverb')} / werden",f"{e('will / going to')}"),
    ("Dauer seit …",f"Präsens: {d('Ich wohne seit 2020 hier')}",f"present perfect: {e('I have lived here since 2020')}"),])
  +NOTE("Die Formen scheinen 1:1 (have = haben), doch der Gebrauch weicht stark ab – vor allem Progressiv und Perfekt/Präteritum."),
  P("Lernschwer ist der <b>Gebrauch</b>: Englischsprachige suchen eine Verlaufsform („bin am Lesen“ als Standard), verwenden das present perfect für Andauerndes und übertragen die Perfekt/Präteritum-Verteilung falsch."),
  ITAB([("Ich bin am Lesen (als Standard-Verlauf)","Ich lese gerade","Progressiv aus der L1 gesucht (kein dt. Progressiv)","interlingual"),
        ("Ich habe hier seit 2020 gewohnt","Ich wohne seit 2020 hier","engl. present perfect für Andauerndes → dt. Präsens","interlingual"),
        ("erzählend schriftlich nur Perfekt","… Präteritum (ging, sah)","Perfekt/Präteritum-Gebrauch nicht getrennt","intralingual")]),
  P("„Deutsch hat kein -ing; das Präsens deckt beides“ – bei Bedarf "+d("gerade/immer")+" ergänzen; Perfekt = mündliche Vergangenheit (mit haben/sein); "+d("seit + Präsens")+" für Andauerndes; Präteritum in der Schriftsprache."),
  P("Das englische simple present ohne -ing für Allgemeingültiges ("+e("water boils at 100°")+") ist genau der deutsche Standard – nur ausweiten. Und "+e("I have lived here since 2020")+" bildet auf das deutsche Präsens (seit) ab: den systematischen Versatz sichtbar machen, statt blind Regeln zu pauken."),
 ])

DETAIL["konjunktiv"]=dict(
 modul="Modul II · Morphologie", titel="Konjunktiv II & I",
 lead="Der Konjunktiv II drückt Irreales und Höflichkeit aus (ich hätte, ich würde …); das Englische leistet dies mit „would / if I were“. Der Konjunktiv I der indirekten Rede (er sei) hat kein alltägliches englisches Äquivalent.",
 blocks=[
  T([("Irrealis",f"K II: {d('käme, hätte, würde … kommen')}",f"{e('would come, if I were')}"),
    ("Höflichkeit",f"K II: {d('Ich hätte gern …, Könnten Sie …')}",f"{e('I would like …, Could you …')}"),
    ("Indirekte Rede",f"K I: {d('er sagt, er komme')}",f"backshift: {e('he said he came')}"),],
    head=("Funktion","Deutsch","Englisch"))
  +NOTE("Die Irrealis- und Höflichkeits­funktion kennt das Englische (would/could) – gute Brücke; K I ist neu."),
  P("K II (Irrealis + Höflichkeit) ist für den Alltag am wichtigsten; K I (indirekte Rede) ist bildungssprachlich/journalistisch und im Englischen ohne direktes Äquivalent."),
  ITAB([("Wenn ich reich bin, würde ich … (irreal)","Wenn ich reich wäre, …","Irrealis nicht mit K II markiert","intralingual"),
        ("Ich will einen Kaffee (höflich gemeint)","Ich hätte gern / möchte einen Kaffee","K II als Höflichkeitsmittel unbekannt (engl. „would like“)","interlingual"),
        ("er sagt, er kommt (formell)","er sagt, er komme","indirekte Rede ohne K I","intralingual")]),
  P("K II zuerst: "+d("würde")+" + Infinitiv, dazu "+d("wäre/hätte/könnte")+"; direkte Brücke "+e("if I were = wenn ich wäre")+"; Höflichkeits­formeln als Chunks; K I zunächst rezeptiv (Zeitung, indirekte Rede)."),
  P("Englisch <i>if I were you</i> (<i>were</i> = alter Konjunktiv!) und <i>would/could/should</i> sind lebende Konjunktiv-/Modalreste – direkte funktionale Entsprechungen zum K II. Die Lernenden denken bereits so; das Deutsche hat dafür nur explizite Verbformen."),
 ])

DETAIL["passiv"]=dict(
 modul="Modul II · Morphologie", titel="Passiv",
 lead="Das Deutsche hat ein Vorgangspassiv (werden + Partizip II) und ein Zustandspassiv (sein + Partizip II); das Englische nutzt be/get. Die werden/sein-Unterscheidung und die Agens-Markierung (von/durch) sind die Kernkontraste.",
 blocks=[
  T([("Vorgangspassiv",f"{d('werden')} + Part. II: {d('wird geschrieben')}",f"{e('be + past part.: is written')}"),
    ("Zustandspassiv",f"{d('sein')} + Part. II: {d('ist geöffnet')}",f"oft dasselbe: {e('is open/opened')}"),
    ("Agens",f"{d('von')} + Dativ / {d('durch')} + Akk",f"{e('by')}"),])
  +NOTE("Das englische „to be“ verdeckt die deutsche Unterscheidung werden/sein – genau hier entstehen Fehler."),
  P("Zwei Lernpunkte: die <b>werden/sein</b>-Unterscheidung (Vorgang vs. Zustand) und die Agens-Markierung mit "+d("von/durch")+". Das Akkusativobjekt des Aktivs wird zum Subjekt im Nominativ."),
  ITAB([("Die Tür ist geöffnet (Vorgang gemeint)","Die Tür wird geöffnet","engl. „is opened“ deckt Vorgang & Zustand","interlingual"),
        ("Das Buch ist von mir geschrieben (Vorgang)","… wird von mir geschrieben","Vorgangs-/Zustandspassiv vermischt","interlingual"),
        ("durch mir","von mir / durch mich","Agens-Rektion falsch","intralingual")]),
  P(d("werden")+" + Partizip II sichern; Vorgang vs. Zustand (wird geöffnet / ist geöffnet); Agens "+d("von")+" + Dativ; Umformung Aktiv ↔ Passiv üben."),
  P("Das englische <b>get-Passiv</b> ("+e("the window got broken")+") hebt gerade den <i>Vorgang</i> hervor – die Bedeutung des werden-Passivs. Über die Faustregel <i>get ≈ werden</i>, <i>be ≈ sein</i> erschließt sich eine Unterscheidung, die das Englische halb selbst macht."),
 ])

DETAIL["praep"]=dict(
 modul="Modul II · Morphologie", titel="Präpositionen & Wechselpräpositionen",
 lead="Englische Präpositionen regieren keinen Kasus; deutsche schon – und die Wechselpräpositionen schalten zwischen Akkusativ (Richtung) und Dativ (Ort). Sowohl die Wahl der Präposition als auch der Kasus sind Hürden.",
 blocks=[
  T([("Rektion",f"fester Kasus: {d('mit + Dat, für + Akk, wegen + Gen')}","kein Kasus"),
    ("Wechselpräp.",f"{d('an/auf/in/über')} … wohin? → Akk, wo? → Dat","keine Wechselrektion"),
    ("Beispiel",f"{d('in die Schule')} (Akk) / {d('in der Schule')} (Dat)",f"{e('to / at school')}"),])
  +NOTE("Das Englische unterscheidet Richtung/Ort lexikalisch ("+e("into/in, onto/on, to/at")+") – dieselbe Bedeutung, im Deutschen über den Kasus."),
  P("Doppelte Hürde: die <b>Wahl</b> der Präposition (nicht 1:1, "+d("auf")+" ≠ immer „on“) und ihre <b>Kasusrektion</b> – besonders bei Wechselpräpositionen (wohin? Akkusativ / wo? Dativ)."),
  ITAB([("in die Schule (Ort gemeint)","in der Schule","wohin/wo nicht getrennt","intralingual"),
        ("mit der Auto","mit dem Auto","feste Rektion (mit + Dativ)","interlingual"),
        ("Ich warte für dich","Ich warte auf dich","engl. „wait for“ übertragen (Präpositionenwahl)","interlingual")]),
  P("Präpositionen in Kasusgruppen lernen (Akk-/Dativ-/Wechsel-/Genitivgruppe); Wechsel: <i>wohin? → Akk</i>, <i>wo? → Dat</i>; feste Verb-Präposition-Verbindungen ("+d("warten auf, denken an, sich freuen über")+"); Kontrast "+e("into/in")+" ↔ Akk/Dat."),
  P("Englisch <i>into</i> vs. <i>in</i>, <i>onto</i> vs. <i>on</i> kodiert bereits den Richtung/Ort-Kontrast, den das Deutsche mit Akk/Dativ markiert – die Bedeutungsunterscheidung ist muttersprachlich vorhanden; die Lernenden verschieben sie nur von der Präposition auf die Kasusendung."),
 ])

# -------------------------------------------------------------- Modul III --
DETAIL["satzart"]=dict(
 modul="Modul III · Syntax", titel="Satzarten & Fragebildung",
 lead="Das Deutsche bildet Ja/Nein-Fragen durch Voranstellung des finiten Verbs (Kommst du?); das Englische nutzt do-support (Do you come?). Die Übertragung von „do“ ist eine klassische Interferenz.",
 blocks=[
  T([("Aussage","Verbzweit (V2)","SVO"),
    ("Ja/Nein-Frage",f"Verb voran: {d('Kommst du?')}",f"do-support: {e('Do you come?')}"),
    ("W-Frage",f"W-Wort + V2: {d('Wann kommst du?')}",f"W-Wort + do: {e('When do you come?')}"),],
    head=("Satztyp","Deutsch","Englisch"))
  +NOTE("Das Deutsche braucht kein Hilfsverb „tun“ – die Inversion genügt; das englische „do“ hat kein deutsches Äquivalent."),
  P("Der Knackpunkt ist die Fragebildung: Deutsch stellt das finite Verb voran (Inversion), Englisch schiebt „do“ ein. Die W-Frage verlangt zusätzlich Verbzweitstellung."),
  ITAB([("Tust du kommen? / Machst du sprechen?","Kommst du? / Sprichst du?","do-support aus der L1 übertragen","interlingual"),
        ("Wann du kommst?","Wann kommst du?","W-Wort ohne Inversion/V2","interlingual"),
        ("Du kommst? (nur Intonation als Standard)","Kommst du?","Fragebildung ohne Inversion","interlingual")]),
  P("Ja/Nein-Frage = finites Verb voran; W-Frage = W-Wort + finites Verb (V2); kein „tun“; gezielt englische do-Fragen ins Deutsche umformen."),
  P("Das englische „do“ ist ein Hilfsverb, das das Deutsche nie grammatikalisiert hat – doch die Inversion überlebt im Englischen bei <i>be</i> und Modalverben: "+e("Are you …? / Can you …?")+" stellen direkt voran, genau wie das Deutsche. Über „<i>Can you? = Kannst du?</i>“ lässt sich das do-support umgehen."),
 ])

DETAIL["wortstell"]=dict(
 modul="Modul III · Syntax", titel="Wortstellung (V2 & Satzklammer)",
 lead="Das Englische ist festes SVO; das Deutsche ist Verbzweit mit Satzklammer – das finite Verb steht an zweiter Stelle, infinite Teile rücken ans Ende. Die Klammer und die Freiheit im Vorfeld sind die zentralen Hürden.",
 blocks=[
  T([("Grundstellung","Verbzweit (V2)","SVO (fest)"),
    ("Vorfeld",f"beliebiges Glied vor dem Verb: {d('Heute gehe ich …')}",f"Subjekt zuerst: {e('Today I go …')}"),
    ("Klammer",f"{d('Ich habe … gekauft')} (finites + infinites Verb)","Verben zusammen"),])
  +NOTE("Inversion nach dem Vorfeld: "+d("Heute gehe ich")+" (nicht „Heute ich gehe“) – die englische SVO-Folge wird durchbrochen."),
  P("Lernschwer ist nicht eine Einzelregel, sondern das <b>System</b>: V2, die Inversion nach einem vorangestellten Glied und die Satzklammer (haben … Partizip, Modalverb … Infinitiv)."),
  ITAB([("Heute ich gehe ins Kino.","Heute gehe ich ins Kino.","SVO beibehalten statt V2/Inversion","interlingual"),
        ("Ich habe gekauft ein Buch.","Ich habe ein Buch gekauft.","Klammer nicht geschlossen (engl. „bought a book“)","interlingual"),
        ("Ich will lernen Deutsch.","Ich will Deutsch lernen.","Infinitiv nicht ans Satzende","interlingual")]),
  P("V2-Regel (finites Verb an 2. Stelle, egal was im Vorfeld steht); Inversion nach dem Vorfeld markieren; <b>Satzklammer</b> visualisieren; Umstell- und Klammerübungen."),
  P("Auch das Englische kennt V2-Reste: "+e("Never have I seen …, Here comes the bus, Rarely does he …")+" – ein vorangestelltes Element löst Inversion aus, genau wie im Deutschen. Diese Fälle sichtbar zu machen zeigt: V2 ist nicht fremd; das Deutsche macht es nur zur Regel statt zur Ausnahme."),
 ])

DETAIL["nebensatz"]=dict(
 modul="Modul III · Syntax", titel="Nebensatz & Verbendstellung",
 lead="Im deutschen Nebensatz rückt das finite Verb ganz ans Ende (…, weil er müde ist); das Englische behält auch im Nebensatz SVO. Relativsätze verlangen zusätzlich genus- und kasusmarkierte Pronomen.",
 blocks=[
  T([("Nebensatz",f"Verb am Ende: {d('…, dass er kommt')}",f"SVO: {e('… that he comes')}"),
    ("Konjunktion",f"{d('weil/dass/wenn')} + Verbendstellung",f"{e('because/that/if')} + normale Stellung"),
    ("Relativsatz",f"Relativpronomen (Genus+Kasus) + Verb final: {d('der Mann, den ich sah')}",f"{e('who/which/that')}, oft weglassbar"),])
  +NOTE("Der Wechsel V2 (Hauptsatz) → verbfinal (Nebensatz) ist die eigentliche Hürde."),
  P("Nach unterordnenden Konjunktionen steht das Verb am Ende; das Relativpronomen richtet sich in Genus/Numerus nach dem Bezugswort, im Kasus nach seiner Funktion im Nebensatz. Das englische Relativpronomen ist oft tilgbar ("+e("the man I saw")+"), im Deutschen nicht."),
  ITAB([("…, weil er ist müde.","…, weil er müde ist.","SVO im Nebensatz beibehalten","interlingual"),
        ("der Mann ich sah","der Mann, den ich sah","Relativpronomen getilgt (engl. „the man I saw“)","interlingual"),
        ("die Frau, die ich helfe","der Frau, der ich helfe","Kasus im Relativsatz (helfen + Dativ)","intralingual")]),
  P("Nebensatz = Verb ans Ende; Konjunktionstabelle; Relativpronomen-Tabelle + „Kasus nach der Funktion im Nebensatz“; Komma vor dem Nebensatz; vom englischen Satz „übersetzen“ und das Verb umstellen."),
  P("Das englische <i>whom</i> bewahrt den Relativkasus, und Unterordnung ist als Konzept vertraut. Auf „<i>whom</i> = den/dem“ aufzubauen macht das kasusmarkierte Relativpronomen weniger abstrakt; die Verbendstellung ist dann der einzige wirklich neue Schritt."),
 ])

DETAIL["negation"]=dict(
 modul="Modul III · Syntax", titel="Negation (nicht & kein)",
 lead="Das Deutsche negiert mit nicht (Verben, Adjektive, ganze Sätze) und kein (unbestimmte Nomen); das Englische nutzt not/no/don’t. Die Stellung von nicht und die nicht/kein-Wahl sind die Hürden.",
 blocks=[
  T([("Verbnegation",f"{d('Ich komme nicht.')}",f"do-support: {e('I do not come.')}"),
    ("Nomennegation",f"{d('Ich habe kein Auto.')}",f"{e('I have no car / not a car.')}"),
    ("Stellung",f"{d('nicht')} am Satzende / vor dem negierten Glied",f"{e('not')} nach dem Hilfsverb"),])
  +NOTE("Das Deutsche braucht kein „tun“ zur Negation; die nicht/kein-Wahl richtet sich nach dem Bezug."),
  P("Zwei Punkte: die <b>Stellung von nicht</b> (Satzende bzw. vor dem negierten Element, vor Partizip/Infinitiv in der Klammer) und die <b>nicht/kein</b>-Wahl (kein vor unbestimmten/artikellosen Nomen). Kein do-support."),
  ITAB([("Ich tue nicht kommen. / Ich nicht komme.","Ich komme nicht.","do-support / engl. Stellung übertragen","interlingual"),
        ("Ich habe nicht ein Auto.","Ich habe kein Auto.","nicht statt kein bei unbestimmtem Nomen","interlingual"),
        ("Ich nicht habe Zeit.","Ich habe keine Zeit.","Negationsstellung falsch","intralingual")]),
  P("nicht vs. kein regeln (kein vor unbestimmtem/artikellosem Nomen); nicht-Position üben (Satzende / vor dem negierten Glied); kein „tun“; Kontrast "+e("not a / no")+" → "+d("kein")+"."),
  P("Das englische <i>no</i> als Determinierer ("+e("no money")+" = "+d("kein Geld")+") entspricht direkt dem "+d("kein")+" – die Aufteilung <i>not/no</i> existiert im Englischen bereits, nur weniger systematisch. "+d("kein")+" lässt sich an „<i>no</i> + Nomen“ verankern."),
 ])

DETAIL["modalpart"]=dict(
 modul="Modul III · Syntax", titel="Modalpartikeln (doch, ja, mal …)",
 lead="Das Deutsche würzt Sätze mit Modalpartikeln (doch, ja, mal, halt, denn), die abschwächen, betonen oder gemeinsames Wissen signalisieren. Das Englische hat kein direktes Äquivalent und leistet diese Nuancen über Intonation oder Zusätze.",
 blocks=[
  T([(d("doch"),"Widerspruch/Bekräftigung: "+d("Komm doch!"),f"{e('do come / but')}"),
    (d("ja"),"geteiltes Wissen: "+d("Das ist ja toll!"),f"{e('as you know / clearly')}"),
    (d("mal"),"Auflockerung: "+d("Komm mal her."),f"{e('just / for a moment')}"),
    (d("denn"),"Interesse in Fragen: "+d("Was machst du denn?"),f"{e('so / then')}"),],
    head=("Partikel","Funktion (Deutsch)","Englische Wiedergabe"))
  +NOTE("Partikeln sind unbetont und selten wörtlich übersetzbar – sie tragen Haltung, nicht Inhalt."),
  P("Modalpartikeln tragen pragmatische Bedeutung: Ihr Fehlen klingt schroff, ihr falscher Sitz oder ihre Betonung klingt fremd. Schwer wahrnehmbar, weil das Englische dieselbe Nuance über Intonation ausdrückt."),
  ITAB([("Komm her! (Partikel ganz weggelassen)","Komm mal her!","L1 nutzt Intonation statt Partikel","interlingual"),
        ("Was machst du? (wo Interesse gemeint)","Was machst du denn?","Partikel denn fehlt","interlingual"),
        ("Das ist JA toll (betont/falsch platziert)","Das ist ja toll (unbetont)","Partikel wie ein Inhaltswort behandelt","intralingual")]),
  P("Partikeln funktional in Dialogen lehren, nicht über Übersetzung; typische Positionen (Mittelfeld, unbetont); Minimalkontraste ("+d("Komm her / Komm mal her")+"); zuerst rezeptiv, dann produktiv."),
  P("Auch das Englische nuanciert – mit <i>just, then, you know</i>, dem betonenden <i>do</i> (<i>do sit down</i>) und vor allem der Intonation. Die Lernenden auf ihre eigenen englischen Abtönungsmittel aufmerksam zu machen, öffnet die Tür zu den Partikeln als der deutschen Art, dieselbe Aufgabe zu lösen."),
 ])

# === Arbeitsblätter (DaZ/DaF) =============================================
SHEETS = [
 {"id":"ab_gross","t":"Substantivgroßschreibung","lvl":"A1–B1",
  "desc":"Nomen erkennen, Artikelprobe, Nationalitätsadjektive + Lösungen.",
  "pdf":"arbeitsblaetter/ab_grossschreibung.pdf"},
 {"id":"ab_genus","t":"Genus, Artikel & Kasus","lvl":"A2–B1",
  "desc":"Genus-Heuristik, der/den/dem, Pronomen-Kongruenz + Lösungen.",
  "pdf":"arbeitsblaetter/ab_genus-kasus.pdf"},
 {"id":"ab_wortstell","t":"Wortstellung: V2 & Satzklammer","lvl":"A2–B1",
  "desc":"Verb an 2. Stelle, Klammer schließen, Nebensatz verbfinal + Lösungen.",
  "pdf":"arbeitsblaetter/ab_wortstellung.pdf"},
 {"id":"ab_praep","t":"Präpositionen & Kasus (Wechselpräp.)","lvl":"A2–B1",
  "desc":"wohin?/wo?, feste Rektion, into/in ↔ Akk/Dat + Lösungen.",
  "pdf":"arbeitsblaetter/ab_praepositionen.pdf"},
]
SHEET_FOR = {"grossschreibung":SHEETS[0]["pdf"],"genus":SHEETS[1]["pdf"],
             "kasus":SHEETS[1]["pdf"],"wortstell":SHEETS[2]["pdf"],
             "nebensatz":SHEETS[2]["pdf"],"praep":SHEETS[3]["pdf"]}

# === Literatur ============================================================
LIT = {
 "Kontrastive Grammatik & Sprachvergleich DE–EN": [
  dict(a="König, Ekkehard / Gast, Volker", y="2018", t="Understanding English-German Contrasts",
       q="4., neu bearb. Aufl. Berlin: Erich Schmidt Verlag (Grundlagen der Anglistik und Amerikanistik)", cur=True),
  dict(a="Hawkins, John A.", y="1986", t="A Comparative Typology of English and German. Unifying the Contrasts",
       q="London: Croom Helm / Austin: University of Texas Press"),
  dict(a="Kufner, Herbert L.", y="1962", t="The Grammatical Structures of English and German. A Contrastive Sketch",
       q="Chicago: University of Chicago Press (Contrastive Structure Series)"),
  dict(a="Fox, Anthony", y="2005", t="The Structure of German",
       q="2. Aufl. Oxford: Oxford University Press"),
 ],
 "Deutsche Grammatik für Englischsprachige / DaF-Grammatiken": [
  dict(a="Durrell, Martin", y="2020", t="Hammer’s German Grammar and Usage",
       q="7. Aufl. London/New York: Routledge", cur=True),
  dict(a="Helbig, Gerhard / Buscha, Joachim", y="2001", t="Deutsche Grammatik. Ein Handbuch für den Ausländerunterricht",
       q="Berlin/München: Langenscheidt"),
  dict(a="Russ, Charles V. J.", y="1994", t="The German Language Today. A Linguistic Introduction",
       q="London/New York: Routledge"),
  dict(a="Eisenberg, Peter", y="2020", t="Grundriss der deutschen Grammatik (Bd. 1 Das Wort, Bd. 2 Der Satz)",
       q="5. Aufl. Stuttgart: J. B. Metzler", cur=True),
 ],
 "Phonetik / Aussprache / Orthographie": [
  dict(a="Moulton, William G.", y="1962", t="The Sounds of English and German",
       q="Chicago: University of Chicago Press (Contrastive Structure Series)"),
  dict(a="Hall, Christopher", y="2003", t="Modern German Pronunciation. An Introduction for Speakers of English",
       q="2. Aufl. Manchester: Manchester University Press"),
  dict(a="Kohler, Klaus J.", y="1995", t="Einführung in die Phonetik des Deutschen",
       q="2. Aufl. Berlin: Erich Schmidt Verlag"),
 ],
 "Interlanguage, Fehleranalyse & Interferenz": [
  dict(a="Selinker, Larry", y="1972", t="Interlanguage",
       q="International Review of Applied Linguistics (IRAL) 10(3), 209–231"),
  dict(a="Corder, S. Pit", y="1967", t="The Significance of Learners’ Errors",
       q="International Review of Applied Linguistics (IRAL) 5(4), 161–170"),
  dict(a="Lado, Robert", y="1957", t="Linguistics Across Cultures. Applied Linguistics for Language Teachers",
       q="Ann Arbor: University of Michigan Press (klassische Kontrastivhypothese)"),
  dict(a="Swan, Michael / Smith, Bernard (Hg.)", y="2001", t="Learner English. A Teacher’s Guide to Interference and other Problems",
       q="2. Aufl. Cambridge: Cambridge University Press"),
  dict(a="Benholz, Claudia / Lipkowski, Eva", y="2010", t="Fehler und Fehlerkorrektur bei schriftlichen Arbeiten von mehrsprachigen Schülerinnen und Schülern",
       q="in: Bainski/Krüger-Potratz (Hg.), Handbuch Sprachförderung, 2. Aufl., 132–143. Essen: NDS Verlagsgesellschaft", proj=True),
 ],
 "DaF/DaZ, Mehrsprachigkeit & Didaktik (aktuell)": [
  dict(a="Roche, Jörg", y="2020", t="Fremdsprachenerwerb – Fremdsprachendidaktik",
       q="4. Aufl. Tübingen: Narr Francke Attempto (UTB)", cur=True),
  dict(a="Riehl, Claudia Maria", y="2014", t="Mehrsprachigkeit. Eine Einführung",
       q="Darmstadt: WBG"),
  dict(a="Koch, Nikolas / Riehl, Claudia Maria", y="2024", t="Migrationslinguistik. Eine Einführung",
       q="Tübingen: Narr Francke Attempto", cur=True),
  dict(a="James, Carl", y="1998", t="Errors in Language Learning and Use. Exploring Error Analysis",
       q="London/New York: Longman"),
 ],
 "DaZ/DaF-Didaktik & Zweitspracherwerb (Grundlagen)": [
  dict(a="Ahrenholz, Bernt / Oomen-Welke, Ingelore (Hg.)", y="2017", t="Deutsch als Zweitsprache",
       q="Deutschunterricht in Theorie und Praxis, Bd. 9; 4. Aufl. Baltmannsweiler: Schneider Verlag Hohengehren"),
  dict(a="Hoffmann, L. / Kameyama, S. / Riedel, M. / Şahiner, P. / Wulff, N. (Hg.)", y="2017",
       t="Deutsch als Zweitsprache. Ein Handbuch für die Lehrerausbildung",
       q="Berlin: Erich Schmidt Verlag (mit kontrastivem Überblick über Partnersprachen)", proj=True),
  dict(a="Jeuk, Stefan", y="2018", t="Deutsch als Zweitsprache in der Schule. Grundlagen – Diagnose – Förderung",
       q="4. Aufl. Stuttgart: W. Kohlhammer", cur=True, proj=True),
  dict(a="Rösch, Heidi", y="2011", t="Deutsch als Zweit- und Fremdsprache",
       q="Berlin: Akademie Verlag (Studienbuch; Kap. 2: Hypothesen des Zweitspracherwerbs)", proj=True),
  dict(a="Gebele, Diana", y="2018", t="Grammatik im Deutschunterricht mit neu zugewanderten Schülerinnen und Schülern",
       q="in: Gebele/Zepter (Hg.), Deutsch als Zweitsprache. Unterricht mit neu zugewanderten Kindern und Jugendlichen, 158–173. Baltmannsweiler: Schneider Hohengehren", cur=True, proj=True),
  dict(a="Michalak, Magdalena / Kuchenreuther, Michaela (Hg.)", y="2015",
       t="Grundlagen der Sprachdidaktik Deutsch als Zweitsprache",
       q="3. Aufl. Baltmannsweiler: Schneider Verlag Hohengehren"),
  dict(a="Kniffka, Gabriele / Siebert-Ott, Gesa", y="2012", t="Deutsch als Zweitsprache. Lehren und Lernen",
       q="3. Aufl. Paderborn: Schöningh (UTB)"),
  dict(a="Barkowski, Hans / Krumm, Hans-Jürgen (Hg.)", y="2010", t="Fachlexikon Deutsch als Fremd- und Zweitsprache",
       q="Tübingen: A. Francke (UTB)"),
  dict(a="Topalović, Elvira / Michalak, Magdalena", y="2015", t="Sprachreflexion und Grammatik zwischen DaM und DaZ",
       q="in: Michalak/Kuchenreuther (Hg.), Grundlagen der Sprachdidaktik DaZ, 226–250"),
  dict(a="Chlosta, Christoph / Schäfer, Andrea / Baur, Rupprecht S.", y="2017", t="Fehleranalyse",
       q="in: Ahrenholz/Oomen-Welke (Hg.), Deutsch als Zweitsprache (Bd. 9), 353–368", proj=True),
 ],
}
LIT_INTRO = ("Auswahlbibliografie zum Sprachvergleich Deutsch–Englisch und zur DaF/DaZ-Didaktik. "
  "Mit ● markierte Titel liegen als Referenzmaterial im Projekt vor; mit ✦ markierte sind "
  "aktuelle bzw. jüngst aufgelegte Standardwerke (2018+). "
  "Die letzte Rubrik versammelt didaktische und zweitspracherwerbliche Grundlagenwerke "
  "(sprachübergreifend, u. a. aus den DaZ-Literaturempfehlungen der LMU). "
  "Die Liste dient als Referenz – Konzept und Inhalt der Plattform stammen von Dr. Ergun Özsoy.")

# === Wegweiser (Kurzanleitung, nur Web) ===================================
GUIDE = dict(
 titel="Wegweiser",
 untertitel="So nutzen Sie diese Plattform",
 lead=("Was diese Plattform enthält, wie jedes Thema aufgebaut ist und auf welchen Wegen Sie "
   "die Inhalte erschließen können – eine kurze Orientierung."),
 blocks=[
  ("Was diese Plattform ist",
   P("Eine didaktische Plattform zur <b>kontrastiven Linguistik Deutsch–Englisch</b> für die "
     "DaZ-/DaF-Lehramtsausbildung: Deutsch als Ziel-/Zweitsprache aus der Perspektive englischer "
     "Muttersprachler. Sie umfasst <b>20 Themen</b> in drei Modulen (Laut &amp; Schrift · Morphologie · "
     "Syntax), vier unterrichtsfertige <b>Arbeitsblätter</b> mit Lösungen, eine kommentierte "
     "<b>Bibliografie</b> sowie ein <b>Fazit</b> und einen <b>Werkstattbericht</b> – alles auch als PDF.")),
  ("Wie jedes Thema aufgebaut ist",
   P("Alle Themen folgen demselben Fünf-Schritte-Raster:")
   +"<ul class='li'>"
   "<li><b>1 · Kontrastiver Befund</b> – deutsche und englische Struktur nebeneinander</li>"
   "<li><b>2 · Didaktik &amp; DaZ-Relevanz</b> – warum und wann es im Unterricht zählt</li>"
   "<li><b>3 · Interferenzanalyse</b> – Lernerform · Zielform · Ursache · Typ</li>"
   "<li><b>4 · Korrektur &amp; Förderung</b> – konkrete Unterrichtswege</li>"
   "<li><b>5 · Interkulturalität</b> – Mehrsprachigkeit als Ressource</li></ul>"
   +P("<b>Lesekonventionen:</b> <span class='err'>Lernerform</span> (durchgestrichen) vs. "
     "<span class='ok'>Zielform</span>; "+e("englische Tokens")+" kursiv in warmer Farbe, "
     +d("deutsche Beispiele")+" in Schreibmaschinenschrift; die Herkunft eines Fehlers zeigt der Typ "
     "<span class='tag typ il'>interlingual</span> (aus der L1) bzw. "
     "<span class='tag typ al'>intralingual</span> (im Deutschen selbst angelegt).")),
  ("Drei Wege durch die Themen",
   "<ul class='li'>"
   "<li><b>Systematisch:</b> den Modulen folgen (Laut &amp; Schrift → Morphologie → Syntax) – "
   "die sprachsystematische Ordnung.</li>"
   "<li><b>Nach Priorität:</b> im Menü <i>★ Nach Priorität</i> – Themen sortiert nach Häufigkeit, "
   "Fossilisierungsgefahr und Lehrplan-Gewicht; <span class='kern' style='padding:1px 7px'>★ Kern</span>-Themen "
   "lohnen den frühesten Zugriff.</li>"
   "<li><b>Anlassbezogen (diagnostisch):</b> von einer beobachteten Lernerform ausgehen – über die "
   "<i>Suche</i> das passende Thema finden und die Interferenzanalyse als Diagnosehilfe nutzen.</li></ul>"),
  ("Materialien zum Mitnehmen",
   P("Jedes Thema gibt es als <b>PDF-Dossier</b> (Button auf der Themenseite), dazu vier "
     "<b>Arbeitsblätter mit Lösungsschlüssel</b>, die <b>Literaturliste</b>, das <b>Fazit</b> und den "
     "<b>Werkstattbericht</b> als PDF – alle druckfertig im selben Layout.")),
  ("Weiterführende Seiten",
   P("<b>Fazit &amp; Ausblick</b> bündelt, was der Sprachvergleich lehrt (unten links im Menü). "
     "Der <b>Werkstattbericht</b> dokumentiert, wie die Plattform entstanden ist. Die <b>Literatur</b>-Seite "
     "belegt die Quellen – Titel mit ● liegen dem Projekt als Referenzmaterial vor. "
     "Konzept &amp; Inhalt: Dr. Ergun Özsoy, LMU München.")),
 ])

# === Fazit & Ausblick ======================================================
FAZIT = dict(
 titel="Fazit & Ausblick",
 untertitel="Was der Sprachvergleich lehrt",
 lead=("Zwanzig Themen in drei Modulen – und ein wiederkehrendes Muster: Das Deutsche wird "
   "verständlicher, wenn man es durch die Brille des Englischen betrachtet. Dieses Fazit bündelt "
   "die Befunde der Themen-Dossiers und formuliert Folgerungen für den DaZ-/DaF-Unterricht."),
 blocks=[
  ("Der Leitgedanke: Deutsch durch eine andere Brille",
   P("Wer Deutsch als Erstsprache spricht, hält Genus, Verbzweitstellung oder Satzklammer für "
     "selbstverständlich. Sichtbar werden diese Kategorien erst im Kontrast – durch die Brille einer "
     "Sprache, die sie anders oder gar nicht kennt. Der Sprachvergleich macht so die Struktur des "
     "Deutschen selbst zum Gegenstand: Was von innen „natürlich“ wirkt, erweist sich als <i>eine</i> "
     "Bauform unter mehreren möglichen.")
   +P("Der Nutzen ist doppelt. <b>Lernende</b> verstehen, warum ihnen das Deutsche an bestimmten "
     "Stellen Mühe macht – und dass ihre „Fehler“ meist folgerichtige Hypothesen sind. <b>Lehrende</b> "
     "gewinnen ein diagnostisches Raster: Sie erkennen, welche Lernerform aus der L1 stammt, welche im "
     "Deutschen selbst angelegt ist – und wo die Erstsprache als Brücke trägt.")),
  ("Was der Vergleich zeigt",
   "<ul class='li'>"
   "<li><b>Lernerfehler sind selten zufällig.</b> Sie folgen Regeln – entweder denen der Erstsprache "
   "(<i>interlingual</i>) oder einer Übergeneralisierung des Deutschen (<i>intralingual</i>). Wer die "
   "Ursache kennt, korrigiert gezielter.</li>"
   "<li><b>Schwierigkeit ist relativ zur L1.</b> Für englischsprachige Lernende liegt die Hauptlast in "
   "der Morphologie (Genus, Kasus, Adjektivdeklination) und in der Wortstellung (V2, Satzklammer, "
   "Nebensatz) – genau dort, wo das Englische seine Flexion abgebaut und seine Satzstellung fixiert hat.</li>"
   "<li><b>Verwandtschaft hilft – und täuscht.</b> Die gemeinsame germanische Herkunft liefert Kognaten, "
   "parallele starke Verben und vertraute Konzepte; dieselbe Nähe erzeugt aber „falsche Freunde“ und "
   "übertragene Muster ("+e("do")+"-support, Progressiv, englische Lautwerte vertrauter Buchstaben).</li>"
   "<li><b>Jede Erstsprache bringt Ressourcen mit.</b> Reste von Kasus ("+e("him, whom")+"), Umlaut "
   "("+e("man/men")+") und Verbzweit ("+e("Never have I seen …")+") zeigen: Vieles am Deutschen ist im "
   "Englischen angelegt – es muss nur reaktiviert werden.</li></ul>"),
  ("Das Profil der L1 Englisch: Hürden und Ressourcen",
   P("Aus den zwanzig Einzelbefunden ergibt sich ein klares Gesamtprofil:")
   +"<table><tr><th>Typische Hürden (aus L1-Sicht)</th><th>Ressourcen &amp; Brücken</th></tr>"
   "<tr><td><ul class='li'>"
   "<li>Kasus &amp; Adjektivdeklination – Flexion im Englischen weitgehend abgebaut</li>"
   "<li>Genus &amp; Artikel – Kategorie ohne L1-Entsprechung</li>"
   "<li>V2, Satzklammer, Nebensatz-Verbendstellung – festes SVO der L1</li>"
   "<li>Zeitformen &amp; Aspekt – kein deutsches Progressiv, andere Perfekt-Verteilung</li>"
   "<li>Substantivgroßschreibung – gegenläufige L1-Konvention</li>"
   "<li>ö/ü, ich-/ach-Laut, Auslautverhärtung – neue Laute bzw. Lautregeln</li>"
   "</ul></td><td><ul class='li'>"
   "<li>Kognaten &amp; gemeinsamer Ablaut ("+e("sing/sang/sung")+" = "+d("singen/sang/gesungen")+")</li>"
   "<li>Pronomen-Kasus ("+e("I/me, whom")+" → "+d("ich/mich, den/dem")+")</li>"
   "<li>"+e("thou/thee")+" als historische du/dich-Parallele</li>"
   "<li>"+e("into/in")+" ≈ Akkusativ/Dativ der Wechselpräpositionen</li>"
   "<li>"+e("would / if I were")+" ≈ Konjunktiv II; "+e("get")+"-Passiv ≈ werden-Passiv</li>"
   "<li>V2-Reste ("+e("Never have I …")+") und phrasal verbs ≈ trennbare Verben</li>"
   "</ul></td></tr></table>"
   +NOTE("Dasselbe Deutsch – aber ein eigenes Anforderungsprofil: Welche Themen „schwer“ sind, entscheidet die Erstsprache mit.")),
  ("Folgerungen für den DaZ-/DaF-Unterricht",
   "<ul class='li'>"
   "<li><b>1 · Fehler diagnostisch lesen.</b> Lernerformen sind Fenster in die Lernersprache. Vor der "
   "Korrektur steht die Ursachenfrage: interlingual, intralingual – oder ein normaler Entwicklungsschritt?</li>"
   "<li><b>2 · Kontrastiv bewusst machen – gezielt und dosiert.</b> Sprachvergleich dort einsetzen, wo "
   "die L1 systematisch interferiert oder eine Brücke bietet; er ist Werkzeug, kein Dauerprinzip.</li>"
   "<li><b>3 · Ressourcen aktivieren.</b> Vorhandenes Wissen (Kognaten, Pronomen-Kasus, V2-Reste) "
   "explizit nutzen: Neues an Bekanntem verankern statt bei null zu beginnen.</li>"
   "<li><b>4 · Priorisieren.</b> Häufigkeit, Fossilisierungsgefahr und curriculares Gewicht bestimmen "
   "die Reihenfolge – die ★-Kernthemen zuerst.</li>"
   "<li><b>5 · Fehlertoleranz mit Korrekturplan.</b> Entwicklungsfehler zulassen, fossilisierungs­gefährdete "
   "Kontraste (Adjektivdeklination, V2) dagegen früh und konsequent fördern.</li></ul>"),
  ("Grenzen & Ausblick",
   P("Der kontrastive Vergleich <b>erklärt und diagnostiziert</b> – er prognostiziert nicht alles. Die "
     "starke Kontrastivhypothese gilt als überholt; Erwerb verläuft in Phasen, individuelle Faktoren "
     "(Alter, Kontakt, Motivation) wirken mit, und viele „typische“ Fehler betreffen vor allem "
     "erwachsene Lernende. Der Vergleich ist deshalb ein <i>Diagnose- und Erklärungsinstrument</i> im "
     "Rahmen der Lernersprachen-Theorie – nicht ihr Ersatz.")
   +P("Das Fünf-Schritte-Raster dieser Plattform ist auf weitere Erstsprachen übertragbar: Jede L1 "
     "erzeugt ihr eigenes Profil aus Hürden und Ressourcen. Die Plattform bleibt ein lebendes "
     "Arbeitsinstrument – Erweiterungen werden im Werkstattbericht dokumentiert; Quellen auf der "
     "Literatur-Seite.")),
 ])

def app_json():
    return {"modules":MODULES,"detail":DETAIL,"sheets":SHEETS,
            "sheetFor":SHEET_FOR,"blocknames":BLOCKNAMES,"lit":LIT,"litIntro":LIT_INTRO,
            "fazit":FAZIT,"guide":GUIDE}
