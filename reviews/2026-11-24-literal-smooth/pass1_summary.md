# Stage 2 Pass 1 — Independent Latin-Only Source-Language Fidelity Review

## 1. Pinned Metadata & Scope

| Field | Value |
|---|---|
| **Reviewer Role** | Stage 2 Pass 1 Independent Latin-Only Source-Language Fidelity Reviewer (`lat-fidelity`) |
| **Repository / Branch** | `Latin-Translation` (`review/2026-11-24-literal-smooth`) |
| **Pinned Base Commit (`LAT_BASE_SHA`)** | `5261e1b66c1a076e5618ab852515b419cc7fc0be` |
| **Pinned Studio Commit (`CTS_SHA`)** | `a0d022c1` |
| **Adopted Source Edition** | `Clem1598-USFX` (unified Sixto-Clementine Vulgate base across all 70 books; `lat-amiatinus` apparatus-only; apparatus witnesses `VulgHetzenauer (1906)`, `VulgConte (2009)`, `VulgSistina (1590)`) |
| **Corpus Audited** | **70 books / 1,298 chapters / 34,952 adopted native Vulgate verses** (`0` unverified) |
| **No-Counterpart Passages (Rule 0)** | **Psalm 151** (`no_counterpart` — absent from `Clem1598-USFX`) |
| **Direct Edits to Book JSON/MD Files** | **0** (Pass 1 is strictly proposal-only; all edits await Pass 2 independent Latin verification) |
| **Language Isolation** | **100% Latin-only** (zero exposure to Greek or Hebrew critical texts, English translations, or review files) |

### Deliverable Inventory

- **`pass1_proposals.jsonl`**: **1,035** traceable proposals (`LAT-P1-0001` through `LAT-P1-1035`), 13-key schema validated, zero archaisms, zero forbidden divine names.
- **`pass1_human_queue.jsonl`**: **81** editorial decision items (**71** verse-level `needs_human_editor: true` proposals + **10** corpus-wide doctrinal/policy decisions).
- **`pass1_coverage.json`**: Exact per-book coverage across all **70** Latin books pinned to `LAT_BASE_SHA` & `CTS_SHA` (`verified=34,151`, `disputed=801`, `unverified=0`, `source_total=34,952`).
- **`pass1_summary.md`**: This structured Pass 1 report.

### Proposal Breakdown by Category

| Category | Proposals | Description |
|---|---:|---|
| `restored_verse` | 467 | Newly restored native Sixto-Clementine Vulgate verses & Sirach Translator's Prologue drafted in Literal-Smooth Modern English |
| `stage1_text_upgrade` | 179 | Stage 1 adopted-Latin text changes (Genesis Amiatinus -> Sixto-Clementine reversions, verified typo fixes, apparatus-verified Clementine forms) |
| `native_order_mapping` | 164 | Rule 2 native Vulgate verse/chapter order restorations, verse splits/merges, and Saints.Bible parallel-display mappings |
| `note_update` | 140 | Updates to stale/superseded translator notes referencing old Amiatinus readings, pre-upgrade gaps, or pre-upgrade verse numbers |
| `disputed_capitalization` | 49 | Disputed OT Messianic capitalizations flagged with explanatory notes (text preserved pending human editorial policy) |
| `rule4_ambiguity` | 19 | Rule 4 ambiguity preservation & alternate-reading footnotes (`fides Jesu Christi`, bare `spiritus`, `pœnitentia ductus`, `Deus hujus sæculi`) |
| `stale_removal` | 8 | Removal of obsolete placeholders (`Sirach 1:15, 22:17, 42:1`), stale duplicates (`Ezek 20:45`), interleaved `Dan 1:22-60`, stale `Joel 4`, `Mal 3:19-24`, `Hos 2:25` |
| `punctuation_policy` | 5 | Quotation-mark continuity and cross-chapter dialogue punctuation notes (incl. `Job 14-32`) |
| `fidelity_meaning` | 3 | Aligned fidelity/idiom sweep findings (`Wis 18:21` `Prosperans`, `Isa 14:24` & `Jer 38:16` oath idioms) |
| `proper_name` | 1 | Latin-distinct proper-name verification & clarifying note (`Deut 4:48` `Mount Sion`) |
| **Total** | **1035** | **71 verse-level items flagged `needs_human_editor: true`** |

