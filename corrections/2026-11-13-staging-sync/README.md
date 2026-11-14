# Staging synchronization of the 9 November Latin–English revision · 13–14 November 2026

The [9 November editorial revision](../2026-11-09-latin-editorial/README.md) (595 rows) had been committed to GitHub but not published to the Saints.Bible staging site. This records its publication.

## Result

**593 of the 595 revised readings now match GitHub on staging** (583 word for word; 10 on grouped cards, where the card’s verse rows together give the GitHub reading). Every reading was checked on the staging pages after the last save. Two remain ([remaining.json](remaining.json)):

- **Numbers 15:11** and **Deuteronomy 6:11** are grouped Latin restorations. The GitHub reading includes Latin and English (Numbers 15:2a “Speak to the children of Israel and say to them”, Deuteronomy 6:13) that the staging card has no row for. Publishing them means adding a row to the card, not editing text.

## What was applied

1. **The prepared staging files** on branch `staging/2026-11-09` (`apply-latin-01…07.json.gz`, 65 pages, 978 edits), 14 November 00:01–00:14 UTC. Every page’s fingerprint matched what the files were built from, and every saved page was read back and matched exactly. Checking each reading afterwards showed that these files did not match the GitHub revision: they carried the audit’s proposed English for 157 readings, before the editorial pass settled the final wording, and left out 120 readings (the 109 spoken-English revisions, 7 verse-alignment fixes and 3 transcription checks).
2. **Reconciliation to the GitHub wording**, 14 November, across every page layout involved:
   - Law, History, Job and Wisdom comparison cards (33 readings), including the three variants of their comparison panel markup.
   - New Testament comparison cards (Gospels, Acts, letters): the reading, the English word comparison, the generated “Wording cues” sentence, and the status line under the Latin reading (now “corrected against the Clementine Latin (9 Nov 2026); specialist sign-off pending”, as in the earlier files). Where a summary sentence named the old English pair (“mote/splinter is English wording”), it was updated from the new comparison, or reworded to “the difference is English wording” for Matthew 7:2, 7:9 and 7:10.
   - Prophets, Psalms, and the 1–2 Maccabees and Sirach comparison editions, including the Maccabees/Sirach summary sentence (“Latin–English has … Greek–English has …”).
   - Numbers 5:23, a grouped card: “very bitter water” in the two rows that carry it.

   The word comparisons were recalculated with each card’s own highlighting rule where the existing highlights could be reproduced exactly from the old text; on about 100 cards (most of the Prophets and Psalms and some New Testament cards) the original tie-breaking could not be reproduced, and the standard rule for that page was used. Thirty-four pages were saved in this step and each was read back and verified.

Written verse notes were otherwise left as they are. Most describe the Latin wording itself and remain accurate; some summary notes on the New Testament cards still paraphrase the older English loosely and are worth a read during the specialist review.

Every page was backed up in the publishing browser’s IndexedDB (`saints-apply-backups-20261113`) before saving.
