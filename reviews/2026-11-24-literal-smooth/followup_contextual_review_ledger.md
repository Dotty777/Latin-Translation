# Follow-Up Revision-Pinned Latin Contextual-Review Ledger & Post-Edit Reread Audit

- **Auditor:** `@latin-studio-mapper`
- **Edition:** `Latin` (`Clem1598-USFX`, 70 books, 1,298 chapters, `34,952` native Vulgate verses)
- **Final Text & Notes SHA:** `194da4efff48ae46fedee5a58924b684f37c683d` (0 English verse text changes after Pass 3.5 `1f05ad75`)
- **Wording Proposals (`latin_wording_proposals.jsonl`):** `0` (no meaning-changing English wording defects discovered)

---

## 1. Strict-Honesty Corpus Coverage Accounting (`34,952` Native Vulgate Verses)

Only verses with **individually documented contextual reads** (single verse or explicitly documented exact range/full chapter) in existing reviewer logs are counted as `documented_contextual_read`. Aggregate-only claims without per-verse logs are separated below under **Unattributed Aggregate Claims** and left in `automated_screening_only`.

| Coverage Category (Mutually Exclusive) | Distinct Native Verses | Share | Notes |
|---|---:|---:|---|
| **`documented_contextual_read`** | **3,171** | **9.07%** | Deduplicated across all passes (`4,916` total pass-level ledger entries) |
| &nbsp;&nbsp;↳ `source_checked_contextual_read` | 2,334 | 6.68% | Verified against adopted Latin (`Clem1598-USFX` or `Studio v9` pre-Stage-1) |
| &nbsp;&nbsp;↳ `english_only_standalone_read_only` | 837 | 2.39% | Read ONLY in Pass 3 standalone English (`@lat-flow`), without a separate source-checked read log |
| **`automated_screening_only`** | **31,781** | **90.93%** | Screened by full-corpus programmatic checks (schema, placeholders, archaisms, spelling, quote-stack, JSON↔MD sync, versification) with no individual contextual-read record |
| **`insufficient_evidence`** | **0** | **0.00%** | Zero books/verses lacked automated full-corpus screening |
| **Total (`source_total`)** | **34,952** | **100.00%** | Exact sum (`3,171 + 31,781 + 0 = 34,952`) |

> **Pre-follow-up baseline (before `@latin-studio-mapper`):** `3,133` distinct documented contextual reads (`2,265` source-checked + `868` English-only standalone).

### Editorial Statuses (Kept Strictly Separate from Reading Coverage)

| Editorial Status (`pass2_coverage.json`) | Verse Count | Meaning |
|---|---:|---|
| `verified` | 34,873 | Stage 2 completion status (no open human-editor dispute) — **NOT** a claim of individual verse-by-verse contextual read logs |
| `disputed` / `awaiting_human_signoff` | 79 | Open human-editor queue items (`pass2_human_editor_queue.jsonl`, 72 verse entries expanding Ps 109:1-7 + 2 Cor 4:4) |

### Ledger Entries by Review Pass (Deduplicated Within Each Pass)

| Pass | Reviewer | Entries | Review Mode |
|---|---|---:|---|
| `pre-stage1-verse-review` | `pre-stage1-parallel-reviewers` | 1,157 | source_checked (Studio v9 @ 2fe6fcad) |
| `pass1-fidelity` | `@lat-fidelity` | 1,041 | source_checked (Clem1598-USFX @ 5261e1b6) |
| `pass2-peer` | `@lat-peer` | 1,057 | source_checked (Clem1598-USFX @ 5261e1b6 -> 892d426f) |
| `pass3-standalone-flow` | `@lat-flow` | 1,266 | standalone_english_only (496b9f9d -> 301d7f18) |
| `pass3b-peer` | `@lat-peer` | 40 | source_checked (301d7f18 -> e99f55b0) |
| `pass35-blind-ai-peer-review` | `@ai-peer-review` | 40 | source_checked (CTS a0d022c1 @ f974b724) |
| `pass35-peer-response` | `@lat-peer` | 36 | source_checked (5261e1b6 -> 1f05ad75) |
| `pass4-reconciliation` | `@reconciliation` | 126 | source_checked (5261e1b6 @ 907f6d85) |
| `pass4-peer` | `@lat-peer` | 17 | source_checked (5261e1b6 -> 1fc8f0c3) |
| `followup-mapping-audit` | `@latin-studio-mapper` | 136 | source_checked (5261e1b6 -> 194da4ef) |