---

## 2. Stage 1 Critical-Text Upgrade Diff Audit (`HEAD~1` -> `HEAD`)

A programmatic diff of all 70 books between `HEAD~1` (`34,446` verses) and `HEAD` (`34,952` verses; net **`+506`** slots) accounted for **100%** of changed, shifted, split/merged, restored, and removed verses:

| Stage 1 Diff Classification | Verse Count | Audit Disposition |
|---|---:|---|
| `identical_same_key` | 30,500 | Swept programmatically across full corpus for fidelity, negation, length ratio, `semen`, Rule 4, notes, and style |
| `shifted_identical` | 3,176 | Verified against aligned English via `verse-map.json`; Rule 2 native-order & `Saints.Bible` mapping proposals generated |
| `substantive_change_same_key` | 735 | **727** Genesis (Amiatinus -> Sixto-Clementine) + **8** non-Genesis (`Wis 5:13, 11:5`; `Dan 5:2-3`; `Amos 8:8`; `Mic 3:7`; `Luke 8:2`; `2 Cor 1:23`) — 100% hand-inspected |
| `newly_restored` | 448 | **5** Genesis low-similarity replacements (`15:6, 23:5, 23:14, 37:36, 38:4`) + **443** newly restored native Vulgate verses across 20 books — 100% drafted |
| `split_or_merged_shifted` | 64 | `Numbers` (43), `Deuteronomy` (3), `Wisdom` (10), `Sirach` (4 incl. `1:1` Prologue), `Luke` (2), `John` (2) — 100% mapped/drafted |
| `substantive_change_shifted` | 29 | **12** `Exodus 36-39` + **9** `Jeremiah` + **3** `Sirach` (`1:19, 14:21, 32:9`) + **1** `Daniel 14:42` + **1** `Genesis 50:23` + **1** `1 Chr 6:18` + **1** `Neh 4:18` + **1** `Hos 2:13` — 100% resolved |
| **Total `HEAD` Verses** | **34,952** | **0 dropped Vulgate verses; 0 placeholders; 0 mismatches vs. `Clem1598-USFX`** |

### 2.1 Genesis Amiatinus -> Sixto-Clementine Reversion Audit

Moving `lat-amiatinus` to apparatus-only unified Genesis with the other 69 books on `Clem1598-USFX`, affecting **733** verses (`727` same-key, `5` low-similarity replacements, `1` shifted `50:23`). All **687** substantive/non-orthographic diffs were individually inspected against existing English and notes, yielding **161** wording/note upgrade proposals in Genesis alone. Key meaning-level corrections include:

- **`Gen 41:54`**: Adopted Latin now reads `in omni terra Ægypti panis erat` (the erroneous Amiatinus `<surplus>non</surplus>` is gone — restored from "there was no bread" to "there was bread").
- **Divine names & subjects**: `Gen 4:1` (`per Deum`), `6:22` (`Deus`), `15:6` (`Credidit Abram Deo`), `16:2` (`Dominus`), `20:18` (`Dominus`), `21:17` (`Dei`), `21:23` (`Deum`), `22:12` (`Deum`), `26:24` (`Deus`), `27:28` (`Deus`).
- **Major narrative & lexical reversions**: `Gen 4:6` (`iratus`), `8:21` (no `ad eum`), `18:28` (`propter quadraginta quinque`), `19:17` (`locuti sunt`), `19:29` (`civitates regionis illius`), `20:2` (`rex Geraræ`), `22:1` (`Abraham, Abraham`), `23:16` (no `Heth`), `24:32` (`pedes ejus` rather than `camelorum`), `27:12` (`inducam` 1st sg.), `27:41` (`Venient ... et occidam`), `28:14` (`semen tuum` -> `your seed`), `28:17` (`porta` sg.), `30:26` (`ut abeam`), `30:33` (`furti`), `30:40` (`in canalibus`), `32:10` (`minor sum`), `32:22` (`vadum Jaboc`), `35:5` (`civitates`), `36:40` (`ducum`), `39:18` (`audisset ... quod tenebam`), `42:16` (`adducat`, `vera an falsa`), `42:20` (`possim`), `44:14` (`abierat`), `45:23` (`asinas`), `47:11` (no `solo`), `47:24` (`familiis`), `48:15` (`Jacob filiis Joseph`), `49:9` (`ad prædam`), `50:11` (`Ægyptiis`, `vocatum est`), `50:19` (`resistere voluntati`), plus genealogical name forms (`36:22, 25, 26`; `46:10, 16, 17, 21`).
- **Authentic historic Sixto-Clementine forms verified across apparatus (`Clem1598-USFX`, Sixtine 1590, Hetzenauer 1906, Conte 2009)**: `Gen 6:6` (`hominum`), `38:21` (`in loco ista`), `43:10` (`vice alter`), `46:29` (`curro`), `Ruth 3:10` (`est secuta`), `1 Sam 4:21` (`vocabit`), `2 Kgs 8:11` (`Stetique`), `1 Chr 16:36` (`omnis populo`), `Acts 16:5` (`abundabunt`), `Isa 1:19` (`comeditis`), `Isa 2:6` (`augeres`), `Isa 5:25` (`adversus`), `Isa 9:5` (`violentia`), `Wis 18:21` (`Prosperans`). All verified and documented with precise notes.

