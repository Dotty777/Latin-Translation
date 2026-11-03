# Study Workspace — the textual layer, compiled for every verse

Date: 2 November 2026. Staging site 248834710 only; production untouched.

## What was done

Every verse row of the Parallel Reader now has its own Study Workspace entry with a **textual layer** drawn from the site's existing source studies (the Hebrew–Greek, Latin–Greek and King James–Greek comparison pages, the word notes, and where present the Study Edition and reception pages). The interpretive prose of the Genesis 1 model (`received`, `explain`, `shared`, `instructions`, lexicon entries) is **not** written yet for any verse except Genesis 1; each chapter record says so in its status line:

> Textual notes compiled from the site's studies · study prose not yet written

Scope: 70 books · 1,291 chapters · 34,586 verse rows · 2,582 records (one data record and one sources record per chapter). Reader plugin Saints Parallel Reader **1.9.0** installed on staging; helper Saints Pentateuch Work 1.15.0.

## What each verse now carries

| Field | Content | Verses filled |
|---|---|---|
| `siteNote` | Layer‑1 text of the primary comparison card (direct wording / meaning and context / alignment) | 34,409 of 34,555 (99.6%) |
| `siteNoteLabel` | Which card the note is from and its rating, e.g. `Hebrew and Greek · Different` | same |
| `whyNote` | Layer‑5 "How and why the differences arose" | 30,241 |
| `lost[]` | One line per comparison card: `keeps` / `differs` (Hebrew) or `between` (Latin, KJV), with the card's rating and its layer‑1 or layer‑4 text | 52,674 lines |
| `words[]` | The site's word notes for the verse | 28,997 |
| `chapterNote.lost` | A tally of the chapter's ratings per card and its Divergent/Disparate verses | all 1,290 compiled chapters |

Primary card chosen per verse: Hebrew and Greek 23,117 · Latin and Greek 7,823 · King James and Greek 3,601 (first rated card in that order; otherwise the first card present).

Reader rating badges across all verses: Similar 13,613 · Different 10,184 · Same 4,922 · Divergent 3,687 · Disparate 1,992 · unrated 188.

## By division

| Division | Chapters | Verses | siteNote | whyNote | word notes | lost lines |
|---|---|---|---|---|---|---|
| Law | 187 | 5,834 | 5,799 (+31 Genesis 1 prose) | 4,746 | 5,320 | 11,742 |
| Judgement | 322 | 9,681 | 9,681 | 6,899 | 9,210 | 9,747 |
| Providence | 245 | 5,356 | 5,249 | 5,351 | 5,226 | 5,395 |
| Discipleship | 149 | 3,774 | 3,747 | 3,747 | — | 3,955 |
| Salvation | 89 | 3,773 | 3,773 | 3,773 | 3,739 | 7,545 |
| Wisdom | 277 | 5,763 | 5,755 | 5,320 | 5,502 | 13,480 |
| Glory | 22 | 405 | 405 | 405 | — | 810 |

## Verses with no textual note (146)

These rows exist in the reader but the site has no comparison text for them, so the Workspace shows the sources tab only:

- **Daniel** 107 — the Greek additions numbered 1:22–62 (Susanna) and chapters 13–14 have no comparison pages on the site.
- **3 John** 14 and **2 John** 13 — the site's Discipleship comparison pages for these letters hold no layer‑1 text.
- **Psalms** 8 — 144:13a and Psalm 151:1–7 (Greek‑only material).
- **Exodus** 4 — 38:10, 38:11, 38:24, 39:21 (verses the Hebrew–Greek page skips).

Other site‑side gaps carried through as the site states them: Latin and King James assessments marked "review pending" / "classification open" in many books; Discipleship has no Hebrew card, no word studies and no Study Edition; Job's cross‑references are unreviewed.

## Reader 1.9.0 (installed on staging)

- `DIRECTIONS.differs = 'The Greek differs'` with its own `.svw-dir-differs` style, so the compiled Hebrew lines are not shown as "keeps/loses" claims the prose has not yet made.
- The study‑notes fold is titled from `siteNoteLabel` ("Study notes on the King James and Greek" where no Hebrew card exists) instead of assuming Hebrew.

## Checks

- `wsdata` jobs: 88 bundles loaded, 1,290 records updated, Genesis 1 unchanged, no rejected files.
- `wslist`: 2,582 stored records; md5 of every one matches the four manifests (`data/manifest.json`, `data/judgement/manifest.json`, `data/providence/manifest.json`, `data/discipleship/manifest.json`).
- `wscheck`: data routes for Genesis 2, Matthew 5, Judges 3, 1 Kings 2, Acts 2, Revelation 22, Psalm 151 and the references route for Genesis 2 all answer 200 with well‑formed JSON; the Parallel Reader pages for Genesis 2, Matthew 5, Acts 2, 1 Kings 2 and Psalm 151 enqueue `verse-workspace.js` 1.9.0 with the right `dataUrl`.
- Local render (Playwright against the 1.9.0 assets): Isaiah 53:4 shows "The Greek differs · Hebrew and Greek · Different …" with the new style; Romans 8:28 and Acts 2:4 title the fold "Study notes on the King James and Greek"; Genesis 1 renders as before; no script errors.

## Tooling

`tools/compile_notes.py SRC DST [books]` builds the textual layer from the source records (`out`, `outj`, `outp`, `outd`) into `outc`; `bundle_ws.py` packs it; the helper's `wsdata` job loads it from this repository by commit hash with sha256 checks. `compile_notes.py` skips any verse that already has `received` prose, so authored chapters are never overwritten when the layer is recompiled.

## Next

Interpretive prose, book by book, in the Genesis 1 style, beginning with Genesis 2 and continuing through the Law. Each book is pushed here as a reviewable draft (status "Draft for review") and loaded to staging; a short report accompanies each book.
