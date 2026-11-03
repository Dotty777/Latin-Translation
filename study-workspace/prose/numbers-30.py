K, W, C = 'Knowledge', 'Wisdom', 'Command'
S, R = 'stated', 'reflection'
def ins(t, b, text): return {'type': t, 'basis': b, 'text': text}
def keeps(t): return {'dir': 'keeps', 'text': t}
def loses(t): return {'dir': 'loses', 'text': t}
def between(t): return {'dir': 'between', 'text': t}
AGREE = between("Hebrew, Greek, Latin and King James agree in substance; only the rendering of the divine name and small turns of phrase differ.")
NUM = [between("Verse numbering: the site follows the Hebrew and Greek, where English 29:40 is 30:1 and English 30:1–16 is 30:2–17.")]
CLEAN = [loses("Hebrew salach, 'YHWH will forgive her', is lost."), keeps("Greek 'the Lord will cleanse her' (katharizo)."), between("The Latin has 'the Lord will be gracious to her'; the King James 'the Lord shall forgive her'.")]
BOND = [loses("Hebrew issar, 'binding obligation', is lost."), keeps("Greek horismos, 'a self-imposed restriction', set as an alternative to the vow."), between("The Latin and King James have 'bond'.")]

def v(received, explain, shared, k, w, lost, entries=None, cmd=None):
    inst = [ins(K, S, k)]
    if cmd: inst.append(ins(C, S, cmd))
    inst.append(ins(W, R, w))
    return {'received': received, 'explain': explain, 'shared': shared, 'instructions': inst, 'entries': entries if entries is not None else [], 'lost': lost}

