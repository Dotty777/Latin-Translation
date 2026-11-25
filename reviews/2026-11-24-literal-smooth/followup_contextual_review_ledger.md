# Reconciled Revision-Pinned Latin (Sixto-Clementine Vulgate OT + NT) Evidence & Contextual-Review Ledger (v2.0 — Strict 5-Tier Taxonomy)

- **Date:** 2026-11-25 (Evidence & Reporting Reconciliation; **0** Bible verse-text, note, mapping, or Studio changes)
- **Adopted Source Corpus:** Saints-Latin-Critical-Text (Studio v10 Stage 1 `a0d022c1`, `Clem1598-USFX`, 70 books / 1,298 ch / 34,952 native Vulgate vv)
- **Pinned Text / Mapping Commit SHA:** `42be68737054f05e3aff49aa9b64a27841b7f120`
- **Revision Chain Audited:** `2fe6fcad` → `5261e1b6` → `892d426f` → `301d7f18` → `e99f55b0` → `f974b724` → `1f05ad75` → `907f6d85` → `1fc8f0c3` → `fef22edd` → `194da4ef` → `42be6873` (0 Bible text/note/mapping changes in evidence reconciliation)
- **Studio DB Snapshot:** `data/studio.db` (`seed_version = 10`, SHA-256 `23f39dbdcbc4599b1ed783bfce8a0b6268610e5dde6c200e114057798e64761d`)
- **Machine-Readable Ledgers:** `followup_contextual_review_ledger.json` & `scratch/followup/latin_contextual_ledger.jsonl` (`4,916` deduplicated citations retained after removing `0` exact duplicates)

## 1. Strict 5-Tier Evidence Totals (Each Native Reference Counted Once at Strongest Level)

> **Standard Applied Uniformly Across All Three Editions:** A passage is credited as `full_source_in_context_read` **only** where surviving evidence proves the reviewer compared its English against the adopted source in the surrounding paragraph, speech, or literary unit. Note checks, mapping checks, and isolated wording checks are classified under `targeted_evidence` (with explicit subtype counts and overlap). Batch scans, zero-change book claims, and unexpanded multi-verse issue-title ranges are strictly excluded. An earlier read supports the final revision **only** after programmatically confirming that the reviewed source text, English text, and relevant surrounding context (`±2` native verses / exact Pass 3.5 blind packet context) match final `HEAD` byte-for-byte.

| Strongest Documented Evidence Level | Distinct Native Verses | Share | Supports Final Revision (`true`) | Historical Only (`false`) | Strict Whole-Chapter Final Match |
|---|---:|---:|---:|---:|---:|
| **`full_source_in_context_read`** | **40** | **0.11%** | **37** | **3** | 37 |
| **`targeted_evidence`** *(note / mapping / isolated wording)* | **2,294** | **6.56%** | **2,175** | **119** | — |
| **`english_only_read`** *(Pass 3 standalone English)* | **837** | **2.39%** | **833** | **4** | — |
| **`automated_screening_only`** | **31,781** | **90.93%** | 31,781 | 0 | — |
| **`insufficient_evidence`** | **0** | **0.00%** | 0 | 0 | — |
| **TOTAL (`source_total` — exact partition)** | **34,952** | **100.00%** | — | — | — |

*Separate Editorial Status (NEVER merged with evidence depth): `verified` = **34,873**, `disputed` / `awaiting_human_signoff` = **79**, `unverified` = **0** (`34,873 + 79 = 34,952`).*

### Targeted Evidence Breakdown & Subtype Overlap

| Disjoint Targeted-Tier Subset | Distinct Native Verses | Share of Targeted Tier |
|---|---:|---:|
| `note_check` only | 542 | 23.63% |
| `mapping_check` only | 88 | 3.84% |
| `isolated_wording_check` only | 1,002 | 43.68% |
| `note_check` + `mapping_check` | 108 | 4.71% |
| `note_check` + `isolated_wording_check` | 403 | 17.57% |
| `mapping_check` + `isolated_wording_check` | 52 | 2.27% |
| `note_check` + `mapping_check` + `isolated_wording_check` | 99 | 4.32% |
| **TOTAL (`targeted_evidence` strongest tier)** | **2,294** | **100.00%** |

- **Targeted-tier check totals (non-disjoint across subtypes):** `note_check = 1,152`, `mapping_check = 347`, `isolated_wording_check = 1,556`, **multi-subtype overlap (`2+` subtypes) = `662`** (of which `note ∩ map = 207`).
- **Gross corpus-wide checks (including overlaps on `full_source_in_context_read` passages):** `note_check = 1,162` (`10` also in full), `mapping_check = 352` (`5` also in full), `isolated_wording_check = 1,567` (`11` also in full), `english_only_read = 1,266` (`5` also in full, `424` also in targeted).

