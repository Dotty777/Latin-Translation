# Full Latin–English review of all 70 books · 9 November 2026

Every Latin–English reading in this repository was read from scratch against the Clementine Latin recorded beside it: 34,254 distinct readings across the 70 books (34,429 reader rows carry Latin; 175 of those repeat a grouped card, and 146 rows have no Latin). The review worked from the GitHub record only. **Nothing was changed on the staging site or in the book folders;** everything here is a proposal or a note for decision.

## Result

The column holds up. 481 readings (1.4%) have a proposed English correction that survived a second reading, and 24 of those change what the verse says. The larger issue is coverage, not translation: 687 Clementine verses have no Latin anywhere in the record.

| Outcome | Count | File |
| --- | ---: | --- |
| Proposed English corrections, confirmed or amended on second reading | 481 (24 major, 457 minor) | [proposed-english-corrections.json](proposed-english-corrections.json) |
| First-reading proposals withdrawn on second reading | 36 | [withdrawn-on-second-reading.json](withdrawn-on-second-reading.json) |
| English has words the recorded Latin lacks; needs a printed Clementine | 3 | [source-check-needed.json](source-check-needed.json) |
| English and Latin on a card cover different amounts of text | 61 | [english-latin-span-findings.json](english-latin-span-findings.json) |
| Reader notes on the recorded Latin | 295 | [latin-text-notes.json](latin-text-notes.json) |
| Clementine verses with no Latin in the record | 687 | [vulgate-verses-not-in-record.json](vulgate-verses-not-in-record.json) |

Per-book pages are in [books/](books/); counts per book are in [coverage.csv](coverage.csv) and the table at the end.

## The 24 major corrections

These change a name, a person, a number of items in a list, or what the verse asserts:

- **Wrong or Hebrew-form name against the Latin:** 1 Chronicles 4:11 (Chelub for *Caleb*), 2 Chronicles 31:13 (Azaziah for *Azarias*), Nehemiah 3:20 (Zabbai for *Zachai*), Nehemiah 8:4 (Shema for *Semeia*), Acts 9:11 (the street called "Narrow" for *Rectus*, Straight).
- **Word dropped, person changed or sense garbled:** 2 Timothy 2:22 (*spem*, hope, missing from the list), Romans 6:18 ("we" for *estis*, you), 1 Corinthians 7:7 ("all men" for *omnes vos*), Numbers 3:38 ("Aaron's sons" for *filiis suis*), Acts 3:16 ("this man … has his name strengthened" for *hunc … confirmavit nomen ejus*).
- **English follows the Hebrew or Greek against this Latin:** Exodus 33:16, Leviticus 7:35, Numbers 10:13, 1 Chronicles 15:13, 1 Maccabees 1:13 and 9:13, Job 16:3, Wisdom 1:14, Nahum 3:11, Zechariah 7:2 and 14:10, Acts 2:23, 3 John 1:4.
- **Editorial sentence inside the English:** Sirach 39:1 ("This passage continues Latin 38:39 in the preceding comparison chapter.").

## Patterns in the 457 minor corrections

Most are single words. They are proposals for an editor to accept or reject as sets, not errors of the same weight as the majors.

- **Old Testament fresh renderings shaped by the Hebrew.** 371 of the 481 corrections are in fresh renderings. Recurring cases: *cognatus* (kinsman) as "father-in-law" eight times in Exodus 18; *diis* and *deos* (gods) as "judges" in Exodus 21:6 and 22:7, 22:8, 22:27; *parabola* as "oracle" seven times in Numbers 23–24; *fortitudo* as "host" or "wealth" in Isaiah and Daniel; *frons* as "pier" through Ezekiel 40–41. Isaiah (43), Exodus (29), Jeremiah (26), Ezekiel (25), Numbers (22) and Zechariah (15) have the most.
- **Douay-Rheims modernisation slips in the New Testament.** 106 corrections are in Douay-based readings, 56 of them plain English slips left by the modernisation: "strait" modernised to "narrow" (Mark 5:1, 5:21; Acts 9:11), "to-next day" for "to-morrow" (Acts 23:20, James 4:13), "an fragrance" (Ephesians 5:2, Philippians 4:18), "Stephanus" for Stephanas (1 Corinthians 16:15, 16:17), and "do not be" plus a participle where the old subjunctive was converted mechanically (13 readings). Acts has 37 corrections.
- **The three letters revised on 7 November** (Galatians, 1 Thessalonians, 1 Timothy) drew four proposals, all in Galatians (1:16, 4:4, 4:24, 6:11).
- Seven books drew no correction: Song of Songs, Joel, Obadiah, Jonah, Haggai, 1 Thessalonians, 2 John.

