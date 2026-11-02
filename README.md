# Latin–English column of the Saints.Bible Parallel Reader

The Clementine Vulgate Latin and the Latin–English rendering for every verse of all 70 books of the Saints Holy Bible as shown in the Latin column on Saints.Bible, captured from the staging Parallel Reader on 1 November 2026 (Genesis–Deuteronomy and the four Gospels recaptured on 2 November 2026 after corrections), with an audit of the column's fidelity to the Latin. Companion to [Saints-Translation](https://github.com/Dotty777/Saints-Translation), which records the Saints English (Greek-based) text in the same layout.

- [AUDIT.md](AUDIT.md): the fidelity and accuracy audit (verdict, method, findings, recommendations).
- `audit/`: the audit's working data — a per-verse check table, the nine glued initials, and the 171 readings whose English spans more Vulgate verses than the Latin shown.
- `corrections/`: the data files applied to the staging site, with a change log per date ([2 November 2026, Pentateuch](corrections/2026-11-02/README.md); [2 November 2026, Gospels](corrections/2026-11-02-gospels/README.md)); `staging-backups/` holds the pages as they were before.
- One folder per book: `README.md` (counts and audit results), `<Book>.txt` (Latin and English by chapter), `verses.json` (structured text with card ids, review status, English origin and Vulgate numbering).

Verse numbers follow the Saints column (Greek/Hebrew numbering); where the Vulgate numbers a verse differently, `verses.json` records the Vulgate reference.

## Books

