# Points left for a specialist · 14 November 2026 reading pass

Collected from the reviewers' notes, by section. Nothing listed here was changed.

## Exodus 1–18

# latin-001 notes (Exodus 1–18, Clementine Vulgate)

Left unchanged; possible editorial decisions:

- **Exodus 13:10**: *a diebus in dies* is given as “year after year”, which follows the Hebrew. The Latin literally says “from days to days” (Douay). Is the Hebrew sense acceptable here?
- **Exodus 11:7**: “against either person or beast” follows the Hebrew. The Latin *ab homine usque ad pecus* means “from man to beast” (the column has “from person to beast” in 12:12). I kept “against” because the literal Latin would be unclear when read aloud.
- **Exodus 10:7**: “Release the men” renders *homines* (people). In 10:11 Pharaoh says *tantum viri* (only the men), so the English blurs that contrast. Possible fix: “these people”.
- **Exodus 18:23**: “sustain His instructions” (*præcepta ejus poteris sustentare*) is a little unclear aloud. “bear” or “uphold” would be clearer. It is not wrong, so I left it.
- **Exodus 18:11**: in “because they acted arrogantly against them”, the Latin does not say who “they” and “them” are either (the Egyptians against Israel). Naming them would add an interpretation.
- **Exodus 4:16** (“his guide”) and **18:19** (“Represent the people”) fill in a role where the Latin *esse … in his quæ ad Deum pertinent* is elliptical. Both seem acceptable.
- **Exodus 18:6**: Jethro’s message (“I, Jethro, your relative by marriage, am coming…”) has no quotation marks, unlike the column’s other direct speech. This is only punctuation, so I did not change it.

Data:

- SRC 15:1 begins with “[Cantemus”, SRC 15:19 ends with “ejus.]”, and SRC 15:21 is in brackets. These look like canticle markers in the Latin source data and do not appear in the EN.
- SRC 1:19 reads “Hebreæ”. The Clementine has *Hebrææ*, so this looks like a source typo.

## Exodus 19–33

# latin-002 (Exodus 19–33) · notes

## For a specialist or editor (not changed)

- **Exodus 33:5**: “Once I shall go up in your midst and destroy you” (*semel ascendam in medio tui, et delebo te*) is the Douay wording and is unclear when read aloud. The Douay note reads it as a condition (“if I but once go up among you, I shall destroy you”). An editor should decide whether to render it that way.
- **Exodus 23:26**: *infœcunda* and *sterilis* are feminine (no barren woman). The English has “no one unfruitful or barren”. I left it, but “no woman” would be closer to the Latin.
- **Exodus 21:10**: in “If he takes another woman for him”, *ei* could mean the son (21:9) or the master himself. The Latin is ambiguous too, so I left it.
- **Exodus 19:16**: “rang out increasingly loudly” is a little clumsy aloud but easy to follow. I left it.

## Data

- **Exodus 30:6**: the SRC reads “ante arcum”. The Clementine reads *arcam* (ark), so this is probably a typo in the source text. The English correctly says “ark”.
- **Exodus 28:29a**: an empty LOCKED placeholder row (no Latin, no English).
- **Exodus 20:13–15 and 21:16–17**: these rows follow the Greek order and carry vulgate_reference tags. Each English line matches its own Latin, so no action is needed.

## Exodus 34–40; Leviticus 1–9

# latin-003 notes (Exodus 34–40; Leviticus 1–9)

## For an editor (not changed)

