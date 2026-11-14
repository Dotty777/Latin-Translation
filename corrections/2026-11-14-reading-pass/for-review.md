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
