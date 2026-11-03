# Study Workspace — sources for the Providence division

Staging site only (248834710), 2 November 2026. Production was not touched.

## What was found

None of the Providence books (Isaiah to Malachi) had a Study panel in the Parallel Reader.

## What was done (sources now, prose later)

Same approach as the other divisions (see `REPORT.md` and `REPORT-judgement.md`):

1. **Every Providence chapter in the Parallel Reader now has a working Study panel**: 245 chapters, 5,356 verse rows, in all 16 books (Isaiah, Jeremiah, Ezekiel, Daniel, Hosea, Joel, Amos, Obadiah, Jonah, Micah, Nahum, Habakkuk, Zephaniah, Haggai, Zechariah, Malachi).
2. **Every available site source is in the panel**: Hebrew–Greek, Latin–Greek and KJV–Greek comparisons (every layer, with ratings and links), Saints Translation notes, Study Edition notes, Disparate Study passages, chapter notes, Word Notes word studies, section headings, and live cross-references.
3. Tabs with no written prose say so, as in the other divisions.

**New comparison layout.** Most Providence Hebrew–Greek cards keep layers 2–5 (Rabbinic teaching, Saints' teaching, combined classification, how the difference arose) inside one collapsed block titled "2–5. Teaching, combined classification, and origins". The extractor now reads that block and splits it into its four layers; all 5,249 Hebrew–Greek entries carry their teaching layers. The change applies only to such grouped blocks: a rebuild of Judgement books comes out byte-identical to what is stored.

## Counts (source studies by verse)

| Book | Chapters | Verses | Hebrew–Greek | Latin–Greek | KJV–Greek | Saints notes | Study Edition | Disparate Study | Word studies | Headings | Chapter notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Isaiah | 66 | 1,289 | 1,289 | 1,290 | 1,290 | 53 | 293 | 143 | 2,628 | 297 | 132 |
| Jeremiah | 52 | 1,299 | 1,299 | 1,299 | 1,297 | 13 | 258 | 87 | 2,514 | 249 | 104 |
| Ezekiel | 48 | 1,267 | 1,267 | 1,266 | 1,267 | 13 | 285 | 107 | 2,118 | 197 | 96 |
| Daniel | 12 | 451 | 344 | 519 | 346 | 12 | 67 | 28 | 747 | 74 | 24 |
| Hosea | 14 | 197 | 197 | 198 | 197 | 0 | 56 | 40 | 425 | 51 | 28 |
| Joel | 4 | 73 | 73 | 73 | 73 | 0 | 19 | 8 | 155 | 14 | 8 |
| Amos | 9 | 146 | 146 | 147 | 146 | 0 | 44 | 33 | 311 | 40 | 18 |
| Obadiah | 1 | 21 | 21 | 21 | 21 | 0 | 8 | 4 | 48 | 4 | 2 |
| Jonah | 4 | 48 | 48 | 48 | 48 | 0 | 25 | 7 | 101 | 11 | 8 |
| Micah | 7 | 105 | 105 | 104 | 105 | 0 | 39 | 29 | 215 | 23 | 14 |
| Nahum | 3 | 47 | 47 | 47 | 47 | 0 | 15 | 14 | 116 | 9 | 6 |
| Habakkuk | 3 | 56 | 56 | 56 | 56 | 0 | 15 | 16 | 127 | 10 | 6 |
| Zephaniah | 3 | 53 | 53 | 53 | 53 | 0 | 15 | 11 | 130 | 10 | 6 |
| Haggai | 2 | 38 | 38 | 38 | 38 | 0 | 10 | 3 | 84 | 6 | 4 |
| Zechariah | 14 | 211 | 211 | 211 | 211 | 0 | 62 | 33 | 437 | 46 | 28 |
| Malachi | 3 | 55 | 55 | 55 | 55 | 0 | 18 | 12 | 119 | 13 | 6 |
| **Total** | **245** | **5,356** | **5,249** | **5,425** | **5,250** | **91** | **1,229** | **575** | **10,275** | **1,054** | **490** |

Joel has 4 chapters and Malachi 3, as on the site.

**Ratings.** Every Hebrew–Greek entry is rated (5,249). The Latin–Greek studies are almost all marked *Text: review pending* on the site (82 rated) and the KJV–Greek studies *Text: classification open* (64 rated); the panel shows them as open. 106 verses have no rating, all in Daniel (66 in the Greek additions to chapter 3, 37 in Daniel 1 (see below) and 3 in chapter 4).

**Cross-references.** Built live; checked for one chapter of each book (e.g. Isaiah 53: 260 references; Malachi 3: 638). Almost all are reviewed; a few per chapter appear under *Not yet reviewed*.

Per-chapter counts: `coverage-providence.csv`.

## For the site owner: Daniel

- **Daniel 13–14 (Susanna, Bel and the Dragon)** have chapter pages and Latin/KJV comparison cards, but the Parallel Reader has no rows for them, so they have no Study panel.
- **Daniel 1 shows 37 extra rows (1:22–1:62)** in the Parallel Reader. They hold only Latin-column text from Susanna and Bel and the Dragon (linked to `vulgate-comparison/14/` and `/15/`). The panel reflects what the reader shows; the fix belongs in the Parallel Reader's Daniel data, which was not changed here.

## Where things are

- Saints Parallel Reader **1.7.0** on staging: adds Providence (1,142 chapters across six divisions).
- Data: 490 private `saints_ws_chapter` records (245 chapter + 245 source records); staging now holds 2,284 records, every Providence and Judgement record matching its manifest byte for byte.
- Helper: Saints Pentateuch Work **1.14.0** (reads the Providence books).
- Checks run: data routes return 200 (Isaiah 53, Isaiah 7 sources, Daniel 3, Malachi 3 sources, Obadiah 1) and 404 for Daniel 13 and Malachi 4; a Parallel Reader request enqueues the panel for Isaiah 53, Zechariah 14 and Joel 4 and not for Daniel 13; cross-references build for one chapter of every book; the panel ran in a browser on Isaiah 53, Daniel 3, Obadiah 1, Zechariah 9, Malachi 3 and Ezekiel 37 through every tab with no script errors.

## Still to do

- Write the study prose for all 245 chapters.
- Latin and KJV assessments still open on the site; they appear in the panel when done.
- Daniel 1 rows and Daniel 13–14, as above.
- Production: nothing has been copied there.