- **Exodus 35:30–35 (missing closing quote).** Moses’ speech opens with “ at 35:30, but 35:35 has no closing ”. In the Vulgate, 36:1 (*Fecit ergo Beseleel*) is narrative, so the quote should close at the end of 35:35. I left it because it is a punctuation-only fix.
- **Exodus 39:6 (vg 38:29).** “seventy-two thousand talents and four hundred shekels” follows the Douay reading of *talenta septuaginta duo millia, et quadringenti supra sicli*. The Latin can also be read as 70 talents and 2,400 shekels, which matches the Hebrew. I kept the Douay reading.
- **Exodus 34:6.** The column supplies “Moses said” for the bare *ait*. That fits the Vulgate, because 34:7 speaks to God in the second person (*custodis*, *apud te*). It differs from the Hebrew, where YHWH proclaims, so it is an editorial choice. Kept.
- **Possible spoken tidy-ups, left alone:** 36:28, where “at the individual corners” is clumsy for *per singulos angulos* (one at each corner), and 34:29, where “from sharing in speech with the Lord” is stiff for *ex consortio sermonis Domini*.

## Data problems

- **Duplicate references.** 33 references appear twice because the Vulgate verses are interleaved in Greek row order: Exodus 35:12a, 36:10–36:33, 37:1, 37:4, 37:11, 37:12, 37:20, 37:21, 38:2, 38:6, 38:7 and 39:20. Exodus 35:12a is used for both vg 35:15 and vg 35:17. validate.py keys rows by reference, so only the last row of each pair can be changed and validated. None of my changes touch these rows.
- **Exodus 40:13–15.** These three LOCKED rows share card vg-exodus-40-13 with the same SRC and EN. As a result, the quote opened at 40:2 is closed three times.
- **Empty LOCKED rows:** Exodus 37:18b and 38:11a.
- **Probable typos in the Latin source:**
  - Leviticus 7:38 has *mandabit*; the Clementine has *mandavit*.
  - Leviticus 6:4 (vg 6:11) has *efferret*; the Clementine has *efferet*.
  - In both verses the English follows the correct reading.

## Leviticus 10–24

# latin-004 (Leviticus 10–24): notes

Editorial decisions (not changed):
- Lev 10:1 and 16:1: ignem alienum is rendered “unauthorized fire”. That gloss is fair, but the Vulgate’s image is “strange (alien) fire”. If it changes, change both verses together.
- Lev 14:30: the Latin is singular (turturem sive pullum columbæ), and 14:31 then goes on with “one … the other”. The English plural (“the turtledoves or young pigeons”) gives the sense, so I left it. A specialist can decide whether the singular should show.
- Lev 23:41: solemnitatem ejus is rendered “His solemn feast”, taking the pronoun as God. It could also be “its solemnity” (the feast’s), as Douay has it. Both readings are possible.
- Lev 22:19: “to be offered by you it shall be …” runs together when read aloud. A comma after “you” would help, but that would be a punctuation-only change, so I left it.

Data:
- No LOCKED rows; 492 rows parsed. The EN column uses straight apostrophes (’ only appears in my new text in 13:3).

## Leviticus 25–27; Numbers 1–8

# latin-005 notes (Leviticus 25–27; Numbers 1–8)

- Data: two rows share the reference “Numbers 6:23” (the second is card vg-numbers-6-27, Vulgate 6:27, placed after 6:23 in the Greek order). validate.py keys rows by reference, so the first 6:23 row (vg-numbers-6-23) could not be validated if it were ever changed. Neither row was changed.
- Editorial: panes/mensa propositionis is “bread of the Presence” in Numbers 4:7 and 8:2 (and Leviticus 21:8 in latin-004) but “bread of presentation” in Exodus (latin-002/003). The column should use one term throughout. Left unchanged here.
- Editorial: Leviticus 27:29 morte morietur is “shall surely be put to death”. That matches how the column handles morte moriatur in Leviticus 20, but Exodus 19:12 and 31:14 render morte morietur as “shall surely die”. Left unchanged.
- Specialist: Leviticus 26:1 renders insignem lapidem as “engraved stone”, which matches the Hebrew maskit; Douay has “remarkable stone”. It is defensible because insignis can mean “marked”, so it was left. A Latinist may prefer “marked” or “conspicuous stone”.
- Spoken (left): Numbers 3:25–26 splits as “They shall have charge in the tabernacle of the covenant / of the tabernacle itself …”. It is slightly tangled aloud but follows the Latin verse split.