---

## 2. Unattributed Aggregate Claims (NOT Counted as `documented_contextual_read`)

| ID | Source File | Claimed Count | Why Excluded from Per-Verse Contextual Reads |
|---|---|---:|---|
| `LAT-AGG-01` | `corrections/2026-11-24-modern-english-fidelity/README.md` | 34,363 | Pre-Stage-1 README reports 79 parallel reviewers checked 34,070 canonical + 293 unplaced verses, but individual per-verse logs exist ONLY for the 1,218 changed 'verse-review' rows in wording-changes.jsonl (348 'edition-wide' batch sweep rows are automated consistency edits, not contextual reads). Unchanged verses without per-verse logs remain in automated_screening_only. |
| `LAT-AGG-02` | `reviews/2026-11-24-literal-smooth/pass1_summary.md & pass1_coverage.json` | 34,952 | Pass 1 reports auditing all 34,952 adopted Clem1598-USFX verses (including 687 Genesis diffs, 33 length outliers, 137 negation mismatches, and 50 broad structural native_order_mapping/punctuation_policy range rows in pass1_proposals.jsonl such as Job 13:1-31:40, Sir 30:1-36:28, Jer 25:15-51:64). Only individually named/quoted verses are counted in documented_contextual_read; unenumerated verses remain in automated_screening_only. |
| `LAT-AGG-03` | `reviews/2026-11-24-literal-smooth/pass2_summary.md & pass2_coverage.json` | 34,952 | Pass 2 reports 34,873 verified + 79 disputed = 34,952 across 70 books. Individual peer-review evidence exists for the 1,035 pass2_verdicts.jsonl entries (single-verse + explicit small ranges + anchor verses) and 24 explicitly named bonus/boundary catches; the remaining unchanged verses have no per-verse read log and remain in automated_screening_only. |
| `LAT-AGG-04` | `reviews/2026-11-24-literal-smooth/pass3_summary.md` | 34,952 | Pass 3 ran full-corpus automated typography, archaism, spelling, and quotation-stack sweeps over 34,952 verses / 6,597 notes, plus standalone English-only contextual reads of 41 explicitly named chapters (§3) and 54 Bucket A/B items + named boundary loci (§2). Only those explicitly named chapters/loci enter documented_contextual_read (tagged standalone_english_only); the remaining corpus is automated_screening_only. |
| `LAT-AGG-05` | `reviews/2026-11-24-literal-smooth/pass35_ai_peer_review_response.jsonl#LAT-P35-SWEEP-01,LAT-P35-SWEEP-02` | 802 | Pass 3.5 pattern-expansion sweep logs cite aggregate sets (290 pre-Pass-2 unplaced, 467 restored verses, 16 convers* est/sunt ad, 14 Prophets convers*, 15 dimidi* part*) without per-verse logs for unchanged items. Only the 40 blind samples, 10 verified fix records, 15 named NT Vulgate loci, and Isa 60:5 enter documented_contextual_read. |
| `LAT-AGG-06` | `scratch/reconciliation/pass4_summary.md & reviews/2026-11-24-literal-smooth/pass2_summary.md#§8` | 34,952 | Pass 4 reports 0 unexplained discrepancies across all 34,952 Latin verses and 118 parallel-map metadata cleanups (P4-LAT-10). Only the 121 rows with explicit native_refs.lat in pass4_reconciliation.jsonl and P4-LAT-01..09 enter documented_contextual_read. |

---

## 3. Post-Edit Reread Audit (`5261e1b6` → Final Revision)

- **Verbatim-relocated only in Pass 2 (`5261e1b6 -> 892d426f`):** `3,105` verses (identical English text moved from Saints-aligned key to native Vulgate key; excluded from genuine text-edit count).
- **Verses with genuine English text creation/modification since `5261e1b6`:** **`1,250`**
  - **`reread_on_final_revision: true`:** `414` (`127` source-checked + `287` Pass 3 English-only)
  - **`reread_on_final_revision: false`:** `836`
- **Adjacent-context-only affected verses (`v±1`, own text unchanged):** `1,079` (`reread_true=127`, `reread_false=952`).

### Breakdown by Commit of Final English Text Edit

