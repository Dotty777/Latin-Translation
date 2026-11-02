# Corrections of 2 November 2026: Genesis–Deuteronomy (Latin column)

All changes were made on the **staging** site only; production has not been touched. The five Vulgate comparison pages as they were before any change are in [staging-backups/2026-11-02](../../staging-backups/2026-11-02/).

| File | What it changes |
| --- | --- |
| `vulgate-<book>.json.gz` (5 files) | The whole new content of each Vulgate comparison page (Genesis 20673, Exodus 20676, Leviticus 20678, Numbers 20681, Deuteronomy 20684), applied only if the page still had the md5 it had before. It (1) gives each of the 5,600 cards labelled "Assessment open" its Latin–Greek category, badge and layer-1 comparison note, and recounts the page summary; and (2) marks the extra Greek references inside cards that cover several Vulgate verses as `data-group-ref`, so the Parallel Reader shows such a card once, on its first row, instead of repeating it. Latin and English text are unchanged. |
| [vulgate-classifications.json](vulgate-classifications.json) | The 5,600 classifications with their notes (Same 2,397; Similar 2,207; Different 661; Divergent 311; Disparate 24). |
| [classification-brief.md](classification-brief.md) | The brief the classifications were made to: the site's category definitions and the note style. Each note was checked against its card afterwards. |
| Row alignment | 359 Vulgate cards (Exodus 8, 22, 35–39; Leviticus 6; Numbers 1, 6, 10, 16–17, 26, 29–30; Deuteronomy 5, 12–13, 22–23, 29) now name the Saints verse their Greek pair is, so the Latin sits beside the same verse as the Hebrew, KJV and Saints columns. Data files and method: [Hebrew-Translation corrections/2026-11-02/alignment](https://github.com/Dotty777/Hebrew-Translation/tree/main/corrections/2026-11-02/alignment). |

## Checks after the changes

- Each page was read back after saving and matched the expected md5.
- Every Pentateuch Vulgate card carries a classification (0 "Assessment open" left).
- Grouped cards: Numbers 15:4–7 and 27:3–8, for example, now appear once in the reader with the label "15:4, 15:5, 15:6, 15:7".
- Highlighting still applies to 5,817 of 5,820 Latin readings; the 3 without colours had none before.
- The book folders were recaptured from the reader after all changes (`captured: 2026-11-02`).
