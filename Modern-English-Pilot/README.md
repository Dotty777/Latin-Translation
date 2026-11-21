# Saints Modern English Pilot — Latin — Clementine / Vulgate basis

> **Pilot Status:** `draft: true`  
> **Coverage:** 10 passages, 270 verses, 86 translator notes  
> **Validation:** Passed peer translation review and `validate_modern_english.py --strict` (0 FAIL, 0 WARN)

## Overview

This directory contains the reviewed **Saints Modern English Pilot** translated directly from `Saints-Latin-Critical-Text` under the Saints Modern English style policy ([`STYLE.md`](STYLE.md)) and shared term glossary ([`glossary.json`](glossary.json)).

- Follows **Saints.Bible versification** (Vulgate/Gallican Psalm 22 = MT/English Psalm 23).
- Translated strictly from the Saints Latin Critical Text without harmonizing to Hebrew or Greek (e.g., Gen 1:1 singular `heaven`, Gen 3:15 `she will crush`, unbracketed John 7:53–8:11).

## Directory Contents

- [`STYLE.md`](STYLE.md) — Locked translation style policy (formal-equivalent Modern English, own-source fidelity, no archaisms, original wording).
- [`glossary.json`](glossary.json) — Standardized proper names and recurring theological/lexical terms.
- `json/` — Structured per-passage JSON (`verses` keyed by Saints `ch:v`, plus `notes`).
- `markdown/` — Human-readable Markdown reading editions with inline verse numbers and translator notes.

## Pilot Passages

| Passage | Saints Keys | Verses | Notes | Reading Edition | Structured JSON |
|---|---|---:|---:|---|---|
| Genesis 1 | `1:1–31` | 31 | 5 | [`01-genesis-1.md`](markdown/01-genesis-1.md) | [`01-genesis-1.json`](json/01-genesis-1.json) |
| Genesis 2 | `2:1–25` | 25 | 10 | [`01-genesis-2.md`](markdown/01-genesis-2.md) | [`01-genesis-2.json`](json/01-genesis-2.json) |
| Genesis 3 | `3:1–24` | 24 | 9 | [`01-genesis-3.md`](markdown/01-genesis-3.md) | [`01-genesis-3.json`](json/01-genesis-3.json) |
| Psalms 22 (MT/English Ps 23) | `22:1–6` | 6 | 6 | [`21-psalms-22.md`](markdown/21-psalms-22.md) | [`21-psalms-22.json`](json/21-psalms-22.json) |
| Isaiah 53 | `53:1–12` | 12 | 7 | [`28-isaiah-53.md`](markdown/28-isaiah-53.md) | [`28-isaiah-53.json`](json/28-isaiah-53.json) |
| Daniel 2 | `2:1–49` | 49 | 12 | [`31-daniel-2.md`](markdown/31-daniel-2.md) | [`31-daniel-2.json`](json/31-daniel-2.json) |
| John 1 | `1:1–51` | 51 | 13 | [`47-john-1.md`](markdown/47-john-1.md) | [`47-john-1.json`](json/47-john-1.json) |
| John 7:53–8:11 (Pericope Adulterae) | `7:53–8:11` | 12 | 4 | [`47-john-7-53-8-11.md`](markdown/47-john-7-53-8-11.md) | [`47-john-7-53-8-11.json`](json/47-john-7-53-8-11.json) |
| Romans 8 | `8:1–39` | 39 | 15 | [`49-romans-8.md`](markdown/49-romans-8.md) | [`49-romans-8.json`](json/49-romans-8.json) |
| Romans 12 | `12:1–21` | 21 | 5 | [`49-romans-12.md`](markdown/49-romans-12.md) | [`49-romans-12.json`](json/49-romans-12.json) |
