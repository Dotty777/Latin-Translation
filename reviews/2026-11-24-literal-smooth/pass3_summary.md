# Stage 2 Pass 3 — Standalone English Clarity & Flow Review (Latin Edition)

- **Reviewer:** `@lat-flow` (Independent Standalone English-Only Reader)
- **Isolation Verified:** Read ONLY `Modern-English-OT/` and `Modern-English-NT/` (`STYLE.md`, `glossary.json`, `parallel-verse-map.json`, 70 book JSONs, 1,298 chapter Markdowns) and the Review Charter. Zero exposure to `Saints-Latin-Critical-Text/`, `Greek-Translation/`, or `Hebrew-Translation/`.
- **Starting Revision:** `496b9f9d866deaa335f5a08a97f4b98a775d7940` (branch `review/2026-11-24-literal-smooth`)
- **Corpus Audited:** **70 / 70 books** (43 OT + 27 NT), **1,298 / 1,298 native Vulgate chapters**, **34,952 / 34,952 verses**, **6,597 translator notes** (both JSON and chapter Markdown).

---

## 1. Executive Summary & Counts

| Metric | Result |
|---|---:|
| Books / Chapters / Verses / Notes audited | 70 / 1,298 / 34,952 / 6,597 |
| Schema errors (pre & post) | 0 |
| JSON ↔ Markdown sync errors (pre & post) | 0 |
| Placeholders (`No aligned Latin source passage.`, `TODO`, etc.) | 0 |
| Banned archaisms (`STYLE.md` / `glossary.json` + extended list) | 0 |
| Forbidden divine names (`LORD`, `GOD`, `YHWH`, `Yahweh`, `Jehovah`) | 0 |
| HTML / Markdown / raw bracket (`⟦ ⟧`) artifacts in verses | 0 |
| Double spaces, leading/trailing spaces, space-before-punct, doubled punct | 0 |
| Spelling typos across all 10,448 distinct lowercase words | 0 |
| `a`/`an` article mismatches or UK spelling variants | 0 |
| Chapter-level unbalanced parentheses | 0 |
| **Bucket A surface edits applied (`pass3_surface_edits.jsonl`)** | **20** (JSON + MD synced, `meaning_changed=false`, `resolves_ambiguity=false`) |
| **Bucket B bounce-backs routed to `@lat-peer` (`pass3_bounceback.jsonl`)** | **34** (**9 verse-text** + **25 translator-note** items; NOT applied by Pass 3) |

---

## 2. Full-Corpus Programmatic Sweep Findings

