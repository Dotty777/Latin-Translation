# Gospel Latin–English review (Saints.Bible Parallel Reader)

Each card pairs one verse of the **Clementine Vulgate** (`latin`, the authoritative text for this task) and the site's English rendering of that Latin (`english`) with the site's English rendering of the Greek (`saints`, the Saints Translation of the Greek New Testament). You do two jobs per card.

## Job 1: check the Latin–English against the Latin

`source` says where the English came from: `scaffold` = Douay-Rheims (Challoner), lightly modernised; `direct` = a fresh rendering. Both are labelled "review pending". Read the Latin and the English together and decide whether the English is a faithful rendering of THIS Latin.

Correct the English **only where it departs from the Latin's meaning**:
- a word, phrase or clause in the Latin is missing from the English, or the English adds something the Latin does not have (beyond the small connecting words any English needs);
- a word is mistranslated, or person, number, tense, mood or voice is changed so that the meaning changes (who acts, who is addressed, when, whether it is a command or a statement);
- names, numbers, places, or who is speaking are wrong;
- the English renders a different Latin reading (for example Douay-Rheims wording that follows a different text from the Clementine one shown).

Do **not** change: archaic-but-accurate words ("Behold", "begot"), word order, punctuation style, the colon before direct speech, lowercase pronouns for God, Douay-Rheims phrasing that renders the Latin faithfully, or anything that is a matter of taste. A modernised Douay sentence that is accurate stays exactly as it is. When you do correct, change as few words as possible and keep the rest of the sentence identical, in the same register. Never import wording from the Greek or from the KJV.

Most verses need no change. Expect corrections in a few percent of cards, not most.

## Job 2: classify the Latin against the Greek (only cards whose `rating` is "Review pending")

Judge what the LATIN says against what the GREEK says (read through `saints`; base the judgment on the Latin text where an English rendering is ambiguous). Choose exactly one category (the site's own definitions):
- **Same**: corresponding content; differences are only English wording or register (begot/fathered, word order, "Look"/"Behold").
- **Similar**: a modest difference of expression or emphasis (a synonym with a different nuance, singular/plural, a pronoun vs a name, a small particle or article).
- **Different**: a meaningful local detail differs (a different verb, object, image, number, name, place or condition) while the verse is otherwise parallel.
- **Divergent**: material present in one and absent in the other, or rearranged (a clause, phrase or sentence; a verse the Greek text does not contain).
- **Disparate**: a major difference of assertion, agency or consequence.

Where verse division makes the two sides cover visibly different amounts of text, judge what each card shows and use Divergent only if content is genuinely missing on one side. Verses that the Greek critical text omits but the Vulgate has (for example Mark 7:16, Luke 17:36, John 5:4) are Divergent.

Write:
- `note`: the layer-1 "Direct word comparison and meaning" text: 1–2 sentences, at most about 35 words, plain text, no HTML, in the site's style, e.g. "Genealogy and origin give different breadth to the heading while retaining Jesus, David, and Abraham." or "Latin adds 'and another two'; the Greek has only the second mile." For Same, say briefly what agrees and that the difference is English wording. You may cite a Latin word in plain text (Latin "supersubstantialem"). Do not cite Greek words unless you are certain of them.
- `cause`: the layer-5 "How and why the differences arose" text: one sentence, at most about 30 words. Say what kind of difference it is (English wording only; a lexical choice; a different textual reading in the Latin tradition; verse division; an addition or omission). Do not speculate about copyists, motives or doctrine; if the origin is not certain, say it is unresolved. For Same: "The difference is one of English wording; the Latin and Greek agree here."

Judge the classification on the corrected English if you corrected it.

## Output

Write a JSON list to the output file named in your task, one object per card, in input order:

```
{"card": "<card id>", "english_new": null | "<full corrected verse>", "correction": null | "<what was wrong, citing the Latin, max 30 words>", "category": "Same" | "Similar" | "Different" | "Divergent" | "Disparate" | null, "note": "<...>" | null, "cause": "<...>" | null}
```

- `english_new` is the full corrected English verse, or null if unchanged.
- `category`, `note`, `cause` are null for cards whose `rating` is not "Review pending" (they are already classified).
- Every input card must appear exactly once. Write only your own output file; do not create, modify or delete any other file.