| Final Text-Edit Pass | Commit SHA | Edited Verses | Reread on Final Rev (`true`) | Source-Checked Reread | English-Only Reread | NOT Reread (`false`) |
|---|---|---:|---:|---:|---:|---:|
| `pass2-migration-and-edits` | `892d426f` | 1,202 | 411 | 124 | 287 | 791 |
| `pass3a-surface-edits` | `301d7f18` | 20 | 0 | 0 | 0 | 20 |
| `pass3b-peer-edits` | `e99f55b0` | 12 | 0 | 0 | 0 | 12 |
| `pass35-peer-edits` | `1f05ad75` | 16 | 3 | 3 | 0 | 13 |

### Complete Verse-by-Verse Post-Pass-2 Text-Edit Reread Table (`48` Verses Edited in Pass 3A / 3B / 3.5)

| Native Ref | Final Text-Edit Pass | Edit SHA | `reread_on_final_revision` | Reread Pass & SHA | Evidence |
|---|---|---|---|---|---|
| `Ezekiel 26:2` | `pass35-peer-edits` | `1f05ad75` | `true` | `pass4-reconciliation` (`907f6d85`) | `scratch/reconciliation/pass4_reconciliation.jsonl#P4-REC-091` |
| `Ezekiel 33:25` | `pass35-peer-edits` | `1f05ad75` | `false` | — | *(not reread after edit)* |
| `Ezekiel 33:26` | `pass35-peer-edits` | `1f05ad75` | `false` | — | *(not reread after edit)* |
| `Jeremiah 33:24` | `pass35-peer-edits` | `1f05ad75` | `false` | — | *(not reread after edit)* |
| `Jeremiah 33:26` | `pass35-peer-edits` | `1f05ad75` | `false` | — | *(not reread after edit)* |
| `Jeremiah 51:44` | `pass35-peer-edits` | `1f05ad75` | `false` | — | *(not reread after edit)* |
| `Jeremiah 51:48` | `pass35-peer-edits` | `1f05ad75` | `false` | — | *(not reread after edit)* |
| `Mark 7:15` | `pass35-peer-edits` | `1f05ad75` | `false` | — | *(not reread after edit)* |
| `Mark 7:16` | `pass35-peer-edits` | `1f05ad75` | `true` | `pass4-reconciliation` (`907f6d85`) | `scratch/reconciliation/pass4_reconciliation.jsonl#P4-REC-090` |
| `Mark 9:42` | `pass35-peer-edits` | `1f05ad75` | `false` | — | *(not reread after edit)* |
| `Mark 9:43` | `pass35-peer-edits` | `1f05ad75` | `false` | — | *(not reread after edit)* |
| `Mark 9:44` | `pass35-peer-edits` | `1f05ad75` | `false` | — | *(not reread after edit)* |
| `Mark 9:45` | `pass35-peer-edits` | `1f05ad75` | `false` | — | *(not reread after edit)* |
| `Mark 11:25` | `pass35-peer-edits` | `1f05ad75` | `false` | — | *(not reread after edit)* |
| `Mark 11:26` | `pass35-peer-edits` | `1f05ad75` | `false` | — | *(not reread after edit)* |
| `Nehemiah 4:6` | `pass35-peer-edits` | `1f05ad75` | `true` | `pass4-peer` (`1fc8f0c3`) | `reviews/2026-11-24-literal-smooth/pass4_bounceback_verdicts.jsonl#P4-LAT-04` |
| `1 Kings 5:17` | `pass3a-surface-edits` | `301d7f18` | `false` | — | *(not reread after edit)* |
| `1 Kings 11:1` | `pass3a-surface-edits` | `301d7f18` | `false` | — | *(not reread after edit)* |
| `2 Corinthians 10:14` | `pass3a-surface-edits` | `301d7f18` | `false` | — | *(not reread after edit)* |
| `Esther 1:2` | `pass3a-surface-edits` | `301d7f18` | `false` | — | *(not reread after edit)* |
| `Exodus 37:6` | `pass3a-surface-edits` | `301d7f18` | `false` | — | *(not reread after edit)* |
| `Exodus 37:15` | `pass3a-surface-edits` | `301d7f18` | `false` | — | *(not reread after edit)* |
| `Exodus 39:41` | `pass3a-surface-edits` | `301d7f18` | `false` | — | *(not reread after edit)* |
| `Jeremiah 27:7` | `pass3a-surface-edits` | `301d7f18` | `false` | — | *(not reread after edit)* |
| `Jeremiah 46:26` | `pass3a-surface-edits` | `301d7f18` | `false` | — | *(not reread after edit)* |
| `Sirach 3:9` | `pass3a-surface-edits` | `301d7f18` | `false` | — | *(not reread after edit)* |
| `Sirach 32:2` | `pass3a-surface-edits` | `301d7f18` | `false` | — | *(not reread after edit)* |
| `Sirach 32:4` | `pass3a-surface-edits` | `301d7f18` | `false` | — | *(not reread after edit)* |
| `Sirach 32:22` | `pass3a-surface-edits` | `301d7f18` | `false` | — | *(not reread after edit)* |
| `Sirach 37:15` | `pass3a-surface-edits` | `301d7f18` | `false` | — | *(not reread after edit)* |
| `Sirach 41:1` | `pass3a-surface-edits` | `301d7f18` | `false` | — | *(not reread after edit)* |
| `Sirach 41:3` | `pass3a-surface-edits` | `301d7f18` | `false` | — | *(not reread after edit)* |
| `Sirach 44:22` | `pass3a-surface-edits` | `301d7f18` | `false` | — | *(not reread after edit)* |
| `Sirach 45:10` | `pass3a-surface-edits` | `301d7f18` | `false` | — | *(not reread after edit)* |
| `Sirach 46:1` | `pass3a-surface-edits` | `301d7f18` | `false` | — | *(not reread after edit)* |
| `Sirach 51:6` | `pass3a-surface-edits` | `301d7f18` | `false` | — | *(not reread after edit)* |
| `1 Kings 11:38` | `pass3b-peer-edits` | `e99f55b0` | `false` | — | *(not reread after edit)* |
| `1 Kings 11:39` | `pass3b-peer-edits` | `e99f55b0` | `false` | — | *(not reread after edit)* |
| `Ezekiel 16:23` | `pass3b-peer-edits` | `e99f55b0` | `false` | — | *(not reread after edit)* |
| `Isaiah 52:15` | `pass3b-peer-edits` | `e99f55b0` | `false` | — | *(not reread after edit)* |
| `Jeremiah 11:6` | `pass3b-peer-edits` | `e99f55b0` | `false` | — | *(not reread after edit)* |
| `Jeremiah 11:8` | `pass3b-peer-edits` | `e99f55b0` | `false` | — | *(not reread after edit)* |
| `Jeremiah 22:16` | `pass3b-peer-edits` | `e99f55b0` | `false` | — | *(not reread after edit)* |
| `Jeremiah 30:21` | `pass3b-peer-edits` | `e99f55b0` | `false` | — | *(not reread after edit)* |
| `Jeremiah 30:22` | `pass3b-peer-edits` | `e99f55b0` | `false` | — | *(not reread after edit)* |
| `Jeremiah 35:13` | `pass3b-peer-edits` | `e99f55b0` | `false` | — | *(not reread after edit)* |
| `Jeremiah 39:13` | `pass3b-peer-edits` | `e99f55b0` | `false` | — | *(not reread after edit)* |
| `Jeremiah 39:14` | `pass3b-peer-edits` | `e99f55b0` | `false` | — | *(not reread after edit)* |

