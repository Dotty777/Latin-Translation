# Latin–English column audit — Saints.Bible

1 November 2026 (Wisdom of Solomon added later the same day). Audit of the Latin–English column of the Saints.Bible Parallel Reader (staging) for fidelity to the Clementine Latin. A living copy of this document is kept as a Claude doc; this file is the record for the repository.

## Summary

The Latin–English column is faithful to the Clementine Latin. In a close reading of 160 randomly chosen verses and about 230 verses flagged by automated checks, not one mistranslated the Latin's meaning. The Latin text itself matches the Clementine Vulgate word for word in 98.5% of 34,461 readings, and every remaining difference inspected was a label or a numbering choice, not a copying error.

The column has three real problems, none of them translation errors:

- **Three quarters of the New Testament is not a fresh rendering.** In the Gospels, Acts, and most of the Letters (6,022 of 7,956 readings), the English is the Douay-Rheims (Challoner) text, verbatim or lightly modernised, while the cards label it "Direct Latin rendering". Douay-Rheims is a faithful translation of this same Latin, so the wording is accurate, but the label is not.
- **171 readings show English for two Vulgate verses beside the Latin of one.** The site keeps the Hebrew/Greek verse numbering, and where the Vulgate divides verses differently (Esther's Greek additions, Psalms, Numbers), the English runs on past the Latin displayed. 3,469 readings carry a verse number that differs from the Vulgate's own.
- **88% of readings are still labelled "review pending" or "assessment open"** (29,975 of 34,642). Only 1–2 Maccabees, Wisdom of Solomon, Sirach, 2–3 John and Revelation are fully classified. The labels understate how good the column is.

Small fixes: 9 Latin verses have a glued first letter ("Adiebus" for "A diebus"), and Lamentations keeps the Hebrew letter names in the English but not in the Latin.

## What was checked and how

Every Latin–English reading in the staging Parallel Reader: 34,642 readings in 70 books. Wisdom of Solomon (435 readings, 439 Latin verses) was audited after the rest: the reader had no Latin column for it, although the Comparison Library already held a complete Latin–Greek edition of the book; that edition was wired into the reader on 1 November 2026 and checked the same way (see `wisdom-of-solomon/README.md`). For each, the English was taken as the reader displays it and the Latin from the linked comparison card, then the checks below were run.

**Reference texts.** The Latin was compared with the Clementine Vulgate text of the VulSearch project and the English with the Douay-Rheims Challoner translation, both from the public-domain [mborders/vulgata](https://github.com/mborders/vulgata) dataset. Douay-Rheims was made from this same Latin, so it serves as an independent rendering to compare against, not as a standard the site must copy.

**Automated checks on every reading**

| Check | What it catches |
| --- | --- |
| Latin against the Clementine reference, re-aligned by content where the site's verse numbering differs | Copying errors, dropped or added words, wrong verse |
| English against Douay-Rheims | Readings that are Douay-Rheims rather than a fresh rendering; readings whose content differs sharply from an independent rendering |
| English length against Latin length | Omissions and additions; English running past the Latin shown |
| Negations and numbers in the Latin against the English | Reversed sense, wrong figures |
| English against the Saints (Greek) column | Latin readings copied from the Greek column instead of translated |

**Manual reading.** The Latin was read against the English for 160 randomly chosen fresh renderings (90 spread across Law, History, Wisdom, Prophets and New Testament; 70 more from the harder poetic and prophetic books), plus about 230 readings the automated checks flagged, plus 30 passages where the Vulgate is known to differ from the Greek or Hebrew (Genesis 3:15, Luke 1:28, Matthew 6:11, Exodus 34:29, Romans 5:12, 1 John 5:7, Acts 8:37 and others).

**Limits.** The automated checks compare words, not meaning; the manual sample is where meaning was judged, and 160 random verses detect a problem affecting more than about 2% of readings but not a rarer one. Textual notes on the comparison pages were not assessed. Per-verse results are in `audit/per-verse-checks.csv`.

## Findings

**1. The Latin text is a sound copy of the Clementine Vulgate.** 33,507 of 34,022 readings match the reference word for word. The 224 "near" matches differ only because the site drops editorial labels the reference keeps (Hebrew letter names in Lamentations and Psalm 118, speaker labels in Song of Songs, cross-references in psalm titles). The 291 that could not be compared automatically are Maccabees and Sirach cards whose translation notes sit inside the Latin block, and a handful of verses the reference lacks; those inspected by hand were correct. The only copying flaw found: nine verses where the first letter is glued to the next word, inherited from a drop-cap in the source: Matthew 11:12 ("Adiebus"), Matthew 27:45 ("Asexta"), Mark 13:28 ("Aficu"), John 9:32 ("Asæculo"), Romans 9:20 ("Ohomo"), Romans 11:33 ("Oaltitudo"), Galatians 3:1 ("Oinsensati"), 1 Thessalonians 1:8 ("Avobis") and 1 Timothy 1:6 ("Aquibus") (list in `audit/glued-initials.json`).

**2. The fresh renderings follow the Latin, including where the Latin is distinctive.** Every known crux checked keeps the Vulgate reading rather than drifting toward the Greek or Hebrew column:

| Passage | Latin | Site English |
| --- | --- | --- |
| Genesis 3:15 | ipsa conteret caput tuum | she shall crush your head |
| Exodus 34:29 | cornuta esset facies sua | his face was horned |
| Matthew 6:11 | panem supersubstantialem | our supersubstantial bread |
| Luke 1:28 | gratia plena | full of grace |
| Romans 5:12 | in quo omnes peccaverunt | in whom all sinned |
| Ephesians 5:32 | sacramentum hoc magnum est | this is a great sacrament |
| 1 John 5:7 | tres sunt qui testimonium dant in cælo | three who bear witness in heaven (kept) |
| Acts 8:37 | (verse present in the Vulgate) | kept, where the Greek column has none |
| Sirach 34:10 | multiplicat malitiam | multiplies malice (with a note; Douay has "prudence") |

In the 160-verse random sample and the flagged sets, the liberties found are small and would pass any ordinary review: Numbers 29:27 renders *sacrificia* as "grain offerings" (an interpretation from the Hebrew); Genesis 4:19 and 30:11 supply the names Lamech and Leah where the Latin has only a pronoun; 2 Samuel 4:11 turns the rhetorical "shall I not require" into "shall I require … !"; Job 41:21 makes "the one brandishing the spear" into "the brandished spear". None changes what the verse says.

**3. Most of the New Testament English is Douay-Rheims, not a new rendering.**

| Books | Readings | Douay-Rheims verbatim | Douay-Rheims lightly modernised | Fresh |
| --- | --- | --- | --- | --- |
| Matthew, Mark, Luke, John, Acts | 4,780 | 1,859 | 1,954 | 953 |
| Romans to 1 Timothy, 2 Timothy, Hebrews, James, 1–2 Peter | 2,357 | 1,040 | 1,118 | 199 |
| 2 Thessalonians, Titus, Philemon, 1–3 John, Jude, Revelation | 819 | 1 | 40 | 764 |

"Lightly modernised" means the Douay sentence with *thou/thee/-eth* updated, for example Matthew 11:12 "the kingdom of heaven allows violence" for Douay's "suffereth violence". The Old Testament is the reverse: 24,843 of 26,251 readings are fresh. Douay-Rheims is a faithful rendering of this Latin, so the wording is not wrong, but the card label "Direct Latin rendering · specialist review pending" misdescribes its origin, and the column changes voice between books: archaic in Acts, modern in Revelation.

**4. In 171 readings the English runs past the Latin on the card.** The site keeps the Saints column's verse numbering. Where the Vulgate divides verses differently, the English for the Saints verse covers two or more Vulgate verses but the card shows only the first verse's Latin. Psalm 59:7 shows Latin ending at *dilecti tui* while the English continues "Save with Your right hand and hear me"; Psalm 3:7, Numbers 36:8 (English covers Numbers 36:8–13) and Esther 4:17o (one Latin line beside Esther's whole prayer) are the same. By book: Esther 84, Psalms 52, Numbers 29, six elsewhere (list in `audit/english-spans-more-than-latin.json`). A further 3,469 readings are correct but carry a verse number that is not the Vulgate's (Jeremiah, Psalms, 1 Chronicles 6, Daniel 5–6, 1 Kings 4–5, Haggai 2, Zechariah), so a reader checking against a printed Vulgate will not find "Latin verse 9:1" at 9:1.

**5. The site's own labels undersell the column.** 29,975 of 34,642 readings (87%) still say "review pending", "assessment open" or "unreviewed"; 4,508 carry a classification. Only 1–2 Maccabees, Wisdom of Solomon, Sirach, 2–3 John and Revelation are fully classified, and those books also carry translation notes, which the rest do not.

**6. Small inconsistencies.** Lamentations: 128 English readings begin with the Hebrew letter name ("Nun. They wandered…") while the Latin beside them omits it. Song of Songs drops the Vulgate's speaker labels in both languages. The Latin keeps the source's French-style spacing before colons and question marks ("gentibus : contemptibilis", "dinumeravit ?"). Wisdom of Solomon had no Latin column in the Parallel Reader, although the site already carried a complete Latin–Greek comparison edition of the book in the Comparison Library; the reader looks for a comparison page under the book page and that edition sits under the Comparison Library instead. Fixed on 1 November 2026 by reproducing the edition’s 439 cards as the book’s vulgate-comparison page, each card linking back to its full entry.

## Results by section

| Section | Readings | Latin matches Clementine | English is Douay-Rheims | Labelled "review pending" | Verse number differs from Vulgate |
| --- | --- | --- | --- | --- | --- |
| Law (Genesis–Deuteronomy) | 5,893 | 99.7% | 6% | 96% | 195 |
| History (Joshua–Esther, 1–2 Maccabees) | 8,598 | 98.3% | 3% | 81% | 715 |
| Wisdom (Job–Sirach, with Wisdom of Solomon) | 6,689 | 98.1% | 6% | 70% | 1,194 |
| Prophets (Isaiah–Malachi, Lamentations) | 5,506 | 99.9% | 5% | 98% | 1,269 |
| Gospels and Acts | 4,780 | 99.9% | 80% | 97% | 112 |
| Letters (Romans–Jude) | 2,767 | 99.9% | 79% | 94% | 45 |
| Revelation | 409 | 100% | 8% | 0% | 8 |

The History and Wisdom percentages are lowered only by the Maccabees and Sirach cards whose translation notes are embedded in the Latin block; no copying errors were found there.

## Recommendations

1. **Keep the column as a comparison text, not an official translation.** Its accuracy supports that use; its mixed origin and pending labels do not yet support more.
2. **Say where the English comes from.** On the 6,022 Douay-Rheims readings, replace "Direct Latin rendering" with "Douay-Rheims (Challoner), modernised". Then decide whether to leave Douay in place or re-render those books in the voice used for the Old Testament and Revelation.
3. **Fix the 171 split verses.** Either show the full Latin span on the card (Psalm 59:7–8, Numbers 36:8–13, Esther's prayers) or cut the English at the displayed Latin. A note on each card where the site's numbering differs from the Vulgate's (3,469 readings) would also help readers using a printed Vulgate.
4. **Correct the nine glued initials** (Matthew 11:12, 27:45; Mark 13:28; John 9:32; Romans 9:20, 11:33; Galatians 3:1; 1 Thessalonians 1:8; 1 Timothy 1:6).
5. **Make the labels match the work.** The Pentateuch and Prophets are 96–98% "review pending" yet show no error in the sample; a Latinist sign-off by book, with the label changed to "reviewed", would let the cards claim what has been checked. Start with Genesis, Psalms, Isaiah and the four Gospels.
6. **Tidy the presentation:** add the Hebrew letter names to the Lamentations Latin (or drop them from the English), and remove the space before colons and question marks. (The missing Wisdom of Solomon column has been added; the Comparison Library edition remains the master copy, so any later edit there should be carried over to the book’s vulgate-comparison page.)

No verse was re-translated in this audit; where a reviewer wants a second opinion on a specific passage, the comparison with Douay-Rheims can be rerun for any book from `audit/per-verse-checks.csv`.
