# Staging synchronization of the 9 November Latin–English revision · 13–14 November 2026

The [9 November editorial revision](../2026-11-09-latin-editorial/README.md) (595 rows) had been committed to GitHub but not published to the Saints.Bible staging site. This records its publication and what still differs.

## What was applied

1. **The prepared staging files** on branch `staging/2026-11-09` (`corrections/2026-11-09-staging/apply-latin-01…07.json.gz`, 65 pages, 978 edits). Every page’s fingerprint matched what the files were built from, every edit applied, and every saved page was read back and matched the expected result exactly (14 November, 00:01–00:14 UTC).
2. **Reconciliation on the Vulgate comparison pages for Genesis–Job and Wisdom** (14 November): 33 cards where staging now showed draft wording were brought to the GitHub reading, in both the reading and the English word comparison, which was recalculated with the page’s own matching rule. Thirteen pages were saved and verified. Genesis 17:14 already shows the later [13 November reading](../2026-11-13-genesis-reading-pass/README.md).

## Result

Of the 595 revised readings, **318 now match GitHub on staging** and **277 do not yet** ([remaining.json](remaining.json), with the GitHub reading for each):

- **157 show draft wording.** The 9 November staging files were built from the audit’s proposed English, before the editorial pass adjudicated it. They are improvements on the previous text, but not the final wording.
- **120 still show the earlier wording.** The staging files left out the 109 spoken-English revisions, 7 verse-alignment fixes and 3 transcription checks (Matthew 7, Romans 5 and 12, James 1 and 3, Acts 17 and others).
- 12 of the 277 are grouped cards in Numbers and Deuteronomy that hold several Latin verses; the right row must be matched before editing.

The remaining readings are on page layouts not yet handled by the publishing script: the New Testament comparison cards, which also carry generated “wording cue” sentences that quote the English; the prophets’ `vl-` cards; Psalms units; and the 1–2 Maccabees and Sirach comparison editions. They need a layout-aware pass, including regeneration of those wording cues.

Every page was backed up in the publishing browser’s IndexedDB (`saints-apply-backups-20261113`) before saving.