### 2.2 Newly Restored Native Vulgate Verses & Deleted Bugs/Placeholders

Every newly restored native Sixto-Clementine Vulgate verse across all 25 upgraded books has been freshly translated into Literal-Smooth Modern English strictly conforming to `STYLE.md` and `glossary.json` (zero archaisms, `Dominus` -> `the Lord`, capitalized divine pronouns, plain text, chapter-balanced quotation marks):

| Book | Restored / Key Stage 1 Items | Notes & Deletions Handled |
|---|---|---|
| **Sirach** | **201** restored verses + **Translator's Prologue** (`1:1`) + `1:19, 14:21, 32:9` | Removes all 3 `"No aligned Latin source passage."` placeholders (`1:15, 22:17, 42:1`); full native chapter/verse alignment |
| **Esther** | **99** restored verses: canonical `1:1`, `5:2` (golden scepter), `11:1`, `11:3-16:24` | Relocates old `1:1` (Mordecai's dream) to native `11:2`; restores native Vulgate ch. 11–16 order with `Saints.Bible` Addition A–F mappings |
| **Daniel** | **77** restored verses: `4:4-5, 32`; **ch. 13 Susanna** (37 new + 28 remapped = 65 vv); **ch. 14 Bel & Dragon** (37 new + 5 remapped = 42 vv, incl. `14:42`) | Removes 33 interleaved `unplaced` Susanna/Bel entries from `Dan 1:22-60`; restores native `3:98-100` & `4:1-34`; syncs `Dan 5:2-3` (`Jerusalem`) |
| **Exodus** | **37** restored verses in **Exodus 36–39** (`25 newly_restored` + `12 shifted_and_changed`) | Realigns native Vulgate Tabernacle construction narrative (`Exod 36-39`) to `Saints.Bible` parallel display |
| **Jeremiah** | **31** restored verses (`22 newly_restored` + `9 shifted_and_changed`, incl. `25:14`, `27:1,7,13,17,21`, `30:10-11,16`, **`33:14-24`**, `39:4-7`, `46:1`) | Full native Vulgate `Jer 25-51` order restoration (`706` shifted verses remapped); relocates unplaced `33:25-26`; resolves `50:44` vs `49:19` aligner collision |
| **1 & 2 Maccabees** | `1 Macc 1:5, 32, 48, 54; 13:53` (**5** vv); `2 Macc 2:19; 15:37` (**2** vv) | Verified in narrative context; updated surrounding verse notes |
| **Psalms** | `Ps 10:2, 12:3, 108:17, 129:6` (**4** vv) | Plus native Vulgate Psalter numbering/parallel mappings (`Ps 9-147`) and `Ps 15:10` combined slot |
| **1 Kings** | `1 Kgs 7:13, 36, 45` (**3** vv) | Plus native `1 Kgs 7` & `1 Kgs 20-21` (Naboth/Ben-hadad) order mapping |
| **Joshua, Hosea** | `Josh 4:24, 5:15` (**2** vv); `Hos 2:24, 6:2` (**2** vv) | Removes stale `Hos 2:25` key; aligns native `Hos 6:1-3` & `11:12-12:14` |
| **Other Restorations (1 v each)** | `Num 6:27`, `1 Chr 11:35`, `Neh 4:6`, `Job 16:5`, `Prov 16:9`, `Song 6:12`, `Isa 64:1`, `Amos 6:11`, `Matt 17:20` (**9** vv) | Plus split/merged alignments in `Lev 15:23`, `Num 35:23`, `Wisdom` (10 splits), `Luke` (2), `John` (2) |
| **Stale Bugs Removed** | `Ezek 20:45` duplicate; `Joel 4:1-21` (stale chapter -> native `Joel 1-3`); `Mal 3:19-24` (stale keys -> native `Mal 4:1-6`); `Dan 1:22-60` (33 interleaved entries); `Sirach 1:15, 22:17, 42:1` (3 placeholders); `Hos 2:25` | Zero orphan or placeholder verses remain in proposed state |

### 2.3 Verified Stage 1 Typo Fixes & Apparatus Checks

All Stage 1 verified Latin typo repairs were confirmed directly in `HEAD` (`Clem1598-USFX`) and synced with English notes:

- **`Hos 2:13`** (`inaure sua` "earring" — fixed from `in aure sua`), **`2 Cor 1:23`** (`vestræ`), **`Amos 8:8`** (`ejicietur`), **`Luke 8:2`** (`infirmitatibus`), **`Mic 3:7`** (`vultus`), **`Neh 4:18`** (`ædificantium`), **`Dan 5:2-3`** (`Jerusalem`), **`Wis 5:13`** & **`11:5`**.
- All translator notes citing "the Clementine Vulgate" or previously flagged as `"unverified"` in Claude's checklist were audited directly against `Clem1598-USFX` and the apparatus witnesses (`VulgHetzenauer`, `VulgConte`, `VulgSistina`), producing **140** `note_update` proposals replacing outdated claims.

---

## 3. Rule 2 — Native Vulgate Order & `Saints.Bible` Parallel Mapping

All divergent sequences preserve **native Sixto-Clementine Vulgate order and numbering** in `Modern-English-OT/NT` with clean mappings to `Saints.Bible` parallel display and brief reader notes wherever differences could otherwise look like omissions:

| Priority Passage | Native Vulgate Order (`Clem1598-USFX`) | `Saints.Bible` Parallel Mapping & Reader Note Status |
|---|---|---|
| **`Deut 5:17-18`** | `5:17 Non occides` -> `5:18 neque mœchaberis` (Decalogue order) | Restored native order & mapped to `Saints.Bible` with reader note |
| **`Num 6:23-27`** | `6:27 Invocabuntque nomen meum...` stands as separate verse after Aaronic blessing | Restored `6:27` and remapped `6:23-26` with reader note |
| **`Exod 20:13-15`** | `20:13` murder, `20:14` adultery, `20:15` theft | Restored native order & mapped cleanly |
| **`Exod 21:16-17`** | `21:16` kidnapping, `21:17` cursing parents | Restored native order & mapped cleanly |
| **`Num 1:24-37` & `26:15-47`** | Native Vulgate tribal census order (Gad before Simeon/etc.) | Mapped with reader notes explaining tribal sequence |
| **`Num 10:34-36`** | Cloud verse (`10:34`) precedes Ark sayings (`10:35-36`) | Native order mapped with reader note |
| **`Exod 36-39`** | Native Vulgate Tabernacle construction sequence (+37 vv) | Full chapter/verse parallel mapping & reader notes |
| **`1 Kgs 7` & `20-21`** | Native Vulgate Temple furnishings (`7:13,36,45` restored) & Ahab chapters (`20-21`) | Native order & parallel mapping notes |
| **`Prov 31:25-28`** | Native Vulgate `Prov 31:25-28` order (and `Prov 15-31` shifts) | Native order & parallel mapping notes |
| **`Jer 25-51`** | Oracles Against the Nations at ch. `46-51` (native Vulgate/MT order, `706` shifted vv) | Comprehensive structural remap & chapter-boundary reader notes |
| **`Ezek 7:3-10`** | Native Vulgate `Ezek 7:3-10` oracle sequence | Mapped with reader notes |
| **`Joel 1-3`** | Native 3-chapter Vulgate (`2:28-32` = Saints `3:1-5`; `3:1-21` = Saints `4:1-21`) | Stale `Joel 4` removed; native mapping documented |
| **`Mal 4:1-6`** | Native 4-chapter Vulgate (`4:1-6` = Saints `3:19-24`; `4:4` Moses -> `4:5-6` Elijah) | Stale `Mal 3:19-24` removed; quote flow balanced across `3:18 / 4:1` |
| **`Esth 10:4-16:24`** | Native Vulgate Additions grouped at `10:4-13` & `11:1-16:24` | Mapped to `Saints.Bible` Additions A–F with clear notes |
| **`Dan 1, 3-5, 13-14`** | Native `3:98-100`, `4:1-34`, `5:17-25`, `13` (Susanna), `14` (Bel & Dragon) | `Dan 1:22-60` cleaned; full parallel mapping |
| **`Sirach 1-51`** | Native Vulgate Prologue (`1:1`) & chapter/verse numbering (`1,592` vv) | Full mapping & placeholder removal |
| **`Matt 5:4-5`** | Native Vulgate Beatitudes (`5:4` meek, `5:5` mourn) | Native order preserved & mapped with reader note |
| **Other Shifts** | `Exod 7:28/8:1`, `1 Chr 5:27/6:1`, `Josh 24:29`, `Isa 9:1-21 / 64:1-12`, `Hos 1:10-2:24 / 6:1-3 / 11:12-12:14`, `Amos 6:10-15`, `Mark 8:39-9:49`, `Luke 9:42-44 & 17:35-37`, `John 6:51-52`, `Acts 9:6-7` | All documented in `pass1_proposals.jsonl` |

---

## 4. Rule 4 — Ambiguity Preservation & Mandatory Test Cases

1. **`fides Jesu Christi` (`"the faith of"` vs. `"faith in"`)**: Audited across `Rom 3:22, 3:26`, `Gal 2:16, 2:20, 3:22`, `Eph 3:12`, `Phil 3:9`, `Jas 2:1`, `Rev 14:12`. `Rom 3:22`, `Gal 2:16`, and `Gal 3:22` already preserve the Latin genitive ambiguity `"the faith of..."` with alternate-reading notes; Pass 1 adds matching Rule 4 alternate-reading footnotes to all 6 remaining loci (`Rom 3:26`, `Gal 2:20`, `Eph 3:12`, `Phil 3:9`, `Jas 2:1`, `Rev 14:12`) and queues the policy (`LAT-HQ-POL-01`) + key verses (`Rom 3:22, 3:26`, `Gal 2:16, 2:20`, `Eph 3:12`) for human editorial sign-off.
2. **Bare `spiritus` Capitalization (`Ezekiel` & `Isaiah 32:15`)**: Audited all 9 mandatory loci (`Ezek 2:2, 3:12, 3:14, 3:24, 8:3, 11:1, 11:24, 43:5`; `Isa 32:15`) alongside lowercase controls (`Ezek 1:12, 1:20, 10:17`) and qualified `spiritus Domini/Dei` (`Ezek 11:5, 11:24b`). Pass 1 preserves current English text while adding Rule 4 alternate-reading notes (`"a spirit" / "the spirit" / "wind"`) at all 9 loci and queuing all 9 (`LAT-HQ-POL-02`) for human editorial decision.
3. **`semen` (`"seed"` vs. `"offspring"`)**: Full-corpus noun-only sweep of all **262** aligned `semen` verses confirmed **255/262** already render `"seed"` (preserving `Gen 3:15 -> Gal 3:16` and patriarchal echoes). Caught `Gen 28:14` (where Stage 1 reverted Amiatinus `germem` to Clementine `semen tuum`, updated to `"your seed"`), and verified that `Sirach 45:30-31` already use `"seed"` (while `Sir 45:16` translates `nepotes` as `"descendants"`).
4. **Claude's Checklist Verification**: Verified `Matt 27:3` & `Judg 21:6` (`pœnitentia ductus`), `Dan 9:25-26` (`christus`) + all 48 other OT Messianic capitalization loci, `2 Cor 4:4` (`Deus hujus sæculi`), `Wis 18:21` (`Prosperans`), `Job 14-32` cross-chapter quotes, Latin proper names (`Deut 4:48` `Mount Sion`, `Num 1:11`, `Judg 12:11`, `1 Chr` forms), and Open Item #4 lexical variations (`Euge`, `tribulatio`, `servus`, `visitare`, `latro`, `janitores`, `in monte Ephraim`, `honestas`). Every genuinely unresolved or doctrinally consequential choice is queued in `pass1_human_queue.jsonl`.

---

## 5. Full-Corpus Programmatic Fidelity Sweeps & QA Gates

Across all **34,952** adopted Latin verses (using aligned `HEAD -> HEAD~1 -> verse-map.json -> English` mapping to eliminate shifted-verse false positives):

- **Aligned Length Outliers (`33` true 1-to-1 outliers)**: 100% hand-inspected (genealogies, `Sirach 1:1` Prologue, `Gen 46:21` `Tehi -> Echi`).
- **Aligned Negation Audit (`137` true 1-to-1 mismatches)**: 100% hand-inspected; `0` false-negation errors remain (`Isa 14:24` and `Jer 38:16` conditional oath idioms verified and footnoted; `Gen 41:54` erroneous Amiatinus `non` fixed).
- **Existing `unplaced` Entries (`293` total)**: `257` map cleanly into native `HEAD` positions, `3` are `Sirach` placeholders flagged for deletion, and `33` are obsolete `Dan 1:22-60` Susanna/Bel fragments flagged for removal — **`0` unhandled orphans**.
- **Style & Cleanliness Gate on All `1,035` Proposals**: `0` schema errors, `0` duplicate `(book, native_ref)` keys, `0` banned archaisms, `0` forbidden divine names (`LORD`/`GOD`/`YHWH`), `0` disallowed Latinized proper names, `0` markdown/newline artifacts, `0` length-ratio flags on restored verses, and **even chapter-level quotation-mark balance** across every restored chapter (`Esther 10-16`, `Daniel 13-14`, `Malachi 3-4`).

---

## 6. Per-Book Coverage Summary (All 70 Latin Books)

Exact equation satisfied for every book: **`verified + disputed + unverified == source_total`** (`34,952` total; `0` unverified; `Psalm 151` recorded as `no_counterpart` in `pass1_coverage.json`).

| # | Book | Ch | Source Total | Stage 1 Δ | Verified | Disputed | Unverified | Proposals | Restored | Human Queue |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Genesis | 50 | 1,530 | 0 | 1,363 | 167 | 0 | 194 | 0 | 0 |
| 2 | Exodus | 40 | 1,211 | +37 | 1,169 | 42 | 0 | 45 | 37 | 0 |
| 3 | Leviticus | 27 | 858 | 0 | 858 | 0 | 0 | 2 | 0 | 0 |
| 4 | Numbers | 36 | 1,288 | +31 | 1,282 | 6 | 0 | 14 | 1 | 0 |
| 5 | Deuteronomy | 34 | 959 | +2 | 957 | 2 | 0 | 7 | 0 | 0 |
| 6 | Joshua | 24 | 658 | +2 | 656 | 2 | 0 | 5 | 2 | 0 |
| 7 | Judges | 21 | 618 | 0 | 617 | 1 | 0 | 1 | 0 | 1 |
| 8 | Ruth | 4 | 85 | 0 | 85 | 0 | 0 | 0 | 0 | 0 |
| 9 | 1 Samuel | 31 | 811 | 0 | 811 | 0 | 0 | 1 | 0 | 0 |
| 10 | 2 Samuel | 24 | 695 | 0 | 695 | 0 | 0 | 1 | 0 | 0 |
| 11 | 1 Kings | 22 | 817 | +3 | 814 | 3 | 0 | 5 | 3 | 0 |
| 12 | 2 Kings | 25 | 719 | 0 | 719 | 0 | 0 | 1 | 0 | 0 |
| 13 | 1 Chronicles | 29 | 940 | +1 | 936 | 4 | 0 | 8 | 1 | 3 |
| 14 | 2 Chronicles | 36 | 822 | 0 | 822 | 0 | 0 | 1 | 0 | 0 |
| 15 | Ezra | 10 | 280 | 0 | 280 | 0 | 0 | 0 | 0 | 0 |
| 16 | Nehemiah | 13 | 404 | +1 | 402 | 2 | 0 | 3 | 1 | 0 |
| 17 | Esther | 16 | 275 | +99 | 164 | 111 | 0 | 112 | 99 | 0 |
| 18 | 1 Maccabees | 16 | 929 | +5 | 924 | 5 | 0 | 8 | 5 | 0 |
| 19 | 2 Maccabees | 15 | 558 | +2 | 556 | 2 | 0 | 3 | 2 | 0 |
| 20 | Job | 42 | 1,070 | +1 | 1,069 | 1 | 0 | 9 | 1 | 1 |
| 21 | Psalms | 150 | 2,527 | +4 | 2,519 | 8 | 0 | 21 | 4 | 4 |
| 22 | Proverbs | 31 | 915 | +1 | 913 | 2 | 0 | 7 | 1 | 0 |
| 23 | Ecclesiastes | 12 | 222 | 0 | 222 | 0 | 0 | 1 | 0 | 0 |
| 24 | Song of Songs | 8 | 116 | +1 | 115 | 1 | 0 | 5 | 1 | 0 |
| 25 | Lamentations | 5 | 154 | 0 | 153 | 1 | 0 | 1 | 0 | 1 |
| 26 | Wisdom of Solomon | 19 | 439 | +6 | 426 | 13 | 0 | 22 | 0 | 1 |
| 27 | Sirach | 51 | 1,592 | +196 | 1,386 | 206 | 0 | 259 | 197 | 0 |
| 28 | Isaiah | 66 | 1,292 | +1 | 1,269 | 23 | 0 | 26 | 1 | 17 |
| 29 | Jeremiah | 52 | 1,363 | +31 | 1,328 | 35 | 0 | 44 | 30 | 4 |
| 30 | Ezekiel | 48 | 1,272 | -1 | 1,264 | 8 | 0 | 18 | 0 | 8 |
| 31 | Daniel | 14 | 531 | +77 | 422 | 109 | 0 | 138 | 77 | 7 |
| 32 | Hosea | 14 | 198 | +2 | 193 | 5 | 0 | 9 | 2 | 0 |
| 33 | Joel | 3 | 73 | 0 | 73 | 0 | 0 | 3 | 0 | 0 |
| 34 | Amos | 9 | 147 | +1 | 145 | 2 | 0 | 4 | 1 | 0 |
| 35 | Obadiah | 1 | 21 | 0 | 21 | 0 | 0 | 0 | 0 | 0 |
| 36 | Jonah | 4 | 48 | 0 | 48 | 0 | 0 | 0 | 0 | 0 |
| 37 | Micah | 7 | 104 | 0 | 98 | 6 | 0 | 8 | 0 | 5 |
| 38 | Nahum | 3 | 47 | 0 | 47 | 0 | 0 | 1 | 0 | 0 |
| 39 | Habakkuk | 3 | 56 | 0 | 56 | 0 | 0 | 0 | 0 | 0 |
| 40 | Zephaniah | 3 | 53 | 0 | 53 | 0 | 0 | 0 | 0 | 0 |
| 41 | Haggai | 2 | 38 | 0 | 37 | 1 | 0 | 3 | 0 | 1 |
| 42 | Zechariah | 14 | 211 | 0 | 200 | 11 | 0 | 12 | 0 | 11 |
| 43 | Malachi | 4 | 55 | 0 | 48 | 7 | 0 | 10 | 0 | 2 |
| 44 | Matthew | 28 | 1,070 | +1 | 1,065 | 5 | 0 | 5 | 1 | 1 |
| 45 | Mark | 16 | 677 | 0 | 677 | 0 | 0 | 1 | 0 | 0 |
| 46 | Luke | 24 | 1,151 | +1 | 1,150 | 1 | 0 | 3 | 0 | 0 |
| 47 | John | 21 | 879 | +1 | 879 | 0 | 0 | 1 | 0 | 0 |
| 48 | Acts | 28 | 1,004 | 0 | 1,004 | 0 | 0 | 2 | 0 | 0 |
| 49 | Romans | 16 | 433 | 0 | 431 | 2 | 0 | 2 | 0 | 2 |
| 50 | 1 Corinthians | 16 | 437 | 0 | 437 | 0 | 0 | 0 | 0 | 0 |
| 51 | 2 Corinthians | 13 | 255 | 0 | 254 | 1 | 0 | 1 | 0 | 0 |
| 52 | Galatians | 6 | 149 | 0 | 147 | 2 | 0 | 2 | 0 | 2 |
| 53 | Ephesians | 6 | 155 | 0 | 154 | 1 | 0 | 1 | 0 | 0 |
| 54 | Philippians | 4 | 104 | 0 | 103 | 1 | 0 | 1 | 0 | 0 |
| 55 | Colossians | 4 | 95 | 0 | 95 | 0 | 0 | 0 | 0 | 0 |
| 56 | 1 Thessalonians | 5 | 89 | 0 | 89 | 0 | 0 | 0 | 0 | 0 |
| 57 | 2 Thessalonians | 3 | 47 | 0 | 47 | 0 | 0 | 0 | 0 | 0 |
| 58 | 1 Timothy | 6 | 113 | 0 | 113 | 0 | 0 | 0 | 0 | 0 |
| 59 | 2 Timothy | 4 | 83 | 0 | 83 | 0 | 0 | 1 | 0 | 0 |
| 60 | Titus | 3 | 46 | 0 | 46 | 0 | 0 | 0 | 0 | 0 |
| 61 | Philemon | 1 | 25 | 0 | 25 | 0 | 0 | 0 | 0 | 0 |
| 62 | Hebrews | 13 | 303 | 0 | 303 | 0 | 0 | 0 | 0 | 0 |
| 63 | James | 5 | 108 | 0 | 107 | 1 | 0 | 1 | 0 | 0 |
| 64 | 1 Peter | 5 | 105 | 0 | 105 | 0 | 0 | 0 | 0 | 0 |
| 65 | 2 Peter | 3 | 61 | 0 | 61 | 0 | 0 | 0 | 0 | 0 |
| 66 | 1 John | 5 | 105 | 0 | 105 | 0 | 0 | 0 | 0 | 0 |
| 67 | 2 John | 1 | 13 | 0 | 13 | 0 | 0 | 0 | 0 | 0 |
| 68 | 3 John | 1 | 14 | 0 | 14 | 0 | 0 | 0 | 0 | 0 |
| 69 | Jude | 1 | 25 | 0 | 25 | 0 | 0 | 0 | 0 | 0 |
| 70 | Revelation | 22 | 405 | 0 | 404 | 1 | 0 | 2 | 0 | 0 |
| — | **TOTAL (70 Books)** | **1,298** | **34,952** | **+506** | **34,151** | **801** | **0** | **1,035** | **467** | **71 (+10 policy)** |

---

## 7. Pass 2 Handoff Checklist (Independent Second Latin Reviewer)

1. Verify all **`1,035`** proposals in `pass1_proposals.jsonl` against `Clem1598-USFX` (`LAT_BASE_SHA=5261e1b6` / `CTS_SHA=a0d022c1`) in paragraph/speech context, prioritizing all **`467`** newly restored native Vulgate verses and **`179`** Stage 1 critical-text wording upgrades.
2. Confirm all **`164`** Rule 2 native-order & `Saints.Bible` parallel-display mappings and **`8`** stale-slot/placeholder removals before applying edits to `Modern-English-OT/NT` JSON and Markdown files.
3. Preserve strict escalation of all **`81`** items in `pass1_human_queue.jsonl` (`71` verse-level + `10` corpus-policy decisions) to a qualified human editor — do not silently force doctrinally consequential or unresolved readings.
