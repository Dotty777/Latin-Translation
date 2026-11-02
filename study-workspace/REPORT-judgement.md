# Study Workspace — sources for the Judgement division

Staging site only (248834710), 2 November 2026. Production was not touched.

## What was found

None of the Judgement books had a Study panel in the Parallel Reader: the reader's workspace module only listed the Law, Salvation, Wisdom and Glory books.

## What was done (sources now, prose later)

Same approach as the other four divisions (see `REPORT.md`):

1. **Every Judgement chapter now has a working Study panel**: 322 chapters, 9,681 verse rows, in all 15 books (Joshua, Judges, Ruth, 1–2 Samuel, 1–2 Kings, 1–2 Chronicles, 1–2 Maccabees, Ezra, Nehemiah, Esther, Job).
2. **Every available site source is in the panel**: Hebrew–Greek, Latin–Greek and KJV–Greek comparisons (every layer, with ratings and links), Saints Translation notes, Study Edition notes, Disparate Study passages, chapter notes, Word Notes word studies, section headings, and live cross-references.
3. Tabs with no written prose say so, exactly as in the other divisions.

Sources checked and left out: the *textual and reception notes* pages for 2 Samuel and 1 Kings repeat what the comparison pages already carry, so they were not added twice.

## Counts (source studies by verse)

| Book | Chapters | Verses | Hebrew–Greek | Latin–Greek | KJV–Greek | Saints notes | Study Edition | Disparate Study | Word studies | Headings | Chapter notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Joshua | 24 | 659 | 659 | 659 | 649 | 3 | 118 | 19 | 878 | 113 | 48 |
| Judges | 21 | 618 | 618 | 618 | 618 | 18 | 88 | 22 | 958 | 107 | 42 |
| Ruth | 4 | 85 | 85 | 85 | 85 | 5 | 18 | 2 | 134 | 18 | 8 |
| 1 Samuel | 31 | 773 | 773 | 773 | 772 | 0 | 114 | 26 | 1,374 | 128 | 62 |
| 2 Samuel | 24 | 696 | 696 | 695 | 695 | 0 | 82 | 23 | 1,156 | 112 | 48 |
| 1 Kings | 22 | 883 | 826 | 850 | 756 | 0 | 80 | 44 | 1,111 | 133 | 44 |
| 2 Kings | 25 | 723 | 723 | 719 | 719 | 0 | 87 | 18 | 1,133 | 126 | 50 |
| 1 Chronicles | 29 | 930 | 930 | 930 | 930 | 0 | 109 | 36 | 1,617 | 160 | 58 |
| 2 Chronicles | 36 | 833 | 821 | 833 | 821 | 0 | 121 | 23 | 1,479 | 168 | 72 |
| 1 Maccabees | 16 | 924 | 0 | 924 | 924 | 0 | 64 | 0 | 1,569 | 126 | 32 |
| 2 Maccabees | 15 | 555 | 0 | 555 | 555 | 0 | 60 | 0 | 1,101 | 93 | 30 |
| Ezra | 10 | 280 | 280 | 280 | 280 | 10 | 39 | 21 | 458 | 40 | 20 |
| Nehemiah | 13 | 392 | 392 | 392 | 392 | 10 | 47 | 37 | 773 | 82 | 26 |
| Esther | 10 | 247 | 230 | 247 | 165 | 10 | 33 | 39 | 277 | 53 | 20 |
| Job | 42 | 1,083 | 1,083 | 1,083 | 1,069 | 10 | 144 | 54 | 2,079 | 56 | 84 |
| **Total** | **322** | **9,681** | **8,116** | **9,643** | **9,430** | **66** | **1,204** | **364** | **16,097** | **1,515** | **644** |

1 Kings has more verse rows than Hebrew–Greek studies because of its lettered Greek additions (e.g. 2:35a–o, 2:46a–l); Esther's Greek additions likewise have Latin studies but fewer Hebrew or KJV ones. 1–2 Maccabees have no Hebrew text, so no Hebrew–Greek studies.

**Ratings.** 8,115 Hebrew–Greek verse ratings are set. The Latin–Greek studies are mostly marked *Text: assessment open* on the site (1,583 rated) and the KJV–Greek studies mostly *KJV review pending* (48 rated); the panel shows them as open rather than inventing a rating. 70 verses have no rating at all (58 in 1 Kings, mostly lettered additions; 12 in 2 Chronicles).

**Cross-references.** Built live from the evidence and reviews. All Judgement books have reviewed references except **Job**, whose references all appear under *Not yet reviewed* (e.g. Job 19: 243 references, none reviewed yet).

Per-chapter counts: `coverage-judgement.csv`.

## Where things are

- Saints Parallel Reader **1.6.0** on staging: adds the Judgement books (897 chapters across five divisions).
- Data: 644 private `saints_ws_chapter` records (322 chapter + 322 source records); staging now holds 1,794 records in all, and every Judgement record matches `data/judgement/manifest.json` byte for byte.
- Helper: Saints Pentateuch Work **1.13.0**.
- Checks run: data routes return 200 with valid JSON (Joshua 2, Job 3 sources, 2 Maccabees 15, Esther 10 sources) and 404 for Job 43; a Parallel Reader request enqueues the panel for Joshua 2, Job 42 and 1 Kings 2 and not for Ruth 5; cross-references build for one chapter of each of the 15 books; the panel ran in a browser on Joshua 2, 1 Kings 2, Esther 1, Job 3 and 1 Maccabees 1 with no script errors.

## Still to do

- Write the study prose (Overall Message, Unseen Change summary, Instructions, lexicon) for all 322 chapters.
- Latin and KJV assessments that are still open on the site, and the Job cross-reference reviews; these will show up in the panel as soon as they are done.
- Production: nothing has been copied there.
