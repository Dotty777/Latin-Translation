# Exodus study prose — draft for review

Every chapter of Exodus (1–40) now carries its own interpretive study in the Study Workspace, verse by verse, on staging site 248834710. All forty chapter records have status **Draft for review**; nothing has been sent to production.

## What each verse carries

For each of the 1,195 verse rows (1,186 numbered verses plus nine sub-verse keys the site uses where the Greek and Hebrew do not align one to one: 28:29a, 35:12a, 37:18b, 38:10a/b, 38:11a/b, 38:24a/b):

- **received** — one sentence stating what the verse says, in the Hebrew-column wording.
- **explain** — a paragraph on how the Hebrew, Greek, Latin and King James columns relate: what they share, where the Greek departs from the Hebrew, where the Latin or King James follows one or the other, and what the site's own source notes say about the difference. Interpretations the source calls "proposed, origin unresolved" are reported as such; units, plant names and gem names are kept per column without conversion.
- **shared** — three short statements all four columns agree on.
- **instructions** — a Knowledge line (stated), a Wisdom line (reflection), and a Command line wherever the verse contains a command. 2,595 instructions in all, 205 of them Commands (the Decalogue, the covenant code, the tabernacle instructions and the priestly rites account for the rise from Genesis's 68).
- **entries** — links into the lexicon catalogue, 73 distinct entries (Moses 335 verses, YHWH 326, tabernacle 215, Egypt 118, high priest 90, altar 78, ark 36, Elohim 34, breastpiece 34, lampstand 33, Sinai 32, incense 29, anointing oil 28, ephod 28, manna 24, Passover lamb 21 …).
- **lost** — what the Greek loses from the Hebrew, what the Greek has in its place or adds, and what the Latin and King James do with the difference. Where the consulted Greek has no counterpart at a verse (25:6, 28:23–28, 32:9, 35:8, 35:18, 37:22–28, 39:39, 40:7, 40:11, 40:28, 40:30–32) the entry says so and does not fill the Greek from the Hebrew.
- A **chapter note** summarising the chapter and the pattern of Hebrew–Greek difference in it.

## Chapter sizes

1:22 2:25 3:22 4:31 5:23 6:30 7:29 8:28 9:35 10:29 11:10 12:51 13:22 14:31 15:27 16:36 17:16 18:27 19:25 20:26 21:37 22:30 23:33 24:18 25:40 26:37 27:21 28:44 29:46 30:38 31:18 32:35 33:23 34:35 35:34 36:38 37:28 38:33 39:24 40:38

## Where it lives

- Prose sources: `prose/exodus-1.py` … `prose/exodus-40.py`, one pattern throughout.
- Merged chapter records: `data/exodus-part1.json.gz` (chapters 1–27) and `data/exodus-part2.json.gz` (28–40); sha256s in `data/manifest.json`.
- Loaded to staging through the Saints Pentateuch Work helper (`wsdata` multi job); the reader serves each chapter at `/wp-json/saints-workspace/v1/data/exodus-<ch>`.

Batches and commits: Exodus 1–20 at `a19bdd7`, 21–40 at `9aab67b`.

## For the reviewer

- **The reordered Greek execution narrative (chapters 36–39).** The Greek Exodus tells the building of the tabernacle in a different order from the Hebrew: its chapter 36 is the priestly garments (Hebrew 39), its 37 the curtains and court (Hebrew 36 and 38), its 38 the furniture (Hebrew 37), its 39 the metal accounts and inventory (Hebrew 38–39). The site's source aligns each Greek verse with its Hebrew subject and shows the Hebrew's own chapter beside it. The prose follows that alignment: each `received` sentence names what the Hebrew chapter has at that verse and what the Greek has in its place, and every `lost` entry marks the Hebrew's structural detail (loops, boards, bases, bars, dimensions) as having no Greek counterpart *at that point*, which the source insists is a difference of narrative extent and not a claim that the Greek sanctuary lacked those parts. A reviewer reading 36–39 should expect two subjects per verse; that is the source's shape, not a drafting error.
- **Readings without Hebrew parallel.** The Greek has the bronze altar made from Korah's censers (38:22), the basin from the mirrors of "the women who fasted" with the priests' washing (38:26–27), leftover gold and cloth made into vessels and robes (39:11–12), and Aaron rather than the people saying "these are your gods" (32:4). The prose reports these as the Greek's readings and keeps the source's cautions (the Korah tradition raises a chronological question; the fasting women are not explained by the selected accounts).
- **Totals that differ.** Gold 730 vs 720 shekels (39:1), bronze 2,400 vs 1,500 shekels and the Latin's "seventy-two thousand talents" (39:6), Levite deaths 3,000 vs the Latin's 23,000 (32:28). Each is reported with the columns' own figures and no harmonisation.
- **Divine-name proclamation (34:6–7) and the stiff-necked verse (32:9).** The Latin gives 34:6 to Moses as speaker; the Greek has no numbered 32:9. Both are recorded as the source has them.
- **Lexicon gaps.** No catalogue entries exist for Aaron, Pharaoh (the `pharaoh-monster` entry is a different subject), Jethro, Zipporah, Bezalel, Oholiab, Sabbath, pillar of cloud, golden calf, atonement or sin offering, so those are not linked; `high-priest` has been used for Aaron throughout. Adding entries to `lexicon-catalogue.json` and re-merging is a small job.
- **Voice.** As for Genesis: Wisdom lines are reflective, one sentence each, and avoid doctrinal claims beyond what the four columns say. Commands are quoted in the Hebrew-column wording.

Next: Leviticus, then Numbers and Deuteronomy in the same shape.
