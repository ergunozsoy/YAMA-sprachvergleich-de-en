# Werkstattbericht: YAMA-DaZ-Sprachvergleich — Englisch

**Deutsch ↔ Englisch als kontrastive DaZ/DaF-Plattform — Architektur, Arbeitsablauf, Übertragbarkeit**

Dr. Ergün Özsoy · LMU München · **Lebendes Dokument** — wird mit dem Projekt fortgeschrieben · Stand: Juli 2026

---

## 1. Ziel und Gegenstand

Diese Notiz dokumentiert, wie die englischsprachige Fassung der Sprachvergleichs­plattform
entstanden ist – als **Schwesterprojekt** zu *YAMA-DaZ-Sprachvergleich* (Deutsch–Türkisch).
Sie zeigt zugleich, dass das zugrunde liegende Muster **reproduzierbar** ist: Eine neue
L1-Perspektive lässt sich mit geringem Aufwand aufsetzen, weil Fachkonzept, Datenmodell und
Technik sauber getrennt sind.

- **Gegenstand:** kontrastive Linguistik **Deutsch–Englisch** für die DaZ-/DaF-Lehramtsausbildung –
  Deutsch als Ziel-/Zweitsprache aus der Perspektive **englischer Muttersprachler**.
- **Umfang:** 20 Themen in drei Modulen (Laut & Schrift · Morphologie · Syntax), jedes im festen
  Fünf-Schritte-Raster (Kontrastiver Befund → Didaktik & DaZ → Interferenzanalyse →
  Korrektur & Förderung → Mehrsprachigkeit als Ressource), dazu vier unterrichtsfertige
  Arbeitsblätter mit Lösungsschlüssel und eine kommentierte Bibliografie.

Leitidee unverändert: **Fachwissen zuerst, Technik als Dienerin.** Die kontrastive Linguistik
bestimmt die Struktur; die Technik bleibt so einfach wie möglich.

## 2. Architektur im Überblick

Identisch zur Deutsch–Türkisch-Fassung – bewusst als *eine einzige HTML-Datei* plus
PDF-Generator, ohne Server, ohne Build-Framework:

| | DE–EN-Sprachvergleich |
|---|---|
| Typ | Eine einzige `index.html` (aus Template + Datenquelle erzeugt) |
| Inhalte | zentral in `content.py` (Strukturbaum, Themen, Arbeitsblätter, Literatur) |
| Build | `build_index.py` (Seite) · `gen_pdfs.py` (25 PDFs, WeasyPrint) |
| Hosting | GitHub Pages |
| Automatik | GitHub Actions baut Seite + PDFs bei jedem Push |
| Pflegeaufwand | minimal |

### Das wichtigste Prinzip: Trennung von Inhalt und Code

Alle fachlichen Inhalte liegen in **`content.py`** – einer einzigen Quelle, aus der sowohl die
interaktive Seite als auch sämtliche PDFs erzeugt werden. Eine Korrektur an einer Stelle wirkt in
alle Ausgaben (*ein Quelltext, viele Dokumente*). Neue Themen, Beispiele oder Arbeitsblätter sind
**reine Datenpflege** – ohne Programmierung. Konvention: englische Tokens (die L1) stehen in
`<span class="eng">`, deutsche Beispiele in `<span class="ex">`.

## 3. Vom Türkischen zum Englischen — die inhaltliche Übertragung

Die Übertragung war **keine Übersetzung**, sondern eine fachliche Neubestimmung des Kontrasts.
Das methodische Gerüst (Interlanguage-Rahmen, Fünf-Schritte-Raster, interlingual/intralingual)
blieb; der sprachvergleichende Gehalt wurde vollständig neu erhoben:

1. **Streichen, was für Englisch irrelevant ist:** Vokalharmonie, Sprossvokal (Epenthese),
   Evidentialität, agglutinierende Suffixketten – Phänomene der türkischen L1 ohne Entsprechung
   im Englischen.
2. **Aufnehmen, was englische Lernende typisch trifft:** Substantivgroßschreibung, ö/ü und der
   ach-/ich-Laut, das Vier-Kasus-System, die Adjektivdeklination, der fehlende Progressiv
   (*I am reading* → Präsens), das englische do-support in Fragen/Negation, die Modalpartikeln.
3. **Kognaten als Ressource nutzen** (Block 5 jedes Themas): das germanische Erbe wird zum
   Lernvorsprung – *man/men → Mann/Männer*, *thou/thee → du/dich*, das *get*-Passiv → *werden*,
   die englischen V2-Reste (*Never have I seen …*).

Ergebnis: dieselbe Bauform, dieselbe Didaktik – ein fachlich eigenständiges Werk für eine andere
Ausgangssprache. **Gute Architektur macht die zweite Sprachrichtung billig.**

## 4. Arbeitsablauf Schritt für Schritt

Der bewährte, konservative Zyklus – *lesen → ändern → prüfen → veröffentlichen → verifizieren*:

1. **Fachliche Entscheidung** (Mensch): Themenset, Beispiele, Kontraste für die L1 Englisch.
2. **Ist-Stand einlesen:** Struktur und Konventionen aus dem bestehenden Repository übernehmen.
3. **Minimal-invasiv arbeiten:** nur ergänzen/ersetzen, Bestehendes nicht umbauen.
4. **Vor dem Hochladen validieren:** `content.py` parst? Seite baut? Alle 25 PDFs erzeugt?
   Optische Kontrolle je einer Themenseite, eines Arbeitsblatts und der Literaturseite.
5. **Veröffentlichen** über GitHub (Edit + Commit, keine Drag-&-Drop-Duplikate).
6. **Verifizieren:** Actions-Lauf grün? Live-Seite aktualisiert? PDFs korrekt verlinkt?

## 5. KI-Einsatz und Transparenz

Die technische Umsetzung (Einlesen der Ist-Stände, Einarbeiten der Inhalte, Syntaxprüfung,
PDF-Erzeugung, optische Verifikation, Verifikation der Literaturangaben) erfolgte in
Zusammenarbeit mit einem KI-Assistenten (Claude, Anthropic). Die **fachlichen Inhalte, die
didaktischen Entscheidungen und die Qualitätskontrolle** liegen durchgehend beim Autor; die KI
fungierte als Werkzeug der Implementierung unter fachlicher Steuerung. Bibliografische Angaben
wurden gegen unabhängige Quellen geprüft. Dieses Vorgehen folgt den einschlägigen
Transparenzempfehlungen (COPE; DFG; Europäische Kommission) zum KI-Einsatz in Forschung und Lehre.

## 6. Lessons Learned — Übertragbarkeit als Prüfstein

1. **Inhalt von Code trennen** – die zweite Sprachrichtung ist reine Datenpflege.
2. **Das Datenmodell trägt** – Fünf-Schritte-Raster und Interferenztypologie gelten sprach­übergreifend.
3. **Nicht übersetzen, sondern neu kontrastieren** – jede L1 hat ihr eigenes Fehler- und Ressourcenprofil.
4. **Kognaten sind Gold** – bei nah verwandten Sprachen (EN–DE) wird Block 5 besonders stark.
5. **Vor dem Hochladen validieren, nach dem Hochladen verifizieren** – auch die Quellenangaben.
6. **Ein Muster, viele Sprachen** – die Plattform ist als Familie angelegt (DE–TR, DE–EN, …).

## 7. Ausblick

Geplant sind: ein Werkstatt-Abgleich zwischen den Sprachfassungen; Ausbau der Bibliografie auf
Basis einer gesichteten Quellensammlung (kontrastive Grammatik DE–EN, DaF-Phonetik,
Fehleranalyse); optional weitere L1-Perspektiven nach demselben Muster; perspektivisch die
Einbindung als ergänzendes Material in die persönliche LMU-Seite.

## 8. Änderungsjournal

| Datum | Änderung |
|---|---|
| Juli 2026 | Navigation neu geordnet: Meta-Seiten (Literatur, Werkstatt, Fazit) ans Ende der Sidebar; oben neue Seite „Wegweiser – so nutzen Sie diese Plattform“ (Aufbau, Lesekonventionen, drei Nutzungswege, Materialien). Kontakt-&-Feedback-Block am Sidebar-Ende (e.oezsoy@lmu.de). Parallel in der DE–TR-Fassung. |
| Juli 2026 | Neue Seite „Fazit & Ausblick – Was der Sprachvergleich lehrt“: Synthese der Befunde, L1-Profil (Hürden/Ressourcen), didaktische Folgerungen, Grenzen; als eigene Seite + PDF, verlinkt in Sidebar und Startseite. Parallel in der DE–TR-Fassung. |
| Juli 2026 | Literatur erweitert nach Sichtung der LMU-DaZ-Quellensammlung (11 Scans geprüft, Zitate verifiziert): Rubrik „Grundlagen“ um Rösch 2011 und Gebele 2018 ergänzt, Benholz/Lipkowski 2010 (Fehleranalyse) aufgenommen; ●-Markierung „im Projekt“ eingeführt. Parallel in der DE–TR-Fassung (+ Şahiner 2012, Belke 2012). |
| Juli 2026 | Erstfassung der englischen Plattform: 20 Themen (L1 Englisch), 4 Arbeitsblätter, Literaturseite (verifiziert); Werkstattbericht angelegt. |

*Neue Einträge oben anfügen — eine Zeile pro Entwicklungsschritt genügt.*

---

*Schwesterprojekt zu YAMA-DaZ-Sprachvergleich (Deutsch–Türkisch). Konzept & alle Rechte:
Dr. Ergun Özsoy, LMU München. Dieses Dokument liegt im Repository als `YAMA_WERKSTATT.md`.*
