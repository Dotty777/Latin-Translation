# Follow-Up Latin Mapping, Studio Versification Reconciliation & Note-Attachment Audit

- **Auditor:** `@latin-studio-mapper`
- **Date:** 2026-11-25
- **Latin Critical Text Anchor:** `Clem1598-USFX` (`Saints-Latin-Critical-Text`, 70 books, 1,298 chapters, 34,952 native Vulgate verses)
- **Studio Versification Engine:** `Saints-Critical-Text-Studio/studio/lexica/versification.py` (`tests.test_lexica_versification`: 30/30 OK)
- **Meaning-Changing English Verse Wording Changes Made:** `0` (`latin_wording_proposals.jsonl`: `0` proposals needed)
- **Unresolved Items:** `0`

---

## 1. Full-Corpus 70-Book Status Summary (`34,952` Native Vulgate Verses)

Every native Vulgate verse across all 70 books was audited by passage content against `Saints-Latin-Critical-Text`, `Modern-English-OT/NT`, `studio/lexica/versification.py`, and live `Saints.Bible` display slots:

| Distinct Audit Status | Native Latin Verse Count | Share | Definition |
|---|---:|---:|---|
| `mapped_verified` | 30,701 | 87.84% | 1-to-1 same-number verified match between native Vulgate and Saints.Bible |
| `reordered` | 2,995 | 8.57% | 1-to-1 shifted or reordered match across chapter/verse numbers (`Exod 38:24-25, 28-29`, `Deut 5:17-18`, `1 Kgs 7`, `Psalms`, `Jeremiah`, `Mal 4`, etc.) |
| `split_or_merged` | 817 | 2.34% | Native split into a shared Saints.Bible verse (`Exod 38:26-27 -> 39:4`) or native merge across multiple Saints.Bible verses (`Exod 38:30 -> 39:9, 39:7`; `Sir 42:1 -> 41:27, 41:26, 42:1`) |
| `partial_correspondence` | 8 | 0.02% | Documented partial clause overlap without a clean full-verse equivalent (`Sir 1:1`, `Exod 36:13`, `1 Sam 20:22`, `1 Kgs 7:31`, `Num 16:43`, `Esth 12:6`, `13:7`, `Jer 30:15`) |
| `no_counterpart` | 431 | 1.23% | Genuine Clementine Vulgate verse absent from live Saints.Bible (`Exod 36:10-33`, `Dan 13-14`, LXX-II/Vulgate `Sirach` pluses, `Matt 17:20`, `Neh 4:6`, plus confirmed doublet `Sir 19:6`) |
| `unresolved` | 0 | 0.00% | Zero unresolved verses |
| **Total Native Latin Verses** | **34,952** | **100.00%** | Exact match to `Saints-Latin-Critical-Text` (`34,952`) |

### Saints.Bible-Side Slots Audited Separately (Absent Full-Verse Counterpart in Vulgate)

| Saints.Bible Slot | Studio Greek | `from_saints('latin', ...)` | Audit Status | Explanation |
|---|---|---|---|---|
| `Exodus 39:2` | `39:2` | `[]` | `partial_correspondence` | Combined silver-contribution summary (100 talents + 1,775 shekels; MT 38:25-26a) omitted by Jerome. See Section 2 below. |
| `Psalms 151:1–7` | `151:1–7` | `[]` | `no_counterpart` | LXX Psalm 151 (7 verses) is absent from `Clem1598-USFX`. |

---

## 2. Task 1 — Clause-by-Clause Reconciliation of Native Latin `Exodus 38:24–31` & `Saints 39:2`

Prior to this follow-up, `studio/lexica/versification.py` carried Hebrew MT rules in `_RULES['latin']` (`exodus 38:24-26 = 39:1-3`, `exodus 38:27 > 39:4-5`), causing `Latin 38:25` to mis-map to `Saints 39:2` and `Latin 38:26` to mis-map to `Saints 39:3`. Clause-by-clause verification against `Saints-Latin-Critical-Text/01_Law/02_Exodus/02_Exodus_38_Critical_Text.json`, `Saints-Greek-Critical-Text/01_Law/02_Exodus/02_Exodus_39_Critical_Text.json`, and live `Saints.Bible` Exodus 39 establishes:

