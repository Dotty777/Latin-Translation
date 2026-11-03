# Study prose for Genesis 24 — Saints Parallel Reader Study Workspace. Draft for review.
K, W, C = 'Knowledge', 'Wisdom', 'Command'
S, R = 'stated', 'reflection'
def ins(t, b, text): return {'type': t, 'basis': b, 'text': text}
def keeps(t): return {'dir': 'keeps', 'text': t}
def loses(t): return {'dir': 'loses', 'text': t}
def between(t): return {'dir': 'between', 'text': t}
AGREE = between("Hebrew, Greek, Latin and King James agree in substance; only the rendering of the divine name and small turns of phrase differ.")

CHAPTER = {
 'slug': 'genesis', 'chapter': 24,
 'chapterNote': (
  "The longest chapter of Genesis tells one errand twice, once as it happens and once as the servant retells it in Laban’s house, so the reader can "
  "watch a faithful report shade and compress what it reports. The columns agree on the whole: the oath, the camels, the well, the sign, Rebekah, "
  "Laban, the gifts, the blessing, the veil. The Hebrew keeps a gold nose-ring weighing a beka, the servant bowing before he worships, “blessed of "
  "YHWH” as Laban’s greeting, Abraham who “walked before” God, the family who “cannot speak bad or good,” Rebekah’s nurse, the gate of those who "
  "hate them, and Beer-lahai-roi. The Greek keeps earrings of a drachma, a servant who “was pleased” before worshipping, “blessed be the Lord,” "
  "Abraham who “pleased” God, the family who cannot “set evil against good,” Rebekah’s belongings, the cities of their adversaries, the Well of the "
  "Vision, and Isaac named in Abraham’s charge where the Hebrew says only “my son.” The Latin and King James follow the Hebrew; the Latin says "
  "“blessed of the Lord,” “brothers,” and expands the final verse into grief relieved by love. Three Hebrew-column renderings in this chapter were "
  "corrected today to the Masoretic wording where they had repeated the Greek."),
 'verses': {

 '24:1': {
  'received': "Abraham was old, and the Lord had blessed him in everything.",
  'explain': ("The chapter opens on an old man blessed in all things and with one thing unsettled: a wife for the heir. The Hebrew says advanced in days; "
   "the Greek and Latin in years; all say the Lord had blessed him in all. The blessing of 12:2 is pronounced fulfilled before the last provision for it is made."),
  'shared': ["Abraham was old and advanced in years.", "The Lord had blessed Abraham.", "The blessing was in all things."],
  'instructions': [ins(K, S, "Abraham was old and fully blessed."), ins(W, R, "“Blessed in all things” is said before Isaac has a wife; the blessing is counted complete while its next step is still a journey away.")],
  'entries': ['abraham', 'yhwh-yahweh'],
  'lost': [AGREE]},

 '24:2': {
  'received': "Abraham told the senior servant who managed his household to put his hand under his thigh.",
  'explain': ("The servant is unnamed, the elder of the house who ruled all Abraham had; tradition guesses Eliezer of 15:2. The gesture is an oath by "
   "the organ of generation, fitting for an oath about offspring. The Hebrew says please put; the Greek drops the courtesy; the Latin he said without naming Abraham."),
  'shared': ["Abraham spoke to his senior servant.", "The servant managed all that Abraham had.", "He was told to put his hand under Abraham’s thigh."],
  'instructions': [ins(K, S, "Abraham prepared to bind his steward by oath."), ins(W, R, "Abraham does not go himself; the promise is entrusted to a servant, and the servant will prove faithful.")],
  'entries': ['abraham'],
  'lost': [between("Hebrew sim-na, “please put,” is Greek thes, “put,” without the particle; Latin “the senior servant” drops Abraham’s name; King James “put, I pray thee.”")]},

 '24:3': {
  'received': "He made him swear by the Lord, God of heaven and earth, not to take a wife for his son from the Canaanites.",
  'explain': ("The oath is by the God of heaven and the God of the earth, the fullest title Abraham uses. The prohibition is negative first: not from the "
   "daughters of the Canaanites among whom I live. The Greek names Isaac here, where the Hebrew says my son; the Latin names him in the next verse; the Greek title has God of earth."),
  'shared': ["The oath is by the Lord, God of heaven and earth.", "The servant must not take a wife for Abraham’s son from the Canaanites.", "Abraham lives among them."],
  'instructions': [ins(K, S, "Abraham forbade a Canaanite wife for Isaac."), ins(C, S, "Do not take a wife for my son from the daughters of the Canaanites."), ins(W, R, "The heir of Canaan may not marry into Canaan; the line is kept distinct from the land it will one day hold.")],
  'entries': ['abraham', 'isaac', 'canaan', 'yhwh-yahweh'],
  'lost': [keeps("An added Isaak, “Isaac,” in the Greek names the son where Hebrew li-vni, “for my son,” leaves him unnamed."), between("Latin “God of heaven and earth” compresses the double title; King James “God of heaven, and the God of the earth” keeps it.")]},

 '24:4': {
  'received': "He must go to Abraham’s own land and kindred to take a wife for Isaac.",
  'explain': ("The positive command: go to my land and my kindred. Abraham’s people are in Haran, in Aram-naharaim, since Terah settled there. The "
   "Greek adds where I was born and from there, and says tribe for kindred; the Latin from there. All name Isaac here."),
  'shared': ["The servant must go to Abraham’s land.", "He must go to Abraham’s kindred.", "He must take a wife for Isaac from there."],
  'instructions': [ins(C, S, "Go to my land and my kindred and take a wife for my son Isaac."), ins(W, R, "Abraham left his kindred at God’s call and now sends back to them for a wife; separation from the land was never separation from the family.")],
  'entries': ['abraham', 'isaac', 'haran'],
  'lost': [keeps("An added hou egennēthēn, “where I was born,” and ekeithen, “from there,” fill out the Greek; Hebrew moladti, “my kindred,” becomes phylēn mou, “my tribe.”"), between("Latin “my land and my kindred … from there” and King James “my country, and to my kindred” follow the Hebrew.")]},

 '24:5': {
  'received': "The servant asked whether, if the woman would not follow him, he must take Isaac back to Abraham’s old land.",
  'explain': ("A reasonable objection, put as a question. The servant foresees the woman’s refusal and asks whether the son must then go to her. The "
   "versions agree; the Latin says the place from which you came."),
  'shared': ["The servant speaks.", "Perhaps the woman will not follow him to this land.", "Must he take the son back to Abraham’s land of origin?"],
  'instructions': [ins(K, S, "The servant asked what to do if the woman refused."), ins(W, R, "A good servant names the failure case before he swears; the oath he takes will be one he can keep.")],
  'entries': [],
  'lost': [AGREE]},

 '24:6': {
  'received': "Abraham warned him never to take his son back there.",
  'explain': ("The answer is firm: beware. Isaac must stay in the land of promise even if the errand fails. The versions agree; the Latin take care never."),
  'shared': ["Abraham answers the servant.", "He warns him to be careful.", "The son must not be taken back there."],
  'instructions': [ins(C, S, "Do not take my son back there."), ins(W, R, "The land is not negotiable; Abraham would rather his son stay unmarried in Canaan than married in Haran.")],
  'entries': ['abraham'],
  'lost': [AGREE]},

 '24:7': {
  'received': "The Lord who took Abraham from his father’s house and swore the land to his seed will send His angel before the servant to find the wife.",
  'explain': ("Abraham grounds his confidence in his own call and the oath of the land. The God who brought him out will send His angel ahead. The Hebrew "
   "says God of heaven, to your seed, my son; the Greek adds God of earth, to you and your seed, and names Isaac; the Latin and King James follow the Hebrew."),
  'shared': ["The Lord took Abraham from his father’s house and the land of his birth.", "He swore to give this land to Abraham’s seed.", "He will send His angel before the servant to take a wife for the son."],
  'instructions': [ins(K, S, "Abraham trusted God’s angel to go before the servant."), ins(W, R, "Abraham reasons from what God has done to what God will do; the past call is the warrant for the present errand.")],
  'entries': ['abraham', 'isaac', 'angel-of-the-lord', 'angels', 'yhwh-yahweh'],
  'lost': [keeps("An added kai ho theos tēs gēs, “and the God of the earth,” soi kai, “to you and,” and Isaak, “Isaac,” fill out the Greek title, promise and reference where the Hebrew has “God of heaven … to your seed … my son.”"), between("Latin and King James follow the Hebrew; King James “the land of my kindred” for “the land of my birth.”")]},

 '24:8': {
  'received': "If the woman is unwilling, the servant is free of the oath, but must not take the son back.",
  'explain': ("The release clause. A refusal frees the servant; it does not free him to take Isaac abroad. The Greek says come with you to this land, "
   "spelling out the journey; the Hebrew follow you; the Latin you will not be bound."),
  'shared': ["If the woman is unwilling to follow, the servant is free of the oath.", "Only he must not take the son back there.", "The release is conditional."],
  'instructions': [ins(K, S, "Refusal would release the servant but not permit taking Isaac abroad."), ins(W, R, "The oath has an exit for the servant and none for Isaac; faith provides for failure without surrendering the point.")],
  'entries': [],
  'lost': [keeps("An added eis tēn gēn tautēn, “to this land,” in the Greek spells out the destination the Hebrew lalekhet acharekha, “to follow you,” leaves implicit."), between("Latin “you will not be bound by the oath” and King James “clear from this my oath” follow the Hebrew.")]},

 '24:9': {
  'received': "The servant put his hand under Abraham’s thigh and swore.",
  'explain': ("The oath is taken as asked, concerning this matter. The versions agree."),
  'shared': ["The servant put his hand under Abraham’s thigh.", "Abraham was his master.", "He swore concerning this matter."],
  'instructions': [ins(K, S, "The servant swore the oath.")],
  'entries': ['abraham'],
  'lost': [AGREE]},

 '24:10': {
  'received': "He took ten camels and his master’s goods and went to Aram-naharaim, the city of Nahor.",
  'explain': ("Ten camels with gifts, bound for Nahor’s city, Haran. The Hebrew says Aram-naharaim, Aram of the two rivers; the Greek and Latin Mesopotamia, "
   "the Greek name for the same region. The Hebrew says all his master’s good things in his hand, meaning in his charge; the Greek some of all."),
  'shared': ["The servant took ten of his master’s camels.", "He carried his master’s good things.", "He went to the city of Nahor in Aram-naharaim."],
  'instructions': [ins(K, S, "The servant travelled to Nahor’s city with ten camels."), ins(W, R, "The errand is furnished royally; a bride is to be won for the heir of all things.")],
  'entries': ['haran'],
  'lost': [between("Hebrew Aram Naharayim, “Aram of the two rivers,” is Greek Mesopotamia and Latin Mesopotamia, King James “Mesopotamia”; Hebrew ve-khol-tuv adonav be-yado, “all the good of his master in his hand,” is Greek apo pantōn tōn agathōn, “some of all the good things.”")]},

 '24:11': {
  'received': "He made the camels kneel outside the city by a well at evening, when women come to draw water.",
  'explain': ("He waits at the well at the hour the women come, the place where strangers meet townsfolk. The Hebrew says made them kneel; the Greek lie "
   "down; the Latin adds and said, carrying into the prayer."),
  'shared': ["He made the camels kneel outside the city.", "It was by a well of water at evening.", "That is when women go out to draw water."],
  'instructions': [ins(K, S, "The servant waited at the well at evening."), ins(W, R, "He positions himself where providence can meet him; faith chooses the right well at the right hour, and then prays.")],
  'entries': [],
  'lost': [between("Hebrew va-yavrekh, “he made kneel,” is Greek ekoimisen, “he made lie down”; Latin and King James “kneel.” Latin adds “and said” before the prayer.")]},

 '24:12': {
  'received': "He prayed to the Lord, God of his master Abraham, for success that day and kindness to Abraham.",
  'explain': ("The servant prays in Abraham’s God’s name, not his own: God of my master Abraham. He asks for success today and kindness, chesed, to his master. "
   "The Hebrew says kindness; the Greek mercy; the Latin come to my aid."),
  'shared': ["He prayed to the Lord, God of his master Abraham.", "He asked for success that day.", "He asked for kindness to his master."],
  'instructions': [ins(K, S, "The servant prayed for guidance in Abraham’s God’s name."), ins(W, R, "The first recorded prayer for guidance in Scripture is a servant’s on another man’s behalf; he claims nothing but his master’s God.")],
  'entries': ['abraham', 'yhwh-yahweh'],
  'lost': [between("Hebrew chesed, “kindness,” is Greek eleos, “mercy,” here and through the chapter; Hebrew haqreh-na lefanai, “cause to happen before me,” is Greek euodōson, “grant success,” Latin occurre, “come to my aid.”")]},

 '24:13': {
  'received': "He stands by the spring as the daughters of the city come out to draw.",
  'explain': ("The scene set in prayer: here I stand, the women are coming. The Hebrew says the daughters of the men of the city; the Greek of those who "
   "live in the city. The Hebrew-column rendering was corrected today to the Masoretic wording where it had repeated the Greek."),
  'shared': ["The servant stands by the spring of water.", "The daughters of the city are coming out.", "They come to draw water."],
  'instructions': [ins(K, S, "The servant described his position to God in prayer.")],
  'entries': [],
  'lost': [between("Hebrew benot anshe ha-ir, “the daughters of the men of the city,” is Greek thygateres tōn oikountōn tēn polin, “daughters of those who live in the city”; Latin “this city’s inhabitants” follows the Greek, King James “the men of the city” the Hebrew.")]},

 '24:14': {
  'received': "He asked that the girl who offers him a drink and waters his camels be the one appointed for Isaac, as the sign of kindness to his master.",
  'explain': ("The sign is a test of generosity: a girl who, asked for a drink, offers to water ten camels. The Hebrew says young woman, appointed, my master; "
   "the Greek virgin, prepared, until they stop drinking, and names Abraham; the Latin young woman, prepared. Both call Rebekah a virgin in verse 16."),
  'shared': ["The servant will ask a girl to lower her jar so he may drink.", "If she says drink and offers to water the camels, she is the one appointed for Isaac.", "By this he will know God has shown kindness to his master."],
  'instructions': [ins(K, S, "The servant asked for a sign of generosity to identify the bride."), ins(W, R, "The test is not beauty or birth but kindness beyond what is asked; the bride for the heir of blessing must herself be a blesser.")],
  'entries': ['isaac', 'abraham'],
  'lost': [keeps("An added heōs an pausōntai pinousai, “until they stop drinking,” and Abraam in the Greek extend the sign and name the master; Hebrew na‘arah, “young woman,” is Greek parthenos, “virgin,” and hokhachta, “appointed,” is hētoimasas, “prepared.”"), between("Latin “young woman … prepared … my master” and King James “damsel … appointed … my master” follow the Hebrew.")]},

 '24:15': {
  'received': "Before he finished, Rebekah, granddaughter of Nahor, came out with her jar on her shoulder.",
  'explain': ("The answer outruns the prayer. Rebekah is introduced with full pedigree: daughter of Bethuel, son of Milcah and Nahor, Abraham’s brother; "
   "she is Isaac’s second cousin. The Greek and Latin say speaking in his mind, within himself, which the Hebrew makes explicit only in the retelling at 24:45."),
  'shared': ["Before he finished speaking, Rebekah came out.", "She was daughter of Bethuel, son of Milcah and Nahor, Abraham’s brother.", "Her water-jar was on her shoulder."],
  'instructions': [ins(K, S, "Rebekah appeared before the prayer was finished."), ins(W, R, "God answers before the asking ends; the bride was already on her way to the well while the servant was still choosing his words.")],
  'entries': ['rebekah', 'abraham'],
  'lost': [keeps("An added en tē dianoia, “in his mind,” in the Greek makes the prayer inward here; the Hebrew says so only at 24:45."), between("Latin “within himself” follows the Greek; King James “before he had done speaking” the Hebrew.")]},

 '24:16': {
  'received': "She was very beautiful, a virgin, and she went down to the spring, filled her jar and came up.",
  'explain': ("The narrator vouches for her: beautiful, a virgin whom no man had known. The Hebrew says beautiful in appearance; the Greek of face; the "
   "Latin very graceful, a most beautiful virgin. The Hebrew-column rendering was corrected today to the Masoretic wording."),
  'shared': ["The young woman was exceedingly beautiful.", "She was a virgin whom no man had known.", "She went down to the spring, filled her jar and came up."],
  'instructions': [ins(K, S, "Rebekah was beautiful and a virgin.")],
  'entries': ['rebekah'],
  'lost': [between("Hebrew tovat mar’eh, “good of appearance,” is Greek kalē tē opsei, “beautiful of face”; Latin “very graceful, a most beautiful virgin” expands; King James “very fair to look upon.”")]},

 '24:17': {
  'received': "The servant ran to her and asked for a little water from her jar.",
  'explain': ("He runs; the test begins at once, with the smallest request. The versions agree."),
  'shared': ["The servant ran to meet her.", "He asked to drink.", "He wanted a little water from her jar."],
  'instructions': [ins(K, S, "The servant asked Rebekah for a drink.")],
  'entries': [],
  'lost': [AGREE]},

 '24:18': {
  'received': "She said, Drink, my lord, and quickly gave him water.",
  'explain': ("Courteous and quick: my lord, and the jar lowered onto her arm. The versions agree; the Latin says she answered."),
  'shared': ["She said, Drink, my lord.", "She quickly lowered her jar onto her arm.", "She gave him a drink."],
  'instructions': [ins(K, S, "Rebekah gave the servant water at once."), ins(W, R, "Haste in kindness is the first thing noted of Rebekah; every verb of hers in this scene is quick.")],
  'entries': ['rebekah'],
  'lost': [AGREE]},

 '24:19': {
  'received': "When he had drunk, she offered to draw for his camels until they finished.",
  'explain': ("The sign is given unasked, in the very words the servant had prayed. The Hebrew says when she had finished giving him drink; the Greek when he "
   "had stopped drinking; the Latin she added."),
  'shared': ["She finished giving him a drink.", "She offered to draw water for his camels too.", "She would draw until they had all finished."],
  'instructions': [ins(K, S, "Rebekah offered to water all the camels unasked."), ins(W, R, "Ten camels after a journey drink a great deal; her offer is hours of labour for a stranger, and she makes it before he can ask.")],
  'entries': ['rebekah'],
  'lost': [between("Hebrew va-tekhal le-hashqoto, “she finished giving him drink,” is Greek heōs epausato pinōn, “until he stopped drinking”; Latin and King James follow the Hebrew.")]},

 '24:20': {
  'received': "She emptied her jar into the trough and ran back to draw for all the camels.",
  'explain': ("She does it: quickly, running, for all his camels. The versions agree; the Latin says troughs."),
  'shared': ["She quickly emptied her jar into the trough.", "She ran again to the well to draw.", "She drew for all his camels."],
  'instructions': [ins(K, S, "Rebekah watered all ten camels."), ins(W, R, "The sign asked for words; she gives deeds, and the deeds exceed the sign.")],
  'entries': ['rebekah'],
  'lost': [AGREE]},

 '24:21': {
  'received': "The man watched her in silence to learn whether the Lord had prospered his journey.",
  'explain': ("He does not interrupt; he watches. The Hebrew verb can mean gazed or wondered. The versions agree."),
  'shared': ["The man gazed at her in silence.", "He watched to know.", "Had the Lord made his journey successful or not?"],
  'instructions': [ins(K, S, "The servant watched silently for God’s answer."), ins(W, R, "Silence is part of the discernment; he lets the sign complete itself before he speaks.")],
  'entries': ['yhwh-yahweh'],
  'lost': [AGREE]},

 '24:22': {
  'received': "When the camels had drunk, the man took out a gold ring and two gold bracelets for her.",
  'explain': ("The gifts: a gold ring, nezem, which 24:47 puts on her nose, weighing a beka, half a shekel, and two bracelets of ten shekels. The Greek "
   "says earrings each a drachma and bracelets of ten gold pieces; the Latin earrings of two shekels; the King James a golden earring of half a shekel."),
  'shared': ["The camels finished drinking.", "The man took out gold jewellery.", "There was a ring and two bracelets for her hands of ten weight in gold."],
  'instructions': [ins(K, S, "The servant gave Rebekah gold jewellery at the well."), ins(W, R, "The gifts come before the question of who she is; the servant rewards kindness before he confirms kinship.")],
  'entries': ['rebekah'],
  'lost': [
   loses("Hebrew nezem zahav beqa mishqalo, “a gold ring, a beka its weight,” a nose-ring of half a shekel, becomes Greek enōtia chrysa ana drachmēn holkēs, “gold earrings, a drachma each in weight”; Hebrew asarah zahav, “ten of gold,” shekels understood, becomes deka chrysōn, “ten golds.”"),
   between("Latin “earrings weighing two shekels” differs from both; King James “a golden earring of half a shekel weight” keeps the Hebrew weight with the Greek’s earring."),
  ]},

 '24:23': {
  'received': "He asked whose daughter she was and whether her father’s house had room to lodge.",
  'explain': ("Only now the question. He asks for her family and for lodging, two requests in one breath. The versions agree."),
  'shared': ["He asked whose daughter she was.", "He asked her to tell him.", "Was there room in her father’s house to lodge?"],
  'instructions': [ins(K, S, "The servant asked Rebekah’s family and for lodging.")],
  'entries': [],
  'lost': [AGREE]},

 '24:24': {
  'received': "She said she was the daughter of Bethuel, son of Milcah and Nahor.",
  'explain': ("The answer the servant could have hoped for: Nahor is Abraham’s brother. The versions agree."),
  'shared': ["She answered him.", "She is the daughter of Bethuel.", "Bethuel is the son Milcah bore to Nahor."],
  'instructions': [ins(K, S, "Rebekah identified herself as Nahor’s granddaughter."), ins(W, R, "The kind girl at the well is the right girl; the sign and the pedigree point the same way.")],
  'entries': ['rebekah'],
  'lost': [AGREE]},

 '24:25': {
  'received': "She added that they had plenty of straw and fodder, and room to lodge.",
  'explain': ("Hospitality for the camels first, then the men. The versions agree; the Latin hay, ample room."),
  'shared': ["She spoke further.", "They have plenty of straw and feed.", "They have room to lodge."],
  'instructions': [ins(K, S, "Rebekah offered lodging for the servant and his camels.")],
  'entries': ['rebekah'],
  'lost': [AGREE]},

 '24:26': {
  'received': "The man bowed and worshipped the Lord.",
  'explain': ("Thanksgiving before explanation. The Hebrew says the man bowed down and worshipped, two verbs of the body; the Greek the man was pleased "
   "and worshipped the Lord, saying, with the first verb become an inward approval; the Latin bowed down and worshipped."),
  'shared': ["The man responded to her answer.", "He worshipped the Lord.", "He will bless God in the next verse."],
  'instructions': [ins(K, S, "The servant worshipped on learning who she was."), ins(W, R, "He worships at the well before the family has said yes; gratitude for the sign does not wait for the outcome.")],
  'entries': ['yhwh-yahweh'],
  'lost': [
   loses("Hebrew va-yiqqod ha-ish va-yishtachu la-YHWH, “the man bowed down and prostrated himself to YHWH,” becomes Greek eudokēsas ho anthrōpos prosekynēsen kyriō, “being pleased, the man worshipped the Lord”; the bodily bow is gone, and the Greek adds kai eipen, “and said,” here."),
   between("Latin “bowed down and worshiped the Lord” and King James “bowed down his head, and worshipped” keep the bow."),
  ]},

 '24:27': {
  'received': "He blessed the God of Abraham for not forsaking His kindness and truth and for leading him to his master’s kin.",
  'explain': ("The blessing names God’s chesed and emet, kindness and faithfulness, and the guidance on the way. The Hebrew says kindness and faithfulness, "
   "the house of my master’s brothers; the Greek righteousness and truth, my master’s brother, and the Lord in the last clause; the Latin mercy and faithfulness, a straight way."),
  'shared': ["Blessed be the Lord, the God of his master Abraham.", "God has not forsaken His kindness and truth toward his master.", "The Lord has led the servant to the house of his master’s kin."],
  'instructions': [ins(K, S, "The servant blessed God for guiding him to Abraham’s family."), ins(W, R, "He credits the way, not his own cleverness: “I being in the way, the Lord led me.” Guidance is noticed on the road, not planned in advance.")],
  'entries': ['abraham', 'yhwh-yahweh'],
  'lost': [
   loses("Hebrew chasdo va-amitto, “His kindness and His faithfulness,” becomes Greek tēn dikaiosynēn autou kai tēn alētheian, “His righteousness and truth”; Hebrew achei adoni, “my master’s brothers,” plural kin, becomes Greek tou adelphou tou kyriou mou, “my master’s brother,” singular."),
   between("Latin “mercy and faithfulness … by a straight way … my master’s brother” blends; King James “his mercy and his truth … my master’s brethren” keeps the plural."),
  ]},

 '24:28': {
  'received': "The girl ran to tell her mother’s household.",
  'explain': ("Rebekah runs again, to her mother’s house, the women’s quarters. The versions agree; the Latin everything she had heard."),
  'shared': ["The young woman ran.", "She told her mother’s household.", "She told them these things."],
  'instructions': [ins(K, S, "Rebekah reported to her mother’s household.")],
  'entries': ['rebekah'],
  'lost': [AGREE]},

 '24:29': {
  'received': "Her brother Laban ran out to the man at the spring.",
  'explain': ("Laban enters the story, the brother who will later deal with Jacob. He runs too. The versions agree."),
  'shared': ["Rebekah had a brother named Laban.", "Laban ran out.", "He went to the man at the spring."],
  'instructions': [ins(K, S, "Laban came out to the servant.")],
  'entries': ['rebekah'],
  'lost': [AGREE]},

 '24:30': {
  'received': "Having seen the jewellery and heard Rebekah’s account, Laban found the man standing by the camels.",
  'explain': ("The narrator explains Laban’s haste: he saw the gold first and heard the story second. The Hebrew says ring; the Greek and Latin earrings, as in verse 22."),
  'shared': ["Laban saw the ring and bracelets on his sister’s arms.", "He heard Rebekah’s words, thus the man spoke to me.", "He came to the man standing by the camels at the spring."],
  'instructions': [ins(K, S, "Laban was drawn by the gifts and the report."), ins(W, R, "Laban sees the gold before he hears the man; the order of his seeing foreshadows the Laban of Genesis 29–31.")],
  'entries': ['rebekah'],
  'lost': [between("Hebrew ha-nezem, “the ring,” is Greek ta enōtia, “the earrings,” continuing from 24:22; Latin “earrings,” King James “earring.” The Latin says “recount all the words.”")]},

 '24:31': {
  'received': "Laban welcomed him in as one blessed of the Lord, having prepared the house and a place for the camels.",
  'explain': ("Laban’s greeting. The Hebrew says come in, blessed of YHWH, a title for the guest; the Greek come in; blessed be the Lord, a blessing of God; "
   "the Latin and King James follow the Hebrew. The Hebrew construction allows either reading, and the recipient of the blessing shifts."),
  'shared': ["Laban says, Come in.", "He asks why the man stands outside.", "He has prepared the house and a place for the camels."],
  'instructions': [ins(K, S, "Laban welcomed Abraham’s servant into his house."), ins(W, R, "Whether the guest is blessed or the Lord is, Laban’s house opens to a stranger because of what the Lord has done at the well.")],
  'entries': ['yhwh-yahweh'],
  'lost': [
   loses("Hebrew bo berukh YHWH, “come in, blessed of YHWH,” a vocative title for the visitor, becomes Greek deuro eiselthe, eulogētos kyrios, “come, enter; blessed be the Lord,” a doxology; the Greek also adds autō, “to him.”"),
   between("Latin “come in, blessed of the Lord” and King James “come in, thou blessed of the LORD” keep the title."),
  ]},

 '24:32': {
  'received': "The man came in; the camels were unloaded and fed, and water was brought for the feet of him and his men.",
  'explain': ("Hospitality in order: camels unloaded, straw and fodder, water for feet. The Hebrew says water to wash his feet; the Greek water for his "
   "feet without the verb; the Latin he brought him into the lodging. The Hebrew-column rendering was corrected today."),
  'shared': ["The man entered the house.", "The camels were unloaded and given straw and feed.", "Water was provided for his feet and his men’s."],
  'instructions': [ins(K, S, "The servant and his camels were received and provided for.")],
  'entries': [],
  'lost': [between("Hebrew u-mayim lirchotz raglav, “and water to wash his feet,” is Greek kai hydōr nipsasthai tois posin autou, “water for his feet”; Latin “water to wash his feet,” King James likewise; the Latin makes Laban the subject, “he brought him into the lodging.”")]},

 '24:33': {
  'received': "Food was set before him, but he refused to eat until he had told his errand, and was told to speak.",
  'explain': ("Business before bread; the servant will not eat until he has spoken. The Hebrew says food before him, and the reply was speak; the Greek "
   "bread before them, they said; the Latin bread before him, he answered. Grammar shifts the participants, not the sense."),
  'shared': ["Food was set before him.", "He would not eat until he had spoken his business.", "He was told, Speak."],
  'instructions': [ins(K, S, "The servant insisted on stating his errand before eating."), ins(W, R, "He puts his master’s business before his own hunger; the faithful servant’s appetite waits on his task.")],
  'entries': [],
  'lost': [between("Hebrew va-yusam lefanav le’ekhol, “and it was set before him to eat,” is Greek parethēken autois artous, “set bread before them,” and the reply va-yomer is Greek eipan, “they said”; Latin “bread before him … he answered,” King James “set meat before him … he said.”")]},

 '24:34': {
  'received': "He said, I am Abraham’s servant.",
  'explain': ("The speech begins with his credentials, which are his master’s name. The versions agree."),
  'shared': ["He speaks.", "He is a servant.", "His master is Abraham."],
  'instructions': [ins(K, S, "The servant identified himself by his master.")],
  'entries': ['abraham'],
  'lost': [AGREE]},

 '24:35': {
  'received': "The Lord has greatly blessed his master with flocks, herds, silver, gold, slaves, camels and donkeys.",
  'explain': ("The servant reports Abraham’s wealth as the Lord’s blessing: become great, with the standard inventory. The Hebrew says flocks and herds; "
   "the Greek sheep and calves, exalted; the Latin sheep, oxen."),
  'shared': ["The Lord has greatly blessed his master.", "His master has become great.", "He has flocks, herds, silver, gold, male and female servants, camels and donkeys."],
  'instructions': [ins(K, S, "The servant reported Abraham’s God-given wealth."), ins(W, R, "Wealth is named as blessing, not achievement; the servant is making a case for the family to trust the God who gave it.")],
  'entries': ['abraham', 'yhwh-yahweh'],
  'lost': [between("Hebrew tzon u-vaqar, “flocks and herds,” is Greek probata kai moschous, “sheep and calves,” and va-yigdal, “he became great,” is kai hypsōthē, “he was exalted”; Latin “sheep, oxen,” King James “flocks, and herds.”")]},

 '24:36': {
  'received': "Sarah bore his master a son in old age, and he has given him everything.",
  'explain': ("Isaac, unnamed here, is the heir of all. The Hebrew says in her old age, Sarah’s; the Greek after he had grown old, Abraham’s, and one son; "
   "the Latin and King James follow the Hebrew. Both are true."),
  'shared': ["Sarah, his master’s wife, bore his master a son.", "It was in old age.", "His master has given the son everything he has."],
  'instructions': [ins(K, S, "The servant presented Isaac as sole heir."), ins(W, R, "The suit is for a son born of a miracle and heir of everything; the family is told what kind of house their daughter would join.")],
  'entries': ['sarah', 'isaac'],
  'lost': [between("Hebrew acharei ziqnatah, “after her old age,” is Greek meta to gērasai auton, “after he had grown old,” and the Greek adds hena, “one” son; Latin “in her old age” and King James “when she was old” follow the Hebrew.")]},

 '24:37': {
  'received': "His master made him swear not to take a wife from the Canaanites.",
  'explain': ("The retelling of 24:3, close to verbatim. The versions agree; the oath by the God of heaven is omitted in the retelling in all columns."),
  'shared': ["His master made him swear.", "He must not take a wife for the son from the Canaanite daughters.", "His master lives in their land."],
  'instructions': [ins(K, S, "The servant repeated Abraham’s prohibition.")],
  'entries': ['canaan'],
  'lost': [AGREE]},

 '24:38': {
  'received': "He must go to Abraham’s father’s house and clan for a wife.",
  'explain': ("The retelling of 24:4, with my father’s house for my land. The Greek adds from there; the Latin from my kindred."),
  'shared': ["He must go to his master’s father’s house.", "He must go to his master’s clan.", "He must take a wife for the son."],
  'instructions': [ins(K, S, "The servant repeated the charge to seek the wife among kin.")],
  'entries': [],
  'lost': [keeps("An added ekeithen, “from there,” in the Greek; Hebrew mishpachti, “my clan,” is Greek phylēn mou, “my tribe.”"), between("Latin “take a wife for my son from my kindred” rearranges; King James follows the Hebrew.")]},

 '24:39': {
  'received': "He objected that perhaps the woman would not follow.",
  'explain': ("The retelling of 24:5, shortened: the question about taking Isaac back is dropped, as the servant would not raise before strangers the "
   "possibility of Isaac coming to them. The versions agree."),
  'shared': ["The servant spoke to his master.", "Perhaps the woman will not follow.", "The objection is reported."],
  'instructions': [ins(K, S, "The servant reported his own objection, shortened."), ins(W, R, "He omits before Laban the question of bringing Isaac to Haran; a faithful report can still choose what not to say.")],
  'entries': [],
  'lost': [AGREE]},

 '24:40': {
  'received': "Abraham said the Lord before whom he walked would send His angel and prosper the way, for a wife from his clan and father’s house.",
  'explain': ("The retelling of 24:7 with a new phrase: the Lord before whom I have walked. The Hebrew idiom of walking before God, as in 17:1, becomes "
   "in the Greek the Lord whom I have pleased, the translators’ regular rendering of the idiom; the Latin in whose presence I walk, direct your way."),
  'shared': ["The Lord will send His angel with the servant.", "He will prosper the journey.", "The servant will take a wife for the son from Abraham’s clan and father’s house."],
  'instructions': [ins(K, S, "Abraham’s confidence in the angel is reported."), ins(W, R, "“Before whom I walk” and “whom I have pleased” describe one life from two sides: the Hebrew names the posture, the Greek its result.")],
  'entries': ['abraham', 'angel-of-the-lord', 'yhwh-yahweh'],
  'lost': [
   loses("Hebrew YHWH asher-hithallakhti lefanav, “YHWH before whom I have walked,” becomes Greek kyrios hō euērestēsa enantion autou, “the Lord whom I have pleased before Him”; the walking idiom of 5:22, 6:9 and 17:1 is rendered by its ethical sense."),
   between("Latin “in whose presence I walk … direct your way” and King James “before whom I walk … prosper thy way” keep the walking."),
  ]},

 '24:41': {
  'received': "Then he would be free of the oath if he came to the clan and they refused her.",
  'explain': ("The release clause retold. The Hebrew uses alah, oath-curse, in both clauses; the Greek distinguishes curse and oath; the Latin free of my "
   "curse. An oath carried its own curse on the breaker; the servant is cleared of both if the family refuses."),
  'shared': ["The servant will be free of the oath.", "The condition is coming to the clan.", "If they will not give her, he is free."],
  'instructions': [ins(K, S, "The servant reported the condition that would release him."), ins(W, R, "He tells the family they can refuse without cost to him; the proposal is made without pressure.")],
  'entries': [],
  'lost': [between("Hebrew alah, “oath,” in both clauses is Greek ara, “curse,” then horkismos, “oath”; Latin “free of my curse” uses one term, King James “clear from this my oath … clear from my oath.”")]},

 '24:42': {
  'received': "Today he came to the spring and prayed that the God of Abraham would prosper his way.",
  'explain': ("The retelling of 24:12, compressed to the one petition. The versions agree; the Latin if You have directed the way."),
  'shared': ["Today he came to the spring.", "He prayed to the Lord, God of his master Abraham.", "He asked God to prosper his journey."],
  'instructions': [ins(K, S, "The servant recounted his prayer at the spring.")],
  'entries': ['abraham', 'yhwh-yahweh'],
  'lost': [AGREE]},

 '24:43': {
  'received': "He stands by the spring; the girl who comes to draw, whom he asks for water,",
  'explain': ("The sign retold, running into the next verse. The Hebrew says the young woman who comes out to draw; the Greek keeps the daughters of the "
   "men of the city from 24:13 and says virgin; the Latin and King James virgin."),
  'shared': ["He stands by the spring of water.", "A young woman will come out to draw.", "He will ask her for a little water from her jar."],
  'instructions': [ins(K, S, "The servant retold the terms of the sign.")],
  'entries': [],
  'lost': [keeps("An added kai hai thygateres tōn anthrōpōn tēs poleōs exeleusontai hydreusasthai, “and the daughters of the men of the city will come out to draw water,” carried over from 24:13 in the Greek; Hebrew ha-almah, “the young woman,” is Greek parthenos, “virgin.”"), between("Latin and King James say “virgin” with the Greek and omit the daughters with the Hebrew.")]},

 '24:44': {
  'received': "and who offers to water the camels too, let her be the woman appointed for his master’s son.",
  'explain': ("The sign completed. The Hebrew ends with appointed for my master’s son; the Greek adds for His own servant Isaac and the closing clause "
   "by this I will know You have shown mercy to my master Abraham, carried over from 24:14; the Latin and King James end with the Hebrew."),
  'shared': ["She will say drink and offer to draw for the camels too.", "She is the woman the Lord has appointed.", "She is for his master’s son."],
  'instructions': [ins(K, S, "The servant retold the sign’s completion.")],
  'entries': ['isaac', 'abraham'],
  'lost': [keeps("An added tō heautou theraponti Isaak, “for His own servant Isaac,” and en toutō gnōsomai hoti pepoiēkas eleos tō kyriō mou Abraam, “by this I will know that You have shown mercy to my master Abraham,” in the Greek fill the retelling from 24:14; the Hebrew says le-ven adoni, “for my master’s son,” and stops."), between("Latin “prepared for my master’s son” and King James “appointed out for my master’s son” follow the Hebrew.")]},

 '24:45': {
  'received': "Before he finished praying in his heart, Rebekah came with her jar, drew water, and he asked to drink.",
  'explain': ("The retelling of 24:15–17. Here the Hebrew says speaking in my heart, making the inward prayer explicit; the Greek in my mind, immediately; "
   "the Latin silently considering within myself."),
  'shared': ["Before he finished speaking inwardly, Rebekah came out.", "Her jar was on her shoulder; she went down and drew.", "He asked her for a drink."],
  'instructions': [ins(K, S, "The servant recounted Rebekah’s arrival.")],
  'entries': ['rebekah'],
  'lost': [between("Hebrew le-dabber el-libbi, “to speak to my heart,” is Greek lalōn en tē dianoia, “speaking in my mind,” with an added eutheōs, “immediately,” for Hebrew ve-hinneh, “and behold”; Latin “silently considering within myself,” King James “speaking in mine heart.”")]},

 '24:46': {
  'received': "She quickly lowered her jar, offered water to him and the camels, and watered them.",
  'explain': ("The retelling of 24:18–20, compressed. The Hebrew says from her shoulder; the Greek omits it; the arm of 24:18 is in neither. The Latin follows the Hebrew."),
  'shared': ["She quickly lowered her jar.", "She said drink, and I will water your camels.", "He drank and she watered the camels."],
  'instructions': [ins(K, S, "The servant recounted Rebekah’s kindness.")],
  'entries': ['rebekah'],
  'lost': [between("Hebrew me-aleha, “from upon her,” the shoulder, is absent from the Greek; Latin “from her shoulder” and King James likewise keep it.")]},

 '24:47': {
  'received': "He asked whose daughter she was, she named Bethuel, and he put the ring and bracelets on her.",
  'explain': ("The retelling of 24:22–24, reordered so the gifts follow the identification, as a prudent servant would tell it. The Hebrew says the ring on "
   "her nose; the Greek earrings on her; the Latin earrings to adorn her face; the King James earring upon her face."),
  'shared': ["He asked whose daughter she was.", "She is the daughter of Bethuel, Nahor’s son, whom Milcah bore.", "He put the ring and bracelets on her."],
  'instructions': [ins(K, S, "The servant recounted the identification and the gifts."), ins(W, R, "In the retelling the gifts follow the pedigree; the servant tells it as it should have been, and the narrator let us see it as it was.")],
  'entries': ['rebekah'],
  'lost': [loses("Hebrew va-asim ha-nezem al-appah, “I put the ring on her nose,” becomes Greek periethēka autē ta enōtia, “I put the earrings on her”; the nose-ring is lost."), between("Latin “hung the earrings to adorn her face” and King James “the earring upon her face” keep the face without the nose.")]},

 '24:48': {
  'received': "He bowed and worshipped, blessing the God of Abraham for leading him on the true way to his master’s brother’s daughter.",
  'explain': ("The retelling of 24:26–27. The Hebrew says bowed down and worshipped, the way of truth; the Greek I was pleased and worshipped, as at 24:26, "
   "the way of truth; the Latin bowed, a straight way; the King James the right way."),
  'shared': ["He worshipped the Lord.", "He blessed the Lord, the God of his master Abraham.", "God led him on the true way to take his master’s brother’s daughter for his son."],
  'instructions': [ins(K, S, "The servant recounted his thanksgiving.")],
  'entries': ['abraham', 'yhwh-yahweh'],
  'lost': [loses("Hebrew va-eqqod va-eshtachaveh, “I bowed down and worshipped,” becomes Greek eudokēsas prosekynēsa, “being pleased I worshipped,” as at 24:26."), between("Latin “bowed down and worshiped … by a straight way” and King James “bowed down my head … the right way” keep the bow; Hebrew be-derekh emet, “in the way of truth,” is Greek en hodō alētheias.")]},

 '24:49': {
  'received': "If they will deal kindly and truly with his master, let them say so; if not, let them say so, that he may turn right or left.",
  'explain': ("The proposal, with a request for a plain answer either way. The Hebrew says kindness and faithfulness; the Greek mercy and righteousness; "
   "the Latin if something else pleases you. To turn right or left is to go elsewhere."),
  'shared': ["If they will show kindness and faithfulness to his master, they should tell him.", "If not, they should tell him.", "Then he may turn to the right or the left."],
  'instructions': [ins(K, S, "The servant asked for a clear answer."), ins(W, R, "He asks for a no as readily as a yes; a servant who trusts providence does not need to manage the answer.")],
  'entries': [],
  'lost': [between("Hebrew chesed ve-emet, “kindness and faithfulness,” is Greek eleos kai dikaiosynēn, “mercy and righteousness”; Latin “kindness and faithfulness … if something else pleases you” expands the second clause; King James “deal kindly and truly.”")]},

 '24:50': {
  'received': "Laban and Bethuel answered that the matter was from the Lord and they could not speak against it.",
  'explain': ("The family consents, Bethuel the father named with Laban the brother. The Hebrew idiom we cannot speak to you bad or good means we have "
   "nothing to add; the Greek we cannot oppose you by setting evil against good; the Latin nothing beyond His pleasure. Abraham’s own words to the king of Sodom used the same idiom."),
  'shared': ["Laban and Bethuel answered.", "The matter has come from the Lord.", "They cannot speak against it."],
  'instructions': [ins(K, S, "Rebekah’s family recognised God’s hand and consented."), ins(W, R, "“The thing proceeds from the Lord” ends all bargaining; where providence is seen, the family has nothing to add for or against.")],
  'entries': ['yhwh-yahweh'],
  'lost': [
   loses("Hebrew lo nukhal dabber elekha ra o-tov, “we cannot speak to you bad or good,” an idiom for having no say, becomes Greek ou dynēsometha oun soi anteipein kakon kalō, “we cannot oppose you, evil against good,” and the Greek adds prostagma, “this command.”"),
   between("Latin “we cannot speak anything else to you beyond His pleasure” paraphrases; King James “we cannot speak unto thee bad or good” keeps the idiom."),
  ]},

 '24:51': {
  'received': "Rebekah is before you; take her and go, and let her be your master’s son’s wife, as the Lord has spoken.",
  'explain': ("The formal consent, acknowledging the Lord’s word in the matter. The versions agree."),
  'shared': ["Rebekah is before the servant.", "He may take her and go.", "She shall be his master’s son’s wife, as the Lord has spoken."],
  'instructions': [ins(K, S, "The family gave Rebekah to be Isaac’s wife.")],
  'entries': ['rebekah', 'yhwh-yahweh'],
  'lost': [AGREE]},

 '24:52': {
  'received': "Hearing this, the servant bowed to the ground and worshipped the Lord.",
  'explain': ("A third act of worship, this time to the ground. Here the Greek keeps the bow. The versions agree."),
  'shared': ["Abraham’s servant heard their words.", "He worshipped the Lord.", "He bowed down to the earth."],
  'instructions': [ins(K, S, "The servant worshipped on receiving consent."), ins(W, R, "Three times the servant worships in this chapter: at the sign, at the pedigree, at the consent. Each step of the way is received as a gift.")],
  'entries': ['yhwh-yahweh'],
  'lost': [AGREE]},

 '24:53': {
  'received': "He gave Rebekah silver and gold articles and clothing, and gifts to her brother and mother.",
  'explain': ("The bride-gifts, then gifts for the family, precious things. The Hebrew and Greek say brother; the Latin brothers. Bethuel is not among the recipients, which some take as a sign he was infirm."),
  'shared': ["The servant brought out silver and gold articles and clothing.", "He gave them to Rebekah.", "He also gave gifts to her brother and mother."],
  'instructions': [ins(K, S, "The servant gave gifts to Rebekah and her family.")],
  'entries': ['rebekah'],
  'lost': [between("Hebrew le-achiha, “to her brother,” and Greek tō adelphō autēs agree; Latin “her brothers” is plural; Hebrew migdanot, “precious things,” is Greek dōra, “gifts,” King James “precious things.”")]},

 '24:54': {
  'received': "They ate, drank and stayed the night; in the morning he asked to be sent to his master.",
  'explain': ("Only now does he eat. He stays one night and asks to leave at dawn. The Hebrew says they arose; the Greek rising he said; the Latin a feast."),
  'shared': ["He and his men ate and drank.", "They stayed the night.", "In the morning he said, Send me away to my master."],
  'instructions': [ins(K, S, "The servant asked to depart the next morning."), ins(W, R, "The errand accomplished, he will not linger; the faithful servant is as quick to return as Rebekah was to draw.")],
  'entries': [],
  'lost': [between("Hebrew va-yaqumu va-boqer, “they arose in the morning,” is Greek anastas to prōi eipen, “rising in the morning he said”; Latin “they began a feast” expands the meal; King James follows the Hebrew.")]},

 '24:55': {
  'received': "Her brother and mother asked that she stay some days, perhaps ten, before going.",
  'explain': ("The family asks for time. The Hebrew phrase days or ten is difficult, a few days, at least ten; the Greek about ten days; the Latin at least ten, brothers; "
   "the King James a few days, at the least ten. The Hebrew and Greek say the young woman and virgin respectively."),
  'shared': ["Her brother and mother spoke.", "Let the young woman stay some days, about ten.", "Afterward she may go."],
  'instructions': [ins(K, S, "Rebekah’s family asked for a delay of about ten days.")],
  'entries': ['rebekah'],
  'lost': [between("Hebrew yamim o asor, “days or ten,” a difficult phrase, is Greek hēmeras hōsei deka, “about ten days”; Hebrew achiha, “her brother,” is Greek hoi adelphoi, “her brothers”; Hebrew na‘arah is Greek parthenos, “virgin.” Latin “brothers … at least ten days”; King James “brother … a few days, at the least ten.”")]},

 '24:56': {
  'received': "He asked them not to delay him, since the Lord had prospered his way.",
  'explain': ("He refuses the delay, on the ground of providence: the Lord has prospered the way, so let it be finished. The versions agree."),
  'shared': ["Do not delay me.", "The Lord has prospered my way.", "Send me away to my master."],
  'instructions': [ins(K, S, "The servant pressed to leave at once."), ins(W, R, "When God has opened the way, delay is a kind of ingratitude; the servant wants to finish what providence began.")],
  'entries': ['yhwh-yahweh'],
  'lost': [AGREE]},

 '24:57': {
  'received': "They proposed to call the girl and ask her.",
  'explain': ("Rebekah is given a voice in her own marriage, unusual in the narratives. The versions agree; the Hebrew says ask at her mouth."),
  'shared': ["They spoke.", "Let us call the young woman.", "Let us ask her herself."],
  'instructions': [ins(K, S, "The family deferred to Rebekah’s own choice."), ins(W, R, "The decision that will carry the promise forward is given to the woman who must make the journey.")],
  'entries': ['rebekah'],
  'lost': [AGREE]},

 '24:58': {
  'received': "Asked if she would go with this man, Rebekah said, I will go.",
  'explain': ("Two words in Hebrew, elekh, I will go. Like Abraham leaving Haran, she goes to a land she has not seen for a man she has not met. The versions agree."),
  'shared': ["They called Rebekah.", "They asked whether she would go with this man.", "She said, I will go."],
  'instructions': [ins(K, S, "Rebekah consented to go."), ins(W, R, "Rebekah leaves Haran as Abraham did, by her own word; the promise passes through a second departure in faith.")],
  'entries': ['rebekah', 'haran'],
  'lost': [AGREE]},

 '24:59': {
  'received': "They sent Rebekah away with her nurse, Abraham’s servant and his men.",
  'explain': ("The company departs. The Hebrew says her nurse, Deborah, named at her death in 35:8; the Greek her belongings; the Latin and King James her nurse. "
   "The Greek does not deny the nurse, but she is not mentioned."),
  'shared': ["They sent away their sister Rebekah.", "Abraham’s servant went with her.", "His men went too."],
  'instructions': [ins(K, S, "Rebekah departed with the servant’s company.")],
  'entries': ['rebekah', 'abraham'],
  'lost': [loses("Hebrew ve-et-meniqtah, “and her nurse,” becomes Greek kai ta hyparchonta autēs, “and her belongings”; the nurse, named Deborah in 35:8, is lost here."), between("Latin “with her nurse” and King James “her nurse” keep her.")]},

 '24:60': {
  'received': "They blessed Rebekah: may she become thousands of ten thousands and her seed possess the gate of their enemies.",
  'explain': ("The family’s blessing echoes God’s to Abraham in 22:17: seed beyond counting, possessing the enemy’s gate. The Hebrew says the gate of "
   "those who hate them; the Greek inherit the cities of their adversaries; the Latin thousands of thousands, the gates of their enemies."),
  'shared': ["They blessed their sister Rebekah.", "May she become thousands of ten thousands.", "May her seed possess the gate of those who hate them."],
  'instructions': [ins(K, S, "Rebekah’s family blessed her with fruitfulness and victory."), ins(W, R, "Without knowing it, Laban’s house speaks the blessing of Moriah over the bride; the promise to Abraham’s seed is now spoken over Isaac’s wife.")],
  'entries': ['rebekah'],
  'lost': [loses("Hebrew sha‘ar sone’av, “the gate of those who hate them,” the city’s strongpoint, becomes Greek tas poleis tōn hypenantiōn, “the cities of their adversaries”; the Greek adds “you are our sister” as a statement."), between("Latin “thousands of thousands … the gates of their enemies” and King James “thousands of millions … the gate of those which hate them” keep the gate.")]},

 '24:61': {
  'received': "Rebekah and her maids mounted the camels and followed the man, and the servant took her and went.",
  'explain': ("The departure, with Rebekah’s attendants. The Hebrew says her young women; the Greek her servant women; the Latin her maidens, who hurried back to his master, "
   "omitting the servant took Rebekah."),
  'shared': ["Rebekah and her maids arose and mounted the camels.", "They followed the man.", "The servant took Rebekah and departed."],
  'instructions': [ins(K, S, "Rebekah set out for Canaan with the servant.")],
  'entries': ['rebekah'],
  'lost': [between("Hebrew na‘aroteha, “her young women,” is Greek hai habrai autēs, “her attendants”; Latin “her maidens … who hurried back to his master” drops “the servant took Rebekah”; King James “her damsels … the servant took Rebekah.”")]},

 '24:62': {
  'received': "Isaac had come from Beer-lahai-roi and was living in the Negev.",
  'explain': ("Isaac is at Beer-lahai-roi, Hagar’s well of 16:14, the well of the Living One who sees. The Hebrew travel phrase is difficult, came from "
   "the way of; the Greek says travelling through the wilderness near the Well of the Vision, translating the name; the Latin the well called The Living One Who Sees, the southern land."),
  'shared': ["Isaac is connected with the well Lahai-roi.", "He was living in the land toward the south.", "He is about to meet the returning company."],
  'instructions': [ins(K, S, "Isaac was living in the Negev near Beer-lahai-roi."), ins(W, R, "Isaac waits at the well where Hagar found that God sees; the heir of the promise meets his bride near the place of the outcast’s comfort.")],
  'entries': ['isaac', 'hagar', 'el-roi'],
  'lost': [loses("Hebrew Be’er Lachai Ro’i, a place name, becomes Greek to phrear tēs horaseōs, “the Well of the Vision,” a translation, and Hebrew ba mi-bo, “came from coming,” becomes dieporeueto dia tēs erēmou, “was travelling through the wilderness”; Hebrew Negev is Greek “the land toward the south.”"), between("Latin “the well called The Living One Who Sees … the southern land” translates; King James “the well Lahairoi … the south country” keeps the name.")]},

 '24:63': {
  'received': "Isaac went out to meditate in the field at evening and saw camels coming.",
  'explain': ("Isaac at evening in the field, meditating, praying or walking; the Hebrew verb is uncertain. He lifts his eyes and sees the camels. The versions agree; the Latin as the day declined, in the distance."),
  'shared': ["Isaac went out into the field toward evening.", "He went to meditate.", "He looked up and saw camels coming."],
  'instructions': [ins(K, S, "Isaac saw the camels approaching at evening."), ins(W, R, "The chapter began at evening by a well with the servant’s prayer and ends at evening in a field with Isaac’s; the bride arrives between two prayers.")],
  'entries': ['isaac'],
  'lost': [AGREE]},

 '24:64': {
  'received': "Rebekah saw Isaac and got down from the camel.",
  'explain': ("She dismounts on seeing a man approach, as modesty required. The Hebrew says she fell from the camel, idiomatically got down; the Greek leaped down; the Latin dismounted."),
  'shared': ["Rebekah lifted her eyes.", "She saw Isaac.", "She got down from the camel."],
  'instructions': [ins(K, S, "Rebekah dismounted on seeing Isaac.")],
  'entries': ['rebekah', 'isaac'],
  'lost': [between("Hebrew va-tippol me-al ha-gamal, “she fell from upon the camel,” an idiom for dismounting, is Greek katepēdēsen apo tēs kamēlou, “she leaped down from the camel”; Latin “dismounted,” King James “lighted off.”")]},

 '24:65': {
  'received': "Told that the man in the field was his master, she covered herself with her veil.",
  'explain': ("She asks, the servant answers, it is my master, now Isaac, not Abraham, and she veils herself for her bridegroom. The versions agree; the Latin she quickly took."),
  'shared': ["She asked the servant who the man walking to meet them was.", "The servant said, It is my master.", "She took her veil and covered herself."],
  'instructions': [ins(K, S, "Rebekah veiled herself before Isaac."), ins(W, R, "The servant calls Isaac “my master” for the first time; the heir has come into his inheritance in the servant’s speech before the father dies.")],
  'entries': ['rebekah', 'isaac'],
  'lost': [AGREE]},

 '24:66': {
  'received': "The servant told Isaac all he had done.",
  'explain': ("The report is to Isaac, not Abraham, and the chapter does not return to Abraham. The versions agree."),
  'shared': ["The servant told Isaac.", "He told all the things.", "They were the things he had done."],
  'instructions': [ins(K, S, "The servant reported to Isaac.")],
  'entries': ['isaac'],
  'lost': [AGREE]},

 '24:67': {
  'received': "Isaac brought Rebekah into his mother Sarah’s tent, took her as his wife and loved her, and was comforted after his mother’s death.",
  'explain': ("The marriage: into Sarah’s tent, as wife, loved, and Isaac comforted for his mother. The Hebrew says the tent of Sarah his mother, after his "
   "mother’s death; the Greek his mother’s house, comforted concerning Sarah his mother; the Latin expands, he loved her so greatly that he found relief from the grief."),
  'shared': ["Isaac brought Rebekah into his mother Sarah’s tent.", "He took Rebekah and she became his wife, and he loved her.", "Isaac was comforted after his mother’s death."],
  'instructions': [ins(K, S, "Isaac married Rebekah and was comforted for Sarah."), ins(W, R, "The chapter that began with Sarah’s empty tent ends with Rebekah in it; love is the comfort God provides for the death that opened the story.")],
  'entries': ['isaac', 'rebekah', 'sarah'],
  'lost': [loses("Hebrew ha-ohelah Sarah immo, “into the tent of Sarah his mother,” becomes Greek eis ton oikon tēs mētros autou, “into his mother’s house,” without Sarah’s name; Hebrew acharei immo, “after his mother,” becomes peri Sarras tēs mētros autou, “concerning Sarah his mother.”"), between("Latin “the tent of his mother Sarah … he loved her so greatly that he found relief from the grief caused by his mother’s death” expands; King James “his mother Sarah’s tent … comforted after his mother’s death.”")]},
 }
}
