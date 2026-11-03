# Genesis study prose — draft for review

Every chapter of Genesis (1–50) now carries its own interpretive study in the Study Workspace, verse by verse, on staging site 248834710. All fifty chapter records have status **Draft for review**; nothing has been sent to production.

## What each verse carries

For each of the 1,534 verse rows (1,533 verses; 35:22 is split a/b as on the site):

- **received** — one sentence stating what the verse says, in the Hebrew-column wording.
- **explain** — a paragraph on how the Hebrew, Greek, Latin and King James columns relate: what they share, where the Greek departs from the Hebrew, where the Latin or King James follows one or the other, and what the site's own source notes (N/W/B lines) say about the difference. Rare or disputed Hebrew words are marked provisional where the source marks them so; interpretations the source calls "proposed, origin unresolved" are reported as such.
- **shared** — three short statements all four columns agree on.
- **instructions** — a Knowledge line (stated), a Wisdom line (reflection), and a Command line wherever the verse contains a command. 2,596 instructions in all, 68 of them Commands.
- **entries** — links into the lexicon catalogue (Jacob 252 verses, Abraham 231, Isaac 110, YHWH 104, Egypt 96, Elohim 60, Canaan 60, Sarah 58 …).
- **lost** — what the Greek loses from the Hebrew, what the Greek has in its place or adds, and what the Latin and King James do with the difference.
- A **chapter note** summarising the chapter and the pattern of Hebrew–Greek difference in it, and recording where Hebrew- or Greek-column renderings were corrected on the day the source was read.

## Chapter sizes

1:31 2:25 3:24 4:26 5:32 6:22 7:24 8:22 9:29 10:32 11:32 12:20 13:18 14:24 15:21 16:16 17:27 18:33 19:38 20:18 21:34 22:24 23:20 24:67 25:34 26:35 27:46 28:22 29:35 30:43 31:55 32:32 33:20 34:31 35:30 36:43 37:36 38:30 39:23 40:23 41:57 42:38 43:34 44:34 45:28 46:34 47:31 48:22 49:33 50:26

## Where it lives

- Prose sources: `prose/genesis-1.py` … `prose/genesis-50.py` (Genesis 1 was written earlier in a slightly different file shape; 2–50 follow one pattern).
- Merged chapter records: `data/genesis-part1.json.gz` (chapters 1–26) and `data/genesis-part2.json.gz` (27–50); sha256s in `data/manifest.json`.
- Loaded to staging through the Saints Pentateuch Work helper (`wsdata` multi job); the reader serves each chapter at `/wp-json/saints-workspace/v1/data/genesis-<ch>`.

Batches and commits: Genesis 2–22 (earlier), 23–35 at `7537b2e`, 36–50 at `ebf76a5`.

## For the reviewer

- **Genesis 1 lexicon anchors.** Genesis 1 was the pilot and some of its lexicon entries were written before the catalogue was fixed; a few anchors there may not resolve. Worth a pass.
- **Disputed poetry.** Genesis 49 (Jacob's blessings) is where Hebrew and Greek diverge most; the prose keeps both portraits distinct rather than harmonising. 49:10 (Shiloh) is reported with the source's caution that a messianic reading is an interpretation, not evidence of the earliest wording.
- **Lexicon gaps.** No catalogue entries exist yet for Sodom, Lot, Moab, Ammon, Ishmael, Cain, Abel, Seth, Damascus, Esau, Judah, Pharaoh, Potiphar, Goshen or Machpelah, so those names are not linked. A `joseph-son-of-jacob` entry does exist but was not linked from Genesis 37–50; linking it is part of the same re-merge. Adding them to `lexicon-catalogue.json` and re-merging is a small job.
- **Day-of corrections.** Chapter notes record where the Hebrew or Greek column rendering was corrected on 2 November 2026 (for example 49:6 Greek "rest upon" for "contend", 50:15 Hebrew singular "all the evil"). These are already in the records; the notes are there so the reviewer can see what moved.
- **Voice.** Wisdom lines are reflective, one sentence each, and avoid doctrinal claims beyond what the four columns say. Commands are quoted in the Hebrew-column wording.

Next: Exodus, then Leviticus, Numbers and Deuteronomy in the same shape.
