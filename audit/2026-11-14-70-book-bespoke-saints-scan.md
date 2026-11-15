# 70-Book Latin-Translation Literal & Bespoke Saints English Scan (14 November 2026)

## 1. Repository-Wide Corpus Totals
- **Total Books / Chapters / Rows:** 70 books · 1,290 chapters · 34,575 reader rows (`34,429` with Latin; `146` locked no-Vulgate rows).
- **Douay-Rheims Scaffold Concentration:** `6,022` of `7,956` NT readings (`3,813` of `4,780` in Gospels/Acts; `2,158` of `2,357` in Romans–2 Peter; `41` of `819` in remaining NT/Revelation), vs. `24,843` of `26,251` fresh OT readings.
- **Open Structural Queues:** `481` unapplied English review proposals (`24` major), `61` English–Latin span findings, and `687` Clementine verses lacking Latin in the record (led by Sirach `248`, Esther `105`, Daniel `89`, Jeremiah `48`, 1 Samuel `40`, Psalms `29`, Numbers `28`).

## 2. Full 70-Book Pattern Scan Across `<Book>.txt` Files
| Pattern | Affected Books | Key Findings & Disposition |
| :--- | ---: | :--- |
| `"You all"` (prohibited `"all"` insertion) | 23 books | Top concentrations in Philippians (8), John (6), Acts (4); replace with plain plural `you` per `TRANSLATION-STANDARD.md` §1 & §3. |
| `"risen again"` (unattested `"again"` for `resurrexit`/`surrexit`) | 13 books | Mark (4), Luke (2), 1 Corinthians (2), John (1), Romans (1), 2 Timothy (1), plus 7 others; inspect each against Latin `iterum`/`rursus`. |
| `Kittim` / `Chislev` (Hebrew spellings in Vulgate column) | 4 books | `Kittim` in 1 Maccabees (3) and 1 Chronicles 1:7 (1) where Vulgate reads `Cethim`; `Chislev` in Nehemiah (1) and Zechariah (1) where Vulgate reads `Casleu`. |
| `Yahweh` | 0 books | Clean across all 70 books. |
| Douay-Rheims negative/archaic syntax | 18+ books | `"know not"` (14 books), `"believe not"` (4 books / 10 matches), `"receive not"` (4 books), `"make not"` (2 books), `"in building"` (2 books), `"have well drunk"` (1 book). |
| Glued Latin initials (`Ohomo`, `Oaltitudo`) | 1 book (2 verses) | `Romans 9:20` and `Romans 11:33` repaired on this branch in `romans/Romans.txt`. |

## 3. Resolution of `source-check-needed.json` Discrepancies
- **`Matthew 17:4` (`matthew-17-4`):** External Vulgate witness confirms second `hic` (`si vis, faciamus hic tria tabernacula`), validating `"let us make here"` once `hic` is restored to recorded Latin.
- **`1 Corinthians 12:28` (`1-corinthians-12-28`):** Standard Clementine reads `tertio doctores` (`"thirdly teachers/doctors"`); recorded `exinde doctores` is a dittography from later `exinde gratias`.
- **`Matthew 2:5` (`matthew-2-5`):** Verify `At illi dixerunt [ei]` against printed Clementine; restore `ei` in Latin or omit `"to him"` so Latin and English match.
