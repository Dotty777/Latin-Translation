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
