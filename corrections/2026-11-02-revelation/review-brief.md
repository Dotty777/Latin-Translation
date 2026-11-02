# Revelation review: Latin column and KJV comparison (Saints.Bible Parallel Reader)

Your input file has two lists for the same run of verses:

- `latin`: Vulgate cards. Each pairs the **Clementine Vulgate** (`latin`, authoritative) and the site's English rendering of it (`english`, labelled "Direct Latin rendering · specialist review pending") with the site's English rendering of the Greek (`saints`, the Saints Translation, SBLGNT-based). `latin_label`/`saints_label` give each side's verse; a few cards pair a Latin verse with parts of two Greek verses.
- `kjv`: KJV comparison cards. Each pairs the **King James Version** (`kjv`, which translates the Textus Receptus) with the same Greek-English (`saints`). `greek_note` is the site's textual note on the Greek, when there is one.

Every card already has a category (`rating`), a comparison note (`note`) and a note on how the difference arose (`cause`). Many are first-pass boilerplate (`generic: true`): the category was assigned without a verse-specific reading. Your job is to make every card right.

## Job 1 (Latin cards): check the English against the Latin

Decide whether `english` is a faithful rendering of THIS Latin. Correct it **only where it departs from the Latin's meaning**: a Latin word, phrase or clause missing, or English added that the Latin lacks (beyond small connecting words); a mistranslated word; person, number, tense, mood or voice changed so the meaning changes; wrong names or numbers; English that renders the Greek (or the KJV) instead of this Latin. Do not change word order, punctuation style, lowercase pronouns for God, free but accurate renderings, or matters of taste. When you correct, change as few words as possible and keep the same modern register. Never import wording from the Greek or the KJV. Expect corrections in a few percent of cards at most.

## Job 2 (Latin cards): classify the LATIN against the GREEK

Judge what the Latin says against what the Greek says (through `saints`; base it on the Latin where the English is ambiguous).

## Job 3 (KJV cards): classify the KJV against the Greek-English

Ignore archaic English (thee, -eth, "unto", "shew"), capitalisation, punctuation and supplied smoothing words; they are English wording. Revelation's Textus Receptus differs from the critical text in many places (for example 1:8 "the beginning and the ending", 1:11, 5:14 "him that liveth for ever and ever", 11:17 "and art to come", 16:5, 22:14 "do his commandments", 22:19 "book of life"); where the KJV has words, a clause or a different reading that the Greek-English lacks, that is a real textual difference, not English wording. The Vulgate often agrees with the critical text against the KJV; you may use the Latin card for the same verse as evidence about the Greek tradition.

## Categories (the site's own definitions; use exactly these)

- **Same**: corresponding content; differences are only English wording or register.
- **Similar**: a modest difference of expression or emphasis (a synonym with a different nuance, singular/plural, a pronoun vs a name, a small particle or article, tense or aspect presentation).
- **Different**: a meaningful local detail differs (a different verb, object, image, number, name, place or condition) while the verse is otherwise parallel.
- **Divergent**: material present in one and absent in the other, or rearranged (a clause, phrase, title or sentence).
- **Disparate**: a major difference of assertion, agency or consequence.

Where verse division makes the two sides cover different amounts of text (Latin 20:7–10), judge what each card shows and say where the rest is.

## What to write for each card

- `category`: your category (it may equal the current one).
- If the card is `generic: true`, write `note` (layer 1, "Direct word comparison and meaning": 1–2 sentences, at most about 35 words, naming the concrete agreement or difference) and `cause` (layer 5, "How and why the differences arose": one sentence, at most about 30 words: English wording only; a lexical choice; a different reading in the Greek tradition the KJV or the Vulgate follows; verse division; an addition or omission. Do not speculate about copyists, motives or doctrine; if the origin is uncertain, say it is unresolved. For Same: "The difference is one of English wording; the [Latin/KJV] and Greek agree here.").
- If the card is not generic, keep its note and cause (`note`: null, `cause`: null) unless you change the category or the existing note is wrong; then write both.
- Plain text only, no HTML; use quotation marks for cited words; you may cite Latin words (Latin "cito"); do not cite Greek words unless you are certain of them.

## Output

Write one JSON object to the output file named in your task:

```
{"latin": [{"card": "...", "english_new": null | "<full corrected English>", "correction": null | "<what was wrong, citing the Latin, max 30 words>", "category": "...", "note": null | "...", "cause": null | "..."}, ...],
 "kjv":   [{"card": "...", "category": "...", "note": null | "...", "cause": null | "..."}, ...]}
```

Every input card must appear exactly once, in input order. Validate the file with `python3 -c "import json;json.load(open('<file>'))"`. Write only your own output file (scratch files only in the folder named in your task).
