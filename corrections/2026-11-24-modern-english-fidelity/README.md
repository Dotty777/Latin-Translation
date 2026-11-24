# Saints Modern English (Latin) — Fidelity Review against the Saints Latin Critical Text (24 November 2026)

- **Status:** `provisional_source_checked_ai_review`. These are AI-made corrections that still need the editor's decisions, an independent human Latin review and a read-aloud review. Verse placement should be re-checked against the Saints Critical Text Studio, which was not available to this review.
- **Scope:** the whole Latin-based Saints Modern English edition: 70 books, 34,070 verses, 6,180 notes and 293 additional (`unplaced`) verses. The NT was reviewed first, then the OT.
- **Source authority:** the Saints Latin Critical Text as held in this repository (`Saints-Latin-Critical-Text/`, synced to Studio v9 Phase 2). Where it has a distinctive or unusual reading, the English translates it as it stands. Nothing was harmonized to the Greek, the Hebrew, the Douay-Rheims or any other published translation.
- **Target:** *literal-smooth*, as defined in `Modern-English-OT/STYLE.md` §1: formal-equivalent English (NASB-1995 method), smoothed only as far as natural modern English requires.
- **Files:**
  - `README.md` (this file): method, results, open decisions.
  - `wording-changes.jsonl`: every wording and note change in canonical order. Each line holds `ref`, `field` (`verse`/`note`), `category`, `pass` (`verse-review`/`edition-wide`), `old`, `new` and `reason`.
  - `structural-changes.jsonl`: every verse, note and additional-verse change made by the structural repair (`book`, `kind`, `key`, `old`, `new`).
  - `verse-map.json`: for each book, the English verses that translate a critical-text verse filed under a different number (`{english key: [critical-text keys]}`). Everything not listed pairs with the critical-text verse of the same number.
  - `critical-text-anomalies.md`: problems in the critical text itself, for the Studio.

## Method

1. **Verse alignment.** A statistical word-alignment model was trained on the edition, and a verse-by-verse aligner run with it. Each English verse and additional verse was compared with the critical-text verse at its number and at neighbouring numbers.

   Before repair, 177 critical-text verses had no English verse at their number, 37 English verses had no critical-text verse at theirs, and about a dozen chapters were shifted. The rule applied was:
   - keep English at Saints.Bible verse slots;
   - translate every critical-text verse exactly once;
   - add critical-text verses that have no Saints slot as additional verses (`unplaced`, `no-site-verse`);
   - where the critical text files content under another number, keep the English at its slot and record the pairing in `verse-map.json`.

   After repair, every one of the 34,446 critical-text verses is covered (0 uncovered, 0 stray English keys).
2. **Rule checks.** These covered banned archaisms, the divine-name style (no `LORD`/`GOD`/`Yahweh`/`YHWH`), stray brackets and quotation-mark balance.
3. **Verse-by-verse review.** Seventy-nine parallel reviewers each covered about 450 verses, every one compared word by word against the Latin, using a single brief. The brief looked for:
   - **additions** with no Latin basis;
   - **omissions**, including Latin connectives;
   - **meaning errors**: tense, voice, mood, person, number, referent, negation;
   - **harmonization**: English that follows the Greek, Hebrew or a familiar English Bible instead of this Latin;
   - **doctrinal bias**, including capitals that settle a disputed referent;
   - **consistency** with the edition's established renderings;
   - **notes** that were doctrinal, described other translations, or were false for this Latin.
4. **Central validation.** Every proposal had to match the current text exactly. Proposals were rejected automatically if they added an archaism or a capital divine name, and flagged if they changed the quotation-mark count. Doctrinal, referent and capitalization changes were read individually; the decisions taken are listed below.
5. **Edition-wide passes.** Terms deliberately left to a central pass were standardized after the review (see *Renderings standardized*).
6. **Final QA.**
   - All 1,290 chapter files were regenerated from the JSON: **0 mismatches**.
   - The critical-text coverage check passes.
   - No banned word, capital divine name or `YHWH` remains in verses or notes.
   - Edition counts were updated in the root, NT, OT and division READMEs.
   - Chapters whose quotation marks balance only across a chapter break or an additional verse are deliberate: Genesis 31, Exodus 32, Joshua 20, and Job 13–29, where speeches now run across chapter breaks.