## 2. Reclassification Audit (Previous Follow-Up Ledger → Strict 5-Tier Ledger)

| Previous Ledger Class → Reconciled 5-Tier Class | Distinct Native Verses | Explanation |
|---|---:|---|
| `old_auto_only -> automated_screening_only` | 31,781 | Unchanged automated screening only |
| `old_doc_src_ctx -> full_source_in_context_read` | 40 | Confirmed genuine full source-in-context read (Pass 3.5 blind review or recovered Greek helper range) |
| `old_doc_src_ctx -> targeted_evidence` | 2,294 | Reclassified from undifferentiated prior bucket into targeted note / mapping / isolated wording check |
| `old_p3_eng_only -> english_only_read` | 837 | Retained as Pass 3 standalone English-only read |

## 3. Unique Native Verses by Pass & Evidence Class

| Pass | Evidence Class | Unique Native Verses |
|---|---|---:|
| `followup-mapping-audit` | `targeted_evidence` | 136 |
| `pass1-fidelity` | `targeted_evidence` | 1,041 |
| `pass2-peer` | `targeted_evidence` | 1,057 |
| `pass35-peer-response` | `targeted_evidence` | 36 |
| `pass3b-peer` | `targeted_evidence` | 40 |
| `pass4-peer` | `targeted_evidence` | 17 |
| `pass4-reconciliation` | `targeted_evidence` | 126 |
| `pre-stage1-verse-review` | `targeted_evidence` | 1,157 |
| `stage2-pass3-standalone-flow` | `english_only_read` | 1,266 |
| `stage2_pass35_blind_ai_peer_review` | `full_source_in_context_read` | 40 |

## 4. Unassigned Aggregate Claims & Batch Scans (`0` Verses Assigned)

- **`LAT-AGG-01`** (`corrections/2026-11-24-modern-english-fidelity/README.md`, claimed `34,363`): No per-verse log for unchanged verses; 348 edition-wide consistency/note batch rows strictly excluded.
- **`LAT-AGG-02`** (`pass1_summary.md & pass1_proposals.jsonl`, claimed `34,952`): Programmatic sweeps (687 Genesis diffs, 33 length outliers, 137 negations) and 50 bulk structural range rows (kept anchor-only; bulk ranges unexpanded).
- **`LAT-AGG-03`** (`pass2_summary.md & pass2_coverage.json`, claimed `34,952`): Editorial status totals (34,873 verified / 79 disputed) kept strictly separate from reading evidence.
- **`LAT-AGG-04`** (`pass3_summary.md`, claimed `34,952`): Full-corpus programmatic typography/quote sweeps; only 41 explicitly named chapters + Bucket A/B items enter english_only_read.
- **`LAT-AGG-05`** (`pass35_ai_peer_review_response.jsonl#LAT-P35-SWEEP-01,02`, claimed `802`): Unenumerated pattern sweeps (290 unplaced, 467 restored, 16+14+15 phrase checks); only specifically named fixes and 16 named loci enter targeted_evidence.
- **`LAT-AGG-06`** (`pass4_summary.md & pass4_bounceback_verdicts.jsonl#P4-LAT-10`, claimed `34,952`): Programmatic reconciliation + 118 parallel-map metadata cleanups; only individually cited verses enter targeted_evidence.
- **`LAT-AGG-07`** (`followup_mapping_decisions.jsonl (programmatic parallel-verse-map parity rows)`, claimed `4,121`): Bulk programmatic regeneration of non-identity parallel-verse-map.json rows from Studio versification.py; only the 106 hand-audited priority/edge-cluster mapping loci and 30 verified note fixes enter targeted_evidence.

## 5. Complete Per-Book 5-Tier Evidence Breakdown (70 Books, Summing to `34,952`)