| Native Latin | Adopted Latin Clause (`Clem1598-USFX`) | Studio Greek | Saints.Bible Slot | Audit Status | Clause-by-Clause Decision |
|---|---|---|---|---|---|
| `Exod 38:24` | *Omne aurum quod expensum est in opere sanctuarii, et quod oblatum in donariis, viginti novem talentorum fuit, et septingentorum triginta siclorum ad mensuram sanctuarii.* | `39:1` | `39:1` | `reordered` | Full 1-to-1 clause match: total gold expended/offered for the sanctuary (29 talents, 730 shekels by the sanctuary shekel) = Studio Greek 39:1 = Saints 39:1. |
| `Exod 38:25` | *Oblatum est autem ab his qui transierunt ad numerum a viginti annis et supra, de sexcentis tribus millibus et quingentis quinquaginta armatorum.* | `39:3` | `39:3` | `reordered` | Full clause match to Studio Greek 39:3 / Saints 39:3 (census count of enrolled men aged 20 and upward: 603,550; Latin adds 'armatorum'). The opening bridge 'Oblatum est autem ab his' only links back to the offering topic without translating Saints 39:2's silver sum (100 talents + 1,775 shekels) or MT 38:26a's half-shekel per head. Corrected from prior erroneous Studio mapping 38:25 -> 39:2. |
| `Exod 38:26` | *Fuerunt præterea centum talenta argenti e quibus conflatæ sunt bases sanctuarii, et introitus, ubi velum pendet.* | `39:4` | `39:4` | `split_or_merged` | Exact clause match to Studio Greek 39:4 = Saints 39:4a ('and the hundred talents of silver were for casting the hundred bases of the sanctuary and the bases of the veil'). Does NOT match Saints 39:2 (shared 100 talents quantity is insufficient for a full-verse match; 38:26 is strictly the casting-of-bases clause, matching MT 38:27a / Studio Greek 39:4). Corrected from prior erroneous Studio mapping 38:26 -> 39:3. |
| `Exod 38:27` | *Centum bases factæ sunt de talentis centum, singulis talentis per bases singulas supputatis.* | `39:5` | `39:4` | `split_or_merged` | Exact clause match to Studio Greek 39:5 = Saints 39:4b ('a hundred bases for the hundred talents, a talent per base'). Native Vulgate splits Saints 39:4 across 38:26 (= Greek 39:4 = Saints 39:4a) and 38:27 (= Greek 39:5 = Saints 39:4b). Studio Greek rule updated from 38:27 > 39:4-5 to 38:27 = 39:5 (still composing to Saints 39:4). |
| `Exod 38:28` | *De mille autem septingentis et septuaginta quinque fecit capita columnarum, quas et ipsas vestivit argento.* | `39:6` | `39:5` | `reordered` | Full clause match to Studio Greek 39:6 = Saints 39:5 (from the 1,775 shekels he made the hooks/capitals of the pillars and overlaid them with silver). Note the 1,775 figure appears in Vulgate only here in the fabrication clause, not in a prior silver-summary verse. |
| `Exod 38:29` | *Æris quoque oblata sunt talenta septuaginta duo millia, et quadringenti supra sicli,* | `39:7` | `39:6` | `reordered` | Full clause match to Studio Greek 39:7 = Saints 39:6 (bronze offering summary; Clementine reads 72,000 talents + 400 shekels vs MT 70 talents + 2,400 shekels vs LXX 70 talents + 1,500 shekels). |
| `Exod 38:30` | *ex quibus fusæ sunt bases in introitu tabernaculi testimonii, et altare æneum cum craticula sua, omniaque vasa quæ ad usum ejus pertinent,* | `39:10, 39:8` | `39:9, 39:7` | `split_or_merged` | One-to-several native merge: bronze altar, grating, and vessels = Studio Greek 39:10 / Saints 39:9 (majority, first target), plus bases of the entrance of the tent = Studio Greek 39:8 / Saints 39:7 (second target). Fixed prior parallel-verse-map omission of 39:7. |
| `Exod 38:31` | *et bases atrii tam in circuitu quam in ingressu ejus, et paxillos tabernaculi atque atrii per gyrum.* | `39:9` | `39:8` | `reordered` | Full clause match to Studio Greek 39:9 = Saints 39:8 (bases of the courtyard around and at its gate, plus pegs of tabernacle and courtyard). |

### Separate Evaluation of `Saints 39:2` (`partial_correspondence`, `from_saints == []`)

