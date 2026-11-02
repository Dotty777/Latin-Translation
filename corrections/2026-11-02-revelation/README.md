# Corrections of 2 November 2026: Revelation (Latin column and KJV comparison)

All changes were made on the **staging** site only; production has not been touched. Both pages as they were before are in [staging-backups/2026-11-02-revelation](../../staging-backups/2026-11-02-revelation/).

| File | What it is |
| --- | --- |
| `vulgate-revelation.json.gz` | The new content of the Vulgate comparison page (20781), applied only if the page still had the md5 it had before ([manifest.json](manifest.json)). |
| `kjv-revelation.json.gz` | The new content of the KJV comparison edition (3847), applied the same way. |
| [english-corrections.json](english-corrections.json) | The 11 Latin–English readings corrected against the Clementine Latin, with the reason for each. |
| [vulgate-classifications.json](vulgate-classifications.json) | All 405 Latin–Greek classifications: previous and new category, note, cause, and whether the note was rewritten. |
| [kjv-classifications.json](kjv-classifications.json) | All 405 KJV ↔ Greek-English classifications, the same way. |
| [corrections-second-reading.json](corrections-second-reading.json) | An independent second reading of the 12 proposed corrections. |
| [blind-sample-check.json](blind-sample-check.json) | A separate reader's blind classification of 100 random cards, beside the new and the previous category. |
| [review-brief.md](review-brief.md) | The rules the review followed. |

## Why

Both Revelation pages were fully classified, but as a first pass: 284 of the 405 Latin cards and 328 of the 405 KJV cards carried a boilerplate note ("The corresponding statement or image is retained with modest changes…"; "Selected English contrasts…") and a category assigned without a verse-specific reading. 281 Latin and 339 KJV cards were "Similar". All 405 Latin–English renderings still said "Direct Latin rendering · specialist review pending".

## What changed

- **Latin English (11 readings):** most had followed the Greek or the KJV instead of this Latin: 2:28 and 11:3 dropped an "authority" the Latin lacks; 4:4 "seats" (sedilia), 4:5 no "of fire", 6:4 "red" (rufus), 7:17 "rule" (reget), 10:6 "time will be no more" (tempus non erit amplius), 14:6 "who sit" (sedentibus), 14:19 no added "grapes", 19:8 "white" (candido); 3:16 "I will begin to vomit" (incipiam). A second reader confirmed 11 and judged one (10:11) unnecessary; it was withdrawn. Every card now says "checked" or "corrected against the Clementine Latin (2 Nov 2026); specialist sign-off pending".
- **Latin classifications:** every card read again; 201 categories changed, 331 notes rewritten. Now Same: 166 · Similar: 151 · Different: 44 · Divergent: 41 · Disparate: 3.
- **KJV classifications:** every card read again; 232 categories changed, 353 notes rewritten. Now Same: 183 · Different: 40 · Divergent: 41 · Similar: 138 · Disparate: 3. The Textus Receptus readings are now named as such (5:14 "him that liveth for ever and ever", 16:5, 20:14, 22:13 and others are Divergent; 22:19 "book of life" is Different). The per-card line "Text rating: provisional English comparison" now says the rating is a verse-by-verse comparison.
- **Reader rows (20:7–10):** the Latin cards for 20:7–10 pair Vulgate verses with parts of Greek verses, and the reader had shown them on invented rows 20:9a, 20:9b, 20:10a and 20:10b (repeating the same English on two of them) while rows 20:9 and 20:10 had no Latin. Each card now names the Saints row it belongs on, so 20:9 and 20:10 show their Latin and nothing is repeated. Row 20:8 is covered by the Latin 20:7 card.
- **Headers:** the "first-pass" status and the tally were updated on the Vulgate page; the KJV chapter headers now say every text rating was read verse by verse.

## Checks

- Both pages were read back after saving and matched the expected md5.
- A blind classification of 100 random cards (50 Latin, 50 KJV) by a separate reader agreed with the new category exactly in 80% and within one step in 97%; it agreed with the previous first-pass category in only 32%.
- Every Latin, KJV and Saints reading of Revelation in the Parallel Reader is coloured (1,215 of 1,215); the colours of the 11 corrected readings were carried over.
