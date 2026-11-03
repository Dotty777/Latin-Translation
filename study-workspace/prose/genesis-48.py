# Study prose for Genesis 48 — Saints Parallel Reader Study Workspace. Draft for review.
K, W, C = 'Knowledge', 'Wisdom', 'Command'
S, R = 'stated', 'reflection'
def ins(t, b, text): return {'type': t, 'basis': b, 'text': text}
def keeps(t): return {'dir': 'keeps', 'text': t}
def loses(t): return {'dir': 'loses', 'text': t}
def between(t): return {'dir': 'between', 'text': t}
AGREE = between("Hebrew, Greek, Latin and King James agree in substance; only the rendering of the divine name and small turns of phrase differ.")

CHAPTER = {
 'slug': 'genesis', 'chapter': 48,
 'chapterNote': (
  "Jacob adopts Joseph’s sons and blesses them with crossed hands, the younger before the elder. The columns agree; the Hebrew keeps El Shaddai, “a company of "
  "peoples,” “to your seed after you,” Paddan, “Rachel died beside me,” “who are these?”, “I had not expected to see your face,” Joseph alone bowing, “for Manasseh "
  "was the firstborn,” “he blessed Joseph,” “before whom my fathers walked,” “who has shepherded me,” “by you Israel will pronounce blessings,” and “one portion.” "
  "The Greek keeps “my God,” “assemblies of nations,” “to you and your seed,” Mesopotamia of Syria, “your mother Rachel,” “the horse-course of Chabratha,” “who are these "
  "to you?”, “I have not been deprived of your face,” “they bowed,” the omission of the firstborn clause, “he blessed them,” “whom my fathers pleased,” “who has nourished "
  "me,” “in you Israel will be blessed,” and “Shechem” as the portion. The Latin and King James follow the Hebrew; the Latin adds “it was springtime” to Rachel’s death "
  "and has Jacob bless “Joseph’s sons.”"),
 'verses': {

 '48:1': {
  'received': "Joseph was told his father was ill, and took his two sons, Manasseh and Ephraim.",
  'explain': ("Choleh, sick, the first illness named in Genesis; death approaches by nature, not violence. The Greek adds and went to Jacob."),
  'shared': ["Joseph was told, Your father is ill.", "He took his two sons with him.", "Manasseh and Ephraim."],
  'instructions': [ins(K, S, "Joseph brought his sons to his dying father."), ins(W, R, "Joseph brings the Egyptian-born sons to the Hebrew deathbed; the boys with the Egyptian mother and priestly grandfather are about to be made Israel.")],
  'entries': [],
  'lost': [keeps("An added kai ēlthen pros Iakōb, “and went to Jacob,” in the Greek."), between("Latin “and set out to go to him” also adds the going; King James ends with the sons.")]},

 '48:2': {
  'received': "Jacob was told Joseph was coming; Israel gathered his strength and sat up in bed.",
  'explain': ("Jacob to Israel in one verse: the sick man becomes the patriarch for the blessing. The Latin says the old man."),
  'shared': ["Jacob was told, Your son Joseph is coming to you.", "Israel gathered his strength.", "He sat up on the bed."],
  'instructions': [ins(K, S, "Jacob roused himself for Joseph."), ins(W, R, "Israel strengthens himself and sits up: the wrestler’s last effort is for a blessing, and the name Israel is used for the act.")],
  'entries': ['jacob'],
  'lost': [between("Latin “The old man was told” for Hebrew va-yagged le-Ya‘aqov, “and it was told to Jacob”; Greek and King James name Jacob and Israel.")]},

 '48:3': {
  'received': "Jacob said: El Shaddai appeared to me at Luz in Canaan and blessed me,",
  'explain': ("Bethel, by its old name Luz, and the vision of 35:9–12. The Hebrew says El Shaddai; the Greek my God; the Latin God Almighty."),
  'shared': ["Jacob said to Joseph.", "God Almighty appeared to me at Luz in the land of Canaan.", "He blessed me."],
  'instructions': [ins(K, S, "Jacob recalled God’s blessing at Bethel."), ins(W, R, "The dying man goes back to Luz, the place of the stair and the vow; the blessing he is about to give he first received, and he says so.")],
  'entries': ['jacob', 'el-shaddai', 'bethel', 'canaan'],
  'lost': [loses("Hebrew El Shaddai becomes Greek ho theos mou, “my God.”"), between("Latin “God Almighty” and King James “God Almighty” keep the title.")]},

 '48:4': {
  'received': "and said, I will make you fruitful and multiply you into a company of peoples, and give this land to your seed after you for ever.",
  'explain': ("The words of 35:11–12 recalled. The Hebrew says a company of peoples, to your seed; the Greek assemblies of nations, to you and your seed; the Latin multitude of peoples, to you and your offspring."),
  'shared': ["I will make you fruitful and multiply you.", "I will make you a company of peoples.", "I will give this land to your seed after you as an everlasting possession."],
  'instructions': [ins(K, S, "Jacob recited the promise of land and people."), ins(W, R, "An everlasting possession, recited in Egypt by a man who will be buried there for a season; the promise is the only land Jacob has, and he hands it on.")],
  'entries': [],
  'lost': [keeps("Greek soi kai tō spermati sou, “to you and your seed,” for Hebrew le-zar‘akha, “to your seed”; Hebrew qehal ammim, “a company of peoples,” is Greek synagōgas ethnōn, “assemblies of nations.”"), between("Latin “to you and your offspring … a multitude of peoples,” King James “to thy seed … a multitude of people.”")]},

 '48:5': {
  'received': "Your two sons born in Egypt before I came are mine; Ephraim and Manasseh shall be mine like Reuben and Simeon.",
  'explain': ("Adoption: Joseph’s sons become tribes, Joseph receiving the double portion of the firstborn through them. Ephraim named first already. The versions agree."),
  'shared': ["Your two sons born to you in Egypt before I came to you are mine.", "Ephraim and Manasseh shall be mine.", "Like Reuben and Simeon."],
  'instructions': [ins(K, S, "Jacob adopted Ephraim and Manasseh as his own sons."), ins(W, R, "Joseph gets the firstborn’s double share by having his two sons made tribes; Reuben lost it by Bilhah, and Jacob gives it quietly to Rachel’s son.")],
  'entries': ['egypt'],
  'lost': [AGREE]},

 '48:6': {
  'received': "Children born to you after them are yours; they shall be reckoned under their brothers’ names in their inheritance.",
  'explain': ("No third tribe: later sons fall under Ephraim and Manasseh. The versions agree."),
  'shared': ["Children you beget after them are yours.", "They shall be called by their brothers’ names.", "In their inheritance."],
  'instructions': [ins(K, S, "Later sons of Joseph would count under the two tribes.")],
  'entries': [],
  'lost': [AGREE]},

 '48:7': {
  'received': "When I came from Paddan, Rachel died beside me in Canaan, some way from Ephrath, and I buried her on the way to Ephrath, Bethlehem.",
  'explain': ("Jacob explains the adoption by Rachel: her sons’ sons are his because she died with only two. The Hebrew says Paddan, Rachel; the Greek Mesopotamia of Syria, your mother Rachel, the horse-course of Chabratha; the Latin it was springtime."),
  'shared': ["When I came from Paddan, Rachel died beside me in Canaan on the journey.", "There was still some distance to Ephrath.", "I buried her on the way to Ephrath, which is Bethlehem."],
  'instructions': [ins(K, S, "Jacob recalled Rachel’s death and burial."), ins(W, R, "Rachel’s death comes into the blessing unbidden; Jacob is adopting her grandsons because she had so few sons, and the old grief explains the legal act.")],
  'entries': ['canaan'],
  'lost': [keeps("Greek Rhachēl hē mētēr sou, “Rachel your mother,” adds the relation; Hebrew kivrat-eretz, “a stretch of land,” is Greek kata ton hippodromon Chabratha, “at the horse-course of Chabratha,” and the Greek adds tēs Syrias, “of Syria.”"), between("Latin “and it was springtime” adds; King James “Padan … but a little way to come unto Ephrath.”")]},

 '48:8': {
  'received': "Israel saw Joseph’s sons and asked, Who are these?",
  'explain': ("Dim-eyed, he asks, as Isaac asked who are you. The Greek adds to you."),
  'shared': ["Israel saw Joseph’s sons.", "He said.", "Who are these?"],
  'instructions': [ins(K, S, "Jacob asked who the boys were."), ins(W, R, "“Who are these?” from a blind old man about to bless: the scene of chapter 27 returns with the roles changed, and this time the blind man will choose the younger on purpose.")],
  'entries': [],
  'lost': [keeps("An added soi, “to you,” in the Greek: “who are these to you?”"), between("Hebrew, Latin and King James “Who are these?”")]},

 '48:9': {
  'received': "Joseph said, My sons, whom God gave me here. Bring them to me, he said, that I may bless them.",
  'explain': ("Whom God gave me here, in Egypt. The Hebrew says please; the Greek names Jacob."),
  'shared': ["They are my sons, whom God has given me here.", "Bring them to me.", "That I may bless them."],
  'instructions': [ins(K, S, "Joseph presented his sons for blessing.")],
  'entries': ['elohim'],
  'lost': [between("Hebrew qachem-na, “please take them,” is Greek prosagage moi autous, with Iakōb added as speaker; Latin “He said,” King James “Bring them, I pray thee.”")]},

 '48:10': {
  'received': "Israel’s eyes were dim with age and he could not see; Joseph brought them near, and he kissed and embraced them.",
  'explain': ("As Isaac’s eyes were dim in 27:1. The Greek names Joseph as bringing them; the Latin could not see clearly."),
  'shared': ["Israel’s eyes were dim with age; he could not see.", "They were brought near to him.", "He kissed and embraced them."],
  'instructions': [ins(K, S, "Blind Jacob embraced Joseph’s sons.")],
  'entries': [],
  'lost': [between("Greek adds Iōsēph as subject of “brought them near”; Latin “could not see clearly … When they were brought to him”; Hebrew and King James “he brought them near.”")]},

 '48:11': {
  'received': "Israel said to Joseph: I never expected to see your face, and now God has shown me your children too.",
  'explain': ("Lo fillalti, I had not judged, expected. The Greek says I have not been deprived of your face; the Latin not deprived of seeing you."),
  'shared': ["Israel said to Joseph.", "I had not expected to see your face.", "Now God has shown me your seed as well."],
  'instructions': [ins(K, S, "Jacob marvelled at seeing Joseph and his sons."), ins(W, R, "“I had not thought to see your face”: twenty-two years of mourning in a clause, and then grandchildren. God shows the old man more than he asked.")],
  'entries': ['elohim'],
  'lost': [between("Hebrew re’oh fanekha lo fillalti, “to see your face I had not expected,” is Greek tou prosōpou sou ouk esterēthēn, “of your face I have not been deprived”; Latin “I have not been deprived of seeing you,” King James “I had not thought to see thy face.”")]},

 '48:12': {
  'received': "Joseph took them from his knees and bowed with his face to the ground.",
  'explain': ("From between his knees, the adoption gesture. The Hebrew says Joseph bowed; the Greek they bowed; the Latin his father’s lap."),
  'shared': ["Joseph brought them out from between his knees.", "There was a bow.", "Face to the ground."],
  'instructions': [ins(K, S, "Joseph bowed before his father."), ins(W, R, "The lord of Egypt bows to the ground before a blind shepherd; the sheaves have bowed to Joseph, and Joseph bows to Israel.")],
  'entries': [],
  'lost': [loses("Hebrew va-yishtachu le-appav, “and he bowed with his face,” Joseph, becomes Greek kai prosekynēsan autō epi prosōpon, “and they bowed to him with their faces,” the sons."), between("Latin “Joseph took them from his father’s lap and bowed” and King James “he bowed himself” keep Joseph.")]},

 '48:13': {
  'received': "Joseph took Ephraim in his right toward Israel’s left and Manasseh in his left toward Israel’s right, and brought them near.",
  'explain': ("Arranged so the right hand falls on the firstborn. The versions agree."),
  'shared': ["Joseph took them both.", "Ephraim with his right hand toward Israel’s left, Manasseh with his left toward Israel’s right.", "He brought them close to him."],
  'instructions': [ins(K, S, "Joseph positioned the boys by birth order."), ins(W, R, "Joseph arranges the sons so the right hand will fall correctly; the man who read Pharaoh’s dreams expects the blessing to follow the seating plan.")],
  'entries': [],
  'lost': [AGREE]},

 '48:14': {
  'received': "Israel crossed his hands, putting his right on Ephraim’s head, the younger, and his left on Manasseh’s, though Manasseh was the firstborn.",
  'explain': ("Sikkel, crossed, or guided wittingly; the blind man knows what he does. The Greek lacks for Manasseh was the firstborn; the Latin who was older."),
  'shared': ["Israel stretched out his right hand on Ephraim’s head, though he was the younger.", "His left hand on Manasseh’s head.", "He crossed his hands."],
  'instructions': [ins(K, S, "Jacob deliberately crossed his hands."), ins(W, R, "Jacob, who got his blessing by a trick on a blind father, gives his with open eyes crossed: the younger over the elder, on purpose. The oracle of 25:23 is now a policy.")],
  'entries': [],
  'lost': [loses("Hebrew ki Menashsheh ha-bekhor, “for Manasseh was the firstborn,” is absent from the Greek."), between("Latin “Manasseh’s head, who was older” and King James “for Manasseh was the firstborn” keep it.")]},

 '48:15': {
  'received': "He blessed Joseph: The God before whom my fathers Abraham and Isaac walked, the God who has shepherded me all my life,",
  'explain': ("Blessing the sons blesses Joseph. God as shepherd, the first time in Scripture. The Hebrew says blessed Joseph, walked, shepherded; the Greek blessed them, pleased, nourished; the Latin Joseph’s sons."),
  'shared': ["He blessed Joseph.", "The God before whom my fathers Abraham and Isaac walked.", "The God who has shepherded me all my life to this day."],
  'instructions': [ins(K, S, "Jacob invoked the God of his fathers who had shepherded him."), ins(W, R, "“The God who shepherded me”: the shepherd of Laban’s flocks calls God his shepherd, before David does. The man knows what the word costs and gives it to God.")],
  'entries': ['abraham', 'isaac', 'elohim'],
  'lost': [loses("Hebrew va-yevarekh et-Yosef, “and he blessed Joseph,” becomes Greek kai eulogēsen autous, “and he blessed them”; Hebrew hithallekhu lefanav, “walked before Him,” becomes euērestēsan enantion autou, “pleased before Him”; Hebrew ha-ro‘eh oti, “who shepherds me,” becomes ho trephōn me, “who nourishes me.”"), between("Latin “Jacob blessed Joseph’s sons … walked … fed me” mixes; King James “blessed Joseph … did walk … fed me.”")]},

 '48:16': {
  'received': "the Angel who redeemed me from all evil, bless the boys; let my name and my fathers’ names be carried on in them, and let them grow into a multitude in the earth.",
  'explain': ("The Angel, the one who wrestled or the one of Bethel, named with God in one blessing. Redeemed, ga’al, the first use. The Greek says delivers, will be called, a great multitude."),
  'shared': ["The Angel who redeemed me from all evil, bless the boys.", "Let my name and the name of my fathers Abraham and Isaac be carried on in them.", "Let them grow into a multitude in the midst of the earth."],
  'instructions': [ins(K, S, "Jacob blessed the boys by God and the redeeming Angel."), ins(W, R, "God, God, the Angel: three names in one blessing, and one verb, bless. Jacob’s theology at the end is the wrestler’s: the One who met him at the Jabbok is the One who redeems.")],
  'entries': ['angel-of-the-lord', 'abraham', 'isaac'],
  'lost': [between("Hebrew ha-go’el oti, “who redeemed me,” is Greek ho rhyomenos me, “who delivers me,” present; Hebrew ve-yiqqare vahem shemi, “and let my name be called in them,” is Greek kai epiklēthēsetai … to onoma mou, “and my name will be called”; Greek adds polla, “great,” to the multitude; Latin “rescued … may my name and the names of my fathers be called upon them,” King James “redeemed … let my name be named on them.”")]},

 '48:17': {
  'received': "Joseph was displeased to see the right hand on Ephraim and took his father’s hand to move it to Manasseh.",
  'explain': ("Joseph corrects his father, as no one corrected Isaac. The versions agree."),
  'shared': ["Joseph saw his father’s right hand on Ephraim’s head and was displeased.", "He took his father’s hand.", "He meant to move it from Ephraim’s head to Manasseh’s."],
  'instructions': [ins(K, S, "Joseph tried to correct the crossed hands."), ins(W, R, "Joseph, the younger son exalted over his brothers, wants the elder honoured; he does not see that he is himself the pattern Jacob is following.")],
  'entries': [],
  'lost': [AGREE]},

 '48:18': {
  'received': "Not so, father, Joseph said; this is the firstborn, put your right hand on him.",
  'explain': ("The versions agree; the Latin this is not fitting."),
  'shared': ["Not so, my father!", "This one is the firstborn.", "Place your right hand on his head."],
  'instructions': [ins(K, S, "Joseph protested for Manasseh’s right.")],
  'entries': [],
  'lost': [AGREE]},

 '48:19': {
  'received': "His father refused: I know, my son, I know. He too shall be a people and be great, but his younger brother shall be greater, and his seed a multitude of nations.",
  'explain': ("I know, I know: the blindness is of the eyes only. Ephraim will be the leading northern tribe, its name a name for Israel. The Greek says exalted, child; the Latin peoples, multiply."),
  'shared': ["I know, my son, I know.", "He too will become a people and be great.", "But his younger brother will be greater, and his seed a multitude of nations."],
  'instructions': [ins(K, S, "Jacob knowingly preferred Ephraim."), ins(W, R, "“I know, my son, I know”: Jacob has lived the younger-over-elder choice from the womb, and makes it now with full knowledge. The blind see here, and the seeing are corrected.")],
  'entries': [],
  'lost': [between("Hebrew yigdal, “he will be great,” is Greek hypsōthēsetai, “he will be exalted”; Hebrew beni, “my son,” is Greek teknon, “child”; Latin “shall become peoples and shall multiply,” King James “shall be great.”")]},

 '48:20': {
  'received': "He blessed them that day: By you Israel will bless, saying, May God make you like Ephraim and Manasseh. So he set Ephraim before Manasseh.",
  'explain': ("A blessing formula for Israel, Ephraim first. The Hebrew says by you Israel will bless, active; the Greek and Latin in you Israel will be blessed, passive."),
  'shared': ["He blessed them that day.", "May God make you like Ephraim and Manasseh.", "He placed Ephraim before Manasseh."],
  'instructions': [ins(K, S, "Jacob set Ephraim before Manasseh in Israel’s blessing."), ins(W, R, "Israel will bless its sons by these two names, and the younger first; the order of the crossed hands is written into the nation’s speech.")],
  'entries': ['elohim'],
  'lost': [loses("Hebrew bekha yevarekh Yisra’el, “by you Israel will bless,” active, becomes Greek en hymin eulogēthēsetai Israēl, “in you Israel will be blessed,” passive."), between("Latin “In you Israel shall be blessed” follows the Greek; King James “In thee shall Israel bless.”")]},

 '48:21': {
  'received': "Israel said to Joseph: I am dying, but God will be with you and bring you back to the land of your fathers.",
  'explain': ("You, plural: Joseph’s people. The promise of 46:4 handed to the next generation. The versions agree."),
  'shared': ["Behold, I am about to die.", "God will be with you.", "He will bring you back to the land of your fathers."],
  'instructions': [ins(K, S, "Jacob promised God’s return of the family to Canaan."), ins(W, R, "“God will bring you back”: said to the lord of Egypt, who has every reason to stay. The exodus is promised at a deathbed to the man least likely to want it, and Joseph will ask for it in his own last words.")],
  'entries': ['elohim'],
  'lost': [AGREE]},

 '48:22': {
  'received': "I give you one portion above your brothers, which I took from the Amorite with my sword and bow.",
  'explain': ("Shekhem achad, one shoulder, one portion, or Shechem, where Joseph will be buried, Joshua 24:32. The Hebrew keeps the ambiguity; the Greek says Shechem as a choice portion; the Latin and King James one portion. Jacob’s sword and bow: the city his sons took."),
  'shared': ["I give you one portion beyond your brothers.", "I took it from the Amorite.", "With my sword and my bow."],
  'instructions': [ins(K, S, "Jacob gave Joseph an extra portion, Shechem."), ins(W, R, "Shechem, taken by Simeon and Levi’s swords and claimed here as Jacob’s own, is given to Joseph; the field bought in 33:19 and seized in 34 becomes Joseph’s grave, and the chapter closes on the land.")],
  'entries': [],
  'lost': [loses("Hebrew shekhem achad, “one shoulder,” a portion, with a play on the city, becomes Greek Sikima exaireton, “Shechem as a choice portion,” the city named outright; Hebrew ha-Emori, “the Amorite,” Greek Amorraiōn, plural."), between("Latin “one portion … from the hand of the Amorite” and King James “one portion above thy brethren” keep the common noun.")]},
 }
}
