# Study prose for Genesis 25 — Saints Parallel Reader Study Workspace. Draft for review.
K, W, C = 'Knowledge', 'Wisdom', 'Command'
S, R = 'stated', 'reflection'
def ins(t, b, text): return {'type': t, 'basis': b, 'text': text}
def keeps(t): return {'dir': 'keeps', 'text': t}
def loses(t): return {'dir': 'loses', 'text': t}
def between(t): return {'dir': 'between', 'text': t}
AGREE = between("Hebrew, Greek, Latin and King James agree in substance; only the rendering of the divine name and small turns of phrase differ.")

CHAPTER = {
 'slug': 'genesis', 'chapter': 25,
 'chapterNote': (
  "Abraham’s story closes and Isaac’s opens: Keturah’s sons, Abraham’s death and burial beside Sarah, Ishmael’s twelve princes, and the birth of "
  "Esau and Jacob with the sale of the birthright. The Hebrew keeps the shorter genealogies, Machpelah by name, Hagar “the Egyptian,” Beer-lahai-roi, "
  "the children “struggling” in the womb, Jacob as a “quiet” man in tents, “game in his mouth,” and Esau’s doubled “that red stuff.” The Greek keeps "
  "three extra names among Keturah’s descendants (Teman, Raguel, Nabdeel), “the double cave,” the cave added to the purchase, the Well of the Vision, "
  "the children “leaping,” Jacob as “unfeigned” in a house, and “today” in the sale. The Latin and King James follow the Hebrew; the Latin moves "
  "Jacob’s birth into verse 25 and says “he died in the presence of all his brothers” of Ishmael."),
 'verses': {

 '25:1': {
  'received': "Abraham took another wife, Keturah.",
  'explain': ("After Sarah, Keturah, called a concubine in 1 Chronicles 1:32 and in verse 6 below. Her sons become the peoples of Arabia. The versions agree."),
  'shared': ["Abraham took another wife.", "Her name was Keturah.", "She follows Sarah."],
  'instructions': [ins(K, S, "Abraham married Keturah after Sarah’s death.")],
  'entries': ['abraham'],
  'lost': [AGREE]},

 '25:2': {
  'received': "She bore him Zimran, Jokshan, Medan, Midian, Ishbak and Shuah.",
  'explain': ("Six sons; Midian is the best known, the people of Moses’ father-in-law and of Gideon’s enemies. The versions agree."),
  'shared': ["Keturah bore Abraham sons.", "They were Zimran, Jokshan, Medan, Midian, Ishbak and Shuah.", "Six are named."],
  'instructions': [ins(K, S, "Keturah bore Abraham six sons."), ins(W, R, "Abraham becomes the father of many nations in the plainest sense; the promise of 17:5 is filled out by peoples who are not the chosen line.")],
  'entries': ['abraham'],
  'lost': [AGREE]},

 '25:3': {
  'received': "Jokshan fathered Sheba and Dedan; Dedan’s sons were Asshurim, Letushim and Leummim.",
  'explain': ("Sheba and Dedan are Arabian trading peoples. The Greek adds Teman among Jokshan’s sons and Raguel and Nabdeel among Dedan’s, names found "
   "elsewhere in the Edomite and Ishmaelite lists; the Hebrew, Latin and King James have the shorter list. The three Dedanite names are plural tribal forms."),
  'shared': ["Jokshan fathered Sheba and Dedan.", "Dedan had sons.", "They were Asshurim, Letushim and Leummim."],
  'instructions': [ins(K, S, "Jokshan’s line ran through Sheba and Dedan.")],
  'entries': [],
  'lost': [keeps("An added Thaiman, “Teman,” among Jokshan’s sons and Ragouēl kai Nabdeēl, “Raguel and Nabdeel,” among Dedan’s appear in the Greek and in no Hebrew witness."), between("Latin and King James give the Hebrew’s five names.")]},

 '25:4': {
  'received': "Midian’s sons were Ephah, Epher, Hanoch, Abida and Eldaah; all these were Keturah’s children.",
  'explain': ("The Midianite clans; Ephah appears with Midian in Isaiah 60:6. The Greek form of the last name is Elraga for Eldaah, a difference of letters, "
   "not of persons. The Latin Enoch for Hanoch is the same name."),
  'shared': ["Midian had sons.", "They were Ephah, Epher, Hanoch, Abida and Eldaah.", "All these were Keturah’s children."],
  'instructions': [ins(K, S, "Midian’s five clans descend from Keturah.")],
  'entries': [],
  'lost': [between("Hebrew Elda‘ah is Greek Elraga, a consonantal variant; Hebrew Chanokh is Latin Enoch; otherwise the lists agree.")]},

 '25:5': {
  'received': "Abraham gave all he had to Isaac.",
  'explain': ("The inheritance is Isaac’s alone, as 24:36 reported. The Greek adds his son; the Hebrew, Latin and King James say Isaac."),
  'shared': ["Abraham gave.", "He gave all that he had.", "He gave it to Isaac."],
  'instructions': [ins(K, S, "Isaac inherited everything from Abraham."), ins(W, R, "Many sons, one heir; the blessing is not divided among the nations Abraham fathered but passed whole to the son of promise.")],
  'entries': ['abraham', 'isaac'],
  'lost': [keeps("An added tō huiō autou, “his son,” in the Greek after Isaac."), between("Latin and King James say “Isaac” without the addition.")]},

 '25:6': {
  'received': "To his concubines’ sons he gave gifts and sent them east, away from Isaac, while he lived.",
  'explain': ("The other sons are provided for and separated, as Ishmael was. Concubines is plural, Hagar and Keturah. The versions agree."),
  'shared': ["Abraham gave gifts to the sons of his concubines.", "He did so while he was still living.", "He sent them eastward, away from Isaac, to the land of the East."],
  'instructions': [ins(K, S, "Abraham settled his other sons in the East before he died."), ins(W, R, "Provision without inheritance: Abraham does his duty by every son and keeps the promise for one.")],
  'entries': ['abraham', 'isaac'],
  'lost': [AGREE]},

 '25:7': {
  'received': "Abraham lived a hundred and seventy-five years.",
  'explain': ("The lifespan formula, as for Sarah: the days of the years of his life. A hundred years in Canaan, since he came at seventy-five. The versions agree; the King James keeps the full formula."),
  'shared': ["The years of Abraham’s life are counted.", "They were a hundred and seventy-five.", "The formula closes his story."],
  'instructions': [ins(K, S, "Abraham died at a hundred and seventy-five.")],
  'entries': ['abraham'],
  'lost': [between("Hebrew yeme shene chayye Avraham asher chai, “the days of the years of Abraham’s life which he lived,” is compressed in the Greek to “the years of Abraham’s life”; King James keeps the full formula, Latin “the days of Abraham’s life.”")]},

 '25:8': {
  'received': "Abraham breathed his last and died old and satisfied, and was gathered to his people.",
  'explain': ("The good death: old, full, gathered to his people. The Hebrew says satisfied; the Greek and Latin full of days; the Greek his strength failed "
   "for breathed his last, and added to his people. Gathered to his people is the first use of the phrase."),
  'shared': ["Abraham breathed his last and died.", "It was at a good old age, old and full of days.", "He was gathered to his people."],
  'instructions': [ins(K, S, "Abraham died content and was gathered to his people."), ins(W, R, "“Gathered to his people” is said of a man buried far from his fathers; the people he joins are not in Haran. Hebrews says he looked for a city.")],
  'entries': ['abraham'],
  'lost': [between("Hebrew va-yigva, “he expired,” is Greek eklipōn, “failing”; Hebrew save‘a, “satisfied,” is Greek plērēs hēmerōn, “full of days,” Latin likewise; Hebrew va-ye’asef el-ammav, “was gathered to his peoples,” is Greek prosetethē pros ton laon autou, “was added to his people.”")]},

 '25:9': {
  'received': "Isaac and Ishmael buried him in the cave of Machpelah, in Ephron’s field facing Mamre.",
  'explain': ("The two sons, together again, bury their father in the tomb of chapter 23. The Hebrew says Machpelah; the Greek and Latin the double cave, as before."),
  'shared': ["His sons Isaac and Ishmael buried him.", "It was in the cave of Machpelah, in the field of Ephron son of Zohar the Hittite.", "It is opposite Mamre."],
  'instructions': [ins(K, S, "Isaac and Ishmael buried Abraham at Machpelah."), ins(W, R, "The sent-away son returns for the burial; whatever divided them, Ishmael and Isaac stand together at their father’s grave.")],
  'entries': ['isaac', 'abraham', 'hebron'],
  'lost': [between("Hebrew me‘arat ha-Makhpelah is Greek to spēlaion to diploun, “the double cave,” Latin likewise; King James “the cave of Machpelah”; Hebrew Tsochar is Greek Saar.")]},

 '25:10': {
  'received': "the field Abraham bought from the sons of Heth; there he was buried with Sarah.",
  'explain': ("The deed is recalled and the two are together. The Greek adds and the cave to the purchase; the Hebrew, Latin and King James say the field."),
  'shared': ["Abraham purchased the field from the sons of Heth.", "Abraham was buried there.", "Sarah his wife was there too."],
  'instructions': [ins(K, S, "Abraham was buried beside Sarah in the purchased field."), ins(W, R, "The one piece of Canaan Abraham owned receives him; he possesses in death the land he was promised in life.")],
  'entries': ['abraham', 'sarah', 'hebron'],
  'lost': [keeps("An added kai to spēlaion, “and the cave,” in the Greek makes the purchase explicit; Greek ethapsan, “they buried,” for the Hebrew passive."), between("Latin and King James follow the Hebrew.")]},

 '25:11': {
  'received': "After Abraham’s death God blessed Isaac, who lived by Beer-lahai-roi.",
  'explain': ("The blessing passes. Isaac lives at Hagar’s well, as in 24:62. The Hebrew keeps the name; the Greek the Well of the Vision; the Latin The Living One Who Sees."),
  'shared': ["Abraham died.", "God blessed his son Isaac.", "Isaac lived by the well Lahai-roi."],
  'instructions': [ins(K, S, "God’s blessing passed to Isaac."), ins(W, R, "The blessing is not inherited with the goods; God blesses Isaac Himself after Abraham is gone.")],
  'entries': ['isaac', 'el-roi'],
  'lost': [loses("Hebrew Be’er Lachai Ro’i becomes Greek to phrear tēs horaseōs, “the Well of the Vision,” as at 24:62."), between("Latin translates the name; King James “the well Lahairoi.”")]},

 '25:12': {
  'received': "These are the generations of Ishmael, whom Hagar, Sarah’s maid, bore to Abraham.",
  'explain': ("Ishmael receives his own toledot, generations, as a son of Abraham. The Hebrew says Hagar the Egyptian; the Greek omits Egyptian here, "
   "though 16:1 has it; the Latin ends with and, running on."),
  'shared': ["These are the generations of Ishmael, Abraham’s son.", "Hagar, Sarah’s slave woman, bore him.", "She bore him to Abraham."],
  'instructions': [ins(K, S, "Ishmael’s line is recorded as Abraham’s son."), ins(W, R, "The son outside the promise still has his generations written; God’s word to Hagar in 16:10 is kept on record.")],
  'entries': ['hagar', 'sarah', 'abraham', 'egypt'],
  'lost': [loses("Hebrew ha-Mitzrit, “the Egyptian,” after Hagar is absent from the Greek here."), between("Latin and King James keep “the Egyptian.”")]},

 '25:13': {
  'received': "Ishmael’s sons by generations: Nebaioth the firstborn, Kedar, Adbeel, Mibsam,",
  'explain': ("Twelve sons, like Jacob’s, begin. Nebaioth and Kedar are Arabian tribes known from Isaiah 60:7. The Greek has Nabdeel for Adbeel, the same form it added in verse 3."),
  'shared': ["These are the names of Ishmael’s sons.", "They are by name and generation.", "Nebaioth is the firstborn, then Kedar, Adbeel and Mibsam."],
  'instructions': [ins(K, S, "Ishmael’s sons begin with Nebaioth.")],
  'entries': [],
  'lost': [between("Hebrew Adbe’el is Greek Nabdeēl; Latin and King James Adbeel; the Latin says “his sons” without naming Ishmael again.")]},

 '25:14': {
  'received': "Mishma, Dumah, Massa,",
  'explain': ("Three more; Dumah and Massa are oases of northern Arabia, named in Isaiah 21:11 and Proverbs 30:1. The versions agree."),
  'shared': ["Mishma.", "Dumah.", "Massa."],
  'instructions': [ins(K, S, "The list continues with Mishma, Dumah and Massa.")],
  'entries': [],
  'lost': [AGREE]},

 '25:15': {
  'received': "Hadad, Tema, Jetur, Naphish and Kedemah.",
  'explain': ("The twelve completed. The Hebrew says Hadad and Tema; the Greek Choddad and Teman; the Latin and King James Hadar. Jetur and Naphish fight Israel in 1 Chronicles 5:19."),
  'shared': ["Hadad.", "Tema.", "Jetur, Naphish and Kedemah."],
  'instructions': [ins(K, S, "Ishmael’s twelve sons end with Kedemah.")],
  'entries': [],
  'lost': [between("Hebrew Chadad and Tema are Greek Choddad and Thaiman; Latin and King James Hadar, a daleth-resh confusion; the persons are the same.")]},

 '25:16': {
  'received': "These are Ishmael’s twelve sons, princes by their settlements and encampments, according to their peoples.",
  'explain': ("Twelve princes, nesi’im, as promised in 17:20. The Hebrew says settlements and encampments; the Greek tents and dwellings, rulers, nations; "
   "the Latin settlements and towns, tribes; the King James towns and castles."),
  'shared': ["These are Ishmael’s sons and their names.", "They are by their settlements and encampments.", "They are twelve princes according to their peoples."],
  'instructions': [ins(K, S, "Ishmael’s sons became twelve princes."), ins(W, R, "God promised Abraham twelve princes from Ishmael and lists them; the promise to the outcast son is kept as carefully as the promise to the heir.")],
  'entries': [],
  'lost': [between("Hebrew be-chatzrehem u-ve-tirotam, “by their villages and their encampments,” is Greek en tais skēnais autōn kai en tais epaulesin, “by their tents and dwellings”; Hebrew le-ummotam, “by their peoples,” is Greek kata ethnē, “by nations,” Latin “tribes,” King James “nations.”")]},

 '25:17': {
  'received': "Ishmael lived a hundred and thirty-seven years, died and was gathered to his people.",
  'explain': ("Ishmael’s death is told in the patriarchs’ formula, breathed his last and was gathered. The Greek says his strength failed, added to his family; the Latin joined to his people."),
  'shared': ["Ishmael lived a hundred and thirty-seven years.", "He breathed his last and died.", "He was gathered to his people."],
  'instructions': [ins(K, S, "Ishmael died at a hundred and thirty-seven.")],
  'entries': [],
  'lost': [between("Hebrew va-ye’asef el-ammav, “was gathered to his peoples,” is Greek prosetethē pros to genos autou, “was added to his family”; Latin “joined to his people,” King James “gathered unto his people.”")]},

 '25:18': {
  'received': "They settled from Havilah to Shur, toward Egypt and Assyria; he settled facing all his brothers.",
  'explain': ("The Ishmaelite range, from Havilah to Shur, the desert between Egypt and Assyria. The Hebrew shifts from they to he and ends with a difficult "
   "verb, fell, read as settled, echoing 16:12; the Greek he settled, dwelt opposite; the Latin and King James he died in the presence of all his brothers."),
  'shared': ["They settled from Havilah to Shur.", "Shur is opposite Egypt, on the way to Assyria.", "He settled facing all his brothers."],
  'instructions': [ins(K, S, "Ishmael’s descendants ranged from Havilah to Shur."), ins(W, R, "“In the presence of all his brothers” fulfils 16:12; Ishmael lives alongside the family he was sent away from, neither absorbed nor exiled.")],
  'entries': ['egypt'],
  'lost': [between("Hebrew nafal, “he fell,” an idiom for settling or for dying, is Greek katōkēsen, “he dwelt”; Latin “he died in the presence of all his brothers” and King James “he died in the presence of all his brethren” take the other sense; Hebrew Ashshurah is Greek “the Assyrians.”")]},

 '25:19': {
  'received': "These are the generations of Isaac, Abraham’s son; Abraham fathered Isaac.",
  'explain': ("The toledot of Isaac, which will run to chapter 35. The versions agree."),
  'shared': ["These are the generations of Isaac.", "He is Abraham’s son.", "Abraham begat Isaac."],
  'instructions': [ins(K, S, "Isaac’s generations begin here."), ins(W, R, "“Abraham begat Isaac” is said as if nothing else need be said; the whole of chapters 12–24 stands behind the three words.")],
  'entries': ['isaac', 'abraham'],
  'lost': [AGREE]},

 '25:20': {
  'received': "Isaac was forty when he married Rebekah, daughter of Bethuel the Aramean of Paddan-aram, sister of Laban.",
  'explain': ("Isaac’s age and Rebekah’s family restated. The Hebrew says Aramean, Paddan-aram; the Greek Syrian, Mesopotamia, and calls Laban Syrian too; "
   "the Latin omits Laban’s epithet. Paddan-aram is the region of Haran."),
  'shared': ["Isaac was forty years old.", "He took Rebekah, daughter of Bethuel the Aramean from Paddan-aram.", "She was sister of Laban."],
  'instructions': [ins(K, S, "Isaac married Rebekah at forty.")],
  'entries': ['isaac', 'rebekah', 'haran'],
  'lost': [between("Hebrew ha-Arammi mi-Paddan Aram, “the Aramean from Paddan-aram,” is Greek tou Syrou ek tēs Mesopotamias, “the Syrian from Mesopotamia”; Latin and King James “Syrian”; the Latin drops Laban’s “the Syrian.”")]},

 '25:21': {
  'received': "Isaac prayed for his barren wife; the Lord answered, and Rebekah conceived.",
  'explain': ("Twenty years of barrenness, by the dates of verses 20 and 26, and then prayer answered. The Hebrew says YHWH answered; the Greek God heard, "
   "and names Rebekah in the first clause; the Latin granted conception."),
  'shared': ["Isaac prayed to the Lord for his wife.", "She was barren.", "The Lord answered him and Rebekah conceived."],
  'instructions': [ins(K, S, "Isaac prayed and Rebekah conceived after barrenness."), ins(W, R, "The second generation also waits; the heir of promise has no heir until he prays, and the chosen line is again born of a barren womb.")],
  'entries': ['isaac', 'rebekah', 'yhwh-yahweh'],
  'lost': [between("Hebrew va-ye‘ater lo YHWH, “YHWH was entreated by him,” is Greek epēkousen de autou ho theos, “God heard him”; Greek adds Rebekah’s name in the first clause; Latin and King James follow the Hebrew.")]},

 '25:22': {
  'received': "The children struggled within her, and she asked why, and went to inquire of the Lord.",
  'explain': ("The twins fight before birth. The Hebrew says struggled, crushed one another, and Rebekah’s question is elliptical, if so, why am I this? The Greek "
   "leaped, as John would in Elizabeth, and if this is to happen to me, why?; the Latin why was there any need to conceive."),
  'shared': ["The children struggled within her.", "She asked why this was happening to her.", "She went to inquire of the Lord."],
  'instructions': [ins(K, S, "Rebekah sought the Lord about her troubled pregnancy."), ins(W, R, "Rebekah takes her question to God directly; the answered prayer brings a new trouble, and the trouble is brought back to the Answerer.")],
  'entries': ['rebekah', 'yhwh-yahweh'],
  'lost': [loses("Hebrew va-yitrotzatzu, “they crushed one another,” becomes Greek eskirtōn, “they leaped,” the verb of Luke 1:41; Hebrew im-ken lammah zeh anokhi, “if so, why this I?” becomes ei houtōs moi mellei ginesthai, hina ti moi touto, “if this is to happen to me, why this to me?”"), between("Latin “struggled together … why was there any need to conceive” expands; King James “struggled together … why am I thus?”")]},

 '25:23': {
  'received': "The Lord said two nations were in her womb, one stronger than the other, and the older would serve the younger.",
  'explain': ("The oracle that governs the rest of Genesis: two nations, two peoples, the elder serving the younger. The Hebrew says stronger, older, younger; "
   "the Greek surpass, the greater serve the lesser, which can mean age or rank; the Latin overcome, elder, younger. Paul reads it in Romans 9:12."),
  'shared': ["Two nations are in her womb.", "Two peoples will be separated from within her.", "One will be stronger, and the older will serve the younger."],
  'instructions': [ins(K, S, "God foretold two nations and the elder serving the younger."), ins(W, R, "Before either child has done anything, the order is reversed; the choice is announced in the womb so that no one can call it earned.")],
  'entries': ['yhwh-yahweh'],
  'lost': [between("Hebrew ve-rav ya‘avod tza‘ir, “and the greater shall serve the lesser,” the Hebrew words themselves meaning great and small, is Greek ho meizōn douleusei tō elassoni, matching the ambiguity; Latin “the elder shall serve the younger,” King James likewise; Hebrew ye’ematz, “will be stronger,” is Greek hyperexei, “will surpass.”")]},

 '25:24': {
  'received': "When her time came, there were twins in her womb.",
  'explain': ("The oracle confirmed at birth. The versions agree; the Latin twins were found."),
  'shared': ["Her days to give birth were fulfilled.", "Behold, twins.", "They were in her womb."],
  'instructions': [ins(K, S, "Rebekah bore twins.")],
  'entries': ['rebekah'],
  'lost': [AGREE]},

 '25:25': {
  'received': "The first came out red and hairy all over, and was named Esau.",
  'explain': ("Esau: red, admoni, and hairy, se‘ar, both names that will attach to him and his land, Edom and Seir. The Hebrew says like a hairy cloak, they named; "
   "the Greek like a hairy hide, he was named; the Latin a pelt, and moves Jacob’s birth and naming into this verse."),
  'shared': ["The first came out red.", "He was hairy all over like a garment.", "He was named Esau."],
  'instructions': [ins(K, S, "Esau was born first, red and hairy.")],
  'entries': [],
  'lost': [between("Hebrew ke-adderet se‘ar, “like a cloak of hair,” is Greek hōsei dora dasys, “like a hairy hide”; Hebrew va-yiqre’u, “they called,” is Greek epōnomasen, “he named”; Latin “like a pelt” and runs Jacob’s birth into this verse; King James “like an hairy garment … they called.”")]},

 '25:26': {
  'received': "Then his brother came out grasping Esau’s heel and was named Jacob; Isaac was sixty.",
  'explain': ("Jacob, Ya‘aqov, from aqev, heel: the heel-grasper, later heard as the supplanter. Isaac is sixty, so twenty years married. The Greek names "
   "Rebekah as the mother; the Latin has only the age here, having placed the birth in the previous verse."),
  'shared': ["His brother came out after him.", "His hand grasped Esau’s heel, and he was named Jacob.", "Isaac was sixty years old when they were born."],
  'instructions': [ins(K, S, "Jacob was born holding Esau’s heel when Isaac was sixty."), ins(W, R, "The younger reaches for the elder’s heel at birth; the name records the oracle before the character enacts it.")],
  'entries': ['jacob', 'isaac'],
  'lost': [keeps("An added Rhebekka, “Rebekah,” in the Greek names the mother in the closing clause; Hebrew be-ledet otam, “when she bore them.”"), between("Latin gives only “Isaac was sixty years old when the children were born to him,” the birth having been moved to 25:25; King James follows the Hebrew.")]},

 '25:27': {
  'received': "The boys grew; Esau was a skilled hunter, a man of the field, and Jacob a quiet man who stayed in tents.",
  'explain': ("Two characters: Esau outdoors, Jacob at home. The Hebrew calls Jacob tam, whole, quiet, plain, dwelling in tents; the Greek aplastos, unfeigned, "
   "guileless, dwelling in a house; the Latin simple, in tents. Neither word is a claim of sinlessness, and the next chapters show it."),
  'shared': ["The boys grew up.", "Esau became a skilful hunter, a man of the field.", "Jacob was a quiet man who stayed at home."],
  'instructions': [ins(K, S, "Esau hunted; Jacob kept to the tents."), ins(W, R, "“A plain man” is the narrator’s word for Jacob before the stew and the blessing; the reader is left to weigh it against what he does.")],
  'entries': ['jacob'],
  'lost': [loses("Hebrew ish tam yoshev ohalim, “a whole man dwelling in tents,” becomes Greek anthrōpos aplastos oikōn oikian, “an unfeigned man dwelling in a house”; the tents of the patriarchal life are a house."), between("Latin “a simple man who lived in tents” and King James “a plain man, dwelling in tents” keep the tents.")]},

 '25:28': {
  'received': "Isaac loved Esau for his game; Rebekah loved Jacob.",
  'explain': ("The household divides. The Hebrew idiom is game was in his mouth, Isaac’s taste for Esau’s hunting; the Greek explains, his hunting was food "
   "for him; the Latin because he ate his game. The Hebrew-column rendering was corrected today to the Masoretic idiom."),
  'shared': ["Isaac loved Esau.", "It was because of Esau’s game.", "Rebekah loved Jacob."],
  'instructions': [ins(K, S, "The parents’ love divided between the twins."), ins(W, R, "Isaac’s love has a reason given and Rebekah’s has none; the narrator lets the asymmetry speak.")],
  'entries': ['isaac', 'rebekah', 'jacob'],
  'lost': [between("Hebrew ki-tzayid be-fiv, “for game was in his mouth,” is Greek hē thēra autou brōsis autō, “his hunting was food for him,” a paraphrase; Latin “because he ate his game,” King James “because he did eat of his venison.”")]},

 '25:29': {
  'received': "Jacob was cooking a stew when Esau came in from the field exhausted.",
  'explain': ("The scene for the sale. The versions agree; the Latin came to him."),
  'shared': ["Jacob cooked a stew.", "Esau came in from the field.", "He was exhausted."],
  'instructions': [ins(K, S, "Esau came home famished while Jacob was cooking.")],
  'entries': ['jacob'],
  'lost': [AGREE]},

 '25:30': {
  'received': "Esau begged for the red stuff, since he was exhausted, and so was called Edom.",
  'explain': ("The Hebrew is coarse and doubled: let me gulp that red, that red; the Greek let me taste this red stew; the Latin give me this red stew. "
   "Edom means red, and the name is pinned to the man by his appetite as well as his skin."),
  'shared': ["Esau asked Jacob for the red stew.", "He was exhausted.", "Therefore he was named Edom."],
  'instructions': [ins(K, S, "Esau’s demand for red stew gave him the name Edom."), ins(W, R, "The Hebrew lets Esau speak like a man who cannot wait, and the name of a nation is born of one hungry evening.")],
  'entries': [],
  'lost': [loses("Hebrew hal‘iteni-na min-ha-adom ha-adom ha-zeh, “let me gulp some of the red, the red, this,” with the emphatic doubling and the verb of feeding animals, becomes Greek geuson me apo tou hepsematos tou pyrrou toutou, “let me taste some of this red stew.”"), between("Latin “give me some of this red stew” and King James “feed me … with that same red pottage” lose the doubling.")]},

 '25:31': {
  'received': "Jacob said, Sell me your birthright today.",
  'explain': ("Jacob’s price for stew is the birthright, the double portion and headship of the firstborn. The Hebrew and Greek say today; the Latin omits it."),
  'shared': ["Jacob spoke to Esau.", "Sell me your birthright.", "He wants it now."],
  'instructions': [ins(K, S, "Jacob demanded the birthright in exchange for food."), ins(W, R, "The plain man drives a hard bargain with a starving brother; the oracle will be fulfilled, but not by this.")],
  'entries': ['jacob'],
  'lost': [between("Hebrew ka-yom, “today” or “first,” is Greek sēmeron; Latin omits it; King James “this day.”")]},

 '25:32': {
  'received': "Esau said he was about to die, so what use was a birthright.",
  'explain': ("Esau’s reasoning: I am dying, so the future is worth nothing. The versions agree. Hebrews 12:16 calls this profane."),
  'shared': ["Esau answered.", "He is going to die.", "What good is the birthright to him?"],
  'instructions': [ins(K, S, "Esau dismissed the birthright as useless to a dying man."), ins(W, R, "Esau is not dying, and he knows it; “I am going to die” is appetite talking, and the birthright is sold for an exaggeration.")],
  'entries': [],
  'lost': [AGREE]},

 '25:33': {
  'received': "Jacob made him swear, and Esau sold his birthright to Jacob.",
  'explain': ("An oath binds the sale, as oaths bound Abraham’s servant. The Hebrew and Greek say swear to me today; the Latin then swear to me."),
  'shared': ["Jacob said, Swear to me.", "Esau swore to him.", "He sold his birthright to Jacob."],
  'instructions': [ins(K, S, "Esau swore away his birthright."), ins(W, R, "Jacob secures by oath what he gained by opportunity; the firstborn’s right is bound with the same solemnity Abraham used to find a bride.")],
  'entries': ['jacob'],
  'lost': [between("Hebrew and Greek “swear to me today”; Latin “then swear to me” omits the day; King James “this day.”")]},

 '25:34': {
  'received': "Jacob gave him bread and lentil stew; Esau ate, drank and left, having despised his birthright.",
  'explain': ("The price paid, bread and lentils, and the narrator’s verdict: Esau despised his birthright. The Hebrew, Greek and King James say despised; "
   "the Latin making little of having sold. The stew was red lentils, a common dish."),
  'shared': ["Jacob gave Esau bread and lentil stew.", "Esau ate and drank, rose and went away.", "So Esau despised his birthright."],
  'instructions': [ins(K, S, "Esau traded his birthright for a meal."), ins(W, R, "The narrator judges Esau, not Jacob, in this verse; despising the birthright is the sin named, though Jacob’s dealing is not thereby praised.")],
  'entries': ['jacob'],
  'lost': [between("Hebrew va-yivez Esav et-ha-bekhorah, “and Esau despised the birthright,” is Greek ephaulisen, “made light of”; Latin “making little of having sold his birthright” adds the sale; King James “despised.”")]},
 }
}
