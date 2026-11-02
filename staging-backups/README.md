# Staging backups

Raw WordPress block content of the Saints.Bible staging comparison pages that feed this column of the Parallel Reader, saved before each round of corrections. Each file is `<page id>-<slug>.html.gz` (gzip of the exact page content); `manifest.json` records the slug, parent book page, last-modified time and MD5 of each page at the time of the backup.

To restore a page, decompress its file and paste the content back into the page (or write it with the WordPress.com connector). Every correction made after a backup is also saved by WordPress as a normal page revision.

- `2026-11-02/`: before the Genesis–Deuteronomy corrections of 2 November 2026.