## Results

**1,566 wording and note changes:**
- 922 to verse text (917 distinct verses) and 644 to notes;
- 307 in the NT and 1,259 in the OT;
- 1,218 from the verse-by-verse review and 348 from the edition-wide passes.

There were also **242 structural changes**: 123 verses, 71 notes and 48 additional verses, across 24 books. 2 John and 3 John needed no change. 1 Thessalonians also needed none; it was already revised on 7 November.

| Category | Changes | What it covers |
| :--- | ---: | :--- |
| consistency | 755 | Same Latin, same English (established renderings, formulas, names, headings) |
| note | 504 | Notes corrected: claims about other translations, doctrinal/devotional framing, false statements about the Latin/Greek/Hebrew or about verse numbering, capital LORD/YHWH |
| harmonization | 91 | English that followed the Greek, Hebrew or Douay-Rheims instead of this Latin |
| meaning | 49 | Wrong sense, tense, mood or relation (e.g. *erat* "existed" → "was" in John 1) |
| addition | 40 | Words with no Latin basis removed (intensifiers, supplied names) |
| grammar | 33 | Latin syntax misrepresented (purpose clauses, deponents, comparatives) |
| doctrinal | 26 | Capitals or wording that settled a disputed referent; doctrinal framing in notes |
| omission | 24 | Latin words or connectives not represented |
| clarity | 22 | Quotation marks and word order where the English was unclear |
| referent | 21 | Wrong subject or object, or a capital for the wrong person |
| negation | 1 | Negation added without Latin basis (Job 31:20) |

### By book

| Book | Verse edits | Note edits |
| :--- | ---: | ---: |
| Genesis | 38 | 18 |
| Exodus | 25 | 21 |
| Leviticus | 29 | 15 |
| Numbers | 17 | 18 |
| Deuteronomy | 25 | 12 |
| Joshua | 15 | 7 |
| Judges | 10 | 13 |
| Ruth | 2 | 0 |
| 1 Samuel | 13 | 14 |
| 2 Samuel | 9 | 14 |
| 1 Kings | 20 | 11 |
| 2 Kings | 13 | 8 |
| 1 Chronicles | 9 | 18 |
| 2 Chronicles | 16 | 13 |
| Ezra | 6 | 3 |
| Nehemiah | 4 | 4 |
| Esther | 3 | 1 |
| 1 Maccabees | 25 | 3 |
| 2 Maccabees | 9 | 7 |
| Job | 37 | 25 |
| Psalms | 79 | 78 |
| Proverbs | 16 | 22 |
| Ecclesiastes | 5 | 8 |
| Song of Songs | 9 | 9 |
| Lamentations | 2 | 3 |
| Wisdom of Solomon | 11 | 4 |
| Sirach | 34 | 24 |
| Isaiah | 44 | 52 |
| Jeremiah | 68 | 30 |
| Ezekiel | 63 | 31 |
| Daniel | 18 | 12 |
| Hosea | 4 | 9 |
| Joel | 3 | 5 |
| Amos | 14 | 2 |
| Obadiah | 0 | 1 |
| Jonah | 1 | 4 |
| Micah | 3 | 7 |
| Nahum | 1 | 2 |
| Habakkuk | 2 | 0 |
| Zephaniah | 0 | 1 |
| Haggai | 1 | 1 |
| Zechariah | 12 | 10 |
| Malachi | 1 | 3 |
| Matthew | 23 | 13 |
| Mark | 21 | 13 |
| Luke | 34 | 12 |
| John | 17 | 5 |
| Acts | 16 | 13 |
| Romans | 23 | 8 |
| 1 Corinthians | 7 | 5 |
| 2 Corinthians | 6 | 6 |
| Galatians | 4 | 2 |
| Ephesians | 4 | 3 |
| Philippians | 2 | 0 |
| Colossians | 4 | 0 |
| 1 Thessalonians | 0 | 0 |
| 2 Thessalonians | 1 | 0 |
| 1 Timothy | 6 | 0 |
| 2 Timothy | 1 | 0 |
| Titus | 2 | 2 |
| Philemon | 0 | 1 |
| Hebrews | 10 | 4 |
| James | 1 | 1 |
| 1 Peter | 0 | 1 |
| 2 Peter | 1 | 2 |
| 1 John | 3 | 2 |
| 2 John | 0 | 0 |
| 3 John | 0 | 0 |
| Jude | 1 | 1 |
| Revelation | 19 | 7 |

