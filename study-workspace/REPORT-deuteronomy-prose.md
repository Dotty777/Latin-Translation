# Deuteronomy study prose — draft for review

Every chapter of Deuteronomy (1–34) now carries its own interpretive study in the Study Workspace, verse by verse, on staging site 248834710. All thirty-four chapter records have status **Draft for review**; nothing has been sent to production. With this book the whole Law (Genesis–Deuteronomy, 187 chapters) has study prose.

## What each verse carries

For each of the 959 verse keys (the site's keys follow the Hebrew/Greek chapter divisions where they differ from the English, see below):

- **received** — one sentence stating what the verse says, in the Hebrew-column wording.
- **explain** — a paragraph on how the Hebrew, Greek, Latin and King James columns relate: what they share, where the Greek departs from the Hebrew, where the Latin or King James follows one or the other, and what the site's own source notes say about the difference. Uncertain Hebrew (the bird list of 14, the disease and crop terms of 28:22 and 27, 'fiery law' at 33:2, 'bars/sandals' at 33:25, 'the watered with the thirsty' at 29:18, 'long-haired heads' at 32:42, the compressed Song and Blessing throughout) is reported as uncertain.
- **shared** — three short statements all four columns agree on.
- **instructions** — a Knowledge line (stated), a Wisdom line (reflection), and a Command line wherever the verse contains a command. 2,144 instructions in all, 226 of them Commands (the most of any book, as expected for the law code of 12–26).
- **entries** — links into the lexicon catalogue, 63 distinct entries (YHWH 434 verses; Moses 65; Egypt 49; gods 37; Jordan 27; covenant 23; grapevine 20; Elohim 18; high priest 18; wheat 15; Jacob 13; olive 13; altar 13; Sinai 12; Og 11; Abraham 11; stone tablets 11; scroll 11; Joshua 10; rock 9; redeemer 8; ark 8 …).
- **lost** — what the Greek loses from the Hebrew, what the Greek has in its place or adds, and what the Latin and King James do with the difference. Recurring differences are carried by shared constants (your God / our God; plains of Moab / western side of Moab; make His name dwell / be invoked; gates / cities; dispossess / destroy; Amen / So be it; the Rock / God; Jeshurun / the Beloved; the evil / the evil person; officers / scribes; household slave; calf / ox; frontlets / immovable).
- A **chapter note** summarising the chapter and listing the Hebrew–Greek differences in it.

## Chapter sizes

1:46 2:37 3:29 4:49 5:33 6:25 7:26 8:20 9:29 10:22 11:32 12:31 13:19 14:29 15:23 16:22 17:20 18:22 19:21 20:20 21:23 22:29 23:26 24:22 25:19 26:19 27:26 28:69 29:28 30:20 31:30 32:52 33:29 34:12

## Where it lives

- Prose sources: `prose/deuteronomy-1.py` … `prose/deuteronomy-34.py`, all on the compact `v()` helper; chapter 27's twelve curses use a small `curse()` helper.
- Merged chapter records: `data/deuteronomy-part1.json.gz` (chapters 1–28) and `data/deuteronomy-part2.json.gz` (29–34); sha256s in `data/manifest.json`.
- Loaded to staging through the Saints Pentateuch Work helper (`wsdata` multi job `d0134`, output page 43704): part1 stored 28 / unchanged 27 / bad none; part2 stored 6 / unchanged 7 / bad none. The reader serves each chapter at `/wp-json/saints-workspace/v1/data/deuteronomy-<ch>`.

Commit: Deuteronomy 1–34 at `46beeaf`.

## For the reviewer

- **Chapter and verse divisions.** The site's keys follow the Hebrew and Greek: English 12:32 is 13:1 and English 13:1–18 is 13:2–19; English 22:30 is 23:1 and English 23:1–25 is 23:2–26; English 29:1 is 28:69 and English 29:2–29 is 29:1–28. The Greek also swaps the grain and vineyard verses at 23:25–26 and places adultery before murder at 5:17–18. The chapter notes say so and a NUM constant carries the note into `lost`.
- **The great Greek variants.** 32:8 'angels of God' for 'sons of Israel' (with the Qumran 'sons of God' noted); 32:43's long expanded ending with heavens, sons of God and angels (the form Hebrews 1:6 quotes); 6:4's prefixed introduction to the Shema; 28:1's Jordan clause; 30:6 'cleanse' for 'circumcise' your heart; 30:3 'heal your sins' for 'restore your fortunes'; 17:18 'this second law' (deuteronomion), the book's Greek name; 18:22 'you shall not spare him' for 'do not fear him'; 21:12–13 the captor, not the woman, shaving and stripping; 22:38 'you ate' for 'the gods ate'; 26:5 'my father abandoned Syria'; 27:23's thirteenth curse; 33:2 'angels' and 'Kadesh'; 34:6 'they buried'. Each is reported as the Greek's reading, with the Latin and King James placed.
- **The Hebrew's shifts of voice.** God's first person breaks into Moses' speech at 11:13–15, 17:3, 28:20, 29:4–5; the Greek normalises most of these to the third person. The prose keeps the Hebrew's voice and flags the Greek's.
- **The hard chapters.** 7:2 and 20:16–17 (the ban), 13 (three executions, 'your hand first'), 21:18–21 (the rebellious son), 22:13–29 (the marriage-bed laws, including 22:28–29), 23:2–4 (exclusions from the assembly), 25:11–12, and 28:53–57 are reported as the text has them in every column. The Wisdom lines say what Israel was told and what later Scripture did with it, and do not present these as patterns for any people since; where the rabbis hedged a law to near-inapplicability (21:18–21, 13) the prose says so.
- **The Hebrew's own difficulties.** 33:2 (eshdat, 'fiery law'), 33:25 (min'al, dove'a), 29:18 (the watered with the thirsty), 32:5 (the broken syntax), 32:42 (long-haired heads / leaders), 28:22 (sword / drought by pointing), 14:12–18 (every bird name), 35:3 and 32:36 (atsur ve-azuv). Each is marked as disputed or uncertain.
- **New Testament reach.** Deuteronomy is the most-quoted Torah book in the New Testament, and the Wisdom lines point to the plain uses: the three temptation answers (6:13, 6:16, 8:3), the great commandment (6:5), 'the word is near you' (30:12–14, Romans 10), 'cursed is everyone who hangs' (21:23, Galatians 3), 'two or three witnesses' (17:6, 19:15), 'muzzle the ox' (25:4), 'vengeance is mine' (32:35), 'a prophet like me' (18:15), 'rejoice, nations' (32:43), 'he will not forsake you' (31:6), 'the root of bitterness' (29:17).
- **Lexicon gaps.** No catalogue entries exist for Aaron, Eleazar or Phinehas (so `high-priest` is used), Caleb, Sihon (Og exists), Balaam, the Levites as a tribe, Molech (`molech` exists), Asherah, the Shema, the Decalogue as such, Horeb (`sinai` is used), Pisgah, Nebo, Beth-peor, Gerizim and Ebal, Jeshurun, cities of refuge, the levirate, Sheol (`death-hades` is used), Amalek, Edom/Moab/Ammon, or the blood-avenger as such (`redeemer` is used). A `sheol` entry was tried at 32:22 and does not exist. Adding entries and re-merging is a small job.
- **Voice.** As for the four books before it: Wisdom lines are reflective, one sentence or two; Commands are quoted in the Hebrew-column wording; the chapter notes list the Greek differences so a reviewer can find them without reading every verse.

The Law is complete. Next: the Former Prophets (Joshua, Judges, Samuel, Kings) in the same shape, unless the reviewer directs otherwise.
