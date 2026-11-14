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

## 1 Samuel 9–25

# latin-013 (1 Samuel 9–25) notes

## Data problems
- 1 Samuel 20:42 and 21:1 both point to card `vg-1-samuel-20-42`, and neither is marked LOCKED. Its English also ends with “David rose and went away, while Jonathan went into the city,” which is Clementine 20:43 (*Et surrexit David, et abiit…*), not 20:42. 20:43 has no row of its own. I left it alone (moving content between rows is not allowed). Someone needs to decide the card mapping.
- Rows follow the Greek column, so these Clementine verses have no row in this chunk: 13:1, 17:12–31, 17:41, 17:50, 17:55–18:5, 18:10–11, 18:17–19, 23:12, 20:43. Because 17:50 is missing, the 17:51 English starts mid-sentence (fixed for the ear in changes.json).
- The column mixes straight (') and curly (’) apostrophes, about 126 straight and 35 curly in this chunk. I did not normalise them.

## Editorial points (left unchanged)
- 14:14: “half a jugerum” keeps the Latin unit; “half an acre” would be easier to hear, but that is a column-wide choice.
- 18:21: “Through two things you shall become my son-in-law today” is literal for *in duabus rebus* and is obscure aloud. Leave it unless the column wants a gloss.
- 25:31: “no sobbing or pang of conscience” is literal for *singultum*. “Grief” (Douay) may sound better aloud.
- 15:17–18: the Latin is one question across both verses. The English turns it into statements. Acceptable, but noted.

## 1 Samuel 26–31; 2 Samuel 1–14

# latin-014 notes (1 Samuel 26–31; 2 Samuel 1–14)

Column is in good shape; only 5 changes. For a human or editorial decision (not changed):

- 1 Sam 30:30: Vulgate "Arama" is rendered "Hormah" (the Hebrew name). This matches the column's habit of using Hebrew-based name forms (Siceleg → Ziklag, Jether → Jattir), but it is a different name from the Latin. Editorial call.
- 1 Sam 31:9: "in populis" is plural ("among the peoples"); the English has "among the people". Douay also has the singular, so it was left.
- 2 Sam 9:11: the Vulgate gives "Miphiboseth comedet super mensam meam" to Ziba ("my table"), and the English follows it. That is correct for the Latin but odd. Left as it is.
- 2 Sam 14:11: "ut non multiplicentur proximi sanguinis ad ulciscendum" means the next of kin should not be multiplied to take revenge. The English has "do not multiply their vengeance", which shifts the sense slightly. Left; worth a look.
- 2 Sam 14:16: "The king has listened, to rescue his maidservant…" is a little stiff when read aloud. Optional smoothing.

Data:
- 1 Sam 30:28 and 30:28a share card vg-1-samuel-30-28 (both LOCKED, identical text).
- 2 Sam 5:16a is an empty LOCKED row (no source or English).
- The validator's regex parses 485 rows. The manifest says 486, including the empty 5:16a row.

## 2 Samuel 15–24; 1 Kings 1–3

# latin-015 notes (2 Samuel 15–24; 1 Kings 1–3)

- 2 Samuel 16:10: the English has “why He has done this?”, with a capital He, which makes it God’s action. In the Latin (quare sic fecerit), the natural subject is Shimei, the one commanded to curse (cf. Hebrew “why have you done so?”). This needs an editorial decision on “he” versus “He”. Not changed.
- 2 Samuel 23:10: Latin cumque ascendissent viri Israël literally says “had gone up”. The English “had withdrawn” follows the Hebrew sense. It is acceptable, but a specialist may prefer the literal wording. Not changed.
- 1 Kings 2:23: Latin has quia contra animam suam locutus est (“for Adonijah has spoken … against his own life”). The English uses the Hebrew-style oath “if … has not spoken”. The sense is the same. Not changed.
- Consistency (not changed): the column spells the spring “En-rogel” at 2 Samuel 17:17 but “the spring of Rogel” at 1 Kings 1:9. It calls the Kidron “the torrent Kidron” at 2 Samuel 15:23 but “the Kidron stream” at 1 Kings 2:37.
- Data: the column uses straight apostrophes (king's) throughout this chunk. None of my changes adds an apostrophe. The LOCKED rows 1 Kings 2:35a–o and 2:46a–l are empty placeholders, with no source and no English.

## 1 Kings 4–15

# latin-016 notes (1 Kings 4–15, Clementine Vulgate)

## Data problems
- Some cards appear on two rows but neither row is LOCKED, so an edit to one would silently show on the other: vg-1-kings-5-17 (5:31 and 6:1a), vg-1-kings-5-18 (5:32 and 6:1b), vg-1-kings-9-16 (5:14b and 9:16), vg-1-kings-4-21 (5:1 and 10:26a), vg-1-kings-9-15 / 9-20 / 9-22 (9:15/9:20/9:22 and 10:22a–c), vg-1-kings-11-26 / 11-29 / 11-40 (11:26/11:29/11:40 and 12:24b/o/c), vg-1-kings-14-1 to 14-6, 14-10, 14-17 (14:1–6/10/17 and 12:24g–n). None of these were changed. The lock rule should probably cover them too.
- Rows follow the Greek (Saints) order, so Vulgate 1 Kings 7:2–13 (the House of the Forest of Lebanon) appears at 7:39–49, and 7:2 (Vulgate 7:14) begins mid-sentence (“the son of a widow…”) without Hiram’s introduction from Vulgate 7:13. Nothing here contains Vulgate 7:13. Check that the 7:13 card appears somewhere on the page.
- 4:17–4:19 rows carry Vulgate 4:18, 4:19, 4:17 (reordered). That is expected, but it means Jehoshaphat of Issachar is listed last.

## For an editor (not changed)
- 14:15 “The Lord God will strike Israel”: in Latin, *percutiet Dominus Deus Israël* can also mean “the Lord, the God of Israel, shall strike” (Douay). The current reading follows the Hebrew object and is defensible.
- 12:18 has “Adoram” (Vulgate Aduram), while 4:6 and 5:28 have “Adoniram”. Both match the Latin, but an editor may want a note for listeners.
- 15:13 “He demolished her grotto”: *specum ejus* could refer to Priapus (“its/his cave”) as easily as Maacah. Douay has “her den”, so it was left alone.
- 6:30 “in both the inner and outer rooms”: the Latin only says *intrinsecus et extrinsecus* (inside and out). This is an interpretation but harmless.

## 1 Kings 16–22; 2 Kings 1–8

# latin-017 notes (1 Kings 16–22; 2 Kings 1–8)

Verses for a specialist or an editorial decision (not changed):

- 1 Kings 16:7: the English says “Baasha killed him”, but the Latin (*occidit eum, hoc est, Jehu*) leaves the subject unstated, and Jehu son of Hanani turns up alive again in 2 Chronicles 19:2. Supplying “Baasha” is an interpretation, so someone should decide whether to keep the plain “he”.
- 1 Kings 16:26: *in vanitatibus suis* comes after a singular subject (Omri), which would give “his vanities”. The English has “their vanities”, as in Douay and the Hebrew. Left as it is.
- 2 Kings 5:19: *electo terrae tempore* (Douay has “in the springtime of the earth”) is rendered “at a favorable season for the land”. This is accurate but obscure when read aloud. Consider “in the springtime”.
- 2 Kings 6:27: *Non te salvat Dominus* is rendered literally (“The Lord does not save you.”), while Douay reads it as a condition (“If the Lord doth not save thee…”). Left literal.
- 2 Kings 8:11: “He stood with him, and he grew troubled…”: two unnamed “he”s. The Latin doesn’t name the subject either, so it was left alone.

Column consistency (editorial):

- The two books use different formulas. 1 Kings has “The Lord says:” and “book of the annals of the kings of Israel/Judah”. 2 Kings has “Thus says the Lord:” and “Book of the Chronicles of the Kings of Israel/Judah”. The capitals also differ: “City of David” in 2 Kings 8:24 against “city of his father David” in 1 Kings 22:51.
- The EN throughout the chunk uses straight apostrophes (’ is house style). They were left alone, and none of the changed text contains an apostrophe.

Data:

- 2 Kings 8:11 SRC reads “Stetique”, which is probably a typo for “Stetitque”.
- 1 Kings 20/21 rows carry the Vulgate’s swapped chapter numbers (vg-1-kings-21-* under 1 Kings 20, and the reverse). This is consistent and fine.
- 1 Kings 16:28a–h and 2 Kings 1:18a–d are empty LOCKED rows.

## 2 Kings 9–24

# latin-018 (2 Kings 9–24) notes

- Data: 2 Kings 15:28 (vg-2-kings-15-28) carries `[vulgate_reference: 15:24]`, and 2 Kings 23:37 (vg-2-kings-23-37) carries `[vulgate_reference: 23:32]`. Both verses repeat the wording of the earlier verse, so the tag looks like a copy or matching error. Please check the mapping.
- Data: 2 Kings 15:5 SRC reads “judicabit” (future). Standard Clementine editions read “judicabat”, which would mean “judged”. The EN “was to judge” follows the typo. Fix the source text, then change the EN to “and judged the people of the land”.
- Editorial: 2 Kings 19:25 “eruntque in ruinam collium pugnantium civitates munitae”. The Vulgate image is something like “the fortified cities will become like the ruin of hills fighting together” (Douay). The EN “fortified cities of fighting men will become ruined heaps” attaches “fighting” to men and drops the hills. I left it as the 9 November reading; a specialist should decide.
- Editorial: 2 Kings 23:33 “mulctam” is a fine or penalty, but the EN says “tribute”. I left it unchanged because the difference is small.
- Style: this chunk’s EN uses a straight apostrophe (') throughout (Lord's, Ahab's). None of my changes adds an apostrophe, so nothing is mixed. A global curly-apostrophe sweep would be a separate decision.

## 2 Kings 25–25; 1 Chronicles 1–11

# latin-019 notes (2 Kings 25; 1 Chronicles 1–11)

No changes made: I checked every editable row against the Clementine, and all numbers, name lists and clauses match. The open points below need an editorial decision or a data fix.

## Data problems
- **1 Chronicles 11:35 (card vg-1-chronicles-11-34)**: SRC is only “Ahiam filius Sachar Ararites,” but EN also has “Eliphal son of Ur;”, which is Vulgate 11:35 (“Eliphal filius Ur”). There is no vg-1-chronicles-11-35 card, so that text has been merged into this one. I left it unchanged so the line is not lost from the site. The card mapping needs fixing (Vulgate chapter-split work).
- **1 Chronicles 9:40 (card vg-1-chronicles-9-40)**: this row has `vulgate_reference: 8:34`. The wording is identical to Vulgate 9:40, so there is no visible effect, but the mapping looks wrong.
- **LOCKED shared cards**: 11:32/11:33 and 11:46/11:47 each show the same Vulgate verse twice on the site. This is expected from the Vulgate's verse merges and was not touched.
- **1 Chronicles 1:11–16 and 1:18–23 have no rows.** That is correct: the Clementine omits these verses.

## For a specialist / editorial decision
- **1 Chronicles 2:23**: “Cepitque Gessur et Aram oppida Jair” can be read two ways. EN follows the Hebrew-style reading (“Geshur and Aram took Jair’s towns”). Douay reads Jair as the subject: “he took Geshur and Aram, the towns of Jair.” The singular *cepit* slightly favours Douay. Needs a decision on which reading the column follows.
- **1 Chronicles 9:17–18**: in the Latin, “Sellum princeps, usque ad illud tempus…” runs on across the verse break. EN ends 9:17 with a full stop and starts 9:18 with “Until that time they kept watch…”. It is acceptable, but Douay keeps it as one sentence.
- **1 Chronicles 11:25**: *posuit eum David ad auriculam suam* (“at his ear”) is rendered “his confidential adviser”. The sense is right but the image is lost. Not changed because it would be unclear aloud.
- **1 Chronicles 10:9**: “They sent it to their own land” follows “removed his armor”, so “it” could be heard as the armour. The Latin leaves the subject unstated (most likely the head). Left as is.
- **1 Chronicles 6:54 (Vg 6:69)**: Latin *Helon* is rendered “Aijalon” (Hebrew form), while *Helon* in 6:43 is “Hilen”. This is a column naming choice and was not changed.

## 1 Chronicles 12–29; 2 Chronicles 1–1

# latin-020 notes (1 Chronicles 12–29; 2 Chronicles 1, Clementine Vulgate)

## Data problems
- 1 Chronicles 16:24 is missing from the input (rows jump from 16:23 to 16:25). Check that the card exists on the page.
- 16:8 SRC begins with “[” and 16:36 has “]” (Clementine bracket marking the psalm). The EN is fine; just a source-display quirk.
- 12:4/12:5 and 20:7/20:8 share cards (both LOCKED), so 12:5 and 20:8 show duplicated text.
- 2 Chronicles 1:18 carries Vulgate 2:1 (Greek numbering), as expected.

## For an editor (not changed)
- 20:5 “God-given, son of the Forest, the Bethlehemite”: Jerome translated the names (Adeodatus filius Saltus). Rendering them as English words is confusing aloud; Douay keeps “Adeodatus the son of Saltus”. Probably from the 9 Nov revision, so not reverted.
- 13:11 “the Lord had broken Uzzah … the Breach of Uzzah”: the Latin is *divisisset … Divisio Ozæ* (divided / Division). “Broken/Breach” follows the Hebrew perez. Defensible, but not literal Vulgate.
- 26:6 Latin has *Semei* (Shimei); the column writes “Shemaiah” to match 26:4/26:7. 27:27 Latin *Semeias* is written “Shimei”. Both harmonise toward the Hebrew; an editor may want a consistent policy.
- 26:7 “his brothers, Elihu and Semachiah, were also very mighty men”: the Latin punctuation (*Elzabad, fratres ejus viri fortissimi: Eliu quoque et Samachias*) is ambiguous; the current reading is one defensible parse.
- 19:18 “seven thousand Syrian chariot crews”: Latin says simply *septem millia curruum* (chariots). Interpretive but sensible.

## 2 Chronicles 2–24

# latin-021 notes (2 Chronicles 2–24, Clementine)

## For a specialist or editorial decision (not changed)
- 2 Chr 21:19: “lost both his illness and his life” renders the Vulgate literally (languore pariter, et vita caruit). It is accurate but may sound odd read aloud; keep or smooth?
- 2 Chr 24:13: “the breaches in the walls were repaired” drops the Latin image obducebatur parietum cicatrix (“the scar of the walls was closed over”). Could be restored if the column wants to keep the Vulgate’s image.
- 2 Chr 7:6: ante eos is rendered “opposite them” (the Hebrew negdam); “before them” would be closer to the Latin. Minor, left as is.
- 2 Chr 12:7: non stillabit furor meus is rendered “will not pour”; stillare is “drip, distil”. Left as is.
- 2 Chr 20:37: the closing quote comes after “struck your works”, so the shipwreck is narration. The Latin allows either reading.

## Data
- Row numbering is shifted against the Vulgate cards: 2:1–2:17 map to vg 2:2–2:18, and 13:23 and 14:1–14:14 map to vg 14:1–14:15, as the vulgate_reference tags show. Vulgate 2:1 is not in this chunk; check that it is in latin-020.
- Apostrophes are mixed: the chunk uses straight ' throughout, except 24:20 (“Lord’s”). New text in my changes uses ’.
- 2 Chr 2:16 writes “153,600” in figures, while the rest of the chunk spells numbers out.

## 2 Chronicles 25–36; Ezra 1–6

# latin-022 notes (2 Chronicles 25–36; Ezra 1–6)

- Data: 2 Chronicles 27:8 is missing from the input (rows jump 27:7 → 27:9). The Clementine has it (“Viginti quinque annorum erat cum regnare cœpisset, et sedecim annis regnavit in Jerusalem”; Douay 27:8), so the card may be missing on the site.
- Data: 2 Chronicles 35:19a–d, 36:2a–c, 36:4a, 36:5a–d are LXX-numbered rows that repeat the plain Vulgate verse (locked, shared card); nothing changed.
- Style: this chunk mostly uses straight apostrophes (Lord's) with an odd curly one (31:15 “priests’ cities”); left as is apart from edited text.
- Editorial: 2 Chronicles 28:20 “He brought against him Tiglath-pileser”: the Latin subject of adduxit could be the Lord (carrying on from 28:19 Humiliaverat Dominus); left ambiguous as in Douay.
- Editorial: 2 Chronicles 31:16 “except for males three years old and above” renders exceptis literally; the sense (in addition to / apart from the genealogical list) is debated, worth a specialist look.
- Editorial: 2 Chronicles 31:13 “Under them” for post quem (“after him”, i.e. next in rank after Shimei); left.

## Ezra 7–10; Nehemiah 1–12

# latin-023 notes (Ezra 7–10; Nehemiah 1–12)

## Data problems
- Missing rows (no row in the input for these Clementine verses, though the Vulgate has them): Nehemiah 3:7; Vulgate 4:6 (= Hebrew 3:38, “Itaque ædificavimus murum…”), between Nehemiah 3:37 (vg 4:5) and 4:1 (vg 4:7); Nehemiah 11:16, 11:20–21, 11:28–29, 11:32–35; Nehemiah 12:4–6. Check whether the cards are absent on the site or just left out of the export.
- Nehemiah 3:30/3:31 and 12:33/12:34 each share one card (locked). The 3:31 row repeats the whole of vg 3:30, so Hebrew 3:31 is shown twice.

## For an editor (not changed)
- Nehemiah 3:8 “They left Jerusalem as far as the wall of the broader street”: this follows dimiserunt literally, but read aloud it sounds like the builders went away from the city. Commentators read it as “left [that stretch] as it was”. Consider a gloss such as “left Jerusalem as it was, as far as…”.
- Ezra 7:26: diligenter could go with fecerit (“does not diligently observe”) or with the judgment. The English takes the second reading, which matches the Aramaic. Left as it is.
- Ezra 8:5 “a son of Ezekiel” for filius Ezechiel: the Vulgate leaves out the leader’s name (Hebrew: Shecaniah son of Jahaziel). The English is acceptable as it stands.
- Ezra 7:6 scriba velox is rendered “skilled scribe” (Douay has “ready scribe”). Left as it is.
- Style: the column uses straight apostrophes (Lord's, God's) all through this chunk. None of my changes add an apostrophe.

## Nehemiah 13–13; Esther 1–10; Job 1–8

# latin-024 notes (Nehemiah 13; Esther 1–10; Job 1–8)

Data problems
- Esther 4:6, 9:5 and 9:30 have no row in the input, though the Clementine has these verses (4:6 Hathach goes out to Mordecai; 9:5 the Jews strike their enemies; 9:30 letters sent to the 127 provinces). Check whether the Latin column is missing these cards or the export skipped them.
- All the Greek additions (Esther 1:1a–r, 3:13a–g, 4:17a–z, 5:1–2b, 8:12a–x, 10:3a–k) and Job 2:9–9e are LOCKED as shared cards, so they were not reviewed. Each 1:1x row repeats the whole 11:2–12:6 block with the same 11:2 Latin.
- The Latin of Job 3–8 still has the editorial square brackets ([ … ]). The English correctly leaves them out.

For a specialist / editorial decision (not changed)
- Job 5:24: “when you inspect your property, you shall not go wrong” follows the Hebrew (navekha / lo techeta). The Vulgate has visitans speciem tuam, non peccabis (“visiting your beauty, you shall not sin”). Changing it means deciding how to render species.
- Esther 4:13: “you alone will save your life” is closer to the Hebrew. The Vulgate (animam tuam tantum liberes) stresses saving only her own life. This is acceptable as it stands, but worth a look.
- Esther 3:8: novis utens legibus is rendered “strange laws”. Douay has “new laws”. It is probably a deliberate choice, so I left it.
- Esther 2:12: in “the twelfth month was coming to its close”, mensis duodecimus means the twelfth month of the preparation. Listeners may hear it as the calendar month (Adar). It is ambiguous in the Latin too.
- Job 7:4: Si dormiero (“If I sleep”) is rendered “If I lie down”, after the Hebrew. The difference is small, so I left it.

## Job 9–28

# latin-025 (Job 9–28) · notes

## Data problems
- Job 16:4 (vg-job-16-4): the English also holds Vulgate 16:5 (“I too would comfort you with speeches and shake my head over you”), which has no row of its own; the next row (16:5) carries vg-job-16-6 / Vulgate 16:6. Rows from here to the end of the chapter are offset by one. Left unchanged; needs a data fix (a separate 16:5 card).
- Job 23:14 has no row: the chunk goes from 23:13 to 23:15, and 23:15 appears twice (23:15 and 23:15a, both on card vg-job-23-15, LOCKED). Vulgate 23:14 (“Cum expleverit in me voluntatem suam…”) seems to have no English on the site.
- Job 19:4 also appears twice (19:4 and 19:4a, same card vg-job-19-4, LOCKED). Probably a leftover from renumbering.

## For a specialist / editorial decision (not changed)
- Job 20:26 “affligetur relictus in tabernaculo suo”: the row reads “whoever remains in his tent shall be afflicted”; Douay takes it as “he shall be afflicted when left in his tent”. The Latin allows either.
- Job 27:22 “Et mittet super eum… de manu ejus fugiens fugiet”: “hurl itself” and “from its power” are free renderings (the Latin has no reflexive, and it says “from its hand”). Acceptable, but could be made more literal.
- Job 15:3 “eum qui non est æqualis tibi” is printed as “One” (God). This follows Gregory’s reading, but the Latin itself is ambiguous.

## Job 29–42; Psalms 1–7

# latin-026 notes (Job 29–42; Psalms 1–7)

## Data problems
- Psalms 2:12 (psalms-unit-18): EN also carries Vulgate 2:13 (“When His anger quickly blazes up, blessed are all who trust in Him”), which is not in the row’s SRC; there is no 2:13 row in this chunk. Not moved (brief forbids moving content between rows).
- Psalms 4:9 (psalms-unit-34): EN also carries Vulgate 4:10 (“for You, Lord, have established me uniquely in hope”), not in the row’s SRC. Not moved.
- Locked shared-card rows (Job 36:28/28a/28b, Job 42:16–17e, Ps 3:7–8, 4:7–8, 5:4–5) repeat one Vulgate verse across several Greek-numbered rows; their EN merges two Vulgate verses (e.g. Ps 3:7–8, 4:7–8, 5:4–5). Left as is.
- The column’s existing Job text uses straight apostrophes (e.g. “widow's”, “Job's”); none of the changes touch them.

## For a specialist / editorial decision (not changed)
- Job 30:8 “in terra penitus non parentes”: EN “altogether without standing in the land” interprets parentes (from pareo, “appearing”); Douay has “not appearing at all upon the earth”.
- Job 31:34: EN turns the last clause (“et non magis tacui, nec egressus sum ostium”) into a rhetorical question; the Latin is still inside the si-series. Defensible, but worth a look.
- Job 32:13 “Ne forte dicatis”: EN “Do not say” makes it an imperative; “lest perhaps you say” would keep the Latin purpose clause. Left as taste.
- Job 40:19 “applicabit gladium ejus”: EN “will bring His sword against it” decides that ejus is the Maker’s; the Latin may mean Behemoth’s own sword (Gregory’s reading). Ambiguous.
- Psalms 3:6 “Ego dormivi, et soporatus sum”: EN “I lay down and slept” follows the Hebrew; the Latin is “I slept and fell into deep sleep”. Small enough to leave.
- Psalms 4:9 “in idipsum” rendered “together”; the Latin tradition (Augustine) reads “in the selfsame”. Editorial call.

## Psalms 8–36

# latin-027 notes (Psalms 8–36, Vulgate numbering)

## Data problems
- Psalms 10:1 (psalms-unit-123): EN also carries Vulgate 10:2 (“In the Lord I trust… like a sparrow”), but SRC shows only the title “In finem. Psalmus David.”; the following row is tagged vulgate_reference 10:3, so Vulgate 10:2 has no row of its own. Left as is.
- Psalms 12:3 (psalms-unit-140): EN includes “How long will my enemy be exalted above me?” (Clementine 12:2b, “usquequo exaltabitur inimicus meus super me?”), but SRC is truncated and lacks it. EN is right; the SRC text needs fixing.
- Psalms 19:1 and 20:1 (title rows) carry vulgate_reference 18:1 and 19:1, which looks like a mis-tag (the titles are 19:1 and 20:1 in the Vulgate).
- Mixed apostrophes in the column (“name’s” in 22:3 vs “name's” elsewhere); not changed on its own.

## For a specialist / editorial decision (not changed)
- Psalms 11:7 “tested for the earth” (probatum terrae): opaque aloud; Douay has “purged from the earth”, and commentators differ (purified of earthy dross vs tested on earth). Needs a decision.
- Psalms 18:6–7: “ipse tamquam sponsus” is lower-cased (“he”, the sun); patristic reading takes the bridegroom as Christ, which would favour “He”. Column’s choice kept.
- Psalms 20:9–13: lower-case “you/your” treats these verses as addressed to the king (God is “the Lord” in 20:10); a defensible reading, but should be checked for consistency with the Hebrew column.
- Psalms 30:12 “More than all my enemies I have become a reproach” (super omnes inimicos meos): could also be “among/because of all my enemies”; kept.
- Psalms 9:18 “return to the underworld” (convertantur in infernum): Douay “be turned into hell”; “return” is defensible but may read oddly.

## Psalms 37–67

# latin-028 (Psalms 37–67, Clementine) · notes

## For a specialist / editorial decision (not changed)

- **Ps 54:21–22**: the EN reads “He has stretched out His hand … the anger of His face, and his heart has drawn near. His words have become softer than oil.” Capitalised He/His makes God the one whose words are “softer than oil, yet javelins”, but “his heart” is lower case in the same verse. Augustine reads it of God/Christ; Douay leaves all lower case. Please make the capitals consistent one way or the other.
- **Ps 58:12**: “God will show me over my enemies” (Deus ostendet mihi super inimicos meos) is hard to follow aloud. Douay has “God shall let me see over my enemies.” A clearer rendering would need an editorial choice, so I left it.
- **Ps 43:19**: “and You have turned our paths aside from Your way” renders the Latin positive *et declinasti* literally. Douay supplies a negative (“neither hast thou turned aside”) from the Hebrew. Both readings are defensible, so I kept the literal one.
- **Ps 67:13–14** (Rex virtutum dilecti, dilecti; pennae columbae deargentatae): the obscure Vulgate is rendered nominally and literally. That is acceptable, but a specialist may want to look at it.
- **Ps 48:15**: *mors depascet eos* is rendered “death will pasture them” (the shepherd image). “Death will feed on them” (Douay) is the other way to read *depascere*. I left it.

## Data problems

- Shared-card LOCKED pairs repeat the first verse’s SRC on the second row, so the SRC for the second verse is missing: 43:22/23, 48:10/11, 52:1/2, 55:11/12, 58:4/5, 59:6/7, 61:12/13, 63:5/6. In several of these (48:10, 58:4, 59:6, 61:12, 63:5) the EN covers two Latin verses but the SRC shows only the first. Rows after these splits carry vulgate_reference offsets (e.g. 43:24 = Vg 43:23, 55:13 = Vg 55:12).
- Row 40:1 is tagged vulgate_reference 39:1, 42:5 is tagged 41:12, 45:12 is tagged 45:8, 58:15 is tagged 58:7, 54:1 is tagged 53:1 and 66:6 is tagged 66:4. Each of these has the same text as the row it points to, but the tags look like a dedupe artefact. Please check the numbering.
- The EN column uses straight apostrophes throughout this span (“Lord's”, “enemies'”, “king's”), against the house style of ’. I did not touch them, apart from the one row I rewrote (44:14).

## Psalms 68–90

# latin-029 notes (Psalms 68–90, Vulgate numbering)

Editorial questions (not changed):
- Ps 72:4 “et firmamentum in plaga eorum”: rendered positively (“there is strength in their affliction”); Douay carries the negative over (“nor is there strength in their stripes”). Both defensible; worth a specialist's decision.
- Ps 77:69 “sicut unicornium sanctificium suum”: “like the one-horned beasts” can sound as if the sanctuary resembles the beasts (Douay “as of unicorns”). Consider “like that of the one-horned beasts”.
- Ps 86:5 “Numquid Sion dicet”: column has “Will Zion say…?”; Douay reads “Shall not Sion say”. Question of how to take numquid here; left as the 9 November revision has it.
- Ps 86:4 “scientium me … who know Me”: capitalised Me makes God the speaker; fine if intended, but the psalmist reading is also traditional.
- Ps 70:17 “until now I will proclaim” is literal (usque nunc pronuntiabo) but sounds odd aloud; left.
- Ps 70:20 “How many great and evil distresses” compresses “tribulationes multas et malas”; acceptable, left.

Data:
- Locked shared-card rows (71:1/2, 73:5/6, 83:12/13, 89:5/6, 90:4/5) carry merged English for two Vulgate verses each, while SRC shows only the first verse; not touched.
- Title wording varies slightly: “For understanding, of Asaph.” (73:1) vs “For understanding. Of Asaph.” (77:1); left.
- Apostrophes in this column are straight (') throughout the chunk; no new apostrophes were introduced.

## Psalms 91–117

# latin-030 (Psalms 91–117, Vulgate numbering) · notes

## Data problems
- Psalms 108:16 / 108:17: the 108:16 EN also contains the content of Vulgate 108:17 (“but persecuted the needy and destitute person … to put him to death”), while the 108:17 row (LOCKED, vulgate_reference 108:18) shows 108:18’s Latin and English. The 108:17 Latin (“et persecutus est hominem inopem et mendicum…”) has no row of its own. Not changed; needs a row/card fix.
- Psalms 115:5 (psalms-unit-1959, Vulgate 115:14 “Vota mea Domino reddam…”) is missing from the input; 115:1–10 carry vulgate_reference 115:10–19.
- Locked shared-card rows (94:8/9, 99:1/2, 108:1/2, 110:6/7, 113:9/10) show one combined EN for two rows; the SRC shown is only the first part of the verse.

## For a specialist or editorial decision (not changed)
- Psalms 109:1: “The Lord said to my lord” (lowercase “lord”, “your”) for Domino meo; the Latin column may want “my Lord” given Christian reading of this psalm. Editorial call.
- Psalms 109:6: “fill them with ruins” adds “them” (Latin implebit ruinas, “He will fill ruins”; Augustine reads “fill up the ruins”). Consider “He will fill up ruins”.
- Psalms 108:24: “my flesh has changed because of oil” is literal for propter oleum, but listeners may miss the usual sense “for lack of oil” (Challoner).
- Psalms 105:13: “They acted quickly: they forgot His works” is literal for Cito fecerunt; obliti sunt, but the sense is “they were quick to forget.”
- Psalms 96:1: “For this David” (Huic David) is odd aloud; Douay has “For the same David.”
- Psalms 91:4: “on the ten-stringed harp” merges decachordo and psalterio; acceptable as apposition.

## Psalms 118–148

# latin-031 notes (Psalms 118–148, Vulgate numbering)

## Data problems
- Psalms 129:6 (psalms-unit-2241, vulgate_reference 129:5): SRC is only “speravit anima mea in Domino.”, but EN also carries Vulgate 129:6 (“A custodia matutina usque ad noctem, speret Israel in Domino”). The Latin for that half is missing from SRC; English left as is.
- Psalms 123:4/123:5 (unit-2203), 129:4/129:5 (unit-2240), 145:2/145:3 (unit-2440), 148:12/148:13 (unit-2479), 144:13/144:13a (unit-2430): locked shared cards whose EN covers more Latin than the SRC shown (e.g. 145:2 EN has “in the children of men, in whom there is no salvation”, 148:12 EN has “for His name alone has been exalted”, 123:4 EN has Vulgate 123:5). Not touched.
- Psalms 147:1–9 carry vulgate_reference 147:12–20. In the Clementine, Ps 147 is numbered 1–9 (it is Hebrew 147:12–20), so the label looks like the Hebrew reference, not the Vulgate one.
- Psalms 124:1/124:2: the row break falls mid-clause (“who dwells / in Jerusalem”), following the source split. English mirrors it; fine but odd aloud.

## For a specialist / editorial decision (not changed)
- 135:15 “shook Pharaoh and his army into the Red Sea”: Latin has in mari Rubro (ablative, “in the Red Sea”); “into” follows the Hebrew. Acceptable, but an editor may prefer “in”.
- 131:17 “a horn for David”: cornu David can be “the horn of David” (Douay); current reading follows the Hebrew l-David.
- 118:138 “in righteousness and in the abundance of Your truth” smooths the difficult Mandasti justitiam testimonia tua, et veritatem tuam nimis; kept.
- 140:10 “its net” for retiaculo ejus (Douay “his net”); referent unclear in the Latin.

## Psalms 149–150; Proverbs 1–15

# latin-032 notes (Psalms 149–150; Proverbs 1–15)

Data problems
- Clementine verses with no row in the input (so missing from the column, or merged somewhere upstream): Proverbs 4:7 (“Principium sapientiae, posside sapientiam…”), 8:33 (“Audite disciplinam, et estote sapientes…”), 11:4 (“Non proderunt divitiae in die ultionis…”), 15:31 (“Auris quae audit increpationes vitae…”). Worth checking that the site shows them.
- Proverbs 15:27a/28a/29a/29b carry Vulgate 16:6–9 under the Greek numbering; the renderings match their Latin, but check this is the placement you want.

Possible editorial decisions (not changed)
- Proverbs 14:26 “there will be hope for His children”: filiis ejus could mean the God-fearer’s children (the Hebrew sense, Rashi) rather than God’s; the capital “His” commits to one reading.
- Proverbs 6:26: Douay takes viri with animam (“the woman catches the precious soul of a man”); the column reads mulier viri as “another man’s wife” (the Hebrew sense). Both defensible.
- Proverbs 10:23 and 14:24 reverse the Latin subject and predicate (“prudence is wisdom” for sapientia … est prudentia; “The riches of the wise are their crown” for Corona sapientium divitiae eorum). Left as the column’s habit; Douay keeps the Latin order.
- Proverbs 7:27 “Her house is the ways to the underworld” is literal (Viae inferi domus ejus) but slightly awkward aloud.
- Proverbs 9:10 “knowledge of holy things”: scientia sanctorum may equally be “of the holy ones/saints”.

## Proverbs 16–31; Ecclesiastes 1–1

# latin-033 notes (Proverbs 16–31; Ecclesiastes 1)

## For a specialist / editorial decision (not changed)
- Proverbs 16:2 — "patent oculis ejus": non-reflexive ejus most naturally means the Lord's eyes (Douay leaves "his"); EN "his eyes" reads as the person's own eyes. Decide whether to capitalise "His" (follows column convention for God).
- Proverbs 29:10 — "justi autem quærunt animam ejus": in Vulgate idiom "quærere animam" usually means seeking to kill (cf. Mt 2:20), but here the just are the subject; EN "the just seek his life" sounds hostile in English. Consider "seek his soul" (Douay) or a note.
- Proverbs 22:8 — "virga iræ suæ consummabitur" can be read with ablative ("by the rod of his anger he will be consumed", Douay); EN takes virga as subject. Both defensible.
- Proverbs 25:20 — "cordi pessimo" rendered "a most troubled heart" (Hebrew sense); 26:23 renders "pessimo corde" as "a most evil heart". Check consistency.
- Proverbs 28:17 — "animæ sanguinem" as "a life's blood" is awkward aloud; possible spoken fix if wanted.
- Ecclesiastes 1:2 — "Futility of futilities" for vanitas vanitatum (presumably the 9 Nov choice); traditional "vanity" may be preferred for a Vulgate column.

## Data
- Rows follow Greek order: many Vulgate verses absent from this chunk (e.g. Prov 16:1, 3–4, 6–8; 19:1–2; 20:14–22 except 20:20–22 shown as 20:9a–c; 21:5; 22:6; 23:23) — presumably handled elsewhere or not mapped.
- Prov 16:9 carries Vulgate 16:4; Prov 31:25/31:26 carry Vulgate 31:26/31:25 (swapped); EN matches SRC in each.
- SRC text contains stray "[" and "]" bracket marks (source editorial brackets), not in EN; harmless.
- Changed rows' "after" uses curly apostrophe (house style) while the column's existing text uses straight apostrophes.

## Ecclesiastes 2–12; Song of Songs 1–8; Wisdom of Solomon 1–7

# latin-034 notes (Ecclesiastes 2–12; Song of Songs 1–8; Wisdom 1–7)

## For a specialist or editorial decision (not changed)
- Ecclesiastes 8:2 — “I observe the king’s command” interprets *os regis* (“the mouth of the king”, Douay); keep the image or leave the gloss?
- Ecclesiastes 10:11 — “no better than it” is a fair reading of *nihil eo minus habet*; some editors prefer “no less harmful”.
- Song of Songs 3:3 — the bride’s question “Have you seen the one my soul loves?” has no quotation marks, so aloud it can sound like the watchmen asking. Column elsewhere (e.g. 7:9 “I said: I will climb…”) also leaves speech unquoted, so this is a column-wide style choice.
- Wisdom 3:14 — “So too will the eunuch who…” is an ellipsis (“will have fruit”, from 3:13) held over a long relative clause; fine on the page, slightly hard aloud.
- Wisdom 7:22–23 — *certus* appears in both verses but is rendered “sure” then “certain” (*subtilis* is “subtle” both times). Probably harmless; flag in case the column wants the list repetition kept.

## Data problems
- Song of Songs 1:1 has no source or English (LOCKED).
- Song of Songs 7:1 and 7:2 share card song-of-songs-unit-90, with the SRC showing only Vulgate 6:12 while the EN covers 6:12 plus the Shulammite dialogue and 7:1 (steps, thighs). The Latin for “What will you see in the Shulammite…” and “How beautiful are your steps…” is not shown in either row.
- Apostrophes are mixed in this column: Ecclesiastes and Song use straight ', Wisdom mixes ' and ’ (e.g. 2:3 “sun’s” vs 2:22 “God's”). Left as is; changed verses keep their existing straight apostrophes.
- Several SRC lines carry stray pericope brackets ([ and ]) from the source text (e.g. Eccl 2:11, 2:12); harmless, not in the English.

## Wisdom of Solomon 8–19; Sirach 1–8

# latin-035 · Wisdom 8–19, Sirach 1–8 · notes

## For a specialist (not changed)

- Wisdom 17:13 — *impotentem vere noctem* is rendered “a truly overpowering night”; *impotens* (Greek ἀδύνατον) more likely means “powerless” (Douay “without power”), which would reverse the adjective. Needs a decision.
- Wisdom 17:14 — “fainting from their souls’ exposure” for *animae deficiebant traductione* is hard to follow aloud; the sense is the soul betraying or failing them (Douay “their soul betraying them”).
- Wisdom 12:5 — the dashes and “from the midst of Your sacred mystery” (*a medio sacramento tuo*) make 12:3–6 hard to follow; the Latin itself is obscure.
- Wisdom 12:13 — “to whom You must show” follows the Greek sense; the Latin *ut ostendas* is more naturally “so that You may show”.
- Wisdom 12:24 — *diutius erraverunt* is rendered “wandered far”; the Latin is temporal (“for a long time / too long”).
- Wisdom 16:9 — *sanitas animae illorum* “healing for their souls”; *anima* here is probably “life”.
- Wisdom 11:7 and 18:5 — this pass rendered *traductio* as “rebuke” in both; 17:14 (above) uses the same noun and should be decided with them.

## Data

- Many Sirach SRC fields carry an appended “· Translation note. …” inside the Latin (1:8, 1:9, 1:14, 2:18, 3:14, 4:17, 4:22, 5:3, 5:5, 6:12, 6:22, 7:18, 7:23, 7:31). They should live outside the source field.
- Sirach 5:5 SRC reads *propitiatio peccato*; the Clementine has *propitiato peccato* (transcription slip; English already follows the correct reading).
- Sirach 1:15 is a placeholder row (“No aligned Latin source passage” / “No corresponding passage is supplied…”); 6:35 is a locked placeholder.
- Rows follow Greek numbering, so several Vulgate-only verses have no row (e.g. Vulg. Sir 1:5, 1:24, 1:32, 1:35, 2:21–23, 3:10, 4:19, 4:21, 5:7). Visible effects: Sir 2:18 opens a quotation that never closes; Sir 3:8 ends with a comma before an unrelated verse; Sir 5:6 closes a quote the Latin continues.
- Duplicate cards: Wisdom 19:13/19:14 (vg-wisdom-of-solomon-19-13) and 19:21/19:22 (vg-wisdom-of-solomon-19-20) repeat the same verse.
- Stray pericope brackets “[” / “]” appear at the start/end of many SRC lines (harmless, English unaffected).

## Sirach 9–26

# latin-036 (Sirach 9–26) notes

## For a specialist / editorial decision (not changed)
- Sirach 22:5 — *ab impiis non minorabitur*: the column reads “will not be held in less regard by the ungodly” (ab = agent); Douay takes it comparatively (“will not be inferior to the ungodly”), which fits the sense better. Worth a Latin review.
- Sirach 17:22 — *quasi signaculum cum ipso*: English capitalises “with Him” (God); the Latin could also mean “with him” (the almsgiver). Editorial call.
- Sirach 19:13–14 — “lest he perhaps has not understood and says …” / “lest perhaps he did not say it” keep the Douay-style *ne forte* and sound odd aloud; left alone, but they could be smoothed if the column wants that.
- Sirach 20:9 — *processio in malis* rendered “progress amid troubles”; Douay has “success in evil things”. Both are defensible.

## Data problems (Vulgate verses with no row, so the English dangles)
- 11:19 ends with a comma; Vulgate 11:20 (*et non scit quod tempus praeteriet…*) is missing, so the sentence never finishes. (Vulgate 11:15–16 and 11:23 are also absent.)
- 16:17 opens a quotation (“I will hide from God; …?) that is never closed; Vulgate 16:17 (*in populo magno non agnoscar…*) is missing.
- 17:17 ends with a comma; Vulgate 17:15 (*et pars Dei Israel facta est manifesta*) is missing.
- 22:18 ends with a comma; the “so also a timid heart…” clause (Vulgate 22:22–23) is missing.
- 23:14 ends with a comma; Vulgate 23:19 is missing. 23:18 opens “Who sees me? with no closing quote; Vulgate 23:26 is missing.
- 24:6 ends “and among every people” and 24:7 starts “With power I trod…”; Vulgate 24:10 (*et in omni gente primatum habui*) is missing, so the two rows run together wrongly aloud.
- 22:17 is a placeholder row (“No aligned Latin source passage”) and is not marked LOCKED.
- Apostrophes are mostly straight (') in this chunk, but 23:19 and 25:22 use the curly ’.

## Sirach 27–43

# latin-037 (Sirach 27–43) notes

- Data: many SRC lines carry stray `[` / `]` brackets at section edges (e.g. 27:3, 27:22, 28:12–13); they are in the Latin only, not the English.
- Data: several Vulgate verses have no row of their own (e.g. Vulgate 27:19, 27:24, 28:7, 28:9, 29:8–9, 30:20, 31:13, 33:13b); check the alignment is intentional.
- Data: 29:13 SRC/EN hold only “Super scutum potentis” (“More than the shield of a mighty man”); the rest of Vulgate 29:16 (“et super lanceam … pugnabit”) is missing.
- Data: 33:13 SRC/EN give only the first clause of Vulgate 33:13; “omnes viæ ejus … secundum judicium suum” is missing.
- 41:20: the translation note says “before God’s truth and covenant”, but the EN says “of God’s truth and covenant”; the two should match. Also “of reclining upon the bread” (de discubitu in panibus) sounds odd aloud. Douay has “leaning with thy elbow upon bread”. This needs an editorial decision.
- 38:33: “they will not spring forward into the assembly” (in ecclesiam non transilient). The phrase is literal but unclear aloud; consider “go up into the assembly” (Douay).
- 38:34: “they will not be found among parables”. Consider “where parables are spoken”.
- 40:6: “as though he were under observation by day” (quasi in die respectus). The Latin may mean that he is keeping watch, not being watched. A specialist should check this.
- 30:14: “scourged by illness” for flagellatus malitia is interpretive; the Latin is “afflicted by evil”. Left as is.

## Sirach 44–51; Isaiah 1–13

# latin-038 notes (Sirach 44–51; Isaiah 1–13)

- Sirach 45:6 (Vg 45:7): similem sibi is reflexive and most naturally means “like himself” (God’s subject), not “like him” (Moses) as the 9 November note chose; “made him like him” is also unclear aloud. Editorial decision.
- Sirach 45:8 (Vg 45:9): “crowned him with splendid furnishings” for coronavit eum in vasis virtutis sounds odd aloud (Douay: “majestic attire”). Worth a look.
- Sirach 46:5 (Vg 46:6): valde fortis may go with virtutis (“hailstones of very great power”, Douay) rather than with God as the English has it. Specialist check.
- Sirach 47:6 (Vg 47:7): singular glorificavit/laudavit is rendered with God as subject (“He”), which makes “praised him with the Lord’s blessings” awkward; the people/women may be meant. Editorial decision.
- Isaiah 5:10: “jugera” and “modii” are opaque to listeners; consider “acres” / “bushels” (Douay) if the column does not deliberately keep Latin units.
- Isaiah 6:2: velabant faciem ejus / pedes ejus — ejus (not suam) allows Jerome’s reading that the seraphim veil God’s face and feet; English “his” (lowercase) settles it the other way. Editorial decision on capitalisation.
- Isaiah 8:2: Latin has Zachariam filium Barachiae; English uses the Hebrew form “Jeberechiah”. Left as the column’s spelling; flag if the column should follow the Latin form here.
- Data: several Sirach SRC lines carry stray “[” / “]” bracket marks and appended “Translation note.” text (e.g. 44:15, 44:16, 45:5); English rows are unaffected.

## Isaiah 14–39

# latin-039 (Isaiah 14–39) notes

- Isaiah 14:12: Latin has the proper name *Lucifer*; the column renders it “morning star”. Editorial decision whether the Vulgate column should keep “Lucifer” here (not changed).
- Isaiah 16:1: *dominatorem terræ* is rendered “the ruler of the land”; the traditional (Advent) reading of the Vulgate is “ruler of the earth”. Editorial call (not changed).
- Isaiah 24:14: *hinnient de mari* (literally “they will neigh from the sea”) is smoothed to “they will cry out”; the Vulgate image is lost, but “neigh” is awkward aloud. Left for an editor.
- Isaiah 25:11: same *sub eo* as 25:10 (“beneath Him”) is rendered “beneath him” here, and the EN switches subject mid-verse (Moab stretches, “He” humbles) though the Latin has one subject for both verbs. Ambiguous verse; read aloud the him/He shift is hard to follow. Needs a specialist decision (not changed).
- Isaiah 20:1: Latin *Thathan*; column has “Tartan”. Kept the column spelling.
- Data: the column uses straight apostrophes in possessives (e.g. “Lord's”) alongside curly quotes; left untouched.

## Isaiah 40–64

# latin-040 · Isaiah 40–64 · notes

## For a specialist (not changed)

- Isaiah 45:4 — *assimilavi te* is rendered “I have designated you”; the Latin says “I have likened you” (Douay “I have made a likeness of thee”). “Designated” follows the Hebrew *akhannekha* (“I have surnamed you”).
- Isaiah 53:2 — “yet we desired him:” for *et desideravimus eum* makes a contrast the Latin does not mark, and it pulls against “no attractiveness”. Douay reads it as a result (“that we should be desirous of him”). Needs a decision.
- Isaiah 48:14 — *faciet voluntatem suam … et brachium suum* is rendered “His will … His arm” (capitalised, so God’s). The reflexive more naturally points to the one the Lord loves (Cyrus). Douay leaves it ambiguous with lowercase “his”.
- Isaiah 57:16 — *flatus ego faciam* is rendered “I will make the breath of life”. “Of life” is an interpretive addition (Douay “breathings I will make”).
- Isaiah 63:1–2 — inconsistent capitals in one exchange: 63:1 has “his robe … his strength” and 63:2 has “Your clothing … Your garments”. Same speaker. Pick one.
- Isaiah 64:9 — *facta est deserta, Sion deserta facta est* repeats *deserta*; the English varies it (“deserted … wilderness”). Low priority.

## Data

- **Vulgate Isaiah 64:1 is missing.** *Utinam dirumperes cælos, et descenderes! a facie tua montes defluerent* is in neither the 63:19 row nor the 64:1 row. The 64:1 row (card vl-isaiah-64-2) starts mid-sentence (“melt as at fire’s burning…”, *tabescerent* with no subject), so read aloud it is a fragment. Restoring the Vulgate verse, or a fuller rendering, is an editorial job. Not changed here.
- Isaiah 43:3 SRC reads *Æthopiam*; the Clementine has *Æthiopiam* (transcription slip; the English is correct).
- Stray pericope brackets “[” / “]” appear in many SRC lines, including mid-line in 57:13. Harmless; the English is unaffected.
- The column mixes straight (') and curly (’) apostrophes, e.g. 53:10 “Lord’s” vs “Lord's” elsewhere. Not touched.

## Isaiah 65–66; Jeremiah 1–17

# latin-041 notes (Isaiah 65–66; Jeremiah 1–17)

## For a specialist / editorial decision (not changed)
- Isaiah 65:7 — *remetiar opus eorum primum*: EN takes *primum* as an adverb (“I will first measure”); Douay reads it with *opus* (“their first work”). Both are defensible; left as is.
- Jeremiah 15:17 — *Non sedi … et gloriatus sum a facie manus tuæ*: EN gives a positive “I gloried”; Douay carries the negative over (“nor did I make a boast”). Scope of *non* worth a specialist’s look.
- Jeremiah 2:33 — “you have even taught your ways your own wickedness” is hard to follow aloud; the Latin double accusative is ambiguous (Douay reverses it), so not changed.
- Jeremiah 15:4 — “an object of agitation” for *in fervorem* is a little opaque aloud (Douay “to be tossed”); left for an editorial call.

## Data problems
- Jeremiah 7:28 row (card vl-jeremiah-7-27, LOCKED) repeats Vulgate 7:27; the Vulgate’s own 7:28 (*Et dices ad eos: Hæc est gens quæ non audivit…*) does not appear in any row.
- No rows for Vulgate Jer 2:1, 7:1, 8:11–12, 10:6–8, 10:10, 11:7, 17:1–4 (verses absent from the Greek, so the Latin text there is not shown anywhere).
- SRC carries editorial speech brackets and stray closing “]” (e.g. Isa 65:25, 66:24, throughout Jeremiah); harmless but not Clementine text.
- EN column in this chunk uses straight apostrophes (e.g. “Lord's”) against the curly-apostrophe house style; not changed, as punctuation-only edits are out of scope.

## Jeremiah 18–35

# latin-042 · Jeremiah 18–35 (Greek row order) · notes

## For a specialist or editor (not changed)

- Jeremiah 19:1 (changed, major): I read *accipe … a senioribus populi* as partitive, following Douay and 19:10. Please confirm. The Latin has no *et*, so some readers take it as “from the elders”.
- Jeremiah 20:10: the English gives “Pursue him! Let us pursue him!” to the “many”, then has the friends say “Perhaps he may be deceived…”. In the Latin both cries come *ab omnibus viris qui erant pacifici mei*. This is defensible, but it is an editorial call.
- Jeremiah 18:8: *a malo suo quod locutus sum adversus eam* reads “from the evil against which I have spoken”, which drops *suo* (“its own evil”). Low priority.

## Data / consistency

- Jeremiah 25:14 (card vl-jeremiah-49-34): the SRC reads *Quod facum est*. The Clementine has *factum* (transcription slip; the English is correct).
- Inconsistent house style across the chunk. In 18:1–25:13 and 32:29–35:17 the column uses “Look” and straight apostrophes ('). In the Greek-order oracle blocks (25:15–31:44, plus 32:15ff) it uses “Behold” and curly ’. Worth a global pass.
- Jeremiah 23:9–23:40: 23:9 opens with no quotation mark, but 23:11 opens one (“) and 23:40 closes it. The quote marks are unbalanced.
- These rows are absent from the input, not merely empty: 26:1, 26:26, 28:45–48, 30:22, 32:1–12, 32:14, 34:1, 34:7, 34:13, 34:17, 34:21. This presumably follows the Greek row order and the shorter Greek text. Rows 25:20 and 32:13 are LOCKED with no source.

## Jeremiah 36–52; Lamentations 1–2

# latin-043 notes (Jeremiah 36–52 [Vulgate 29–45, 52]; Lamentations 1–2)

## Editorial / specialist questions (not changed)
- Lamentations 1:18: “I provoked His word to anger” renders *os ejus ad iracundiam provocavi* (literally “His mouth”). The hybrid reads oddly aloud; decide between the literal image (“His mouth”) and a sense rendering (e.g. “I defied His word”).
- Jeremiah 38:7 (Vulg 31:7): *hinnite* (“neigh”) is rendered “cry aloud”, which drops the Vulgate image. Probably right for listeners, but it is an editorial call.
- Jeremiah 38:33 (Vulg 31:33): *in visceribus eorum* is rendered “within them”, which drops “inward parts”. Acceptable, but this is a famous verse, so it may deserve the literal image.
- Jeremiah 43:23 (Vulg 36:23): the English supplies “the king” as the one who cut the scroll (the Latin just has *scidit*). It is the standard reading, but it is an addition.
- Jeremiah 48:7 (Vulg 41:7): *circa medium laci* (“in the middle of the cistern”) is softened to “at the cistern”.

## Data problems
- Wrong `vulgate_reference` on three identical “Et factum est verbum Domini ad Jeremiam, dicens” rows. These look like text-matching collisions:
  - Jeremiah 36:30 (card vl-jeremiah-29-30) shows 35:12.
  - Jeremiah 39:26 (vl-jeremiah-32-26) shows 29:30.
  - Jeremiah 42:12 (vl-jeremiah-35-12) shows 29:30.
- Jeremiah 52:8: the SRC has the typo “Chadæorum” (for Chaldæorum).
- Straight apostrophes (') appear in several EN rows instead of the house ’. Not changed, per the punctuation rule:
  - Jeremiah 36:22, 36:23, 36:26
  - Lamentations 1:7, 1:17, 2:7, 2:11, 2:12, 2:20, 2:22
- Jeremiah 44:5 is LOCKED with no source and no English. This is expected: Vulgate 37:3 already holds the Pharaoh sentence.

## Lamentations 3–5; Ezekiel 1–17

# latin-044 notes (Lamentations 3–5; Ezekiel 1–17:18)

## For a specialist or an editorial decision (not changed)
- Lamentations 4:20: “the anointed Lord” for *christus Dominus*. Douay has “Christ the Lord”, and the Hebrew means “the Lord’s anointed”. The current wording is literal but could be heard as calling God “anointed”. This needs a column-wide decision.
- Lamentations 4:3: “lamias” keeps the Vulgate’s *lamiæ*. Listeners may not know the word. Leave it, or gloss it as “sea monsters/jackals”?
- Lamentations 4:14: “When they were unable, they clutched their garments” is obscure aloud. *cumque non possent* is elliptical, and Douay supplies “could not help walking in it”.
- Lamentations 3:65: “Your affliction” for *laborem tuum* is acceptable, but “Your labour/toil” is closer to the Latin.
- Ezekiel 2:5, 2:7, 3:11, 12:3: *si forte* is rendered “in case (they may listen)”. Aloud this can sound like “as a precaution”, and “if perhaps” is clearer. The wording recurs, so I left it for a consistent decision.
- Ezekiel 2:4: “Their children are hard-faced” for *et filii dura facie … sunt*. Douay has “they are children of a hard face”. The current wording could be heard as meaning a new generation.

## Data problems
- Missing rows (no row in input): Lamentations 3:22–24 and 3:29; Ezekiel 1:14; Ezekiel 10:14. Ezekiel 2:1 and 2:10 are LOCKED with no source or English, but the Clementine has text for both (2:1 *Et dixit ad me: Fili hominis, sta super pedes tuos…*).
- Wrong `vulgate_reference` tags on the repeated formula *Et factus est sermo Domini ad me, dicens*: Ezekiel 7:1 has 6:1; 12:17, 12:21, 12:26 and 13:1 have 12:1; 14:2 and 14:12 have 13:1; 15:1 has 14:2; 16:1 has 15:1; 17:11 has 17:1. They look like they were matched to the first identical text.
- Stray “[” and “]” in SRC text from the source extraction (for example Lamentations 3:66, 4:22, 5:22; Ezekiel 6:3, 7:2, 12:10–28, 13:2, 14:13, 15:2). The English is unaffected.
- Ezekiel 7 rows 3–9 follow Greek order (Vulgate 7:6–9 then 7:3–5). The rows match their SRC, so this is noted only.
- The chunk ends at Ezekiel 17:18.

## Ezekiel 18–34

# latin-045 notes (Ezekiel 18–34, Clementine)

## For a specialist / editorial decision (not changed)
- Ezekiel 21:32 (Vulg 21:27): “This has not been done until he comes to whom judgment belongs” mixes tenses awkwardly; the Latin is past sequence (non factum est, donec veniret), Douay “this was not done till he came whose right it is”. Worth an editorial look given its messianic reading.
- Ezekiel 23:10: “The women became notorious” for factæ sunt famosæ mulieres; the Latin subject is unclear (“they became notorious women”). Left as is.
- Ezekiel 24:14: adinventiones rendered “deeds”; the Vulgate’s sense is “devices, schemes”. Left (borderline synonym).
- Ezekiel 30:24: gement gemitibus interfecti could be “the slain will groan” rather than “they will groan … with the groans of the slain”. Ambiguous; left.

## Data problems
- Rows missing from the input: Ezekiel 27:31, 32:19, 33:26 (chunk jumps 27:30→27:32, 32:18→32:20, 33:25→33:27).
- vulgate_reference tags look wrong: every “The word of the Lord came to me” row in ch. 21 (21:1, 21:6, 21:13, 21:23) says 20:2; 22:17 and 22:23 say 22:1; 28:20 says 28:1; 33:23 and 34:1 say 33:1; 34:9 says 34:7. Looks like duplicate-text matching to the first identical Latin verse.
- Straight apostrophes (') in about 23 EN rows in chs 25–34 (e.g. 25:9 “Moab's”, 26:4 “Tyre's”, 27:28, 28:2, 29:14, 30:9, 33:6, 33:17, 34:14), while other rows use ’. Not changed (punctuation-only); fix in a bulk pass.
- Introductory formula ends with “saying,” in chs 18–24 but “saying:” from ch. 25 on; inconsistent but left.

## Ezekiel 35–48; Daniel 1–1

# latin-046 notes (Ezekiel 35–48; Daniel 1)

## Data problems
- Ezekiel 40:30 is missing from the input (Clementine: “Et vestibulum per gyrum longitudine viginti quinque cubitorum, et latitudine quinque cubitorum.”). Check whether the row/card exists on the site.
- Daniel 1:22 onward does not hold Daniel 1 at all: the rows carry Susanna (Dan 13) and Bel and the Dragon (Dan 14) cards (vl-daniel-13-22 … 13-60, 14-23 … 14-41), out of order, with a “1:35a” row and gaps (1:43, 1:46–47, 1:49–50). Several rows share cards (1:44/1:45 → 13-44; 1:60/1:61/1:62 → 13-60). This looks like a broken Vulgate chapter split for Daniel; the row-to-card mapping needs fixing. I reviewed each row against its own SRC only.
- Ezekiel 38:1 carries `vulgate_reference: 37:15`, but its SRC/EN are the ordinary 38:1 formula; probably a harmless mapping note, worth a glance.

## Editorial questions (not changed)
- Ezekiel 37:26, 37:28: “sanctificationem/sanctificatio mea” is rendered “My sanctuary” (Hebrew reading). The Vulgate’s literal sense is “My sanctification”; decide whether the column should follow the Latin wording here.
- Ezekiel 43:26: “implebunt manum ejus” (fill its hand) is rendered “consecrate it”. That is the right sense, but the image is lost. Keep it as it is unless the column prefers to keep the idiom.
- Ezekiel 35:6: “cum sanguinem oderis” is rendered as a concession (“Though you hate blood”). Douay reads it as causal (“whereas you have hated blood”). Both are defensible.

## Daniel 2–12; Hosea 1–7

# latin-047 notes (Daniel 2–12; Hosea 1–7)

## For a specialist / editorial decision (not changed)
- Daniel 6:23 (vl-daniel-6-22): “innocence” renders *justitia*; the column elsewhere uses “justice/righteousness”. Consider “righteousness was found in me”.
- Daniel 7:27: “all kings will serve and obey Him”: the capital H reads *ei* as God; the Latin can equally refer to the people of the holy ones.
- Daniel 2:44: “His kingdom will not be handed over”: *regnum ejus* could be “its sovereignty” (the kingdom’s own), not God’s.
- Hosea 3:2: “I obtained her”: Clementine has the Vulgate-specific *fodi* (“I dug”); Douay also gives “bought”. Leave unless the column wants to show the Vulgate reading.
- Hosea 4:10: “by failing to keep watch” for *in non custodiendo* (Douay “in not observing”). It may suggest a sentry’s duty rather than keeping the law.
- Daniel 2:9: “because you have also prepared…”: *quod* may mean “that” (the verdict is that you concocted it) rather than “because”.

## Data problems
- Daniel 5:26–5:28 all share card vl-daniel-5-26 and show only the “Mane” text. The Vulgate 5:27 (Thecel) and 5:28 (Phares) verses are missing.
- Rows absent from the input: Daniel 4:1–3, 4:6–9, 4:35; Daniel 5:14–15, 5:18–22, 5:24–25.
- Hosea 6:1 SRC stops at “revertamur ad Dominum,”: the clause “quia ipse cepit, et sanabit nos : percutiet, et curabit nos” is missing. The row labelled Hosea 6:2 uses card vl-hosea-6-3 and holds the Vulgate text of 6:2–3, while Hosea 6:3 is empty.
- Daniel 8:3 SRC typo: “oculus” should read “oculos”.
- Straight apostrophes in Hosea EN (1:2 “Lord's”, 5:5, 6:10, 7:1, 7:10 “Israel's/Ephraim's/Samaria's”). These should be curly; I left them because punctuation-only edits are out of scope.
- Daniel 4 has mixed quote nesting: 4:17 closes with ” but 4:18–4:33 use ‘ ’ inside Nebuchadnezzar’s letter. This should be checked for the whole chapter.

## Hosea 8–14; Joel 1–4; Amos 1–9; Obadiah 1–1; Jonah 1–4; Micah 1–7

# latin-048 notes (Hosea 8 – Micah 7)

## Data problems
- Amos 6: the Clementine Vulgate 6:11 (“Et respondebit: Finis est. Et dicet ei: Tace, et non recorderis nominis Domini.”) appears in no row. Row 6:10 holds Vulg 6:10, and row 6:11 jumps to Vulg 6:12. The verse is missing from the Latin column.
- Micah 5: the row and card mapping is off. Row 5:10 (vl-micah-5-11) holds Vulg 5:11 and 5:12 together, row 5:11 is LOCKED and empty, and rows 5:12–5:14 (vl-micah-5-12/13/14, no vulgate_reference) actually hold Vulg 5:13–5:15. The cards need checking against the Clementine numbering.
- There are stray “[” and “]” brackets in many SRC lines (e.g. Hosea 8:14, 12:1, 14:1/14:2, Joel 2:17/2:18, Micah 4:14). They look like leftover pericope markers. The EN is not affected.
- There are typos in the SRC text: Amos 8:8 “ejicicetur” (read ejicietur) and Micah 3:7 “vultos” (read vultus).

## For an editorial decision (not changed)
- Some verses render “Dominus Deus exercituum” as “the Lord, the God of hosts” (Hosea 12:6, Amos 5:16) and others as “the Lord God of hosts” (Amos 5:14–15, 6:8, 9:5). The brief’s rule is Dominus Deus = the Lord God. The meaning is the same, so I left them alone.
- Amos 4:1 “Afferte, et bibemus” is rendered as “Bring us drink.” A more literal reading is “Bring, and we will drink.” The meaning is close, so I left it.

## 1 Maccabees 1–8

# latin-050 (1 Maccabees 1–8) · notes

## Data problems
- Four Clementine verses in ch. 1 have no row at all: Vulgate 1:22 (“et ascendit Jerosolymam in multitudine gravi”), 1:32 (the sudden attack on the city), 1:48 (sabbaths and feast days), 1:54 (the order to the cities of Judah to sacrifice). Row 1:20 maps to Vg 1:21 and row 1:21 to Vg 1:23, and so on. Their Latin and English are missing from the column; not added (no moving content between rows).
- LOCKED placeholder rows 1:22 and 1:49 point to “1:23” and “1:51”, but those verses show in rows 1:21 and 1:48. Check the placeholder wording.
- 3:3 SRC starts with “[” and 3:9 SRC ends with “]”. Stray brackets around the Judas poem in the Latin text; probably an import artefact.
- 2:48 translation note talks about rendering cornu as “horn of strength”, but the English says just “a horn”. Either the note or the English is out of date.

## For an editorial decision (not changed)
- 1:59: the English adds “of God” (“opposite the altar of God”); the Latin has only contra altare. It helps listeners, but it goes beyond the translation note.
- 1:20: “ascendit ad Israël” is rendered “went up against Israel” (Douay); the Latin itself only says “to”.
- 3:18 / 4:31: “hemmed in within the hands of” (concludi / conclude in manus) is a little clumsy aloud. Kept because the two verses render it the same way.
- 6:4: “returning toward Babylonia” for reversus est in Babyloniam (Latin: returned to Babylonia).

## 1 Maccabees 9–16; 2 Maccabees 1–1

# latin-051 notes (1 Maccabees 9–16; 2 Maccabees 1)

## Data problems
- 1 Maccabees 12:53: SRC and EN both stop at "dixerunt enim :" / "for they said," with no speech. The Clementine continues in 12:54 ("Non habent principem, et adjuvantem…"), and there is no row for it, so the nations' speech is missing from the column.
- 1 Maccabees 13:52–53: the 13:53 row carries Vulgate 13:54 (Simon appoints John). Vulgate 13:53 (Simon fortifies the temple mount beside the citadel and lives there) does not appear in any row and looks dropped.
- 1 Maccabees 15:39: SRC reads "Typhonem" (probably a misprint for Tryphonem); EN correctly has Trypho.
- This chunk uses straight apostrophes (Judas's, king's) throughout, not the house-style ’. I left them alone because the brief says not to change punctuation on its own.

## For a specialist or editor (not changed)
- 1 Maccabees 16:3: "et fratres mei" is taken as vocative ("my brothers") addressed to the sons. The 9 Nov note already marks this as a priority for specialist review.
- 1 Maccabees 16:9: "quam ædificavit": the builder (John or Cendebaeus) is left ambiguous, as the note intends. Confirm that is acceptable.
- 1 Maccabees 9:35: "misit fratrem suum ducem populi" ("his brother, a leader of the people"). John is not named until 9:36, so a listener may not know who is meant. Editorial call.
- 1 Maccabees 12:22: "benefacitis" is present tense ("you do well"), but the EN has "you will do well", matching 12:18. Minor; left as is.

## 2 Maccabees 2–14

# latin-052 (2 Maccabees 2–14) · notes

Not changed; for a specialist or an editorial decision:

- 5:27 *qui decimus fuerat* is rendered “who was one of ten” (the Greek sense). The Latin literally says “who was the tenth” (Douay). The meaning is close, but decide whether the column should keep the Vulgate’s wording.
- 10:12 Latin *Macer* is rendered “Macron”, the Greek byname, under the translation note. That conflicts with “render the Latin”. Keep for consistency, or change to “Macer”?
- 14:37 Latin *Razias* is rendered “Razis”, the Greek form. I left it because it is the column’s existing spelling.
- 14:1 *per portam Tripolis* is rendered “through the harbor of Tripolis”. *Porta* means “gate”, but Douay also says “haven”, so I left it.
- 6:15 The Latin has no negative (*ita et in nobis statuit … ita demum in nos vindicet*). The English supplies one from the *Non enim* in 6:14, as the translation note says. That is reasonable, but a Latin specialist should confirm it.
- 13:25 *indignantes ne forte fœdus irrumperent* is ambiguous: who might break the treaty? The current “so indignant that they might break the treaty” is acceptable. It is flagged only for review.
- 9:19 The translation note says the header (*rex et principes Antiochus*) needs checking against a printed witness before publication. Still open.
- 14:44 The translation note asks for independent Latin and textual review of *per mediam cervicem*. Still open.

Data: none of the rows I changed carries a bracketed tag. The 2:19–2:32 rows have vulgate_reference values one higher than the row numbers (2:20–2:33). That is expected and was left as it is.

## Matthew 14–25

# latin-054 (Matthew 14–25:42) notes

## Data problems
- Missing Clementine verses: **Mt 17:20** (“Hoc autem genus non ejicitur nisi per orationem et jejunium”, Greek 17:21), **Mt 18:11** (“Venit enim Filius hominis salvare quod perierat”) and **Mt 23:14** (“Væ vobis … quia comeditis domos viduarum …”). None of these has a row in the input: 17:20 → 17:22, 18:10 → 18:12, 23:13 → 23:15. Check whether the cards exist on the site.
- Mt 16: the row labelled “Matthew 16:3” has card `matthew-16-4` (vulgate 16:4), and “Matthew 16:4” is a LOCKED empty row. So the reference label and the card are one verse apart. Same offset in Mt 17:15–17:27 (Vulgate 17:14 includes the father’s plea). Expected Vulgate numbering, but worth checking that the labels show correctly.
- The chunk ends at 25:42. 25:43–46 are presumably in latin-055.

## Editorial decisions (not changed)
- Spelling is mixed within the chunk: “neighbor” (19:19) vs “neighbour” (22:39), “rumours” (24:6), and “insnare” (22:15). Should one spelling be used throughout?
- The 9 Nov fresh renderings (16:3–4, 16:17–19, 17:4, 17:27, 18:6–9, 19:3–12, 24:10, 25:22) use modern punctuation, and 17:4 and 25:22 use quotation marks. The Douay rows around them don’t. The renderings are accurate, but the style is uneven.
- 16:18 “gates of the underworld” for portæ inferi was kept as the 9 Nov reading. Most Catholic readers expect “hell”, so an editor may want to look at it.
- 19:4 “he who made humanity” for qui fecit hominem: the Genesis pass changed “humankind” back to “man” for hominem. Consider using the same wording here.
- Douay “seduce” for seducere (24:4, 24:5, 24:11) can sound sexual to modern listeners; “lead astray” would avoid that. Left unchanged.
- 25:40 “as long as you did it” (quamdiu): modern listeners may hear this as time (“for as long as”) rather than “inasmuch as”. It’s a well-known Douay phrase, so it was left unchanged.
- 25:27 “with usury” (cum usura = interest) and 23:25 “rapine” are archaic. Left unchanged.
