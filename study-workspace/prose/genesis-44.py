# Study prose for Genesis 44 — Saints Parallel Reader Study Workspace. Draft for review.
K, W, C = 'Knowledge', 'Wisdom', 'Command'
S, R = 'stated', 'reflection'
def ins(t, b, text): return {'type': t, 'basis': b, 'text': text}
def keeps(t): return {'dir': 'keeps', 'text': t}
def loses(t): return {'dir': 'loses', 'text': t}
def between(t): return {'dir': 'between', 'text': t}
AGREE = between("Hebrew, Greek, Latin and King James agree in substance; only the rendering of the divine name and small turns of phrase differ.")

CHAPTER = {
 'slug': 'genesis', 'chapter': 44,
 'chapterNote': (
  "The silver cup in Benjamin’s sack, the pursuit, the return, and Judah’s speech, the longest in Genesis, ending with his offer to be a slave in Benjamin’s "
  "place. The columns agree closely; the Hebrew keeps “the mouth of the sack,” “with whom it is found” without naming the cup, “the cup was found,” “Joseph’s house,” "
  "“a word in my lord’s ears,” “you are like Pharaoh,” “set my eyes on him,” “I said, he is surely torn” in 44:28, “my gray hairs,” Sheol, and Judah’s request “please "
  "let your servant remain.” The Greek keeps Joseph named in 44:1, an added “Why have you stolen my silver cup?” in 44:5, “the cup” named in 44:9, “he found the cup,” "
  "“you are next to Pharaoh,” “I will take care of him,” “you said, he has been devoured” in 44:28, “sickness,” “my old age,” Hades, and Judah’s statement “I will "
  "remain.” One Hebrew-column rendering was corrected today. The Latin and King James follow the Hebrew; the Latin has Judah go in first and “speak boldly.”"),
 'verses': {

 '44:1': {
  'received': "Joseph told his steward to fill the men’s sacks with all the food they could carry and put each man’s silver in his sack’s mouth.",
  'explain': ("The last test is set: silver again, and the cup. The Greek names Joseph; the Latin the top of the sack."),
  'shared': ["Fill the men’s sacks with food, as much as they can carry.", "Put each man’s silver in the mouth of his sack.", "Joseph commanded his steward."],
  'instructions': [ins(K, S, "Joseph again returned the brothers’ silver."), ins(W, R, "Silver returned a second time, and this time a cup added; Joseph is building the situation in which the brothers must choose between Benjamin and themselves.")],
  'entries': [],
  'lost': [keeps("An added Iōsēph as subject in the Greek."), between("Hebrew, Latin and King James “he commanded.”")]},

 '44:2': {
  'received': "Put my silver cup in the youngest’s sack with his grain money. He did as Joseph said.",
  'explain': ("Gavia, a goblet; the divining cup of verse 5. Benjamin is to be the thief. The Hebrew says my cup, the silver cup, the mouth of the sack; the Greek my silver cup, his sack."),
  'shared': ["Put my cup, the silver cup, in the youngest man’s sack.", "Put his grain money with it.", "He did as Joseph had said."],
  'instructions': [ins(K, S, "Joseph planted his cup on Benjamin."), ins(W, R, "The favourite is framed; Joseph makes Benjamin the one who must be abandoned or defended, and asks the ten what they will do this time with Rachel’s son.")],
  'entries': [],
  'lost': [between("Hebrew gevi‘i gevia ha-kesef be-fi amtachat ha-qaton, “my cup, the silver cup, in the mouth of the youngest’s sack,” is Greek to kondy mou to argyroun eis ton marsippon tou neōterou, “my silver cup in the youngest’s sack”; Latin and King James follow the Hebrew.")]},

 '44:3': {
  'received': "At first light the men were sent off with their donkeys.",
  'explain': ("The versions agree."),
  'shared': ["Morning dawned.", "The men were sent away.", "They and their donkeys."],
  'instructions': [ins(K, S, "The brothers departed at dawn.")],
  'entries': [],
  'lost': [AGREE]},

 '44:4': {
  'received': "Not far from the city, Joseph sent his steward after them: Why have you repaid evil for good?",
  'explain': ("Evil for good: the charge the brothers deserve, for another reason. The versions agree."),
  'shared': ["They had left the city and were not far off.", "Joseph said to his steward, Go after the men.", "When you overtake them, say, Why have you repaid evil for good?"],
  'instructions': [ins(K, S, "Joseph sent his steward in pursuit."), ins(W, R, "“Evil for good”: the words fit the sale of Joseph better than the cup, and the brothers will hear them as an accusation they cannot refute.")],
  'entries': [],
  'lost': [AGREE]},

 '44:5': {
  'received': "Is this not the cup my lord drinks from and divines with? You have done evil.",
  'explain': ("A divining cup, hydromancy; Joseph’s Egyptian mask includes magic. The Greek adds why have you stolen my silver cup; the Latin the cup you stole."),
  'shared': ["Is not this the cup from which my lord drinks?", "He practises divination with it.", "You have done evil in what you have done."],
  'instructions': [ins(K, S, "The steward accused them of stealing the divining cup."), ins(W, R, "Joseph lets his steward call him a diviner; the man who said interpretations belong to God wears the pagan’s reputation to finish the test.")],
  'entries': [],
  'lost': [keeps("An added hina ti eklepsate mou to kondy to argyroun, “why have you stolen my silver cup?” at the head of the Greek verse."), between("Latin “The cup you stole is the one” also names the theft; King James “Is not this it in which my lord drinketh?”")]},

 '44:6': {
  'received': "He overtook them and said these words.",
  'explain': ("The versions agree; the Latin in order."),
  'shared': ["He overtook them.", "He spoke to them.", "These same words."],
  'instructions': [ins(K, S, "The steward delivered the accusation.")],
  'entries': [],
  'lost': [AGREE]},

 '44:7': {
  'received': "Why does my lord say this? Far be it from your servants to do such a thing!",
  'explain': ("Indignation, honest for once. The Latin says such a disgraceful deed."),
  'shared': ["Why does my lord speak this way?", "Far be it from your servants.", "To do such a thing."],
  'instructions': [ins(K, S, "The brothers denied the theft.")],
  'entries': [],
  'lost': [between("Latin “as though your servants had committed such a disgraceful deed” paraphrases Hebrew chalilah la-avadekha, “far be it from your servants”; Greek and King James follow the Hebrew.")]},

 '44:8': {
  'received': "We brought back the silver we found in our sacks from Canaan; how would we steal silver or gold from your lord’s house?",
  'explain': ("The argument from character: men who return silver do not steal cups. The Hebrew says the mouths of our sacks; the Latin the tops."),
  'shared': ["We brought back from Canaan the silver we found in our sacks.", "How then could we steal?", "Silver or gold from your lord’s house."],
  'instructions': [ins(K, S, "The brothers cited their returned silver as proof."), ins(W, R, "They plead the honesty they have learned; the men who took silver for a brother now argue from returning it, and the argument is true.")],
  'entries': ['canaan'],
  'lost': [between("Hebrew be-fi amtechotenu, “in the mouth of our sacks,” is Greek en tois marsippois hēmōn, “in our sacks”; Latin “at the tops of our sacks,” King James “in our sacks’ mouths.”")]},

 '44:9': {
  'received': "Whoever of your servants has it, let him die, and the rest of us will be my lord’s slaves.",
  'explain': ("A rash oath, like Jacob’s in 31:32. The Hebrew says with whom it is found; the Greek names the cup. The Hebrew-column rendering was corrected today."),
  'shared': ["With whomever of your servants it is found.", "Let him die.", "And we will be slaves to our lord."],
  'instructions': [ins(K, S, "The brothers offered death and slavery as penalty."), ins(W, R, "Death for the thief and slavery for the rest: they swear it certain of innocence, and the cup is in Benjamin’s sack. Confidence in Genesis is the prelude to a reckoning.")],
  'entries': [],
  'lost': [between("Hebrew asher yimmatze itto, “with whom it is found,” is Greek par’ hō an heurethē to kondy, “with whom the cup is found”; Latin “found with what you seek,” King James “with whomsoever of thy servants it be found.”")]},

 '44:10': {
  'received': "He said: Let it be as you say, but only the one with whom it is found shall be my slave; the rest are blameless.",
  'explain': ("The steward lowers the penalty to what Joseph wants: Benjamin alone. The versions agree."),
  'shared': ["Let it be according to your words.", "He with whom it is found shall be my slave.", "The rest of you shall be blameless."],
  'instructions': [ins(K, S, "The steward set the penalty on the culprit alone."), ins(W, R, "The steward spares the ten and dooms the one; the test is designed so that they can walk away free and leave Benjamin, as they left Joseph.")],
  'entries': [],
  'lost': [AGREE]},

 '44:11': {
  'received': "Each quickly lowered his sack and opened it.",
  'explain': ("The versions agree."),
  'shared': ["They hastened.", "Each took his sack down to the ground.", "Each opened his sack."],
  'instructions': [ins(K, S, "The brothers opened their sacks for search.")],
  'entries': [],
  'lost': [AGREE]},

 '44:12': {
  'received': "He searched from eldest to youngest, and the cup was found in Benjamin’s sack.",
  'explain': ("Eldest to youngest, drawing out the suspense to the last sack. The Hebrew says the cup was found; the Greek he found."),
  'shared': ["He searched, beginning with the oldest and ending with the youngest.", "The cup.", "It was found in Benjamin’s sack."],
  'instructions': [ins(K, S, "The cup was found with Benjamin."), ins(W, R, "In the last sack, the favourite’s: the brothers’ oath has condemned Rachel’s son, and the ten must decide whether their father loses him too.")],
  'entries': [],
  'lost': [between("Hebrew va-yimmatze ha-gavia, “and the cup was found,” passive, is Greek kai heuren to kondy, “and he found the cup”; Latin “found the cup,” King James “the cup was found.”")]},

 '44:13': {
  'received': "They tore their clothes, reloaded their donkeys, and returned to the city.",
  'explain': ("They tear their clothes, as Jacob did for Joseph; they all go back. The Greek adds his sack."),
  'shared': ["They tore their clothes.", "Each man loaded his donkey.", "They returned to the city."],
  'instructions': [ins(K, S, "All the brothers returned with Benjamin."), ins(W, R, "They all go back. Ten free men return to the city with the condemned eleventh; the first answer to Joseph’s question is given by their feet.")],
  'entries': [],
  'lost': [keeps("An added ton marsippon autou, “his sack,” in the Greek: “each loaded his sack on his donkey.”"), between("Hebrew, Latin and King James “loaded his donkey.”")]},

 '44:14': {
  'received': "Judah and his brothers came to Joseph’s house, where he still was, and fell to the ground before him.",
  'explain': ("Judah first, now named as leader. The third prostration. The Greek lacks house; the Latin Judah went in first."),
  'shared': ["Judah and his brothers came to Joseph’s house.", "He was still there.", "They fell before him to the ground."],
  'instructions': [ins(K, S, "The brothers fell before Joseph in his house."), ins(W, R, "Judah and his brothers: the order of names is the chapter’s argument. The brother who sold Joseph leads the brothers back to him, to plead for Benjamin.")],
  'entries': [],
  'lost': [loses("Hebrew betah Yosef, “to Joseph’s house,” is Greek pros Iōsēph, “to Joseph,” without the house."), between("Latin “Judah went in first to Joseph with his brothers” adds; King James “came to Joseph’s house.”")]},

 '44:15': {
  'received': "Joseph said: What have you done? Did you not know a man like me divines?",
  'explain': ("Joseph keeps up the diviner. The Latin says no one equals me."),
  'shared': ["What is this deed you have done?", "Did you not know?", "A man such as I practises divination."],
  'instructions': [ins(K, S, "Joseph confronted the brothers.")],
  'entries': [],
  'lost': [between("Latin “no one equals me in the knowledge of divination” expands Hebrew nachesh yenachesh ish asher kamoni, “a man like me surely divines”; Greek and King James follow the Hebrew.")]},

 '44:16': {
  'received': "Judah said: What can we say or how clear ourselves? God has found out your servants’ guilt. We are my lord’s slaves, we and the one with the cup.",
  'explain': ("Judah confesses a guilt the cup did not create: God has found out. He offers all eleven, refusing the steward’s separation. The versions agree."),
  'shared': ["What can we say to my lord? How can we clear ourselves?", "God has found out your servants’ guilt.", "We are my lord’s slaves, both we and the man with whom the cup was found."],
  'instructions': [ins(K, S, "Judah confessed guilt and offered all as slaves."), ins(W, R, "“God has found out our guilt”: not the cup’s, but the pit’s. Judah accepts a false charge as a true judgment, and refuses to leave Benjamin to it alone.")],
  'entries': ['elohim'],
  'lost': [between("Hebrew avadim la-adoni, “slaves to my lord,” is Greek oiketai tō kyriō hēmōn, “household slaves to our lord”; Latin “See, we are all my lord’s slaves,” King James “we are my lord’s servants.”")]},

 '44:17': {
  'received': "Joseph said: Far be it from me; only the man with the cup will be my slave; the rest of you go up in peace to your father.",
  'explain': ("Joseph presses the separation: take your freedom and go home without him. The Greek says safely; the Latin the one who stole."),
  'shared': ["Far be it from me to do this.", "The man with whom the cup was found will be my slave.", "The rest of you go up in peace to your father."],
  'instructions': [ins(K, S, "Joseph offered freedom to all but Benjamin."), ins(W, R, "“Go up in peace to your father” without Benjamin: the exact temptation of chapter 37, offered again. Joseph gives them the pit a second time and watches.")],
  'entries': [],
  'lost': [between("Hebrew le-shalom, “in peace,” is Greek meta sōtērias, “with safety”; Latin “The one who stole the cup … go freely,” King James “get you up in peace unto your father.”")]},

 '44:18': {
  'received': "Judah came near: Please, my lord, let your servant speak a word in my lord’s ears, and do not be angry, for you are like Pharaoh.",
  'explain': ("The speech begins, the longest in Genesis, a plea and a confession. The Hebrew says you are like Pharaoh; the Greek next to Pharaoh; the Latin spoke boldly."),
  'shared': ["Judah approached him.", "Please, my lord, let your servant speak a word in my lord’s ears, and do not be angry.", "You are like Pharaoh."],
  'instructions': [ins(K, S, "Judah asked leave to plead."), ins(W, R, "Judah approaches: the verb of Abraham before God at Sodom. He pleads for a brother as Abraham pleaded for a city, and the plea is the making of him.")],
  'entries': [],
  'lost': [between("Hebrew ki khamokha ke-Far‘oh, “for you are like Pharaoh,” is Greek hoti sy ei meta Pharaō, “for you are next to Pharaoh”; Latin “spoke boldly … next to Pharaoh you are my lord”; King James “thou art even as Pharaoh.”")]},

 '44:19': {
  'received': "My lord asked his servants, Have you a father or a brother?",
  'explain': ("Judah retells the story from Joseph’s first question. The Greek addresses him directly."),
  'shared': ["My lord questioned his servants.", "Have you a father?", "Or a brother?"],
  'instructions': [ins(K, S, "Judah recalled Joseph’s first question.")],
  'entries': [],
  'lost': [between("Hebrew adoni sha’al et-avadav, “my lord asked his servants,” is Greek kyrie, sy ērōtēsas tous paidas sou, “my lord, you asked your servants”; Latin “You first asked your servants,” King James “My lord asked his servants.”")]},

 '44:20': {
  'received': "We said, We have an old father and a young son of his old age; his brother is dead, he alone is left of his mother, and his father loves him.",
  'explain': ("Judah tells Joseph’s own story to Joseph: his brother is dead. His father loves him: Judah states the favouritism without resentment now. The versions agree."),
  'shared': ["We have an old father and a young son born in his old age.", "His brother is dead, and he alone is left of his mother.", "His father loves him."],
  'instructions': [ins(K, S, "Judah described Benjamin and Jacob’s love."), ins(W, R, "“His father loves him,” Judah says of Benjamin, and it is no longer a grievance. The brother who hated Joseph for being loved pleads for Benjamin because he is.")],
  'entries': [],
  'lost': [AGREE]},

 '44:21': {
  'received': "You said, Bring him down to me that I may set my eyes on him.",
  'explain': ("The Hebrew idiom, set my eyes on, to see or to favour; the Greek take care of him."),
  'shared': ["You said to your servants.", "Bring him down to me.", "That I may set my eyes on him."],
  'instructions': [ins(K, S, "Judah recalled the demand for Benjamin.")],
  'entries': [],
  'lost': [between("Hebrew ve-asimah eni alav, “and I will set my eye on him,” is Greek kai epimeloumai autou, “and I will take care of him”; Latin “I will set my eyes upon him,” King James “that I may set mine eyes upon him.”")]},

 '44:22': {
  'received': "We said, The boy cannot leave his father; if he leaves him, he will die.",
  'explain': ("He will die: the father, as verse 31 shows, or the boy. The versions agree."),
  'shared': ["We said to my lord.", "The young man cannot leave his father.", "If he leaves his father, he will die."],
  'instructions': [ins(K, S, "Judah recalled their warning about Jacob.")],
  'entries': [],
  'lost': [AGREE]},

 '44:23': {
  'received': "You said, Unless your youngest brother comes down you shall not see my face again.",
  'explain': ("The versions agree."),
  'shared': ["You said to your servants.", "Unless your youngest brother comes down with you.", "You shall not see my face again."],
  'instructions': [ins(K, S, "Judah recalled Joseph’s condition.")],
  'entries': [],
  'lost': [AGREE]},

 '44:24': {
  'received': "When we went up to your servant my father we told him my lord’s words.",
  'explain': ("Your servant my father: Jacob again a servant. The Hebrew says my father; the Greek our father."),
  'shared': ["We went up to your servant our father.", "We told him.", "The words of my lord."],
  'instructions': [ins(K, S, "Judah recounted the report to Jacob.")],
  'entries': [],
  'lost': [between("Hebrew avi, “my father,” is Greek tou patros hēmōn, “our father,” here and in 44:27; Latin “our father,” King James “my father.”")]},

 '44:25': {
  'received': "Our father said, Go again, buy us a little food.",
  'explain': ("The versions agree."),
  'shared': ["Our father said.", "Go again.", "Buy us a little food."],
  'instructions': [ins(K, S, "Judah recalled Jacob’s instruction.")],
  'entries': [],
  'lost': [AGREE]},

 '44:26': {
  'received': "We said, We cannot go down unless our youngest brother is with us, for we cannot see the man’s face without him.",
  'explain': ("The versions agree."),
  'shared': ["We cannot go down.", "If our youngest brother goes with us we will go.", "We cannot see the man’s face unless our youngest brother is with us."],
  'instructions': [ins(K, S, "Judah recalled the brothers’ refusal.")],
  'entries': [],
  'lost': [AGREE]},

 '44:27': {
  'received': "Your servant my father said, You know my wife bore me two sons;",
  'explain': ("My wife: Rachel, the only one Jacob calls wife here. The Greek says our father."),
  'shared': ["Your servant my father said to us.", "You know.", "My wife bore me two sons."],
  'instructions': [ins(K, S, "Judah quoted Jacob on Rachel’s two sons."), ins(W, R, "“My wife bore me two sons”: Jacob has four wives and twelve sons and counts one wife and two. Judah repeats it to the second of the two without flinching.")],
  'entries': [],
  'lost': [between("Hebrew avi is Greek ho patēr hēmōn, “our father”; Latin “He answered,” King James “thy servant my father.”")]},

 '44:28': {
  'received': "one went from me and I said, Surely he is torn to pieces; I have not seen him since.",
  'explain': ("Jacob’s version of Joseph’s death, quoted to Joseph. The Hebrew says I said, surely torn; the Greek you said, devoured by a wild animal; the Latin you said."),
  'shared': ["One went away from me.", "He has surely been torn to pieces.", "I have not seen him since."],
  'instructions': [ins(K, S, "Judah quoted Jacob’s belief in Joseph’s death."), ins(W, R, "Joseph hears his own death told as his father tells it: torn to pieces, not seen since. The lie the brothers planted is quoted to its victim by its planter.")],
  'entries': [],
  'lost': [loses("Hebrew va-omar akh tarof toraf, “and I said, surely he is torn, torn,” becomes Greek kai eipate hoti thēriobrōtos gegonen, “and you said that he has been devoured by a beast”; the father’s own conclusion becomes the sons’ report."), between("Latin “you said, A wild beast has devoured him” follows the Greek; King James “I said, Surely he is torn in pieces.”")]},

 '44:29': {
  'received': "If you take this one too and harm befalls him, you will bring my gray hairs down to Sheol in sorrow.",
  'explain': ("Jacob’s words of 42:38 quoted. The Greek says sickness, on the journey, old age, Hades."),
  'shared': ["If you take this one from me too.", "Harm befalls him.", "You will bring my gray hairs down in sorrow to Sheol."],
  'instructions': [ins(K, S, "Judah quoted Jacob’s fear for Benjamin.")],
  'entries': [],
  'lost': [loses("Hebrew ason, “harm,” sevati, “my gray hairs,” She’olah, become Greek malakia en tē hodō, “sickness on the journey,” to gēras mou, “my old age,” eis hadou."), between("Latin “anything happens to him on the way … my gray hairs … the realm of the dead” and King James “mischief … my gray hairs … the grave” follow the Hebrew.")]},

 '44:30': {
  'received': "Now, if I return to my father without the boy, since his life is bound up with the boy’s,",
  'explain': ("Judah speaks for himself again. Bound up: Jacob’s soul tied to Benjamin’s. The Greek says hangs upon, our father."),
  'shared': ["If I return to your servant my father and the young man is not with us.", "His life.", "It is bound up with the young man’s life."],
  'instructions': [ins(K, S, "Judah described Jacob’s dependence on Benjamin."), ins(W, R, "“His life is bound up in the lad’s life”: Judah understands his father’s love for the son who is not Judah, and pleads from inside it. That understanding is the repentance.")],
  'entries': [],
  'lost': [between("Hebrew qeshurah be-nafsho, “bound up in his soul,” is Greek ekkrematai ek tēs toutou psychēs, “hangs upon this one’s soul”; Latin “his soul depends upon this one’s soul,” King James “his life is bound up in the lad’s life.”")]},

 '44:31': {
  'received': "when he sees the boy is gone he will die, and your servants will bring our father’s gray hairs down to Sheol in sorrow.",
  'explain': ("The father’s death foreseen. The Greek says old age, Hades, anguish."),
  'shared': ["When he sees the young man is not with us, he will die.", "Your servants will bring your servant our father’s gray hairs down.", "In sorrow to Sheol."],
  'instructions': [ins(K, S, "Judah foresaw Jacob’s death if Benjamin were lost."), ins(W, R, "“He will die”: Judah has seen his father mourn one son and knows he cannot survive the second. The brothers who caused the first grief now stand to prevent the second.")],
  'entries': [],
  'lost': [between("Hebrew sevat avdekha avinu, “the gray hairs of your servant our father,” is Greek to gēras tou paidos sou patros de hēmōn, “the old age of your servant and our father”; Hebrew be-yagon She’olah, Greek meta lypēs eis hadou; Latin and King James follow the Hebrew.")]},

 '44:32': {
  'received': "Your servant became surety for the boy to my father: if I do not bring him back I will bear the blame all my days.",
  'explain': ("The pledge of 43:9 recalled. The Greek adds and set him before you; the Latin let me especially be your slave."),
  'shared': ["Your servant became guarantor for the young man to my father.", "If I do not bring him back to you.", "I will bear the blame before my father all my days."],
  'instructions': [ins(K, S, "Judah recalled his pledge for Benjamin.")],
  'entries': [],
  'lost': [keeps("An added kai stēsō auton enantion sou, “and set him before you,” in the Greek, from 43:9."), between("Latin “Let me especially be your slave, for I took the boy into my own keeping” anticipates 44:33; King James follows the Hebrew.")]},

 '44:33': {
  'received': "So let your servant stay as my lord’s slave in the boy’s place, and let the boy go up with his brothers.",
  'explain': ("The offer: himself for Benjamin. The Hebrew asks, please let your servant remain; the Greek states, I will remain; the Latin I will remain."),
  'shared': ["Let your servant remain as my lord’s slave.", "In place of the young man.", "Let the young man go up with his brothers."],
  'instructions': [ins(K, S, "Judah offered himself as slave in Benjamin’s place."), ins(W, R, "“Let your servant abide instead of the lad”: the brother who sold a brother into slavery offers to become a slave for one. This is the turning of Judah, and of the whole story; Joseph can keep the mask no longer.")],
  'entries': [],
  'lost': [between("Hebrew yeshev-na avdekha, “please let your servant remain,” a request, is Greek nyn oun paramenō soi pais, “now therefore I will remain with you as a slave,” a statement; Latin “I will remain your slave,” King James “let thy servant abide.”")]},

 '44:34': {
  'received': "How could I go up to my father without the boy? I could not bear to see the evil that would come on my father.",
  'explain': ("The speech ends on the father. The Hebrew says with me; the Greek with us, could not bear; the Latin lest I stand as witness."),
  'shared': ["How could I go up to my father if the young man were not with me?", "I could not bear to see.", "The calamity that would befall my father."],
  'instructions': [ins(K, S, "Judah refused to face Jacob without Benjamin."), ins(W, R, "Judah ends with his father’s grief, not his own fate; the plea is for Jacob, whom Judah once let mourn a living son. He will not do it twice, and the man he is pleading with is that son.")],
  'entries': [],
  'lost': [between("Hebrew itti, “with me,” is Greek meth’ hēmōn, “with us”; Hebrew pen er’eh va-ra, “lest I see the evil,” is Greek hina mē idō ta kaka, rendered “I could not bear to see”; Latin “lest I stand as witness to the calamity,” King James “lest peradventure I see the evil.”")]},
 }
}