| # | Book | Test. | Ch | `source_total` | `full_src_ctx` *(fin / hist)* | `targeted` *(fin / hist)* | `tgt_note` | `tgt_map` | `tgt_word` | `tgt_ov2+` | `eng_only` | `auto_only` | `insuff_ev` | Ed. `verified` / `disputed` *(sep.)* |
|---:|---|:---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Genesis | OT | 50 | 1,530 | 1 (1/0) | 217 (209/8) | 79 | 2 | 179 | 43 | 20 | 1,292 | 0 | 1,530 / 0 |
| 2 | Exodus | OT | 40 | 1,211 | 2 (2/0) | 112 (107/5) | 41 | 59 | 65 | 45 | 73 | 1,024 | 0 | 1,211 / 0 |
| 3 | Leviticus | OT | 27 | 858 | 0 (0/0) | 38 (35/3) | 16 | 8 | 25 | 8 | 35 | 785 | 0 | 858 / 0 |
| 4 | Numbers | OT | 36 | 1,288 | 1 (1/0) | 67 (65/2) | 38 | 30 | 21 | 16 | 23 | 1,197 | 0 | 1,288 / 0 |
| 5 | Deuteronomy | OT | 34 | 959 | 2 (2/0) | 28 (27/1) | 14 | 5 | 17 | 6 | 21 | 908 | 0 | 959 / 0 |
| 6 | Joshua | OT | 24 | 658 | 0 (0/0) | 30 (30/0) | 16 | 4 | 20 | 9 | 0 | 628 | 0 | 658 / 0 |
| 7 | Judges | OT | 21 | 618 | 0 (0/0) | 18 (18/0) | 10 | 0 | 11 | 3 | 0 | 600 | 0 | 617 / 1 |
| 8 | Ruth | OT | 4 | 85 | 0 (0/0) | 1 (1/0) | 0 | 0 | 1 | 0 | 0 | 84 | 0 | 85 / 0 |
| 9 | 1 Samuel | OT | 31 | 811 | 1 (1/0) | 20 (19/1) | 6 | 5 | 11 | 2 | 2 | 788 | 0 | 811 / 0 |
| 10 | 2 Samuel | OT | 24 | 695 | 1 (1/0) | 14 (13/1) | 9 | 1 | 6 | 1 | 3 | 677 | 0 | 695 / 0 |
| 11 | 1 Kings | OT | 22 | 817 | 1 (1/0) | 43 (32/11) | 20 | 15 | 22 | 13 | 83 | 690 | 0 | 817 / 0 |
| 12 | 2 Kings | OT | 25 | 719 | 0 (0/0) | 19 (19/0) | 7 | 2 | 12 | 2 | 0 | 700 | 0 | 719 / 0 |
| 13 | 1 Chronicles | OT | 29 | 940 | 1 (1/0) | 30 (29/1) | 24 | 4 | 9 | 7 | 2 | 907 | 0 | 937 / 3 |
| 14 | 2 Chronicles | OT | 36 | 822 | 0 (0/0) | 28 (26/2) | 12 | 1 | 17 | 2 | 0 | 794 | 0 | 822 / 0 |
| 15 | Ezra | OT | 10 | 280 | 0 (0/0) | 8 (8/0) | 3 | 0 | 6 | 1 | 0 | 272 | 0 | 280 / 0 |
| 16 | Nehemiah | OT | 13 | 404 | 1 (0/1) | 12 (11/1) | 9 | 5 | 5 | 6 | 0 | 391 | 0 | 404 / 0 |
| 17 | Esther | OT | 16 | 275 | 1 (1/0) | 112 (112/0) | 27 | 19 | 110 | 35 | 2 | 160 | 0 | 275 / 0 |
| 18 | 1 Maccabees | OT | 16 | 929 | 0 (0/0) | 32 (32/0) | 12 | 2 | 26 | 8 | 0 | 897 | 0 | 929 / 0 |
| 19 | 2 Maccabees | OT | 15 | 558 | 0 (0/0) | 15 (15/0) | 8 | 1 | 9 | 3 | 0 | 543 | 0 | 558 / 0 |
| 20 | Job | OT | 42 | 1,070 | 1 (1/0) | 60 (54/6) | 21 | 1 | 43 | 5 | 77 | 932 | 0 | 1,069 / 1 |
| 21 | Psalms | OT | 150 | 2,527 | 3 (3/0) | 115 (114/1) | 66 | 8 | 65 | 23 | 32 | 2,377 | 0 | 2,517 / 10 |
| 22 | Proverbs | OT | 31 | 915 | 1 (1/0) | 40 (40/0) | 25 | 8 | 20 | 10 | 0 | 874 | 0 | 915 / 0 |
| 23 | Ecclesiastes | OT | 12 | 222 | 0 (0/0) | 10 (7/3) | 5 | 1 | 5 | 1 | 0 | 212 | 0 | 222 / 0 |
| 24 | Song of Songs | OT | 8 | 116 | 0 (0/0) | 17 (16/1) | 8 | 1 | 10 | 2 | 0 | 99 | 0 | 116 / 0 |
| 25 | Lamentations | OT | 5 | 154 | 0 (0/0) | 5 (5/0) | 3 | 0 | 4 | 2 | 0 | 149 | 0 | 153 / 1 |
| 26 | Wisdom of Solomon | OT | 19 | 439 | 2 (2/0) | 31 (31/0) | 22 | 15 | 21 | 16 | 1 | 405 | 0 | 438 / 1 |
| 27 | Sirach | OT | 51 | 1,592 | 4 (4/0) | 301 (282/19) | 263 | 54 | 224 | 214 | 109 | 1,178 | 0 | 1,592 / 0 |
| 28 | Isaiah | OT | 66 | 1,292 | 1 (1/0) | 90 (88/2) | 68 | 1 | 45 | 23 | 7 | 1,194 | 0 | 1,275 / 17 |
| 29 | Jeremiah | OT | 52 | 1,363 | 0 (0/0) | 133 (93/40) | 58 | 14 | 96 | 32 | 38 | 1,192 | 0 | 1,359 / 4 |
| 30 | Ezekiel | OT | 48 | 1,272 | 2 (1/1) | 97 (96/1) | 41 | 8 | 64 | 15 | 27 | 1,146 | 0 | 1,264 / 8 |
| 31 | Daniel | OT | 14 | 531 | 2 (2/0) | 158 (156/2) | 39 | 46 | 124 | 43 | 0 | 371 | 0 | 524 / 7 |
| 32 | Hosea | OT | 14 | 198 | 1 (1/0) | 19 (19/0) | 13 | 3 | 10 | 5 | 0 | 178 | 0 | 198 / 0 |
| 33 | Joel | OT | 3 | 73 | 1 (1/0) | 9 (7/2) | 6 | 1 | 4 | 1 | 0 | 63 | 0 | 73 / 0 |
| 34 | Amos | OT | 9 | 147 | 0 (0/0) | 8 (8/0) | 5 | 1 | 5 | 2 | 2 | 137 | 0 | 147 / 0 |
| 35 | Obadiah | OT | 1 | 21 | 0 (0/0) | 1 (1/0) | 1 | 0 | 0 | 0 | 0 | 20 | 0 | 21 / 0 |
| 36 | Jonah | OT | 4 | 48 | 0 (0/0) | 4 (4/0) | 3 | 0 | 1 | 0 | 0 | 44 | 0 | 48 / 0 |
| 37 | Micah | OT | 7 | 104 | 0 (0/0) | 14 (14/0) | 13 | 0 | 6 | 5 | 0 | 90 | 0 | 99 / 5 |
| 38 | Nahum | OT | 3 | 47 | 0 (0/0) | 2 (2/0) | 1 | 0 | 1 | 0 | 0 | 45 | 0 | 47 / 0 |
| 39 | Habakkuk | OT | 3 | 56 | 0 (0/0) | 2 (2/0) | 0 | 0 | 2 | 0 | 0 | 54 | 0 | 56 / 0 |
| 40 | Zephaniah | OT | 3 | 53 | 0 (0/0) | 1 (1/0) | 1 | 0 | 0 | 0 | 0 | 52 | 0 | 53 / 0 |
| 41 | Haggai | OT | 2 | 38 | 0 (0/0) | 3 (3/0) | 3 | 1 | 2 | 2 | 0 | 35 | 0 | 37 / 1 |
| 42 | Zechariah | OT | 14 | 211 | 0 (0/0) | 21 (21/0) | 17 | 0 | 15 | 11 | 0 | 190 | 0 | 200 / 11 |
| 43 | Malachi | OT | 4 | 55 | 0 (0/0) | 11 (11/0) | 8 | 6 | 7 | 7 | 0 | 44 | 0 | 53 / 2 |
| 44 | Matthew | NT | 28 | 1,070 | 3 (3/0) | 36 (35/1) | 14 | 1 | 27 | 5 | 46 | 985 | 0 | 1,069 / 1 |
| 45 | Mark | NT | 16 | 677 | 3 (2/1) | 34 (30/4) | 11 | 1 | 25 | 2 | 0 | 640 | 0 | 677 / 0 |
| 46 | Luke | NT | 24 | 1,151 | 1 (1/0) | 47 (46/1) | 14 | 1 | 34 | 1 | 0 | 1,103 | 0 | 1,151 / 0 |
| 47 | John | NT | 21 | 879 | 0 (0/0) | 23 (23/0) | 6 | 1 | 18 | 2 | 69 | 787 | 0 | 879 / 0 |
| 48 | Acts | NT | 28 | 1,004 | 0 (0/0) | 34 (34/0) | 19 | 9 | 17 | 9 | 4 | 966 | 0 | 1,004 / 0 |
| 49 | Romans | NT | 16 | 433 | 0 (0/0) | 23 (23/0) | 8 | 0 | 17 | 2 | 63 | 347 | 0 | 431 / 2 |
| 50 | 1 Corinthians | NT | 16 | 437 | 0 (0/0) | 12 (12/0) | 5 | 0 | 8 | 1 | 0 | 425 | 0 | 437 / 0 |
| 51 | 2 Corinthians | NT | 13 | 255 | 0 (0/0) | 10 (10/0) | 4 | 0 | 7 | 1 | 1 | 244 | 0 | 254 / 1 |
| 52 | Galatians | NT | 6 | 149 | 0 (0/0) | 5 (5/0) | 3 | 0 | 4 | 2 | 18 | 126 | 0 | 147 / 2 |
| 53 | Ephesians | NT | 6 | 155 | 1 (1/0) | 8 (8/0) | 4 | 0 | 6 | 2 | 0 | 146 | 0 | 154 / 1 |
| 54 | Philippians | NT | 4 | 104 | 0 (0/0) | 3 (3/0) | 1 | 0 | 3 | 1 | 0 | 101 | 0 | 104 / 0 |
| 55 | Colossians | NT | 4 | 95 | 0 (0/0) | 4 (4/0) | 0 | 0 | 4 | 0 | 0 | 91 | 0 | 95 / 0 |
| 56 | 1 Thessalonians | NT | 5 | 89 | 0 (0/0) | 0 (0/0) | 0 | 0 | 0 | 0 | 0 | 89 | 0 | 89 / 0 |
| 57 | 2 Thessalonians | NT | 3 | 47 | 0 (0/0) | 1 (1/0) | 0 | 0 | 1 | 0 | 0 | 46 | 0 | 47 / 0 |
| 58 | 1 Timothy | NT | 6 | 113 | 0 (0/0) | 6 (6/0) | 0 | 0 | 6 | 0 | 0 | 107 | 0 | 113 / 0 |
| 59 | 2 Timothy | NT | 4 | 83 | 0 (0/0) | 2 (2/0) | 1 | 1 | 1 | 1 | 0 | 81 | 0 | 83 / 0 |
| 60 | Titus | NT | 3 | 46 | 0 (0/0) | 4 (4/0) | 2 | 0 | 2 | 0 | 0 | 42 | 0 | 46 / 0 |
| 61 | Philemon | NT | 1 | 25 | 0 (0/0) | 1 (1/0) | 1 | 0 | 0 | 0 | 0 | 24 | 0 | 25 / 0 |
| 62 | Hebrews | NT | 13 | 303 | 1 (1/0) | 14 (14/0) | 4 | 0 | 10 | 0 | 40 | 248 | 0 | 303 / 0 |
| 63 | James | NT | 5 | 108 | 0 (0/0) | 3 (3/0) | 2 | 0 | 2 | 1 | 0 | 105 | 0 | 108 / 0 |
| 64 | 1 Peter | NT | 5 | 105 | 0 (0/0) | 0 (0/0) | 0 | 0 | 0 | 0 | 0 | 105 | 0 | 105 / 0 |
| 65 | 2 Peter | NT | 3 | 61 | 0 (0/0) | 3 (3/0) | 2 | 0 | 1 | 0 | 0 | 58 | 0 | 61 / 0 |
| 66 | 1 John | NT | 5 | 105 | 0 (0/0) | 5 (5/0) | 2 | 0 | 3 | 0 | 0 | 100 | 0 | 105 / 0 |
| 67 | 2 John | NT | 1 | 13 | 0 (0/0) | 0 (0/0) | 0 | 0 | 0 | 0 | 13 | 0 | 0 | 13 / 0 |
| 68 | 3 John | NT | 1 | 14 | 0 (0/0) | 0 (0/0) | 0 | 0 | 0 | 0 | 0 | 14 | 0 | 14 / 0 |
| 69 | Jude | NT | 1 | 25 | 0 (0/0) | 2 (2/0) | 1 | 0 | 1 | 0 | 0 | 23 | 0 | 25 / 0 |
| 70 | Revelation | NT | 22 | 405 | 1 (1/0) | 18 (18/0) | 7 | 1 | 13 | 3 | 26 | 360 | 0 | 405 / 0 |
| — | **TOTAL (70 books)** | — | **1,298** | **34,952** | **40** (37/3) | **2,294** (2,175/119) | **1,152** | **347** | **1,556** | **662** | **837** | **31,781** | **0** | **34,873 / 79** |
