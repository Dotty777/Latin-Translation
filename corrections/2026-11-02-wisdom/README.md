# Corrections of 2 November 2026: the Wisdom Division (Latin column)

Psalms, Proverbs, Ecclesiastes, Song of Songs and Lamentations. All changes were made on the **staging** site only; production has not been touched. The five Vulgate comparison pages as they were before are in [staging-backups/2026-11-02-wisdom](../../staging-backups/2026-11-02-wisdom/).

| File | What it is |
| --- | --- |
| `vulgate-<book>.json.gz` (5 files) | The new content of each Vulgate comparison page (Psalms 20713, Proverbs 20715, Ecclesiastes 20717, Song of Songs 20719, Lamentations 20721), applied only if the page still had the md5 it had before ([manifest.json](manifest.json)). |
| [english-corrections.json](english-corrections.json) | The 29 Latin–English readings corrected against the Clementine Latin: old and new English and the reason for each. |
| [vulgate-classifications.json](vulgate-classifications.json) | The 3,805 classifications of the cards that were "Review pending": category, layer-1 comparison note, layer-5 note. |
| [corrections-second-reading.json](corrections-second-reading.json) | An independent second reading of the 32 proposed corrections. |
| [review-brief.md](review-brief.md) | The rules the review followed. |

## Result by book

| Book | Cards read against the Latin | English corrected | Newly classified | Classification of every card now |
| --- | --- | --- | --- | --- |
| Psalms | 2,495 | 25 | 2,389 | Same: 1,659 · Similar: 693 · Different: 100 · Divergent: 49 · Disparate: 1 |
| Proverbs | 915 | 3 | 949 | Same: 80 · Similar: 353 · Different: 322 · Divergent: 135 · Disparate: 68 |
| Ecclesiastes | 222 | 0 | 214 | Same: 39 · Similar: 135 · Different: 37 · Divergent: 6 · Disparate: 5 |
| Song of Songs | 115 | 1 | 105 | Same: 22 · Similar: 51 · Different: 32 · Divergent: 9 · Disparate: 2 |
| Lamentations | 154 | 0 | 148 | Same: 44 · Similar: 48 · Different: 50 · Divergent: 8 · Disparate: 4 |

The Gallican Psalter was translated from the Greek, so the Psalms are mostly Same or Similar; Jerome translated the other four books from the Hebrew, so they show many more real differences from the Septuagint (Proverbs above all, where the Greek has many lines the Latin lacks and orders chapters 24–31 differently). The 66 cards with a unit on one side only are all Divergent, with the note naming where the other text has the material when it has it elsewhere.

## What changed on each card

- **English (29 readings):** Psalms 25, Proverbs 3, Song of Songs 1. Most restore the Latin's mood or tense where the English had turned a statement into a wish or command (Psalm 7:10, 18:15, 105:48; Song 5:17), or give the Latin's word where the English had followed the Hebrew (Psalm 7:1 "Chusi", 34:25, 43:5 "salutes"; Proverbs 2:17 "guide of her youth", 10:4 and 12:24 "the hand of the strong"). Others fix a mistranslated word (Psalm 106:11 "irritaverunt" = provoked; 142:12, 144:20, 145:9 "disperdo" = destroy utterly) or remove words the Latin does not have (Psalm 58:8 "they say", 58:12 "triumph"). The highlighted comparison was regenerated for each.
- **Source line:** "English: the project's 28 September Wisdom Division volume" now adds "checked (or corrected) against the Clementine Latin, 2 November 2026" on every card that has Latin.
- **Classification:** each "Review pending" card got its category on the badge and in section 4, a comparison note in section 1 and a note in section 5 on what kind of difference it is; the closing line "Text review pending" became "Focused working assessment", as on the cards classified earlier.
- **Page header:** the status sentence now reports the completed classification and Latin review with the tally. Reception review (section 4's second half) is unchanged and still pending.
- **Lamentations letter names** ("Aleph." etc.) were left in the English: the Clementine Latin carries them too (shown as `<Aleph>` on the card).

## Checks

- An independent second reading checked all 32 proposed corrections against the Latin: 29 correct, 3 unnecessary (Psalm 44:5, 79:16, Ecclesiastes 2:24; reverted before publishing), none wrong. Psalm 58:12 was given the reader's suggested wording "over my enemies".
- A blind re-classification of 80 randomly chosen Latin cards (and 100 KJV cards) by a separate reader matched the review's category exactly in 82% of the 180 cards and within one step in 97%; the six two-step differences are judgement calls about verse division and how strong a difference is.
- Every page was read back after saving and matched the expected md5; card counts and order are unchanged.
- The Parallel Reader shows the corrected English for all 29 readings, and their highlight colours were carried over (Psalms 2,527 and Proverbs 896 Latin readings coloured; Song of Songs 114 of 116, the two uncoloured readings 7:1–7:2 were already uncoloured before this work).