- **Saints.Bible `Exodus 39:2`** (`Studio Greek 39:2`): *"The silver contribution from the enrolled men of the congregation was a hundred talents and one thousand seven hundred and seventy-five shekels"* (`καὶ ἀργυρίου ἀφαίρεμα παρὰ τῶν ἐπεσκεμμένων τῆς συναγωγῆς ἑκατὸν τάλαντα, καὶ χίλιοι ἑπτακόσιοι ἑβδομήκοντα πέντε σίκλοι...`).
- **Why it is NOT a full-verse match to `Latin 38:25` or `38:26`:**
  1. Jerome completely omits MT 38:25's combined silver total and MT 38:26a's half-shekel per head (`beka`).
  2. `Latin 38:25` preserves only the 5-word transitional bridge *"Oblatum est autem ab his"* before translating the census clause of `Saints 39:3` (`a viginti annis et supra, de sexcentis tribus millibus et quingentis quinquaginta armatorum`).
  3. `Latin 38:26` mentions `centum talenta argenti` strictly inside the casting-of-bases clause (`e quibus conflatæ sunt bases sanctuarii, et introitus, ubi velum pendet`), which is word-for-word `Studio Greek 39:4 / Saints 39:4a`. Shared quantity (100 silver talents) is insufficient to establish a full-verse match to `Saints 39:2`.
  4. The remaining `1,775` shekels appear in Latin only in the pillar-capital fabrication verse `38:28` (`Studio Greek 39:6 / Saints 39:5`).
- **Reconciled Studio rules (`_RULES['latin']`):**
  ```text
  exodus 38:24 = 39:1
  exodus 38:25 = 39:3
  exodus 38:26-27 = 39:4-5
  ```
- **Agreement Check:** `studio/lexica/versification.py`, `tests/test_lexica_versification.py`, `Modern-English-OT/parallel-verse-map.json`, `corrections/2026-11-24-modern-english-fidelity/verse-map.json`, and the translator note on `Exodus 38:25` now agree **100%** with zero contradictions.

---

## 3. Studio `versification.py` Cross-Edition Reconciliation (Greek Post-Stage-1 Integration)