## Numbers 9–24

# latin-006 notes (Numbers 9–24)

- Specialist: Num 24:7 Tolletur propter Agag, rex ejus is rendered “Because of Agag his king shall be removed”, which follows Douay and the old reading about Saul. Tolletur can also mean “shall be lifted up” (exalted above Agag, as in the Hebrew). Left unchanged.
- Spoken (left): Num 10:13 “They were the first to break camp” leaves it unclear who “they” are. Primi is most likely the leading camp (Douay “the first went forward”), which is Judah in 10:14. A rewording would need an editorial decision.
- Editorial: Num 16:3 Sufficiat vobis is “Enough from you!”. Douay has “Let it be enough for you”, meaning “be content with what you have”, while the English sounds like “stop talking”. Close enough that I left it.
- Editorial: Num 16:9 ministraretis ei is rendered “to minister to them” (the people), as in the Hebrew. Douay takes ei as God. The Latin allows either reading. Left unchanged.
- Editorial: The Vulgate’s harlotry image is softened in Num 14:33 (fornicationem, “unfaithfulness”) and 15:39 (fornicantes, “straying unfaithfully”). The two verses agree with each other, so I left them.
- Editorial: Num 14:10 tectum fœderis (Douay “roof of the covenant”) is rendered “tent of the covenant”. That is a fair gloss. Num 13:22 has “Tanis, the city of Egypt” for urbem Ægypti (“a city of Egypt”). Both left.
- Data: 494 rows parsed, 6 LOCKED (11:34/11:35 share a card; 15:4, 15:11, 17:7 and 20:28 are grouped). Num 10:13 has a curly “Lord’s” where the rest of the chunk uses straight apostrophes. My new text uses curly apostrophes, and I left the existing straight ones as they are (as in latin-004).

## Numbers 25–36; Deuteronomy 1–2

# latin-007 notes (Numbers 25–36; Deuteronomy 1–2)

- Editorial: after the Numbers 26:61 change, Numbers 3:4 and 26:61 both have “strange fire” for ignem alienum. Leviticus 10:1 and 16:1 (latin-004) still have “unauthorized fire”, so Leviticus should be brought into line.
- Verse boundary (left): in Deuteronomy 2:10–11, crederentur (“were believed”) is in 2:11, but the English puts “they were thought to belong to the line of the Anakim” in 2:10. The sense is right, and splitting the clause at the Latin verse break would read worse aloud. It is an editorial call whether to realign it.
- Specialist: Numbers 31:42 renders quam separaverat his qui in prælio fuerant as “that he had set apart for those who had been in battle”. Douay reads it as “separated from them that had been in the battle”. The current reading fits the contrast with vero in 31:43, so it was left, but a Latinist may want to confirm it.
- Left: Numbers 29:1 renders dies clangoris … et tubarum as “a day of trumpet blasts and sounding”. That reverses the Latin order and sounds slightly odd aloud (Douay has “the day of the sounding and of trumpets”).
- Left: Numbers 28:15 renders in holocaustum sempiternum as “with the continual burnt offering”. The Latin literally says “for a continual burnt offering”, and Douay has “over and above the perpetual holocaust”.
- Data: none of the 5 LOCKED grouped rows were touched (27:3, 28:29, 35:13, 35:22, 36:7). Numbers 26:15–47 follow the Greek order, with vulgate_reference giving the Latin verse. No problems were found.

## Deuteronomy 3–21

# latin-008 notes (Deuteronomy 3–21)

