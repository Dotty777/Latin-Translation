# Study Workspace — sources for the Law, Salvation, Wisdom and Glory divisions

Staging site only (248834710), 2 November 2026. Production was not touched.

## What was found

The Study Workspace panel of the Parallel Reader worked for **Genesis 1 only**. Every other chapter of the four divisions (574 chapters) had no panel. Genesis 1's own readings were current (no stale readings), but its cross-references were a fixed file and its links pointed at the production address.

## What was done (sources now, prose later)

1. **Every chapter now has a working Study panel**: 575 chapters, 15,775 verse rows, in all 17 books (Genesis–Deuteronomy, Matthew–John, Psalms, Proverbs, Ecclesiastes, Song of Songs, Lamentations, Wisdom of Solomon, Sirach, Revelation).
2. **Every available site source is in the panel**, taken from the pages the Parallel Reader links to and from the site's study pages:
   - Hebrew–Greek comparisons (Law and Wisdom), Latin–Greek comparisons, King James–Greek comparisons: every layer of each comparison (word comparison, Jewish/Catholic/Protestant reception, medieval Christian reception, combined classification, how the difference arose), with each source's rating and a link to the full study.
   - Saints Translation notes from the chapter pages (wording notes, numbered notes, Revelation and Gospel footnotes).
   - Study Edition notes (Law and Wisdom), assigned to every verse of each note's range, with the chapter summary, wording changes and open questions.
   - Disparate Study passage studies (Law and Song of Songs).
   - Chapter notes: the current Bespoke editorial notes and other chapter-level notes on each Saints chapter page.
   - Word studies from the Word Notes plugin (word, Greek, literal sense, theme, note, see-also).
   - Section headings from each Saints chapter page.
   - Cross-references, now built live from the cross-reference evidence and its reviews (supported, looser, reviewed and not supported, and a new **Not yet reviewed** group with the evidence note), so new reviews appear without rebuilding anything.
3. **Tabs with no written prose say so.** Overall Message, the Unseen Change summary, Instructions and the lexicon say they have not been written yet. Overall Message shows the four translations and each source's rating instead; Unseen Change shows every source study in full. Genesis 1 keeps its written notes and now also shows all its source studies.
4. The verse dot and the chip in Unseen Change come from the highest source rating (Divergent or Disparate = clear difference; Similar or Different = subtle; Same = none), labelled as a source rating until prose is written.

Original-language verses are not collected: Latin, Hebrew and Greek reading blocks are skipped; only the short phrases inside the English notes remain.

## Counts (source studies by verse)

| Division | Book | Chapters | Verses | Hebrew–Greek | Latin–Greek | KJV–Greek | Saints notes | Study Edition | Disparate Study | Word studies | Headings | Chapter notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Law | Genesis | 50 | 1,534 | 1,534 | 1,534 | 1,534 | 110 | 575 | 174 | 1,523 | 182 | 99 |
| Law | Exodus | 40 | 1,195 | 1,222 | 1,213 | 1,222 | 0 | 520 | 25 | 1,664 | 139 | 78 |
| Law | Leviticus | 27 | 859 | 859 | 859 | 859 | 70 | 342 | 86 | 1,264 | 111 | 54 |
| Law | Numbers | 36 | 1,287 | 1,288 | 1,257 | 1,288 | 117 | 484 | 176 | 1,840 | 174 | 72 |
| Law | Deuteronomy | 34 | 959 | 959 | 957 | 959 | 123 | 372 | 96 | 1,538 | 143 | 68 |
| Salvation | Matthew | 28 | 1,068 | 0 | 1,067 | 1,068 | 68 | 0 | 0 | 2,244 | 188 | 28 |
| Salvation | Mark | 16 | 678 | 0 | 677 | 679 | 19 | 0 | 0 | 1,345 | 114 | 16 |
| Salvation | Luke | 24 | 1,149 | 0 | 1,149 | 1,149 | 20 | 0 | 0 | 2,310 | 195 | 24 |
| Salvation | John | 21 | 878 | 0 | 878 | 878 | 19 | 0 | 0 | 1,480 | 134 | 21 |
| Wisdom | Psalms | 151 | 2,534 | 2,526 | 2,527 | 2,526 | 20 | 479 | 0 | 5,526 | 0 | 302 |
| Wisdom | Proverbs | 31 | 939 | 939 | 896 | 897 | 14 | 153 | 0 | 1,421 | 0 | 62 |
| Wisdom | Ecclesiastes | 12 | 222 | 222 | 222 | 222 | 15 | 53 | 0 | 404 | 44 | 24 |
| Wisdom | Song of Songs | 8 | 117 | 117 | 116 | 117 | 15 | 43 | 14 | 218 | 0 | 16 |
| Wisdom | Lamentations | 5 | 150 | 150 | 150 | 150 | 15 | 27 | 0 | 271 | 17 | 10 |
| Wisdom | Wisdom of Solomon | 19 | 435 | 0 | 441 | 435 | 32 | 103 | 0 | 909 | 57 | 38 |
| Wisdom | Sirach | 51 | 1,366 | 0 | 1,366 | 1,366 | 45 | 249 | 0 | 2,635 | 0 | 102 |
| Glory | Revelation | 22 | 405 | 0 | 405 | 405 | 39 | 0 | 0 | 0 | 96 | 0 |
| | **Total** | **575** | **15,775** | **9,816** | **15,714** | **15,754** | **741** | **3,400** | **571** | **26,592** | **1,594** | **1,014** |

Word studies: Revelation has none in the Word Notes plugin. Ratings: 9,784 Hebrew–Greek, 15,666 Latin–Greek and 10,014 KJV–Greek verse ratings; the Pentateuch KJV cards are still "assessment open" (shown as such). 11 verses have no rating because only the Saints column has text (Exodus 38:10, 38:11, 38:24, 39:21; Psalm 151:1–7).

Per-chapter counts: `coverage.csv`.

## Where things are

- Saints Parallel Reader **1.5.0** (`modules/verse-workspace`): all 575 chapters; data routes `/wp-json/saints-workspace/v1/data/<book>-<ch>` and `…-sources`; cross-references `/wp-json/saints-workspace/v1/references/<book>-<ch>`. Backup of 1.4.0 kept locally.
- Data: 1,150 private `saints_ws_chapter` records on staging (575 chapter records and 575 source records), each checked byte-for-byte against `data/manifest.json`.
- Helper: Saints Pentateuch Work **1.12.1** (jobs `wsdata`, `wslist`, `wsrefs`, `wscheck`).
- Checks run: all 1,150 records match; data and references routes return 200 with valid JSON (404 for a missing chapter); a Parallel Reader request enqueues the panel for Genesis 1, Psalm 151 and John 21 and not for Revelation 23; the panel was run in a browser on ten chapters across every source template, every tab, with no script errors.

## Still to do

- Write the prose (overall message, Unseen Change summary, instructions, lexicon links), division by division, starting with Law.
- Pentateuch KJV assessments (open) and reception ratings remain as on the source pages.