In coordination with `@greek-mapper` (board #115), 5 stale post-Stage-1 Greek rules + 1 boundary refinement were independently verified word-for-word against live `studio.db` and `Saints.Bible` English and integrated into `studio/lexica/versification.py` + `tests/test_lexica_versification.py`:

- `exodus 39:14 > 39:13-14`, `exodus 39:15 = 39:15` (removed from `_DUPLICATE_OR_PLACEHOLDER`; added composition guards `exodus 39:33 = 39:13` in `_SITE_RULES['hebrew']` and `exodus 39:32 = 39:13` in `_SITE_RULES['latin']`).
- `leviticus 8:19 > 8:20-21`, `leviticus 8:20-29 = 8:21-30` (added `leviticus 8:20 = 8:20` guard in `_SITE_RULES['hebrew']` and `_SITE_RULES['latin']`).
- `numbers 21:20 = 21:21`, `numbers 21:21 = 21:22` (removed `21:20` from `_DUPLICATE_OR_PLACEHOLDER`; cleaned Hebrew/Latin `_RULES` `numbers 21:21 = 21:20`).
- `1-chronicles 12:4-5` and `nehemiah 12:17-19` restored to identity (removed `1-chronicles 12:5` from `_DUPLICATE_OR_PLACEHOLDER` and cleaned Hebrew `1-chronicles 12:5`).
- `sirach 41:23 = 41:26`, `sirach 41:24 = 41:27` (removed `41:23` from `_DUPLICATE_OR_PLACEHOLDER`; updated Latin `_RULES` `sirach 42:1 > 41:24,41:23,42:1` so Vulgate `42:1` retains all three clauses `41:26 + 41:27 + 42:1` -> `[(41, 27), (41, 26), (42, 1)]`).
- Verification: `python -B -m unittest tests.test_lexica_versification -v` -> **30/30 OK** (`0` unintended Hebrew/Latin `to_saints` deltas).

---

## 4. Full-Corpus 70-Book Parallel Map Reconciliation

- Regenerated `Modern-English-OT/parallel-verse-map.json` and `corrections/2026-11-24-modern-english-fidelity/verse-map.json` directly from `studio/lexica/versification.py`.
- Reconciled all **247** prior `parallel-verse-map.json` vs `versification.py` discrepancies (`23` target-order fixes + `224` target-set fixes, including previously broken omitted target `Numbers 6:27 -> 6:23`, `Exodus 36:10-33`, `37:11-12`, `37:20-22`, `38:30 -> [39:9, 39:7]`, `39:17-18`, `1 Kings 7:20, 7:31`, `Deuteronomy 6:13`, `Numbers 27:3-8`, `Daniel 3:67-70`, `Esther 15:1-3`, `Wisdom 5:14, 6:1, 6:23`, and `80` Sirach verses).
- **Post-reconciliation invariant check:** `0` broken Saints.Bible targets, `0` diffs between `parallel-verse-map.json`, `verse-map.json`, and `studio/lexica/versification.py` across all **70 books / 34,952 verses** (`46` books with non-identity mappings; `4,121` non-identity entries: `2,996` `shifted_or_reordered`, `589` `split_in_native`, `102` `merged_in_native`, `434` `unmatched_in_saints`).

---

## 5. Translator-Note Attachment & Cross-Reference Audit (`6,597` Notes; `30` Fixed)

- **Orphan notes:** `0` (`6,597 / 6,597` notes attached to valid native Vulgate verse keys).
- **Verified factual/mapping/cross-reference note bugs fixed (`30`, JSON + chapter Markdown 100% synced, `0` verse-text changes):**

| # | Native Ref | Saints Target(s) | Summary of Note Fix |
|---:|---|---|---|
| 1 | `1 Chronicles 6:28` | `6:13` | Stale internal verse cross-reference: Joel son of Samuel is native 6:33 (old Saints-aligned v. 18). |
| 2 | `1 Chronicles 6:34` | `6:19` | Stale internal verse cross-references: 'Cusi' is native 6:44 and 'Amasai' is native 6:46 (old Saints-aligned vv. 29-31). |
| 3 | `1 Maccabees 1:22` | `1:20` | Fixed inverted order claim: native 1:22 stands BEFORE the plundering of the sanctuary in native 1:23. |
| 4 | `1 Samuel 20:43` | `21:1` | Fixed stale Saints-perspective note ('one lower than here') to native Vulgate perspective. |
| 5 | `2 Kings 12:5` | `12:6` | Fixed shifted internal verse references: 'juxta ordinem suum' is in native 12:7 (not 12:8) and 'sartatecta' occurs in native vv. 5-8, 12 (not 6-9, 13). |
| 6 | `2 Maccabees 2:21` | `2:20` | Fixed shifted internal reference: 'illuminationibus' occurs in native 2:22 (not v. 21). |
| 7 | `Deuteronomy 6:11` | `6:11` | Fixed erroneous claim that 6:11-13 all map to Saints.Bible 6:11; native 6:13 maps to Saints.Bible 6:12-13. |
| 8 | `Exodus 38:25` | `39:3` | Added reconciled Rule 2 mapping note for Exod 38:25-27 and the absence of a full-verse Vulgate counterpart for Saints 39:2. |
| 9 | `Exodus 38:29` | `39:6` | Fixed factual error attributing 2,400 shekels to the Septuagint; Greek Exod 39:7 (Saints 39:6) reads 70 talents and 1,500 shekels. |
| 10 | `Exodus 39:1` | `36:8` | Fixed range endpoint: priestly garments span native 39:1-30 (39:31 maps to Saints 39:10). |
| 11 | `Joshua 21:21` | `21:21` | Fixed shifted internal verse reference: the last plural 'civitates fugitivorum' is native 21:37 (not v. 38). |
| 12 | `Joshua 21:36` | `21:36, 21:37` | Fixed internal verse reference: native v. 37 (not v. 38) encompasses Saints.Bible/Hebrew vv. 38-39. |
| 13 | `Leviticus 6:17` | `6:10` | Fixed shifted internal verse reference: 'thus' ('frankincense') is in native Lev 6:15 (old Saints-aligned 6:8). |
| 14 | `Nehemiah 10:27` | `10:28` | Fixed shifted internal verse reference: 'Harem' is in native Neh 10:5 (old Saints-aligned 10:6). |
| 15 | `Numbers 27:3` | `27:3, 27:4` | Fixed erroneous claim that 27:3-8 all map to Saints.Bible 27:3; aligned to exact Studio mapping. |
| 16 | `Sirach 13:18` | `(unmatched)` | Aligned note to versification.py: Sir 13:18 is an unmatched LXX-II/Vulgate expansion (Saints 13:14 is absent). |
| 17 | `Sirach 1:27` | `(unmatched)` | Aligned note to versification.py: Sir 1:27 is an unmatched LXX-II/Vulgate expansion (Saints 1:21 is absent). |
| 18 | `Sirach 20:4` | `(unmatched)` | Aligned note to versification.py: Sir 20:4 is an unmatched Vulgate/LXX-II expansion following Saints 20:3. |
| 19 | `Sirach 25:16` | `(unmatched)` | Aligned note to versification.py: Sir 25:16 is an unmatched LXX-II/Vulgate expansion (Saints 25:12 is absent). |
| 20 | `Sirach 27:19` | `27:17` | Fixed Saints target from 27:16-17 to 27:17b (matching versification.py). |
| 21 | `Sirach 2:10` | `(unmatched)` | Clarified Sir 2:10 is an unmatched Vulgate/LXX-II expansion following Saints 2:9. |
| 22 | `Sirach 30:20` | `30:19` | Fixed Saints target from 30:20 to 30:19b (matching versification.py and content of Saints 30:19). |
| 23 | `Sirach 30:21` | `30:20` | Fixed Saints target for 30:20 from 30:20 to 30:19b (matching versification.py). |
| 24 | `Sirach 33:29` | `33:28` | Fixed Saints target from 33:27b to 33:28b (matching versification.py). |
| 25 | `Sirach 33:33` | `33:33` | Fixed Saints target for 33:32-33 from 33:32b to 33:33 (matching versification.py). |
| 26 | `Sirach 35:3` | `(unmatched)` | Fixed false claim of parallel to Saints 35:3; native 35:3 is an unmatched Vulgate expansion and 35:5 maps to Saints 35:3. |
| 27 | `Sirach 36:2` | `36:1` | Fixed Saints target for 36:1-2 from 36:1-2 to 36:1 (matching versification.py). |
| 28 | `Sirach 41:26` | `41:23, 41:22` | Aligned Saints target from 41:22 to 41:22b/41:23a (matching versification.py [(41, 23), (41, 22)]). |
| 29 | `Sirach 42:1` | `41:27, 41:26, 42:1` | Fixed stale Saints target '41:23 and 42:1' (Swete numbering) to live Saints.Bible '41:26, 41:27, and 42:1'. |
| 30 | `Sirach 51:16` | `51:11` | Fixed stale 'Saints unplaced 51:11 / Greek 51:11b-12a' to exact live Saints.Bible 51:11b (continuing 51:15 = 51:10b-11a). |

---

## 6. Per-Book Status Breakdown (All 70 Books)

| Book | Total | `mapped_verified` | `reordered` | `split_or_merged` | `partial_correspondence` | `no_counterpart` | `unresolved` |
|---|---:|---:|---:|---:|---:|---:|---:|
| Genesis | 1530 | 1487 | 37 | 6 | 0 | 0 | 0 |
| Exodus | 1211 | 969 | 165 | 29 | 1 | 47 | 0 |
| Leviticus | 858 | 820 | 35 | 3 | 0 | 0 | 0 |
| Numbers | 1288 | 1154 | 117 | 16 | 1 | 0 | 0 |
| Deuteronomy | 959 | 881 | 75 | 3 | 0 | 0 | 0 |
| Joshua | 658 | 622 | 13 | 15 | 0 | 8 | 0 |
| Judges | 618 | 615 | 0 | 3 | 0 | 0 | 0 |
| Ruth | 85 | 85 | 0 | 0 | 0 | 0 | 0 |
| 1 Samuel | 811 | 754 | 16 | 1 | 1 | 39 | 0 |
| 2 Samuel | 695 | 651 | 44 | 0 | 0 | 0 | 0 |
| 1 Kings | 817 | 588 | 149 | 61 | 1 | 18 | 0 |
| 2 Kings | 719 | 696 | 22 | 0 | 0 | 1 | 0 |
| 1 Chronicles | 940 | 804 | 118 | 5 | 0 | 13 | 0 |
| 2 Chronicles | 822 | 788 | 33 | 0 | 0 | 1 | 0 |
| Ezra | 280 | 280 | 0 | 0 | 0 | 0 | 0 |
| Nehemiah | 404 | 306 | 78 | 6 | 0 | 14 | 0 |
| Esther | 275 | 156 | 0 | 114 | 2 | 3 | 0 |
| 1 Maccabees | 929 | 860 | 51 | 18 | 0 | 0 | 0 |
| 2 Maccabees | 558 | 535 | 17 | 6 | 0 | 0 | 0 |
| Job | 1070 | 990 | 76 | 3 | 0 | 1 | 0 |
| Psalms | 2527 | 2489 | 12 | 25 | 0 | 1 | 0 |
| Proverbs | 915 | 879 | 2 | 15 | 0 | 19 | 0 |
| Ecclesiastes | 222 | 192 | 30 | 0 | 0 | 0 | 0 |
| Song of Songs | 116 | 74 | 40 | 2 | 0 | 0 | 0 |
| Lamentations | 154 | 150 | 0 | 0 | 0 | 4 | 0 |
| Wisdom of Solomon | 439 | 364 | 62 | 10 | 0 | 3 | 0 |
| Sirach | 1592 | 394 | 722 | 427 | 1 | 48 | 0 |
| Isaiah | 1292 | 1254 | 32 | 4 | 0 | 2 | 0 |
| Jeremiah | 1363 | 587 | 704 | 4 | 1 | 67 | 0 |
| Ezekiel | 1272 | 1220 | 43 | 3 | 0 | 6 | 0 |
| Daniel | 531 | 348 | 56 | 6 | 0 | 121 | 0 |
| Hosea | 198 | 154 | 39 | 5 | 0 | 0 | 0 |
| Joel | 73 | 47 | 26 | 0 | 0 | 0 | 0 |
| Amos | 147 | 141 | 4 | 2 | 0 | 0 | 0 |
| Obadiah | 21 | 21 | 0 | 0 | 0 | 0 | 0 |
| Jonah | 48 | 48 | 0 | 0 | 0 | 0 | 0 |
| Micah | 104 | 93 | 10 | 1 | 0 | 0 | 0 |
| Nahum | 47 | 33 | 14 | 0 | 0 | 0 | 0 |
| Habakkuk | 56 | 56 | 0 | 0 | 0 | 0 | 0 |
| Zephaniah | 53 | 53 | 0 | 0 | 0 | 0 | 0 |
| Haggai | 38 | 14 | 24 | 0 | 0 | 0 | 0 |
| Zechariah | 211 | 194 | 17 | 0 | 0 | 0 | 0 |
| Malachi | 55 | 49 | 6 | 0 | 0 | 0 | 0 |
| Matthew | 1070 | 1053 | 13 | 1 | 0 | 3 | 0 |
| Mark | 677 | 623 | 48 | 1 | 0 | 5 | 0 |
| Luke | 1151 | 1143 | 0 | 7 | 0 | 1 | 0 |
| John | 879 | 855 | 20 | 3 | 0 | 1 | 0 |
| Acts | 1004 | 971 | 25 | 3 | 0 | 5 | 0 |
| Romans | 433 | 433 | 0 | 0 | 0 | 0 | 0 |
| 1 Corinthians | 437 | 437 | 0 | 0 | 0 | 0 | 0 |
| 2 Corinthians | 255 | 254 | 0 | 1 | 0 | 0 | 0 |
| Galatians | 149 | 149 | 0 | 0 | 0 | 0 | 0 |
| Ephesians | 155 | 155 | 0 | 0 | 0 | 0 | 0 |
| Philippians | 104 | 104 | 0 | 0 | 0 | 0 | 0 |
| Colossians | 95 | 95 | 0 | 0 | 0 | 0 | 0 |
| 1 Thessalonians | 89 | 89 | 0 | 0 | 0 | 0 | 0 |
| 2 Thessalonians | 47 | 47 | 0 | 0 | 0 | 0 | 0 |
| 1 Timothy | 113 | 113 | 0 | 0 | 0 | 0 | 0 |
| 2 Timothy | 83 | 80 | 0 | 3 | 0 | 0 | 0 |
| Titus | 46 | 46 | 0 | 0 | 0 | 0 | 0 |
| Philemon | 25 | 25 | 0 | 0 | 0 | 0 | 0 |
| Hebrews | 303 | 303 | 0 | 0 | 0 | 0 | 0 |
| James | 108 | 108 | 0 | 0 | 0 | 0 | 0 |
| 1 Peter | 105 | 105 | 0 | 0 | 0 | 0 | 0 |
| 2 Peter | 61 | 61 | 0 | 0 | 0 | 0 | 0 |
| 1 John | 105 | 105 | 0 | 0 | 0 | 0 | 0 |
| 2 John | 13 | 13 | 0 | 0 | 0 | 0 | 0 |
| 3 John | 14 | 13 | 0 | 1 | 0 | 0 | 0 |
| Jude | 25 | 25 | 0 | 0 | 0 | 0 | 0 |
| Revelation | 405 | 401 | 0 | 4 | 0 | 0 | 0 |
