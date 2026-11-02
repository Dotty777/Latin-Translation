# Study Workspace data — Law, Salvation, Wisdom and Glory divisions

Data for the Study Workspace panel of the Parallel Reader (Saints Parallel Reader plugin 1.5.0, `modules/verse-workspace`).

- 17 books, 575 chapters, 15,775 verse rows.
- `data/*.json.gz`: bundles of chapter records, `{"files": {"<book>-<ch>.json": "...", "<book>-<ch>.sources.json": "..."}}`. `data/manifest.json` lists each bundle's sha256 and each file's md5.
- `tools/`: the scripts that build the records from the site's own pages (`build_ws.py`, with `extract.py`, `saintspage.py`, `studyed.py`, `srcpage.py`) and pack them (`bundle_ws.py`).

The staging helper (Saints Pentateuch Work 1.12.0, job `wsdata`) stores each record as a private `saints_ws_chapter` post. The reader serves them at `/wp-json/saints-workspace/v1/data/<book>-<ch>` and `/wp-json/saints-workspace/v1/data/<book>-<ch>-sources`. Cross-references are built live at `/wp-json/saints-workspace/v1/references/<book>-<ch>`.

Kept in this repository because the Saints-Translation repository cannot be pushed from this session. See `REPORT.md` for what each chapter contains and what is still to be written.
