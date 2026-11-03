# Leviticus study prose — draft for review

Every chapter of Leviticus (1–27) now carries its own interpretive study in the Study Workspace, verse by verse, on staging site 248834710. All twenty-seven chapter records have status **Draft for review**; nothing has been sent to production.

## What each verse carries

For each of the 859 verses (Leviticus has no sub-verse keys; the Hebrew and Greek align one to one throughout):

- **received** — one sentence stating what the verse says, in the Hebrew-column wording.
- **explain** — a paragraph on how the Hebrew, Greek, Latin and King James columns relate: what they share, where the Greek departs from the Hebrew, where the Latin or King James follows one or the other, and what the site's own source notes say about the difference. Uncertain Hebrew terms (the blemish lists of 21:18–20 and 22:22–23, the disease words of 26:16, the hairstyle of 19:27, *ba'al* at 21:4) are reported as uncertain, and ancient disease and animal names are not converted into modern diagnoses or species.
- **shared** — three short statements all four columns agree on.
- **instructions** — a Knowledge line (stated), a Wisdom line (reflection), and a Command line wherever the verse contains a command. 1,883 instructions in all, 165 of them Commands.
- **entries** — links into the lexicon catalogue, 39 distinct entries (high priest, used for Aaron and the priesthood, 282 verses; YHWH 243; altar 129; Moses 80; tabernacle 54; Canaan 19; savor 17; unleavened bread 15; anointing oil 13; Egypt 13; incense 10; covenant 10; Lamb of God 9; divine names 9; wheat 8; YHWH-who-sanctifies 8 …).
- **lost** — what the Greek loses from the Hebrew, what the Greek has in its place or adds, and what the Latin and King James do with the difference. Recurring differences are carried by shared constants in the prose sources so that the wording is the same wherever the same difference recurs (Tent of Meeting / Tent of Testimony; well-being / deliverance; burn / offer up; cut off / destroyed; Jubilee / release; Molech / a ruler; blood-liability formula / "they are guilty"; afflict / humble; booths / tents; shekel / didrachma).
- A **chapter note** summarising the chapter and listing the Hebrew–Greek differences in it.

## Chapter sizes

1:17 2:16 3:17 4:35 5:26 6:23 7:38 8:36 9:24 10:20 11:47 12:8 13:59 14:57 15:33 16:34 17:16 18:30 19:37 20:27 21:24 22:33 23:44 24:23 25:55 26:46 27:34

## Where it lives

- Prose sources: `prose/leviticus-1.py` … `prose/leviticus-27.py`. Chapters 1–12 use the long-form pattern of Genesis and Exodus; from chapter 13 a compact `v()` helper builds the same record shape.
- Merged chapter records: `data/leviticus-part1.json.gz` (chapters 1–26) and `data/leviticus-part2.json.gz` (27); sha256s in `data/manifest.json`.
- Loaded to staging through the Saints Pentateuch Work helper (`wsdata` multi job `l0127`, output page 43633): part1 stored 25 / unchanged 24 / bad none; part2 stored 2 / unchanged 3 / bad none. The reader serves each chapter at `/wp-json/saints-workspace/v1/data/leviticus-<ch>`.

Commit: Leviticus 1–27 at `c76f976`.

## For the reviewer

- **Where the Greek changes the sense, not just the word.** The prose flags these in `explain`, `lost` and the chapter note rather than smoothing them: the blood rationale at 17:11 and 17:14 (Hebrew "the life of the flesh is *in* the blood … atones *by* the life"; Greek "the life of all flesh *is* its blood … *in place of* the life"); Molech read as "a ruler" throughout 18:21 and 20:2–5, with "the name of those consecrated to Me" for "My holy name" at 20:3; "the land became indignant" for the Hebrew's "vomited out" (18:25, 28; 20:22); "the day after the first day" for "the day after the Sabbath" at 23:11 (the Greek keeps "Sabbath" at 23:15), which bears on the Pentecost count and is left unharmonised; "My covenant" for "My dwelling" at 26:11; "destroy them in their enemies' land" for "bring them into" at 26:41; "eat on the mountains" for "eat over the blood" at 19:26; "names the Name" for "blasphemes" at 24:11 and 24:16, with the source's warning that 24:11 and 24:15 tie it to cursing.
- **Greek anomalies the source leaves uncorrected.** "The sixth year of release" for "the year of Jubilee" at 25:28; "when the release has passed" at 27:21; "from the year of release" for "until the year of Jubilee" at 27:23; "Aaron and his sons" for "Aaron" at 24:3; salt added to the showbread frankincense at 24:7; the chaste-tree branches added at 23:40. Each is reported as the Greek's reading.
- **Lists that do not line up.** The priestly and animal blemish lists (21:18–20, 22:22–23), the forbidden birds and swarming things (11), the disease terms (26:16), the cult objects at 26:30, the measures at 19:35–36 and 27:16/25. The prose gives each column's list and does not map one onto the other.
- **The Hebrew's own difficulties.** 21:4 (*ba'al*: husband, master, ruler, or the Greek's "suddenly"); 25:30 (written "no wall" / read "has a wall"); 25:33 (an awkward opening kept without a supplied "not"); 19:16 ("stand by at the blood", bystander or hostile reading); 25:47 (*eqer*). Each is marked as disputed.
- **Slavery.** 25:44–46 is reported as the text has it: foreign slaves permitted and inherited, Israelites protected. The prose does not soften it.
- **Lexicon gaps.** No catalogue entries exist for Aaron (so `high-priest` is used), Nadab and Abihu, Eleazar and Ithamar, Azazel's rite as a whole (the `azazel` entry is used at 16), sin/guilt/peace offerings, atonement, Sabbath, Jubilee, Molech, leprosy, clean/unclean, blasphemy, showbread, tithe, firstborn or *herem*. A `palm` entry was tried at 23:40 and does not exist. Adding entries and re-merging is a small job.
- **Voice.** As for Genesis and Exodus: Wisdom lines are reflective, one sentence or two, and point forward only to what later Scripture plainly does with the verse (Ruth and the gleaners, Pentecost, "love your neighbour", eye for eye, the Liberty Bell verse, the Shema's second commandment). Commands are quoted in the Hebrew-column wording.

Next: Numbers, then Deuteronomy in the same shape.
