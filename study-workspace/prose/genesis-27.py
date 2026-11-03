# Study prose for Genesis 27 — Saints Parallel Reader Study Workspace. Draft for review.
K, W, C = 'Knowledge', 'Wisdom', 'Command'
S, R = 'stated', 'reflection'
def ins(t, b, text): return {'type': t, 'basis': b, 'text': text}
def keeps(t): return {'dir': 'keeps', 'text': t}
def loses(t): return {'dir': 'loses', 'text': t}
def between(t): return {'dir': 'between', 'text': t}
AGREE = between("Hebrew, Greek, Latin and King James agree in substance; only the rendering of the divine name and small turns of phrase differ.")

CHAPTER = {
 'slug': 'genesis', 'chapter': 27,
 'chapterNote': (
  "The stolen blessing. Every column tells the same deception: Isaac blind, Rebekah’s plan, the goatskins, the voice of Jacob and the hands of Esau, "
  "the blessing given, Esau’s cry, the lesser blessing, the plot to kill, the flight to Haran. The Hebrew keeps “go out to the field,” “the smooth part of "
  "his neck” echoing Jacob’s own word for himself, “a field which YHWH has blessed” without an adjective, “peoples … nations … your brothers … your mother’s "
  "sons,” Isaac who “trembled violently,” “Esau hated Jacob,” and Esau “consoling himself” with murder. The Greek keeps “the plain,” Jacob called “her younger "
  "son” and “his son” in the narration, “tender” goats, “loaves,” an “abundant” field, “nations … rulers … your brother … your father’s sons,” Isaac “utterly "
  "astonished,” an added “Isaac was deeply moved” in 27:38, “Mesopotamia” in the flight, and the fury-and-anger clause split across 27:44–45. Three Hebrew-column "
  "renderings were corrected today to the Masoretic wording. The Latin and King James follow the Hebrew; the Latin reads Esau’s blessing in 27:39 positively, "
  "“in the richness of the earth,” where Hebrew and Greek can be read “away from.”"),
 'verses': {

 '27:1': {
  'received': "Isaac, old and blind, called his elder son Esau, who answered, Here I am.",
  'explain': ("Isaac’s eyes have failed; the blindness is the condition of everything that follows. He calls the elder son by right of birth to receive the blessing. "
   "The versions agree; the Latin makes my son a question."),
  'shared': ["Isaac was old and his eyes were dim.", "He called Esau his older son.", "Esau answered, Here I am."],
  'instructions': [ins(K, S, "Blind Isaac summoned Esau."), ins(W, R, "The father who cannot see is about to be deceived by touch, smell and taste; the chapter is a study in senses that mislead.")],
  'entries': ['isaac'],
  'lost': [AGREE]},

 '27:2': {
  'received': "Isaac said he was old and did not know the day of his death.",
  'explain': ("Isaac is about a hundred and thirty-seven, and will live another forty-three years; the fear of death prompts a premature blessing. The versions agree."),
  'shared': ["Isaac has grown old.", "He does not know the day of his death.", "He wants to settle matters."],
  'instructions': [ins(K, S, "Isaac prepared to bless before he died."), ins(W, R, "Not knowing the day of death is given as a reason to act; Isaac is right about mortality and wrong, as the oracle warned, about the heir.")],
  'entries': ['isaac'],
  'lost': [AGREE]},

 '27:3': {
  'received': "He told Esau to take his quiver and bow, go to the field and hunt game for him.",
  'explain': ("The blessing is to be preceded by a meal of game, Esau’s gift. The Hebrew says go out to the field; the Greek into the plain, its regular word for field "
   "in these chapters. The Hebrew-column rendering was corrected today."),
  'shared': ["Take your hunting gear, quiver and bow.", "Go out to the field.", "Hunt game for me."],
  'instructions': [ins(C, S, "Take your weapons, go to the field and hunt game for me."), ins(K, S, "Isaac sent Esau hunting before the blessing.")],
  'entries': [],
  'lost': [between("Hebrew ve-tze ha-sadeh, “go out to the field,” is Greek exelthe eis to pedion, “go out into the plain”; Latin “go out” without the place; King James “go out to the field.”")]},

 '27:4': {
  'received': "Make me a savoury dish as I like it, that I may eat and bless you before I die.",
  'explain': ("Savoury food, matammim, and the blessing of the soul: the formula will recur six times. The versions agree."),
  'shared': ["Prepare a savoury meal such as I like.", "Bring it so I may eat.", "Then my soul may bless you before I die."],
  'instructions': [ins(C, S, "Prepare a savoury meal and bring it to me."), ins(W, R, "The blessing is tied to a meal; Isaac who loved Esau for his game makes the game the gate to the inheritance.")],
  'entries': [],
  'lost': [AGREE]},

 '27:5': {
  'received': "Rebekah overheard, and Esau went to hunt.",
  'explain': ("Rebekah listens and Esau goes; the plot has its opening. The Greek says to procure game for his father and names Isaac speaking to Esau; the Latin to fulfil his father’s command."),
  'shared': ["Rebekah heard Isaac speaking to Esau.", "Esau went out to the field.", "He went to hunt game and bring it."],
  'instructions': [ins(K, S, "Rebekah overheard Isaac’s plan."), ins(W, R, "Rebekah knows the oracle of 25:23 and acts on it; the question the chapter never answers is whether she was meant to.")],
  'entries': ['rebekah', 'isaac'],
  'lost': [keeps("An added tō patri autou, “for his father,” in the Greek; Hebrew latzud tzayid le-havi, “to hunt game to bring.”"), between("Latin “to fulfil his father’s command” paraphrases; King James follows the Hebrew.")]},

 '27:6': {
  'received': "Rebekah told Jacob she had heard his father speaking to Esau.",
  'explain': ("She reports to the son she loves. The Greek calls Jacob her younger son; the Hebrew her son; the Latin her son Jacob."),
  'shared': ["Rebekah spoke to Jacob her son.", "I heard your father speaking.", "He spoke to Esau your brother."],
  'instructions': [ins(K, S, "Rebekah recruited Jacob.")],
  'entries': ['rebekah', 'jacob'],
  'lost': [keeps("An added ton elassō, “the younger,” after her son in the Greek."), between("Latin and King James “her son.”")]},

 '27:7': {
  'received': "Bring me game and make a savoury meal, that I may eat and bless you before the Lord before I die.",
  'explain': ("Rebekah quotes Isaac and adds before the Lord, raising the stakes: the blessing is a sacred act. The versions agree."),
  'shared': ["Bring me game and make me a savoury meal.", "I will eat and bless you.", "It is before the Lord, before I die."],
  'instructions': [ins(K, S, "Rebekah reported Isaac’s intent to bless Esau before the Lord.")],
  'entries': ['yhwh-yahweh'],
  'lost': [AGREE]},

 '27:8': {
  'received': "Now, my son, obey my voice in what I command you.",
  'explain': ("A mother’s command to deceive, in the words God used of Abraham’s obedience in 26:5, obey my voice. The Latin says follow my counsel."),
  'shared': ["Now therefore, my son.", "Obey my voice.", "Do what I command you."],
  'instructions': [ins(K, S, "Rebekah demanded Jacob’s obedience."), ins(W, R, "“Obey my voice” was the ground of Abraham’s blessing; here it is the ground of a fraud. The same words serve faith and scheming.")],
  'entries': ['rebekah'],
  'lost': [between("Hebrew shema be-qoli la-asher ani metzavvah otakh, “obey my voice in what I command you,” is Greek akouson mou kathа egō soi entellomai; Latin “follow my counsel” softens; King James “obey my voice.”")]},

 '27:9': {
  'received': "Go to the flock, bring two good kids, and I will make the savoury meal your father likes.",
  'explain': ("Goat for game; Rebekah knows she can cook to deceive. The Greek says tender and good; the Hebrew good; the Latin choice."),
  'shared': ["Go to the flock.", "Bring me two good young goats.", "I will make them into a savoury meal as your father likes."],
  'instructions': [ins(K, S, "Rebekah planned to pass goat off as game.")],
  'entries': [],
  'lost': [keeps("An added hapalous, “tender,” before good in the Greek."), between("Latin “two choice young goats,” King James “two good kids.”")]},

 '27:10': {
  'received': "You will bring it to your father to eat, so that he blesses you before he dies.",
  'explain': ("The purpose stated plainly: the blessing, taken by substitution. The versions agree."),
  'shared': ["You shall bring it to your father.", "He will eat it.", "He may bless you before he dies."],
  'instructions': [ins(K, S, "The aim was to obtain Isaac’s blessing for Jacob.")],
  'entries': [],
  'lost': [AGREE]},

 '27:11': {
  'received': "Jacob objected that Esau was hairy and he was smooth.",
  'explain': ("Jacob’s objection is practical, not moral: the plan may fail. Smooth, chalaq, also means slippery, and the word will echo in verse 16. The Latin says you know."),
  'shared': ["Jacob spoke to his mother Rebekah.", "Esau my brother is a hairy man.", "I am a smooth man."],
  'instructions': [ins(K, S, "Jacob feared the deception would be detected."), ins(W, R, "Jacob worries about being caught, not about the lie; his conscience, like his skin, is smooth.")],
  'entries': ['jacob', 'rebekah'],
  'lost': [between("Latin “you know that my brother Esau is hairy” adds the appeal; Hebrew, Greek and King James name Jacob and Rebekah.")]},

 '27:12': {
  'received': "If his father felt him he would seem a mocker and bring a curse, not a blessing.",
  'explain': ("The risk named. The Hebrew says I will seem to be mocking him; the Greek I shall appear as one who treats him with contempt; the Latin he will think I intended to mock; the King James as a deceiver."),
  'shared': ["Perhaps my father will feel me.", "I will seem to him a mocker.", "I will bring a curse on myself, not a blessing."],
  'instructions': [ins(K, S, "Jacob weighed the risk of a curse.")],
  'entries': [],
  'lost': [between("Hebrew ki-meta‘tea, “as a mocker,” is Greek hōs kataphronōn, “as one despising”; Latin “intended to mock,” King James “as a deceiver.”")]},

 '27:13': {
  'received': "His mother said, Let your curse be on me; only obey me and fetch them.",
  'explain': ("Rebekah takes the curse on herself, as Judah will later offer himself for Benjamin. The versions agree; the Latin bring what I have said."),
  'shared': ["Upon me be your curse, my son.", "Only obey my voice.", "Go and bring them to me."],
  'instructions': [ins(K, S, "Rebekah took the risk of the curse on herself."), ins(W, R, "She offers to bear the curse and in the end bears a lesser one: she never sees Jacob again after he flees. The chapter does not say so, but Genesis does.")],
  'entries': ['rebekah'],
  'lost': [AGREE]},

 '27:14': {
  'received': "He fetched the kids and his mother made the savoury meal as his father liked it.",
  'explain': ("Jacob obeys. The versions agree."),
  'shared': ["He went and took them and brought them to his mother.", "His mother prepared a savoury meal.", "It was as his father liked it."],
  'instructions': [ins(K, S, "The meal was prepared for the deception.")],
  'entries': [],
  'lost': [AGREE]},

 '27:15': {
  'received': "Rebekah dressed Jacob in Esau’s best garments, which she kept in the house.",
  'explain': ("Esau’s clothes, with Esau’s smell, from the mother’s keeping; a hunter’s garments would smell of the field. The versions agree; the Latin uses pronouns."),
  'shared': ["Rebekah took the best garments of Esau her older son.", "They were with her in the house.", "She put them on Jacob her younger son."],
  'instructions': [ins(K, S, "Jacob wore Esau’s clothes.")],
  'entries': ['rebekah', 'jacob'],
  'lost': [AGREE]},

 '27:16': {
  'received': "She put the goatskins on his hands and on the smooth of his neck.",
  'explain': ("The disguise completed with kidskin. The Hebrew says hands, and the smooth part of his neck, chelqat, echoing Jacob’s chalaq of verse 11; the Greek arms, the bare parts; the Latin hands, the bare part."),
  'shared': ["She put the skins of the kids on him.", "They went on his hands.", "They covered the smooth part of his neck."],
  'instructions': [ins(K, S, "Goatskins disguised Jacob’s smooth skin."), ins(W, R, "The smooth man is covered in a goat’s hide; the disguise is as crude as it is successful, because the one who must judge it is blind.")],
  'entries': [],
  'lost': [loses("Hebrew al-yadav … chelqat tzavvarav, “on his hands … the smooth part of his neck,” becomes Greek epi tous brachionas … ta gymna tou trachēlou, “on his arms … the bare parts of his neck”; the echo of chalaq, “smooth,” in 27:11 is lost."), between("Latin “hands … the bare part” and King James “hands … the smooth of his neck” keep the hands.")]},

 '27:17': {
  'received': "She handed the meal and the bread to Jacob.",
  'explain': ("The props are passed. The Hebrew says the bread; the Greek the loaves; the Latin she gave him the dish and the bread she had baked. The Hebrew-column rendering was corrected today."),
  'shared': ["She gave the savoury meal.", "She gave the bread she had prepared.", "She gave them into Jacob’s hands."],
  'instructions': [ins(K, S, "Rebekah sent Jacob in with the meal.")],
  'entries': ['jacob'],
  'lost': [between("Hebrew ve-et-ha-lechem, “and the bread,” is Greek kai tous artous, “and the loaves”; Latin and King James singular.")]},

 '27:18': {
  'received': "He came to his father and said, My father; Isaac said, Here I am; who are you, my son?",
  'explain': ("The first question Jacob must lie to. The Greek says he brought them to his father; the Latin Isaac answers I hear you."),
  'shared': ["He came to his father.", "He said, My father.", "Isaac said, Here I am; who are you, my son?"],
  'instructions': [ins(K, S, "Isaac asked which son had come."), ins(W, R, "“Who are you, my son?” is the question Jacob will spend twenty years answering; at the Jabbok a stranger will ask his name.")],
  'entries': ['isaac'],
  'lost': [between("Greek eisēnegken tō patri autou, “he brought them in to his father,” for Hebrew va-yavo el-aviv, “he came to his father”; Latin “I hear you” for “Here I am.”")]},

 '27:19': {
  'received': "Jacob said, I am Esau your firstborn; I have done as you said; sit up and eat my game, that your soul may bless me.",
  'explain': ("The lie in full: name, status, obedience, game. The versions agree. Jacob speaks the words, and the narrator calls him Jacob while he does."),
  'shared': ["I am Esau your firstborn.", "I have done as you told me.", "Arise, sit and eat of my game, so that your soul may bless me."],
  'instructions': [ins(K, S, "Jacob lied that he was Esau."), ins(W, R, "“I am Esau” is the first of three lies in six verses; the man who will be renamed Israel begins by taking another’s name.")],
  'entries': ['jacob'],
  'lost': [AGREE]},

 '27:20': {
  'received': "Isaac asked how he had found game so quickly; Jacob said the Lord your God had brought it to him.",
  'explain': ("The second lie invokes God. Your God, not my God; Jacob keeps a distance even in blasphemy. The Hebrew says brought it before me; the Greek placed it before me; the Latin it was God’s will."),
  'shared': ["How did you find it so quickly, my son?", "Jacob answered.", "Because the Lord your God brought it to me."],
  'instructions': [ins(K, S, "Jacob credited God with his supposed speed."), ins(W, R, "The deceiver cites providence for a lie; the narrator reports it without comment, and the reader is left to feel the chill.")],
  'entries': ['jacob', 'yhwh-yahweh'],
  'lost': [between("Hebrew hiqrah YHWH Elohekha lefanai, “YHWH your God caused it to happen before me,” is Greek paredōken kyrios ho theos sou enantion mou, “the Lord your God delivered it before me”; Latin “it was God’s will that what I wanted should meet me quickly” paraphrases; King James “the LORD thy God brought it to me.”")]},

 '27:21': {
  'received': "Isaac said, Come near and let me feel you, to know whether you are really Esau.",
  'explain': ("Suspicion; touch is to settle what voice has unsettled. The versions agree."),
  'shared': ["Draw near to me.", "I will feel you, my son.", "Are you truly my son Esau or not?"],
  'instructions': [ins(K, S, "Isaac tested the claim by touch.")],
  'entries': ['isaac'],
  'lost': [AGREE]},

 '27:22': {
  'received': "Jacob came near; Isaac felt him and said, The voice is Jacob’s, but the hands are Esau’s.",
  'explain': ("The famous sentence. Isaac hears the truth and touches the lie, and trusts the touch. The versions agree."),
  'shared': ["Jacob drew near to his father Isaac.", "Isaac felt him.", "The voice is Jacob’s voice, but the hands are the hands of Esau."],
  'instructions': [ins(K, S, "Isaac noticed the voice but trusted the hands."), ins(W, R, "The voice tells the truth and the hands lie; Isaac believes his hands. Faith, Paul says, comes by hearing.")],
  'entries': ['jacob', 'isaac'],
  'lost': [AGREE]},

 '27:23': {
  'received': "He did not recognise him, because his hands were hairy like Esau’s, so he blessed him.",
  'explain': ("The disguise works. The narrator gives the reason and the result in one breath. The versions agree; the Latin runs on into the next verse."),
  'shared': ["He did not recognise him.", "His hands were hairy like his brother Esau’s.", "So he blessed him."],
  'instructions': [ins(K, S, "Isaac was deceived and blessed Jacob.")],
  'entries': ['isaac'],
  'lost': [AGREE]},

 '27:24': {
  'received': "He asked, Are you my son Esau? and Jacob said, I am.",
  'explain': ("The third lie, two words. The versions agree."),
  'shared': ["Are you my son Esau?", "He answered.", "I am."],
  'instructions': [ins(K, S, "Jacob affirmed the lie a third time."), ins(W, R, "Isaac asks once more, and Jacob does not take the exit; the deception is now wholly his.")],
  'entries': ['jacob'],
  'lost': [AGREE]},

 '27:25': {
  'received': "Isaac ate the game and drank the wine Jacob brought.",
  'explain': ("The meal, with wine the plan did not mention. The Hebrew says I will eat of my son’s game; the Greek of your game, my son; the Latin compresses."),
  'shared': ["Bring it near and I will eat, so that my soul may bless you.", "He brought it and Isaac ate.", "He brought him wine and he drank."],
  'instructions': [ins(K, S, "Isaac ate and drank before blessing.")],
  'entries': ['isaac'],
  'lost': [between("Hebrew mi-tzeid beni, “of my son’s game,” is Greek apo tēs thēras sou, teknon, “of your game, child”; Latin “from your game, my son”; King James “of my son’s venison.”")]},

 '27:26': {
  'received': "Isaac said, Come near and kiss me, my son.",
  'explain': ("The last test is smell, through a kiss. The versions agree."),
  'shared': ["Isaac his father spoke.", "Draw near to me.", "Kiss me, my son."],
  'instructions': [ins(K, S, "Isaac asked for a kiss.")],
  'entries': ['isaac'],
  'lost': [AGREE]},

 '27:27': {
  'received': "He kissed him; Isaac smelled his garments and blessed him: the smell of my son is like a field the Lord has blessed.",
  'explain': ("Esau’s clothes carry the field, and the blessing begins from the smell. The Hebrew says a field which YHWH has blessed; the Greek an abundant field; the Latin a full field."),
  'shared': ["He came near and kissed him.", "Isaac smelled his garments and blessed him.", "The smell of my son is like the smell of a field the Lord has blessed."],
  'instructions': [ins(K, S, "Isaac blessed Jacob, deceived by Esau’s clothes."), ins(W, R, "The blessing is drawn out by a borrowed smell; Jacob receives in another’s garments what he will spend his life learning to wear as his own.")],
  'entries': ['jacob', 'isaac', 'yhwh-yahweh'],
  'lost': [keeps("An added plērous, “full,” before field in the Greek."), between("Latin “a full field” follows the Greek; King James “a field which the LORD hath blessed” the Hebrew.")]},

 '27:28': {
  'received': "May God give you the dew of heaven, the fat of the earth, and plenty of grain and wine.",
  'explain': ("The blessing of the land: dew, fatness, grain, wine. The versions agree."),
  'shared': ["May God give you the dew of heaven.", "May He give the richness of the earth.", "May He give abundant grain and wine."],
  'instructions': [ins(K, S, "Isaac blessed Jacob with the land’s fertility."), ins(W, R, "Dew and fatness are the gifts of Canaan; the blessing is tied to the land as the promise was.")],
  'entries': ['jacob'],
  'lost': [AGREE]},

 '27:29': {
  'received': "May peoples serve you and nations bow to you; be lord over your brothers; cursed be those who curse you, blessed those who bless you.",
  'explain': ("Dominion and the Abrahamic curse-and-blessing formula of 12:3. The Hebrew says peoples, nations, your brothers, your mother’s sons, plural; the Greek nations, rulers, your brother, your father’s sons; "
   "the Latin peoples, tribes, brothers, mother’s sons. The Greek’s singular brother points at Esau; the Hebrew’s plural is formulaic."),
  'shared': ["May peoples serve you and nations bow to you.", "Be lord over your brothers and let your mother’s sons bow to you.", "Cursed be those who curse you, blessed those who bless you."],
  'instructions': [ins(K, S, "Isaac gave Jacob lordship over his brothers and the Abrahamic blessing."), ins(W, R, "Isaac speaks the oracle of 25:23 without knowing it; the elder is made to serve the younger by the father who meant the opposite.")],
  'entries': ['jacob'],
  'lost': [loses("Hebrew ammim … le’ummim … le-achekha … bene immekha, “peoples … nations … your brothers … your mother’s sons,” becomes Greek ethnē … archontes … tou adelphou sou … hoi huioi tou patros sou, “nations … rulers … your brother … your father’s sons”; the plurals narrow to Esau and the mother becomes the father."), between("Latin “peoples … tribes … brothers … mother’s sons” and King James “people … nations … brethren … mother’s sons” follow the Hebrew.")]},

 '27:30': {
  'received': "As soon as Jacob left Isaac’s presence, Esau came in from the hunt.",
  'explain': ("The narrowest of escapes. The Greek calls Jacob his son; the Latin compresses to Isaac had scarcely finished speaking."),
  'shared': ["Isaac had finished blessing Jacob.", "Jacob had just gone out from his father.", "Esau his brother came in from his hunt."],
  'instructions': [ins(K, S, "Esau returned moments after Jacob left."), ins(W, R, "The timing is providence or luck, and the narrator declines to say which; the reader who knows the oracle will decide.")],
  'entries': ['jacob', 'isaac'],
  'lost': [keeps("An added ton huion autou, “his son,” after Jacob in the Greek."), between("Latin “Isaac had scarcely finished speaking, and Jacob had gone out, when Esau arrived” compresses; King James follows the Hebrew.")]},

 '27:31': {
  'received': "Esau brought his meal and asked his father to rise and eat his son’s game and bless him.",
  'explain': ("Esau’s words echo Jacob’s almost exactly; he has done what was asked. The versions agree."),
  'shared': ["He also prepared a savoury meal and brought it to his father.", "Let my father arise and eat of his son’s game.", "So that your soul may bless me."],
  'instructions': [ins(K, S, "Esau brought the real game for the blessing.")],
  'entries': [],
  'lost': [AGREE]},

 '27:32': {
  'received': "Isaac asked who he was; Esau said, Your firstborn son, Esau.",
  'explain': ("The same question, now answered truly. The versions agree."),
  'shared': ["Isaac his father said, Who are you?", "He answered.", "I am your firstborn son, Esau."],
  'instructions': [ins(K, S, "Esau identified himself truly.")],
  'entries': ['isaac'],
  'lost': [AGREE]},

 '27:33': {
  'received': "Isaac trembled violently and asked who had brought game; he had eaten and blessed him, and blessed he would be.",
  'explain': ("Isaac understands and does not revoke. The Hebrew says trembled a very great trembling; the Greek was utterly astonished; the Latin trembled in great astonishment, amazed beyond belief. The last clause is the point: the blessing stands."),
  'shared': ["Isaac trembled greatly.", "Who was it who hunted game and brought it, so that I ate and blessed him?", "He shall be blessed."],
  'instructions': [ins(K, S, "Isaac realised the deception but confirmed the blessing."), ins(W, R, "“Yea, and he shall be blessed”: Isaac does not undo what he did in error, and in that submission the oracle is received at last.")],
  'entries': ['isaac'],
  'lost': [between("Hebrew va-yecherad Yitzchaq charadah gedolah ad-me’od, “Isaac trembled a very great trembling,” is Greek exestē de Isaak ekstasin megalēn sphodra, “Isaac was astonished with a very great astonishment”; Hebrew gam-barukh yihyeh, “indeed he shall be blessed,” is Greek kai eulogēmenos estō, “and let him be blessed.” Latin and King James keep the trembling.")]},

 '27:34': {
  'received': "Esau cried out bitterly and begged, Bless me too, my father.",
  'explain': ("The great and exceeding bitter cry Hebrews 12:17 recalls. The Hebrew and Greek say even me also; the Latin said in dismay."),
  'shared': ["Esau heard his father’s words.", "He cried out with a great and bitter cry.", "Bless me, even me also, my father."],
  'instructions': [ins(K, S, "Esau pleaded for a blessing."), ins(W, R, "The man who sold his birthright for stew weeps for the blessing; Hebrews says he found no place of repentance, though he sought it with tears.")],
  'entries': [],
  'lost': [between("Latin “cried out with a great cry and said in dismay” varies; Hebrew, Greek and King James “a great and exceedingly bitter cry … even me also.”")]},

 '27:35': {
  'received': "Isaac said, Your brother came with deceit and took your blessing.",
  'explain': ("Isaac names it: mirmah, deceit, the word used of Laban’s trick on Jacob in 29:25. The versions agree."),
  'shared': ["Isaac spoke to him.", "Your brother came with guile.", "He took your blessing."],
  'instructions': [ins(K, S, "Isaac told Esau the truth about Jacob’s deceit."), ins(W, R, "Isaac calls it deceit and lets it stand; what God has used He does not thereby approve.")],
  'entries': ['isaac'],
  'lost': [AGREE]},

 '27:36': {
  'received': "Esau said Jacob was rightly named, having supplanted him twice, and asked if no blessing was reserved.",
  'explain': ("Esau plays on the name: Ya‘aqov, from aqav, to follow at the heel, to overreach. The Hebrew is a question, is he not rightly named; the Greek an assertion; the Latin a second time, stolen."),
  'shared': ["Is he not rightly named Jacob? He has supplanted me twice.", "He took my birthright and now my blessing.", "Have you not reserved a blessing for me?"],
  'instructions': [ins(K, S, "Esau accused Jacob of supplanting him twice."), ins(W, R, "Esau reads his brother’s name as a verdict; the heel-grasper has grasped twice, and Esau forgets that the first time he sold.")],
  'entries': ['jacob'],
  'lost': [between("Hebrew ha-khi qara shemo Ya‘aqov, “is it that his name is called Jacob?” a question, is Greek dikaiōs eklēthē to onoma autou Iakōb, “rightly was his name called Jacob,” an assertion; Latin “rightly is he named Jacob … stolen my blessing” expands; King James “Is not he rightly named Jacob?”")]},

 '27:37': {
  'received': "Isaac said he had made Jacob lord and given him his brothers as servants and grain and wine; what was left for Esau?",
  'explain': ("Isaac rehearses the blessing as given and spent. The Hebrew says behold, I have made him your lord; the Greek if I have made him, framing an argument; the Latin I have appointed."),
  'shared': ["I have made him your lord.", "I have given all his brothers to him as servants and sustained him with grain and wine.", "What then shall I do for you, my son?"],
  'instructions': [ins(K, S, "Isaac said the blessing was spent on Jacob."), ins(W, R, "A blessing once spoken is a thing done; Isaac has nothing of the first rank left to give, and knows it.")],
  'entries': ['isaac'],
  'lost': [between("Hebrew hen gevir samtiv lakh, “behold, lord I have made him to you,” is Greek ei kyrion auton epoiēsa sou, “if I have made him your lord”; Hebrew la-avadim, “as servants,” is Greek oiketas, “household slaves”; Latin and King James follow the Hebrew.")]},

 '27:38': {
  'received': "Esau asked whether he had only one blessing, begged to be blessed, and wept aloud.",
  'explain': ("Esau’s tears. The Greek adds Isaac was deeply moved, katanychthentos, pierced, before Esau wept; the Hebrew has only Esau’s weeping; the Latin carries Isaac’s being moved into the next verse."),
  'shared': ["Have you only one blessing, my father?", "Bless me too, my father.", "Esau lifted his voice and wept."],
  'instructions': [ins(K, S, "Esau wept for a blessing."), ins(W, R, "The hunter weeps; the Greek lets the father be pierced too. Either way, the tears come after the sale and cannot unsell it.")],
  'entries': ['isaac'],
  'lost': [keeps("An added katanychthentos de Isaak, “and Isaac being deeply moved,” in the Greek before Esau’s weeping; the Hebrew has only va-yissa Esav qolo va-yevk, “and Esau lifted his voice and wept.”"), between("Latin moves “Isaac was moved” to 27:39; King James follows the Hebrew.")]},

 '27:39': {
  'received': "Isaac answered: your dwelling shall be away from the fat of the earth and the dew of heaven.",
  'explain': ("Esau’s blessing, which reads as its opposite. The Hebrew preposition min can mean of or away from; read against verse 28 the Hebrew and Greek are usually taken as away from, Edom being dry country. "
   "The Latin and King James read it positively, in the richness of the earth, the fatness of the earth. The rendering remains under review."),
  'shared': ["Isaac his father answered him.", "Your dwelling is spoken of in relation to the richness of the earth.", "And the dew of heaven above."],
  'instructions': [ins(K, S, "Isaac gave Esau a blessing concerning the earth and the dew."), ins(W, R, "The same words that were Jacob’s gift are Esau’s with a preposition changed; blessing and its absence can be a matter of one small word.")],
  'entries': ['isaac'],
  'lost': [between("Hebrew mi-shmanne ha-aretz … u-mi-tal ha-shamayim, “from the fat of the earth and from the dew of heaven,” Greek apo tēs piotētos … apo tēs drosou, ambiguous between “of” and “away from”; Latin “in the richness of the earth and in the dew of heaven” and King James “thy dwelling shall be the fatness of the earth” take the positive sense.")]},

 '27:40': {
  'received': "You shall live by your sword and serve your brother, but when you break loose you shall throw off his yoke.",
  'explain': ("Edom’s history in a sentence: a sword, servitude, revolt. The Hebrew verb for break loose, tarid, is uncertain, grow restless or have dominion; the Greek a time will come when you pull down; the Latin shake off. The Latin opens with shall your blessing be, completing verse 39."),
  'shared': ["By your sword you shall live.", "You shall serve your brother.", "But a time will come when you break his yoke from your neck."],
  'instructions': [ins(K, S, "Esau was promised a life by the sword, service, and eventual freedom."), ins(W, R, "Even the lesser blessing ends in release; Edom will serve and then shake free, as 2 Kings 8:20 records.")],
  'entries': [],
  'lost': [between("Hebrew ka-asher tarid, “when you grow restless” or “have dominion,” a difficult form, is Greek estai de hēnika ean kathelēs, “but it shall be when you pull down”; Latin “the time shall come when you shake off”; King James “when thou shalt have the dominion.”")]},

 '27:41': {
  'received': "Esau hated Jacob for the blessing and resolved to kill him once their father was mourned.",
  'explain': ("Murder deferred for filial piety. The Hebrew says Esau hated, in his heart, the days of mourning are near; the Greek was angry, in his mind, let the days draw near, a wish; the Latin continually hated."),
  'shared': ["Esau hated Jacob because of the blessing.", "He said in his heart, the days of mourning for my father are near.", "Then I will kill my brother Jacob."],
  'instructions': [ins(K, S, "Esau planned to kill Jacob after Isaac’s death."), ins(W, R, "Esau will wait for his father to die before killing his brother; the piety and the murder sit together in one heart.")],
  'entries': ['jacob'],
  'lost': [loses("Hebrew va-yistom, “hated,” becomes Greek enekotei, “was angry with”; Hebrew yiqrevu yeme evel avi, “the days of mourning for my father are near,” a statement, becomes engisatōsan hai hēmerai, “let the days draw near,” a wish."), between("Latin “continually hated … the days will come” and King James “hated … are at hand” follow the Hebrew.")]},

 '27:42': {
  'received': "Rebekah heard of it and told Jacob that Esau was consoling himself with plans to kill him.",
  'explain': ("Rebekah hears everything. The Hebrew idiom is Esau consoles himself concerning you by planning to kill you; the Greek is threatening to kill you; the Latin threatens. The Greek names the older and younger sons."),
  'shared': ["Rebekah was told what Esau her older son had said.", "She sent for Jacob her younger son.", "Your brother Esau plans to kill you."],
  'instructions': [ins(K, S, "Rebekah warned Jacob of Esau’s plan."), ins(W, R, "Esau comforts himself with a murder he has not committed; the Hebrew lets us see revenge as a kind of consolation.")],
  'entries': ['rebekah', 'jacob'],
  'lost': [loses("Hebrew mitnachem lekha le-horgekha, “consoles himself concerning you to kill you,” becomes Greek apeilei soi tou apokteinai se, “threatens you, to kill you”; the consolation is lost."), between("Latin “threatens to kill you” follows the Greek’s sense; King James “doth comfort himself, purposing to kill thee” keeps the idiom.")]},

 '27:43': {
  'received': "So obey me, my son: flee to my brother Laban in Haran.",
  'explain': ("Obey my voice again, this time to save his life. The Greek adds into Mesopotamia; the others say Laban in Haran."),
  'shared': ["Now, my son, obey my voice.", "Arise and flee.", "Go to Laban my brother in Haran."],
  'instructions': [ins(C, S, "Arise and flee to Laban my brother in Haran."), ins(W, R, "The mother who schemed for the blessing now sends the blessed son into exile; the fruit of the plan is twenty years’ separation.")],
  'entries': ['haran'],
  'lost': [keeps("An added eis tēn Mesopotamian, “into Mesopotamia,” in the Greek before Laban."), between("Latin and King James “to Laban my brother in Haran.”")]},

 '27:44': {
  'received': "Stay with him a while, until your brother’s fury turns away,",
  'explain': ("A few days, she says; it will be twenty years. The Greek breaks the sentence after until the fury and carries the rest into verse 45; the Hebrew completes it here."),
  'shared': ["Stay with him a few days.", "Wait until your brother’s fury subsides.", "The sentence continues."],
  'instructions': [ins(K, S, "Rebekah expected a short exile.")],
  'entries': [],
  'lost': [between("Hebrew ad asher-tashuv chamat achikha, “until your brother’s fury turns away,” is complete here; the Greek stops at heōs tou apostrepsai ton thymon, “until the fury,” and continues in 27:45; Latin and King James follow the Hebrew.")]},

 '27:45': {
  'received': "until his anger turns and he forgets what you did; then I will send for you. Why should I lose you both in one day?",
  'explain': ("Rebekah fears a double loss, Jacob killed and Esau executed or exiled. The Hebrew repeats until and asks why should I be bereaved; the Greek joins the clause from verse 44 and makes the end a precaution, lest."),
  'shared': ["Until your brother’s anger turns from you and he forgets what you did.", "Then I will send and bring you back.", "Why should I be bereaved of both of you in one day?"],
  'instructions': [ins(K, S, "Rebekah promised to recall Jacob when it was safe."), ins(W, R, "She will not send; Rebekah dies before Jacob returns, and the recall she promises is never recorded.")],
  'entries': ['rebekah'],
  'lost': [between("Hebrew lammah eshkal gam-shenekhem, “why should I be bereaved of both of you,” a question, is Greek mēpote ateknōthō apo tōn dyo hymōn, “lest I be bereaved of both of you,” a purpose; the Greek’s “and anger of your brother” completes 27:44; Latin and King James follow the Hebrew.")]},

 '27:46': {
  'received': "Rebekah told Isaac she was weary of life because of the Hittite women; if Jacob married one, why live?",
  'explain': ("Rebekah gives Isaac a different reason for Jacob’s departure, a true one: Esau’s wives. The Hebrew repeats daughters of Heth and says what is life to me; the Greek daughters of the Hittites, why should I live; the Latin I do not wish to live."),
  'shared': ["Rebekah spoke to Isaac.", "I am weary of my life because of the daughters of Heth.", "If Jacob takes such a wife, what is life to me?"],
  'instructions': [ins(K, S, "Rebekah used Esau’s marriages as the reason to send Jacob away."), ins(W, R, "Rebekah manages Isaac to the end, telling him the true reason that is not the real one; the chapter closes as it opened, with the father kept in the dark.")],
  'entries': ['rebekah', 'isaac', 'jacob'],
  'lost': [between("Hebrew mi-benot Chet ka-elleh mi-benot ha-aretz, “from the daughters of Heth like these, from the daughters of the land,” is compressed in Greek to apo tōn thygaterōn tēs gēs tautēs, “from the daughters of this land”; Hebrew lammah li chayyim, “why to me life?” is Greek hina ti moi zēn; Latin “I do not wish to live”; King James “what good shall my life do me?”")]},
 }
}
