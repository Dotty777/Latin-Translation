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
