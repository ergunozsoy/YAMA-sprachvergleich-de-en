# Sprachvergleich Deutsch ↔ Englisch — DaZ/DaF-Lernplattform

Interaktive Lehr- und Lernplattform zur **kontrastiven Linguistik Deutsch–Englisch**
für die **DaZ-/DaF-Lehramtsausbildung**: Deutsch als Ziel-/Zweitsprache aus der
Perspektive **englischer Muttersprachler**, die Deutsch lernen.
Konzept & alle Rechte: **Dr. Ergun Özsoy**, LMU München.

> Englischsprachiges Schwester­projekt zu **YAMA-DaZ-Sprachvergleich** (Deutsch–Türkisch).
> Gleiches didaktisches Modell (5 Schritte je Thema), gleiche Technik – neue L1-Perspektive.

## Inhalt
- **20 Themen** in 3 Modulen (Laut & Schrift · Morphologie · Syntax) — je 5 Blöcke:
  Kontrastiver Befund · Didaktik & DaZ · Interferenzanalyse (interlingual/intralingual) · Korrektur & Förderung · Interkulturalität.
- **20 Themen-Dossiers** als PDF (`themen/<id>.pdf`).
- **4 DaZ/DaF-Arbeitsblätter** mit Lösungsschlüssel (`arbeitsblaetter/`).
- **Literatur**-Seite + PDF (`literatur/literatur-de-en.pdf`): kontrastive Grammatik DE–EN,
  DaF-Grammatiken, Phonetik/Aussprache, Interlanguage & Fehleranalyse, aktuelle DaF-Forschung.

Theoretischer Rahmen: **Lernersprache-/Interlanguage-Hypothese** (nicht die widerlegte Kontrastivhypothese);
Fehler werden in *intralingual* (systematisch) vs. *interlingual* (aus der L1 Englisch) unterschieden.

## Themenübersicht (englische L1)
| Modul | Themen |
|---|---|
| I · Laut & Schrift | Alphabet & Buchstaben-Lautwerte (w/v/j/z), ch-/r-Laut & Konsonanten, Auslautverhärtung, Vokale: Länge & Umlaute (ä ö ü), Substantivgroßschreibung & ß |
| II · Morphologie | Genus & Artikel, Kasus (4 Fälle), Plural, Adjektivdeklination, Pronomen & Anrede (du/Sie), Verben & trennbare Verben, Zeitformen & Aspekt (kein Progressiv), Konjunktiv II & I, Passiv, Präpositionen & Wechselpräpositionen |
| III · Syntax | Satzarten & Fragebildung (do-support), Wortstellung (V2 & Satzklammer), Nebensatz & Verbendstellung, Negation (nicht & kein), Modalpartikeln |

Gegenüber der Deutsch–Türkisch-Fassung entfallen für Englisch irrelevante Themen
(Vokalharmonie, Sprossvokal, Evidentialität); neu sind typisch englische Hürden
(Substantivgroßschreibung, ö/ü, Adjektivdeklination, fehlender Progressiv,
do-support, Modalpartikeln).

## Aufbau / Build
Eine einzige Inhaltsquelle: **`content.py`**.
```
python3 build_index.py   # erzeugt index.html aus index.template.html + content.py
python3 gen_pdfs.py      # erzeugt themen/, arbeitsblaetter/, literatur/ (WeasyPrint)
```
`requirements.txt`: `weasyprint>=60`. Der GitHub-Action-Workflow `.github/workflows/build-pdfs.yml`
baut die PDFs bei jedem Push automatisch neu.

Konvention in `content.py`: englische Tokens (L1) stehen in `<span class="eng">` (kursiv, warme Farbe),
deutsche/neutrale Beispiele in `<span class="ex">`.

## Veröffentlichen (GitHub Pages)
1. Repository anlegen — empfohlener (URL-sicherer) Name: `yama-sprachvergleich-de-en`.
2. Dateien hochladen (Inhalt dieses Ordners).
3. *Settings → Pages → Branch: main /(root)* → Speichern.
4. Seite erscheint unter `https://<user>.github.io/<repo>/`.

© Dr. Ergun Özsoy – alle Rechte vorbehalten.