## Coverage: Clementine verses with no Latin in the record

An automated comparison with the reference Clementine text found 687 Vulgate verses whose Latin appears in no reading of the book's record, and 43 more that are partly there. Readers reported many of the same gaps independently (for example Matthew 17:20, 18:11 and 23:14; Luke 17:36 and 23:17; John 5:4; Acts 9:7 and 13:31; Isaiah 56:12 and 64:1; Job 23:14; 2 Maccabees 15:37).

| Book | Verses | What they are |
| --- | ---: | --- |
| Sirach | 248 | The Latin Sirach is longer than the Greek; where a site verse spans several Vulgate verses only one is recorded |
| Esther | 105 | The Greek additions (Vulgate chapters 10–16): each grouped card records only its first Latin verse beside the whole English |
| Daniel | 89 | Susanna (chapter 13) in part, Bel and the Dragon (chapter 14), and verses of chapters 3–5 |
| Jeremiah | 48 | Verses the Greek Jeremiah lacks (for example in 33:18–26 and 39:4–13) |
| 1 Samuel | 40 | Mostly 17:12–31 and 17:55–18:5, absent from the Greek |
| Psalms | 29 | The second verse of two-verse cards |
| Numbers | 28 | Grouped cards (for example 5:23–26, 15:11–15, 27:3–8, 35:22–25, 36:7–10) |
| 19 other books | 100 | Listed in the file |

Two causes account for nearly all of them: the reader rows follow the Saints (Greek) verses, so a Vulgate verse the Greek lacks has no row; and grouped cards were recorded with only their opening Latin verse. The 7 November audit note found that for Esther the staging source page does hold the full Latin, so some of these are gaps in this archive, not on the site. **Whether staging shows the Latin for each of the 687 was not checked in this review.**

The 61 span findings are the same problem seen from the English side (Psalms 32, Esther 7, Numbers 5, Acts 5). In Esther 1:1 and 3:13a the English also carries fragments of Jerome's notes as if they were scripture. Acts 8:7–9 has its English shifted by one verse, and Acts 23:25–26 puts the letter's opening clause under the wrong verse.

## The recorded Latin

The recorded Latin was compared word for word with the reference Clementine transcription. It agrees in all but a handful of readings, and those differ by letter names, speaker labels and psalm-title notes, not by copying errors.

- **Suspected typos (139 notes).** In 137 the recorded Latin has the same words as the reference, so the site did not introduce them. Some look like slips in the electronic transcription itself (*sacrificum* 13 times in the reference, *agressus*, *Chadæorum*, *facum*, *imprudentissimi* at Isaiah 56:11); others may be the Clementine's real reading and the reader's memory at fault (*frustra* at Judges 14:6, *princeps plebis* at Luke 19:47). Settling these needs a printed Clementine. Where the English follows a suspect Latin word (2 Maccabees 8:8 "swiftly", Isaiah 56:11, 2 Kings 15:5 "was to judge"), fix the Latin first.
- **Glued initials and stray spaces (17 notes).** Romans 9:20 "Ohomo" and 11:33 "Oaltitudo" are still glued; 2 Maccabees 10:1 reads "Machab æus"; the Latin has 43 places with a space before a comma, typically after a chapter's first word ("Paulus ,").
- **Brackets (88 notes).** The Latin keeps 658 opening and 859 closing square brackets from the source edition's poetry and section layout. The reference has none. They are a presentation choice to keep or strip in one pass.
- **Coverage notes (51).** Latin missing, truncated or repeated on a card; superseded by the automated list above.

## Method

