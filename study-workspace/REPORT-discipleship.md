# Study Workspace — sources for the Discipleship division

Staging site only (248834710), 2 November 2026. Production was not touched.

## What was found

None of the Discipleship books (Acts to Jude) had a Study panel in the Parallel Reader. The Epistle of Barnabas page now points to the Scholarly Companion and is outside the seventy-book Bible, so it is not included.

## What was done (sources now, prose later)

Same approach as the other divisions:

1. **Every Discipleship chapter now has a working Study panel**: 149 chapters, 3,774 verse rows, in all 22 books.
2. **Every available site source is in the panel**: the Latin–Greek (Vulgate) and King James–Greek comparisons with all five layers (word comparison, Catholic / Protestant explanation, medieval Christian reception, combined classification, how the difference arose), with ratings and links; the Saints Translation notes; chapter notes; section headings; and live cross-references.
3. **New source: patristic reception.** 2 Corinthians has a verse-by-verse reception page drawn from St John Chrysostom's homilies. Its 256 entries now appear in the panel as *Patristic reception*, each with its homily link. The builder handles such pages generally; this is the only one on the site so far. Rebuilds of Judgement and Providence books come out byte-identical to what is stored.

The site has no Hebrew–Greek comparison, Study Edition or Disparate Study pages for these books, and no word studies: the Word Notes files for Acts–Jude hold only wording-difference highlights. Those tabs say so in the panel.

## Counts (source studies by verse)

| Book | Chapters | Verses | Latin–Greek | KJV–Greek | Saints notes | Patristic reception | Headings | Chapter notes |
|---|---|---|---|---|---|---|---|---|
| Acts | 28 | 1,007 | 1,004 | 1,007 | 66 | 0 | 163 | 28 |
| Romans | 16 | 433 | 433 | 433 | 52 | 0 | 73 | 16 |
| 1 Corinthians | 16 | 437 | 437 | 437 | 71 | 0 | 73 | 16 |
| 2 Corinthians | 13 | 256 | 255 | 256 | 20 | 256 | 38 | 13 |
| Galatians | 6 | 149 | 149 | 149 | 23 | 0 | 24 | 6 |
| Ephesians | 6 | 155 | 155 | 155 | 13 | 0 | 23 | 6 |
| Philippians | 4 | 104 | 104 | 104 | 9 | 0 | 19 | 4 |
| Colossians | 4 | 95 | 95 | 95 | 17 | 0 | 19 | 4 |
| 1 Thessalonians | 5 | 89 | 89 | 89 | 15 | 0 | 16 | 5 |
| 2 Thessalonians | 3 | 47 | 47 | 47 | 11 | 0 | 9 | 3 |
| 1 Timothy | 6 | 113 | 113 | 113 | 17 | 0 | 23 | 6 |
| 2 Timothy | 4 | 83 | 83 | 83 | 15 | 0 | 15 | 4 |
| Titus | 3 | 46 | 46 | 46 | 12 | 0 | 8 | 3 |
| Philemon | 1 | 25 | 25 | 25 | 12 | 0 | 5 | 1 |
| Hebrews | 13 | 303 | 303 | 303 | 43 | 0 | 48 | 13 |
| James | 5 | 108 | 108 | 108 | 23 | 0 | 19 | 5 |
| 1 Peter | 5 | 105 | 105 | 105 | 17 | 0 | 20 | 5 |
| 2 Peter | 3 | 61 | 61 | 61 | 16 | 0 | 11 | 3 |
| 1 John | 5 | 105 | 105 | 105 | 43 | 0 | 19 | 5 |
| 2 John | 1 | 13 | 13 | 13 | 12 | 0 | 4 | 1 |
| 3 John | 1 | 15 | 14 | 15 | 11 | 0 | 4 | 1 |
| Jude | 1 | 25 | 25 | 25 | 12 | 0 | 6 | 1 |
| **Total** | **149** | **3,774** | **3,769** | **3,774** | **530** | **256** | **639** | **149** |

**Ratings.** The King James–Greek studies are rated for every verse but one (3,773). The Latin–Greek studies are mostly marked *Review pending* on the site (182 rated), shown as open in the panel. One verse has no rating at all (1 John 4:8, both comparisons still open). Seven rows have no Latin study because the Latin column is empty there (Acts 7:56, 9:7, 13:31, 14:7, 19:40b; 2 Corinthians 1:24; 3 John 1:15).

**Cross-references.** Built live; checked for one chapter of every book (e.g. Acts 2: 854 references; Romans 8: 836). Almost all are reviewed; a few per chapter appear under *Not yet reviewed*.

Per-chapter counts: `coverage-discipleship.csv`.

## Where things are

- Saints Parallel Reader **1.8.0** on staging: all seven divisions (1,291 chapters). The installed files were read back and match the build exactly.
- Data: 298 private `saints_ws_chapter` records (149 chapter + 149 source records); staging now holds 2,582 records, and every Discipleship, Providence and Judgement record matches its manifest byte for byte.
- Helper: Saints Pentateuch Work **1.15.0** (reads the Discipleship books).
- Checks run: data routes return 200 (Acts 2, Romans 8 sources, 2 Corinthians 5 sources, Hebrews 11, Jude 1, and Genesis 1 from the first division) and 404 for Jude 2; a Parallel Reader request enqueues the panel for Acts 2, 3 John 1 and Genesis 1 and not for Hebrews 14; cross-references build for one chapter of every book; the panel ran in a browser on Acts 2, Romans 8, 2 Corinthians 5, Hebrews 11, 3 John 1 and Jude 1 through every tab with no script errors, including the new Chrysostom entries.

## Still to do

- Write the study prose for all 149 chapters.
- Latin assessments still open on the site; they appear in the panel when done.
- Production: nothing has been copied there.
