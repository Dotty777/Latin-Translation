# Study prose for Genesis 31 — Saints Parallel Reader Study Workspace. Draft for review.
K, W, C = 'Knowledge', 'Wisdom', 'Command'
S, R = 'stated', 'reflection'
def ins(t, b, text): return {'type': t, 'basis': b, 'text': text}
def keeps(t): return {'dir': 'keeps', 'text': t}
def loses(t): return {'dir': 'loses', 'text': t}
def between(t): return {'dir': 'between', 'text': t}
AGREE = between("Hebrew, Greek, Latin and King James agree in substance; only the rendering of the divine name and small turns of phrase differ.")

CHAPTER = {
 'slug': 'genesis', 'chapter': 31,
 'chapterNote': (
  "Jacob’s flight from Haran, Rachel’s theft of the household gods, Laban’s pursuit, the quarrel in Gilead, and the covenant at the heap of witness. The "
  "columns agree on the story and disagree most in the covenant scene, where the Greek distributes Laban’s words differently across 31:44–53. The Hebrew keeps "
  "“the land of your fathers,” “changed my wages ten times,” “Here I am,” “the God of Bethel,” the teraphim, the idiom “stole the heart of Laban,” “good or bad” "
  "in God’s warning, “I was afraid,” the Aramaic and Hebrew names Jegar-sahadutha and Galeed, Mizpah, “God is witness” in 31:50, a separate 31:51, and “the God of "
  "their father.” The Greek keeps “the land of your father,” “my wages of ten lambs” twice, “What is it?”, “the place of God” with an added “I will be with you,” "
  "“idols,” “Laban the Syrian” added twice, “speak evil,” an added search of the tents in a different order, the names translated as Witness Heap and The Heap "
  "Bears Witness and The Watch, God as witness moved to 31:44, no text at 31:51, and drinking at the covenant meal. The Latin and King James follow the Hebrew; the "
  "Latin adds “each according to his own language” and has Laban rise “in the night.” The reader numbers 31:55 where the Hebrew and Greek begin chapter 32."),
 'verses': {

 '31:1': {
  'received': "Jacob heard Laban’s sons saying he had taken all their father’s wealth.",
  'explain': ("Six years of the speckled-sheep wage have made Jacob rich and Laban’s sons resentful. Glory, kavod, here is wealth. The versions agree."),
  'shared': ["Jacob heard the words of Laban’s sons.", "Jacob has taken all that was our father’s.", "From our father’s property he has gained all this wealth."],
  'instructions': [ins(K, S, "Laban’s sons accused Jacob of taking their inheritance."), ins(W, R, "Isaac’s wealth drew Philistine envy; Jacob’s draws his cousins’. Blessing makes a man unwelcome, and the unwelcome are moved on toward the promise.")],
  'entries': ['jacob'],
  'lost': [AGREE]},

 '31:2': {
  'received': "Jacob saw that Laban’s face toward him had changed.",
  'explain': ("The Hebrew says Laban’s face was not with him as yesterday and the day before. The versions agree."),
  'shared': ["Jacob saw Laban’s countenance.", "It was not toward him as before.", "The welcome had cooled."],
  'instructions': [ins(K, S, "Jacob noticed Laban’s hostility.")],
  'entries': ['jacob'],
  'lost': [AGREE]},

 '31:3': {
  'received': "The Lord told Jacob to return to his fathers’ land and kindred, and promised to be with him.",
  'explain': ("The command to return, with the Bethel promise repeated. The Hebrew says the land of your fathers; the Greek your father, singular; the Latin fathers, and above all the Lord was saying."),
  'shared': ["The Lord said to Jacob.", "Return to the land of your fathers and your kindred.", "I will be with you."],
  'instructions': [ins(C, S, "Return to the land of your fathers and your kindred."), ins(K, S, "God commanded Jacob’s return."), ins(W, R, "Three reasons to go arrive together: the sons’ envy, Laban’s face, and God’s word. Providence speaks through circumstance and then in its own voice.")],
  'entries': ['jacob', 'yhwh-yahweh'],
  'lost': [between("Hebrew eretz avotekha, “the land of your fathers,” is Greek tēn gēn tou patros sou, “the land of your father”; Latin “fathers,” King James “fathers.”")]},

 '31:4': {
  'received': "Jacob called Rachel and Leah to the field.",
  'explain': ("A private council away from the camp; Rachel is named first. The versions agree."),
  'shared': ["Jacob sent and called Rachel and Leah.", "He called them to the field.", "His flock was there."],
  'instructions': [ins(K, S, "Jacob consulted his wives privately.")],
  'entries': ['jacob'],
  'lost': [AGREE]},

 '31:5': {
  'received': "He told them their father’s face had changed, but the God of his father had been with him.",
  'explain': ("Jacob’s speech to his wives, the longest he has made. The God of my father: not yet my God. The versions agree."),
  'shared': ["I see that your father’s countenance is not toward me as before.", "But the God of my father.", "He has been with me."],
  'instructions': [ins(K, S, "Jacob contrasted Laban’s hostility with God’s presence."), ins(W, R, "Jacob’s theology is still his father’s; the God who has kept him for twenty years is “the God of my father.” Bethel’s vow waits on the homecoming.")],
  'entries': ['jacob'],
  'lost': [AGREE]},

 '31:6': {
  'received': "You know I have served your father with all my strength.",
  'explain': ("The appeal to the record. The versions agree."),
  'shared': ["You yourselves know.", "With all my power.", "I have served your father."],
  'instructions': [ins(K, S, "Jacob asserted his faithful service.")],
  'entries': [],
  'lost': [AGREE]},

 '31:7': {
  'received': "Your father cheated me and changed my wages ten times, but God did not let him harm me.",
  'explain': ("Ten times is round for often. The Greek reads the Hebrew monim, times, as if lambs, my wages of ten lambs, an odd phrase repeated in verse 41; the Hebrew, Latin and King James ten times. Deceived, hetel, is a new word for an old pattern."),
  'shared': ["Your father has deceived me.", "He changed my wages repeatedly.", "God has not allowed him to harm me."],
  'instructions': [ins(K, S, "Jacob accused Laban of repeated fraud."), ins(W, R, "Jacob the deceiver names deception in another; twenty years with Laban have taught him what it is to be on the receiving end.")],
  'entries': ['elohim'],
  'lost': [loses("Hebrew ve-hechelif et-maskurti aseret monim, “and changed my wages ten times,” becomes Greek kai ēllaxen ton misthon mou tōn deka amnōn, “and changed my wages of ten lambs”; monim, “times,” is read as a count of animals."), between("Latin “changed my wages ten times” and King James “ten times” follow the Hebrew.")]},

 '31:8': {
  'received': "Whatever marking he named as my wages, the flock bore that kind.",
  'explain': ("Laban kept moving the terms; the flock kept following them. The Hebrew says speckled, striped; the Greek variegated, white; the Latin variegated, white; the King James speckled, ringstraked."),
  'shared': ["If he said the speckled shall be your wages, all the flock bore speckled.", "If he said the striped shall be your wages, all bore striped.", "The wage followed Laban’s word."],
  'instructions': [ins(K, S, "The flock bore whatever Laban named as Jacob’s wage."), ins(W, R, "Laban changes the rules and the sheep change with them; Jacob tells it as providence, not husbandry, and the rods go unmentioned.")],
  'entries': [],
  'lost': [between("Hebrew nequddim … aquddim, “speckled … striped,” is Greek poikila … leuka, “variegated … white”; Latin “variegated … white,” King James “speckled … ringstraked.”")]},

 '31:9': {
  'received': "So God took your father’s livestock and gave it to me.",
  'explain': ("Jacob’s own account of the flocks: God took and gave. The Greek adds all; the Latin possessions."),
  'shared': ["God has taken away.", "He took your father’s livestock.", "He gave them to me."],
  'instructions': [ins(K, S, "Jacob credited God with his flocks."), ins(W, R, "“God has taken and given”: the rods of chapter 30 are not mentioned; in Jacob’s telling, the wealth is God’s doing, and the narrator lets the two accounts stand side by side.")],
  'entries': ['elohim'],
  'lost': [keeps("An added panta, “all,” before the livestock in the Greek."), between("Latin “your father’s possessions,” King James “the cattle of your father.”")]},

 '31:10': {
  'received': "At mating time I saw in a dream that the males mounting the flock were striped, speckled and mottled.",
  'explain': ("A dream not told in chapter 30. The Hebrew says male goats, striped, speckled, mottled; the Greek male goats and rams, white-marked, variegated, ash-gray spotted; the King James grisled."),
  'shared': ["It was the time the flock mated.", "I looked up in a dream.", "The males mounting the flock were marked."],
  'instructions': [ins(K, S, "Jacob reported a dream of marked males.")],
  'entries': ['jacob'],
  'lost': [keeps("An added kai hoi krioi, “and the rams,” and epi ta probata kai tas aigas, “on the sheep and goats,” in the Greek; Hebrew ha-attudim, “the he-goats.”"), between("Latin “the males mounting the females” and King James “the rams which leaped upon the cattle” vary.")]},

 '31:11': {
  'received': "The angel of God called me in the dream, and I said, Here I am.",
  'explain': ("The angel of God, as at Beersheba for Hagar and Moriah for Abraham. The Hebrew says Here I am, hinneni; the Greek What is it?; the Latin Here I am."),
  'shared': ["The angel of God spoke to me in the dream.", "Jacob.", "I answered."],
  'instructions': [ins(K, S, "The angel of God addressed Jacob in a dream."), ins(W, R, "“Here I am” is Abraham’s answer at Moriah and Isaac’s and Esau’s in chapter 27; Jacob says it to God at last, in a dream about sheep.")],
  'entries': ['angel-of-the-lord', 'jacob'],
  'lost': [loses("Hebrew hinneni, “here I am,” becomes Greek ti estin, “what is it?”"), between("Latin “Here I am” and King James “Here am I” follow the Hebrew.")]},

 '31:12': {
  'received': "He said, Look up: the males mounting the flock are all marked, for I have seen what Laban is doing to you.",
  'explain': ("The dream explained: God has seen Laban. The pattern words repeat verse 10. The versions agree in substance."),
  'shared': ["Look up and see.", "All the males mounting the flock are striped, speckled and mottled.", "I have seen all that Laban is doing to you."],
  'instructions': [ins(K, S, "God told Jacob He had seen Laban’s dealings."), ins(W, R, "“I have seen”: the God who saw Leah unloved sees Jacob cheated. The marked flock is a verdict, not a trick.")],
  'entries': ['elohim'],
  'lost': [between("Hebrew aquddim nequddim u-veruddim, “striped, speckled, mottled,” is Greek dialeukoi kai poikiloi kai spodoeideis rhantoi; Latin “variegated, spotted, and speckled,” King James “ringstraked, speckled, and grisled.”")]},

 '31:13': {
  'received': "I am the God of Bethel, where you anointed a pillar and vowed; now leave this land and return to the land of your birth.",
  'explain': ("The God of Bethel recalls the vow and commands the return that will trigger it. The Hebrew says the God of Bethel; the Greek the God who appeared to you in the place of God, and adds and I will be with you; the Latin the God of Bethel, the stone."),
  'shared': ["I am the God of Bethel.", "There you anointed a pillar and made a vow to Me.", "Now arise, leave this land, and return to the land of your birth."],
  'instructions': [ins(C, S, "Arise, leave this land and return to the land of your birth."), ins(W, R, "God identifies Himself by Jacob’s vow: the God of Bethel is the God to whom Jacob owes a tenth and a house. The return is also a reckoning.")],
  'entries': ['bethel', 'elohim'],
  'lost': [keeps("Greek ho theos ho ophtheis soi en topō theou, “the God who appeared to you in the place of God,” for Hebrew ha-El Bet-El, “the God of Bethel,” and an added kai esomai meta sou, “and I will be with you.”"), between("Latin “the God of Bethel, where you anointed the stone” and King James “the God of Bethel … the pillar” follow the Hebrew without the addition.")]},

 '31:14': {
  'received': "Rachel and Leah asked whether any portion or inheritance was left them in their father’s house.",
  'explain': ("The sisters, for once, speak with one voice. The versions agree."),
  'shared': ["Rachel and Leah answered.", "Is there any portion or inheritance for us?", "In our father’s house."],
  'instructions': [ins(K, S, "Jacob’s wives agreed to leave Laban.")],
  'entries': [],
  'lost': [AGREE]},

 '31:15': {
  'received': "He treats us as strangers; he sold us and consumed our price.",
  'explain': ("The daughters’ grievance: the bride-price, Jacob’s fourteen years, went to Laban and never came to them as dowry. The versions agree."),
  'shared': ["Are we not counted as strangers by him?", "He has sold us.", "He has entirely consumed our money."],
  'instructions': [ins(K, S, "Rachel and Leah accused Laban of selling them."), ins(W, R, "The sisters were sold for labour and the price spent; their bitterness toward their father is the one thing the two have shared without rivalry.")],
  'entries': [],
  'lost': [AGREE]},

 '31:16': {
  'received': "The wealth God took from our father is ours and our children’s; do whatever God has told you.",
  'explain': ("The wives’ consent. The Greek adds and glory; the Latin delivered them to us."),
  'shared': ["All the wealth God has taken from our father is ours and our children’s.", "Now therefore.", "Do whatever God has said to you."],
  'instructions': [ins(K, S, "The wives endorsed Jacob’s departure as God’s word."), ins(W, R, "“Do whatever God has spoken”: the daughters of Laban the diviner speak better faith than their father, and the household leaves Haran in agreement.")],
  'entries': ['elohim'],
  'lost': [keeps("An added kai tēn doxan, “and the glory,” after wealth in the Greek."), between("Latin “God has taken our father’s riches and delivered them to us” and King James “all the riches which God hath taken” follow the Hebrew.")]},

 '31:17': {
  'received': "Jacob set his children and wives on camels.",
  'explain': ("The Hebrew orders children then wives; the Greek wives then children; the Latin adds and departed."),
  'shared': ["Jacob arose.", "He put his children and wives on camels.", "The departure began."],
  'instructions': [ins(K, S, "Jacob mounted his family for the journey.")],
  'entries': ['jacob'],
  'lost': [between("Hebrew banav ve-et-nashav, “his children and his wives,” is Greek tas gynaikas autou kai ta paidia autou, “his wives and his children”; Latin “children and wives … and departed”; King James “sons and his wives.”")]},

 '31:18': {
  'received': "He drove off all his livestock and goods gained in Paddan-aram, to go to Isaac in Canaan.",
  'explain': ("The Hebrew repeats livestock, miqneh, twice, the livestock of his acquiring; the Greek says belongings and household goods, aposkeuē, which can include dependants; the Latin possessions, flocks, Mesopotamia."),
  'shared': ["He drove away all his livestock and goods.", "He had acquired them in Paddan-aram.", "He went to Isaac his father in the land of Canaan."],
  'instructions': [ins(K, S, "Jacob set out for Isaac in Canaan with all he had."), ins(W, R, "He came with a staff and leaves with a household; the twenty years are counted in camels, and the land he left is the land he returns to.")],
  'entries': ['jacob', 'isaac', 'canaan', 'haran'],
  'lost': [between("Hebrew kol-miqnehu … miqneh qinyano, “all his livestock … the livestock of his acquiring,” is Greek panta ta hyparchonta autou kai pasan tēn aposkeuēn autou, “all his belongings and all his household goods”; Hebrew Paddan Aram is Greek Mesopotamia; Latin “possessions, his flocks … Mesopotamia”; King James “cattle … Padanaram.”")]},

 '31:19': {
  'received': "While Laban was shearing, Rachel stole her father’s household gods.",
  'explain': ("Teraphim, small figures, household gods or ancestral images; their function is disputed, and Rachel’s motive is not given. The Hebrew keeps the word; the Greek and Latin idols; the King James images."),
  'shared': ["Laban had gone to shear his sheep.", "Rachel stole.", "She took her father’s household gods."],
  'instructions': [ins(K, S, "Rachel stole Laban’s teraphim."), ins(W, R, "Rachel steals her father’s gods as Jacob stole his brother’s blessing; the household of promise leaves Haran with idols in its baggage, and will bury them at Shechem.")],
  'entries': [],
  'lost': [between("Hebrew ha-terafim, a term left untranslated, is Greek ta eidōla, “the idols,” Latin idola, King James “the images.”")]},

 '31:20': {
  'received': "Jacob stole away from Laban the Aramean by not telling him he was leaving.",
  'explain': ("The Hebrew idiom is Jacob stole the heart of Laban, deceived him, a pun on Rachel’s theft; the Greek concealed his departure; the Latin was unwilling to tell his father-in-law."),
  'shared': ["Jacob deceived Laban the Aramean.", "He did not tell him.", "He was fleeing."],
  'instructions': [ins(K, S, "Jacob left without telling Laban."), ins(W, R, "Rachel steals the gods and Jacob steals Laban’s heart; the narrator uses one verb for both, and the family of promise leaves Haran as thieves.")],
  'entries': ['jacob'],
  'lost': [between("Hebrew va-yignov Ya‘aqov et-lev Lavan, “Jacob stole the heart of Laban,” an idiom, is Greek ekrypsen de Iakōb Laban ton Syron, “Jacob hid from Laban the Syrian”; Latin “unwilling to tell his father-in-law”; King James “stole away unawares to Laban.”")]},

 '31:21': {
  'received': "He fled with all he had, crossed the River and set his face toward Gilead.",
  'explain': ("The River is the Euphrates; Gilead is the hill country east of Jordan. The Hebrew says set his face; the Greek rushed; the Latin journeyed."),
  'shared': ["He fled with all that he had.", "He crossed the River.", "He headed toward the mountain of Gilead."],
  'instructions': [ins(K, S, "Jacob crossed the Euphrates toward Gilead.")],
  'entries': ['jacob'],
  'lost': [between("Hebrew va-yasem et-panav har ha-Gil‘ad, “and set his face toward the mountain of Gilead,” is Greek hōrmēsen eis to oros Galaad, “rushed to the mountain of Gilead”; Latin “journeyed toward,” King James “set his face toward.”")]},

 '31:22': {
  'received': "Laban was told on the third day that Jacob had fled.",
  'explain': ("Three days’ start, the distance Laban had put between the flocks. The Greek adds the Syrian."),
  'shared': ["It was reported to Laban.", "It was on the third day.", "Jacob had fled."],
  'instructions': [ins(K, S, "Laban learned of the flight after three days.")],
  'entries': ['jacob'],
  'lost': [keeps("An added tō Syrō, “the Syrian,” after Laban in the Greek."), between("Hebrew, Latin and King James without it.")]},

 '31:23': {
  'received': "He took his kinsmen, pursued seven days, and overtook Jacob in the hills of Gilead.",
  'explain': ("A seven-day chase to catch a herd moving slowly. The Greek adds all his kinsmen. Brethren is kin."),
  'shared': ["He took his kinsmen with him.", "He pursued seven days’ journey.", "He overtook him in the mountain of Gilead."],
  'instructions': [ins(K, S, "Laban overtook Jacob in Gilead."), ins(W, R, "Laban pursues with kin as Abraham pursued the kings; the chase is to recover daughters and gods, and he will find he can keep neither.")],
  'entries': ['jacob'],
  'lost': [keeps("An added pantas, “all,” before his kinsmen in the Greek."), between("Hebrew, Latin and King James “his brethren.”")]},

 '31:24': {
  'received': "God came to Laban the Aramean in a night dream and warned him not to speak to Jacob good or bad.",
  'explain': ("The Hebrew idiom good or bad means do nothing at all, as in 24:50; the Greek speak evil; the Latin speak harshly, and drops at night and the Aramean."),
  'shared': ["God came to Laban in a dream at night.", "Be careful.", "Do not speak to Jacob good or bad."],
  'instructions': [ins(K, S, "God restrained Laban in a dream."), ins(W, R, "God speaks to the diviner in his sleep, as to Abimelech; the Lord protects Jacob through the dreams of the men who mean him harm.")],
  'entries': ['elohim'],
  'lost': [between("Hebrew mi-tov ad-ra, “from good to bad,” the idiom of total restraint, is Greek ponēra, “evil things”; Latin “speak harshly” and drops “the Syrian” and “at night”; King James “either good or bad.”")]},

 '31:25': {
  'received': "Laban overtook Jacob, who had camped in the hills; Laban and his kin camped in Gilead too.",
  'explain': ("Two camps on one mountain. The Hebrew says Laban camped with his kinsmen; the Greek stationed his kinsmen; the Latin pitched his own tent on the same mountain."),
  'shared': ["Laban overtook Jacob.", "Jacob had pitched his tent in the hills.", "Laban with his kinsmen camped in the hill country of Gilead."],
  'instructions': [ins(K, S, "The two parties camped facing each other in Gilead.")],
  'entries': ['jacob'],
  'lost': [between("Hebrew ve-Lavan taqa et-echav, “and Laban pitched with his brethren,” is Greek Laban de estēsen tous adelphous autou, “Laban stationed his brethren”; Latin “he pitched his own tent on the same mountain”; King James “Laban with his brethren pitched.”")]},

 '31:26': {
  'received': "Laban asked what Jacob had done, deceiving him and carrying off his daughters like captives of war.",
  'explain': ("Laban’s indictment opens with Jacob’s own words to him in 29:25, what have you done? The Greek adds a separate question, why did you run away secretly and defraud me."),
  'shared': ["What have you done?", "You have deceived me.", "You have carried off my daughters like captives taken by the sword."],
  'instructions': [ins(K, S, "Laban accused Jacob of abducting his daughters."), ins(W, R, "“What have you done to me?” was Jacob’s cry on the morning after Leah; Laban returns it word for word. The two deceivers speak one language.")],
  'entries': ['jacob'],
  'lost': [keeps("An added hina ti kryphē apedras kai eklopophorēsas me, “why did you run away secretly and defraud me,” in the Greek, drawn from 31:27."), between("Latin “Why have you acted like this, secretly driving my daughters away” and King James “stolen away unawares to me” follow the Hebrew.")]},

 '31:27': {
  'received': "Why flee secretly, when I would have sent you off with songs, tambourine and lyre?",
  'explain': ("Laban paints the farewell he would have given. The Hebrew asks why; the Greek, having asked in verse 26, says if you had told me; the Latin why did you choose."),
  'shared': ["You fled secretly and did not tell me.", "I would have sent you away with joy and songs.", "With tambourine and lyre."],
  'instructions': [ins(K, S, "Laban claimed he would have given a festive send-off.")],
  'entries': [],
  'lost': [between("Hebrew lammah nachbeta livroach, “why did you hide to flee,” a question, is Greek kai ei anēngeilas moi, “and if you had told me,” the question having been moved to 31:26; Latin and King James keep the question here.")]},

 '31:28': {
  'received': "You did not let me kiss my children; you have acted foolishly.",
  'explain': ("The Hebrew says you did not allow me; the Greek I was not thought worthy; the Latin runs on into verse 29."),
  'shared': ["I could not kiss my sons and daughters.", "You did not allow it.", "You have acted foolishly."],
  'instructions': [ins(K, S, "Laban complained of the lost farewell.")],
  'entries': [],
  'lost': [between("Hebrew ve-lo netashtani, “and you did not let me,” is Greek kai ouk ēxiōthēn, “and I was not thought worthy”; Latin “you did not allow me,” King James “hast not suffered me.”")]},

 '31:29': {
  'received': "I have power to harm you, but the God of your father warned me last night not to speak to Jacob good or bad.",
  'explain': ("Laban admits the restraint. The Hebrew says it is in the power of my hand, the God of your father, good or bad; the Greek and now my hand has power, evil things; the Latin the God of your fathers, yesterday."),
  'shared': ["It is in the power of my hand to do you harm.", "But the God of your father spoke to me last night.", "Take heed not to speak to Jacob good or bad."],
  'instructions': [ins(K, S, "Laban admitted God had restrained him."), ins(W, R, "“The God of your father”: Laban, like Jacob, cannot yet call Him Jacob’s God. The restraint is confessed by the man restrained.")],
  'entries': ['elohim'],
  'lost': [between("Hebrew yesh le-el yadi, “there is power to my hand,” is Greek kai nyn ischyei hē cheir mou, “and now my hand has power”; Hebrew mi-tov ad-ra is Greek ponēra; Latin “the God of your fathers … yesterday”; King James “either good or bad.”")]},

 '31:30': {
  'received': "Granted you longed for your father’s house; but why did you steal my gods?",
  'explain': ("The real charge. My gods, elohai: Laban’s teraphim. The versions agree; the Latin granted."),
  'shared': ["You have gone because you longed for your father’s house.", "But.", "Why have you stolen my gods?"],
  'instructions': [ins(K, S, "Laban accused Jacob of stealing his gods."), ins(W, R, "“My gods” that can be stolen and sat upon: the narrator lets Laban’s word expose his religion. The God of Jacob’s father speaks in dreams; Laban’s gods are in a saddlebag.")],
  'entries': ['gods'],
  'lost': [AGREE]},

 '31:31': {
  'received': "Jacob answered that he was afraid Laban would take his daughters from him by force.",
  'explain': ("Jacob answers the first charge, not knowing the second is true. The Hebrew says I was afraid; the Greek lacks it and adds and everything I have; the Latin I departed without your knowledge because I feared."),
  'shared': ["Jacob answered Laban.", "I thought you might take your daughters from me.", "He acted from fear."],
  'instructions': [ins(K, S, "Jacob explained his flight as fear of losing his wives.")],
  'entries': ['jacob'],
  'lost': [loses("Hebrew ki yareti, “because I was afraid,” is absent from the Greek, which adds kai panta ta ema, “and everything I have.”"), between("Latin “because I feared you would take your daughters away by force” and King James “Because I was afraid” keep the fear.")]},

 '31:32': {
  'received': "Whoever has your gods shall not live; search before our kinsmen and take what is yours. Jacob did not know Rachel had stolen them.",
  'explain': ("Jacob pronounces death on the thief, who is his wife. The Hebrew puts the sentence first, then the search; the Greek puts the search first, adds he identified nothing, and calls Rachel his wife; the Latin whoever is found with your gods shall be killed."),
  'shared': ["Whoever has your gods shall not live.", "Before our kinsmen, identify what is yours with me and take it.", "Jacob did not know that Rachel had stolen them."],
  'instructions': [ins(K, S, "Jacob unknowingly condemned the thief, Rachel."), ins(W, R, "Jacob swears death on the thief, and the thief is Rachel; Rachel dies young, at Benjamin’s birth, and readers since the rabbis have wondered whether the oath found her.")],
  'entries': ['jacob'],
  'lost': [keeps("The Greek reorders: epignōthi … kai labe, “identify … and take,” first, then kai ouk epegnō par’ autō outhen, “and he identified nothing with him,” an added clause, then the death sentence, and Rhachēl hē gynē autou, “Rachel his wife.”"), between("Latin “whoever is found with your gods shall be killed … Search” and King James “let him not live: before our brethren discern” follow the Hebrew order.")]},

 '31:33': {
  'received': "Laban searched Jacob’s, Leah’s and the maids’ tents and found nothing, then entered Rachel’s.",
  'explain': ("The search, tent by tent, Rachel’s last. The Hebrew order is Jacob, Leah, the maids, Rachel; the Greek Leah, Jacob, the maids, Rachel; the Latin ends the verse with when he entered Rachel’s tent, running on."),
  'shared': ["Laban entered Jacob’s tent, Leah’s tent and the maids’ tents.", "He found nothing.", "He entered Rachel’s tent."],
  'instructions': [ins(K, S, "Laban searched the tents and came last to Rachel’s.")],
  'entries': ['jacob'],
  'lost': [between("Hebrew Ya‘aqov … Le’ah … shete ha-amahot … Rachel is Greek Leia … Iakōb … tōn dyo paidiskōn … Rhachēl, a different order, with “found nothing” said twice; Latin and King James follow the Hebrew.")]},

 '31:34': {
  'received': "Rachel had put the teraphim in the camel’s saddle and sat on them; Laban searched the tent and found nothing.",
  'explain': ("The hiding place: the camel’s kar, saddle-basket or litter. The Hebrew ends with Laban’s fruitless search; the Greek moves that clause to verse 35; the Latin she quickly hid."),
  'shared': ["Rachel had taken the teraphim and put them in the camel’s saddle.", "She sat on them.", "Laban searched the whole tent but found nothing."],
  'instructions': [ins(K, S, "Rachel hid the idols under herself."), ins(W, R, "Laban’s gods are sat upon by a woman who claims her period; the scene is comedy at the idols’ expense, and the narrator enjoys it.")],
  'entries': [],
  'lost': [between("Hebrew va-yemashesh Lavan et-kol-ha-ohel ve-lo matza, “and Laban felt through the whole tent and did not find,” stands here; the Greek carries it to 31:35; Latin and King James keep it here; Hebrew terafim is Greek eidōla.")]},

 '31:35': {
  'received': "She told her father she could not rise because the way of women was on her; he searched and found nothing.",
  'explain': ("Rachel’s excuse, a euphemism for menstruation, which would make the saddle unclean to touch. The Greek adds do not take it badly, my lord, to her father, and repeats the fruitless search here; the Latin his careful search was thwarted."),
  'shared': ["Do not be angry, my lord, that I cannot rise before you.", "The way of women is upon me.", "He searched but did not find the teraphim."],
  'instructions': [ins(K, S, "Rachel’s excuse kept Laban from the idols."), ins(W, R, "Rachel outwits her father as Jacob outwitted his; Laban’s daughter has learned the family trade, and the gods that cannot save themselves are saved by a lie.")],
  'entries': [],
  'lost': [between("Greek mē bareōs phere, kyrie, “do not take it badly, lord,” expands Hebrew al-yichar be-ene adoni, “let it not burn in my lord’s eyes”; the Greek repeats the search clause from 31:34 here; Latin “his careful search was thwarted”; King James “he searched, but found not the images.”")]},

 '31:36': {
  'received': "Jacob grew angry and demanded what sin of his justified the hot pursuit.",
  'explain': ("Vindicated by the empty search, Jacob attacks. The Greek runs the question into verse 37. The versions agree."),
  'shared': ["Jacob was angry and disputed with Laban.", "What is my offence? What is my sin?", "That you have hotly pursued me."],
  'instructions': [ins(K, S, "Jacob turned on Laban in anger."), ins(W, R, "Jacob’s indignation is honest and misplaced at once; the gods were stolen, by his wife, and his innocence is only ignorance.")],
  'entries': ['jacob'],
  'lost': [AGREE]},

 '31:37': {
  'received': "You have searched all my goods; what of yours have you found? Set it before our kin to judge between us.",
  'explain': ("A challenge to arbitration before witnesses. The versions agree."),
  'shared': ["You have searched all my belongings.", "What have you found of your household goods?", "Set it here before my kinsmen and yours, and let them judge between us."],
  'instructions': [ins(K, S, "Jacob demanded arbitration before the kinsmen.")],
  'entries': ['jacob'],
  'lost': [AGREE]},

 '31:38': {
  'received': "Twenty years I was with you; your ewes and goats did not miscarry, and I ate none of your rams.",
  'explain': ("The shepherd’s defence: no losses, no theft. The Latin makes it a question, was this why. The versions agree."),
  'shared': ["These twenty years I have been with you.", "Your ewes and goats have not miscarried.", "I have not eaten the rams of your flock."],
  'instructions': [ins(K, S, "Jacob recounted twenty years of faithful shepherding.")],
  'entries': ['jacob'],
  'lost': [between("Latin “Was this why I was with you twenty years? Your sheep and goats were not barren” varies; Hebrew, Greek and King James state the years and “not miscarried.”")]},

 '31:39': {
  'received': "I brought you no animal torn by beasts but bore the loss; you demanded of me what was stolen by day or night.",
  'explain': ("Jacob made good losses a shepherd could lawfully report, Exodus 22:13. The Hebrew says you demanded it of my hand; the Greek lacks that clause and says I made restitution for what was stolen by day or night; the Latin whatever was lost by theft you demanded."),
  'shared': ["I did not bring you animals torn by wild beasts.", "I bore the loss myself.", "What was stolen by day or night was required of me."],
  'instructions': [ins(K, S, "Jacob absorbed losses beyond a shepherd’s duty."), ins(W, R, "Jacob paid for what the wolves took; the narrator, who knows about the rods, lets this stand too. Men are more than one thing.")],
  'entries': ['jacob'],
  'lost': [loses("Hebrew mi-yadi tevaqshennah, “from my hand you required it,” is absent from the Greek, which has egō apetinnyon par’ emautou klemmata hēmeras kai klemmata nyktos, “I paid from myself for thefts of day and thefts of night.”"), between("Latin “Whatever was lost by theft you demanded from me” and King James “of my hand didst thou require it” keep the demand.")]},

 '31:40': {
  'received': "Heat consumed me by day and frost by night, and sleep fled my eyes.",
  'explain': ("The shepherd’s hardship in one line. The versions agree."),
  'shared': ["By day the heat consumed me.", "By night the frost.", "Sleep fled from my eyes."],
  'instructions': [ins(K, S, "Jacob described the hardship of his service.")],
  'entries': [],
  'lost': [AGREE]},

 '31:41': {
  'received': "Twenty years in your house: fourteen for your daughters, six for your flock, and you changed my wages ten times.",
  'explain': ("The reckoning. The Greek again has ten ewe lambs for ten times. The fourteen and six agree in all."),
  'shared': ["I have been twenty years in your house.", "Fourteen years for your two daughters and six for your flock.", "You changed my wages ten times."],
  'instructions': [ins(K, S, "Jacob summed up twenty years of service and fraud."), ins(W, R, "Twenty years are totted up in a sentence; the “few days” of 27:44 became a working life, and Jacob can account for every one.")],
  'entries': ['jacob'],
  'lost': [loses("Hebrew aseret monim, “ten times,” again becomes Greek deka amnadōn, “ten ewe lambs,” as at 31:7."), between("Latin and King James “changed my wages ten times.”")]},

 '31:42': {
  'received': "Had the God of my father, the God of Abraham and the Fear of Isaac, not been with me, you would have sent me away empty; God saw my affliction and gave judgment last night.",
  'explain': ("The Fear of Isaac, pachad Yitzchaq, a divine title found only here and in verse 53. The Hebrew says the God of my father, the God of Abraham; the Greek the God of my father Abraham; the Hebrew God gave judgment; the Greek and Latin rebuked you."),
  'shared': ["If the God of my father, the God of Abraham and the Fear of Isaac, had not been with me.", "You would have sent me away empty.", "God saw my affliction and the labour of my hands, and judged last night."],
  'instructions': [ins(K, S, "Jacob credited God’s intervention for his wealth and safety."), ins(W, R, "“The Fear of Isaac”: Jacob names God by what his father felt before Him. The dread on Moriah is a name of God for the next generation.")],
  'entries': ['abraham', 'isaac', 'elohim'],
  'lost': [between("Hebrew Elohe avi Elohe Avraham, “the God of my father, the God of Abraham,” is Greek ho theos tou patros mou Abraam, “the God of my father Abraham”; Hebrew va-yokhach amesh, “and he gave judgment last night,” is Greek kai ēlenxen se echthes, “and rebuked you yesterday”; Latin “rebuked you yesterday,” King James “rebuked thee yesternight.”")]},

 '31:43': {
  'received': "Laban said the daughters, children and flocks were all his; what could he do against his own daughters and their children?",
  'explain': ("Laban’s last claim and his surrender in one breath. The Greek adds and my daughters’; the Latin my children and grandchildren."),
  'shared': ["The daughters are my daughters, the children my children, the flock my flock.", "All you see is mine.", "What can I do today to these daughters of mine or their children?"],
  'instructions': [ins(K, S, "Laban yielded, unable to act against his own kin."), ins(W, R, "Laban claims everything and can take nothing; his ownership is a speech, and the covenant he proposes is the price of his pride.")],
  'entries': [],
  'lost': [keeps("An added kai tōn thygaterōn mou, “and my daughters’,” after mine in the Greek."), between("Latin “my children and grandchildren” compresses; King James follows the Hebrew.")]},

 '31:44': {
  'received': "Come, let us make a covenant, you and I, and let it be a witness between us.",
  'explain': ("Laban proposes a treaty. The Greek adds a sentence, Look, no one is with us; see, God is witness between you and me, which in the Hebrew stands at verse 50; the Latin a testimony."),
  'shared': ["Come now, let us make a covenant.", "You and I.", "Let it be a witness between us."],
  'instructions': [ins(K, S, "Laban proposed a covenant with Jacob.")],
  'entries': ['term-covenant'],
  'lost': [keeps("An added idou outheis meth’ hēmōn estin, ide ho theos martys ana meson emou kai sou, “look, no one is with us; see, God is witness between me and you,” in the Greek here, the Hebrew’s clause from 31:50."), between("Latin and King James end with the witness between them.")]},

 '31:45': {
  'received': "Jacob took a stone and set it up as a pillar.",
  'explain': ("Jacob’s second matzevah, after Bethel. The versions agree."),
  'shared': ["Jacob took a stone.", "He set it up.", "It was a pillar."],
  'instructions': [ins(K, S, "Jacob raised a pillar for the covenant.")],
  'entries': ['jacob'],
  'lost': [AGREE]},

 '31:46': {
  'received': "Jacob had his kin gather stones into a heap, and they ate there by the heap.",
  'explain': ("A pillar and a heap, and a meal. The Greek adds and drank and Laban’s words this heap is a witness between you and me today, which the Hebrew gives at verse 48."),
  'shared': ["Jacob said to his kinsmen, Gather stones.", "They made a heap.", "They ate there by the heap."],
  'instructions': [ins(K, S, "A heap of stones was raised and a meal eaten."), ins(W, R, "Stone and meal: the covenant is marked in the oldest way, by what will last and what is shared.")],
  'entries': ['jacob'],
  'lost': [keeps("An added kai epion, “and drank,” and eipen de autō Laban, ho bounos houtos martyrei ana meson emou kai sou sēmeron, “and Laban said to him, this heap witnesses between me and you today,” in the Greek, the Hebrew’s words from 31:48."), between("Latin “made a mound, and ate upon it” and King James “did eat there upon the heap” follow the Hebrew.")]},

 '31:47': {
  'received': "Laban called it Jegar-sahadutha and Jacob called it Galeed.",
  'explain': ("Two names for heap of witness, Laban’s Aramaic and Jacob’s Hebrew; the first Aramaic in the Bible. The Hebrew keeps both names; the Greek translates both, Witness Heap and The Heap Bears Witness; the Latin translates and adds each according to his own language."),
  'shared': ["Laban named the heap.", "Jacob named the heap.", "Both names mean heap of witness."],
  'instructions': [ins(K, S, "The heap was named in Aramaic and Hebrew."), ins(W, R, "Uncle and nephew name one heap in two tongues; the family is already two peoples, and the border runs through the language.")],
  'entries': ['jacob'],
  'lost': [loses("Hebrew Yegar Sahaduta, Aramaic, and Gal‘ed, Hebrew, both names, become Greek Bounos tēs martyrias, “Heap of Witness,” and Bounos martys, “Heap Witness,” translations; the two languages are lost."), between("Latin Tumulum testis … Acervum testimonii and adds “each according to his own language”; King James “Jegarsahadutha … Galeed.”")]},

 '31:48': {
  'received': "Laban said, This heap is a witness between you and me today; therefore it was named Galeed,",
  'explain': ("The naming explained. The Greek here gives the fuller heap-and-pillar speech of the Hebrew’s verses 51–52: behold this heap and the pillar I have set between me and you; the Latin Gilead, Mound of Witness."),
  'shared': ["Laban said.", "This heap is a witness between you and me today.", "Therefore it was named Galeed."],
  'instructions': [ins(K, S, "The heap was named Galeed as a witness.")],
  'entries': [],
  'lost': [keeps("The Greek here reads idou ho bounos houtos kai hē stēlē autē, hēn estēsa ana meson emou kai sou, martyrei ho bounos houtos kai martyrei hē stēlē autē, “behold this heap and this pillar which I set between me and you; this heap witnesses and this pillar witnesses,” the Hebrew’s material from 31:51–52."), between("Latin “This mound shall be a witness … Gilead, that is, Mound of Witness” and King James “This heap is a witness … Galeed” follow the Hebrew.")]},

 '31:49': {
  'received': "and Mizpah, because he said, May the Lord watch between you and me when we are out of sight of one another.",
  'explain': ("Mizpah, watchtower, a second name. The Hebrew says YHWH; the Greek God, and translates the name The Watch; the Latin omits the name and says watch and judge."),
  'shared': ["It was also called Mizpah.", "May the Lord watch between you and me.", "When we are absent from one another."],
  'instructions': [ins(K, S, "The place was named Mizpah for God’s watching."), ins(W, R, "“The Lord watch between me and thee” is spoken by a man who divines and keeps idols; the words outlive their speaker and become a blessing in other mouths.")],
  'entries': ['yhwh-yahweh'],
  'lost': [loses("Hebrew ha-Mitzpah, a name, becomes Greek hē Horasis, “the Watch,” and Hebrew YHWH becomes ho theos."), between("Latin “May the Lord watch and judge between us” drops the name; King James “Mizpah … The LORD watch.”")]},

 '31:50': {
  'received': "If you mistreat my daughters or take other wives, though no one is with us, God is witness between you and me.",
  'explain': ("Laban’s terms for his daughters. The Hebrew ends with God is witness; the Greek, having placed that at verse 44, ends see, there is no one with us; the Latin no one witnesses our words except God."),
  'shared': ["If you mistreat my daughters or take other wives beside them.", "No one is with us.", "God is witness between you and me."],
  'instructions': [ins(K, S, "Laban bound Jacob to treat his daughters well."), ins(W, R, "Laban, who sold his daughters, now protects them by oath; the father’s late care is sincere and the narrator does not mock it.")],
  'entries': ['elohim'],
  'lost': [loses("Hebrew re’eh Elohim ed beni u-venekha, “see, God is witness between me and you,” is absent here in the Greek, which placed it at 31:44 and ends hora, outheis meth’ hēmōn estin, “see, no one is with us.”"), between("Latin “No one witnesses our words except God, who is present and sees” and King James “see, God is witness betwixt me and thee” keep it here.")]},

 '31:51': {
  'received': "Laban said to Jacob, See this heap and this pillar I have set between you and me.",
  'explain': ("The Hebrew, Latin and King James have Laban point to heap and pillar here; the Greek has no separate text at this verse, its equivalent standing at verse 48. An empty slot, not a loss."),
  'shared': ["Laban said to Jacob.", "See this heap and this pillar.", "I have set them between you and me."],
  'instructions': [ins(K, S, "Laban pointed to the heap and pillar as boundary.")],
  'entries': ['jacob'],
  'lost': [loses("No Greek text stands at 31:51; the Hebrew hinneh ha-gal ha-zeh ve-hinneh ha-matzevah asher yariti beni u-venekha, “behold this heap and this pillar which I have cast between me and you,” was rendered in the Greek at 31:48."), between("Latin and King James have the verse in place.")]},

 '31:52': {
  'received': "This heap and pillar are witness that I will not pass them to harm you, nor you to harm me.",
  'explain': ("A non-aggression boundary. The Hebrew says this heap is witness, this pillar is witness; the Greek, having said so at verse 48, gives only the conditional, if I do not cross to you, neither shall you cross to me; the Latin they shall be a witness."),
  'shared': ["This heap and this pillar are witness.", "I will not pass this heap to harm you.", "You will not pass this heap and pillar to harm me."],
  'instructions': [ins(K, S, "The heap marked a mutual boundary."), ins(W, R, "The border between Jacob and Laban is the border between Israel and Aram; the family quarrel is settled by a line of stones that nations will later fight over.")],
  'entries': [],
  'lost': [loses("Hebrew ed ha-gal ha-zeh ve-edah ha-matzevah, “this heap is witness and this pillar is witness,” is absent here in the Greek, which has ean te gar egō mē diabō pros se mēde sy diabēs pros me, “for if I do not cross to you, neither shall you cross to me.”"), between("Latin “they shall be a witness. This mound and stone … shall be testimony” and King James “This heap be witness, and this pillar be witness” keep the clause.")]},

 '31:53': {
  'received': "May the God of Abraham and the God of Nahor, the God of their father, judge between us. Jacob swore by the Fear of his father Isaac.",
  'explain': ("Laban invokes two gods, or one God under two names, and the God of their father Terah; Jacob swears by one, the Fear of Isaac. The Greek lacks the God of their father; the Hebrew verb judge is plural."),
  'shared': ["May the God of Abraham and the God of Nahor judge between us.", "Laban spoke.", "Jacob swore by the Fear of his father Isaac."],
  'instructions': [ins(K, S, "The covenant was sworn by each man’s ancestral God."), ins(W, R, "Laban swears by the gods of Abraham and Nahor together; Jacob swears by the Fear of Isaac alone. One oath is a hedge and the other a confession.")],
  'entries': ['abraham', 'isaac'],
  'lost': [loses("Hebrew Elohe avihem, “the God of their father,” is absent from the Greek; the Hebrew yishpetu, “may they judge,” is plural, the Greek krinai singular."), between("Latin and King James “the God of their father” keep the clause.")]},

 '31:54': {
  'received': "Jacob offered a sacrifice on the mountain and called his kin to eat bread, and they spent the night there.",
  'explain': ("Jacob’s first sacrifice, zevach, and the covenant meal. The Hebrew says eat bread, ate bread; the Greek ate and drank, without bread; the Latin ate and stayed."),
  'shared': ["Jacob offered a sacrifice on the mountain.", "He called his kinsmen to eat bread.", "They ate and spent the night on the mountain."],
  'instructions': [ins(K, S, "Jacob sealed the covenant with sacrifice and a meal.")],
  'entries': ['jacob'],
  'lost': [between("Hebrew le’ekhol-lachem va-yokhlu lechem, “to eat bread, and they ate bread,” is Greek kai ephagon kai epion, “and they ate and drank,” without bread; Latin “to eat bread. They ate and stayed”; King James “to eat bread: and they did eat bread.”")]},

 '31:55': {
  'received': "In the morning Laban kissed and blessed his children and went home.",
  'explain': ("Laban’s exit from the story, with a kiss and a blessing. The Hebrew and Greek number this 32:1, so the reader’s chapter 32 runs one verse behind both. The Latin says rose in the night."),
  'shared': ["Laban rose early in the morning.", "He kissed his sons and daughters and blessed them.", "He departed and returned to his place."],
  'instructions': [ins(K, S, "Laban blessed his family and departed."), ins(W, R, "Laban leaves blessing the children he could not keep; the grasping uncle ends as a grandfather, and the narrator gives him that.")],
  'entries': [],
  'lost': [between("Hebrew and Greek number this verse 32:1; Latin “rose in the night” for Hebrew ba-boqer, “in the morning”; Greek and King James “early in the morning.”")]},
 }
}