- Data: Deuteronomy 7:25 SRC reads “abominatio est Domini tui”, and the EN follows it (“an abomination to your Lord”). The Clementine text as usually printed (and Douay, “to the Lord thy God”) has “Domini Dei tui”, so “Dei” may have dropped out of the source. If it has, the EN should be “to the Lord your God”. Left unchanged until the source is checked.
- Data: rows 5:17/5:18 carry swapped cards (vg-deuteronomy-5-18 “neque mœchaberis” sits in the 5:17 row) because they follow the Greek order. This looks intended. Neither row was changed.
- Editorial: in 21:14 “because you have violated her” renders humiliasti (Douay “humbled her”). The modern sense of “violated” is stronger than the Latin. Left unchanged.
- Spoken (left): 15:18 “he has served you at the worth of a hired worker’s wages” (juxta mercedem mercenarii) is a little stiff aloud but can be followed.
- Specialist (left): 5:24 “a human being can live when God speaks with him” generalises vixerit homo (“man has lived”), the experience they have just had. It is defensible next to 5:26, so it was left.

## Deuteronomy 22–34; Joshua 1–5

# latin-009 notes (Deuteronomy 22–34; Joshua 1–5)

- Data: Deuteronomy 23:25 and 23:26 look swapped against the Greek/Hebrew order. Row 23:25 carries vg 23:25 (the standing grain) and row 23:26 carries vg 23:24 (the vineyard). In the Greek and Hebrew, 23:25 is the vineyard and 23:26 is the grain. Neither row was changed.
- Data: Joshua 4:23 EN also contains Vulgate 4:24 (“just as He had done before at the Red Sea …”), which is not in the row’s SRC. No row carries vg-joshua-4-24, because the Joshua 4:24 row is vg-joshua-4-25. Left as is.
- Data: Joshua 5:14 EN also contains Vulgate 5:15 (Joshua falls facedown and asks “What does my lord say …”), which is not in the SRC. The Joshua 5:15 row is vg-joshua-5-16. Left as is.
- Data (harmless): the Deuteronomy 32–33 SRC keeps the Clementine canticle brackets [ ]. Deuteronomy 26:13 SRC has the Clementine misprint “Domini Deo tui”. The EN is unaffected in both places.
- Editorial: Deuteronomy 33:5 renders apud rectissimum (singular, the Vulgate’s Jeshurun) as “among the most upright”. “With the most upright one” would match 33:26 (“the God of the most upright”). Left unchanged.
- Editorial: Confortare et esto robustus is “Be strong and resolute” in Deuteronomy 31:7 and 31:23 but “Take courage and be strong” in Joshua 1:6, 1:7 and 1:9, where the Joshua passage echoes Deuteronomy 31. The column may want one rendering. Also, Joshua marks speech with quotation marks but Deuteronomy uses a colon with no quotes.
- Spoken (left): Deuteronomy 27:20 “uncovers the covering of his bed” (lectuli ejus = the father’s) has the same ambiguity that was fixed in 23:1, but the context makes it clear. Deuteronomy 26:1 “take possession of it and live there” sounds like a command, though the Latin is part of the “when” clause. It does no harm.

## Joshua 6–21

# latin-010 notes (Joshua 6–21)

## Editorial / specialist (not changed)
- Joshua 7:25: “may the Lord drive you out in trouble today” for *exturbet te Dominus* reads oddly aloud; it seems to be trying to keep the *turbasti/exturbet* wordplay. Douay has “the Lord trouble thee this day”. Possibly a 9 November reading, so left alone; worth an editor’s look.
- Joshua 13:1–12: God’s speech opens at 13:1 and closes at 13:12, so God speaks of “Moses, the Lord’s servant” (13:8) and “Moses struck them down” (13:12). The Latin sentence runs on from 13:7 into 13:8, so there is no clean break, but most versions end the speech at 13:7. Needs an editorial decision across two or three rows.
- Joshua 14:15: *Adam maximus ibi inter Enacim situs est* can mean either “Adam, the greatest among the Anakim, was laid there” (Douay) or “Adam the great was laid there among the Anakim” (Jerome’s Adam-at-Hebron tradition). The current English follows the second reading. Kept.