## Structural repair (summary)

The full list is in `structural-changes.jsonl` and `critical-text-anomalies.md`.

- **Verses split into their Saints slots:**
  - *Where the critical text holds two or more Saints verses in one condensed verse:* Genesis 50:22–23; Numbers 3:9–10, 5:23–26, 35:13–15, 35:22–25, 36:7–10; 1 Samuel 20:21–22; Nehemiah 7:47–48, 12:33–34; Psalms 12, 15, 43, 108, 129; Hosea 6:2–3; Matthew 17:14–15; Mark 4:40–41; Luke 4:18–19; Acts 9:6–7; 2 Corinthians 1:23–24; and many Sirach verses.
  - *Re-paired where the English had drifted by a half verse:* Psalm 72:22–23, Wisdom 2:3–4, Ezekiel 7:9–10, 2 Timothy 4:8–10, Revelation 20:7–10.
- **Critical-text verses with no Saints slot, added as additional verses:**
  - Pentateuch: Genesis 31:51, 35:21; Exodus 28:24–25, 35:15, 35:17, 37:22.
  - Historical books: Joshua 8:13, 8:30–35; Judges 5:32; Nehemiah 7:68; Daniel 3:67–70.
  - Poetry and Wisdom: Psalms 2:13, 4:10; Sirach 51:11 and others.
  - NT: Luke 17:36.
- **Content the critical text files under Vulgate numbers:** the English stays at the Saints slot and is mapped. Examples are Genesis 31:55–32:32, Exodus 36–39, Leviticus 15:19–23, 1 Kings (many 3 Kingdoms placements), Esther 5 and 10, Proverbs 15–16, 20 and 31, Sirach 30–36 and Revelation 20:7–10.
- **Notes rewritten** where they misdescribed the numbering. Examples include notes claiming a verse is "absent from the Vulgate" when the critical text has it.

## Renderings standardized (edition-wide)

| Latin | Rendering | Notes |
| :--- | :--- | :--- |
| *semen* (descendants) | "seed" | ~140 verses; replaces "offspring"/"descendants"/"lineage". It keeps the Latin's collective singular (Genesis 3:15, Galatians 3:16). |
| *Hæc dicit Dominus …* | "This is what the Lord … says" | Includes Revelation 2–3 ("This is what the One who … says"). |
| *ait/dicit Dominus* (inserted) | "says the Lord" | Replaces the stray "declares the Lord". |
| *in finem* (Psalm headings) | "To the end" | Psalm headings also use "for David himself" and "A song of steps". |
| *infernus/inferi* | "the underworld" | *gehenna* → "Gehenna". |
| *pactum*, *fœdus* | "covenant" | Isaiah 28:15, 28:18 now read "covenant with death". |
| *pœnitentia*, *pœnitentiam agere* | "repentance", "repent" | No "penance" remains. *pœnitet* in the sense of regret keeps "regret" where the edition uses it. |
| *propitiatorium*; *tabernaculum testimonii*; *arca testamenti* | "mercy seat"; "tabernacle of the testimony"; "ark of the covenant" | |
| *sancti* (OT persons) | "holy ones" | The NT keeps "saints". |
| *Absit* (Paul) | "Far from it" | Luke 20:16 and Acts 10:14 are aligned with it. |
| *fides Jesu Christi* | "the faith of Jesus Christ" | The literal genitive, which keeps the Latin's ambiguity. Applies at Romans 3:22, 3:26 and Galatians 2:16, 2:20; the edition already had it at Galatians 3:22 and Philippians 3:9. **The Greek-based edition uses "faith in" with a note.** This is a deliberate own-source choice and is listed as an open item. |
| *caprea* | "roe deer" | |
| *sacramentum* (Ephesians 5:32, Colossians 1:27) | "mystery" | As everywhere else in the edition. |