- [Genesis — 50 chapters](genesis/README.md): 1,534 readings; Latin matches the Clementine reference in 100%; English is a fresh rendering; every card classified on the site (Latin–Greek comparison, 2 November 2026).
- [Exodus — 40 chapters](exodus/README.md): 1,216 readings; Latin matches the Clementine reference in 100%; English is a fresh rendering; every card classified on the site (Latin–Greek comparison, 2 November 2026).
- [Leviticus — 27 chapters](leviticus/README.md): 859 readings; Latin matches the Clementine reference in 100%; English is a fresh rendering; every card classified on the site (Latin–Greek comparison, 2 November 2026).
- [Numbers — 36 chapters](numbers/README.md): 1,257 readings; Latin matches the Clementine reference in 100%; English is a fresh rendering; every card classified on the site (Latin–Greek comparison, 2 November 2026).
- [Deuteronomy — 34 chapters](deuteronomy/README.md): 957 readings; Latin matches the Clementine reference in 100%; English is a fresh rendering; every card classified on the site (Latin–Greek comparison, 2 November 2026).
- [Joshua — 24 chapters](joshua/README.md): 659 readings; Latin matches the Clementine reference in 100%; English is a fresh rendering; 99% still labelled review pending on the site.
- [Judges — 21 chapters](judges/README.md): 618 readings; Latin matches the Clementine reference in 100%; English is a fresh rendering; 100% still labelled review pending on the site.
- [Ruth — 4 chapters](ruth/README.md): 85 readings; Latin matches the Clementine reference in 100%; English is a fresh rendering; 94% still labelled review pending on the site.
- [1 Samuel — 31 chapters](1-samuel/README.md): 773 readings; Latin matches the Clementine reference in 100%; English is a fresh rendering; 100% still labelled review pending on the site.
- [2 Samuel — 24 chapters](2-samuel/README.md): 696 readings; Latin matches the Clementine reference in 100%; English is a fresh rendering; 98% still labelled review pending on the site.
- [1 Kings — 22 chapters](1-kings/README.md): 883 readings; Latin matches the Clementine reference in 100%; English is a fresh rendering; 95% still labelled review pending on the site.
- [2 Kings — 25 chapters](2-kings/README.md): 723 readings; Latin matches the Clementine reference in 100%; English is a fresh rendering; 98% still labelled review pending on the site.
- [1 Chronicles — 29 chapters](1-chronicles/README.md): 930 readings; Latin matches the Clementine reference in 100%; English is a fresh rendering; 99% still labelled review pending on the site.
- [2 Chronicles — 36 chapters](2-chronicles/README.md): 833 readings; Latin matches the Clementine reference in 100%; English is a fresh rendering; 99% still labelled review pending on the site.
- [1 Maccabees — 16 chapters](1-maccabees/README.md): 924 readings; Latin matches the Clementine reference in 93%; English is a fresh rendering; 0% still labelled review pending on the site.
- [2 Maccabees — 15 chapters](2-maccabees/README.md): 555 readings; Latin matches the Clementine reference in 86%; English is a fresh rendering; 0% still labelled review pending on the site.
- [Ezra — 10 chapters](ezra/README.md): 280 readings; Latin matches the Clementine reference in 100%; English is a fresh rendering; 99% still labelled review pending on the site.
- [Nehemiah — 13 chapters](nehemiah/README.md): 392 readings; Latin matches the Clementine reference in 100%; English is a fresh rendering; 99% still labelled review pending on the site.
- [Esther — 10 chapters](esther/README.md): 247 readings; Latin matches the Clementine reference in 100%; English is a fresh rendering; 92% still labelled review pending on the site.
- [Job — 42 chapters](job/README.md): 1,083 readings; Latin matches the Clementine reference in 100%; English is a fresh rendering; 98% still labelled review pending on the site.
- [Psalms — 150 chapters](psalms/README.md): 2,527 readings; Latin matches the Clementine reference in 99%; English is a fresh rendering; 96% still labelled review pending on the site.
- [Proverbs — 31 chapters](proverbs/README.md): 939 readings; Latin matches the Clementine reference in 100%; English is a fresh rendering; 94% still labelled review pending on the site.
- [Ecclesiastes — 12 chapters](ecclesiastes/README.md): 222 readings; Latin matches the Clementine reference in 100%; English is a fresh rendering; 96% still labelled review pending on the site.
- [Song of Songs — 8 chapters](song-of-songs/README.md): 117 readings; Latin matches the Clementine reference in 100%; English is a fresh rendering; 90% still labelled review pending on the site.
- [Lamentations — 5 chapters](lamentations/README.md): 150 readings; Latin matches the Clementine reference in 100%; English is a fresh rendering; 97% still labelled review pending on the site.
- [Wisdom of Solomon — 19 chapters](wisdom-of-solomon/README.md): 435 readings (439 Latin verses); Latin matches the Clementine reference in 100%; English is the Comparison Library’s own rendering; 0% still labelled review pending on the site — column added to the Parallel Reader on 1 November 2026 from the existing Comparison Library edition.
- [Sirach — 51 chapters](sirach/README.md): 1,366 readings; Latin matches the Clementine reference in 92%; English is a fresh rendering; 0% still labelled review pending on the site.
- [Isaiah — 66 chapters](isaiah/README.md): 1,289 readings; Latin matches the Clementine reference in 100%; English is a fresh rendering; 99% still labelled review pending on the site.
- [Jeremiah — 52 chapters](jeremiah/README.md): 1,299 readings; Latin matches the Clementine reference in 100%; English is a fresh rendering; 99% still labelled review pending on the site.
- [Ezekiel — 48 chapters](ezekiel/README.md): 1,267 readings; Latin matches the Clementine reference in 100%; English is a fresh rendering; 99% still labelled review pending on the site.
- [Daniel — 12 chapters](daniel/README.md): 451 readings; Latin matches the Clementine reference in 100%; English is a fresh rendering; 96% still labelled review pending on the site.
- [Hosea — 14 chapters](hosea/README.md): 197 readings; Latin matches the Clementine reference in 100%; English is a fresh rendering; 97% still labelled review pending on the site.
- [Joel — 4 chapters](joel/README.md): 73 readings; Latin matches the Clementine reference in 100%; English is a fresh rendering; 96% still labelled review pending on the site.
- [Amos — 9 chapters](amos/README.md): 146 readings; Latin matches the Clementine reference in 100%; English is a fresh rendering; 98% still labelled review pending on the site.
- [Obadiah — 1 chapters](obadiah/README.md): 21 readings; Latin matches the Clementine reference in 100%; English is a fresh rendering; 86% still labelled review pending on the site.
- [Jonah — 4 chapters](jonah/README.md): 48 readings; Latin matches the Clementine reference in 100%; English is a fresh rendering; 92% still labelled review pending on the site.
- [Micah — 7 chapters](micah/README.md): 105 readings; Latin matches the Clementine reference in 100%; English is a fresh rendering; 96% still labelled review pending on the site.
- [Nahum — 3 chapters](nahum/README.md): 47 readings; Latin matches the Clementine reference in 100%; English is a fresh rendering; 94% still labelled review pending on the site.
- [Habakkuk — 3 chapters](habakkuk/README.md): 56 readings; Latin matches the Clementine reference in 100%; English is a fresh rendering; 95% still labelled review pending on the site.
- [Zephaniah — 3 chapters](zephaniah/README.md): 53 readings; Latin matches the Clementine reference in 98%; English is a fresh rendering; 92% still labelled review pending on the site.
- [Haggai — 2 chapters](haggai/README.md): 38 readings; Latin matches the Clementine reference in 100%; English is a fresh rendering; 92% still labelled review pending on the site.
- [Zechariah — 14 chapters](zechariah/README.md): 211 readings; Latin matches the Clementine reference in 100%; English is a fresh rendering; 96% still labelled review pending on the site.
- [Malachi — 3 chapters](malachi/README.md): 55 readings; Latin matches the Clementine reference in 100%; English is a fresh rendering; 87% still labelled review pending on the site.
- [Matthew — 28 chapters](matthew/README.md): 1,071 readings; Latin matches the Clementine reference in 100%; English is modernised Douay-Rheims with 246 fresh renderings, every reading checked against the Latin (22 corrected); every card classified on the site (2 November 2026).
- [Mark — 16 chapters](mark/README.md): 679 readings; Latin matches the Clementine reference in 100%; English is modernised Douay-Rheims with 145 fresh renderings, every reading checked against the Latin (9 corrected); every card classified on the site (2 November 2026).
- [Luke — 24 chapters](luke/README.md): 1,151 readings; Latin matches the Clementine reference in 100%; English is modernised Douay-Rheims with 218 fresh renderings, every reading checked against the Latin (25 corrected); every card classified on the site (2 November 2026).
- [John — 21 chapters](john/README.md): 879 readings; Latin matches the Clementine reference in 100%; English is modernised Douay-Rheims with 245 fresh renderings, every reading checked against the Latin (28 corrected); every card classified on the site (2 November 2026).
- [Acts — 28 chapters](acts/README.md): 1,007 readings; Latin matches the Clementine reference in 100%; English is Douay-Rheims-based in 89%; 98% still labelled review pending on the site.
- [Romans — 16 chapters](romans/README.md): 433 readings; Latin matches the Clementine reference in 100%; English is Douay-Rheims-based in 83%; 98% still labelled review pending on the site.
- [1 Corinthians — 16 chapters](1-corinthians/README.md): 437 readings; Latin matches the Clementine reference in 100%; English is Douay-Rheims-based in 85%; 97% still labelled review pending on the site.
- [2 Corinthians — 13 chapters](2-corinthians/README.md): 256 readings; Latin matches the Clementine reference in 100%; English is Douay-Rheims-based in 93%; 98% still labelled review pending on the site.
- [Galatians — 6 chapters](galatians/README.md): 149 readings; Latin matches the Clementine reference in 100%; English is Douay-Rheims-based in 91%; 95% still labelled review pending on the site.
- [Ephesians — 6 chapters](ephesians/README.md): 155 readings; Latin matches the Clementine reference in 100%; English is Douay-Rheims-based in 87%; 95% still labelled review pending on the site.
- [Philippians — 4 chapters](philippians/README.md): 104 readings; Latin matches the Clementine reference in 100%; English is Douay-Rheims-based in 91%; 96% still labelled review pending on the site.
- [Colossians — 4 chapters](colossians/README.md): 95 readings; Latin matches the Clementine reference in 100%; English is Douay-Rheims-based in 86%; 97% still labelled review pending on the site.
- [1 Thessalonians — 5 chapters](1-thessalonians/README.md): 89 readings; Latin matches the Clementine reference in 99%; English is Douay-Rheims-based in 76%; 90% still labelled review pending on the site.
- [2 Thessalonians — 3 chapters](2-thessalonians/README.md): 47 readings; Latin matches the Clementine reference in 100%; English is a fresh rendering; 87% still labelled review pending on the site.
- [1 Timothy — 6 chapters](1-timothy/README.md): 113 readings; Latin matches the Clementine reference in 99%; English is Douay-Rheims-based in 82%; 92% still labelled review pending on the site.
- [2 Timothy — 4 chapters](2-timothy/README.md): 83 readings; Latin matches the Clementine reference in 100%; English is Douay-Rheims-based in 86%; 95% still labelled review pending on the site.
- [Titus — 3 chapters](titus/README.md): 46 readings; Latin matches the Clementine reference in 98%; English is a fresh rendering; 80% still labelled review pending on the site.
- [Philemon — 1 chapters](philemon/README.md): 25 readings; Latin matches the Clementine reference in 100%; English is a fresh rendering; 64% still labelled review pending on the site.
- [Hebrews — 13 chapters](hebrews/README.md): 303 readings; Latin matches the Clementine reference in 100%; English is Douay-Rheims-based in 87%; 97% still labelled review pending on the site.
- [James — 5 chapters](james/README.md): 108 readings; Latin matches the Clementine reference in 100%; English is Douay-Rheims-based in 79%; 96% still labelled review pending on the site.
- [1 Peter — 5 chapters](1-peter/README.md): 105 readings; Latin matches the Clementine reference in 100%; English is Douay-Rheims-based in 85%; 98% still labelled review pending on the site.
- [2 Peter — 3 chapters](2-peter/README.md): 61 readings; Latin matches the Clementine reference in 100%; English is Douay-Rheims-based in 90%; 95% still labelled review pending on the site.
- [1 John — 5 chapters](1-john/README.md): 105 readings; Latin matches the Clementine reference in 100%; English is a fresh rendering; 82% still labelled review pending on the site.
- [2 John — 1 chapters](2-john/README.md): 13 readings; Latin matches the Clementine reference in 100%; English is a fresh rendering; 0% still labelled review pending on the site.
- [3 John — 1 chapters](3-john/README.md): 15 readings; Latin matches the Clementine reference in 100%; English is a fresh rendering; 0% still labelled review pending on the site.
- [Jude — 1 chapters](jude/README.md): 25 readings; Latin matches the Clementine reference in 100%; English is a fresh rendering; 72% still labelled review pending on the site.
- [Revelation — 22 chapters](revelation/README.md): 409 readings; Latin matches the Clementine reference in 100%; English is a fresh rendering; 0% still labelled review pending on the site.

Wisdom of Solomon: the Parallel Reader had no Latin column for this book until 1 November 2026, although the Comparison Library already held a complete Latin–Greek edition of it; that edition was reproduced as the book’s vulgate-comparison page the same day and is captured in [wisdom-of-solomon/](wisdom-of-solomon/README.md).

Source of the reference texts used in the audit: [mborders/vulgata](https://github.com/mborders/vulgata) (Clementine Vulgate from VulSearch; Douay-Rheims Challoner), public domain.