---

## 4. Per-Book Coverage Table (All 70 Latin Books, Summing to `34,952`)

| Book | `source_total` | `documented_contextual_read` | (Source-Checked) | (English-Only) | `automated_screening_only` | `insufficient_evidence` |
|---|---:|---:|---:|---:|---:|---:|
| Genesis | 1530 | 238 | 218 | 20 | 1292 | 0 |
| Exodus | 1211 | 187 | 114 | 73 | 1024 | 0 |
| Leviticus | 858 | 73 | 38 | 35 | 785 | 0 |
| Numbers | 1288 | 91 | 68 | 23 | 1197 | 0 |
| Deuteronomy | 959 | 51 | 30 | 21 | 908 | 0 |
| Joshua | 658 | 30 | 30 | 0 | 628 | 0 |
| Judges | 618 | 18 | 18 | 0 | 600 | 0 |
| Ruth | 85 | 1 | 1 | 0 | 84 | 0 |
| 1 Samuel | 811 | 23 | 21 | 2 | 788 | 0 |
| 2 Samuel | 695 | 18 | 15 | 3 | 677 | 0 |
| 1 Kings | 817 | 127 | 44 | 83 | 690 | 0 |
| 2 Kings | 719 | 19 | 19 | 0 | 700 | 0 |
| 1 Chronicles | 940 | 33 | 31 | 2 | 907 | 0 |
| 2 Chronicles | 822 | 28 | 28 | 0 | 794 | 0 |
| Ezra | 280 | 8 | 8 | 0 | 272 | 0 |
| Nehemiah | 404 | 13 | 13 | 0 | 391 | 0 |
| Esther | 275 | 115 | 113 | 2 | 160 | 0 |
| 1 Maccabees | 929 | 32 | 32 | 0 | 897 | 0 |
| 2 Maccabees | 558 | 15 | 15 | 0 | 543 | 0 |
| Job | 1070 | 138 | 61 | 77 | 932 | 0 |
| Psalms | 2527 | 150 | 118 | 32 | 2377 | 0 |
| Proverbs | 915 | 41 | 41 | 0 | 874 | 0 |
| Ecclesiastes | 222 | 10 | 10 | 0 | 212 | 0 |
| Song of Songs | 116 | 17 | 17 | 0 | 99 | 0 |
| Lamentations | 154 | 5 | 5 | 0 | 149 | 0 |
| Wisdom of Solomon | 439 | 34 | 33 | 1 | 405 | 0 |
| Sirach | 1592 | 414 | 305 | 109 | 1178 | 0 |
| Isaiah | 1292 | 98 | 91 | 7 | 1194 | 0 |
| Jeremiah | 1363 | 171 | 133 | 38 | 1192 | 0 |
| Ezekiel | 1272 | 126 | 99 | 27 | 1146 | 0 |
| Daniel | 531 | 160 | 160 | 0 | 371 | 0 |
| Hosea | 198 | 20 | 20 | 0 | 178 | 0 |
| Joel | 73 | 10 | 10 | 0 | 63 | 0 |
| Amos | 147 | 10 | 8 | 2 | 137 | 0 |
| Obadiah | 21 | 1 | 1 | 0 | 20 | 0 |
| Jonah | 48 | 4 | 4 | 0 | 44 | 0 |
| Micah | 104 | 14 | 14 | 0 | 90 | 0 |
| Nahum | 47 | 2 | 2 | 0 | 45 | 0 |
| Habakkuk | 56 | 2 | 2 | 0 | 54 | 0 |
| Zephaniah | 53 | 1 | 1 | 0 | 52 | 0 |
| Haggai | 38 | 3 | 3 | 0 | 35 | 0 |
| Zechariah | 211 | 21 | 21 | 0 | 190 | 0 |
| Malachi | 55 | 11 | 11 | 0 | 44 | 0 |
| Matthew | 1070 | 85 | 39 | 46 | 985 | 0 |
| Mark | 677 | 37 | 37 | 0 | 640 | 0 |
| Luke | 1151 | 48 | 48 | 0 | 1103 | 0 |
| John | 879 | 92 | 23 | 69 | 787 | 0 |
| Acts | 1004 | 38 | 34 | 4 | 966 | 0 |
| Romans | 433 | 86 | 23 | 63 | 347 | 0 |
| 1 Corinthians | 437 | 12 | 12 | 0 | 425 | 0 |
| 2 Corinthians | 255 | 11 | 10 | 1 | 244 | 0 |
| Galatians | 149 | 23 | 5 | 18 | 126 | 0 |
| Ephesians | 155 | 9 | 9 | 0 | 146 | 0 |
| Philippians | 104 | 3 | 3 | 0 | 101 | 0 |
| Colossians | 95 | 4 | 4 | 0 | 91 | 0 |
| 1 Thessalonians | 89 | 0 | 0 | 0 | 89 | 0 |
| 2 Thessalonians | 47 | 1 | 1 | 0 | 46 | 0 |
| 1 Timothy | 113 | 6 | 6 | 0 | 107 | 0 |
| 2 Timothy | 83 | 2 | 2 | 0 | 81 | 0 |
| Titus | 46 | 4 | 4 | 0 | 42 | 0 |
| Philemon | 25 | 1 | 1 | 0 | 24 | 0 |
| Hebrews | 303 | 55 | 15 | 40 | 248 | 0 |
| James | 108 | 3 | 3 | 0 | 105 | 0 |
| 1 Peter | 105 | 0 | 0 | 0 | 105 | 0 |
| 2 Peter | 61 | 3 | 3 | 0 | 58 | 0 |
| 1 John | 105 | 5 | 5 | 0 | 100 | 0 |
| 2 John | 13 | 13 | 0 | 13 | 0 | 0 |
| 3 John | 14 | 0 | 0 | 0 | 14 | 0 |
| Jude | 25 | 2 | 2 | 0 | 23 | 0 |
| Revelation | 405 | 45 | 19 | 26 | 360 | 0 |