## Decisions taken centrally

- **"Spirit" capitals.** "Spirit" stays capitalized for *spiritus Dei/Domini* and "My/His Spirit" where God speaks or is the plain referent, as in the Greek-based edition. The proposals to lowercase Genesis 1:2, Genesis 6:3 and Romans 1:4 were rejected. Lowercase was accepted where the speaker is a pagan (Genesis 41:38) or the Latin has a bare, open *spiritus*: Numbers 27:18, and Revelation 1:10, 4:2 and 21:10 (*in spiritu*, matching 17:3).
- **2 Corinthians 4:4** keeps "the god of this age", lowercase. The critical text's capital *Deus* is a printing convention, and the note now explains both readings.
- **Disputed OT figures.** As in the Greek review, the edition's existing capitals were kept: proposals for Psalm 2:2, 2:7–9, 15:10 and 31:8 were rejected. Capitals were changed only where they were inconsistent inside one passage. In Isaiah 52:13–15 the servant is now lowercase, matching 53:1–12 and the other servant passages; this is reversible as a set.
- **Job quotation marks.** In Job 14–32, speeches now run across chapter breaks instead of closing and reopening at each chapter. The rest of Job keeps the per-chapter close and reopen. The marks balance either way, but this is a mixed style to settle.

## Open items for the editor

1. **Capitals for disputed figures.** These were left as the edition had them and flagged by reviewers:
   - Psalms: 2, 15:10, 31:8, 109.
   - Isaiah: 7:14–15; 8:8; 9:5–6; 11:1–10; 24:16, 41:2 and 41:10 ("Righteous One"); 45:8; 48:16; 59:20.
   - Jeremiah 23:5–6; Lamentations 4:20; Micah 5:1–5; Haggai 2:7.
   - Daniel: 7:13–14 ("Son of Man", He/Him), 8:11, 8:25, 9:24, and 9:25–26. In 9:25–26 the English says "Christ the leader" and "Christ will be put to death" for lowercase *christus*, while the edition elsewhere writes "anointed".
   - Zechariah: 2:12–15 ("sent Me", against "me" at 4:9 and 6:15), 3:8, 6:12–13, 9:9–11, 12:10.
   - Malachi 2:15 and 3:1.

   One rule is needed for the whole edition, and it should match whatever is decided for the Greek-based edition.
2. **Bare *spiritus* capitalized as "Spirit"** in Ezekiel (2:2, 3:12, 3:14, 3:24, 8:3, 11:1, 11:24, 43:5) and Isaiah 32:15, while Ezekiel 1:12, 1:20 and 10:17 are lowercase.
3. ***fides Jesu Christi*: "the faith of" here against "faith in" in the Greek-based edition.** Matthew 27:3 (Judas, *pœnitentia ductus*) now reads "moved by repentance", and Judges 21:6 likewise. Both are reversible.
4. **Remaining small variation:**
   - *tribulatio*: tribulation / affliction / distress;
   - *servus*: servant / slave (left by sense);
   - *visitare*: punish / visit / bring a reckoning;
   - *Euge*: "Aha" (Hebrew sense; a note gives the literal "Well done");
   - *latro*: robber / bandit in places;
   - *janitores*: doorkeepers / gatekeepers;
   - *in monte Ephraim*: "hill country of Ephraim" / "Mount Ephraim";
   - *honestas*: wealth / honor.
5. **Names.** Some Latin name forms were kept where the Latin genuinely has a different name: Gideon for *Gedeonis*, Numbers 1:11; Aijalon for *Ahialon*, Judges 12:11; Helon, 1 Chronicles 6:54; Shemaiah/Shimei, 1 Chronicles 25:17 and 27:27. Otherwise the edition's standard spellings stand.
6. **Notes on the printed Clementine.** Several notes still compare with "the Clementine Vulgate". Where the critical text differs from the printed Clementine, those were reworded to "this Latin text"; any that remain should be checked against a printed Clementine.

## Commits

This review is in the commits on branch `ccr-46393f40-vccvrn` dated 24 November 2026:
- three structural commits (`f0a30c4`, `eab2201`, `ab1eeee`);
- the wording-review batches;
- the edition-wide standardization commits;
- this record.
