# Saints Parallel Reader

One home for the Parallel Reader's additions, kept as separate modules. The reader's table itself stays in Saints Study.

| Module | Replaces | Status |
|---|---|---|
| `modules/layout.php` | Saints Parallel Layout 1.0.1 | Included |
| `modules/verse-workspace/` | Saints Verse Workspace 0.1.0 | Included; administrators only, except on staging |
| `modules/latin-text.php` | New | Removes whole Latin verses from displayed pages |
| Highlights | Saints Parallel Reader Highlights 1.4.1 | Waiting for its source code |
| Word Notes | Saints Parallel Reader Word Notes 0.2.2 | Waiting for its source code |

## Switching over

Each module stays silent while the older plugin it replaces is active, so this plugin can be activated first without anything printing twice. Deactivating the older plugin hands the work to the module. Reactivating it hands the work back.

## Settings

- `SAINTS_PARALLEL_READER_LAYOUT_LIVE` in `modules/layout.php`: false shows the layout changes to administrators only.
- `SAINTS_PARALLEL_READER_WORKSPACE_LIVE` in `modules/verse-workspace/module.php`: false shows the panel to administrators only. Set it to true after the notes are reviewed. Sites on a `.wpcomstaging.com` address always show the panel to everyone, so the notes can be reviewed there.

## Adding a Verse Workspace chapter

Run these from `modules/verse-workspace/tools`:

1. `build_chapter.py` generates `data/<book>-<chapter>.source.json` from the published pages. Whole verses in the original languages are not collected.
2. `digest.py` prints that file for writing `data/<book>-<chapter>.notes.json`.
3. `assemble.py` validates the notes and creates `data/<book>-<chapter>.json`. It stops if any Greek or Hebrew passage runs longer than `MAX_ORIGINAL_WORDS`.
4. Add the chapter to `saints_parallel_reader_workspace_chapters()`, then run `tools/package.py` from this folder.

## Licences

- Code: GPL-2.0-or-later.
- Greek phrases in the notes: H. B. Swete, *The Old Testament in Greek* (1901), digital text from the First1KGreek Project, University of Leipzig, CC BY-SA 4.0. Only short phrases are quoted; whole verses are not published.
- Notes and comparison content: CC BY-SA 4.0, matching the site.
