# Corrections of 2 November 2026: the four Gospels (Latin column)

All changes were made on the **staging** site only; production has not been touched. The four Vulgate comparison pages as they were before are in [staging-backups/2026-11-02-gospels](../../staging-backups/2026-11-02-gospels/).

| File | What it is |
| --- | --- |
| `vulgate-<book>.json.gz` (4 files) | The new content of each Vulgate comparison page (Matthew 20755, Mark 20756, Luke 20757, John 20758), applied only if the page still had the md5 it had before ([manifest.json](manifest.json)). |
| [english-corrections.json](english-corrections.json) | The 84 Latin–English readings corrected against the Clementine Latin: old and new English and the reason for each. |
| [vulgate-classifications.json](vulgate-classifications.json) | The 3,672 classifications of the cards that were "Review pending": category, layer-1 comparison note, layer-5 note. |
| [review-brief.md](review-brief.md) | The rules the review followed: correct only where the English departs from the Latin's meaning, never import wording from the Greek or the KJV, and the site's own category definitions. |

## What changed on each card

- **English:** 84 readings corrected (Matthew 22, Mark 9, Luke 25, John 28), with the highlighted comparison regenerated. About 28 of these are typographical ("an donkey", "to-next day", stray commas and stops); the rest restore a word or clause the English had dropped, remove one the Latin does not have, fix number, person, tense or speaker, or move a clause to the verse where this Latin has it (for example Matthew 27:22–23, Mark 6:27–28, John 5:18–19, John 14:12–13).
- **Source label:** "Modernized English scaffold · individual Latin review pending" and "Direct Latin rendering · specialist review pending" became "… checked (or corrected) against the Clementine Latin (2 Nov 2026); specialist sign-off pending".
- **Classification:** each "Review pending" card got its category on the badge and in section 4, a comparison note in section 1 (the wording cues are kept) and a note in section 5 on what kind of difference it is.
- **Latin text:** the four glued initials (Matthew 11:12, 27:45; Mark 13:28; John 9:32) and Matthew 25:42 "desistis" → "dedistis".
- **Page header:** the tally line and the Latin review status now report the completed classification and review.

## Checks

- An independent second reading checked all 93 proposed corrections against the Latin: 84 correct, 9 unnecessary (reverted before publishing), none wrong.
- Every page was read back after saving and matched the expected md5; card count and order are unchanged.
- The Parallel Reader shows the corrected English, and the highlight colours of all 84 corrected readings were carried over (Gospels: every Latin, KJV and Saints reading coloured).
- The Latin, KJV and Saints columns were already aligned row by row in the Gospels; the remaining rows without a Saints verse (Mark 7:16, 9:44, 9:46, 11:26, 15:28) are verses the Greek critical text omits.