## Data problems
- Clementine verses with no row in this chunk: 6:4, 8:13, 8:26, 10:15, 13:33, 20:4–6. They are already listed in `..\latin\corrections\2026-11-09-full-review\vulgate-verses-not-in-record.json`.
- Duplicate locked rows repeat the same Latin and English: 15:59/15:59a; 19:47/47a (Vulgate 19:48) and 19:48/48a (Vulgate 19:47), which also puts 19:48 before 19:47; 21:36/21:37 (both Vulgate 21:36); 21:38/21:39 (both Vulgate 21:37); and 21:42–42d (all Vulgate 21:40). The site probably shows these verses twice or more.
- Locked 21:36 spells names differently from the rest of the column: “Jaser” (Jazer elsewhere: 13:25, 21:37) and “Jethson” (Jahaz in 13:18). Fix this when the duplicate rows are unlocked.
- The source text has stray square brackets in 10:12 (“[Sol”) and 10:13 (“suis.]”). The English correctly leaves them out.

## Joshua 22–24; Judges 1–13

# latin-011 notes (Joshua 22–24; Judges 1–13)

- Judges 5:31: EN ends with “The land had rest for forty years.” That sentence is Clementine Judges 5:32 (Quievitque terra per quadraginta annos), which has no row of its own and is not in this row's SRC. Left unchanged so the sentence is not lost; editorial/data decision needed (add a 5:32 row or accept the merge).
- Joshua 24:29–31 and 24:33: rows follow the Greek order with Vulgate 24:29/30/31 shuffled and shared LOCKED cards (24:31/31a, 24:33/33a/33b) duplicating the same text. Not touched; worth a data check.
- Joshua 22:24: “that we said” for ut diceremus (“that we should say”) slightly suggests the words were actually spoken; acceptable, left for an editor.
- Judges 1:30, 1:33, 1:35: “became subject to their/his/its tribute” for factus est ei tributarius is a little opaque aloud (“became tributary to them”); left as a column convention.
- Judges 8:7, 8:16: “tear” for conteram/contrivit (crush, grind) follows the Hebrew-influenced image; left.
- The column uses straight apostrophes (Lord's) throughout, against house style ’; my edits introduce no new apostrophes. A global pass may be wanted.

## Judges 14–21; Ruth 1–4; 1 Samuel 1–8

# latin-012 notes (Judges 14–21; Ruth 1–4; 1 Samuel 1–8)

## For a specialist / editorial decision (not changed)
- 1 Samuel 7:14 — EN “Israel rescued them from the hand of the Philistines” follows the Hebrew (Israel delivered their territory). The Latin *liberavitque Israël de manu Philisthinorum* has no “them” and Douay reads “and he delivered Israel”; decide whether to render the Vulgate as “and He delivered Israel…”.
- Judges 18:19 — *in una tribu* (“in one tribe”) is set against *unius viri*; EN “in a tribe” keeps the contrast loosely. Optional.
- 1 Samuel 2:3 — EN “let the old boasts leave your mouths” adds “boasts”; Latin *vetera* is just “old things” (Douay “old matters”). Left as a fair reading.
- 1 Samuel 1:26 — *coram te* is “before you”; EN “beside you” follows the Hebrew. Small; left.
- 1 Samuel 4:18 — *juxta ostium* is “by the door”; EN has “beside the gate” (Hebrew). Small; left.

## Data problems
- Judges 16:8 SRC reads *quibus vinxit eam* (“her”); the Clementine reads *eum*. Probably a transcription error in the source text. EN correctly has “him”.
- 1 Samuel 2:10 SRC ends with a stray “]” (*christi sui.]*) with no opening bracket.
- 1 Samuel 4:21 SRC has *vocabit* (future); the sense, and EN, is past (*vocavit*).
- The column in this chunk uses straight apostrophes (’ house style not applied); my edits add no new apostrophes.
