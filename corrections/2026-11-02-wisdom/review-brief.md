# Wisdom Division Latin–English review (Saints.Bible Parallel Reader)

Each card pairs the **Clementine Vulgate** (`latin`, the authoritative text for this task; Psalms is the Gallican Psalter) and the site's English rendering of that Latin (`english`, the project's own 28 September 2026 rendering, labelled "review pending") with the site's English rendering of the Septuagint Greek (`saints`, the Saints Translation). Books: Psalms, Proverbs, Ecclesiastes, Song of Songs, Lamentations. Each of `latin`, `english` and `saints` is a list of verse units `{ref, text}`; most cards have one unit per side, a few have two, and a few have none on one side. You do two jobs per card.

Transcription notes: the Latin may contain stray square brackets (`]` at the end of a psalm, `[` before a title) and spaces before `; : ! ?`. These are features of the transcription; ignore them. In Lamentations the Latin carries the Hebrew letter names (`<Aleph>`), and the English rightly renders them as "Aleph." etc. Keep them.

## Job 1: check the Latin–English against the Latin (every card that has Latin)

Read each Latin unit with its English unit and decide whether the English is a faithful rendering of THIS Latin.

Correct the English **only where it departs from the Latin's meaning**:
- a word, phrase or clause in the Latin is missing from the English, or the English adds something the Latin does not have (beyond the small connecting words any English needs);
- a word is mistranslated, or person, number, tense, mood or voice is changed so that the meaning changes (who acts, who is addressed, when, whether it is a command, wish or statement);
- names, numbers, places, or who is speaking are wrong;
- the English renders a different text (for example the Hebrew or the Greek) instead of this Latin.

Do **not** change: word order, punctuation style, modern idiom that renders the Latin faithfully, a free but accurate rendering, lowercase pronouns for God, or anything that is a matter of taste. When you do correct, change as few words as possible, keep the rest of the sentence identical and in the same modern register. Never import wording from the Greek or from the KJV.

Most verses need no change. Expect corrections in a few percent of cards at most.

## Job 2: classify the Latin against the Greek (only cards whose `rating` is "Review pending")

Judge what the LATIN says against what the GREEK says (read through `saints`; base the judgment on the Latin text where the English is ambiguous). Choose exactly one category (the site's own definitions):
- **Same**: corresponding content; differences are only English wording or register.
- **Similar**: a modest difference of expression or emphasis (a synonym with a different nuance, singular/plural, a pronoun vs a name, a small particle or article, a slightly different tense).
- **Different**: a meaningful local detail differs (a different verb, object, image, number, name, place or condition) while the verse is otherwise parallel.
- **Divergent**: material present in one and absent in the other, or rearranged (a clause, phrase or sentence; a unit the other text does not contain).
- **Disparate**: a major difference of assertion, agency or consequence (one says the opposite, or a different subject does a different thing).

The Gallican Psalter was translated from the Greek, so Psalms will mostly be Same or Similar. In Proverbs the Greek has many lines the Latin does not (and some the other way), and its order differs in chapters 24–31.

Cards with no unit on one side (`english` or `saints` is empty) come with `context_before` and `context_after` (the neighbouring cards). If the material is genuinely absent from the other text, the category is Divergent: say which text has the line and that the other has no counterpart here. If the neighbouring cards show the same content placed or divided differently, still use Divergent but say the content is located at the neighbouring verse (name it).

Where verse division makes the two sides cover visibly different amounts of text, judge what each card shows, and use Divergent only if content is genuinely missing on one side. In the Psalms a title (superscription) is part of the verse numbering in both texts.

Write:
- `note`: the layer-1 "Direct word comparison and meaning" text: 1–2 sentences, at most about 35 words, plain text, no HTML, in the site's style, e.g. "The Latin adds the question about seeking things greater than oneself and calls life a pilgrimage; the Greek speaks of days of futility." or "Latin 'justorum' and Greek 'righteous' agree; both contrast the way of the just with the perishing way of the ungodly." For Same, say briefly what agrees and that the difference is English wording. You may cite a Latin word in plain text (Latin "peregrinationis"). Do not cite Greek words unless you are certain of them.
- `cause`: the layer-5 "How and why the differences arose" text: one sentence, at most about 30 words. Say what kind of difference it is (English wording only; a lexical choice; a different reading in the Hebrew-based Latin versus the Septuagint; verse division; an addition or omission). Jerome translated Proverbs, Ecclesiastes, Song of Songs and Lamentations from the Hebrew, so many differences reflect Hebrew versus Greek; say so where that is the evident reason, without naming a cause you cannot see. Do not speculate about copyists, motives or doctrine; if the origin is not certain, say it is unresolved. For Same: "The difference is one of English wording; the Latin and Greek agree here."

Judge the classification on the corrected English if you corrected it.

## Output

Write a JSON list to the output file named in your task, one object per card, in input order:

```
{"card": "<card id>", "english_new": null | {"<unit ref>": "<full corrected unit text>"}, "correction": null | "<what was wrong, citing the Latin, max 30 words>", "category": "Same" | "Similar" | "Different" | "Divergent" | "Disparate" | null, "note": "<...>" | null, "cause": "<...>" | null}
```

- `english_new` maps the `ref` of each corrected English unit to its full corrected text (keep any "Aleph."-type heading); null if nothing changed.
- `category`, `note`, `cause` are null for cards whose `rating` is not "Review pending" (they are already classified).
- Every input card must appear exactly once. Validate your file with `python3 -c "import json;json.load(open('<file>'))"`. Write only your own output file; do not create, modify or delete any other file.
