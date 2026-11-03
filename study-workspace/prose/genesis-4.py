# Study prose for Genesis 4 — Saints Parallel Reader Study Workspace. Draft for review.
K, W, C = 'Knowledge', 'Wisdom', 'Command'
S, R = 'stated', 'reflection'
def ins(t, b, text): return {'type': t, 'basis': b, 'text': text}
def keeps(t): return {'dir': 'keeps', 'text': t}
def loses(t): return {'dir': 'loses', 'text': t}
def between(t): return {'dir': 'between', 'text': t}

CHAPTER = {
 'slug': 'genesis', 'chapter': 4,
 'chapterNote': (
  "Cain and Abel, the first murder, Cain’s line and the birth of Seth are told alike in every column. What varies is the "
  "inner life of Cain and a few hard sayings. The Hebrew keeps Cain’s anger, sin crouching at the door, the fugitive and "
  "wanderer, the plural “bloods” of Abel, the name Nod with its echo of wandering, “therefore” before the sevenfold vengeance, "
  "and the beginning of calling on the name of YHWH. The Greek keeps Cain’s grief, a saying about offering and dividing "
  "correctly with the command “be still,” Cain’s invitation “let us go out into the plain,” groaning and trembling in place of "
  "wandering, “not so” before the vengeance, guilt too great to be forgiven, and Enosh who hoped to call on the name of the "
  "Lord God. The Latin and King James follow the Hebrew in most of these; the Latin alone has Cain’s invitation “let us go outside.”"),
 'verses': {

 '4:1': {
  'received': "Adam knew Eve, who bore Cain and said she had gained a man through the Lord.",
  'explain': ("The story moves outside the garden and the first child is born. “Knew” is the Bible’s word for the union of "
   "husband and wife. Eve names the child with a word of acquiring and credits God: the Hebrew says “with YHWH,” commonly "
   "understood as with his help; the Greek and Latin say “through God.” The Greek uses the names Adam and Eve, after calling her Life in 3:20."),
  'shared': ["Adam knew his wife Eve.", "She conceived and bore Cain.", "She spoke of gaining a man through the Lord."],
  'instructions': [ins(K, S, "The first child was born outside the garden and received with thanks to God."), ins(W, R, "A child is acknowledged as a gift before anything is known of what he will do.")],
  'entries': ['adam', 'eve', 'yhwh-yahweh'],
  'lost': [
   loses("Hebrew et-YHWH, “with YHWH,” is a terse phrase usually read as “with the help of YHWH.” Greek dia tou theou, “through God,” spells out the help and drops the name. The Hebrew still says “the human”; the Greek says Adam."),
   keeps("Greek egnō, “knew,” is the verb Matthew 1:25 uses of Joseph and Mary, so the Greek keeps the Hebrew idiom for marital union. Greek Eve returns here as a name after Zōē in 3:20."),
   between("Latin “through God” follows the Greek; King James “from the LORD” follows the Hebrew name."),
  ]},

 '4:2': {
  'received': "Eve bore Abel as well; Abel became a shepherd and Cain a worker of the ground.",
  'explain': ("A second son, and two ways of life: Abel with the flock, Cain with the soil that was cursed in 3:17. The "
   "Hebrew flock can be sheep and goats; the Greek says sheep. Abel’s Hebrew name is the word for a breath, which Ecclesiastes "
   "uses for vanity; Jesus and Hebrews remember him as righteous."),
  'shared': ["Eve bore Abel, Cain’s brother.", "Abel became a shepherd.", "Cain worked the ground."],
  'instructions': [ins(K, S, "The brothers took up the two first occupations, keeping flocks and working the ground."), ins(W, R, "Different callings are not yet rivalry; the trouble comes from the heart, not the work.")],
  'entries': ['eve'],
  'lost': [
   between("Hebrew tson, “flock,” includes sheep and goats; Greek probatōn, “sheep,” is narrower. Hebrew adamah, “ground,” is again Greek gē, “earth.” Latin and King James keep the shepherd and the tiller. Hebrew Hevel, “breath,” is the word of Ecclesiastes 1:2; Hebrews 11:4 calls Abel faithful."),
  ]},

 '4:3': {
  'received': "In time Cain brought the Lord an offering from the fruit of the ground.",
  'explain': ("Worship appears for the first time, and Cain begins it. He brings produce, the fruit of his own work. The "
   "Hebrew calls it a minchah, a gift or offering; the Greek calls it a sacrifice, the Latin gifts. The Greek word does not "
   "make it an animal offering, and nothing in the verse says why it will be refused."),
  'shared': ["After some time Cain brought an offering.", "It was from the fruit of the ground.", "It was brought to the Lord."],
  'instructions': [ins(K, S, "Cain offered the fruit of the ground to the Lord."), ins(W, R, "Bringing an offering is the beginning of worship; what the offering means depends on the one who brings it.")],
  'entries': ['yhwh-yahweh', 'lord-translation'],
  'lost': [
   loses("Hebrew minchah is a gift or tribute offering; Greek thysia is “sacrifice,” the word for an altar offering. The Hebrew YHWH is “the Lord.” The produce is the same in both; only the category of the offering shifts."),
   between("Latin munera, “gifts,” and King James “offering” stay nearer the Hebrew. Hebrew “after some time” is literally “at the end of days”; Latin has “after many days,” Greek “after some days.”"),
  ]},

 '4:4': {
  'received': "Abel brought the firstborn of his flock and their fat, and the Lord looked with favour on Abel and his offering.",
  'explain': ("Abel brings the best: firstborn animals and their fat portions. God regards him and his gift. The Greek calls "
   "Abel’s offerings “gifts,” the word Hebrews uses when it says God bore witness to his gifts, and sets them against Cain’s "
   "“sacrifices.” The Hebrew names YHWH; the Greek says God."),
  'shared': ["Abel also brought an offering.", "It was from the firstborn of his flock and their fat.", "The Lord regarded Abel and his offering."],
  'instructions': [ins(K, S, "God accepted Abel and his offering of the firstborn."), ins(W, R, "The first and the best given freely are the shape of an acceptable offering.")],
  'entries': ['yhwh-yahweh', 'god-theos'],
  'lost': [
   loses("Hebrew YHWH “regarded” Abel; the Greek has “God looked upon.” Hebrew tson, “flock,” is again Greek “sheep.”"),
   keeps("Greek dōra, “gifts,” for Abel against thysiai, “sacrifices,” for Cain in 4:3 and 4:5 is the Greek’s own distinction; Hebrews 11:4 takes up dōra. Greek prōtotoka, “firstborn,” is the word later used of Christ (Colossians 1:15)."),
   between("Latin “gifts” and “the Lord” split between the two; King James “firstlings” and “had respect unto” follow the Hebrew."),
  ]},

 '4:5': {
  'received': "The Lord did not regard Cain and his offering, and Cain’s face fell.",
  'explain': ("The refusal is stated without a reason, and Cain’s response is in his face. The Hebrew says he burned with "
   "anger; the Greek says he was deeply grieved. Both have his face fall, a picture of dejection that God will ask about in "
   "the next verse. The two emotions can belong to one rejection, but the texts choose differently."),
  'shared': ["The Lord did not regard Cain and his offering.", "Cain reacted strongly.", "His face fell."],
  'instructions': [ins(K, S, "Cain’s offering was not accepted and he took it badly."), ins(W, R, "How we take a refusal shows what the offering was for.")],
  'entries': [],
  'lost': [
   loses("Hebrew va-yichar le-Qayin me’od, “it burned greatly for Cain,” is anger. Greek elypēsen, “he was grieved,” is sorrow or distress. The Greek keeps this reading through 4:6, so the change is sustained, not accidental."),
   between("Latin iratus and King James “wroth” keep the anger of the Hebrew. All four have the fallen face (Greek synepesen tō prosōpō), the same picture as Nehemiah 2:2."),
  ]},

 '4:6': {
  'received': "The Lord asked Cain why he was angry and why his face had fallen.",
  'explain': ("Before Cain acts, God questions him, as he questioned Adam. The question names the emotion of verse 5: anger "
   "in the Hebrew, Latin and King James, grief in the Greek. The Greek also calls the speaker “the Lord God” where the Hebrew "
   "has YHWH alone, and addresses Cain by name."),
  'shared': ["The Lord spoke to Cain.", "He asked about Cain’s reaction.", "He asked why Cain’s face had fallen."],
  'instructions': [ins(K, S, "God questioned Cain about his anger before he sinned further."), ins(W, R, "God’s question is a chance to stop; the fallen face is noticed before the raised hand.")],
  'entries': ['lord-translation', 'yhwh-yahweh'],
  'lost': [
   loses("Hebrew lammah charah lakh, “why are you angry,” becomes Greek “why have you become deeply grieved,” carrying the reading of 4:5. Hebrew YHWH becomes Greek kyrios ho theos, “the Lord God.”"),
   between("Latin “the Lord said to him” drops Cain’s name; Latin and King James keep the anger."),
  ]},

 '4:7': {
  'received': "God warned Cain that right conduct brings acceptance and that sin, if not mastered, lies in wait.",
  'explain': ("The hardest verse in the chapter, and the versions read it differently. The Hebrew pictures sin crouching at "
   "the door like an animal, its desire toward Cain, and tells him he must rule over it. The Greek speaks of offering "
   "correctly but not dividing correctly, then commands “be still,” and says “his turning is toward you, and you shall rule over him,” words that may point to Abel. The Latin and King James follow the Hebrew picture."),
  'shared': ["Doing well has a good outcome.", "Doing wrong brings sin close.", "Cain is told he can and must rule."],
  'instructions': [ins(C, S, "Do well, and rule over the sin that waits for you."), ins(W, R, "Sin is pictured as a creature at the door, not yet inside; mastering it is still possible before the act.")],
  'entries': [],
  'lost': [
   loses("Hebrew chattat rovets, “sin crouching,” and teshuqato, “its desire,” give a picture of sin as a beast at the door to be mastered. Greek has no crouching sin and no door: ouk ean orthōs prosenenkēs, orthōs de mē dielēs, hēmartes, “if you offer correctly but do not divide correctly, you have sinned.” The Hebrew image is absent."),
   keeps("Greek hēsychason, “be still,” is a direct command to Cain, the verb of 1 Thessalonians 4:11. Greek hē apostrophē autou, “his turning,” and “you shall rule over him” repeat the pattern of 3:16; the masculine pronouns can refer to Abel, though that is debated."),
   between("Latin “will you not receive” and “sin at the door … its desire under you” and King James “accepted … sin lieth at the door” both follow the Hebrew shape. The Hebrew is compressed enough to allow several readings, and the Greek has taken one tied to the sacrifice."),
  ]},

 '4:8': {
  'received': "Cain spoke to Abel, and in the field he rose against his brother and killed him.",
  'explain': ("The first murder is told in a few words. The Hebrew says Cain spoke to Abel but does not say what; the Greek "
   "and Latin supply the words, an invitation to go out, into the plain or outside. All versions then put the brothers in the "
   "field, where Cain rises and kills. The Hebrew’s silence about the words should be left visible rather than filled in."),
  'shared': ["Cain spoke to his brother Abel.", "They were together in the field.", "Cain rose against Abel and killed him."],
  'instructions': [ins(K, S, "Cain murdered his brother Abel in the field."), ins(W, R, "The warning of verse 7 was not heeded; anger unmastered becomes violence.")],
  'entries': [],
  'lost': [
   keeps("Greek dielthōmen eis to pedion, “let us go out into the plain,” gives the content of Cain’s speech. The Hebrew only says “Cain spoke to Abel his brother” and moves to the field; the Greek fills the gap and names the place."),
   between("Latin egrediamur foras, “let us go outside,” also supplies words but without the plain; King James “Cain talked with Abel” keeps the Hebrew silence. 1 John 3:12 and Hebrews 11:4 look back on the killing."),
  ]},

 '4:9': {
  'received': "The Lord asked Cain where Abel was, and Cain denied knowing, asking if he was his brother’s keeper.",
  'explain': ("God’s question to Cain matches his question to Adam, “where?” Cain answers with a lie and a sneer. His word "
   "“keeper” is a guard, the same root as the task given to Adam in the garden and to the cherubim at its gate; Cain refuses "
   "the duty the word implies. The Hebrew names YHWH, the Greek says God."),
  'shared': ["The Lord asked Cain where Abel was.", "Cain said he did not know.", "Cain asked whether he was his brother’s keeper."],
  'instructions': [ins(K, S, "Cain lied to God and disowned responsibility for his brother."), ins(W, R, "We are our brother’s keeper; the question is meant to be answered yes.")],
  'entries': ['yhwh-yahweh', 'god-theos'],
  'lost': [
   loses("Hebrew YHWH asks the question; the Greek has “God.” Otherwise the question and the denial are the same."),
   keeps("Greek phylax, “keeper,” shares its root with phylassein in 2:15 and 3:24, so the Greek reader hears the keeping of the garden behind Cain’s refusal."),
   between("Latin and King James agree with the Hebrew in naming the Lord."),
  ]},

 '4:10': {
  'received': "God asked what Cain had done, for his brother’s blood was crying out from the ground.",
  'explain': ("The lie is answered by evidence that cannot be silenced. Abel’s blood has a voice, and it cries to God from "
   "the ground that received it. The Hebrew says “bloods,” a plural often read as the many lives lost in Abel; the Greek has "
   "one blood. Hebrews says the blood of Jesus speaks a better word than Abel’s."),
  'shared': ["God asked Cain what he had done.", "His brother’s blood cries out to God.", "The cry comes from the ground."],
  'instructions': [ins(K, S, "Innocent blood cries to God and is heard."), ins(W, R, "No act against another is hidden from God; the ground itself bears witness.")],
  'entries': [],
  'lost': [
   loses("Hebrew deme, “bloods,” is plural, an idiom for bloodshed that the Mishnah reads as Abel’s blood and all his unborn descendants. Greek haima is singular. Hebrew adamah, “ground,” is Greek “earth.”"),
   keeps("The Greek names God as the speaker where the Hebrew has only “He said.” Greek boa, “cries,” is the cry of Hebrews 12:24 and Revelation 6:10."),
   between("Latin “He said to him” and King James “he said” follow the Hebrew’s unnamed speaker and keep “ground.”"),
  ]},

 '4:11': {
  'received': "Cain is cursed from the ground that opened its mouth to receive his brother’s blood.",
  'explain': ("The curse on Cain comes through the ground, as the curse on Adam did. The soil that drank Abel’s blood now "
   "turns against the man who shed it. The earth “opening its mouth” will recur when it swallows Korah. The Hebrew again "
   "has “bloods”; the Greek one blood. The Latin says cursed “upon” the earth, the others “from” it."),
  'shared': ["Cain is cursed.", "The curse is bound to the ground.", "The ground received his brother’s blood from his hand."],
  'instructions': [ins(K, S, "Cain was cursed in relation to the ground that received Abel’s blood."), ins(W, R, "Violence poisons the place where it happens; the land itself is party to the wrong.")],
  'entries': [],
  'lost': [
   loses("Hebrew plural deme, “bloods,” is again Greek singular haima. Hebrew adamah becomes Greek gē. The personified earth opening its mouth is in both."),
   between("Latin “cursed upon the earth” changes the preposition; Hebrew, Greek and King James say “from.” Numbers 16:32 has the earth open its mouth again."),
  ]},

 '4:12': {
  'received': "The ground will no longer yield to Cain, and he will live unsettled on the earth.",
  'explain': ("The sentence has two parts: the ground will withhold its strength from Cain, and Cain himself will not be at "
   "rest. The Hebrew makes him a fugitive and a wanderer, a social condition; the Greek makes him groaning and trembling, a "
   "bodily one. The Latin says the ground will withhold its fruits. The farmer loses his field and his home at once."),
  'shared': ["Cain will work the ground.", "It will no longer give him its yield.", "He will have no rest on the earth."],
  'instructions': [ins(K, S, "Cain lost the fruit of the ground and a settled life."), ins(W, R, "The one who destroys a brother loses the ground under his own feet.")],
  'entries': [],
  'lost': [
   loses("Hebrew na‘ va-nad, “a fugitive and a wanderer,” describes exile and movement. Greek stenōn kai tremōn, “groaning and trembling,” describes Cain’s body and mind. The wandering is gone from the Greek, here and in 4:14."),
   between("Latin “wanderer and fugitive” and King James “fugitive and vagabond” follow the Hebrew; Latin “fruits” where the others have “strength.”"),
  ]},

 '4:13': {
  'received': "Cain told the Lord that his guilt and its burden were greater than he could bear.",
  'explain': ("Cain’s reply can be heard two ways, and the versions divide. The Hebrew word covers both a wrong and its "
   "punishment, and the verb can mean bear or forgive. The Hebrew and King James read “my punishment is greater than I can "
   "bear”; the Greek and Latin read “my guilt is too great to be forgiven.” The Greek uses the New Testament’s verb for forgiving sins."),
  'shared': ["Cain spoke to the Lord.", "He called his situation too great for him.", "He speaks of his wrong or its consequence, not of repentance."],
  'instructions': [ins(K, S, "Cain found his guilt or punishment too great to bear."), ins(W, R, "Despair at guilt is not the same as sorrow for the deed; Cain speaks of himself, not of Abel.")],
  'entries': ['lord-translation'],
  'lost': [
   loses("Hebrew gadol avoni min-neso, “my avon is greater than bearing,” lets avon mean both wrongdoing and its punishment, and nasa both bear and forgive. Greek meizōn hē aitia mou tou aphethēnai me, “my guilt is too great for me to be forgiven,” chooses guilt and forgiveness and closes the other reading."),
   keeps("Greek aphethēnai is aphiēmi, the ordinary New Testament verb for the forgiving of sins (Matthew 6:12; 9:2). The Greek reader hears Cain speaking of forgiveness."),
   between("Latin “too great to deserve forgiveness” sides with the Greek; King James “my punishment is greater than I can bear” with the Hebrew. Both are within the Hebrew’s range."),
  ]},

 '4:14': {
  'received': "Driven from the ground and hidden from God’s face, Cain feared that anyone who found him would kill him.",
  'explain': ("Cain spells out his sentence as he hears it: expelled from the soil, cut off from God’s face, unsettled, and in "
   "danger. The Hebrew states the expulsion as done, “You have driven me”; the Greek begins “If You drive me.” The "
   "wandering-or-trembling difference of 4:12 returns. Fear of being killed is in all four."),
  'shared': ["Cain is driven from the face of the ground.", "He will be hidden from God’s face.", "He fears that whoever finds him will kill him."],
  'instructions': [ins(K, S, "Cain feared death at the hands of others after his sentence."), ins(W, R, "The killer expects to be killed; violence teaches those who use it to fear it.")],
  'entries': [],
  'lost': [
   loses("Hebrew hen gerashta oti, “behold, You have driven me,” is a statement; Greek ei ekballeis me, “if You drive me,” is conditional. Hebrew “fugitive and wanderer” is again Greek “groaning and trembling.”"),
   between("Latin “See, today You drive me” and King James “thou hast driven me out” keep the statement with the Hebrew and the wandering."),
  ]},

 '4:15': {
  'received': "The Lord promised sevenfold vengeance on anyone who killed Cain, and set a sign on him for protection.",
  'explain': ("God answers Cain’s fear with protection. The Hebrew begins “therefore”; the Greek and Latin begin “not so,” "
   "rejecting the fear outright. The vengeance clause is hard in Greek, rendered here as discharging seven acts of "
   "vengeance, where the Hebrew has the killer suffer sevenfold. The sign is for Cain’s safety; no version describes what it looked like."),
  'shared': ["The Lord answered Cain.", "Whoever kills Cain will face sevenfold vengeance.", "The Lord set a sign on Cain so that no one who found him would kill him."],
  'instructions': [ins(K, S, "God protected Cain’s life even after the murder."), ins(W, R, "God does not hand the murderer over to murder; even Cain’s life is guarded.")],
  'entries': ['lord-translation'],
  'lost': [
   loses("Hebrew lakhen, “therefore,” opens the reply; Greek ouch houtōs, “not so,” contradicts Cain’s fear instead. Hebrew “shall suffer sevenfold vengeance” becomes Greek hepta ekdikoumena paralysei, a difficult clause provisionally rendered “will discharge seven acts of vengeance.” The Hebrew YHWH is the Lord God."),
   keeps("The Greek construction has been read, as in Basil’s Letter 260, to mean that killing Cain would release him from his continuing punishment. The reading needs philological review; it is reception, not a settled sense."),
   between("Latin “it shall certainly not be so” follows the Greek opening but “punished sevenfold” follows the Hebrew; King James “therefore” and “vengeance … sevenfold” follow the Hebrew. The sign (Hebrew ot, Greek sēmeion) is not described by any of them."),
  ]},

 '4:16': {
  'received': "Cain left the Lord’s presence and settled in the land of Nod, east of Eden.",
  'explain': ("Cain goes out from God’s presence and settles, but in a land whose Hebrew name means wandering. Nod comes from "
   "the same root as the “wanderer” of 4:12, a pun the Greek spelling Naid cannot carry. The Hebrew puts the land east of "
   "Eden; the Greek says opposite Eden, as it placed Adam in 3:24. The Latin gives no name and says Cain lived as a fugitive."),
  'shared': ["Cain went out from the Lord’s presence.", "He settled in a land near Eden.", "That land lay beyond the garden."],
  'instructions': [ins(K, S, "Cain left God’s presence and lived east of Eden."), ins(W, R, "To settle in a place called Wandering is the condition of the one who leaves God’s presence.")],
  'entries': ['eden', 'yhwh-yahweh'],
  'lost': [
   loses("Hebrew Nod, “wandering,” echoes nad in 4:12; Greek Naid is a spelling without the meaning. Hebrew qidmat-Eden, “east of Eden,” becomes Greek katenanti Edem, “opposite Eden.” YHWH is “God.”"),
   between("Latin omits the name and makes Cain a fugitive “east of Eden,” translating the sense of Nod rather than the name; King James keeps Nod and “on the east of Eden.”"),
  ]},

 '4:17': {
  'received': "Cain’s wife bore Enoch, and Cain built a city and named it after his son.",
  'explain': ("Cain’s line begins, and with it the first city. His son is Enoch, a name shared with the Enoch of Seth’s line "
   "who pleased God, and often linked to the Hebrew for dedicate. The Greek says Cain “was building” the city when he named "
   "it. Hebrews will speak of the patriarchs looking for a city whose builder is God. No version says where Cain’s wife came from."),
  'shared': ["Cain knew his wife and she bore Enoch.", "Cain built a city.", "He named the city after his son."],
  'instructions': [ins(K, S, "Cain built the first city and named it for his son Enoch."), ins(W, R, "The exile builds walls; a city is the fugitive’s answer to having no rest.")],
  'entries': [],
  'lost': [
   between("Hebrew and Greek agree; Greek ēn oikodomōn, “he was building,” gives the act as in progress, where Latin and King James say he built. The wife’s origin is supplied by none of them. Hebrews 11:10 and 11:16 speak of the city whose builder is God."),
  ]},

 '4:18': {
  'received': "Enoch’s line ran through Irad, Mehujael and Methushael to Lamech.",
  'explain': ("Four generations pass in one verse. The names of the middle three differ in form between Hebrew and Greek: "
   "Irad becomes Gaidad, Mehujael Maiel, Methushael Mathousala. The Greek Mathousala looks like the Methuselah of Seth’s "
   "line in chapter 5, but the two genealogies remain distinct. This Lamech is the seventh from Adam in Cain’s line."),
  'shared': ["Enoch had a son.", "The line passed through three more generations.", "It ended in Lamech."],
  'instructions': [ins(K, S, "Cain’s line continued for several generations to Lamech.")],
  'entries': [],
  'lost': [
   loses("Hebrew Irad, Mechuyael and Metushael appear in Greek as Gaidad, Maiel and Mathousala; the forms differ materially, and the Greek Mathousala coincides in spelling with Methuselah of 5:21 without merging the two lines."),
   between("Latin and King James keep the Hebrew forms of the names. In Seth’s line the seventh from Adam is Enoch, as Jude 14 notes; here it is Lamech."),
  ]},

 '4:19': {
  'received': "Lamech took two wives, Adah and Zillah.",
  'explain': ("Lamech is the first man in Scripture with two wives. The verse records it without comment, and all four "
   "versions agree exactly. Jesus will later point back past this to the one man and one woman of 2:24. Lamech’s wives are named, "
   "and through them his sons will found crafts and arts."),
  'shared': ["Lamech took two wives.", "One was Adah.", "The other was Zillah."],
  'instructions': [ins(K, S, "Lamech was the first man recorded with two wives."), ins(W, R, "The pattern of 2:24 bends in Cain’s line; what is recorded is not thereby approved.")],
  'entries': [],
  'lost': [
   between("Hebrew, Greek, Latin and King James agree in every detail. Matthew 19:4–6 returns to the one flesh of 2:24."),
  ]},

 '4:20': {
  'received': "Adah bore Jabal, the father of those who live in tents and keep livestock.",
  'explain': ("Lamech’s sons are founders. Jabal fathers the herdsmen who live in tents, the way of life the patriarchs will "
   "later follow. The Hebrew says he was the father of tent-dwellers and herders; the Greek makes the animal-keeping explicit, "
   "“livestock breeders who dwell in tents”; the Latin names tent-dwellers and shepherds as two groups."),
  'shared': ["Adah bore Jabal.", "He was the father of those who live in tents.", "His descendants kept livestock."],
  'instructions': [ins(K, S, "Jabal began the life of herdsmen in tents.")],
  'entries': [],
  'lost': [
   between("Hebrew “father of those who dwell in tents and keep livestock” becomes Greek “father of livestock breeders who dwell in tents,” one group with two marks; Latin makes “those who live in tents” and “shepherds” two groups; King James has “such as dwell in tents, and such as have cattle.” Greek skēnai, “tents,” is the word of Hebrews 11:9."),
  ]},

 '4:21': {
  'received': "His brother Jubal was the origin of those who play stringed and wind instruments.",
  'explain': ("Music begins with Jubal. The Hebrew calls him the father of all who play the lyre and pipe; the Greek says he "
   "introduced the harp and lyre. The instruments do not match neatly: the Hebrew kinnor and ugav correspond here to the Greek "
   "psaltērion and kithara, and none of these ancient names maps cleanly onto a modern instrument."),
  'shared': ["Jubal was Jabal’s brother.", "He was the origin of musicians.", "He is linked to two kinds of instrument."],
  'instructions': [ins(K, S, "Jubal began instrumental music."), ins(W, R, "Music is among the first human arts, and it arises in Cain’s line as well as anywhere.")],
  'entries': [],
  'lost': [
   loses("Hebrew avi kol-tofes kinnor ve-ugav, “father of all who handle lyre and pipe,” becomes Greek ho katadeixas psaltērion kai kitharan, “the one who introduced harp and lyre.” The founder becomes an introducer, and the pipe becomes a second stringed instrument."),
   between("Latin “father of those who play the lyre and pipe” and King James “father of all such as handle the harp and organ” keep the Hebrew’s “father of.” Instrument identities are conventional in every column."),
  ]},

 '4:22': {
  'received': "Zillah bore Tubal-cain, a worker in bronze and iron, whose sister was Naamah.",
  'explain': ("Metalwork begins with Zillah’s son. The Hebrew calls him Tubal-cain and describes him with a compact phrase about "
   "sharpening tools of bronze and iron; the Greek calls him Tubal and says plainly he was a hammering smith. His sister "
   "Naamah, whose name means pleasant, is one of the few women named in these early lists."),
  'shared': ["Zillah bore a son.", "He worked bronze and iron.", "His sister was Naamah."],
  'instructions': [ins(K, S, "Tubal-cain began the working of bronze and iron.")],
  'entries': [],
  'lost': [
   loses("Hebrew Tuval-Qayin, “Tubal-cain,” keeps Cain in the name; Greek Thobel, “Tubal,” drops it. Hebrew lotesh kol-choresh nechoshet u-varzel, a difficult phrase about sharpening or hammering every worker or tool of bronze and iron, becomes Greek sphyrokopos chalkeus, “hammering smith.”"),
   between("Latin keeps Tubal-cain and expands, “hammer-worker and craftsman in every kind of bronze and iron work”; King James has “an instructer of every artificer.” Greek Noema is Hebrew Na‘amah, “pleasant.”"),
  ]},

 '4:23': {
  'received': "Lamech boasted to his wives that he had killed a man for wounding him and a youth for bruising him.",
  'explain': ("The first poem in Scripture is a boast of violence. Lamech calls his wives to hear and tells them he has killed "
   "for a wound and for a bruise. The versions agree closely. The relation of the killing to the wound is open to "
   "interpretation, and none of the texts adds that he acted alone or in self-defence."),
  'shared': ["Lamech addressed his wives Adah and Zillah.", "He called them to hear his words.", "He claimed to have killed a man for a wound and a young man for a bruise."],
  'instructions': [ins(K, S, "Lamech boasted of killing in return for injury."), ins(W, R, "Violence grows in Cain’s line from murder to a song about murder.")],
  'entries': [],
  'lost': [
   between("Hebrew and Greek keep the parallel lines; Hebrew imrati, “my speech,” is Greek “my words.” Latin and King James give the same boast; King James “to my wounding … to my hurt” reads the Hebrew prepositions differently."),
  ]},

 '4:24': {
  'received': "Lamech claimed that if Cain is avenged sevenfold, he will be avenged seventy-sevenfold.",
  'explain': ("Lamech takes God’s protection of Cain and inflates it into a threat. The Hebrew says seventy-seven; the Greek "
   "idiom is rendered here as seventy times seven, though seventy-seven is also argued for it. The same Greek expression is "
   "the one Jesus uses when Peter asks how often to forgive, so Lamech’s measure of vengeance becomes a measure of mercy."),
  'shared': ["Cain’s vengeance was sevenfold.", "Lamech claims a far greater vengeance for himself.", "The boast builds on God’s word to Cain."],
  'instructions': [ins(K, S, "Lamech claimed a vengeance far beyond Cain’s."), ins(W, R, "What Lamech claims for revenge, Jesus turns into the measure of forgiveness.")],
  'entries': [],
  'lost': [
   loses("Hebrew shiv‘im ve-shiv‘ah, “seventy-seven,” is a plain number. Greek hebdomēkontakis hepta, “seventy times seven,” is an idiom that may also mean seventy-seven; the Greek ek, “from,” leaves the relation to the avenging act open."),
   keeps("Hebdomēkontakis hepta is the expression of Matthew 18:22. The Greek reader can hear Jesus answering Lamech."),
   between("Latin “shall be sevenfold … seventy-sevenfold” and King James “seventy and sevenfold” keep the Hebrew number; Latin makes the vengeance future, Greek past."),
  ]},

 '4:25': {
  'received': "Adam knew his wife again, and she bore Seth, saying God had given her another child in place of Abel.",
  'explain': ("After the line of Cain, the story returns to Adam and Eve and a new son. Seth’s name is explained by his "
   "mother: God has set, or appointed, another offspring in place of Abel. The Greek says God “raised up” another seed, a "
   "phrase about provision of offspring, not resurrection. The Greek names Eve and mentions conception where the Hebrew says “again.”"),
  'shared': ["Adam knew his wife and she bore a son.", "She named him Seth.", "She said God had given another offspring in place of Abel, whom Cain killed."],
  'instructions': [ins(K, S, "Seth was given in place of Abel."), ins(W, R, "Loss is answered by a new gift, and the gift is named for God’s act, not for the grief.")],
  'entries': ['adam', 'eve'],
  'lost': [
   loses("Hebrew shat, “appointed,” sounds like Shet, “Seth”; Greek exanestēsen, “raised up,” loses the sound-play. Hebrew od, “again,” is absent from the Greek, which instead names Eve and adds “conceived.” Hebrew “because Cain killed him” becomes Greek “whom Cain killed.”"),
   between("Latin and King James “appointed” keep the Hebrew verb and “again.” Luke 3:38 traces Jesus’ line through Seth."),
  ]},

 '4:26': {
  'received': "Seth had a son, Enosh, and in his time the name of the Lord began to be called upon.",
  'explain': ("The chapter ends with prayer. Enosh is born, a name that means man in his frailty, and calling on the name of "
   "the Lord begins. The Hebrew makes it a general beginning, “then people began to call”; the Greek makes it Enosh’s own hope, "
   "“he hoped to call upon the name of the Lord God”; the Latin says he began. Joel, Peter and Paul will promise salvation to whoever calls on that name."),
  'shared': ["Seth had a son named Enosh.", "The name of the Lord is called upon.", "This is the first mention of calling on the Lord’s name."],
  'instructions': [ins(K, S, "Calling on the name of the Lord began in the line of Seth."), ins(W, R, "Prayer begins with the awareness of frailty; the man named Frail is the one who calls.")],
  'entries': ['yhwh-yahweh', 'lord-translation'],
  'lost': [
   loses("Hebrew az huchal liqro be-shem YHWH, “then it was begun to call on the name of YHWH,” is impersonal. Greek houtos ēlpisen epikaleisthai to onoma kyriou tou theou, “he hoped to call upon the name of the Lord God,” makes Enosh the subject and turns beginning into hope. The Hebrew verb has also been read, in some Jewish interpretation, as profaning rather than beginning."),
   keeps("Greek epikaleisthai to onoma, “to call upon the name,” is the phrase of Joel 3:5 (2:32), Acts 2:21 and Romans 10:13."),
   between("Latin “he began to call” makes Enosh the subject with the Greek but keeps “began” with the Hebrew; King James “then began men to call” follows the Hebrew. Hebrew Enosh is the “man” of Psalm 8:4."),
  ]},
 }
}