1. **Inputs.** Every reading was taken from the book folders' `verses.json` (captured from staging 1–7 November 2026) and cut into 301 batches.
2. **First reading.** Forty AI reviewers (Claude), assigned by division, each read their batches unit by unit, Latin against English, under [review-brief.md](review-brief.md). They recorded only departures from the Latin's meaning; style, register, accurate Douay wording and modern name forms were out of scope. All 301 batches came back with the full unit count.
3. **Reference check.** The recorded Latin was aligned by content with the public-domain Clementine and Douay-Rheims texts of [mborders/vulgata](https://github.com/mborders/vulgata) (from VulSearch), the same reference the 1 November audit used. This is what settles the Latin notes and the coverage list; reviewers' recollections of the Clementine were not relied on.
4. **Second reading.** All 520 proposed English corrections went to eight further reviewers who took no part in the first reading, under [second-reading-brief.md](second-reading-brief.md): 467 confirmed, 14 amended, 39 withdrawn (three of those reclassified as source checks).
5. **Coordinator check.** The 24 majors and a random sample of 22 minors were read again; none was overturned.

## Limits

- The reviewers are AI models. No human Latinist has read this, and the earlier "specialist sign-off pending" status stands.
- The second readers saw the first reader's proposal and reason, so the second reading was independent but not blind; a 90% confirmation rate should be read with that in mind. The minor corrections lean literal (for example "most bitter" for *amarissimæ* where the English has "bitter"), and an editor may reasonably decline some.
- One reading pass finds most plain departures, not all. The 13 books already checked on 2 and 7 November still drew 51 proposals between them, which shows a single pass leaves a residue.
- The review read the GitHub capture, not live staging. Readings changed on staging after capture were not seen.
- The reference transcription and the site's Latin descend from the same electronic Clementine text, so agreement between them shows faithful copying, not that the transcription is free of error. The reference also misfiles a few verses (Zephaniah 3:20, Zechariah 14:21, Titus 3:15), which were set aside.
- Span findings and reader notes on missing Latin were reported, not rewritten.

## By book

| Book | Readings read | Corrections (major) | Span | Latin notes | Vulgate verses not in record |
| --- | ---: | ---: | ---: | ---: | ---: |
| [Genesis](books/genesis.md) | 1,531 | 17 (0) | 0 | 7 | 0 |
| [Exodus](books/exodus.md) | 1,211 | 29 (1) | 0 | 4 | 0 |
| [Leviticus](books/leviticus.md) | 858 | 4 (1) | 0 | 4 | 0 |
| [Numbers](books/numbers.md) | 1,256 | 22 (2) | 5 | 20 | 28 |
| [Deuteronomy](books/deuteronomy.md) | 957 | 8 (0) | 1 | 7 | 1 |
| [Joshua](books/joshua.md) | 647 | 3 (0) | 2 | 3 | 11 |
| [Judges](books/judges.md) | 617 | 3 (0) | 1 | 6 | 0 |
| [Ruth](books/ruth.md) | 85 | 1 (0) | 0 | 2 | 0 |
| [1 Samuel](books/1-samuel.md) | 771 | 11 (0) | 3 | 1 | 40 |
| [2 Samuel](books/2-samuel.md) | 695 | 8 (0) | 0 | 1 | 0 |
| [1 Kings](books/1-kings.md) | 844 | 9 (0) | 0 | 9 | 5 |
| [2 Kings](books/2-kings.md) | 719 | 9 (0) | 0 | 10 | 0 |
| [1 Chronicles](books/1-chronicles.md) | 926 | 10 (2) | 1 | 5 | 14 |
| [2 Chronicles](books/2-chronicles.md) | 821 | 14 (1) | 0 | 3 | 0 |
| [1 Maccabees](books/1-maccabees.md) | 922 | 6 (2) | 0 | 8 | 7 |
| [2 Maccabees](books/2-maccabees.md) | 555 | 1 (0) | 0 | 11 | 3 |
| [Ezra](books/ezra.md) | 280 | 2 (0) | 0 | 2 | 0 |
| [Nehemiah](books/nehemiah.md) | 390 | 6 (2) | 0 | 0 | 14 |
| [Esther](books/esther.md) | 170 | 1 (0) | 7 | 0 | 105 |
| [Job](books/job.md) | 1,068 | 15 (1) | 1 | 2 | 2 |
| [Psalms](books/psalms.md) | 2,494 | 8 (0) | 32 | 3 | 29 |
| [Proverbs](books/proverbs.md) | 896 | 4 (0) | 0 | 1 | 18 |
| [Ecclesiastes](books/ecclesiastes.md) | 222 | 2 (0) | 0 | 0 | 0 |
| [Song of Songs](books/song-of-songs.md) | 115 | 0 (0) | 1 | 7 | 1 |
| [Lamentations](books/lamentations.md) | 150 | 1 (0) | 0 | 6 | 4 |
| [Wisdom of Solomon](books/wisdom-of-solomon.md) | 433 | 3 (1) | 0 | 50 | 0 |
| [Sirach](books/sirach.md) | 1,342 | 7 (1) | 0 | 39 | 248 |
| [Isaiah](books/isaiah.md) | 1,289 | 43 (0) | 0 | 19 | 3 |
| [Jeremiah](books/jeremiah.md) | 1,295 | 26 (0) | 0 | 5 | 48 |
| [Ezekiel](books/ezekiel.md) | 1,265 | 25 (0) | 0 | 0 | 7 |
| [Daniel](books/daniel.md) | 439 | 9 (0) | 0 | 5 | 89 |
| [Hosea](books/hosea.md) | 196 | 4 (0) | 0 | 3 | 2 |
| [Joel](books/joel.md) | 73 | 0 (0) | 0 | 0 | 0 |
| [Amos](books/amos.md) | 146 | 5 (0) | 0 | 2 | 1 |
| [Obadiah](books/obadiah.md) | 21 | 0 (0) | 0 | 0 | 0 |
| [Jonah](books/jonah.md) | 48 | 0 (0) | 0 | 0 | 0 |
| [Micah](books/micah.md) | 104 | 1 (0) | 0 | 2 | 0 |
| [Nahum](books/nahum.md) | 47 | 1 (1) | 0 | 0 | 0 |
| [Habakkuk](books/habakkuk.md) | 56 | 4 (0) | 0 | 0 | 0 |
| [Zephaniah](books/zephaniah.md) | 53 | 2 (0) | 0 | 1 | 0 |
| [Haggai](books/haggai.md) | 38 | 0 (0) | 0 | 0 | 0 |
| [Zechariah](books/zechariah.md) | 211 | 15 (2) | 0 | 0 | 0 |
| [Malachi](books/malachi.md) | 55 | 2 (0) | 0 | 0 | 0 |
| [Matthew](books/matthew.md) | 1,067 | 10 (0) | 0 | 1 | 2 |
| [Mark](books/mark.md) | 677 | 3 (0) | 0 | 8 | 0 |
| [Luke](books/luke.md) | 1,149 | 12 (0) | 0 | 8 | 2 |
| [John](books/john.md) | 878 | 5 (0) | 0 | 3 | 1 |
| [Acts](books/acts.md) | 1,002 | 37 (3) | 5 | 4 | 2 |
| [Romans](books/romans.md) | 433 | 9 (1) | 0 | 5 | 0 |
| [1 Corinthians](books/1-corinthians.md) | 437 | 16 (1) | 0 | 1 | 0 |
| [2 Corinthians](books/2-corinthians.md) | 255 | 9 (0) | 2 | 3 | 0 |
| [Galatians](books/galatians.md) | 149 | 4 (0) | 0 | 3 | 0 |
| [Ephesians](books/ephesians.md) | 155 | 5 (0) | 0 | 1 | 0 |
| [Philippians](books/philippians.md) | 104 | 2 (0) | 0 | 0 | 0 |
| [Colossians](books/colossians.md) | 95 | 2 (0) | 0 | 2 | 0 |
| [1 Thessalonians](books/1-thessalonians.md) | 89 | 0 (0) | 0 | 0 | 0 |
| [2 Thessalonians](books/2-thessalonians.md) | 47 | 1 (0) | 0 | 1 | 0 |
| [1 Timothy](books/1-timothy.md) | 113 | 1 (0) | 0 | 0 | 0 |
| [2 Timothy](books/2-timothy.md) | 83 | 1 (1) | 0 | 1 | 0 |
| [Titus](books/titus.md) | 46 | 6 (0) | 0 | 0 | 0 |
| [Philemon](books/philemon.md) | 25 | 1 (0) | 0 | 0 | 0 |
| [Hebrews](books/hebrews.md) | 303 | 3 (0) | 0 | 1 | 0 |
| [James](books/james.md) | 108 | 1 (0) | 0 | 1 | 0 |
| [1 Peter](books/1-peter.md) | 105 | 4 (0) | 0 | 3 | 0 |
| [2 Peter](books/2-peter.md) | 61 | 4 (0) | 0 | 1 | 0 |
| [1 John](books/1-john.md) | 105 | 1 (0) | 0 | 0 | 0 |
| [2 John](books/2-john.md) | 13 | 0 (0) | 0 | 0 | 0 |
| [3 John](books/3-john.md) | 14 | 1 (1) | 0 | 0 | 0 |
| [Jude](books/jude.md) | 25 | 1 (0) | 0 | 0 | 0 |
| [Revelation](books/revelation.md) | 405 | 1 (0) | 0 | 0 | 0 |
| **Total** | **34,254** | **481 (24)** | **61** | **295** | **687** |

"Latin notes" counts brackets, spacing, suspected typos and coverage notes together.