### 2.1 Typography, Vocabulary, and Style Compliance
- **Zero banned archaisms** across all 34,952 verses (`thee`, `thou`, `thy`, `thine`, `ye`, `unto`, `behold`, `-eth` verbs, etc.). Three uppercase `Lo` hits were verified as the place name `Lo-debar` (`2 Sam 9:4, 5; 17:27`).
- **Zero forbidden divine names** (`LORD`, `GOD`, `YHWH`, `Yahweh`, `Jehovah`).
- **Disallowed proper-name scan:** `12` hits checked and cleared — `Deuteronomy 4:48` `Mount Sion` is explicitly the Transjordan alternative name for Mount Hermon (distinct from Jerusalem's `Mount Zion`, explained in note `4:48`), and `11` occurrences of `Ananias` in `Acts` are valid NT personal names.
- **Spelling & doubled words:** All `12` doubled-word pairs (`had had`, `that that`, `give her her portions`, `who labors labors`, `used to steal steal`), all `5` repeated bigrams (`one by one by`, `little by little by`, `them to them to`, `year to year to`, `were written were written`), all `69` unspaced em-dashes (`—`), and all `1,731` unexplained singleton words were inspected: **0 spelling typos**.
- **Cross-verse parentheses:** All `6` multi-verse parenthetical spans (`1 Kgs 8:41-42`, `10:11-12`; `1 Chr 5:1-2`; `Amos 5:6-7`; `Acts 1:18-19`; `Heb 7:20-21`) balance cleanly within their chapters (`0` chapter-level paren errors).
- **Chapter-end non-period punctuation (`4` chapters):** `1 Sam 1:28`, `Esther 12:6`, `Wisdom 8:21`, and `Acts 21:40` each end with a colon (`:`) introducing the direct speech / letter / prayer that opens with `"` in verse 1 of the next chapter (`1 Sam 2:1`, `Esther 13:1`, `Wisdom 9:1`, `Acts 22:1`) — all four read smoothly and balance cleanly.

### 2.2 Full-Corpus Quotation Stack Audit & Specific Loci Checked
A full nesting-aware quotation parser (supporting 1-, 2-, and 3-level American English nesting `" ... ' ... "..." ... ' ... "`) was executed across all 1,298 chapters:
- **Books with odd double-quote totals:** `0 / 70`.
- **Chapters with stack-level quotation errors:** `11 / 1,298`:
  - **`10` chapters in Job** (`Job 13, 14, 16, 17, 23, 24, 27, 28, 29, 31` — cross-chapter Job speeches; see §2.3 below).
  - **`1` chapter in Jeremiah** (`Jeremiah 11:6-7` — premature single-quote closure at `11:6` causing illegal `"` inside `"` at `11:7`; routed to `@lat-peer` as `P3-B-03`).
- **Balanced-count premature quote closures caught by cross-verse boundary & speaker checks:**
  - `1 Kings 11:38-39` (`P3-B-01`) and `Jeremiah 30:21-22` (`P3-B-05`) both close quotes one verse early while first-person divine speech continues with lowercase `and` in the next verse. Both routed to `@lat-peer`.
- **`Numbers 6:23-27` (explicitly checked per brief):** Verified balanced at HEAD `496b9f9d` — `6:23` opens `"` (`"Speak to Aaron...`), `6:24` opens `'` (`'May the Lord bless you...`), `6:26` closes `'` (`...give you peace.'`), and `6:27` closes `"` (`And they shall invoke My name... bless them."`). No trailing quote defect remains in JSON or Markdown.
- **`Leviticus`, `Deuteronomy`, `Isaiah`, `Jeremiah`, `Ezekiel`, `Esther 10-16`, `Daniel 13-14`, `John 13-17`, `Revelation`:** All zero stack-level quote errors except `Jeremiah 11:6-7` (plus premature closes in `Jer 30:21-22` and unquoted `?`/`! says the Lord` in `Jer 22:16`, `Jer 35:13`, `Ezek 16:23`, all routed to `@lat-peer`). `John 13-16` and `Revelation 1-3` consistently close and reopen `"` cleanly at every chapter boundary.

### 2.3 Standalone Readability Analysis of `Job 1–42` (Cross-Chapter Quotes in `Job 13–31`)
*Per brief, `Job 13–31` cross-chapter vs. per-chapter quotation policy is already in the human editor queue and was NOT modified in Pass 3. Standalone readability findings across all 42 chapters are documented here for the editor:*
- **Internal inconsistency inside `Job`:** Eight multi-chapter speeches in `Job` (`4–5`, `6–7`, `9–10`, `12–13`, `32–33`, `36–37`, `38–39`, `40–41`) **close `"` at chapter end and reopen `"` at verse 1 of the next chapter** (matching `John 13–16` and `Revelation 1–3`), so every individual `chapter-*.md` file is self-contained and quote-balanced.
- **Exception in `Job 13–31`:** Only five middle speeches (`13–14`, `16–17`, `23–24`, `27–28`, `29–30–31`) leave `"` unclosed across chapter breaks without reopening `"` at the start of the continuation chapter.
- **Standalone chapter-file impact:** When reading individual chapter files (`chapter-14.md`, `chapter-17.md`, `chapter-24.md`, `chapter-28.md`, `chapter-30.md`, `chapter-31.md`), `Job 30` displays zero quotation marks, `Job 28` uses single quotes (`'It is not in me,'` in `28:14`, `'Look...'` in `28:28`) with no visible opening double quote in the chapter, and `Job 14:22`, `17:16`, `24:25`, `28:28`, `31:40` terminate with an orphan closing `"` (or `'"`). Notably, Job's own speech in `Job 12–14` mixes both conventions mid-speech (`12:25` closes `"` and `13:1` reopens `"`, but `13:28` does not close `"` and `14:1` does not reopen `"`).
- **Standalone recommendation for the human editor:** Standardizing `Job 13–31` to the per-chapter close/reopen convention already used by the other 8 multi-chapter speeches in `Job` (and `John 13–16`) would make every standalone chapter Markdown file self-contained and visually unambiguous; alternatively, adopting formal multi-chapter open-quote-on-new-chapter (Chicago style) across all 13 multi-chapter Job speeches would achieve internal consistency.

---

## 3. Standalone Prose & Flow Read — Representative & Restored Chapters

The following chapters were read in full as standalone Literal-Smooth Modern English across all biblical genres and newly restored native Vulgate sections:

- **Law / Narrative / Holiness Code / Restored Tabernacle:** `Genesis 22`, `Exodus 36`, `Exodus 37`, `Exodus 38`, `Exodus 39`, `Leviticus 19`, `Numbers 6`, `Deuteronomy 6`
- **Historical & Restored Chapters:** `1 Kings 7`, `1 Kings 11`, `Esther 10`, `Esther 11`, `Esther 12`, `Esther 13`, `Esther 14`, `Esther 15`, `Esther 16`
- **Wisdom & Poetry & Restored Sirach:** `Job 13`, `Job 14`, `Job 28`, `Psalms 22`, `Psalms 50`, `Psalms 150`, `Sirach 1` (with Translator's Prologue), `Sirach 24`, `Sirach 44`, `Sirach 51`
- **Prophecy & Restored Daniel:** `Isaiah 53`, `Jeremiah 31`, `Ezekiel 37`, `Daniel 13` (Susanna), `Daniel 14` (Bel and the Dragon)
- **Gospels, Epistles & Apocalyptic:** `Matthew 5`, `John 13`, `John 14`, `Romans 3`, `Romans 8`, `Galatians 2`, `Hebrews 11`, `2 John 1`, `Revelation 21`

**Overall Standalone Assessment:** The English across both the core canon and newly restored Vulgate chapters (`Esther 11–16`, `Daniel 13–14`, `Sirach`, `Exodus 36–39`, `1 Kings 7`, `Psalms`) reads at a consistently high Literal-Smooth standard: dignified, crisp, modern vocabulary, faithful formal structure, clear pronoun referents, and well-preserved ambiguity notes (`Rom 3:22, 26`, `Gal 2:16, 20`, `Ezek 37:5`). The defects discovered fell cleanly into two structural classes:
1. **Mechanical verse-boundary seams (20 Bucket A fixes)** — primarily left where Stage 1 restored continuation verses (11 in `Sirach`, 1 in `Esther 1:2`, 3 in `Exodus 37/39`, 2 in `1 Kings`, 2 in `Jeremiah`, 1 in `2 Corinthians 10:14`).
2. **Meaning/quote-scope verse issues (9 Bucket B items) and stale/misplaced/duplicated translator notes (25 Bucket B items)** — left behind after Stage 1 native Vulgate renumbering (`Exodus 37–39`, `1 Kings 5:18 / 11:25`, `1 Chr 12:4`, `Jer 45:5`, `Ezek 20:46`, `Dan 3:99–100`, `Luke 9:42`, `Acts 7:56`, `Acts 14:6`, plus 9 concatenated duplicate notes).

---

## 4. Bucket A Surface Edits Applied (`20` items — `pass3_surface_edits.jsonl`)

All 20 edits have `meaning_changed=false` and `resolves_ambiguity=false`, and have been applied identically to both `json/*.json` and `markdown/*/chapter-*.md`:

| ID | Native Ref | Category | Mechanical Fix Applied |
|---|---|---|---|
| `P3-A-01` | Exodus 37:6 | verse-boundary punct | Trailing `.` → `;` before lowercase continuation `37:7` |
| `P3-A-02` | Exodus 37:15 | verse-boundary punct | Trailing `.` → `;` before lowercase continuation `37:16` |
| `P3-A-03` | Exodus 39:41 | sentence-initial cap | `the` → `The` after completed sentence in `39:40` |
| `P3-A-04` | 1 Kings 5:17 | verse-boundary punct | Trailing `;` → `.` before capitalized sentence `5:18` |
| `P3-A-05` | 1 Kings 11:1 | verse-boundary punct | Trailing `,` → `.` before capitalized resumptive sentence `11:2` |
| `P3-A-06` | Esther 1:2 | restoration-seam cap | `When` → `when` after comma-ending phrase restored in `1:1` |
| `P3-A-07` | Sirach 3:9 | restoration-seam punct | Trailing `.` → `,` before restored lowercase `3:10` |
| `P3-A-08` | Sirach 32:2 | restoration-seam punct | Trailing `.` → `,` before restored lowercase `32:3` |
| `P3-A-09` | Sirach 32:4 | restoration-seam punct | Trailing `.` → `,` before restored lowercase `32:5` |
| `P3-A-10` | Sirach 32:22 | restoration-seam punct | Trailing `.` → `,` before restored lowercase `32:23` |
| `P3-A-11` | Sirach 37:15 | restoration-seam punct | Trailing `.` → `,` before restored lowercase `37:16` |
| `P3-A-12` | Sirach 41:1 | restoration-seam punct | Trailing `!` → `,` before restored lowercase `41:2` (keeps `!` at `41:2`) |
| `P3-A-13` | Sirach 41:3 | restoration-seam punct | Trailing `.` → `,` before restored lowercase `41:4` |
| `P3-A-14` | Sirach 44:22 | restoration-seam punct | Trailing `.` → `,` before restored lowercase `44:23` |
| `P3-A-15` | Sirach 45:10 | restoration-seam punct | Trailing `.` → `,` before restored lowercase `45:11` |
| `P3-A-16` | Sirach 46:1 | restoration-seam punct | Trailing `.` → `,` before restored lowercase `46:2` |
| `P3-A-17` | Sirach 51:6 | restoration-seam cap | `From` → `from` after semicolon in restored `51:5` |
| `P3-A-18` | Jeremiah 27:7 | sentence-initial cap | `and` → `And` after completed sentence in `27:6` |
| `P3-A-19` | Jeremiah 46:26 | sentence-initial cap | `and` → `And` after completed sentence in `46:25` |
| `P3-A-20` | 2 Corinthians 10:14 | verse-boundary punct | Trailing `.` → `,` before lowercase participial continuation `10:15` |

---

## 5. Bucket B Bounce-Backs Routed to `@lat-peer` (`34` items — `pass3_bounceback.jsonl`)

**None of these 34 items were modified by Pass 3.** All are routed to `@lat-peer` for independent verification against `Saints-Latin-Critical-Text` before adoption (or escalation to the human editor):

### 5.1 Verse-Text Bounce-Backs (`9` items)
- **`P3-B-01` — 1 Kings 11:38–39:** Premature `'"` close at `11:38` leaving first-person divine speech (`and I will afflict...`) unquoted with lowercase `and` in `11:39`.
- **`P3-B-02` — Isaiah 52:14–15:** Period at `52:14` before lowercase `he` in `52:15` — syntactic clause-attachment question (`Just as ... so ...`).
- **`P3-B-03` — Jeremiah 11:6–7:** Only non-Job stack quote nesting violation in corpus (`11:6` closes `'` prematurely before lowercase `for` and nested `"Hear My voice."` in `11:7`).
- **`P3-B-04` — Jeremiah 22:16:** Unquoted lowercase `? says the Lord.` without quote/comma framing.
- **`P3-B-05` — Jeremiah 30:21–22:** Premature `"` close after unpunctuated `? says the Lord."` in `30:21`, leaving first-person divine speech (`and you will be a people to Me...`) unquoted with lowercase `and` in `30:22`.
- **`P3-B-06` — Jeremiah 35:13:** Bare lowercase `? says the Lord.` inside open single quote.
- **`P3-B-07` — Jeremiah 39:13–14:** Comma at end of `39:13` (`...sent, along with ...`) before capitalized resumptive `They sent and took...` in `39:14`.
- **`P3-B-08` — Jeremiah 46:25:** Apparent repeated phrase `and upon Pharaoh` twice in the same list — verify against Clementine Vulgate.
- **`P3-B-09` — Ezekiel 16:23:** Parenthetical `(woe, woe to you! says the Lord God)` with lowercase `says` directly after `!`.

### 5.2 Stale, Misplaced, & Duplicated Translator-Note Bounce-Backs (`25` items)
Routed to `@lat-peer` because every translator note cites Latin/Hebrew/Greek readings or native-vs-Saints mappings that require source verification:
- **Misplaced / factually stale notes (`14` items):** `Acts 7:56` (`P3-B-30`, erroneous copy-paste of `Acts 14:6` note!), `Acts 14:6` (`P3-B-33`), `Exodus 37:1` (`P3-B-11`), `Exodus 38:10` (`P3-B-12`), `Exodus 38:17` (`P3-B-13`), `Exodus 39:1` (`P3-B-14`), `Exodus 39:2` (`P3-B-15`), `Exodus 39:8` (`P3-B-16`), `1 Kings 5:18` (`P3-B-21`), `1 Kings 11:25` (`P3-B-22`), `Jeremiah 45:5` (`P3-B-26`, out-of-range `v. 34` in a 5-verse chapter), `Daniel 3:99` (`P3-B-28`), `Daniel 3:100` (`P3-B-34`), `Luke 9:42` (`P3-B-29`, duplicate of `9:44` note).
- **Self-contradictory or concatenated duplicate notes (`11` items):** `1 Chronicles 12:4` (`P3-B-23`, self-contradictory), `Ezekiel 20:46` (`P3-B-27`, contradictory `21:7` vs `21:2`), `Genesis 50:22` (`P3-B-10`), `Leviticus 15:19` (`P3-B-17`), `Numbers 27:3` (`P3-B-18`), `Numbers 35:22` (`P3-B-19`), `Deuteronomy 6:11` (`P3-B-20`), `Job 16:6` (`P3-B-24`), `Ecclesiastes 7:1` (`P3-B-25`), `2 Timothy 4:8` (`P3-B-31`), `Revelation 20:7` (`P3-B-32`).

---

## 6. Post-Edit Validation Gate
Full-corpus validation re-run after applying all 20 Bucket A edits confirmed:
- `70 / 70` JSON files valid, `0` schema errors (`1,298` chapters, `34,952` verses, `6,597` notes).
- `1,298 / 1,298` chapter Markdown files 100% verbatim synced with JSON (`0` drift).
- `0` placeholders, `0` banned archaisms, `0` forbidden divine names, `0` remaining mechanical sentence-boundary/capitalization seams outside the Bucket B items routed to `@lat-peer`.