CHAPTER = {
 'slug': 'numbers', 'chapter': 30,
 'chapterNote': "Vows, and who may annul them. Moses relays the offering calendar (30:1, English 29:40), then tells the tribal heads the law of vows: a man who vows or swears must not profane his word. A daughter in her father's house: if he hears and is silent her vow stands; if he disallows it on the day he hears, it falls and YHWH forgives her. A woman who marries with vows upon her, or who vows in her husband's house: the same, with the husband. A widow or divorced woman's vow stands absolutely. A husband may establish or annul a vow of self-denial; silence day after day establishes it; annulling it late makes him bear her guilt. The site follows the Hebrew and Greek numbering (English 29:40 = 30:1; English 30:1–16 = 30:2–17). The Greek has 'any person' and makes the 'restriction' (horismos) a third alternative beside vow and oath (30:3), 'or' for 'and' (30:4), 'the Lord will cleanse her' for 'will forgive her' (30:6, 9, 13), lacks 'a rash utterance of her lips' (30:7), and at 30:16 has 'after the day' and 'his sin' for 'after he has heard' and 'her guilt'. The Latin at 30:7 has 'a woman with a husband' rather than one who marries with vows upon her, and at 30:14 names fasting and abstinence.",
 'verses': {
  '30:1': v("Moses told the Israelites everything YHWH had commanded Moses.", "All four columns agree; this is English 29:40.",
   ["Moses told Israel.", "Everything YHWH commanded.", "The offerings relayed."], "Moses passed on the calendar.", "The close of two chapters of altar arithmetic: the whole fixed year of sacrifice, handed down in a sentence. What God told Moses, Moses told the people, without remainder.", NUM, ['moses', 'yhwh-yahweh']),
  '30:2': v("Moses spoke to the heads of the Israelite tribes: this is what YHWH has commanded.", "'Heads' and 'rulers' name the same men; the Greek 'the word the Lord has commanded'.",
   ["To the heads of the tribes.", "This is the word.", "YHWH has commanded."], "The vow law went to the tribal heads.", "Vows are given to the heads of tribes, not to the priests: a vow is a civil and family matter before it is a temple one, and the men who judge disputes must know when a word binds.", NUM + [between("The Latin has 'princes'; the Greek 'rulers'; the King James 'heads'.")], ['moses', 'yhwh-yahweh']),
  '30:3': v("If a man vows a vow to YHWH or swears an oath to bind himself with a bond, he shall not profane his word; he shall do all that comes from his mouth.", "The Greek 'any person … a vow, or swears an oath, or sets a restriction on himself' gives three alternatives; the Hebrew two, with the bond describing the oath.",
   ["A vow or an oath.", "Not profane his word.", "Do all that comes from his mouth."], "A man's word to God binds him.", "'He shall not profane his word': the vocabulary of the sanctuary applied to speech. A word spoken to God is holy, and breaking it is a desecration, not merely a default.",
   BOND + [between("The Latin has 'a man'; the Greek 'any person'.")], ['yhwh-yahweh'], "Do not profane your word; do all that comes from your mouth."),
  '30:4': v("If a woman vows a vow to YHWH and binds herself with a bond in her father's house in her youth,", "The Hebrew 'and binds'; the Greek 'or sets a restriction'; the Latin runs on into the father's silence.",
   ["A woman vows.", "In her father's house.", "In her youth."], "The first case is the unmarried daughter.", "'In her youth' marks dependence, not age alone: a daughter under her father's roof speaks within his household, and her promise to God touches his house.",
   BOND + [between("The Latin carries the father's silence and her obligation into this verse; the Greek and King James hold them for the next.")], ['yhwh-yahweh']),
  '30:5': v("and her father hears her vow and bond and is silent toward her, all her vows stand and every bond she has bound on herself stands.", "The father's silence confirms in all four; the Latin says she must fulfil what she promised.",
   ["Her father hears.", "He is silent.", "Her vows stand."], "Silence confirms the daughter's vow.", "The father's silence is consent: to hear a vow and say nothing is to let it stand. The law makes silence do work, so that a house cannot later pretend it never knew.", [AGREE], []),
  '30:6': v("But if her father disallows her on the day he hears, none of her vows or bonds stand; YHWH will forgive her, because her father disallowed her.", "The Hebrew 'YHWH will forgive her' (salach); the Greek 'the Lord will cleanse her'; the Latin lacks the clause.",
   ["Her father disallows.", "On the day he hears.", "YHWH will forgive her."], "A father's veto releases his daughter.", "Forgiveness for a vow she did not break: the daughter meant her word, but her father's refusal unmakes it, and God holds her clear. Authority in the house carries liability with it.",
   CLEAN + [between("The Latin has no 'the Lord will forgive her' clause here.")], ['yhwh-yahweh']),
  '30:7': v("If she becomes a man's wife while her vows are on her, or a rash utterance of her lips by which she has bound herself,", "The Hebrew includes 'a rash utterance of her lips'; the Greek lacks the characterisation; the Latin has 'a woman with a husband'.",
   ["She marries.", "Her vows are on her.", "A rash utterance of her lips."], "Vows carried into marriage are the next case.", "'A rash utterance of her lips': the law knows that vows are made in heat. The question is not whether she meant it but whose house now answers for it.",
   [loses("Hebrew 'a rash utterance of her lips' (mibta) is lost."), keeps("Greek 'the pronouncement of her lips', without 'rash'."), between("The Latin has 'if she has a husband and vows'; the King James 'she had at all an husband, when she vowed, or uttered ought out of her lips'.")], []),
  '30:8': v("and her husband hears and is silent toward her on the day he hears, her vows stand and her bonds stand.", "All four columns agree; the Latin 'bound … must render'.",
   ["Her husband hears.", "Silent on that day.", "Her vows stand."], "The husband's silence confirms.", "The same rule transfers from father to husband: whoever heads the house she speaks in has one day to object, and his silence is his word.", [AGREE], []),
  '30:9': v("But if her husband disallows her on the day he hears, he annuls her vow and the utterance of her lips; YHWH will forgive her.", "The Greek 'all her vows and restrictions shall not stand … because her husband disallowed … the Lord will cleanse her'.",
   ["Her husband disallows.", "He annuls her vow.", "YHWH will forgive her."], "A husband's same-day veto annuls.", "'He annuls': the verb is the husband's act; the forgiveness is God's. The two together protect the woman from a vow she can no longer keep in a house that will not support it.", CLEAN, ['yhwh-yahweh']),
  '30:10': v("Every vow of a widow or a divorced woman, everything she has bound on herself, stands against her.", "All four columns agree; 'render' versus 'remain against her'.",
   ["A widow or divorced woman.", "Everything she has bound.", "Stands against her."], "The unattached woman's vow is absolute.", "No one can annul the widow's word: she is head of her own house, and the law that limits a daughter's and wife's vows here grants the independent woman the full weight of a man's.", [AGREE], [], "A widow's or divorced woman's vow stands."),
  '30:11': v("If she vowed in her husband's house, or bound herself with a bond by an oath,", "The Latin a single case; the Greek 'a vow or a restriction with an oath'.",
   ["In her husband's house.", "A vow.", "A bond by oath."], "The last case is the wife vowing at home.", "The fourth case closes the set: daughter at home, bride with old vows, widow, wife at home. The law moves through a woman's life and names who answers at each stage.", BOND, []),
  '30:12': v("and her husband heard, was silent, and did not disallow her, all her vows and bonds stand.", "All four columns agree; the Greek keeps 'against her'.",
   ["Her husband heard.", "Silent, not disallowing.", "All stands."], "Silence again establishes.", "Three verbs for one act: heard, was silent, did not disallow. The law spells out that knowledge plus inaction is consent.", [AGREE], []),
  '30:13': v("But if her husband annuls them on the day he hears, whatever came from her lips about vows or bonds does not stand; her husband annulled them, YHWH will forgive her.", "The Hebrew 'forgive'; the Greek 'cleanse'.",
   ["Her husband annuls.", "On the day he hears.", "YHWH will forgive her."], "A same-day annulment is clean.", "The third repetition of 'YHWH will forgive her': the woman is never the guilty party when a vow is undone by the house she lives in.", CLEAN, ['yhwh-yahweh']),
  '30:14': v("Every vow and every binding oath to humble herself, her husband may establish it or her husband may annul it.", "The Latin names fasting and abstinence and 'at his discretion'; the Greek 'establish or cancel'.",
   ["Every vow to humble herself.", "Her husband may establish.", "Or may annul."], "Vows of self-denial are the husband's call.", "'To humble herself': fasting and abstinence, the vows that reach into the shared life of the house. The husband's power here is over what affects the household, not over her relation to God.",
   [between("The Latin names 'fasting or abstaining' and 'at the husband's discretion'; the Greek, Hebrew and King James 'to afflict/humble the soul'.")], []),
  '30:15': v("But if her husband is wholly silent toward her from day to day, he establishes all her vows and bonds; he established them because he was silent on the day he heard.", "The Latin 'postponing his decision to another day'; the Greek 'remains silent from day to day'.",
   ["Silent from day to day.", "He establishes.", "Because he was silent."], "Delay is confirmation.", "A husband cannot sit on a vow: one day to speak, and after that his silence has already decided. The law refuses to let authority be exercised by indefinite postponement.",
   [between("The Latin has 'postponing his judgement to another day'; the Greek and King James 'altogether hold his peace from day to day'.")], []),
  '30:16': v("But if he annuls them after he has heard, he shall bear her guilt.", "The Hebrew 'after he has heard … her guilt'; the Greek 'after the day … his sin'; the Latin 'her iniquity'.",
   ["He annuls late.", "After he has heard.", "He bears her guilt."], "A late annulment transfers guilt to him.", "'He shall bear her guilt': the broken vow is still broken, and someone owes God for it. If the husband unmakes her word late, the debt moves to him. The woman is shielded at every turn; the man who misuses his say is not.",
   [loses("Hebrew 'after he has heard … he shall bear her guilt' is lost."), keeps("Greek 'after the day he heard … he shall bear his sin'."), between("The Latin and King James have 'her iniquity'.")], []),
  '30:17': v("These are the statutes YHWH commanded Moses between a man and his wife, and between a father and his daughter in her youth in her father's house.", "All four columns agree.",
   ["The statutes.", "Man and wife.", "Father and daughter."], "The vow law is household law.", "The colophon names the two relationships the chapter governs; it is a law of houses, of who may speak for whom before God, and the widow stands outside it as her own head.", NUM, ['yhwh-yahweh', 'moses']),
 },
}
